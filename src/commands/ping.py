import discord
from discord.ext import commands


def register_ping_command(bot: commands.Bot) -> None:
    @bot.tree.command(name="ping", description="Reply with pong!")
    async def ping(interaction: discord.Interaction) -> None:
        await interaction.response.send_message("pong!")
