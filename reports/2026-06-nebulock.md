# Nebulock

**Report date:** 2026-06-29  
**Slug:** `nebulock-raises-25-million-for-ai-native-contextual-security`  
**Type:** startup  
**Categories:** detection_response, data_ai  
**Status:** published

---

## Executive Summary

Nebulock is a Boston-based cybersecurity startup (founded 2023) building an **AI-native, hunt-first contextual security platform** that correlates telemetry across endpoint, identity, cloud, network, and SaaS to surface subtle behavioral threats that alert-driven SIEMs miss. In **June 2026** it raised a **$25M Series A** led by FirstMark, bringing total funding to approximately **$33.5M** after an $8.5M seed in July 2025 ([SiliconANGLE](https://siliconangle.com/2026/06/25/nebulock-raises-25m-expand-hunt-first-security-platform/)). Differentiation centers on **behavioral context graphs**, **agentic threat hunting**, and expanding into **proactive detection engineering**—positioning against reactive SIEM workflows rather than replacing the SIEM outright. Named customers include Cribl, HealthEdge, and Bain Capital per [Business Wire](https://www.businesswire.com/news/home/20260625381441/en/Nebulock-Raises-25-Million-Series-A-to-Bring-a-Hunt-First-Context-to-the-Enterprise); operational metrics (300M+ investigations) are vendor-reported and not independently audited.

## Landscape Context

### The problem

Traditional SIEM and alert-driven tools evaluate events in isolation. Attackers using valid credentials, insider abuse, and workplace AI agents ("shadow AI") produce activity that looks **ordinary**—Nebulock calls these **"green flags"** ([SiliconANGLE](https://siliconangle.com/2026/06/25/nebulock-raises-25m-expand-hunt-first-security-platform/)). The [2026 Verizon DBIR](https://www.businesswire.com/news/home/20260625381441/en/Nebulock-Raises-25-Million-Series-A-to-Bring-a-Hunt-First-Context-to-the-Enterprise) is cited in Nebulock's release regarding AI-assisted attack techniques.

### Incumbents

| Incumbent | Approach | Gap Nebulock targets |
|-----------|----------|----------------------|
| Splunk / Sentinel / Elastic | Alert correlation, detection rules | Sequential behavioral context across silos |
| CrowdStrike / EDR vendors | Endpoint-centric detections | Cross-domain identity + SaaS + cloud narrative |
| Manual threat hunting | Human-led hypothesis testing | Autonomous/agentic hunts at scale |
| CardinalOps / Anvilogic | Detection engineering automation | Hunt-first behavioral graph vs rule lifecycle focus |

## What It Is

Per [Business Wire](https://www.businesswire.com/news/home/20260625381441/en/Nebulock-Raises-25-Million-Series-A-to-Bring-a-Hunt-First-Context-to-the-Enterprise) and [SiliconANGLE](https://siliconangle.com/2026/06/25/nebulock-raises-25m-expand-hunt-first-security-platform/):

- **Vendor-agnostic** platform ingesting telemetry from existing security stacks
- **Autonomous/agentic hunts** across endpoint, identity, cloud, network, SaaS
- **Behavioral system of record** / context graph correlating entities (humans and AI agents)
- **Proactive detection engineering** and behavioral analytics (expanded post-seed)
- Product features announced with Series A: insider-risk entity unification, cross-domain correlated detections with evidence chains, **Command Center** for hunt prioritization and SIEM coverage-gap visibility

**Company:** Founded 2023; CEO **Damien Lewke**; team described as alumni of CrowdStrike, Palo Alto Networks, and Arctic Wolf (press release). Website: [nebulock.io](https://nebulock.io) — **not** nebulock.com (unrelated industrial maintenance company).

## Evidence-Backed Deep Dive

### Architecture (publicly described)

Nebulock's public materials describe a **context layer** above existing tools:

1. Ingest cross-domain telemetry (endpoint, IdP, cloud, network, SaaS)
2. Build/maintain a **behavioral context graph** linking identities, hosts, and AI agents
3. Run **agentic investigations** continuously (vendor cites 300M+ investigations)
4. Output high-confidence findings and detection candidates for analyst review/deployment

No public API documentation, data schema, or deployment architecture was available for independent verification.

### Real-world signals (vendor-reported)

Business Wire lists example customer findings: long-dwell external actor at a retailer, insider exfiltrating 748 source files to USB, credentials in CLI args, malicious browser extension at Fortune 500 F&B company. **OpenClaw** shadow-AI scenario: 50,000+ events across 40% of customer base within a week; vendor claims detections deployed before incidents ([Business Wire](https://www.businesswire.com/news/home/20260625381441/en/Nebulock-Raises-25-Million-Series-A-to-Bring-a-Hunt-First-Context-to-the-Enterprise)).

**Customer quote (tier A via press):** Myke Lyons, CISO of Cribl, states Nebulock shortened time from threat-intel awareness to evidence for remediation ([Business Wire](https://www.businesswire.com/news/home/20260625381441/en/Nebulock-Raises-25-Million-Series-A-to-Bring-a-Hunt-First-Context-to-the-Enterprise)).

### Funding & maturity

| Signal | Detail |
|--------|--------|
| Series A | $25M, June 25, 2026, FirstMark lead |
| Seed | $8.5M, July 2025 |
| Total | ~$33.5M ([SiliconANGLE](https://siliconangle.com/2026/06/25/nebulock-raises-25m-expand-hunt-first-security-platform/)) |
| Investors | FirstMark, Bain Capital Ventures, Decibel, Zetta, Step Function |
| GTM | Fortune 500 financial services, healthcare, tech |

## Key Findings

- Nebulock raised **$25M Series A in June 2026** (FirstMark-led), ~$33.5M total, positioning as hunt-first contextual security—not a rip-and-replace SIEM ([SiliconANGLE](https://siliconangle.com/2026/06/25/nebulock-raises-25m-expand-hunt-first-security-platform/)).
- The platform emphasizes **cross-telemetry behavioral correlation** and **agentic hunting** for threats that appear benign in isolation ([Business Wire](https://www.businesswire.com/news/home/20260625381441/en/Nebulock-Raises-25-Million-Series-A-to-Bring-a-Hunt-First-Context-to-the-Enterprise)).
- Post-seed expansion into **detection engineering** and **Command Center** coverage-gap views moves Nebulock closer to Spectrum Security's detection-lifecycle space while retaining hunt-first DNA ([Business Wire](https://www.businesswire.com/news/home/20260625381441/en/Nebulock-Raises-25-Million-Series-A-to-Bring-a-Hunt-First-Context-to-the-Enterprise)).
- **Shadow AI / agentic insider risk** (OpenClaw case study) is a concrete differentiation narrative versus legacy SIEM alerts ([Business Wire](https://www.businesswire.com/news/home/20260625381441/en/Nebulock-Raises-25-Million-Series-A-to-Bring-a-Hunt-First-Context-to-the-Enterprise)).
- CEO vision statement compares ambition to **"what EDR did for endpoint" applied to SIEM**—collapse complexity, deliver out-of-box value ([Business Wire](https://www.businesswire.com/news/home/20260625381441/en/Nebulock-Raises-25-Million-Series-A-to-Bring-a-Hunt-First-Context-to-the-Enterprise)).

## Differentiation Analysis

| Dimension | Nebulock | Typical SIEM (Splunk/Sentinel) | Manual threat hunting |
|-----------|----------|-------------------------------|------------------------|
| Primary unit | Behavioral sequences / entities | Alerts & rules | Hypothesis-driven queries |
| AI role | Agentic investigations at scale | Copilots / rule suggestions | None (human) |
| Stack model | Overlay on existing telemetry | Central log platform | Uses SIEM data |
| Strength | "Green flag" insider/agent abuse | Broad log collection | Deep but slow |
| Weakness | Early-stage; metrics unverified | Alert fatigue | Headcount-bound |

### Novel vs incremental

**Novel framing:** Behavioral system of record + agentic hunts for credentialed/agentic abuse. **Incremental tech:** Cross-domain correlation and detection engineering are established categories; Nebulock packages them under hunt-first GTM.

## Risks and Open Questions

- Investigation/finding metrics are **vendor-reported** only
- Limited public technical documentation for evaluation
- Overlap with detection-engineering startups (Spectrum, Anvilogic) and XDR narrative may confuse buyers
- Founder pedigree claims from press release not independently verified

## Sources

| # | Source | Tier | URL |
|---|--------|------|-----|
| 1 | Business Wire (Series A announcement) | A | https://www.businesswire.com/news/home/20260625381441/en/Nebulock-Raises-25-Million-Series-A-to-Bring-a-Hunt-First-Context-to-the-Enterprise |
| 2 | SiliconANGLE funding analysis | A | https://siliconangle.com/2026/06/25/nebulock-raises-25m-expand-hunt-first-security-platform/ |
| 3 | SecurityWeek (discovery RSS source) | A | https://www.securityweek.com/nebulock-raises-25-million-for-ai-native-contextual-security/ |
| 4 | Axios Pro (funding exclusive) | A | https://www.axios.com/pro/enterprise-software-deals/2026/06/25/nebulock-threat-hunting-cybersecurity |
| 5 | Nebulock website | C | https://nebulock.io |
