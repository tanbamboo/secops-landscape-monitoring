# Hayabusa (Yamato Security)

**Report date:** 2026-06-29  
**Slug:** `yamato-security-hayabusa`  
**Type:** technology  
**Categories:** detection_response  
**Status:** published

---

## Executive Summary

**Hayabusa** (隼) is an open-source **Windows EVTX threat-hunting and forensics timeline generator** written in **Rust** by [Yamato Security](https://yamatosecurity.connpass.com/). It ingests Windows event logs and outputs consolidated **CSV/JSON/JSONL timelines** enriched with **Sigma-based detections**, including Sigma v2 correlation rules per project claims ([README](https://github.com/Yamato-Security/hayabusa/blob/main/README.md)). With **~3,200 GitHub stars**, active development through June 2026, and presentations at Black Hat Arsenal and SANS DFIR Summit, Hayabusa is a leading practitioner tool for **DFIR and detection engineering on Windows**—complementary to SIEMs rather than replacing them. Licensed under **AGPL-3.0** (tool) and **DRL 1.1** (rules). Differentiation vs commercial EDR analytics is **speed, Sigma fidelity, and offline/air-gapped forensics** at zero license cost.

## Landscape Context

### The problem

Windows-centric investigations require fast triage across EVTX logs from one host or thousands of endpoints—often offline after Velociraptor collection—without waiting for centralized SIEM indexing.

### Incumbents

| Tool | Role | Hayabusa contrast |
|------|------|-------------------|
| Splunk / Sentinel | Central SIEM | Hayabusa offline, portable, Sigma-native |
| Chainsaw (FalconForce) | EVTX + Sigma | Hayabusa emphasizes speed, correlation rules, i18n docs |
| Eric Zimmerman tools | DFIR parsers | Hayabusa integrated detection + timeline |
| Wazuh / OSSEC | Agent SIEM | Hayabusa is analyst workstation tool |

## What It Is

From [README](https://github.com/Yamato-Security/hayabusa/blob/main/README.md) and [documentation](https://yamato-security.github.io/hayabusa/):

- **Input:** Windows event logs (EVTX), live or collected
- **Output:** Single timeline (CSV/JSON/JSONL) with detection annotations
- **Detection:** Sigma rules (project claims full Sigma support incl. v2 correlation)
- **Scale:** Multi-threaded; single host to enterprise via [Velociraptor](https://docs.velociraptor.app/) integration
- **Export targets:** Timeline Explorer, Elastic Stack, Timesketch, jq pipelines
- **Maintenance:** Actively developed; docs in 15 languages

**License:** GNU AGPLv3 ([GitHub](https://github.com/Yamato-Security/hayabusa)); detection rules under Sigma DRL 1.1.

## Evidence-Backed Deep Dive

### Technical positioning

Hayabusa sits in the **DFIR / threat hunting** layer:

1. Collect EVTX (live, Velociraptor, forensic image)
2. Run Hayabusa with rule set
3. Produce annotated timeline for analyst review
4. Import to SIEM or spreadsheet tools for collaboration

It does **not** provide continuous monitoring, SOAR, or cloud CNAPP—unlike Wazuh or ThreatMapper.

### Sigma ecosystem role

Sigma is the lingua franca for portable detection logic. Hayabusa's claim of **full Sigma support including correlation rules** positions it for detection engineers validating rules against raw Windows telemetry before SIEM deployment ([README](https://github.com/Yamato-Security/hayabusa/blob/main/README.md)). Independent verification against every Sigma feature should use the project's [rules documentation](https://yamato-security.github.io/hayabusa/rules/).

### Community & maturity

| Signal | Evidence |
|--------|----------|
| Created | 2020-09-18 |
| Stars | 3,229 |
| Language | Rust |
| Conferences | Black Hat Arsenal USA 2025/2026, SANS DFIR 2023, BSides Tokyo, etc. ([README badges](https://github.com/Yamato-Security/hayabusa)) |
| Org | Yamato Security community (Japan) |

## Key Findings

- Hayabusa is a **Rust-based Windows EVTX timeline + Sigma detection** tool for DFIR and hunting—not a SIEM ([README](https://github.com/Yamato-Security/hayabusa/blob/main/README.md)).
- **Multi-threaded** design targets speed on large log volumes per project documentation ([docs](https://yamato-security.github.io/hayabusa/)).
- **Velociraptor** integration enables enterprise-scale collection with local/central analysis ([README](https://github.com/Yamato-Security/hayabusa/blob/main/README.md)).
- **AGPL-3.0** license affects embedding in commercial products; rules use separate DRL ([README](https://github.com/Yamato-Security/hayabusa/blob/main/README.md)).
- **~3.2k stars** and sustained 2026 commits show mature community adoption ([GitHub](https://github.com/Yamato-Security/hayabusa)).

## Differentiation Analysis

| Dimension | Hayabusa | Splunk ES | Chainsaw |
|-----------|----------|-----------|----------|
| Deployment | CLI workstation | Enterprise platform | CLI |
| Cost | Free (AGPL) | Licensed | Free |
| Windows EVTX focus | Primary | General SIEM | Strong |
| Timeline output | Core feature | Search-based | CSV JSON |
| Live monitoring | No | Yes | No |
| Sigma correlation | Claimed full | Via pipelines | Sigma support |

**Novel:** High-performance Rust timeline with broad Sigma correlation on Windows. **Incremental:** EVTX+Sigma is a known pattern; Hayabusa optimizes execution and UX for DFIR practitioners.

## Risks and Open Questions

- **Windows-only**—no Linux/cloud log support in core tool
- AGPL may block some enterprise redistribution models
- "Only OSS tool with full Sigma support" is a strong marketing claim—competitive tools exist
- Does not replace centralized SIEM for 24/7 SOC—point-in-time hunting tool
- Rule quality/maintenance burden shifts to operator like any Sigma workflow

## Sources

| # | Source | Tier | URL |
|---|--------|------|-----|
| 1 | Hayabusa GitHub | B | https://github.com/Yamato-Security/hayabusa |
| 2 | Hayabusa README | B | https://github.com/Yamato-Security/hayabusa/blob/main/README.md |
| 3 | Hayabusa documentation site | B | https://yamato-security.github.io/hayabusa/ |
| 4 | Sigma project (context) | B | https://github.com/SigmaHQ/sigma |
| 5 | Velociraptor docs (enterprise hunting) | B | https://docs.velociraptor.app/ |
| 6 | GitHub API metadata | B | https://api.github.com/repos/Yamato-Security/hayabusa |
