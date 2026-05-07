import sqlite3


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
    return int(cursor.lastrowid)
