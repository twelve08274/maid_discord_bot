import discord
from discord.ext import commands

from maid_discord_bot.database.connection import get_connection
from maid_discord_bot.database.repositories.achievements import (
    count_unlocked_visible_achievements,
    count_visible_achievements,
    get_unlocked_achievements_for_user,
)
from maid_discord_bot.database.repositories.users import get_or_create_user_id
from maid_discord_bot.database.schema import initialize_database


def register_achievements_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="achievements",
        description="Show your unlocked achievements.",
    )
    async def achievements(interaction: discord.Interaction) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            user_id = get_or_create_user_id(connection, interaction.user.id)
            unlocked = get_unlocked_achievements_for_user(
                connection,
                user_id,
            )
            total_count = count_visible_achievements(connection)
            unlocked_count = count_unlocked_visible_achievements(
                connection,
                user_id,
            )

        embed = discord.Embed(
            title="Achievement List",
            color=0xF1C40F,
        )

        if unlocked:
            for achievement in unlocked:
                embed.add_field(
                    name=f"Unlocked: {achievement['name']}",
                    value=(
                        f"{achievement['description']}\n"
                        f"Unlocked at: {achievement['unlocked_at']}"
                    ),
                    inline=False,
                )
        else:
            embed.description = "No achievements unlocked yet."

        embed.set_footer(text=f"Unlocked: {unlocked_count} / {total_count}")
        await interaction.response.send_message(embed=embed, ephemeral=True)
