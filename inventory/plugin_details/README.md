# プラグイン詳細の調査記録

ChatGPTのプラグイン詳細画面で、一覧の名前・短い説明だけでは機能が分かりにくい項目を優先して確認する。

各JSONには表示時の名前、提供元、バージョン、出典URL、英文の説明または確認した抜粋、日本語の要点、制約、確認状況を記録する。機能・対象・制約は提供元の画面表示に基づく。実際の動作、料金、対象地域は別途確認し、推測で埋めない。詳細画面の「続きを読む」は展開し、ページを下まで確認する。正式なプラグイン詳細ページの識別子と、一覧本体のサイト内仮IDは区別する。

## 記録項目

- `official_app_name`: ChatGPTのプラグイン詳細画面に表示された名前。別媒体の商標や同名アプリとの同一性は未確認。
- `original_description`: 詳細画面に表示された説明原文（英語以外の場合は言語も記録）。全文を取得できない場合は抜粋と明記し、出典を残す。
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

- [Krea](krea_2026-11-14.json) — 画像・動画・3D素材の作成と管理。
- [Pollo AI](pollo_ai_2026-11-14.json) — 動画・画像・音楽・音声の生成と編集。
- [Mobbin](mobbin_2026-11-14.json) — 実際のアプリ画面を使ったUI設計の参考調査。
- [Refero](refero_2026-11-14.json) — 製品画面・操作フローのデザイン調査。
- [to3D](to3d_2026-11-14.json) — 画像からシンプルな3D glTFモデルを作成。
- [BioRender](biorender_2026-11-14.json) — 科学図のテンプレート検索と下書き作成。
- [MyFonts](myfonts_2026-11-14.json) — 画像や説明文からフォント候補を探す。
- [VideoZero](videozero_2026-11-14.json) — 数学などの概念を説明する動画の作成。
- [Instavar Video Templates](instavar_video_templates_2026-11-14.json) — Remotion向け動画テンプレート。詳細の一部は説明だけでは不明。
- [MagicPath](magicpath_2026-11-14.json) — アプリ・ウェブ画面の共有キャンバスでの設計・試作。

- [Vulca](vulca_2026-11-14.json) — ビジュアルの方向性・文化的表現の調査と評価。画像生成等は対象外と説明。一覧本体に名称なし。

- [Worldkeep](worldkeep_2026-11-14.json) — 創作世界の設定を承認を経て整理し、グラフ表示。
- [Dramatica](dramatica_2026-11-14.json) — 認証済み作家の保存済み物語構造の確認・検証。
- [Inkroost: Comic & Manga Maker](inkroost_2026-11-14.json) — 漫画・ウェブトゥーンの企画と作画、アニメ化を案内。

- [NoveLand for Writers](noveland_for_writers_2026-11-14.json) — 小説・脚本の人物設定、伏線、相関図などを管理。
- [ShotClick: Screenplay & Script](shotclick_2026-11-14.json) — 脚本形式で編集し別案を管理。接続にStudioプランが必要と説明。

- [PictureBooks](picturebooks_2026-11-14.json) — 既存クレジットを使って非公開の絵本を作成。
- [Character Creator](character_creator_2026-11-14.json) — キャラクターの設定・外見・画像用プロンプトを考案。アフィリエイトリンクの記載あり。

- [Character Maker](character_maker_2026-11-14.json) — MegaScenesでオリジナルキャラクター画像を作成。Character Creatorとは表示名・提供元が異なる。
- [Game Maker AI](game_maker_ai_2026-11-14.json) — ゲーム企画と難易度の検討。ゲームそのものの作成・実行・公開は行わないと説明。


- [RunComfy](runcomfy_2026-11-14.json) — クラウドでComfyUIのワークフローを実行し、画像・動画の生成や独自LoRAの学習を行う。
- [AI Video and Image by AIRP](ai_video_and_image_by_airp_2026-11-14.json) — 対話で画像・ロゴ・動画の制作内容を整理し、ManyMotionsで制作するためのリンクを作る。
- [FLORA](flora_2026-11-14.json) — 会話から画像やムードボードなどのビジュアル素材を生成・整理・改善する。
- [Screel](screel_2026-11-14.json) — シーンごとの絵コンテや静止画を基に動画を制作し、音声や音楽も追加する。
- [Kive](kive_2026-11-14.json) — 保存済みの商品や素材を参照し、ブランドに沿った商品画像・動画を作成・編集する。
- [Mirelo](mirelo_2026-11-14.json) — 文章や動画から効果音・環境音を生成、既存音声の編集やMIDI・楽譜への変換を行う。
- [Midify](midify_2026-11-14.json) — コード進行やハーモニーを検討し、会話でMIDIの楽曲構成を作る。
- [Subdivide](subdivide_2026-11-14.json) — テンポや拍子、細分音符、テンポの変化を指定できるメトロノームを作る。
- [VisualSong](visualsong_2026-11-14.json) — 端末内の音声ファイルに反応する映像表現をChatGPT内に表示する。
- [Appllama](appllama_2026-11-14.json) — 売上上位のモバイルアプリの画面、操作フロー、オンボーディングや課金画面を調べるためのデザイン資料。


- [Alpix](alpix_2026-11-14.json) — 共有キャンバス上でAIと一緒にドット絵を描く。
- [Vectorize](vectorize_2026-11-14.json) — ロゴ画像を編集可能なSVGに変換し、色・曲線・背景などを調整する。
- [Shapesoda](shapesoda_2026-11-14.json) — 既存画像をSVG・PDF・EPS・DXFなどに変換し、色や背景を調整する。
- [Vectali](vectali_2026-11-14.json) — ロゴやイラストをSVG・PDF・EPS・DXFに変換し、元画像と比較する。
- [Rasterless](rasterless_2026-11-14.json) — アイコンやロゴなどをSVGに変換し、元画像と比較する。


- [B&A: Draw Sketches](ba_draw_sketches_2026-11-14.json) — ホワイトボードに手描きや図形、矢印、文字で考えを描く。
- [B&A: Sketch](ba_sketch_2026-11-14.json) — ホワイトボードでスケッチや図、メモを作る。
- [drawDash - Sketch Challenge!](drawdash_sketch_challenge_2026-11-14.json) — お題に沿って絵を描き、ChatGPTが何を描いたか当てるゲーム。
- [Amazing Drawing](amazing_drawing_2026-11-14.json) — 絵や図を描き、ChatGPTに説明・分析・感想などを依頼する。
- [unsketch](unsketch_2026-11-14.json) — 商品写真から広告画像や短い動画を作成し、会話で修正・字幕編集する。


- [mnml AI](mnml_ai_2026-11-14.json) — スケッチや建築モデルの画像から建築・内装の写実的な画像を生成・修正する。
- [AI Architectures](ai_architectures_2026-11-14.json) — 既成の間取りを検索し、アカウント連携で説明やスケッチからCAD図面を作る。
- [Floor Plans](floor_plans_2026-11-14.json) — 部屋の構成や保存済みスケッチから、俯瞰の間取りイメージを生成する。
- [WalkMyPlan — Floor Plans in 3D](walkmyplan_floor_plans_in_3d_2026-11-14.json) — 会話や既存図面から住宅の3D間取りを作り、歩行表示や編集を行う。
- [HZplan](hzplan_2026-11-14.json) — 間取り画像や寸法から編集可能な住宅プランを作り、家具配置や2D・3D・VR表示を検討する。


- [Architecture Designer](architecture_designer_2026-11-14.json) — 建築や内装、リフォームの企画、間取り案、材料や照明、チェックリストなどを検討する。
- [PropertyPrompt](propertyprompt_2026-11-14.json) — 実寸を一つ以上使い、間取りから家具を配置できる3Dモデルを作る。
- [Rayon](rayon_2026-11-14.json) — 接続済みRayonのプロジェクトで間取り・家具配置を検討し、表やプレゼン資料を作る。
- [kernelCAD](kernelcad_2026-11-14.json) — 文章で寸法を変更できるCAD部品や組立モデルを作り、3D確認や図面出力を行う。
- [Comic Strips](comic_strips_2026-11-14.json) — 文章で各コマ・人物・台詞を指定し、吹き出し付きの3・4・6コマ漫画を作る。


- [Fantasy Maps](fantasy_maps_2026-11-14.json) — 文章で架空の国や都市、ダンジョンなどの地図画像を作る。
- [Character Art](character_art_2026-11-14.json) — 文章から創作キャラクターの肖像・全身像・三面図を作る。
- [Pixel Art](pixel_art_2026-11-14.json) — 文章から8・16ビット風のドット絵やスプライトシートを作る。
- [Book Covers by Abracadabrax](book_covers_by_abracadabrax_2026-11-14.json) — 書名や著者、ジャンルを指定して電子書籍・印刷本の表紙画像を作る。
- [Coloring Pages by Abracadabrax](coloring_pages_by_abracadabrax_2026-11-14.json) — 文章から、対象年齢に合わせた線の細かさの印刷用塗り絵を作る。


- [PersonalizedComics](personalizedcomics_2026-11-14.json) — 写真の人物を登場させ、表紙・2ページの物語・裏表紙からなる短編漫画を作る。
- [AI Manga Studio](ai_manga_studio_2026-11-14.json) — 漫画の企画・ネーム・コマ・吹き出しや画像配置を、連携した作品に対して会話で編集する。
- [Image Translator](image_translator_2026-11-14.json) — 保存済みの漫画ページなどの画像内の文字を翻訳して差し替えた画像を作る。
- [Anifusion](anifusion_2026-11-14.json) — 物語やコマごとの脚本から非公開の漫画を作り、Anifusionでレイアウトや文字を編集する。
- [TicToon](tictoon_2026-11-14.json) — 参加済みTicToonチャンネルに、画像と文章を漫画のスレッドとして投稿する。

## 一覧本体との照合

[名称照合の記録](catalog_name_audit_2026-11-14.json) — 詳細35件と作業ブランチの一覧3,941件を比較。34件は名前が一致、Palimpsestは一致なし。名前の一致は同一性の確定ではない。個々のJSONにある旧「照合未確認」の記載は調査時点の記録で、最新の照合結果はこの記録を参照。

## 再開

金融とクリエイティブの一覧から詳細調査を開始。各詳細を開いた後に一覧へ戻ると先頭へ戻ることがあるため、再開時は上記の記録と重複しないよう名前と詳細ページを確認する。次の候補は、一覧の短文だけでは対象や提供範囲が曖昧な項目から選ぶ。カテゴリー全体の選別・詳細調査はまだ完了していない。
