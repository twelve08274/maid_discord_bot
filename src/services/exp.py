import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class ExpResult:
    previous_level: int
    level: int
    exp: int
    leveled_up: bool


def required_exp_for_level(level: int) -> int:
    return level * 100


def add_exp(
    connection: sqlite3.Connection,
    user_id: int,
    amount: int,
) -> ExpResult:
    row = connection.execute(
        """
        SELECT level, exp
        FROM users
        WHERE id = ?
        """,
        (user_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"User {user_id} does not exist.")

    previous_level = int(row["level"])
    level = previous_level
    exp = int(row["exp"]) + amount

    while exp >= required_exp_for_level(level):
        exp -= required_exp_for_level(level)
        level += 1

    connection.execute(
        """
        UPDATE users
        SET level = ?, exp = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (level, exp, user_id),
    )
    connection.commit()

    return ExpResult(
        previous_level=previous_level,
        level=level,
        exp=exp,
        leveled_up=level > previous_level,
    )
