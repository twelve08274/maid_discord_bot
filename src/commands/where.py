import io
from datetime import UTC, datetime

import discord
from discord import app_commands
from discord.ext import commands

from src.database.connection import get_connection
from src.database.repositories.ft_links import (
    get_ft_link_by_login,
    update_ft_tokens,
)
from src.services.auto_daily import TOKEN_REFRESH_MARGIN
from src.services.ft_api import fetch_active_location, refresh_access_token
from src.services.seat_map import (
    CLUSTER_META,
    build_description,
    parse_host,
    render_seat_map_gif,
)


def register_where_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="where",
        description="登録済みユーザーの現在の席を表示します。",
    )
    @app_commands.describe(login="42のログイン名")
    async def where(interaction: discord.Interaction, login: str) -> None:
        await interaction.response.defer(ephemeral=True)

        with get_connection() as connection:
            account = get_ft_link_by_login(connection, login)
            if account is None:
                await interaction.followup.send(
                    f"`{login}` は登録されていません。",
                    ephemeral=True,
                )
                return

            expires_soon = (
                account.token_expires_at
                <= datetime.now(UTC) + TOKEN_REFRESH_MARGIN
            )
            if expires_soon:
                token = await refresh_access_token(account.refresh_token)
                update_ft_tokens(
                    connection,
                    user_id=account.user_id,
                    access_token=token.access_token,
                    refresh_token=token.refresh_token,
                    token_expires_at=token.expires_at,
                )
                access_token = token.access_token
            else:
                access_token = account.access_token

        try:
            location = await fetch_active_location(
                access_token, account.ft_login
            )
        except Exception:
            await interaction.followup.send(
                "場所の取得に失敗しました。",
                ephemeral=True,
            )
            return

        if location is None or location.host is None:
            await interaction.followup.send(
                f"`{login}` は現在キャンパスにいません。",
                ephemeral=True,
            )
            return

        host = location.host
        try:
            cluster_id, row, seat = parse_host(host)
        except ValueError:
            await interaction.followup.send(
                f"`{login}` は **{host}** にいます。",
                ephemeral=True,
            )
            return

        if cluster_id not in CLUSTER_META:
            await interaction.followup.send(
                f"`{login}` は **{host}** にいます。（マップ未対応クラスタ）",
                ephemeral=True,
            )
            return

        gif_bytes = render_seat_map_gif(cluster_id, row, seat)
        description = build_description(cluster_id, row, seat, login)

        embed = discord.Embed(
            title=f"{login} の現在地",
            description=description,
            color=discord.Color.from_rgb(243, 139, 168),
        )
        embed.set_footer(text=f"ホスト: {host}")
        embed.set_image(url="attachment://seat_map.gif")

        file = discord.File(io.BytesIO(gif_bytes), filename="seat_map.gif")
        await interaction.followup.send(
            embed=embed,
            file=file,
            ephemeral=True,
        )
