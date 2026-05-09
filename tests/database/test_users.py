import sqlite3
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from src.database.repositories.users import (  # noqa: E402
    get_user_by_discord_id,
    set_user_level_by_discord_id,
    set_user_mood_by_discord_id,
)
from src.database.schema import initialize_database  # noqa: E402


class UserRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        initialize_database(self.connection)

    def tearDown(self) -> None:
        self.connection.close()

    def test_set_user_level_creates_user_and_resets_exp(self) -> None:
        set_user_level_by_discord_id(self.connection, 123, 5)

        user = get_user_by_discord_id(self.connection, 123)

        assert user is not None
        self.assertEqual(int(user["level"]), 5)
        self.assertEqual(int(user["exp"]), 0)

    def test_set_user_level_updates_existing_user(self) -> None:
        self.connection.execute(
            """
            INSERT INTO users (discord_user_id, level, exp)
            VALUES (?, ?, ?)
            """,
            ("123", 2, 42),
        )

        set_user_level_by_discord_id(self.connection, 123, 3)
        user = get_user_by_discord_id(self.connection, 123)

        assert user is not None
        self.assertEqual(int(user["level"]), 3)
        self.assertEqual(int(user["exp"]), 0)

    def test_set_user_mood_creates_user_and_updates_stamina(self) -> None:
        set_user_mood_by_discord_id(self.connection, 123, "sleepy", 10)

        user = get_user_by_discord_id(self.connection, 123)

        assert user is not None
        self.assertEqual(user["mood"], "sleepy")
        self.assertEqual(int(user["stamina"]), 10)

    def test_set_user_mood_updates_existing_user(self) -> None:
        self.connection.execute(
            """
            INSERT INTO users (discord_user_id, mood, stamina)
            VALUES (?, ?, ?)
            """,
            ("123", "normal", 50),
        )

        set_user_mood_by_discord_id(self.connection, 123, "happy", 100)
        user = get_user_by_discord_id(self.connection, 123)

        assert user is not None
        self.assertEqual(user["mood"], "happy")
        self.assertEqual(int(user["stamina"]), 100)


if __name__ == "__main__":
    unittest.main()
