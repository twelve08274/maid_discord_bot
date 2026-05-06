import discord
from discord.ext import commands

from maid_discord_bot.config import ConfigError
from maid_discord_bot.services.ft_api import create_authorization_url
from maid_discord_bot.services.oauth_state import create_oauth_state


def create_register_authorization_url(discord_user_id: int) -> str:
    state = create_oauth_state(discord_user_id)
    return create_authorization_url(state)


def build_register_message(authorization_url: str) -> str:
    return (
        "Open this URL to authenticate with 42:\n"
        f"{authorization_url}\n\n"
        "The link expires in 10 minutes."
    )


def register_register_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="register",
        description="Start 42 account authentication.",
    )
    async def register(interaction: discord.Interaction) -> None:
        try:
            authorization_url = create_register_authorization_url(
                interaction.user.id,
            )
        except ConfigError as error:
            await interaction.response.send_message(
                f"Registration is not configured yet: {error}",
                ephemeral=True,
            )
            return

        await interaction.response.send_message(
            build_register_message(authorization_url),
            ephemeral=True,
        )
