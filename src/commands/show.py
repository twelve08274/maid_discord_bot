from pathlib import Path

import discord
from discord.ext import commands

from src.database.connection import get_connection
from src.database.repositories.users import get_user_by_discord_id
from src.services.mood_service import (
    character_image_path,
    determine_mood,
    level_group,
    mood_display_name,
)


def register_show_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="show",
        description="キャラクターの立ち絵を表示します",
    )
    async def show(interaction: discord.Interaction) -> None:
        with get_connection() as connection:
            user = get_user_by_discord_id(connection, interaction.user.id)
            if user is None:
                await interaction.response.send_message(
                    "まだ登録されていません。/register を使ってください。",
                    ephemeral=True,
                )
                return

        level = int(user["level"])
        stamina = int(user["stamina"])
        mood = determine_mood(stamina)

        path = Path(character_image_path(level, mood))

        if not path.exists():
            await interaction.response.send_message(
                f"画像が見つかりませんでした。\n"
                f"（探した場所: `{path}`）\n"
                f"`assets/` フォルダに画像を配置してください。",
                ephemeral=True,
            )
            return

        group = level_group(level)
        mood_jp = mood_display_name(mood)

        file = discord.File(str(path), filename="character.png")
        embed = discord.Embed(
            title=f"{interaction.user.display_name} のキャラクター",
            description=f"レベル帯: **{group}**　Mood: **{mood_jp}**",
            color=0x7EC8E3,
        )
        embed.set_image(url="attachment://character.png")
        await interaction.response.send_message(embed=embed, file=file)
