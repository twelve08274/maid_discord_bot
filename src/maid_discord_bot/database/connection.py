import sqlite3
from pathlib import Path
from types import TracebackType

from maid_discord_bot.config import get_database_path


class ClosingConnection(sqlite3.Connection):
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool:
        try:
            result = super().__exit__(exc_type, exc_value, traceback)
        finally:
            self.close()
        return bool(result)


def get_connection(database_path: Path | None = None) -> sqlite3.Connection:
    if database_path is None:
        database_path = get_database_path()

    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path, factory=ClosingConnection)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection
