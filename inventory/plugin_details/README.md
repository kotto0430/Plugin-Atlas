# プラグイン詳細の調査記録

ChatGPTのプラグイン詳細画面で、一覧の名前・短い説明だけでは機能が分かりにくい項目を優先して確認する。

各JSONには表示時の名前、提供元、バージョン、出典URL、英文の説明または確認した抜粋、日本語の要点、制約、確認状況を記録する。機能・対象・制約は提供元の画面表示に基づく。実際の動作、料金、対象地域は別途確認し、推測で埋めない。詳細画面の「続きを読む」は展開し、ページを下まで確認する。正式なプラグイン詳細ページの識別子と、一覧本体のサイト内仮IDは区別する。

## 記録項目

- `official_app_name`: ChatGPTのプラグイン詳細画面に表示された名前。別媒体の商標や同名アプリとの同一性は未確認。
- `original_description`: 詳細画面の英語説明原文。全文を取得できない場合は抜粋と明記し、出典を残す。
- `summary_ja`: 説明に基づく日本語の要点。
- `usage_tags`: 説明から確認できる用途だけを配列で記録。
- `verification_status`: 「公式説明を確認済み」「機能未検証」「説明だけでは不明」などを必要に応じて併記。公式説明を確認しても、実動作を検証したとは扱わない。
- `source_url`、提供元、観察日、必要な制約も記録。分からない項目は推測せず不明とする。

## 確認済み

- [Palimpsest](palimpsest_2026-11-14.json) — 公開記録・資料の出典、改訂や利用制限を調査。候補として記録、一覧本体未追加。
- [TradingCursor](tradingcursor_2026-11-14.json) — 株式、暗号資産、為替、ETFの複数シグナル分析。名前は一覧本体にあり。
- [IBI SMART](ibi_smart_2026-11-14.json) — 口座情報を閲覧する連携。プラットフォーム自体の取引機能と、この連携が読み取りのみと説明する範囲を区別。名前は一覧本体にあり。
- [Economic Mind](economic_mind_2026-11-14.json) — 市場規模・予測・競合情報のデータベース。名前は一覧本体にあり。

- [S&P Global - Deterministic](sp_global_deterministic_2026-11-14.json) — 自然言語による企業情報や財務・市場データの検索。名前は一覧本体にあり。

- [VODER](voder_2026-11-14.json) — Xeroなどの会計情報への質問。
- [Third Bridge](third_bridge_2026-11-14.json) — 専門家コンテンツやデータを企業・金融分析に活用。
- [CB Insights](cb_insights_2026-11-14.json) — 非上場企業や競合の調査。
- [Cube](cube_2026-11-14.json) — 実績・予算・予測の参照や差異分析。同名製品との同一性は未検証。
- [Parqet](parqet_2026-11-14.json) — 連携口座の資産や配当を確認し、ポートフォリオの記録を管理。実際の売買は行わないと説明。

- [Massive](massive_2026-11-14.json) — 株式、先物、為替などの市場データ。
- [Bigdata.com](bigdata_com_2026-11-14.json) — 出典付きの金融・企業リサーチ。情報源の範囲は権限などに依存。
- [Unusual Whales](unusual_whales_2026-11-14.json) — オプションの取引動向や市場データ。
- [Moneytree](moneytree_2026-11-14.json) — 連携データを使った残高や支出傾向の確認。
- [CryptoAudit](cryptoaudit_2026-11-14.json) — 暗号資産のチャートや指標、市場分析。

- [Rallies](rallies_2026-11-14.json) — 米国株の調査と連携した保有資産の確認。取引は執行しないと説明。
- [Synci](synci_2026-11-14.json) — 銀行・証券・暗号資産口座の読み取り連携。銀行の記載対象地域に注意。
- [Kubera](kubera_2026-11-14.json) — 資産・負債の確認と保有情報の更新例。
- [Co-Invest](co_invest_2026-11-14.json) — Liquidの市場調査と資産配分の検討。注文の扱いは要確認。
- [Accounting（OpenAI）](accounting_openai_2026-11-14.json) — 会計ソフトやワークブックでの記帳・報告・監査の支援。

- [StrategyTune: Backtesting](strategytune_backtesting_2026-11-14.json) — 過去の市場データを使った取引戦略の検証。
- [LONA™](lona_2026-11-14.json) — 文章やPythonを使った戦略作成と過去データの検証。
- [HyperFrames by HeyGen](hyperframes_by_heygen_2026-11-14.json) — HTML・CSSなどを使った動画制作。
- [Creative Claw](creative_claw_2026-11-14.json) — 絵コンテやキャラクターを使った動画・画像・音声制作。
- [Creative Production（OpenAI）](creative_production_openai_2026-11-14.json) — 企画や商品画像を基にした広告・SNS向け画像案の検討。

## 再開

金融とクリエイティブの一覧から詳細調査を開始。各詳細を開いた後に一覧へ戻ると先頭へ戻ることがあるため、再開時は上記の記録と重複しないよう名前と詳細ページを確認する。次の候補は、一覧の短文だけでは対象や提供範囲が曖昧な項目から選ぶ。カテゴリー全体の選別・詳細調査はまだ完了していない。
