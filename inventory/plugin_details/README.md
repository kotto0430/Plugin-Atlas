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


- [MangaBoom](mangaboom_2026-11-14.json) — 文章や会話から、縦スクロール形式などのカラー漫画を作る。
- [Story Writer](story_writer_2026-11-14.json) — 物語の発想、構成、人物、台詞、推敲や出版準備を支援する。
- [Firemoon Storyboard Studio](firemoon_storyboard_studio_2026-11-14.json) — 指示や参考画像から2〜6枚の絵コンテを作り、短い動画をつなぐ。
- [Storybook Maker](storybook_maker_2026-11-14.json) — 短い物語の挿絵を1ページずつ生成し、絵本制作を支援する。
- [Storytailor](storytailor_2026-11-14.json) — Storytailorの物語の作成・閲覧・続き・翻訳や登場人物を管理する。


- [StoryCrest](storycrest_2026-11-14.json) — 子どもを主人公にした絵本の表紙・あらすじを作り、外部サイトで印刷本を注文できる。
- [Kids Book Maker](kids_book_maker_2026-11-14.json) — 大人が子ども向けに、挿絵・読み上げ・字幕のある絵本を作る。
- [Storyblocks](storyblocks_2026-11-14.json) — ストック動画・音楽・効果音・画像を検索して確認する。

- [Conversational Narrative](conversational_narrative_2026-11-15.json) — 専門的な考えを会話調に書き直し、文章を点検する。
- [Anime Stories](anime_stories_2026-11-15.json) — オリジナル物語の短いアニメ動画を作る。
- [Short Story Lovers](short_story_lovers_2026-11-15.json) — 作家アカウントの下書きや公開を管理する。
- [Animation Maker](animation_maker_2026-11-15.json) — アニメの企画や制作工程を検討する。
- [Bedtime Story Maker](bedtime_story_maker_2026-11-15.json) — 子ども向け物語を音声で読み上げる。
- [gilmOS](gilmos_2026-11-15.json) — 脚本、映像素材と制作予定を管理する。
- [Topview 3D Builder](topview_3d_builder_2026-11-15.json) — 人物やカメラの配置を3Dで組み立てて映像の構図を検討する。

- [Zovo Love Story Poster](zovo_love_story_poster_2026-11-15.json) — 記念日から経過日数や節目を計算し、ポスターPDFと予定表を作る。
- [Memory Book of Voice Messages](memory_book_of_voice_messages_2026-11-15.json) — 一人の音声メッセージを文字起こしして回想録にまとめる。日本語の印刷と配送地域に制限あり。

- [Short Films（ManyMotions）](short_films_manymotions_2026-11-15.json) — 物語の概要から短編映画を制作。同名・同提供元の2ページを比較し、関係は未確認。

- [Meminto – Write Your Book](meminto_write_your_book_2026-11-15.json) — 本の構想・執筆や対応する原稿の取り込みを支援する。
- [papergarden](papergarden_2026-11-15.json) — 物語と挿絵のある絵本を制作し、印刷本を注文する。
- [KitCut](kitcut_2026-11-15.json) — アイデアや画像からナレーション付きアニメ動画を作る。
- [LongStories](longstories_2026-11-15.json) — 物語や脚本から動画やシリーズを制作・編集する。

- [Social Images](social_images_2026-11-15.json) — SNSごとのサイズに合わせた新規投稿画像を作る。
- [Website Builder（AI Research Plus）](website_builder_ai_research_plus_2026-11-15.json) — サイトの構成・文章・コード作成やページ改善を支援する。
- [Brix36](brix36_2026-11-15.json) — 映画や音楽動画の企画・絵コンテ・動画を扱う。
- [Sequencer](sequencer_2026-11-15.json) — 画像・動画・音声の生成と編集、動画の書き出しを行う。
- [Reverie Movies](reverie_movies_2026-11-15.json) — 絵コンテから映像や音楽動画を制作する。

- [Social Media Posts（MegaScenes）](social_media_posts_megascenes_2026-11-15.json) — 指定した文字を載せたSNS画像を作る。
- [Video Lab](video_lab_2026-11-15.json) — 動画の企画・脚本・絵コンテやプロンプトを作る。
- [Imago](imago_2026-11-15.json) — 利用できる画像ツールを使った画像制作・編集や図解を支援する。
- [AI Video Generator（Syed Fasih Haider Raza Rizvi）](ai_video_generator_fasih_2026-11-15.json) — 動画の企画・脚本・生成用プロンプトなどを用意する。
- [Designly（Mamdouh Abo Ammar）](designly_mamdouh_2026-11-15.json) — 広告やSNSの構図・文字・画像表現の検討と改善を支援する。

- [VideoGen - AI Video Generator](videogen_ai_video_generator_2026-11-15.json) — 文章・画像などから動画を作成・編集し、MP4を書き出す。
- [Martini](martini_2026-11-15.json) — 共有プロジェクトで映像を企画・生成・編集する。
- [PixVerse (Legacy; EOL soon)](pixverse_legacy_2026-11-15.json) — 画像・動画制作の旧版。新しいページへの移行を案内。
- [PixVerse](pixverse_2026-11-15.json) — 画像・短編動画や映像企画を扱う新しいページ。

- [Simple Photo Gallery](simple_photo_gallery_2026-11-15.json) — アップロードした写真をアルバムや共有ギャラリーに整理する。
- [Ridvay: Carousels & Posters](ridvay_carousels_posters_2026-11-15.json) — 編集可能なSNS投稿やポスターを作る。
- [Memolio](memolio_2026-11-15.json) — 家族の思い出を水彩風の挿絵が付いた記念本にする。
- [Semblora](semblora_2026-11-15.json) — 脚本・絵コンテや映像制作を扱う。
- [AISTLabs](aistlabs_2026-11-15.json) — 商品写真から短い商品動画や画像・音声を作る。
- [HeyGen](heygen_2026-11-15.json) — アバター動画・画像・音声・動画翻訳を扱う。

- [Autodesk Product Help](autodesk_product_help_2026-11-15.json) — Autodesk製品の公式ヘルプを検索する。
- [AI Graphic Design（Superdesign）](ai_graphic_design_superdesign_2026-11-15.json) — ポスターやスライドを作り、参考画像をムードボードに集める。
- [Arcads](arcads_2026-11-15.json) — 商品や企画から広告画像・動画を制作する。

- [Everygen](everygen_2026-11-15.json) — 短い動画や画像、音声、脚本の制作を扱う。
- [AI Voice Generator（Level 2 Labs）](ai_voice_generator_level2_2026-11-15.json) — 文章からナレーション音声を作る。
- [fal](fal_2026-11-15.json) — 画像・動画・音声・3Dなどを生成する。
- [Magnific](magnific_2026-11-15.json) — 画像・動画などの制作や編集、キャンペーン制作を扱う。
- [OpenArt](openart_2026-11-15.json) — 複数のモデルを使って画像や動画などを作る。
- [invideo](invideo_2026-11-15.json) — 動画のタイムライン編集や書き出しを扱う。
- [AI Video Maker（InfoseekAI）](ai_video_maker_infoseek_2026-11-15.json) — 短い動画を制作。説明では定額契約は不要で、使用量に応じた料金が発生する。

- [Visla Video Maker](visla_video_maker_2026-11-15.json) — 文書やPDFなどを基に台本とナレーション動画を作る。
- [OpusClip: Video Editing](opusclip_video_editing_2026-11-15.json) — 動画の切り抜き・字幕編集・SNS投稿予約を扱う。
- [VEED Video Generator](veed_video_generator_2026-11-15.json) — キャラクターと声を選んで動画を作る。
- [Genspark AI Slides](genspark_ai_slides_2026-11-15.json) — テーマや内容からスライドを生成する。
- [sync. labs](sync_labs_2026-11-15.json) — 動画の吹き替え・口の動きの同期や発話修正を扱う。
- [BlitzReels](blitzreels_2026-11-15.json) — 録画から字幕付きの短い動画を編集・出力する。
- [ImagineArt](imagineart_2026-11-15.json) — 画像・動画・音楽・広告を制作し、既存素材を編集する。
- [Sparki](sparki_2026-11-15.json) — 手元の動画を自然言語で編集し、クラウドでレンダリングする。
- [Tesseract（Mirage）](tesseract_mirage_2026-11-15.json) — 動画やモーショングラフィックスを制作。同名の2ページを比較。
- [Riverside](riverside_2026-11-15.json) — 動画・ポッドキャストの編集、投稿、配信管理を扱う。

- [Videomagic](videomagic_2026-11-15.json) — 話題や資料から説明動画を作る。会話情報の送信範囲は実挙動未確認。
- [Frameo.AI](frameo_ai_2026-11-15.json) — 物語や写真から画像・音声を組み合わせた短い動画を作る。
- [Shutterstock](shutterstock_2026-11-15.json) — ストック素材を検索。ダウンロード可否の説明が食い違うため要確認。

- [Synthesia](synthesia_2026-11-15.json) — 資料や台本から動画を作り、会話で修正する。
- [AI Music Maker（InfoseekAI）](ai_music_maker_infoseek_2026-11-15.json) — 文章や歌詞、任意の音声を参考に楽曲を生成する。
- [B12 Website Generator](b12_website_generator_2026-11-15.json) — 事業や企画の説明からウェブサイトを作る。
- [Deep Art AI](deep_art_ai_2026-11-15.json) — 画像や動画を生成し、動画の進捗を確認する。

- [Morphix](morphix_2026-11-15.json) — 画像・動画の生成、商品写真や広告素材の制作、画像の補正を扱う。

- [Color Designer - Palette Maker](color_designer_palette_maker_2026-11-15.json) — 文章から配色を提案し、パレットの色を編集する。
- [Orshot](orshot_2026-11-15.json) — テンプレートから画像・動画・PDFを作り、SNS投稿・予約や分析を扱う。
- [Apixel](apixel_2026-11-15.json) — 文章から画像を生成する。画像内の文字の精度は未検証。
- [Loomly](loomly_2026-11-15.json) — SNSの投稿予定や素材を確認し、下書き・アイデアを作る。
- [Instant Website / Insta Website Builder（Pyxl）](instant_website_pyxl_2026-11-15.json) — 説明からサイトを作り編集・公開。同じ提供元・サイトの2ページの関係は未確認。
- [LogoGenic Image Generator](logogenic_image_generator_2026-11-15.json) — 説明やスタイルを指定して画像を生成する。
- [TalkGen](talkgen_vidline_2026-11-15.json) — 写真やアバターを使って話す人物の動画を作る。
- [Hypernatural](hypernatural_2026-11-15.json) — ChatGPTの会話を基に物語や広告の動画を作る。

- [Kolbo.AI](kolbo_ai_2026-11-15.json) — 画像・動画・音声・3Dなどの制作と整理。動画編集の対象範囲は説明とスキル欄の読み分けが必要。

- [AI Song Maker（Syed Fasih Haider Raza Rizvi）](ai_song_maker_fasih_2026-11-15.json) — 歌詞や曲の構成、音楽生成用プロンプトを作る。アフィリエイト表示の記述差と音声生成の範囲は要確認。

- [Krikey AI Animation](krikey_ai_animation_2026-11-15.json) — 3Dキャラクターと題材を選び、音楽付きアニメーション動画を作る。
- [Image to Video（Syed Fasih Haider Raza Rizvi）](image_to_video_fasih_2026-11-15.json) — 画像から動画制作のプロンプトや企画を支援。直接生成とアフィリエイト表示の条件は未確認。

## 一覧本体との照合

[名称照合の記録](catalog_name_audit_2026-11-14.json) — 詳細35件と作業ブランチの一覧3,941件を比較。34件は名前が一致、Palimpsestは一致なし。名前の一致は同一性の確定ではない。個々のJSONにある旧「照合未確認」の記載は調査時点の記録で、最新の照合結果はこの記録を参照。

## 再開

金融とクリエイティブの一覧から詳細調査を開始。各詳細を開いた後に一覧へ戻ると先頭へ戻ることがあるため、再開時は上記の記録と重複しないよう名前と詳細ページを確認する。次の候補は、一覧の短文だけでは対象や提供範囲が曖昧な項目から選ぶ。カテゴリー全体の選別・詳細調査はまだ完了していない。
