#!/usr/bin/env python3
"""Generate a daily SecOps landscape brief outline from the topic registry."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

from scripts.common import ROOT, load_registry

BRIEFS_DIR = ROOT / "briefs"
MAX_TOPICS = 5


def pick_topics(limit: int = MAX_TOPICS) -> list[dict]:
    skip_slugs = {
        "waydabber-betterdisplay",
        "mthcht-awesome-lists",
        "sentinel-enterprise-siem-for-startups-splunk-alternativ",
    }
    topics = [
        t
        for t in load_registry()
        if t.get("status") != "published"
        and t.get("slug") not in skip_slugs
        and t.get("type") in ("startup", "technology", "product")
    ]
    topics.sort(key=lambda t: t.get("triage_score", 0), reverse=True)
    return topics[:limit]


def render_outline(topics: list[dict], today: str) -> str:
    lines = [
        f"# SecOps Landscape 每日简报（大纲）",
        "",
        f"**日期：** {today}  ",
        f"**状态：** 待 Agent 深化撰写",
        "",
        "> 运行 `python scripts/generate_brief.py --write` 生成大纲；"
        "由 Cursor Agent 补充深度介绍后保存为完整简报。",
        "",
        "## 今日候选（按 triage score）",
        "",
    ]
    for i, t in enumerate(topics, 1):
        src = (t.get("sources") or [{}])[0]
        lines.extend(
            [
                f"### {i}. {t.get('name', t.get('slug', ''))}",
                "",
                f"- **Slug:** `{t.get('slug')}`",
                f"- **类型:** {t.get('type')} | **优先级:** {t.get('priority')} | **Score:** {t.get('triage_score', 0)}",
                f"- **分类:** {', '.join(t.get('categories', []))}",
                f"- **来源:** {src.get('url', '')}",
                f"- **摘要:** {t.get('snippet', '')[:300]}",
                "",
                "#### 待撰写",
                "- 是什么",
                "- 与 incumbent 差异",
                "- 风险与开放问题",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate daily SecOps brief outline")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write briefs/YYYY-MM-DD-secops-landscape-outline.md",
    )
    parser.add_argument("--limit", type=int, default=MAX_TOPICS)
    args = parser.parse_args()

    today = date.today().isoformat()
    topics = pick_topics(args.limit)
    if not topics:
        print("No unpublished topics found.", file=sys.stderr)
        sys.exit(1)

    content = render_outline(topics, today)
    if args.write:
        BRIEFS_DIR.mkdir(exist_ok=True)
        path = BRIEFS_DIR / f"{today}-secops-landscape-outline.md"
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path}")
    else:
        print(content)


if __name__ == "__main__":
    main()
