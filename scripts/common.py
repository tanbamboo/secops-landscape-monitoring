"""Shared utilities for SecOps landscape monitoring scripts."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parent.parent
TOPICS_DIR = ROOT / "topics"
CONFIG_DIR = ROOT / "config"


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, dict) else {}


def save_yaml(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def normalize_name(name: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", name.lower().strip())
    return cleaned.strip("-")


def normalize_url(url: str) -> str:
    parsed = urlparse(url.strip().lower())
    host = parsed.netloc.removeprefix("www.")
    path = parsed.path.rstrip("/")
    return f"{host}{path}"


def slug_from_name(name: str) -> str:
    return normalize_name(name)[:80]


def make_id(source: str, name: str, url: str = "") -> str:
    base = slug_from_name(name)
    if url:
        host = urlparse(url).netloc.replace("www.", "").split(".")[0]
        if host and host not in base:
            return f"{source}-{host}-{base}"[:100]
    return f"{source}-{base}"[:100]


def load_inbox() -> list[dict[str, Any]]:
    return load_yaml(TOPICS_DIR / "inbox.yaml").get("items", []) or []


def save_inbox(items: list[dict[str, Any]]) -> None:
    save_yaml(TOPICS_DIR / "inbox.yaml", {"items": items})


def load_registry() -> list[dict[str, Any]]:
    return load_yaml(TOPICS_DIR / "registry.yaml").get("topics", []) or []


def save_registry(topics: list[dict[str, Any]]) -> None:
    save_yaml(TOPICS_DIR / "registry.yaml", {"topics": topics})


def existing_keys(registry: list[dict[str, Any]], inbox: list[dict[str, Any]]) -> set[str]:
    keys: set[str] = set()
    for item in registry + inbox:
        keys.add(item.get("id", ""))
        keys.add(normalize_name(item.get("name", "")))
        url = item.get("source_url", "")
        if url:
            keys.add(normalize_url(url))
    keys.discard("")
    return keys


def is_duplicate(item: dict[str, Any], keys: set[str]) -> bool:
    item_id = item.get("id", "")
    if item_id and item_id in keys:
        return True
    name_key = normalize_name(item.get("name", ""))
    if name_key and name_key in keys:
        return True
    url = item.get("source_url", "")
    if url and normalize_url(url) in keys:
        return True
    return False
