# 🌏 Plugin Atlas

**Find ChatGPT apps in your own language. Discover → Save → Use.**

**日本語** | [English](#english) · [Report a bug / 不具合報告](https://github.com/kotto0430/Plugin-Atlas/issues/new/choose)

## 日本語

Plugin Atlas は、ChatGPTで使えるアプリ・プラグインを**自分の言語で探し、保存し、呼び出す**ための無料の非公式ガイドです。

- **v2.9**：42アプリ、12カテゴリー、9言語に対応
- 名前や用途から検索、カテゴリー別の一覧表示
- 「マイアプリ」にお気に入りを登録し、次回からすぐ使える
- 「ChatGPTで使う」で依頼文をChatGPTに渡す
- スマートフォン・PCで利用可能。Android実機で動作確認済み

**公開ページ（GitHub Pages設定後に有効）：** https://kotto0430.github.io/Plugin-Atlas/

**使い方：** ページを開く → 言語を選ぶ → アプリを探す → 「マイアプリ」に登録 → 「使う」。

> ⚠️ Plugin Atlas は OpenAI 公式製品ではありません。ChatGPT側のアプリの提供状況・利用条件・接続状態はユーザーごとに異なります。「使う」ボタンはChatGPTへ依頼文を渡す仕組みで、アプリのインストールや実行を保証しません。

### 不具合報告・提案

[🐛 不具合を報告する](https://github.com/kotto0430/Plugin-Atlas/issues/new?template=bug_report.yml) · [💡 改善案・アプリ掲載希望](https://github.com/kotto0430/Plugin-Atlas/issues/new?template=feature_request.yml)

報告の際は「使用言語・端末・ブラウザ・再現手順」があると助かります。**メールアドレス、パスワード、認証情報などの個人情報は投稿しないでください。**

### プライバシー

マイアプリのお気に入りと言語設定はブラウザのローカルストレージに保存されます。ブラウザのデータを消すと登録内容も消える場合があります。ChatGPTのアプリ接続状況とは連動しません。外部サービスへのリンクを開くと、移動先のプライバシーポリシーが適用されます。

---

## English

Plugin Atlas is a **free, unofficial multilingual directory and launcher** for ChatGPT apps and plugins.

- **v2.9:** 42 curated apps, 12 categories, 9 interface languages
- Search by name or purpose; browse by category
- Save favorites in **My Apps** for quick access
- Send suggested prompts to ChatGPT using **Use in ChatGPT**
- Mobile-friendly; tested on a real Android device

**Public website (available after enabling GitHub Pages):** https://kotto0430.github.io/Plugin-Atlas/

**How to use:** Open the site → choose your language → find an app → save it to My Apps → select Use.

> Plugin Atlas is **not affiliated with or endorsed by OpenAI**. App availability and installation requirements vary. Sending a prompt to ChatGPT does not guarantee that an app is installed or invoked.

**Feedback:** [Report a bug](https://github.com/kotto0430/Plugin-Atlas/issues/new?template=bug_report.yml) · [Request a feature or app](https://github.com/kotto0430/Plugin-Atlas/issues/new?template=feature_request.yml)

**Privacy:** Favorites and language preferences are stored locally in your browser, not synced with ChatGPT. Do not share passwords or private data in public GitHub Issues.

---

## Development and catalog updates

- `index.html`: the stable standalone browser app
- `collector.py`: collects publicly available plugin metadata
- `known-plugins.json`: entries tracked by the collector (not necessarily the complete app catalog)
- `official-metadata.json`, `pending-translation.json`, `sync-report.json`: collector outputs
- `.github/workflows/sync.yml`: scheduled collector, **Tuesday 23:59 JST** (GitHub scheduling may be delayed)

**Important:** The collector currently gathers candidate information for review. It does **not** automatically translate, classify, or publish new apps to `index.html`. It does not use private ChatGPT APIs.

### Maintainer

Created by **Kotto & Yomi**. Feedback is welcome through GitHub Issues.
