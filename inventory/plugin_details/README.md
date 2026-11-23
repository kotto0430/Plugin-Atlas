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

- [Pixlie](pixlie_2026-11-15.json) — 動画生成用の指示文と絵コンテ案を作る。ChatGPT内での動画レンダリングは行わないと説明。

- [UX Pilot](ux_pilot_2026-11-15.json) — 言葉からワイヤーフレームや複数画面のUIを作る。
- [Font Pairing: Design & Brands](font_pairing_design_brands_2026-11-15.json) — 用途や雰囲気に応じて見出し・アクセント・本文の書体を提案する。

- [Glinded for Birthday Videos](glinded_birthday_videos_2026-11-15.json) — 写真や動画と音楽を使って記念動画を作る。
- [VoiceLabs](voicelabs_2026-11-15.json) — 音声合成や文字起こしを扱う。声の複製は対象外と説明。
- [Grapes Studio](grapes_studio_2026-11-15.json) — ウェブサイトやメールのページ、レイアウト、文章を作成・編集する。

- [Impeccable](impeccable_2026-11-15.json) — コーディングエージェントとUIの制作・評価・改善。
- [Montage](montage_2026-11-15.json) — 動画を取り込み、指定箇所の切り抜きと編集。
- [Havi: Slides & PPT Maker](havi_slides_ppt_maker_2026-11-15.json) — スライドの作成・編集とPPT・PDF出力。既存ファイルは開けないと説明。
- [Motionvid](motionvid_2026-11-15.json) — 台本から音楽やナレーション付きの動画を制作。有料プランの記載あり。
- [Interior Company](interior_company_2026-11-15.json) — 内装の情報、費用概算、デザイン相談。
- [Supericons](supericons_2026-11-15.json) — SVGアイコンの検索とプレビュー。
- [kernelCAD](kernelcad_2026-11-15.json) — パラメトリックCADの作成、確認と書き出し。
- [123 Piano](123_piano_2026-11-15.json) — 鍵盤を演奏し、AIと演奏について話す。
- [AI Image Generator（Syed Fasih Haider Raza Rizvi）](ai_image_generator_fasih_2026-11-15.json) — 画像制作・プロンプト作成。直接生成の範囲と広告リンクの表示条件は未確認。

- [AI Color Picker - Design Tool](ai_color_picker_design_tool_2026-11-15.json) — 色を選び、配色や読みやすさを相談する。
- [Faceless Video Maker（Syed Fasih Haider Raza Rizvi）](faceless_video_maker_fasih_2026-11-15.json) — 顔出し動画の企画・台本・映像用プロンプト。直接生成と広告リンクの表示条件は未確認。

- [Morphed](morphed_2026-11-15.json) — AI画像・動画の制作とクレジット見積もり。
- [Pika](pika_2026-11-15.json) — 写真・動画を使った映像、画像、音楽の制作。
- [01 Superdesign](01_superdesign_2026-11-15.json) — UIやスライド、告知画像の制作・比較。
- [Logo Generator（B12）](logo_generator_b12_2026-11-15.json) — ロゴを作り、SVG・PNGを出力。
- [FashionTrendAI](fashiontrendai_2026-11-15.json) — ファッション動向を分析し企画やデザインを支援。
- [Pablooo.club Benchmark library](pablooo_club_benchmark_library_2026-11-15.json) — アプリ画面の実例を検索・比較。

- [Glinded for Memorial Videos](glinded_memorial_videos_2026-11-15.json) — 写真や動画を追悼・記念映像にまとめる。
- [Kopi - Shopify Email Creator](kopi_shopify_email_creator_2026-11-15.json) — EC向け販促メールのHTML作成・修正。
- [Clipwave Video & Image Maker](clipwave_video_image_maker_2026-11-15.json) — アカウントとクレジットを使い画像・動画を生成。
- [Vocuno](vocuno_2026-11-15.json) — 楽曲生成、音声編集やパート分離。
- [UI UX Designer（Syed Fasih Haider Raza Rizvi）](ui_ux_designer_fasih_2026-11-15.json) — UI・UX設計を支援。広告リンクの表示条件は未確認。

- [Pixelixe](pixelixe_2026-11-15.json) — 連携したアカウントで販促画像を作成し、既存のデザインから別案を作る。
- [AI Photo Editor（Syed Fasih Haider Raza Rizvi）](ai_photo_editor_fasih_2026-11-15.json) — 写真編集を支援。直接編集の範囲と広告リンクの表示条件は未確認。

- [Infographic Artist](infographic_artist_2026-11-15.json) — デザイン原則や事例の調査・批評と企画。メイン説明はフランス語。
- [Faces（Perhaps Inc.）](faces_perhaps_2026-11-15.json) — 対話型プレゼンの作成・編集・公開。
- [VIXNODE](vixnode_2026-11-15.json) — サイトの作成・編集・公開と管理。
- [Gradient Maker - Linear Color](gradient_maker_linear_color_2026-11-15.json) — グラデーションの提案・調整とCSS・色コード。
- [DepositPhotos](depositphotos_2026-11-15.json) — 写真・動画・音楽などの検索。素材の利用条件とダウンロード方法は未検証。
- [Simple SoapCalc](simple_soapcalc_2026-11-15.json) — 手作り石けんの材料の量を計算。精度と安全性は未検証。
- [Flipbook - Publuu](flipbook_publuu_2026-11-15.json) — PDFをオンラインで共有できるフリップブックに変換。
- [Davia Creation](davia_creation_2026-11-15.json) — 非公開ゲーム草案の世界観やルール、マップを編集。
- [Poster Maker（POSTER APP LLP）](poster_maker_poster_app_2026-11-15.json) — テンプレートからポスターを探して文字を入れ、編集。
- [Whiteboard by Athena AI](whiteboard_athena_ai_2026-11-15.json) — 図表や画面案などを共同ホワイトボードに保存・共有。

- [Sonilo](sonilo_2026-11-15.json) — 音楽・効果音を作り動画の音声をミックス。
- [Flipsnack](flipsnack_2026-11-15.json) — PDFから電子冊子を作り、公開・分析を管理。直接アップロードの範囲は未検証。
- [Kittl](kittl_2026-11-15.json) — 商品画像やモックアップ、販促動画を作る。
- [Image Generator（The Doers Firm）](image_generator_the_doers_firm_2026-11-15.json) — 画像制作の指示文や生成素材を用意。
- [Image Generator（B12）](image_generator_b12_2026-11-15.json) — ウェブサイト用画像と代替テキストを用意。
- [Spline](spline_2026-11-15.json) — 対話型3Dシーンやウェブページを作成・編集。
- [Wixel](wixel_2026-11-15.json) — ロゴ・画像・プレゼン・動画の作成と編集。
- [Clueso](clueso_2026-11-15.json) — 画面録画や資料から説明動画・手順書を制作。
- [Make A Viz](make_a_viz_2026-11-15.json) — 図表やマインドマップを作成・編集。
- [SSHOW](sshow_2026-11-15.json) — プレゼンの編集・再生。エディターを閉じた状態での読み取りは説明が異なり未確認。

- [Maze](maze_2026-11-15.json) — ユーザー調査やセッション結果を検索・確認。
- [AI Fashion Designer（F Word）](ai_fashion_designer_f_word_2026-11-15.json) — 衣服のデザインや作品集の制作を支援。
- [PrintTiler](printtiler_2026-11-15.json) — 一枚の画像を複数枚に分割印刷するレイアウトを作る。

- [PosterMyWall](postermywall_2026-11-15.json) — テンプレートを探し、PosterMyWall上で編集する。
- [Dazzly](dazzly_2026-11-15.json) — ウェブサイト制作や商品販売を支援。ChatGPT連携からの操作範囲は未確認。

- [GifGen - GIFs](gifgen_gifs_2026-11-15.json) — 文章や画像からループGIFを作る。
- [12ui Design](12ui_design_2026-11-15.json) — UIの参考を探し、画像からコード化する。
- [DevMotion](devmotion_2026-11-15.json) — 編集可能なアニメーション動画を制作。
- [3aqel Arabic Creative](3aqel_arabic_creative_2026-11-15.json) — アラビア語の広告デザインや音声を作る。
- [skima](skima_2026-11-15.json) — 建物の初期段階の間取り案や外観モデルを作る。
- [Sitelas](sitelas_2026-11-15.json) — サイトを作成し、公開後も管理する。
- [Goldie](goldie_2026-11-15.json) — オンデマンド印刷向けの商品企画・デザインを支援。
- [PoolVisionIA](poolvisionia_2026-11-15.json) — 庭の写真にプールを設置したイメージを作る。説明はフランス語。
- [Magic Hour AI](magic_hour_ai_2026-11-15.json) — 画像・動画・音声を生成・編集。

- [Sequel.io](sequel_io_2026-11-15.json) — ウェビナーの文字起こしからブログやSNS向け文章を作る。
- [Butter](butter_2026-11-15.json) — 広告動画を作り、ブラウザーで編集する。
- [Logo Designer（Syed Fasih Haider Raza Rizvi）](logo_designer_fasih_2026-11-15.json) — ロゴやブランド素材の制作を支援。広告リンクの表示条件は未確認。

- [Novel Writer（Syed Fasih Haider Raza Rizvi）](novel_writer_fasih_2026-11-15.json) — 小説の構想・執筆・推敲を支援。広告リンクの表示条件は未確認。

- [Pexafy Stock Photos](pexafy_stock_photos_2026-11-15.json) — 文章や参考画像から写真素材を検索。認証・利用枠の条件は未確認。

- [Flixly](flixly_2026-11-15.json) — 画像・動画の生成モデルや費用を比較し、生成状況を確認。
- [Planner5D: Plan, Build, Create](planner5d_plan_build_create_2026-11-15.json) — 間取りや家具配置を作成し、2D・3Dで検討。
- [Aspicio](aspicio_2026-11-15.json) — DXF図面のレイヤー・寸法・文字を確認。
- [Atlas Cloud](atlas_cloud_2026-11-15.json) — 複数のAIモデルを使って画像・動画・音声などを生成。
- [Graphic Design Studio（Syed Fasih Haider Raza Rizvi）](graphic_design_studio_fasih_2026-11-15.json) — 印刷物やSNSのデザインを支援。広告リンクの表示条件は未確認。

- [Malloy Studio](malloy_studio_2026-11-15.json) — 動画用の動くタイトルや図表を作る。
- [Tripo 3D](tripo_3d_2026-11-15.json) — 文章や画像から3Dモデルを制作・編集。
- [Taste（Saul Martí）](taste_saul_marti_2026-11-15.json) — フロントエンド画面のデザインと実装を支援。
- [Tolstoy](tolstoy_2026-11-15.json) — EC向け商品写真・動画・広告を制作。
- [Cardboard](cardboard_2026-11-15.json) — 動画を会話で編集。書き出し解像度の条件は未確認。

- [AINSOF](ainsof_2026-11-15.json) — 映像向け楽曲の検索・試聴やライセンス支援を依頼。
- [Heyzine Flipbooks](heyzine_flipbooks_2026-11-15.json) — 文書から電子冊子を作り公開・管理。
- [GIF Maker（Syed Fasih Haider Raza Rizvi）](gif_maker_syed_2026-11-15.json) — GIFの制作や編集を支援。広告リンクの表示条件は未確認。

- [Drivethrough](drivethrough_2026-11-15.json) — 会話でサイトを作り、共有・公開や版の復元を行う。
- [Uxia](uxia_2026-11-15.json) — UX調査のテスト案と結果を扱う。Uxia MCPサーバーが必要。
- [The Altiora Codex Oracle](altiora_codex_oracle_2026-11-15.json) — 個人の内省や着想向けのカードリーディング。
- [CutPro](cutpro_2026-11-16.json) — 画像・動画・音声の制作や短尺動画への編集を支援。
- [AdKraft](adkraft_2026-11-16.json) — 商品写真からナレーション付き動画広告を作る。クレジットを使用。
- [Flatma](flatma_2026-11-16.json) — 家具の寸法や材料を調整できる3Dモデルを作る。
- [Air（Air Inc）](air_inc_2026-11-16.json) — ブランドやライブラリを扱う。具体的な操作範囲は説明だけでは不明。
- [DropTrack](droptrack_2026-11-16.json) — 楽曲を分析し、提出先の発見や販促を支援。
- [Thumbnail Maker（Syed Fasih Haider Raza Rizvi）](thumbnail_maker_fasih_2026-11-16.json) — サムネイルの企画・改善を支援。広告リンクの表示条件は未確認。

- [PostNitro](postnitro_2026-11-16.json) — SNSのカルーセルや画像を作り、投稿を予約。
- [Embroidery File Converter](embroidery_file_converter_2026-11-16.json) — 画像の刺繍データ化や刺繍ファイル形式の変換。
- [Widemile](widemile_2026-11-16.json) — 映像などの企画・絵コンテ・素材生成を支援。
- [Treza](treza_2026-11-16.json) — 動画の生成・編集と確認後のSNS投稿を支援。
- [Artlist](artlist_2026-11-16.json) — 画像・動画・音声の生成や楽曲検索。
- [Laotan AI Copywriting](laotan_ai_copywriting_2026-11-16.json) — 複数の文案作成エージェントを切り替えて文章を編集。
- [NewsTune Studio](newstune_studio_2026-11-16.json) — ポッドキャストを制作し公開ページやRSSを管理。
- [Ullbek](ullbek_2026-11-16.json) — 会話でウェブサイトを作成・修正し公開。
- [Pitch](pitch_2026-11-16.json) — プレゼン資料の作成・検索・共有。
- [Web Design（Syed Fasih Haider Raza Rizvi）](web_design_fasih_2026-11-16.json) — ウェブデザインやHTML/CSSモックアップを支援。広告リンクの表示条件は未確認。

- [Carat](carat_2026-11-16.json) — 画像・動画・音声や広告素材を生成・編集。
- [MotionDesign](motiondesign_2026-11-16.json) — GSAPを使った動きの多いウェブ画面を制作。
- [WonderWorks](wonderworks_2026-11-16.json) — 絵コンテや画像・動画・音楽を作る。
- [Taste（ALEXANDER ETHAN KEHR）](taste_alexander_kehr_2026-11-16.json) — 保存したデザイン参考を検索。同名のSaul Martí提供のTasteとは別。
- [Art Designer（Syed Fasih Haider Raza Rizvi）](art_designer_fasih_2026-11-16.json) — イラストや漫画の構想・プロンプト・講評を支援。直接生成の範囲は未確認。
- [Yaps Video Captions](yaps_video_captions_2026-11-16.json) — ローカルで文字起こしし字幕を動画に焼き込む。
- [AdsTurbo](adsturbo_2026-11-16.json) — 広告向け動画・商品画像の生成と編集。Pro以上が必要との説明。
- [Quickads](quickads_2026-11-16.json) — 広告の調査・制作・実施と分析を支援。
- [Text to Speech（Syed Fasih Haider Raza Rizvi）](text_to_speech_fasih_2026-11-16.json) — 読み上げ用の原稿や音声設定を準備。広告リンクの表示条件は未確認。

- [Cartoon Yourself（Syed Fasih Haider Raza Rizvi）](cartoon_yourself_fasih_2026-11-16.json) — 写真をもとに漫画風の似顔絵やアバターの制作を支援。広告リンクの表示条件は未確認。

- [Incarn](incarn_2026-11-16.json) — 古い家族写真に動きを加えて短い動画にする。
- [Room Renovation Visualizer](room_renovation_visualizer_2026-11-16.json) — 部屋の写真や間取りからリフォーム案を視覚化。
- [GifGen - Sticker Maker](gifgen_sticker_maker_2026-11-16.json) — 同じキャラクターの表情違いのステッカーを作る。
- [Logos & app icons](logos_and_app_icons_2026-11-16.json) — ロゴやアプリアイコンの案・納品仕様を検討。
- [AppLaunchFlow](applaunchflow_2026-11-16.json) — アプリのストア画像や宣伝動画を作成・編集。
- [Astria](astria_2026-11-16.json) — 画像・動画や商品写真、人物写真の制作を支援。
- [StitchDesign](stitchdesign_2026-11-16.json) — Google Stitch用のデザイン方針をDESIGN.mdにまとめる。
- [Kapwing](kapwing_2026-11-16.json) — 動画・音声の翻訳、字幕、吹き替え。口の動きへの同期は対象外と説明。
- [GIF Creator（The Doers Firm）](gif_creator_doers_2026-11-16.json) — アイデアや画像からGIFアニメーションを制作。
- [Lawh.ai](lawh_ai_2026-11-16.json) — 編集可能なレイヤー付きデザインを作成しPhotoshop形式で書き出す。

- [Nonica](nonica_2026-11-16.json) — Revit用のローカルMCP連携の導入・接続・機能を案内。
- [Yaps Background Remover](yaps_background_remover_2026-11-16.json) — 画像の背景をローカルで除去してPNGに保存。
- [Voiceover Lab（Syed Fasih Haider Raza Rizvi）](voiceover_lab_fasih_2026-11-16.json) — ナレーション原稿や話し方を準備。広告リンクの表示条件は未確認。

- [Voice Cloning（Syed Fasih Haider Raza Rizvi）](voice_cloning_fasih_2026-11-16.json) — 本人または許可のある声のクローンについて録音・設定などを支援。広告リンクの表示条件は未確認。

- [DesignSystem](designsystem_2026-11-16.json) — UIのデザインシステムを初期化・文書化。
- [Framer](framer_2026-11-16.json) — Framerのサイトを作成・修正しCMSや公開を管理。
- [Voicepanel](voicepanel_2026-11-16.json) — 実際の人から製品へのフィードバックを集める。調査手順は未確認。
- [Aholo Lux3D](aholo_lux3d_2026-11-16.json) — 3D素材制作のタスクとオフラインプレビューを管理。
- [Yaps Audio Cleaner](yaps_audio_cleaner_2026-11-16.json) — 録音のノイズをローカルで除去。
- [AI Film Pipeline Master](ai_film_pipeline_master_2026-11-16.json) — 映像の企画から脚本・絵コンテ・プロンプトまで計画。
- [Templated](templated_2026-11-16.json) — テンプレートから画像・PDF・動画を生成。
- [Uwear](uwear_2026-11-16.json) — ファッション商品の画像や動画を制作。
- [ShirtLab](shirtlab_2026-11-16.json) — 画像や文字を黒いシャツに配置してデザイン。
- [Blog Generator（B12）](blog_generator_b12_2026-11-16.json) — B12上のブログサイトを生成。

- [Musamimuk](musamimuk_2026-11-16.json) — ポスターや画像の制作、背景除去などを支援。画像生成にはコインを使用。
- [Diagram Builder（B12）](diagram_builder_b12_2026-11-16.json) — 業務の流れなどを図にしSVGで出力。
- [Pedra](pedra_2026-11-16.json) — 不動産写真の編集や紹介動画、360度ツアーの制作を支援。
- [BrandKit](brandkit_2026-11-16.json) — ブランドガイドやロゴのビジュアル制作を支援。
- [Yaps Video Clipping](yaps_video_clipping_2026-11-16.json) — 話す動画の無音を検出・カットし別のMP4に出力。
- [Details.so](details_so_2026-11-16.json) — ウェブデザインの参考や部品を探し、実装を支援。
- [Awesome DESIGN.md](awesome_design_md_2026-11-16.json) — 参考資料を使って製品・画面のデザイン分析と改善を支援。
- [UXCritique](uxcritique_2026-11-16.json) — UXや情報の優先順位を評価し改善点を整理。
- [Swish Sports Court Builder](swish_sports_court_builder_2026-11-16.json) — スポーツコートを2D・3Dでデザイン。
- [ImageToCode](image_to_code_2026-11-16.json) — 参考画像に沿ったフロントエンドの実装を支援。

- [Studio by Memes](studio_by_memes_2026-11-17.json) — ブランド向け画像・動画の制作やSNS投稿の計画を支援。
- [Meshy 3D](meshy_3d_2026-11-17.json) — 文章や画像から3Dモデルを作り、ゲーム制作や印刷向けの編集を支援。
- [Klap](klap_2026-11-17.json) — 長い公開動画から字幕付きショート動画を作成し投稿を予約。
- [VOSU](vosu_2026-11-17.json) — 画像・動画・3Dモデルを生成。
- [UIAudit](uiaudit_2026-11-17.json) — UIのアクセシビリティや性能など技術的な問題を点検。
- [MeiGen Gallery](meigen_gallery_2026-11-17.json) — 参考画像の検索、画像・動画の生成や編集。候補数の説明に相違あり。

- [PlayDrop](playdrop_2026-11-17.json) — ブラウザーゲームの制作、非公開テスト、公開を支援。
- [EmpirioLabs AI](empiriolabs_ai_2026-11-17.json) — 画像・動画・音声の生成やOCR、検索、開発向け処理。
- [Rendemo](rendemo_2026-11-17.json) — 操作できる製品デモやツアーを制作。
- [Redesign（Saul Martí）](redesign_saul_marti_2026-11-17.json) — 既存サイトやアプリの画面デザインを改善。
- [ShapeUI](shapeui_2026-11-17.json) — 実装前にUX・UIの方針を整理。
- [Studio Ghibli Anime Creator（The Doers Firm）](studio_ghibli_anime_creator_2026-11-17.json) — 写真やアイデアからアニメ調の場面づくりを支援。
- [Zim Studio](zim_studio_2026-11-17.json) — 広告向けの画像・動画・音声や絵コンテの制作を支援。
- [Hansora AI](hansora_ai_2026-11-17.json) — 画像・動画・音声を生成。詳しい対応範囲は未確認。
- [Writing Assistant（Matthew Lane）](writing_assistant_matthew_lane_2026-11-17.json) — 書き手の文体や意図を持つ下書きの改善を支援。
- [AI Headshot Generator（Syed Fasih Haider Raza Rizvi）](ai_headshot_generator_fasih_2026-11-17.json) — プロフィール写真の企画・撮影条件・生成結果の確認を支援。広告リンクの表示条件は未確認。

- [Property Video](property_video_2026-11-17.json) — 不動産紹介用の短い動画台本や撮影指示を作成。
- [FreeTTS](freetts_2026-11-17.json) — 文章の読み上げや複数の声による音声制作。
- [Content Lab](content_lab_2026-11-17.json) — 学習者が保存したブランド情報を使いSNS投稿文や動画台本を作成。
- [Marq](marq_2026-11-17.json) — ブランドのテンプレートやデータで資料・SNS素材を制作。
- [Orisu](orisu_2026-11-17.json) — 商品写真から広告画像や動画を制作。動画への音声合成は未確認。

- [WebMockup](webmockup_2026-11-17.json) — ウェブの各セクションのデザイン参考画像を作る。
- [Email Love](email_love_2026-11-17.json) — Figmaでのメール制作と配信向け個別化を支援。
- [MobileMockup](mobilemockup_2026-11-17.json) — モバイル画面と操作フローのデザイン案を画像で作る。
- [Fuji X100VI Look Emulator](fuji_x100vi_look_emulator_2026-11-17.json) — X100VI風の画像編集を支援。
- [Polish（Saul Martí）](polish_saul_marti_2026-11-17.json) — 公開前のUIを仕上げる。
- [Fashion & Style Finder](fashion_style_finder_2026-11-17.json) — 靴や服の選び方と着こなしを提案。
- [Flav.IA — Fotos de Imóveis](flav_ia_fotos_de_imoveis_2026-11-17.json) — 不動産写真の調整や広告企画。原文はポルトガル語。
- [Vivideo](vivideo_2026-11-17.json) — 文章や画像からAI動画を制作。
- [Icon Design（ailuntz）](icon_design_ailuntz_2026-11-17.json) — アイコン案の比較とApple Icon Composer向け素材の準備。原文は中国語。
- [Meme Marketing Agent](meme_marketing_agent_2026-11-17.json) — 線画を使ったミームの制作を支援。
- [MixMatter](mixmatter_2026-11-17.json) — 元画像を印刷物風のコラージュに再構成。
- [Viral Hook Suite 1.0](viral_hook_suite_1_0_2026-11-17.json) — ドイツ語の短尺動画用文章や見出しを作成。
- [Hen Screenshots](hen_screenshots_2026-11-17.json) — アプリストア用画像や端末モックアップを作成。
- [Sandcastles](sandcastles_2026-11-17.json) — 短尺動画のチャンネルや人気の形式を調査。
- [Viral 80 Trend](viral_80_trend_2026-11-17.json) — 写真やアイデアを4つの時代の画像案に展開。
- [Viral Hook Suite](viral_hook_suite_2026-11-17.json) — ドイツ語のSNS向け文章を作成。同提供元の1.0とは別ページで関係未確認。
- [HardenUI](hardenui_2026-11-17.json) — UIのエラーや多言語対応など例外的なケースへの対応を支援。
- [SlidesAI](slidesai_2026-11-17.json) — メモや文書から編集可能なプレゼン資料を制作。
- [YouTube Thumbnail Creator（The Doers Firm）](youtube_thumbnail_creator_doers_2026-11-17.json) — サムネイルの構想、画像制作、評価を支援。
- [Vivu](vivu_2026-11-17.json) — 登録済み動画の場面検索、要約、管理。

- [Parallax Card](parallax_card_2026-11-17.json) — 画像や作品を使った立体的なカード制作を支援。
- [Ad Army](ad_army_2026-11-17.json) — 広告向け画像・動画の制作や素材管理。アカウントとクレジットが必要。
- [CaseWrite](casewrite_2026-11-17.json) — Charleston DPS職員向けの報告書作成を支援。
- [Julius: PowerPoint & Slides](julius_powerpoint_slides_2026-11-17.json) — 文章や対応文書から編集可能なPowerPointを作成。

- [TTS Studio: AI Text to Speech](tts_studio_ai_text_to_speech_2026-11-17.json) — 入力した文章を音声に変換し、声や速度などを調整。

- [WonderWhy](wonderwhy_2026-11-17.json) — 商品写真からマーケティング仮説と広告案を作成。
- [Topo de Bolo Express](topo_de_bolo_express_2026-11-17.json) — ケーキ飾りの写真から印刷・カット用データを作成。受講生向け、原文はポルトガル語。

- [Nox Design](nox_design_2026-11-17.json) — 服のデザインを抽出・デジタル化。原文はスペイン語。
- [Brancha](brancha_2026-11-17.json) — 複数の制作案をツリー状の画面で比較し展開。

- [Viral Hook Suite — Shared Code](viral_hook_suite_shared_code_2026-11-17.json) — ドイツ語のSNS文章を作成。新しい会話ごとにコードを要求すると説明。

- [text-to-cad（earthtojake）](text_to_cad_6ac09476_2026-11-17.json) — 3Dモデル・図面の作成や製造向け確認。別URLの同名掲載を併記し、同一性は未確認。

- [Melius](melius_2026-11-17.json) — 商品広告の画像案を企画・生成。動画やアバターの対応範囲は未確認。

- [Humanizer AI（AE-Intelligence）](humanizer_ai_ae_intelligence_2026-11-17.json) — 文章の意味を保ちながら表現や文体を調整。

- [Doitong](doitong_2026-11-22.json) — 動画・画像・音楽や短編映像を制作。
- [Cadabra AI](cadabra_ai_2026-11-22.json) — 商品広告の画像や動画、短編映像を制作。
- [English Query Refiner](english_query_refiner_2026-11-22.json) — 英語表現を整えて二言語で回答。具体的な対応言語は未確認。
- [About Me – AI Life Box](about_me_ai_life_box_2026-11-22.json) — 自分を表す物を詰めた箱の画像を作成。原文はベトナム語。
- [PartForge](partforge_2026-11-22.json) — 3Dプリント用部品の設計を支援。データ共有範囲は未確認。

- [MapPoster](mapposter_2026-11-22.json) — 思い出の場所を使った地図ポスターを制作。
- [Hermoso: AI Marketing Agent](hermoso_ai_marketing_agent_2026-11-22.json) — 広告制作・競合調査・SNS投稿や広告運用を支援。
- [Insurance Agent Content Studio](insurance_agent_content_studio_2026-11-22.json) — 保険代理店向けSNS投稿やキャンペーンの制作を支援。
- [Tattoos Wizard](tattoos_wizard_2026-11-22.json) — タトゥーの料金目安や彫師、ケア情報を検索。
- [LYRC](lyrc_2026-11-22.json) — 楽曲から歌詞付き動画を制作。楽曲の追加方法には説明の相違あり。

- [ModRetro Chromatic Plugin](modretro_chromatic_plugin_2026-11-22.json) — CodexでChromatic向けゲームを制作し、対応カートリッジへの書き込みを支援。
- [Crealix](crealix_2026-11-22.json) — アイデアや台本から音声・字幕・音楽付き動画を制作。クレジットを使用。

- [esigna](esigna_2026-11-22.json) — メール署名をデザインし、プレビューや編集を行う。
- [Super Map World](super_map_world_2026-11-22.json) — 世界や国の地図画像を投影法や色、境界などで検索。
- [Pray Production Studio](pray_production_studio_2026-11-22.json) — 映像プロジェクトの検索や予告編の企画・生成を支援。
- [Lovart](lovart_2026-11-22.json) — 文章や参考画像から画像・動画を生成し、画像を編集。
- [Polymend](polymend_2026-11-22.json) — 3Dモデルを点検・修復し、印刷用のSTLと3MFを出力。
- [3D CAD Converter](3d_cad_converter_2026-11-22.json) — Windows上でCAD・3Dファイルの形式変換を支援。
- [SignalGrade](signalgrade_2026-11-22.json) — 楽曲の音量・周波数・ステレオなどを分析し、参考音源と比較。
- [Doublespeed](doublespeed_2026-11-22.json) — SNS向け動画やカルーセルを作り、投稿の予約や下書き共有を支援。
- [Human Prose Editor](human_prose_editor_2026-11-22.json) — 書き手の文体や意味を保ちながら、文章の構造や表現を見直す。
- [ViewMax](viewmax_2026-11-22.json) — 企画文から動画・画像・ナレーション・音楽や効果音を生成。

- [NameSTL](namestl_2026-11-22.json) — 名前入りの3Dプリント用デザインを作成し、プレビュー・保存。
- [QynTro AI](qyntro_ai_2026-11-22.json) — 画像・動画・音楽・音声や3Dモデル、スライドを制作。
- [Ruwana](ruwana_2026-11-22.json) — 素材や企画から広告・写真・映像などの制作を支援。
- [RiffAds](riffads_2026-11-22.json) — AI出演者を使った動画広告と画像・音声の制作や編集。
- [Cyber AI](cyber_ai_2026-11-22.json) — 画像・動画・音楽・音声や3Dモデルをアカウントの残高で生成。
- [Shorts Generator](shorts_generator_2026-11-22.json) — 企画文や最大4枚の静止画から15秒動画を制作・仕上げ。
- [FXI Studio](fxi_studio_2026-11-22.json) — 静止画や動画を生成し、複数ショットをつないだ映像を制作。
- [Canvora](canvora_2026-11-22.json) — ブランドの設定を使い、SNS投稿や広告・資料向け画像を制作。
- [SkeuDesign](skeudesign_2026-11-22.json) — アイコン素材を検索・比較し、利用可能なPNGを出力。
- [Generate Greetings](generate_greetings_2026-11-22.json) — 祝い事などの挨拶文やカードを13言語で作成。

- [McSill Ultra 5.0](mcsill_ultra_5_0_2026-11-22.json) — 物語や原稿の構成・人物・対話などを分析し、改稿を支援。
- [AI Video Enhancer Studio](ai_video_enhancer_studio_2026-11-22.json) — Windows上で動画の高解像度化・手ぶれ補正・ノイズ除去を支援。
- [Namsiang Thai Voice](namsiang_thai_voice_2026-11-22.json) — タイ語音声の配役や感情・間合いを指定し、ドラマやナレーションを制作。
- [APODICTIC Development Editor](apodictic_development_editor_2026-11-22.json) — 小説や論考の構造を分析し、優先順位付きの改稿計画を作成。
- [UnifyAI](unifyai_2026-11-22.json) — ChatGPT内で動画と画像の制作を支援。
- [SMC Schrijversstem](smc_schrijversstem_2026-11-22.json) — SMCの文体に沿う文章の作成・評価・修正を支援。
- [Scribe Animator Director](scribe_animator_director_2026-11-22.json) — Scribe Animator向けの編集可能なホワイトボード動画や説明場面を制作。
- [WebCAD](webcad_2026-11-22.json) — 機械部品や簡単な機構の設計、画像表示、STEP出力を支援。
- [Eden](eden_2026-11-22.json) — 公開SNS投稿の調査や分析、下書き保存と承認後の投稿予約を支援。
- [3D Website Creator](3d_website_creator_2026-11-22.json) — 3Dウェブサイトの場面・動き・構成・表示確認を計画。

- [Bildy](bildy_2026-11-22.json) — 会話から画像・動画を生成・編集し、動画の切り出しや結合を行う。
- [Algorithmic Ink](algorithmic_ink_2026-11-22.json) — 写真を幾何学的な線画に変換し、SVG・PNGとして出力。
- [Songs To Your Eyes](songs_to_your_eyes_2026-11-22.json) — 映画や動画の場面・長さに合うライセンス楽曲を検索。

- [UGCBuilder](ugcbuilder_2026-11-22.json) — 商品写真と企画からランディングページ用画像やUGC動画を制作。
- [Photoroom](photoroom_2026-11-22.json) — 商品写真の背景・色などを編集し、商品画像や短い動画を制作。
- [Video Generator（MegaScenes）](video_generator_megascenes_2026-11-22.json) — 文章から数秒の動画クリップを制作。
- [VoxelDraft](voxeldraft_2026-11-22.json) — ボクセルモデルを作成・確認し、OBJ/MTLなどに出力。
- [SuperCool](supercool_2026-11-22.json) — 動画・画像・サイト・資料・音楽などの制作を支援。
- [Syllaby](syllaby_2026-11-22.json) — 企画や映像から短い縦動画を制作し、SNSへの投稿・予約を支援。

- [Rainbrand](rainbrand_2026-11-23.json) — ブランド情報・指針・素材の共有や更新。
- [BusbySim](busbysim_2026-11-23.json) — システムのSysML v2モデル作成・構文確認・図表示。
- [Sleek](sleek_2026-11-23.json) — アプリの複数画面のデザイン案を作成・編集。
- [Agent-Native Design](agent-native-design_2026-11-23.json) — 会話で対話型プロトタイプを作りワークスペース上で改善。
- [Outfit Preview: Virtual Try-On](outfit-preview-virtual-try-on_2026-11-23.json) — 人物写真と衣服の写真から試着イメージを作成。
- [Boy or Girl Names](boy-or-girl-names_2026-11-23.json) — 頭文字などを指定して赤ちゃんの名前を探す。
- [Samautomation Video](samautomation-video_2026-11-23.json) — 画像・動画・ナレーション・字幕をMP4にまとめる。
- [Segmind](segmind_2026-11-23.json) — 画像・音声・動画の生成を支援。
- [KDP Coloring Book Studio](kdp-coloring-book-studio_2026-11-23.json) — 会話から複数ページのぬり絵本を企画・制作。
- [varg.ai](varg-ai_2026-11-23.json) — 画像・動画・音声・音楽の生成と広告動画の制作。

- [ShareCube](sharecube_2026-11-23.json) — 文書をHTMLやMarkdownとして共有し、コメントや版を管理する。
- [QuickStage](quickstage_2026-11-23.json) — 物件写真に家具や装飾を仮想配置する。
- [Fenestra](fenestra_2026-11-23.json) — 建築スケッチや画像からパースを作成・編集する。
- [AI Video Maker – Dora](ai-video-maker-dora_2026-11-23.json) — 文章や写真から短い動画や画像を作る。
- [Inspire by KGL](inspire-by-kgl_2026-11-23.json) — 出典付きの言葉を探し、カードに載せる。
- [theprintspace](theprintspace_2026-11-23.json) — 写真や作品の印刷・額装を設定し注文する。
- [NOLGIA](nolgia_2026-11-23.json) — プリセットや手持ち素材で画像・動画・音声を制作する。
- [Gigapixel AI](gigapixel-ai_2026-11-23.json) — 画像や動画の拡大・高画質化と生成を支援する。

- [WFI — WhatFontIs](wfi-whatfontis_2026-11-23.json) — 画像から似たフォントの候補を探す。
- [BlockGPT](blockgpt_2026-11-23.json) — 文章や公開画像からMinecraft用建築データを作る。
- [getimg](getimg_2026-11-23.json) — 画像・動画・音声などの生成や編集を行う。
- [SC Adelsdorf Matchreporter](sc-adelsdorf-matchreporter_2026-11-23.json) — SC Adelsdorf のSNS向け試合レポート作成を支援する。
- [OceanToken](oceantoken_2026-11-23.json) — 複数のAIモデルを検索し、文章・画像・動画・音声などを生成する。
- [Lazybird](lazybird_2026-11-23.json) — 台本からナレーション音声や動画プロジェクトを作る。
- [Runchat](runchat_2026-11-23.json) — 設計ワークフローを構築し、対応するCADツールと連携する。
- [Revid](revid_2026-11-23.json) — 短尺動画を作成し、SNS投稿の準備や調査を支援する。
- [Pretty](pretty_2026-11-23.json) — 資料や指示からPowerPoint用プレゼンを作成・修正する。
- [appdesigns](appdesigns_2026-11-23.json) — アプリ画面からストア掲載用スクリーンショットを作る。

- [Cav](cav_2026-11-23.json) — Cavalryでモーショングラフィックスの制作・レンダリングを支援する。
- [TrackGleam](trackgleam_2026-11-23.json) — 楽曲の音量や音質の確認と公開準備を支援し、外部の制作ツールへ案内する。
- [Tatty — Tattoo ideas & design](tatty-tattoo-ideas-design_2026-11-23.json) — タトゥーの参考例を探し、オリジナルのデザイン案を作成・修正する。
- [Kombai](kombai_2026-11-23.json) — Codexでページや製品UIのデザイン案を作り、編集可能なキャンバスで比較・修正する。
- [AI Video Maker Gem](ai-video-maker-gem_2026-11-23.json) — 文章や参考画像・動画から動画を生成し、編集・延長する。
- [YouWorkForThem](youworkforthem_2026-11-23.json) — フォント・グラフィック・写真を検索し、類似フォントや素材の詳細を確認する。
- [WizPrompt Studio](wizprompt-studio_2026-11-23.json) — 楽曲のアイデアから音楽生成用のプロンプトや歌詞を作り、企画や版を管理する。

- [AVSBL Website Builder](avsbl-website-builder_2026-11-23.json) — AVSBLのウェブサイト下書きを会話で作成・編集する。
- [Gradients Studio](gradients-studio_2026-11-23.json) — サイトやスライド向けのグラデーション背景を作成・調整する。
- [Dịch Anh Việt](dich-anh-viet_2026-11-23.json) — 医療従事者や学習者向けに英語・ベトナム語の翻訳や用語学習、OET練習を支援する。
- [MeltFlex](meltflex_2026-11-23.json) — 室内や外観の写真からデザイン案を作り、仮想家具配置や動画化を支援する。
- [Mondovo](mondovo_2026-11-23.json) — 事業の説明からウェブサイトを設計・編集し、公開や運用を支援する。

- [Moon & Star Map](moon-star-map_2026-11-23.json) — 指定した日時の月相や星空を確認し、記念用のポスターを作る。
- [Daydream](daydream_2026-11-23.json) — 文章から最大2分のインスト曲を作り、パートごとに再生・調整する。
- [Your Color Palette](your-color-palette_2026-11-23.json) — 自撮り写真を用いたパーソナルカラーの候補と配色を表示する。
- [Fablyn](fablyn_2026-11-23.json) — 短い説明動画やスライドを作成・修正し、Fablynで確認する。
- [ScoreStarling](scorestarling_2026-11-23.json) — 音声や楽譜画像などを編集可能な楽譜に変換し、さまざまな形式に書き出す。
- [Raylight](raylight_2026-11-23.json) — Raylightのブラウザ編集画面で製品紹介やアプリ紹介の動画を制作・編集する。
- [Designelier](designelier_2026-11-23.json) — 統一したスタイルのアイコンや小さなイラストのセットを生成する。

- [Renoise](renoise_2026-11-23.json) — 広告や短編などの動画・画像・音楽の生成と素材分析を支援する。
- [Theme Emporium](theme-emporium_2026-11-23.json) — UIテーマやデザイントークンを確認し、専用ウィジェット内で配色などを試す。
- [OpenClip](openclip_2026-11-23.json) — 動画から共有向けの場面を探し、字幕を付けて書き出す。
- [RoomLab.app](roomlab-app_2026-11-23.json) — 室内・物件写真から家具配置や内装変更のイメージを作る。
- [KozyGrid](kozygrid_2026-11-23.json) — アイデアや画像から太い糸のブランケット用の編み図を作り、編集する。
- [GoFaceless](gofaceless_2026-11-23.json) — 写真とテンプレートを使った短い動画や顔出しなしの動画を制作する。
- [SoeMind](soemind_2026-11-23.json) — 小規模事業向けに広告動画・商品画像・音声などを制作する。
- [PrintNexus Toolbox](printnexus-toolbox_2026-11-23.json) — 画像から単色の平らなリソフェイン用3Dモデルを作成する。
- [style-my-space.com](style-my-space-com_2026-11-23.json) — 写真や説明から、予算に応じた部屋の模様替えや買い物の計画を提案する。
- [Rephrasy](rephrasy_2026-11-23.json) — AIで書いた下書きの表現を調整し、読みやすさを確認する。

- [convert3d](convert3d_2026-11-23.json) — 3D・CADファイルを別形式に変換し、3Dプレビューする。
- [PromptKosh](promptkosh_2026-11-23.json) — 公開スタイルのプロンプトを探し、ChatGPTの画像機能で画像を作る。
- [Print Ready](print-ready_2026-11-23.json) — 寸法や写真をもとに、3Dプリント向けの部品を設計する。
- [aicut](aicut_2026-11-23.json) — 短い動画や画像・音声を制作し、確認後のSNS投稿を支援する。
- [Flownato](flownato_2026-11-23.json) — 実在するモバイルアプリの画面や操作フローを探し、UI設計の参考にする。
- [Poolday](poolday_2026-11-23.json) — Pooldayのワークスペースで動画や画像の制作を依頼し、進捗や修正を管理する。
- [AppScreenshotStudio](appscreenshotstudio_2026-11-23.json) — アプリストア掲載用のスクリーンショットを作り、レイアウトなどを調整する。
- [LivePair](livepair_2026-11-23.json) — 画像・動画生成のプロンプトとその生成例を検索する。
- [PrintMap](printmap_2026-11-23.json) — 場所やスタイルを指定して、地図ポスターを作成・編集する。
- [Aaina Product Photos](aaina-product-photos_2026-11-23.json) — 商品写真から架空のモデルが着用・所持する商品画像を作成する。

- [Blendstra](blendstra_2026-11-23.json) — 3Dモデルを生成・確認・修正し、権限を指定して共有する。
- [Restream](restream_2026-11-23.json) — 複数プラットフォームへのライブ配信の予定・配信・管理を支援する。
- [Podigee](podigee_2026-11-23.json) — ポッドキャストのエピソード、文字起こし、配信状況や分析を管理する。
- [Alpenmarketing QR-Code](alpenmarketing-qr-code_2026-11-23.json) — URLや連絡先などからPNG形式のQRコードを作る。
- [Art Overlay](art-overlay_2026-11-23.json) — 手描きで画像を紙や壁などに写すための下絵と手順を用意する。
- [SpriteCook](spritecook_2026-11-23.json) — ゲーム向けスプライト、タイル、アニメーションやUI素材を作る。
- [Batch Banana](batch-banana_2026-11-23.json) — 画像・動画の生成や画像編集、複数プロンプトの一括処理を支援する。
- [Pixara](pixara_2026-11-23.json) — 画像・動画・音声の生成や編集、動画への素材の組み立てを行う。
- [Handymade](handymade_2026-11-23.json) — 手作り化粧品や石けん向けの材料、商品情報や資料を探す。
- [AutoSprite](autosprite_2026-11-23.json) — 2Dゲーム向けにキャラクターのアニメーションとスプライトシートを作る。

- [Logos do Brasil](logos_do_brasil_2026-11-23.json) — ブラジルのロゴ公開カタログでブランドや形式・出典・利用条件を調べる。
- [Moodle: Mood Board plan+design](moodle_mood_board_plan_design_2026-11-23.json) — 対話型のムードボードを作成・編集する。
- [Idea Generator](idea_generator_2026-11-23.json) — 概念を分解・組み合わせて制約を保ちながら新しい発想を生み出す。
- [Typography Studio](typography_studio_2026-11-23.json) — フォントの設計・字間調整・表示見本の確認を支援する。
- [Nova Creative](nova_creative_2026-11-23.json) — 画像・動画・音声・3D素材の生成ワークフローを作り、設定や見積もりを確認する。
- [Predis.ai](predis_ai_2026-11-23.json) — アイデアや商品URLから広告動画・画像やSNS投稿用素材を制作する。
- [Rawnd](rawnd_2026-11-23.json) — カメラのRAW内のJPEG表示や撮影情報の確認、写真の仕上げ候補選びを支援する。
- [YouCam](youcam_2026-11-23.json) — 顔や肌の特徴に基づく美容提案、メイクや髪型のプレビュー、写真編集を支援する。
- [Nafy AI Song Generator](nafy_ai_song_generator_2026-11-23.json) — 楽曲やインストの生成、カバー、楽曲の延長や声の変更を支援する。
- [Eddie](eddie_2026-11-23.json) — Eddieのプロジェクト内の映像を確認・編集し、完成動画や編集タイムラインを出力する。

- [AI Video Maker FX](ai-video-maker-fx_2026-11-23.json) — 文章や画像をもとに動画を生成し、既存動画の編集・延長を支援する。
- [Rebrand](rebrand_2026-11-23.json) — 公開デザインカタログからブランドやビジュアル素材を検索し、似た参考例を探す。

- [Bloomroom](bloomroom_2026-11-23.json) — 花や容器を選び、編集可能なデジタル3Dの花束を作る。
- [Animx](animx_2026-11-23.json) — 文章や静止画から画像・動画を生成し、進捗を確認する。
- [Vidova](vidova_2026-11-23.json) — 素材の内容を確認し、字幕や音楽を加えて動画の編集・出力を支援する。
- [Video Grab](video-grab_2026-11-23.json) — 再利用可能な動画とライセンス・出典表記を探し、自分の動画の公式書き出し手順を案内する。
- [Inkdrop](inkdrop_2026-11-23.json) — 画像をTシャツなどの商品に配置し、選択肢や完成イメージを確認する。
- [MAP Audio](map-audio_2026-11-23.json) — 録音の波形・音量を解析し、ビートや音声エフェクトを扱う。
- [App Listing Screenshots](app-listing-screenshots_2026-11-23.json) — アプリストア掲載用の画像を、見出しや端末枠を付けて作成する。
- [Packaging Design Assistant](packaging-design-assistant_2026-11-23.json) — 商品のパッケージ案、表示面、印刷準備やモックアップを検討する。
- [Moda - Slides & Designs](moda-slides-designs_2026-11-23.json) — 編集可能なスライドや販促・SNS向け素材を作成し、各形式に書き出す。
- [Phoenix One Prompt Studio](phoenix-one-prompt-studio_2026-11-23.json) — 画像・動画生成に使うプロンプトや映像演出の指示を作る。

- [ULLIMO](ullimo_2026-11-23.json) — 保存済みの音声・動画プロジェクトやトークン残高を確認し、音声生成を管理する。
- [Flat](flat_2026-11-23.json) — 楽譜を作成・検索し、MusicXMLやMIDIで書き出す。
- [Misar.Blog](misar-blog_2026-11-23.json) — ブログ記事の執筆・公開予定や反応の確認を支援する。
- [Adly](adly_2026-11-23.json) — ブランドに合わせたSNS投稿や広告の制作・予約投稿を支援する。 TikTok対応状況は説明間に相違があり未確認。

- [Clypmint: AI Video Editor](clypmint-ai-video-editor_2026-11-23.json) — 映像や台本から動画を作り、字幕やクリップの編集を支援する。
- [Image to Video (MegaScenes)](image-to-video-megascenes_2026-11-23.json) — MegaScenesの画像ライブラリから画像を選び、動きを指定して短い動画を作る。
- [TeamTime Make It Real](teamtime-make-it-real_2026-11-23.json) — 衣類のデザインを商品としてプレビューし、購入者や店舗所有者の操作を支援する。
- [Contenta Converter](contenta-converter_2026-11-23.json) — Windows上で画像の一括変換・縮小やPDFの画像化を支援する。

- [Viral Hook Engine](viral-hook-engine_2026-11-23.json) — SNS投稿の冒頭を、収録された型を使って作成・調整する。
- [AI Jingle Maker](ai-jingle-maker_2026-11-23.json) — 音声と既存の音素材を組み合わせ、短いジングルを制作する。
- [Print Shop by BYB](print-shop-by-byb_2026-11-23.json) — 画像からステッカーやラベルの印刷用プレビューと注文リンクを作る。
- [Glif](glif_2026-11-23.json) — 画像・動画・音声を同じプロジェクトで作成し、後から続きを編集する。
- [Globestudio](globestudio_2026-11-23.json) — ドット地図や3D地球儀のデザインリンクと埋め込みコードを作る。
- [AI Voiceover](ai-voiceover_2026-11-23.json) — 文章からナレーション音声を作り、MP3のリンクを返す。
- [Text to Speech (MegaScenes)](text-to-speech-megascenes_2026-11-23.json) — 台本を読み上げた音声をMegaScenesで作成する。
- [Wonder](wonder_2026-11-23.json) — 実際のHTML・CSSを使うキャンバスで画面の設計や編集を支援する。
- [Cattalog](cattalog_2026-11-23.json) — 表データや画像を使って商品カタログを作成・編集し、PDFに出力する。
- [One4Wall](one4wall_2026-11-23.json) — 雰囲気や色からスマートフォン向け壁紙を探し、表示・保存する。

- [refern Notan Generator](refern-notan-generator_2026-11-23.json) — 画像を2〜5段階の明暗に分け、絵や写真の構図を確認する。
- [Songtekst schrijven](songtekst-schrijven_2026-11-23.json) — 主にオランダ語で記念日などのオリジナル歌詞を作り、音節や韻を確認する。
- [Linepace Teleprompter](linepace-teleprompter_2026-11-23.json) — 原稿をスクロール表示し、スピーチの読み上げ時間を見積もる。
- [Ember Websites](ember-websites_2026-11-23.json) — 事業紹介やポートフォリオなどのサイトを会話で作り、プレビュー・公開する。
- [Faceless.video](faceless-video_2026-11-23.json) — 顔出しなしの動画を作り、SNSへの投稿を自動化すると説明する。
- [Music Generator (MegaScenes)](music-generator-megascenes_2026-11-23.json) — ジャンルや雰囲気を指定して、インストゥルメンタル曲を作る。
- [Gulab](gulab_2026-11-23.json) — 画像や短い動画を生成し、Gulabのプロジェクトで管理する。
- [PINOC](pinoc_2026-11-23.json) — 文章や動画から3Dキャラクター向けの動きや環境を作る。
- [UlazAI Media](ulazai-media_2026-11-23.json) — 対応モデルを選び、提供枠を使った非公開の1K画像生成を支援する。
- [DesignerBox](designerbox_2026-11-23.json) — 商品写真から広告やネットショップ向けの画像を作成・編集する。

- [Formatry](formatry_2026-11-23.json) — 商品写真や文章から広告を作成・編集し、画像や動画に出力する。
- [Fuzzbucket](fuzzbucket_2026-11-23.json) — ブランドに合わせた画像・動画・音声・文章の制作をワークスペースで管理する。
- [Luma AI](luma-ai_2026-11-23.json) — 画像や動画を生成し、動画の延長や画角の変更を行う。
- [CookUp](cookup_2026-11-23.json) — 保存した音楽セッションを再生・編集し、楽曲やビートの制作を支援する。
- [Diorama](diorama_2026-11-23.json) — 文章から小さな3Dボクセルの風景を作り、会話で変更する。
- [Ringoz](ringoz_2026-11-23.json) — 入力した言葉を歌う着信音やアラームを作る。
- [1TapEdit AI Studio](1tapedit-ai-studio_2026-11-23.json) — 画像・動画・ナレーションを生成する。
- [Video Crop](video-crop_2026-11-23.json) — 短い動画の中央を横長・縦長・正方形に切り抜く。
- [Media Studio (MegaScenes)](media-studio-megascenes_2026-11-23.json) — 複数のモデルから選び、画像・動画・音声や音楽を生成する。
- [HeyTurbine](heyturbine_2026-11-23.json) — ブランド調査・コンテンツ制作の説明と内包アプリ欄の読み取り専用の説明が異なり、対応範囲は未確認。


- [Krumzi](krumzi_2026-11-23.json) — SNS用の編集可能な画像やカルーセルを作成・出力する。
- [Textile Designer AI](textile-designer-ai_2026-11-23.json) — 柄を印刷用に調整し、繰り返し模様や色違いを作る。
- [Commish](commish_2026-11-23.json) — 物品の製作方法・数量別費用を検討し、見積もり依頼をまとめる。
- [Video Editor AI](video-editor-ai_2026-11-23.json) — ライブラリの動画を指示に沿って画風変更・リフレーム・延長する。
- [Image Upscaler](image-upscaler-megascenes_2026-11-23.json) — ライブラリ内の画像を高解像度に拡大する。
- [Viral Recreate Ai](viral-recreate-ai_2026-11-23.json) — 画像や動画を分析し、生成用プロンプトや動きの計画を作る。
- [AI Headshots — MyBestAngle](ai-headshots-mybestangle_2026-11-23.json) — 自分の自撮りからプロフィール用の人物画像を作成する。
- [Wevi](wevi_2026-11-23.json) — テンプレートと実際の製品画面を使い、ソフトウェアの紹介動画を作る。
- [Draw40](draw40_2026-11-23.json) — 保存した図やホワイトボードを作成・検索・編集する。
- [Tunmire](tunmire_2026-11-23.json) — 原稿から書籍本文PDF・EPUB・表紙を作り、出版規格の確認や編集レビューを行う。

## 一覧本体との照合

[名称照合の記録](catalog_name_audit_2026-11-14.json) — 詳細35件と作業ブランチの一覧3,941件を比較。34件は名前が一致、Palimpsestは一致なし。名前の一致は同一性の確定ではない。個々のJSONにある旧「照合未確認」の記載は調査時点の記録で、最新の照合結果はこの記録を参照。

## 再開

金融とクリエイティブの一覧から詳細調査を開始。各詳細を開いた後に一覧へ戻ると先頭へ戻ることがあるため、再開時は上記の記録と重複しないよう名前と詳細ページを確認する。次の候補は、一覧の短文だけでは対象や提供範囲が曖昧な項目から選ぶ。カテゴリー全体の選別・詳細調査はまだ完了していない。
