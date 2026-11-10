#!/usr/bin/env python3
"""Read PUBLIC OpenAI plugin pages; never access accounts or private APIs."""
import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
BASE = "https://openai.com/business/plugins/"
HEADERS = {"User-Agent": "PluginAtlasResearch/0.2 (public catalog; no login)"}


def approved(url):
    p = urlparse(url)
    if p.scheme != "https" or p.netloc != "openai.com":
        return None
    if not re.fullmatch(r"/business/plugins/(?:[a-z0-9-]+/)?", p.path):
        return None
    return "https://openai.com" + p.path


def links(html):
    soup = BeautifulSoup(html, "html.parser")
    return sorted({u for a in soup.select("a[href]")
                   if (u := approved(urljoin(BASE, a["href"]))) and u != BASE})


def discover_browser(max_clicks):
    """Click the site's public Load more control if present."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page(locale="en-US", viewport={"width": 1360, "height": 900})
            page.goto(BASE, wait_until="domcontentloaded", timeout=30000)
            for _ in range(max_clicks):
                button = page.get_by_role("button", name=re.compile("load more", re.I))
                if not button.count() or not button.first.is_visible() or not button.first.is_enabled():
                    break
                before = len(links(page.content()))
                button.first.click(timeout=5000)
                try:
                    page.wait_for_function(
                        "n => document.querySelectorAll('a[href*=\"/business/plugins/\"]').length > n",
                        arg=before, timeout=4000)
                except Exception:
                    if len(links(page.content())) <= before:
                        break
            return links(page.content())
        finally:
            browser.close()


def read_json(name, default):
    path = HERE / name
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def save_json(name, obj):
    (HERE / name).write_text(
        json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8")


def parse(url, html):
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find("main") or soup
    h1 = main.find("h1")
    if not h1:
        return None
    name = h1.get_text(" ", strip=True)
    if not 1 <= len(name) <= 120:
        return None
    desc = soup.find("meta", attrs={"name": "description"})
    summary = (desc.get("content", "") if desc else "").strip()
    if not summary:
        p = h1.find_next("p")
        summary = p.get_text(" ", strip=True) if p else ""
    how = ""
    for h in main.find_all(["h2", "h3"]):
        if h.get_text(" ", strip=True).casefold() == "how it works":
            parts = []
            for sibling in h.next_elements:
                if sibling is h:
                    continue
                if getattr(sibling, "name", None) == "h2":
                    break
                if getattr(sibling, "name", None) == "p":
                    t = sibling.get_text(" ", strip=True)
                    if t and t not in parts:
                        parts.append(t)
                if len(parts) >= 3:
                    break
            how = " ".join(parts)
            break
    if not summary and not how:
        return None
    record = {"name": name, "url": url, "summary": summary[:800],
              "howItWorks": how[:1800]}
    record["contentHash"] = hashlib.sha256(
        json.dumps(record, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()[:16]
    return record


def run(args):
    session = requests.Session()
    def fetch(url):
        if not approved(url):
            raise ValueError("Unapproved URL")
        r = session.get(url, headers=HEADERS, timeout=25, allow_redirects=False)
        r.raise_for_status()
        if len(r.content) > 5_000_000:
            raise ValueError("Page too large")
        return r.text

    directory = fetch(BASE)
    urls = set(links(directory))
    if args.browser_discovery:
        try:
            extra = discover_browser(args.max_clicks)
            urls.update(extra)
            print("Chromium discovered", len(extra), "detail links")
        except Exception as exc:
            print("WARN browser discovery:", str(exc)[:200], file=sys.stderr)
    old = read_json("official-metadata.json", {"plugins": {}})
    for entry in old.get("plugins", {}).values():
        if approved(entry.get("url", "")):
            urls.add(entry["url"])
    known = {name.casefold(): ident for name, ident in
             read_json("known-plugins.json", {}).items()}
    known.update({"teams": "teams", "ticktick:to-do list & calendar": "tick"})
    previous = dict(old.get("plugins", {}))
    pending = dict(read_json("pending-translation.json", {"plugins": {}}).get("plugins", {}))
    changes = []
    parsed = 0
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for url in sorted(urls)[:args.max_pages]:
        try:
            item = parse(url, fetch(url))
            if not item:
                print("WARN no metadata:", url)
                continue
            parsed += 1
            ident = known.get(item["name"].casefold())
            if not ident:
                for old_id, old_item in previous.items():
                    if old_item.get("url") == url:
                        ident = old_id
                        break
            if ident:
                if previous.get(ident, {}).get("contentHash") != item["contentHash"]:
                    changes.append({"id": ident, "name": item["name"]})
                item["checkedAt"] = date
                previous[ident] = item
            else:
                pending[item["name"]] = item
        except (requests.RequestException, ValueError) as exc:
            print("WARN detail:", url, str(exc)[:150], file=sys.stderr)
        time.sleep(args.delay)
    if parsed == 0:
        raise RuntimeError("No detail pages parsed: leaving previous JSON untouched")
    save_json("official-metadata.json", {
        "source": "OpenAI public plugin pages; incomplete catalog possible",
        "lastSuccessfulCheck": date, "pagesParsed": parsed, "plugins": previous})
    save_json("pending-translation.json", {
        "checkedAt": date, "note": "Review and translate before publishing",
        "plugins": pending})
    save_json("sync-report.json", {
        "checkedAt": date, "directoryLinksFound": len(urls),
        "pagesParsed": parsed, "knownPluginsChanged": changes,
        "pendingNames": sorted(pending)})
    print("Success:", parsed, "pages,", len(changes), "known changes,",
          len(pending), "pending entries")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--browser-discovery", action="store_true")
    ap.add_argument("--max-pages", type=int, default=100)
    ap.add_argument("--max-clicks", type=int, default=40)
    ap.add_argument("--delay", type=float, default=0.4)
    run(ap.parse_args())
