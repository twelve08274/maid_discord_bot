import os
import discord
from discord.ext import commands

from maid_discord_bot.database.connection import get_connection
from maid_discord_bot.database.repositories.ft_links import get_ft_link
from maid_discord_bot.services.mood_service import (
    determine_mood,
    mood_display_name,
    mood_to_color,
    mood_asset_path,
)


def register_status_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="status",
        description="キャラクターのステータスを表示します",
    )
    async def status(interaction: discord.Interaction) -> None:
        discord_user_id = str(interaction.user.id)

        with get_connection() as connection:
            user_row = connection.execute(
                """
                SELECT id, level, exp, stamina, affection,
                       auto_daily_enabled, last_login_date
                FROM users
                WHERE discord_user_id = ?
                """,
                (discord_user_id,),
            ).fetchone()

            if user_row is None:
                await interaction.response.send_message(
                    "まだ登録されていません。/register で登録してください。",
                    ephemeral=True,
                )
                return

            ft_row = get_ft_link(connection, user_row["id"])

        level        = user_row["level"]
        exp          = user_row["exp"]
        stamina      = user_row["stamina"]
        affection    = user_row["affection"]
        auto_daily   = user_row["auto_daily_enabled"]
        last_login   = user_row["last_login_date"] or "なし"  # ← usersから取得
        required_exp = level * 100

        mood    = determine_mood(stamina)
        mood_jp = mood_display_name(mood)
        color   = mood_to_color(mood)

        ft_status = "連携済み ✅" if ft_row else "未連携 ❌"

        embed = discord.Embed(
            title=f"{interaction.user.display_name} のステータス",
            color=color,
        )
        embed.add_field(name="Level",         value=str(level),                        inline=False)
        embed.add_field(name="EXP",           value=f"{exp} / {required_exp}",         inline=True)
        embed.add_field(name="Stamina",       value=str(stamina),                      inline=True)
        embed.add_field(name="Affection",     value=str(affection),                    inline=True)
        embed.add_field(name="Mood",          value=mood_jp,                           inline=True)
        embed.add_field(name="42",            value=ft_status,                         inline=True)
        embed.add_field(name="Auto Daily",    value="ON ✅" if auto_daily else "OFF ❌", inline=True)
        embed.add_field(name="Last 42 Login", value=last_login,                        inline=False)
        embed.set_footer(text="今日もお疲れさまです")

        image_path = mood_asset_path(mood)
        if os.path.exists(image_path):
            file = discord.File(image_path, filename="character.png")
            embed.set_thumbnail(url="attachment://character.png")
            await interaction.response.send_message(embed=embed, file=file)
        else:
            await interaction.response.send_message(embed=embed)
