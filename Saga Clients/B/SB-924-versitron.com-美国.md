# versitron.com
**官方名称（调研核实）**：Versitron, Inc.（美国特拉华）

> **评级 B**　|　美国　|　档案编号 `SB-924`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：DC线索　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-924
rating: B
rating_auto: B
name_official: "Versitron, Inc.（美国特拉华）"
score: 31
country: 美国
region: 北美
website: versitron.com
type: 经销/集成（类型待核）
tier_tags: ["DC线索"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 50 msgs (out 29 / in 21), 2023-11-09 -> 2026-03-11
p1: STI-110GE
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-21
sources: 1
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：美国铜转光连接方案设计制造商（数据 / 语音 / 视频；switch 646 / sfp 416 / poe 368 / media converter 197 / industrial 180），Greg Massott；表内「Stacking」（堆叠交换机需求，Saga 无堆叠）；无跟进。制造商 → OEM 30%（MC / 工业 PoE 贴牌）。（调研 2026-10-21；表内兴趣：Stacking）
- **为什么是 B 级**：+0 数据中心交换机线索（Hohunet/CENTEC 线）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：CENTEC STH 系列（10G/25G 接入 + 100G 上联，VXLAN/EVPN/Stacking）——而不是继续推 AC5「stacking」 — 美国品牌商 + 三年关系 + 明确的产品线需求 = J1 第一档；只是 Saga 过去一年把牌打坏了，需要一封诚实的对表信；按 CENTEC 底线 ≥35%；先给 2 款 1U 的 OEM 报价区间而非单价
- **第一问（只问一个）**：Greg — is the stackable line still on your 2027 roadmap, and if so, which is the first SKU you would need (24/48-port 1G access with 10G uplinks, or 10G access with 40/100G stacking)?
- **最大未知**：年走量与现供应商
- **下一步**：现在 S 邮箱 → gmassott@versitron.com（同一串 Re: 48 Port PoE Managed Switch） 一封对表信：承认 2025 年拖延；按他 2025-01-31 的三条硬规格逐条写「有/没有/哪个型号」；给 CENTEC 两款的 OEM 价格区间；问他现在堆叠项目还在不在

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-924` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：较深的「关系绑定」但零成交（S 邮箱三年 21 来 29 去，全是 Greg Massott 本人；他在 2024-11 → 2025-10 之间 6 次主动追问堆叠；2026-03-11 Simon 宣布堆叠可用后只收到自动回复，至今 7 个月无回）** ｜ 类型：美国老牌光传输/工业以太网品牌商（第一档 OEM 品牌商；Greg = 采购/产品经理级，Simon 前东家时代就认识，Olycom HDMI） ｜ 筛子：3→4 之间：要过数据表、报价、芯片追问，但从未要样品；原因是它要的是「能和 Cisco 比的堆叠整线」，不是单品 ｜ 停点：两个断点：① 2024-11 Simon 承诺堆叠「2~3 个月」，拖到 2025-10-31 坦白「1st release 出了严重问题」，期间 Greg 追了 6 次——信用被消耗；② 2026-03-11 Simon 说「Finally, stacking available on all models」，Greg 只回了 OOO 自动回复——要么没看到，要么已另寻来源 ｜ 复活：不要再发群发。按 Greg 2025-01-31 写下的硬规格逐条对表回一封：10/100/1G/10G 铜 + SFP；专用高速堆叠口（40/80/100G）；多台识别为一台逻辑交换机的虚拟化管理——CENTEC 线（STH 系列 VXLAN/EVPN/Stacking）才对得上，Marvell AC5 的「stacking」对不上 Catalyst 9300 ｜ 通路：US 主攻；品牌商 OEM = 目标顺位第一 ｜ 节奏：一封「对表信」现在发；之后每季度只发与堆叠/核心相关的实质更新，不发 PoE 小品 ｜ 证据：k=1025007cd6875d3e（2024-11-19 堆叠需求原话）；1c4ec9e7a2e3b881（Simon「2~3 months」）；f8ad0f8ce32688ea（2025-01-31 硬规格）；0a50926da6770aea / 517fb73517e3920c / e1fd8f4094de16bc / 08fe828b2a31d85b / e97d49af1e93423b（5 次追问）；973470596a08bd2e（2025-10-31「serious issues after 1st release」）；401b90aaadcce218（「alternative to Cisco」）；3cab7e50e48fea36（2026-03-11 宣布可用）；4ac602505b7d8db3（只收到 OOO）
- **现状一句话**：这是 S 邮箱里最典型的「客户在追、供方在拖」的反例。Greg 在 2024-11-19 主动提出要开发一条带堆叠的交换机产品线「so that we can compete with Cisco in the USA market」，并问 Simon 公司能否做；Simon 答 2~3 个月会有。接下来一年 Greg 追了六次（2025-06-11/18/23、10-15、10-30），Simon 的回答从「ready, what spec?」到「serious issues after 1st release」再到「honestly we do not see a big demand」。2026-03-11 Simon 终于说所有型号都支持堆叠并附 Drive 链接，对方只有自动回复。Greg 给出的规格（10G 铜/光 + 40/80/100G 专用堆叠口 + 单逻辑交换机）实际上是 Catalyst 9300 级别，SmartByte Marvell AC5 线不具备，CENTEC 线才有可能。
- **对方真实需求（有据）**：可堆叠的企业接入/汇聚整线（1G/10G 接入 + 40/80/100G 堆叠口 + 单逻辑管理），用 Versitron 品牌替代 Cisco。
- **断点 / 为什么停在这里**：承诺与交付之间的 16 个月；以及产品线对不上（AC5 ≠ Catalyst 9300 级堆叠）。
- **Saga 现在该推什么**：P1 **CENTEC STH 系列（10G/25G 接入 + 100G 上联，VXLAN/EVPN/Stacking）——而不是继续推 AC5「stacking」**（30% 档，按 CENTEC 底线 ≥35%；先给 2 款 1U 的 OEM 报价区间而非单价）——美国品牌商 + 三年关系 + 明确的产品线需求 = J1 第一档；只是 Saga 过去一年把牌打坏了，需要一封诚实的对表信
  - 做不了 / 要先核的：Greg 是否仍在职/是否已找到替代（2026-03 后无回）；CENTEC 线堆叠的真实成熟度（固件 7.5 口径：PIM-SM CLI only——堆叠在哪个版本、几台、什么口，要查固件说明再写）
- **下一步（具体）**：现在　S 邮箱 → gmassott@versitron.com（同一串 Re: 48 Port PoE Managed Switch）　一封对表信：承认 2025 年拖延；按他 2025-01-31 的三条硬规格逐条写「有/没有/哪个型号」；给 CENTEC 两款的 OEM 价格区间；问他现在堆叠项目还在不在
  - 第一问（只问一个）：Greg — is the stackable line still on your 2027 roadmap, and if so, which is the first SKU you would need (24/48-port 1G access with 10G uplinks, or 10G access with 40/100G stacking)?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-11-19 | 来 | Greg Massott | We are interested in developing a switch product line that offers stacking technology, so that we can compete with Cisco in the USA market. Is this something that your company… | 需求起点 | `1025007cd6875d3e` |
| 2024-11-21 | 去 | Simon | Yes, we received many stacking requirements, but sorry to tell you that it is not available now… expected to be ready in 2~3 months | 承诺 | `1c4ec9e7a2e3b881` |
| 2025-01-31 | 来 | Greg | We do not have a chip preference… must support 10/100/1G/10G copper and SFP… dedicated high-speed stacking modules (40/80/100G)… all stacked switches must be recognized as one logical switch | 硬规格 | `f8ad0f8ce32688ea` |
| 2025-06-11 | 来 | Greg | I'm following up to see if you have been able to successfully design the stacking switches discussed below. | 追问 ×3（06-11/18/23） | `0a50926da6770aea` |
| 2025-10-31 | 去 | Simon | stacking is still not available, we found some serious issues after 1st release… honestly we do not see a big demand | 坦白 + 质疑需求 | `973470596a08bd2e` |
| 2025-10-31 | 来 | Greg | We are trying to offer stacking as an alternative to Cisco. | 目标对手 | `401b90aaadcce218` |
| 2026-03-11 | 去 | Simon | Finally, our "stacking" feature is available on all models… I guess you mean Cisco Catalyst 9300 Switches? This is fine. | 宣布可用；只收到 OOO | `3cab7e50e48fea36` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：2026-03-11 之后 Greg 是否读信（只有自动回复 4ac602505b7d8db3）；Saga 当天附的「stacking」资料是 AC5 还是 CENTEC——附件名未见

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | versitron.com（取自域名，公司全名待核） | 推断 |
| 国家 | 美国 | 事实（用户表）|
| 网站/域名 | versitron.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Greg Massott | 事实（用户表） |
| 来源（From） | O | 事实（用户表） |
| 兴趣（Interested in） | Stacking | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | DC线索 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线（versitron.com，快照 2026-10-21）
- **是谁**：美国铜转光连接方案设计制造商（数据 / 语音 / 视频；switch 646 / sfp 416 / poe 368 / media converter 197 / industrial 180），Greg Massott；表内「Stacking」（堆叠交换机需求，Saga 无堆叠）；无跟进。制造商 → OEM 30%（MC / 工业 PoE 贴牌）。
- **在卖/在用品牌**：Versitron（自有）
- **【官网快照】铜转光连接方案设计与制造；关键词 switch 646 / media converter 197**
  > Versiton specializes in designing and manufacturing copper-to-fiber connectivity solutions tailored for data, voice, and video applications across diverse industries
  > 来源：https://versitron.com/（抓取 2026-10-21）
- **【用户表】Stacking**
  > 兴趣：Stacking
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【S 邮箱原文】关系起点：2023-11-09 Simon 首信——Olycom 时期已与 Greg 谈过 HDMI 产品，自立门户后发 CCTV PoE 价表；Greg 祝贺并「keep on-hand」。此后 2023-11→2026-03 共 50 封、29 出 21 入，Greg 每信必回（典型 US 老派采购：礼貌、不下单、问价）**
  > We discussed HDMI unit before(Olycom model), I set up my own office now.
  > 来源：（S 邮箱 thr 1782055947356135738，2023-11-09）（抓取 2026-10-22）
- **【S 邮箱原文】Saga 给 Versitron 的历史报价：2024-05 4×10G+16×1G SFP+8 Combo L3 商用 $375 / 工业 $550；2024-06 10G 光纤 MC $75；2025-08 24 口 L3 DIN PoE（af/at/bt 370W，DI/DO/RS485）$500「expensive because Marvell」；2025-10 24 口 SFP 汇聚双 AC $280**
  > Commercial model, 375usd/pc Industrial model, 550usd/pc … It is 500usd/pc, it is expensive because we are doing Marvell chip. … price-competitive aggregation switch(280usd/pc)
  > 来源：（S 邮箱 thr 1782055947356135738 / 1839339295413255932 / 1844786008444924799）（抓取 2026-10-22）
- **【S 邮箱原文】Versitron 真正的需求 = **堆叠交换机（替代 Cisco Catalyst 9300）**：2025-06-11/18/23 三次催「stacking switches discussed below」（指 2024-11-19 48 口讨论），2025-10-15「Any news on this?」，2025-10-31「We are trying to offer stacking as an alternative to Cisco」；Simon 2025-10-31 称首版有严重问题、客户都买 H3C/华为/Cisco；**2026-03-11 Simon 宣布「stacking feature is available on all models」并给 CENTEC 资料 Drive 链接**（1nKIZPptuYQhoUs0FbjyXYStrn2sl4iRU）；Greg 自动回复后至今无回音**
  > Finally, our "stacking" feature is available on all models. 1. We are trying to offer stacking as an alternative to Cisco. I guess you mean Cisco Catalyst 9300 Switches? This is fine.
  > 来源：（S 邮箱 thr 1844786008444924799，2026-03-11T08:24Z；Versitron 最后一封 2025-10-31）（抓取 2026-10-22）
- **KP**：Greg Massott（）gmassott@versitron.com 〔（本地 Clients/ 表格，无公开 URL）〕
- 备注：（无首轮调研；由 deepen.py 建档） ｜ 针对性加厚 2026-10-22（S 邮箱 50 封通读：三年关系、4 次报价、堆叠需求链，T29-U13 ②）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（官网快照核对 + 表内））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Versitron, Inc. |
| 成立 | 1958 |
| 总部/地址 | Newark, DE, USA |

- **业务线**：铜 / 光转换、MC、工业交换机（自有品牌）
- **触达通道（公开）**：role: 美国制造商（OEM 采购）；region: 美国
- **近况信号**：
  - MC / 工业 PoE 为其核心品类 → 贴 Versitron 标
- **风险/边界**：堆叠交换机 Saga 无；美国：常要求 UL 列名（Saga 无 UL，仅 FCC/CE）→ 首触即说明；【2026-10-22 复盘冲突，原样保留】本档 email_hook / saga_fit 写「不做堆叠」，但 S 邮箱 2026-03-11 Simon 已向 Greg 宣布 stacking 全系列可用（CENTEC/Hohunet 线）；两种口径并存——若 Simon 确认 CENTEC 堆叠可卖，Versitron 是美国最对口的堆叠买家（Cisco 替代），hook 应改为「堆叠已就绪 + 价格」；否则维持。
- **Saga 对位结论**：P1 STI-110GE（30% 档）——MC 为其主线 → STI-110GE（$24.3 @30%）贴 Versitron 标；工业 PoE STI-288GPM；堆叠不供。
- **邮件切入句（英文）**：Greg, we don't do stacking — but for the Versitron media-converter and industrial PoE lines we build DIN gigabit MCs and 8-PoE + 2-SFP managed units under your label from small lots (FCC/CE); which SKU family is up for re-sourcing?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://www.versitron.com/　语言：en　站点地图 URL 数：219
- **标题**：Secure & Reliable Fiber Optic Connectivity Solutions
- **描述**：Versiton specializes in designing and manufacturing copper-to-fiber connectivity solutions tailored for data, voice, and video applications across diverse industries. Our products are backed by a lifetime warranty and renowned for their exceptional longevity.
- **首页栏目**：Item added to your cart / Tethered Drone Fiber Optic Converters / Fiber Optic Solutions for / MISSION-CRITICAL APPLICATIONS / Fiber Optic Media Converters / Fiber Optic Network Switches / Serial to Fiber Converters / VersiVision Analog Video
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：fiber 889、switch 646、sfp 416、poe 368、ethernet 223、10g 216、media converter 197、industrial 180、surveillance 120、gigabit 110、camera 68、cable 56
- **站内型号串**（正则抽取，含非交换机）：SGX368244M, SGX75270MP, SGX72870MPA, SGX72870MA, SGX75270MA, RJ-45, IEEE802, SGX75270M, SGX288164M
- **站内公开邮箱**：sales@versitron.com
- **站内公开电话**：000 (1) 1000 (1, 000 (14) 10, 000 (8) 100
- **社媒**：https://twitter.com/versitron, https://www.facebook.com/versitroninc, https://www.linkedin.com/company/versitron-inc-/, https://www.youtube.com/channel/UCq7WBvce5EjKVu0Q9XXL_8g
- **产品类页面**：https://www.versitron.com/blogs/post/how-does-a-poe-switch-work；https://www.versitron.com/blogs/post/how-to-configure-poe-switch-setup-with-nvr；https://www.versitron.com/blogs/post/poe-media-converter-poe-nvr-and-poe-switches；https://www.versitron.com/blogs/post/features-to-consider-with-industrial-switches；https://www.versitron.com/blogs/post/poe-vs-poe-vs-poe-switches-know-the-real-difference；https://www.versitron.com/blogs/post/understanding-and-reducing-power-consumption-of-poe-network-switches
- **已抓子页**：[52 Port PoE Switch / 52-Port Managed PoE+ Switch](https://www.versitron.com/products/sgx75270mp-52port-managed-poe-poe-plus-switch)；[28 Port PoE Switch / 28 Port Managed PoE+ Switch](https://www.versitron.com/products/sgx72870mp-28port-managed-commercial-poe-poe-plus-switch)；[Industrial Network Switches / Industrial Ethernet Switches](https://www.versitron.com/collections/fiber-ethernet-industrial-network-switches)；[36 Port Ethernet Switch / 36-Port Managed Switch / 36 Port N](https://www.versitron.com/products/36port-managed-switch-sgx368244m)；[52 Port Gigabit Managed Switch / 52 Port Gigabit Switch / 52](https://www.versitron.com/products/sgx75270m-52port-managed-10g-switch)；[28 Port Gigabit Switch / 28 Port Managed Switch](https://www.versitron.com/products/sgx72870ma-28port-managed-10g-commercial-switch)
- 首页正文摘录：Skip to content Safeguarding Communications Since 1958 1-800-537-2296 sales@versitron.com Request a Quote Home About us About Versitron Warranty What's New? Products Fiber Optic Network Switches Managed Switches Unmanaged Switches Modular Switch PoE Switches Industrial Switches Fiber Optic Media Converters 10/100Base Fast Ethernet Media Converters 1000Base Gigabit Media Converter 10 Gigabit Media Converter Multimode 
- **自动对位建议**：STI-288GP（官网快照对位：工业/自动化词频 207、PoE 368 → DIN 8 PoE+ 2 SFP 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SB-924.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：50 封（去 29 / 来 21）　|　**期间**：2023-11-09 → 2026-03-11　|　**最后去信**：2026-03-11
- **对方邮箱**：gmassott@versitron.com
- **最后一封来信**：2026-03-11 gmassott@versitron.com「Automatic reply: 10G Enterprise SFP Switch」：Hello: I hope all is well. I will be out of the office until 03/12/26, and will reply to any messages when I return. Should you require immediate assistance, please call our office at 302-894-0699, or contact R.W. Tull at rwtull@versitron.com.
- **邮件里报过的价**：2025-10-30 $280；2025-08-28 $500；2025-01-03 $240；2024-11-19 $300；2024-06-18 $75；2024-05-16 $375；2024-05-16 $550

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 10G Enterprise SFP Switch | 2025-10-30 | 2026-03-11 | 2 | 3 | 24 |
| Automatic reply: 10G Enterprise SFP Switch | 2026-03-11 | 2026-03-11 | 1 | 0 | 0 |
| Booster PoE Switch | 2025-11-28 | 2025-11-28 | 0 | 1 | 1 |
| 48 Port PoE Managed Switch | 2024-11-19 | 2025-10-15 | 6 | 5 | 65 |
| L3 Managed Switch | 2025-08-27 | 2025-08-28 | 2 | 2 | 18 |
| Marvell Industrial Alert System | 2025-05-27 | 2025-05-27 | 0 | 1 | 1 |
| Managed Optical Bypass Switch | 2025-03-28 | 2025-03-28 | 0 | 1 | 1 |
| 24 Port Fiber Switch | 2025-01-03 | 2025-01-03 | 1 | 1 | 5 |
| 16 Port Ethernet Switch | 2024-12-11 | 2024-12-11 | 0 | 1 | 1 |
| 10G Ethernet Web Managed Switch | 2024-10-23 | 2024-10-23 | 0 | 1 | 1 |
| Power Converter | 2024-09-16 | 2024-09-16 | 0 | 1 | 1 |
| POE switch | 2023-11-09 | 2024-08-14 | 9 | 12 | 335 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：5 个　|　**数据截至**：2026-10-24T04:35:40Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-924/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://www.versitron.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 12813 字符；首行：Secure & Reliable Fiber Optic Connectivity Solutions |
| [sitemap](https://www.versitron.com/sitemap.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |
| [news_1](https://www.versitron.com/pages/knowledge-center) | html | HTTP 200 | 2026-10-23T04:20:51Z | 8034 字符；首行：Knowledge Center |
| [news_2](https://www.versitron.com/pages/case-studies) | html | HTTP 200 | 2026-10-23T04:20:51Z | 8382 字符；首行：Case Studies |
| [youtube](https://www.youtube.com/feeds/videos.xml?channel_id=UCq7WBvce5EjKVu0Q9XXL_8g) | rss | YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过） | 2026-10-23T04:20:51Z | YouTube 频道 https://www.youtube.com/channel/UCq7WBvce5EjKVu0Q9XXL_8g |

- **人工定期看（登录墙，不自动抓）**：Facebook: https://www.facebook.com/versitroninc；X/Twitter: https://twitter.com/versitron；LinkedIn: https://www.linkedin.com/company/versitron-inc-/

## 联系方式（已有 · 原值照录）

- 邮箱：`gmassott@versitron.com`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Greg Massott
- 网站/域名：versitron.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Greg Massott | — | gmassott@versitron.com | 调研核实（公开页） | （本地 Clients/ 表格，无公开 URL） |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| DC Switches 08.10.xlsx#总表:4 | 3 |  | 美国 | Greg Massott | O | Stacking | gmassott@versitron.com |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-110GE | 深挖对位：MC 为其主线 → STI-110GE（$24.3 @30%）贴 Versitron 标；工业 PoE STI-288GPM；堆叠不供。 | $24.3 USD EXW（30% 档，SmartByte LT-IMC30G-E 125 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（经销/集成（类型待核）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $151.6 USD EXW（30% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $196.3 USD EXW（30% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-110GE），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STI-110GE 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：北美主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STI-110GE 按 30% 档报价，做现供应商的第二货源
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
| 需求面成立（在卖/在用交换机或 PoE） | ❓ 表内兴趣不含交换机关键词 |
| 决策人识别 | ✅ |
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STI-110GE - industrial mini Gigabit media converter (Marvell-based, neutral label)

```text
Hi Greg,

We have been in touch before about PoE and industrial switches; instead of a catalogue, here is one concrete option. Greg, we don't do stacking — but for the Versitron media-converter and industrial PoE lines we build DIN gigabit MCs and 8-PoE + 2-SFP managed units under your label from small lots (FCC/CE); which SKU family is up for re-sourcing?

We supply a Marvell-based industrial mini Gigabit media converter (1 fiber + 1 copper) - model STI-110GE - that fits the same slot as the usual Taiwan-grade units at a lower landed cost, and we can ship it under your own label with neutral packaging. Current price: $24.3 USD EXW (price snapshot 2026-10-17, valid 15 days).

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

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 31）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
