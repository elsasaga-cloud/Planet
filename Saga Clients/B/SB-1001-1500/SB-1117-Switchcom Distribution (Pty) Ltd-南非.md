# Switchcom Distribution (Pty) Ltd

> **评级 B**　|　南非　|　档案编号 `SB-1117`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：网络设备分销商（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：补录、S邮箱回复、分销商、未入正题　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-1117
rating: B
rating_auto: B
rating_research: B  # 有邮箱、是真实分销商、双向往来，但对话方向反了且无采购人 → B（低优先）
name_official: "Switchcom Distribution (Pty) Ltd"
score: 31
country: 南非
region: 非洲
website: switchcom.co.za
type: 网络设备分销商
tier_tags: ["补录", "S邮箱回复", "分销商", "未入正题"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 10 msgs (out 6 / in 4), 2024-07-07 -> 2024-12-12
p1: STC-424DGGPM-280W
price_tier: 20%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：南非网络设备分销商（销售台 sales@ + 客户经理 Kevin Maphanga）。Simon 2024-07 推 10G 媒体转换器、2024-12 推 52 口 L2+ PoE，对方两次都把 Saga 当买家：自动回复「Kevin received your request…」并于 2024-12-12 发来其自家报价单 Quotation QU509692.PDF——没有进入采购对话。S 邮箱 10 封（2024-07-07 → 2024-12-12）。（调研 2026-10-22；表内兴趣：Simon 推过 10G 媒体转换器（2024-07）、52 口 L2+ PoE（2024-12）；对方两次都以「销售报价」回应（把 Saga 当买家））
- **为什么是 B 级**：**调研后定级 B**（有邮箱、是真实分销商、双向往来，但对话方向反了且无采购人 → B（低优先））；自动分级 B：+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-6 区域 非洲/南非；+2 最近活动 2024
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：— — —；—
- **第一问（只问一个）**：Are PoE / industrial switches something you still source today, or has that line been dropped?
- **最大未知**：年走量与现供应商
- **下一步**：不动（同行分销商；把 Saga 当买家） — 若 Simon 想做南非分销：找 Switchcom 采购/产品经理谈白牌供货，不再用群发

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-1117` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（4 封：2 封 Switchcom 工单 + Kevin 2024-12 反向发来 Switchcom 报价单（把 Saga 当买家）+ elberts@firsttech 2024-08「cannot receive samples」；Elsa 箱：`to:switchcom.co.za` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 6 / 来 4）（第 74 批(n)））** ｜ 类型：南非网络分销（Switchcom） ｜ 筛子：1 ｜ 停点：角色错位：对方在卖 ｜ 复活：不动 ｜ 通路：ZA ｜ 节奏：不动 ｜ 证据：k=a7d9a3952458bd64 / 40e70b0706c53fbb
- **现状一句话**：—
- **对方真实需求（有据）**：—
- **断点 / 为什么停在这里**：—
- **Saga 现在该推什么**：P1 **—**（20% 档，—）———
- **下一步（具体）**：不动（同行分销商；把 Saga 当买家）　—　若 Simon 想做南非分销：找 Switchcom 采购/产品经理谈白牌供货，不再用群发

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-07-08 | 来 | Switchcom Distribution 工单机器人 | Kevin received your request and is currently working diligently to provide you with pricing… your request is a top priority for us | Saga 的推销信被当成「客户询价」进了对方的销售工单——Switchcom 是南非分销商（Ubiquiti/MikroTik 类），其系统把一切来信视为买家 | `gmail_s（switchcom.co.za，jsonl client 字段为空，按域名重扫）` |
| 2024-12-12 | 来 | Kevin Maphanga（Account Manager, Switchcom） | Please see the attached sales quote above on what we can offer and stock is available.（回 Simon「48 Port PoE Managed Switch, 300usd/pc」） | 对方反向给 Saga 报价 + 有现货 = 同行分销商，不是买家；Saga 的 300 USD 52 口 L2+ 价对它没有意义，除非谈 OEM/白牌供货。维持不动；若要动，只能以「supplier onboarding」口径找其采购而不是 Account Manager | `gmail_s（switchcom.co.za，jsonl client 字段为空，按域名重扫）` |

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Switchcom Distribution (Pty) Ltd | 事实（用户表） |
| 国家 | 南非 | 事实（用户表）|
| 网站/域名 | switchcom.co.za | 事实（用户表 URL/邮箱域名） |
| 类型 | 网络设备分销商 | 推断（据兴趣/备注关键词） |
| 联系人 | Kevin Maphanga | 事实（用户表） |
| 来源（From） | 补录：S 邮箱双向往来但不在 Clients/ 表（T29-U10 复盘发现） | 事实（用户表） |
| 兴趣（Interested in） | Simon 推过 10G 媒体转换器（2024-07）、52 口 L2+ PoE（2024-12）；对方两次都以「销售报价」回应（把 Saga 当买家） | 事实（用户表） |
| 用户备注（Remark） | S 邮箱 10 封（2024-07-07 → 2024-12-12）：销售台自动回复「Kevin received your request…」+ 2024-12-12 Kevin 发来其自家报价单 Quotation QU509692.PDF —— 未进入真正的采购对话；需要换角度（渠道/贴牌）重新切入；详见 research JSON | 事实（用户表） |
| 用户分档（Category） | 网络设备分销商（MikroTik/Ubiquiti 类渠道） | 事实（用户表） |
| 所在清单 | 补录、S邮箱回复、分销商、未入正题 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-22）**　网站状态：未核（本轮只用 S 邮箱证据）
- **是谁**：南非网络设备分销商（销售台 sales@ + 客户经理 Kevin Maphanga）。Simon 2024-07 推 10G 媒体转换器、2024-12 推 52 口 L2+ PoE，对方两次都把 Saga 当买家：自动回复「Kevin received your request…」并于 2024-12-12 发来其自家报价单 Quotation QU509692.PDF——没有进入采购对话。S 邮箱 10 封（2024-07-07 → 2024-12-12）。
- **类型**：网络设备分销商
- **规模**：中（有销售台 + 多客户经理）
- **【email】销售台把 Simon 当询价客户**
  > Kevin received your request and is currently working diligently to provide you with pricing. Please be assured that your request is a top priority for us
  > 来源：data/gmail_s/messages/2024/2024-07.jsonl（from sales@switchcom.co.za）（抓取 2024-07-08）
- **【email】客户经理发来自家报价单（方向反了）**
  > Please see the attached sales quote above on what we can offer and stock is available.（附 Quotation QU509692.PDF）Kevin Maphanga, Account Manager, Office: +27(0)10 007 2555
  > 来源：data/gmail_s/messages/2024/2024-12.jsonl（抓取 2024-12-12）
- **KP**：Kevin Maphanga（Account Manager（销售侧，非采购））kevin@switchcom.co.za +27 (0)10 007 2555〔S 邮箱签名〕
- **调研后定级**：B（原自动 B）——有邮箱、是真实分销商、双向往来，但对话方向反了且无采购人 → B（低优先）
- 备注：分销商的采购/品类经理才是对的人；现有联系人是销售。南非不在 Planet 仓重点区域，但 Saga Clients 全域覆盖：慢慢跟，换「渠道/贴牌」角度找品类负责人再发。


## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：10 封（去 6 / 来 4）　|　**期间**：2024-07-07 → 2024-12-12　|　**最后去信**：2024-12-12
- **对方邮箱**：joash@switchcom.co.za、kevin@switchcom.co.za、sales@switchcom.co.za
- **最后一封来信**：2024-12-12 sales@switchcom.co.za「RE: 48 Port PoE Managed Switch」：Hi there, Thanks for reaching out! We’ve received your request and are already working on getting the best pricing for you. Rest assured, your request is a priority for us, and we'll have a response to you as soon as possible. We appreciate you choosing Switch

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 48 Port PoE Managed Switch | 2024-12-12 | 2024-12-12 | 2 | 1 | 5 |
| 8 Port Industrial PoE Switch | 2024-11-15 | 2024-11-15 | 0 | 1 | 1 |
| 10G Media Converter | 2024-10-15 | 2024-10-15 | 0 | 1 | 1 |
| Power Converter | 2024-09-10 | 2024-09-10 | 0 | 1 | 1 |
| Passive PoE Switch | 2024-08-16 | 2024-08-16 | 3 | 3 | 7 |
| 10G fiber media converter | 2024-07-07 | 2024-07-08 | 1 | 1 | 3 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-25T07:41:18Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-1117/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://switchcom.co.za/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 7603 字符；首行：Switchcom Distribution |

## 联系方式（已有 · 原值照录）

- 邮箱：`kevin@switchcom.co.za`〔企业邮箱；来源：用户表原值〕
- 邮箱：`sales@switchcom.co.za`〔企业邮箱；来源：用户表原值〕
- 电话：`+270100072555`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Kevin Maphanga
- 职位（原值）：Account Manager
- 网站/域名：switchcom.co.za
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Kevin Maphanga | Account Manager（销售侧，非采购） | kevin@switchcom.co.za / +27 (0)10 007 2555 | 调研核实（公开页） | S 邮箱签名 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 补录客户.jsonl#(补录):10 | GM-003 | Switchcom Distribution (Pty) Ltd | 南非 | Kevin Maphanga | 补录：S 邮箱双向往来但不在 Clients/ 表（T29-U10 复盘发现） | Simon 推过 10G 媒体转换器（2024-07）、52 口 L2+ PoE（2024-12）；对方两次都以「销售报价」回应（把 Saga 当买家） | kevin@switchcom.co.za; sales@switchcom.co.za +27 (0)10 007 2555 https://www.switchcom.co.za | S 邮箱 10 封（2024-07-07 → 2024-12-12）：销售台自动回复「Kevin received your request…」+ 2024-12-12 Kevin 发来其自家报价单 Quotation QU509692.PDF —— 未进入真正的采购对话；需要换角度（渠道/贴牌）重新切入；详见 research JSON Account Manager | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-424DGGPM-280W | 深挖对位：分销商 → 20% 档；走量口型 24 口 PoE | $134.5 USD EXW（20% 档，SmartByte LT-S8328GP-4GX24GT-S 750 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 20%（网络设备分销商） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $80.7 USD EXW（20% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：20% 档 $139.9 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），20% 档公式为 $181.2——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-424DGGPM-280W 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；20% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：名单内已有联系记录，不是零起点
- **W**：非洲：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STC-424DGGPM-280W 按 20% 档报价，做现供应商的第二货源；规模（调研）：中（有销售台 + 多客户经理）
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
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STC-424DGGPM-280W - 24-port Gigabit PoE+ L2+ managed switch (Marvell-based, neutral label)

```text
Hi Kevin,

We have been in touch before about PoE and industrial switches; instead of a catalogue, here is one concrete option.

We supply a Marvell-based 24-port Gigabit PoE+ L2+ managed switch (280 W PoE budget, 4 uplinks) - model STC-424DGGPM-280W - that fits the same slot as the units you source today at a lower landed cost, and we can ship it under your own label with neutral packaging. Current price: $134.5 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Are PoE / industrial switches something you still source today, or has that line been dropped?

If useful, one unit at the unit price for a 30-day side-by-side test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 发送前检查：① 不出现「Made in China」或原产地；② 不承诺未实测指标（PoE 功率/温宽）；③ 落款换成发件人姓名；④ 一次只问一个问题；⑤ 价格为 USD EXW 快照，过窗先核价；⑥ 只用表内/公开原值邮箱，不猜地址；⑦ 发出后在「新跟进记录」补一行并告知日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-24**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 31）

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
