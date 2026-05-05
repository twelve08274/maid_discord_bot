import discord
from discord.ext import commands

from maid_discord_bot.config import ConfigError
from maid_discord_bot.services.ft_api import create_authorization_url
from maid_discord_bot.services.oauth_state import create_oauth_state


def register_register_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="register",
        description="Start 42 account authentication.",
    )
    async def register(interaction: discord.Interaction) -> None:
        try:
            state = create_oauth_state(interaction.user.id)
            authorization_url = create_authorization_url(state)
        except ConfigError as error:
            await interaction.response.send_message(
                f"Registration is not configured yet: {error}",
                ephemeral=True,
            )
            return

        await interaction.response.send_message(
            "Open this URL to authenticate with 42:\n"
            f"{authorization_url}\n\n"
            "The link expires in 10 minutes.",
            ephemeral=True,
        )
