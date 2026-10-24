# telexcell.com
**官方名称（调研核实）**：Telexcell Infranet Solutions Pvt. Ltd.（印度孟买）

> **评级 C**　|　印度　|　档案编号 `SC-1538`　|　优先级 —　|　状态：WhatsApp 已加·未回复
>
> **类型**：印度系统集成/贸易商（推断）　|　**历史关系**：WhatsApp 已加　|　**所在清单**：AI评估(IN)·DONE　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-1538
rating: C
rating_auto: C
name_official: "Telexcell Infranet Solutions Pvt. Ltd.（印度孟买）"
score: 4
country: 印度
region: 南亚
website: telexcell.com
type: 印度系统集成/贸易商
tier_tags: ["AI评估(IN)·DONE"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 13 msgs (out 8 / in 5), 2025-04-09 -> 2026-09-16
p1: STC-28DGGPM / STC-424XGGPM-280W / STI-41616XGGPM
price_tier: 25%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：A 邮箱 2026-05 → 09 实质往来 13 封：Tarun Jain Lalwani（Director Sales）2026-07-29 发正式 RFP（8 口 ×100 / 24 口 ×20 / 16 口工业 ×100，均要 AC+DC 双电、L2+ PoE、1G/10G SFP+），Alan 当日回规格书但拒报价（「prices after reviewing… PCBs soaring」），之后无下文；2026-09-16 同司 jmkl 又问 Cisco IP 话机 200 台/型 → 贸易商特征。（调研 2026-10-24；表内兴趣：MC FS 光纤 网络）
- **为什么是 C 级**：+2 在 AI 客户评估名单；-15 AI/Claude 评估 C；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-6 区域 南亚/印度；C 级细分：低价值区域冷线索
- **历史互动**：WhatsApp 已加
- **P1**：不推（C 级）；若对方主动来询，起手 STC-28DGGPM / STC-424XGGPM-280W / STI-41616XGGPM（深挖对位：RFP 规格与 Saga L2+ PoE 线基本对得上，差在电源形态。）
- **最大未知**：年走量与现供应商
- **下一步**：2026-11（印度 Q3 财年前）；若 Simon 不想做印度价格战则「不动」 A 邮箱（Tarun 直邮 tarun@telexcell.com；WhatsApp +91-8828269065 已加） 只补上当时没给的三行预算价 + 一句「DC 输入版可按项目定制」，问项目是否还在

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SC-1538` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达→有 RFP 无报价（A 邮箱 2026-05-16 → 07-29 来 5 去 7：ERPS 功能问答 → 07-29 正式 RFP 两份合规表（8 口 ×100、24 口 ×20、16 口工业 ×100，要 AC+DC 双电、L2+ PoE、1G/10G SFP+）；Alan 当日回 6 份规格书但「prices after reviewing」未报价 → 断；09-16 另一人问 Cisco IP 话机 200 台/型；用户表「WhatsApp 已加·未回复」)** ｜ 类型：印度集成/贸易商（Telexcell Infranet，孟买；项目型 RFP + 杂货询价并存） ｜ 筛子：2（技术预审 + 正式 RFP；未到报价） ｜ 停点：Alan 2026-07-29 不给价（「PCBs and memory prices are soaring」）；电源形态不符（8 口要 -48V DC 电信电源，24 口要 AC+DC 双输入）；用户表 C 级「低价值区域冷线索」 ｜ 复活：同一项目若再招（印度电信/园区 PoE 环网）；或 Simon 愿意给三型号预算价让他填合规表 ｜ 通路：IN 无先例记录（Elsa 线对 HFCL 有 AWB 先例可借）；-48V DC 电源版要向 HRUI/SmartByte 确认是否有 DC 输入型 ｜ 节奏：— ｜ 证据：A 邮箱附件正文 `data/gmail_a/attachments/text/`（2026-10-24 对表）
- **现状一句话**：印度孟买 Telexcell（Tarun Jain Lalwani，Director Sales）2026-05 回 24 口 SFP 群发后先问 ERPS 清单，07-29 发正式 RFP：8 口 L2+ PoE（-48V DC 电信电源）×100、24 口 L2+ PoE（AC+DC）×20、16 口工业 L2+ PoE ×100，附两张合规表（含「Chipset Model & Part Code」栏）。Alan 当天回 6 份规格书、指出电源形态差异，但不报价。此后无任何来信；09-16 同司另一人要 Cisco IP 话机。
- **对方真实需求（有据）**：8 口 2×10G SFP+ L2+ PoE 120W（DC -32~-78V 输入、无风扇）×100；24 口 4×10G L2+ PoE 400W（AC+DC）×20；16 口 4×SFP 工业 L2+ PoE ×100；要合规表逐项 Yes/No + 芯片型号 + 转售价。
- **断点 / 为什么停在这里**：没有数字。220 台的 RFP 要的是「Transfer Pricing」，Alan 以元器件涨价为由不报 → 对方无法填标，线断。电源形态差异（-48V DC / AC+DC）是真缺口但可以写「DC 版按项目定制」而不是沉默。
- **Saga 现在该推什么**：P1 **8 口 → STC-28DGGPM（2.5G 上联，$99 列表；10G 上联版另询）；24 口 → STC-424XGGPM-280W（$198 列表，PoE 280W 低于其 400W 要求 → 可报 STC-424DGGPM-440W $220）；16 口工业 → STI-21616XGGPM（$324.5 列表，L2+）或 STI-41616XGGPM（$495，L3）**（% 档，按 `列表价 USD EXW（2026-10-17 快照，15 天有效）`：STC-28DGGPM $99 / STC-424DGGPM-440W $220 / STI-21616XGGPM $324.5；集成商 25% 档；-48V DC 版加价待 HRUI 确认后另报）——
- **下一步（具体）**：2026-11（印度 Q3 财年前）；若 Simon 不想做印度价格战则「不动」　A 邮箱（Tarun 直邮 tarun@telexcell.com；WhatsApp +91-8828269065 已加）　只补上当时没给的三行预算价 + 一句「DC 输入版可按项目定制」，问项目是否还在
  - 第一问（只问一个）：Tarun — is the July RFP (100 × 8-port, 20 × 24-port, 100 × 16-port industrial PoE) still open? Budget prices: 8-port L2+ PoE $99, 24-port 4×10G PoE 440W $220, 16-port industrial 4×10G PoE $324.5 USD EXW; the −48V DC input version is a project build — which site is this for?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-05-18 | 来 | Tarun Jain Lalwani（Director Sales） | List of Saga switches support (ERPS) Ethernet Ring Protection Switching (version ERPSv1 & ERPSv2) also called ITU-T G.8032/Y.1344. | 技术预审从 ERPS 开始 = 做运营商/园区环网项目 | `gmail_a 2026-05-18` |
| 2026-07-29 | 来 | Tarun Jain Lalwani | we are currently seeking support for the following requirements. 1) 8 Port + 2 SFP 1G/10G L2+ Managed POE Switch with DC & AC Power -100 2) 24 Port + 4 SFP 1G/10G L2+ Managed POE Switch with DC & AC Power - 20 3) 16 Port + 4 SFP 1G/10G L2+ Managed POE Switch with DC & AC Power (Industrial Grade) -100 Share the Compliant Product data sheets & Transfer Pricing. | 220 台、三型号、写明数量 = 真 RFP（不是问价） | `gmail_a 2026-07-29` |
| 2026-07-29 | 来 | Tarun（附件 Switch 8 x Gig + 2x SFP RFP.xlsx / 24 Port + 4 SFP POE Switch.xlsx） | 8 口：Fixed ports 8*10/100/1000M + 2*1G/2.5G/10G SFP+ · 56Gbps · Fan less · Power Supply DC: -32V~-78V · PoE Budget ≤120W · 0~50℃ · 4K VLAN/QinQ/GVRP/LLDP/ERPS 合规表（Yes/No + Chipset Model & Part Code）；24 口：128Gbps · 220V AC / 48V DC · PoE ≤400W · ≤430W 满载 | 8 口要 -48V DC 电信电源（-32~-78V）= 电信机房/基站配套；24 口要 AC+DC 双输入；要填芯片型号 = 招标合规表 | `gmail_a att sha（见 attachments/text）` |
| 2026-07-29 | 去 | Alan | 1) fine, but just single AC input, without DC input 2) fine, support single or dual AC input, without DC input 3) fine, but just dual DC input, without AC input … About 8 port model, it is a 2.5G based version. We can do 10G fiber uplink version … 2. Let's talk about prices after reviewing the shared information. As you know, the PCBs and memory prices are soaring. We will give a specified quotation if all discussion is good.（附 STC-28DGGPM / STC-424XGGPM-280W / STI-42424XGGPM-U / STI-41616XGGPM 规格书 + Saga Feature List 7.5.x L2+） | 规格基本对上，电源形态对不上；关键是拒报「Transfer Pricing」→ 对方拿不到数字无法填标 → 死 | `gmail_a 2026-07-29` |
| 2026-09-16 | 来 | jmkl@telexcell.com | Cisco ip phone Cp 7821 Cp 8811 Cp 8841 Cp 8845 Cp 8851 Cp 8861 All 200 units each | 同司另一人回 400G 群发却要 Cisco 话机 = 贸易商什么都问；不是 Saga 线 | `gmail_a 2026-09-16` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：C 级人工定级：建议 Simon 复核（有 220 台 RFP + 合规表 = 至少 B）；-48V DC 输入版是否可做：HRUI/SmartByte 未核；WhatsApp 上是否谈过价：只在 Simon 手机

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | telexcell.com（取自域名，公司全名待核） | 推断 |
| 国家 | 印度 | 事实（用户表）|
| 网站/域名 | telexcell.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 印度系统集成/贸易商 | 推断（据兴趣/备注关键词） |
| 联系人 | Tarun Lalwani / Director | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | MC FS 光纤 网络 | 事实（用户表） |
| 用户备注（Remark） | 91 88022 77996 <br>网站上的  已加 | 事实（用户表） |
| 用户 AI 评估 | AI 20% C | 事实（用户表 AI评估结果/CALUDE评估结果列） |
| 所在清单 | AI评估(IN)·DONE | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | FS | 事实（用户备注）/ 推断 |

### 用户 AI / Claude 评估原文

- **AI**（AI客户评估_IN 08.31.xlsx）：
  > 20% C
  > 官网产品信息不明确（主要展示services），备注提到MC、FS、光纤、网络等但无具体交换机产品展示；核心业务方向未确认，建议人工介入

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-24）**　网站状态：未查
- **是谁**：A 邮箱 2026-05 → 09 实质往来 13 封：Tarun Jain Lalwani（Director Sales）2026-07-29 发正式 RFP（8 口 ×100 / 24 口 ×20 / 16 口工业 ×100，均要 AC+DC 双电、L2+ PoE、1G/10G SFP+），Alan 当日回规格书但拒报价（「prices after reviewing… PCBs soaring」），之后无下文；2026-09-16 同司 jmkl 又问 Cisco IP 话机 200 台/型 → 贸易商特征。
- **类型**：印度系统集成/贸易商
- **在卖/在用品牌**：Cisco
- **KP**：Tarun Jain Lalwani（）tarun@telexcell.com +91-8828269065 / +91-9322037477〔A 邮箱签名 2026-05-16〕
- 备注：（建档：T29-U42 第 15 批，由 A 邮箱附件 RFP 触发；C 级人工定级不改，建议 Simon 复核升 B）

### 加厚挖掘（2026-10-24 · 仅邮件证据）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | TELEXCELL INFRANET SOLUTIONS PRIVATE LTD. |
| 总部/地址 | 印度 |

- **触达通道（公开）**：role: 集成/贸易；region: 印度
- **风险/边界**：AC+DC 双电输入 Saga 现货无（单 AC 或双 DC）；印度价格战；要 Transfer Pricing 却无项目名
- **Saga 对位结论**：P1 STC-28DGGPM / STC-424XGGPM-280W / STI-41616XGGPM（25% 档）——RFP 规格与 Saga L2+ PoE 线基本对得上，差在电源形态。
- **邮件切入句（英文）**：（见 mail_review）

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`jmkl@telexcell.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`tarun@telexcell.com`〔企业邮箱；来源：用户表原值〕
- 电话：`+918802277996`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Tarun Lalwani / Director
- 网站/域名：telexcell.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Tarun Jain Lalwani | — | tarun@telexcell.com / +91-8828269065 / +91-9322037477 | 调研核实（公开页） | A 邮箱签名 2026-05-16 |
| Tarun Lalwani | — | jmkl@telexcell.com / tarun@telexcell.com / +918802277996 | 用户表原值·WhatsApp 已加 | Clients/ 表 |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| AI客户评估/DONE/AI客户评估_IN 08.31.xlsx#总表:32 | 31 | http://www.telexcell.com/services.html# | 印度 | Tarun Lalwani<br>Director | 谷歌 | MC FS 光纤 网络 | Jmkl@telexcell.com<br>tarun@telexcell.com | 91 88022 77996 <br>网站上的  已加 | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：低价值区域冷线索。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-1538,B,理由` 后重跑即可。

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
| 现用/在卖交换品牌 | ✅ FS |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **不合格（见 C 级细分）→ 不主动跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: RFP (8/24/16-port PoE) — the prices we did not give in July

```text
Hi Tarun,

In July you sent a clear RFP (100 × 8-port, 20 × 24-port, 100 × 16-port industrial L2+ PoE) and we answered with datasheets but no numbers. That was our mistake. Budget prices, USD EXW (2026-10-17 snapshot, valid 15 days):

- 8-port L2+ PoE 120W + 2× 2.5G SFP: STC-28DGGPM $99 (10G-uplink version on request)
- 24-port L2+ PoE 440W + 4× 10G SFP+: STC-424DGGPM-440W $220
- 16-port industrial L2+ PoE + 4× 10G SFP+, -40 to +75 °C: STI-21616XGGPM $324.5

The −48 V DC input (−32 to −78 V) on the 8-port is a project build, not a stock item.

One question: is the RFP still open, and which site / operator is it for?

Best regards,
Alan
Saga Telecom · sagatele.com
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

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 4）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
