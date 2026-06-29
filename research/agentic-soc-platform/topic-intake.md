# Topic Intake: Agentic SOC Platform (ASP)

**Slug:** `agentic-soc-platform`  
**Date:** 2026-06-29  
**Type:** technology  
**Categories:** data_ai, automation_orchestration, detection_response  
**Status:** new

## Problem Statement

SOC teams face alert fatigue, manual investigation bottlenecks, and fragmented tooling between SIEM, SOAR/SIRP, and emerging LLM-assisted workflows. ASP targets consolidation of alert ingestion, case management, playbook automation, and agent-driven investigation in a self-hosted open-source stack.

## Target Buyer / User

- Primary persona: SOC analysts, detection engineers, security architects at mid-size organizations
- Organization size / maturity: Teams already running Splunk or ELK who want AI-assisted triage without SaaS lock-in

## Why Now?

Agentic AI and MCP integration are reshaping security tooling. OCSF adoption is growing among SIEM vendors. Open-source alternatives to commercial SOAR are scarce, especially with native LLM/MCP support.

## Initial Hypothesis

ASP may be differentiated by combining: (1) open-source MIT-licensed full-stack SIRP + SOAR, (2) MCP-native agent integration (Claude Code, etc.), (3) unified multi-SIEM abstraction for LLM queries, and (4) OCSF-aligned data model—originating from the same author/ecosystem as the VIPER red-team platform.

## Discovery Context

- **Discovered via:** GitHub search (autonomous soc security)
- **Initial URL:** https://github.com/FunnyWolf/agentic-soc-platform
- **Snippet:** Open-source agent-centric automated security operations platform (AI SOC); ~925 stars; Python; MIT license

## Incumbent Comparison Scope

- [x] detection_response
- [x] automation_orchestration
- [ ] cloud_identity
- [x] data_ai
- [ ] vuln_exposure

**Baseline incumbents:** Splunk SOAR, Palo Alto XSOAR, Torq, Tines, Splunk ES, Elastic Security

## Research Questions

1. What is the actual architecture (alert flow, modules, SIRP) per primary sources?
2. How does MCP/agent integration differ from commercial SOAR + copilot add-ons?
3. What is the project's maturity, governance, and author lineage (VIPER/404Starlink)?

## Next Steps

- [x] Gather tier A/B primary sources (minimum 3)
- [x] Complete claims-evidence table
- [x] Draft differentiation matrix
- [x] Write report
