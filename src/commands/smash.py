import discord
from discord.ext import commands

from src.database.connection import get_connection
from src.database.repositories.access import check_command_access
from src.database.schema import initialize_database


def register_smash_commands(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="smash-rate",
        description="Show Smash rate management.",
    )
    async def smash_rate(interaction: discord.Interaction) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            allowed, reason = check_command_access(
                connection,
                interaction.user.id,
                "smash-rate",
            )

        if not allowed:
            await interaction.response.send_message(
                reason,
                ephemeral=True,
            )
            return

        await interaction.response.send_message(
            "スマブラレート管理機能は準備中です。",
            ephemeral=True,
        )
