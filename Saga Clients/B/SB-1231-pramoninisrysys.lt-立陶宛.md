# pramoninisrysys.lt

> **评级 B**　|　立陶宛　|　档案编号 `SB-1231`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：智能电网 RTU 制造商兼网店（立陶宛，工业 FS 为配套；仅民用口径）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：群发(筛选后质量一般的_群发)、表:Italy　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-1231
rating: B
rating_auto: B
score: 25
country: 立陶宛
country_table: 意大利  # 表内原填；调研纠正为 立陶宛（research JSON country_fix）
region: 欧洲
website: pramoninisrysys.lt
type: 智能电网 RTU 制造商兼网店（立陶宛，工业 FS 为配套；仅民用口径）
tier_tags: ["群发(筛选后质量一般的_群发)", "表:Italy"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 2 msgs (out 2 / in 0), 2024-11-15 -> 2024-12-13
p1: STI-280GE
price_tier: 25%
research: done
site_snapshot: ok  # 2026-10-21
sources: 1
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：立陶宛 Elseta（pramoninisrysys.lt 为 Elseta 在线商店：面向配电网/公用事业智能电网数字化——Mini RTU、转换器、I/O 模块、软件；表内国别「意大利」有误（.lt 域名、Elseta 为立陶宛公司）；表内「Beijer sbjlink 的工业 FS」「质量一般」）；表内未跟进。（调研 2026-10-21；表内兴趣：Beijer sbjlink的工业FS）
- **为什么是 B 级**：-6 群发批次名单；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/意大利
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-25）**：STI-280GE — RTU 配套工业 FS（现 Beijer/Westermo 系）→ 工业 8 GE + 2 SFP 管理 STI-280GE（$48.6 @25%）/ 5 GE STI-050GE（$17.8）；IEC 61850-3 Saga 无（注明）。已打开的主题（1/2 封有打开记录）：「Industrial PoE Switch」(2024-11-15) → 读者兴趣偏「工业」；与 P1 同类，继续；按主表（研究档 saga_fit）；群发里他已看到的价（续，第 66 批全量复核）：2024-12-13 $300（48 Port PoE Managed Switch）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-08-31 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-08-31；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170）
- **第一问（只问一个）**：For the industrial switches bundled with your Mini RTU and converter kits, we supply DIN-rail 5-GE and 8-GE + 2 SFP units (−40~75 °C, redundant 12–57 V input, CE/RoHS; the managed 8-GE on a Marvell platform) from single units, EXW USD — which port count do your DNO substation kits use most?
- **最大未知**：年走量与现供应商
- **下一步**：群发节奏 A 邮箱 观察打开

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-25）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-1231` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-25。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未触达（S 邮箱 2 封 2024，1 次记录打开，0 回；收件 info@pramoninisrysys.lt；主题多为「Industrial PoE Switch、48 Port PoE Managed Switch」）；Elsa 群发 BCC 已触达 2026-08-31「24 Port PoE Managed Switch」，正文「Price: 170USD/PC」，IT 批次 To INFO@sarcitalia.it，0 回（第 73 批(o) Bcc 头核对 msg 1a057bf756774b15）** ｜ 类型：智能电网 RTU 制造商兼网店（立陶宛，工业 FS 为配套；仅民用口径） ｜ 筛子：1~2（1 次打开） ｜ 停点：只打通用邮箱，无记录打开 ｜ 复活：保持季度群发到 2027-Q1；无打开即停 ｜ 通路：立陶宛（欧洲全域主攻） ｜ 节奏：季度 ｜ 证据：gmail_digest：out 2，Opened 标签 1（Simon 群发追踪）；用户表：「Beijer sbjlink的工业FS」；研究档 risks：守界备注：公用事业/配电网场景——只供民用通用工业交换机，IEC 61850-3 认证 Saga 无；data/gmail_e/bcc_batches_2026.json；批次时间线：同批次（To INFO@sarcitalia.it）2025-04-01→2026-08-31 共 9 轮群发（Marvell Alleycat5 Solution、8 Port Industrial PoE Switch、Commercial PoE Switch、48 Port PoE Managed Switch、16 Port Ethernet Switch、10G Enterprise SFP Switch、Industrial PoE Switch、OEM Core Switching Solution、24 Port PoE Managed Switch），本户在首尾两轮 Bcc 名单内，名单稳定、中间轮次按同名单推断
- **现状一句话**：立陶宛 Elseta（pramoninisrysys.lt 为 Elseta 在线商店：面向配电网/公用事业智能电网数字化——Mini RTU、转换器、I/O 模块、软件；表内国别「意大利」有误（.lt 域名、Elseta 为立陶宛公司）；表内「Beijer sbjlink 的工业 FS」「质量一般」）；表内未跟进。
- **对方真实需求（有据）**：RTU 配套工业 FS（现 Beijer/Westermo 系）→ 工业 8 GE + 2 SFP 管理 STI-280GE（$48.6 @25%）/ 5 GE STI-050GE（$17.8）；IEC 61850-3 Saga 无（注明）
- **断点 / 为什么停在这里**：守界备注：公用事业/配电网场景——只供民用通用工业交换机，IEC 61850-3 认证 Saga 无
- **Saga 现在该推什么**：P1 **STI-280GE**（25% 档，按主表（研究档 saga_fit）；群发里他已看到的价（续，第 66 批全量复核）：2024-12-13 $300（48 Port PoE Managed Switch）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-08-31 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-08-31；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170））——RTU 配套工业 FS（现 Beijer/Westermo 系）→ 工业 8 GE + 2 SFP 管理 STI-280GE（$48.6 @25%）/ 5 GE STI-050GE（$17.8）；IEC 61850-3 Saga 无（注明）。已打开的主题（1/2 封有打开记录）：「Industrial PoE Switch」(2024-11-15) → 读者兴趣偏「工业」；与 P1 同类，继续
- **下一步（具体）**：群发节奏　A 邮箱　观察打开
  - 第一问（只问一个）：For the industrial switches bundled with your Mini RTU and converter kits, we supply DIN-rail 5-GE and 8-GE + 2 SFP units (−40~75 °C, redundant 12–57 V input, CE/RoHS; the managed 8-GE on a Marvell platform) from single units, EXW USD — which port count do your DNO substation kits use most?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-12-13 | 去 | S 群发 | Industrial PoE Switch、48 Port PoE Managed Switch | 2 封 / 1 次打开 / 0 回｜首封 2024-11-15 → 末封 2024-12-13（2 去 / 0 来） | `gmail_digest` |
| 2025-04-01 | 去 | Elsa 群发（BCC；To INFO@sarcitalia.it，IT 批次） | Marvell Alleycat5 Solution — We are doing Marvell Alleycat5 chip for tailored networking solutions. 1, Support Web GUI change(Logo, model name, MAC, SN, SNMP, OID) 2, Added intere | Elsa 箱群发 BCC 触达证据（命中地址 info@pramoninisrysys.lt, pramoninisrysys.lt）；S/A digest 看不到 Elsa 的 BCC，之前据此写的「未发信/未触达」不成立 | `elsa_bcc` |
| 2026-08-31 | 去 | Elsa 群发（BCC；To INFO@sarcitalia.it，IT 批次） | 24 Port PoE Managed Switch — Marvell AC5 L2+ 24 PoE af/at + 10G uplinks, OEM/Web GUI; Price: 170USD/PC | Elsa 箱群发 BCC 触达证据（命中地址 info@pramoninisrysys.lt, pramoninisrysys.lt）；S/A digest 看不到 Elsa 的 BCC，之前据此写的「未发信/未触达」不成立 | `elsa_bcc` |
| 2026-10-21 | 用户表 | Simon | Beijer sbjlink的工业FS | 表内备注 | `用户表` |

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | pramoninisrysys.lt（取自域名，公司全名待核） | 推断 |
| 国家 | 立陶宛 | 事实（用户表）|
| 网站/域名 | pramoninisrysys.lt | 事实（用户表 URL/邮箱域名） |
| 类型 | 智能电网 RTU 制造商兼网店（立陶宛，工业 FS 为配套；仅民用口径） | 推断（据兴趣/备注关键词） |
| 联系人 | 质量一般 | 事实（用户表） |
| 来源（From） | — | 事实（用户表） |
| 兴趣（Interested in） | Beijer sbjlink的工业FS | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | 群发(筛选后质量一般的_群发)、表:Italy | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | FS | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线（pramoninisrysys.lt，快照 2026-10-21）
- **是谁**：立陶宛 Elseta（pramoninisrysys.lt 为 Elseta 在线商店：面向配电网/公用事业智能电网数字化——Mini RTU、转换器、I/O 模块、软件；表内国别「意大利」有误（.lt 域名、Elseta 为立陶宛公司）；表内「Beijer sbjlink 的工业 FS」「质量一般」）；表内未跟进。
- **类型**：智能电网 RTU 制造商兼网店（立陶宛，工业 FS 为配套；仅民用口径）
- **在卖/在用品牌**：Beijer, Westermo
- **【官网快照】官网标题：Elseta online shop；品类词 工业自动化 / OT 网络 / 网络交换 / PoE**
  > This is the place to buy Elseta products directly worldwide. Everything for DNO and Utilities smart Grid digitalization.
  > 来源：https://shop.elseta.com（抓取 2026-10-21）
- **【用户表】表内兴趣/备注**
  > Beijer sbjlink的工业FS
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【官网快照】Elseta 定位**
  > Elseta online shop ; Everything for DNO and Utilities smart Grid digitalization ; Digitalizing energy & Simplifying complexity ; Mini RTU
  > 来源：https://shop.elseta.com（抓取 2026-10-21）
- **【用户表】Beijer 工业 FS**
  > Beijer sbjlink的工业FS；质量一般
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- 备注：（无首轮调研；由 deepen.py 建档） ｜ 规则加厚 2026-10-21（autodeep.py；T 档 T4）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（人工复核：官网快照逐家核对 + 表内；T4/T5 信号优先））

| 公司事实 | 内容 |
|---|---|
| 总部/地址 | 意大利 |
| 其他 | 官网 pramoninisrysys.lt，语言 en-US，快照状态 ok；角色判定来源：官网文案 |

- **业务线**：智能电网 RTU / 转换器 / I/O（自有品牌 Elseta）
- **触达通道（公开）**：role: 智能电网 RTU 制造商兼网店（立陶宛，工业 FS 为配套；仅民用口径）；region: 立陶宛；contact: info@pramoninisrysys.lt
- **近况信号**：
  - 官网：Elseta online shop ; This is the place to buy Elseta products directly worldwide. Everything for DNO and Utilities smart Grid digitalization ; Mini RTU；页面 /shop/category/rtu-s-1、/shop/category/converters-4
  - 表内：Beijer sbjlink 的工业 FS；质量一般
- **风险/边界**：守界备注：公用事业/配电网场景——只供民用通用工业交换机，IEC 61850-3 认证 Saga 无；小国（立陶宛）；国别已更正（表内误填意大利）；Beijer/Westermo 价格基准高但品牌粘性强；表内「质量一般」
- **Saga 对位结论**：P1 STI-280GE（25% 档）——RTU 配套工业 FS（现 Beijer/Westermo 系）→ 工业 8 GE + 2 SFP 管理 STI-280GE（$48.6 @25%）/ 5 GE STI-050GE（$17.8）；IEC 61850-3 Saga 无（注明）
- **邮件切入句（英文）**：For the industrial switches bundled with your Mini RTU and converter kits, we supply DIN-rail 5-GE and 8-GE + 2 SFP units (−40~75 °C, redundant 12–57 V input, CE/RoHS; the managed 8-GE on a Marvell platform) from single units, EXW USD — which port count do your DNO substation kits use most?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://shop.elseta.com　语言：en-US　站点地图 URL 数：67
- **标题**：Elseta online shop
- **描述**：This is the place to buy Elseta products directly worldwide. Everything for DNO and Utilities smart Grid digitalization.
- **首页栏目**：Digitalizing energy & Simplifying complexity / Mini RTU
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：industrial 4、automation 4、cable 2、switch 1、fiber 1、wifi 1
- **站内型号串**（正则抽取，含非交换机）：RS232, RS485, RS422, CT-1A, CT-5A, VT-100V, VT-400V
- **站内公开邮箱**：austa@elseta.com, info@elseta.com
- **产品类页面**：https://shop.elseta.com/shop/category/rtu-s-1；https://shop.elseta.com/shop/category/software-3；https://shop.elseta.com/shop/category/converters-4；https://shop.elseta.com/shop/category/i-o-modules-2；https://shop.elseta.com/shop/category/accessories-5；https://shop.elseta.com/shop/product/clmod6-elseta-clmod6-25
- **已抓子页**：[Contact Us / Elseta](https://shop.elseta.com/contactus)；[Shop / Elseta](https://shop.elseta.com/shop)
- 首页正文摘录：Elseta Home Shop Contact us My Cart Sign in Digitalizing energy & Simplifying complexity Mini RTU Mini RTU by Elseta is the most versatile modular solution for secondary substation automation for distribution network operators, utility companies, and factories. Elseta’s mini RTU solution is based on WCC Lite and optional I/O modules Read more Protocol Analyzer & Converter Simply a unique tool for commissioning engine
- **自动对位建议**：STI-280GE（官网快照对位：工业/自动化词频 8、无 PoE 侧重 → DIN 8 GE + 2 SFP 非 PoE 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SB-1231.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：2 封（去 2 / 来 0）　|　**期间**：2024-11-15 → 2024-12-13　|　**最后去信**：2024-12-13
- **对方邮箱**：info@pramoninisrysys.lt
- 对方从未回信（全部为我方去信）
- **邮件里报过的价**：2024-12-13 $300

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 48 Port PoE Managed Switch | 2024-12-13 | 2024-12-13 | 0 | 1 | 1 |
| Industrial PoE Switch | 2024-11-15 | 2024-11-15 | 0 | 1 | 1 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：2 个　|　**数据截至**：2026-10-24T07:26:33Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-1231/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://shop.elseta.com) | html | HTTP 200 | 2026-10-23T04:20:51Z | 1545 字符；首行：Elseta online shop |
| [sitemap](https://shop.elseta.com/sitemap.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 67 个 URL；最新 lastmod 2023-03-16 |

## 联系方式（已有 · 原值照录）

- 邮箱：`info@pramoninisrysys.lt`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：质量一般
- 网站/域名：pramoninisrysys.lt
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| —（未具名） | 公司级 | info@pramoninisrysys.lt | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E/群发/筛选后质量一般的_群发.xlsx#Italy:3 | 2 | http://www.pramoninisrysys.lt/page/en/eshop/industrial-converters-rs232-serial-rs422-rs485-ethernet-rj45?sid=02NWb5BHm4t5T5f& | 意大利 | 质量一般 |  | Beijer sbjlink的工业FS | info@pramoninisrysys.lt |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-280GE | 深挖对位：RTU 配套工业 FS（现 Beijer/Westermo 系）→ 工业 8 GE + 2 SFP 管理 STI-280GE（$48.6 @25%）/ 5 GE STI-050GE（$17.8）；IEC 61850-3 Saga 无（注明） | $48.6 USD EXW（25% 档，SmartByte LT-IS3010G-2GX8GT 260 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（智能电网 RTU 制造商兼网店（立陶宛，工业 FS 为配套；仅民用口径）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-280GE），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STI-280GE 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：欧洲主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STI-280GE 按 25% 档报价，做现供应商的第二货源
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
| 现用/在卖交换品牌 | ✅ FS |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STI-280GE - industrial DIN-rail switch (neutral label)

```text
Hello,

Over the past months you had a few product mails from us - most recently "24 Port PoE Managed Switch" on 31 August 2026 - and there was no reason to answer a mass mail. This one is specific. For the industrial switches bundled with your Mini RTU and converter kits, we supply DIN-rail 5-GE and 8-GE + 2 SFP units (−40~75 °C, redundant 12–57 V input, CE/RoHS; the managed 8-GE on a Marvell platform) from single units, EXW USD — which port count do your DNO substation kits use most?

We supply an industrial DIN-rail switch, 8x Gigabit plus 2 SFP (unmanaged) - model STI-280GE - that fits the same slot as the units you source today at a lower landed cost, and we can ship it with neutral packaging. Current price: $48.6 USD EXW (price snapshot 2026-10-17, valid 15 days).

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

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 25）

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
