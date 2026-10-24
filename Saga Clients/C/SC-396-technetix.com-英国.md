# technetix.com
**官方名称（调研核实）**：Technetix Ltd.（英国 West Sussex；宽带/光纤接入设备品牌商；KP Mark Basham, VP Product Management – Fiber Access）

> **评级 C**　|　英国　|　档案编号 `SC-396`　|　优先级 —　|　状态：有回复·跟进中
>
> **类型**：OEM 品牌商（光纤/宽带接入设备）（推断）　|　**历史关系**：实质回复 2 次；推送 2 次（2025-04-22 → 2026-01-21）　|　**所在清单**：DC线索　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-396
rating: C
rating_auto: C
name_official: "Technetix Ltd.（英国 West Sussex；宽带/光纤接入设备品牌商；KP Mark Basham, VP Product Management – Fiber Access）"
score: 18
country: 英国
region: 欧洲
website: technetix.com
type: OEM 品牌商（光纤/宽带接入设备）
tier_tags: ["DC线索"]
deal: no
replies: 2
followups: 2
first_contact: 2025-04-22
last_contact: 2026-01-21
s_mail: 24 msgs (out 22 / in 2), 2024-06-20 -> 2026-08-10
p1: 无直接对位；2.5G 需求 → STI-288DGGPM / STC-28DGGPM（2.5G 铜口 + 10G SFP+，SFP+ 不跑 2.5G）；CENTEC STH10G 仅 1G/10G
price_tier: 30%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：A 邮箱群发 22 封中两次具名真回：2025-04-22 要规格书/Marvell 芯片型号/能否定制设计/公司介绍 PPT（答：STI-488XGGPM 规格书 + 98DX2515）；2026-01-21 对 CENTEC 群发追问 10G SFP+ 能否跑 2.5G、SFP+ 口最大供电、有无 REST/JSON 管理接口、样机多快（Alan 01-22 答：NO / 见 STH10G 第 6 页 / 「RESTful API with JSON… planned and available in Q2」/ 样机 3~5 工作日）→ 无回；2026-08-10 单发 24 口 PoE $170 → 无回。巨头规则（technetix.com 在 GIANT_DOMAINS）自动 C。（调研 2026-10-24；表内兴趣：基本不用PoE 要10G工业管理收发器 3层工业交换机。8/12/16个SFP+, 主做工业品，问了芯片）
- **为什么是 C 级**：+30 实质回复 2 次（问价/要资料/问型号等）；+0 数据中心交换机线索（Hohunet/CENTEC 线）；-3 WhatsApp 加不上；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/英国；+5 最近活动 2026；-45 巨头/品牌厂商/运营商/军工（INH 规则：体量不匹配或非客户）；C 级细分：体量过大/品牌厂商/运营商
- **历史互动**：实质回复 2 次；推送 2 次（2025-04-22 → 2026-01-21）；最近一次客户回复：2026-01-21：问了一些问题
- **P1**：不推（C 级）；若对方主动来询，起手 无直接对位；2.5G 需求 → STI-288DGGPM / STC-28DGGPM（2.5G 铜口 + 10G SFP+，SFP+ 不跑 2.5G）；CENTEC STH10G 仅 1G/10G（深挖对位：品牌商/定制意向，但巨头体量；先把承诺交代清楚，再看他是否还有话）
- **最大未知**：年走量与现供应商
- **下一步**：2026-11 A 邮箱 → mark.basham@technetix.com（回 2026-01-22 原线程「OEM Core Switching Solution」） 一封收尾信（巨头例外档，仅此一封）：①REST/JSON Q2 承诺——现状是 RPC-API，不是 REST，直说；②「SFP+ 跑 2.5G」在 CENTEC 线是 NO，在 Marvell AC5 线是 YES（1G/2.5G/10G SFP+），1 月答漏了；③只问一个问题：2.5G 那条需求背后是什么应用；不推 $170 的 24 口

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SC-396` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（A 邮箱 22 去 2 来，两次都是 VP Mark Basham 具名、带 4~5 个具体技术问题；2026-01-22 Alan 答复含「REST/JSON API Q2 可用」承诺后无回；巨头规则 C）** ｜ 类型：品牌商 VP 自问 ｜ 筛子：3~4（具体问题层面，未到型号/数量） ｜ 停点：我们的答复一个「NO」（SFP+ 不跑 2.5G）+ 一个未兑现的承诺（REST Q2）——他没再回 ｜ 复活：一封收尾信：交代 REST 承诺现状 + 2.5G 的正确对位机型；不带新品，不群发 ｜ 通路：英国（四大主攻之一）；巨头例外档 ｜ 节奏：一次收尾，之后半年 ｜ 证据：gmail_a 2025-03-24 → 2026-08-10（22 去 2 来）；digest in 2 / out 22；flags giant=1, wa_failed=1
- **现状一句话**：英国宽带设备品牌商 Technetix 的产品 VP 两次具名提问（2025-04 定制设计/芯片；2026-01 CENTEC 线 2.5G/供电/REST/样机）。Alan 2026-01-22 答「REST/JSON API Q2 可用」，Q2 已过，STOS V2.4 功能表没有 REST——承诺悬着；此后只收到群发与一封 $170 推送。
- **对方真实需求（有据）**：光纤接入侧的交换/汇聚：10G SFP+ 口能否 2.5G、SFP+ 供电、程序化管理接口（REST/JSON）、快速样机；更早的问题是「能否定制设计」。
- **断点 / 为什么停在这里**：2026-01-22 的答复：一个 NO + 一个未兑现的 Q2 承诺；之后 9 个月没人交代。
- **Saga 现在该推什么**：P1 **2.5G 问题的正确答案：Marvell AC5 线的 SFP+ 笼子本来就是 1G/2.5G/10G（STC-424XGGM、STI-480XGGM 等），DG 型号的 SFP 是 1G/2.5G——他问的「10G SFP+ 能否跑 2.5G」在 AC5 线上是 YES，Alan 的「NO」只对 CENTEC STH10G 成立；AC5 线无 2.5G 铜口；Realtek 商用线有（STC-18XGDGE/-PW、STC-624XGDGM 等，有价）；CENTEC VastLakes 表有 24/48 口 2.5G/5G/10G Multi-Gig 铜口（含 PoE++，无价）——收尾信第 2 点可带一句**（OEM 30%（品牌商定制）% 档，Realtek 线按 HRUI 2026-09-30 进价 +30% 现算（Q-47 默认，不用 Drive 旧表价）：STC-624XGDGPM $396→$466.4；STC-424XGGM $143 / STI-480XGGM $253 EXW（主表 @6.69）；2026-08-10 推过 24 口 PoE $170）——对外统一口径（#2/#15/#12）：2026-01-22 的「1, NO」只对 CENTEC STH10G 对；AC5 线 SFP+ = 1G/2.5G/10G（主表规格栏），这一点要补上。STOS V2.4 只有「RPC-API management」，无 REST/JSON——2026-01-22 的 Q2 承诺要主动收尾，写法「the programmable interface shipped as an RPC-based API, not REST/JSON; I will not dress it up」；巨头规则 C 不动（Q-55 默认），只发一封｜已发资料（勿重发）：Saga Software Function List-release 7.3.0(2025-03-24)、STI-488XGGPM.pdf(2025-04-23)、BigFlow V2.1 / STH10G Series / Function List V2.4(2026-01-22)
  - 复购/在买项：品；牌；商；若；立；项；为；定；制；，；才；有；复；购
  - 做不了 / 要先核的：他；的；具；体；应；用；（；为；什；么；要； ；S；F；P；+； ；跑； ；2；.；5；G；）；；；T；e；c；h；n；e；t；i；x； ；供；应；商；准；入；要；求；；；R；E；S；T； ；是；否；仍；是；硬；条；件；；；S；i；m；o；n；《；S；T；H；计；划；》；：；1；G；/；2；.；5；G；/；5；G； ；铜；口； ；C；E；N；T；E；C； ；机；「；暂；不；宣；传；、；信；息；备；好；」；→； ；信；稿；只；答；「；o；n； ；r；e；q；u；e；s；t； ；/； ；n；o；t； ；o；n； ；p；u；b；l；i；s；h；e；d； ；l；i；s；t；」；，；不；主；推；；；估；算；带；见； ；C；E；N；T；E；C； ；锚；表； ；§；5；.；3；，；对；客；户；仍； ；p；r；i；c；e； ；o；n； ；r；e；q；u；e；s；t
- **下一步（具体）**：2026-11　A 邮箱 → mark.basham@technetix.com（回 2026-01-22 原线程「OEM Core Switching Solution」）　一封收尾信（巨头例外档，仅此一封）：①REST/JSON Q2 承诺——现状是 RPC-API，不是 REST，直说；②「SFP+ 跑 2.5G」在 CENTEC 线是 NO，在 Marvell AC5 线是 YES（1G/2.5G/10G SFP+），1 月答漏了；③只问一个问题：2.5G 那条需求背后是什么应用；不推 $170 的 24 口
  - 第一问（只问一个）：Mark — closing two loops from January: (1) the programmable interface on the CENTEC line shipped as an RPC-based management API, not the REST/JSON interface I said would come in Q2 — please do not plan on REST; (2) my "NO" on 2.5G was only for the CENTEC STH10G — on our Marvell line the SFP+ cages are 1G/2.5G/10G. What is the application behind the 2.5G requirement?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-04-22 | 来 | Mark Basham（VP Product Management, Fiber Access） | Do you have a data sheet… What Marvell chip is in the switch? Can you do custom designs? Do you have an overview slide deck for Saga telecom | 品牌商 VP 的定制意向问句 | `interest` |
| 2025-04-23 | 去 | Alan | please see attached datasheet. 2, Marvell 98DX 2515… Profile: About us>Factory Information>google link. Customization: in the datesheet itself, web gui or manufacturing | 答了，但没问他要做什么 | `reply` |
| 2026-01-21 | 来 | Mark Basham | Are the 10G SFP+ ports able to run at 2.5Gbps? What the max power that can be drawn by the SFP+ ports? Is there a management interface such as REST, or JSON. Can you send me a data sheet please. And finally how quickly can I get a sample if the answers to above are positive? | 四个硬问题 + 样机意愿 | `rfq` |
| 2026-01-22 | 去 | Alan | 1, NO 2, Please check the power consumption on page 6(STH10 Series) 3, A RESTful management API with JSON data format is planned and available in Q2. 4, Please see attached information. 5, For samples, 3~5 working days is good. We are still improving some features, this takes a while. | REST Q2 承诺——未兑现（STOS V2.4 无 REST） | `promise` |
| 2026-01-22 | 内 | （仓内核对 2026-10-24） | 主表规格栏：STC-424XGGM「4*1G/2.5G/10G SFP+」、STI-480XGGM「4*1G/2.5G/10GBase-X SFP+」；STI-288DGGPM 规格书「DG: 2.5 Gigabit based for optical ports」 | Alan 的「1, NO」只对 CENTEC；AC5 线 SFP+ 可跑 2.5G——收尾信要补 | `check` |
| 2026-08-10 | 去 | Alan | 24 Port PoE af/at… 10G Fiber Uplinks… Price: 170USD/PC. Do you need some samples for testing? | 与他的问题无关的推送；无回 | `push` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：Technetix 当前产品线中哪一段需要 2.5G/SFP+ 供电（官网未爬）；REST 承诺的来源（Alan 当时依据什么说 Q2）；WhatsApp 加不上（flags.wa_failed）的时间与号码

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | technetix.com（取自域名，公司全名待核） | 推断 |
| 国家 | 英国 | 事实（用户表）|
| 网站/域名 | technetix.com | 事实（用户表 URL/邮箱域名） |
| 类型 | OEM 品牌商（光纤/宽带接入设备） | 推断（据兴趣/备注关键词） |
| 联系人 | Mark | 事实（用户表） |
| 来源（From） | IFSEC fair <br>2023 | 事实（用户表） |
| 兴趣（Interested in） | 基本不用PoE<br>要10G工业管理收发器 3层工业交换机。8/12/16个SFP+, 主做工业品，问了芯片 | 事实（用户表） |
| 用户备注（Remark） | 44 7827 990840 <br>加不上  比较专业 | 事实（用户表） |
| 所在清单 | DC线索 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-24）**　网站状态：正常（technetix.com）
- **是谁**：A 邮箱群发 22 封中两次具名真回：2025-04-22 要规格书/Marvell 芯片型号/能否定制设计/公司介绍 PPT（答：STI-488XGGPM 规格书 + 98DX2515）；2026-01-21 对 CENTEC 群发追问 10G SFP+ 能否跑 2.5G、SFP+ 口最大供电、有无 REST/JSON 管理接口、样机多快（Alan 01-22 答：NO / 见 STH10G 第 6 页 / 「RESTful API with JSON… planned and available in Q2」/ 样机 3~5 工作日）→ 无回；2026-08-10 单发 24 口 PoE $170 → 无回。巨头规则（technetix.com 在 GIANT_DOMAINS）自动 C。
- **类型**：OEM 品牌商（光纤/宽带接入设备）
- **规模**：（集团数百人；未核）
- **【邮件】VP 产品管理问定制设计与公司介绍**
  > What Marvell chip is in the switch? Can you do custom designs? Do you have an overview slide deck for Saga telecom
  > 来源：data/gmail_a/messages/<year>/<month>.jsonl（抓取 2025-04-22）
- **【邮件】CENTEC 线四问：2.5G on SFP+ / SFP+ 供电 / REST·JSON / 样机速度**
  > Are the 10G SFP+ ports able to run at 2.5Gbps? What the max power that can be drawn by the SFP+ ports? Is there a management interface such as REST, or JSON… how quickly can I get a sample
  > 来源：data/gmail_a/messages/<year>/<month>.jsonl（抓取 2026-01-21）
- **【邮件（去）】Alan 承诺 REST/JSON API「Q2 可用」**
  > 1, NO 2, …page 6(STH10 Series) 3, A RESTful management API with JSON data format is planned and available in Q2. 4, … 5, For samples, 3~5 working days
  > 来源：data/gmail_a/messages/<year>/<month>.jsonl（抓取 2026-01-22）
- **KP**：Mark Basham（）mark.basham@technetix.com +44 1444 251260 / m +44 7827 990840（信尾；对外材料不写电话）〔data/gmail_a/messages/<year>/<month>.jsonl〕
- 备注：巨头规则（INH：体量不匹配）→ C 不动；但这是仓内少有的英国品牌商 VP 两次具名提问，按 Q-55「巨头例外档」处理：档案齐全，只允许一封收尾信（把 2026-01-22 的 REST 承诺交代清楚），不进群发。flags.wa_failed=1（WhatsApp 加不上）。

### 加厚挖掘（2026-10-24 · 邮件证据 + 官网常识）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Technetix Ltd. |
| 总部/地址 | Albourne, West Sussex, UK |
| 其他 | 宽带/光纤接入设备（信尾 Fiber Access） |

- **触达通道（公开）**：role: VP Product Management；region: 英国
- **风险/边界**：巨头采购流程（供应商准入/UL/合规）小贸易商难进；2026-01-22 对他说了「RESTful API JSON Q2 可用」——STOS V2.4（2026/Q2）功能表只有「RPC-API management」，无 REST/JSON 字样：承诺未兑现或措辞不符，需交代；他真正的兴趣（2.5G on SFP+、SFP+ 供电）指向光纤接入侧的特殊用法，Saga 标准机型不对位
- **Saga 对位结论**：P1 无直接对位；2.5G 需求 → STI-288DGGPM / STC-28DGGPM（2.5G 铜口 + 10G SFP+，SFP+ 不跑 2.5G）；CENTEC STH10G 仅 1G/10G（30% 档）——品牌商/定制意向，但巨头体量；先把承诺交代清楚，再看他是否还有话
- **邮件切入句（英文）**：（见 mail_review.draft_en）

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 2 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-04-22 | 2025.4.22 | bypass | 问了一些问题 | A |  | DC Switches 08.10.xlsx#23 |
| 2026-01-21 | 2026.1.21 | CENTEC | 问了一些问题 | A |  | DC Switches 08.10.xlsx#23 |

## 联系方式（已有 · 原值照录）

- 邮箱：`mark.basham@technetix.com`〔企业邮箱；来源：用户表原值〕
- 电话：`+447827990840`〔WhatsApp 加不上；原值见来源表〕
- 联系人（原值）：Mark
- 网站/域名：technetix.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Mark Basham | — | mark.basham@technetix.com / +44 1444 251260 / m +44 7827 990840（信尾；对外材料不写电话） | 调研核实（公开页） | data/gmail_a/messages/<year>/<month>.jsonl |
| Mark | — | mark.basham@technetix.com / +447827990840 | 用户表原值 | Clients/ 表 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| DC Switches 08.10.xlsx#总表:24 | 23 | https://emea.technetix.com/ | 英国 | Mark | IFSEC fair <br>2023 | 基本不用PoE<br>要10G工业管理收发器 3层工业交换机。8/12/16个SFP+, 主做工业品，问了芯片 | mark.basham@technetix.com | 44 7827 990840 <br>加不上  比较专业 | 2 条 |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：体量过大/品牌厂商/运营商。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-396,B,理由` 后重跑即可。

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
| 商业资格结论 | **不合格（见 C 级细分）→ 不主动跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: OEM Core Switching Solution — closing two loops from January

```text
Hello Mark,

Two things from my January reply that I owe you a straight update on.

1. The management interface: I wrote that a RESTful API with JSON would be available in Q2. What shipped in the 2026/Q2 software is an RPC-based management API plus SNMP v3 and CLI — not REST/JSON. Please do not plan on REST from our side; I would rather say so than let the Q2 line stand.

2. 2.5G on SFP+: my "NO" was correct only for the CENTEC STH10G. On our Marvell AC5 line the SFP+ cages run at 1G/2.5G/10G (for example 24 x GbE + 4 x SFP+, or the industrial 8 x GbE + 4 x SFP+ at -40 to +75 C), and the DG models carry 1G/2.5G SFP. I should have said that in January. Copper ports on that line are 1G; if the requirement is multi-gig copper, we have two ways: the commercial Realtek line (8 x 2.5G PoE + 10G SFP web-managed at $66 USD EXW, 24 x 2.5G PoE++ L3 at $466.4 USD EXW, single PSU) or, on request and not on our published list, CENTEC-based 24/48 x 2.5G/5G/10G Base-T units with PoE++ and dual PSU.

One question: what is the application behind the 2.5G requirement — ONT/CPE uplinks, or something else? That tells me whether a sample (3-5 working days) is worth your time.

Thank you.
Alan
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- 不复核。对方主动来询 → 在 `data/saga_clients/人工定级.csv` 写一行升级后重跑。

## 变更日志

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 18）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
