import httpx
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse

from ..database.connection import get_connection
from ..database.repositories.ft_links import upsert_ft_link
from ..database.repositories.users import get_or_create_user_id
from ..database.schema import initialize_database
from ..services.ft_api import exchange_code_for_token, fetch_current_user
from ..services.oauth_state import OAuthStateError, parse_oauth_state


router = APIRouter()


@router.get("/oauth/42/callback", response_class=HTMLResponse)
async def ft_oauth_callback(
    code: str = Query(...),
    state: str = Query(...),
) -> str:
    try:
        parsed_state = parse_oauth_state(state)
    except OAuthStateError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    try:
        token = await exchange_code_for_token(code)
        ft_user = await fetch_current_user(token.access_token)
    except httpx.HTTPStatusError as error:
        detail = f"42 API returned {error.response.status_code}."
        raise HTTPException(status_code=502, detail=detail) from error
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail="42 API request failed.") from error

    with get_connection() as connection:
        initialize_database(connection)
        user_id = get_or_create_user_id(
            connection,
            parsed_state.discord_user_id,
        )
        upsert_ft_link(
            connection,
            user_id=user_id,
            ft_user_id=ft_user.id,
            ft_login=ft_user.login,
            access_token=token.access_token,
            refresh_token=token.refresh_token,
            token_expires_at=token.expires_at,
        )

    return (
        "<!doctype html>"
        "<html><head><meta charset=\"utf-8\"><title>42 linked</title></head>"
        "<body><h1>42 account linked</h1>"
        "<p>You can close this tab and return to Discord.</p>"
        "</body></html>"
    )
