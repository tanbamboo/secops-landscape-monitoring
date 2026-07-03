# SecOps Landscape 每日简报

**日期：** 2026-07-03（周五）  
**来源：** `topics/registry.yaml` 未发布候选 + 本周已发布报告上下文  
**本期深度介绍：** 5 项（开源技术为主）

---

## 今日概览

本周仓库已完成 **179 项** inbox 批量 triage，并发布 10 份深度报告（Devo、CloudQuery、Prowler、Shuffle 等）。今日简报从 **293 个未发布候选** 中选取 5 个与 **AI 原生 SOC、开源 SIEM/SOAR、云安全数据平面** 高度相关的项目，供今日研判与跟进。

| # | 名称 | 类型 | 赛道 | 成熟度信号 |
|---|------|------|------|------------|
| 1 | Tracecat | 技术 | AI 原生 SOAR | ~3.7k stars，Temporal + nsjail |
| 2 | SecurityClaw | 技术 | 自治 SOC Agent | ~250 stars，LangGraph + RAG |
| 3 | UTMStack v11 | 技术 | 开源 SIEM/XDR | ~574 stars，v10 将于 2026-12 停服 |
| 4 | Steampipe | 技术 | 云安全 SQL 查询 | 成熟项目，2000+ API 表 |
| 5 | VictoriaLogs | 技术 | 日志存储后端 | VictoriaMetrics 生态，TB 级日志 |

---

## 1. Tracecat — Agentic 安全自动化平台

**一句话：** 面向 AI 原生安全团队的开源 SOAR，把 Agent、工作流、工单和 MCP 集成放在同一平台。

### 是什么

[Tracecat](https://tracecat.com) 是 AGPL-3.0 开源的**安全自动化平台**，定位是「teams and AI agents」共同使用的 SOAR 替代方案（[GitHub README](https://github.com/TracecatHQ/tracecat/blob/main/README.md)）。核心能力包括：

- **Agents**：自定义提示词、工具与对话式 Agent
- **Workflows**：低代码编排，基于 **Temporal** 实现持久化执行；支持条件、循环
- **Case management**：工单跟踪与自动化结案
- **Tracecat MCP**：通过 Claude Code、Copilot 等将自然语言提示转为自动化
- **100+ 集成**：HTTP、SMTP、gRPC、OAuth 等连接器
- **默认沙箱**：不可信代码在 **nsjail** 中运行

技术栈：Python/FastAPI 后端，Next.js 前端，PostgreSQL，S3 兼容对象存储。

### 与现有格局的差异

| 维度 | Tracecat | Cortex XSOAR / Splunk SOAR | Shuffle（已发布报告） |
|------|----------|---------------------------|----------------------|
| AI 原生 | MCP + Agent 为一等公民 | Copilot  bolt-on 为主 | OpenAPI 集成为主 |
| 执行引擎 | Temporal 持久化 | 厂商运行时 | Orborus 混合部署 |
| 许可 | AGPL-3.0（EE 功能闭源） | 商业 | AGPL 核心 |

**真正新颖之处：** Prompt-to-automation + MCP 双向集成（既可被编码助手驱动，也可作为 MCP 客户端连接外部 Agent 工具），比传统 SOAR 更贴近 2026 年「安全团队用 AI 自建 runbook」的工作方式。

### 风险与开放问题

- 活跃开发中，升级需关注 [changelog](https://github.com/TracecatHQ/tracecat/releases)
- Enterprise 功能（RBAC、Git 同步、托管 MCP）在付费/云版本
- AGPL 对 MSSP 托管部署有合规考量

**建议跟进：** 与已发布的 [Shuffle SOAR](../reports/2026-06-shuffle.md)、[AiSOC](../reports/2026-06-aisoc.md) 做三角对比——Tracecat 更强调 **Agent + MCP 产品化**，Shuffle 更偏传统 SOAR 开源替代。

---

## 2. SecurityClaw — 模块化自治 SOC Agent

**一句话：** 基于 OpenSearch/Elasticsearch 与本地 LLM（Ollama）的自治 SOC Agent 框架，技能可插拔、带 RAG 行为记忆。

### 是什么

[SecurityClaw](https://github.com/SecurityClaw/SecurityClaw)（约 **250 stars**）是模块化的**自治 SOC Agent**（[README](https://github.com/SecurityClaw/SecurityClaw/blob/main/README.md)）：

- **Skill 架构**：每个能力为独立文件夹（`logic.py` + `instruction.md`）
- **心跳调度**：1 分钟异常监视 + 6 小时记忆构建
- **LangGraph**：DECIDE→EXECUTE→EVALUATE 监督循环；SQLite 检查点持久化对话
- **RAG 记忆**：向量嵌入存于 OpenSearch，支撑上下文威胁分析
- **Web UI**：React 聊天、记忆可视化、技能派发
- **默认 LLM**：Ollama + `qwen2.5:7b`（可换提供商）

数据源：OpenSearch 或 Elasticsearch 8.x；可对接 AbuseIPDB、OTX、VirusTotal 等外部 API。

### 与现有格局的差异

| 维度 | SecurityClaw | AiSOC | Wazuh + 自建 Copilot |
|------|--------------|-------|---------------------|
| 定位 | SIEM 数据上的自治 Agent | 全栈 MIT AI SOC | 传统 SIEM + 外挂 AI |
| 部署 | 自托管 + Ollama | Docker 全栈 | 成熟 SIEM + 实验性 AI |
| 审计 | LangGraph 状态 + 技能清单 | Investigation Ledger | 依赖 SIEM 自身 |

**真正新颖之处：** **技能清单驱动（manifest-grounded）** 的规划与重试，避免 LLM 编造工具名；适合已有 Elastic/OpenSearch 日志栈、希望叠加自治分析而非替换 SIEM 的团队。

### 风险与开放问题

- 项目较新，社区规模小于 Tracecat/AiSOC
- 本地小模型（7B）在复杂调查上的可靠性需实测
- 非全栈 SIEM——依赖现有日志平台质量

**建议跟进：** 适合作为「**Elastic/Sentinel 之上的自治层**」评估对象，与 [AiSOC 报告](../reports/2026-06-aisoc.md) 对比全栈 vs overlay 路线。

---

## 3. UTMStack v11 — 开源 SIEM + SOAR + 合规

**一句话：** AGPL 统一威胁管理平台，v11 重写关联引擎；v10 将于 **2026-12-05** 停止支持。

### 是什么

[UTMStack](https://github.com/utmstack/UTMStack)（约 **574 stars**）是集成 **SIEM、SOAR、XDR、合规** 的开源平台（[v11 README](https://github.com/utmstack/UTMStack/blob/v11/README.md)）：

- **关联在摄入前完成**（非 ELK/Logstash 管道），宣称降低索引负载、缩短响应时间
- 自研 EventProcessor，**不使用 Logstash** 做关联（存储仍用 Elasticsearch）
- 功能：日志管理、威胁检测与响应、威胁情报、文件分类、**SOC AI 分析**、合规（CMMC、HIPAA、SOC 2、ISO 27001、PCI）
- **v11**：水平扩展 manager/worker、强制 MFA、插件系统
- 商业版 [utmstack.com](https://utmstack.com) 提供支持、更快关联与 TI 更新

### 与现有格局的差异

| 维度 | UTMStack v11 | Wazuh | Elastic Security |
|------|--------------|-------|------------------|
| 打包 | SIEM+SOAR+合规一体 | XDR/SIEM 模块丰富 | Elastic 栈 + Kibana |
| 关联 | 摄入前关联（自研） | 规则 + 解码器 | Detection engine |
| 许可 | AGPL-3.0 | GPLv2 系 | Elastic License / SSPL |

**真正新颖之处：** **预摄入关联** 架构在开源 SIEM 中较少见；对资源受限、希望单平台覆盖合规的中型企业有吸引力。

### 风险与开放问题

- **v10→v11 需全新安装**，不可原地升级；v10 仅关键修复至 2026-12-05
- **140+ open issues**，企业级 SLA 需商业版
- Ubuntu 22.04/24.04 导向，资源需求随日志量陡增（官方 sizing 表：500 数据源需 32C/64GB）

**建议跟进：** 与已发布 [Wazuh](../reports/2026-06-wazuh.md) 对照；registry triage score=38，建议优先安排完整 landscape 报告。

---

## 4. Steampipe — Zero-ETL 云安全 SQL 查询

**一句话：** 用 SQL 实时查询云 API（AWS/Azure/GCP/K8s/GitHub 等），无需自建 ETL 管道。

### 是什么

[Steampipe](https://steampipe.io)（[turbot/steampipe](https://github.com/turbot/steampipe)，AGPL-3.0）将云服务 API **映射为 SQL 表**，支持：

- **CLI 交互查询**：内置 Postgres 实例
- **Postgres FDW**：外部表方式接入现有数据库
- **SQLite 扩展**、**导出工具**、云托管 **Turbot Pipes**
- [Steampipe Hub](https://hub.steampipe.io/)：**2000+ 表**，覆盖 AWS、Azure、GCP、Kubernetes、GitHub、Microsoft 365 等

安全运营典型用法：云资产盘点、合规检查、跨账号配置审计、与 [Powerpipe](https://github.com/turbot/powerpipe) 可视化、与 [CloudQuery](../reports/2026-06-cloudquery.md) 的 ELT 批处理形成互补。

### 与现有格局的差异

| 维度 | Steampipe | CloudQuery | Prowler |
|------|-----------|------------|---------|
| 数据模型 | 实时 API→SQL | ELT 入仓 | 检查引擎 + CLI |
| 新鲜度 | 实时查询 | 批处理同步 | 扫描时点 |
| 学习曲线 | SQL 即可 | 需数据工程 | CLI/Hub 检查 |

**真正新颖之处：** **Zero-ETL** 让检测工程师用 SQL 直接问云 API，适合 ad-hoc 狩猎与合规脚本；与 CloudQuery「入仓再查」是架构级取舍。

### 风险与开放问题

- 大规模并行 API 查询可能触发云厂商限流
- 商业品牌 Turbot Pipes 与开源 CLI 功能边界需厘清
- 非 CNAPP——无攻击路径图或运行时威胁检测

**建议跟进：** 与 [CloudQuery](../reports/2026-06-cloudquery.md)、[Prowler](../reports/2026-06-prowler.md) 组成「开源云安全数据平面」专题。

---

## 5. VictoriaLogs — 高性能开源日志库

**一句话：** VictoriaMetrics 团队出品的日志数据库，面向 TB 级日志存储与查询，可作为 SIEM 后端替代 Elasticsearch 成本热点。

### 是什么

[VictoriaLogs](https://github.com/VictoriaMetrics/VictoriaLogs) 是 VictoriaMetrics 团队出品的**开源日志数据库**（**Apache-2.0**，[文档](https://docs.victoriametrics.com/victorialogs/)）：

- 官方宣称较 Elasticsearch/Loki **显著降低 RAM 与磁盘占用**（见 [benchmarks](https://docs.victoriametrics.com/victorialogs/)）
- **LogsQL** 查询语言；内置 Web UI；Grafana 插件
- 支持高基数字段（`trace_id`、`user_id` 等）与 **SIEM 场景**（含 Syslog CEF 自动解析）
- 单节点与集群模式；可与 `grep`/`jq` 等 Unix 工具管道组合

在 SecOps 格局中，VictoriaLogs 属于 **数据平面/可观测性基础设施**，而非检测逻辑本身——常与 Vector、Fluent Bit、Grafana、自研关联引擎组合。

### 与现有格局的差异

| 维度 | VictoriaLogs | Elasticsearch (SIEM 常用) | Splunk |
|------|--------------|---------------------------|--------|
| 角色 | 日志存储与查询引擎 | 日志 + 搜索 + ES 安全特性 | 全栈 SIEM 平台 |
| 成本曲线 | 开源、资源效率导向 | 集群成本随数据量上升 | 许可证按量 |
| 生态 | VictoriaMetrics 用户 | Elastic Security 深度集成 | 最广 SIEM 生态 |

**真正新颖之处：** 在 **SIEM 成本优化** 叙事下（日志保留 400 天、热温冷分层），VictoriaLogs 类引擎是 2026 年多个团队评估的 Elasticsearch 替代路径之一。

### 风险与开放问题

- 不自带 SIEM 关联、SOAR、UEBA——需上层产品
- 与 Elastic Security _detection 工作流迁移成本
- 企业支持模式依赖 VictoriaMetrics 商业服务

**建议跟进：** 适合作为「**SIEM 后端选型**」研究，与 Devo/Splunk 等数据平台定价叙事对照。

---

## 本周已发布报告（延伸阅读）

- [Devo Technology](../reports/2026-06-devo.md) · [CloudQuery](../reports/2026-06-cloudquery.md) · [Prowler](../reports/2026-06-prowler.md)
- [Shuffle SOAR](../reports/2026-06-shuffle.md) · [CyberStrikeAI](../reports/2026-06-cyberstrikeai.md)
- [以色列网络生态](../reports/2026-06-israeli-cyber-dominance.md) · [B2B 平台安全化](../reports/2026-06-b2b-platform-security.md)

---

## 明日建议

1. 对 **Tracecat** 或 **UTMStack** 启动完整 `research/{slug}/` + 报告流程（当前 registry 状态：`new`）
2. 运行 `python scripts/discover.py` 刷新 inbox，关注 Venture in Security / Talos 新文
3. 评估 **SecurityClaw** 与现有 Elastic 栈的 PoC 成本（Ollama + OpenSearch）

---

*本简报由 SecOps Landscape Monitoring 系统自动生成，结论基于 tier A/B 公开来源；vendor 数据以交叉验证为准。*
