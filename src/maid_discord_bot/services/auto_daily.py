import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from maid_discord_bot.config import get_daily_reward_timezone
from maid_discord_bot.database.repositories.daily_claims import (
    create_daily_claim,
)
from maid_discord_bot.database.repositories.ft_links import (
    LinkedFtAccount,
    update_ft_tokens,
)
from maid_discord_bot.database.repositories.ft_location_rewards import (
    create_ft_location_reward,
)
from maid_discord_bot.services.exp import ExpResult, add_exp
from maid_discord_bot.services.ft_api import (
    FtLocation,
    fetch_active_location,
    refresh_access_token,
)


AUTO_DAILY_EXP = 10
TOKEN_REFRESH_MARGIN = timedelta(minutes=5)


@dataclass(frozen=True)
class AutoDailyRewardResult:
    account: LinkedFtAccount
    location: FtLocation
    exp_gained: int
    exp_result: ExpResult
    claim_date: str


async def check_and_reward_auto_daily(
    connection: sqlite3.Connection,
    account: LinkedFtAccount,
) -> AutoDailyRewardResult | None:
    access_token = await _ensure_access_token(connection, account)
    location = await fetch_active_location(access_token, account.ft_login)
    if location is None:
        return None

    claim_date = _claim_date(location.begin_at)
    claimed_daily = create_daily_claim(
        connection,
        user_id=account.user_id,
        claim_date=claim_date,
        source="auto",
        exp_gained=AUTO_DAILY_EXP,
    )
    if not claimed_daily:
        return None

    exp_result = add_exp(connection, account.user_id, AUTO_DAILY_EXP)
    create_ft_location_reward(
        connection,
        user_id=account.user_id,
        ft_location_id=location.id,
        ft_login=account.ft_login,
        host=location.host,
        begin_at=location.begin_at,
        exp_gained=AUTO_DAILY_EXP,
    )
    return AutoDailyRewardResult(
        account=account,
        location=location,
        exp_gained=AUTO_DAILY_EXP,
        exp_result=exp_result,
        claim_date=claim_date,
    )


async def _ensure_access_token(
    connection: sqlite3.Connection,
    account: LinkedFtAccount,
) -> str:
    if account.token_expires_at > datetime.now(UTC) + TOKEN_REFRESH_MARGIN:
        return account.access_token

    token = await refresh_access_token(account.refresh_token)
    update_ft_tokens(
        connection,
        user_id=account.user_id,
        access_token=token.access_token,
        refresh_token=token.refresh_token,
        token_expires_at=token.expires_at,
    )
    return token.access_token


def _claim_date(begin_at: datetime) -> str:
    reward_timezone = _get_reward_timezone()
    return begin_at.astimezone(reward_timezone).date().isoformat()


def _get_reward_timezone() -> timezone | ZoneInfo:
    timezone_name = get_daily_reward_timezone()
    try:
        return ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError:
        if timezone_name == "Asia/Tokyo":
            return timezone(timedelta(hours=9))
        raise
