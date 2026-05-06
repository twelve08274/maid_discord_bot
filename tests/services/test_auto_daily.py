import sqlite3
import sys
import unittest
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import AsyncMock, patch


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from maid_discord_bot.database.repositories.ft_links import (  # noqa: E402
    LinkedFtAccount,
    upsert_ft_link,
)
from maid_discord_bot.database.repositories.ft_location_rewards import (  # noqa: E402,E501
    create_ft_location_reward,
)
from maid_discord_bot.database.repositories.users import (  # noqa: E402
    get_or_create_user_id,
)
from maid_discord_bot.database.schema import initialize_database  # noqa: E402
from maid_discord_bot.services.auto_daily import (  # noqa: E402
    check_and_reward_auto_daily,
)
from maid_discord_bot.services.ft_api import FtLocation, FtToken  # noqa: E402


class AutoDailyTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        initialize_database(self.connection)
        self.user_id = get_or_create_user_id(self.connection, 123)
        self.connection.execute(
            """
            UPDATE users
            SET auto_daily_enabled = 1
            WHERE id = ?
            """,
            (self.user_id,),
        )
        self.connection.commit()

    def tearDown(self) -> None:
        self.connection.close()

    async def test_rewards_active_location_once_per_day(self) -> None:
        account = self._linked_account()
        location = FtLocation(
            id=42,
            begin_at=datetime(2026, 5, 6, 1, 0, tzinfo=UTC),
            end_at=None,
            host="c1r1s1",
        )

        with patch(
            "maid_discord_bot.services.auto_daily.fetch_active_location",
            new=AsyncMock(return_value=location),
        ):
            first_result = await check_and_reward_auto_daily(
                self.connection,
                account,
            )
            second_result = await check_and_reward_auto_daily(
                self.connection,
                account,
            )

        self.assertIsNotNone(first_result)
        self.assertIsNone(second_result)

        user = self.connection.execute(
            "SELECT level, exp FROM users WHERE id = ?",
            (self.user_id,),
        ).fetchone()
        self.assertEqual(int(user["level"]), 1)
        self.assertEqual(int(user["exp"]), 10)

        daily_claims = self.connection.execute(
            "SELECT COUNT(*) AS count FROM daily_claims"
        ).fetchone()
        self.assertEqual(int(daily_claims["count"]), 1)

    async def test_refreshes_expired_access_token(self) -> None:
        account = self._linked_account(
            access_token="old-access-token",
            refresh_token="old-refresh-token",
            token_expires_at=datetime.now(UTC) - timedelta(minutes=1),
        )
        refreshed_token = FtToken(
            access_token="new-access-token",
            refresh_token="new-refresh-token",
            expires_at=datetime.now(UTC) + timedelta(hours=2),
        )

        with (
            patch(
                "maid_discord_bot.services.auto_daily.refresh_access_token",
                new=AsyncMock(return_value=refreshed_token),
            ) as refresh_mock,
            patch(
                "maid_discord_bot.services.auto_daily.fetch_active_location",
                new=AsyncMock(return_value=None),
            ) as location_mock,
        ):
            result = await check_and_reward_auto_daily(
                self.connection,
                account,
            )

        self.assertIsNone(result)
        refresh_mock.assert_awaited_once_with("old-refresh-token")
        location_mock.assert_awaited_once_with("new-access-token", "alice")

        row = self.connection.execute(
            """
            SELECT access_token, refresh_token
            FROM ft_links
            WHERE user_id = ?
            """,
            (self.user_id,),
        ).fetchone()
        self.assertEqual(row["access_token"], "new-access-token")
        self.assertEqual(row["refresh_token"], "new-refresh-token")

    async def test_rewards_even_if_location_was_recorded_before_claim(
        self,
    ) -> None:
        account = self._linked_account()
        location = FtLocation(
            id=42,
            begin_at=datetime(2026, 5, 6, 1, 0, tzinfo=UTC),
            end_at=None,
            host="c1r1s1",
        )
        create_ft_location_reward(
            self.connection,
            user_id=self.user_id,
            ft_location_id=location.id,
            ft_login="alice",
            host=location.host,
            begin_at=location.begin_at,
            exp_gained=10,
        )

        with patch(
            "maid_discord_bot.services.auto_daily.fetch_active_location",
            new=AsyncMock(return_value=location),
        ):
            result = await check_and_reward_auto_daily(
                self.connection,
                account,
            )

        self.assertIsNotNone(result)

        user = self.connection.execute(
            "SELECT exp FROM users WHERE id = ?",
            (self.user_id,),
        ).fetchone()
        self.assertEqual(int(user["exp"]), 10)

        daily_claims = self.connection.execute(
            "SELECT COUNT(*) AS count FROM daily_claims"
        ).fetchone()
        self.assertEqual(int(daily_claims["count"]), 1)

    def _linked_account(
        self,
        access_token: str = "access-token",
        refresh_token: str = "refresh-token",
        token_expires_at: datetime | None = None,
    ) -> LinkedFtAccount:
        if token_expires_at is None:
            token_expires_at = datetime.now(UTC) + timedelta(hours=2)

        upsert_ft_link(
            self.connection,
            user_id=self.user_id,
            ft_user_id=456,
            ft_login="alice",
            access_token=access_token,
            refresh_token=refresh_token,
            token_expires_at=token_expires_at,
        )
        return LinkedFtAccount(
            user_id=self.user_id,
            discord_user_id=123,
            ft_user_id="456",
            ft_login="alice",
            access_token=access_token,
            refresh_token=refresh_token,
            token_expires_at=token_expires_at,
        )


if __name__ == "__main__":
    unittest.main()
