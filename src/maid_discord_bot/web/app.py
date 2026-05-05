from fastapi import FastAPI

from maid_discord_bot.database.connection import get_connection
from maid_discord_bot.database.schema import initialize_database
from maid_discord_bot.web.oauth import router as oauth_router


def create_app() -> FastAPI:
    app = FastAPI(title="Maid Discord Bot OAuth")
    app.include_router(oauth_router)

    @app.on_event("startup")
    def startup() -> None:
        with get_connection() as connection:
            initialize_database(connection)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
