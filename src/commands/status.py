from pathlib import Path

import discord
from discord.ext import commands

from src.database.connection import get_connection
from src.database.repositories.ft_links import get_ft_link
from src.database.repositories.users import get_user_by_discord_id
from src.database.schema import initialize_database
from src.services.mood_service import (
    determine_mood,
    mood_asset_path,
    mood_display_name,
    mood_to_color,
)


def register_status_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="status",
        description="Show your character status.",
    )
    async def status(interaction: discord.Interaction) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            user = get_user_by_discord_id(connection, interaction.user.id)
            if user is None:
                await interaction.response.send_message(
                    "You are not registered yet. Use /register first.",
                    ephemeral=True,
                )
                return

            ft_link = get_ft_link(connection, int(user["id"]))

        level = int(user["level"])
        exp = int(user["exp"])
        stamina = int(user["stamina"])
        affection = int(user["affection"])
        auto_daily_enabled = bool(user["auto_daily_enabled"])
        last_login = user["last_login_date"] or "None"
        required_exp = level * 100

        mood = determine_mood(stamina)
        embed = discord.Embed(
            title=f"{interaction.user.display_name}'s Status",
            color=mood_to_color(mood),
        )
        embed.add_field(name="Level", value=str(level), inline=True)
        embed.add_field(
            name="EXP",
            value=f"{exp} / {required_exp}",
            inline=True,
        )
        embed.add_field(name="Stamina", value=str(stamina), inline=True)
        embed.add_field(
            name="Affection",
            value=str(affection),
            inline=True,
        )
        embed.add_field(
            name="Mood",
            value=mood_display_name(mood),
            inline=True,
        )
        embed.add_field(
            name="42",
            value="Linked" if ft_link is not None else "Not linked",
            inline=True,
        )
        embed.add_field(
            name="Auto Daily",
            value="ON" if auto_daily_enabled else "OFF",
            inline=True,
        )
        embed.add_field(
            name="Last 42 Login",
            value=str(last_login),
            inline=False,
        )
        embed.set_footer(text="Keep going.")

        image_path = Path(mood_asset_path(mood))
        if image_path.exists():
            file = discord.File(str(image_path), filename="character.png")
            embed.set_thumbnail(url="attachment://character.png")
            await interaction.response.send_message(embed=embed, file=file)
            return

        await interaction.response.send_message(embed=embed)
