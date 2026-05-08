import sqlite3
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from src.database.schema import initialize_database  # noqa: E402


class SchemaTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        initialize_database(self.connection)

    def tearDown(self) -> None:
        self.connection.close()

    def test_initialize_database_creates_expected_tables(self) -> None:
        rows = self.connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            """
        ).fetchall()

        table_names = {row["name"] for row in rows}

        self.assertTrue(
            {
                "users",
                "ft_links",
                "daily_claims",
                "ft_location_rewards",
                "achievements",
                "user_achievements",
                "tasks",
                "guilds",
                "user_guilds",
                "command_requirements",
            }.issubset(table_names)
        )

    def test_daily_claims_are_unique_per_user_and_date(self) -> None:
        cursor = self.connection.execute(
            "INSERT INTO users (discord_user_id) VALUES (?)",
            ("123",),
        )
        user_id = int(cursor.lastrowid)
        self.connection.execute(
            """
            INSERT INTO daily_claims (user_id, claim_date, source)
            VALUES (?, ?, ?)
            """,
            (user_id, "2026-05-06", "manual"),
        )

        with self.assertRaises(sqlite3.IntegrityError):
            self.connection.execute(
                """
                INSERT INTO daily_claims (user_id, claim_date, source)
                VALUES (?, ?, ?)
                """,
                (user_id, "2026-05-06", "auto"),
            )

    def test_user_achievements_are_unique(
        self,
    ) -> None:
        user_cursor = self.connection.execute(
            "INSERT INTO users (discord_user_id) VALUES (?)",
            ("123",),
        )
        achievement_cursor = self.connection.execute(
            """
            INSERT INTO achievements (code, name, description)
            VALUES (?, ?, ?)
            """,
            (
                "schema_test_achievement",
                "First Register",
                "Registered for the first time.",
            ),
        )

        user_id = int(user_cursor.lastrowid)
        achievement_id = int(achievement_cursor.lastrowid)
        self.connection.execute(
            """
            INSERT INTO user_achievements (user_id, achievement_id)
            VALUES (?, ?)
            """,
            (user_id, achievement_id),
        )

        with self.assertRaises(sqlite3.IntegrityError):
            self.connection.execute(
                """
                INSERT INTO user_achievements (user_id, achievement_id)
                VALUES (?, ?)
                """,
                (user_id, achievement_id),
            )

    def test_initialize_database_seeds_initial_achievements(self) -> None:
        rows = self.connection.execute(
            """
            SELECT code, reward_affection
            FROM achievements
            ORDER BY code
            """
        ).fetchall()

        achievements = {row["code"]: row for row in rows}

        self.assertIn("first_register", achievements)
        self.assertEqual(
            int(achievements["first_register"]["reward_affection"]),
            5,
        )

    def test_tasks_are_unique_per_user_and_task_name(self) -> None:
        cursor = self.connection.execute(
            "INSERT INTO users (discord_user_id) VALUES (?)",
            ("123",),
        )
        user_id = int(cursor.lastrowid)
        self.connection.execute(
            "INSERT INTO tasks (user_id, task_name) VALUES (?, ?)",
            (user_id, "push_swap"),
        )

        with self.assertRaises(sqlite3.IntegrityError):
            self.connection.execute(
                "INSERT INTO tasks (user_id, task_name) VALUES (?, ?)",
                (user_id, "push_swap"),
            )

    def test_initialize_database_seeds_initial_guilds(self) -> None:
        rows = self.connection.execute(
            """
            SELECT name, display_name
            FROM guilds
            ORDER BY name
            """
        ).fetchall()

        guilds = {row["name"]: row["display_name"] for row in rows}

        self.assertEqual(guilds["smash"], "スマブラギルド")
        self.assertEqual(guilds["poker"], "ポーカーギルド")

    def test_initialize_database_seeds_command_requirements(self) -> None:
        rows = self.connection.execute(
            """
            SELECT
                command_requirements.command_name,
                command_requirements.required_level,
                guilds.name AS guild_name
            FROM command_requirements
            LEFT JOIN guilds
                ON guilds.id = command_requirements.required_guild_id
            """
        ).fetchall()

        requirements = {row["command_name"]: row for row in rows}

        self.assertEqual(
            int(requirements["status"]["required_level"]),
            1,
        )
        self.assertIsNone(requirements["status"]["guild_name"])
        self.assertEqual(
            int(requirements["smash-rate"]["required_level"]),
            3,
        )
        self.assertEqual(requirements["smash-rate"]["guild_name"], "smash")


if __name__ == "__main__":
    unittest.main()
