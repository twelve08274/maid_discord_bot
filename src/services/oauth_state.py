import base64
import hashlib
import hmac
import json
import time
from dataclasses import dataclass

from ..config import get_ft_state_secret


STATE_TTL_SECONDS = 600


class OAuthStateError(ValueError):
    pass


@dataclass(frozen=True)
class OAuthState:
    discord_user_id: int
    issued_at: int


def _sign(payload: bytes, secret: str) -> str:
    digest = hmac.new(secret.encode(), payload, hashlib.sha256).digest()
    return base64.urlsafe_b64encode(digest).decode().rstrip("=")


def _encode(payload: bytes) -> str:
    return base64.urlsafe_b64encode(payload).decode().rstrip("=")


def _decode(value: str) -> bytes:
    padding = "=" * (-len(value) % 4)
    return base64.urlsafe_b64decode(value + padding)


def create_oauth_state(discord_user_id: int) -> str:
    payload = json.dumps(
        {
            "discord_user_id": int(discord_user_id),
            "issued_at": int(time.time()),
        },
        separators=(",", ":"),
    ).encode()
    encoded_payload = _encode(payload)
    signature = _sign(payload, get_ft_state_secret())
    return f"{encoded_payload}.{signature}"


def parse_oauth_state(value: str) -> OAuthState:
    try:
        encoded_payload, signature = value.split(".", 1)
        payload = _decode(encoded_payload)
    except ValueError as error:
        raise OAuthStateError("Invalid OAuth state.") from error

    expected_signature = _sign(payload, get_ft_state_secret())
    if not hmac.compare_digest(signature, expected_signature):
        raise OAuthStateError("Invalid OAuth state signature.")

    try:
        data = json.loads(payload.decode())
        discord_user_id = int(data["discord_user_id"])
        issued_at = int(data["issued_at"])
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise OAuthStateError("Invalid OAuth state payload.") from error

    if int(time.time()) - issued_at > STATE_TTL_SECONDS:
        raise OAuthStateError("OAuth state expired.")

    return OAuthState(discord_user_id=discord_user_id, issued_at=issued_at)
