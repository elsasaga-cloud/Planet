# germany24.com.ua

> **评级 B**　|　乌克兰　|　档案编号 `SA-018`　|　优先级 ★★　|　状态：有回复·跟进中
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：实质回复 3 次；推送 22 次（2024-03-21 → 2025-12-29）　|　**所在清单**：S重点　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SA-018
rating: B
rating_auto: B
score: 65
country: 乌克兰
region: 乌克兰
website: germany24.com.ua
type: 经销/集成（类型待核）
tier_tags: ["S重点"]
deal: no
replies: 3
followups: 22
first_contact: 2024-03-21
last_contact: 2025-12-29
s_mail: 32 msgs (out 28 / in 4), 2024-05-29 -> 2026-09-08
p1: STI-288GP
price_tier: 20%
research: done
site_snapshot: ok  # 2026-10-21
sources: 1
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：（加厚挖掘建档，摘要见下文加厚块）（调研 2026-10-21；表内兴趣：之前谈了工业FS）
- **为什么是 B 级**：+30 实质回复 3 次（问价/要资料/问型号等）；+25 在 Simon 的 S 重点名单；-3 WhatsApp 加不上；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-20 区域 乌克兰/乌克兰；+5 最近活动 2025；+5 跟进表最近平台标记 S；封顶 B：乌克兰（守界：不主动投入，仅被动响应）
- **历史互动**：实质回复 3 次；推送 22 次（2024-03-21 → 2025-12-29）；最近一次客户回复：2024-11-20：想下单 后续over
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：BO 内 Marvell 款（具体型号在 DI order #1.xls，附件未入库）；Realtek 款按 Simon 是否开线 — J3：一次性回答身份 + 问旧 BO，成本一封信；UA 风险另核｜已发资料（勿重发）：Saga Feature List_7.5.x_L2+(2026-06-22)；还没给过：Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）；按 30% 自有标档
- **第一问（只问一个）**：Your Nov-2024 test order (DI order #1) — is it still worth shipping the Marvell items with your label, 7–10 days after payment?
- **最大未知**：年走量与现供应商
- **下一步**：2026-11（一次） S 邮箱 → sergiy.khodun@gmail.com 两段：Saga 现身份一句话；2024 BO 的 Marvell 项是否仍要、7–10 天交期不变

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SA-018` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未绑定（订单意向止于身份追问）——曾递交首张测试订单 BO（2024-11-20）** ｜ 类型：乌克兰进口商 + 自有标（要印自己品牌/型号/序列号，每型号常规 20–30 台）；Sergiy Khodun——第二档「有进口经验者」+ 贴牌 ｜ 筛子：3（BO 已发：DI order #1.xls；问交期/标签样/GUI logo） ｜ 停点：2024-11-22「your company is not a manufacturer and does not have its own production facilities… right?」→ Simon「We are a manufacturer, at the same time, we trade. Marvell… manufacture, Realtek from other suppliers」→ 再无来信；BO 疑含 Realtek 低价款（他 5 月问过 STI-050FE/080FE 25/40 USD 的价差） ｜ 复活：以 sagatele.com 现口径（Engineering & Supply-Chain-First）重述身份一次 + 问 2024 BO 是否仍有效；UA 物流/付款需先核 ｜ 通路：UA（战时物流/付款待核；对方 2024 要普通快递） ｜ 节奏：2024-05 → 2026-09 去信 28 封；最后来信 2024-11-22 ｜ 证据：k=ce8e1aaaf377b7e8 / 510ef3ba6b343873 / fbd001897a47c982 / eaa8056ace798022 / d6c3e30a8869b4c6
- **现状一句话**：Deutsche Import 是 A 级里唯一真正递交过订单表的乌克兰客户：2024-05 就问能否按其品牌印标签/型号/序列号（每型号 20–30 台常规量），2024-11-20 发来「first order for testing」BO，问交期（Simon：7–10 工作日）、标签样、GUI 加 logo（Simon：免费）。两天后他问「你们不是制造商、没有自己的产线对吧？」，Simon 答「既制造也贸易，Marvell 自产、Realtek 来自其他供应商」，对话终止。
- **对方真实需求（有据）**：小批量自有标：Marvell 管理型 + Realtek 低价非管理（DIN 5/8 口），GUI 带 logo。
- **断点 / 为什么停在这里**：身份问题是真实停点（摘读 D12/D13）：对方要的是「厂」的确定性，Saga 当时的回答把 Realtek 线的「贸易」属性摆在了订单前面。现口径「Engineering & Supply-Chain-First」正好是对这个问题的答案。
- **Saga 现在该推什么**：P1 **BO 内 Marvell 款（具体型号在 DI order #1.xls，附件未入库）；Realtek 款按 Simon 是否开线**（30% 档，按 30% 自有标档）——J3：一次性回答身份 + 问旧 BO，成本一封信；UA 风险另核｜已发资料（勿重发）：Saga Feature List_7.5.x_L2+(2026-06-22)；还没给过：Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）
  - 做不了 / 要先核的：DI order #1.xls 内容未入库；UA 物流（百运网能否到基辅）与付款（T/T 可否）
- **下一步（具体）**：2026-11（一次）　S 邮箱 → sergiy.khodun@gmail.com　两段：Saga 现身份一句话；2024 BO 的 Marvell 项是否仍要、7–10 天交期不变
  - 第一问（只问一个）：Your Nov-2024 test order (DI order #1) — is it still worth shipping the Marvell items with your label, 7–10 days after payment?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-05-29 | 来 | Sergiy Khodun | Do you print labels with our BRAND name, model's name and serial number if we'll be do order regularly about 20-30pcs per models? | 自有标 + 常规量 | `ce8e1aaaf377b7e8` |
| 2024-11-20 | 来 | Sergiy | We are going to do our first order for testing your products. Pls refer to our current BO attached. | BO 递交 | `510ef3ba6b343873` |
| 2024-11-20 | 去 | Simon | For the listed quantity and models, 7~10 working days… logo… free of cost | 交期与贴牌答复 | `fbd001897a47c982` |
| 2024-11-22 | 来 | Sergiy | As far as I understand, your company is not a manufacturer and does not have its own production facilities. You operate in cooperation with other manufacturers, right? | 身份追问 = 停点 | `eaa8056ace798022` |
| 2024-11-22 | 去 | Simon | We are a manufacturer, at the same time, we trade. Marvell solution is what we do/manufacture, while Realtek is from other suppliers(trading). | 当时口径 | `d6c3e30a8869b4c6` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：BO 具体型号/数量；对方 2026 年是否仍在营业（战时）——官网未核

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | germany24.com.ua（取自域名，公司全名待核） | 推断 |
| 国家 | 乌克兰 | 事实（用户表）|
| 网站/域名 | germany24.com.ua / planet.kiev.ua | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Sergey Khodun / CEO | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | 之前谈了工业FS | 事实（用户表） |
| 用户备注（Remark） | tel: 38(044)59 37976<br>加不上 | 事实（用户表） |
| 所在清单 | S重点 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | FS | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：
- **是谁**：（加厚挖掘建档，摘要见下文加厚块）
- **【用户表】S 重点；之前谈了工业 FS；CEO；WA 加不上**
  > 之前谈了工业FS / Sergey Khodun CEO / tel: 38(044)59 37976 加不上 / germany24.com.ua / planet.kiev.ua
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（基于首轮调研整理 + 需求映射；乌克兰守界））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Germany24 / planet.kiev.ua 运营主体（待核） |
| 总部/地址 | Kyiv, Ukraine（+380 44 593 7976，WA 加不上） |
| 其他 | 域名 planet.kiev.ua 表明其为 PLANET 品牌在乌克兰的经销/推广站；S 重点名单；22 次跟进、1 次实质回复 |

- **业务线**：网络设备经销（PLANET 线）；（待核）德国商品代购站 germany24
- **触达通道（公开）**：网站: germany24.com.ua · planet.kiev.ua（未抓取）；邮箱: info@germany24.com.ua（用户表）
- **近况信号**：
  - 曾谈工业 FS（光纤交换机）→ 对位 PLANET 工业 DIN 系列；S 重点名单；CEO Sergey Khodun 直达
- **风险/边界**：乌克兰：战时物流/保险/付款与最终用途不可控 → 守界（只被动响应、不主动推送军用可用品类）；WA 加不上
- **Saga 对位结论**：P1 STI-288GP（20% 档）——分销 20% 档（被动）：STI-288GP（DIN 8 GE PoE+ 2 SFP，$57.4）对应曾谈的工业 FS；管理型 STI-288DGGPM（$139.9）。乌克兰守界：仅在对方来询且用途为民用基础设施时报价
- **邮件切入句（英文）**：（守界：不主动发送；若对方来询——Sergey, for the industrial fibre switch we discussed: DIN-rail 8× GbE PoE+ + 2× SFP at $57.4 EXW, managed L2+ at $139.9; please confirm the civil end-use and delivery route so I can quote shipping.）

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://germany24.com.ua/　语言：uk　站点地图 URL 数：19
- **标题**：Home - LLC DEUTSCHE IMPORT
- **首页栏目**：LLC DEUTSCHE IMPORT / PLANET TECHNOLOGY УКРАЇНА / ОБЛАДНАННЯ ВІД DDC GmbH / DEUTSCHE ГАРАНТУЄ / НАШІ ПРОПОЗИЦІЇ
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：planet 8、poe 1、ethernet 1
- **站内出现的品牌**：PLANET, Teltonika, LevelOne　（「（！）」= Saga 自家/供应商品牌已在其站内出现）
- **站内公开邮箱**：info@germany24.com.ua
- **站内公开电话**：+38 (044) 593-79-76, +38 (066) 329-37-31
- **产品类页面**：https://germany24.com.ua/shop/
- **已抓子页**：[Контакти - LLC DEUTSCHE IMPORT](https://germany24.com.ua/contacts/)；[Про нас, компанія Дойч Імпорт - LLC DEUTSCHE IMPORT](https://germany24.com.ua/about-us/)
- 首页正文摘录：Перейти до вмісту Ми працюємо: Пн.- Пт. 9:30 - 18:30 +38 (044) 593-79-76, +38 (066) 329-37-31 (з Viber) info@germany24.com.ua LLC DEUTSCHE IMPORT VAD дистрибутор IT обладнання та промислових систем ГОЛОВНА ПРО НАС PLANET CERIO TELTONIKA E-LINK UTEPO КОНТАКТИ PLANET TECHNOLOGY УКРАЇНА Ми офіційні представники PLANET в Україні. Здійснюємо імпорт продукції, сертифікацію, гарантійні та післягарантійні зобов'язання Деталь
- **自动对位建议**：STC-28DGGPM（官网快照对位：PoE 词频 1 → 8 口 PoE+ 2 SFP L2+ 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SA-018.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 22 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2024-03-21 | 2024.3.21 | 发了工业电电源价格册 |  | Email |  | S 09.08.xlsx#16 |
| 2024-04-26 | 2024.4.26 | 发了2光4小壳信息 | sergiy.khodun@gmail.com | Email |  | S 09.08.xlsx#16 |
| 2024-05-22 | 2024.5.22 | 发了3层管理448信息 | 问了很多型号 | Email |  | S 09.08.xlsx#16 |
| 2024-06-20 | 2024.6.20 | 发了48口引流信息 |  | Email |  | S 09.08.xlsx#16 |
| 2024-07-29 | 2024.7.29 | 24口passive poe |  | Email |  | S 09.08.xlsx#16 |
| 2024-08-29 | 2024.8.29 | 10G MC |  | Email |  | S 09.08.xlsx#16 |
| 2024-09-30 | 930 | 22mini |  | Email |  | S 09.08.xlsx#16 |
| 2024-10-24 | 1024 | 28poe |  | Email |  | S 09.08.xlsx#16 |
| 2024-11-20 | 1120 | 154 | 想下单 后续over | Email |  | S 09.08.xlsx#16 |
| 2024-12-11 | 1211 | 16电 |  | Email |  | S 09.08.xlsx#16 |
| 2025-01-03 | 1.3 | 24fiber |  | Email |  | S 09.08.xlsx#16 |
| 2025-02-28 | 2025.2.28 | 24poe |  | S |  | S 09.08.xlsx#16 |
| 2025-04-07 | 4.7 | 48口 |  | S |  | S 09.08.xlsx#16 |
| 2025-04-30 | 430 | bypass |  | S |  | S 09.08.xlsx#16 |
| 2025-05-28 | 528 | Alarm |  | S |  | S 09.08.xlsx#16 |
| 2025-06-25 | 625 | 芯片 |  | S |  | S 09.08.xlsx#16 |
| 2025-07-28 | 728 | 28bt |  | S |  | S 09.08.xlsx#16 |
| 2025-08-27 | 827 | 22mini |  | S |  | S 09.08.xlsx#16 |
| 2025-09-30 | 930 | 28poe |  | S |  | S 09.08.xlsx#16 |
| 2025-10-29 | 1029 | dac |  | S |  | S 09.08.xlsx#16 |
| 2025-11-27 | 1127 | solar |  | S |  | S 09.08.xlsx#16 |
| 2025-12-29 | 1229 | taiwan |  | S |  | S 09.08.xlsx#16 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：32 封（去 28 / 来 4）　|　**期间**：2024-05-29 → 2026-09-08　|　**最后去信**：2026-09-08
- **对方邮箱**：info@germany24.com.ua、sergiy.khodun@gmail.com
- **最后一封来信**：2024-11-22 sergiy.khodun@gmail.com「RE: Samples order form DI」：Hi Simon, Tnx for your replay. As far as I understand, your company is not a manufacturer and does not have its own production facilities. You operate in cooperation with other manufacturers, right? BR Sergiy Khodun LLC DEUTSCHE IMPORT 02068 Kiev, Ukraine str.

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 24 Port PoE Managed Switch | 2026-09-08 | 2026-09-08 | 0 | 1 | 1 |
| 24 Port 10G SFP+ Switch | 2026-07-20 | 2026-07-20 | 0 | 1 | 1 |
| Firmware 7.5 L2+ Feature Update | 2026-06-22 | 2026-06-22 | 0 | 1 | 2 |
| Updated Ethernet Switches Links | 2026-03-02 | 2026-03-02 | 0 | 1 | 1 |
| OEM Core Switching Solution | 2026-01-29 | 2026-01-29 | 0 | 1 | 1 |
| Optional Marvell Chipset Solutions | 2025-12-29 | 2025-12-29 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-27 | 2025-11-27 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-29 | 2025-10-29 | 0 | 1 | 1 |
| 8 Port Industrial PoE Switch | 2025-09-30 | 2025-09-30 | 0 | 1 | 1 |
| Mini Industrial PoE Switch | 2025-08-27 | 2025-08-27 | 0 | 1 | 1 |
| 90W PoE Managed Switch | 2025-07-28 | 2025-07-28 | 0 | 1 | 1 |
| Marvell Alleycat5 Solution | 2025-06-25 | 2025-06-25 | 0 | 1 | 1 |
| …共 23 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：3 个　|　**数据截至**：2026-10-24T07:26:33Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SA-018/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://germany24.com.ua/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 1787 字符；首行：Home - LLC DEUTSCHE IMPORT |
| [sitemap](https://germany24.com.ua/sitemap_index.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |
| [feed_auto](https://germany24.com.ua/feed/) | rss | HTTP 200 | 2026-10-23T04:20:51Z | 1 条；最新：Tue, 22 Mar 2022 14:00:53 Привіт, світ! |

## 联系方式（已有 · 原值照录）

- 邮箱：`info@germany24.com.ua`〔企业邮箱；来源：用户表原值〕
- 电话：`+380445937976`〔WhatsApp 加不上；原值见来源表〕
- 联系人（原值）：Sergey Khodun / CEO
- 网站/域名：germany24.com.ua
- 网站/域名：planet.kiev.ua
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Sergey Khodun | — | info@germany24.com.ua / +380445937976 | 用户表原值 | Clients/ 表 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| S 09.08.xlsx#总表:17 | 16 | www.germany24.com.ua<br>www.planet.kiev.ua | 乌克兰 | Sergey Khodun<br>CEO | 谷歌 | 之前谈了工业FS | info@germany24.com.ua | tel: 38(044)59 37976<br>加不上 | 22 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-288GP | 深挖对位：分销 20% 档（被动）：STI-288GP（DIN 8 GE PoE+ 2 SFP，$57.4）对应曾谈的工业 FS；管理型 STI-288DGGPM（$139.9）。乌克兰守界：仅在对方来询且用途为民用基础设施时报价 | $57.4 USD EXW（20% 档，SmartByte LT-IS3010GP-2GX8GT 320 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 20%（经销/集成（类型待核）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $80.7 USD EXW（20% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $181.2 USD EXW（20% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STI-288GP 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；20% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 3 次实质回复（对方认识我们）
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STI-288GP 按 20% 档报价，做现供应商的第二货源
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

**主题**：Re: DI order #1 (Nov 2024) — still worth shipping?

```text
Hi Sergiy,

Two years ago your first test order (DI order #1, 20 Nov 2024) stopped on the question of who we are. The plain answer today: Saga is an engineering-led supplier — the Marvell managed line is our own platform (firmware, web GUI with your logo, feature roadmap), the low-cost unmanaged items are sourced from partner factories under our QC. We do not pretend to own the SMT line.

One question: are the Marvell items in that BO still worth shipping with your label, 7–10 working days after payment, as quoted then? If yes, I will re-issue the proforma at current prices; if no, I will close the file.

Best regards,
Simon
Saga Telecom · sagatele.com
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

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 65）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
