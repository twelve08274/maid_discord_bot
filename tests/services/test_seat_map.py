import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from src.services import seat_map  # noqa: E402


class SeatMapRenderTests(unittest.TestCase):
    def _skip_without_cluster_layout_files(self) -> None:
        missing = [
            str(path)
            for path in seat_map._SVG_FILES.values()
            if not path.exists()
        ]
        if missing:
            self.skipTest(
                "cluster layout files are missing: " + ", ".join(missing)
            )

    def test_cluster_layout_files_are_loaded_from_data_directory(self) -> None:
        expected_dir = (
            Path(__file__).resolve().parents[2] / "data" / "clusters"
        )

        for cluster_id, path in seat_map._SVG_FILES.items():
            with self.subTest(cluster_id=cluster_id):
                self.assertEqual(path.parent, expected_dir)

    def _desk_margins(
        self,
        cluster_id: str,
    ) -> tuple[float, float, float, float]:
        layout = seat_map._get_layout(cluster_id)
        tuning = seat_map.RENDER_TUNING.get(
            cluster_id,
            seat_map.RenderTuning(),
        )
        transform = seat_map._compute_scale(layout, tuning)
        scale, x_min, x_max, y_min, rw, rh, ox, oy = transform
        xs: list[float] = []
        ys: list[float] = []

        for svg_x, svg_y in layout.values():
            cx, cy = seat_map._to_canvas(
                svg_x,
                svg_y,
                scale,
                x_min,
                x_max,
                y_min,
                ox,
                oy,
            )
            xs.extend([cx, cx + rw])
            ys.extend([cy, cy + rh])

        return (
            min(xs),
            min(ys),
            tuning.canvas_w - max(xs),
            tuning.canvas_h - max(ys),
        )

    def test_c1_layout_includes_all_rows(self) -> None:
        self._skip_without_cluster_layout_files()
        layout = seat_map._get_layout("c1")

        self.assertIn((1, 1), layout)
        for row in range(1, 8):
            with self.subTest(row=row):
                self.assertEqual(
                    sorted(seat for layout_row, seat in layout
                           if layout_row == row),
                    [1, 2, 3, 4, 5, 6, 7, 8],
                )

    def test_c1_r1_target_seat_is_visible(self) -> None:
        self._skip_without_cluster_layout_files()
        frame = seat_map._make_frame("c1", 1, 1, show_dot=True)
        pixels = getattr(frame, "get_flattened_data", frame.getdata)()
        target_pixels = [
            pixel for pixel in pixels if pixel == seat_map._TARGET_FILL
        ]

        self.assertGreater(len(target_pixels), 0)

    def test_desk_area_is_centered_in_canvas(self) -> None:
        self._skip_without_cluster_layout_files()
        for cluster_id in seat_map.CLUSTER_META:
            with self.subTest(cluster_id=cluster_id):
                left, top, right, bottom = self._desk_margins(cluster_id)

                self.assertLess(abs(left - right), 1.0)
                self.assertLess(abs(top - bottom), 1.0)

    def test_seat_number_font_uses_cell_height(self) -> None:
        self._skip_without_cluster_layout_files()
        layout = seat_map._get_layout("c1")
        tuning = seat_map.RENDER_TUNING.get("c1", seat_map.RenderTuning())
        *_, rh, _, _ = seat_map._compute_scale(layout, tuning)

        self.assertGreaterEqual(seat_map._seat_font_size(rh), 12)

    def test_entrance_marker_is_defined_by_canvas_coordinates(self) -> None:
        marker = seat_map.ENTRANCE_MARKERS["c1"]
        self.assertEqual(marker.label, "入口↓")
        self.assertIsInstance(marker.x, int)
        self.assertIsInstance(marker.y, int)

    def test_render_tuning_can_override_canvas_size(self) -> None:
        tuning = seat_map.RENDER_TUNING["c5"]

        self.assertLess(tuning.canvas_w, seat_map._CANVAS_W)
        self.assertGreater(tuning.canvas_h, seat_map._CANVAS_H)

    def test_frame_uses_cluster_canvas_size(self) -> None:
        self._skip_without_cluster_layout_files()
        tuning = seat_map.RENDER_TUNING["c5"]
        frame = seat_map._make_frame("c5", 1, 1, show_dot=True)

        self.assertEqual(frame.size, (tuning.canvas_w, tuning.canvas_h))


if __name__ == "__main__":
    unittest.main()
