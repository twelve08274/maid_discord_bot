import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class ConfigError(RuntimeError):
    pass


@dataclass(frozen=True)
class FtOAuthConfig:
    client_id: str
    client_secret: str
    redirect_uri: str
    scopes: str


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


def get_database_path() -> Path:
    value = os.getenv("DATABASE_PATH", "data/maid_discord_bot.sqlite3")
    return Path(value)


def get_ft_oauth_config() -> FtOAuthConfig:
    client_id = os.getenv("FT_CLIENT_ID")
    client_secret = os.getenv("FT_CLIENT_SECRET")
    redirect_uri = os.getenv("FT_REDIRECT_URI")
    scopes = os.getenv("FT_SCOPES", "public")

    missing = [
        name
        for name, value in (
            ("FT_CLIENT_ID", client_id),
            ("FT_CLIENT_SECRET", client_secret),
            ("FT_REDIRECT_URI", redirect_uri),
        )
        if value is None or value == ""
    ]
    if missing:
        raise ConfigError(f"{', '.join(missing)} must be set.")

    return FtOAuthConfig(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scopes=scopes,
    )


def get_ft_state_secret() -> str:
    value = os.getenv("FT_STATE_SECRET")
    if value is None or value.strip() == "":
        raise ConfigError("FT_STATE_SECRET is not set.")
    return value
