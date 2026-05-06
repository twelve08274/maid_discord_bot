import discord
from discord.ext import commands

from src.database.connection import get_connection
from src.database.schema import initialize_database
from src.services.neko import (
    NEKO_REPLY,
    NEKO_UNLOCK_MESSAGE,
    claim_neko,
)


def register_neko_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="neko",
        description="Call a neko once per day.",
    )
    async def neko(interaction: discord.Interaction) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            result = claim_neko(connection, interaction.user.id)

        await interaction.response.send_message(NEKO_REPLY)

        if not result.achievement_unlocked:
            return

        try:
            await interaction.user.send(NEKO_UNLOCK_MESSAGE)
        except (discord.Forbidden, discord.HTTPException):
            await interaction.followup.send(NEKO_UNLOCK_MESSAGE)
