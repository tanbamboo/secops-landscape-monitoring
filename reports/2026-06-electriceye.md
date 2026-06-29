# ElectricEye

**Report date:** 2026-06-29  
**Slug:** `jonrau1-electriceye`  
**Type:** technology  
**Categories:** cloud_identity, vuln_exposure  
**Status:** published

---

## Executive Summary

**ElectricEye** is an **Apache-2.0** Python CLI for **multi-cloud and multi-SaaS CSPM/SSPM** with **1,000+ checks** across AWS, GCP, Azure, OCI, M365, Salesforce, ServiceNow, and Snowflake ([README](https://github.com/jonrau1/ElectricEye/blob/master/README.md)). With **~1,043 stars** since 2020, it maps findings to **20+ compliance frameworks** and outputs ASFF for AWS Security Hub, OCSF, PostgreSQL, and Slack. ASM enrichment uses Shodan, Nmap, and CISA KEV. Differentiation vs **Wiz/Prowler** is **broad SaaS + cloud scope in one OSS CLI** without managed graph UI.

## Landscape Context

### The problem

Organizations need agentless posture assessment across heterogeneous cloud and SaaS without CNAPP licensing.

### Incumbents

Wiz, Prisma Cloud, Prowler, ScoutSuite, Microsoft Defender for Cloud.

## What It Is

Per [README](https://github.com/jonrau1/ElectricEye/blob/master/README.md):

- Agentless API-based audits
- Compliance: CIS, PCI, HIPAA, NIST mappings (20+ frameworks)
- Outputs: [OUTPUTS.md](https://github.com/jonrau1/ElectricEye/blob/master/docs/outputs/OUTPUTS.md) — Security Hub, OCSF v1.1/v1.4
- Custom checks via [Developer Guide](https://github.com/jonrau1/ElectricEye/blob/master/docs/new_checks/DEVELOPER_GUIDE.md)

## Evidence-Backed Deep Dive

### Development / maturity signals

| Signal | Detail |
|--------|--------|
| Stars | 1,043 |
| Last code push | 2026-02-09 |
| License | Apache-2.0 |
| CI | CodeQL, SBOM pipelines per README |

## Key Findings

- **1,000+ checks** across 100+ services and 20+ frameworks ([README](https://github.com/jonrau1/ElectricEye/blob/master/README.md)).
- **Multi-SaaS** (M365, Salesforce, ServiceNow) beyond typical CSPM tools ([README](https://github.com/jonrau1/ElectricEye/blob/master/README.md)).
- Native **AWS Security Hub ASFF** export ([OUTPUTS.md](https://github.com/jonrau1/ElectricEye/blob/master/docs/outputs/OUTPUTS.md)).
- **CLI-only**—no central console vs Wiz/Prisma ([GitHub](https://github.com/jonrau1/ElectricEye)).
- Development cadence slower than Prowler in 2026 ([GitHub activity](https://github.com/jonrau1/ElectricEye)).

## Differentiation Analysis

| Dimension | ElectricEye | Prowler | Wiz |
|-----------|-------------|---------|-----|
| SaaS coverage | Broad | Growing | Broad SaaS |
| UI | CLI | App + Cloud | SaaS graph |
| License | Apache-2.0 | Apache-2.0 | Proprietary |

## Risks and Open Questions

- Complex AWS org-wide IAM setup
- ASM features need third-party API keys (Shodan, VT)
- Production-use claims tier C until verified

## Sources

| # | Source | Tier | URL |
|---|--------|------|-----|
| 1 | ElectricEye GitHub | B | https://github.com/jonrau1/ElectricEye |
| 2 | README | B | https://github.com/jonrau1/ElectricEye/blob/master/README.md |
| 3 | OUTPUTS.md | B | https://github.com/jonrau1/ElectricEye/blob/master/docs/outputs/OUTPUTS.md |
| 4 | Developer Guide | B | https://github.com/jonrau1/ElectricEye/blob/master/docs/new_checks/DEVELOPER_GUIDE.md |
| 5 | Apache-2.0 LICENSE | B | https://github.com/jonrau1/ElectricEye/blob/master/LICENSE |
