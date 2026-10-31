# Ugur Simsek Netmax
**官方名称（调研核实）**：Netmax（Uğur Şimşek，TR；无域名）

> **评级 B**　|　土耳其　|　档案编号 `SB-738`　|　优先级 ★★　|　状态：名单内·未触达
>
> **P 池并入（B 档，等级不动）：☆ P 池 · 观察档（试单 / 回访后转正或退回 C）**（批 AB-01 · 2026-10-29 · 下次巡检 2026-12-28）：☆ P 池观察（P 观察候选，B 档并池 · 等级不动）：真回 ✔ 但 未坐实 → 观察；命中 3/6（成单/样品 — · 真回 ✔ · WA — · 对位 ✔ 交换机 · 登记 未坐实 · 体量 小型（11–50））
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：ISAF2025展会、表:Ady　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-738
rating: B
rating_auto: B
sieve: pool_watch  # 闸 3 AB1 2026-10-29
name_official: "Netmax（Uğur Şimşek，TR；无域名）"
score: 32
country: 土耳其
region: 土耳其
website: none
type: 经销/集成（类型待核）
tier_tags: ["ISAF2025展会", "表:Ady"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STI-288DGGPM
price_tier: 25%
research: done
site_snapshot: none
sources: 2
updated: 2026-10-31
```

## SALES BRIEF（压缩模型）

- **是谁**：ISAF 记录：Uğur Şimşek / Netmax（无邮箱/域名）——Ady 加了 WhatsApp；问了 bypass，具体问了 2 光 8 电带 PoE 带管理的价格，现场报价 $120；无后续跟进。仅表内信息。映射：2 SFP + 8 GE PoE 管理型工业 = STI-288GPM（L2，$82.2）/ STI-288DGGPM（L2+，$137.5）；现场 $120 介于两者之间，报价前核价并说明层级；bypass 仅 4 SFP 版（SmartByte 型号注明）。（调研 2026-10-21；表内兴趣：Ady加了WhatsApp  问了bypass 具体问了2光8带POE带管理价格  报价120usd）
- **为什么是 B 级**：+12 备注记录了对方问价/要资料/见面等互动；+12 ISAF 2025 展会面对面名片；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；-8 无邮箱，仅电话/WhatsApp；+8 区域 土耳其/土耳其
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-288DGGPM — 工程 25% 档：STI-288DGGPM（DIN 2 SFP + 8 GE PoE+ L2+ ERPS，$137.5）；L2 版 STI-288GPM（$82.2）；ISAF 现场报 $120（层级待核，报价前核价）；bypass 版 SmartByte LT-IS6312GP-4GX8GT-FBP（$194.3；Saga 暂无对应型号）；按主表（研究档 saga_fit）（㉕ 封顶：STI-288DGGPM 档位价高于 2026-06 列表价，文本按列表价改；第 75 批 2026-10-25）
- **第一问（只问一个）**：Uğur Bey, ISAF'ta sorduğunuz 2 SFP + 8 port PoE yönetilebilir endüstriyel switch için net fiyat: L2 sürümü 82,2 USD, L2+ (ERPS halka) sürümü 137,5 USD EXW; bypass gerekiyorsa 4 SFP + 8 PoE bypass'lı model 194,3 USD — projeniz için hangisi?
- **最大未知**：公司网站（表内无域名，无法核实是否仍在运营）
- **下一步**：2026-11（Simon） A 邮箱首封 + WhatsApp（Simon） 首封 + 一句话（第 75 批(n)：信稿「ERPS」改「halka yedekli」——口径只说 ring redundancy）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-738` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（展会名片 + WhatsApp 已加，邮件 0 封）：用户表「Ady加了WhatsApp  问了bypass 具体问了2光8带POE带管理价格  报价120usd / Ugur Simsek Netmax」；S/A 邮箱 0 封；Elsa 箱无可查地址（仓内无此户任何邮箱/域名——用户表/WhatsApp/展会名片户，`from:e.sagatelecom to:` 无从下手；Elsa 群发是否碰过他无法判定，不写「未触达」）（第 74 批(o)）** ｜ 类型：— ｜ 筛子：3（已加 WhatsApp，表内有往来） ｜ 停点：仓库只有用户表一行；往来在 Simon 手机 ｜ 复活：首封邮件（A 邮箱，按 email_hook）+ WhatsApp 一句话 ｜ 通路：土耳其 非主攻 ｜ 节奏：一封 ｜ 证据：gmail_digest：out 0；用户表：「Ady加了WhatsApp  问了bypass 具体问了2光8带POE带管理价格  报价120usd / Ugur Simsek Netmax」；研究档 risks：现场报价与公式价差异需统一口径；bypass 缺口；无后续跟进
- **现状一句话**：ISAF 记录：Uğur Şimşek / Netmax（无邮箱/域名）——Ady 加了 WhatsApp；问了 bypass，具体问了 2 光 8 电带 PoE 带管理的价格，现场报价 $120；无后续跟进。仅表内信息。映射：2 SFP + 8 GE PoE 管理型工业 = STI-288GPM（L2，$82.2）/ STI-288DGGPM（L2+，$137.5）；现场 $120 介于两者之间，报价前核价并说明层级；bypass 仅 4 SFP 版（SmartByte 型号注明）。
- **对方真实需求（有据）**：工程 25% 档：STI-288DGGPM（DIN 2 SFP + 8 GE PoE+ L2+ ERPS，$137.5）；L2 版 STI-288GPM（$82.2）；ISAF 现场报 $120（层级待核，报价前核价）；bypass 版 SmartByte LT-IS6312GP-4GX8GT-FBP（$194.3；Saga 暂无对应型号）
- **断点 / 为什么停在这里**：现场报价与公式价差异需统一口径；bypass 缺口；无后续跟进
- **Saga 现在该推什么**：P1 **STI-288DGGPM**（25% 档，按主表（研究档 saga_fit）（㉕ 封顶：STI-288DGGPM 档位价高于 2026-06 列表价，文本按列表价改；第 75 批 2026-10-25））——工程 25% 档：STI-288DGGPM（DIN 2 SFP + 8 GE PoE+ L2+ ERPS，$137.5）；L2 版 STI-288GPM（$82.2）；ISAF 现场报 $120（层级待核，报价前核价）；bypass 版 SmartByte LT-IS6312GP-4GX8GT-FBP（$194.3；Saga 暂无对应型号）
- **下一步（具体）**：2026-11（Simon）　A 邮箱首封 + WhatsApp（Simon）　首封 + 一句话（第 75 批(n)：信稿「ERPS」改「halka yedekli」——口径只说 ring redundancy）
  - 第一问（只问一个）：Uğur Bey, ISAF'ta sorduğunuz 2 SFP + 8 port PoE yönetilebilir endüstriyel switch için net fiyat: L2 sürümü 82,2 USD, L2+ (ERPS halka) sürümü 137,5 USD EXW; bypass gerekiyorsa 4 SFP + 8 PoE bypass'lı model 194,3 USD — projeniz için hangisi?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-10-21 | 用户表 | Simon | Ady加了WhatsApp  问了bypass 具体问了2光8带POE带管理价格  报价120usd / Ugur Simsek Netmax | 表内备注 | `用户表` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：WhatsApp 往来未入库

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **发信窗口（TR 全库 901 封群发的打开标签，对方本地时间；均值 4.0%）**：周四 10–12 点 5.9%（51 封）、周一 10–12 点 5.2%（58 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **本国来询季节（TR 全库 17 个「户·月」真人来信，样本小）**：5 月 17.6% / 1 月 11.8% / 2 月 11.8%——本户来信太少，按本国节奏排下一步。
- **同国同档参照（TR，25% 档、主推线「工业 2.5G PoE 管理型」，共 1 户有动静，列前 3）**：SA-086 netas.com.tr（A，同档同线：成交 STI-488DGGPM-2BT，回过 24 次（最近 2026-08-12））。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-10-29 共和国日（10-28 下午起放）；2027-01-01 元旦（1 天） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**假日避让（土耳其 · 按下一步「2026-11」窗口 2026-11-01→2026-11-30）：**

- 窗口内无该国法定假日

**公司底数 · 第 91 批（TR · 1 次检索：LinkedIn 公司页（2016 起企业 + 个人互联网服务，11–50 人，Çerkezköy）+ D&B（法定全名；Gazi Mustafa Kemal Paşa Mah. Öztırak Cad. No:141 Çerkezköy 59500；Key Principal Ugur Simsek, Manager）+ TRNOG 社区名单（Uğur Şimşek = Netmax 代表），2026-10-27 查；https://www.linkedin.com/company/netmaxtr）：**

- 法定名 / 登记号：NETMAX TELEKOMÜNİKASYON İLETİŞİM HİZMETLERİ TİCARET LİMİTED ŞİRKETİ（Çerkezköy / Tekirdağ；ISP） · 未取（Mersis 未命中） · 状态 **Aktif** · 成立 2016 · Limited Şirket
- 行业码 / 经营范围：区域 ISP（有线 / 无线接入、企业专线；Tekirdağ Çerkezköy 工业区）
- 注册地址：Gazi Mustafa Kemal Paşa Mah. Öztırak Cad. No:141, 59500 Çerkezköy / Tekirdağ
- 规模档：小型（11–50）
- 账目：—；—
- 高管：Uğur ŞİMŞEK — Manager / 业主（D&B Key Principal；TRNOG 成员；研究档 ISAF 名片）= 老板 = 联系人（WhatsApp 已加）
- 控制人 / 股东：Şimşek（推定）
- **这意味着什么：**
  - **ISAF 名片上的 Uğur Şimşek 就是 Netmax 的老板，而 Netmax 是切尔凯兹柯伊工业区的 ISP —— ISP 买的是接入交换机 + 给无线 CPE 供电的 PoE，不是 CCTV 套装** → WhatsApp 一页价：STI-0240GE 24 口管理型 $130、光口上联 STC-110XGE $65、室外 PoE 供电款 STI-154GP；分销 20%、CE；TR 周四 10–12
  - 不说：不提 TRNOG
- 备注：研究档 KP Uğur Şimşek 角色补 Manager / 业主。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Ugur Simsek Netmax | 推断 |
| 国家 | 土耳其 | 事实（用户表）|
| 网站/域名 | — | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Ugur Simsek Netmax | 事实（用户表） |
| 来源（From） | — | 事实（用户表） |
| 兴趣（Interested in） | Ady加了WhatsApp  问了bypass 具体问了2光8带POE带管理价格  报价120usd | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | ISAF2025展会、表:Ady | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：无域名
- **是谁**：ISAF 记录：Uğur Şimşek / Netmax（无邮箱/域名）——Ady 加了 WhatsApp；问了 bypass，具体问了 2 光 8 电带 PoE 带管理的价格，现场报价 $120；无后续跟进。仅表内信息。映射：2 SFP + 8 GE PoE 管理型工业 = STI-288GPM（L2，$82.2）/ STI-288DGGPM（L2+，$137.5）；现场 $120 介于两者之间，报价前核价并说明层级；bypass 仅 4 SFP 版（SmartByte 型号注明）。
- **【用户表】ISAF：bypass；2 光 8 电 PoE 管理 $120；WA 已加**
  > Ady加了WhatsApp  问了bypass 具体问了2光8带POE带管理价格  报价120usd / Ugur Simsek Netmax
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Uğur Şimşek（Manager / 业主（D&B Key Principal；TRNOG 成员）= **老板 = 联系人**（WhatsApp 已加）—— 公司 = **Çerkezköy 工业区 ISP（2016 起，11–50 人）→ 要的是接入交换机 + 给无线 CPE 供电的 PoE，不是 CCTV 套装**：STI-0240GE $130 / STC-110XGE $65 / STI-154GP，分销 20%（第 91 批 官方登记核实 2026-10-27））— —（Ady WhatsApp）〔（本地 Clients/ 表格，无公开 URL）〕
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · 无域名 · 仅表内信息）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | NETMAX TELEKOMÜNİKASYON İLETİŞİM HİZMETLERİ TİCARET LİMİTED ŞİRKETİ（Mersis 未命中） |
| 成立 | 2016（LinkedIn）（第 91 批 官方登记核实 2026-10-27） |
| 总部/地址 | Gazi Mustafa Kemal Paşa Mah. Öztırak Cad. No:141, 59500 Çerkezköy / Tekirdağ（第 91 批 官方登记核实 2026-10-27） |
| 人数 | 11–50（LinkedIn）（第 91 批 官方登记核实 2026-10-27） |
| 其他 | WhatsApp 已加 |

- **业务线**：网络/安防工程或分销（推测）
- **触达通道（公开）**：WhatsApp: Ady 已加
- **近况信号**：
  - 已问到具体价格（$120）→ 需求真实；WhatsApp 直达
- **风险/边界**：现场报价与公式价差异需统一口径；bypass 缺口；无后续跟进
- **Saga 对位结论**：P1 STI-288DGGPM（25% 档）——工程 25% 档：STI-288DGGPM（DIN 2 SFP + 8 GE PoE+ L2+ ERPS，$137.5）；L2 版 STI-288GPM（$82.2）；ISAF 现场报 $120（层级待核，报价前核价）；bypass 版 SmartByte LT-IS6312GP-4GX8GT-FBP（$194.3；Saga 暂无对应型号）
- **邮件切入句（英文）**：Uğur Bey, ISAF'ta sorduğunuz 2 SFP + 8 port PoE yönetilebilir endüstriyel switch için net fiyat: L2 sürümü 82,2 USD, L2+ (ERPS halka) sürümü 137,5 USD EXW; bypass gerekiyorsa 4 SFP + 8 PoE bypass'lı model 194,3 USD — projeniz için hangisi?

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## B 分层（B-PASS-02 · 2026-10-31）：**B2**

- 依据：有回信（R+）；B-PASS-02 2026-10-31：Netmax（Uğur Şimşek）：无域名 → B2（不可挖）；身份 法定名 · 路径 弱 · 回信 R+ · 区域档 focus
- 节奏：B1 重点普通跟 = 分组群发每 6 周 + 一年两次点名；B2 普通跟 = 分组群发每 8 周；C 储备 = 不发、两月巡检，有动静捞回。

## 商业情报·挖底（A 类 · 截至 2026-10-30 · 1 条）

> 规则（Simon 2026-10-30）：A 类挖个底掉——年报 / 领英 / KP / 人事变动 / 展会 / 论坛 / GitHub …能挂上的都进仓库；一轮一轮补。未得也记，免得重复查。

**登记**

- 2026-10-30：TR · 1 次检索：LinkedIn 公司页（2016 起企业 + 个人互联网服务，11–50 人，Çerkezköy：NETMAX TELEKOMÜNİKASYON İLETİŞİM HİZMETLERİ TİCARET LİMİTED ŞİRKETİ（Çerkezköy / Tekirdağ；I · 未取（Mersis 未命中） · Aktif · 成立 2016 · Gazi Mustafa Kemal Paşa Mah. Öztırak Cad. No:141, 59500 Çerkezköy / Tekirdağ — <https://www.linkedin.com/company/netmaxtr>　*登记库镜像（公司底数 2026-10-27 批次）*

待挖：年报/财务、领英公司页、KP、人事变动、展会/活动、新闻/招标、GitHub/技术足迹（下一轮）

## 联系方式（已有 · 原值照录）

- 电话：`+905325710885`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Ugur Simsek Netmax
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Uğur Şimşek | Manager / 业主（D&B Key Principal；TRNOG 成员）= **老板 = 联系人**（WhatsApp 已加）—— 公司 = **Çerkezköy 工业区 ISP（2016 起，11–50 人）→ 要的是接入交换机 + 给无线 CPE 供电的 PoE，不是 CCTV 套装**：STI-0240GE $130 / STC-110XGE $65 / STI-154GP，分销 20%（第 91 批 官方登记核实 2026-10-27） | — / —（Ady WhatsApp） | 调研核实（公开页） | （本地 Clients/ 表格，无公开 URL） |
| Ugur Simsek Netmax | — | +905325710885 | 用户表原值 | Clients/ 表 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；无邮箱：只能电话 / WhatsApp / 官网表单

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`p:325710885`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/2025土耳其ISAF客户.xlsx#Ady:15 | 14 |  |  | Ugur Simsek Netmax |  | Ady加了WhatsApp  问了bypass 具体问了2光8带POE带管理价格  报价120usd | 90 532 571 0885 |  | — |
| A/2025土耳其ISAF客户.xlsx#Sheet1:21 | 49 |  |  | Ugur Simsek Netmax |  | Ady加了WhatsApp  问了bypass 具体问了2光8带POE带管理价格  报价120usd | 90 532 571 0885 |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-288DGGPM | 深挖对位：工程 25% 档：STI-288DGGPM（DIN 2 SFP + 8 GE PoE+ L2+ ERPS，$137.5）；L2 版 STI-288GPM（$82.2）；ISAF 现场报 $120（层级待核，报价前核价）；bypass 版 SmartByte LT-IS6312GP-4GX8GT-FBP（$194.3；Saga 暂无对应型号） | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（经销/集成（类型待核）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288DGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STI-288DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：土耳其主攻区，复购与口碑可外溢；ISAF 2025 面对面建立过联系
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STI-288DGGPM 按 25% 档报价，做现供应商的第二货源
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
| 触达通道 | ⚠️ 仅电话 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 公司网站（表内无域名，无法核实是否仍在运营）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：WhatsApp / 私信一句话（复制即发；不发邮件）

```text
Uğur Bey, ISAF'ta sorduğunuz 2 SFP + 8 port PoE yönetilebilir endüstriyel switch için net fiyat: L2 sürümü 82,2 USD, L2+ (halka yedekli) sürümü 137,5 USD EXW; bypass gerekiyorsa 4 SFP + 8 PoE bypass'lı model 194,3 USD — projeniz için hangisi?
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

> 客户语言一句话（研究档 email_hook；对方若不读英文，整段单发 WhatsApp/邮件）：Uğur Bey, ISAF'ta sorduğunuz 2 SFP + 8 port PoE yönetilebilir endüstriyel switch için net fiyat: L2 sürümü 82,2 USD, L2+ (ERPS halka) sürümü 137,5 USD EXW; bypass gerekiyorsa 4 SFP + 8 PoE bypass'lı model 194,3 USD — projeniz için hangisi?

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-30**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-31：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 B，分数 32）

---

*建档日期：2026-10-31　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
