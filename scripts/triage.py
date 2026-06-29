#!/usr/bin/env python3
"""Triage inbox items into the topic registry and manage lifecycle."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from typing import Any

from scripts.common import load_inbox, load_registry, save_inbox, save_registry, slug_from_name


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


if __name__ == "__main__":
    main()
