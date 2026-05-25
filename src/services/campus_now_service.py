from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from src.config import (
    get_campus_now_cache_seconds,
    get_campus_now_campus_id,
    get_campus_now_pc_count,
)
from src.services.ft_api import (
    FtAppToken,
    FtLocation,
    fetch_active_campus_locations,
    fetch_app_access_token,
)
from src.services.seat_map import parse_host, parse_svg_layout


@dataclass(frozen=True)
class CampusNow:
    active_count: int
    pc_count: int
    crowd_percent: float
    comment: str
    fetched_at: datetime


@dataclass(frozen=True)
class ClusterNow:
    cluster_id: str
    cluster_name: str
    active_count: int
    seat_count: int
    crowd_percent: float
    comment: str
    fetched_at: datetime


@dataclass(frozen=True)
class CampusAll:
    campus: CampusNow
    clusters: tuple[ClusterNow, ...]


CLUSTERS: dict[str, tuple[str, str]] = {
    "koi": ("c1", "koi"),
    "ume": ("c2", "ume"),
    "washi": ("c3", "washi"),
    "fuji": ("c4", "fuji"),
    "sakura": ("c5", "sakura"),
    "tsuru": ("c6", "tsuru"),
}

_CLUSTER_ALIASES = {
    **{cluster_name: cluster_name for cluster_name in CLUSTERS},
    **{
        cluster_id: cluster_name
        for cluster_name, (cluster_id, _) in CLUSTERS.items()
    },
}

_cached_app_token: FtAppToken | None = None
_cached_campus_now: CampusNow | None = None
_cached_locations: tuple[datetime, list[FtLocation]] | None = None


def describe_crowd(crowd_percent: float) -> str:
    if crowd_percent < 40:
        return "\u7a7a\u3044\u3066\u3044\u307e\u3059"
    if crowd_percent < 70:
        return "\u305d\u3053\u305d\u3053\u6df7\u3093\u3067\u3044\u307e\u3059"
    if crowd_percent < 90:
        return "\u6df7\u96d1\u3057\u3066\u3044\u307e\u3059"
    return "\u304b\u306a\u308a\u6df7\u96d1\u3057\u3066\u3044\u307e\u3059"


def build_campus_now(
    *,
    active_count: int,
    pc_count: int,
    fetched_at: datetime | None = None,
) -> CampusNow:
    if fetched_at is None:
        fetched_at = datetime.now(UTC)

    crowd_percent = active_count / pc_count * 100
    return CampusNow(
        active_count=active_count,
        pc_count=pc_count,
        crowd_percent=crowd_percent,
        comment=describe_crowd(crowd_percent),
        fetched_at=fetched_at,
    )


def resolve_cluster_name(cluster: str) -> str:
    normalized = cluster.strip().lower()
    try:
        return _CLUSTER_ALIASES[normalized]
    except KeyError as error:
        message = f"Unknown cluster: {cluster}"
        raise ValueError(message) from error


def build_cluster_now(
    *,
    cluster_name: str,
    active_count: int,
    seat_count: int,
    fetched_at: datetime | None = None,
) -> ClusterNow:
    if fetched_at is None:
        fetched_at = datetime.now(UTC)

    cluster_id, display_name = CLUSTERS[resolve_cluster_name(cluster_name)]
    crowd_percent = active_count / seat_count * 100
    return ClusterNow(
        cluster_id=cluster_id,
        cluster_name=display_name,
        active_count=active_count,
        seat_count=seat_count,
        crowd_percent=crowd_percent,
        comment=describe_crowd(crowd_percent),
        fetched_at=fetched_at,
    )


def _count_locations_by_cluster(
    locations: list[FtLocation],
) -> dict[str, int]:
    counts = {cluster_id: 0 for cluster_id, _name in CLUSTERS.values()}
    for location in locations:
        if location.host is None:
            continue
        try:
            location_cluster_id, _row, _seat = parse_host(location.host)
        except ValueError:
            continue
        if location_cluster_id in counts:
            counts[location_cluster_id] += 1
    return counts


def clear_campus_now_cache() -> None:
    global _cached_app_token, _cached_campus_now, _cached_locations
    _cached_app_token = None
    _cached_campus_now = None
    _cached_locations = None


async def _get_app_access_token(now: datetime) -> str:
    global _cached_app_token
    if (
        _cached_app_token is not None
        and _cached_app_token.expires_at > now + timedelta(seconds=60)
    ):
        return _cached_app_token.access_token

    _cached_app_token = await fetch_app_access_token()
    return _cached_app_token.access_token


async def _get_active_campus_locations() -> tuple[datetime, list[FtLocation]]:
    global _cached_locations
    now = datetime.now(UTC)
    cache_ttl = timedelta(seconds=get_campus_now_cache_seconds())
    if (
        _cached_locations is not None
        and now - _cached_locations[0] < cache_ttl
    ):
        return _cached_locations

    campus_id = get_campus_now_campus_id()
    access_token = await _get_app_access_token(now)
    locations = await fetch_active_campus_locations(
        access_token,
        campus_id,
    )
    _cached_locations = (now, locations)
    return _cached_locations


async def get_campus_now() -> CampusNow:
    global _cached_campus_now

    fetched_at, locations = await _get_active_campus_locations()
    if (
        _cached_campus_now is not None
        and _cached_campus_now.fetched_at == fetched_at
    ):
        return _cached_campus_now

    pc_count = get_campus_now_pc_count()
    active_count = len(locations)
    _cached_campus_now = build_campus_now(
        active_count=active_count,
        pc_count=pc_count,
        fetched_at=fetched_at,
    )
    return _cached_campus_now


async def get_cluster_now(cluster: str) -> ClusterNow:
    cluster_name = resolve_cluster_name(cluster)
    cluster_id, _display_name = CLUSTERS[cluster_name]
    fetched_at, locations = await _get_active_campus_locations()
    counts = _count_locations_by_cluster(locations)

    return build_cluster_now(
        cluster_name=cluster_name,
        active_count=counts[cluster_id],
        seat_count=len(parse_svg_layout(cluster_id)),
        fetched_at=fetched_at,
    )


async def get_campus_all() -> CampusAll:
    fetched_at, locations = await _get_active_campus_locations()
    counts = _count_locations_by_cluster(locations)

    campus = build_campus_now(
        active_count=len(locations),
        pc_count=get_campus_now_pc_count(),
        fetched_at=fetched_at,
    )

    clusters = tuple(
        build_cluster_now(
            cluster_name=cluster_name,
            active_count=counts[cluster_id],
            seat_count=len(parse_svg_layout(cluster_id)),
            fetched_at=fetched_at,
        )
        for cluster_name, (cluster_id, _display_name) in CLUSTERS.items()
    )
    return CampusAll(campus=campus, clusters=clusters)
