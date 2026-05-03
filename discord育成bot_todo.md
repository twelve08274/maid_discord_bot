# Discord育成Bot TODOリスト

## 0. ゴール

**42にログインすると、自動でDaily報酬が入り、キャラが育つDiscord Bot** をまず完成させる。

優先順位は以下の通り。

1. キャラ育成
2. 生活支援
3. 42支援

---

## 1. 方針決定

- [ ] Bot名を決める
- [ ] メイド型・執事型・選択式のどれにするか決める
- [ ] 最初に使うDiscordサーバーを決める
- [ ] Bot用チャンネルを決める
- [ ] 管理者ロールを決める

---

## 2. 開発環境・基盤

### 2.1 Discord Bot基盤

- [ ] Discord Developer PortalでBotを作成
- [ ] Bot Tokenを取得
- [ ] BotをDiscordサーバーに招待
- [ ] Pythonプロジェクトを作成
- [ ] 仮想環境を作成
- [ ] `discord.py` を導入
- [ ] `python-dotenv` を導入
- [ ] `.env` でTokenを管理
- [ ] `/ping` コマンドを作成
- [ ] `/ping` がDiscord上で動くことを確認

### 2.2 DB基盤

- [ ] SQLiteを使う方針で決定
- [ ] DB接続処理を作成
- [ ] `schema.sql` を作成
- [ ] `users` テーブルを作成
- [ ] `daily_claims` テーブルを作成
- [ ] `achievements` テーブルを作成
- [ ] `user_achievements` テーブルを作成
- [ ] `tasks` テーブルを作成

---

## 3. キャラ育成コア

### 3.1 ユーザー登録

#### コマンド

```txt
/register
```

#### TODO

- [ ] `/register` コマンドを作成
- [ ] DiscordユーザーIDをDBに保存
- [ ] 初期ステータスを保存
- [ ] すでに登録済みならエラーではなく案内を返す

#### 初期ステータス

```txt
level = 1
exp = 0
stamina = 100
affection = 0
mood = normal
```

---

### 3.2 ステータス表示

#### コマンド

```txt
/status
```

#### TODO

- [ ] `/status` コマンドを作成
- [ ] levelを表示
- [ ] expを表示
- [ ] staminaを表示
- [ ] affectionを表示
- [ ] moodを表示
- [ ] 最終ログイン日を表示
- [ ] Embed表示にする
- [ ] 後で立ち絵画像を表示できる形にする

---

### 3.3 EXP・レベルアップ

#### TODO

- [ ] EXP加算処理を作成
- [ ] レベルアップ判定を作成
- [ ] 必要EXPを `level * 100` にする
- [ ] レベルアップ時にlevelを更新
- [ ] 余ったEXPを保持する
- [ ] レベルアップ通知を出す

#### 報酬例

```txt
42ログインDaily: EXP +10
/done: EXP +20
/study: EXP +5
/review-message: EXP +5
/food: EXP +3
```

---

### 3.4 stamina・affection・mood

#### TODO

- [ ] staminaを保存する
- [ ] affectionを保存する
- [ ] コマンド利用時にaffectionを増やす
- [ ] 42ログインDailyでstaminaを回復する
- [ ] 放置日数に応じてstaminaを下げる
- [ ] staminaからmoodを判定する
- [ ] `/status` にmoodを表示する

#### mood案

```txt
stamina >= 70: 元気
stamina >= 40: 普通
stamina < 40: 疲れ気味
stamina < 20: しょんぼり
```

---

### 3.5 立ち絵

#### TODO

- [ ] `assets` フォルダを作成
- [ ] `normal.png` を用意
- [ ] `happy.png` を用意
- [ ] `tired.png` を用意
- [ ] `sleepy.png` を用意
- [ ] `levelup.png` を用意
- [ ] moodに応じて表示画像を切り替える
- [ ] `/status` のEmbedに画像を表示する

---

## 4. 42 API連携

### 4.1 42 API準備

- [ ] 42 APIアプリを作成
- [ ] Client IDを取得
- [ ] Client Secretを取得
- [ ] Redirect URIを決める
- [ ] `.env` に42 API情報を保存

#### `.env` 例

```env
DISCORD_TOKEN=xxxxx
FT_CLIENT_ID=xxxxx
FT_CLIENT_SECRET=xxxxx
FT_REDIRECT_URI=http://localhost:8000/oauth/42/callback
DATABASE_URL=maid.db
```

---

### 4.2 42アカウント連携

#### コマンド

```txt
/link42
```

#### TODO

- [ ] `/link42` コマンドを作成
- [ ] 42 OAuth認証URLを生成
- [ ] ユーザーに認証URLを送る
- [ ] FastAPIでOAuth callbackを受ける
- [ ] codeからaccess_tokenを取得
- [ ] refresh_tokenを取得
- [ ] `/v2/me` で42ユーザー情報を取得
- [ ] DiscordユーザーIDと42ユーザーIDを紐づける
- [ ] `ft_links` テーブルに保存

---

### 4.3 トークン管理

- [ ] access_tokenの期限を保存
- [ ] `token_expires_at` を保存
- [ ] 期限切れを判定
- [ ] refresh_tokenでaccess_tokenを更新
- [ ] 更新後のtokenをDBに保存
- [ ] refresh失敗時は再連携を促す

---

### 4.4 手動チェックイン

#### コマンド

```txt
/checkin
```

#### TODO

- [ ] `/checkin` コマンドを作成
- [ ] 42連携済みか確認
- [ ] 42 APIでlocation履歴を取得
- [ ] 今日のlocation履歴があるか確認
- [ ] 今日未受け取りならDaily付与
- [ ] 受け取り済みなら案内
- [ ] 未ログインなら案内

---

### 4.5 自動Daily

#### コマンド

```txt
/autodaily on
/autodaily off
```

#### TODO

- [ ] `/autodaily on` コマンドを作成
- [ ] `/autodaily off` コマンドを作成
- [ ] `auto_daily_enabled` をDBに保存
- [ ] APSchedulerを導入
- [ ] 30分ごとの自動チェック処理を作成
- [ ] `auto_daily_enabled = true` のユーザーを取得
- [ ] 各ユーザーの42 location履歴を確認
- [ ] 今日ログイン済みならDaily付与
- [ ] 付与済みならスキップ
- [ ] Daily付与後にDM通知する
- [ ] API制限に引っかからないように間隔を調整

#### Daily付与条件

```txt
今日のlocation履歴が1件以上ある
かつ
今日まだDailyを受け取っていない
```

---

## 5. アチーブメント

### 5.1 基本実績

#### コマンド

```txt
/achievements
```

#### TODO

- [ ] `achievements` テーブルを作成
- [ ] 初期アチーブメントを登録
- [ ] `user_achievements` テーブルを作成
- [ ] 実績解除判定を作成
- [ ] `/achievements` コマンドを作成
- [ ] 達成済み実績を表示
- [ ] 未達成実績を表示するか決める

#### 実績案

- [ ] 初めての登録
- [ ] 初めての42ログインDaily
- [ ] 3日連続ログイン
- [ ] 7日連続ログイン
- [ ] 初めての課題完了
- [ ] 課題3個完了
- [ ] 課題5個完了
- [ ] Lv.5到達
- [ ] Lv.10到達
- [ ] 初めてのレビュー募集
- [ ] 初めての課題並走募集

---

## 6. 42支援機能

### 6.1 課題完了登録

#### コマンド

```txt
/done push_swap
```

#### TODO

- [ ] `/done` コマンドを作成
- [ ] 課題名を引数で受け取る
- [ ] `tasks` テーブルに保存
- [ ] 同じ課題を重複登録しないようにする
- [ ] EXP +20
- [ ] affection +5
- [ ] アチーブメント判定

---

### 6.2 最近終わった人紹介

#### コマンド

```txt
/who-done push_swap
```

#### TODO

- [ ] `/who-done` コマンドを作成
- [ ] 課題名を引数で受け取る
- [ ] その課題を最近完了した人を取得
- [ ] 完了日時順に表示
- [ ] 「レビュー可能」とは断定しない文面にする

---

### 6.3 課題並走募集

#### コマンド

```txt
/study minishell
```

#### TODO

- [ ] `/study` コマンドを作成
- [ ] 課題名を引数で受け取る
- [ ] 募集メッセージを投稿
- [ ] 参加用リアクションを付ける
- [ ] `study_posts` テーブルに保存
- [ ] EXP +5
- [ ] affection +2

---

### 6.4 レビュー募集文面生成

#### コマンド

```txt
/review-message push_swap
```

#### TODO

- [ ] `/review-message` コマンドを作成
- [ ] 課題名を引数で受け取る
- [ ] 汎用レビュー募集文を生成
- [ ] 必要なら時間帯も引数で受け取れるようにする
- [ ] EXP +5
- [ ] affection +1

---

## 7. 生活支援機能

### 7.1 天気予報

#### コマンド

```txt
/weather
```

#### TODO

- [ ] 天気APIを選ぶ
- [ ] APIキーを取得
- [ ] `.env` に保存
- [ ] `/weather` コマンドを作成
- [ ] 今日の天気を表示
- [ ] EXP +1 または affection +1

---

### 7.2 傘通知

#### コマンド

```txt
/umbrella
```

#### TODO

- [ ] `/umbrella` コマンドを作成
- [ ] 降水確率を取得
- [ ] 雨なら傘をすすめる
- [ ] 晴れなら不要と返す
- [ ] 朝の自動通知に組み込むか決める

---

### 7.3 ご飯募集

#### コマンド

```txt
/food
```

#### TODO

- [ ] `/food` コマンドを作成
- [ ] 時間を指定できるようにする
- [ ] 場所を指定できるようにする
- [ ] 募集メッセージを投稿
- [ ] 🍚リアクションを付ける
- [ ] `food_posts` テーブルに保存
- [ ] EXP +3
- [ ] 参加者にもEXPを付けるか決める

---

## 8. 後回し機能

### 8.1 プライバシー・荒れやすい機能

以下は最初は作らない。

- [ ] 匿名TIG告発
- [ ] 座席共有
- [ ] レビューする人の席の地図送信
- [ ] 本科生予報
- [ ] evapoを明らかにするbot
- [ ] 煽りbot

作る場合の条件：

- [ ] 本人の明示的な許可制にする
- [ ] 管理者用ログを残す
- [ ] 通報・削除機能を作る
- [ ] 公開範囲を制限する
- [ ] 位置情報をそのまま表示しない

---

## 9. 推奨スプリント

### Sprint 1：Bot基盤

- [ ] プロジェクト作成
- [ ] `discord.py` 導入
- [ ] `.env` 作成
- [ ] `/ping` 作成
- [ ] SQLite接続
- [ ] `users` テーブル作成

---

### Sprint 2：育成コア

- [ ] `/register`
- [ ] `/status`
- [ ] EXP加算
- [ ] レベルアップ
- [ ] stamina
- [ ] affection
- [ ] mood

---

### Sprint 3：42ログインDaily

- [ ] 42 APIアプリ作成
- [ ] `/link42`
- [ ] OAuth callback
- [ ] `ft_links` テーブル
- [ ] `/checkin`
- [ ] `daily_claims` テーブル
- [ ] 自動Daily

---

### Sprint 4：見た目強化

- [ ] Embed整備
- [ ] 立ち絵画像表示
- [ ] mood別画像切り替え
- [ ] levelup演出
- [ ] `/achievements`

---

### Sprint 5：42支援

- [ ] `/done`
- [ ] `/who-done`
- [ ] `/study`
- [ ] `/review-message`

---

### Sprint 6：生活支援

- [ ] `/weather`
- [ ] `/umbrella`
- [ ] `/food`

---

## 10. 最初のMVP範囲

最初に完成させる範囲は以下。

- [ ] `/ping`
- [ ] `/register`
- [ ] `/status`
- [ ] EXP・Level
- [ ] stamina・affection・mood
- [ ] `/link42`
- [ ] `/checkin`
- [ ] 自動Daily
- [ ] 立ち絵表示

---

## 11. 最終的な方向性

```txt
登録する
↓
42アカウントと連携する
↓
42にログインする
↓
Botが自動でDailyを付与する
↓
キャラが育つ
↓
/statusで成長を見る
↓
/achievementsで達成感を見る
```

まずは **「42にログインすると育つキャラBot」** を完成させる。
