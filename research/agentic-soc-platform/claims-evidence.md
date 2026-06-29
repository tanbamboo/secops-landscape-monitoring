# Claims vs Evidence: Agentic SOC Platform (ASP)

**Slug:** `agentic-soc-platform`  
**Date:** 2026-06-29

## Claims Table

| # | Claim | Who said it | Tier | Evidence found | Confidence | Notes |
|---|-------|-------------|------|----------------|------------|-------|
| 1 | ASP is MIT-licensed open source | GitHub repo metadata | B | License field = MIT on GitHub API/README | verified | |
| 2 | Supports Splunk and ELK with unified log search API | README, v0.3.0 release notes | B | Release notes explicitly state SIEM plugin for Splunk/ELK; README describes YAML-based index config | verified | |
| 3 | Built-in SIRP for case/alert/artifact management | README, releases | B | v0.1.0 release describes complete SIRP; README workflow diagrams | verified | |
| 4 | OCSF-based data model since v0.2.0 | v0.2.0 release notes | B | Release tag documents SIRP restructure on OCSF | verified | |
| 5 | MCP plugin exposes core ASP capabilities to external agents | v0.3.0 release, asp-marketplace repo | B | Release notes + marketplace README list agents/skills | verified | |
| 6 | "99% noise reduction" from alert aggregation | asp.viperrtp.com homepage | C | Marketing site; no independent benchmark cited | unverified | Treat as aspirational |
| 7 | "Seconds not hours" for AI investigation | README, website | C | Architecture supports LLM reports; no published latency benchmarks | partial | Capability exists; performance unverified |
| 8 | Part of Knownsec 404Starlink program | README, 404StarLink repo | B | README badge; VIPER listed in 404StarLink-Project history | verified | |
| 9 | Same author as VIPER red-team platform | GitHub (FunnyWolf), shared viperrtp.com domain | B | Both repos under FunnyWolf; ASP homepage at asp.viperrtp.com | verified | Important adoption context |
| 10 | ~925 GitHub stars, active development | GitHub API at discovery | B | Created Sep 2025; last push Jun 2026; 4 releases | verified | Star count fluctuates |

## Verified Facts (summary)

1. ASP is a Python/TypeScript MIT-licensed project with built-in SIRP, module-based alert processing, playbook automation, Splunk/ELK plugins, OCSF-aligned schema (v0.2.0+), and MCP/Claude Code integration (v0.3.0).
2. Author FunnyWolf also maintains VIPER (open-source red-team platform); ASP is endorsed via 404Starlink (Knownsec 404 Team open-source program).

## Unverified / Marketing Claims (do not use as facts)

1. Quantified noise reduction (99%) and investigation time ("seconds not hours")—no third-party benchmarks found.

## Contradicted Claims

None identified from available sources.

## Evidence Gaps

- No independent SOC deployment case studies or production references found
- No published performance/security audit of LLM investigation quality
- Enterprise support model unclear (community/open-source only)
- Sentinel/Microsoft 365 Defender and other SIEMs not yet in supported list per release notes
