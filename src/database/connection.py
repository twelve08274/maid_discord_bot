import sqlite3
from pathlib import Path

from ..config import get_database_path


def get_connection(database_path: Path | None = None) -> sqlite3.Connection:
    if database_path is None:
        database_path = get_database_path()

    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection
