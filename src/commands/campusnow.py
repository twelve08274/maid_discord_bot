import discord
from discord import app_commands
from discord.ext import commands

from src.config import ConfigError
from src.services.campus_now_service import (
    CLUSTERS,
    CampusAll,
    ClusterNow,
    get_campus_all,
    get_campus_now,
    get_cluster_now,
)


CLUSTER_CHOICES = [
    app_commands.Choice(name=cluster_name, value=cluster_name)
    for cluster_name in CLUSTERS
]


def _campus_embed(campus_now) -> discord.Embed:
    embed = discord.Embed(
        title="\U0001f4cd Campus",
        color=discord.Color.from_rgb(88, 166, 255),
    )
    embed.add_field(
        name="\u73fe\u5728\u30ed\u30b0\u30a4\u30f3\u4e2d",
        value=f"{campus_now.active_count}\u4eba",
        inline=True,
    )
    embed.add_field(
        name="\u5168\u4f53\u306e\u5e2d\u6570",
        value=f"{campus_now.pc_count}\u5e2d",
        inline=True,
    )
    embed.add_field(
        name="\u6df7\u96d1\u7387",
        value=f"{campus_now.crowd_percent:.1f}%",
        inline=True,
    )
    embed.add_field(
        name="\u72b6\u6cc1",
        value=campus_now.comment,
        inline=False,
    )
    embed.set_footer(
        text="\u4eba\u6570\u306e\u307f\u3092\u8868\u793a\u3057\u3066"
        "\u3044\u307e\u3059\u3002\u500b\u4eba\u306e\u4f4d\u7f6e"
        "\u60c5\u5831\u306f\u8868\u793a\u3057\u307e\u305b\u3093\u3002"
    )
    return embed


def _cluster_embed(cluster_now: ClusterNow) -> discord.Embed:
    embed = discord.Embed(
        title=f"\U0001f4cd Campus Now: {cluster_now.cluster_name}",
        color=discord.Color.from_rgb(88, 166, 255),
    )
    embed.add_field(
        name="\u73fe\u5728\u30ed\u30b0\u30a4\u30f3\u4e2d",
        value=f"{cluster_now.active_count}\u4eba",
        inline=True,
    )
    embed.add_field(
        name="cluster\u5e2d\u6570",
        value=f"{cluster_now.seat_count}\u5e2d",
        inline=True,
    )
    embed.add_field(
        name="\u6df7\u96d1\u7387",
        value=f"{cluster_now.crowd_percent:.1f}%",
        inline=True,
    )
    embed.add_field(
        name="\u72b6\u6cc1",
        value=cluster_now.comment,
        inline=False,
    )
    embed.set_footer(
        text="\u4eba\u6570\u306e\u307f\u3092\u8868\u793a\u3057\u3066"
        "\u3044\u307e\u3059\u3002\u500b\u4eba\u306e\u4f4d\u7f6e"
        "\u60c5\u5831\u306f\u8868\u793a\u3057\u307e\u305b\u3093\u3002"
    )
    return embed


def _summary_card_value(
    *,
    active_count: int,
    seat_count: int,
    crowd_percent: float,
) -> str:
    return (
        "\u4eba\u6570/\u5e2d\u6570: "
        f"**{active_count} / {seat_count}**\n"
        "\u200b\u6df7\u96d1\u7387: "
        f"**{crowd_percent:.1f}%**"
    )


def _campus_all_embed(campus_all: CampusAll) -> discord.Embed:
    embed = discord.Embed(
        title="\U0001f4cd Campus All",
        color=discord.Color.from_rgb(88, 166, 255),
    )
    embed.add_field(
        name="Campus",
        value=_summary_card_value(
            active_count=campus_all.campus.active_count,
            seat_count=campus_all.campus.pc_count,
            crowd_percent=campus_all.campus.crowd_percent,
        ),
        inline=False,
    )
    for index, cluster_now in enumerate(campus_all.clusters):
        if index > 0 and index % 3 == 0:
            embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(
            name=f"{cluster_now.cluster_id}/{cluster_now.cluster_name}",
            value=_summary_card_value(
                active_count=cluster_now.active_count,
                seat_count=cluster_now.seat_count,
                crowd_percent=cluster_now.crowd_percent,
            ),
            inline=True,
        )
    embed.set_footer(
        text="\u4eba\u6570\u306e\u307f\u3092\u8868\u793a\u3057\u3066"
        "\u3044\u307e\u3059\u3002\u500b\u4eba\u306e\u4f4d\u7f6e"
        "\u60c5\u5831\u306f\u8868\u793a\u3057\u307e\u305b\u3093\u3002"
    )
    return embed


async def _send_fetch_error(interaction: discord.Interaction) -> None:
    await interaction.followup.send(
        "\u0042 API\u304b\u3089\u73fe\u5728\u306e\u6df7\u96d1"
        "\u72b6\u6cc1\u3092\u53d6\u5f97\u3067\u304d\u307e\u305b"
        "\u3093\u3067\u3057\u305f\u3002\u5c11\u3057\u6642\u9593"
        "\u3092\u304a\u3044\u3066\u3082\u3046\u4e00\u5ea6\u304a"
        "\u8a66\u3057\u304f\u3060\u3055\u3044\u3002",
        ephemeral=True,
    )


def register_campusnow_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="campus",
        description="Show current 42Tokyo campus crowding.",
    )
    async def campus(interaction: discord.Interaction) -> None:
        await interaction.response.defer()

        try:
            campus_now = await get_campus_now()
        except ConfigError as error:
            await interaction.followup.send(
                f"Campus Now is not configured yet: {error}",
                ephemeral=True,
            )
            return
        except Exception:
            await _send_fetch_error(interaction)
            return

        await interaction.followup.send(embed=_campus_embed(campus_now))

    @bot.tree.command(
        name="campusnow",
        description="Show current 42Tokyo cluster crowding.",
    )
    @app_commands.describe(cluster="Cluster name.")
    @app_commands.choices(cluster=CLUSTER_CHOICES)
    async def campusnow(
        interaction: discord.Interaction,
        cluster: app_commands.Choice[str],
    ) -> None:
        await interaction.response.defer()

        try:
            cluster_now = await get_cluster_now(cluster.value)
        except ConfigError as error:
            await interaction.followup.send(
                f"Campus Now is not configured yet: {error}",
                ephemeral=True,
            )
            return
        except Exception:
            await _send_fetch_error(interaction)
            return

        await interaction.followup.send(embed=_cluster_embed(cluster_now))

    @bot.tree.command(
        name="campusall",
        description="Show current 42Tokyo campus and cluster crowding.",
    )
    async def campusall(interaction: discord.Interaction) -> None:
        await interaction.response.defer()

        try:
            campus_all = await get_campus_all()
        except ConfigError as error:
            await interaction.followup.send(
                f"Campus Now is not configured yet: {error}",
                ephemeral=True,
            )
            return
        except Exception:
            await _send_fetch_error(interaction)
            return

        await interaction.followup.send(embed=_campus_all_embed(campus_all))
