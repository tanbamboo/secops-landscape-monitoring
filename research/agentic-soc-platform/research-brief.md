# Research Brief: Agentic SOC Platform (ASP)

**Slug:** `funnywolf-agentic-soc-platform`  
**Date:** 2026-06-29

## Scope

Open-source technology (not a commercial startup). Research limited to publicly verifiable sources: GitHub, release notes, 404Starlink, and landscape context for OCSF/SOAR. Marketing site used only for claim identification.

## Landscape Context

ASP sits at the intersection of SOAR, SIRP, and agentic AI—domains where incumbents are adding AI copilots but rarely open-sourcing full stacks with MCP-native control planes.

## Subject Overview

MIT-licensed Python platform by FunnyWolf (VIPER author). Combines webhook/Redis alert ingestion, module engines, built-in SIRP, playbooks, Splunk/ELK plugins, OCSF schema (v0.2.0+), and MCP/Claude Code integration (v0.3.0).

## Differentiation Preview

| Dimension | ASP | Typical incumbent SOAR |
|-----------|-----|------------------------|
| Agent model | MCP harness agents as operators | UI copilot / chat sidebar |
| Deployment | Self-hosted MIT | SaaS or licensed |
| SIEM role | Overlay on Splunk/ELK | Often bundled or deeply integrated |
| Schema | OCSF at case layer | Vendor-specific or OCSF at ingest only |

## Open Questions

- Production SOC adoption stories
- LLM investigation accuracy
- Roadmap for additional SIEM platforms (Sentinel, etc.)

See full report: [reports/2026-06-agentic-soc-platform.md](../../reports/2026-06-agentic-soc-platform.md)
