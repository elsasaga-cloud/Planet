# Litech (Pvt) Ltd

> **评级 B**　|　巴基斯坦　|　档案编号 `SB-1338`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：系统集成/项目承包（华为渠道）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：补录、S邮箱来询未回、RFQ　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-1338
rating: B
rating_auto: B
rating_research: B  # 具名 BD 经理 + 真实 RFQ，但年代久、规格对标华为（部分做不了）、未回 → B
name_official: "Litech (Pvt) Ltd"
score: 31
country: 巴基斯坦
region: 南亚
website: litech.com.pk
type: 系统集成/项目承包（华为渠道）
tier_tags: ["补录", "S邮箱来询未回", "RFQ"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 1 msgs (out 0 / in 1), 2024-03-09 -> 2024-03-09
p1: STI-41616XGGPM
price_tier: 25%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-23
```

## SALES BRIEF（压缩模型）

- **是谁**：巴基斯坦伊斯兰堡系统集成/项目承包商（华为渠道），2024-03-09 主动发来 RFQ：接入/汇聚交换机 + 路由器规格书（以华为型号为参照）要做技术符合性声明，称多个项目在管线、想长期合作。S 邮箱内未见 Simon 回复（来询未回）。（调研 2026-10-22；表内兴趣：接入/汇聚交换机 + 路由器 RFQ（客户规格以华为型号为参照，要求做技术符合性声明）；称项目在管线、想长期合作）
- **为什么是 B 级**：**调研后定级 B**（具名 BD 经理 + 真实 RFQ，但年代久、规格对标华为（部分做不了）、未回 → B）；自动分级 B：+12 备注记录了对方问价/要资料/见面等互动；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-6 区域 南亚/巴基斯坦；+2 最近活动 2024
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-22）**：STC-424XGGPM-280W — 项目集成商 → 25% 档；接入层两款正好对上他的 ① ②（AC5 L2+ 规格书列 802.1X、IP source guard、ARP-check、DHCP snooping、SSHv2/HTTPS/SNMPv3）；汇聚 ③ 需 L3 OSPF——用 L3 款另议；$188.7 USD EXW（CNY 1010 ×1.25）；48 口 STC-448XGGPM $349.4；汇聚 48×SFP+4×10G L3 用 SmartByte 型号报价并标注
- **第一问（只问一个）**：Is the access/aggregation project from your March 2024 RFQ still live (or a similar one in the pipeline), and roughly how many 24/48-port PoE units does it need?
- **最大未知**：年走量与现供应商
- **下一步**：本周（Simon 从 S 邮箱发） S 邮箱回 2024-03-09 原件（Re: RFQ Switches） 按下稿发重开门短信；若对方回复项目仍在，再按 ①②③ 逐条出符合性表

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-22）

> 依据：S 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-1338` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-22。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **现状一句话**：伊斯兰堡 Litech（华为渠道集成商，BD 经理 Hassan Ijaz Cheema）2024-03-09 主动发 RFQ：《Access and aggregation switches specs.docx》+ 路由器规格，要求技术符合性声明，并写明「number of projects in pipeline, want long business partnership」。**S 邮箱内无任何回复**（T29-U11 Simon 裁定：重开）。
- **对方真实需求（有据）**：规格以华为为参照：① 24 口 GE PoE+ + SFP 接入机（S5735-L24P4S 级）；② 48 口 GE PoE+ 370W + 4 SFP（S5735-L48P4S 级）；③ 汇聚 48×1G SFP + 4×10G SFP+、支持 OSPF/RIP（S5736-S48S4X 级）；④ 1000Base-LX SFP；⑤ AR6300 路由器。功能要求：802.1X / RADIUS CoA、Port Security、DAI、IP Source Guard、DHCP snooping、SSHv2/HTTPS/SNMPv3。
- **断点 / 为什么停在这里**：2024-03 没人回（可能微信/其他渠道回过，Simon 未确认）；2.5 年后项目是否还在不知道。路由器不做；汇聚 48×SFP 商用款价格主表没有标准条目。
- **Saga 现在该推什么**：P1 **STC-424XGGPM-280W**（25% 档，$188.7 USD EXW（CNY 1010 ×1.25）；48 口 STC-448XGGPM $349.4；汇聚 48×SFP+4×10G L3 用 SmartByte 型号报价并标注）——项目集成商 → 25% 档；接入层两款正好对上他的 ① ②（AC5 L2+ 规格书列 802.1X、IP source guard、ARP-check、DHCP snooping、SSHv2/HTTPS/SNMPv3）；汇聚 ③ 需 L3 OSPF——用 L3 款另议
  - 做不了 / 要先核的：RADIUS CoA / Flexible Authentication、DAI（SmartByte 叫 ARP-check）逐条符合性要向 SmartByte 核；48×SFP + 4×10G 商用 L3 汇聚：价格主表无条目，需向 SmartByte 询 LT-S85xx 48 光口 L3 价格；守界：若终端是政府/军队/运营商标的，先问清收货主体与最终用户再报价；路由器（AR6300 级）：不做，明说
- **下一步（具体）**：本周（Simon 从 S 邮箱发）　S 邮箱回 2024-03-09 原件（Re: RFQ Switches）　按下稿发重开门短信；若对方回复项目仍在，再按 ①②③ 逐条出符合性表
  - 第一问（只问一个）：Is the access/aggregation project from your March 2024 RFQ still live (or a similar one in the pipeline), and roughly how many 24/48-port PoE units does it need?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-03-09 | 来 | Hassan Ijaz Cheema, Manager BD | Attached herewith are the technical specifications of different Access/Aggregation switches and Routers for your working for technical compliance statement… customer has prepared these specifications with reference to different models of Huawei Switches… number of projects in pipeline, want long business partnership | 主动来询 + 长期合作意向；S 邮箱无回复 | `7203d72a927b7030` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：Simon 当年是否在微信/其他邮箱回过（T29-U11 决定不等确认直接重开）

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Litech (Pvt) Ltd | 事实（用户表） |
| 国家 | 巴基斯坦 | 事实（用户表）|
| 网站/域名 | litech.com.pk | 事实（用户表 URL/邮箱域名） |
| 类型 | 系统集成/项目承包（华为渠道） | 推断（据兴趣/备注关键词） |
| 联系人 | Hassan Ijaz Cheema | 事实（用户表） |
| 来源（From） | 补录：S 邮箱来询未回（T29-U10 复盘发现） | 事实（用户表） |
| 兴趣（Interested in） | 接入/汇聚交换机 + 路由器 RFQ（客户规格以华为型号为参照，要求做技术符合性声明）；称项目在管线、想长期合作 | 事实（用户表） |
| 用户备注（Remark） | S 邮箱 1 封（2024-03-09 来信，附《Access and aggregation switches specs.docx》）；S 邮箱内未见回复（可能微信/其他渠道回了，待 Simon 确认）；路由器不在 Saga 线内，只能对交换机部分；详见 research JSON | 事实（用户表） |
| 用户分档（Category） | 系统集成/项目承包（华为渠道） | 事实（用户表） |
| 所在清单 | 补录、S邮箱来询未回、RFQ | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | 华为 | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-22）**　网站状态：未核（本轮只用 S 邮箱证据；注意 litech.cc 马来西亚 = 另一家 SC-917，勿混）
- **是谁**：巴基斯坦伊斯兰堡系统集成/项目承包商（华为渠道），2024-03-09 主动发来 RFQ：接入/汇聚交换机 + 路由器规格书（以华为型号为参照）要做技术符合性声明，称多个项目在管线、想长期合作。S 邮箱内未见 Simon 回复（来询未回）。
- **类型**：系统集成/项目承包（华为渠道）
- **规模**：中（有 BD 经理、项目制）
- **在卖/在用品牌**：Huawei
- **【email】主动 RFQ + 长期合作意向（来询未回）**
  > Attached herewith are the technical specifications of different Access/Aggregation switches and Routers for your working for technical compliance statement… customer has prepared these specifications with reference to different models of Huawei Switches… number of projects are in pipe line and we want long business partnership with you（附 Access and aggregation switches specs.docx）
  > 来源：data/gmail_s/messages/2024/2024-03.jsonl（from hassancheema@litech.com.pk，主题 RFQ Switches）（抓取 2024-03-09）
- **KP**：Hassan Ijaz Cheema（Manager Business Development）hassancheema@litech.com.pk +92 310 092 4444 / +92 51 8744109〔S 邮箱签名〕
- **调研后定级**：B（原自动 B）——具名 BD 经理 + 真实 RFQ，但年代久、规格对标华为（部分做不了）、未回 → B
- 备注：2.5 年前的 RFQ，先确认 Simon 当时是否在别的渠道回过；若没有，可发一封「当年没接上，现在 L2+/L3 线成熟」的短信重新开门（只对交换机部分，路由器不做）。公共项目/运营商类项目注意守界。


## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| 华为 | 企业级大牌（Cisco/HPE/华为类） | Saga 只能接接入层/工业层，不对标核心；问清是否有白牌接入层需求 |

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：1 封（去 0 / 来 1）　|　**期间**：2024-03-09 → 2024-03-09　|　**最后去信**：—
- **对方邮箱**：hassancheema@litech.com.pk
- **最后一封来信**：2024-03-09 hassancheema@litech.com.pk「RFQ Switches」：Dear Mr. Simon, Hoping you are doing well, Attached herewith are the technical specifications of different Access/Aggregation switches and Routers for your working for technical compliance statement. Please note that customer has prepared these specifications 

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| RFQ Switches | 2024-03-09 | 2024-03-09 | 1 | 0 | 13 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：2 个　|　**数据截至**：2026-10-23T04:20:51Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-1338/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://litech.com.pk/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 3700 字符；首行：Litech Pakistan offering Optical Fiber Cables & Telecom Cables in Pakistan |
| [feed_auto](https://litech.com.pk/feed/) | rss | HTTP 200 | 2026-10-23T04:20:51Z | 10 条；最新：Fri, 01 May 2026 06:24:11 Fiber Optic Cable Connectors and Splicing |

## 联系方式（已有 · 原值照录）

- 邮箱：`hassancheema@litech.com.pk`〔企业邮箱；来源：用户表原值〕
- 电话：`+923100924444`〔电话/WhatsApp 状态未记；原值见来源表〕
- 电话：`+92518744109`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Hassan Ijaz Cheema
- 职位（原值）：Manager Business Development
- 网站/域名：litech.com.pk
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Hassan Ijaz Cheema | Manager Business Development | hassancheema@litech.com.pk / +92 310 092 4444 / +92 51 8744109 | 调研核实（公开页） | S 邮箱签名 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 补录客户.jsonl#(补录):11 | GM-004 | Litech (Pvt) Ltd | 巴基斯坦 | Hassan Ijaz Cheema | 补录：S 邮箱来询未回（T29-U10 复盘发现） | 接入/汇聚交换机 + 路由器 RFQ（客户规格以华为型号为参照，要求做技术符合性声明）；称项目在管线、想长期合作 | hassancheema@litech.com.pk +92 310 092 4444; +92 51 8744109 https://www.litech.com.pk | S 邮箱 1 封（2024-03-09 来信，附《Access and aggregation switches specs.docx》）；S 邮箱内未见回复（可能微信/其他渠道回了，待 Simon 确认）；路由器不在 Saga 线内，只能对交换机部分；详见 research JSON Manager Business Development | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-41616XGGPM | 深挖对位：项目集成商 → 25% 档；汇聚层 L3 口型先用工业 L3 顶上，商用 48 口 L3 另议 | $469.0 USD EXW（25% 档，SmartByte LT-IS6520XGP-4XS16GT 2510 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（系统集成/项目承包（华为渠道）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $145.7 USD EXW（25% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $188.7 USD EXW（25% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-41616XGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STI-41616XGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：名单内已有联系记录，不是零起点
- **W**：南亚：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STI-41616XGGPM 按 25% 档报价，做现供应商的第二货源；规模（调研）：中（有 BD 经理、项目制）
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
| 现用/在卖交换品牌 | ✅ 华为 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: RFQ Switches - picking this up (access / aggregation switches only)

```text
Hi Hassan,

Your RFQ from March 2024 (access and aggregation switches referenced to Huawei S5735 / S5736) did not get the answer it deserved from our side, and I would like to pick it up properly now - for the switch part only; we do not offer routers.

What we can quote today, with a line-by-line compliance statement:
- 24 x Gigabit PoE+ (802.3at, 280 W) + 4 x 1G/2.5G/10G SFP+, L2+ managed (Marvell AC5): 802.1X, port security, DHCP snooping, IP source guard, ARP inspection, SSHv2 / HTTPS / SNMPv3 - about USD 189 EXW per unit (snapshot 2026-10-22, valid 15 days).
- 48 x Gigabit PoE+ (440 W) + 4 x SFP+, same feature set - about USD 349 EXW.
- 48 x 1G SFP + 4 x 10G SFP+ L3 aggregation (OSPF / RIP) - on request.
Neutral or your own branding, CE / RoHS / FCC, 10-15 days lead time.

One question: is the project from that RFQ (or a similar one in your pipeline) still live, and roughly how many 24/48-port PoE units does it need?

Best regards,
Simon
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-22**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-23：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 31）

---

*建档日期：2026-10-23　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
