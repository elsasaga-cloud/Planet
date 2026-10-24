# actelis.com
**官方名称（调研核实）**：Actelis Networks, Inc.（NASDAQ: ASNS；actelis.com）

> **评级 B**　|　美国　|　档案编号 `SB-933`　|　优先级 ★★　|　状态：有回复·跟进中
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：实质回复 2 次；回复暂无需求 1 次；推送 15 次（2025-02-08 → 2025-12-30）　|　**所在清单**：S重点、用户判定不行　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-933
rating: B
rating_auto: B
name_official: "Actelis Networks, Inc.（NASDAQ: ASNS；actelis.com）"
score: 30
country: 美国
region: 北美
website: actelis.com
type: 经销/集成（类型待核）
tier_tags: ["S重点", "用户判定不行"]
deal: no
replies: 2
followups: 15
first_contact: 2025-02-08
last_contact: 2025-12-30
s_mail: 37 msgs (out 30 / in 7), 2024-06-21 -> 2026-09-08
p1: none
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-21
sources: 2
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：美国上市公司（NASDAQ: ASNS，1998 年成立，Fremont/Sunnyvale CA，51–200 人）：**混合光纤-铜缆**以太网接入设备（MetaLIGHT ML600/ML620/ML640Ex/ML684D、GigaLine GL800/GL900）、硬化 L2 光纤交换机与汇聚设备、网管与「cyber-hardened」安全；目标市场为联邦/州/地方政府、ITS、**军方、公用事业、铁路**、电信与园区。制造商兼潜在竞争者，且政府/军方导向意味着原产地与 TAA 门槛。用户表：S 重点，1 次实质回复，15 次跟进。（调研 2026-10-21；表内兴趣：工业FS 外壳比较独特；用的Edimax的工业FS）
- **为什么是 B 级**：+30 实质回复 2 次（问价/要资料/问型号等）；+6 有互动但表示暂无需求/已有供应商 1 次；+25 在 Simon 的 S 重点名单；-60 用户已归入「不行及不太相关的」；-12 备注提示大公司/上市公司/运营商（体量不匹配）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国；+5 最近活动 2025；+5 跟进表最近平台标记 S
- **历史互动**：实质回复 2 次；回复暂无需求 1 次；推送 15 次（2025-02-08 → 2025-12-30）；最近一次客户回复：1.4：info
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-4248XGGCM / 24 口 SFP 汇聚（2025-10 已给规格书） — 上市品牌商 + VP 直联 + 七次回复；$500 STI-42424XGGPM-4BT（2025-04）；汇聚款按 OEM 30% 档
- **第一问（只问一个）**：Casey — after your team reviewed the 24-port SFP aggregation spec and manual last October, was there a specific gap (features, certification, price) that kept it off the list?
- **最大未知**：年走量与现供应商
- **下一步**：现在 S 邮箱 → pchurley@actelis.com（回到 10G Enterprise SFP Switch 串） 一句话问评审结论

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-933` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度绑定（7 封实质来信、两年：2024-09 Casey「Maybe…」→ 2025-01 Michal 要数据表 + Casey「Let us review」→ 2025-04「How much are they?」→ $500 → 2025-08「keep you in mind」→ 2025-10 要规格书与手册 → 2026-03「Thank you…」；无样品无单）** ｜ 类型：美国上市宽带接入设备商（Actelis；Casey = VP Sales Strategic Accounts，Michal = 产品）——第一档品牌商，接入侧（铜/光宽带 + 工业以太网） ｜ 筛子：3（数据表 + 价格 + 手册，三次） ｜ 停点：每次对话都停在 Saga 发完资料之后：Casey 从不说「不」，只说「review / keep in mind」；Saga 从不问「评审结论是什么」——C10 一句话缺位 ｜ 复活：一句话问 2025-10 要走的 24 口 SFP 汇聚规格书/手册评审结果；并把 2026-09 新固件 7.5 的 L2+/IPv6 变化作为「有实质进展」的理由 ｜ 通路：US 主攻；品牌商 ｜ 节奏：季度一封只含实质进展的信；不发 PoE 小品 ｜ 证据：k=421dd559ac7a7b63（Maybe）；b591a174013b884b（Michal 要 datasheet）；4b1f19886629af5d（Let us review）；5f74509fff9d6018（How much）；d6394cf0f807b767（$500 STI-42424XGGPM-4BT）；ad286e0945b31160（keep in mind）；2818350b0dbd1e1a（spec sheet + manual）；840ce51782b3829d（Thank you…）；第 19 批回补来信原文 4 条（gmail_s/gmail_a）
- **现状一句话**：Casey 每隔几个月回一句，从「Maybe」到「How much」到「spec sheet and user manual」——七次回信没有一个「不」，但也没有一次 Saga 追问评审结果。Actelis 的产品是宽带接入（铜/光 + 工业），Saga 的 24 口 SFP 汇聚和工业 L3 PoE 对它是补线而非主线。
- **对方真实需求（有据）**：补线：24 口 SFP 汇聚（10G 上联）、工业 L3 PoE。
- **断点 / 为什么停在这里**：没有闭环问题。
- **Saga 现在该推什么**：P1 **STC-4248XGGCM / 24 口 SFP 汇聚（2025-10 已给规格书）**（30% 档，$500 STI-42424XGGPM-4BT（2025-04）；汇聚款按 OEM 30% 档）——上市品牌商 + VP 直联 + 七次回复
  - 做不了 / 要先核的：U；L；/；N；E；B；S； ；仓；库；明；确；无； ；→； ；若；对；方；要；求；则；直；接；回；「；无；」
- **下一步（具体）**：现在　S 邮箱 → pchurley@actelis.com（回到 10G Enterprise SFP Switch 串）　一句话问评审结论
  - 第一问（只问一个）：Casey — after your team reviewed the 24-port SFP aggregation spec and manual last October, was there a specific gap (features, certification, price) that kept it off the list?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-09-26 | 来 | pchurley@actelis.com | Maybe…. Best Regards, P. Casey Hurley VP Sales - Strategic Accounts Actelis Networks 732-477-7447 (C) 732-477-1606 (O) Technical Support - 1-866-638-2 | 来信原文（主题「RE: [External]8 Port 2.5G Switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `421dd559ac7a7b63` |
| 2025-01-03 | 来 | Michal Winkler | Thank you for approaching us. Can you please share a data sheet of the switch ? | 产品侧介入 | `b591a174013b884b` |
| 2025-01-04 | 来 | pchurley@actelis.com | Simon, Thank you for the information. Let us review. Best Regards, P. Casey Hurley VP Sales - Strategic Accounts Actelis Networks 732-477-7447 (C) 732 | 来信原文（主题「RE: [External]24 Port Fiber Switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `4b1f19886629af5d` |
| 2025-04-28 | 来 | Casey Hurley | How much are they? | 问价 | `5f74509fff9d6018` |
| 2025-08-27 | 来 | pchurley@actelis.com | Simon, Thank you. We will keep you in mind for future projects. Best Regards, P. Casey Hurley VP Sales - Strategic Accounts Actelis Networks 732-477-7 | 来信原文（主题「RE: [External]90W PoE Managed Switc」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `ad286e0945b31160` |
| 2025-10-29 | 来 | Casey | Do you have a spec sheet on this unit and a user manual? | 三次索资料 | `2818350b0dbd1e1a` |
| 2026-03-02 | 来 | pchurley@actelis.com | Thank you… Best Regards, P. Casey Hurley VP Sales - Strategic Accounts Actelis Networks 732-477-7447 (C) 732-477-1606 (O) Technical Support - 1-866-63 | 来信原文（主题「RE: [External]Updated Ethernet Swit」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `840ce51782b3829d` |

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | actelis.com（取自域名，公司全名待核） | 推断 |
| 国家 | 美国（另见：加拿大） | 事实（用户表）|
| 网站/域名 | actelis.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | 美国上市公司！ / Casey Hurley | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | 工业FS 外壳比较独特 / 用的Edimax的工业FS | 事实（用户表） |
| 用户备注（Remark） | 邮件中有详细的联系信息 | 事实（用户表） |
| 所在清单 | S重点、用户判定不行 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | FS | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：美国上市公司（NASDAQ: ASNS，1998 年成立，Fremont/Sunnyvale CA，51–200 人）：**混合光纤-铜缆**以太网接入设备（MetaLIGHT ML600/ML620/ML640Ex/ML684D、GigaLine GL800/GL900）、硬化 L2 光纤交换机与汇聚设备、网管与「cyber-hardened」安全；目标市场为联邦/州/地方政府、ITS、**军方、公用事业、铁路**、电信与园区。制造商兼潜在竞争者，且政府/军方导向意味着原产地与 TAA 门槛。用户表：S 重点，1 次实质回复，15 次跟进。
- **在卖/在用品牌**：Actelis（自产）
- **【官网】产品定位与市场**
  > Actelis Networks, Inc. (NASDAQ: ASNS) is a market leader in cyber-hardened, rapid-deployment networking solutions for wide-area IoT applications including federal, state and local government, ITS, military, utility, rail, telecom and campus applications. Actelis' unique portfolio of hybrid fiber-copper, environmentally hardened aggregation switches, high density Ethernet devices, advanced management software
  > 来源：https://www.sec.gov/Archives/edgar/data/1141284/000121390023035156/ea177800ex99-1_actelis.htm（抓取 2023-05-01）
- **【官网】光纤交换机产品线**
  > Actelis' fiber portfolio includes our managed layer 2 fiber switches and aggregation devices designed to extend connectivity over fiber, as well as our hybrid fiber-copper ethernet access devices
  > 来源：https://actelis.com/actelis-products/products-technology/fiber/（抓取 2023-02-03）
- **【LinkedIn】规模与成立年**
  > Actelis Networks … Company size: 51-200 employees Headquarters: Sunnyvale, California Type: Public Company Founded: 1998
  > 来源：https://www.linkedin.com/company/actelis-networks（抓取 2026-01-28）
- **【用户表】S 重点；1 次实质回复；15 次跟进**
  > （用户表字段）
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（官网 + 公告核对））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Actelis Networks, Inc.（NASDAQ: ASNS） |
| 成立 | 1998 |
| 总部/地址 | Fremont / Sunnyvale, California, USA |
| 其他 | 产品：ML600 系列 EAD（铜缆绑定 Ethernet，1–16 对，最高 240 Mbps）、ML684D 8 口硬化 DIN 混合交换机（2 SFP + 6 FE，−40~+75 ℃，12–48 VDC）、ML630R L3、GL800/GL900 千兆混合方案（2023-05）；客户案例含印度 Beetel/大型运营商 |

- **业务线**：混合光纤-铜缆以太网接入设备（EAD）；硬化 L2 光纤交换机与汇聚；网管与网络安全加固

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| Actelis | ML684D | 8 口硬化工业 DIN 混合光纤-铜缆管理交换机：2×100/1000 SFP + 6×10/100BT + 铜缆绑定，−40~+75 ℃，12–48 VDC 冗余 | —（铜缆绑定技术，Saga 无；纯以太网侧可对位 STI-280DGGM） | https://actelis.com/portfolio/ml684d/（2024-02-01） |
| Actelis | ML640Ex 系列 | 6 口硬化管理混合交换机，2×100/1000F + 4×100/1000BT，MACsec 256-bit（EL 型） | — | https://actelis.com/portfolio/ml640ex/（2024-02-07） |

- **触达通道（公开）**：网站: https://actelis.com/；LinkedIn: https://www.linkedin.com/company/actelis-networks
- **近况信号**：
  - 其「managed layer 2 fiber switches and aggregation devices」为标准以太网品类，理论上可外购 OEM；但政府/军方客户结构下中国产品难入
- **风险/边界**：守界：军方、铁路、联邦政府为其核心市场——Saga 不供；TAA/NDAA 原产地限制；上市制造商、潜在竞争者；S 重点但仅 1 次回复
- **Saga 对位结论**：P1 待核型（无标准对应）（30% 档）——待核型：唯一路径是面向其非政府商业/海外（如印度运营商）项目的 OEM 标准 L2 光纤汇聚交换机（STI-480XGGM / STC-424XGGM 口型，OEM 30% 档）；在对方明确非 TAA 用途前不报价
- **邮件切入句（英文）**：For the non-federal and overseas carrier projects where TAA does not apply, we can supply standard L2+ fibre aggregation switches (8×GE + 4×10G SFP+, −40 to +75 °C) under the Actelis label; is there such a programme where a second source would help?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://actelis.com/　语言：en-US　站点地图 URL 数：847
- **标题**：Home Page / Actelis Networks
- **描述**：Actelis' hybrid-fiber networking solutions enables immediate Gigabit, fiber-grade performance from any combination of newly deployed fiber infrastructure and existing copper and coaxial lines.
- **首页栏目**：Intelligent Traffic Systems / IoT-enabled Sites & Campuses / Smart Rail / Utilities / Multi-Dwelling Units / Smart City / Military / Connectivity For Apartments
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：switch 340、ethernet 203、gigabit 176、fiber 164、poe 102、sfp 88、10g 71、industrial 40、access control 7、camera 6、wifi 5、cable 4
- **站内型号串**（正则抽取，含非交换机）：GL900, GL800, GL6010, ML650SV, GL5020, GL5030, GL5060, GL5080, ML540E, ML540M, GL5070, GL6030
- **站内公开邮箱**：info@actelis.com
- **社媒**：https://twitter.com/actelis, https://www.facebook.com/Actelis/, https://www.linkedin.com/company/actelis-networks/, https://www.youtube.com/channel/UC1LgMhGApbpEhgylGLuOsRA
- **产品类页面**：https://actelis.com/actelis-enters-industrial-ethernet-switching-market/；https://actelis.com/ml5114d-actelis-new-fiber-based-industrial-14-gigabit-port-managed-ethernet-switch-and-ext…；https://actelis.com/actelis-announces-availability-of-its-first-two-industrial-ethernet-switches-provides-reli…；https://actelis.com/actelis-products/aggregation-switches-by-type/ml2300n/ml2300n-highlights/；https://actelis.com/industrial-video-surveillance-brief/；https://actelis.com/introducing-ml560m-actelis-10ge-ethernet-over-fiber-switch/
- **已抓子页**：[PoE Switches / Actelis Networks](https://actelis.com/ethernet-switch-portfolio/poe-switches/)；[Layer 3 Network Switches / Actelis Networks](https://actelis.com/ethernet-switch-portfolio/layer-3-network-switches/)；[MetaLIGHT 650SV](https://actelis.com/portfolio/ml650sv-high-performance-ethernet-switch-for-tdm-over-fiber/)；[Actelis Fiber Solutions Portfolio / Actelis Networks](https://actelis.com/actelis-fiber-solutions-portfolio/)；[GigaLine 800 / Actelis Networks](https://actelis.com/actelis-products-ethernet-access-devices-gl800/)；[Connectivity for Multi-Dwelling Units GigaLine 900](https://actelis.com/actelis-products-ethernet-access-devices-gl900/)
- 首页正文摘录：Skip to content info@actelis.com My Actelis Log In Menu My Actelis Log In Industries Intelligent Traffic Systems Anticipate & fast reaction to Incidents city-wide IoT-enabled Sites & Campuses Unlocking connectivity hidden in airport, factory, hospital & campus networks Smart Rail Transform existing rail communications Infrastructure Utilities Secure, responsive, energy, oil, gas and water communication networks Multi
- **自动对位建议**：STI-288GP（官网快照对位：工业/自动化词频 40、PoE 102 → DIN 8 PoE+ 2 SFP 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SB-933.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 15 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-02-08 | 2025.2.8 | 28poe |  | S |  | S 09.08.xlsx#8 |
| 2025-03-28 | 328 | 芯片 |  | S |  | S 09.08.xlsx#8 |
| 2025-04-29 | 429 | 4 24 |  | S |  | S 09.08.xlsx#8 |
| 2025-05-27 | 527 | bypass |  | S |  | S 09.08.xlsx#8 |
| 2025-06-25 | 625 | alarm |  | S |  | S 09.08.xlsx#8 |
| 2025-07-29 | 729 | 16电 |  | S |  | S 09.08.xlsx#8 |
| 2025-08-27 | 827 | 28bt | 有需求会说的 | S |  | S 09.08.xlsx#8 |
| 2025-10-30 | 1030 | dac |  | S |  | S 09.08.xlsx#8 |
| 2025-11-28 | 1128 | solar |  | S |  | S 09.08.xlsx#8 |
| 2025-12-30 | 1230 | taiwan |  | S |  | S 09.08.xlsx#8 |
| ? | 929 | 群发了18 2.5G | 可能有用 | Email |  | S 09.08.xlsx#8 |
| ? |  | 后续推了10G Ethernet型号 |  |  |  | S 09.08.xlsx#8 |
| ? | 1115 | 154 |  | Email |  | S 09.08.xlsx#8 |
| ? | 1212 | 48口 |  | Email |  | S 09.08.xlsx#8 |
| ? | 1.4 | 24fiber | info | Email |  | S 09.08.xlsx#8 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：37 封（去 30 / 来 7）　|　**期间**：2024-06-21 → 2026-09-08　|　**最后去信**：2026-09-08
- **对方邮箱**：info@actelis.com、michalw@actelis.com、pchurley@actelis.com
- **最后一封来信**：2026-03-02 pchurley@actelis.com「RE: [External]Updated Ethernet Switches Links」：Thank you… Best Regards, P. Casey Hurley VP Sales - Strategic Accounts Actelis Networks 732-477-7447 (C) 732-477-1606 (O) Technical Support - 1-866-638-2544 Skype - casey_hurley
- **邮件里报过的价**：2026-09-08 $170；2026-07-20 $1500；2025-10-29 $280；2025-04-29 $500（STI-42424XGGPM-4BT）；2025-01-03 $240；2024-12-12 $300；2024-11-25 $300；2024-08-19 $65

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 24 Port PoE Managed Switch | 2026-09-08 | 2026-09-08 | 0 | 1 | 1 |
| 24 Port 10G SFP+ Switch | 2026-07-20 | 2026-07-20 | 0 | 1 | 1 |
| Firmware 7.5 L2+ Feature Update | 2026-06-22 | 2026-06-22 | 0 | 1 | 2 |
| Updated Ethernet Switches Links | 2026-03-02 | 2026-03-02 | 1 | 1 | 1 |
| OEM Core Switching Solution | 2026-01-29 | 2026-01-29 | 0 | 1 | 1 |
| Optional Marvell Chipset Solutions | 2025-12-29 | 2025-12-29 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-28 | 2025-11-28 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-29 | 2025-10-30 | 1 | 2 | 5 |
| 90W PoE Managed Switch | 2025-08-27 | 2025-08-27 | 1 | 1 | 2 |
| 16 Port Ethernet Switch | 2025-07-28 | 2025-07-28 | 0 | 1 | 1 |
| Marvell Industrial Alert System | 2025-06-25 | 2025-06-25 | 0 | 1 | 1 |
| Managed Optical Bypass Switch | 2025-05-27 | 2025-05-27 | 0 | 1 | 1 |
| …共 26 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：6 个　|　**数据截至**：2026-10-24T04:35:40Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-933/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://actelis.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 11179 字符；首行：Home Page \| Actelis Networks |
| [sitemap](https://actelis.com/sitemap_index.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |
| [news_1](https://actelis.com/support/actelis-publications/articles/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 9944 字符；首行：Articles & Blog Posts Archives \| Actelis Networks |
| [news_2](https://actelis.com/category/in-the-news/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 14309 字符；首行：In The News \| Actelis Networks |
| [youtube](https://www.youtube.com/feeds/videos.xml?channel_id=UC1LgMhGApbpEhgylGLuOsRA) | rss | YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过） | 2026-10-23T04:20:51Z | YouTube 频道 https://www.youtube.com/channel/UC1LgMhGApbpEhgylGLuOsRA |
| [feed_auto](https://actelis.com/feed/) | rss | HTTP 200 | 2026-10-23T04:20:51Z | 10 条；最新：Wed, 19 Aug 2026 12:27:55 Actelis Networks Powers Broadband to Remote Alaska Schoo |

- **人工定期看（登录墙，不自动抓）**：Facebook: https://www.facebook.com/Actelis/；X/Twitter: https://twitter.com/actelis；LinkedIn: https://www.linkedin.com/company/actelis-networks/

## 联系方式（已有 · 原值照录）

- 邮箱：`info@actelis.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`pchurley@actelis.com`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：美国上市公司！ / Casey Hurley
- 网站/域名：actelis.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| —（未具名） | 公司级 | info@actelis.com / pchurley@actelis.com | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:actelis.com`, `e:info@actelis.com`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| S 09.08.xlsx#总表:9 | 8 | https://actelis.com/technology-2/copper-broadband-technologies/industrial-ethernet/ | 美国 | 美国上市公司！<br>Casey Hurley | 谷歌 | 工业FS 外壳比较独特 | info@actelis.com<br>pchurley@actelis.com | 邮件中有详细的联系信息 | 15 条 |
| 不行及不太相关的.xlsx#总表:709 |  | https://actelis.com/portfolio/gl5020/ | 加拿大 |  | 谷歌 | 用的Edimax的工业FS | info@actelis.com |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | 待核型（无标准对应，向 SmartByte 核） | 深挖对位：待核型：唯一路径是面向其非政府商业/海外（如印度运营商）项目的 OEM 标准 L2 光纤汇聚交换机（STI-480XGGM / STC-424XGGM 口型，OEM 30% 档）；在对方明确非 TAA 用途前不报价 | — | 深挖对位；档位 30%（经销/集成（类型待核）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $151.6 USD EXW（30% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $196.3 USD EXW（30% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STC-424DGGPM-280W 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 2 次实质回复（对方认识我们）；北美主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 — 按 30% 档报价，做现供应商的第二货源
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
| 采购量/预算 | ❓ 未确认（有回复但未报量） |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: 24-port SFP aggregation switch — one question

```text
Hi, Casey,

Last October your team asked for the spec sheet and user manual of our 24-port SFP aggregation switch (4x 10G uplinks) and we sent both. Since then no feedback — which usually means something did not fit.

If it is useful: the industrial L3 24-port PoE with 4x 10G SFP+ (STI-42424XGGPM-4BT) we priced at $500 USD in April 2025 still stands within 15 days of this mail; the aggregation SFP box is priced on request for OEM quantities.

One question: was there a specific gap — a feature, a certification (UL/NEBS), or price — that kept the 24-SFP unit off your list? A one-line answer is enough; it tells us whether to keep investing in Actelis.

Thank you.
Simon
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-23**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 B，分数 30）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
