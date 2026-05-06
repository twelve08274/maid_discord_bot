# Maid Discord Bot

Discord上でメイド育成・学習支援・42アカウント連携を行うためのBotです。

## 現在までに実装したもの

- Discord Botの基本起動処理
- `/ping` コマンド
- `/register` コマンド
- 42 OAuth認証URLの生成
- OAuth `state` の署名付き生成・検証
- 42 OAuth callback用のFastAPI Webサーバー
- callback成功時のDiscordユーザーと42アカウントのSQLite保存
- SQLiteの初期スキーマ作成
- `users` テーブル
- `ft_links` テーブル
- DB接続の自動close対応
- `tests/` 配下のローカルテスト
- まとめて確認するための `scripts/check.py`

## 42 OAuth連携の流れ

1. Discordで `/register` を実行する
2. Botが42 OAuth認証URLを返す
3. ユーザーがURLを開いて42で認証する
4. 42が `FT_REDIRECT_URI` にcallbackする
5. FastAPI側で認証コードを42 APIに交換する
6. 42ユーザー情報を取得する
7. DiscordユーザーIDと42アカウント情報をSQLiteに保存する

## 環境変数

このリポジトリには、デフォルトでは `.env` は存在しません。

`.env` にはDiscord tokenや42 OAuth client secretなどの秘密情報を書くため、Git管理しない前提です。最初に `.env.example` をコピーして、自分のローカル用 `.env` を作成してください。

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

macOS / Linux:

```bash
cp .env.example .env
```

作成した `.env` をエディタで開き、Discord Botと42 OAuthの値を記入します。

Windows PowerShellでVS Codeを使う場合:

```powershell
code .env
```

macOS / LinuxでVS Codeを使う場合:

```bash
code .env
```

VS Codeを使わない場合は、普段使っているエディタで `.env` を開いて編集してください。

```env
DISCORD_TOKEN=your_discord_bot_token
DISCORD_TEST_GUILD_ID=your_test_guild_id
DATABASE_PATH=data/maid_discord_bot.sqlite3

FT_CLIENT_ID=your_42_client_id
FT_CLIENT_SECRET=your_42_client_secret
FT_REDIRECT_URI=http://localhost:8000/oauth/42/callback
FT_SCOPES=public
FT_STATE_SECRET=your_long_random_secret
```

各項目の意味:

- `DISCORD_TOKEN`: Discord Developer Portalで作成したBotのtoken
- `DISCORD_TEST_GUILD_ID`: slash commandを同期したいテスト用DiscordサーバーID
- `DATABASE_PATH`: SQLite DBの保存先
- `FT_CLIENT_ID`: 42 OAuthアプリのclient ID
- `FT_CLIENT_SECRET`: 42 OAuthアプリのclient secret
- `FT_REDIRECT_URI`: 42 OAuthアプリに登録したcallback URL
- `FT_SCOPES`: 42 APIで要求するscope
- `FT_STATE_SECRET`: OAuth state署名用のランダムな秘密文字列

`DISCORD_TEST_GUILD_ID` は、開発中にslash commandをすぐ反映したいDiscordサーバーのIDです。空欄でも動かせますが、グローバル同期になり反映に時間がかかることがあります。

ローカル開発では、42 OAuthアプリ側のredirect URIにも以下を登録してください。

```text
http://localhost:8000/oauth/42/callback
```

`FT_STATE_SECRET` は長いランダム文字列にしてください。Discord BotプロセスとOAuth Webプロセスの両方で同じ値を使います。

`.env` は秘密情報を含むため、絶対にコミットしないでください。`.env.example` はコミットして問題ありません。

`.env` がないまま起動すると、Discord BotやOAuth設定の読み込みでエラーになります。起動前に必ず `.env.example` から `.env` を作成し、必要な値を記入してください。

## セットアップ

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windowsで `python` が見つからず、`py` ランチャーを使う場合:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## DB初期化

`.env` を作成して依存関係を入れたあと、DBを初期化します。

```powershell
python scripts/init_db.py
```

デフォルトでは `data/maid_discord_bot.sqlite3` にSQLite DBを作成します。

## 起動方法

OAuthの実通し確認では、ターミナルを2つ使います。

1つ目のターミナルでOAuth callback用Webサーバーを起動します。

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn maid_discord_bot.web.app:app --app-dir src --host 127.0.0.1 --port 8000
```

macOS / Linux:

```bash
source .venv/bin/activate
uvicorn maid_discord_bot.web.app:app --app-dir src --host 127.0.0.1 --port 8000
```

別ターミナルで起動確認します。

Windows PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

macOS / Linux:

```bash
curl http://127.0.0.1:8000/health
```

`status` が `ok` ならWebサーバーは起動できています。

2つ目のターミナルでDiscord Botを起動します。

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```

macOS / Linux:

```bash
source .venv/bin/activate
python main.py
```

Botが起動したら、Discordで `/register` を実行します。Botが返したURLを開いて42で認証し、callback画面に `42 account linked` が表示されればOAuth連携は成功です。

## 起動までの全体手順

初回は、プロジェクト直下で以下の順に進めます。

1. venvを作成する
2. venvを有効化する
3. 依存関係をインストールする
4. `.env.example` をコピーして `.env` を作成する
5. `.env` にDiscordと42 OAuthのAPI情報を記入する
6. DBを初期化する
7. OAuth Webサーバーを起動する
8. 別ターミナルでDiscord Botを起動する

まず、venv作成から `.env` 作成までを実行します。

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

次に `.env` を編集して、以下を記入します。

- `DISCORD_TOKEN`
- `DISCORD_TEST_GUILD_ID`
- `FT_CLIENT_ID`
- `FT_CLIENT_SECRET`
- `FT_REDIRECT_URI`
- `FT_STATE_SECRET`

ローカル開発の `FT_REDIRECT_URI` は、基本的に以下のままでOKです。

```env
FT_REDIRECT_URI=http://localhost:8000/oauth/42/callback
```

`.env` を保存したら、同じターミナルでDB初期化とOAuth Webサーバー起動を行います。

その後:

Windows PowerShell:

```powershell
python scripts/init_db.py
uvicorn maid_discord_bot.web.app:app --app-dir src --host 127.0.0.1 --port 8000
```

macOS / Linux:

```bash
python scripts/init_db.py
uvicorn maid_discord_bot.web.app:app --app-dir src --host 127.0.0.1 --port 8000
```

別ターミナルで:

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```

macOS / Linux:

```bash
source .venv/bin/activate
python main.py
```

## ローカル検証

基本チェックをまとめて実行する場合:

```powershell
python scripts/check.py
```

テストだけを実行する場合:

```powershell
python -m unittest discover -s tests
```

現在のテストでは以下を確認します。

- OAuth stateの生成・検証
- OAuth stateの改ざん検知
- 42 OAuth認証URLの生成
- SQLiteへの `users` / `ft_links` 保存
- 42 API部分をmockしたcallback処理

mockテストは本物のDiscordや42 APIには接続しません。コードのロジック確認用です。

詳しいテスト手順は [docs/testing.md](docs/testing.md) を参照してください。

## 実通し確認

mockテストが通ったあとに、必要に応じて本物のDiscordと42 OAuthで確認します。

1. `.env` にDiscordと42 OAuthの値を設定する
2. `python scripts/init_db.py` でDBを初期化する
3. `uvicorn maid_discord_bot.web.app:app --app-dir src --host 127.0.0.1 --port 8000` を起動する
4. 別ターミナルで `python main.py` を起動する
5. Discordで `/register` を実行する
6. 返ってきたURLを開いて42で認証する
7. callback画面に `42 account linked` が出ることを確認する
8. SQLiteの `users` と `ft_links` にレコードが入ることを確認する

## 開発メモ

- 普段の確認はmockテストで行う
- 外部サービスとの接続確認は最後に実通しで行う
- `.env` とトークン類はコミットしない
- `tests/` はGit管理対象のテストコード置き場として使う
