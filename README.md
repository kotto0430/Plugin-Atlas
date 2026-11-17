# 🌏 Plugin Atlas

[English](README.md) · [日本語](docs/README.ja.md) · [Esperanto](docs/README.eo.md) · [Français](docs/README.fr.md) · [Español](docs/README.es.md) · [Deutsch](docs/README.de.md) · [Português](docs/README.pt.md) · [中文](docs/README.zh.md) · [한국어](docs/README.ko.md)

**Find ChatGPT apps in your own language. Discover → Save → Use.**

Plugin Atlas is a **free, unofficial multilingual guide and launcher** for discovering, saving, and using ChatGPT apps and plugins.

## Features

- **134 ChatGPT apps, 16 categories, 9 interface languages** (v3.12)
- Search by name or purpose and browse by category
- Save favorites in **My Apps** for quick access
- Send suggested prompts to ChatGPT with **Use in ChatGPT**
- Mobile-friendly; tested on a real Android device

## Open the app

**[Launch Plugin Atlas](https://kotto0430.github.io/Plugin-Atlas/)**

If you see a 404 error, GitHub Pages deployment may still be in progress.

## How to use

Open the site → choose your language → find an app → save it to My Apps → select Use.

## Feedback and app requests

[🐛 Report a bug](https://github.com/kotto0430/Plugin-Atlas/issues/new?template=bug_report.yml) · [💡 Suggest a feature or app](https://github.com/kotto0430/Plugin-Atlas/issues/new?template=feature_request.yml)

Please include your display language, device, browser, and steps to reproduce an issue. **Do not share email addresses, passwords, access keys, or personal information in public issues.**

## Privacy

Favorites and language preferences are stored locally in your browser. They may disappear if you clear browser data. They do **not** sync with apps installed in ChatGPT. Opening external links takes you to other services governed by their own privacy policies.

## Important disclaimer

Plugin Atlas is **not affiliated with or endorsed by OpenAI**. App availability and requirements vary by user and region. The Use button sends a prompt to ChatGPT; it does not guarantee that an app is installed or invoked.

## Development and catalog updates

- `index.html`: the stable standalone browser app
- `collector.py`: collects publicly accessible plugin metadata
- `known-plugins.json`: tracked collector entries, not necessarily the complete app catalog
- `official-metadata.json`, `pending-translation.json`, `sync-report.json`: collector outputs
- `.github/workflows/sync.yml`: scheduled collector, **Tuesday 23:59 JST** (GitHub scheduling may be delayed)

The collector currently gathers candidate information for review. It does **not** automatically translate, classify, or publish new apps to `index.html`. It does not use private ChatGPT APIs.

---

Created by **Kotto & Yomi**. Contributions and feedback are welcome through GitHub Issues.
