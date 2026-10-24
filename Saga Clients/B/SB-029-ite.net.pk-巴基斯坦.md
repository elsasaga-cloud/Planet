# ite.net.pk
**官方名称（调研核实）**：International Technology Exchanger (ITE)（Karachi）

> **评级 B**　|　巴基斯坦　|　档案编号 `SB-029`　|　优先级 ★★　|　状态：有回复·跟进中
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：实质回复 1 次；推送 4 次（2025-04-09 → 2025-10-02）　|　**所在清单**：E已回复　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-029
rating: B
rating_auto: B
name_official: "International Technology Exchanger (ITE)（Karachi）"
score: 59
country: 巴基斯坦
region: 南亚
website: ite.net.pk
type: 经销/集成（类型待核）
tier_tags: ["E已回复"]
deal: no
replies: 1
followups: 4
first_contact: 2025-04-09
last_contact: 2025-10-02
p1: STC-28DGGPM
price_tier: 20%
research: done
site_snapshot: ok  # 2026-10-21
sources: 1
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：卡拉奇 IT 方案商（20+ 年，Cisco / Fortinet / Huawei / Ubiquiti / Juniper），Faisal Javed；2025-04 对 2 光 2 电 mini 群发反问「有 1 GE + 4 FE 路由器吗」（Saga 无路由器）。（调研 2026-10-21；表内兴趣：switch）
- **为什么是 B 级**：+22 实质回复 1 次；+18 在「已回复」名单（A/E Replied）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-6 区域 南亚/巴基斯坦；+5 最近活动 2025；-3 跟进表最近平台标记 E（已降为群发）
- **历史互动**：实质回复 1 次；推送 4 次（2025-04-09 → 2025-10-02）；最近一次客户回复：2025-04-09：have Routers with 1GE and 4 FE ports?
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-28DGGPM — 交换机兴趣 → STC-28DGGPM 起手（经销 20%）；路由器不供。；按主表（研究档 saga_fit）
- **第一问（只问一个）**：Are PoE / industrial switches something you still source today, or has that line been dropped?
- **最大未知**：年走量与现供应商
- **下一步**：不动 — —

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-029` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未发信→明确不对口（Elsa 邮箱 2025-04-09 Faisal（ITE，巴基斯坦）三封：要「Routers with 1GE and 4 FE ports」+ 路由规格 IP SLA / GRE / PPPoE / BGP / IPsec——是路由器需求，Saga 不做路由器）** ｜ 类型：— ｜ 筛子：—（需求路由器，非交换机） ｜ 停点：从未触达 ｜ 复活：不动（需求不对口） ｜ 通路：巴基斯坦 非主攻 ｜ 节奏：不动 ｜ 证据：gmail_digest：out 0；用户表：「回复：have Routers with 1GE and 4 FE ports?」；研究档 risks：需求为路由器（缺口）；巴基斯坦 L/C / 外汇；Elsa 邮箱 `data/gmail_e/text/`（Replied 线程，客户→Elsa 正文；Elsa 回复正文未入库）
- **现状一句话**：卡拉奇 IT 方案商（20+ 年，Cisco / Fortinet / Huawei / Ubiquiti / Juniper），Faisal Javed；2025-04 对 2 光 2 电 mini 群发反问「有 1 GE + 4 FE 路由器吗」（Saga 无路由器）。
- **对方真实需求（有据）**：交换机兴趣 → STC-28DGGPM 起手（经销 20%）；路由器不供。
- **断点 / 为什么停在这里**：产品线不对口（路由器）
- **Saga 现在该推什么**：P1 **STC-28DGGPM**（20% 档，按主表（研究档 saga_fit））——交换机兴趣 → STC-28DGGPM 起手（经销 20%）；路由器不供。
- **下一步（具体）**：不动　—　—

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-04-09 | 来 | Faisal（International Technology Exchanger，PK） | Do you have Routers with 1GE and 4 FE ports … IP SLA, GRE Tunneling, PPPoE, BGP, IPsec Tunnels | 路由器 + VPN 规格 = 守界外（C10）；不设计绕路 | `gmail_e` |
| 2025-04-09 | 去 | Elsa | Sorry, it is not on our list. We can help source it if this is fine with you. | 路由器需求，Elsa 答没有、可代找 | `gmail_e 196197e0cbc6c411` |
| 2025-04-09 | 去 | Elsa | Is something as attached OK?（附 Info.docx） | 同日发了一份代找方案 → 无下文 | `gmail_e 196199ab58b3499b` |
| 2026-10-21 | 用户表 | Simon | 回复：have Routers with 1GE and 4 FE ports? | 表内备注 | `用户表` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：（已核 2026-10-24，第 73 批）Elsa 邮箱有往来：04-09 Faisal 三封要 1GE+4FE 路由器 → Elsa 答没有、可代找 + Info.docx → 无下文；用户表「有回复·跟进中」= 这条；（已核 2026-10-24，第 73 批）见上条；不是 WhatsApp

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | ite.net.pk（取自域名，公司全名待核） | 推断 |
| 国家 | 巴基斯坦 | 事实（用户表）|
| 网站/域名 | ite.net.pk | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Faisal Javed | 事实（用户表） |
| 来源（From） | 富通天下 | 事实（用户表） |
| 兴趣（Interested in） | switch | 事实（用户表） |
| 用户备注（Remark） | faisal@ite.net.pk | 事实（用户表） |
| 所在清单 | E已回复 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线（ite.net.pk，快照 2026-10-21）
- **是谁**：卡拉奇 IT 方案商（20+ 年，Cisco / Fortinet / Huawei / Ubiquiti / Juniper），Faisal Javed；2025-04 对 2 光 2 电 mini 群发反问「有 1 GE + 4 FE 路由器吗」（Saga 无路由器）。
- **在卖/在用品牌**：Cisco, Fortinet, Huawei, Ubiquiti, Juniper
- **【官网快照】20+ 年 IT 方案；品牌 Cisco / Fortinet / Huawei / Ubiquiti / Juniper；021-34598598**
  > 20+ Years of Excellence in IT Solutions… 021-34598598; brands Cisco, Fortinet, Huawei, Ubiquiti, Juniper
  > 来源：https://ite.net.pk/（抓取 2026-10-21）
- **【用户表】兴趣 switch；2025-04 群发 22 迷你→have Routers with 1GE and 4 FE ports?**
  > 回复：have Routers with 1GE and 4 FE ports?
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Faisal Javed（）faisal@ite.net.pk +92 21 3459 8598〔（本地 Clients/ 表格，无公开 URL）〕
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（官网快照核对））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | International Technology Exchanger |
| 成立 | 约 2005（20+ 年） |
| 总部/地址 | Karachi, Pakistan |
| 其他 | info@/sales@ite.net.pk |

- **业务线**：企业网络 / 安全集成（多品牌）
- **触达通道（公开）**：role: IT 方案商 / 经销；region: 巴基斯坦
- **近况信号**：
  - 主动反问路由器 → 有 SOHO 路由采购需求（Saga 无，缺口记录）
- **风险/边界**：需求为路由器（缺口）；巴基斯坦 L/C / 外汇
- **Saga 对位结论**：P1 STC-28DGGPM（20% 档）——交换机兴趣 → STC-28DGGPM 起手（经销 20%）；路由器不供。
- **邮件切入句（英文）**：Faisal, we don't do routers — but for the switch side, the 8-PoE + 2-SFP managed (Marvell) is in stock from 1 pc; is that useful for the same projects, or is it routers only right now?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://ite.net.pk/　语言：en　站点地图 URL 数：0
- **标题**：International Technology Exchanger
- **首页栏目**：1 Place For Your IT Solution / Your Ultimate Destination for IT Solution / Trusted IT Experts, Transforming Businesses Since 2004. / 20+ Years of Excellence in IT Solutions. / 021-34598598 / 1234 / Explore Our Services / Request A Free Quote!
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：cisco 9、industrial 2
- **站内出现的品牌**：Cisco, Fortinet, Huawei, Ubiquiti, Juniper　（「（！）」= Saga 自家/供应商品牌已在其站内出现）
- **站内公开邮箱**：info@ite.net.pk
- **社媒**：https://htmlcodex.com
- **已抓子页**：[International Technology Exchanger](https://ite.net.pk/about.html)；[International Technology Exchanger](https://ite.net.pk/contact.html)；[International Technology Exchanger](https://ite.net.pk/service.html)
- 首页正文摘录：Loading... Home About Services Contact 021-34598598 Empowering Businesses with Cutting-Edge IT Solutions 1 Place For Your IT Solution driving innovation, security, and seamless connectivity. Read More Free Quote Your Trusted Partner in IT Excellence Your Ultimate Destination for IT Solution Delivering innovation, security, and uninterrupted connectivity. Read More Free Quote About Us Trusted IT Experts, Transforming 
- 数据文件：`data/saga_clients/site_snapshots/SB-029.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 4 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-04-09 | 2025.4.9 | 群发了22迷你 | have Routers with 1GE and 4 FE ports? | E |  | E Replied 2026.08.04.xlsx#5 |
| 2025-05-12 | 512 | 28poe |  | E |  | E Replied 2026.08.04.xlsx#5 |
| 2025-06-21 | 621 | 16电 |  | E |  | E Replied 2026.08.04.xlsx#5 |
| 2025-10-02 | 102 | dac |  | E |  | E Replied 2026.08.04.xlsx#5 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-24T07:26:33Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-029/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://ite.net.pk/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 2868 字符；首行：International Technology Exchanger |

## 联系方式（已有 · 原值照录）

- 邮箱：`info@ite.net.pk`〔企业邮箱；来源：用户表原值〕
- 邮箱：`sales@ite.net.pk`〔企业邮箱；来源：用户表原值〕
- 邮箱：`faisal@ite.net.pk`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Faisal Javed
- 网站/域名：ite.net.pk
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Faisal Javed | — | faisal@ite.net.pk / +92 21 3459 8598 | 调研核实（公开页） | （本地 Clients/ 表格，无公开 URL） |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E Replied 2026.08.04.xlsx#总表:6 | 5 | https://ite.net.pk/network-switches/ | 巴基斯坦 | Faisal Javed | 富通天下 | switch | info@ite.net.pk <br>sales@ite.net.pk | faisal@ite.net.pk | 4 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：交换机兴趣 → STC-28DGGPM 起手（经销 20%）；路由器不供。 | $80.7 USD EXW（20% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 20%（经销/集成（类型待核）） |
| 备选2 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $181.2 USD EXW（20% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STC-28DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；20% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 1 次实质回复（对方认识我们）
- **W**：南亚：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STC-28DGGPM 按 20% 档报价，做现供应商的第二货源
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
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STC-28DGGPM - 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks (Marvell-based, neutral label)

```text
Hi Faisal,

Picking up our earlier exchange about PoE / industrial switches. Faisal, we don't do routers — but for the switch side, the 8-PoE + 2-SFP managed (Marvell) is in stock from 1 pc; is that useful for the same projects, or is it routers only right now?

We supply a Marvell-based 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks - model STC-28DGGPM - that fits the same slot as the usual Taiwan-grade units at a lower landed cost, and we can ship it under your own label with neutral packaging. Current price: $80.7 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Are PoE / industrial switches something you still source today, or has that line been dropped?

If useful, I can send one unit for a 30-day side-by-side test. If not a fit, one line and I close the loop.

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

- **2026-11-23**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 59）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
