#!/usr/bin/env python3
"""Triage inbox items into the topic registry and manage lifecycle."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from typing import Any

from scripts.common import load_inbox, load_registry, save_inbox, save_registry, slug_from_name

OFF_TOPIC_PATTERNS = (
    "autonomous car",
    "autonomous society",
    "volga german",
    "home security startup",
    "polymarket",
    "instagram bot",
    "fireeye shares",
    "slicklogin",
    "autonomous flying",
    "autonomous vehicles for social",
    "driving is social",
    "apple loses copyright",
    "corellium",
    "ask hn: what are the interesting security startups",
    "web startup security is failing",
    "tinfoil security -- security for startups. launching soon",
)

STARTUP_SIGNALS = (
    "raises",
    "million",
    "funding",
    "seed round",
    "series a",
    "series b",
    "series c",
    "stealth",
    "venture",
    "startup",
)

SECOPS_SIGNALS = (
    "siem",
    "soar",
    "soc",
    "xdr",
    "edr",
    "mdr",
    "detection",
    "threat hunt",
    "cnapp",
    "cspm",
    "ciem",
    "agentic",
    "autonomous soc",
    "mitre",
    "sigma",
    "security operations",
    "secops",
    "llm",
    "ai soc",
    "orchestration",
    "attack surface",
    "vulnerability",
    "exposure management",
    "identity governance",
    "guardian agent",
    "cybersecurity",
    "security platform",
    "wazuh",
    "splunk",
)


def list_inbox() -> None:
    inbox = load_inbox()
    if not inbox:
        print("Inbox is empty.")
        return
    for item in inbox:
        cats = ", ".join(item.get("categories", []))
        print(f"  {item['id']}")
        print(f"    name: {item.get('name', '')[:80]}")
        print(f"    source: {item.get('source')} | categories: {cats}")
        print(f"    url: {item.get('source_url', '')[:100]}")


def list_registry(status: str | None = None) -> None:
    topics = load_registry()
    if status:
        topics = [t for t in topics if t.get("status") == status]
    if not topics:
        print("Registry is empty." if not status else f"No topics with status '{status}'.")
        return
    for topic in topics:
        cats = ", ".join(topic.get("categories", []))
        print(f"  {topic.get('slug', topic.get('id', ''))} [{topic.get('status')}] ({topic.get('priority', 'medium')})")
        print(f"    name: {topic.get('name', '')[:80]}")
        print(f"    type: {topic.get('type', 'technology')} | categories: {cats}")


def infer_topic_type(item: dict[str, Any]) -> str:
    text = f"{item.get('name', '')} {item.get('snippet', '')}".lower()
    source = item.get("source", "")
    if any(s in text for s in STARTUP_SIGNALS):
        return "startup"
    if source == "arxiv":
        return "research"
    if source == "github":
        return "technology"
    if source == "rss":
        return "product" if "platform" in text or "solution" in text else "technology"
    return "technology"


def score_item(item: dict[str, Any]) -> tuple[int, str, str]:
    """Return (score, priority, topic_type)."""
    text = f"{item.get('name', '')} {item.get('snippet', '')}".lower()
    if any(pattern in text for pattern in OFF_TOPIC_PATTERNS):
        return 0, "low", infer_topic_type(item)

    score = 0
    topic_type = infer_topic_type(item)

    if any(s in text for s in ("raises", "million", "funding", "seed", "series a", "series b", "stealth")):
        score += 40
        topic_type = "startup"
    elif "startup" in text:
        score += 25
        topic_type = "startup"

    score += sum(8 for signal in SECOPS_SIGNALS if signal in text)

    stars = (item.get("metadata") or {}).get("stars") or 0
    if stars >= 1000:
        score += 30
    elif stars >= 500:
        score += 20
    elif stars >= 100:
        score += 10

    if item.get("source") == "rss":
        score += 5
    if item.get("source_tier") == "A":
        score += 3
    if item.get("source_tier") == "B":
        score += 2

    points = (item.get("metadata") or {}).get("points") or 0
    if points >= 100:
        score += 10
    elif points >= 30:
        score += 5

    if score >= 50:
        priority = "high"
    elif score >= 20:
        priority = "medium"
    else:
        priority = "low"

    return score, priority, topic_type


def unique_slug(base: str, existing: set[str], item_id: str) -> str:
    if base not in existing:
        return base
    suffix = re.sub(r"[^a-z0-9]+", "-", item_id.lower())[-24:].strip("-")
    candidate = f"{base}-{suffix}"[:80]
    n = 2
    while candidate in existing:
        candidate = f"{base}-{suffix}-{n}"[:80]
        n += 1
    return candidate


def item_to_topic(
    item: dict[str, Any],
    priority: str,
    topic_type: str,
    score: int,
    existing_slugs: set[str],
) -> dict[str, Any]:
    slug = unique_slug(slug_from_name(item["name"]), existing_slugs, item["id"])
    existing_slugs.add(slug)
    topic: dict[str, Any] = {
        "id": item["id"],
        "slug": slug,
        "name": item["name"],
        "type": topic_type,
        "categories": item.get("categories", []),
        "status": "archived" if priority == "low" and score == 0 else "new",
        "priority": priority,
        "discovered_at": item.get("discovered_at", date.today().isoformat()),
        "last_researched_at": None,
        "sources": [
            {
                "url": item.get("source_url", ""),
                "tier": item.get("source_tier", "A"),
                "label": item.get("source_name", item.get("source", "")),
            }
        ],
        "incumbent_comparison": item.get("categories", []),
        "snippet": item.get("snippet", ""),
        "discovery_source": item.get("source", ""),
        "triage_score": score,
    }
    if item.get("metadata"):
        topic["metadata"] = item["metadata"]
    return topic


def triage_all() -> dict[str, int]:
    inbox = load_inbox()
    registry = load_registry()
    existing_ids = {t.get("id") for t in registry}
    existing_slugs = {t.get("slug") for t in registry if t.get("slug")}

    promoted = 0
    skipped = 0
    counts = {"high": 0, "medium": 0, "low": 0}

    remaining: list[dict[str, Any]] = []
    for item in inbox:
        if item["id"] in existing_ids:
            skipped += 1
            continue

        score, priority, topic_type = score_item(item)
        topic = item_to_topic(item, priority, topic_type, score, existing_slugs)
        registry.append(topic)
        existing_ids.add(item["id"])
        counts[priority] += 1
        promoted += 1

    save_registry(registry)
    save_inbox(remaining)
    return {"promoted": promoted, "skipped": skipped, **counts}


def list_top(priority: str = "high", limit: int = 5, startups_only: bool = False) -> None:
    topics = load_registry()
    if startups_only:
        topics = [t for t in topics if t.get("type") == "startup"]
    topics = [t for t in topics if t.get("priority") == priority and t.get("status") != "published"]
    topics.sort(key=lambda t: t.get("triage_score", 0), reverse=True)
    if not topics:
        print(f"No {priority}-priority topics found.")
        return
    for topic in topics[:limit]:
        score = topic.get("triage_score", "?")
        print(f"  {topic.get('slug')} (score: {score}) [{topic.get('status')}]")
        print(f"    name: {topic.get('name', '')[:90]}")
        print(f"    type: {topic.get('type')} | categories: {', '.join(topic.get('categories', []))}")
        url = (topic.get("sources") or [{}])[0].get("url", "")
        if url:
            print(f"    url: {url[:100]}")


def promote(
    inbox_id: str,
    priority: str = "medium",
    topic_type: str = "technology",
    incumbent_comparison: list[str] | None = None,
) -> None:
    inbox = load_inbox()
    registry = load_registry()
    match = next((i for i in inbox if i["id"] == inbox_id), None)
    if not match:
        print(f"Error: inbox item '{inbox_id}' not found.", file=sys.stderr)
        sys.exit(1)

    slug = slug_from_name(match["name"])
    if any(t.get("slug") == slug for t in registry):
        print(f"Error: topic with slug '{slug}' already in registry.", file=sys.stderr)
        sys.exit(1)

    topic: dict[str, Any] = {
        "id": match["id"],
        "slug": slug,
        "name": match["name"],
        "type": topic_type,
        "categories": match.get("categories", []),
        "status": "new",
        "priority": priority,
        "discovered_at": match.get("discovered_at", date.today().isoformat()),
        "last_researched_at": None,
        "sources": [
            {
                "url": match.get("source_url", ""),
                "tier": match.get("source_tier", "A"),
                "label": match.get("source_name", match.get("source", "")),
            }
        ],
        "incumbent_comparison": incumbent_comparison or match.get("categories", []),
        "snippet": match.get("snippet", ""),
        "discovery_source": match.get("source", ""),
    }
    if match.get("metadata"):
        topic["metadata"] = match["metadata"]

    registry.append(topic)
    inbox = [i for i in inbox if i["id"] != inbox_id]
    save_registry(registry)
    save_inbox(inbox)
    print(f"Promoted '{match['name'][:60]}' -> registry slug '{slug}' (status: new, priority: {priority})")


def set_status(slug: str, status: str) -> None:
    registry = load_registry()
    topic = next((t for t in registry if t.get("slug") == slug), None)
    if not topic:
        print(f"Error: topic '{slug}' not found.", file=sys.stderr)
        sys.exit(1)
    topic["status"] = status
    if status in ("researching", "draft", "published"):
        topic["last_researched_at"] = date.today().isoformat()
    save_registry(registry)
    print(f"Updated '{slug}' status -> {status}")


def add_source(slug: str, url: str, tier: str, label: str = "") -> None:
    registry = load_registry()
    topic = next((t for t in registry if t.get("slug") == slug), None)
    if not topic:
        print(f"Error: topic '{slug}' not found.", file=sys.stderr)
        sys.exit(1)
    sources = topic.setdefault("sources", [])
    if any(s.get("url") == url for s in sources):
        print(f"Source already registered for '{slug}'.")
        return
    sources.append({"url": url, "tier": tier, "label": label or url})
    save_registry(registry)
    print(f"Added tier-{tier} source to '{slug}'")


def main() -> None:
    parser = argparse.ArgumentParser(description="Triage SecOps landscape topics")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("inbox", help="List inbox items")

    reg_parser = sub.add_parser("list", help="List registry topics")
    reg_parser.add_argument("--status", help="Filter by status")

    promote_parser = sub.add_parser("promote", help="Promote inbox item to registry")
    promote_parser.add_argument("inbox_id", help="Inbox item ID")
    promote_parser.add_argument("--priority", choices=["high", "medium", "low"], default="medium")
    promote_parser.add_argument("--type", dest="topic_type", choices=["startup", "product", "technology", "research"], default="technology")
    promote_parser.add_argument("--incumbents", nargs="*", help="Category keys for incumbent comparison")

    status_parser = sub.add_parser("status", help="Update topic status")
    status_parser.add_argument("slug")
    status_parser.add_argument("status", choices=["new", "researching", "draft", "published", "stale", "archived"])

    source_parser = sub.add_parser("add-source", help="Add a source URL to a topic")
    source_parser.add_argument("slug")
    source_parser.add_argument("url")
    source_parser.add_argument("--tier", choices=["A", "B", "C"], required=True)
    source_parser.add_argument("--label", default="")

    triage_all_parser = sub.add_parser("triage-all", help="Bulk-promote all inbox items with auto priority")
    top_parser = sub.add_parser("top", help="List highest-priority registry topics")
    top_parser.add_argument("--priority", choices=["high", "medium", "low"], default="high")
    top_parser.add_argument("--limit", type=int, default=5)
    top_parser.add_argument("--startups-only", action="store_true")

    args = parser.parse_args()

    if args.command == "inbox":
        list_inbox()
    elif args.command == "list":
        list_registry(args.status)
    elif args.command == "promote":
        promote(args.inbox_id, args.priority, args.topic_type, args.incumbents)
    elif args.command == "status":
        set_status(args.slug, args.status)
    elif args.command == "add-source":
        add_source(args.slug, args.url, args.tier, args.label)
    elif args.command == "triage-all":
        stats = triage_all()
        print(
            f"Triage complete: {stats['promoted']} promoted "
            f"(high={stats['high']}, medium={stats['medium']}, low={stats['low']}), "
            f"{stats['skipped']} skipped (already in registry)."
        )
    elif args.command == "top":
        list_top(args.priority, args.limit, args.startups_only)


if __name__ == "__main__":
    main()
