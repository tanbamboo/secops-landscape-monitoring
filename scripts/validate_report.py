#!/usr/bin/env python3
"""Validate SecOps landscape reports before publishing."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "Executive Summary",
    "Landscape Context",
    "What It Is",
    "Evidence-Backed Deep Dive",
    "Key Findings",
    "Differentiation Analysis",
    "Risks and Open Questions",
    "Sources",
]

WEASEL_WORDS = [
    "revolutionary",
    "best-in-class",
    "game-changing",
    "industry-leading",
    "unprecedented",
    "cutting-edge",
]

LINK_PATTERN = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
TIER_PATTERN = re.compile(r"\b[ABC]\b")


def validate_report(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"File not found: {path}"]

    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()

    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Missing required section: {section}")

    links = LINK_PATTERN.findall(content)
    if len(links) < 5:
        errors.append(f"Insufficient sources: found {len(links)} links, minimum 5 required")

    # Check sources section for tier tags
    sources_start = content.find("## Sources")
    if sources_start >= 0:
        sources_block = content[sources_start:]
        tier_count = len(re.findall(r"\|\s*[ABC]\s*\|", sources_block))
        if tier_count < 3:
            errors.append(f"Sources table needs tier tags (A/B/C) for at least 3 entries; found {tier_count}")
        ab_count = len(re.findall(r"\|\s*[AB]\s*\|", sources_block))
        if ab_count < 3:
            errors.append(f"At least 3 tier A or B sources required in Sources table; found {ab_count}")

    # Key Findings should have citations
    kf_start = content.find("## Key Findings")
    kf_end = content.find("## ", kf_start + 1) if kf_start >= 0 else -1
    if kf_start >= 0:
        kf_block = content[kf_start:kf_end] if kf_end > kf_start else content[kf_start:]
        bullets = [ln for ln in kf_block.splitlines() if ln.strip().startswith("-") and ln.strip() != "-"]
        for bullet in bullets:
            if bullet.strip() in ("-", "- ", "> Each bullet must include an inline citation to a tier A/B source."):
                continue
            if not LINK_PATTERN.search(bullet):
                errors.append(f"Key finding missing inline citation: {bullet.strip()[:80]}")

    # Weasel words check (unless in quotes)
    lower = content.lower()
    for word in WEASEL_WORDS:
        if word in lower:
            # Allow if appears in quoted context or as attributed claim
            for i, line in enumerate(lines):
                if word in line.lower() and '"' not in line and "'" not in line and "claims" not in line.lower():
                    errors.append(f"Weasel word '{word}' on line {i + 1} without attribution")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a SecOps landscape report")
    parser.add_argument("report", type=Path, help="Path to report markdown file")
    args = parser.parse_args()

    errors = validate_report(args.report)
    if errors:
        print(f"Validation FAILED for {args.report}:\n")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print(f"Validation PASSED for {args.report}")


if __name__ == "__main__":
    main()
