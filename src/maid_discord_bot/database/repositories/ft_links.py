import sqlite3
from datetime import datetime


def upsert_ft_link(
    connection: sqlite3.Connection,
    user_id: int,
    ft_user_id: int,
    ft_login: str,
    access_token: str,
    refresh_token: str,
    token_expires_at: datetime,
) -> None:
    connection.execute(
        """
        INSERT INTO ft_links (
            user_id,
            ft_user_id,
            ft_login,
            access_token,
            refresh_token,
            token_expires_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            ft_user_id = excluded.ft_user_id,
            ft_login = excluded.ft_login,
            access_token = excluded.access_token,
            refresh_token = excluded.refresh_token,
            token_expires_at = excluded.token_expires_at,
            updated_at = CURRENT_TIMESTAMP
        """,
        (
            user_id,
            str(ft_user_id),
            ft_login,
            access_token,
            refresh_token,
            token_expires_at.isoformat(),
        ),
    )
    connection.commit()
