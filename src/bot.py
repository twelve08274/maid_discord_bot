import logging
from threading import Thread

import discord
import uvicorn
from discord.ext import commands

from .commands.achievements import register_achievements_command
from .commands.autodaily import register_autodaily_command
from .commands.ping import register_ping_command
from .commands.register import register_register_command
from .config import (
    get_discord_test_guild_id,
    get_discord_token,
    get_oauth_web_host,
    get_oauth_web_port,
)
from .scheduler import FtLocationAutoDailyScheduler


class OAuthWebServer:
    def __init__(self) -> None:
        self.server: uvicorn.Server | None = None
        self.thread: Thread | None = None

    def start(self) -> None:
        config = uvicorn.Config(
            "src.web.app:app",
            host=get_oauth_web_host(),
            port=get_oauth_web_port(),
            log_level="info",
        )
        self.server = uvicorn.Server(config)
        self.thread = Thread(target=self.server.run, daemon=True)
        self.thread.start()

    def stop(self) -> None:
        if self.server is not None:
            self.server.should_exit = True
        if self.thread is not None and self.thread.is_alive():
            self.thread.join(timeout=5)


class MaidBot(commands.Bot):
    auto_daily_scheduler: FtLocationAutoDailyScheduler

    async def setup_hook(self) -> None:
        register_ping_command(self)
        register_register_command(self)
        register_achievements_command(self)
        register_autodaily_command(self)
        self.auto_daily_scheduler = FtLocationAutoDailyScheduler(self)
        self.auto_daily_scheduler.start()

        test_guild_id = get_discord_test_guild_id()
        if test_guild_id is None:
            await self.tree.sync()
            return

        guild = discord.Object(id=test_guild_id)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

    async def close(self) -> None:
        if hasattr(self, "auto_daily_scheduler"):
            await self.auto_daily_scheduler.stop()
        await super().close()


def create_bot() -> MaidBot:
    intents = discord.Intents.default()
    return MaidBot(command_prefix="!", intents=intents)


def run_bot() -> None:
    logging.basicConfig(level=logging.INFO)
    oauth_web_server = OAuthWebServer()
    oauth_web_server.start()
    bot = create_bot()
    try:
        bot.run(get_discord_token())
    finally:
        oauth_web_server.stop()
