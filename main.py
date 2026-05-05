import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from maid_discord_bot.bot import run_bot  # noqa: E402


if __name__ == "__main__":
    run_bot()
