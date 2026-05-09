import sqlite3
import sys
import unittest
from datetime import UTC, datetime
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from src.database.repositories.ft_links import (  # noqa: E402
    FtAccountAlreadyLinkedError,
    delete_ft_link_for_discord_user,
    upsert_ft_link,
)
from src.database.schema import initialize_database  # noqa: E402


class FtLinksTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        initialize_database(self.connection)
        self.expires_at = datetime(2026, 5, 9, tzinfo=UTC)

    def tearDown(self) -> None:
        self.connection.close()

    def create_user(self, discord_user_id: int) -> int:
        cursor = self.connection.execute(
            "INSERT INTO users (discord_user_id) VALUES (?)",
            (str(discord_user_id),),
        )
        assert cursor.lastrowid is not None
        return int(cursor.lastrowid)

    def test_upsert_ft_link_updates_same_user(self) -> None:
        user_id = self.create_user(123)
        upsert_ft_link(
            self.connection,
            user_id=user_id,
            ft_user_id=42,
            ft_login="old_login",
            access_token="old_access",
            refresh_token="old_refresh",
            token_expires_at=self.expires_at,
        )

        upsert_ft_link(
            self.connection,
            user_id=user_id,
            ft_user_id=42,
            ft_login="new_login",
            access_token="new_access",
            refresh_token="new_refresh",
            token_expires_at=self.expires_at,
        )
        row = self.connection.execute(
            "SELECT ft_login, access_token FROM ft_links WHERE user_id = ?",
            (user_id,),
        ).fetchone()

        self.assertEqual(row["ft_login"], "new_login")
        self.assertEqual(row["access_token"], "new_access")

    def test_upsert_ft_link_rejects_account_linked_to_other_user(self) -> None:
        first_user_id = self.create_user(123)
        second_user_id = self.create_user(456)
        upsert_ft_link(
            self.connection,
            user_id=first_user_id,
            ft_user_id=42,
            ft_login="login",
            access_token="access",
            refresh_token="refresh",
            token_expires_at=self.expires_at,
        )

        with self.assertRaises(FtAccountAlreadyLinkedError):
            upsert_ft_link(
                self.connection,
                user_id=second_user_id,
                ft_user_id=42,
                ft_login="login",
                access_token="access",
                refresh_token="refresh",
                token_expires_at=self.expires_at,
            )

    def test_delete_ft_link_for_discord_user_removes_link(self) -> None:
        user_id = self.create_user(123)
        upsert_ft_link(
            self.connection,
            user_id=user_id,
            ft_user_id=42,
            ft_login="login",
            access_token="access",
            refresh_token="refresh",
            token_expires_at=self.expires_at,
        )

        deleted = delete_ft_link_for_discord_user(self.connection, 123)
        row = self.connection.execute(
            "SELECT 1 FROM ft_links WHERE user_id = ?",
            (user_id,),
        ).fetchone()

        self.assertTrue(deleted)
        self.assertIsNone(row)

    def test_delete_ft_link_for_discord_user_returns_false_without_link(
        self,
    ) -> None:
        self.create_user(123)

        deleted = delete_ft_link_for_discord_user(self.connection, 123)

        self.assertFalse(deleted)


if __name__ == "__main__":
    unittest.main()
