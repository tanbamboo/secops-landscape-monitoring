# Deepfence ThreatMapper

**Report date:** 2026-06-29  
**Slug:** `deepfence-threatmapper`  
**Type:** technology  
**Categories:** cloud_identity, vuln_exposure  
**Status:** published

---

## Executive Summary

**ThreatMapper** is Deepfence's **Apache 2.0 open-source CNAPP** for runtime threat management, vulnerability prioritization, and attack-path visualization in cloud-native environments. It combines **agent-based Sensor Agents** and **agentless Cloud Scanner** tasks under a containerized Management Console, ranking risks by exploitability via **ThreatGraph** (v1.5+) ([README](https://github.com/deepfence/ThreatMapper/blob/master/README.md)). With **~5,300 GitHub stars** since 2020 and documented enterprise adoption claims via parent company Deepfence, it is a mature OSS alternative in the CNAPP/CSPM space. Commercial **ThreatStryker** adds runtime protection and enterprise support atop the same foundation ([PR Newswire](https://www.prnewswire.com/news-releases/deepfence-unleashes-threatstryker-the-enterprise-evolution-of-open-source-cloud-native-application-protection-platform-301891285.html)). Differentiation vs Wiz/Prisma is **open-source self-management** and **attack-path graphing**; vs pure CSPM tools, it adds malware scanning and runtime context.

## Landscape Context

### The problem

Cloud-native teams need continuous visibility into vulnerabilities, secrets, misconfigurations, and malware across Kubernetes, containers, serverless, and multi-cloud estates—with prioritization, not endless CVE lists.

### Incumbents

| Incumbent | Focus | ThreatMapper contrast |
|-----------|-------|----------------------|
| Wiz / Prisma Cloud | Commercial CNAPP SaaS | ThreatMapper OSS + self-host |
| Aqua / Sysdig | Runtime + CNAPP | Overlapping; ThreatMapper emphasizes ThreatGraph |
| Tenable/Qualys | VM breadth | ThreatMapper cloud-native/runtime graph |

## What It Is

Per [GitHub README](https://github.com/deepfence/ThreatMapper/blob/master/README.md) and [documentation](https://community.deepfence.io/threatmapper/docs/v1.5/):

**Components:**
- **Management Console** — Docker or Kubernetes deployment
- **Cloud Scanner** — agentless cloud asset monitoring
- **Sensor Agents** — host/container inspection

**Capabilities:**
- Vulnerable software component detection
- Exposed secrets discovery
- Malware identification (YARA-based scanner noted in v1.4 [Dark Reading](https://www.darkreading.com/cloud-security/deepfence-threatmapper-1-4-unveils-open-source-threat-graph-to-visualize-cloud-native-threat-landscape))
- Compliance posture vs industry benchmarks (CSPM, v1.4+)
- **ThreatGraph** — correlates vulnerabilities with network/runtime context to prioritize attack paths (v1.5)

**License:** Apache 2.0 ([GitHub](https://github.com/deepfence/ThreatMapper)).

**Commercial path:** ThreatStryker enterprise CNAPP on AWS Marketplace and via Deepfence ([AWS Marketplace listing](https://aws.amazon.com/marketplace/pp/prodview-6ek6jqkzfpmta)).

## Evidence-Backed Deep Dive

### Architecture

ThreatMapper follows a **console + scanners** pattern:

1. Deploy Management Console (Docker host or K8s)
2. Schedule Cloud Scanner jobs for cloud APIs
3. Deploy Sensor Agents on workloads for deep inspection
4. Aggregate findings; ThreatGraph ranks exploitability
5. Operators remediate prioritized paths

Deepfence blog states ThreatMapper is **100% open source** (Apache 2.0) with APIs for SIEM/external consumption; ThreatStryker consumes telemetry for runtime protection ([Deepfence blog](https://www.deepfence.io/blog/threatmapper-is-now-100-open-source)).

### ThreatGraph differentiation

v1.5 ThreatGraph uses **runtime context (e.g., network flows)** to reduce thousands of findings to actionable attack paths ([README](https://github.com/deepfence/ThreatMapper/blob/master/README.md))—addressing alert fatigue in vulnerability management.

### Maturity signals

| Signal | Evidence |
|--------|----------|
| Created | 2020-02-06 |
| Stars | 5,290 |
| Latest major | ThreatMapper 1.5 (ThreatGraph) |
| Company | Deepfence, Inc. (ThreatStryker GA Aug 2023) |
| Community | Slack/Discord per README |

Vendor PR (2023) cites 10k+ stars across Deepfence OSS portfolio and 3,000 enterprise users—**not independently verified** ([PR Newswire](https://www.prnewswire.com/news-releases/deepfence-unleashes-threatstryker-the-enterprise-evolution-of-open-source-cloud-native-application-protection-platform-301891285.html)).

## Key Findings

- ThreatMapper is an **Apache 2.0 CNAPP** covering VM, secrets, malware, CSPM, and **attack-path prioritization** via ThreatGraph ([README](https://github.com/deepfence/ThreatMapper/blob/master/README.md)).
- **Agent + agentless** hybrid coverage targets Kubernetes, serverless (Fargate), and multi-cloud per product positioning ([README](https://github.com/deepfence/ThreatMapper/blob/master/README.md)).
- Deepfence **open-sourced** ThreatMapper fully (2023 blog) while monetizing **ThreatStryker** for enterprise runtime protection ([Deepfence blog](https://www.deepfence.io/blog/threatmapper-is-now-100-open-source)).
- **ThreatGraph** (1.4–1.5) is the primary technical differentiator vs flat CVE scanners ([Dark Reading](https://www.darkreading.com/cloud-security/deepfence-threatmapper-1-4-unveils-open-source-threat-graph-to-visualize-cloud-native-threat-landscape)).
- At **5k+ stars** over 5+ years, ThreatMapper is established OSS; not a startup experiment ([GitHub](https://github.com/deepfence/ThreatMapper)).

## Differentiation Analysis

| Dimension | ThreatMapper | Wiz (incumbent) | Tenable |
|-----------|--------------|-----------------|---------|
| License | Apache 2.0 OSS | Commercial SaaS | Commercial |
| Runtime graph | ThreatGraph | Attack path features | Limited cloud graph |
| Deployment | Self-managed | SaaS | Hybrid |
| Runtime blocking | via ThreatStryker | Cloud-native | Agent-based |
| Cost | Free OSS core | Enterprise $$$ | Enterprise $$ |

**Novel (at OSS launch):** Open ThreatGraph-style correlation across cloud-native stack. **Incremental now:** CNAPP category is crowded; ThreatMapper competes on OSS + graph UX.

## Risks and Open Questions

- Enterprise features (inline protection) largely in **ThreatStryker**, not pure OSS
- Operational overhead of console + agents + cloud scanners at scale
- Vendor enterprise claims (3,000 customers) from 2023 PR—not updated independently
- Last push June 2026 but slower cadence than greenfield AI SOC projects
- SIEM integration depends on API export maturity vs native Splunk apps

## Sources

| # | Source | Tier | URL |
|---|--------|------|-----|
| 1 | ThreatMapper GitHub | B | https://github.com/deepfence/ThreatMapper |
| 2 | ThreatMapper README | B | https://github.com/deepfence/ThreatMapper/blob/master/README.md |
| 3 | Deepfence docs v1.5 | B | https://community.deepfence.io/threatmapper/docs/v1.5/ |
| 4 | Deepfence ThreatStryker PR (context) | A | https://www.prnewswire.com/news-releases/deepfence-unleashes-threatstryker-the-enterprise-evolution-of-open-source-cloud-native-application-protection-platform-301891285.html |
| 5 | Dark Reading ThreatGraph 1.4 | A | https://www.darkreading.com/cloud-security/deepfence-threatmapper-1-4-unveils-open-source-threat-graph-to-visualize-cloud-native-threat-landscape |
| 6 | Deepfence 100% OSS blog | C | https://www.deepfence.io/blog/threatmapper-is-now-100-open-source |
| 7 | AWS Marketplace ThreatStryker | A | https://aws.amazon.com/marketplace/pp/prodview-6ek6jqkzfpmta |
