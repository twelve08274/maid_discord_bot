# Maid Discord Bot

42へのログイン状況をもとにDaily報酬を付与し、Discord上のキャラを育てるBotです。

現在は、Discordユーザーと42アカウントをOAuth連携し、42 Location APIでログイン状態を確認して、ログイン中ならDaily報酬として `EXP +10` を付与します。

## 前提

このREADMEでは、すでにプロジェクト直下に `.env` がある前提で進めます。

`.env` には最低限、次の値が必要です。

```env
DISCORD_TOKEN=
DISCORD_TEST_GUILD_ID=
DATABASE_PATH=data/maid_discord_bot.sqlite3

FT_CLIENT_ID=
FT_CLIENT_SECRET=
FT_REDIRECT_URI=http://localhost:8000/oauth/42/callback
FT_SCOPES=public
FT_STATE_SECRET=
FT_LOCATION_POLL_INTERVAL_SECONDS=300
DAILY_REWARD_TIMEZONE=Asia/Tokyo
```

`FT_REDIRECT_URI` は42 OAuthアプリ側に登録したRedirect URIと完全に一致させてください。

`FT_STATE_SECRET` はDiscord BotプロセスとOAuth Webプロセスで共通の、十分に長いランダム文字列にしてください。

## `.venv` 作成から実行まで

以下はWindows PowerShellでの手順です。

### 1. `.venv` を作成する

Pythonランチャーが使える場合:

```powershell
py -3.12 -m venv .venv
```

`py` が使えない場合:

```powershell
python -m venv .venv
```

### 2. `.venv` を有効化する

```powershell
.\.venv\Scripts\Activate.ps1
```

PowerShellの実行ポリシーで止まる場合は、現在のPowerShellセッションだけ許可してから再実行します。

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1
```

有効化できると、プロンプトの先頭に `(.venv)` が付きます。

### 3. 依存関係をインストールする

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. データベースを初期化する

```powershell
python scripts/init_db.py
```

`DATABASE_PATH` に指定したSQLiteファイルと必要なテーブルが作成されます。

### 5. OAuth Webサーバーを起動する

42アカウント連携のcallbackを受けるため、Botとは別のPowerShellで起動します。

```powershell
.\.venv\Scripts\Activate.ps1
python -m uvicorn maid_discord_bot.web.app:app --app-dir src --host 0.0.0.0 --port 8000
```

初回の `/register` を使う場合、このWebサーバーが起動している必要があります。

すでにDBに42連携済みユーザーが入っていて、自動Dailyだけ動かしたい場合は、このWebサーバーなしでもBot本体は動きます。

### 6. Discord Botを起動する

別のPowerShellで実行します。

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```

`main.py` を起動すると、次の処理が動きます。

- `.env` の読み込み
- Discord Botの起動
- slash commandの登録
- 自動Dailyスケジューラの起動
- `FT_LOCATION_POLL_INTERVAL_SECONDS` ごとの42 Location API確認

## Discordでの使い方

### 42アカウントを連携する

Discordで次のコマンドを実行します。

```txt
/register
```

42の認証URLが返ってくるので、ブラウザで開いて認証します。

認証に成功すると、DiscordユーザーIDと42アカウント情報がSQLiteに保存されます。

### 自動Dailyを有効にする

42アカウント連携後、次のコマンドを実行します。

```txt
/autodaily enabled:true
```

無効化する場合:

```txt
/autodaily enabled:false
```

自動Dailyが有効なユーザーは、Bot起動中に42 Location APIでログイン状態を確認されます。

42にログイン中のactive locationが見つかった場合、`DAILY_REWARD_TIMEZONE` の日付ごとに一度だけ `EXP +10` が付与され、Discord DMで通知されます。

## 自動Dailyの仕様

42 Location APIは次の形で呼び出します。

```txt
GET /v2/users/:user_id/locations
filter[active]=true
```

処理の流れ:

1. 自動Dailyが有効な42連携済みユーザーをDBから取得する
2. access tokenが期限切れに近ければrefresh tokenで更新する
3. 42 Location APIでactive locationを取得する
4. active locationがあれば `ft_location_rewards` にlocation単位の履歴を保存する
5. その日の `daily_claims` が未作成なら `EXP +10` を付与する
6. レベルアップがあれば通知文に含める
7. Discord DMで報酬通知を送る

重複防止:

- `daily_claims` は `UNIQUE (user_id, claim_date)` なので、同じ日にDaily報酬は一度だけです。
- `ft_location_rewards` は `UNIQUE (user_id, ft_location_id)` なので、同じ42 locationは重複処理されません。

## テスト実行

### 全テスト

```powershell
python -m unittest discover
```

### 自動Dailyのモックテストだけ

```powershell
python -m unittest tests.services.test_auto_daily
```

### EXPテストだけ

```powershell
python -m unittest tests.services.test_exp
```

### DBスキーマテストだけ

```powershell
python -m unittest tests.database.test_schema
```

### lintと型チェック

```powershell
python -m flake8 --jobs=1 src tests
python -m mypy src
```

Windows環境ではflake8の並列実行が権限エラーになる場合があるため、`--jobs=1` を付けています。

## テストコードの説明

### `tests/services/test_auto_daily.py`

自動Daily処理のモックテストです。

実際の42 APIにはアクセスせず、`unittest.mock.patch` と `AsyncMock` を使って外部API呼び出しを差し替えています。

#### `test_rewards_active_location_once_per_day`

目的:

- 42にログイン中のactive locationがある場合にDaily報酬が付与されること
- 同じlocationでは2回目の報酬が付与されないこと
- EXPが `10` 増えること
- `daily_claims` が1件だけ作成されること

モックしている関数:

```python
maid_discord_bot.services.auto_daily.fetch_active_location
```

この関数は本来42 Location APIを呼びますが、テストでは次のような `FtLocation` を返すように差し替えています。

```python
location = FtLocation(
    id=42,
    begin_at=datetime(2026, 5, 6, 1, 0, tzinfo=UTC),
    end_at=None,
    host="c1r1s1",
)
```

テスト内では同じユーザーに対して `check_and_reward_auto_daily` を2回呼びます。

```python
first_result = await check_and_reward_auto_daily(connection, account)
second_result = await check_and_reward_auto_daily(connection, account)
```

期待結果:

- `first_result` は `None` ではない
- `second_result` は `None`
- DB上のユーザーEXPは `10`
- `daily_claims` の件数は `1`

#### `test_refreshes_expired_access_token`

目的:

- access tokenが期限切れの場合にrefresh tokenで更新されること
- 更新後のaccess tokenでLocation確認に進むこと
- 新しいtokenがDBに保存されること

モックしている関数:

```python
maid_discord_bot.services.auto_daily.refresh_access_token
maid_discord_bot.services.auto_daily.fetch_active_location
```

`refresh_access_token` は本来42 OAuth APIを呼びますが、テストでは次の `FtToken` を返すように差し替えています。

```python
refreshed_token = FtToken(
    access_token="new-access-token",
    refresh_token="new-refresh-token",
    expires_at=datetime.now(UTC) + timedelta(hours=2),
)
```

`fetch_active_location` は `None` を返すようにして、ログイン報酬の付与までは進まないケースを作っています。

期待結果:

- `refresh_access_token` が古いrefresh tokenで1回呼ばれる
- `fetch_active_location` が新しいaccess tokenで1回呼ばれる
- DBの `ft_links.access_token` が `new-access-token` に更新される
- DBの `ft_links.refresh_token` が `new-refresh-token` に更新される

### `tests/services/test_exp.py`

EXPとレベルアップ処理のユニットテストです。

外部APIは使わず、SQLiteのインメモリDBを使います。

#### `test_required_exp_for_level_scales_by_level`

目的:

- 必要EXPが `level * 100` になっていること

期待結果:

- Lv.1の必要EXPは `100`
- Lv.5の必要EXPは `500`

#### `test_add_exp_levels_up_and_keeps_remaining_exp`

目的:

- EXP加算でレベルアップすること
- 余ったEXPが保持されること
- DB上の `users.level` と `users.exp` が更新されること

テストでは、Lv.1 / EXP 95 のユーザーに `EXP +10` します。

期待結果:

- Lv.1からLv.2に上がる
- 余りEXPは `5`
- DB上も `level = 2`, `exp = 5` になる

### `tests/database/test_schema.py`

SQLiteスキーマのユニットテストです。

外部APIは使わず、SQLiteのインメモリDBに `initialize_database` を実行して検証します。

#### `test_initialize_database_creates_expected_tables`

目的:

- 必要なテーブルが作成されること

確認している主なテーブル:

- `users`
- `ft_links`
- `daily_claims`
- `ft_location_rewards`
- `achievements`
- `user_achievements`
- `tasks`

#### `test_daily_claims_are_unique_per_user_and_date`

目的:

- 同じユーザーが同じ日にDaily報酬を二重取得できないこと

期待結果:

- 同じ `user_id` と `claim_date` で2件目をINSERTすると `sqlite3.IntegrityError` になる

#### `test_user_achievements_are_unique`

目的:

- 同じユーザーに同じ実績が二重付与されないこと

期待結果:

- 同じ `user_id` と `achievement_id` で2件目をINSERTすると `sqlite3.IntegrityError` になる

#### `test_tasks_are_unique_per_user_and_task_name`

目的:

- 同じユーザーに同じtask名を二重登録できないこと

期待結果:

- 同じ `user_id` と `task_name` で2件目をINSERTすると `sqlite3.IntegrityError` になる
