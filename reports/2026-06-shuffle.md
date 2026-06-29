# Shuffle (Open-Source SOAR)

**Report date:** 2026-06-29  
**Slug:** `shuffle-shuffle`  
**Type:** technology  
**Categories:** automation_orchestration  
**Status:** published

---

## Executive Summary

**Shuffle** is an **open-source security automation / SOAR platform** with **~2,332 GitHub stars** (AGPL-3.0 core, MIT workflows/apps) offering visual workflows, **OpenAPI-first app integrations**, and hybrid **Shuffle Cloud + on-prem Orborus workers** ([README](https://github.com/Shuffle/Shuffle/blob/main/README.md)). Active development through June 2026 with commercial SaaS at [shuffler.io](https://shuffler.io). Differentiation vs **Cortex XSOAR / Splunk SOAR** is **openness and OpenAPI extensibility**; tradeoffs include **481 open issues**, AGPL copyleft, and default deployment not production-scalable without tuning ([install guide](https://github.com/Shuffle/Shuffle/blob/main/.github/install-guide.md)).

## Landscape Context

### The problem

SOAR platforms are expensive and closed; teams want self-hosted orchestration with broad security tool integrations.

### Incumbents

Cortex XSOAR, Splunk SOAR, Tines, Palo Alto Cortex SOAR, demisto/content ecosystem.

## What It Is

Per [Shuffle README](https://github.com/Shuffle/Shuffle/blob/main/README.md):

- Go backend, React frontend, **Orborus** worker distribution
- OpenAPI app creator; premade integrations (Wazuh, Elastic, etc.)
- MSSP multi-org support
- Hybrid: cloud UI optional; workers on-prem for execution isolation

## Evidence-Backed Deep Dive

### Architecture

Hybrid cloud frontend with on-prem workers; OpenSearch default backend; Docker/K8s deploy paths.

### Development / maturity signals

| Signal | Detail |
|--------|--------|
| Stars | 2,332 |
| Created | May 2020 |
| Open issues | 481 |
| Releases | 30 tagged |

## Key Findings

- **OpenAPI-first** app model differentiates from proprietary SOAR connectors ([README](https://github.com/Shuffle/Shuffle/blob/main/README.md)).
- **AGPL-3.0 core** with MIT workflows affects MSSP/hosted deployment legal review ([README](https://github.com/Shuffle/Shuffle/blob/main/README.md)).
- **Hybrid Orborus workers** enable on-prem execution with optional cloud UI ([README](https://github.com/Shuffle/Shuffle/blob/main/README.md)).
- Default install **not production-scalable** without extra config ([install guide](https://github.com/Shuffle/Shuffle/blob/main/.github/install-guide.md)).
- **481 open issues** signal support/maintenance burden vs commercial SOAR ([GitHub](https://github.com/Shuffle/Shuffle)).

## Differentiation Analysis

| Dimension | Shuffle | Cortex XSOAR | Tines |
|-----------|---------|----------------|-------|
| License | AGPL OSS | Proprietary | SaaS |
| Extensibility | OpenAPI apps | Content packs | Prebuilt |
| Case management | Present | Mature | Strong |
| Enterprise SLA | Commercial tier | Vendor | Vendor |

## Risks and Open Questions

- AGPL compliance for SaaS operators
- Production HA complexity
- shuffler.io dependency for some hybrid features

## Sources

| # | Source | Tier | URL |
|---|--------|------|-----|
| 1 | Shuffle GitHub | B | https://github.com/Shuffle/Shuffle |
| 2 | Shuffle README | B | https://github.com/Shuffle/Shuffle/blob/main/README.md |
| 3 | Install guide | B | https://github.com/Shuffle/Shuffle/blob/main/.github/install-guide.md |
| 4 | Shuffle releases | B | https://github.com/Shuffle/Shuffle/releases |
| 5 | Shuffle docs repo | B | https://github.com/Shuffle/Shuffle-docs |
