# CloudQuery

**Report date:** 2026-06-29  
**Slug:** `cloudquery-cloudquery`  
**Type:** technology  
**Categories:** cloud_identity  
**Status:** published

---

## Executive Summary

**CloudQuery** is an open-core **ELT pipeline** (Go, **MPL-2.0**) that syncs cloud and SaaS configuration metadata into customer-controlled SQL databases for analysis with standard SQL and BI tools ([GitHub](https://github.com/cloudquery/cloudquery)). With **~6,400+ GitHub stars** since 2020 and **$34.5M total funding** ($15M Series A 2022, $16M 2025 per [FinSMEs](https://www.finsmes.com/2025/06/cloudquery-raises-16m-in-funding.html)), it enables DIY **asset inventory, CSPM policies, and compliance reporting** across **70+ sources**. Differentiation vs **Wiz** is **data ownership and SQL flexibility** versus managed detections and risk graphs; teams must build policies and remediation themselves ([TechCrunch](https://techcrunch.com/2022/06/22/as-cloudquerys-open-source-infrastructure-visibility-tool-gains-traction-it-lands-15m-series-a/)).

## Landscape Context

### The problem

Security teams need normalized multi-cloud asset inventory and posture data in warehouses they control—not only vendor SaaS dashboards.

### Incumbents

Wiz, Prisma Cloud, Microsoft Defender for Cloud, Steampipe (alternative SQL approach).

## What It Is

Per [GitHub README](https://github.com/cloudquery/cloudquery/blob/main/README.md):

- Extract-load-transform from AWS, Azure, GCP, Okta, and 70+ integrations
- Data lands in Postgres, Snowflake, BigQuery, etc.
- Security use cases: CSPM via SQL, asset inventory, cross-source joins (e.g., Okta + AWS)
- **Open-core shift (Oct 2025):** some integrations moved closed-source; prior OSS versions archived under MPL 2.0

## Evidence-Backed Deep Dive

### Architecture

Agentless API reads → normalized tables → customer SQL. Read-only cloud permissions; data stays on customer infrastructure ([GitHub README](https://github.com/cloudquery/cloudquery/blob/main/README.md)).

### Development / maturity signals

| Signal | Detail |
|--------|--------|
| Stars | ~6,446 (June 2026) |
| Funding | $34.5M total ([FinSMEs](https://www.finsmes.com/2025/06/cloudquery-raises-16m-in-funding.html)) |
| License | MPL-2.0 core |
| Alternative | Steampipe real-time Postgres FDW ([HN discussion](https://news.ycombinator.com/item?id=32481270)) |

## Key Findings

- CloudQuery syncs **70+ cloud/SaaS sources** into customer SQL DBs for inventory and DIY CSPM ([GitHub README](https://github.com/cloudquery/cloudquery/blob/main/README.md)).
- **$16M round (June 2025)** brought total raised to **$34.5M** ([FinSMEs](https://www.finsmes.com/2025/06/cloudquery-raises-16m-in-funding.html)).
- Practitioners note CSPM requires building **policies, dashboards, and remediation**—not turnkey like Wiz ([HN](https://news.ycombinator.com/item?id=25414416)).
- **MPL-2.0** file-level copyleft; Oct 2025 open-core migration affects some plugins ([GitHub README](https://github.com/cloudquery/cloudquery/blob/main/README.md)).
- ELT batch model trades **freshness** for warehouse-scale analytics vs real-time tools ([HN](https://news.ycombinator.com/item?id=32481270)).

## Differentiation Analysis

| Dimension | CloudQuery | Wiz | Native cloud APIs |
|-----------|------------|-----|-------------------|
| Model | ELT + SQL | Managed CNAPP | Per-cloud inventory |
| Data ownership | Customer DB | Vendor SaaS | Vendor |
| Posture detection | DIY SQL rules | Built-in | Limited cross-cloud |
| Openness | MPL open-core | Proprietary | Vendor-locked |

## Risks and Open Questions

- Build/operate burden for full CSPM
- Open-core plugin erosion
- Enterprise customer claims company-sourced only

## Sources

| # | Source | Tier | URL |
|---|--------|------|-----|
| 1 | CloudQuery GitHub | B | https://github.com/cloudquery/cloudquery |
| 2 | CloudQuery README | B | https://github.com/cloudquery/cloudquery/blob/main/README.md |
| 3 | TechCrunch — Series A | A | https://techcrunch.com/2022/06/22/as-cloudquerys-open-source-infrastructure-visibility-tool-gains-traction-it-lands-15m-series-a/ |
| 4 | FinSMEs — 2025 funding | A | https://www.finsmes.com/2025/06/cloudquery-raises-16m-in-funding.html |
| 5 | Hacker News — practitioner discussion | A | https://news.ycombinator.com/item?id=25414416 |
