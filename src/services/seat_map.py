"""Seat map renderer for 42Tokyo clusters — parses actual SVG layout files."""

import io
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import lxml.etree as ET

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# SVG file paths
# ---------------------------------------------------------------------------

_BASE_DIR = Path(__file__).parent.parent.parent
_CLUSTER_LAYOUT_DIR = _BASE_DIR / "data" / "clusters"
_SVG_FILES = {
    "c1": _CLUSTER_LAYOUT_DIR / "c1-koi",
    "c2": _CLUSTER_LAYOUT_DIR / "c2-ume",
    "c3": _CLUSTER_LAYOUT_DIR / "c3-washi",
    "c4": _CLUSTER_LAYOUT_DIR / "c4-fuji",
    "c5": _CLUSTER_LAYOUT_DIR / "c5-sakura",
    "c6": _CLUSTER_LAYOUT_DIR / "c6-tsuru",
}

_SVG_NS = "http://www.w3.org/2000/svg"

# ---------------------------------------------------------------------------
# Cluster metadata
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ClusterMeta:
    name: str
    floor: int
    from_stairs: Literal["right", "left"]
    entrance_row: int  # row/col index nearest to entrance (1-based)
    entrance_seat_first: bool  # True → s1 side is near the entrance


@dataclass(frozen=True)
class EntranceMarker:
    x: int
    y: int
    label: str


CLUSTER_META: dict[str, ClusterMeta] = {
    "c1": ClusterMeta(
        "鯉 (c1)", 2, "right", entrance_row=4, entrance_seat_first=True
    ),
    "c2": ClusterMeta(
        "梅 (c2)", 2, "left", entrance_row=5, entrance_seat_first=False
    ),
    "c3": ClusterMeta(
        "鷲 (c3)", 3, "right", entrance_row=4, entrance_seat_first=True
    ),
    "c4": ClusterMeta(
        "富士 (c4)", 3, "left", entrance_row=3, entrance_seat_first=False
    ),
    "c5": ClusterMeta(
        "桜 (c5)", 4, "right", entrance_row=1, entrance_seat_first=False
    ),
    "c6": ClusterMeta(
        "鶴 (c6)", 4, "left", entrance_row=4, entrance_seat_first=False
    ),
}

# Entrance label positions are image canvas coordinates.
# Tweak these by hand when the automatic layout does not match the real floor.
ENTRANCE_MARKERS: dict[str, EntranceMarker] = {
    "c1": EntranceMarker(x=364, y=28, label="入口↓"),
    "c2": EntranceMarker(x=360, y=270, label="入口↑"),
    "c3": EntranceMarker(x=394, y=28, label="入口↓"),
    "c4": EntranceMarker(x=444, y=288, label="入口↑"),
    "c5": EntranceMarker(x=374, y=38, label="入口↓"),
    "c6": EntranceMarker(x=374, y=278, label="入口↑"),
}

# Row-based: seats arranged horizontally per row group.
# Col-based: each "row" group is actually a vertical column.
_ROW_BASED = {"c1", "c2", "c3"}

# In row-based clusters: s1 is at x=280, seat step = 16px.
# Used to infer correct seat number from x when the rect ID is mislabeled.
_S1_X = 280.0
_SEAT_STEP = 16.0

# ---------------------------------------------------------------------------
# SVG parser
# ---------------------------------------------------------------------------

_RECT_ID_RE = re.compile(r"^c(\d+)r(\d+)s(\d+)$")
_GROUP_ID_RE = re.compile(r"^row(\d+)$")


def parse_svg_layout(
    cluster_id: str,
) -> dict[tuple[int, int], tuple[float, float]]:
    """Parse SVG → {(row, seat): (svg_x, svg_y)}.

    Uses <g id="rowXX"> for the authoritative row number.
    Infers seat number from x-position when a rect is mislabeled
    (e.g., c1r7s4 at x=184 in group row06 → actual c1r6s7).
    """
    svg_path = _SVG_FILES[cluster_id]
    svg_text = svg_path.read_text(encoding="utf-8")
    svg_text = re.sub(r'(?<!=)""(?=\s|/?>)', '"', svg_text)

    # lxml recovery mode handles malformed SVG attributes after sanitising
    # known stray quotes that would otherwise drop following sibling nodes.
    parser = ET.XMLParser(recover=True)
    root = ET.fromstring(svg_text.encode("utf-8"), parser=parser)

    cluster_num = int(cluster_id[1:])
    row_based = cluster_id in _ROW_BASED

    seats: dict[tuple[int, int], tuple[float, float]] = {}

    for group in root.iter(f"{{{_SVG_NS}}}g"):
        gid = group.get("id", "")
        gm = _GROUP_ID_RE.match(gid)
        if not gm:
            continue
        group_row = int(gm.group(1))

        for rect in group.findall(f"{{{_SVG_NS}}}rect"):
            rid = rect.get("id", "")
            rm = _RECT_ID_RE.match(rid)
            if not rm or int(rm.group(1)) != cluster_num:
                continue

            rect_row = int(rm.group(2))
            seat_from_id = int(rm.group(3))
            x = float(rect.get("x", 0))
            y = float(rect.get("y", 0))

            # Mislabeled rect (rect row ≠ group row): infer seat from x.
            if row_based and rect_row != group_row:
                seat_num = round((_S1_X - x) / _SEAT_STEP) + 1
            else:
                seat_num = seat_from_id

            key = (group_row, seat_num)
            if key not in seats:
                seats[key] = (x, y)

    return seats


# ---------------------------------------------------------------------------
# Position normalisation — collapse stagger to mean ± small offset
# ---------------------------------------------------------------------------

# SVG units to shift each sub-group from the row mean
_STAGGER_OFFSET = 5.0


def _normalize_positions(
    cluster_id: str,
    layout: dict[tuple[int, int], tuple[float, float]],
) -> dict[tuple[int, int], tuple[float, float]]:
    """Move each seat to y_mean ± _STAGGER_OFFSET instead of exact y_mean.

    This keeps the two facing sides of each physical desk slightly apart
    so you can tell which side the target seat is on, while still grouping
    them visually within the same row strip.
    """
    row_positions: dict[int, list[tuple[float, float]]] = {}
    for (row, _seat), pos in layout.items():
        row_positions.setdefault(row, []).append(pos)

    result: dict[tuple[int, int], tuple[float, float]] = {}

    if cluster_id in _ROW_BASED:
        for (row, seat), (x, y) in layout.items():
            positions = row_positions[row]
            xs = [p[0] for p in positions]
            if len(set(xs)) <= 1:
                result[(row, seat)] = (x, y)
            else:
                ys = [p[1] for p in positions]
                y_mean = sum(ys) / len(ys)
                offset = -_STAGGER_OFFSET if y <= y_mean else _STAGGER_OFFSET
                result[(row, seat)] = (x, y_mean + offset)
    else:
        for (row, seat), (x, y) in layout.items():
            positions = row_positions[row]
            xs = [p[0] for p in positions]
            x_mean = sum(xs) / len(xs)
            offset = -_STAGGER_OFFSET if x <= x_mean else _STAGGER_OFFSET
            result[(row, seat)] = (x_mean + offset, y)

    return result


# ---------------------------------------------------------------------------
# Layout cache
# ---------------------------------------------------------------------------

_layout_cache: dict[str, dict[tuple[int, int], tuple[float, float]]] = {}


def _get_layout(
    cluster_id: str,
) -> dict[tuple[int, int], tuple[float, float]]:
    if cluster_id not in _layout_cache:
        raw = parse_svg_layout(cluster_id)
        _layout_cache[cluster_id] = _normalize_positions(cluster_id, raw)
    return _layout_cache[cluster_id]


# ---------------------------------------------------------------------------
# Host string parser
# ---------------------------------------------------------------------------

_HOST_RE = re.compile(r"^(c\d+)r(\d+)s(\d+)$")


def parse_host(host: str) -> tuple[str, int, int]:
    """Parse 'c1r3s5' → ('c1', 3, 5). Raises ValueError on bad format."""
    m = _HOST_RE.match(host.lower())
    if not m:
        raise ValueError(f"Invalid host format: {host!r}")
    return m.group(1), int(m.group(2)), int(m.group(3))


# ---------------------------------------------------------------------------
# Description text generator
# ---------------------------------------------------------------------------


def build_description(cluster_id: str, row: int, seat: int, login: str) -> str:
    meta = CLUSTER_META[cluster_id]
    stairs = "右手" if meta.from_stairs == "right" else "左手"

    entrance_r = meta.entrance_row
    row_dist = abs(row - entrance_r)

    # Row position relative to entrance
    if row == entrance_r:
        row_hint = "入口のすぐ目の前の列"
    elif row_dist == 1:
        row_hint = "入口から1列奥"
    else:
        row_hint = f"入口から {row_dist} 列奥"

    # Seat position within the row
    layout = _get_layout(cluster_id)
    # Count total seats in this row
    seats_in_row = [s for (r, s) in layout if r == row]
    total = max(seats_in_row) if seats_in_row else seat

    if meta.entrance_seat_first:
        # s1 is closest to entrance side
        if seat == 1:
            seat_hint = "入口側の端の席"
        elif seat == total:
            seat_hint = "奥の端の席"
        else:
            seat_hint = f"入口側から {seat} 番目の席"
    else:
        # high seat# is closest to entrance side
        from_entrance = total - seat + 1
        if from_entrance == 1:
            seat_hint = "入口側の端の席"
        elif seat == 1:
            seat_hint = "奥の端の席"
        else:
            seat_hint = f"入口側から {from_entrance} 番目の席"

    lines = [
        f"**`{login}`** さんの現在地",
        "",
        f"📍 **{meta.name}** クラスタ　{meta.floor}F",
        f"　　階段を上がって **{stairs}** へ進んでください。",
        "",
        f"　　{row_hint}、**{seat_hint}** です。",
        f"　　（R{row} / s{seat}）",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Renderer — 90° CW rotation so all clusters render landscape
#
# Transform: svg_y → canvas_x (row/col axis goes horizontal)
#            (x_max - svg_x) → canvas_y (seat axis goes vertical, s1 at top)
#
# SVG rect is 16(x) × 20(y).  After rotation the canvas rect becomes:
#   rw = 20 * scale  (from svg height/y → now horizontal)
#   rh = 16 * scale  (from svg width/x  → now vertical)
# ---------------------------------------------------------------------------

# Canvas — wide landscape format
_CANVAS_W = 720
_CANVAS_H = 320
_PAD_X = 36
_PAD_Y = 32

# Colors (Catppuccin-inspired dark palette)
_BG = (30, 30, 46)
_DESK_FILL = (69, 71, 90)
_DESK_OUTLINE = (108, 112, 134)
_SEAT_BAR = (166, 227, 161)
_TARGET_FILL = (243, 139, 168)
_TEXT = (205, 214, 244)
_LABEL = (147, 153, 178)
_ENTRANCE = (250, 179, 135)
_DOT = (243, 139, 168)


def _font(size: int = 11) -> ImageFont.ImageFont:
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()


def _compute_scale(
    positions: dict[tuple[int, int], tuple[float, float]],
) -> tuple[float, float, float, float, float, float, float, float]:
    """Return transform values for the rotated mapping."""
    xs = [p[0] for p in positions.values()]
    ys = [p[1] for p in positions.values()]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)

    # After rotation: y-span → canvas width, x-span → canvas height
    data_w = (y_max - y_min) + 20  # svg_height of rect = 20
    data_h = (x_max - x_min) + 16  # svg_width  of rect = 16

    avail_w = _CANVAS_W - 2 * _PAD_X
    avail_h = _CANVAS_H - 2 * _PAD_Y

    scale = min(avail_w / data_w, avail_h / data_h)
    rw = 20 * scale  # canvas rect width  (was svg height)
    rh = 16 * scale  # canvas rect height (was svg width)
    origin_x = (_CANVAS_W - data_w * scale) / 2
    origin_y = (_CANVAS_H - data_h * scale) / 2
    return scale, x_min, x_max, y_min, rw, rh, origin_x, origin_y


def _to_canvas(
    svg_x: float,
    svg_y: float,
    scale: float,
    x_min: float,
    x_max: float,
    y_min: float,
    origin_x: float,
    origin_y: float,
) -> tuple[float, float]:
    cx = origin_x + (svg_y - y_min) * scale
    cy = origin_y + (x_max - svg_x) * scale
    return cx, cy


def _seat_font_size(rect_h: float) -> int:
    return max(10, min(13, int(rect_h * 0.58)))


def _draw_centered_text(
    draw: ImageDraw.ImageDraw,
    box: tuple[float, float, float, float],
    text: str,
    fill: tuple[int, int, int],
    font: ImageFont.ImageFont,
) -> None:
    left, top, right, bottom = box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = left + (right - left - text_w) / 2
    y = top + (bottom - top - text_h) / 2 - 1
    draw.text((x, y), text, fill=fill, font=font)


def _make_frame(
    cluster_id: str,
    target_row: int,
    target_seat: int,
    show_dot: bool,
) -> Image.Image:
    layout = _get_layout(cluster_id)
    meta = CLUSTER_META[cluster_id]
    scale, x_min, x_max, y_min, rw, rh, ox, oy = _compute_scale(layout)

    img = Image.new("RGB", (_CANVAS_W, _CANVAS_H), _BG)
    draw = ImageDraw.Draw(img)

    fn_sm = _font(_seat_font_size(rh))
    fn_md = _font(11)
    fn_lg = _font(13)

    draw.text((8, 8), meta.name, fill=_TEXT, font=fn_lg)

    for (row, seat), (svg_x, svg_y) in layout.items():
        cx, cy = _to_canvas(svg_x, svg_y, scale, x_min, x_max, y_min, ox, oy)
        is_target = row == target_row and seat == target_seat

        fill = _TARGET_FILL if is_target else _DESK_FILL
        draw.rectangle(
            [cx, cy, cx + rw - 1, cy + rh - 1],
            fill=fill,
            outline=_DESK_OUTLINE,
        )

        # Indicator bar on left edge shows which side of desk faces entrance
        bar_color = _TARGET_FILL if is_target else _SEAT_BAR
        draw.rectangle([cx, cy + 1, cx + 2, cy + rh - 2], fill=bar_color)

        _draw_centered_text(
            draw,
            (cx + 3, cy, cx + rw - 1, cy + rh - 1),
            str(seat),
            _TEXT,
            fn_sm,
        )

    _draw_labels(
        draw,
        layout,
        cluster_id,
        scale,
        x_min,
        x_max,
        y_min,
        rw,
        rh,
        ox,
        oy,
        fn_md,
    )
    _draw_entrance(
        draw,
        layout,
        cluster_id,
        meta,
        scale,
        x_min,
        x_max,
        y_min,
        rw,
        rh,
        ox,
        oy,
        fn_md,
    )

    if show_dot and (target_row, target_seat) in layout:
        sx, sy = layout[(target_row, target_seat)]
        cx, cy = _to_canvas(sx, sy, scale, x_min, x_max, y_min, ox, oy)
        dot_cx = int(cx + rw / 2)
        dot_cy = int(cy + rh / 2)
        r = max(4, int(min(rw, rh) * 0.30))
        draw.ellipse(
            [dot_cx - r, dot_cy - r, dot_cx + r, dot_cy + r],
            fill=_DOT,
            outline=(255, 255, 255),
        )

    return img


def _draw_labels(
    draw: ImageDraw.ImageDraw,
    layout: dict[tuple[int, int], tuple[float, float]],
    cluster_id: str,
    scale: float,
    x_min: float,
    x_max: float,
    y_min: float,
    rw: float,
    rh: float,
    origin_x: float,
    origin_y: float,
    font: ImageFont.ImageFont,
) -> None:
    """Draw R-number labels above each row strip (after rotation)."""
    rows: dict[int, list[tuple[float, float]]] = {}
    for (row, _seat), pos in layout.items():
        rows.setdefault(row, []).append(pos)

    for row, positions in rows.items():
        svg_ys = [p[1] for p in positions]
        svg_xs = [p[0] for p in positions]
        mid_svg_y = (min(svg_ys) + max(svg_ys)) / 2
        top_svg_x = max(svg_xs)

        cx, cy = _to_canvas(
            top_svg_x,
            mid_svg_y,
            scale,
            x_min,
            x_max,
            y_min,
            origin_x,
            origin_y,
        )
        draw.text(
            (cx + rw / 2 - 8, cy - 14),
            f"R{row}",
            fill=_LABEL,
            font=font,
        )


def _draw_entrance(
    draw: ImageDraw.ImageDraw,
    layout: dict[tuple[int, int], tuple[float, float]],
    cluster_id: str,
    meta: ClusterMeta,
    scale: float,
    x_min: float,
    x_max: float,
    y_min: float,
    rw: float,
    rh: float,
    origin_x: float,
    origin_y: float,
    font: ImageFont.ImageFont,
) -> None:
    """Draw an entrance label at a manually configured canvas coordinate."""
    marker = ENTRANCE_MARKERS.get(cluster_id)
    if marker is None:
        return

    draw.text((marker.x, marker.y), marker.label, fill=_ENTRANCE, font=font)


def render_seat_map_gif(cluster_id: str, row: int, seat: int) -> bytes:
    """Return animated GIF bytes with a blinking dot at the target seat."""
    frame_on = _make_frame(cluster_id, row, seat, show_dot=True)
    frame_off = _make_frame(cluster_id, row, seat, show_dot=False)

    buf = io.BytesIO()
    frame_on.save(
        buf,
        format="GIF",
        save_all=True,
        append_images=[frame_off],
        loop=0,
        duration=600,
        optimize=False,
    )
    buf.seek(0)
    return buf.read()
