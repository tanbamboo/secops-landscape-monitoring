# Prowler

**Report date:** 2026-06-29  
**Slug:** `prowler-cloud-prowler`  
**Type:** technology  
**Categories:** cloud_identity  
**Status:** published

---

## Executive Summary

**Prowler** is a widely deployed **open-source cloud security and compliance platform** (**Apache-2.0**, **~14,062 stars**) automating posture checks across **22+ provider modules** (AWS, Azure, GCP, Kubernetes, GitHub, Okta, M365, IaC, LLM, container images) ([GitHub](https://github.com/prowler-cloud/prowler)). It ships as CLI, self-hosted **Prowler App**, and commercial **Prowler Cloud**, with checks cataloged on [Prowler Hub](https://hub.prowler.com). Differentiation vs **Wiz/Prisma** is **OSS deployability and compliance mapping** (CIS, DORA, CSA CCM) without full CNAPP attack-path graph or runtime DSPM.

## Landscape Context

### The problem

Teams need agentless multi-cloud compliance scanning without enterprise CNAPP pricing.

### Incumbents

Wiz, Prisma Cloud, Microsoft Defender for Cloud, ScoutSuite, ElectricEye.

## What It Is

Per [introduction docs](https://github.com/prowler-cloud/prowler/blob/master/docs/introduction.mdx):

- CLI: `prowler <provider>`
- Outputs: SARIF, JSON-OCSF; GitHub Action for CI
- Compliance frameworks under `prowler/compliance/`
- Extensibility: custom checks, MCP server, Lighthouse AI features (per CONTRIBUTING)

## Evidence-Backed Deep Dive

### Development / maturity signals

| Signal | Detail |
|--------|--------|
| Stars | 14,062 |
| Latest release | v5.31.1 (Jun 2025) |
| License | Apache-2.0 |
| Last push | 2026-06-29 |

## Key Findings

- **14k+ stars** make Prowler one of the most-used OSS CSPM tools ([GitHub](https://github.com/prowler-cloud/prowler)).
- **22 provider modules** span cloud, SaaS, K8s, IaC, and LLM checks ([introduction.mdx](https://github.com/prowler-cloud/prowler/blob/master/docs/introduction.mdx)).
- **Prowler Hub** hosts versioned checks and compliance frameworks ([hub.prowler.com](https://hub.prowler.com)).
- **Apache-2.0** enables self-hosted and fork-friendly deployments ([GitHub](https://github.com/prowler-cloud/prowler)).
- Lacks Wiz-style **unified risk graph and runtime CNAPP** depth—CSPM/compliance-first ([introduction.mdx](https://github.com/prowler-cloud/prowler/blob/master/docs/introduction.mdx)).

## Differentiation Analysis

| Dimension | Prowler | Wiz | AWS Config |
|-----------|---------|-----|------------|
| Scope | Multi-cloud CSPM OSS | Full CNAPP SaaS | Single-cloud |
| License | Apache-2.0 | Proprietary | AWS-native |
| Runtime threats | Limited | Strong | Limited |

## Risks and Open Questions

- Commercial Prowler Cloud vs OSS feature split
- Check quality varies by provider maturity
- AI/MCP features need independent security review

## Sources

| # | Source | Tier | URL |
|---|--------|------|-----|
| 1 | Prowler GitHub | B | https://github.com/prowler-cloud/prowler |
| 2 | Prowler README | B | https://github.com/prowler-cloud/prowler/blob/master/README.md |
| 3 | Introduction docs | B | https://github.com/prowler-cloud/prowler/blob/master/docs/introduction.mdx |
| 4 | Prowler Hub | B | https://hub.prowler.com |
| 5 | Provider modules | B | https://github.com/prowler-cloud/prowler/tree/master/prowler/providers |
