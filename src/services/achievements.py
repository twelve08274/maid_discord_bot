import logging
import sqlite3
from typing import Any

from ..database.repositories.achievements import (
    get_achievement,
    unlock_achievement,
)
from ..database.repositories.users import get_or_create_user_id
from .exp import add_exp


logger = logging.getLogger(__name__)


def apply_achievement_rewards(
    connection: sqlite3.Connection,
    user_id: int,
    achievement: sqlite3.Row,
) -> None:
    reward_exp = int(achievement["reward_exp"])
    reward_affection = int(achievement["reward_affection"])
    reward_stamina = int(achievement["reward_stamina"])

    if reward_exp > 0:
        add_exp(connection, user_id, reward_exp)

    if reward_affection > 0 or reward_stamina > 0:
        connection.execute(
            """
            UPDATE users
            SET
                affection = affection + ?,
                stamina = MIN(100, stamina + ?),
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (reward_affection, reward_stamina, user_id),
        )
        connection.commit()


async def send_achievement_dm(
    bot: Any,
    discord_user_id: int,
    achievement: sqlite3.Row,
) -> bool:
    import discord

    try:
        user = await bot.fetch_user(discord_user_id)
        embed = discord.Embed(
            title="Achievement unlocked!",
            description=(
                f"**{achievement['name']}**\n{achievement['description']}"
            ),
            color=0xF1C40F,
        )

        rewards = []
        if int(achievement["reward_exp"]) > 0:
            rewards.append(f"EXP +{achievement['reward_exp']}")
        if int(achievement["reward_affection"]) > 0:
            rewards.append(f"Affection +{achievement['reward_affection']}")
        if int(achievement["reward_stamina"]) > 0:
            rewards.append(f"Stamina +{achievement['reward_stamina']}")

        if rewards:
            embed.add_field(
                name="Reward",
                value="\n".join(rewards),
                inline=False,
            )

        await user.send(embed=embed)
        return True
    except (discord.Forbidden, discord.HTTPException):
        logger.warning(
            "Failed to send achievement DM to user %s for %s.",
            discord_user_id,
            achievement["code"],
        )
        return False


async def grant_achievement(
    bot: Any,
    connection: sqlite3.Connection,
    discord_user_id: int,
    achievement_code: str,
) -> bool:
    achievement = get_achievement(connection, achievement_code)
    if achievement is None:
        return False

    user_id = get_or_create_user_id(connection, discord_user_id)
    if not unlock_achievement(connection, user_id, achievement_code):
        return False

    apply_achievement_rewards(connection, user_id, achievement)
    await send_achievement_dm(bot, discord_user_id, achievement)
    return True
