# versitron.com
**官方名称（调研核实）**：Versitron, Inc.（美国特拉华）

> **评级 B**　|　美国　|　档案编号 `SB-826`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：DC线索　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-826
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
updated: 2026-10-27
```

## SALES BRIEF（压缩模型）

- **是谁**：美国铜转光连接方案设计制造商（数据 / 语音 / 视频；switch 646 / sfp 416 / poe 368 / media converter 197 / industrial 180），Greg Massott；表内「Stacking」（堆叠交换机需求，Saga 无堆叠）；无跟进。制造商 → OEM 30%（MC / 工业 PoE 贴牌）。（调研 2026-10-21；表内兴趣：Stacking）
- **为什么是 B 级**：+0 数据中心交换机线索（Hohunet/CENTEC 线）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：CENTEC STH1G：STH-2QX4DX48GP-HSI（48×1G PoE++ 90W + 4×25G SFP28 + 2×40G QSFP+，堆叠 ≤8 台 / 360 Gbps，链或环，双热插拔 1200W PSU）= 他要的 Catalyst 9300 级可堆叠 48 口 PoE；-SFI 为 PoE+ 30W 单电源版。汇聚/核心再配 STH-8C48DX / 2C6QX — 美国品牌商 + 三年关系 + 明确的产品线需求 = J1 第一档；只是 Saga 过去一年把牌打坏了，需要一封诚实的对表信｜已发资料（勿重发）：Marvell Based Web Manual(2024-05-16)、STC-110XGE(2024-06-18)、Passive PoE(2024-07-16)、Ordering Information(2024-08-14)、Variants(2024-08-14)、STI-42424XGGPM-4BT(2025-08-28)、STH1G Series(2026-03-11)；已发单据：Quotation(2024-08-14)；还没给过：7.5 Feature List、Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）｜对外统一口径（#1，2026-10-24 第 48 批改正）：2026-03-11 Simon 的「stacking available on all models」指的是随信附的 STH1G Series.pdf（CENTEC 48×1G PoE 线，ST 堆叠许可，≤8 台），不是 AC5——AC5 规格书明写「Stacking… NOT going to develop it in 2 or 3 years」，7.5 功能表 Stacking Management ✖。对表信要把这两层说清：接入 AC5 不堆叠；可堆叠 48 口 PoE = STH1G。Greg 自 2026-03-11 起无回（只自动回复）——他可能根本没打开那份 pdf｜第 56 批：MACsec 有证（STOS V2.4「MacSec(802.1AE) ◯」，BigFlow 平台除外，STH1G 是 VastLakes 可用）；10G 铜口改为指同族 STH-2QX4DX8XP40DP-HSI（堆叠待证）；他见过的实报：2023-11-09 首版整表（424XGGM $130 / 448XGGPM $394 / 28GPM $63…）；2024-08-14 STI-222GP $36 / 266FP $39 / 088GP $40；按 CENTEC 底线 ≥35%；先给 2 款 1U 的 OEM 报价区间而非单价；历史报价（邮件原话，老汇率）：2024-05-16 375usd / 550usd；2024-06-18 75usd；2025-08-28 500usd；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2025-10-30 $280（10G Enterprise SFP Switch）；群发里他已看到的价（续，第 66 批全量复核）：2024-11-19 $300（48 Port PoE Managed Switch）、2025-01-03 $240（24 Port Fiber Switch）
- **第一问（只问一个）**：Greg — the stackable line exists now: STH-2QX4DX48GP-HSI, 48×1G PoE++ + 4×25G + 2×40G, stacks up to 8 units over the fiber ports (ring or chain, 360 Gbps), hot-swap PSUs, your label. Is the Cisco-alternative stackable line still on your 2027 plan, and for how many units per stack?
- **最大未知**：年走量与现供应商
- **下一步**：现在 S 邮箱 → gmassott@versitron.com（回 2026-03-11 那封「Re: 10G Enterprise SFP Switch」，他没回过）；备用具名邮箱 → rwtull@versitron.com 一封对表信：承认 2025 年拖延 + 3 月那封写得太短（一句「available on all models」+ 一个 pdf）；按他 2025-01-31 的三条硬规格逐条写 STH-2QX4DX48GP-HSI 有/没有（1G 铜口 PoE++ 有、10G 铜口没有、40G 光口堆叠 ≤8 台有、单逻辑设备有）；价格写「按首批数量给 EXW」——Simon 先定 STH1G 区间（仓内无价）；只问一个问题：堆叠线还在不在 2027 计划里；回原串沿用原主题（邮件客户端自动加 Re:），上面的主题只在另起新信时用

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-826` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：较深的「关系绑定」但零成交（S 邮箱三年 21 来 29 去，全是 Greg Massott 本人；他在 2024-11 → 2025-10 之间 6 次主动追问堆叠；2026-03-11 Simon 宣布堆叠可用后只收到自动回复，至今 7 个月无回；Elsa 箱：`to:versitron.com` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 29 / 来 21）（第 74 批(h)））** ｜ 类型：美国老牌光传输/工业以太网品牌商（第一档 OEM 品牌商；Greg = 采购/产品经理级，Simon 前东家时代就认识，Olycom HDMI） ｜ 筛子：3→4 之间：要过数据表、报价、芯片追问，但从未要样品；原因是它要的是「能和 Cisco 比的堆叠整线」，不是单品 ｜ 停点：两个断点：① 2024-11 Simon 承诺堆叠「2~3 个月」，拖到 2025-10-31 坦白「1st release 出了严重问题」，期间 Greg 追了 6 次——信用被消耗；② 2026-03-11 Simon 说「Finally, stacking available on all models」，Greg 只回了 OOO 自动回复——要么没看到，要么已另寻来源 ｜ 复活：不要再发群发。按 Greg 2025-01-31 写下的硬规格逐条对表回一封：10/100/1G/10G 铜 + SFP；专用高速堆叠口（40/80/100G）；多台识别为一台逻辑交换机的虚拟化管理——CENTEC 线（STH 系列 VXLAN/EVPN/Stacking）才对得上，Marvell AC5 的「stacking」对不上 Catalyst 9300；备用具名邮箱：rwtull@versitron.com（自动回复中出现的同司具名邮箱，2026-03-11，k=4ac602505b7d8db3；从未发过） ｜ 通路：US 主攻；品牌商 OEM = 目标顺位第一 ｜ 节奏：一封「对表信」现在发；之后每季度只发与堆叠/核心相关的实质更新，不发 PoE 小品 ｜ 证据：k=1025007cd6875d3e（2024-11-19 堆叠需求原话）；1c4ec9e7a2e3b881（Simon「2~3 months」）；f8ad0f8ce32688ea（2025-01-31 硬规格）；0a50926da6770aea / 517fb73517e3920c / e1fd8f4094de16bc / 08fe828b2a31d85b / e97d49af1e93423b（5 次追问）；973470596a08bd2e（2025-10-31「serious issues after 1st release」）；401b90aaadcce218（「alternative to Cisco」）；3cab7e50e48fea36（2026-03-11 宣布可用）；4ac602505b7d8db3（只收到 OOO）；第 19 批回补来信原文 8 条（gmail_s/gmail_a）
- **现状一句话**：这是 S 邮箱里最典型的「客户在追、供方在拖」的反例。Greg 在 2024-11-19 主动提出要开发一条带堆叠的交换机产品线「so that we can compete with Cisco in the USA market」，并问 Simon 公司能否做；Simon 答 2~3 个月会有。接下来一年 Greg 追了六次（2025-06-11/18/23、10-15、10-30），Simon 的回答从「ready, what spec?」到「serious issues after 1st release」再到「honestly we do not see a big demand」。2026-03-11 Simon 终于说所有型号都支持堆叠并附 Drive 链接，对方只有自动回复。Greg 给出的规格（10G 铜/光 + 40/80/100G 专用堆叠口 + 单逻辑交换机）实际上是 Catalyst 9300 级别，SmartByte Marvell AC5 线不具备，CENTEC 线才有可能。
- **对方真实需求（有据）**：可堆叠的企业接入/汇聚整线（1G/10G 接入 + 40/80/100G 堆叠口 + 单逻辑管理），用 Versitron 品牌替代 Cisco。
- **断点 / 为什么停在这里**：承诺与交付之间的 16 个月；2026-03-11 终于有了可堆叠线（STH1G），却只发了一句话 + pdf，Greg 没回——对表没做完。
- **Saga 现在该推什么**：P1 **CENTEC STH1G：STH-2QX4DX48GP-HSI（48×1G PoE++ 90W + 4×25G SFP28 + 2×40G QSFP+，堆叠 ≤8 台 / 360 Gbps，链或环，双热插拔 1200W PSU）= 他要的 Catalyst 9300 级可堆叠 48 口 PoE；-SFI 为 PoE+ 30W 单电源版。汇聚/核心再配 STH-8C48DX / 2C6QX**（30% 档，他见过的实报：2023-11-09 首版整表（424XGGM $130 / 448XGGPM $394 / 28GPM $63…）；2024-08-14 STI-222GP $36 / 266FP $39 / 088GP $40；按 CENTEC 底线 ≥35%；先给 2 款 1U 的 OEM 报价区间而非单价；历史报价（邮件原话，老汇率）：2024-05-16 375usd / 550usd；2024-06-18 75usd；2025-08-28 500usd；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2025-10-30 $280（10G Enterprise SFP Switch）；群发里他已看到的价（续，第 66 批全量复核）：2024-11-19 $300（48 Port PoE Managed Switch）、2025-01-03 $240（24 Port Fiber Switch））——美国品牌商 + 三年关系 + 明确的产品线需求 = J1 第一档；只是 Saga 过去一年把牌打坏了，需要一封诚实的对表信｜已发资料（勿重发）：Marvell Based Web Manual(2024-05-16)、STC-110XGE(2024-06-18)、Passive PoE(2024-07-16)、Ordering Information(2024-08-14)、Variants(2024-08-14)、STI-42424XGGPM-4BT(2025-08-28)、STH1G Series(2026-03-11)；已发单据：Quotation(2024-08-14)；还没给过：7.5 Feature List、Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）｜对外统一口径（#1，2026-10-24 第 48 批改正）：2026-03-11 Simon 的「stacking available on all models」指的是随信附的 STH1G Series.pdf（CENTEC 48×1G PoE 线，ST 堆叠许可，≤8 台），不是 AC5——AC5 规格书明写「Stacking… NOT going to develop it in 2 or 3 years」，7.5 功能表 Stacking Management ✖。对表信要把这两层说清：接入 AC5 不堆叠；可堆叠 48 口 PoE = STH1G。Greg 自 2026-03-11 起无回（只自动回复）——他可能根本没打开那份 pdf｜第 56 批：MACsec 有证（STOS V2.4「MacSec(802.1AE) ◯」，BigFlow 平台除外，STH1G 是 VastLakes 可用）；10G 铜口改为指同族 STH-2QX4DX8XP40DP-HSI（堆叠待证）
  - 做不了 / 要先核的：S；T；H；1；G； ；仓；内；无；价；（；主；表；/；C；E；N；T；E；C； ；Q；2； ；x；l；s； ；都；没；有； ；S；T；H；-；2；Q；X；4；D；X； ；行；）；—；—；报；价；区；间；要； ；S；i；m；o；n； ；自；己；定；；；1；0；G； ；铜；口；接；入；（；他； ；2；0；2；5；-；0；1；-；3；1； ；要； ；1；0；/；1；0；0；/；1；G；/；1；0；G； ；c；o；p；p；e；r；）；S；T；H；1；G； ；没；有；，；只；有； ；1；G； ；铜； ；+； ；2；5；G；/；4；0；G； ；光；；；S；i；m；o；n；《；S；T；H；计；划；》；：；1；G；/；2；.；5；G；/；5；G； ；铜；口； ；C；E；N；T；E；C； ；机；「；暂；不；宣；传；、；信；息；备；好；」；→； ；信；稿；只；答；「；o；n； ；r；e；q；u；e；s；t； ；/； ；n；o；t； ；o；n； ；p；u；b；l；i；s；h；e；d； ；l；i；s；t；」；，；不；主；推；；；估；算；带；见； ；C；E；N；T；E；C； ；锚；表； ；§；5；.；3；，；对；客；户；仍； ；p；r；i；c；e； ；o；n； ；r；e；q；u；e；s；t
- **下一步（具体）**：现在　S 邮箱 → gmassott@versitron.com（回 2026-03-11 那封「Re: 10G Enterprise SFP Switch」，他没回过）；备用具名邮箱 → rwtull@versitron.com　一封对表信：承认 2025 年拖延 + 3 月那封写得太短（一句「available on all models」+ 一个 pdf）；按他 2025-01-31 的三条硬规格逐条写 STH-2QX4DX48GP-HSI 有/没有（1G 铜口 PoE++ 有、10G 铜口没有、40G 光口堆叠 ≤8 台有、单逻辑设备有）；价格写「按首批数量给 EXW」——Simon 先定 STH1G 区间（仓内无价）；只问一个问题：堆叠线还在不在 2027 计划里；回原串沿用原主题（邮件客户端自动加 Re:），上面的主题只在另起新信时用
  - 第一问（只问一个）：Greg — the stackable line exists now: STH-2QX4DX48GP-HSI, 48×1G PoE++ + 4×25G + 2×40G, stacks up to 8 units over the fiber ports (ring or chain, 360 Gbps), hot-swap PSUs, your label. Is the Cisco-alternative stackable line still on your 2027 plan, and for how many units per stack?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2023-11-09 | 来 | gmassott@versitron.com | Hello Simon: I hope all is well, and congratulations & good luck! We'll keep this information on-hand for future reference. Thank you, Greg Massott \| | 来信原文（主题「Re: POE switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `85123ce32bd28e55` |
| 2023-11-09 | 去 | Simon → Greg Massott（`Price.pdf`，S 邮箱附件，47 款） | Saga **首版整表价格单**（2023-11，Realtek 时代命名）：商用非管理 STC-05GE $6.6 / 08GE $10.8 / 016GE $37 / 024GE $47~53 / 248GE $140；商用 PoE 非管理 STC-028GP $24.5 / 228GP $30.5 / 2224GP $100；管理型 STC-28GM $52 / 424GM $100 / **424XGGM $130** / 448XGGM $255 / 4248XGGCM $300 / 28GPM $63 / 424XGGPM $256 / 448XGGPM $394 / 120XGM $168；工业 STI-114GE $19 / 204GE $23.5 / 208GE $51 / 114GP $27.5 / 204GP $31 / 208GP $60。 | Greg 收到后回「congratulations & good luck… keep on-hand」——这是 Versitron 关系的起点；也是价格史上最早的一张整表：STC-424XGGM $130 与 2026 年 SA-002 的 $130 底价同量级，说明三年来 Simon 的量级没变（口径 ㉕ 的「老表量级」有据） | `S 邮箱附件 `Price.pdf` sha=82c72d3e1bd2f784（2023-11-09）` |
| 2023-12-12 | 来 | gmassott@versitron.com | Hello Simon: Thank you for this information. Greg Massott \| P: 302.894.0699 Ext. 20 \|F: 302.894.0624 \| gmassott@versitron.com<mailto:gmassott@versitro | 来信原文（主题「Re: POE switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `bf1123a71b98d0a9` |
| 2023-12-12 | 去 | Saga（Simon） | Hi, Greg, Thanks for your kind words. There is also din power supply for your choice. You may also download the information from below Google Drive link. https://drive.google.com/drive/folders/1ZG50Ugnns3XQ2RuFzFx7CwNX6eZAbf4H?usp=drive_link… | Saga 实质答复原文（主题「Re: POE switch」；第 20 批从 gmail_s 回补）——承诺/口径以此为准 | `045cc03da988c60f` |
| 2024-01-08 | 来 | gmassott@versitron.com | Hello Simon: Thank you, and Happy New Year to you as well! Greg Massott \| P: 302.894.0699 Ext. 20 \|F: 302.894.0624 \| gmassott@versitron.com<mailto:gma | 来信原文（主题「Re: POE switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `bdc33af7998da6ad` |
| 2024-02-19 | 去 | Saga（Simon） | Hi, Greg, How are you? I am back to work and would like to recommend a 16 port PoE Industrial Switch. Please see attached product information. For this series, you could also get more information from below google drive link. https://drive.google.com/drive/folders/1PKhmEboNZkl105nBUotOBcTBrH9qX6EU?u… | Saga 实质答复原文（主题「Re: POE switch」；第 20 批从 gmail_s 回补）——承诺/口径以此为准 | `b88fdfbd72e71b7e` |
| 2024-02-20 | 来 | gmassott@versitron.com | Hello Simon: I hope all is well, and thank you for this information. Greg Massott \| P: 302.894.0699 Ext. 20 \|F: 302.894.0624 \| gmassott@versitron.com< | 来信原文（主题「Re: POE switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `c043a5ceedc13b6e` |
| 2024-05-16 | 来 | gmassott@versitron.com | Hello Simon: It's nice to hear from you, and I hope all is well. Can you send the datasheets for both the industrial and commercial versions along wit | 来信原文（主题「Re: POE switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `362966d662d4b69d` |
| 2024-05-16 | 去 | Saga（Simon） | Hi, Greg, Please see attached datasheets, web manual and CLI manual. Commercial model, 375usd/pc Industrial model, 550usd/pc Both models share the same specification as below. 4*10 Gigabit SFP+16*Gigabit SFP+8*Gigabit SFP/RJ45(Combo ports)+1*Console Port, Stan | 历史报价点（主题「Re: POE switch」；第 20 批从 gmail_s 回补）：375usd / 550usd | `73339deec6e397bd` |
| 2024-06-18 | 去 | Saga（Simon） | Hi, Greg, How are you? Last time we talked about 24 port managed switch, is there any plan for sample testing? And I would like to recommend a 10G fiber media converter. Good outlook and 14-slot rack mountable. Price: 75usd/pc, 1*10G SFP+1*100M/1G/2.5G/10G Eth | 历史报价点（主题「Re: POE switch」；第 20 批从 gmail_s 回补）：75usd | `533485b14a400b6f` |
| 2024-07-17 | 来 | gmassott@versitron.com | Hello Simon: I am well, I hope the same for you. Thank you for this information, we will keep it on file for future reference. Greg Massott \| P: 302.8 | 来信原文（主题「Re: POE switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `5b36ad2e37bc3754` |
| 2024-08-14 | 来 | gmassott@versitron.com | I was asking if there are managed versions of the same variants that you provided. Greg Massott \| P: 302.894.0699 Ext. 20 \|F: 302.894.0624 \| gmassott@ | 来信原文（主题「Re: POE switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `8da54ed91f1c24e4` |
| 2024-08-14 | 来 | gmassott@versitron.com | Hello Simon: Thank you for this information. Do you offer managed versions as well? If so, please provide the available models and prices. Greg Massot | 来信原文（主题「Re: POE switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `16e894d27961f348` |
| 2024-08-14 | 去 | Simon → Greg（Quotation.pdf） | 工业非管理三款：STI-222GP（2×SFP + 2×GE PoE 60W）$36；STI-266FP（2×100M SFP + 6×FE PoE 180W）$39；STI-088GP（8×GE PoE 240W）$40；validity 15 d，-40~75℃，DIP。→ Greg 当天回「Do you offer managed versions as well? If so, please provide the available models and prices」。 | Greg 要的一直是**管理型/可堆叠**（后来的堆叠长追由此而来）；非管理价他只是存档 | `S 邮箱附件 `Quotation.pdf` sha=8b9b9eab6e8f69f3（2024-08-14）` |
| 2024-11-19 | 来 | Greg Massott | We are interested in developing a switch product line that offers stacking technology, so that we can compete with Cisco in the USA market. Is this something that your company… | 需求起点 | `1025007cd6875d3e` |
| 2024-11-21 | 去 | Simon | Yes, we received many stacking requirements, but sorry to tell you that it is not available now… expected to be ready in 2~3 months | 承诺 | `1c4ec9e7a2e3b881` |
| 2025-01-03 | 来 | Greg Massott | （Re: 24 Port Fiber Switch）We currently offer a similar product, but will keep this on file.（2025-08-27 Re: L3 Managed Switch）What is the price of this unit? → 08-28 Simon: 500usd/pc, it is expensive because we are doing Marvell chip | Versitron 自有 24 口光纤交换机 → 单品推送无效；只有堆叠整线这个空白才是他要 Saga 的理由。L3 $500 他收下「thank you」即止——价格不是他的决定因素，产品线是 | `gmail_s 2025-01-03 / 2025-08-27` |
| 2025-01-31 | 来 | Greg | We do not have a chip preference… must support 10/100/1G/10G copper and SFP… dedicated high-speed stacking modules (40/80/100G)… all stacked switches must be recognized as one logical switch | 硬规格 | `f8ad0f8ce32688ea` |
| 2025-06-11 | 来 | Greg | I'm following up to see if you have been able to successfully design the stacking switches discussed below. | 追问 ×3（06-11/18/23） | `0a50926da6770aea` |
| 2025-06-23 | 来 | Greg Massott | （06-11 / 06-18 / 06-23 三封同文）I'm following up to see if you have been able to successfully design the stacking switches discussed below. Please advise when you have a moment.（10-15）Any news on this?（10-30）What is the status of the stacking switches that we had been discussing? | 一个月内三封同文催问 + 10 月两封——Versitron 这边是认真排了产品线的；Saga 的回复节奏（06 无回、10-31 坦白出问题）是这条线断掉的直接原因。对表信要先认这件事 | `gmail_s 2025-06-11/18/23, 10-15, 10-30` |
| 2025-08-27 | 来 | Greg Massott（Versitron） | What is the price of this unit?（L3 管理 24 口 DIN PoE，370W） | Simon 08-28 答 $500/pc「expensive because we are doing Marvell chip」→ 无下文 | `gmail_s f6115f259e0a5e6b` |
| 2025-08-28 | 去 | Saga（Simon） | Hi, Greg, Thanks for your email. It is 500usd/pc, it is expensive because we are doing Marvell chip. Please see attached datasheet. Thank you. | 历史报价点（主题「Re: L3 Managed Switch」；第 20 批从 gmail_s 回补）：500usd | `d9911e2b978f6965` |
| 2025-10-31 | 去 | Simon | stacking is still not available, we found some serious issues after 1st release… honestly we do not see a big demand | 坦白 + 质疑需求 | `973470596a08bd2e` |
| 2025-10-31 | 来 | Greg | We are trying to offer stacking as an alternative to Cisco. | 目标对手 | `401b90aaadcce218` |
| 2026-03-11 | 去 | Simon | Finally, our "stacking" feature is available on all models… I guess you mean Cisco Catalyst 9300 Switches? This is fine. | 宣布可用；只收到 OOO | `3cab7e50e48fea36` |
| 2026-03-11 | 来 | 自动回复 | 自动回复（Greg Massott 2026-03-11 休假）里指定「contact R.W. Tull at rwtull@versitron.com」 | Versitron 内部第二个具名入口（R.W. Tull）；三年只跟 Greg 一人谈，这是绕开单点的现成地址 | `4ac602505b7d8db3` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：2026-03-11 之后 Greg 是否读信（只有自动回复 4ac602505b7d8db3）；（已核 2026-10-24，第 73 批）2026-03-11 S 邮箱去信附件 = 「STH1G Series.pdf」+「Dual AC.jpg」→ 发的是 CENTEC STH1G 系列资料（不是 AC5），正文却写「stacking available on all models」——信稿已据此纠正：只有 STH 堆叠，Marvell 不堆叠

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **时机与节律**：真人来信 20 封（2023-11-09 → 2025-10-31）；多在 8 月（5） / 1 月（3） / 6 月（3）；对方本地时间中位 10:30，四分位 09:06–11:42（= 北京时间 23:30）；周三最多（8）；**他们回信中位 5.9 小时**（20 次，70% 在 24 小时内）；我方回信中位 30.9 小时（16 次，>72 小时 7 次）；**我方未回 4 封**。
- **发信窗口（US 全库 2491 封群发的打开标签，对方本地时间；均值 5.4%）**：周三 08–10 点 13.6%（44 封）、周二 08–10 点 11.1%（63 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 11 封（2023-11-09 → 2025-11-28），打开标签 5 次（近 12 个月 1，最后 2025-10-30）；打开过：「POE switch」×1（2023-11-09）、「48 Port PoE Managed Switch」×1（2024-11-19）、「24 Port Fiber Switch」×1（2025-01-03）、「L3 Managed Switch」×1（2025-08-27）；从未打开：「Power Converter」、「10G Ethernet Web Managed Switch」、「16 Port Ethernet Switch」。
- **报价轨迹**（S/A 去信里「价 + 型号/描述同句」：1:1 4 条 + 个性化群发价 3 条，2024-05-16 → 2025-10-30；「今天」= 价格主表 2026-10-17 汇率、30% 档、不高于 2026-06 列表价；只列每个型号/描述最近一次，最多 8 行）：

  | 日期 | 型号 / 原句 | 当时 | 今天应报 | 变化 | 性质 | 主题 | 消息 key |
  |---|---|---|---|---|---|---|---|
  | 2025-10-30 | 「It is a price-competitive aggregation switch(280usd/pc)」 | $280 | —（原句无型号） | — | 群发价 | 10G Enterprise SFP Switch | `c63ae0d8d2f14dae` |
  | 2025-08-28 | 「It is 500usd/pc, it is expensive because we are doing Marvell chip.」 | $500 | —（原句无型号） | — | 1:1 | L3 Managed Switch | `d9911e2b978f6965` |
  | 2025-01-03 | 「Price: 240usd/pc」 | $240 | —（原句无型号） | — | 群发价 | 24 Port Fiber Switch | `13601a02ac7fdef0` |
  | 2024-11-19 | 「Price is very competitive, 300usd/pc」 | $300 | —（原句无型号） | — | 群发价 | 48 Port PoE Managed Switch | `c9f08eec36ddb223` |
  | 2024-06-18 | 「Price: 75usd/pc, 1×10G SFP+1×100M/1G/2.5G/10G Ethernet, unmanaged, non」 | $75 | —（原句无型号） | — | 1:1 | POE switch | `533485b14a400b6f` |
  | 2024-05-16 | 「Commercial model, 375usd/pc」 | $375 | —（原句无型号） | — | 1:1 | POE switch | `73339deec6e397bd` |
  | 2024-05-16 | 「Industrial model, 550usd/pc」 | $550 | —（原句无型号） | — | 1:1 | POE switch | `73339deec6e397bd` |

  「个性化群发价」= 同一句价发给 ≥5 家的信（Simon 的手工群发），对方未必读过，但它就是对方邮箱里躺着的「上次报价」。
- **品类覆盖与缺口**：官网兴趣：工业（industrial 180 / automation 26） / 安防 PoE（cctv 14 / camera 68 / poe 368） / 10G 汇聚（10g 216 / sfp 416） / 光纤接入 / 媒体转换（media converter 197 / fiber 889）；我们 1:1 从未报过价、也没成交；打开过的群发主题落在：10G 汇聚 / L3 / PoE；**还没碰过的一类：工业** → 下封信可加一句 STI-288GP（8 口千兆 PoE+ 2 SFP 工业非管理，$62.2 EXW）。
- **规模与贴牌线索（官网快照 2026-10-21）**：站点地图 219 条 URL；社媒：https://twitter.com/versitron、https://www.facebook.com/versitroninc、https://www.linkedin.com/company/versitron-inc-/。
- **写信的人（来信签名机械抽取）**：Greg Massott（gmassott@versitron.com，20 封，2023-11-09 → 2025-10-31）。
- **他们嘴里的词（20 封来信、去引用后 25,270 字符的词频）**：话题（次数，最近一次）：管理型 / L2+ / L3 ×10（2025-10-31）、价格 / 折扣 ×4（2025-08-27）、贴牌 / OEM ×2（2024-11-19）、质保 / 售后 ×2（2025-01-31）、工业 ×1（2024-05-16）、10G ×1（2025-01-31）；**提到的同行品牌**：Cisco ×2（2025-10-31）。
- **最后一球**：1:1 对话 4 段，最长一段 20 封 / 跨 279 天（2023-11-09 → 2024-08-14，「Re: POE switch」）；最后一句是我们说的（2026-03-11，229 天前，「Re: 10G Enterprise SFP Switch」，`3cab7e50e48fea36`）→ 球在对方手里。
- **同国同档参照（US，30% 档，共 8 户有动静，列前 3）**：SB-831 actelis.com（B，同档：回过 6 次（最近 2026-03-02），1:1 报过 1 次）；SA-002 simrex.com（A，同档：回过 4 次（最近 2026-07-20），1:1 报过 2 次）；SB-085 DIGI Group（B，同档：回过 3 次（最近 2025-11-28），1:1 报过 1 次）。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-11-26 感恩节（周四–周日四天基本停摆）；2026-12-24 圣诞–元旦（12-24 → 01-04 多数公司半停） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 进口记录（公开海关数据 · 第 80 批 · 2026-10-27）

> 来源：ImportYeti 整理的 **美国海关（CBP）海运提单**，2015-01 起；只覆盖海运到美国港口的货，**空运 / 快递 / 陆运看不见，欧洲 / 土耳其 / 加拿大按公司查不到**。美国提单**没有货值**，只有到港日 / 发货人 / 重量 / 件数 / 品名 / 估算海运费——所以「金额」一栏给不出，量只能用重量与箱数估。查询日 2026-10-27。

- **查无**：ImportYeti 公司页没有此户（company/versitron 404；company/versitron-inc 404）。美国海运提单库查不到 → 要么走空运/快递（小批量交换机常态），要么以其他法人名报关
- 查无 ≠ 不进口：可能用别的报关主体名、走空运 / 快递、或申请了舱单保密（ImportYeti FAQ）。

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
- 数据文件：`data/saga_clients/site_snapshots/SB-826.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

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

- **监控层**：B 级面层　|　**自动源**：5 个　|　**数据截至**：2026-10-26T07:56:19Z　|　**最近变化**：2026-10-24T07:26:33Z
- **最近变化摘要**：2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过））
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-826/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://www.versitron.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 12813 字符；首行：Secure & Reliable Fiber Optic Connectivity Solutions |
| [sitemap](https://www.versitron.com/sitemap.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |
| [news_1](https://www.versitron.com/pages/knowledge-center) | html | HTTP 200 | 2026-10-23T04:20:51Z | 8034 字符；首行：Knowledge Center |
| [news_2](https://www.versitron.com/pages/case-studies) | html | HTTP 200 | 2026-10-23T04:20:51Z | 8382 字符；首行：Case Studies |
| [youtube](https://www.youtube.com/feeds/videos.xml?channel_id=UCq7WBvce5EjKVu0Q9XXL_8g) | rss | HTTP 200 | 2026-10-24T07:26:33Z | 15 条；最新：2026-05-28T12:00:05+00:00 NDAA Compliant Fiber Optic Converter for Tethered Drone  |

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
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

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

**主题**：48 port stacking switches — the stackable line, properly this time

```text
Hi, Greg,

In March I sent you one line and a PDF and called it done — that was too short after you had asked about stacking since 2024. Here is the proper answer against your January-2025 list.

The stackable platform is our CENTEC-based STH1G series, not the Marvell access switches (those will not stack, and I will not claim otherwise). It is a build-to-order line that we do not list publicly — lead time is confirmed per order, not the 3-5 days of the Marvell units:
- STH-2QX4DX48GP-HSI: 48 x 1G PoE++ (90 W/port, 1200 W dual hot-swap PSU) + 4 x 25G SFP28 + 2 x 40G QSFP+ (25G ports can run at 10G)
- Stacking: up to 8 units as one logical switch, ring or chain over the fiber ports, 360 Gbps stack bandwidth (Catalyst 9300-class StackWise-320 is the comparison your market will make)
- 10G copper access: the 48-port unit is 1G copper; the same family has a 40 x 2.5G + 8 x 10G multi-gig PoE++ model (STH-2QX4DX8XP40DP-HSI) with the same 4 x 25G + 2 x 40G uplinks — stacking on that model I will confirm before promising it
- L3 with OSPF/BGP/PIM, VXLAN-EVPN, MPLS, MACsec; Versitron logo, model name and SNMP strings on the unit
- Lighter version: STH-2QX4DX48GP-SFI (PoE+ 30 W, single PSU)

Pricing is by first-batch quantity, so I will not guess a number here.

One question: is the Cisco-alternative stackable line still on your 2027 plan, and if yes, how many units per stack and roughly how many stacks? With that I will send the EXW price the same day.

Thank you.
Simon
Saga Telecom - sagatele.com
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-26**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-27：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 31）

---

*建档日期：2026-10-27　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
