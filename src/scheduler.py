import asyncio
import logging

import discord
import httpx

from src.config import (
    ConfigError,
    get_ft_location_poll_interval_seconds,
)
from src.database.connection import get_connection
from src.database.repositories.ft_links import (
    list_auto_daily_ft_links,
)
from src.database.repositories.ft_location_rewards import (
    mark_ft_location_reward_notified,
)
from src.database.schema import initialize_database
from src.services.auto_daily import (
    AutoDailyRewardResult,
    check_and_reward_auto_daily,
)


logger = logging.getLogger(__name__)


class FtLocationAutoDailyScheduler:
    def __init__(self, bot: discord.Client) -> None:
        self.bot = bot
        self._task: asyncio.Task[None] | None = None

    def start(self) -> None:
        if self._task is not None and not self._task.done():
            return
        self._task = asyncio.create_task(self._run_forever())

    async def stop(self) -> None:
        if self._task is None:
            return
        self._task.cancel()
        try:
            await self._task
        except asyncio.CancelledError:
            pass

    async def _run_forever(self) -> None:
        await self.bot.wait_until_ready()
        try:
            interval_seconds = get_ft_location_poll_interval_seconds()
        except ConfigError as error:
            logger.warning("42 auto daily scheduler is disabled: %s", error)
            return

        while not self.bot.is_closed():
            await self.run_once()
            await asyncio.sleep(interval_seconds)

    async def run_once(self) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            accounts = list_auto_daily_ft_links(connection)

            for account in accounts:
                try:
                    result = await check_and_reward_auto_daily(
                        connection,
                        account,
                    )
                except httpx.HTTPStatusError as error:
                    logger.warning(
                        "42 location check failed for %s: HTTP %s",
                        account.ft_login,
                        error.response.status_code,
                    )
                    continue
                except httpx.HTTPError:
                    logger.exception(
                        "42 location check failed for %s",
                        account.ft_login,
                    )
                    continue
                except Exception:
                    logger.exception(
                        "Auto daily check failed for %s",
                        account.ft_login,
                    )
                    continue

                if result is None:
                    continue

                try:
                    notified = await self._notify_reward(result)
                except discord.HTTPException:
                    logger.exception(
                        "Failed to send auto daily notification to user %s",
                        result.account.discord_user_id,
                    )
                    notified = False
                if notified:
                    mark_ft_location_reward_notified(
                        connection,
                        result.account.user_id,
                        result.location.id,
                    )

    async def _notify_reward(self, result: AutoDailyRewardResult) -> bool:
        user = await self.bot.fetch_user(result.account.discord_user_id)
        host_text = (
            f" at {result.location.host}"
            if result.location.host
            else ""
        )
        level_text = ""
        if result.exp_result.leveled_up:
            level_text = (
                f"\nLevel up: Lv.{result.exp_result.previous_level}"
                f" -> Lv.{result.exp_result.level}"
            )

        await user.send(
            "42 login detected"
            f"{host_text}.\n"
            f"Daily reward: EXP +{result.exp_gained}\n"
            f"Current: Lv.{result.exp_result.level} "
            f"EXP {result.exp_result.exp}/"
            f"{result.exp_result.level * 100}"
            f"{level_text}"
        )
        return True
