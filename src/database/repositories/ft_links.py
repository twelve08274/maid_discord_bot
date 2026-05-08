import sqlite3
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class LinkedFtAccount:
    user_id: int
    discord_user_id: int
    ft_user_id: str
    ft_login: str
    access_token: str
    refresh_token: str
    token_expires_at: datetime


class FtAccountAlreadyLinkedError(RuntimeError):
    pass


def upsert_ft_link(
    connection: sqlite3.Connection,
    user_id: int,
    ft_user_id: int,
    ft_login: str,
    access_token: str,
    refresh_token: str,
    token_expires_at: datetime,
) -> None:
    existing_link = connection.execute(
        """
        SELECT user_id
        FROM ft_links
        WHERE ft_user_id = ?
          AND user_id != ?
        """,
        (str(ft_user_id), user_id),
    ).fetchone()
    if existing_link is not None:
        raise FtAccountAlreadyLinkedError(
            "This 42 account is already linked to another Discord user."
        )

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


def get_ft_link_for_discord_user(
    connection: sqlite3.Connection,
    discord_user_id: int,
) -> sqlite3.Row | None:
    return connection.execute(  # type: ignore[no-any-return]
        """
        SELECT ft_links.*
        FROM ft_links
        INNER JOIN users ON users.id = ft_links.user_id
        WHERE users.discord_user_id = ?
        """,
        (str(discord_user_id),),
    ).fetchone()


def get_ft_link(
    connection: sqlite3.Connection,
    user_id: int,
) -> sqlite3.Row | None:
    return connection.execute(
        "SELECT ft_login FROM ft_links WHERE user_id = ?",
        (user_id,),
    ).fetchone()


def delete_ft_link_for_discord_user(
    connection: sqlite3.Connection,
    discord_user_id: int,
) -> bool:
    cursor = connection.execute(
        """
        DELETE FROM ft_links
        WHERE user_id = (
            SELECT id
            FROM users
            WHERE discord_user_id = ?
        )
        """,
        (str(discord_user_id),),
    )
    connection.commit()
    return cursor.rowcount > 0


def get_ft_link_by_login(
    connection: sqlite3.Connection,
    ft_login: str,
) -> LinkedFtAccount | None:
    row = connection.execute(
        """
        SELECT
            users.id AS user_id,
            users.discord_user_id,
            ft_links.ft_user_id,
            ft_links.ft_login,
            ft_links.access_token,
            ft_links.refresh_token,
            ft_links.token_expires_at
        FROM ft_links
        INNER JOIN users ON users.id = ft_links.user_id
        WHERE ft_links.ft_login = ?
        """,
        (ft_login,),
    ).fetchone()
    if row is None:
        return None
    return LinkedFtAccount(
        user_id=int(row["user_id"]),
        discord_user_id=int(row["discord_user_id"]),
        ft_user_id=str(row["ft_user_id"]),
        ft_login=str(row["ft_login"]),
        access_token=str(row["access_token"]),
        refresh_token=str(row["refresh_token"]),
        token_expires_at=datetime.fromisoformat(str(row["token_expires_at"])),
    )


def list_auto_daily_ft_links(
    connection: sqlite3.Connection,
) -> list[LinkedFtAccount]:
    rows = connection.execute(
        """
        SELECT
            users.id AS user_id,
            users.discord_user_id,
            ft_links.ft_user_id,
            ft_links.ft_login,
            ft_links.access_token,
            ft_links.refresh_token,
            ft_links.token_expires_at
        FROM users
        INNER JOIN ft_links ON ft_links.user_id = users.id
        WHERE users.auto_daily_enabled = 1
        ORDER BY users.id
        """
    ).fetchall()

    return [
        LinkedFtAccount(
            user_id=int(row["user_id"]),
            discord_user_id=int(row["discord_user_id"]),
            ft_user_id=str(row["ft_user_id"]),
            ft_login=str(row["ft_login"]),
            access_token=str(row["access_token"]),
            refresh_token=str(row["refresh_token"]),
            token_expires_at=datetime.fromisoformat(
                str(row["token_expires_at"]),
            ),
        )
        for row in rows
    ]


def update_ft_tokens(
    connection: sqlite3.Connection,
    user_id: int,
    access_token: str,
    refresh_token: str,
    token_expires_at: datetime,
) -> None:
    connection.execute(
        """
        UPDATE ft_links
        SET
            access_token = ?,
            refresh_token = ?,
            token_expires_at = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE user_id = ?
        """,
        (
            access_token,
            refresh_token,
            token_expires_at.isoformat(),
            user_id,
        ),
    )
    connection.commit()
