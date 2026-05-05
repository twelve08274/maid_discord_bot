# DATABASE.md

# Discord育成Bot データベース設計書

## 1. 方針

最初はSQLiteを使用する。
将来的にユーザー数や機能が増えた場合は、PostgreSQLなどへの移行を検討する。

## 2. 命名規則

- テーブル名は複数形にする。
- カラム名はsnake_caseにする。
- 主キーは基本的に `id` とする。
- DiscordユーザーIDは `discord_user_id` とする。
- 42ユーザーIDは `ft_user_id` とする。
- 作成日時は `created_at` とする。
- 更新日時は `updated_at` とする。

---

## 3. テーブル一覧

| テーブル名 | 目的 |
|---|---|
| `users` | Discordユーザーの育成ステータスを保存する |
| `ft_links` | Discordユーザーと42アカウントの連携情報を保存する |
| `daily_claims` | Daily報酬の受け取り履歴を保存する |
| `achievements` | 実績マスタを保存する |
| `user_achievements` | ユーザーごとの実績解除状況を保存する |
| `tasks` | ユーザーが完了した課題を保存する |
| `study_posts` | 課題並走募集の投稿を保存する |
| `food_posts` | ご飯募集の投稿を保存する |

---

## 4. `users`

## 4.1 目的

Discordユーザーの基本情報と育成ステータスを保存する。

## 4.2 カラム

| カラム名 | 型 | 制約 | 説明 |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | 内部ID |
| `discord_user_id` | TEXT | UNIQUE NOT NULL | DiscordユーザーID |
| `level` | INTEGER | NOT NULL DEFAULT 1 | 現在レベル |
| `exp` | INTEGER | NOT NULL DEFAULT 0 | 現在EXP |
| `stamina` | INTEGER | NOT NULL DEFAULT 100 | 元気度 |
| `affection` | INTEGER | NOT NULL DEFAULT 0 | 親密度 |
| `mood` | TEXT | NOT NULL DEFAULT 'normal' | 現在の気分 |
| `auto_daily_enabled` | INTEGER | NOT NULL DEFAULT 0 | 自動Dailyが有効か。0=false, 1=true |
| `last_login_date` | TEXT | NULL | 最終42ログイン日 |
| `created_at` | TEXT | NOT NULL | 作成日時 |
| `updated_at` | TEXT | NOT NULL | 更新日時 |

## 4.3 備考

- SQLiteでは真偽値を `INTEGER` で扱う。
- `discord_user_id` は数値が大きいため、TEXTとして保存する。

---

## 5. `ft_links`

## 5.1 目的

Discordユーザーと42アカウントの連携情報を保存する。

## 5.2 カラム

| カラム名 | 型 | 制約 | 説明 |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | 内部ID |
| `user_id` | INTEGER | NOT NULL | `users.id` |
| `ft_user_id` | TEXT | NOT NULL | 42ユーザーID |
| `ft_login` | TEXT | NOT NULL | 42ログイン名 |
| `access_token` | TEXT | NOT NULL | 42 API access token |
| `refresh_token` | TEXT | NOT NULL | 42 API refresh token |
| `token_expires_at` | TEXT | NOT NULL | access tokenの期限 |
| `created_at` | TEXT | NOT NULL | 作成日時 |
| `updated_at` | TEXT | NOT NULL | 更新日時 |

## 5.3 制約

```sql
FOREIGN KEY (user_id) REFERENCES users(id)
```

## 5.4 注意

- tokenは漏洩すると危険なので、Gitに含めない。
- 本番運用では暗号化や安全なSecret管理を検討する。

---

## 6. `daily_claims`

## 6.1 目的

Daily報酬の受け取り履歴を保存する。

## 6.2 カラム

| カラム名 | 型 | 制約 | 説明 |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | 内部ID |
| `user_id` | INTEGER | NOT NULL | `users.id` |
| `claim_date` | TEXT | NOT NULL | Dailyを受け取った日付 |
| `source` | TEXT | NOT NULL | `manual` または `auto` |
| `exp_gained` | INTEGER | NOT NULL DEFAULT 10 | 獲得EXP |
| `created_at` | TEXT | NOT NULL | 作成日時 |

## 6.3 制約

```sql
FOREIGN KEY (user_id) REFERENCES users(id)
UNIQUE (user_id, claim_date)
```

## 6.4 備考

`UNIQUE (user_id, claim_date)` により、同じ日にDailyを二重受け取りできないようにする。

---

## 7. `achievements`

## 7.1 目的

実績のマスタ情報を保存する。

## 7.2 カラム

| カラム名 | 型 | 制約 | 説明 |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | 内部ID |
| `code` | TEXT | UNIQUE NOT NULL | 実績コード |
| `name` | TEXT | NOT NULL | 実績名 |
| `description` | TEXT | NOT NULL | 実績説明 |
| `created_at` | TEXT | NOT NULL | 作成日時 |

## 7.3 実績例

| code | name |
|---|---|
| `first_register` | 初めての登録 |
| `first_daily` | 初めての42ログインDaily |
| `login_3_days` | 3日連続ログイン |
| `login_7_days` | 7日連続ログイン |
| `first_task_done` | 初めての課題完了 |
| `tasks_3_done` | 課題3個完了 |
| `tasks_5_done` | 課題5個完了 |
| `level_5` | Lv.5到達 |
| `level_10` | Lv.10到達 |
| `first_review_message` | 初めてのレビュー募集 |
| `first_study_post` | 初めての課題並走募集 |

---

## 8. `user_achievements`

## 8.1 目的

ユーザーごとの実績解除状況を保存する。

## 8.2 カラム

| カラム名 | 型 | 制約 | 説明 |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | 内部ID |
| `user_id` | INTEGER | NOT NULL | `users.id` |
| `achievement_id` | INTEGER | NOT NULL | `achievements.id` |
| `unlocked_at` | TEXT | NOT NULL | 解除日時 |

## 8.3 制約

```sql
FOREIGN KEY (user_id) REFERENCES users(id)
FOREIGN KEY (achievement_id) REFERENCES achievements(id)
UNIQUE (user_id, achievement_id)
```

---

## 9. `tasks`

## 9.1 目的

ユーザーが完了した42課題を保存する。

## 9.2 カラム

| カラム名 | 型 | 制約 | 説明 |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | 内部ID |
| `user_id` | INTEGER | NOT NULL | `users.id` |
| `task_name` | TEXT | NOT NULL | 課題名 |
| `completed_at` | TEXT | NOT NULL | 完了登録日時 |
| `created_at` | TEXT | NOT NULL | 作成日時 |

## 9.3 制約

```sql
FOREIGN KEY (user_id) REFERENCES users(id)
UNIQUE (user_id, task_name)
```

## 9.4 備考

同じユーザーが同じ課題を重複登録できないようにする。

---

## 10. `study_posts`

## 10.1 目的

課題並走募集の投稿情報を保存する。

## 10.2 カラム

| カラム名 | 型 | 制約 | 説明 |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | 内部ID |
| `user_id` | INTEGER | NOT NULL | 投稿者の `users.id` |
| `guild_id` | TEXT | NOT NULL | DiscordサーバーID |
| `channel_id` | TEXT | NOT NULL | DiscordチャンネルID |
| `message_id` | TEXT | NOT NULL | DiscordメッセージID |
| `task_name` | TEXT | NOT NULL | 課題名 |
| `created_at` | TEXT | NOT NULL | 作成日時 |

## 10.3 制約

```sql
FOREIGN KEY (user_id) REFERENCES users(id)
```

---

## 11. `food_posts`

## 11.1 目的

ご飯募集の投稿情報を保存する。

## 11.2 カラム

| カラム名 | 型 | 制約 | 説明 |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | 内部ID |
| `user_id` | INTEGER | NOT NULL | 投稿者の `users.id` |
| `guild_id` | TEXT | NOT NULL | DiscordサーバーID |
| `channel_id` | TEXT | NOT NULL | DiscordチャンネルID |
| `message_id` | TEXT | NOT NULL | DiscordメッセージID |
| `time_text` | TEXT | NULL | 募集時間 |
| `place_text` | TEXT | NULL | 募集場所 |
| `created_at` | TEXT | NOT NULL | 作成日時 |

## 11.3 制約

```sql
FOREIGN KEY (user_id) REFERENCES users(id)
```

---

## 12. 初期schema案

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_user_id TEXT UNIQUE NOT NULL,
    level INTEGER NOT NULL DEFAULT 1,
    exp INTEGER NOT NULL DEFAULT 0,
    stamina INTEGER NOT NULL DEFAULT 100,
    affection INTEGER NOT NULL DEFAULT 0,
    mood TEXT NOT NULL DEFAULT 'normal',
    auto_daily_enabled INTEGER NOT NULL DEFAULT 0,
    last_login_date TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ft_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    ft_user_id TEXT NOT NULL,
    ft_login TEXT NOT NULL,
    access_token TEXT NOT NULL,
    refresh_token TEXT NOT NULL,
    token_expires_at TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS daily_claims (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    claim_date TEXT NOT NULL,
    source TEXT NOT NULL,
    exp_gained INTEGER NOT NULL DEFAULT 10,
    created_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE (user_id, claim_date)
);

CREATE TABLE IF NOT EXISTS achievements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS user_achievements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    achievement_id INTEGER NOT NULL,
    unlocked_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (achievement_id) REFERENCES achievements(id),
    UNIQUE (user_id, achievement_id)
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    task_name TEXT NOT NULL,
    completed_at TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE (user_id, task_name)
);

CREATE TABLE IF NOT EXISTS study_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    guild_id TEXT NOT NULL,
    channel_id TEXT NOT NULL,
    message_id TEXT NOT NULL,
    task_name TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS food_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    guild_id TEXT NOT NULL,
    channel_id TEXT NOT NULL,
    message_id TEXT NOT NULL,
    time_text TEXT,
    place_text TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

## 13. 今後追加する可能性があるテーブル

| テーブル名 | 目的 |
|---|---|
| `weather_settings` | ユーザーやサーバーごとの天気設定 |
| `guild_settings` | サーバーごとのBot設定 |
| `character_settings` | メイド型・執事型などのキャラ設定 |
| `login_streaks` | 連続ログイン管理を分離する場合 |
| `event_logs` | 管理者用ログ |

---

## 14. 注意事項

- `.env` やtoken情報は絶対にGit管理しない。
- SQLiteファイルも基本的にはGit管理しない。
- `schema.sql` はGit管理する。
- 本番運用ではDBバックアップ方法を決める。
