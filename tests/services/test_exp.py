import sqlite3
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from src.database.schema import initialize_database  # noqa: E402
from src.services.exp import (  # noqa: E402
    add_exp,
    required_exp_for_level,
)


class ExpTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        initialize_database(self.connection)
        cursor = self.connection.execute(
            "INSERT INTO users (discord_user_id, level, exp) VALUES (?, ?, ?)",
            ("123", 1, 95),
        )
        self.user_id = int(cursor.lastrowid)

    def tearDown(self) -> None:
        self.connection.close()

    def test_required_exp_for_level_scales_by_level(self) -> None:
        self.assertEqual(required_exp_for_level(1), 100)
        self.assertEqual(required_exp_for_level(5), 500)

    def test_add_exp_levels_up_and_keeps_remaining_exp(self) -> None:
        result = add_exp(self.connection, self.user_id, 10)

        self.assertTrue(result.leveled_up)
        self.assertEqual(result.previous_level, 1)
        self.assertEqual(result.level, 2)
        self.assertEqual(result.exp, 5)

        row = self.connection.execute(
            "SELECT level, exp FROM users WHERE id = ?",
            (self.user_id,),
        ).fetchone()
        self.assertEqual(int(row["level"]), 2)
        self.assertEqual(int(row["exp"]), 5)


if __name__ == "__main__":
    unittest.main()
