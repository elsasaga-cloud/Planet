# cmd-sec.ru

> **评级 B**　|　俄罗斯　|　档案编号 `SB-970`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：安防品牌商（俄罗斯，自有型号 PoE）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：群发(Russia)　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-970
rating: B
rating_auto: B
score: 29
country: 俄罗斯
region: 俄语区
website: cmd-sec.ru
type: 安防品牌商（俄罗斯，自有型号 PoE）
tier_tags: ["群发(Russia)"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 7 msgs (out 7 / in 0), 2024-07-06 -> 2025-01-27
p1: STC-28DGGPM
price_tier: 30%
research: done
site_snapshot: unreachable  # 2026-10-21
sources: 1
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：俄罗斯 CMD-sec（安防：自有型号商用 PoE 为主，工业 FS 有 Utepo；官网 unreachable）；表内未跟进。（调研 2026-10-21；表内兴趣：有Utepo的工业FS 主要是商业POE 自己的型号）
- **为什么是 B 级**：-6 群发批次名单；+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+0 区域 俄语区/俄罗斯
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-25）**：STC-28DGGPM — 自有型号商用 PoE → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$87.4 @30%）、24 口 STC-424DGGPM-280W（$145.7）贴标；工业 8 PoE + 2 SFP STI-288GP（$62.2）作 Utepo 二供。已打开的主题（3/7 封有打开记录）：「Mini industrial switch」(2024-08-18)、「Power Converter」(2024-09-14)、「16 Port PoE Managed Switch」(2025-01-27) → 读者兴趣偏「工业」；与 P1 同类，继续；首触锚价 STC-28DGGPM $87.4 EXW（主表档位（PDF 上限 $99）；第 72 批 2026-10-24）；按主表（研究档 saga_fit）；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-11-17 $300（48 Port PoE Managed Switch）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-05-21 $280（10G Enterprise SFP Switch = STC-4168XGGCM 双 AC，Elsa 箱 1 轮 2026-05-21；$280 仍是 Simon 在用的群发价（NYNEX 实付 $265.2）——别写主表 377–408 档）；2026-08-26 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-08-26；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170）
- **第一问（只问一个）**：For the PoE switches sold under your own model numbers, we can be a second ODM source on a Marvell L2+ platform (8-PoE + 2 SFP, 24-PoE 280 W; DIN-rail 8-PoE for Utepo positions) in your packaging from small lots, CE/RoHS; EAC by your side — which PoE SKU do you reorder most? Reference: STC-28DGGPM at $87.4 USD EXW (MOQ 1, 15-day validity).
- **最大未知**：采购/产品负责人姓名（表内只有公司级邮箱）；官网当前状态异常（域名不可达（DNS/连接失败））——公司是否仍在运营待核
- **下一步**：2026-11 S 邮箱 → sales@cmd-sec.ru 首封前知悉：本户是 Elsa 俄罗斯-3 批次的锚，To 直收 15 轮（2025-02-21→2026-08-26，最近 24-PoE $170），一封未回；S 箱 2024→2025 另 7 封、3 次打开。开头按 ㉝「我们发过不少信、你没有理由回」，别当陌生户；24-PoE 要报 $180 就先说 8 月那封是 $170、汇率 7.2→6.7；短信一问（email_hook）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-25）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-970` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-25。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：读而不回（S 邮箱 7 封 2024→2025，其中 3 封被打开，0 回；收件 sales@cmd-sec.ru；被打开主题「Passive PoE Switch、Mini industrial switch」）；Elsa 群发 To 直收 15 轮 2025-02-21→2026-08-26（本户是「俄罗斯-3（锚 cmd-sec.ru）」批次的锚：Elsa 每轮 To sales@cmd-sec.ru、其余 24–27 家俄罗斯安防/CCTV 商在 Bcc；轮次 2025-02-21 Mini Industrial PoE / 03-16 90W PoE / 04-10 Commercial Network / 05-10 Commercial PoE / 06-13 48 Port PoE / 07-13 16 Port / 08-14 24 Port Fiber / 09-29 10G SFP / 10-31 Industrial PoE / 12-15 Booster PoE / 2026-01-22 OEM Core / 03-17 Updated Links / 04-17 Industrial PoE / 05-21 10G SFP / 08-26 24 Port PoE Managed（正文「Price: 170USD/PC」）），0 回（Elsa 箱 Replied 标签无）（第 74 批(l) `from:e.sagatelecom to:sales@cmd-sec.ru` complete 15 条 + Bcc 头 1a03d832440f86d9 / 19be523b1cac7f03；第 74 批(e) 曾按 in:sent 排锚扫描误记为「单发、非 BCC」，本批纠正）** ｜ 类型：安防品牌商（俄罗斯，自有型号 PoE） ｜ 筛子：2（有人在读，无人回） ｜ 停点：读而不回 = 内容未命中或没有当下需求 ｜ 复活：一封「只问一句」的短信给打开过的地址（不附图不附表） ｜ 通路：RU 次级（Simon 2026-08 点名） ｜ 节奏：一封；回了再说 ｜ 证据：gmail_digest：out 7，Opened 标签 3（Simon 群发追踪）；用户表：「有Utepo的工业FS 主要是商业POE 自己的型号」；研究档 risks：俄罗斯：结算/物流/合规风险；官网 unreachable（经营状态待核）；现供 Utepo 价格基准低；未跟进过，仅 sales@；data/gmail_e/bcc_batches_2026.json；批次时间线：同批次（To sales@cmd-sec.ru）2026-01-22→2026-08-26 共 5 轮群发（OEM Core Switching Solution、Updated Ethernet Switches Links、Industrial PoE Switch、10G Enterprise SFP Switch、24 Port PoE Managed Switch），本户在首尾两轮 Bcc 名单内，名单稳定、中间轮次按同名单推断；该批次最早 2025-02-21 起共 15 轮，更早轮次 Bcc 未读
- **现状一句话**：俄罗斯 CMD-sec（安防：自有型号商用 PoE 为主，工业 FS 有 Utepo；官网 unreachable）；表内未跟进。
- **对方真实需求（有据）**：自有型号商用 PoE → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$87.4 @30%）、24 口 STC-424DGGPM-280W（$145.7）贴标；工业 8 PoE + 2 SFP STI-288GP（$62.2）作 Utepo 二供
- **断点 / 为什么停在这里**：俄罗斯：结算/物流/合规风险；官网 unreachable（经营状态待核）；现供 Utepo 价格基准低；未跟进过，仅 sales@
- **Saga 现在该推什么**：P1 **STC-28DGGPM**（30% 档，首触锚价 STC-28DGGPM $87.4 EXW（主表档位（PDF 上限 $99）；第 72 批 2026-10-24）；按主表（研究档 saga_fit）；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-11-17 $300（48 Port PoE Managed Switch）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-05-21 $280（10G Enterprise SFP Switch = STC-4168XGGCM 双 AC，Elsa 箱 1 轮 2026-05-21；$280 仍是 Simon 在用的群发价（NYNEX 实付 $265.2）——别写主表 377–408 档）；2026-08-26 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-08-26；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170））——自有型号商用 PoE → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$87.4 @30%）、24 口 STC-424DGGPM-280W（$145.7）贴标；工业 8 PoE + 2 SFP STI-288GP（$62.2）作 Utepo 二供。已打开的主题（3/7 封有打开记录）：「Mini industrial switch」(2024-08-18)、「Power Converter」(2024-09-14)、「16 Port PoE Managed Switch」(2025-01-27) → 读者兴趣偏「工业」；与 P1 同类，继续
- **下一步（具体）**：2026-11　S 邮箱 → sales@cmd-sec.ru　首封前知悉：本户是 Elsa 俄罗斯-3 批次的锚，To 直收 15 轮（2025-02-21→2026-08-26，最近 24-PoE $170），一封未回；S 箱 2024→2025 另 7 封、3 次打开。开头按 ㉝「我们发过不少信、你没有理由回」，别当陌生户；24-PoE 要报 $180 就先说 8 月那封是 $170、汇率 7.2→6.7；短信一问（email_hook）
  - 第一问（只问一个）：For the PoE switches sold under your own model numbers, we can be a second ODM source on a Marvell L2+ platform (8-PoE + 2 SFP, 24-PoE 280 W; DIN-rail 8-PoE for Utepo positions) in your packaging from small lots, CE/RoHS; EAC by your side — which PoE SKU do you reorder most? Reference: STC-28DGGPM at $87.4 USD EXW (MOQ 1, 15-day validity).

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-01-27 | 去 | S 群发 | Passive PoE Switch、Mini industrial switch | 7 封 / 3 次打开 / 0 回｜首封 2024-07-06 → 末封 2025-01-27（7 去 / 0 来） | `gmail_digest` |
| 2025-02-21 | out | Elsa 群发（To 直收：本户是「俄罗斯-3（锚 cmd-sec.ru）」批次的锚，其余客户在 Bcc） | Mini Industrial PoE Switch（俄罗斯-3 批次月轮之一；To 本户、其余 Bcc） | 第 74 批(e) 误判为 1:1 单发；第 74 批(l) 读 Bcc 头证实本户是锚（每轮 To 本户、Bcc 24–27 家） | `elsa_bcc` |
| 2025-12-15 | out | Elsa 群发（To 直收：本户是「俄罗斯-3（锚 cmd-sec.ru）」批次的锚，其余客户在 Bcc） | Booster PoE Switch（俄罗斯-3 批次月轮之一；To 本户、其余 Bcc） | 第 74 批(e) 误判为 1:1 单发；第 74 批(l) 读 Bcc 头证实本户是锚（每轮 To 本户、Bcc 24–27 家） | `elsa_bcc` |
| 2026-01-22 | 去 | Elsa 群发（To 直收：本户是「俄罗斯-3（锚 cmd-sec.ru；2025-02-21 起月轮，15 轮）」批次的锚，其余客户在 Bcc） | OEM Core Switching Solution — I am introducing our CENTEC-based core and aggregation switches. 1, A cost-effective alternative to Cisco or Huawei models 2, Multiple models(10G~800G | Elsa 箱群发直达证据（To sales@cmd-sec.ru）；该批次 15 轮 2025-02-21→2026-08-26 每轮都以本户为 To；S/A digest 看不到 Elsa 的发信 | `elsa_bcc` |
| 2026-05-21 | out | Elsa 群发（To 直收：本户是「俄罗斯-3（锚 cmd-sec.ru）」批次的锚，其余客户在 Bcc） | 10G Enterprise SFP Switch（俄罗斯-3 批次月轮之一；To 本户、其余 Bcc；正文价 280usd/pc，第 74 批(p) 读稿 msg 19984c1d62ba38d6 / 19df5ef64e6ba213） | 第 74 批(e) 误判为 1:1 单发；第 74 批(l) 读 Bcc 头证实本户是锚（每轮 To 本户、Bcc 24–27 家） | `elsa_bcc` |
| 2026-08-26 | 去 | Elsa（e.sagatelecom，Gmail 连接器实时查询） | Elsa 邮箱群发「24 Port PoE Managed Switch」→ sales@cmd-sec.ru（截至 2026-10-24 无回复） | 仓库 gmail_e 只收录有回复的线程，Elsa 2026-08-19 → 09-15 的 201 封群发不在库里；本户在前 100 封内。意义：S/A 邮箱的「未发信/未触达」判断不等于 Elsa 没碰过——三个邮箱对同一户的触达要合看；Elsa 群发无回 = 再加一次「读而不回/未触达」证据 | `Gmail 连接器 list_messages newer_than:70d from:e.sagatelecom（2026-10-24 07:3x Z）` |
| 2026-08-26 | out | Elsa 群发（To 直收：本户是「俄罗斯-3（锚 cmd-sec.ru）」批次的锚，其余客户在 Bcc） | 24 Port PoE Managed Switch（俄罗斯-3 批次月轮之一；To 本户、其余 Bcc；正文价 170usd/pc，第 74 批(p) 读稿 msg 1a05bfb71364077f） | 第 74 批(e) 误判为 1:1 单发；第 74 批(l) 读 Bcc 头证实本户是锚（每轮 To 本户、Bcc 24–27 家） | `elsa_bcc` |
| 2026-10-21 | 用户表 | Simon | 有Utepo的工业FS 主要是商业POE 自己的型号 | 表内备注 | `用户表` |

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | cmd-sec.ru（取自域名，公司全名待核） | 推断 |
| 国家 | 俄罗斯 | 事实（用户表）|
| 网站/域名 | cmd-sec.ru | 事实（用户表 URL/邮箱域名） |
| 类型 | 安防品牌商（俄罗斯，自有型号 PoE） | 推断（据兴趣/备注关键词） |
| 联系人 | — | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | 有Utepo的工业FS<br>主要是商业POE 自己的型号 | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | 群发(Russia) | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | Utepo, FS | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：快照失败（unreachable）
- **是谁**：俄罗斯 CMD-sec（安防：自有型号商用 PoE 为主，工业 FS 有 Utepo；官网 unreachable）；表内未跟进。
- **类型**：安防品牌商（俄罗斯，自有型号 PoE）
- **在卖/在用品牌**：Utepo
- **【用户表】表内兴趣/备注**
  > 有Utepo的工业FS 主要是商业POE 自己的型号
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【用户表】自己的型号；Utepo**
  > 有Utepo的工业FS 主要是商业POE 自己的型号
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- 备注：（无首轮调研；由 deepen.py 建档） ｜ 规则加厚 2026-10-21（autodeep.py；T 档 T5）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（人工复核：官网快照逐家核对 + 表内；T4/T5 信号优先））

| 公司事实 | 内容 |
|---|---|
| 总部/地址 | 俄罗斯 |
| 其他 | 官网 cmd-sec.ru，语言 ?，快照状态 unreachable；角色判定来源：用户表 |

- **业务线**：安防 / PoE（自有型号，俄罗斯）
- **触达通道（公开）**：role: 安防品牌商（俄罗斯，自有型号 PoE）；region: 俄罗斯；contact: sales@cmd-sec.ru
- **近况信号**：
  - 表内：有 Utepo 的工业 FS 主要是商业 POE 自己的型号
  - 快照：unreachable
- **风险/边界**：俄罗斯：结算/物流/合规风险；官网 unreachable（经营状态待核）；现供 Utepo 价格基准低；未跟进过，仅 sales@
- **Saga 对位结论**：P1 STC-28DGGPM（30% 档）——自有型号商用 PoE → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$87.4 @30%）、24 口 STC-424DGGPM-280W（$145.7）贴标；工业 8 PoE + 2 SFP STI-288GP（$62.2）作 Utepo 二供
- **邮件切入句（英文）**：For the PoE switches sold under your own model numbers, we can be a second ODM source on a Marvell L2+ platform (8-PoE + 2 SFP, 24-PoE 280 W; DIN-rail 8-PoE for Utepo positions) in your packaging from small lots, CE/RoHS; EAC by your side — which PoE SKU do you reorder most?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：域名不可达（DNS/连接失败））

- 尝试域名：cmd-sec.ru
  > https://cmd-sec.ru/ conn: HTTPSConnectionPool(host='cmd-sec.ru', port=443): Max retries exceeded with url: / (Caused by NewConnectionError("HTTPSC
  > https://www.cmd-sec.ru/ conn: HTTPSConnectionPool(host='www.cmd-sec.ru', port=443): Max retries exceeded with url: / (Caused by NewConnectionError("HT
  > http://cmd-sec.ru/ conn: HTTPConnectionPool(host='cmd-sec.ru', port=80): Max retries exceeded with url: / (Caused by NewConnectionError("HTTPConn
- **提示**：域名不可达 → 表内域名可能拼错/过期；跟进前核对邮箱域名。
- 数据文件：`data/saga_clients/site_snapshots/SB-970.json`

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| Utepo | 深圳/国内白牌或品牌供应商 | 对方已在买中国货：以 Marvell 芯片 + L2+ 功能 + 交期为差异点做第二货源 |
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：7 封（去 7 / 来 0）　|　**期间**：2024-07-06 → 2025-01-27　|　**最后去信**：2025-01-27
- **对方邮箱**：sales@cmd-sec.ru
- 对方从未回信（全部为我方去信）
- **邮件里报过的价**：2024-11-17 $300

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 16 Port PoE Managed Switch | 2025-01-27 | 2025-01-30 | 3 | 1 | 7 |
| 8 Port Industrial PoE Switch | 2024-12-15 | 2024-12-15 | 0 | 1 | 1 |
| 48 Port PoE Managed Switch | 2024-11-17 | 2024-11-17 | 0 | 1 | 1 |
| Industrial PoE Switch | 2024-10-19 | 2024-10-19 | 0 | 1 | 1 |
| Power Converter | 2024-09-14 | 2024-09-14 | 0 | 1 | 1 |
| Mini industrial switch | 2024-08-18 | 2024-08-18 | 1 | 1 | 4 |
| Passive PoE Switch | 2024-07-06 | 2024-07-06 | 0 | 1 | 1 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-24T07:26:33Z　|　**最近变化**：2026-10-24T04:35:40Z
- **最近变化摘要**：2026-10-24 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-970/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://cmd-sec.ru/) | html | HTTP 200 | 2026-10-24T04:35:40Z | 3745 字符；首行：CMD оборудование для видеонаблюдения - купить CMD \| cmd-sec.ru |

## 联系方式（已有 · 原值照录）

- 邮箱：`sales@cmd-sec.ru`〔企业邮箱；来源：用户表原值〕
- 网站/域名：cmd-sec.ru
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| —（未具名） | 公司级 | sales@cmd-sec.ru | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E/群发/Russia 08.26 08.27.xlsx#总表:41 | 40 | https://cmd-sec.ru/catalog/setevoe-oborudovanie/ | 俄罗斯 |  | 谷歌 | 有Utepo的工业FS<br>主要是商业POE 自己的型号 | sales@cmd-sec.ru |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：自有型号商用 PoE → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$87.4 @30%）、24 口 STC-424DGGPM-280W（$145.7）贴标；工业 8 PoE + 2 SFP STI-288GP（$62.2）作 Utepo 二供 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（安防品牌商（俄罗斯，自有型号 PoE）） |
| 备选2 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-28DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：自有品牌/贴牌需求 = 现成 OEM 客户
- **W**：无具名决策人，仍是公司级触达；俄语区：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STC-28DGGPM 按 30% 档报价，做现供应商的第二货源；贴牌 + 定制 UI/型号 → 30% 档与长期绑定；对位其在用/在卖的 Utepo：涨价、断货或交期拉长时切入
- **T**：深圳同行（ONV / Utepo / 迈威等）价格战；现有品牌分销协议可能限制同品类采购；汇率与海运波动吃掉 20–30% 的价差

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
| 决策人识别 | ❌ 未识别（公司级） |
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ✅ Utepo, FS |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 采购/产品负责人姓名（表内只有公司级邮箱）
- [ ] 官网当前状态异常（域名不可达（DNS/连接失败））——公司是否仍在运营待核
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：One question — Passive PoE Switch

```text
Hello,

We have sent you a few mails on "Passive PoE Switch" and you never had a reason to answer — fair enough. No brochure this time, just one question:

For the PoE switches sold under your own model numbers, we can be a second ODM source on a Marvell L2+ platform (8-PoE + 2 SFP, 24-PoE 280 W; DIN-rail 8-PoE for Utepo positions) in your packaging from small lots, CE/RoHS; EAC by your side — which PoE SKU do you reorder most?

Reference price: 8-PoE + 2 × 1G/2.5G SFP L2+ managed switch (Marvell AC5), 120 W (STC-28DGGPM) $87.4 USD EXW, MOQ 1 pc, 15-day validity, 1-year warranty.

If it is not relevant now, a one-word reply is enough and I will take you off the catalog mails.

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

- **2026-11-24**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 29）

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
