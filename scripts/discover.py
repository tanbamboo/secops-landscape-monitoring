#!/usr/bin/env python3
"""Poll discovery sources and append new candidates to topics/inbox.yaml."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from datetime import date
from email.utils import parsedate_to_datetime
from typing import Any

import feedparser
import httpx

from scripts.common import (
    CONFIG_DIR,
    existing_keys,
    is_duplicate,
    load_inbox,
    load_registry,
    load_yaml,
    make_id,
    normalize_url,
    save_inbox,
    slug_from_name,
)

ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
ARXIV_NS = {"arxiv": "http://arxiv.org/schemas/atom"}


RSS_HEADERS = {
    "User-Agent": "secops-landscape-monitoring/0.1",
    "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
}


def _parse_rss_feed(url: str) -> feedparser.FeedParserDict:
    feed = feedparser.parse(url)
    if feed.entries:
        return feed
    try:
        with httpx.Client(timeout=30.0, follow_redirects=True, headers=RSS_HEADERS) as client:
            resp = client.get(url)
            resp.raise_for_status()
            return feedparser.parse(resp.content)
    except Exception:
        return feed


def fetch_rss(sources: list[dict[str, Any]], today: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for source in sources:
        try:
            feed = _parse_rss_feed(source["url"])
        except Exception as exc:
            print(f"  RSS skip {source['name']}: {exc}", file=sys.stderr)
            continue
        if not feed.entries:
            print(f"  RSS empty {source['name']}: {source['url']}", file=sys.stderr)
            continue
        for entry in feed.entries[:15]:
            title = (entry.get("title") or "").strip()
            link = (entry.get("link") or "").strip()
            if not title or not link:
                continue
            snippet = (entry.get("summary") or entry.get("description") or "")[:500]
            snippet = re.sub(r"<[^>]+>", "", snippet).strip()
            items.append(
                {
                    "id": make_id("rss", title, link),
                    "name": title,
                    "discovered_at": today,
                    "source": "rss",
                    "source_name": source["name"],
                    "source_url": link,
                    "source_tier": source.get("tier", "A"),
                    "categories": source.get("categories", []),
                    "snippet": snippet,
                    "status": "inbox",
                }
            )
    return items


def fetch_github(config: dict[str, Any], today: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    gh = config.get("github", {})
    base_url = gh.get("base_url", "https://api.github.com/search/repositories")
    per_page = gh.get("per_page", 10)
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "secops-landscape-monitoring",
    }
    with httpx.Client(timeout=30.0, headers=headers) as client:
        for query in gh.get("queries", []):
            params = {"q": query["q"], "sort": "updated", "order": "desc", "per_page": per_page}
            try:
                resp = client.get(base_url, params=params)
                resp.raise_for_status()
                data = resp.json()
            except Exception as exc:
                print(f"  GitHub skip '{query['q']}': {exc}", file=sys.stderr)
                continue
            for repo in data.get("items", []):
                name = repo.get("full_name") or repo.get("name", "")
                url = repo.get("html_url", "")
                if not name or not url:
                    continue
                items.append(
                    {
                        "id": make_id("github", name, url),
                        "name": name,
                        "discovered_at": today,
                        "source": "github",
                        "source_name": "GitHub",
                        "source_url": url,
                        "source_tier": "B",
                        "categories": query.get("categories", []),
                        "snippet": (repo.get("description") or "")[:500],
                        "metadata": {
                            "stars": repo.get("stargazers_count"),
                            "language": repo.get("language"),
                            "updated_at": repo.get("updated_at"),
                        },
                        "status": "inbox",
                    }
                )
    return items


def fetch_hackernews(config: dict[str, Any], today: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    hn = config.get("hackernews", {})
    base_url = hn.get("base_url", "https://hn.algolia.com/api/v1/search")
    with httpx.Client(timeout=30.0) as client:
        for query in hn.get("queries", []):
            params = {
                "query": query["query"],
                "tags": query.get("tags", "story"),
                "hitsPerPage": 10,
            }
            try:
                resp = client.get(base_url, params=params)
                resp.raise_for_status()
                data = resp.json()
            except Exception as exc:
                print(f"  HN skip '{query['query']}': {exc}", file=sys.stderr)
                continue
            for hit in data.get("hits", []):
                title = hit.get("title") or hit.get("story_title") or ""
                url = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID', '')}"
                if not title:
                    continue
                items.append(
                    {
                        "id": make_id("hn", title, url),
                        "name": title,
                        "discovered_at": today,
                        "source": "hackernews",
                        "source_name": "Hacker News",
                        "source_url": url,
                        "source_tier": "A",
                        "categories": query.get("categories", []),
                        "snippet": (hit.get("comment_text") or "")[:300],
                        "metadata": {"points": hit.get("points"), "num_comments": hit.get("num_comments")},
                        "status": "inbox",
                    }
                )
    return items


def fetch_arxiv(config: dict[str, Any], today: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    arxiv_cfg = config.get("arxiv", {})
    base_url = arxiv_cfg.get("base_url", "http://export.arxiv.org/api/query")
    max_results = arxiv_cfg.get("max_results", 15)
    category = arxiv_cfg.get("category", "cs.CR")
    default_categories = arxiv_cfg.get("categories", ["data_ai", "detection_response"])

    with httpx.Client(timeout=30.0) as client:
        for term in arxiv_cfg.get("search_terms", []):
            params = {
                "search_query": f"cat:{category} AND all:{term}",
                "start": 0,
                "max_results": max_results,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }
            try:
                resp = client.get(base_url, params=params)
                resp.raise_for_status()
                root = ET.fromstring(resp.text)
            except Exception as exc:
                print(f"  arXiv skip '{term}': {exc}", file=sys.stderr)
                continue
            for entry in root.findall("atom:entry", ATOM_NS):
                title_el = entry.find("atom:title", ATOM_NS)
                id_el = entry.find("atom:id", ATOM_NS)
                summary_el = entry.find("atom:summary", ATOM_NS)
                title = (title_el.text if title_el is not None else "").strip().replace("\n", " ")
                url = (id_el.text if id_el is not None else "").strip()
                summary = (summary_el.text if summary_el is not None else "").strip().replace("\n", " ")
                if not title or not url:
                    continue
                items.append(
                    {
                        "id": make_id("arxiv", title, url),
                        "name": title,
                        "discovered_at": today,
                        "source": "arxiv",
                        "source_name": "arXiv",
                        "source_url": url,
                        "source_tier": "B",
                        "categories": default_categories,
                        "snippet": summary[:500],
                        "status": "inbox",
                    }
                )
    return items


def discover() -> tuple[int, int]:
    today = date.today().isoformat()
    config = load_yaml(CONFIG_DIR / "sources.yaml")
    registry = load_registry()
    inbox = load_inbox()
    keys = existing_keys(registry, inbox)

    print("Discovering from RSS...")
    rss_items = fetch_rss(config.get("rss", []), today)
    print(f"  Found {len(rss_items)} RSS entries")

    print("Discovering from GitHub...")
    gh_items = fetch_github(config, today)
    print(f"  Found {len(gh_items)} GitHub repos")

    print("Discovering from Hacker News...")
    hn_items = fetch_hackernews(config, today)
    print(f"  Found {len(hn_items)} HN stories")

    print("Discovering from arXiv...")
    arxiv_items = fetch_arxiv(config, today)
    print(f"  Found {len(arxiv_items)} arXiv papers")

    all_candidates = rss_items + gh_items + hn_items + arxiv_items
    new_items: list[dict[str, Any]] = []
    skipped = 0

    for item in all_candidates:
        if is_duplicate(item, keys):
            skipped += 1
            continue
        new_items.append(item)
        keys.add(item["id"])
        keys.add(slug_from_name(item["name"]))
        if item.get("source_url"):
            keys.add(normalize_url(item["source_url"]))

    if new_items:
        inbox.extend(new_items)
        save_inbox(inbox)

    return len(new_items), skipped


def main() -> None:
    new_count, skipped = discover()
    print(f"\nDone: {new_count} new items added to inbox, {skipped} duplicates skipped.")


if __name__ == "__main__":
    main()
