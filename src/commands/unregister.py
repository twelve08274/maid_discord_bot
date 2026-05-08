import discord
from discord.ext import commands

from src.database.connection import get_connection
from src.database.repositories.users import delete_user_by_discord_id


def register_unregister_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="unregister",
        description="Delete your account and all associated data.",
    )
    async def unregister(interaction: discord.Interaction) -> None:
        with get_connection() as connection:
            deleted = delete_user_by_discord_id(
                connection, interaction.user.id
            )

        if not deleted:
            await interaction.response.send_message(
                "登録情報が見つかりません。",
                ephemeral=True,
            )
            return

        await interaction.response.send_message(
            "退会しました。すべてのデータを削除しました。",
            ephemeral=True,
        )
