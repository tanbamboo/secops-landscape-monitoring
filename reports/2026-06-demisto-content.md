# Cortex XSOAR Content (demisto/content)

**Report date:** 2026-06-29  
**Slug:** `demisto-content`  
**Type:** technology  
**Categories:** automation_orchestration  
**Status:** published

---

## Executive Summary

**demisto/content** is Palo Alto Networks' official **MIT-licensed content repository** for **Cortex XSOAR**—community-maintained packs of playbooks, automation scripts, integrations, and report templates that run inside a licensed XSOAR instance ([README](https://github.com/demisto/content/blob/master/README.md)). With **~1,286 stars** and daily commits through June 2026, it is **not a SOAR platform** but the **open content layer** for XSOAR. Differentiation vs **Splunk SOAR** is ecosystem lock-in: content requires XSOAR runtime; value is breadth of pre-built integrations and contribution model ([xsoar.pan.dev](https://xsoar.pan.dev/)).

## Landscape Context

### The problem

SOAR deployments need hundreds of vendor integrations and playbooks; maintaining them in-house is expensive.

### Incumbents

Splunk SOAR, Cortex XSOAR (platform), Shuffle (open SOAR), Tines.

## What It Is

Per [demisto/content README](https://github.com/demisto/content/blob/master/README.md):

- **Playbooks** — visual workflows; export via **COPS** open format ([COPS spec](https://github.com/demisto/COPS))
- **Scripts** — Python/JS automation in Docker containers ([demisto Docker Hub](https://hub.docker.com/u/demisto/))
- **Integrations** — vendor API connectors
- **Packs/** directory — versioned content packs validated via CI

## Evidence-Backed Deep Dive

### Architecture

Content-only repo; execution requires Cortex XSOAR platform (commercial). MIT license enables fork/contribute; platform remains proprietary.

### Development / maturity signals

| Signal | Detail |
|--------|--------|
| Stars | 1,286 |
| Forks | ~1,948 |
| License | MIT |
| Last push | 2026-06-29 |

## Key Findings

- Repository is **XSOAR content**, not standalone SOAR ([README](https://github.com/demisto/content/blob/master/README.md)).
- **MIT license** allows open contribution; platform runtime is paid XSOAR ([LICENSE](https://github.com/demisto/content/blob/master/LICENSE)).
- **COPS format** provides open playbook interchange specification ([COPS](https://github.com/demisto/COPS)).
- Developer docs and pack validation at [xsoar.pan.dev](https://xsoar.pan.dev/) ([Content Contribution Guide](https://xsoar.pan.dev/docs/contributing/contributing)).
- No cross-platform portability to Splunk SOAR playbooks ([README](https://github.com/demisto/content/blob/master/README.md)).

## Differentiation Analysis

| Dimension | demisto/content | Splunk SOAR | Shuffle |
|-----------|-----------------|-------------|---------|
| What it is | Content packs | Full platform | Full OSS platform |
| License | MIT content | Proprietary | AGPL core |
| Runtime | XSOAR required | Splunk SOAR | Self-hosted |

## Risks and Open Questions

- XSOAR platform cost required to use content
- Pack quality varies; community-maintained
- Palo Alto roadmap dependency

## Sources

| # | Source | Tier | URL |
|---|--------|------|-----|
| 1 | demisto/content GitHub | B | https://github.com/demisto/content |
| 2 | demisto/content README | B | https://github.com/demisto/content/blob/master/README.md |
| 3 | MIT LICENSE | B | https://github.com/demisto/content/blob/master/LICENSE |
| 4 | COPS playbook format | B | https://github.com/demisto/COPS |
| 5 | XSOAR developer portal | B | https://xsoar.pan.dev/ |
