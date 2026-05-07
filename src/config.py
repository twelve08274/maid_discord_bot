import os

from dotenv import load_dotenv


load_dotenv()


class ConfigError(RuntimeError):
    pass


def get_discord_token() -> str:
    token = os.getenv("DISCORD_TOKEN")
    if token is None:
        raise ConfigError("DISCORD_TOKEN is not set.")
    return token


def get_discord_test_guild_id() -> int | None:
    guild_id = os.getenv("DISCORD_TEST_GUILD_ID")
    if guild_id is None or guild_id == "":
        return None
    try:
        return int(guild_id)
    except ValueError as error:
        message = "DISCORD_TEST_GUILD_ID must be an integer."
        raise ConfigError(message) from error
