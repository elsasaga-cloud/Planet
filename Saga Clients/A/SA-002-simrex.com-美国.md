# simrex.com
**官方名称（调研核实）**：SIMREX Corporation（Buffalo, NY）

> **评级 A**　|　美国　|　档案编号 `SA-002`　|　优先级 ★★★　|　状态：有回复·跟进中
>
> **类型**：品牌商/贴牌需求（OEM/ODM）——工业无线厂商自有品牌加固交换机（推断）　|　**历史关系**：实质回复 1 次；推送 11 次（2025-02-08 → 2025-11-28）　|　**所在清单**：S重点　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SA-002
rating: A
rating_auto: A
name_official: "SIMREX Corporation（Buffalo, NY）"
score: 88
country: 美国
region: 北美
website: simrex.com
type: 品牌商/贴牌需求（OEM/ODM）——工业无线厂商自有品牌加固交换机
tier_tags: ["S重点"]
deal: no
replies: 1
followups: 11
first_contact: 2025-02-08
last_contact: 2025-11-28
s_mail: 32 msgs (out 25 / in 7), 2024-12-04 -> 2026-09-08
p1: STI-288DGGPM
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-21
sources: 1
updated: 2026-10-27
```

## SALES BRIEF（压缩模型）

- **是谁**：美国纽约州 Buffalo 的工业无线数据通信设备制造商（1996 年成立，11–50 人，收入 $1–4.9M），品牌 ARIA Wireless / GLB Electronics / SIMREX；产品线含 DataMover 无线电台与 **DataMover 加固型管理交换机 MS-5 / MS-5GS / MSG-8E4S**（贴自有品牌的工业交换机）；行业：航空、轨道、能源、水务、交通 ITS。已成单。（调研 2026-10-21；表内兴趣：switch）
- **为什么是 A 级**：+22 实质回复 1 次；+25 在 Simon 的 S 重点名单；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国；+5 最近活动 2025；+5 跟进表最近平台标记 S
- **历史互动**：实质回复 1 次；推送 11 次（2025-02-08 → 2025-11-28）；最近一次客户回复：1.3：L3管理 后续未下单
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：Simon 2026-07-21 已报的 130 USD Marvell 24 口（附件 STC-424XGGM.docx + Saga Feature List 7.5.x + Dual AC.jpg，即 STC-424XGGM 24 GE + 4×10G SFP+ L2+，对标 CRS326-24G-2S+RM）+ OID/MIB 清单（PI 包里有 NMS-MIB-7.4.7 OID 文件，德国 Frederik 用过） — J6：把「能不能进你的 NMS」变成可测问题，先给 OID 列表再谈价｜已发资料（勿重发）：A copy of reply(2024-12-06)、L3 PoE(2024-12-13)、Saga Software Function List-release 7.(2025-03-28)、Product Link_2026Q2(2026-03-02)、Saga Feature List_7.5.x_L2+(2026-06-22)、STC-424XGGM(2026-07-21)；还没给过：Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）；130 USD/PC 单 AC（2026-07-21 报价；复核汇率与 30% 档）；历史报价（邮件原话，老汇率）：2024-12-05 ；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2025-04-28 $300（48 Port PoE Managed Switch）、2025-08-27 $240（24 Port Fiber Switch）、2025-10-30 $280（10G Enterprise SFP Switch）、2026-09-08 $170（24 Port PoE Managed Switch）；群发里他已看到的价（续，第 66 批全量复核）：2026-07-20 $1500（24 Port 10G SFP+ Switch）；2026-07-21 Simon 已报 **STC-424XGGM 单 AC $130**（对标 CRS326-24G-2S+RM $209 MSRP / 他的 OEM 成本 $90–120 是 6/12 口 MT）——再谈只能守 $130，不再往下（主表 LT-S8328XG-4XS24GT-S CNY 710 → $127.4 / $132.7 / $138.0，上限 $143：$130 ≈ 分销档，已是底）
- **第一问（只问一个）**：Did the 130-USD Marvell unit get a lab slot? If your NMS only needs SNMP discovery + port stats, I can send the OID list first.
- **最大未知**：年走量与现供应商
- **下一步**：2026-11 WhatsApp（Simon） 问 130 USD 款是否排进实验室；主动给 SNMP OID/MIB 文件

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SA-002` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度（用户表「已成单 switch」；邮件无 PI——2024-12-05 起转 WhatsApp，成交细节不在邮箱；Elsa 箱：`to:simrex.com` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 25 / 来 7）（第 74 批(g)））** ｜ 类型：美国工业无线品牌商（DataMover），自有品牌加固交换机 = 目前贴 Mikrotik（6/12 口，成本 $90–120 含加固外壳，自建云 NMS 调 Mikrotik API） ｜ 筛子：2–3 ｜ 停点：Mikrotik 锁定：2026-07-20 Frank「We have built a cloud NMS using the API… custom scripting and product validity certificate… Is there something that your switch does that MT does not do?」；Saga 1,500 USD CENTEC 10G 被拿去比 CRS326 $209/$289 ｜ 复活：Saga 交换机能被其 NMS 发现/诊断（SNMP/CLI/OID）——固件侧问题；Simon 2026-07-21 已给 130 USD 的 Marvell 对位款（同 CRS326 档），等 Frank 测 ｜ 通路：US；WhatsApp 为主（2024-12-05 起） ｜ 节奏：2024-12 → 2026-09 去信 25 封；最后实质来信 2026-07-20 ｜ 证据：k=95d30a86d792cc0d / d83e2c902092c388 / a5829330c3f7b38f / 5ad38241fd821cfe / 06610cfbde4173c3；第 19 批回补来信原文 2 条（gmail_s/gmail_a）
- **现状一句话**：Frank Neuperger 2024-12 一周内连问 5 封（管理？OS？每口功率？250 m 怎么跑以太网？56V 行不行？「Do you work for Saga Telecom?」），Simon 答「Saga Telecom is my sister's… 56V OK」后转 WhatsApp；用户表记成单。2026-07-20 Frank 的长信是 A 级里最有信息量的一封：他们私标 Mikrotik、靠 API 做云 NMS 和脚本增值、成本 90–120 美元，问 Saga 交换机能做什么 MT 做不到的。Simon 次日给了 130 USD 的 Marvell 24 口（与 CRS326 同级）。
- **对方真实需求（有据）**：6/12/24 口加固管理交换机，能进其 NMS（API/SNMP 发现 + 吞吐测试），56V PoE，成本 ≤$120 级。
- **断点 / 为什么停在这里**：客户系统依赖的是 Mikrotik 固件（J 系列「客户系统依赖固件」反向案例）；Saga 想替代就得在固件侧给出等价接口，不是价格。
- **Saga 现在该推什么**：P1 **Simon 2026-07-21 已报的 130 USD Marvell 24 口（附件 STC-424XGGM.docx + Saga Feature List 7.5.x + Dual AC.jpg，即 STC-424XGGM 24 GE + 4×10G SFP+ L2+，对标 CRS326-24G-2S+RM）+ OID/MIB 清单（PI 包里有 NMS-MIB-7.4.7 OID 文件，德国 Frederik 用过）**（30% 档，130 USD/PC 单 AC（2026-07-21 报价；复核汇率与 30% 档）；历史报价（邮件原话，老汇率）：2024-12-05 ；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2025-04-28 $300（48 Port PoE Managed Switch）、2025-08-27 $240（24 Port Fiber Switch）、2025-10-30 $280（10G Enterprise SFP Switch）、2026-09-08 $170（24 Port PoE Managed Switch）；群发里他已看到的价（续，第 66 批全量复核）：2026-07-20 $1500（24 Port 10G SFP+ Switch）；2026-07-21 Simon 已报 **STC-424XGGM 单 AC $130**（对标 CRS326-24G-2S+RM $209 MSRP / 他的 OEM 成本 $90–120 是 6/12 口 MT）——再谈只能守 $130，不再往下（主表 LT-S8328XG-4XS24GT-S CNY 710 → $127.4 / $132.7 / $138.0，上限 $143：$130 ≈ 分销档，已是底））——J6：把「能不能进你的 NMS」变成可测问题，先给 OID 列表再谈价｜已发资料（勿重发）：A copy of reply(2024-12-06)、L3 PoE(2024-12-13)、Saga Software Function List-release 7.(2025-03-28)、Product Link_2026Q2(2026-03-02)、Saga Feature List_7.5.x_L2+(2026-06-22)、STC-424XGGM(2026-07-21)；还没给过：Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）
  - 做不了 / 要先核的：2026-07-21 报价型号已核实 = STC-424XGGM（24×GE + 4×10G SFP+，L2+，非 PoE，附 Feature List 7.5.x L2+ + 双 AC 照片）$130 单 AC——对标他自报的 CRS326-24G-2S+RM $209 MSRP；WhatsApp 成交内容未入库——成单型号/数量不明
- **下一步（具体）**：2026-11　WhatsApp（Simon）　问 130 USD 款是否排进实验室；主动给 SNMP OID/MIB 文件
  - 第一问（只问一个）：Did the 130-USD Marvell unit get a lab slot? If your NMS only needs SNMP discovery + port stats, I can send the OID list first.

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-12-04 | 来 | Frank Neuperger | Is this a managed switch? If so, what operating system? What is max power per port?… With the specified 250 m POE distance, how do you get ETH connectivity? | 工程师式追问 | `95d30a86d792cc0d` |
| 2024-12-05 | 来 | frank@simrex.com | Simon: 1. Can you answer the questions in my email below? 2. Provide a link to data sheet?. 3. Link to your web page? 4. Pricing? Regards Fank Frank N | 来信原文（主题「RE: Industrial PoE Switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `beb1989d2b8314a0` |
| 2024-12-05 | 去 | Saga（Simon） | Hi, Frank, Please check this google drive link, there are many other models available. *https://drive.google.com/drive/folders/1PKhmEboNZkl105nBUotOBcTBrH9qX6EU?usp=drive_link* <https://drive.google.com/drive/folders/1PKhmEboNZkl105nBUotOBcTBrH9qX6EU?usp=drive | 历史报价点（主题「Re: Industrial PoE Switch」；第 20 批从 gmail_s 回补）： | `b5564e71079c9744` |
| 2024-12-05 | 内 | Gmail 退信（S 邮箱） | frank@simrex.com 邮箱满（暂时性）：552 5.2.2 User's mailbox is full | 该地址当时收不到信，之后若无再发成功记录就别再往这个地址发 | `gmail_s a664a09affcd2944` |
| 2024-12-06 | 来 | Frank | Do you work for Saga Telecom? Can we use 56V with any of the products… Most of our POE is 56V. | 身份 + 56V | `d83e2c902092c388` |
| 2024-12-07 | 去 | Simon | Saga Telecom is my sister's. I deal with foreign trade only… 56V is OK. For PoE models, the max input is 57V | 身份口径（历史） | `a5829330c3f7b38f` |
| 2024-12-12 | 来 | frank@simrex.com | Simon, I will see what I can learn from your web site. Do any of your POE switches have layer 3? VLAN, IGMP etc. Frank Frank Neuperger Simrex Corporat | 来信原文（主题「RE: Industrial PoE Switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `19b86efa448c3a2c` |
| 2026-07-20 | 来 | Frank | we currently use Mikrotik… We have built a cloud NMS using the API… Our cost $90 to $120 including hardened metal packaging… your $1500 pricing is at least 5x… Is there something that your switch does that MT does not do? | 锁定与成本基准 | `5ad38241fd821cfe` |
| 2026-07-21 | 去 | Simon | We have this model… similar to Mikrotik model. Both are Marvell based… Price is 130USD/PC for single AC input.  [附件：STC-424XGGM.docx、Saga Feature List_7.5.x_L2+.xlsx、Dual AC.jpg → 报的是 STC-424XGGM 单 AC $130；双 AC 版可做] | Saga 对位；型号 = STC-424XGGM（2026-10-24 从附件名核实） | `06610cfbde4173c3` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：成单仅见用户表，PI 包无 Simrex；SmartByte 规划 2027 出 EN50155 系列（其轨道应用）——但轨交 PASS 口径不变

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **时机与节律**：真人来信 5 封（2024-12-04 → 2026-07-20）；多在 12 月（4）；对方本地时间中位 14:36，四分位 12:18–16:18（= 北京时间 03:36）；周四最多（2）；**他们回信中位 4.8 小时**（4 次，100% 在 24 小时内）；我方回信中位 6.9 小时（5 次）。
- **发信窗口（US 全库 2491 封群发的打开标签，对方本地时间；均值 5.4%）**：周三 08–10 点 13.6%（44 封）、周二 08–10 点 11.1%（63 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 16 封（2025-01-03 → 2026-09-08），打开标签 5 次（近 12 个月 1，最后 2026-07-20）；打开过：「Industrial PoE Switch」×1（2025-01-03）、「Marvell Alleycat5 Solution」×1（2025-03-28）、「48 Port PoE Managed Switch」×1（2025-04-28）、「24 Port Fiber Switch」×1（2025-08-27）；从未打开：「Marvell Industrial Alert System」、「16 Port Ethernet Switch」、「Managed Optical Bypass Switch」；近 180 天发 3 封、打开 1 次 → 还在读，主题沿着打开过的那类走。
- **报价轨迹**（S/A 去信里「价 + 型号/描述同句」：1:1 2 条 + 个性化群发价 5 条，2024-12-05 → 2026-09-08；「今天」= 价格主表 2026-10-17 汇率、30% 档、不高于 2026-06 列表价；只列每个型号/描述最近一次，最多 8 行）：

  | 日期 | 型号 / 原句 | 当时 | 今天应报 | 变化 | 性质 | 主题 | 消息 key |
  |---|---|---|---|---|---|---|---|
  | 2026-09-08 | 「Price: 170USD/PC」 | $170 | —（原句无型号） | — | 群发价 | 24 Port PoE Managed Switch | `935007727c3ea96f` |
  | 2026-07-21 | 「Price is 130USD/PC for single AC input.」 | $130 | —（原句无型号） | — | 1:1 | 24 Port 10G SFP+ Switch | `06610cfbde4173c3` |
  | 2026-07-20 | 「Price: 1500USD/PC」 | $1500 | —（原句无型号） | — | 群发价 | 24 Port 10G SFP+ Switch | `e44ed147f5c2bbb7` |
  | 2025-10-30 | 「It is a price-competitive aggregation switch(280usd/pc)」 | $280 | —（原句无型号） | — | 群发价 | 10G Enterprise SFP Switch | `959981a7454f2b8d` |
  | 2025-08-27 | 「Price: 240usd/pc」 | $240 | —（原句无型号） | — | 群发价 | 24 Port Fiber Switch | `64ef9b106ddf943c` |
  | 2025-04-28 | 「Price is very competitive, 300usd/pc」 | $300 | —（原句无型号） | — | 群发价 | 48 Port PoE Managed Switch | `95cec6bd97cfe34e` |
  | 2024-12-05 | STI-154GP | $38 | $40.8 | +7% | 1:1 | Industrial PoE Switch | `b5564e71079c9744` |

  涨的部分只有一个口径：汇率 7.2 → 6.7（成本按人民币不变）；对方若拿旧价压，先认旧价有效期已过，再谈量；「个性化群发价」= 同一句价发给 ≥5 家的信（Simon 的手工群发），对方未必读过，但它就是对方邮箱里躺着的「上次报价」。
- **规模与贴牌线索（官网快照 2026-10-21）**：社媒：http://www.simrex.com/site/apps/traffic.htm、http://www.simrex.com/site/compinfo/contact.htm、http://www.simrex.com/site/index.htm。
- **关联户**：SB-1026 epygi.com（B；同一封邮件）——写信前看一眼对方档案，别两边说两套价。
- **写信的人（来信签名机械抽取）**：Frank Neuperger（frank@simrex.com，5 封，2024-12-04 → 2026-07-20）。
- **他们嘴里的词（5 封来信、去引用后 2,866 字符的词频）**：话题（次数，最近一次）：价格 / 折扣 ×5（2026-07-20）、PoE ×4（2026-07-20）、管理型 / L2+ / L3 ×3（2024-12-12）、固件 / 软件 ×3（2026-07-20）、贴牌 / OEM ×2（2026-07-20）、工业 ×1（2026-07-20）；**提到的同行品牌**：MikroTik ×2（2026-07-20）。
- **最后一球**：1:1 对话 2 段，最长一段 12 封 / 跨 65 天（2024-12-04 → 2025-02-07，「RE: Industrial PoE Switch」）；最后一句是我们说的（2026-07-21，97 天前，「Re: 24 Port 10G SFP+ Switch」，`06610cfbde4173c3`）→ 球在对方手里；按他们过去中位 4.8 小时回信（4 次），这次 97 天没回 ≈ 常态的 485 倍 → **值得追一句**（不是催，是换个问法）。
- **同国同档参照（US，30% 档，共 8 户有动静，列前 3）**：SB-831 actelis.com（B，同档：回过 6 次（最近 2026-03-02），1:1 报过 1 次）；SB-826 versitron.com（B，同档：回过 20 次（最近 2025-10-31），1:1 报过 4 次）；SB-085 DIGI Group（B，同档：回过 3 次（最近 2025-11-28），1:1 报过 1 次）。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-11-26 感恩节（周四–周日四天基本停摆）；2026-12-24 圣诞–元旦（12-24 → 01-04 多数公司半停） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | simrex.com（取自域名，公司全名待核） | 推断 |
| 国家 | 美国 | 事实（用户表）|
| 网站/域名 | simrex.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 品牌商/贴牌需求（OEM/ODM）——工业无线厂商自有品牌加固交换机 | 推断（据兴趣/备注关键词） |
| 联系人 | Frank Neuperger | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | switch | 事实（用户表） |
| 用户备注（Remark） | 邮件中有详细的联系信息 | 事实（用户表） |
| 所在清单 | S重点 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：美国纽约州 Buffalo 的工业无线数据通信设备制造商（1996 年成立，11–50 人，收入 $1–4.9M），品牌 ARIA Wireless / GLB Electronics / SIMREX；产品线含 DataMover 无线电台与 **DataMover 加固型管理交换机 MS-5 / MS-5GS / MSG-8E4S**（贴自有品牌的工业交换机）；行业：航空、轨道、能源、水务、交通 ITS。已成单。
- **类型**：品牌商/贴牌需求（OEM/ODM）——工业无线厂商自有品牌加固交换机
- **规模**：11–50 人；$1–4.9M 营收（Crunchbase / Thomasnet）
- **在卖/在用品牌**：ARIA Wireless, GLB Electronics, DataMover
- **【第三方（Crunchbase）】产品线含自有品牌加固管理交换机 MS-5/MS-5GS/MSG-8E4S，与其无线电台配套——正是 OEM 工业交换机需求**
  > DataMover Managed Switches (MS-5, MS-5GS, MSG-8E4S) Hardened managed Ethernet switches with multiple ports, VLAN support, and diagnostics, designed to integrate with DataMover WB radios … Buffalo, New York … 11-50
  > 来源：https://www.crunchbase.com/organization/simrex（抓取 2026-10-21）
- **【官网】公司自述：工业无线数据通信制造商，服务航空/轨道/能源/水务/交通**
  > A wireless data communications equipment manufacturer for mobile and stationary wireless networks … Industries served: Aviation, Rail, Energy, Water/Wastewater, Traffic/ITS.
  > 来源：http://www.simrex.com/site/（抓取 2026-10-21）
- **【第三方（Thomasnet）】体量：制造商，$1–4.9M 营收**
  > SIMREX Corporation Buffalo, NY 14206 Manufacturer* ⚫$1 - 4.9 Mil Revenue
  > 来源：https://www.thomasnet.com/suppliers/usa/null-52091287（抓取 2026-10-21）
- **【官网】DataMover 交换机型号与规格（MS-5、MS-5GS、MSG-8E4S）**
  > DATAMOVER MS-5GS - Hardened Gigabit Managed Switch Supported by SIMREX CRMS NMS … Five 10/100/1000 Mbit/s … DATAMOVER MSG-8E4S - Hardened Gigabit Managed Switch … Eight 10/100/1000 Mbit/s … Supports 802.3af/at devices if the 48-57VDC input is used. Max current 450mA per port
  > 来源：https://www.simrex.com/site/apps/traffic.htm（抓取 2026-10-21）
- **KP**：Frank Neuperger（General Manager（RocketReach 口径））frank@simrex.com +1 716-206-0174（总机）〔https://rocketreach.co/frank-neuperger-email_64101596 ; https://cage.report/DUNS/087787573；S 邮箱 2024-12 来信表头 4 封〕
- 备注：A 级确认：自有品牌加固交换机 = 最优 OEM 客户类型；注意其应用含轨道/ITS，Saga 无 EN50155，只按 DIN 工业 L2+ 对位。

### 加厚挖掘（2026-10-21 · 深挖 v1）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | SIMREX Corporation |
| 成立 | 1996 |
| 总部/地址 | Buffalo, New York, USA |
| 人数 | 11–50 |
| 营收 | $1–4.9M（Crunchbase） |
| 其他 | 品牌 DataMover / ARIA Wireless / GLB；交换机与自家 CRMS NMS 配合；客户为交通 ITS、水务、能源、航空、轨道 |

- **业务线**：DataMover 工业无线电台（900 MHz/2.4 GHz，PtP/PtMP/mesh）；DataMover 加固管理交换机 MS-5 / MS-5GS / MSG-8E4S（贴牌）；DataMover WB 以太网桥接延长套件（400 m，48V PoE 25W）

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| SIMREX DataMover | MS-5GS | 加固千兆管理 5×GE，VLAN/IGMP/RSTP，CRMS NMS 支持，2A 总电流 | STI-144GP（管理型待核） | https://www.simrex.com/site/apps/traffic.htm（2026-10-21） |
| SIMREX DataMover | MSG-8E4S | 加固千兆管理 8×GE（+4 SFP 按型号名），802.3af/at（48–57VDC 输入时），450mA/口 | STI-288DGGPM | https://www.simrex.com/site/apps/traffic.htm（2026-10-21） |
| SIMREX DataMover | MS-5 | 加固 5 口百兆管理，PoE 500mA/口 | STI-144GP | https://www.simrex.com/site/apps/traffic.htm（2026-10-21） |

- **触达通道（公开）**：网站: https://www.simrex.com/（Product Inquiry Form）；直邮: frank@simrex.com（Frank Neuperger，cage.report 公开）/ sales@simrex.com
- **近况信号**：
  - 交通页（traffic.htm）仍列 MS-5/MS-5GS/MSG-8E4S 全系——交换机为其 ITS 方案的固定组成（2026-10-21）
  - 用户表：已成单（switch）
- **风险/边界**：ITS/交通控制 = 美国公共项目，常要求 NEMA TS2 与 Buy America——Saga 无 UL/NEMA，仅供其商业/私营项目或按客户自担认证；轨道客户部分守界（不做 EN50155）
- **Saga 对位结论**：P1 STI-288DGGPM（30% 档）——MSG-8E4S（8 GE PoE + SFP 加固管理）对位 STI-288DGGPM，MS-5GS 对位 STI-144GP；DataMover 贴牌 30% 档；要求与 CRMS NMS 兼容的 SNMP 口径
- **邮件切入句（英文）**：For the MSG-8E4S slot in your DataMover line, the Marvell-based 8-port gigabit PoE managed DIN switch with SNMP for CRMS polling is the unit I can supply in DataMover packing, so that is what I am quoting first.

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：http://www.simrex.com/site/　语言：未标　站点地图 URL 数：0
- **标题**：SIMREX Corporation
- **描述**：A wireless data communications equipment manufacturer for mobile and stationary wireless networks and monitoring / tracking applications.
- **首页栏目**：Wireless Data Solutions
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：wireless 6、industrial 1、ethernet 1
- **站内型号串**（正则抽取，含非交换机）：RS-232, RS485
- **社媒**：http://www.simrex.com/site/apps/traffic.htm, http://www.simrex.com/site/compinfo/contact.htm, http://www.simrex.com/site/index.htm, http://www.simrex.com/site/products/broadband.htm, http://www.simrex.com/site/products/choosing.htm, http://www.simrex.com/site/products/custom.htm
- 首页正文摘录：Wireless Data Solutions SIMREX Corporation serves industries requiring secure and reliable wireless data communications for vital systems under the toughest of conditions. Industries served: Aviation, Rail, Energy, Water/Wastewater, Traffic/ITS. Can't find the product you need? Do you have a custom application? Simrex engineers pride themselves in providing exactly what you need. Here's what we can do for you..... An
- 数据文件：`data/saga_clients/site_snapshots/SA-002.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 11 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-02-08 | 2025.2.8 | 2 16 |  | S |  | S 09.08.xlsx#10 |
| 2025-03-28 | 328 | 芯片 |  | S |  | S 09.08.xlsx#10 |
| 2025-04-29 | 429 | 48口 |  | S |  | S 09.08.xlsx#10 |
| 2025-05-27 | 527 | alarm |  | S |  | S 09.08.xlsx#10 |
| 2025-06-26 | 626 | 16电 |  | S |  | S 09.08.xlsx#10 |
| 2025-07-29 | 729 | bypass |  | S |  | S 09.08.xlsx#10 |
| 2025-08-28 | 828 | 24fiber |  | S |  | S 09.08.xlsx#10 |
| 2025-09-29 | 929 | 22迷你 |  | S |  | S 09.08.xlsx#10 |
| 2025-10-30 | 1030 | dac |  | S |  | S 09.08.xlsx#10 |
| 2025-11-28 | 1128 | solar |  | S |  | S 09.08.xlsx#10 |
| ? | 1.3 | 24poe | L3管理 后续未下单 | Email |  | S 09.08.xlsx#10 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：32 封（去 25 / 来 7）　|　**期间**：2024-12-04 → 2026-09-08　|　**最后去信**：2026-09-08
- **对方邮箱**：frank@simrex.com、maquilino@simrex.com、sales@simrex.com、sktona@simrex.com
- **最后一封来信**：2026-07-20 frank@simrex.com「RE: 24 Port 10G SFP+ Switch」：Simon , we currently use Mikrotik. We like the scripting and the powerful features. Our value added is the custom scripting and product validity certificate. We have built a cloud NMS using the API. We use 6 and 12 port models. Our cost $90 to $120 including h
- **邮件里报过的价**：2026-09-08 $170；2026-07-21 $130；2026-07-20 $1500；2025-10-30 $280；2025-08-27 $240；2025-04-28 $300；2024-12-05 $38（STI-154GP）

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 24 Port PoE Managed Switch | 2026-09-08 | 2026-09-08 | 0 | 1 | 1 |
| 24 Port 10G SFP+ Switch | 2026-07-20 | 2026-07-21 | 1 | 2 | 6 |
| Firmware 7.5 L2+ Feature Update | 2026-06-22 | 2026-06-22 | 0 | 1 | 2 |
| Updated Ethernet Switches Links | 2026-03-02 | 2026-03-02 | 0 | 1 | 1 |
| OEM Core Switching Solution | 2026-01-29 | 2026-01-29 | 0 | 1 | 1 |
| Optional Marvell Chipset Solutions | 2025-12-29 | 2025-12-29 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-28 | 2025-11-28 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-30 | 2025-10-30 | 0 | 1 | 1 |
| Mini Industrial PoE Switch | 2025-09-29 | 2025-09-29 | 0 | 1 | 1 |
| 24 Port Fiber Switch | 2025-08-27 | 2025-08-27 | 0 | 1 | 1 |
| Managed Optical Bypass Switch | 2025-07-29 | 2025-07-29 | 0 | 1 | 1 |
| 16 Port Ethernet Switch | 2025-06-25 | 2025-06-25 | 0 | 1 | 1 |
| …共 17 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：A 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-26T07:56:19Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SA-002/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](http://www.simrex.com/site/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 1954 字符；首行：SIMREX Corporation |

## 联系方式（已有 · 原值照录）

- 邮箱：`frank@simrex.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`sales@simrex.com`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Frank Neuperger
- 网站/域名：simrex.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Frank Neuperger | General Manager（RocketReach 口径） | frank@simrex.com / +1 716-206-0174（总机） | 调研核实（公开页） | https://rocketreach.co/frank-neuperger-email_64101596 ; https://cage.report/DUNS/087787573；S 邮箱 2024-12 来信表头 4 封 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| S 09.08.xlsx#总表:11 | 10 | https://www.simrex.com/site/apps/traffic.htm | 美国 | Frank Neuperger | 谷歌 | switch | frank@simrex.com<br>sales@simrex.com | 邮件中有详细的联系信息 | 11 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-288DGGPM | 深挖对位：MSG-8E4S（8 GE PoE + SFP 加固管理）对位 STI-288DGGPM，MS-5GS 对位 STI-144GP；DataMover 贴牌 30% 档；要求与 CRMS NMS 兼容的 SNMP 口径 | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（品牌商/贴牌需求（OEM/ODM）——工业无线厂商自有品牌加固交换机） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288DGGPM），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STI-288DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 1 次实质回复（对方认识我们）；自有品牌/贴牌需求 = 现成 OEM 客户；北美主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STI-288DGGPM 按 30% 档报价，做现供应商的第二货源；贴牌 + 定制 UI/型号 → 30% 档与长期绑定；规模（调研）：11–50 人；$1–4.9M 营收（Crunchbase / Thomasnet）
- **T**：深圳同行（ONV / Utepo / 迈威等）价格战；汇率与海运波动吃掉 20–30% 的价差

## 触达与风险红线

1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。
2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。
3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。
4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。
5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（在卖/在用交换机或 PoE） | ✅ |
| 决策人识别 | ✅ |
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认（有回复但未报量） |
| 商业资格结论 | **技术上合格 / 商业上有互动证据（成交或实质回复或面谈）→ 值得长期跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：WhatsApp / 私信一句话（复制即发；不发邮件）

```text
Did the 130-USD Marvell unit get a lab slot? If your NMS only needs SNMP discovery + port stats, I can send the OID list first.
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-10**（14 天）：无回复 → 换通道再试一次；仍无 → 降 B。有任何回复 → 当即更新 research JSON 并重渲染。

## 变更日志

- 2026-10-27：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 A，分数 88）

---

*建档日期：2026-10-27　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
