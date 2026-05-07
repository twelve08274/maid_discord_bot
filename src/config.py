import importlib
import os
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType

try:
    dotenv_module: ModuleType | None = importlib.import_module("dotenv")
except ModuleNotFoundError:
    dotenv_module = None


if dotenv_module is not None:
    load_dotenv = getattr(dotenv_module, "load_dotenv")
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

    assert client_id is not None
    assert client_secret is not None
    assert redirect_uri is not None

    return FtOAuthConfig(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scopes=scopes,
    )


def get_ft_state_secret() -> str:
    value = os.getenv("FT_STATE_SECRET")
    if value is None or value == "":
        raise ConfigError("FT_STATE_SECRET is not set.")
    return value


def get_ft_location_poll_interval_seconds() -> int:
    env_name = "FT_LOCATION_POLL_INTERVAL_SECONDS"
    value = os.getenv(env_name, "300")
    try:
        interval = int(value)
    except ValueError as error:
        message = f"{env_name} must be an integer."
        raise ConfigError(message) from error

    if interval <= 0:
        raise ConfigError(f"{env_name} must be positive.")
    return interval


def get_daily_reward_timezone() -> str:
    return os.getenv("DAILY_REWARD_TIMEZONE", "Asia/Tokyo")


def get_openweather_api_key() -> str:
    value = os.getenv("OPENWEATHER_API_KEY")
    if value is None or value == "":
        raise ConfigError("OPENWEATHER_API_KEY is not set.")
    return value


def get_weather_default_location() -> str:
    value = os.getenv("WEATHER_DEFAULT_LOCATION")
    if value is None or value == "":
        raise ConfigError("WEATHER_DEFAULT_LOCATION is not set.")
    return value


def get_oauth_web_host() -> str:
    return os.getenv("OAUTH_WEB_HOST", "0.0.0.0")


def get_oauth_web_port() -> int:
    env_name = "OAUTH_WEB_PORT"
    value = os.getenv(env_name, "8000")
    try:
        port = int(value)
    except ValueError as error:
        message = f"{env_name} must be an integer."
        raise ConfigError(message) from error

    if port <= 0 or port > 65535:
        raise ConfigError(f"{env_name} must be between 1 and 65535.")
    return port
