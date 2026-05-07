import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from src.database.connection import get_connection  # noqa: E402
from src.database.schema import initialize_database  # noqa: E402


def main() -> None:
    with get_connection() as connection:
        initialize_database(connection)
    print("Database initialized.")


if __name__ == "__main__":
    main()
