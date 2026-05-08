import sqlite3
from datetime import datetime


def create_ft_location_reward(
    connection: sqlite3.Connection,
    user_id: int,
    ft_location_id: int,
    ft_login: str,
    host: str | None,
    begin_at: datetime,
    exp_gained: int,
) -> bool:
    cursor = connection.execute(
        """
        INSERT OR IGNORE INTO ft_location_rewards (
            user_id,
            ft_location_id,
            ft_login,
            host,
            begin_at,
            exp_gained
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            str(ft_location_id),
            ft_login,
            host,
            begin_at.isoformat(),
            exp_gained,
        ),
    )
    connection.commit()
    return cursor.rowcount == 1


def mark_ft_location_reward_notified(
    connection: sqlite3.Connection,
    user_id: int,
    ft_location_id: int,
) -> None:
    connection.execute(
        """
        UPDATE ft_location_rewards
        SET notified_at = CURRENT_TIMESTAMP
        WHERE user_id = ? AND ft_location_id = ?
        """,
        (user_id, str(ft_location_id)),
    )
    connection.commit()
