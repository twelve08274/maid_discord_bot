import unittest
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, patch

from src.services.campus_now_service import (
    build_campus_now,
    build_cluster_now,
    clear_campus_now_cache,
    get_campus_all,
    get_campus_now,
    get_cluster_now,
    resolve_cluster_name,
)
from src.services.ft_api import FtAppToken, FtLocation


class CampusNowServiceTests(unittest.IsolatedAsyncioTestCase):
    def tearDown(self) -> None:
        clear_campus_now_cache()

    def test_build_campus_now_calculates_crowd_percent(self) -> None:
        campus_now = build_campus_now(active_count=128, pc_count=300)

        self.assertEqual(campus_now.active_count, 128)
        self.assertEqual(campus_now.pc_count, 300)
        self.assertAlmostEqual(campus_now.crowd_percent, 42.6666, places=3)
        self.assertEqual(
            campus_now.comment,
            "\u305d\u3053\u305d\u3053\u6df7\u3093\u3067\u3044\u307e\u3059",
        )

    async def test_get_campus_now_uses_short_cache(self) -> None:
        token = FtAppToken(
            access_token="app-token",
            expires_at=datetime.now(UTC) + timedelta(hours=1),
        )

        with (
            patch(
                "src.services.campus_now_service.fetch_app_access_token",
                new=AsyncMock(return_value=token),
            ) as token_mock,
            patch(
                "src.services.campus_now_service."
                "fetch_active_campus_locations",
                new=AsyncMock(
                    return_value=[
                        FtLocation(
                            id=index,
                            begin_at=datetime.now(UTC),
                            end_at=None,
                            host=f"c1r1s{index}",
                        )
                        for index in range(1, 43)
                    ]
                ),
            ) as locations_mock,
            patch(
                "src.services.campus_now_service.get_campus_now_campus_id",
                return_value="26",
            ),
            patch(
                "src.services.campus_now_service.get_campus_now_pc_count",
                return_value=300,
            ),
            patch(
                "src.services.campus_now_service.get_campus_now_cache_seconds",
                return_value=60,
            ),
        ):
            first = await get_campus_now()
            second = await get_campus_now()

        self.assertIs(first, second)
        token_mock.assert_awaited_once()
        locations_mock.assert_awaited_once_with("app-token", "26")

    def test_resolve_cluster_name_accepts_cluster_name(self) -> None:
        self.assertEqual(resolve_cluster_name("koi"), "koi")
        self.assertEqual(resolve_cluster_name("Koi"), "koi")

    def test_build_cluster_now_calculates_crowd_percent(self) -> None:
        cluster_now = build_cluster_now(
            cluster_name="koi",
            active_count=14,
            seat_count=56,
        )

        self.assertEqual(cluster_now.cluster_id, "c1")
        self.assertEqual(cluster_now.cluster_name, "koi")
        self.assertEqual(cluster_now.active_count, 14)
        self.assertEqual(cluster_now.seat_count, 56)
        self.assertAlmostEqual(cluster_now.crowd_percent, 25.0)

    async def test_get_cluster_now_counts_hosts_by_cluster_name(self) -> None:
        token = FtAppToken(
            access_token="app-token",
            expires_at=datetime.now(UTC) + timedelta(hours=1),
        )
        locations = [
            FtLocation(
                id=1,
                begin_at=datetime.now(UTC),
                end_at=None,
                host="c1r1s1",
            ),
            FtLocation(
                id=2,
                begin_at=datetime.now(UTC),
                end_at=None,
                host="c1r1s2",
            ),
            FtLocation(
                id=3,
                begin_at=datetime.now(UTC),
                end_at=None,
                host="c2r1s1",
            ),
        ]

        with (
            patch(
                "src.services.campus_now_service.fetch_app_access_token",
                new=AsyncMock(return_value=token),
            ),
            patch(
                "src.services.campus_now_service."
                "fetch_active_campus_locations",
                new=AsyncMock(return_value=locations),
            ),
            patch(
                "src.services.campus_now_service.get_campus_now_campus_id",
                return_value="26",
            ),
            patch(
                "src.services.campus_now_service.get_campus_now_cache_seconds",
                return_value=60,
            ),
        ):
            cluster_now = await get_cluster_now("koi")

        self.assertEqual(cluster_now.cluster_id, "c1")
        self.assertEqual(cluster_now.active_count, 2)

    async def test_get_campus_all_returns_campus_and_clusters(self) -> None:
        token = FtAppToken(
            access_token="app-token",
            expires_at=datetime.now(UTC) + timedelta(hours=1),
        )
        locations = [
            FtLocation(
                id=1,
                begin_at=datetime.now(UTC),
                end_at=None,
                host="c1r1s1",
            ),
            FtLocation(
                id=2,
                begin_at=datetime.now(UTC),
                end_at=None,
                host="c2r1s1",
            ),
            FtLocation(
                id=3,
                begin_at=datetime.now(UTC),
                end_at=None,
                host=None,
            ),
        ]

        with (
            patch(
                "src.services.campus_now_service.fetch_app_access_token",
                new=AsyncMock(return_value=token),
            ),
            patch(
                "src.services.campus_now_service."
                "fetch_active_campus_locations",
                new=AsyncMock(return_value=locations),
            ),
            patch(
                "src.services.campus_now_service.get_campus_now_campus_id",
                return_value="26",
            ),
            patch(
                "src.services.campus_now_service.get_campus_now_pc_count",
                return_value=300,
            ),
            patch(
                "src.services.campus_now_service.get_campus_now_cache_seconds",
                return_value=60,
            ),
        ):
            campus_all = await get_campus_all()

        self.assertEqual(campus_all.campus.active_count, 3)
        self.assertEqual(len(campus_all.clusters), 6)
        self.assertEqual(campus_all.clusters[0].cluster_name, "koi")
        self.assertEqual(campus_all.clusters[0].active_count, 1)
        self.assertEqual(campus_all.clusters[1].cluster_name, "ume")
        self.assertEqual(campus_all.clusters[1].active_count, 1)


if __name__ == "__main__":
    unittest.main()
