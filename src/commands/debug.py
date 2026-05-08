import discord
from discord import app_commands
from discord.ext import commands

from src.database.connection import get_connection
from src.database.repositories.access import (
    get_guild_by_name,
    is_registered_user,
    join_user_guild,
    leave_user_guild,
)
from src.database.repositories.users import (
    set_user_level_by_discord_id,
    set_user_mood_by_discord_id,
)
from src.database.schema import initialize_database


GUILD_CHOICES = [
    app_commands.Choice(name="smash", value="smash"),
    app_commands.Choice(name="poker", value="poker"),
    app_commands.Choice(name="study", value="study"),
    app_commands.Choice(name="food", value="food"),
]

GUILD_ACTION_CHOICES = [
    app_commands.Choice(name="join", value="join"),
    app_commands.Choice(name="leave", value="leave"),
]

MOOD_CHOICES = [
    app_commands.Choice(name="happy", value="happy"),
    app_commands.Choice(name="normal", value="normal"),
    app_commands.Choice(name="tired", value="tired"),
    app_commands.Choice(name="sleepy", value="sleepy"),
]

MOOD_STAMINA = {
    "happy": 100,
    "normal": 50,
    "tired": 30,
    "sleepy": 10,
}


def register_debug_commands(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="debug-level",
        description="Set your level for local debugging.",
    )
    @app_commands.describe(level="Level to set for your character.")
    async def debug_level(
        interaction: discord.Interaction,
        level: app_commands.Range[int, 1, 100],
    ) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            set_user_level_by_discord_id(
                connection,
                interaction.user.id,
                int(level),
            )

        await interaction.response.send_message(
            f"Debug level set to {int(level)}.",
            ephemeral=True,
        )

    @bot.tree.command(
        name="debug-mood",
        description="Set your mood for local debugging.",
    )
    @app_commands.describe(mood="Mood to set for your character.")
    @app_commands.choices(mood=MOOD_CHOICES)
    async def debug_mood(
        interaction: discord.Interaction,
        mood: app_commands.Choice[str],
    ) -> None:
        stamina = MOOD_STAMINA[mood.value]
        with get_connection() as connection:
            initialize_database(connection)
            set_user_mood_by_discord_id(
                connection,
                interaction.user.id,
                mood.value,
                stamina,
            )

        await interaction.response.send_message(
            f"Debug mood set to {mood.value}.",
            ephemeral=True,
        )

    @bot.tree.command(
        name="debug-guild",
        description="Set your guild membership for local debugging.",
    )
    @app_commands.describe(
        action="Whether to join or leave the guild.",
        guild="Guild to update.",
    )
    @app_commands.choices(action=GUILD_ACTION_CHOICES, guild=GUILD_CHOICES)
    async def debug_guild(
        interaction: discord.Interaction,
        action: app_commands.Choice[str],
        guild: app_commands.Choice[str],
    ) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            if not is_registered_user(connection, interaction.user.id):
                await interaction.response.send_message(
                    "You are not registered yet. Use /register first.",
                    ephemeral=True,
                )
                return

            guild_row = get_guild_by_name(connection, guild.value)
            if guild_row is None:
                await interaction.response.send_message(
                    f"Unknown guild: {guild.value}",
                    ephemeral=True,
                )
                return

            if action.value == "join":
                changed = join_user_guild(
                    connection,
                    interaction.user.id,
                    guild.value,
                )
                message = (
                    f"Joined {guild_row['display_name']}."
                    if changed
                    else f"Already in {guild_row['display_name']}."
                )
            else:
                changed = leave_user_guild(
                    connection,
                    interaction.user.id,
                    guild.value,
                )
                message = (
                    f"Left {guild_row['display_name']}."
                    if changed
                    else f"Not in {guild_row['display_name']}."
                )

        await interaction.response.send_message(message, ephemeral=True)
