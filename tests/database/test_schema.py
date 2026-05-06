import sqlite3
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from maid_discord_bot.database.schema import initialize_database  # noqa: E402


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
                "neko_claims",
                "ft_location_rewards",
                "achievements",
                "user_achievements",
                "tasks",
            }.issubset(table_names)
        )

    def test_users_have_neko_streak_columns(self) -> None:
        rows = self.connection.execute("PRAGMA table_info(users)").fetchall()
        column_names = {row["name"] for row in rows}

        self.assertIn("neko_streak", column_names)
        self.assertIn("last_neko_date", column_names)

    def test_neko_claims_are_unique_per_user_and_date(self) -> None:
        cursor = self.connection.execute(
            "INSERT INTO users (discord_user_id) VALUES (?)",
            ("123",),
        )
        user_id = int(cursor.lastrowid)
        self.connection.execute(
            """
            INSERT INTO neko_claims (user_id, claimed_date)
            VALUES (?, ?)
            """,
            (user_id, "2026-05-06"),
        )

        with self.assertRaises(sqlite3.IntegrityError):
            self.connection.execute(
                """
                INSERT INTO neko_claims (user_id, claimed_date)
                VALUES (?, ?)
                """,
                (user_id, "2026-05-06"),
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
        self.assertIn("neko_7_days", achievements)
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


if __name__ == "__main__":
    unittest.main()
