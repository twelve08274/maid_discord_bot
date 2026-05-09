from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from urllib.parse import urlencode

import httpx

from ..config import FtOAuthConfig, get_ft_oauth_config


FT_AUTHORIZE_URL = "https://api.intra.42.fr/oauth/authorize"
FT_TOKEN_URL = "https://api.intra.42.fr/oauth/token"
FT_ME_URL = "https://api.intra.42.fr/v2/me"
FT_USER_LOCATIONS_URL = "https://api.intra.42.fr/v2/users/{user_id}/locations"
FT_CAMPUS_LOCATIONS_URL = (
    "https://api.intra.42.fr/v2/campus/{campus_id}/locations"
)


@dataclass(frozen=True)
class FtToken:
    access_token: str
    refresh_token: str
    expires_at: datetime


@dataclass(frozen=True)
class FtUser:
    id: int
    login: str


@dataclass(frozen=True)
class FtLocation:
    id: int
    begin_at: datetime
    end_at: datetime | None
    host: str | None


@dataclass(frozen=True)
class FtAppToken:
    access_token: str
    expires_at: datetime


def create_authorization_url(
    state: str,
    config: FtOAuthConfig | None = None,
) -> str:
    if config is None:
        config = get_ft_oauth_config()

    query = urlencode(
        {
            "client_id": config.client_id,
            "redirect_uri": config.redirect_uri,
            "response_type": "code",
            "scope": config.scopes,
            "state": state,
        }
    )
    return f"{FT_AUTHORIZE_URL}?{query}"


async def exchange_code_for_token(
    code: str,
    config: FtOAuthConfig | None = None,
) -> FtToken:
    if config is None:
        config = get_ft_oauth_config()

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(
            FT_TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "client_id": config.client_id,
                "client_secret": config.client_secret,
                "code": code,
                "redirect_uri": config.redirect_uri,
            },
        )
        response.raise_for_status()

    payload = response.json()
    expires_in = int(payload.get("expires_in", 7200))
    return FtToken(
        access_token=str(payload["access_token"]),
        refresh_token=str(payload["refresh_token"]),
        expires_at=datetime.now(UTC) + timedelta(seconds=expires_in),
    )


async def fetch_app_access_token(
    config: FtOAuthConfig | None = None,
) -> FtAppToken:
    if config is None:
        config = get_ft_oauth_config()

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(
            FT_TOKEN_URL,
            data={
                "grant_type": "client_credentials",
                "client_id": config.client_id,
                "client_secret": config.client_secret,
            },
        )
        response.raise_for_status()

    payload = response.json()
    expires_in = int(payload.get("expires_in", 7200))
    return FtAppToken(
        access_token=str(payload["access_token"]),
        expires_at=datetime.now(UTC) + timedelta(seconds=expires_in),
    )


async def refresh_access_token(
    refresh_token: str,
    config: FtOAuthConfig | None = None,
) -> FtToken:
    if config is None:
        config = get_ft_oauth_config()

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(
            FT_TOKEN_URL,
            data={
                "grant_type": "refresh_token",
                "client_id": config.client_id,
                "client_secret": config.client_secret,
                "refresh_token": refresh_token,
            },
        )
        response.raise_for_status()

    payload = response.json()
    expires_in = int(payload.get("expires_in", 7200))
    return FtToken(
        access_token=str(payload["access_token"]),
        refresh_token=str(payload.get("refresh_token", refresh_token)),
        expires_at=datetime.now(UTC) + timedelta(seconds=expires_in),
    )


async def fetch_current_user(access_token: str) -> FtUser:
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            FT_ME_URL,
            headers={"Authorization": f"Bearer {access_token}"},
        )
        response.raise_for_status()

    payload = response.json()
    return FtUser(id=int(payload["id"]), login=str(payload["login"]))


async def fetch_active_location(
    access_token: str,
    user_id: str,
) -> FtLocation | None:
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            FT_USER_LOCATIONS_URL.format(user_id=user_id),
            headers={"Authorization": f"Bearer {access_token}"},
            params={
                "filter[active]": "true",
                "sort": "-begin_at",
                "page[size]": "1",
            },
        )
        response.raise_for_status()

    payload = response.json()
    if not payload:
        return None

    location = payload[0]
    end_at = location.get("end_at")
    return FtLocation(
        id=int(location["id"]),
        begin_at=datetime.fromisoformat(
            str(location["begin_at"]).replace("Z", "+00:00")
        ),
        end_at=(
            None
            if end_at is None
            else datetime.fromisoformat(str(end_at).replace("Z", "+00:00"))
        ),
        host=location.get("host"),
    )


async def fetch_active_campus_location_count(
    access_token: str,
    campus_id: str,
) -> int:
    locations = await fetch_active_campus_locations(access_token, campus_id)
    return len(locations)


async def fetch_active_campus_locations(
    access_token: str,
    campus_id: str,
) -> list[FtLocation]:
    page_size = 100
    page_number = 1
    locations: list[FtLocation] = []

    async with httpx.AsyncClient(timeout=10.0) as client:
        while True:
            response = await client.get(
                FT_CAMPUS_LOCATIONS_URL.format(campus_id=campus_id),
                headers={"Authorization": f"Bearer {access_token}"},
                params={
                    "filter[active]": "true",
                    "page[number]": str(page_number),
                    "page[size]": str(page_size),
                },
            )
            response.raise_for_status()

            payload = response.json()
            for location in payload:
                end_at = location.get("end_at")
                if end_at is not None:
                    continue
                locations.append(
                    FtLocation(
                        id=int(location["id"]),
                        begin_at=datetime.fromisoformat(
                            str(location["begin_at"]).replace("Z", "+00:00")
                        ),
                        end_at=None,
                        host=location.get("host"),
                    )
                )

            if len(payload) < page_size:
                return locations
            page_number += 1
