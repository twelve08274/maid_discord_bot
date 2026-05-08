import sqlite3

def get_ft_link(
    connection: sqlite3.Connection,
    user_id: int,
) -> sqlite3.Row | None:
    return connection.execute(
        "SELECT ft_login FROM ft_links WHERE user_id = ?",
        (user_id,),
    ).fetchone()
