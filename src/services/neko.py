import sqlite3
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from ..database.repositories.achievements import unlock_achievement
from ..database.repositories.neko_claims import insert_neko_claim
from ..database.repositories.users import (
    get_or_create_user_id,
    get_user_by_discord_id,
    update_neko_streak,
)


NEKO_ACHIEVEMENT_CODE = "neko_7_days"
NEKO_REPLY = "nya"
NEKO_UNLOCK_MESSAGE = (
    "Hidden achievement unlocked!\n\n"
    "Chosen by the Cat\n"
    "Ran /neko for 7 consecutive days."
)
TOKYO_TIMEZONE = ZoneInfo("Asia/Tokyo")


@dataclass(frozen=True)
class NekoClaimResult:
    user_id: int
    claimed: bool
    streak: int
    achievement_unlocked: bool


def today_in_tokyo() -> date:
    return datetime.now(TOKYO_TIMEZONE).date()


def calculate_next_neko_streak(
    last_neko_date: str | None,
    current_streak: int,
    today: date,
) -> int:
    if last_neko_date == today.isoformat():
        return current_streak

    yesterday = today - timedelta(days=1)
    if last_neko_date == yesterday.isoformat():
        return current_streak + 1

    return 1


def claim_neko(
    connection: sqlite3.Connection,
    discord_user_id: int,
    today: date | None = None,
) -> NekoClaimResult:
    if today is None:
        today = today_in_tokyo()

    today_str = today.isoformat()
    user_id = get_or_create_user_id(connection, discord_user_id)
    user = get_user_by_discord_id(connection, discord_user_id)
    if user is None:
        raise ValueError(f"User {discord_user_id} was not created.")

    current_streak = int(user["neko_streak"] or 0)
    last_neko_date = user["last_neko_date"]
    if last_neko_date == today_str:
        return NekoClaimResult(
            user_id=user_id,
            claimed=False,
            streak=current_streak,
            achievement_unlocked=False,
        )

    if not insert_neko_claim(connection, user_id, today_str):
        return NekoClaimResult(
            user_id=user_id,
            claimed=False,
            streak=current_streak,
            achievement_unlocked=False,
        )

    new_streak = calculate_next_neko_streak(
        last_neko_date,
        current_streak,
        today,
    )
    update_neko_streak(connection, user_id, new_streak, today_str)

    achievement_unlocked = False
    if new_streak >= 7:
        achievement_unlocked = unlock_achievement(
            connection,
            user_id,
            NEKO_ACHIEVEMENT_CODE,
        )

    return NekoClaimResult(
        user_id=user_id,
        claimed=True,
        streak=new_streak,
        achievement_unlocked=achievement_unlocked,
    )
