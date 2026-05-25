import discord
from discord.ext import commands

from src.database.connection import get_connection
from src.database.repositories.ft_links import delete_ft_link_for_discord_user
from src.database.schema import initialize_database


def register_unlink42_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="unlink42",
        description="Unlink your 42 account from this bot.",
    )
    async def unlink42(interaction: discord.Interaction) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            deleted = delete_ft_link_for_discord_user(
                connection,
                interaction.user.id,
            )

        if not deleted:
            await interaction.response.send_message(
                "No linked 42 account was found.",
                ephemeral=True,
            )
            return

        await interaction.response.send_message(
            "Your 42 account link has been removed.",
            ephemeral=True,
        )
