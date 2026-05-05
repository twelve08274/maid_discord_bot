import base64
import hashlib
import hmac
import json
import time
from dataclasses import dataclass
from secrets import token_urlsafe
from maid_discord_bot.config import get_ft_state_secret


class OAuthStateError(ValueError):
    pass


@dataclass(frozen=True)
class OAuthState:
    discord_user_id: int
    issued_at: int
    nonce: str


def create_oauth_state(discord_user_id: int, secret: str | None = None) -> str:
    if secret is None:
        secret = get_ft_state_secret()

    payload = {
        "discord_user_id": discord_user_id,
        "iat": int(time.time()),
        "nonce": token_urlsafe(16),
    }
    payload_bytes = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    payload_part = _urlsafe_b64encode(payload_bytes)
    signature = _sign(payload_part, secret)
    return f"{payload_part}.{signature}"


def parse_oauth_state(
    state: str,
    secret: str | None = None,
    max_age_seconds: int = 600,
) -> OAuthState:
    if secret is None:
        secret = get_ft_state_secret()

    try:
        payload_part, signature = state.split(".", 1)
    except ValueError as error:
        raise OAuthStateError("Invalid OAuth state format.") from error

    expected = _sign(payload_part, secret)
    if not hmac.compare_digest(signature, expected):
        raise OAuthStateError("Invalid OAuth state signature.")

    try:
        payload = json.loads(_urlsafe_b64decode(payload_part))
        discord_user_id = int(payload["discord_user_id"])
        issued_at = int(payload["iat"])
        nonce = str(payload["nonce"])
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise OAuthStateError("Invalid OAuth state payload.") from error

    if int(time.time()) - issued_at > max_age_seconds:
        raise OAuthStateError("OAuth state has expired.")

    return OAuthState(
        discord_user_id=discord_user_id,
        issued_at=issued_at,
        nonce=nonce,
    )


def _sign(payload_part: str, secret: str) -> str:
    digest = hmac.new(
        secret.encode("utf-8"),
        payload_part.encode("ascii"),
        hashlib.sha256,
    ).digest()
    return _urlsafe_b64encode(digest)


def _urlsafe_b64encode(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode("ascii").rstrip("=")


def _urlsafe_b64decode(value: str) -> bytes:
    padding = "=" * (-len(value) % 4)
    return base64.urlsafe_b64decode(value + padding)
