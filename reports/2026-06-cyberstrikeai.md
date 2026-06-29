# CyberStrikeAI

**Report date:** 2026-06-29  
**Slug:** `ed1s0nz-cyberstrikeai`  
**Type:** technology  
**Categories:** data_ai, automation_orchestration  
**Status:** published

---

## Executive Summary

**CyberStrikeAI** is a **Go-based AI-native offensive security platform** (**Apache-2.0**, **~4,809 stars** since Nov 2025) wrapping **100+ pentest tools** behind **MCP/REST APIs**, multi-agent orchestration (CloudWeGo Eino), and a **built-in C2** for authorized engagements ([README](https://github.com/Ed1s0nZ/CyberStrikeAI/blob/main/README.md)). Rapid 2026 growth (v1.6.x releases) positions it at the intersection of **LLM agents and red-team automation**—not defensive SOC/SOAR. Differentiation vs **Cortex XSOAR/Shuffle** is **offensive tool orchestration + MCP + C2 UI**; vs manual pentest it offers AI-driven tool chaining with significant dual-use risk.

## Landscape Context

### The problem

Red teams want LLM-assisted tool selection and workflow automation across fragmented offensive toolchains.

### Incumbents

Manual pentest stacks, Cobalt Strike (commercial C2), PlexTrac, defensive SOAR (opposite mission).

## What It Is

Per [README](https://github.com/Ed1s0nZ/CyberStrikeAI/blob/main/README.md) and [MULTI_AGENT_EINO.md](https://github.com/Ed1s0nZ/CyberStrikeAI/blob/main/docs/MULTI_AGENT_EINO.md):

- MCP HTTP/stdio/SSE; external MCP federation; Burp plugin
- Agents: deep, plan_execute, supervisor modes
- Built-in C2: listeners, beacons, sessions, human-in-the-loop approval
- Skills system (YAML); SQLite persistence; RAG knowledge base
- Wraps nmap, nuclei, metasploit, prowler, trivy, etc.

## Evidence-Backed Deep Dive

### Development / maturity signals

| Signal | Detail |
|--------|--------|
| Stars | 4,809 |
| Created | Nov 2025 |
| Releases | v1.6.47 (Jun 2026) |
| Contributors | 8 |

## Key Findings

- **MCP-native** offensive orchestration with multi-agent modes ([MULTI_AGENT_EINO.md](https://github.com/Ed1s0nZ/CyberStrikeAI/blob/main/docs/MULTI_AGENT_EINO.md)).
- **Built-in C2** for authorized engagements raises dual-use and policy concerns ([README](https://github.com/Ed1s0nZ/CyberStrikeAI/blob/main/README.md)).
- **100+ tool recipes** repackage existing OSS offensive tools—not novel exploit logic ([README](https://github.com/Ed1s0nZ/CyberStrikeAI/blob/main/README.md)).
- **~4.8k stars in ~7 months** indicates viral adoption; security maturity may lag popularity ([GitHub](https://github.com/Ed1s0nZ/CyberStrikeAI)).
- **LLM non-determinism** risks unsafe tool invocation and credential leakage ([README](https://github.com/Ed1s0nZ/CyberStrikeAI/blob/main/README.md)).

## Differentiation Analysis

| Dimension | CyberStrikeAI | Shuffle SOAR | Manual pentest |
|-----------|---------------|--------------|----------------|
| Mission | Offensive AI | Defensive SOAR | Human-led |
| C2 | Built-in | None | Varied |
| License | Apache-2.0 | AGPL | N/A |

## Risks and Open Questions

- Legal/ethical misuse of C2 features
- Limited tier-A independent security review
- Star velocity vs code review depth

## Sources

| # | Source | Tier | URL |
|---|--------|------|-----|
| 1 | CyberStrikeAI GitHub | B | https://github.com/Ed1s0nZ/CyberStrikeAI |
| 2 | README | B | https://github.com/Ed1s0nZ/CyberStrikeAI/blob/main/README.md |
| 3 | Multi-agent docs | B | https://github.com/Ed1s0nZ/CyberStrikeAI/blob/main/docs/MULTI_AGENT_EINO.md |
| 4 | Releases | B | https://github.com/Ed1s0nZ/CyberStrikeAI/releases |
| 5 | Apache-2.0 LICENSE | B | https://github.com/Ed1s0nZ/CyberStrikeAI/blob/main/LICENSE |
