import sqlite3
import unittest
from datetime import UTC, datetime

from maid_discord_bot.database.repositories.ft_links import upsert_ft_link
from maid_discord_bot.database.repositories.users import get_or_create_user_id
from maid_discord_bot.database.schema import initialize_database


class FtLinksRepositoryTests(unittest.TestCase):
    def test_upsert_ft_link_creates_and_updates_link(self) -> None:
        connection = sqlite3.connect(":memory:")
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        initialize_database(connection)

        user_id = get_or_create_user_id(connection, 111)
        expires_at = datetime(2026, 5, 5, tzinfo=UTC)

        upsert_ft_link(
            connection,
            user_id=user_id,
            ft_user_id=42,
            ft_login="first",
            access_token="access-1",
            refresh_token="refresh-1",
            token_expires_at=expires_at,
        )
        upsert_ft_link(
            connection,
            user_id=user_id,
            ft_user_id=42,
            ft_login="second",
            access_token="access-2",
            refresh_token="refresh-2",
            token_expires_at=expires_at,
        )

        rows = connection.execute(
            "SELECT ft_user_id, ft_login, access_token FROM ft_links",
        ).fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["ft_user_id"], "42")
        self.assertEqual(rows[0]["ft_login"], "second")
        self.assertEqual(rows[0]["access_token"], "access-2")


if __name__ == "__main__":
    unittest.main()
