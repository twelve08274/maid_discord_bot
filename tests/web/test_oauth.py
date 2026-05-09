import sqlite3
import sys
import unittest
from contextlib import nullcontext
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import AsyncMock, patch


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from src.database.schema import initialize_database  # noqa: E402
from src.services.ft_api import FtToken, FtUser  # noqa: E402
from src.services.oauth_state import OAuthState  # noqa: E402
from src.web.oauth import ft_oauth_callback  # noqa: E402


class OAuthCallbackTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        initialize_database(self.connection)

    def tearDown(self) -> None:
        self.connection.close()

    async def test_callback_links_account_and_enables_auto_daily(
        self,
    ) -> None:
        token = FtToken(
            access_token="access-token",
            refresh_token="refresh-token",
            expires_at=datetime.now(UTC) + timedelta(hours=2),
        )
        ft_user = FtUser(id=456, login="alice")
        oauth_state = OAuthState(
            discord_user_id=123,
            issued_at=1,
            nonce="nonce",
        )

        with (
            patch("src.web.oauth.parse_oauth_state", return_value=oauth_state),
            patch(
                "src.web.oauth.exchange_code_for_token",
                new=AsyncMock(return_value=token),
            ),
            patch(
                "src.web.oauth.fetch_current_user",
                new=AsyncMock(return_value=ft_user),
            ),
            patch(
                "src.web.oauth.get_connection",
                return_value=nullcontext(self.connection),
            ),
        ):
            response = await ft_oauth_callback(
                code="oauth-code",
                state="oauth-state",
            )

        self.assertIn("42 account linked", response)

        user = self.connection.execute(
            """
            SELECT users.auto_daily_enabled, ft_links.ft_login
            FROM users
            INNER JOIN ft_links ON ft_links.user_id = users.id
            WHERE users.discord_user_id = ?
            """,
            ("123",),
        ).fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(int(user["auto_daily_enabled"]), 1)
        self.assertEqual(user["ft_login"], "alice")


if __name__ == "__main__":
    unittest.main()
