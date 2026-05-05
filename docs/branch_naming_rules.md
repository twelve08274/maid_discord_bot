# ブランチ命名規則

## 目的

このプロジェクトでは、作業内容がひと目で分かるようにブランチ名の命名規則を統一する。

Discord育成Botでは、キャラ育成・42 API連携・生活支援・DB設計など複数の機能を並行して開発するため、ブランチ名から「何の作業か」が分かる状態にする。

---

## 基本ルール

```txt
<type>/<issue番号>-<内容>
```

Issue番号がない場合は、以下の形式でもよい。

```txt
<type>/<内容>
```

---

## 使用できる type

| type | 用途 | 例 |
|---|---|---|
| `feature` | 新機能追加 | `feature/12-status-command` |
| `fix` | バグ修正 | `fix/18-token-error` |
| `refactor` | 挙動を変えない整理 | `refactor/23-db-connection` |
| `docs` | ドキュメント修正 | `docs/branch-naming-rules` |
| `test` | テスト追加・修正 | `test/31-level-up` |
| `chore` | 設定・環境構築など | `chore/setup-dotenv` |
| `design` | 設計・仕様整理 | `design/42-daily-flow` |
| `hotfix` | 緊急修正 | `hotfix/login-check-crash` |

---

## 命名ルール

- 小文字英数字を使う
- 単語の区切りは `-` を使う
- 日本語は使わない
- スペースは使わない
- `_` は使わない
- 内容は短く、分かりやすくする
- 1ブランチにつき1目的にする

---

## 良い例

```txt
feature/1-ping-command
feature/2-register-command
feature/3-status-command
feature/10-link42-oauth
feature/11-checkin-command
feature/12-auto-daily
feature/20-achievements
fix/21-invalid-discord-token
fix/22-db-migration-error
refactor/30-user-service
docs/update-todo-list
chore/setup-sqlite
```

---

## 悪い例

```txt
new-feature
修正
feature/status command
feature_status_command
feature/status/command
fix/bug
work
```

### 理由

| 悪い例 | 理由 |
|---|---|
| `new-feature` | 作業種別が分からない |
| `修正` | 日本語で環境によって扱いづらい |
| `feature/status command` | スペースが入っている |
| `feature_status_command` | `_` を使っている |
| `feature/status/command` | `/` が多く階層が深い |
| `fix/bug` | 何のバグ修正か分からない |
| `work` | 内容が不明確 |

---

## Discord育成Botでの例

### Bot基盤

```txt
feature/ping-command
chore/setup-discord-py
chore/setup-dotenv
```

### DB

```txt
feature/sqlite-schema
feature/users-table
feature/daily-claims-table
refactor/db-connection
```

### キャラ育成

```txt
feature/register-command
feature/status-command
feature/exp-level-system
feature/stamina-mood-system
feature/status-embed-image
```

### 42 API連携

```txt
feature/link42-oauth
feature/ft-token-refresh
feature/checkin-command
feature/auto-daily
fix/ft-api-token-expired
```

### 生活支援

```txt
feature/weather-command
feature/umbrella-command
feature/food-command
```

---

## ブランチ作成コマンド

```bash
git switch -c feature/status-command
```

Issue番号を使う場合：

```bash
git switch -c feature/3-status-command
```

---

## ブランチ名を間違えた場合

まだpushしていない場合：

```bash
git branch -m feature/status-command
```

すでにpushした場合：

```bash
git branch -m feature/status-command
git push origin -u feature/status-command
git push origin --delete old-branch-name
```

---

## 運用方針

- `main` ブランチに直接作業しない
- 作業前に必ずブランチを切る
- 作業が終わったらPull Requestを作る
- ブランチ名はPull Requestの内容と一致させる
- 大きすぎる作業は複数ブランチに分ける

---

## 推奨フロー

```txt
Issueを作る
↓
Issue番号に合わせてブランチを切る
↓
作業する
↓
commitする
↓
pushする
↓
Pull Requestを作る
↓
レビュー後にmainへmergeする
```

---

## このプロジェクトで特に使いそうな命名

```txt
feature/ping-command
feature/register-command
feature/status-command
feature/link42-oauth
feature/checkin-command
feature/auto-daily
feature/level-up-system
feature/achievement-system
feature/weather-command
chore/setup-project
chore/setup-env
chore/setup-sqlite
refactor/db-layer
docs/update-readme
docs/update-todo
```
