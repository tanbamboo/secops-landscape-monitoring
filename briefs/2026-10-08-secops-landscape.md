# SecOps Landscape 每周简报

**日期：** 2026-10-08（周四；覆盖周 2026-10-05 至 2026-10-11）  
**来源：** `python scripts/discover.py` 当日 inbox、`topics/registry.yaml` 未发布候选、`reports/INDEX.md`  
**本期深度介绍：** 4 项（2 家创业公司 + 2 个开源检测技术）

---

## 本周概览

本周 discovery 新增 **162** 条 inbox。registry 里按 triage score 排在最前、且尚未发布的条目，多数不适合作为本期深度对象：`sentinel-enterprise-siem-for-startups-splunk-alternative-free`（score 44）指向 `github.com/yourusername/sentinel` 占位地址；Qadium（score 43）是 2016 年 Forbes 旧闻；`0xSteph/pentest-ai`（score 40）与已发布的 [CyberStrikeAI](../reports/2026-06-cyberstrikeai.md) 同属进攻向 AI 编排；UTMStack（score 38）已写入 [2026-07-03 简报](2026-07-03-secops-landscape.md)。Xingrin（score 38）的 README 写明当前版本暂停维护、准备迁到 Go 重写，公开材料基本来自仓库自身。

本期改选 **有独立报道或现行技术文档、且不在已发布报告中** 的四项。主线是：商业侧把「外部暴露面验证」和「入侵后仿真」拆成两个产品，开源侧则继续用集成发行版和单机检测引擎补网络与终端可见性。

| # | 名称 | 类型 | 赛道 | 本期信号 |
|---|------|------|------|----------|
| 1 | Hadrian | 创业公司 | 外部攻击面 + 渗透测试 | 2026-10-06 前后再融 $40M，累计 $65M |
| 2 | RemoteThreat | 创业公司 | 授权红队 / 入侵后仿真 | 2026-09-29 出隐，pre-seed $7M |
| 3 | Security Onion 3.3 | 技术 | 网络狩猎 / NSM | 3.3.0（2026-09）；2.4 已于 2026-10-01 EOL |
| 4 | Rustinel | 技术 | 终端检测引擎 | Apache-2.0，约 501 stars，2026-10-07 仍在推送 |

---

## 1. Hadrian — 外部暴露面的持续测绘与按需渗透

**一句话：** 阿姆斯特丹创业公司把外部攻击面测绘（Atlas）和按需渗透测试（Nova）放在同一上下文里，用新一轮融资扩 EMEA 与美国。

### 是什么

[SecurityWeek](https://www.securityweek.com/hadrian-raises-40-million-to-expand-autonomous-offensive-security-platform/) 与 [Tech.eu](https://tech.eu/2026/10/06/hadrian-raises-40m-to-tackle-ai-driven-cyber-threats/) 对同一轮融资的事实一致：[Sifted](https://sifted.eu/articles/hadrian-ai-funding-round-cyber-security) 的可读导语也确认荷兰公司 Hadrian 完成 $40M、由 Forgepoint 与 SmartFin 领投。交叉后可以站住的事实是：

- 本轮 **$40M**，累计 **$65M**；联合领投 **Forgepoint Capital International** 与 **SmartFin**，跟投包括 HV Capital、Motive Partners、Picus Capital、Oetker Ventures。
- 资金用途是 EMEA 与美国扩张，以及工程和研究团队。
- 公司由 Rogier Fischer、Olivier Beg、Maurice Clin 创立。SecurityWeek 写明成立于 **2021**，Fischer 任 CEO，Beg 为 chief hacking officer。
- 产品分两块，且据 Tech.eu 报道 **共享上下文**：
  - **Atlas**：持续测绘外部攻击面，并用专用 AI agent 判断哪些暴露面可被利用。
  - **Nova**：按需的 agentic 渗透测试。
- 两家媒体都引述公司说法：人设定目标并做关键决定，agent 承担中间的重复探测。

「10 倍关键风险可见性、相对人工渗透 5 倍 ROI、修复时间缩短 80%」以及客户名单（McKesson、NBCUniversal、TotalEnergies 等）都是公司自己的数字，经媒体转述，**没有独立审计**。SecurityWeek 引用的「87% 组织仍做人工渗透、扫描结果里仅 0.47% 真正可利用」同样来自 Hadrian，不能当成行业基线。

### 与现有格局的差异

taxonomy 里漏洞与暴露面的参照物是 Tenable、Rapid7、Censys、Mandiant Attack Surface Management、Qualys。

| 维度 | Hadrian | Censys / Mandiant ASM | Qualys / Tenable | 已发布的 Sn1per |
|------|---------|----------------------|------------------|-----------------|
| 数据从哪来 | 外部暴露面持续测绘 | 互联网测绘 / 外部攻击面 | 漏洞与配置扫描 | 本机编排 90+ 现成工具 |
| 验证方式 | 公司称 agent 判断可利用性，并提供按需渗透 | 以资产与暴露发现为主 | 以扫描发现为主 | 扫描与利用链由操作者选择 |
| 交付 | 商业平台，人下达任务 | 商业订阅 | 商业平台 | 开源编排器 |
| 公开证据 | 融资与产品分层有多家媒体一致报道 | 成熟品类 | 成熟品类 | 仓库与既有报告 |

**已经存在的部分：** 外部资产发现、可利用性验证、周期性渗透，都不是新品类。Mandiant ASM、Censys 以及各类商业渗透服务已经覆盖其中几段。

**本期能分开的部分：** 公开材料把「始终在线的暴露面」和「按需渗透」做成共享上下文的两个产品名（Atlas / Nova）。这是包装与工作流上的差异。agent 是否比脚本化扫描器多做了可复核的攻击路径判断，媒体没有给出检测样例或第三方评测。

### 风险与开放问题

- 效果数字与客户名单停留在公司陈述。
- 没有公开的规则、日志或评测集，SOC 无法对照自己的暴露面数据复现 Atlas 的「可利用」判定。
- 它不替代 SIEM / EDR。检测与响应仍在现有栈上。
- 与 [Sn1per](../reports/2026-06-sn1per.md) 的差别是商业 agent 平台对开源工具链，不是同一部署形态。

---

## 2. RemoteThreat — 面向内部红队的入侵后仿真

**一句话：** 前 IBM X-Force Red 负责人创办的公司于 2026-09-29 出隐，pre-seed $7M，卖的是给已获授权的红队使用的进攻操作平台，而不是外部漏洞扫描器。

### 是什么

三家独立媒体对融资与定位一致：

- [Dark Reading](https://www.darkreading.com/cybersecurity-operations/remotethreat-bets-security-teams-need-to-test-what-happens-after-defenses-fail)（2026-10-02）：Chris Thompson（CEO）与 Shawn Jones（CTO）于 **2025** 年创立，刚以 **$7M pre-seed** 出隐。平台给企业和政府团队做任务辅助，测试防御在对手进来之后还能否成立。Thompson 对媒体说，渗透测试会变成规模化的商品市场；组织要的是自己能操作的平台，而不是只买一次外包。AI 可以接入客户自己的模型，也可以不用 AI，由人操作或人机混合。
- [The Register](https://www.theregister.com/security/2026/09/29/former-x-force-hackers-chase-the-offensive-cyber-gold-rush/5299662)（2026-09-29）：两人此前领导 IBM X-Force Red。公司称平台超出持续渗透和漏洞发现，用于计划、执行并调整进攻性网络操作。客户包括一家大银行、一家证券交易所运营方、一家美国大型医疗机构和一家领先 AI 实验室——**均为公司陈述**。访问范围据公司说限于经过审查的企业、国防承包商和美国政府客户。
- [SiliconANGLE](https://siliconangle.com/2026/09/29/remotethreat-launches-with-7m-for-an-offensive-cyber-operations-platform/)：本轮由 **Osage University Partners** 与 **DataTribe** 联合领投（仅此一家写出投资方名称）。CTO Jones 的原话是：答案不是再做一个把操作员拿掉的黑盒自动化渗透工具。

公司自称「首个商业化端到端进攻性网络操作平台」。这是营销句，三家媒体都是在转述，没有对照其他红队平台做功能审计。

本简报不展开该平台的模块、工具数量或任何绕过终端防护的做法。那些细节对防御方的选型没有帮助，也不适合写进景观简报。

### 与现有格局的差异

taxonomy 没有单列「红队平台」或 BAS。最近的参照物是检测响应里的 CrowdStrike、Cortex XDR（被检验的控制），以及暴露面里的 Mandiant ASM（外部视角）。

| 维度 | RemoteThreat | Hadrian | 传统渗透外包 | EDR / XDR |
|------|--------------|---------|--------------|-----------|
| 问题 | 防御被绕过之后，关键目标是否仍可达成 | 外部暴露面里哪些路径现在可被利用 | 约定窗口内的评估 | 终端上的检测与响应 |
| 谁在操作 | 客户自己的红队；公司称也可服务政府任务团队 | 客户安全团队设定任务 | 外部顾问 | SOC / 终端团队 |
| 公开技术证据 | 融资、创始人履历、市场定位 | 产品分层（Atlas / Nova） | 项目制 | 成熟产品 |
| 对 SOC 的直接产出 | 没有公开的检测内容或日志格式 | 暴露面与验证结果（细节未公开） | 报告 | 告警与遥测 |

**已经存在的部分：** 假设失陷、对抗仿真、把红队能力留在企业内部，都是现成需求。SpecterOps、Mandiant 等顾问公司和各类 BAS 产品已经在卖「检验控制是否真的挡住人」。

**本期能分开的部分：** 独立报道把 RemoteThreat 放在 Hadrian 的外侧：Hadrian 公开材料停留在外部暴露面与渗透；RemoteThreat 的媒体叙事是入侵之后的任务仿真，并且同一产品也被描述为卖给美国政府与国防客户。技术上新不新，目前无法从公开文档判断。

### 风险与开放问题

- **双重用途。** Register 与 SiliconANGLE 都写到：平台同时面向企业红队和美国政府 / 国防客户的进攻任务。对防御型 SOC 来说，它是控制验证市场的信号，不是检测规则来源。
- 客户名单、工具效果、「人工仍在回路中」都是公司陈述。没有第三方架构评审。
- 闭源，且访问被公司描述为资格审查制。审查强度无法从外部核对。
- 不要把它和 Hadrian 写成同一品类的两家融资新闻。一个在外，一个在假设失陷之后。

---

## 3. Security Onion 3.3 — 网络狩猎发行版，2.4 已停服

**一句话：** 仍是 Suricata、Zeek 与 Elastic 的集成发行版；当前版本 3.3.0，2.4 按项目博客已于 2026-10-01 结束支持。控制台和 Elastic 组件在官方 SBOM 里是 Elastic License 2.0。

### 是什么

[GitHub](https://github.com/Security-Onion-Solutions/securityonion) 当前约 **4,920** stars，最新发布 **3.3.0-20260911**（2026-09-11）。[3.x 文档](https://docs.securityonion.net/en/3/main/introduction/) 描述的免费检测栈是：

- **网络：** Suricata 做签名检测；协议元数据默认 Zeek，可改为 Suricata 以省 CPU；全包捕获由 **Suricata** 写盘（3.x 文档不再把 Stenographer 列为当前捕获器）；Strelka 做文件分析。
- **终端：** Elastic Agent 采集日志，并用 Osquery 做实时查询，由 **Elastic Fleet** 集中管理。这里的 Fleet 是 Elastic 的产品，不是 FleetDM。
- **分析面：** Security Onion Console 提供 Alerts、Dashboards、Hunt、Cases、PCAP 与 Detections（调 NIDS、Sigma、YARA）。可选 OpenCanary 蜜罐节点。
- **官方 SBOM**（[software-bill-of-materials](https://docs.securityonion.net/en/3/main/software-bill-of-materials/)）给出的当前主版本包括 Suricata **8.0.6**（GPL-2.0）、Zeek **8.0.10**（BSD-3-Clause）、Elasticsearch / Kibana / Logstash / Elastic Agent **9.4.5**，以及 Security Onion Console **3.3.0**。后五者在 SBOM 中的许可证都是 **Elastic License 2.0**。

[项目博客](https://blog.securityonion.net/2026/09/security-onion-330-now-available.html)（2026-09-08）把 Agent Studio、Agentic memory、Onion AI Reports 列为 **Pro** 新功能。同一页写明 **Security Onion 2.4 于 2026-10-01 EOL**。3.x 只支持 Oracle Linux 9；2.4 若不在该系统上，需要全新安装。免费文档的介绍页没有把这些 Pro 的 agent 功能写成默认检测路径。

从业者 Stefano Noferi 在 [2023 年的 2.4 笔记](https://noferi.it/en/blog/security-onion/) 里记录过：2.4 用单一 Elastic Agent 替换原先并列的 Wazuh、Beats 和 osquery，并把 Elastic 组件的许可证问题写清楚（Elastic License 2.0 / SSPL，OSI 不承认其为开源；对内 SOC 通常可用，对外提供托管服务会碰到限制）。3.3 的 SBOM 说明 Elastic 组件和 Console 仍是 Elastic License 2.0。2.4 的代理合并史不能直接当成 3.3 的升级手册。

「下载超过 200 万次」只出现在项目博客，未交叉验证。

### 与现有格局的差异

| 维度 | Security Onion 3.3 | 已发布的 Wazuh | Elastic Security | Splunk ES |
|------|--------------------|----------------|------------------|-----------|
| 重心 | 网络元数据、签名、PCAP、案件 | 终端代理 + 规则 / 合规 | 检测引擎与 SIEM | 全栈 SIEM |
| 终端 | Elastic Agent / Osquery | 自有代理、FIM、主动响应 | Elastic Defend 等 | 转发器与应用 |
| 狩猎界面 | Console 的 Hunt，可下钻 PCAP | 仪表板与规则 | Kibana / ES | SPL |
| 许可证 | 传感器多为 GPL/BSD；Console 与 Elastic 栈为 Elastic License 2.0 | GPL 系 | Elastic 商业与许可证分层 | 商业 |

**已经存在的部分：** Suricata、Zeek、Elasticsearch、Osquery、Strelka、CyberChef 都是现成项目。Security Onion 的产品是把它们收成一套可安装的网格（manager / search / sensor）和一套狩猎工单界面。检测算法本身没有被换成新模型。

**本期能分开的部分：** 相对已发布的 Wazuh，它是网络取证优先，而不是主机 XDR 优先；2.4 起就已经不再捆绑 Wazuh。3.3 新增的 agent 能力在项目自己的发布说明里属于 Pro，不应写成开源发行版已经内置自治 SOC。

### 风险与开放问题

- **2.4 已过 EOL（2026-10-01，项目博客）。** 仍停在 2.4 且不在 Oracle Linux 9 上的网格，路径是重装 3.x，不是原地小版本升级。
- Console 与 Elastic 9.4.5 均为 Elastic License 2.0。对内监控与对外 MSSP 托管不是同一件事，签约前要读许可，不能只看「free and open」这句介绍。
- Pro 的 Agent Studio / Onion AI 没有独立评测。免费栈的狩猎质量仍取决于规则、传感器摆放和 PCAP 磁盘。
- 加密流量增多后，文档自己也强调必须补终端日志。只有网络传感器时，东向西与主机行为会缺。

---

## 4. Rustinel — 本地 Sigma 终端检测引擎

**一句话：** Apache-2.0 的 Rust 代理，在 Windows / Linux / macOS 上读操作系统自带遥测，本地跑 Sigma、YARA 和 IOC，把告警写成 ECS NDJSON。它写明自己不是 EDR。

### 是什么

[GitHub API](https://github.com/Karib0u/rustinel) 核对结果：仓库 **Karib0u/rustinel**，**Apache-2.0**，约 **501** stars、62 forks，创建于 **2026-01-31**，**2026-10-07** 仍有推送，主页指向 docs.rustinel.io。描述是跨 Windows、Linux、macOS 的终端检测，Sigma / YARA / IOC，不需要云账号。

[How it works](https://docs.rustinel.io/how-it-works/) 与 [Limitations](https://docs.rustinel.io/limitations/) 把边界写在文档里，而不是放在营销页：

- **传感器：** Windows 用 ETW 与事件日志；Linux 用 eBPF（文档要求内核 5.8+ 与 BTF）；macOS 用 Endpoint Security，网络与 DNS 来自 `/dev/bpf` 抓包。**不自带内核驱动。**
- **事件模型：** 统一成 Sysmon 风格字段（如 `Image`、`CommandLine`、`TargetFilename`），便于复用已有 Sigma。
- **检测：** Sigma 与 IP / 域名 / 路径 IOC 走事件热路径；YARA 与哈希 IOC 在后台扫新可执行文件，避免拖慢 Sigma。规则热加载；加载失败则保留上一套规则。
- **输出：** 告警追加为按日滚动的 ECS NDJSON，可选 webhook。可选的主动响应是在告警达到阈值后结束进程，发生在行为之后。
- **作者自己划定的非目标：** 无反篡改、无执行前拦截、无隔离。高权限攻击者可以停掉它。macOS 支持标为实验性。突发流量下有界队列会丢事件并计数，而不是拖住主机。

配套内容仓 [Karib0u/rustinel-rules](https://github.com/Karib0u/rustinel-rules) 与引擎分开：引擎负责采集和求值，规则包负责 Sigma / YARA / IOC。文档写明 Sigma 由 RSigma 引擎求值。

公开检索没有找到独立于该项目站点与仓库的评测或生产案例。下面关于架构的句子来自仓库与文档；关于「能否替代 EDR」的判断，文档已经自己否定。

### 与现有格局的差异

| 维度 | Rustinel | CrowdStrike / Cortex XDR | 已发布的 Wazuh | 已发布的 Hayabusa |
|------|----------|---------------------------|----------------|-------------------|
| 角色 | 单机检测引擎 | 托管 EDR / XDR | 代理 + 服务端 + 索引的 XDR/SIEM | 离线 EVTX 时间线与 Sigma 狩猎 |
| 遥测 | ETW / eBPF / ESF，无自有驱动 | 厂商代理与云端 | 自有代理与解码器 | 已落地的 Windows 事件日志 |
| 规则 | 本地 Sigma、YARA、IOC | 厂商内容 + 自定义 | 自有规则与解码器 | Sigma |
| 管理面 | 无控制台；告警是文件 | 云控制台 | 仪表板与管理器 | CLI |
| 许可 | Apache-2.0 | 商业 | GPL 系 | 开源（既有报告） |

**已经存在的部分：** 用 Sigma 描述行为、用 YARA 扫文件、用 ECS 把告警送进 Elastic，都是检测工程的现成做法。Sysmon、Elastic Agent、Wazuh 已经在终端上做采集。

**本期能分开的部分：** 一个 Rust 进程把三套操作系统遥测收成同一字段模型，并在终端本地完成三类检测，而且把「没有防护、没有控制台、macOS 是实验性的」写进限制页。这和「再包一层商业 EDR」不是同一架构。它是否在真实噪声下守住误报，没有公开对照数据。

### 风险与开放问题

- 项目不满一年，stars 约 500。没有独立部署报告。
- 限制页很长，而且多处失败是静默的：平台没有对应采集器时规则会加载但永不触发；Windows 命令行在 ETW 路径上可能被截到 1024 字符；Linux 长路径截断会影响 `endswith`；默认每个事件只出一条最高严重性 Sigma 告警。检测工程若把上游 Sigma 原样丢进去，覆盖率会低于规则库看起来的数字。`rustinel doctor` 是文档给出的自查手段，尚未经第三方验证。
- 无反篡改。把它当成唯一终端控制，和文档的范围声明相反。
- 主动响应只会在事后结束进程。误报时的影响要在小范围里看，不能从 README 推断。

---

## 选题之外

- **Xingrin**（registry score 38）：MIT 开源 ASM，编排 Subfinder、Naabu、Nuclei 等现成工具。README 写明当前版本暂停维护。这是工具链包装，不是新的暴露面数据模型，且缺少独立来源。
- **Vigil**（今日 GitHub，约 353 stars，Apache-2.0）：仓库自称开源 AI SOC，用 MCP 接 SIEM/EDR。与已发布的 [AiSOC](../reports/2026-06-aisoc.md)、[Agentic SOC Platform](../reports/2026-06-agentic-soc-platform.md) 同题，且几乎只有项目自身材料，本期不单列。
- **UTMStack、Tracecat、SecurityClaw、Steampipe、VictoriaLogs** 已在 7 月 3 日简报中写过，不重复。

---

## 建议跟进

1. 若要把 Hadrian 做成正式报告，需要一份非公司提供的产品演示或客户技术笔记，用来核对 Atlas「可利用」判定是否独立于扫描器严重性。
2. RemoteThreat 保持在市场信号层。后续只跟踪独立媒体对客户与访问控制的核实，不收集其进攻模块细节。
3. Security Onion 3.3 适合作为下一份开源 NSM 报告的对象：SBOM 已经把许可证拆开，2.4 EOL 也已经到期。
4. Rustinel 适合做一次规则兼容性抽样（拿一小份公开 Sigma，对照文档里的 logsource 与 doctor），再决定是否立项。在那之前不要把它写成 EDR 替代。

---

## 来源

| 来源 | 层级 | 用于 |
|------|------|------|
| [SecurityWeek：Hadrian $40M](https://www.securityweek.com/hadrian-raises-40-million-to-expand-autonomous-offensive-security-platform/) | A | Hadrian 融资、创始人、Atlas / Nova |
| [Tech.eu：Hadrian $40M](https://tech.eu/2026/10/06/hadrian-raises-40m-to-tackle-ai-driven-cyber-threats/) | A | 同一轮融资与产品分层的交叉 |
| [Sifted：Hadrian 融资导语](https://sifted.eu/articles/hadrian-ai-funding-round-cyber-security) | A | 轮次与领投方存在；正文其余数字未采用 |
| [Hadrian 博客](https://hadrian.io/blog/hadrian-40m-raised-to-tackle-the-ai-hacking-cyber-security-crisis) | C | 公司自述，仅作主张，不作事实 |
| [Dark Reading：RemoteThreat](https://www.darkreading.com/cybersecurity-operations/remotethreat-bets-security-teams-need-to-test-what-happens-after-defenses-fail) | A | 创立年份、融资额、人机分工 |
| [The Register：RemoteThreat](https://www.theregister.com/security/2026/09/29/former-x-force-hackers-chase-the-offensive-cyber-gold-rush/5299662) | A | 创始人背景、政府与企业双重客户、访问限制主张 |
| [SiliconANGLE：RemoteThreat](https://siliconangle.com/2026/09/29/remotethreat-launches-with-7m-for-an-offensive-cyber-operations-platform/) | A | 领投方名称；「端到端平台」为公司主张 |
| [RemoteThreat 公司页](https://remotethreat.com/company) | C | 未用作事实来源 |
| [Security Onion 3.x 介绍](https://docs.securityonion.net/en/3/main/introduction/) | B | 当前传感器与 Console 工作流 |
| [Security Onion SBOM](https://docs.securityonion.net/en/3/main/software-bill-of-materials/) | B | 3.3 组件版本与 Elastic License 2.0 |
| [Security Onion 3.3.0 发布](https://github.com/Security-Onion-Solutions/securityonion/releases/tag/3.3.0-20260911) | B | 版本与日期 |
| [Security Onion 3.3 博客](https://blog.securityonion.net/2026/09/security-onion-330-now-available.html) | C | Pro 功能清单、2.4 EOL 日期、下载量主张 |
| [Stefano Noferi：Security Onion 2.4](https://noferi.it/en/blog/security-onion/) | A | 2.4 代理合并与许可证历史；不覆盖 3.3 的现行架构 |
| [Karib0u/rustinel](https://github.com/Karib0u/rustinel) | B | 许可、stars、创建与推送时间 |
| [Rustinel：How it works](https://docs.rustinel.io/how-it-works/) | B | 传感器、事件模型、输出 |
| [Rustinel：Limitations](https://docs.rustinel.io/limitations/) | B | 非 EDR、静默失败与平台缺口 |
| [Karib0u/rustinel-rules](https://github.com/Karib0u/rustinel-rules) | B | 规则与引擎分离 |

---

*本简报依据公开 tier A/B 来源撰写。公司效果数字、客户名单与「行业首个」类表述均标明为主张。进攻性产品只记录市场定位与双重用途风险，不记录操作细节。*
