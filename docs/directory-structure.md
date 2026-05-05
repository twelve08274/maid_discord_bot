# ディレクトリ構成の意図

このドキュメントは、Discord 育成 Bot の実装を進めるときに「どこへ何を書くか」を迷わないための整理です。

## ルート直下

| パス | 役割 |
|---|---|
| `main.py` | Bot を起動するためのエントリポイントです。将来的には `src/maid_discord_bot/bot.py` 側へ処理を寄せ、ここは起動だけを担当します。 |
| `.env.example` | 必要な環境変数のサンプルを置きます。実際の秘密情報は `.env` に置き、Git には含めません。 |
| `requirements.txt` | Python の依存ライブラリを管理します。`discord.py`、FastAPI、APScheduler、dotenv などを追加する想定です。 |
| `README.md` | プロジェクト概要、起動方法、開発手順などをまとめます。 |
| `docs/` | 仕様、設計、運用ルール、開発メモなどのドキュメントを置きます。 |

## `src/maid_discord_bot/`

Bot 本体の実装を置くパッケージです。Discord のイベント処理、設定読み込み、スケジューラ、各機能の呼び出し口をここに集めます。

| パス | 役割 |
|---|---|
| `bot.py` | Discord Bot インスタンスの作成、コマンド登録、起動前の初期化を担当します。 |
| `config.py` | 環境変数や設定値の読み込みを担当します。 |
| `scheduler.py` | 自動 Daily など、定期実行が必要な処理を管理します。 |

## `src/maid_discord_bot/commands/`

Discord コマンドごとの入り口を置きます。ユーザーからの入力を受け取り、細かい処理は `services/` や `database/` に委譲します。

| パス | 役割 |
|---|---|
| `ping.py` | Bot の疎通確認コマンドを担当します。 |
| `register.py` | ユーザー登録コマンドを担当します。 |
| `status.py` | 育成ステータス表示コマンドを担当します。 |
| `link42.py` | Discord アカウントと 42 アカウントの連携コマンドを担当します。 |
| `checkin.py` | 42 ログイン状況の確認と Daily 報酬付与を担当します。 |
| `autodaily.py` | 自動 Daily の有効化・無効化を担当します。 |
| `tasks.py` | `/done` や `/who-done` など、課題・タスク系コマンドを担当します。 |
| `study.py` | `/study` や学習投稿系コマンドを担当します。 |
| `life_support.py` | `/weather`、`/umbrella`、`/food` など生活支援系コマンドを担当します。 |

## `src/maid_discord_bot/database/`

SQLite との接続、テーブル定義、データアクセスを管理します。SQL や永続化に関わる処理はこの配下に閉じ込めます。

| パス | 役割 |
|---|---|
| `connection.py` | SQLite 接続の作成、トランザクション管理を担当します。 |
| `schema.py` | テーブル作成や初期スキーマを担当します。 |
| `repositories/` | テーブルごとの読み書き処理を置きます。 |

## `src/maid_discord_bot/database/repositories/`

DB テーブル単位の操作を置きます。コマンドやサービスが直接 SQL を書かなくてよいようにする層です。

| パス | 役割 |
|---|---|
| `users.py` | ユーザー登録情報、育成ステータス、自動 Daily 設定を扱います。 |
| `ft_links.py` | 42 アカウント連携情報とトークン情報を扱います。 |
| `daily_claims.py` | Daily 報酬の受け取り履歴を扱います。 |
| `achievements.py` | 実績マスタとユーザー実績を扱います。 |
| `tasks.py` | 課題完了や学習タスクの履歴を扱います。 |

## `src/maid_discord_bot/models/`

アプリ内で使うデータ構造を置きます。DB の行データや外部 API の結果を、そのまま辞書で回すのではなく、意味のある単位として扱うための場所です。

| パス | 役割 |
|---|---|
| `user.py` | ユーザーと育成ステータスを表します。 |
| `ft_link.py` | 42 アカウント連携情報を表します。 |
| `daily_claim.py` | Daily 報酬履歴を表します。 |
| `achievement.py` | 実績情報を表します。 |
| `task.py` | 課題・タスク情報を表します。 |

## `src/maid_discord_bot/services/`

Bot の主要な業務ロジックを置きます。コマンドから呼ばれ、DB や外部 API を組み合わせて実際の処理を行います。

| パス | 役割 |
|---|---|
| `character.py` | stamina、affection、mood などキャラクター状態の更新を担当します。 |
| `exp.py` | EXP 加算、レベルアップ判定を担当します。 |
| `ft_api.py` | 42 API へのアクセス、トークン更新、ログイン状況取得を担当します。 |
| `daily.py` | Daily 報酬の付与条件判定と付与処理を担当します。 |
| `weather.py` | 天気 API や生活支援系の判定を担当します。 |
| `achievements.py` | 実績解除条件の判定と記録を担当します。 |

## `src/maid_discord_bot/views/`

Discord に返す見た目を作る場所です。Embed や立ち絵画像など、表示に関わる処理をまとめます。

| パス | 役割 |
|---|---|
| `embeds.py` | ステータス表示や通知に使う Discord Embed を作成します。 |
| `character_images.py` | mood などに応じた立ち絵画像の選択を担当します。 |

## `src/maid_discord_bot/web/`

FastAPI など、Discord Bot 以外の Web エンドポイントを置きます。主に 42 OAuth の callback を受ける用途です。

| パス | 役割 |
|---|---|
| `app.py` | FastAPI アプリ本体を定義します。 |
| `oauth.py` | 42 OAuth callback や認証関連の Web 処理を担当します。 |

## `scripts/`

開発や運用で手動実行する補助スクリプトを置きます。

| パス | 役割 |
|---|---|
| `init_db.py` | SQLite の初期化やテーブル作成を実行するスクリプトです。 |

## `tests/`

自動テストを置きます。実装ディレクトリに合わせて、コマンド、DB、サービスの単位で分けます。

| パス | 役割 |
|---|---|
| `tests/commands/` | Discord コマンドの振る舞いを確認します。 |
| `tests/database/` | SQLite スキーマや repository の処理を確認します。 |
| `tests/services/` | EXP、Daily、42 API 連携などの業務ロジックを確認します。 |

## 基本方針

- Discord から直接呼ばれる処理は `commands/` に置く。
- 複数コマンドで使う処理は `services/` に置く。
- DB の読み書きは `database/repositories/` に寄せる。
- 表示の組み立ては `views/` に寄せる。
- 42 OAuth callback のような Web 処理は `web/` に置く。
- 起動、設定、定期実行は `bot.py`、`config.py`、`scheduler.py` に分ける。
