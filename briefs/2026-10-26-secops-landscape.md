# SecOps Landscape 每周简报

**日期：** 2026-10-26（周一；discovery 于 2026-10-25 23:04 UTC 运行）  
**来源：** `python scripts/discover.py` 当日 inbox、`python scripts/generate_brief.py --write` 大纲、`topics/registry.yaml` 未发布候选、`reports/INDEX.md`、当周独立报道与项目文档  
**本期深度介绍：** 5 项（3 家创业公司 + 1 个厂商控制面 + 1 个检测引擎）

---

## 本周概览

本周 discovery 新增 **117** 条 inbox，跳过 **198** 条重复。RSS 取回 245 条；Hacker News 40 条全部是已有条目。GitHub 在拿到 30 个仓库后开始返回 403，后面的查询没有跑完。arXiv 仍走 `http://export.arxiv.org`，客户端没有跟随 301，本轮论文数为 0。

`generate_brief.py` 按 triage score 排出的前五名与 10 月 8 日、10 月 12 日相同，仍不适合作为深度对象：`sentinel-enterprise-siem-for-startups-splunk-alternative-free`（score 44）指向 `github.com/yourusername/sentinel`；Qadium（score 43）是 2016 年 Forbes 旧闻；`0xSteph/pentest-ai`（score 40）与已发布的 [CyberStrikeAI](../reports/2026-06-cyberstrikeai.md) 同属进攻向 AI 编排；UTMStack（score 38）已写入 [2026-07-03 简报](2026-07-03-secops-landscape.md)；Xingrin（score 38）已在 [2026-10-08 简报](2026-10-08-secops-landscape.md) 中因停更而搁置。

新 inbox 里唯一达到 high、且是一家公司而不是一条事故标题的条目，是 Mave（score 64）。Blackwall 与 Indurex 的融资稿没有进入这批 RSS 的前 15 条窗口，但有独立报道可以交叉。下面五项都 **没有对应的已发布报告**。主线是：调查 agent 接到现有安全栈上，网站流量的机器人控制卖给主机商，工业现场把工程组态和告警放进同一视图；微软则把员工带来的 agent 写成可调权限的内部人。开源侧，YARA-X 1.22.0 补上 64 位整数读取，进程内存扫描仍不在文档列出的能力里。

| # | 名称 | 类型 | 赛道 | 本期信号 |
|---|------|------|------|----------|
| 1 | Mave | 创业公司 | 现有安全栈上的调查 agent | 2026-10-22 公布，seed + Series A 合计 $34M |
| 2 | Blackwall | 创业公司 | 主机商渠道的机器人 / agent 流量 | 2026-10-20 Series C $100M，估值 $2.2B |
| 3 | Indurex | 创业公司 | 工控工程数据与安全告警 | 2026-10-22 融资 €7M |
| 4 | Microsoft Project Perception | 产品 | 内部 agent 的身份与权限 | 2026-10-19 起多家媒体报道 Guardian Agents |
| 5 | YARA-X 1.22.0 | 技术 | 文件与二进制模式匹配 | 1.22.0 于 2026-10-20 发布；SANS 日记 2026-10-25 |

---

## 1. Mave — 在现有工具里做调查，再按人工批准动作

**一句话：** 特拉维夫公司于 2026-10-22 公布合计 **$34M**（$6M seed + $28M Series A）。三家独立媒体对轮次、创始人和「查询现有安全系统、动作须人工批准」的描述一致。

### 是什么

交叉后可以站住的事实：

- [SecurityWeek](https://www.securityweek.com/former-unit-8200-officers-raise-34-million-for-agentic-secops-startup-mave/)（Kevin Townsend，2026-10-25）：2025 年成立，特拉维夫。CEO **Raziel Oren**，CTO **Guy Eshel**，两人都来自 Unit 8200。2026-10-22 公布的资金是创立时的 **$6M seed**（Dell Technologies Capital 与 Emerge Ventures 领投）加上新的 **$28M Series A**（Red Dot Capital Partners 领投，Lumir Growth Partners 跟投；seed 的两家也参加了 A 轮）。员工约 **30** 人，招聘面向市场和 AI 研究。
- [ynet](https://www.ynetnews.com/business/article/symkvnpngg)（2026-10-22 前后）：同一轮次、同一对创始人。Oren 曾是 8200 上尉，后在 Wing Security 负责进入市场；Eshel 曾是 8200 少校，Alterya 的第一名员工、后任研发副总裁，Alterya 被 Chainalysis 收购。
- [Business Insider](https://www.businessinsider.com/mave-startup-cybersecurity-funding-ai-agents-pitch-deck-2026-10)（Alice Tecotzky，2026-10-22）：两人在 8200 相识时，Oren 是 Eshel 的导师。公司对记者说，agent 从现有安全系统汇总信息、调查告警、滤掉误报，并执行人工批准的动作；按客户规模和需求收固定费用。员工 30 人，资金主要用于市场和 AI 研究。

三家对产品形状的重合部分是：agent 向客户已经有的安全系统取上下文，人可以看到推理和动作记录，自动执行停在批准过的动作上。SecurityWeek 引 Oren 的原话是：没有控制的自治本身是风险；现在提供的是最小权限集成、需要时的批准门，以及每次动作和决定的审计。ynet 补充了公司说法：记录每次调查的查询、决定和动作；在客户划定的参数内可以隔离系统或停用账户，并称已在真实事件中这样做过。Business Insider 引 Oren：有的客户需要时间才愿意把安全运营交给 agent，公司把「每一步都留下记录」当作建立信任的方式。

「调查 100% 告警、ARR 过去一年增长超过 400%、已经在签七位数合同」出现在公司通稿和 ynet 对公司的转述里。Business Insider 与 SecurityWeek 的正文没有把这些数字写成已核实业绩。公司博客上的「已在 200 个 SOC 运行」没有出现在上述三篇报道里，本期不采用。

### 与现有格局的差异

taxonomy 里 AI SecOps 的参照物是 Dropzone AI、Prophet Security，以及 Splunk / Elastic 的数据平台。自动化参照物包含 Torq。已发布的 [Nebulock](../reports/2026-06-nebulock.md) 是狩猎优先的上下文分析，[Spectrum](../reports/2026-06-spectrum-security.md) 是检测工程生命周期。上周简报里的 Rein 是放在自建 agent 执行路径上的 sidecar。

| 维度 | Mave | Dropzone / Prophet | Nebulock | Rein（10 月 12 日简报） |
|------|------|--------------------|----------|-------------------------|
| 问题 | 把现有工具里的证据合成一次调查 | 告警调查与 SOC 自动化 | 跨终端 / 身份 / 云的狩猎 | 自建 agent 这一步是否偏离基线 |
| 数据位置 | 三家媒体：向已有系统取实时上下文 | 接入 SOC 数据 | 接入已有遥测 | 公司称在客户云内 |
| 动作 | 三家媒体：人工批准后的动作；审计记录 | 调查与建议为主 | 狩猎产出 | 公司称只拦单次动作 |
| 公开证据 | 轮次与产品边界有三家编辑部 | 成熟品类 | 既有报告 | 上周简报 |

**已经存在的部分：** 用模型读告警、跨工具取证、把响应收在人的批准后面，是 Dropzone、Prophet 和各家 SOAR 已经在卖的形状。Business Insider 自己也把 Dropzone 和 Prophet 写成同一机会上的公司。

**本期能分开的部分：** 公开报道把第一产品放在「不先把数据收进一个新的库，而是用各工具自己的查询把证据拼起来」，并且三家都把动作停在批准和审计上。查询语言、连接器名单、误报怎么从记录里复核，都还没有日志样例。

### 风险与开放问题

- 400% ARR、七位数合同、真实事件中的隔离，是公司对媒体的陈述。
- 通稿里「不必采集进一个昂贵的中心库」比新闻稿的措辞更满。新闻侧能站住的是「向现有系统取上下文」，不是一份架构审计。
- 与已发布的 [以色列网络安全格局](../reports/2026-06-israeli-cyber-dominance.md) 是不同题目：那份报告写大型退出，这里是 2025 年成立、约 30 人的调查产品。
- 闭源。SOC 无法用自己的告警集复现「滤掉误报」的判定。

---

## 2. Blackwall — 卖给主机商的机器人与 agent 流量层

**一句话：** 爱沙尼亚公司（2019 年成立，曾用名 BotGuard）于 2026-10-20 宣布 Series C **$100M**、估值 **$2.2B**。TechCrunch 的采访把卖法说成主机商白标，网站客户关系留在主机商手里。

### 是什么

两家编辑部对这一轮的数字一致，产品细节主要来自 TechCrunch 对管理层的采访：

- [TechCrunch](https://techcrunch.com/2026/10/20/blackwall-quadruples-valuation-to-2-2b-as-websites-wrangle-an-increasingly-crowded-internet/)（Ram Iyer，2026-10-20）：Series C **$100M**，估值 **$2.2B**，AVP 领投，Dawn Capital、MMC Ventures、Tera Ventures 跟投。执行董事长 Roi Carthy 对记者说，估值是 2025 年上一次融资的 4 倍。CEO Nikita Rozenberg 描述的卖法是渠道：卖给主机、云和托管服务商，由他们拼装组件、自定价格、与 Blackwall 分成，再以自己的品牌提供给下游网站。免费层展示流量和威胁，防护和处置工具收费。Rozenberg 还说，公司用数字指纹识别发请求的软件（他举的例子包括 Microsoft Office 和 Codex），并用自有模型判断请求意图，用来分开「人派出的正常 agent」和恶意机器人。资金用于北美、欧洲、亚太、中东，以及给主机商的更多工具。
- [Tech.eu](https://tech.eu/2026/10/20/blackwall-hits-2-2b-valuation-with-100m-series-c-just-weeks-after-joining-estonia-s-unicorn-club/)（Cate Lawrence，同日）：同一金额、估值和投资人。稿中列出的平台范围包括机器人缓解、DDoS、WAF、负载均衡、服务端加密，以及 agent 流量管理，并写明部署在主机商自己的基础设施里。AVP 的 Warda Shaheen 称它已经是「数百万网站前面的一层」——这是投资人的话。稿中还提到一个月前爱沙尼亚 TopTech 排名曾把它放在约 €1B。12 个区域的扩张计划出现在这篇稿子里，TechCrunch 的采访只说到四大区域。

2025-03-12 的 [TechCrunch](https://techcrunch.com/2025/03/12/estonia-based-blackwall-raises-e45-million-series-b-to-protect-smbs-from-malicious-online-traffic/) 记录了更早的事实，不能当成 2026 年 10 月的经营数字：当时公司从 BotGuard 改名 Blackwall，Series B **€45M** 由 Dawn Capital 领投；旗舰 GateKeeper 被写成反向代理，实时过滤恶意请求；Rozenberg 说的渠道模式已经存在。公司当时称约 65 人、100 多家合作方、部署在超过 230 万个网站和应用上。这些是 2025 年 3 月的公司陈述。本轮报道没有给出新的员工数或经审计的网站数。

### 与现有格局的差异

taxonomy 的云与身份参照物是 Wiz、Prisma Cloud、Okta、Zscaler、Defender for Cloud。TechCrunch 把 Blackwall 放在 Cloudflare、Akamai、Imperva 同一条线上：站在网站前面处理 DDoS、爬取和机器人。这是边缘流量，不是云配置或企业身份。

| 维度 | Blackwall | Cloudflare 等边缘平台 | Wiz / Defender for Cloud | Zscaler |
|------|-----------|----------------------|--------------------------|---------|
| 卖给谁 | 采访：主机商和 MSP，再白标给网站 | 网站或企业直接购买的常见路径 | 企业云账户 | 企业流量与身份 |
| 看什么 | 采访：入站请求的软件指纹和意图 | 爬虫控制、WAF、DDoS | 云资产与配置 | 访问路径 |
| 部署 | 2025 年报道：反向代理；2026 年 Tech.eu：在主机商基础设施内 | 厂商网络或客户侧配置 | API 与扫描 | 安全服务边缘 |
| 公开证据 | 轮次有两家媒体；产品机制来自 CEO 采访 | 成熟品类 | 成熟品类 | 成熟品类 |

**已经存在的部分：** 反向代理上的机器人识别、DDoS 和 WAF 是 Cloudflare 一代产品的现成能力。TechCrunch 也写了 Cloudflare 的 AI Crawl Control：站长可以按爬虫放行、拒绝或收费。

**本期能分开的部分：** 2025 年和 2026 年的采访都把客户关系留在主机商一侧，Blackwall 分成，网站不直接成为 Blackwall 的合同方。指纹能稳定认出哪一种 agent、模型是否在主机商机器上运行，只有 CEO 的描述，没有报文样例或第三方测试。

### 风险与开放问题

- 「4 倍估值」是董事长对 TechCrunch 的话。上轮 €45M 是金额，不是上一轮估值，不能从 4 倍倒推出旧估值。
- 230 万网站、65 人、100 多家伙伴停在 2025 年 3 月的公司陈述。2026 年 10 月的「数百万网站」是投资人引语。
- GateKeeper 作为反向代理，和「模型跑在客户端点上」是两次采访里的两句话。公开材料没有说明二者怎么接在同一条请求路径上。
- 它不进入 SOC 的告警队列。检测与响应仍在现有 SIEM / EDR 上。

---

## 3. Indurex — 把工程组态和安全告警放进同一视图

**一句话：** 阿姆斯特丹公司于 2026-01 出隐，2026-10-22 公布 **€7M**（约 $7.84M）。SecurityWeek 与 Tech.eu 都把产品写成：在网络资产之外，读控制系统、安全仪表、历史库和告警系统里的工程状态。

### 是什么

出隐和本轮是两篇独立报道，中间隔了九个月：

- [SecurityWeek](https://www.securityweek.com/indurex-emerges-from-stealth-to-close-security-gap-in-cyber-physical-systems/)（Eduard Kovacs，2026-01-28）：荷兰公司出隐。CEO **Jalal Bouhdada** 创立过 Applied Risk，DNV 于 2021 年收购该公司。COO 是 **Maarten Oosterink**。当时 Bouhdada 告诉 SecurityWeek，公司在谈 pre-seed，轮次关上之前仍是自筹、团队很小。平台被写成汇集工业历史库、仪表与资产管理系统、告警管理，以及 OT 网络和终端数据，并可与第三方 OT 安全产品集成；用自适应风险分把网络、工艺和安全上下文放在一个视图里。
- [SecurityWeek](https://www.securityweek.com/indurex-raises-8-million-to-expand-industrial-cybersecurity-platform/)（Mike Lennon，2026-10-22）：标题写成 $8M，正文是 **€7M（约 $7.84M）**，Contrarian Ventures 领投，Axeleo Capital 与 Curiosity 跟投。资金用于研发，以及欧洲和中东的商业扩张，其后是美国和亚太。SafeGuard AI 分析分布式控制系统、安全仪表系统、过程历史库、告警管理和 IT 安全工具，标出工程组态、保护定值和安全功能上需要人看的偏差。早期客户被公司说成中型到跨国的能源和制造业，并在接触公用事业和数据中心。
- [Tech.eu](https://tech.eu/2026/10/22/indurex-raises-eur7m-to-strengthen-cybersecurity-across-critical-infrastructure/)（Tamara Djurickovic，同日）：同一金额和投资人。稿中引 Bouhdada：关键行业的网络防御盯着网络，Indurex 盯工程、工艺和安全信号，看装置是否还在安全限度内。AI agent 被写成从这些数据里标出异常和工程偏差，并给出建议动作。

Gartner Cool Vendor 只出现在公司通稿里，两篇新闻都没有把它当作独立奖项来核实，本期不采用。

### 与现有格局的差异

taxonomy 没有单列 OT。检测响应的参照物是 Splunk、Elastic、Sentinel、CrowdStrike、Cortex XDR，它们看的是 IT 遥测。工业现场常见的另一类产品盯网络资产和流量。SecurityWeek 1 月稿把 Indurex 放在「可以接到第三方 OT 安全产品上」，10 月稿把差距说成：传统 OT 工具常常停在已连接资产和网络活动。

| 维度 | Indurex | IT SIEM / XDR | 网络向的 OT 监控 |
|------|---------|---------------|------------------|
| 看什么 | 报道：控制系统、安全仪表、历史库、告警、IT 安全工具 | 日志、终端、身份 | 资产、会话、协议 |
| 输出 | 公司称：组态和安全功能是否偏离原意，并给建议 | 告警与案例 | 资产风险与异常流量 |
| 交付 | 商业平台；1 月时仍可与第三方 OT 产品集成 | 成熟平台 | 成熟平台 |
| 公开证据 | 出隐报道 + 本轮两家编辑部 | 成熟品类 | 成熟品类 |

**已经存在的部分：** 把工艺历史库和告警系统接进一个视图，工业监控和历史库厂商已经做了多年。OT 网络可见性也已经有专门产品。

**本期能分开的部分：** 两篇 SecurityWeek 把检测对象写成工程定值和安全功能的偏差，并把 IT 安全工具当作输入之一，而不是再做一台网络探针。自适应风险分怎么计算、和哪一家 OT 产品有现成集成，1 月的集成说法在 10 月的融资稿里没有展开。

### 风险与开放问题

- 客户范围是公司陈述。没有点名客户，也没有一份组态偏差的样例。
- 1 月说正在谈 pre-seed、团队很小。10 月的 €7M 没有披露这是不是当时那一轮、也没有披露员工数。
- 「Engineering Intelligence」是公司自己的品类名。
- 建议动作如果会碰到安全仪表或跳闸逻辑，公开材料没有写人的批准停在哪一步。在没有这份说明之前，把它写成可以自动改工艺，没有证据。

---

## 4. Project Perception — 把内部 agent 收进微软的身份和风险分

**一句话：** 2026-10-19 这一周，微软把 Project Perception 从「对付外部 AI 攻击」转向「对付企业自己在跑的 agent」。SecurityWeek、Dark Reading、TechCrunch 对功能名单一致；上线范围和定价，Dark Reading 写得最具体。

### 是什么

三家对 10 月这批控制的描述重合：

- [SecurityWeek](https://www.securityweek.com/microsoft-targets-rogue-ai-agents-with-dynamic-permissions-risk-scoring/)（Eduard Kovacs，2026-10-20）：Perception 最初面向外部 AI 攻击，现在用到企业自己的 agent。Hayete Gallot（安全业务执行副总裁）写道，前沿模型按「把任务做完」来训练，不按组织规范来训练。Nadim Abdo（身份与网络访问企业副总裁）对「内部人」的界定是：agent 可以被用户授予重要系统的访问，会犯错、被操纵或被攻破。新控制包括：Dynamic Permissions（起步无权限或最小权限，按任务授予，任务结束即收缩，高影响动作要人复核）；Dynamic Agent Risk（持续风险分，输入包括活动、身份、数据、终端、云、网络和运行时）；Dynamic Conditional Access（可只读不写、限制数据和网络、要求人批准，风险够高时隔离或停掉运行时）。Playbooks 规定响应要达成什么，Guardian Agents 去查风险为什么变了，并建议或执行遏制。本地 agent 发现再增加 35 类，合计 60 类，点名 Claude Code、OpenAI Codex、GitHub Copilot。SecurityWeek 把 Perception 的首次发布写成 7 月。
- [Dark Reading](https://www.darkreading.com/cybersecurity-operations/ai-agents-insider-threats-inside-microsoft-unified-security-stack)（Jeffrey Schwartz，2026-10-23）：首次公开预览写的是 8 月、经 Microsoft Defender；7 月的用途是漏洞管理（MDASH，仍在预览）。Abdo 对记者说，每个 agent 有独立于用户的身份，从零权限开始，只为完成用户交给的任务而升权。同一篇还写了 Entra Agent ID 可以给本来不接 Entra 的 agent 发身份，风险分吃 Entra、Defender、Intune、Purview、Sentinel 和 Global Secure Access，以及 Microsoft Execution Container：凭据和安全控制放在 agent 够不着的沙箱外面。Abdo 举的例子是报销 agent 读到隐藏指令后去碰电汇系统，风险分应上升。Guardian Agents 目前只用在微软内部和一小批选定客户，当周开始扩大到更多外部客户，随后几个月进入更宽的预览。Perception 按用量计价。它依赖 Microsoft 365 E7（目录价 $99/用户/月，含 E5、Agent 365 和 Entra Suite）提供的信号和执行点；这些新能力是否包含在 E7 里，微软没有说明。
- [TechCrunch](https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/)（Julie Bort，2026-10-19）：Gallot 的原话是前沿模型无论来自哪里都不能被信任，原因是不可预测，不是因为它们必然恶意。记者引 Satya Nadella 更早的博客：要把「智能的供应」和「对智能的授权」分开，模型厂商的保证不能代替企业自己的责任。TechCrunch 把 Perception 的首次发布写成 6 月。发现名单里除 Claude Code 和 Codex 外还写了 OpenClaw；SecurityWeek 与 Dark Reading 写的第三项是 GitHub Copilot。本期采用两家一致的三个名字。

Dark Reading 记下的外部意见：

- Forrester 的 Andras Cser：微软和第三方安全产品的集成历来不算一流；用另一个不可预测的 agent 去看着 agent，是「不确定性的平方」；这更像最小权限，还说不上最小行动权（least agency）。他认为 Blueprint Alliance 更像伙伴地图，开放标准仍缺位。他也预期这会推动客户购买更贵的套件。
- Okta 的 Harish Peri：Guardian Agents 的效果取决于它接进的整个栈，而不只是一家云。他同意要管的是授权，不是模型怎么想。Okta 自己的 Agent Gateway、Teleport 的任务结束即失效，Dark Reading 当作同一周之前已经公开的同类做法。微软不在 Okta 上月公布的 Blueprint Alliance 名单里；Abdo 的回应是 Entra 基于开放标准，参与与否仍在看。
- Suzu Labs 的 Denis Calderone：动态权限划的是 agent 能碰什么；更坏的结果可以发生在已经被授权的范围之内。Guardian Agents 自己也是权限很大的 agent。

Nadella 在 Dark Reading 描述的一场 CISO 对谈里说，Defender 这类行为监测的水平还要大幅提高，Perception 和 Agent 365 需要实战检验。

### 与现有格局的差异

| 维度 | Project Perception | Okta / Teleport（Dark Reading 的转述） | Mave（本期） | Rein（上周） |
|------|--------------------|----------------------------------------|--------------|--------------|
| 对象 | 企业里已经在跑的 agent，含员工本机上的编码 agent | agent 的身份和任务期限 | 安全告警的调查 | 自建 agent 的执行点 |
| 控制 | 独立身份、按任务授权、风险分、条件访问 | 身份与用户分离；任务结束权限消失 | 批准后的响应动作 | 公司称只拦单次动作 |
| 执行者 | Guardian Agents，外加沙箱外的凭据 | 身份产品自己的策略 | 调查 agent | sidecar |
| 堆栈 | 微软安全与身份产品上的信号 | 多家厂商的联盟或单点产品 | 客户现有安全工具 | 客户云 |
| 公开证据 | 三家媒体；分析师和竞品有引语 | Dark Reading 的对照 | 三家融资报道 | 上周简报 |

**已经存在的部分：** 把非人类身份从用户权限里拆开、按任务发短期授权、高风险动作要人批，是零信任和 PIM 的现成原则。Okta、Teleport 在这篇报道里已经被写成同一方向。

**本期能分开的部分：** 公开材料把发现、风险分和处置绑在已经部署的 Entra、Defender、Intune、Purview、Sentinel 上，并用 Guardian Agents 去解释风险分为什么变了。Cser 和 Calderone 的反对点也在这里：看守者本身是 agent，第三方信号还没有点名集成。60 类本地 agent 的检测质量没有公开样本。

### 风险与开放问题

- 首次发布的月份，三家媒体写成 6 月、7 月、8 月预览，本期不对齐成一个日期。10 月这次「转向内部 agent」是三家都在写的事件。
- Guardian Agents 在 Dark Reading 发稿时仍限于微软内部和少量客户。更宽的外部预览是路线，不是已经完成的发布。
- 按用量计价，以及是否要买 E7，微软没有说死。Cser 的「大约 $1,200/用户/年、折扣后约一半」是分析师估算。
- 与已发布的 [B2B 平台安全化](../reports/2026-06-b2b-platform-security.md) 不同：那份报告写平台通过并购把安全做进业务系统，这里是微软安全产品线里的一组预览功能。

---

## 5. YARA-X 1.22.0 — 文件模式匹配的 Rust 重写，仍不做进程扫描

**一句话：** VirusTotal 用 Rust 重写 YARA，许可证 **BSD-3-Clause**。1.22.0（2026-10-20）加上 64 位整数读取；SANS 日记于 2026-10-25 只点了这一项。官方对照页写明：API 不兼容，进程扫描还没做。

### 是什么

[GitHub](https://github.com/VirusTotal/yara-x) 2026-10-25 查阅约 **1,332** stars，语言 Rust，仓库描述是 “A rewrite of YARA in Rust”，当天仍有推送。[README](https://github.com/VirusTotal/yara-x/blob/main/README.md) 写的目标是成为恶意软件研究者的默认模式匹配工具，并最终取代 YARA。规则仍是一组字符串或字节模式加一个布尔条件。README 同时写明：经典 YARA 继续维护，后续是缺陷修复和小功能；新的大功能和模块放在 YARA-X。VirusTotal 称自己已在生产中用 YARA-X 扫过数十亿文件、数万条规则。这是作者自己的运行陈述。

[1.22.0 发布说明](https://github.com/VirusTotal/yara-x/releases)（2026-10-20）里和检测作者直接有关的条目包括：`int64`、`int64be`、`uint64`、`uint64be`，以及大于 `i64::MAX` 的整数字面量；`pe.offset_to_rva`，把 PE 文件偏移换成 RVA；C 与 Go API 可以读到匹配的 `xor_key`；编译器在规则条件过大时对生成的 WASM 函数尺寸报错，而不是继续发出去。同一版还有语言服务器的工作区符号和补全、常量折叠，以及若干整数溢出类缺陷修复。[SANS ISC](https://isc.sans.edu/diary/rss/33454)（Didier Stevens，2026-10-25）的日记只有发布本身和这四个 64 位读取函数，没有做兼容性测试。

[官方对照](https://virustotal.github.io/yara-x/docs/intro/yara-x-vs-yara/) 把差异写成项目自己的判断：

- 错误信息更完整；CLI 可以在不写规则的情况下把 PE、ELF、Mach-O、LNK 等模块输出成 YAML 或 JSON。
- 正则和复杂十六进制模式更快。页面给的例子是一条比特币地址规则：约 200MB 文件上，YARA 超过 20 秒，YARA-X 不到 1 秒；一条全文件 `uint32` 循环大约快 5–6 倍。这是项目文档里的例子，不是第三方基准。
- 解析器和编译分开，方便格式化和检查工具复用。
- C/C++、Python、Go 的 API 与经典 YARA 不兼容，要改调用方。
- 进程扫描还没做，页面把它标成低优先级。

### 与现有格局的差异

已发布的 [Hayabusa](../reports/2026-06-hayabusa.md) 和上周简报里的 Zircolite 都是把 Sigma 跑在日志上。YARA-X 回答的是另一题：这些字节在不在这个文件里。

| 维度 | YARA-X 1.22 | 经典 YARA | Hayabusa / Zircolite | EDR |
|------|-------------|-----------|----------------------|-----|
| 输入 | 文件字节；CLI 也可拆 PE / ELF / Mach-O / LNK | 文件，且支持进程内存 | Windows 事件日志等 | 终端行为 |
| 规则 | YARA 语法；项目另有一份规则级差异说明 | YARA 语法 | Sigma | 厂商规则 |
| 本周增量 | 64 位整数读取、PE 偏移换算、`xor_key` 进 C/Go API | 继续小版本维护 | 各自的日志引擎 | 不适用 |
| 进程内存 | 对照页：尚未实现 | 已有 | 不扫描进程镜像 | 常见能力 |
| 许可证 | BSD-3-Clause | BSD-3-Clause（经典 YARA） | 见既有报告 / 上周简报 | 商业 |

**已经存在的部分：** 用字节模式给恶意软件家族写规则，是 YARA 从 2010 年代就有的工作。Sigma 工具覆盖的是日志狩猎，两者本来就并列，不是替代。

**本期能分开的部分：** 1.22.0 让规则直接读 64 位整数，并把 PE 文件偏移换算放进 `pe` 模块；C 和 Go 的调用方可以拿到 XOR 键。官方对照页同时把「还不能扫进程」写成当前限制。已有的内存狩猎流水线不能靠换二进制来迁移。规则级是否逐条兼容，项目有单独文档，本期没有拿一套生产规则重编译。

### 风险与开放问题

- 「几乎总是更快」和两个计时例子都出自项目文档。存在项目自己也承认的反向情况：有的规则和文件上经典 YARA 更快。
- 「生产中扫过数十亿文件」是 VirusTotal 的自述。
- API 不兼容。把 `libyara` 的绑定换成 YARA-X，要改调用代码。
- 它不产生 SIEM 告警。要进案例流程，仍要外面的采集和工单。

---

## 选题之外

- **大纲前五：** 占位仓库、2016 年 Qadium、与 CyberStrikeAI 同题的 pentest-ai、已简报过的 UTMStack 与 Xingrin。
- **Snitch（`aixisstudio/Snitch`）：** discovery 记到约 570 stars，仓库创建于 2026-10-01。README 同时写下 SIEM 导出、Sigma 子集、Rust 代理和主机防火墙。没有独立评测，本期不把功能表当成已核实能力。
- **Sweet Security Virtual Patching（2026-10-19）：** Help Net Security 的产品周报与公司通稿一致，没有第二家编辑部的技术采访，也没有策略样例。
- **iVerify $17M（2026-10-20）：** 公司稿和 Axios Pro 的标题可以确认有这一轮；Axios 正文未能读全，移动 EDR 的采集点没有可引用的技术说明。
- **PHP、LiteLLM、Capcom：** 本周 RSS 的主体是漏洞利用和泄露事件，不是可采购的产品。本简报不记录利用步骤。
- **Artex 等被报道用于入侵的自动化测试工具：** 与已发布的 CyberStrikeAI 同属进攻编排。本期不写模块和步骤。
- **Hadrian、RemoteThreat、Security Onion、Rustinel** 已在 10 月 8 日简报；**Rein、Hilt、OSS Scanner、Zircolite、OpenCode/Hermes 取证** 已在 10 月 12 日简报。Pluto Security 的 TechCrunch 稿在 2026-10-13，主题与 Rein 的 agent 运行时重叠，留到有部署笔记再写。

---

## 建议跟进

1. Mave 若要做成正式报告，需要一份非公司提供的连接器清单和一条带查询记录的调查样例。在那之前，400% ARR 和七位数合同保持为公司陈述。
2. Blackwall 先把 2026 年的请求路径写清楚：反向代理、指纹和「端点上的模型」各在哪一跳。230 万网站不要续写成当前数字。
3. Indurex 的 €7M 与 1 月正在谈的 pre-seed 是不是同一轮，公开稿没有说。集成名单和「建议动作」的批准点也还没有。
4. Project Perception 等 Ignite 前后的预览说明：Guardian Agents 的外部范围、是否含在 E7、第三方风险事件有哪些具名伙伴。Cser 对 least agency 的保留，要用一份策略样例才能核对。
5. YARA-X 1.22 的速度要用同一批文件和同一套规则对经典 YARA 重跑。进程扫描仍缺席时，内存狩猎继续留在经典 YARA 或 EDR。

---

## 来源

| 来源 | 层级 | 用于 |
|------|------|------|
| [SecurityWeek：Mave $34M](https://www.securityweek.com/former-unit-8200-officers-raise-34-million-for-agentic-secops-startup-mave/) | A | 轮次、创始人职务、约 30 人、批准门与审计 |
| [ynet：Mave](https://www.ynetnews.com/business/article/symkvnpngg) | A | Wing / Alterya 履历；公司声称的隔离与 400% ARR |
| [Business Insider：Mave](https://www.businessinsider.com/mave-startup-cybersecurity-funding-ai-agents-pitch-deck-2026-10) | A | 导师关系、固定费用、与 Dropzone / Prophet 并列 |
| [Mave 公司博客](https://www.mave.com/resources/mave-launches-with-34-million) | C | 「200 个 SOC」未交叉，本期不采用 |
| [TechCrunch：Blackwall Series C](https://techcrunch.com/2026/10/20/blackwall-quadruples-valuation-to-2-2b-as-websites-wrangle-an-increasingly-crowded-internet/) | A | $100M、$2.2B、渠道分成、指纹与模型的 CEO 陈述 |
| [Tech.eu：Blackwall](https://tech.eu/2026/10/20/blackwall-hits-2-2b-valuation-with-100m-series-c-just-weeks-after-joining-estonia-s-unicorn-club/) | A | 同一轮次；平台模块列表；投资人引语 |
| [TechCrunch：Blackwall Series B](https://techcrunch.com/2025/03/12/estonia-based-blackwall-raises-e45-million-series-b-to-protect-smbs-from-malicious-online-traffic/) | A | 2019、BotGuard 改名、€45M、GateKeeper、2025 年 3 月的经营数字 |
| [SecurityWeek：Indurex 出隐](https://www.securityweek.com/indurex-emerges-from-stealth-to-close-security-gap-in-cyber-physical-systems/) | A | 创始人、Applied Risk / DNV、2026-01 的数据源 |
| [SecurityWeek：Indurex €7M](https://www.securityweek.com/indurex-raises-8-million-to-expand-industrial-cybersecurity-platform/) | A | 金额与约合美元、SafeGuard AI 的输入、客户陈述 |
| [Tech.eu：Indurex](https://tech.eu/2026/10/22/indurex-raises-eur7m-to-strengthen-cybersecurity-across-critical-infrastructure/) | A | 同一轮；CEO 对工程信号的表述 |
| [Indurex 通稿](https://www.prnewswire.com/news-releases/indurex-raises-7-million-to-bring-engineering-intelligence-to-critical-infrastructure-and-industrial-operations-302916960.html) | C | Gartner Cool Vendor 未交叉，本期不采用 |
| [SecurityWeek：Project Perception](https://www.securityweek.com/microsoft-targets-rogue-ai-agents-with-dynamic-permissions-risk-scoring/) | A | 动态权限、风险分、条件访问、60 类 agent |
| [Dark Reading：Project Perception](https://www.darkreading.com/cybersecurity-operations/ai-agents-insider-threats-inside-microsoft-unified-security-stack) | A | 预览范围、用量计价、E7、Cser / Peri / Calderone |
| [TechCrunch：Project Perception](https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/) | A | Gallot 与 Nadella 的授权分离表述；首次发布月份与另两家不一致 |
| [微软安全博客](https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/) | C | 厂商对四项职责的自述；结论以三家新闻为准 |
| [VirusTotal/yara-x](https://github.com/VirusTotal/yara-x) | B | BSD-3-Clause、约 1,332 stars、取代 YARA 的目标 |
| [YARA-X 1.22.0 发布说明](https://github.com/VirusTotal/yara-x/releases) | B | 64 位整数、`pe.offset_to_rva`、`xor_key`、WASM 尺寸限制 |
| [YARA-X vs YARA](https://virustotal.github.io/yara-x/docs/intro/yara-x-vs-yara/) | B | API 不兼容、无进程扫描、文档内的速度例子 |
| [SANS ISC：YARA-X 1.22.0](https://isc.sans.edu/diary/rss/33454) | A | 2026-10-25 日记确认发布与四个 64 位读取函数 |

---

*本简报依据公开 tier A/B 来源撰写。公司效果数字、客户名单与自有基准均标明为主张。进攻性研究只保留披露层面的影响，不记录操作步骤。*
