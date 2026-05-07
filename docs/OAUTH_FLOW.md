# OAuth認証フロー 完全解説

## 最初に：この認証はどんなロジックで動いているか

このシステムが解決したい問題は「**DiscordのユーザーとIntra 42のアカウントが同一人物であることを証明する**」ことです。

単純に「あなたのIntraログイン名は何ですか？」とDiscordで聞いてもなりすましができてしまいます。  
本当にそのIntraアカウントを持っているかどうかは、「42のサーバーにログインして許可ボタンを押せた」という事実で証明します。

しかしここに問題があります。

```
問題①: BotはDiscordを通してしか話せない。ブラウザを操作できない。
問題②: ブラウザで42にログインした後、「このブラウザの人はDiscordの誰だったのか」が分からなくなる。
```

この2つを解決するのが今回のシステム全体の設計です。

**解決策の全体ロジック：**

```
1. /register コマンドを受け取ったとき、「Discordのユーザーを識別できる情報」を
   URLの中に隠して持たせる（stateパラメータ）

2. ユーザーはそのURLをブラウザで開いて42にログインし「許可する」を押す

3. 42は許可後に、受け取ったstateをそのまま付けてWebサーバーへブラウザを転送する

4. WebサーバーはstateからDiscordのユーザーIDを取り出し、
   42のアカウントと紐付けてDBに保存する
```

ポイントは「**Discordのユーザー情報をURLに乗せて42経由で運ぶ**」という点です。  
BotとWebサーバーは直接通信しません。stateという文字列がリレーの役割を果たします。

---

## なぜ2つのプロセスが必要か

```
ターミナル①: python main.py           → Discord Bot プロセス
ターミナル②: uvicorn ... web/app.py  → Webサーバー プロセス
```

Discordコマンドはテキストベースのやり取りです。  
しかし「42にログインして許可ボタンを押す」操作は**ブラウザでしか行えません**。  
BotはブラウザのHTTPリクエストを受け取る機能を持っていないため、それを受け取るWebサーバーを別途立てる必要があります。

---

---

## 実行順序ブロック1：`python main.py` を叩いた瞬間

**このブロックでやること：PythonにsrcフォルダをimportできるようにしてBotを起動する**

```python
# main.py 1〜2行目
import sys
from pathlib import Path
```

普通のimport。まだ何もしていない。

```python
# main.py 5行目
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
```

- `__file__` は `/home/.../maid_discord_bot_twelve08274/main.py` という文字列
- `.parent / "src"` は `/home/.../maid_discord_bot_twelve08274/src` になる
- `sys.path.insert(0, ...)` は「Pythonがimportするとき、このフォルダも探してね」とリストの先頭に追加する

これをしないと次の `from maid_discord_bot.bot import run_bot` が「そんなモジュールはない」とエラーになる。

```python
# main.py 7行目
from maid_discord_bot.bot import run_bot
```

`src/maid_discord_bot/bot.py` を読み込む。このとき `bot.py` の `import` 文も全部実行される（関数の中身はまだ動かない）。

```python
# main.py 10〜11行目
if __name__ == "__main__":
    run_bot()
```

`python main.py` で直接実行したときだけ `run_bot()` が呼ばれる。  
`if __name__ == "__main__"` は「テストや他ファイルからimportされたときは実行しない」という慣用句。

---

## 実行順序ブロック2：`run_bot()` → Bot起動

**このブロックでやること：Botオブジェクトを作り、Discordに接続して待機状態に入る**

```python
# bot.py 32〜34行目
def run_bot() -> None:
    bot = create_bot()
    bot.run(get_discord_token())
```

`bot.run()` はここで「止まる」。内部でずっとDiscordからのメッセージを待ち続けるループが動く。  
プログラムはこの行から先に進まない（Ctrl+Cするまで）。

```python
# bot.py 27〜29行目
def create_bot() -> MaidBot:
    intents = discord.Intents.default()
    return MaidBot(command_prefix="!", intents=intents)
```

`intents` は「DiscordにBotが何のイベントを受け取りたいかを申告するオブジェクト」。  
スラッシュコマンドだけ使うなら `default()` で十分。  
`MaidBot(...)` でBotオブジェクトが作られる。この時点ではまだDiscordに繋いでいない。

`bot.run(token)` を呼ぶと、discord.pyがDiscordのサーバーに**WebSocket接続**する。  
WebSocketとは「繋ぎっぱなしにして、メッセージが来るたびに受け取れる双方向通信」のこと。  
HTTPと違い、一度繋いだら切らずに使い続ける。

---

## 実行順序ブロック3：`setup_hook()` → コマンドをDiscordに登録する

**このブロックでやること：Botが持つスラッシュコマンドをDiscordのサーバーに申請する**

```python
# bot.py 13〜24行目
class MaidBot(commands.Bot):
    async def setup_hook(self) -> None:
        register_ping_command(self)
        register_register_command(self)
        ...
        await self.tree.sync(guild=guild)
```

### なぜ `setup_hook()` が自動で呼ばれるのか

discord.pyの `Bot` クラスは内部でBotのライフサイクルを管理している。  
`bot.run()` を呼ぶと以下の順序で処理が進む：

```
1. bot.run() → Discordにログイン開始
2. WebSocket接続確立
3. setup_hook() を呼び出す ← ここ（discord.pyが自動で呼ぶ）
4. on_ready イベント発火（"ログイン完了"の通知）
5. 以後、イベント待機ループ
```

`setup_hook` は「コマンド登録やデータベース準備など、Botが動き始める前に必ず済ませておくべき初期化処理を書く場所」としてdiscord.pyが用意したフックメソッド。  
`setup_hook` という名前のメソッドを定義するだけで、接続後に自動的に呼ばれる。これはdiscord.pyの仕様であり、Pythonの継承の仕組みで実現されている。

```python
        test_guild_id = get_discord_test_guild_id()
        # 環境変数 DISCORD_TEST_GUILD_ID が "987654321" なら → int(987654321) が返る
        # 未設定なら → None が返る

        guild = discord.Object(id=987654321)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
```

`self.tree.sync()` はDiscordのAPIにHTTPリクエストを送る処理。  
「このBotは `/ping` と `/register` というコマンドを持っています」と申請する。  
Discordがこれを受け取って初めて、ユーザーのDiscordアプリで `/` を打ったとき候補に出てくる。

特定のギルドへの `sync` は即時反映。グローバルな `sync` は最大1時間かかるため、開発中はギルド指定が便利。

---

## 実行順序ブロック4：ユーザーが `/register` を打つ

**このブロックでやること：stateを作り、42の認証URLを組み立てて、ユーザーにDMで送る**

```python
# commands/register.py 9〜30行目
def register_register_command(bot: commands.Bot) -> None:
    @bot.tree.command(name="register", description="Start 42 account authentication.")
    async def register(interaction: discord.Interaction) -> None:
```

`@bot.tree.command(...)` はデコレータ。「この下の `register` 関数を `/register` コマンドとして扱う」という宣言。  
setup_hook のときにこの定義が `bot.tree` に登録される。実際にユーザーが打つまで中身は動かない。

`interaction` は「誰がどのサーバーのどのチャンネルでこのコマンドを叩いたか」という情報の塊。  
`interaction.user.id` でコマンドを叩いたユーザーのDiscord IDが取れる（例：`123456789`）。

```python
        state = create_oauth_state(interaction.user.id)
        authorization_url = create_authorization_url(state)

        await interaction.response.send_message(
            f"{authorization_url}\n\nThe link expires in 10 minutes.",
            ephemeral=True,
        )
```

`ephemeral=True` は「このメッセージはコマンドを叩いた本人にしか見えない」設定。

---

## 実行順序ブロック5：`create_oauth_state()` → 署名付きstateを作る

**このブロックでやること：Discord user_idを安全に運ぶための改ざん検知付き文字列を生成する**

```python
# services/oauth_state.py 22〜34行目
def create_oauth_state(discord_user_id: int, secret: str | None = None) -> str:
    if secret is None:
        secret = get_ft_state_secret()
    # secret = "mysupersecretkey32characters!!"  ← 環境変数 FT_STATE_SECRET の値
```

```python
    payload = {
        "discord_user_id": 123456789,
        "iat": 1746518400,           # int(time.time()) ← 現在のUnixタイムスタンプ
        "nonce": "Xk2mN9qLpRtY3vWz", # token_urlsafe(16) ← 毎回異なるランダム文字列
    }
```

### なぜ `token_urlsafe(16)` で毎回異なる文字列を入れるのか

同じ `discord_user_id` と同じ時刻でも、毎回異なる state を生成するためです。  
同じstateが再利用されると「リプレイ攻撃」という攻撃が可能になります：

```
悪意あるユーザーが以前のstateを保存しておき、
後からWebサーバーに再度送りつけて認証を通過させようとする攻撃
```

`token_urlsafe(16)` はOSの乱数ソース（`/dev/urandom` 等）から取得した、  
暗号論的に安全な16バイトのランダム文字列を生成する。毎回全く異なる値になるため、  
同じstateが2回生成されることは実用上ありえない。

```python
    payload_bytes = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    # separators=(",", ":") はスペースを省く設定（コンパクトなJSON）
    # json.dumps の結果: '{"discord_user_id":123456789,"iat":1746518400,"nonce":"Xk2m..."}'
    # .encode("utf-8") でバイト列に変換: b'{"discord_user_id":123456789,...}'
```

```python
    payload_part = _urlsafe_b64encode(payload_bytes)
```

### なぜBase64エンコードで「英数字と `-` `_` だけ」で表現できるのか

コンピュータが扱うデータは最終的に「0と1のビット列」です。  
例えば `{"a":1}` というJSON文字列を `utf-8` でバイト列にすると：

```
文字:  {      "     a     "     :     1     }
バイト: 0x7B  0x22  0x61  0x22  0x3A  0x31  0x7D
2進数: 01111011 00100010 01100001 00100010 00111010 00110001 01111101
```

このバイト列をURLに直接埋め込むと `%7B%22a%22%3A1%7D` のように `%XX` だらけになり、扱いにくい。

Base64は「6ビットずつ区切って64種類の文字に変換する」手法です：

```
元のビット列（8ビット単位）:
  01111011  00100010  01100001

6ビット単位に区切り直す:
  011110  110010  001001  100001

それぞれを0〜63の数値に変換:
  30      50      9       33

64種類の文字（A-Z, a-z, 0-9, -, _）にマッピング:
  e       y       J       h
```

64という数は「URLで安全に使える文字の種類」に合わせた設計です。  
バイナリデータをそのまま送る代わりに、必ず安全な文字だけで構成された文字列に変換できます。  
`urlsafe` 版は通常の `+/` の代わりに `-_` を使い、URLに直接埋め込めるようにしています。

```python
    signature = _sign(payload_part, secret)
    return f"{payload_part}.{signature}"
    # 結果例: "eyJkaXN...（長い文字列）".""Op8Sm3k...（署名）"
```

---

## 実行順序ブロック6：`create_authorization_url()` → 42の認証URLを組み立てる

**このブロックでやること：42のログインページに飛ぶためのURLを、必要な情報を全部付けて作る**

```python
# services/ft_api.py 28〜44行目
def create_authorization_url(state: str, ...) -> str:
    query = urlencode({
        "client_id":     "u-s4t2af-xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "redirect_uri":  "http://localhost:8000/oauth/42/callback",
        "response_type": "code",
        "scope":         "public",
        "state":         "eyJkaXN....Op8Sm3k",
    })
    return f"https://api.intra.42.fr/oauth/authorize?{query}"
```

### 各パラメータの意味

| パラメータ | 具体的な意味 |
|---|---|
| `client_id` | 42の開発者ページでアプリを登録したときに発行されたID。「私はこのアプリです」という名刺。これがないと42はどのアプリからのリクエストか分からない |
| `redirect_uri` | 認証が終わったら「ブラウザをここへ転送してください」という転送先URL。**42の管理画面に事前登録したものと完全一致しないと42が拒否する**。これにより悪意ある第三者が `redirect_uri` を自分のサーバーに書き換えても通らない |
| `response_type=code` | OAuth2には複数の認証方式がある。`code` は「認証コード方式」を使うという宣言。最初にブラウザを通じて一時的な「引換券（code）」をもらい、その後サーバー間通信でアクセストークンに交換する方式。ブラウザにアクセストークンを直接渡さないため最も安全 |
| `scope=public` | 「このユーザーのどの情報へのアクセスを許可してほしいか」の要求範囲。`public` は公開情報（名前、login名等）のみ。スコープを指定しないと不要な権限まで要求することになる |
| `state` | CSRF攻撃対策と、Discord user_idを運ぶための署名付き文字列（ブロック5で作ったもの）。42はこの値を変えずにそのままコールバックURLに付けて転送してくれる |

`urlencode` は辞書を `key=value&key=value` 形式の文字列に変換し、特殊文字を `%XX` にエスケープする。

---

## 実行順序ブロック7：ブラウザが42にアクセスする

**このブロックでやること：ユーザーが42のログインページを開いて「許可する」を押す**

```
ブラウザが https://api.intra.42.fr/oauth/authorize?... にGETリクエストを送る
```

### 「このBotとは無関係」とはどういう意味か

この通信はブラウザと42のサーバーの間で直接行われています。  
BotのWebサーバーは一切関与していません。

```
（関与している）
ブラウザ ───GETリクエスト──→ 42のサーバー

（関与していない）
Botのプロセス①  ← この通信には一切タッチしていない
Webサーバープロセス②  ← この通信には一切タッチしていない
```

BotがしたことはURLを作ってDiscordに送っただけ。  
ブラウザがそのURLを開くのはユーザーの操作であり、Botの制御外です。  
42のログイン画面もHTML・CSSも全部42のサーバーが返しています。

ユーザーが「Authorize」を押すと、42のサーバーがブラウザに対してこう命令します：

```
HTTP/1.1 302 Found
Location: http://localhost:8000/oauth/42/callback?code=AbCdEf1234&state=eyJkaXN....Op8Sm3k
```

`302 Found` はHTTPのリダイレクト命令。「このURLに移動してください」という意味。  
ブラウザは自動的にそのURLに移動します。このとき `code` と `state` が付いてきます。

`code` は「ユーザーが許可した」という42が発行した一時的な引換券。有効期限は数分。

---

## 実行順序ブロック8：Webサーバーがコールバックを受け取る

**このブロックでやること：ブラウザから届いたcodeとstateを受け取り、処理を開始する**

```python
# web/oauth.py 16〜20行目
@router.get("/oauth/42/callback", response_class=HTMLResponse)
async def ft_oauth_callback(
    code: str = Query(...),
    state: str = Query(...),
) -> str:
```

### なぜURLのクエリパラメータを自動的に受け取れるのか

ブラウザが送るHTTPリクエストの中身はこうなっています：

```
GET /oauth/42/callback?code=AbCdEf1234&state=eyJkaXN....Op8Sm3k HTTP/1.1
Host: localhost:8000
```

FastAPIはこのリクエストを受け取ると、次のように処理します：

```
1. URLパスの "/oauth/42/callback" を見て → @router.get("/oauth/42/callback") の関数を探す
2. "?" 以降の文字列 "code=AbCdEf1234&state=eyJkaXN..." を "&" で分割してキーと値のペアにする
3. 関数の引数を見る: code: str = Query(...), state: str = Query(...)
4. "code" という名前のクエリパラメータ → 引数 code に "AbCdEf1234" を代入
5. "state" という名前のクエリパラメータ → 引数 state に "eyJkaXN..." を代入
6. 関数を呼び出す
```

`Query(...)` の `...`（エリプシス）は「このパラメータは必須」という意味。URLに `code=` が含まれていなければFastAPIが自動的に400エラーを返す。

---

## 実行順序ブロック9：stateの検証

**このブロックでやること：受け取ったstateが改ざんされていないか・期限切れでないかを確認する**

```python
# services/oauth_state.py 37〜69行目
def parse_oauth_state(state: str, ...) -> OAuthState:
    payload_part, signature = state.split(".", 1)
    # state = "eyJkaXN...".""Op8Sm3k..." をドットで分割
    # payload_part = "eyJkaXN..."
    # signature    = "Op8Sm3k..."
```

```python
    expected = _sign(payload_part, secret)
    # Webサーバー側で FT_STATE_SECRET を使って同じ計算をする
    # secret が同じなら expected = "Op8Sm3k..."（Botが生成したときと同じ値になるはず）

    if not hmac.compare_digest(signature, expected):
        raise OAuthStateError("Invalid OAuth state signature.")
    # 受け取った signature と今計算した expected が一致 → 改ざんなし
    # 不一致なら誰かが state を書き換えている → 拒否
```

`hmac.compare_digest()` を `==` の代わりに使う理由：  
`==` は最初の文字から順に比べ、不一致が見つかった時点で止まるため、  
処理時間が「何文字一致したか」によって変わる。これを悪用してタイミング差を測ることで  
署名を少しずつ推測する「タイミング攻撃」が可能になる。  
`compare_digest` は必ず全文字比較するため処理時間が一定になり、この攻撃を防げる。

```python
    payload = json.loads(_urlsafe_b64decode(payload_part))
    # Base64デコード → JSON文字列 → Pythonの辞書
    # payload = {"discord_user_id": 123456789, "iat": 1746518400, "nonce": "Xk2m..."}

    if int(time.time()) - issued_at > max_age_seconds:
        raise OAuthStateError("OAuth state has expired.")
    # 現在時刻 - 1746518400 > 600 なら期限切れ（10分以上経過）→ 拒否

    return OAuthState(discord_user_id=123456789, issued_at=1746518400, nonce="Xk2m...")
```

---

## 実行順序ブロック10：codeをアクセストークンに交換する

**このブロックでやること：一時的な引換券（code）を、42 APIを叩けるアクセストークンに変える**

```python
# services/ft_api.py 47〜73行目
async def exchange_code_for_token(code: str, ...) -> FtToken:
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(
            "https://api.intra.42.fr/oauth/token",
            data={
                "grant_type":    "authorization_code",
                "client_id":     "u-s4t2af-xxx",
                "client_secret": "s-s4t2af-yyy",  # FT_CLIENT_SECRET（秘密）
                "code":          "AbCdEf1234",     # ブラウザ経由で受け取った引換券
                "redirect_uri":  "http://localhost:8000/oauth/42/callback",
            },
        )
```

この通信は**BotのWebサーバーから42のサーバーへ**のHTTPリクエスト。ブラウザは関与しない。  
`client_secret` を送る必要があるため、ブラウザに見せられない。  
だからこそサーバー側（Webサーバープロセス）でやる必要がある。

`async with httpx.AsyncClient() as client:` は「HTTPクライアントを作って、このブロックを抜けたら自動でコネクションを閉じる」という意味。  
`await client.post(...)` は「POSTリクエストを送って、レスポンスが返るまで待つ（その間他の処理を進められる）」という意味。

42が返すレスポンス（JSON）：

```json
{
    "access_token": "eyJhbGciOiJSUzI1...",
    "token_type": "bearer",
    "expires_in": 7200,
    "refresh_token": "abcdefghijklmnop",
    "scope": "public",
    "created_at": 1746518410
}
```

```python
    payload = response.json()
    expires_in = int(payload.get("expires_in", 7200))
    return FtToken(
        access_token="eyJhbGciOiJSUzI1...",
        refresh_token="abcdefghijklmnop",
        expires_at=datetime.now(UTC) + timedelta(seconds=7200),
        # expires_at = 現在時刻 + 2時間 = このトークンの有効期限
    )
```

---

## 実行順序ブロック11：アクセストークンで42ユーザー情報を取得する

**このブロックでやること：アクセストークンを使って「このトークンの持ち主は誰か」を42に聞く**

```python
# services/ft_api.py 76〜85行目
async def fetch_current_user(access_token: str) -> FtUser:
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            "https://api.intra.42.fr/v2/me",
            headers={"Authorization": "Bearer eyJhbGciOiJSUzI1..."},
        )
```

`Authorization: Bearer <トークン>` はHTTPヘッダの形式。  
`Bearer` は「私はこのトークンの持ち主です」という意味。  
42はこのトークンを見て「このトークンを持っているなら、そのユーザーの情報を返してよい」と判断する。

42が返すレスポンス（JSON、実際はもっと大きい）：

```json
{
    "id": 98765,
    "login": "jdoe",
    "email": "jdoe@student.42.fr",
    ...
}
```

```python
    return FtUser(id=98765, login="jdoe")
```

---

## 実行順序ブロック12：DBへの保存

**このブロックでやること：DiscordユーザーIDと42アカウントをSQLiteに紐付けて保存する**

```python
# web/oauth.py 35〜49行目
with get_connection() as connection:
```

`with` はここを抜けるとき自動的に `connection.close()` を呼ぶ。  
SQLiteとのコネクションが確実に閉じられるため、ファイルのロックが残り続ける問題を防ぐ。

```python
    user_id = get_or_create_user_id(connection, 123456789)
```

`get_or_create_user_id()` の中：

```python
# database/repositories/users.py 7〜23行目
row = connection.execute(
    "SELECT id FROM users WHERE discord_user_id = ?",
    ("123456789",),
).fetchone()

if row is not None:
    return int(row["id"])   # 既存ユーザーならそのIDを返す

cursor = connection.execute(
    "INSERT INTO users (discord_user_id) VALUES (?)",
    ("123456789",),
)
connection.commit()
return int(cursor.lastrowid)
```

### `cursor.lastrowid` とは何か

SQLiteは `AUTOINCREMENT` の列に対して行を挿入するとき、  
「今まで使ったことのない最大のID + 1」を自動的に割り当てます。

```
INSERTする前: users テーブルにまだ行がない
INSERT後:     id=1, discord_user_id="123456789" の行が作られる
cursor.lastrowid = 1  ← 今作られた行のID
```

`cursor` は `connection.execute()` が返すオブジェクトで、直前に実行したSQLの結果情報を持っている。  
`lastrowid` はその中の「直前のINSERTで作られた行のID」を表す属性。  
これにより、INSERT後に「今作った行のIDは何番か」を知ることができる。

```python
upsert_ft_link(
    connection,
    user_id=1,
    ft_user_id=98765,
    ft_login="jdoe",
    access_token="eyJhbGci...",
    refresh_token="abcdefgh...",
    token_expires_at=datetime(2026, 5, 6, 10, 0, 0, tzinfo=UTC),
)
```

```python
# database/repositories/ft_links.py
connection.execute(
    """
    INSERT INTO ft_links (user_id, ft_user_id, ft_login, ...)
    VALUES (?, ?, ?, ...)
    ON CONFLICT(user_id) DO UPDATE SET
        ft_user_id = excluded.ft_user_id,
        ...
    """,
    (1, "98765", "jdoe", "eyJhbGci...", "abcdefgh...", "2026-05-06T10:00:00+00:00"),
)
connection.commit()
```

`ON CONFLICT(user_id) DO UPDATE SET ...` はSQLの構文。  
`user_id` が既にテーブルに存在するとき、INSERTをせずにUPDATEとして扱う。  
`excluded.ft_user_id` は「今INSERTしようとした値」を指すSQLの記法。  
2回目以降に `/register` を叩いたとき、新しい行を作らず既存行を上書きする。

---

## 最後：ブラウザにHTMLを返す

**このブロックでやること：処理完了をブラウザに通知するHTMLページを返す**

```python
# web/oauth.py 51〜57行目
return (
    "<!doctype html>"
    "<html>..."
    "<body><h1>42 account linked</h1>..."
)
```

FastAPIがこの文字列をHTTPレスポンスのボディとして返す。  
ブラウザがそれを受け取ってHTMLとして表示する。  
ユーザーのブラウザに「42 account linked」と表示される。

---

## 全処理の実行順序まとめ

```
--- python main.py 起動 ---

1.  sys.path に src を追加
2.  bot.py が import される（関数の定義だけ読み込まれる）
3.  run_bot() が呼ばれる
4.  MaidBot オブジェクトが作られる
5.  bot.run(token) でDiscordにWebSocket接続
6.  discord.pyがsetup_hook()を自動で呼ぶ
7.  register_register_command(self) で register 関数を bot.tree に登録
8.  tree.sync() でDiscordに「/registerコマンドがあります」とHTTPリクエスト
9.  以後、bot.run() はWebSocketを待ち続ける ← ここで止まる

--- ユーザーが /register を打つ ---

10. Discordから「user_id=123456789 が /register を実行」がWebSocket経由で届く
11. register(interaction) が呼ばれる
12. create_oauth_state(123456789) が呼ばれる
13.   payload = {"discord_user_id":123456789, "iat":1746518400, "nonce":"Xk2m..."}
14.   payload → JSON文字列 → バイト列 → Base64文字列 (payload_part)
15.   HMAC-SHA256(payload_part, secret) → Base64文字列 (signature)
16.   state = "payload_part.signature" を返す
17. create_authorization_url(state) でURLを組み立てる
18. interaction.response.send_message(url, ephemeral=True) でDiscordにURLを返す

--- ユーザーがブラウザでURLを開く（BotもWebサーバーも関与しない）---

19. ブラウザが https://api.intra.42.fr/oauth/authorize?...&state=xxx に GET
20. 42がログイン画面のHTMLを返す
21. ユーザーがログインして「Authorize」を押す
22. 42がブラウザに http://localhost:8000/oauth/42/callback?code=AbCd&state=xxx へ
    302リダイレクト命令を送る
23. ブラウザが自動的にそのURLへ移動する

--- Webサーバーがコールバックを受け取る ---

24. FastAPIが GET /oauth/42/callback?code=AbCd&state=xxx を受け取る
25. URLのクエリ文字列をパースして code="AbCd", state="xxx" を取り出す
26. ft_oauth_callback(code="AbCd", state="xxx") が呼ばれる
27. parse_oauth_state(state)
28.   state を "." で分割 → payload_part, signature
29.   HMAC-SHA256(payload_part, secret) を再計算 → expected
30.   signature == expected か検証 → OK
31.   payload_part を Base64デコード → JSON → discord_user_id=123456789 を取り出す
32.   発行時刻が10分以内か確認 → OK
33.   OAuthState(discord_user_id=123456789, ...) を返す
34. exchange_code_for_token("AbCd")
35.   POST https://api.intra.42.fr/oauth/token に code, client_secret 等を送る
36.   42がアクセストークンを返す: {"access_token":"eyJ...", "expires_in":7200, ...}
37.   FtToken(access_token="eyJ...", ...) を返す
38. fetch_current_user("eyJ...")
39.   GET https://api.intra.42.fr/v2/me に Authorization: Bearer eyJ... を付けて送る
40.   42がユーザー情報を返す: {"id":98765, "login":"jdoe", ...}
41.   FtUser(id=98765, login="jdoe") を返す
42. get_or_create_user_id(connection, 123456789)
43.   SELECT id FROM users WHERE discord_user_id = '123456789' → 結果なし（初回）
44.   INSERT INTO users (discord_user_id) VALUES ('123456789')
45.   cursor.lastrowid = 1 → user_id = 1 を返す
46. upsert_ft_link(connection, user_id=1, ft_user_id=98765, ft_login="jdoe", ...)
47.   INSERT INTO ft_links ... ON CONFLICT DO UPDATE
48.   commit()
49. HTML文字列を返す → ブラウザに「42 account linked」が表示される
```
