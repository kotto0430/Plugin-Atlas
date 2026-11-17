# Plugin Atlas 引き継ぎ地図（HANDOFF）

最終調査日：**2026-11-17（JST）**  
対象：**作業ブランチ** `feature/popular-17-v3-12-20261113`  
調査時のブランチ先頭：`0c8da5d62a75850ef7de276a5fe81e1e4999ba3a`  
リポジトリ：[kotto0430/Plugin-Atlas](https://github.com/kotto0430/Plugin-Atlas)  
公開サイト：[Plugin Atlas](https://kotto0430.github.io/Plugin-Atlas/)

> **最重要：収集済み ≠ 調査済み ≠ 公開済み ≠ 実動作確認済み。** この4つを混ぜないこと。本文の数値は上記コミットを調べた時点のスナップショットで、作業が進めば変わる。この文書自身は公開サイトの動作を変えない。

## 1. 30秒で分かる仕組み

Plugin Atlasは「ChatGPTで使うアプリを母語や目的から探すための**非公式ガイド**」です。GitHub Pagesで公開される静的Webサイトで、利用者の検索はブラウザの中で実行されます。独立したデータベースサーバーや、ChatGPTのインストール状態との自動同期はありません。

~~~text
【資料の収集】                         【利用者が見るサイト】
OpenAI公開プラグインページ             main の index.html
    ↓ collector.py                     ↑ 人が確認して公開作業
official-metadata.json /               │
pending-translation.json               │
    ↓ 人の確認・翻訳が必要               │
    └──────────────┐                  │
                    ▼                  │
ChatGPT公式ディレクトリ画面             │
    ↓ スクショ・PDF・Chromeの目視        │
inventory/ （収集証拠・候補・保留）     │
    ↓ 詳細ページで英文・提供元を確認     │
inventory/plugin_details/             │
    ↓ 日本語要約・用途タグ・制約を保存   │
    └──── 人が照合して反映 ──→ 作業版 index.html
                                      │
                 PRの確認・マージ・公開作業（まだ未実施）
                                      ↓
                              公開版 main / GitHub Pages
                                      ↓
                            利用者のブラウザで検索・表示
                                      ↓
                  お気に入りと言語設定は利用者端末内に保存
~~~

**注意：上の矢印「人が照合して反映」は、現在は自動化されていない。** 個別の詳細JSONに日本語要約を書いても、画面の説明文へ自動反映されるわけではない。

## 2. 倉庫の地図：どのファイルが何をする？

| 場所 | たとえ | 役割・注意 |
| --- | --- | --- |
| [`index.html`](index.html) | **店舗と商品棚** | 画面のHTML/CSS/JavaScript、表示用アプリ一覧、9言語の画面文言、検索辞書、説明辞書が大部分ここに直書きされている。現在の作業版の一覧は**3,941件**。 |
| [`collector.py`](collector.py) | **公開情報の仕入れ係** | `openai.com/business/plugins/`配下の公開ページを探索・解析するPython。ChatGPTのログイン済み個人ディレクトリを読み取るプログラムではない。 |
| [`.github/workflows/sync.yml`](.github/workflows/sync.yml) | **定期巡回のタイマー** | 毎週火曜日23:59（JST）に収集処理を実行する設定。手動起動も可能。収集レポートJSONだけをコミットし、サイト画面は自動変更しない。 |
| [`official-metadata.json`](official-metadata.json) | **既知の公開説明帳** | 収集係が取得した、認識済み公開ページの英語情報とハッシュ。確認時点は13件、最終成功日2026-11-10。 |
| [`pending-translation.json`](pending-translation.json) | **翻訳待ちの箱** | 取得できたが既知のIDに対応しない候補など。確認時点11件。「まだ掲載可能と確定した」という意味ではない。 |
| [`sync-report.json`](sync-report.json) | **巡回日誌** | 最終確認日、見つかったURL件数、解析ページ件数、変更候補、保留名。 |
| [`known-plugins.json`](known-plugins.json) | **収集係の名前照合表** | 「表示名 → 内部識別子」の対応。確認時点27件。3,941件全部のID辞書ではない。 |
| [`catalog.json`](catalog.json) | **旧版の多言語商品台帳** | `version: 2.5`、27件×9言語の個別説明など。**現在の3,941件を表示する中心データではない**。`autoSync: false`。 |
| [`inventory/`](inventory/) | **調査資料の保管庫** | スクショ/PDFからの抽出、Chrome目視記録、未確認候補、検証済み名称の証拠をカテゴリー・バッチごとに保存。 |
| [`inventory/plugin_details/`](inventory/plugin_details/) | **個別調査カルテ** | 正式表示名、提供元、版、元の説明文、日本語要約、用途タグ、制約、出典URL、確認状況。調査時点で個別JSON**366ファイル**（監査用JSONは除外）。 |
| [`SCREENSHOT_TRACKER.md`](SCREENSHOT_TRACKER.md) | **作業日誌** | 収集したバッチ、進捗、判読保留、再開位置、調査時に発見した説明の食い違い。途中から仕事を再開するときはまず読む。 |
| [`tools/pdf_inventory/`](tools/pdf_inventory/) | **PDFの文字切り出し工具** | 高解像度画像のタイトル領域を分割し、OCRの候補と原画像の照合証拠を残す。 |
| [`README.md`](README.md)、[`docs/`](docs/) | **利用者への案内** | ルートREADMEは英語、`docs/README.ja.md`など8言語。READMEに記載の「134件」は大規模な作業版データと未整合。 |
| `donation-preview.html`、`language-preview.html` | **別の表示試作** | 名前どおり別HTML。公開の入口は原則`index.html`。表示差は編集時に個別確認すること。 |
| [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/) | **問い合わせ用紙** | バグ報告、機能・アプリ掲載希望のGitHub Issueテンプレート。 |
| [`requirements.txt`](requirements.txt) | **収集係の道具リスト** | Pythonの`requests`、`beautifulsoup4`、`playwright`。PDF用の依存は別ファイル。 |

### 特に重要な区別

- **公開版**：`main` の `index.html`。前回確認時のv3.11は117件。公開サイトは通常このブランチ側を基準にする。GitHub Pagesの公開設定はこの調査だけでは変更していない。
- **作業版**：`feature/popular-17-v3-12-20261113` の `index.html`。実データの配列は3,941件。PR #2は調査時点でオープン、未マージ。
- **詳細調査**：`inventory/plugin_details/` に別保存。366個の詳細カルテがあることと、366個の説明が画面に反映されていることは**別**。
- **公式メタデータ自動収集**：`collector.py` が取得する対象は`openai.com`の公開ページ。スクショから集めた数千件の処理とは**別ルート**。

## 3. 「辞書」はどこにある？（ここが画面の心臓部）

作業版の `index.html` の `<script>` 内に以下の定義がある。独立した辞書ファイルへきれいに分割されているわけではない。大量のデータと画面プログラムが**1つのHTMLに同居**している。

| 変数名 | 現状の規模 | 意味 |
| --- | ---: | --- |
| `catalog` | **3,941件** | 画面に出すアプリの基本名簿。ID・名称・カテゴリー・アイコン・出典区分・観測日など。 |
| `locale` | **9言語** | ボタン、注意文、検索欄、マイアプリなどの画面文言。ja/en/eo/fr/es/de/pt/zh/ko。 |
| `catOrder` | **17カテゴリー** | 内部カテゴリーの順序を定義する英語名のリスト。 |
| `catNames` | **9言語×17カテゴリー** | カテゴリーの表示名を各言語へ変換する対訳表。 |
| `legacyDetail` | **42アプリ名** | 旧版から引き継いだ個別説明と依頼例。 |
| `legacyLocalized` | **42アプリ名** | 旧版アプリの、各言語の詳細説明・検索用別名・機能例・依頼例。 |
| `additionalLocalized` | **75アプリ名** | 追加された用途ガイドの多言語文面。個別の実操作が検証済みという意味ではない。 |
| `goalIndex` | **252個の目的・検索語** | 例：「漫画」「manga」などの表現から候補アプリ名へ結ぶ、目的別検索辞書。 |
| `detailLabels` | **9言語** | 「詳細確認済み」「用途ガイド」「未確認」など、詳細画面のラベル。 |
| `starterI18n` | **9言語** | 初心者向けの「漫画を作りたい」「メール整理」「中古品」選択画面。 |
| `starterChoices` | **3種類の入口** | 上の選択肢に対応する、候補アプリ名の固定リスト。 |
| `mercariText` | **9言語** | 日本向けメルカリについての個別説明・プロンプト。 |
| `messages`（後半の寄付パネル） | **9言語** | 炭酸水の寄付パネルに表示する文言。アプリ一覧とは別のスクリプト。 |

**辞書の検索順のポイント：** `openDetail()` で説明を表示するときは、アプリ名をキーに `legacyLocalized[p.name] || additionalLocalized[p.name]` を選ぶ。該当する個別文面がなければ一般的なカテゴリー説明にフォールバックする。**`inventory/plugin_details/*.json` を直接読み込む処理は、確認した `index.html` には存在しない。**

#### 内部名簿の1件のイメージ

~~~json
{
  "id": "atlas-pdf-finance-p03r23",
  "name": "GREI",
  "category": "Finance",
  "icon": "💰",
  "source": "directory",
  "checked": "2026-11-14"
}
~~~

- `id`：お気に入りの保存や表示で使うキー。`atlas-...` はサイト内の仮IDであり、**OpenAI公式アプリIDではない**。
- `name`：表示名。似た名前でも同じアプリとは限らない。
- `category`：画面内部で使う英語カテゴリー。`catNames` と `catOrder` を通して翻訳表示する。
- `icon`：一覧カードの絵文字。
- `source`：`directory`（ディレクトリ画面で観測）、`search`（検索で観測）、`connected`（連携機能を観測）、`catalog`（従来版）など。**インストール可否・実動作・安全性の証明ではない**。
- `checked`：観測した日付であり、公開後にリアルタイムで検証された日付ではない。
- 一部の項目には `aliases` や `description` があるが、全件に付くわけではない。

#### 個別調査カルテの形

例：[`inventory/plugin_details/drivethrough_2026-11-15.json`](inventory/plugin_details/drivethrough_2026-11-15.json)

主な項目は `official_app_name`（画面上の名前）、`provider`（提供元）、`version`、`source_url`（公式詳細画面のURL）、`observed_at`（確認日）、`original_description`（元の説明）、`summary_ja`（日本語要約）、`usage_tags`（用途）、`limitations` や `limitations_ja`（制約）、`verification_status`（確認状態）など。**カルテによって項目名・説明の言語・有無に違いがある**ため、画面へ反映する前に形式を揃える必要がある。

## 4. 実際の画面プログラムの動き

`index.html` では、HTMLが画面の部品、CSSが見た目、JavaScriptが動作と辞書を担う。

1. **起動**：`browserLanguage()` がブラウザの優先言語を読み、9言語なら採用。過去に選んだ言語が保存されていればそちらを優先。未対応なら英語。
2. **検索**：`matches(p,q)` がアプリ名・カテゴリー・別名・利用可能な多言語説明・機能例・`goalIndex` に照合。`searchRelevance(p,q)` が名前一致などに点数を付け、`visible()` が絞り込みと並べ替えを行う。中古品関連の検索ではメルカリを優先する特別な加点もある。**AIが毎回リアルタイムで探す方式ではなく、登録済みの文字列をブラウザ内で検索する方式。**
3. **カテゴリー**：`renderCategories()` が`catOrder`、`catNames` を使い、該当カテゴリーの件数とフィルタを表示。
4. **アプリカード**：`render()` が名前・アイコン・分類・情報確認状況・お気に入りボタン・詳細ボタンを生成。
5. **詳細画面**：`openDetail()` が多言語説明、例文、情報の出典、最終観測日を表示。個別説明がない場合は汎用説明に切り替え。
6. **ChatGPTで使う**：`makePrompt()` で依頼文を作り、`https://chatgpt.com/?q=...` を別タブで開く。**アプリを直接インストール・接続・起動するAPIではない。** 例文のコピーも可能。
7. **マイアプリ**：`toggleFavorite()` がお気に入りのID一覧をブラウザの`localStorage`へ保存。使用キーは`pluginAtlasFavorites_v1`。言語キーは`pluginAtlasLanguage`。初心者案内の表示設定は`pluginAtlasIntroDismissed_v1`。
8. **端末間移行**：お気に入りは`plugin-atlas-favorites.json`としてエクスポート・インポート可能。保存するのはIDと名前で、ChatGPTの接続済みアプリとは連動しない。
9. **名簿JSONの保存**：サイトの「一覧JSONを保存」ボタンから、埋め込み`catalog`・`legacyLocalized`・`additionalLocalized`・`goalIndex`をまとめて出力できる。**注意：ダウンロードするJSON内部の`version`は`3.11`、ファイル名は`v3.12`となっており、現状の件数・バージョン表記との整合性確認が必要。**
10. **寄付表示**：別のインラインスクリプトで9言語の炭酸水寄付案内を表示。アプリ収集やマイアプリとは独立。

## 5. 集め方の詳細：自動巡回と画面調査は別物

### A. 公開Webページの自動収集（`collector.py`）

- `BASE = https://openai.com/business/plugins/`。対象URLを`approved()`でHTTPSの`openai.com`配下に制限。
- `requests` と `BeautifulSoup` でページの`h1`、説明メタタグ、`How it works`などを抽出。
- オプション `--browser-discovery` はPlaywright/Chromiumで公開ページの`Load more`ボタンを追う。
- 既知名は`known-plugins.json`を通じてIDに対応付け、内容の`contentHash`を比較。未知の名前は`pending-translation.json`に保留する。
- 書き出すのは`official-metadata.json`、`pending-translation.json`、`sync-report.json`。
- 定期実行`.github/workflows/sync.yml`は`python collector.py --browser-discovery --max-pages 100 --max-clicks 40`を実行し、この3ファイルだけをGitに反映する。
- **新規候補の翻訳、カテゴリー付け、`index.html`への追加、3,941件との統合は自動ではない。**
- 画面収集の数千件を同じ場所から自動取得できる保証もない。収集元の構造が変われば対応が必要。

### B. スクショ・PDF・Chromeの収集（`inventory/`）

- `SCREENSHOT_TRACKER.md` が何枚・何行・どこまで確認したかの一次記録。
- `inventory/B003_verified/`：生産性向上PDFの検証済み出力。`extraction_raw.json`（機械抽出）、`review.json`（人の修正・保留）、`inventory.json`（統合）、`apps.csv`（表示名単位）、`rows.csv`（掲載枠単位）、`unconfirmed.csv`（判読保留）、`evidence/`（元画像切り出し）、`verification.md`（検証報告）。
- `inventory/B005_communication/` ～ `B013_business/`、`data_analytics_chrome/`、`scientific_research_chrome/`、`security_chrome/`、`other_chrome/`など：カテゴリー別のPDF証拠・目視記録・照合中のデータ。**フォルダごとに検証進度は異なる。**
- `tools/pdf_inventory/extract.py`：PDF内画像を直接抽出（条件が合わなければ高解像度レンダリング）、2列の文字領域を切り出し、Tesseract OCRで候補作成。画像証拠と生のOCR結果を保存し、OCR結果だけでは確定扱いにしない。
- `tools/pdf_inventory/b003-layout.json`：B003専用の画像幅、左右列の座標、輝度しきい値、OCR言語、作業数。別PDFへそのまま流用できるとは限らない。
- `tools/pdf_inventory/finalize.py`：`review.json`の人による目視修正、PDFのハッシュ、各列行数、ページ境界を検査し、CSV/JSON/検証報告へまとめる。`README.md`に実行例。
- **大文字I・小文字l・数字1、ページ境界、同名アプリ**は特に誤判定の原因。名前が分からないときは推測で埋めず保留。名前だけ一致しても同一アプリとは断定しない。

### C. 個々の説明の調査（`inventory/plugin_details/`）

- [`inventory/plugin_details/README.md`](inventory/plugin_details/README.md) が個別カルテの索引。
- ChatGPT公式ディレクトリの**詳細画面で見える**原文・提供元・URLなどを確認し、日本語要点と用途タグを別JSONへ記録する。
- 「公式画面の説明を確認した」と「実際に操作した」は区別する。料金・地域・インストール要件・アフィリエイト表示・解像度上限などで説明が食い違えば、両方保存して未確認にする。
- 調査時点の`plugin_details/`には**366件の個別JSON**、索引には**365件の個別リンク**。最新1件の索引更新が追い付いていない可能性がある。`catalog_name_audit_2026-11-14.json`は監査データで、個別アプリの1件に数えない。
- **調査済みカルテを既存`catalog`と公式IDで安全に突き合わせ、9言語の正式説明へ昇格させる工程は未完了。**

## 6. 最新の進捗と、読み間違えやすい数字

| 項目 | 2026-11-17調査時の状況 | 数字の意味 |
| --- | --- | --- |
| `main` | v3.11・117件（以前の公開版記録） | 本番側。作業版の数千件とは別。 |
| 作業版`index.html` | **3,941件・17カテゴリー** | ブラウザで表示する名簿。名前・仮ID中心で、全件の実動作は未検証。 |
| 作業版の詳細カルテ | **366個のアプリ詳細JSON** | 詳細画面の原文と要約など。検索画面への正式統合は別。 |
| 個別カルテ索引 | **365リンク** | 進捗の索引。一覧名との照合が全件完了した数字ではない。 |
| `catalog.json` | **27件×9言語** | 旧版の構造化データ。作業版の全アプリDBではない。 |
| `legacyLocalized` | **42件** | サイト内の詳しい多言語説明辞書。 |
| `additionalLocalized` | **75件** | サイト内の追加用途ガイド辞書。 |
| `goalIndex` | **252語** | 目的を表す検索語と候補アプリのマッピング。 |
| 定期巡回の出力 | 13既知＋11保留（2026-11-10時点） | 公開ページから取得した別ルートの情報。3,941件に足さない。 |
| PR #2 | オープン・未マージ | 既存`main`への反映は未実施。 |

**表記に注意：** `README.md`や`index.html`のタイトル・概要文に「134 apps」「v3.12」が残っているが、作業版`catalog`は実際には3,941件。名簿の実数と、説明・宣伝・エクスポートのバージョン表記にずれがある。**数だけ急に書き換えて公開せず**、データ品質と9言語の実態を確認してから揃える。

## 7. 次に手を入れるときの安全な順番

1. [`SCREENSHOT_TRACKER.md`](SCREENSHOT_TRACKER.md) の末尾と[個別詳細の索引](inventory/plugin_details/README.md)を開き、前回の再開位置・未確認事項・GitHub最新コミットを確認する。
2. **`main`か作業ブランチかを明示**し、通常は作業ブランチで変更案を作る。本番へのマージは所有者の承認後。
3. `inventory/`の生データは元の証拠として保存し、確認できていない名前を修正済みと偽らない。
4. 既存の名簿ID、公式詳細URL、提供元、説明文を突き合わせる。**仮IDと公式IDを混同しない。同名でも自動統合しない。**
5. 新しい詳細説明を公開する場合は、`legacyLocalized`・`additionalLocalized`など画面で実際に参照される辞書を確認し、言語ごとの未翻訳を明示する。
6. 検索（日本語名・別名・目的語）、カテゴリー、マイアプリ、9言語切り替え、スマホ表示、JSONインポート/エクスポート、「ChatGPTで使う」リンクをテストする。
7. 件数、カテゴリー数、バージョン、README、ページのメタ情報、名簿JSONの出力内容を揃えてからPRでレビューする。
8. 内容が確認できたら所有者の許可を得て公開する。収集用の`sync.yml`は画面を自動更新しないので、これとは別の公開フローが必要。

### 保留・リスクのメモ

- **最大の構造的課題**：画面のコードと数千件のデータが`index.html`の1ファイルに同居し、`inventory`の調査成果から表示用辞書への自動変換がない。今後の保守では、まず「元データ・翻訳・画面」を別工程に分けられるか検討するとよい。ただしこの文書作成だけでリファクタリングはしない。
- **同名・異名**：画像OCRの`I/l/1`など、違う公式URLで同名の掲載がある問題。必ず証拠を保存。
- **言語品質**：9言語UI対応と、3,941件すべての詳しい9言語説明が完成していることは別。
- **外部依存**：OpenAIの公開ページやディレクトリUIが変われば、収集・リンク先が変化する。
- **利用制約**：サイト上の「使う」は依頼文を開くだけ。アプリの接続・プラン・料金・地域・権限は別途確認。
- **セキュリティ**：個人のトークン、パスワード、メール本文、銀行情報などを`inventory`や公開Issueへ入れない。詳細カルテに残すのは公開説明に必要な情報だけ。

## 8. 次のAI・開発者が最初に読むリンク

1. [全体進捗：`SCREENSHOT_TRACKER.md`](SCREENSHOT_TRACKER.md)
2. [個別詳細：`inventory/plugin_details/README.md`](inventory/plugin_details/README.md)
3. [公開画面の本体：`index.html`](index.html)
4. [旧多言語データ：`catalog.json`](catalog.json)
5. [公開ページの収集：`collector.py`](collector.py)
6. [定期収集設定：`.github/workflows/sync.yml`](.github/workflows/sync.yml)
7. [PDFツールの使い方：`tools/pdf_inventory/README.md`](tools/pdf_inventory/README.md)
8. [PDF検証例：`inventory/B003_verified/verification.md`](inventory/B003_verified/verification.md)
9. [公開版`main`](https://github.com/kotto0430/Plugin-Atlas/tree/main) / [作業版ブランチ](https://github.com/kotto0430/Plugin-Atlas/tree/feature/popular-17-v3-12-20261113) / [PR #2](https://github.com/kotto0430/Plugin-Atlas/pull/2)

---

**このファイルの目的：** 初めて見る人でも、「どこで集める → どこに記録する → どう確かめる → どの辞書を使って表示する → どこから公開する」が追えるようにすること。**開発・収集の実装は変更しない。**
