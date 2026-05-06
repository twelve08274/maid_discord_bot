import sqlite3


def insert_neko_claim(
    connection: sqlite3.Connection,
    user_id: int,
    claimed_date: str,
) -> bool:
    cursor = connection.execute(
        """
        INSERT OR IGNORE INTO neko_claims (user_id, claimed_date)
        VALUES (?, ?)
        """,
        (user_id, claimed_date),
    )
    connection.commit()
    return cursor.rowcount > 0
