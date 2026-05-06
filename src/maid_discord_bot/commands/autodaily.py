import discord
from discord import app_commands
from discord.ext import commands

from maid_discord_bot.database.connection import get_connection
from maid_discord_bot.database.repositories.ft_links import (
    get_ft_link_for_discord_user,
)
from maid_discord_bot.database.repositories.users import set_auto_daily_enabled
from maid_discord_bot.database.schema import initialize_database


def register_autodaily_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="autodaily",
        description=(
            "Enable or disable automatic 42 login daily rewards."
        ),
    )
    @app_commands.describe(
        enabled="Whether automatic daily rewards are enabled.",
    )
    async def autodaily(
        interaction: discord.Interaction,
        enabled: bool,
    ) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            ft_link = get_ft_link_for_discord_user(
                connection,
                interaction.user.id,
            )
            if ft_link is None:
                await interaction.response.send_message(
                    "42 account is not linked yet. Use /register first.",
                    ephemeral=True,
                )
                return

            set_auto_daily_enabled(connection, interaction.user.id, enabled)

        status = "enabled" if enabled else "disabled"
        await interaction.response.send_message(
            f"Automatic 42 login daily rewards are now {status}.",
            ephemeral=True,
        )
