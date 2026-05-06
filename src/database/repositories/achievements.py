import sqlite3


def get_achievement(
    connection: sqlite3.Connection,
    achievement_code: str,
) -> sqlite3.Row | None:
    return connection.execute(  # type: ignore[no-any-return]
        """
        SELECT *
        FROM achievements
        WHERE code = ?
        """,
        (achievement_code,),
    ).fetchone()


def unlock_achievement(
    connection: sqlite3.Connection,
    user_id: int,
    achievement_code: str,
) -> bool:
    achievement = get_achievement(connection, achievement_code)
    if achievement is None:
        return False

    cursor = connection.execute(
        """
        INSERT OR IGNORE INTO user_achievements (user_id, achievement_id)
        VALUES (?, ?)
        """,
        (user_id, int(achievement["id"])),
    )
    connection.commit()
    return cursor.rowcount > 0


def get_unlocked_achievements_for_user(
    connection: sqlite3.Connection,
    user_id: int,
) -> list[sqlite3.Row]:
    return list(
        connection.execute(
            """
            SELECT
                a.id,
                a.code,
                a.name,
                a.description,
                a.hidden,
                a.reward_exp,
                a.reward_affection,
                a.reward_stamina,
                ua.unlocked_at
            FROM user_achievements ua
            JOIN achievements a
                ON ua.achievement_id = a.id
            WHERE ua.user_id = ?
            ORDER BY ua.unlocked_at ASC
            """,
            (user_id,),
        ).fetchall()
    )


def count_visible_achievements(connection: sqlite3.Connection) -> int:
    row = connection.execute(
        """
        SELECT COUNT(*) AS count
        FROM achievements
        WHERE hidden = 0
        """
    ).fetchone()
    return int(row["count"])


def count_unlocked_visible_achievements(
    connection: sqlite3.Connection,
    user_id: int,
) -> int:
    row = connection.execute(
        """
        SELECT COUNT(*) AS count
        FROM user_achievements ua
        JOIN achievements a
            ON ua.achievement_id = a.id
        WHERE ua.user_id = ?
            AND a.hidden = 0
        """,
        (user_id,),
    ).fetchone()
    return int(row["count"])
