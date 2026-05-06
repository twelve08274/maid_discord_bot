import discord
from discord.ext import commands

from .commands.ping import register_ping_command
from .commands.register import register_register_command
from .config import (
    get_discord_test_guild_id,
    get_discord_token,
)


class MaidBot(commands.Bot):
    async def setup_hook(self) -> None:
        register_ping_command(self)
        register_register_command(self)

        test_guild_id = get_discord_test_guild_id()
        if test_guild_id is None:
            await self.tree.sync()
            return

        guild = discord.Object(id=test_guild_id)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)


def create_bot() -> MaidBot:
    intents = discord.Intents.default()
    return MaidBot(command_prefix="!", intents=intents)


def run_bot() -> None:
    bot = create_bot()
    bot.run(get_discord_token())
