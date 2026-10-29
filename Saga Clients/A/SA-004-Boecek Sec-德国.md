# Boecek Sec
**官方名称（调研核实）**：Boecek Sec（boecek.de，用户表原值）

> **评级 A**　|　德国　|　档案编号 `SA-004`　|　优先级 ★★★　|　状态：成交过·维护
>
> **P 池并入（A 档，等级不动）：★ P 池 · 正式入池（资产池，终身跟进 + 每 2 个月巡检）**（批 AB-01 · 2026-10-29 · 下次巡检 2026-12-28）：★ P 池正式（P 核心，A 档并池 · 等级不动）：A 档默认入池（长期跟进）；成单 / 样品 ✔；命中 3/6（成单/样品 ✔ · 真回 — · WA ✔ · 对位 ✔ 交换机 · 登记 未坐实 · 体量 未知）　|　标签：core（核心：成单 / 样品 / PI 或 A 档）
>
> **类型**：安防集成/经销（据用户备注推断）（推断）　|　**历史关系**：成交/下单过；WhatsApp 已加；推送 7 次（2025-04-14 → 2025-11-05）　|　**所在清单**：A优质名单(DE)、AI评估(DE)·DONE　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SA-004
rating: A
rating_auto: A
sieve: pool  # 闸 3 AB1 2026-10-29
name_official: "Boecek Sec（boecek.de，用户表原值）"
score: 131
country: 德国
region: 欧洲
website: boecek.de
type: 安防集成/经销（据用户备注推断）
tier_tags: ["A优质名单(DE)", "AI评估(DE)·DONE"]
deal: yes
replies: 0
followups: 7
first_contact: 2025-04-14
last_contact: 2025-11-05
s_mail: 15 msgs (out 15 / in 0), 2025-04-14 -> 2026-09-23
p1: STI-144GP
price_tier: 25%
research: done
site_snapshot: parked_or_empty  # 2026-10-29
sources: 2
updated: 2026-10-29
```

## SALES BRIEF（压缩模型）

- **是谁**：德国安防客户（用户表：买了 5 电口样品，需要一起买工业电源，问了 2 款 2.5G 价格，对机架式工业管理交换机有兴趣，需要支持…）。网页搜索未找到该域名的公开页面，公司规模/类型待用户侧确认。（调研 2026-10-21；表内兴趣：买了5电口样品，需要一起买工业电源，也问了拿的2款2.5G网的价格，对机架式工业管理有兴趣，需要能支持CLI管理，知道Aliexpress, 比较在意运费和进口税，展会结束时一直在扫货）
- **为什么是 A 级**：+50 有成单/下单/买过记录（用户备注或跟进表）；+10 谈到样品/测样；+12 备注记录了对方问价/要资料/见面等互动；+6 在 A/DONE 优质国家名单（已做过整轮推送）；+2 在 AI 客户评估名单；+15 AI/Claude 评估 A；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/德国；+5 最近活动 2025
- **历史互动**：成交/下单过；WhatsApp 已加；推送 7 次（2025-04-14 → 2025-11-05）
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-288GPM（8 口管理 DIN）+ STI-144GP（4+1 PoE） — 展会扫货后拿了 5 口工业样机 + DIN 电源 → 顺位是 8 口管理 DIN 与 4+1 PoE；他在意运费/关税 → 只报 EXW；锚价：STI-288GPM $82.2（25% 档）（第 72 批 2026-10-24）；—；群发里他已看到的价（续）：2026-08-18 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，2026-07-22→09-08 那轮；现价轮是 $180）——同款信稿写 $180 要点明 9 月前那封是 $170；群发里他已看到的价（续，第 66 批全量复核）：2025-06-09 $300（48 Port PoE Managed Switch）、2025-10-06 $280（10G Enterprise SFP Switch）
- **第一问（只问一个）**：Since you took the 5-port industrial samples with the DIN power supply, the natural next step is the 8-port managed DIN unit with CLI and the 4+1 PoE version, both quoted EXW so the freight and import-duty side is transparent. Are the 5-port samples still in service, and is the 8-port managed DIN unit worth a current quote? Reference: STI-288GPM at $82.2 USD EXW (MOQ 1, 15-day validity).
- **最大未知**：官网当前状态异常（停放/空站（疑停业或仅占位））——公司是否仍在运营待核
- **下一步**：2027-Q1（换人；A 级但邮件 0 回，用研究档 email_hook 一问） A 邮箱 → boecek@（先核地址是否有效；无具名 KP） 一问（研究档 email_hook + 价锚）；邮件 0 回的 A 级户按「换人」节奏，不加频（第 75 批(o) 2026-10-25：英文信稿已写 `draft_en`（2027-Q1 用；换人/一问口径）；钩子「CLI」不写——未核实）（第 76 批(e) 2026-10-25：薄档补时间线——邮箱索引去/来信 + 报价史 + Elsa 群发命中）（全量审计 2026-10-25 U57：署名对齐渠道邮箱）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SA-004` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未绑定（邮件 15 封 0 回、Opened 0；用户表「样品购买 + 型号问价」无 PI/邮件痕迹；Elsa 箱：`to:.de` 穷举 29 条（2026-10-25，锚批 Bcc 头已读）未见 boecek.de → Elsa 箱从未发过本户，往来只在 S/A 箱（去 15 / 来 0）（第 74 批(f)））** ｜ 类型：德国安防（boecek.de，实体不可核） ｜ 筛子：0（邮件层无人工回复） ｜ 停点：邮件从未被打开 ｜ 复活：核实实体后再定 ｜ 通路：DE ｜ 节奏：不主动 ｜ 证据：邮件：去信 15 封（2025-04-14 → 2026-09-23），来信 0；Opened 标签 0 次；收件人 boecek@boecek.de
- **现状一句话**：15 封邮件 0 打开 = 地址可能不活；用户表的样品购买在 PI 包里找不到。
- **对方真实需求（有据）**：5 口工业样机之后的 8 口管理 DIN / 4+1 PoE（用户表）
- **断点 / 为什么停在这里**：触达无效 + 证据缺失。
- **Saga 现在该推什么**：P1 **STI-288GPM（8 口管理 DIN）+ STI-144GP（4+1 PoE）**（25% 档，锚价：STI-288GPM $82.2（25% 档）（第 72 批 2026-10-24）；—；群发里他已看到的价（续）：2026-08-18 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，2026-07-22→09-08 那轮；现价轮是 $180）——同款信稿写 $180 要点明 9 月前那封是 $170；群发里他已看到的价（续，第 66 批全量复核）：2025-06-09 $300（48 Port PoE Managed Switch）、2025-10-06 $280（10G Enterprise SFP Switch））——展会扫货后拿了 5 口工业样机 + DIN 电源 → 顺位是 8 口管理 DIN 与 4+1 PoE；他在意运费/关税 → 只报 EXW
- **下一步（具体）**：2027-Q1（换人；A 级但邮件 0 回，用研究档 email_hook 一问）　A 邮箱 → boecek@（先核地址是否有效；无具名 KP）　一问（研究档 email_hook + 价锚）；邮件 0 回的 A 级户按「换人」节奏，不加频（第 75 批(o) 2026-10-25：英文信稿已写 `draft_en`（2027-Q1 用；换人/一问口径）；钩子「CLI」不写——未核实）（第 76 批(e) 2026-10-25：薄档补时间线——邮箱索引去/来信 + 报价史 + Elsa 群发命中）（全量审计 2026-10-25 U57：署名对齐渠道邮箱）
  - 第一问（只问一个）：Since you took the 5-port industrial samples with the DIN power supply, the natural next step is the 8-port managed DIN unit with CLI and the 4+1 PoE version, both quoted EXW so the freight and import-duty side is transparent. Are the 5-port samples still in service, and is the 8-port managed DIN unit worth a current quote? Reference: STI-288GPM at $82.2 USD EXW (MOQ 1, 15-day validity).

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-04-14 | 去 | Saga（Alan） | 「16 Port Ethernet Switch」——A 邮箱对 boecek@boecek.de 的第 1 封群发 | A 级（人工定）却从未有任何来信；15 封群发 2025-04→2026-09 无一次打开记录 | `f5b9385c457b416c` |
| 2025-04-14 | 去 | A 箱（Alan） | 16 Port Ethernet Switch | 首封去信（邮箱索引；去信共 15 封） | `f5b9385c457b416c` |
| 2026-08-18 | 去 | A 箱（Alan） | 24 Port PoE Managed Switch｜稿内价 $170 | 去信正文含价（邮箱索引） | `3711c54c803677ad` |
| 2026-09-23 | 去 | Saga（Alan） | 「Managed PoE Switches」——最后一封群发，仍是 boecek@ 公用地址 | 同一地址打了 17 个月；换人（找具名采购）比再发更有用 | `7c09d3b669698238` |
| 2026-09-23 | 去 | A 箱（Alan） | Managed PoE Switches | 最近一封去信（邮箱索引；去信共 15 封） | `7c09d3b669698238` |
| 2026-10-29 | 查 | Agent 复核 LT-R10 | DNS 2026-10-29 16:2xZ：boecek.de MX smtpin.rzone.de.；A 217.160.0.167；NS docks02.rzone.de. / shades02.rzone.de. | 长期客户群复核证据（非邮件事实，不计真回） | `` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：用户表「样品购买」无 PI；邮件 0 打开

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **发信窗口（DE 全库 922 封群发的打开标签，对方本地时间；均值 4.4%）**：周四 12–14 点 7.3%（41 封）、周二 08–10 点 6.7%（45 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **本国来询季节（DE 全库 15 个「户·月」真人来信，样本小）**：11 月 13.3% / 12 月 13.3% / 9 月 13.3%——本户来信太少，按本国节奏排下一步。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 15 封（2025-04-14 → 2026-09-23），打开标签 0 次；**最近连续 15 封没打开**（近 180 天发 5 封 0 打开）→ 群发对这户已失效，停两个月，改一句 1:1 或换收件人。
- **日历窗口**：对方：2026-12-24 圣诞–元旦（12-24 → 01-06，德国多数工厂整周停） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-29 查）：**

- `boecek.de` → 德国主机商邮箱（MX：smtpin.rzone.de）。主机商附带邮箱（德国主机商邮箱）：过滤弱、几乎不丢信，但常是老板自己收、没人代读 → 短、直接、一行型号 + 价格 + 一个问题

**假日避让（德国 · 按下一步「2027-Q1」窗口 2027-01-01→2027-03-31）：**

- 法定假日：01-01 New Year's Day；03-26 Good Friday；03-29 Easter Monday —— 假日前一个工作日下午、当天、长假后第一个上午都别发
- 【惯例】12-21→01-03：圣诞-新年停摆：多数公司 12-21 起只剩值班，决策人 1-04 以后才回
- 【供应侧】01-25→02-21：我方供应侧春节停摆：SmartByte / HRUI 工厂约 2-01→2-17 放假，1-25 前不锁单的 2 月出不了货，节后出货排队到 2 月底；任何「现在要货」的客户 1 月中就得催 PI

**公司底数 · 第 106 批（DE · 1 次检索未命中（boeck-technology.de / sicherheitstechnik-bock.de / cboeck.de / boeck-technik.de 均为同名他家，不采）→ 未坐实，按规程不补查；主体信息改由 Simon 侧样品订单的发票抬头 / 收货地址补，2026-10-28 查；）：**

- 法定名 / 登记号：Boecek Sec（boecek.de；用户表原值；德国）— 1 次检索未命中该域名的任何公开页面（同名 boeck GmbH Leipheim HRB 15558 / Sicherheitstechnik Bock Berlin / Böck Technik GmbH 均 ≠）→ 未坐实；A 级依据为 Simon 一手证据（买过 5 电口样品、要工业电源、问 2 款 2.5G 价、对机架式工业网管机有兴趣） · 未取 · 状态 **未知（域名无公开页）** · 成立 未取 · 未知
- 行业码 / 经营范围：安防（用户表）
- 注册地址：未取（德国）
- 规模档：未知
- 账目：—；—
- 高管：（未具名）— 用户表联系人（样品买家）
- 控制人 / 股东：未取
- **这意味着什么：**
  - **A 级维持（有样品订单 + 具体型号问价）；主体未坐实 → 下一封跟进顺手要一次「公司全称 + 送货地址 + 增值税号」（报价单需要，不突兀）**
  - **Simon 可做**：把该样品订单的发票抬头 / 收货地址 / VAT 号给我，底数当场补齐；2.5G 两款 + 机架式工业网管机（STI-288DGGPM / STI-488DGGPM）继续按 A 跟
- 备注：A 维持；未坐实（域名无公开页）；Simon 侧发票抬头可补。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Boecek Sec | 事实（用户表） |
| 国家 | 德国 | 事实（用户表）|
| 网站/域名 | boecek.de | 事实（用户表 URL/邮箱域名） |
| 类型 | 安防集成/经销（据用户备注推断） | 推断（据兴趣/备注关键词） |
| 联系人 | Boecek / Manager | 事实（用户表） |
| 来源（From） | 埃森展2024 | 事实（用户表） |
| 兴趣（Interested in） | 买了5电口样品，需要一起买工业电源，也问了拿的2款2.5G网的价格，对机架式工业管理有兴趣，需要能支持CLI管理，知道Aliexpress, 比较在意运费和进口税，展会结束时一直在扫货 | 事实（用户表） |
| 用户备注（Remark） | 49 17253 68536 已加 | 事实（用户表） |
| 用户 AI 评估 | AI 35% A | 事实（用户表 AI评估结果/CALUDE评估结果列） |
| 所在清单 | A优质名单(DE)、AI评估(DE)·DONE | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

### 用户 AI / Claude 评估原文

- **AI**（AI客户评估_DE 09.23.xlsx）：
  > 35% A
  > 德国小型安防/弱电集成商，展会上购买了5电口样品，对工业电源、2.5G交换机、机架式工业管理型交换机有兴趣，明确要求支持CLI管理（我司主场）。了解Aliexpress说明对中国供应链开放，关注运费和进口税。公司规模极小，决策链极短。
  > 发送CLI管理型工业交换机报价+运费/税务方案说明，强调我司CLI/MIB深度支持能力，推荐机架式工业管理型+2.5G产品
  > 机架式工业管理型交换机（CLI）、2.5G PoE交换机、5口工业交换机
  > 展会已购样品（有真实采购行为）；明确要求CLI管理（我司技术主场）；对中国供应链完全开放（用Aliexpress）；关注运费/进口税（需提供物流方案）；公司极小但需求明确

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：官网停放（boecek.de = STRATO「Domain reserved」占位页，2026-10-21 / 10-29 两次；域名与邮箱 MX 仍在）
- **是谁**：德国安防客户（用户表：买了 5 电口样品，需要一起买工业电源，问了 2 款 2.5G 价格，对机架式工业管理交换机有兴趣，需要支持…）。网页搜索未找到该域名的公开页面，公司规模/类型待用户侧确认。
- **类型**：安防集成/经销（据用户备注推断）
- **规模**：未知
- **【检索记录】2026-10-21 用 web_search 查「boecek.de Böcek Sicherheitstechnik Germany」无相关结果（返回同名无关公司 Sicherheitstechnik Bock / boeck GmbH）**
  > （无可引用原文）
  > 来源：https://www.google.com/search?q=boecek.de（抓取 2026-10-21）
- **【核查】boecek.de 不可访问；无公开页面**
  > Failed to fetch page (HTTP 500)
  > 来源：https://boecek.de/（抓取 2026-10-21）
- 备注：LT-T03 官网快照加厚（2026-10-29）：fail#2。
LT-T03 官网快照加厚（2026-10-21）：fail#1。
A 级维持：有样品购买 + 具体型号问价（用户一手证据）；网页无法核实不扣分，但「最大未知」= 公司实体与规模。

### 加厚挖掘（2026-10-21 · 深挖 v1（受限：无公开网页））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Boecek Sec（boecek.de；未坐实：域名无公开页；同名 boeck GmbH Leipheim HRB 15558 / Sicherheitstechnik Bock Berlin ≠） |
| 成立 | 未取（第 106 批 官方登记核实 2026-10-28） |
| 总部/地址 | 德国（用户表） |
| 其他 | boecek.de 2026-10-21 返回 HTTP 500；搜索引擎无该域名/公司的公开页面——属无公开网页的小型安防/网络安装商；第 106 批：**A 维持（样品订单 + 具体型号问价为 Simon 一手证据）**；主体改由 Simon 侧样品订单发票抬头 / 收货地址 / VAT 号补，或下一封跟进顺手要「公司全称 + 送货地址 + VAT」（第 106 批 官方登记核实 2026-10-28） |

- **业务线**：（用户表推断）安防/网络安装：买 5 电口工业样品 + 工业电源，问 2.5G 机型，要机架式工业管理型（CLI）

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| （样品） | 5 电口工业交换机 + 工业电源 | 展会现场采购的样品；关注 2.5G 与机架式工业管理型，要求 CLI | STI-144GP | （本地 Clients/ 表格，无公开 URL）（用户表） |

- **触达通道（公开）**：直邮: boecek@boecek.de（用户表）；网站: boecek.de（2026-10-21 HTTP 500，不可用）
- **近况信号**：
  - 用户表：展会结束时一直在扫货；在意运费与进口税；知道 Aliexpress（价格敏感、对比渠道）
- **风险/边界**：无公开网页、无 LinkedIn → 规模与资质无法核实，按「小型安装商/个体」对待；价格敏感且会对比 Aliexpress，报价必须给 EXW + 明确运费/关税说明
- **Saga 对位结论**：P1 STI-144GP（25% 档）——已买 5 电口工业样品 → 复购口径先给 4+1 口工业 PoE（STI-144GP）与 8+2 口工业管理型（STI-288DGGPM，支持 CLI/Web）；2.5G 需求用 STC-424XGGPM-280W（2.5G 下行待核）仅作备选
- **邮件切入句（英文）**：Since you took the 5-port industrial samples with the DIN power supply, the natural next step is the 8-port managed DIN unit with CLI and the 4+1 PoE version, both quoted EXW so the freight and import-duty side is transparent.

### 官网快照（自动摘要 · 抓取 2026-10-29 · 状态：停放/空站（疑停业或仅占位））

- 尝试域名：boecek.de
  > https://boecek.de/ conn: HTTPSConnectionPool(host='boecek.de', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(1, '[SSL:
  > https://www.boecek.de/ conn: HTTPSConnectionPool(host='www.boecek.de', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(1, '[
- **提示**：域名停放/空站 → 公司可能已停业或换域名；跟进前先用邮箱/电话核实，勿只凭网站判死。
- 数据文件：`data/saga_clients/site_snapshots/SA-004.json`

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 7 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-04-14 | 2025.4.14 | 16电 |  | A |  | DE 1.22.xlsx#105 |
| 2025-05-12 | 512 | 24poe |  | A |  | DE 1.22.xlsx#105 |
| 2025-07-14 | 714 | bypass |  | A |  | DE 1.22.xlsx#105 |
| 2025-10-06 | 106 | dac |  | A |  | DE 1.22.xlsx#105 |
| 2025-11-05 | 115 | solar |  | A |  | DE 1.22.xlsx#105 |
| ? | 69 | 48口 |  | A |  | DE 1.22.xlsx#105 |
| ? | 95 | 22mini |  | A |  | DE 1.22.xlsx#105 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：a.sagatelecom　|　**邮件**：15 封（去 15 / 来 0）　|　**期间**：2025-04-14 → 2026-09-23　|　**最后去信**：2026-09-23
- **对方邮箱**：boecek@boecek.de
- 对方从未回信（全部为我方去信）

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Managed PoE Switches | 2026-09-23 | 2026-09-23 | 0 | 1 | 1 |
| 24 Port PoE Managed Switch | 2026-08-18 | 2026-08-18 | 0 | 1 | 1 |
| Firmware 7.5 L2+ Feature Update | 2026-07-07 | 2026-07-07 | 0 | 1 | 2 |
| 10G L3 Managed Switch | 2026-06-02 | 2026-06-02 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2026-05-04 | 2026-05-04 | 0 | 1 | 1 |
| Marvell Managed Commercial Switches | 2026-03-27 | 2026-03-27 | 0 | 1 | 1 |
| OEM Core Switching Solution | 2026-01-23 | 2026-01-23 | 0 | 1 | 1 |
| Marvell Industrial Alert System | 2025-12-17 | 2025-12-17 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-05 | 2025-11-05 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-06 | 2025-10-06 | 0 | 1 | 1 |
| Mini Industrial PoE Switch | 2025-09-05 | 2025-09-05 | 0 | 1 | 1 |
| Managed Optical Bypass Switch | 2025-07-14 | 2025-07-14 | 0 | 1 | 1 |
| …共 15 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：A 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-29T15:11:51Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SA-004/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](http://boecek.de/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 541 字符；首行：STRATO - Domain reserved |

## 联系方式（已有 · 原值照录）

- 邮箱：`boecek@boecek.de`〔企业邮箱；来源：用户表原值〕
- 电话：`+491725368536`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Boecek / Manager
- 网站/域名：boecek.de
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Boecek | — | boecek@boecek.de / +491725368536 | 用户表原值·WhatsApp 已加 | Clients/ 表 |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:boecek.de`, `e:boecek@boecek.de`, `n:DE|boecek sec`, `p:725368536`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/DONE/DE 1.22.xlsx#总表:106 | 105 | Boecek Sec<br>http://boecek.de/ | 德国 | Boecek<br>Manager | 埃森展2024 | 买了5电口样品，需要一起买工业电源，也问了拿的2款2.5G网的价格，对机架式工业管理有兴趣，需要能支持CLI管理，知道Aliexpress, 比较在意运费和进口税，展会结束时一直在扫货 | Boecek@boecek.de | 49 17253 68536 已加 | 7 条 |
| AI客户评估/DONE/AI客户评估_DE 09.23.xlsx#总表:45 | 44 | Boecek Sec<br>http://boecek.de/ | 德国 |  | 埃森展2024 | 买了5电口样品，需要一起买工业电源，也问了拿的2款2.5G网的价格，对机架式工业管理有兴趣，需要能支持CLI管理，知道Aliexpress, 比较在意运费和进口税，展会结束时一直在扫货 | Boecek@boecek.de | 49 17253 68536 已加 | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-144GP | 深挖对位：已买 5 电口工业样品 → 复购口径先给 4+1 口工业 PoE（STI-144GP）与 8+2 口工业管理型（STI-288DGGPM，支持 CLI/Web）；2.5G 需求用 STC-424XGGPM-280W（2.5G 下行待核）仅作备选 | $35.5 USD EXW（25% 档，SmartByte LT-IS3005GP-1GX4GT 190 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（安防集成/经销（据用户备注推断）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-144GP），备选型不进首触。

- **第 1 次**：老客户回访——问上次所购型号的使用情况 + 告知 Marvell 新款（STI-144GP）；只问一个问题：当前在采购的主力型号与月量。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有成交史，信任与开户成本已付；WhatsApp 直达；欧洲主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STI-144GP 按 25% 档报价，做现供应商的第二货源；规模（调研）：未知
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
| 采购量/预算 | ✅ 有成交史（量待确认） |
| 商业资格结论 | **技术上合格 / 商业上有互动证据（成交或实质回复或面谈）→ 值得长期跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 官网当前状态异常（停放/空站（疑停业或仅占位））——公司是否仍在运营待核
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：After the 5-port industrial samples - the 8-port managed DIN unit and the 4+1 PoE version

```text
Hello,

Our record says you took the 5-port industrial switch samples from us together with the DIN power supply, and asked about two 2.5G models; the product mails you had since were general ones, and nobody had a reason to answer them. This one is specific.

The two units that normally follow the 5-port: DIN-rail 8 x Gigabit PoE+ + 2 x SFP, L2 managed (web GUI, VLAN, QoS, IGMP), Marvell-based, -40 to 75 C, CE/RoHS - model STI-288GPM - $82.2 USD EXW (MOQ 1, 15-day validity); DIN-rail 4 x Gigabit PoE+ + 1 x SFP unmanaged - STI-144GP - $35.5. Both EXW, so the freight and import side stays transparent on your end.

One question: is the rack-mount managed industrial switch you mentioned still on your list - and for which cabinet, 19-inch with how many ports?

Best regards,
Alan
Saga Telecom - sagatele.com
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-12**（14 天）：无回复 → 换通道再试一次；仍无 → 降 B。有任何回复 → 当即更新 research JSON 并重渲染。

## 变更日志

- 2026-10-29：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 A，分数 131）

---

*建档日期：2026-10-29　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
