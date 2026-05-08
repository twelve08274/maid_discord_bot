import sqlite3


def get_user_by_discord_id(
    connection: sqlite3.Connection,
    discord_user_id: int,
) -> sqlite3.Row | None:
    return connection.execute(  # type: ignore[no-any-return]
        """
        SELECT *
        FROM users
        WHERE discord_user_id = ?
        """,
        (str(discord_user_id),),
    ).fetchone()


def get_or_create_user_id(
    connection: sqlite3.Connection,
    discord_user_id: int,
) -> int:
    value = str(discord_user_id)
    row = connection.execute(
        "SELECT id FROM users WHERE discord_user_id = ?",
        (value,),
    ).fetchone()
    if row is not None:
        return int(row["id"])

    cursor = connection.execute(
        """
        INSERT INTO users (discord_user_id)
        VALUES (?)
        """,
        (value,),
    )
    connection.commit()
    assert cursor.lastrowid is not None
    return int(cursor.lastrowid)


def set_user_level_by_discord_id(
    connection: sqlite3.Connection,
    discord_user_id: int,
    level: int,
) -> None:
    user_id = get_or_create_user_id(connection, discord_user_id)
    connection.execute(
        """
        UPDATE users
        SET level = ?, exp = 0, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (level, user_id),
    )
    connection.commit()


def set_user_mood_by_discord_id(
    connection: sqlite3.Connection,
    discord_user_id: int,
    mood: str,
    stamina: int,
) -> None:
    user_id = get_or_create_user_id(connection, discord_user_id)
    connection.execute(
        """
        UPDATE users
        SET mood = ?, stamina = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (mood, stamina, user_id),
    )
    connection.commit()


def delete_user_by_discord_id(
    connection: sqlite3.Connection,
    discord_user_id: int,
) -> bool:
    row = get_user_by_discord_id(connection, discord_user_id)
    if row is None:
        return False
    user_id = int(row["id"])
    child_tables = (
        "user_achievements",
        "user_guilds",
        "daily_claims",
        "ft_location_rewards",
        "tasks",
        "ft_links",
    )
    for table in child_tables:
        connection.execute(
            f"DELETE FROM {table} WHERE user_id = ?", (user_id,)
        )
    connection.execute("DELETE FROM users WHERE id = ?", (user_id,))
    return True


def set_auto_daily_enabled(
    connection: sqlite3.Connection,
    discord_user_id: int,
    enabled: bool,
) -> None:
    user_id = get_or_create_user_id(connection, discord_user_id)
    connection.execute(
        """
        UPDATE users
        SET auto_daily_enabled = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (1 if enabled else 0, user_id),
    )
    connection.commit()
