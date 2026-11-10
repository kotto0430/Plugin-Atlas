# Plugin Atlas 🌏

A multilingual guide to ChatGPT plugins. This private repository is the experimental home of the **automatic public-catalog collector**.

## Status
- Android-tested **v2.5 HTML app** is kept separate until its complete release package is uploaded.
- The collector reads only publicly accessible pages on `openai.com/business/plugins/`; it does **not** use private ChatGPT APIs.
- Every Tuesday at **08:20 JST**, GitHub Actions attempts to discover plugin pages and writes JSON reports. GitHub schedules can be delayed.
- New apps go to `pending-translation.json` for human review. **No automatic 9-language translation or publication yet.**
- The first live GitHub Actions run must be validated before we claim that online collection works.

## Files
- `collector.py`: public-page discovery and metadata collection
- `known-plugins.json`: IDs of the 27 curated entries
- `.github/workflows/sync.yml`: scheduled/manual collector run
- `official-metadata.json`, `pending-translation.json`, `sync-report.json`: generated on a successful run

## First test
On GitHub, open **Actions → Refresh plugin metadata → Run workflow**. Check the job log and the generated JSON files.

The stable Android HTML should never be modified by the collector.
