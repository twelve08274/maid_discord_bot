# Project Management Rules

## 1. ブランチ戦略

### 基本構造

```txt
main        : 本番用（安定）
develop     : 開発統合
feature/*   : 新機能
fix/*       : バグ修正
docs/*      : ドキュメント
refactor/*  : リファクタリング
```

---

### 命名規則

```txt
種類/スプリント番号-内容
```

例：

```txt
feature/s1-ping-command
feature/s2-register-command
feature/s3-auto-daily
fix/token-load-error
docs/sprint-rules
refactor/db-layer
```

---

## 2. 開発フロー

```txt
① develop からブランチを切る
② 作業する
③ 動作確認する
④ PRを作る
⑤ develop にマージ
⑥ スプリント終了後 main にマージ
```

---

### 実際のコマンド

```bash
git checkout develop
git pull
git checkout -b feature/s1-ping-command
```

---

## 3. スプリントボード

### カラム構成

```txt
Backlog
Sprint Todo
In Progress
Review
Done
```

---

### 各カラムの意味

* Backlog：いつかやる
* Sprint Todo：今回やる
* In Progress：作業中
* Review：確認待ち
* Done：完了

---

## 4. タスクの粒度

### 原則

```txt
1タスク = 1機能
```

---

### 良い例

```txt
/ping コマンドを作る
SQLite接続を作る
usersテーブルを作る
```

---

### 悪い例

```txt
Botを作る
```

---

## 5. タスクテンプレ

```md
## 目的
何を作るか

## 完了条件
- [ ] 実装した
- [ ] 動作確認した
- [ ] エラー確認した
- [ ] PRを作成した

## branch
feature/sX-xxxx

## メモ
```

---

## 6. Pull Request ルール

```txt
タイトル：何をしたか
例：/ping コマンドを追加

内容：
- 何をしたか
- 動作確認方法
- 未解決の問題（あれば）
```

---

## 7. スプリントの進め方

### Sprint 1（Bot基盤）

```txt
- Bot作成
- /ping
- SQLite接続
- usersテーブル
```

---

### Sprint 2（育成）

```txt
- /register
- /status
- EXP
- level
```

---

### Sprint 3（42連携）

```txt
- /link42
- /checkin
- auto daily
```

---

## 8. ルール（重要）

```txt
・main は壊さない
・1タスク1ブランチ
・動かしてからマージ
・デカい変更は分割する
```
