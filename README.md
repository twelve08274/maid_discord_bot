# Maid Discord Bot

## 42 OAuth setup

Create a 42 OAuth application and set its redirect URI to the same value as
`FT_REDIRECT_URI`.

Local development example:

```env
DISCORD_TOKEN=
DISCORD_TEST_GUILD_ID=
DATABASE_PATH=data/maid_discord_bot.sqlite3
FT_CLIENT_ID=
FT_CLIENT_SECRET=
FT_REDIRECT_URI=http://localhost:8000/oauth/42/callback
FT_SCOPES=public
FT_STATE_SECRET=
```

`FT_STATE_SECRET` should be a long random string shared by both the Discord bot
process and the OAuth web process.

Install dependencies:

```powershell
pip install -r requirements.txt
```

Initialize the database:

```powershell
python scripts/init_db.py
```

Run the Discord bot:

```powershell
python main.py
```

Run the OAuth web process separately:

```powershell
uvicorn maid_discord_bot.web.app:app --app-dir src --host 0.0.0.0 --port 8000
```

Then use `/register` in Discord. The command returns a 42 authorization URL,
and the callback stores the Discord user and 42 account link in SQLite.
