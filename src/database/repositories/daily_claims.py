import sqlite3


def create_daily_claim(
    connection: sqlite3.Connection,
    user_id: int,
    claim_date: str,
    source: str,
    exp_gained: int,
) -> bool:
    cursor = connection.execute(
        """
        INSERT OR IGNORE INTO daily_claims (
            user_id,
            claim_date,
            source,
            exp_gained
        )
        VALUES (?, ?, ?, ?)
        """,
        (user_id, claim_date, source, exp_gained),
    )
    connection.commit()
    return cursor.rowcount == 1
