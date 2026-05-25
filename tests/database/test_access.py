import sqlite3
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from src.database.repositories.access import (  # noqa: E402
    check_command_access,
    get_command_requirement,
    get_guild_by_name,
    is_registered_user,
    is_user_in_guild,
    join_user_guild,
    leave_user_guild,
    list_guilds,
)
from src.database.schema import initialize_database  # noqa: E402


class AccessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        initialize_database(self.connection)

    def tearDown(self) -> None:
        self.connection.close()

    def create_user(self, discord_user_id: int, level: int = 1) -> int:
        cursor = self.connection.execute(
            """
            INSERT INTO users (discord_user_id, level)
            VALUES (?, ?)
            """,
            (str(discord_user_id), level),
        )
        assert cursor.lastrowid is not None
        return int(cursor.lastrowid)

    def add_user_to_guild(self, user_id: int, guild_name: str) -> None:
        self.connection.execute(
            """
            INSERT INTO user_guilds (user_id, guild_id)
            SELECT ?, id
            FROM guilds
            WHERE name = ?
            """,
            (user_id, guild_name),
        )

    def test_is_registered_user_checks_discord_id(self) -> None:
        self.create_user(123)

        self.assertTrue(is_registered_user(self.connection, 123))
        self.assertFalse(is_registered_user(self.connection, 456))

    def test_is_user_in_guild_checks_membership(self) -> None:
        user_id = self.create_user(123)
        self.add_user_to_guild(user_id, "smash")

        self.assertTrue(is_user_in_guild(self.connection, 123, "smash"))
        self.assertFalse(is_user_in_guild(self.connection, 123, "poker"))

    def test_get_command_requirement_returns_guild_requirement(self) -> None:
        requirement = get_command_requirement(self.connection, "smash-rate")

        assert requirement is not None
        self.assertEqual(int(requirement["required_level"]), 3)
        self.assertEqual(requirement["required_guild_name"], "smash")

    def test_get_command_requirement_returns_campus_levels(self) -> None:
        campus = get_command_requirement(self.connection, "campus")
        campusnow = get_command_requirement(self.connection, "campusnow")
        campusall = get_command_requirement(self.connection, "campusall")

        assert campus is not None
        assert campusnow is not None
        assert campusall is not None
        self.assertEqual(int(campus["required_level"]), 0)
        self.assertEqual(int(campusnow["required_level"]), 2)
        self.assertEqual(int(campusall["required_level"]), 5)

    def test_list_guilds_returns_initial_guilds(self) -> None:
        guilds = list_guilds(self.connection)

        guild_names = {guild["name"] for guild in guilds}

        self.assertIn("smash", guild_names)
        self.assertIn("poker", guild_names)

    def test_get_guild_by_name_returns_guild(self) -> None:
        guild = get_guild_by_name(self.connection, "smash")

        assert guild is not None
        self.assertEqual(guild["display_name"], "スマブラギルド")

    def test_join_user_guild_adds_membership_once(self) -> None:
        self.create_user(123)

        first_joined = join_user_guild(self.connection, 123, "smash")
        second_joined = join_user_guild(self.connection, 123, "smash")

        self.assertTrue(first_joined)
        self.assertFalse(second_joined)
        self.assertTrue(is_user_in_guild(self.connection, 123, "smash"))

    def test_leave_user_guild_removes_membership_once(self) -> None:
        self.create_user(123)
        join_user_guild(self.connection, 123, "smash")

        first_left = leave_user_guild(self.connection, 123, "smash")
        second_left = leave_user_guild(self.connection, 123, "smash")

        self.assertTrue(first_left)
        self.assertFalse(second_left)
        self.assertFalse(is_user_in_guild(self.connection, 123, "smash"))

    def test_check_command_access_rejects_unregistered_user(self) -> None:
        allowed, reason = check_command_access(
            self.connection,
            123,
            "status",
        )

        self.assertFalse(allowed)
        self.assertIsNotNone(reason)

    def test_check_command_access_rejects_low_level_user(self) -> None:
        self.create_user(123, level=2)

        allowed, reason = check_command_access(
            self.connection,
            123,
            "smash-rate",
        )

        self.assertFalse(allowed)
        assert reason is not None
        self.assertIn("level 3", reason)

    def test_check_command_access_rejects_low_level_campusall(self) -> None:
        self.create_user(123, level=4)

        allowed, reason = check_command_access(
            self.connection,
            123,
            "campusall",
        )

        self.assertFalse(allowed)
        assert reason is not None
        self.assertIn("level 5", reason)

    def test_check_command_access_allows_required_campus_level(self) -> None:
        self.create_user(123, level=2)

        allowed, reason = check_command_access(
            self.connection,
            123,
            "campusnow",
        )

        self.assertTrue(allowed)
        self.assertIsNone(reason)

    def test_check_command_access_rejects_missing_guild(self) -> None:
        self.create_user(123, level=3)

        allowed, reason = check_command_access(
            self.connection,
            123,
            "smash-rate",
        )

        self.assertFalse(allowed)
        assert reason is not None
        self.assertIn("スマブラギルド", reason)

    def test_check_command_access_allows_matching_user(self) -> None:
        user_id = self.create_user(123, level=3)
        self.add_user_to_guild(user_id, "smash")

        allowed, reason = check_command_access(
            self.connection,
            123,
            "smash-rate",
        )

        self.assertTrue(allowed)
        self.assertIsNone(reason)


if __name__ == "__main__":
    unittest.main()
