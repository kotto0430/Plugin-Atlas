# Plugin Atlas スクリーンショット収集ログ

更新日: 2026-11-13 (JST)
対象リポジトリ: https://github.com/kotto0430/Plugin-Atlas
作業ブランチ: `feature/popular-17-v3-12-20261113` （本番 `main` とは別）
対象PR: https://github.com/kotto0430/Plugin-Atlas/pull/2

## 進捗（確認済みのスクショのみ）

- 受領: ChatGPTアプリ「人気」一覧のスクショ **7枚**（第1セット、2026-11-13）。
- 読み取った重複を除く候補: **50件**。
- v3.11の`main`と名前が一致: **33件**。
- `main`に名前がない候補: **17件**。現在これらはv3.12案の作業ブランチ内に収録済み。
- `main`はまだv3.11（117件）。v3.12案の`index.html`は134件。公開承認・マージは別工程。
- スクショに表示されていることの確認と、アプリID・個別の機能・利用地域の公式検証は別。後者の未確認事項を確定情報として扱わない。

## 第1セット：人気（スクリーンショット7枚）

| No. | スクショ表示名 | Atlasでの候補名 | 収録状況 |
|---:|---|---|---|
| 1 | Gmail | Gmail | main既存 |
| 2 | Google Drive | Google Drive | main既存 |
| 3 | Health | Health | v3.12案に追加 |
| 4 | GitHub | GitHub | main既存 |
| 5 | Remote Desktop Co… | Remote Desktop Commander | v3.12案に追加 |
| 6 | Writing Style | Writing Style | v3.12案に追加 |
| 7 | Supabase | Supabase | main既存 |
| 8 | Outlook Email | Outlook Email | main既存 |
| 9 | Notion | Notion | main既存 |
| 10 | Google Calendar | Google Calendar | main既存 |
| 11 | Shopify | Shopify | main既存 |
| 12 | TinyFish | TinyFish | main既存 |
| 13 | Canva | Canva | main既存 |
| 14 | Vercel | Vercel | main既存 |
| 15 | Slack | Slack | main既存 |
| 16 | Metricool | Metricool | main既存 |
| 17 | Dropbox | Dropbox | main既存 |
| 18 | Data | Data | main既存 |
| 19 | Outlook Calendar | Outlook Calendar | main既存 |
| 20 | Exa | Exa | v3.12案に追加 |
| 21 | Firecrawl | Firecrawl | main既存 |
| 22 | Todoist | Todoist | main既存 |
| 23 | Lovable | Lovable | main既存 |
| 24 | vidIQ | vidIQ | main既存 |
| 25 | Sales | Sales | v3.12案に追加 |
| 26 | WPVibe | WPVibe | v3.12案に追加 |
| 27 | SharePoint | SharePoint | main既存 |
| 28 | Windsor.ai | Windsor.ai | main既存 |
| 29 | Parallel | Parallel | v3.12案に追加 |
| 30 | Higgsfield | Higgsfield | main既存 |
| 31 | Figma | Figma | main既存 |
| 32 | Interactive Brokers (… | Interactive Brokers (IBKR) | v3.12案に追加 |
| 33 | Browser | Browser | v3.12案に追加 |
| 34 | Trello | Trello | main既存 |
| 35 | Runway | Runway | main既存 |
| 36 | Airtable | Airtable | main既存 |
| 37 | Flaim Fantasy | Flaim Fantasy | v3.12案に追加 |
| 38 | Product Design | Product Design | main既存 |
| 39 | Daily Tarot | Daily Tarot | v3.12案に追加 |
| 40 | Google Contacts | Google Contacts | main既存 |
| 41 | Public Equity Investing | Public Equity Investing | v3.12案に追加 |
| 42 | HeyGen | HeyGen | main既存 |
| 43 | Descript | Descript | main既存 |
| 44 | Consensus | Consensus | v3.12案に追加 |
| 45 | Atlassian | Atlassian | main既存 |
| 46 | Wix | Wix | main既存 |
| 47 | Fitness AI Connector | Fitness AI Connector | v3.12案に追加 |
| 48 | Base44 | Base44 | v3.12案に追加 |
| 49 | Booking.com | Booking.com | v3.12案に追加 |
| 50 | Binance | Binance | v3.12案に追加 |

### 名前の照合に関する保留事項

- スクショ上の `Remote Desktop Co…` と `Interactive Brokers (…` は末尾が省略。v3.12案ではそれぞれ `Remote Desktop Commander` と `Interactive Brokers (IBKR)` として仮登録した。正式表記はアプリ詳細画面で再確認する。
- `Daily Tarot` は既存 `Tarot` と名称が近いが、別アプリとして扱っている。同一性は要確認。
- `Parallel` は `Parallel Search` などとの別名・同一性確認が必要。
- `Sales`・`Browser`・`Health` など一般名詞型の名称は別製品への誤対応に注意。
- 画像は存在確認の根拠。説明文・料金・地域・接続条件を調べるときは公式情報を優先する。

## 第2セット：PCのカテゴリ別スクリーンショット（B002）

- 受領日: **2026-11-13**、**11枚**（生産性向上7・人気2・新着/注目1・中小企業1）。
- 読み取ったアプリ表示枠: **338枠**。ページ境界の重複を除くと **289件の異なる名称**。
- v3.12案（134件）との名前の一致: **70件**。名前の不一致: **219件**。不一致は未収録候補であり、同一性の精査前に新規アプリと断定しない。
- **全11画像の左右2列すべてのアプリ名を、画像名・カテゴリ別にJSON保存済み**。
- [📂 B002アプリ名原本（JSON）](inventory/B002_2026-11-13.json)
- 既存カタログへの追加・公開はまだ行っていない。現時点では名前の保存と一次照合まで。

### B002 画像ごとの収集件数

| カテゴリ | 元画像 | 収集枠 |
|---|---|---:|
| 生産性向上 | 生産性向上１.png | 32 |
| 生産性向上 | 生産性向上2.png | 36 |
| 生産性向上 | 生産性向上3.png | 36 |
| 生産性向上 | 生産性向上4.png | 36 |
| 生産性向上 | 生産性向上5.png | 36 |
| 生産性向上 | 生産性向上6.png | 36 |
| 生産性向上 | 生産性向上7.png | 36 |
| 新着・注目 | 新着・注目.png | 22 |
| 中小企業 | 中小企業.png | 16 |
| 人気 | 人気１.png | 30 |
| 人気 | 人気2.png | 22 |

**未確認事項:** アプリ名の微細なスペル差・正式なplugin ID・機能・接続/利用条件・対応地域は公式情報と照合する。特にUIに見える`Codex Tasks (Internal/CCA)`等の内部向け名称は、一般公開可能性の確認を要する。

## 次の収集方法

1. KottoがPCで公式アプリ一覧を開いて、**最大10枚ずつ**チャットに送付する。
2. Yomiが画像を読み取り、**表示名・カテゴリ・重複候補・確認事項**をこのログに追記する。
3. 各回、GitHubの作業ブランチに保存し、コミットの成功を確認する。会話が変わってもこのファイルを読み直す。
4. 本番更新前に`main`と照合し、追加候補だけを作業ブランチで検証する。Kottoの公開承認までは`main`を変更しない。

## 収集バッチ履歴

| バッチ | 日付(JST) | カテゴリ | スクショ枚数 | ユニーク候補 | 状況 |
|---|---|---|---:|---:|---|
| B001 | 2026-11-13 | 人気 | 7 | 50 | 画像照合・v3.12案に17件追加済み |
| B002 | 2026-11-13 | 生産性向上／新着・注目／中小企業／人気 | 11 | 289 | 338掲載枠から重複除外。70件はv3.12案に一致、219件は未収録候補。原本JSON保存済み |

### 再開メモ

次のチャットで「Plugin Atlasのスクショ続きをやろう」と言われたら、この`SCREENSHOT_TRACKER.md`をGitHubから読み取って、直前までの受領バッチと既存登録を突き合わせること。画像を再送してもらう前にこのログを確認する。
