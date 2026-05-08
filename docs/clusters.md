# 42Tokyo クラスタ レイアウト情報

## クラスタ一覧

| クラスタ | 名前 | フロア | 階段からの方向 | 入口列 (entrance_row) | s1側が入口か |
|---------|------|-------|--------------|----------------------|-------------|
| c1 | 鯉 (koi)   | 2F | 右 | R4 | Yes (s1が入口側) |
| c2 | 梅 (ume)   | 2F | 左 | R5 | No  (高番号席が入口側) |
| c3 | 鷲 (washi) | 3F | 右 | R4 | Yes (s1が入口側) |
| c4 | 富士 (fuji)| 3F | 左 | R3 | No  (高番号席が入口側) |
| c5 | 桜 (sakura)| 4F | 右 | R1 | No  (高番号席が入口側) |
| c6 | 鶴 (tsuru) | 4F | 左 | R4 | No  (高番号席が入口側) |

## SVGファイルと配置方向

`data/clusters/` に置かれているSVGファイル（拡張子なし）をレイアウトの元データとして使用。
プロジェクトルート直下には置かない。

| ファイル | クラスタ | 配置タイプ |
|---------|---------|----------|
| `data/clusters/c1-koi`   | c1 | row-based（行が水平方向） |
| `data/clusters/c2-ume`   | c2 | row-based |
| `data/clusters/c3-washi` | c3 | row-based |
| `data/clusters/c4-fuji`  | c4 | col-based（SVGの "row" グループが実際は縦列） |
| `data/clusters/c5-sakura`| c5 | col-based |
| `data/clusters/c6-tsuru` | c6 | col-based |

## 机・席の構造

- 1つの机に2台のPCがあり、**向かい合って**2人が座る
- SVG上では同じ行内に**2つのy座標レベル**（row-based）または**2つのx座標レベル**（col-based）として表現されている
- 奇数席と偶数席が互い違いに配置されているように見えるが、実際には1つの机の表と裏

## SVG パース上の注意点

### c1-koi の不正XML
- `style` 属性に二重の `""` が含まれておりXML的に不正
- 対策: `lxml` の `recover=True` モードで解析

### ミスラベルされた rect ID
- `c1-koi` の `group row06` 内に `id="c1r7s4"` という不正なrectが存在（本来は c1r6s7）
- `c3-washi` の `group row06` 内に `id="c3r7s4"` という不正なrectが存在（本来は c3r6s7）
- 検出方法: `rect` の行番号 ≠ `<g>` の行番号のとき
- 修正方法: x座標から席番号を逆算 `seat = round((280 - x) / 16) + 1`

## 画像レンダリング仕様

- Pillow で生成（SVGをそのまま変換しない）
- 向き: 90° 時計回り回転して横長
  - SVG の y軸（行方向）→ canvas の x軸（左右）
  - SVG の x軸（席方向）→ canvas の y軸（上下）、s1が上
- 出力サイズ・倍率は `src/services/seat_map.py` の `RENDER_TUNING` でクラスタごとに調整
  - `canvas_w`, `canvas_h`: GIF画像自体のサイズ
  - `scale`: fit後の追加倍率（端が切れない最大倍率で自動clamp）
  - `offset_x`, `offset_y`: 手動の位置補正
- 入口ラベル位置は `ENTRANCE_MARKERS` の canvas 座標で手動指定
- 色テーマ: Catppuccin Mocha ベース
- アニメーション: 対象席のドットが点滅する2フレームGIF（600ms間隔）
- 机ペアの可視化: 各行内で2つのy-levelを `±5 SVGユニット` だけ中心からずらして表示し、どちら側の席かを判別できるようにしている
