# SecOps Landscape Monitoring

Ongoing monitoring of startups and emerging technologies in Security Operations. Discovery scripts surface candidates; structured research workflows produce fact-grounded reports that analyze differentiation from the current landscape—not vendor marketing.

## Scope

Broad SecOps coverage:

- Detection & response (SIEM, XDR, EDR, MDR, threat hunting)
- Automation & orchestration (SOAR, playbooks, case management)
- Cloud & identity security (CNAPP, CSPM, IAM, zero trust)
- Data pipeline & AI in SecOps (LLM agents, autonomous SOC, ML detection)
- Vulnerability & exposure management (ASM, EASM, VM)

## Workflow

```
Discovery (scripts) → Inbox → Triage → Registry → Research → Report
```

1. **Discover** — Poll RSS, GitHub, Hacker News, and arXiv for new candidates.
2. **Triage** — Promote promising inbox items to the topic registry with priority.
3. **Research** — Gather primary sources, build claims-evidence tables, compare to incumbents.
4. **Report** — Publish validated reports under `reports/`.

## Quick Start

```bash
# Install dependencies
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e .

# Run discovery
python scripts/discover.py

# Triage an inbox item into the registry
python scripts/triage.py promote <inbox-id> --priority high --type startup

# List registry topics
python scripts/triage.py list

# Validate a report before publishing
python scripts/validate_report.py reports/2026-06-example.md
```

## Research with AI

Ask Cursor:

> Research topic `{slug}` from the registry. Follow `.cursor/rules/secops-research-standards.mdc`, complete `research/{slug}/` notes, and write the report using `templates/report.md`.

## Source Quality Standards

| Tier | Examples | Use |
|------|----------|-----|
| A | Independent news, HN, practitioner blogs | Funding, launches, discourse |
| B | GitHub, arXiv, conference talks, patents, SEC filings | Primary technical evidence |
| C | Vendor blogs, press releases | Claims to cross-check only |

**Minimum before conclusions:** 3 non-vendor (tier A/B) sources. Reports require 5+ sources with at least 3 tier A/B.

## Directory Layout

```
config/          # Taxonomy and source watchlists
topics/          # registry.yaml (master list) + inbox.yaml (discovered)
templates/       # Intake, brief, claims-evidence, report templates
research/        # Working notes per topic
reports/         # Published reports + INDEX.md
scripts/         # discover.py, triage.py, validate_report.py
.cursor/rules/   # AI research standards
```

## Scheduling

A GitHub Actions workflow ([`.github/workflows/discover.yml`](.github/workflows/discover.yml)) runs discovery weekly (Mondays 06:00 UTC) or on manual trigger.

**What it does:** runs `discover.py`, then pushes any `topics/inbox.yaml` changes to branch `discovery/weekly-inbox`. Open a PR from that branch into `main` and merge when ready.

**Repo settings required** (one-time):

1. GitHub → **Settings** → **Actions** → **General**
2. Under **Workflow permissions**, choose **Read and write permissions**
3. Save

You do **not** need “Allow GitHub Actions to create and approve pull requests” unless you switch back to an auto-PR action. The workflow pushes a branch only; you merge via a normal PR in the UI.

**Local alternative:** `python scripts/discover.py` before each research session.
