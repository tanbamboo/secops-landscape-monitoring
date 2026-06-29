# Agentic SOC Platform (ASP)

**Report date:** 2026-06-29  
**Slug:** `funnywolf-agentic-soc-platform`  
**Type:** technology  
**Categories:** data_ai, automation_orchestration, detection_response  
**Status:** published

---

## Executive Summary

The Agentic SOC Platform (ASP) is an open-source, MIT-licensed security operations stack created by FunnyWolf—the same developer behind the VIPER red-team platform. ASP combines a built-in Security Incident Response Platform (SIRP), Python-based alert modules, playbook automation, and LLM/agent integrations (including MCP for Claude Code) into a self-hosted platform oriented around Splunk and ELK. Its main differentiation from commercial SOAR/SIEM suites is architectural: it treats agentic AI and MCP as first-class control planes rather than bolt-on copilots, uses OCSF-aligned schemas for interoperability, and ships as deployable open source rather than SaaS. The project is young (created September 2025, ~925 GitHub stars) with no verified enterprise production references; marketing claims about noise reduction and investigation speed lack independent benchmarks.

## Landscape Context

### The problem

SOC teams routinely juggle separate tools for alert ingestion (SIEM), case management (SIRP/ticketing), orchestration (SOAR playbooks), and increasingly LLM-assisted investigation. Commercial platforms (Splunk SOAR, Palo Alto XSOAR, Torq, Tines) address orchestration but are proprietary, often SaaS-centric, and only recently adding AI copilots. Open-source SOAR alternatives exist (e.g., TheHive, Shuffle) but few natively integrate MCP, multi-SIEM LLM query abstractions, and OCSF-aligned case data in one stack.

### Incumbents and current approaches

| Incumbent | Approach | Known limitations |
|-----------|----------|-------------------|
| Splunk SOAR / XSOAR | Commercial playbook automation atop SIEM ecosystem | Proprietary, licensing cost, AI features added incrementally |
| Torq / Tines | Cloud-native workflow automation | SaaS model; limited on-prem agent-native control |
| Elastic Security | Integrated detection + cases in Elastic Stack | Less emphasis on external harness-agent (MCP) orchestration |
| Shuffle | Open-source SOAR | Mature workflow focus; less agentic/MCP-native design |

### Market gaps this addresses (if any)

Teams wanting on-prem, Python-extensible SOAR/SIRP with native LLM agent hooks and unified Splunk/ELK access—without replacing their existing SIEM—have limited open-source options. ASP targets this gap explicitly.

## What It Is

ASP is an open-source security operations platform ([GitHub repository](https://github.com/FunnyWolf/agentic-soc-platform)) written primarily in Python (93%) with a TypeScript/JavaScript frontend. It is MIT-licensed, supports local/private deployment, and includes:

- A **built-in SIRP** for cases, alerts, and artifacts (complete as of v0.1.0 per [release notes](https://github.com/FunnyWolf/agentic-soc-platform/releases/tag/v0.1.0))
- **Module engines** that consume alerts from webhooks/Redis streams, perform analysis (often via AI agents), and write standardized records to the SIRP
- **Playbooks** for orchestrating investigation, enrichment, and remediation actions
- **SIEM plugins** for Splunk and ELK with a unified log-search API ([v0.3.0 release](https://github.com/FunnyWolf/agentic-soc-platform/releases/tag/v0.3.0))
- **MCP and Claude Code plugins** exposing case operations, log search, and module authoring to external harness agents ([asp-marketplace](https://github.com/FunnyWolf/asp-marketplace))

The project joined the [Knownsec 404Starlink](https://github.com/knownsec/404StarLink) open-source security program and shares infrastructure branding with VIPER (`asp.viperrtp.com`).

## Evidence-Backed Deep Dive

### Architecture

Documented alert flow ([README](https://github.com/FunnyWolf/agentic-soc-platform/blob/master/README.md)):

1. SIEM/EDR sources send alerts (webhook forwarder)
2. Alerts land in Redis Streams (per alert type)
3. Python **modules** consume streams, extract IOCs, correlate, run LLM analysis
4. Standardized outputs create/update cases, alerts, artifacts in the **SIRP**
5. Analysts or agents trigger **playbooks** for further enrichment or response

This is a modular pipeline pattern—SIEM remains upstream; ASP acts as orchestration + case layer + agent host.

### Data flow and inputs

From v0.2.0 onward, SIRP entities were restructured to follow the [OCSF standard](https://github.com/FunnyWolf/agentic-soc-platform/releases/tag/v0.2.0), aligning alerts, cases, and artifacts with the industry schema used by Splunk, Datadog, and others for telemetry normalization. SIEM log metadata is stored in YAML configuration files with a unified external search interface so LLM callers need not understand per-SIEM query dialects ([v0.3.0 release notes](https://github.com/FunnyWolf/agentic-soc-platform/releases/tag/v0.3.0)).

### Technical differentiators (verified)

- **MCP-first agent integration:** Official MCP plugin and Claude Code marketplace with case investigators, threat-hunting agents, and granular skills ([asp-marketplace README](https://github.com/FunnyWolf/asp-marketplace))
- **Multi-SIEM abstraction:** Splunk + ELK first; unified API for log retrieval designed for LLM/agent consumption
- **OCSF-native SIRP:** Schema alignment at the case layer, not only ingestion
- **Python extensibility:** Modules and playbooks as Python scripts—low barrier for customization
- **Self-hosted MIT stack:** Contrasts with SaaS SOAR; data stays on-prem per project documentation

### Development / maturity signals

| Signal | Evidence |
|--------|----------|
| Created | 2025-09-07 ([GitHub](https://github.com/FunnyWolf/agentic-soc-platform)) |
| Latest release | v0.3.0 (2026-04-08) |
| Community | ~925 stars, 153 forks at discovery (2026-06-29) |
| Contributors | Primarily single author (FunnyWolf) |
| Lineage | Same author as [VIPER](https://github.com/FunnyWolf/Viper) red-team platform (5k+ stars); 404Starlink member |

## Key Findings

- ASP is a self-hosted, MIT-licensed open-source platform combining SIRP, SOAR-style playbooks, and agentic AI—not a SIEM replacement but an orchestration layer atop Splunk/ELK ([GitHub README](https://github.com/FunnyWolf/agentic-soc-platform/blob/master/README.md)).
- OCSF alignment for SIRP data was introduced in v0.2.0, placing ASP in the same interoperability camp as major SIEM vendors adopting OCSF ([v0.2.0 release](https://github.com/FunnyWolf/agentic-soc-platform/releases/tag/v0.2.0)).
- MCP integration (v0.3.0) lets external harness agents (e.g., Claude Code) operate cases, search logs, and author modules—an architectural choice distinct from typical SOAR "AI assistant" panels ([v0.3.0 release](https://github.com/FunnyWolf/agentic-soc-platform/releases/tag/v0.3.0)).
- The project shares authorship and ecosystem with VIPER, a widely used open-source red-team platform endorsed by Knownsec's 404Starlink ([404StarLink-Project](https://github.com/knownsec/404StarLink-Project)).
- SIEM support is currently limited to Splunk and ELK per release documentation; other platforms are not yet verified ([v0.3.0 release notes](https://github.com/FunnyWolf/agentic-soc-platform/releases/tag/v0.3.0)).

## Differentiation Analysis

### Novel vs incremental

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| MCP-native agent control plane | Novel for open-source SOAR | asp-marketplace, v0.3.0 MCP plugin |
| OCSF at SIRP/case layer | Incremental but well-timed | v0.2.0 release; OCSF widely adopted by vendors |
| Built-in SIRP + modules + playbooks | Incremental (similar to SOAR pattern) | Architecture mirrors commercial SOAR |
| Multi-SIEM LLM query abstraction | Partially novel | Unified YAML + API; only Splunk/ELK verified |
| Open-source MIT full stack | Differentiated vs Torq/Tines/SOAR SaaS | License + deployment model |

### Comparison vs incumbents

| Dimension | ASP | Splunk SOAR / XSOAR | Torq / Tines | Notes |
|-----------|-----|---------------------|--------------|-------|
| Architecture | Module + Redis stream + SIRP; agent/MCP layer | Proprietary playbook engine integrated with Splunk/Cortex | Cloud workflow automation | ASP is orchestration overlay, not SIEM |
| Detection/response | Consumes SIEM alerts; LLM investigation modules | Native SIEM + SOAR in vendor stack | Integrates via APIs/connectors | ASP depends on upstream SIEM |
| Integrations | Splunk, ELK, MCP, Claude Code; TI enrichment | Broad commercial connector ecosystem | Large SaaS integration library | ASP integration breadth unproven |
| Openness | MIT, on-prem, Python modules | Proprietary / licensed | SaaS, limited on-prem | ASP wins on openness for self-hosters |
| Pricing | Free (open source) | Enterprise licensing | Per-workflow SaaS pricing | ASP has no documented commercial support tier |

### What's genuinely new

Treating **harness agents** (via MCP) as operators that can search SIEM logs, manage cases, and write Python modules/playbooks is a concrete architectural bet not commonly seen in open-source SOAR. Storing SIEM index metadata in YAML for LLM-friendly retrieval (vs. wiki-based runbooks) is a pragmatic design choice documented in release notes.

### What appears repackaged

Core alert → case → playbook flow mirrors established SOAR patterns. OCSF adoption follows industry direction rather than inventing a new schema. LLM-generated investigation reports are increasingly common across security vendors.

## Risks and Open Questions

### Limitations

- Single-primary-contributor project; bus factor and long-term maintenance risk
- SIEM support limited to Splunk and ELK in verified releases
- No independent production deployment references found
- Shared author lineage with offensive-security tooling (VIPER) may affect enterprise procurement perception

### Unverified claims

- Website claims of "99% noise reduction" and sub-hour-to-seconds investigation times lack cited benchmarks ([asp.viperrtp.com](https://asp.viperrtp.com/))

### Adoption barriers

- Requires operational capacity to run and secure another platform (Redis, webhooks, LLM API keys)
- LLM investigation quality and hallucination risk not evaluated in independent studies
- Enterprise support, SLAs, and compliance certifications not documented

## Sources

| # | Source | Tier | URL |
|---|--------|------|-----|
| 1 | ASP GitHub repository | B | https://github.com/FunnyWolf/agentic-soc-platform |
| 2 | ASP README (architecture, features) | B | https://github.com/FunnyWolf/agentic-soc-platform/blob/master/README.md |
| 3 | ASP v0.3.0 release (SIEM plugin, MCP) | B | https://github.com/FunnyWolf/agentic-soc-platform/releases/tag/v0.3.0 |
| 4 | ASP v0.2.0 release (OCSF) | B | https://github.com/FunnyWolf/agentic-soc-platform/releases/tag/v0.2.0 |
| 5 | ASP Claude Code marketplace | B | https://github.com/FunnyWolf/asp-marketplace |
| 6 | Knownsec 404Starlink program | B | https://github.com/knownsec/404StarLink-Project |
| 7 | VIPER red-team platform (author lineage) | B | https://github.com/FunnyWolf/Viper |
| 8 | Splunk OCSF blog (landscape context) | A | https://www.splunk.com/en_us/blog/security/enhancing-soc-efficiency-with-ocsf-splunk-enterprise-security.html |
| 9 | ASP official website (marketing claims) | C | https://asp.viperrtp.com/ |
