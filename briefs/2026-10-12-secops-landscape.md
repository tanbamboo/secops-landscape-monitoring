# SecOps Landscape 每周简报

**日期：** 2026-10-12（周一；discovery 于 2026-10-11 23:03 UTC 运行）  
**来源：** `python scripts/discover.py` 当日 inbox、`topics/registry.yaml` 未发布候选、`reports/INDEX.md`、当周独立报道  
**本期深度介绍：** 5 项（2 家创业公司 + 3 个检测 / 取证技术）

---

## 本周概览

本周 discovery 新增 **89** 条 inbox，跳过 **226** 条重复。`generate_brief.py` 按 triage score 排出的前五名仍不适合作为深度对象：`sentinel-enterprise-siem-for-startups-splunk-alternative-free`（score 44）指向 `github.com/yourusername/sentinel` 占位地址；Qadium（score 43）是 2016 年 Forbes 旧闻；`0xSteph/pentest-ai`（score 40）与已发布的 [CyberStrikeAI](../reports/2026-06-cyberstrikeai.md) 同属进攻向 AI 编排；UTMStack（score 38）已写入 [2026-07-03 简报](2026-07-03-secops-landscape.md)；Xingrin（score 38）已在 [2026-10-08 简报](2026-10-08-secops-landscape.md) 中因停更而搁置。

RSS 窗口也没把本周两轮融资带进高分：SecurityWeek 的 Rein 稿被后续条目挤出每个源只取的前 15 条。下面五项是 **未出现在已发布报告、也未写入 7 月 3 日或 10 月 8 日简报**、且能对上独立报道或现行技术文档的对象。主线是：商业侧在给「自己部署的 AI agent」和「合法权限下的数据移动」各做一层运行时控制；开源与从业者侧则在补离线 Sigma 狩猎，以及编码 agent 留在终端上的会话记录。

| # | 名称 | 类型 | 赛道 | 本期信号 |
|---|------|------|------|----------|
| 1 | Rein Security | 创业公司 | Agent 运行时防护 | 2026-10-08 Series A $25M，累计 $35M |
| 2 | Hilt | 创业公司 | 数据移动检测 | 2026-10-07 前后出隐，seed $4.2M |
| 3 | Anthropic OSS Scanner | 技术 | 开源漏洞发现 | 2026-10-08 上线，报告不经人工复核 |
| 4 | Zircolite 4.5 | 技术 | 离线 Sigma 检测 | 4.5.0 于 2026-10-10 发布 |
| 5 | OpenCode / Hermes 取证脚本 | 技术 | 编码 agent 取证 | SANS ISC 2026-10-08 日记 |

---

## 1. Rein Security — 企业自建 agent 的运行时控制

**一句话：** 特拉维夫 / 纽约公司于 2026-10-08 宣布 Series A $25M，卖的是放在 agent 执行路径上的 sidecar：看见每一次动作，并按基线拦下单次动作。

### 是什么

三家独立媒体对融资事实一致：

- [SecurityWeek](https://www.securityweek.com/rein-security-raises-25-million-to-guard-ai-agents-at-runtime/)（2026-10-08）：**$25M Series A**，累计 **$35M**。联合领投 **Glilot Capital** 与 **Sienna Venture Capital**，跟投 Corner Ventures、Atlacle、RNP Capital Advisors。公司 **2024** 年成立，总部特拉维夫与纽约，起初做应用运行时防护，后扩到 AI agent。资金用于产品、agent 研究和扩编。
- [Calcalist](https://www.calcalistech.com/ctechnews/article/rkf52cnimg)（2026-10-08）：创始人 **Matan Bar-Efrat** 与 **Netanel Rubin**，员工 **31** 人。Rubin 对记者说，公司盯的是企业自己建的 agent，部署在客户云里，不把公司或客户数据送过网关或代理。平台被描述为带专利的 sidecar：在动作执行时看代码与资源访问，并设实时护栏。
- [SiliconANGLE](https://siliconangle.com/2026/10/08/rein-security-raises-25m-to-rein-in-insecure-ai-agents/)：同一轮、同一对创始人（Bar-Efrat 任 CEO，Rubin 任 CTO）。记者转述的架构是轻量 sidecar，覆盖提示词、API 调用和数据库访问；先为每个 agent 建行为基线，再在执行点做动作级控制。Bar-Efrat 的原话是：不结束 agent 进程、线程或整次请求，只阻止那一次有害动作，其余工作流继续。

「收入较 2026 年 1 月产品上线增长 8 倍、客户数 5 倍、已保护数千个 agent、每周数百万次动作」是公司对 Calcalist 与 SiliconANGLE 的陈述。SiliconANGLE 列出的客户（Flex、Swimlane、Lemonade、Dun & Bradstreet）同样来自公司。Black Hat USA 2026 上 Agent Breakers 演示「攻破一家美国大型零售商的购物 agent」也是公司叙述，本简报不记录演示手法。

### 与现有格局的差异

taxonomy 里 AI SecOps 的参照物是 Dropzone AI、Prophet Security，以及 Splunk / Elastic 的数据平台；检测响应参照物是 CrowdStrike Falcon 与 Cortex XDR。已发布的 [Nebulock](../reports/2026-06-nebulock.md) 是狩猎优先的上下文分析，[Spectrum](../reports/2026-06-spectrum-security.md) 是检测工程生命周期。

| 维度 | Rein | Dropzone / Prophet | EDR / XDR | 已发布的 Nebulock |
|------|------|--------------------|-----------|-------------------|
| 问题 | 自建 agent 正在执行的这一步是否偏离基线 | 告警调查与 SOC 自动化 | 终端上的进程与身份 | 跨终端 / 身份 / 云的狩猎 |
| 部署 | 公司称客户云内 sidecar | 接入现有 SOC 数据 | 终端代理 | 接入现有遥测做狩猎 |
| 干预 | 公司称只拦单次动作，不拆掉整个请求 | 调查与建议为主 | 隔离主机 / 杀进程 | 狩猎产出，不是执行期拦截 |
| 公开证据 | 融资、创始人、sidecar 叙事有三家媒体 | 成熟品类 | 成熟品类 | 既有报告 |

**已经存在的部分：** 在工作负载旁边放探针、为行为建基线、在运行时拦截，是 RASP 和 EDR 的现成形状。提示词注入检测、网关式 AI 防火墙，也已经有人在卖。

**本期能分开的部分：** 独立报道把产品放在「企业自己编写的 agent」的执行点，并且 CEO 对媒体把控制粒度说成单次动作，而不是整进程或整请求。这和「再做一个告警分诊 agent」不是同一层。sidecar 是否真能看见每一次工具调用、误拦时工作流是否还能继续，没有公开的日志样例或第三方评测。专利内容未核对。

### 风险与开放问题

- 增长倍数、客户名单、「数千 agent」都是公司陈述。
- 「现有平台保不住 agent」是创始人与投资人的判断，不是对照评测。
- 闭源。规则、基线特征和拦截日志格式都未公开，SOC 无法拿自己的 agent 轨迹复现。
- 与已发布的 [以色列网络安全格局](../reports/2026-06-israeli-cyber-dominance.md) 不是同一题：那份报告写的是大型退出，这里是一家 2024 年成立的运行时产品。

---

## 2. Hilt — 合法权限下的数据移动

**一句话：** Chattanooga 团队于 2026 年 10 月出隐，seed **$4.2M**。公开访谈把产品说成内核级行为检测：有权限的数据移动也可以被标成异常，并可隔离。

### 是什么

融资细节来自一篇独家，而不是多篇独立调查。[Crunchbase News](https://news.crunchbase.com/cybersecurity/from-ballet-to-breach-prevention-ai-startup-hilt-cielen/)（Mary Ann Azevedo，2026-10-07）写明数字由公司向该刊独家提供：

- Seed **$4.2M**，领投 **Array Ventures**，跟投 Verdict Capital、Base10 Partners、Brickyard、Liquid 2 Ventures、Sequel、Sarah Smith Fund、Alumni Ventures。累计 **$4.7M**，其中 **$500K** pre-seed 由 Pear VC 于 2025 年 10 月领投。
- CEO **William Cielen**，CTO **Alex Genest**，创始工程师 **Zin Bitar**。约 **11** 人。团队从旧金山迁到田纳西州 Chattanooga，投资方之一是 Brickyard。
- 软件看数据如何在云、计算机和网络上移动，为用户和资源建行为基线；当事人有权限时仍可告警。资金主要用于招聘和进入市场。
- Cielen 对记者说：采集在内核进行，活动流送进图神经网络；客户把产品跑在自己的基础设施里，按采集器年费付费；响应可以是通知调查，也可以在发生时隔离。一位对冲基金客户在产品完成前付了六位数预付款，以及「某客户测到上线后云系统变快」，都是创始人陈述，没有测试方法。

[Dealroom](https://dealroom.co/news/160643-hilt-exits-stealth-with-4-2m-seed-to-catch-data-breaches-that-look-norma/) 记下同一轮金额和投资人，事实来源仍是这一独家，不能算第二家新闻编辑部的独立采访。

[公司平台页](https://hilt.ai/platform) 在访谈之外还写了：默认只看元数据、控制面做主机网络隔离且不在线阻断、采集器覆盖云工作负载以及 macOS / Windows、另有浏览器扩展。这些句子没有第二来源，下面不把它们当成已核实架构。

### 与现有格局的差异

taxonomy 没有单列 DLP。最近的参照物是检测响应里的 CrowdStrike 与 Microsoft 终端产品，以及云安全里的 Wiz / Defender for Cloud。

| 维度 | Hilt | EDR | 云配置 / 数据面扫描 | 传统内容 DLP |
|------|------|-----|---------------------|----------------|
| 看什么 | 访谈：数据怎么移动，含已授权行为 | 进程、身份、恶意行为 | 资产、配置、暴露 | 文件内容与策略标签 |
| 采集点 | 创始人称在内核 | 厂商代理 | API 与扫描器 | 网络、终端或邮件网关 |
| 数据是否出域 | 访谈与投资人：留在客户环境 | 常见为厂商云 | 视产品而定 | 视产品而定 |
| 公开证据 | 一轮独家融资访谈 | 成熟品类 | 成熟品类 | 成熟品类 |

**已经存在的部分：** 用终端遥测发现异常外传、对内部人已授权的访问做行为分析，是 EDR 和内部风险产品的现成问题。内核采集本身也不是新品类。

**本期能分开的部分：** 公开材料把第一批客户放在不能接受明显延迟的交易环境，并把「有权限的移动」而不是「已知恶意文件」写成检测对象。图神经网络、元数据边界和隔离是否可逆，都还只有公司说法。

### 风险与开放问题

- 除 Crunchbase News 的独家外，没有第二家编辑部做独立采访。Dealroom 是同一事实的转记。
- 没有规则、日志样本或延迟测试。六位数预付款和「上线后变快」无法复核。
- 平台页上的浏览器扩展、0.1% CPU 一类数字未进入访谈，本期不采用。
- 内核采集器的操作系统版本、权限和失效方式完全未公开。把它写成 EDR 替代还没有证据。

---

## 3. Anthropic OSS Scanner — 不经人工复核的开源漏洞报告

**一句话：** 2026-10-08 上线的免费、须项目方主动加入的扫描服务。模型直接把漏洞报告寄给维护者，报告里可以有复现说明和补丁草案，Anthropic 明确说这些报告没有人工复核。

### 是什么

[SecurityWeek](https://www.securityweek.com/anthropic-fast-tracks-ai-bug-reports-to-oss-maintainers-taps-11-firms-for-ot-security/)、[Help Net Security](https://www.helpnetsecurity.com/2026/10/09/anthropic-oss-scanner-ai-security-scans/) 与 [Anthropic 研究帖](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source)（2026-10-08）对服务形状一致：

- 对象是维护者 **opt-in** 的开源项目，不收费。Anthropic 把对照物写成 Google 的 **OSS-Fuzz**：那边用模糊测试，这里用其最强模型（研究帖点名包含 Claude Mythos）。
- 报告由模型生成，**不经人工复核**。SecurityWeek 写明每份报告解释疑点、附带可如何利用的材料，并在有的时候给出修复建议。Help Net Security 写明首扫后用邮件送出一捆报告，之后的频率取决于需求和使用面。
- 未经验证的发现 **没有强制的 90 天披露期**。若日后走 Anthropic 原有的协调披露并被人工验证，90 天可以从那次通知算起。项目可以暂停自动报告，退回只收人工验证结果。
- 资格由 Anthropic 个案判断，标准接近 OSS-Fuzz：对基础设施和用户安全有关键影响，且维护者消化得了更多发现。加入方式是向 [anthropics/oss-scanner](https://github.com/anthropics/oss-scanner) 提 PR。该仓库 **Apache-2.0**，创建于 2026-10-08，2026-10-11 查阅时约 **794** stars。

研究帖里的流水账是公司自己的数字，媒体在转述：过去六个月约 **29,000** 条候选，人工只复核了约 **6,000** 条；已有维护者主动要过近 **5,000** 份未验证报告。早期版本由公司自己的渗透测试人员抽查 **48** 个项目上的 **97** 条高危 / 严重发现：**85** 条达到其协调披露门槛，**11** 条属实但是已知或重复，**1** 条无效。Help Net Security 同时引了维护者的另一面：严重性可能被抬高，模型会误解项目的威胁模型。OpenSSL、curl、wolfSSL、PostgreSQL、HotCRP 的引语都出现在 Anthropic 的帖子里，属于厂商收集的推荐语。

同一天 SecurityWeek 还写了 **Critical Infrastructure Defense Program**：把 Claude、驻场工程师和威胁研究提供给 OT 安全相关公司。点名的 11 家是 Accenture、Booz Allen、CrowdStrike、Deloitte、Dragos、Hitachi、Insane Cyber、Nozomi Networks、Palo Alto Networks、PwC、Rockwell Automation。这是合作名单，不是扫描器的检测结果，也没有独立的成效数据。研究帖把面向企业的代码扫描产品称作 Claude Security，与 OSS Scanner 分开。

### 与现有格局的差异

| 维度 | OSS Scanner | Tenable / Qualys | Google OSS-Fuzz | 企业里的 Claude Security |
|------|-------------|------------------|-----------------|--------------------------|
| 扫什么 | 主动加入的开源代码 | 企业资产上的已知漏洞与配置 | 开源项目的模糊测试 | 公司称面向企业系统 |
| 谁复核 | 维护者；Anthropic 默认不复核 | 扫描器规则加客户流程 | 模糊测试的崩溃分类 | 未在本期核实 |
| 产出 | 模型报告、复现材料、有时有补丁草案 | 工单里的发现 | 崩溃与回归样例 | 商业产品 |
| 披露时钟 | 未验证报告无强制 90 天 | 客户自己的 SLA | 项目既有披露实践 | 不适用 |

**已经存在的部分：** 用自动化在开源项目里找内存和逻辑问题，OSS-Fuzz 已经做了多年。把未验证的模型输出寄给维护者，也是过去一年维护者已经在抱怨的报告形态。

**本期能分开的部分：** 服务被做成可加入、可退出的正式通道，并且白纸黑字写明「不人工复核」和「未验证则不起 90 天时钟」。97 条样本的命中率是 Anthropic 自有测试人员的统计，不是第三方审计。它不进入企业 SOC 的资产清单，也不替代 Tenable 或 Qualys。

### 风险与开放问题

- 85/97 的样本由卖方自己的渗透测试人员挑选并打分。严重性膨胀被维护者单独指出，不能把「1 条无效」读成整体误报率。
- 报告附带复现材料。对维护者这是验证手段；对未加入的项目，这些材料不会按 90 天流程公开。SOC 不应期待从这里得到可直接导入 SIEM 的规则。
- 扫描频率、模型版本和项目拒绝标准都由 Anthropic 掌握。仓库说明只接受报名 PR，不接受对扫描器本身的外部补丁。
- CIDP 的 11 家伙伴是宣布，不是测评。

---

## 4. Zircolite 4.5 — 离线 Sigma，外加一个浏览器查看包

**一句话：** 2021 年就有的 Python 工具，把日志摊进 SQLite，再把 Sigma 编成 SQL。4.5.0（2026-10-10）换掉 Mini-GUI，改成一个离线打开的查看包。许可证是 **LGPL-3.0**。

### 是什么

[GitHub](https://github.com/wagga40/Zircolite) 2026-10-11 查阅约 **860** stars，最近推送同日。[4.5.0 发布说明](https://github.com/wagga40/Zircolite/releases/tag/v4.5.0)（2026-10-10）与 [文档](https://wagga40.github.io/Zircolite/) 写的当前能力是：

- **输入：** Windows EVTX（二进制、XML、JSON）、Auditd、Sysmon for Linux、EVTXtract、CSV、XML、JSON，含常见压缩包。格式自动判断。
- **规则：** 原生 Sigma YAML 经 pySigma 转到 SQLite，或使用仓库里预转换的 JSON 规则集。关联规则（计数、时间序列、缺失条件）走同一后端。
- **输出：** JSON、CSV，以及 Splunk、Elastic、OpenSearch、Timesketch、SARIF、ATT&CK Navigator 模板。
- **4.5 的包装变化：** `--package` 把一次运行的全部事件（不只是命中）打进一个 zip，本地打开 `index.html`。页面包含检测、时间线、ATT&CK 矩阵、进程树和只读 SQL。发布说明写明内容安全策略禁止页面对外请求，并捆绑 ATT&CK Enterprise 19.2。事件打成 Parquet 后超过 1 GiB 的包会被拒绝。`duckdb` 成为依赖，独立二进制里自带。
- **许可证：** 仓库 LICENSE 为 GNU LGPL 3.0。规则集另有上游许可证，更新通道会把 Hayabusa 等社区规则的许可证文本放进 `rules/licenses/`。

[r/blueteamsec](https://www.reddit.com/r/blueteamsec/comments/1x2gy3t/zircolite_45_sigma_rules_over_evtx_auditd_sysmon/) 在本周转发了 4.5 的发布，标题与版本一致。帖子本身不是评测。

README 上的速度表是项目自己的基准，不是第三方复现。项目写明规则集不同，因此命中条数不能横比。它给出的一组数字是：4 个 Sysmon EVTX、单通道、478 MB、452,554 事件上，Zircolite 加载 4,319 条规则用 11.6 秒、峰值约 1,207 MiB（4 个工作进程）；对照栏写 Hayabusa 4.1.0 为 24.7 秒、900 MiB，Chainsaw 2.16.0 为 113.5 秒、346 MiB。另一组 13.3 GB 混合通道上，Zircolite 峰值到约 8,103 MiB。项目同时写了 `--no-parallel` 可收成单进程。这些数字本期只当作项目自述。

### 与现有格局的差异

| 维度 | Zircolite 4.5 | 已发布的 Hayabusa | Chainsaw | Splunk / Elastic |
|------|---------------|-------------------|----------|------------------|
| 形态 | 分析机上的一条命令 | Windows 时间线与 Sigma | EVTX 狩猎，并可解析部分取证工件 | 集中索引 |
| 日志 | EVTX，外加 Auditd、Sysmon for Linux、JSON 等 | 以 Windows EVTX 为主 | 以 Windows 证据为主 | 转发进来的一切 |
| 引擎 | 事件进 SQLite，规则变 SQL | Rust，Sigma 与自有规则 | Rust | 各自主查询语言 |
| 许可 | LGPL-3.0 | AGPL-3.0（既有报告） | GPL-3.0 | 商业 |
| 本周变化 | 离线查看包，不再是 Mini-GUI | 无对应发布 | 无对应发布 | 无 |

**已经存在的部分：** 离线跑 Sigma、把结果送进 Timesketch 或 Elastic，Hayabusa 和 Chainsaw 已经在做。SQLite 求值也是 Zircolite 原有设计，不是 4.5 新发明的检测语言。

**本期能分开的部分：** 相对已发布的 Hayabusa，它从第一天就覆盖 Linux 审计与 Sysmon for Linux，许可证是 LGPL 而不是 AGPL，4.5 把「一次调查的全部事件」封进一个不能对外联网的浏览器包。速度优势只存在于作者自己的测试设计里。

### 风险与开放问题

- 基准没有独立复现。内存换速度这句话来自项目自己的对照表。
- 默认规则集是 Sigma 目录的直接转换。文档提醒它们吵、也慢，建议自己生成规则集。直接拿上游全量规则，误报会高于「规则条数」看起来的覆盖。
- 查看包里是原始日志。发布说明要求把它当成日志本身来保存和传递。
- 它不采集、不响应。没有传感器时，它只是调查笔记本上的第二遍筛选。

---

## 5. OpenCode / Hermes 取证脚本 — 编码 agent 留在磁盘上的会话

**一句话：** SANS 讲师 Jim Clausing 于 2026-10-08 放出两个只读 Python 脚本，把 OpenCode 的 SQLite 和 Hermes 的本地状态导出成可读记录。它们是取证提取，不是检测引擎。

### 是什么

[SANS ISC 日记](https://isc.sans.edu/diary/rss/33410)（2026-10-08）说明背景：FOR577 增加了调查 Claude Code、Codex、Gemini CLI、Cursor、Copilot、Warp、Windsurf、Qwen Code 等编码助手的内容；这篇日记只交付其中两个工具的脚本，放在 [clausing/scripts](https://github.com/clausing/scripts)（BSD-3-Clause，2026-10-11 查阅约 86 stars，2026-10-08 推送）：

- `opencode-chat-replay.py`：从 OpenCode 的 SQLite 重建会话。日记给出的默认路径是 `~/.local/share/opencode/opencode.db`。脚本同时认识分开的 `message` / `part` 表和较新的 `session_message` 存储。输出 Markdown、JSON 或 JSONL。查询前把数据库连同 `-wal`、`-shm` 复制到临时目录，再以只读 URI 打开，避免碰原始证据。日记写明脚本不打开 `auth.json`，但工具调用的输入输出里仍可能有秘密。
- `hermes_forensic_extract.py`：从 `~/.hermes/state.db`、`~/.hermes/sessions/request_dump_*.json` 和 `~/.hermes/logs/*.log` 抽出会话、模型用量、API 请求体和应用日志，写成 JSONL。日记写明它以只读方式打开数据库，没有记录与 OpenCode 脚本同等的 wal/shm 快照步骤。Hermes 的 profile 在 `~/.hermes/profiles/<name>/`，可用 `--hermes-home` 指到取证镜像里的目录。

作者写明：OpenCode 脚本由 OpenCode 写成，Hermes 脚本由 Hermes 写成。两个脚本都只要 Python 3.10+ 标准库。日记强调它们暴露的是已记录下来的内容，不是「每个动作都曾被记下」的证明。

第三方存储文档能对上 OpenCode 的一半。[OpenCode 排障文档](https://opencode.ai/docs/troubleshooting/) 写明 macOS / Linux 的数据目录是 `~/.local/share/opencode/`，其中有 `auth.json`，并另有 `project/` 下的会话与消息数据。仓库源码 [db.ts](https://github.com/sst/opencode/blob/b2baddcd/packages/opencode/src/storage/db.ts) 把默认库放在该数据目录的 `opencode.db`，并执行 `PRAGMA journal_mode = WAL`。Hermes 的路径本期只有日记和脚本，没有第二份项目文档。

### 与现有格局的差异

| 维度 | 这两个脚本 | 已发布的 Hayabusa | EDR 遥测 | SIEM |
|------|------------|-------------------|----------|------|
| 证据 | 编码 agent 自己的 SQLite、请求转储和日志 | Windows EVTX | 进程、文件、网络 | 已转发的日志 |
| 问题 | 人让 agent 做了什么、agent 调了什么工具 | 主机上哪些 Sigma 命中 | 终端是否执行了恶意行为 | 跨源关联 |
| 部署 | 分析机上的只读脚本 | 分析机上的时间线工具 | 代理 | 平台 |
| 检测 | 无规则 | Sigma | 厂商内容 | 关联规则 |

**已经存在的部分：** 从应用数据库导出聊天记录，是现成的取证动作。脚本没有新的检测语言，也不监控正在运行的 agent。

**本期能分开的部分：** 证据位置从「操作系统日志」换成「编码 agent 的私有状态」，并且作者把只读、不打开 `auth.json`、工具输出仍可能含秘密写进日记。OpenCode 官方文档同时提到 `project/` 目录，所以只导出 `opencode.db` 并不等于拿全了该产品的本地痕迹。

### 风险与开放问题

- 仓库约 86 stars，作者承认脚本由被调查的同类工具生成。没有独立的模式对照测试。
- Hermes 提取器没有日记中描述的数据库快照步骤。对着正在写入的 `state.db` 做只读打开，和先复制 wal/shm 不是同一取证卫生水平。
- 导出物里可以有密钥和源代码。脚本不打开 `auth.json` 不等于导出结果可以随便传。
- 日记覆盖的是 OpenCode 和 Hermes。Claude Code、Cursor、Copilot 的痕迹不在这两个文件里。FOR577 的课程大纲不能当成这些脚本已经支持八种产品。

---

## 选题之外

- **大纲前五：** 占位仓库、2016 年 Qadium、与 CyberStrikeAI 同题的 pentest-ai、已简报过的 UTMStack 与 Xingrin。
- **今日 GitHub 高分里的进攻编排：** xalgorix（约 1,192 stars）、Pentest-Swarm-AI（约 2,817）、Raptor（约 3,890）。它们和已发布的 CyberStrikeAI 同属「把现成模型接到攻击流程」。本期不写模块和步骤。
- **AgentCorruption（Amazon Bedrock AgentCore）：** [The Register](https://www.theregister.com/security/2026/10/09/aws-agentcore-security-undone-by-prompt-requesting-credentials/5302436) 与 [Dark Reading](https://www.darkreading.com/cloud-security/agentcorruption-aws-environments-at-risk-single-prompt) 报道 Zenity 于 2026-10-08 前后公开的一组默认权限问题；AWS 在披露后收紧了新建 agent 的元数据服务和默认角色。这是已修复的云上身份配置问题，不是一家可采购的新产品。本简报不记录利用步骤。
- **Netsec（巴黎，2026-10-06 前后融资超过 $10M）：** 金额和「单一运营方」叙事目前主要来自 [Partech 稿](https://partechpartners.com/news/netsec-raises-more-than-10m-to-grow-its-ai-native-solution-for-cybersecurity-and-it) 和转载。缺少独立技术采访，本期不单列。
- **Cisco / Astrix / WideField：** 收购意向在 2026 年 5–7 月，registry 里已有 Dark Reading 条目。和已发布的 [B2B 平台安全化](../reports/2026-06-b2b-platform-security.md) 同属平台并购，不是本周事件。
- **Hadrian、RemoteThreat、Security Onion 3.3、Rustinel** 已在 10 月 8 日简报；**Tracecat、SecurityClaw、UTMStack、Steampipe、VictoriaLogs** 已在 7 月 3 日简报。

---

## 建议跟进

1. Rein 若要做成正式报告，需要一份非公司提供的部署笔记：sidecar 实际挂在哪一层、拦截日志长什么样、误拦后请求是否继续。在那之前，增长倍数和客户名单保持为公司陈述。
2. Hilt 先等第二家编辑部或一份客户技术说明。内核采集器的系统要求和隔离的撤销路径都还没出现在访谈里。
3. OSS Scanner 适合跟踪维护者事后公开的「有效 / 无效」比例，而不是 Anthropic 自测的 97 条。CIDP 只在有伙伴写出具体工单结果时再单列。
4. Zircolite 4.5 的速度表要用项目自带的 `tools/tool-benchmark.py` 在同一批 EVTX 上重跑，才能拿来和 Hayabusa 比较。查看包按日志同等敏感处理。
5. 取证脚本可以先在实验镜像上核对 OpenCode 的 `opencode.db` 与 `project/` 各有什么。Hermes 路径在出现官方存储文档之前，只把日记和脚本当成单一来源。

---

## 来源

| 来源 | 层级 | 用于 |
|------|------|------|
| [SecurityWeek：Rein $25M](https://www.securityweek.com/rein-security-raises-25-million-to-guard-ai-agents-at-runtime/) | A | 轮次、领投方、成立年份、总部 |
| [Calcalist：Rein Series A](https://www.calcalistech.com/ctechnews/article/rkf52cnimg) | A | 创始人、人数、sidecar、数据不出网关 |
| [SiliconANGLE：Rein](https://siliconangle.com/2026/10/08/rein-security-raises-25m-to-rein-in-insecure-ai-agents/) | A | 动作级拦截的 CEO 表述；客户名单为公司陈述 |
| [Rein 公司博客](https://reinsec.io/blog/series-a/) | C | 未单独采用其中的增长数字 |
| [Crunchbase News：Hilt](https://news.crunchbase.com/cybersecurity/from-ballet-to-breach-prevention-ai-startup-hilt-cielen/) | A | 独家融资、团队、内核与隔离的创始人陈述 |
| [Dealroom：Hilt](https://dealroom.co/news/160643-hilt-exits-stealth-with-4-2m-seed-to-catch-data-breaches-that-look-norma/) | B | 同一轮的数据库转记，不是第二篇采访 |
| [Hilt 平台页](https://hilt.ai/platform) | C | 元数据、浏览器扩展等未交叉的主张 |
| [SecurityWeek：OSS Scanner 与 CIDP](https://www.securityweek.com/anthropic-fast-tracks-ai-bug-reports-to-oss-maintainers-taps-11-firms-for-ot-security/) | A | 不复核、11 家 OT 伙伴名单 |
| [Help Net Security：OSS Scanner](https://www.helpnetsecurity.com/2026/10/09/anthropic-oss-scanner-ai-security-scans/) | A | 97 条样本、90 天时钟、维护者对严重性的保留 |
| [Anthropic 研究帖](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source) | C | 29,000 / 6,000、推荐语、自有测试人员的 85/97 |
| [anthropics/oss-scanner](https://github.com/anthropics/oss-scanner) | B | Apache-2.0、创建日、stars |
| [wagga40/Zircolite](https://github.com/wagga40/Zircolite) | B | LGPL-3.0、能力、作者基准 |
| [Zircolite 4.5.0](https://github.com/wagga40/Zircolite/releases/tag/v4.5.0) | B | 查看包、duckdb、1 GiB 上限 |
| [Zircolite 文档](https://wagga40.github.io/Zircolite/) | B | 输入格式与规则路径 |
| [r/blueteamsec：Zircolite 4.5](https://www.reddit.com/r/blueteamsec/comments/1x2gy3t/zircolite_45_sigma_rules_over_evtx_auditd_sysmon/) | A | 本周社区转发，非评测 |
| [SANS ISC：取证脚本](https://isc.sans.edu/diary/rss/33410) | A | 两个脚本的范围、路径、只读行为 |
| [clausing/scripts](https://github.com/clausing/scripts) | B | BSD-3-Clause 与脚本文件 |
| [OpenCode 排障](https://opencode.ai/docs/troubleshooting/) | B | 数据目录与 `auth.json` |
| [OpenCode db.ts](https://github.com/sst/opencode/blob/b2baddcd/packages/opencode/src/storage/db.ts) | B | `opencode.db` 与 WAL |
| [The Register：AgentCorruption](https://www.theregister.com/security/2026/10/09/aws-agentcore-security-undone-by-prompt-requesting-credentials/5302436) | A | 选题之外：默认权限问题已有公开报道 |
| [Partech：Netsec](https://partechpartners.com/news/netsec-raises-more-than-10m-to-grow-its-ai-native-solution-for-cybersecurity-and-it) | C | 选题之外：投资人稿，未作深度对象 |

---

*本简报依据公开 tier A/B 来源撰写。公司效果数字、客户名单与自测命中率均标明为主张。进攻性研究只保留市场或披露层面的影响，不记录操作步骤。*
