# テスト手順

このドキュメントでは、現在のコードを確認するためのテスト方法をまとめます。

## 方針

テストは大きく2段階に分けます。

1. mockを使ったローカルテスト
2. 本物のDiscordと42 OAuthを使った実通し確認

普段の開発では、まずmockテストでコードのロジックを確認します。外部サービスとの接続や設定値が正しいかは、最後に実通し確認で見ます。

## セットアップ

venvを使う場合:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`python` が見つからない場合は、Windowsの `py` ランチャーを使います。

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

次回以降は、プロジェクト直下でvenvを有効化してからテストします。

```powershell
.\.venv\Scripts\Activate.ps1
```

## まとめて確認する

現在は `scripts/check.py` で基本的な確認をまとめて実行できます。

```powershell
python scripts/check.py
```

このスクリプトでは、主に以下を確認します。

- Pythonファイルの構文チェック
- `unittest` による `tests/` 配下のテスト実行
- `flake8`
- `mypy`

`flake8` や `mypy` が未導入の場合は、先に `pip install -r requirements.txt` を実行してください。

## unittestを直接実行する

テストだけを実行したい場合:

```powershell
python -m unittest discover -s tests
```

OAuth/registerまわりでは、以下のような内容をmock中心で確認します。

- OAuth stateの生成・検証
- OAuth stateの改ざん検知
- 42 OAuth認証URLの生成
- SQLiteへの `users` / `ft_links` 保存
- 42 API部分をmockしたcallback処理
- `/register` 用メッセージ生成

mockテストでは、本物のDiscordや42 APIには接続しません。

## 個別チェック

構文チェック:

```powershell
python -m compileall main.py src scripts tests
```

flake8:

```powershell
python -m flake8 src tests scripts main.py
```

mypy:

```powershell
python -m mypy src
```

## 実通し確認

mockテストが通ったあとに、必要に応じて本物のDiscordと42 OAuthで確認します。

1. `.env` にDiscordと42 OAuthの値を設定する
2. `python scripts/init_db.py` でDBを初期化する
3. OAuth callback用Webサーバーを起動する
4. 別ターミナルでDiscord Botを起動する
5. Discordで `/register` を実行する
6. 返ってきたURLを開いて42で認証する
7. callback画面に `42 account linked` が出ることを確認する
8. SQLiteの `users` と `ft_links` にレコードが入ることを確認する

OAuth callback用Webサーバー:

```powershell
uvicorn maid_discord_bot.web.app:app --app-dir src --host 127.0.0.1 --port 8000
```

起動確認:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

Discord Bot:

```powershell
python main.py
```

## 注意点

- `.env` はコミットしない
- トークンやclient secretをテスト出力に出さない
- 普段はmockテストで確認する
- 本物のDiscordや42 APIを使う確認は、OAuthまわりを触った後やリリース前に行う
- `tests/` はGit管理対象のテストコード置き場として使う
