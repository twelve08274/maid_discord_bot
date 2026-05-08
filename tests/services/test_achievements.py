import asyncio
import sqlite3
import sys
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from src.database.repositories.achievements import (  # noqa: E402
    count_unlocked_visible_achievements,
)
from src.database.repositories.users import (  # noqa: E402
    get_or_create_user_id,
)
from src.database.schema import initialize_database  # noqa: E402
from src.services.achievements import grant_achievement  # noqa: E402


class AchievementServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        initialize_database(self.connection)

    def tearDown(self) -> None:
        self.connection.close()

    def test_grant_achievement_unlocks_once_and_applies_reward(self) -> None:
        bot = AsyncMock()

        with patch(
            "src.services.achievements.send_achievement_dm",
            new_callable=AsyncMock,
            return_value=True,
        ) as send_dm:
            first_result = asyncio.run(
                grant_achievement(
                    bot,
                    self.connection,
                    discord_user_id=123,
                    achievement_code="first_register",
                )
            )
            second_result = asyncio.run(
                grant_achievement(
                    bot,
                    self.connection,
                    discord_user_id=123,
                    achievement_code="first_register",
                )
            )

        user_id = get_or_create_user_id(self.connection, 123)
        row = self.connection.execute(
            "SELECT affection FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()

        self.assertTrue(first_result)
        self.assertFalse(second_result)
        self.assertEqual(int(row["affection"]), 5)
        self.assertEqual(
            count_unlocked_visible_achievements(self.connection, user_id),
            1,
        )
        send_dm.assert_awaited_once()

    def test_dm_failure_does_not_revert_unlock(self) -> None:
        bot = AsyncMock()

        with patch(
            "src.services.achievements.send_achievement_dm",
            new_callable=AsyncMock,
            return_value=False,
        ):
            result = asyncio.run(
                grant_achievement(
                    bot,
                    self.connection,
                    discord_user_id=123,
                    achievement_code="first_register",
                )
            )

        user_id = get_or_create_user_id(self.connection, 123)
        row = self.connection.execute(
            "SELECT affection FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()

        self.assertTrue(result)
        self.assertEqual(int(row["affection"]), 5)
        self.assertEqual(
            count_unlocked_visible_achievements(self.connection, user_id),
            1,
        )


if __name__ == "__main__":
    unittest.main()
