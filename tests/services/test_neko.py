import sqlite3
import sys
import unittest
from datetime import date
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from src.database.repositories.achievements import (  # noqa: E402
    get_unlocked_achievements_for_user,
)
from src.database.repositories.users import (  # noqa: E402
    get_or_create_user_id,
)
from src.database.schema import initialize_database  # noqa: E402
from src.services.neko import (  # noqa: E402
    calculate_next_neko_streak,
    claim_neko,
)


class NekoServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        initialize_database(self.connection)

    def tearDown(self) -> None:
        self.connection.close()

    def test_calculate_next_neko_streak(self) -> None:
        today = date(2026, 5, 7)

        self.assertEqual(calculate_next_neko_streak("2026-05-07", 3, today), 3)
        self.assertEqual(calculate_next_neko_streak("2026-05-06", 3, today), 4)
        self.assertEqual(calculate_next_neko_streak("2026-05-05", 3, today), 1)
        self.assertEqual(calculate_next_neko_streak(None, 0, today), 1)

    def test_first_claim_records_claim_and_streak(self) -> None:
        result = claim_neko(self.connection, 123, date(2026, 5, 7))

        user = self.connection.execute(
            "SELECT neko_streak, last_neko_date FROM users WHERE id = ?",
            (result.user_id,),
        ).fetchone()
        claim_count = self._count_claims(result.user_id)

        self.assertTrue(result.claimed)
        self.assertEqual(result.streak, 1)
        self.assertFalse(result.achievement_unlocked)
        self.assertEqual(int(user["neko_streak"]), 1)
        self.assertEqual(user["last_neko_date"], "2026-05-07")
        self.assertEqual(claim_count, 1)

    def test_second_claim_on_same_day_does_not_update(self) -> None:
        first = claim_neko(self.connection, 123, date(2026, 5, 7))
        second = claim_neko(self.connection, 123, date(2026, 5, 7))

        user = self.connection.execute(
            "SELECT neko_streak, last_neko_date FROM users WHERE id = ?",
            (first.user_id,),
        ).fetchone()

        self.assertFalse(second.claimed)
        self.assertEqual(second.streak, 1)
        self.assertEqual(int(user["neko_streak"]), 1)
        self.assertEqual(user["last_neko_date"], "2026-05-07")
        self.assertEqual(self._count_claims(first.user_id), 1)

    def test_consecutive_claim_increments_streak(self) -> None:
        claim_neko(self.connection, 123, date(2026, 5, 6))
        result = claim_neko(self.connection, 123, date(2026, 5, 7))

        self.assertTrue(result.claimed)
        self.assertEqual(result.streak, 2)
        self.assertEqual(self._count_claims(result.user_id), 2)

    def test_gap_resets_streak(self) -> None:
        claim_neko(self.connection, 123, date(2026, 5, 5))
        result = claim_neko(self.connection, 123, date(2026, 5, 7))

        self.assertTrue(result.claimed)
        self.assertEqual(result.streak, 1)
        self.assertEqual(self._count_claims(result.user_id), 2)

    def test_seventh_consecutive_claim_unlocks_hidden_achievement_once(self) -> None:
        result = None
        for day in range(1, 8):
            result = claim_neko(self.connection, 123, date(2026, 5, day))

        assert result is not None
        eighth_result = claim_neko(self.connection, 123, date(2026, 5, 8))
        achievements = get_unlocked_achievements_for_user(
            self.connection,
            result.user_id,
        )

        self.assertTrue(result.achievement_unlocked)
        self.assertFalse(eighth_result.achievement_unlocked)
        self.assertIn("neko_7_days", {row["code"] for row in achievements})

    def test_existing_unique_claim_is_treated_as_already_claimed(self) -> None:
        user_id = get_or_create_user_id(self.connection, 123)
        self.connection.execute(
            """
            INSERT INTO neko_claims (user_id, claimed_date)
            VALUES (?, ?)
            """,
            (user_id, "2026-05-07"),
        )
        self.connection.commit()

        result = claim_neko(self.connection, 123, date(2026, 5, 7))

        self.assertFalse(result.claimed)
        self.assertEqual(result.streak, 0)
        self.assertEqual(self._count_claims(user_id), 1)

    def _count_claims(self, user_id: int) -> int:
        row = self.connection.execute(
            "SELECT COUNT(*) AS count FROM neko_claims WHERE user_id = ?",
            (user_id,),
        ).fetchone()
        return int(row["count"])


if __name__ == "__main__":
    unittest.main()
