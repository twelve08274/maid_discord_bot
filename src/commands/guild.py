import discord
from discord import app_commands
from discord.ext import commands

from src.database.connection import get_connection
from src.database.repositories.access import (
    check_command_access,
    get_user_guilds,
    list_guilds,
)
from src.database.schema import initialize_database


def register_guild_command(bot: commands.Bot) -> None:
    guild_group = app_commands.Group(
        name="guild",
        description="Show guild information.",
    )

    @guild_group.command(
        name="list",
        description="Show available guilds.",
    )
    async def guild_list(interaction: discord.Interaction) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            guilds = list_guilds(connection)

        guild_list = "\n".join(
            f"- {guild['display_name']} (`{guild['name']}`)"
            for guild in guilds
        )
        await interaction.response.send_message(
            f"Available guilds:\n{guild_list}",
            ephemeral=True,
        )

    @guild_group.command(
        name="my",
        description="Show your guild memberships.",
    )
    async def guild_my(interaction: discord.Interaction) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            allowed, reason = check_command_access(
                connection,
                interaction.user.id,
                "guild-my",
            )
            if not allowed:
                await interaction.response.send_message(
                    reason,
                    ephemeral=True,
                )
                return

            guilds = get_user_guilds(connection, interaction.user.id)

        if not guilds:
            await interaction.response.send_message(
                "You are not in any guilds yet.",
                ephemeral=True,
            )
            return

        guild_list = "\n".join(
            f"- {guild['display_name']} (`{guild['name']}`)"
            for guild in guilds
        )
        await interaction.response.send_message(
            f"Your guilds:\n{guild_list}",
            ephemeral=True,
        )

    bot.tree.add_command(guild_group)
