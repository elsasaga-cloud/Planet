# James Clendenan Systems Ltd.

> **评级 A**　|　加拿大　|　档案编号 `SA-078`　|　优先级 ★★★　|　状态：成交过·活跃（Simon）
>
> **类型**：系统集成/工程（北温哥华）（推断）　|　**历史关系**：成交/下单过　|　**所在清单**：补录、已成单、PI成单、Simon:活跃、Xtransfer、成交(PI)　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SA-078
rating: A
rating_auto: A
rating_research: A  # PI 包成单客户，Simon 标签 活跃：活跃/可发展 → A（值得长期跟进）
name_official: "James Clendenan Systems Ltd."
score: 98
country: 加拿大
region: 北美
website: clendenan.ca
type: 系统集成/工程（北温哥华）
tier_tags: ["补录", "已成单", "PI成单", "Simon:活跃", "Xtransfer", "成交(PI)"]
deal: yes
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 19 msgs (out 13 / in 6), 2024-06-27 -> 2026-08-31
p1: STC-448DGGPM
price_tier: 25%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-28
```

## SALES BRIEF（压缩模型）

- **是谁**：已成单 4 次（2024-06 4 台 / 2024-12 6 台 / 2026-08-30 12 台 @ $335）；Simon 标签：活跃 · Xtransfer · 轻度绑定；详见 research/SA-078.json（调研 2026-10-22；表内兴趣：工业 PoE 管理交换机（STI-21616DGGPM 裸板贴牌 SW-3200-16GP-2SM/2SX）、商用 10G 管理（STC-424XGGM）、STI-488XGGPM）
- **为什么是 A 级**：**调研后定级 A**（PI 包成单客户，Simon 标签 活跃：活跃/可发展 → A（值得长期跟进））；自动分级 A：+50 有成单/下单/买过记录（用户备注或跟进表）；+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/加拿大；+5 最近活动 2026
- **历史互动**：成交/下单过
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-488XGGPM / STI-21616XGGPM（在购系列，AC5）｜他 8/26 问的 mGig PoE：CENTEC STH-8DX24VP-HSI（24×2.5/5G PoE++ + 8×25G/10G，双 CRPS）/ STH-2C24XP-HSI（24×10G mGig PoE++ + 2×100G），见 `docs/reference/CENTEC_产品表与报价锚_2026-10-24.md`；价/现货 → Simon（Q-56）｜便宜路径：Realtek STC-624XGDGPM（6×10G SFP + 24×2.5G PoE bt 400W，L3 网管，$396 EXW，单电源，`data/hrui_STC对照表.csv`）——双电源 + PWM 风扇只有 CENTEC — OEM 品牌商档（装进自己的产品）；每一次固件/机械适配都是替换成本（C4/C5）｜毛利复盘：21.7% → 29.3%，正常区间；第四单（2026-09 12 × $335）成本表未更新；第 4 单 $335/台（2026-08-30 PI 为准）；复购沿用；2026-06-22 报价单 STS-20260622-001：裸板 STI-21616DGGPM-PCB $230 / 无壳整机 $240（含 MQTT + LLDP-MED 定制），运费 UPS $180 + 银行 $25 = $1,605——他的 ODM 形态是买板装自己的壳
- **第一问（只问一个）**：For the MQTT setup, what exactly does SCOUT need from the switch side — periodic port/PoE status publish, or alarms only? (And on the power-board rework: which of the four requests is a must-have for the next batch?)
- **最大未知**：年走量与现供应商
- **下一步**：2026-11 上旬（12 台到货后） LinkedIn/WeChat（Simon U28：James 只走这两个） 到货确认 + 问 MQTT 对接需要交换机侧提供什么（Topic/字段），把需求写成一页给 SmartByte；同一封里把《JCSL-Custom power pcb》四项需求逐条回「能/不能/要多少量」，别只回 MQTT；**同一条私信顺手把 8/26 的 mGig PoE 问题正面答了：有（CENTEC 24 口 mGig PoE++，双电源 + 热插拔风扇 + 机架），要不要规格书**

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SA-078` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度（Simon U28 定级）——按 J4 证据为**中度偏深**：客户围绕 Saga 的 4+8 PCB 做自己的机械设计、要求固件定制、2026-07 测 AC5 更新并要做 MQTT 对接、第 4 单 2026-08-30 12 台 @ $335；Elsa 箱：`to:.ca` 穷举 13 条（2026-10-25，锚批 Bcc 头已读）未见 clendenan.ca → Elsa 箱从未发过本户，往来只在 S/A 箱（去 13 / 来 6）（第 74 批(f)）** ｜ 类型：加拿大小型控制/集成公司（Control Ready / SCOUT 产品）（技术流，自研硬件 + 软件） ｜ 筛子：3（4 单 $6,740、Xtransfer、PCB 布局确认、固件定制讨论） ｜ 停点：无停点，节奏慢（项目制小批量）；唯一硬需求 UL 版 PSU（2024-06 Simon 承诺「working on the UL listed PSU 52~57VDC 250W~300W」，全库唯一 UL 需求） ｜ 复活：已在复购；下一级 = MQTT 对接落地（他的 SCOUT 平台直接读 Saga 交换机）→ 深绑定候选 ｜ 通路：CA 已通（Xtransfer、DHL/UPS DAP） ｜ 节奏：最后 2026-08-31 James 回执（PI USD 版）；2026-09-07 PI 包最后单；实质往来 2024-06 → 2026-08，来 6 封（主要在 LinkedIn/WeChat，Simon U28） ｜ 证据：S 邮箱 k=e248bc0c33c534e6 / 51d9acb9ee095737 / aa61c45fc8e5eb33 / ba36e2ca75bc3155；PI 包 4 单；S 邮箱 19 封（2024-06-27 → 2026-08-31，均为 LinkedIn 对话后的单据/固件邮件；jsonl client 字段为空，按域名重扫补入）
- **现状一句话**：加拿大 James Clendenan Systems（James，controlready.ca / SCOUT）2024-06 首单即问「what kind of software customizations we can do… I'll likely want to do a few changes to the firmware」；2024-12 确认 4+8 PCB 布局与自己的机械设计一致；2026-07 测 AC5 更新后「then we can work on the mqtt setup」；2026-08-26 Simon 给 AC5 BIN + 新料号报价，08-30 PI STSC20260830010（12 台 @ $335），USD 版 08-31。**全库最像「深绑定」路径的小客户：把 Saga 板子装进自己的产品，软件对接在推进。**
- **对方真实需求（有据）**：① STI/STC 工业系列板级/整机（4+8 口 PoE）装入自有机箱；② 固件定制 + MQTT 上报（接 SCOUT 平台）；③ UL listed PSU 52–57 VDC 250–300 W（2024-06 起）；④ AC5 BIN 持续更新。 ⑤（2026-08-26《JCSL-Custom power pcb》）电源板改版：电源/告警接点改出板背（Molex MiniFit-JR / JST）、加 i2c 温度传感器、2 个 PWM/TAC 风扇头（Noctua 4-pin 5V）、板上再出 75W 12V DC 给其 PC 模块，高度不超现有板距，FCC Part 15 B / CE / RoHS；⑥（《长期需求》）2.5G/mGig PoE+ 管理型、双电源、机架、PWM 风扇控制。
- **断点 / 为什么停在这里**：没有断点；风险是 MQTT 对接若需要 Saga 侧固件开发，会撞「不做 SDK/API」边界（E2）——MQTT 上报属固件功能而非 SDK，需 Simon 与 SmartByte 确认 7.5.x 是否已有（不由代理问 Peter）。 新增：电源板四项改版是 PCB 级 ODM——HRUI/SmartByte 侧是否愿为 12 台/单的量开板（Angora 的 PC0012 代工询问也停在同一处），要先问 Peter 的 MOQ 而不是先答应 James。
- **Saga 现在该推什么**：P1 **STI-488XGGPM / STI-21616XGGPM（在购系列，AC5）｜他 8/26 问的 mGig PoE：CENTEC STH-8DX24VP-HSI（24×2.5/5G PoE++ + 8×25G/10G，双 CRPS）/ STH-2C24XP-HSI（24×10G mGig PoE++ + 2×100G），见 `docs/reference/CENTEC_产品表与报价锚_2026-10-24.md`；价/现货 → Simon（Q-56）｜便宜路径：Realtek STC-624XGDGPM（6×10G SFP + 24×2.5G PoE bt 400W，L3 网管，$396 EXW，单电源，`data/hrui_STC对照表.csv`）——双电源 + PWM 风扇只有 CENTEC**（30% 档，第 4 单 $335/台（2026-08-30 PI 为准）；复购沿用；2026-06-22 报价单 STS-20260622-001：裸板 STI-21616DGGPM-PCB $230 / 无壳整机 $240（含 MQTT + LLDP-MED 定制），运费 UPS $180 + 银行 $25 = $1,605——他的 ODM 形态是买板装自己的壳）——OEM 品牌商档（装进自己的产品）；每一次固件/机械适配都是替换成本（C4/C5）｜毛利复盘：21.7% → 29.3%，正常区间；第四单（2026-09 12 × $335）成本表未更新
  - 复购/在买项：STI-488XGGPM 12 台（2026-08-30）；STI-21616DGGPM/XGGPM（2024 两单）
  - 做不了 / 要先核的：UL 版 PSU：给 MEAN WELL UL 型号 + 价（交换机本体不承诺 UL）——Simon 2024-06 的承诺要有个结论；MQTT：7.5 L2+ 功能表 ☑（Message Queuing Telemetry Transport）——已核，不用再问 Simon；要问 James 的是 SCOUT 侧要什么 Topic/字段；电源板改版（4 项）的可行性/MOQ/NRE——先内部核再回 James；2.5G/mGig PoE+ 双电源机架：AC5 无；CENTEC STH-8DX24VP-HSI / STH-2C24XP-HSI（双 CRPS，无价，Q-56）；单电源便宜路径 Realtek STC-624XGDGPM $396——已核；Simon《STH计划》：1G/2.5G/5G 铜口 CENTEC 机「暂不宣传、信息备好」→ 信稿只答「on request / not on published list」，不主推；估算带见 CENTEC 锚表 §5.3，对客户仍 price on request
- **下一步（具体）**：2026-11 上旬（12 台到货后）　LinkedIn/WeChat（Simon U28：James 只走这两个）　到货确认 + 问 MQTT 对接需要交换机侧提供什么（Topic/字段），把需求写成一页给 SmartByte；同一封里把《JCSL-Custom power pcb》四项需求逐条回「能/不能/要多少量」，别只回 MQTT；**同一条私信顺手把 8/26 的 mGig PoE 问题正面答了：有（CENTEC 24 口 mGig PoE++，双电源 + 热插拔风扇 + 机架），要不要规格书**
  - 第一问（只问一个）：For the MQTT setup, what exactly does SCOUT need from the switch side — periodic port/PoE status publish, or alarms only? (And on the power-board rework: which of the four requests is a must-have for the next batch?)

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-06-27 | 去 | Simon → James（Invoice.pdf） | Thanks for your information on LinkedIn. Please see attached invoice… I am now working on the UL listed PSU. 52~57VDC output. 250W~300W power | 首单（2024-06-28 James「Wire sent to bank」）：LinkedIn 谈、邮件只发单据；James 从第一单就要 UL 电源 + 「a few changes to the firmware along the way」 | `gmail_s（clendenan.ca 19 封，jsonl client 字段为空，按域名重扫）` |
| 2024-06-27 | 内 | Saga 出口报关资料（PI 包，1st order） | 货物情况说明表：工业交换机 STI-21616DGGPM × 4，8517622990，单价 215 / 总价 860 USD（FOB），品牌 Saga Telecom，生产厂家 Zhengzhou Saga Telecom Co., Ltd.，23×18×7 cm，240W，Metal | 第一单申报口径：品牌与厂家都填 Saga（郑州）——James 后来的两单改为「无品牌 + 他自己的型号名」 | `data/pi_2026-10/text/…10_加拿大_James…1st_order_sample 买单报关资料.xls (0fbeaf83)` |
| 2024-06-28 | 来 | James Clendenan | Please let me know what kind of software customizations we can do together for these. I'll likely want to do a few changes to the firmware | 首单即技术绑定意图 | `e248bc0c33c534e6` |
| 2024-12-18 | 来 | James Clendenan | Working with my mech eng to confirm placement is still identical to what we have designed for | 客户机械设计围绕 Saga PCB（替换成本） | `51d9acb9ee095737` |
| 2024-12-18 | 去 | Simon → James（4+8 PCB layout.dxf） | please check attached a copy of 4+8 model PCB layout. Mounting holes&positioning will be EXACTLY the same for old and new versions… you can think of this as a c[ompatible replacement] | James 12-18「Working with my mech eng to confirm placement is still identical to what we have designed for」→ 客户机械结构围绕 Saga 4+8 板设计 = 换供应商要重开模；12-19 PI STSC20241219010 | `gmail_s（clendenan.ca 19 封，jsonl client 字段为空，按域名重扫）` |
| 2024-12-19 | 内 | Simon 成本表（PI 包） | 内部《成本统计.xlsx》：STSC20240627010：成本 6,238 / 收款 7,968 / 利润 1,729（21.7%） · STSC20241219010：成本 8,368 / 收款 11,840 / 利润 3,472（29.3%） | 利润率 = 利润÷收款；对照 20/25/30 加价 = 16.7%/20%/23% 毛利；详见 docs/成单客户_毛利复盘_内部_2026-10-24.md | `cost_sheet` |
| 2024-12-19 | 内 | Saga 出口报关资料（PI 包，2nd order） | 工业交换机 SW-3200-16GP-2SM × 4 @ 215 = 860 USD；SW-3200-8GP-4S+ × 2 @ 265 = 530 USD；158×115×54 mm；无品牌；申报总价值 1,625 USD，总毛重 8 kg，目的国加拿大 | 从第二单起报关型号就用 James 的 SW-3200 系列名、品牌「无」——他的产品化从 2024 年底就开始了；$265 的 8GP-4S+ = 4+8 PoE 工业机（后来 2025-08 的 AC5 固件也只给这款） | `data/pi_2026-10/text/…10_加拿大_James…2nd_order_sample 发票_买单报关.xlsx (58299045)` |
| 2025-08-28 | 去 | Simon → James | Please download the newest firmware from below WeTransfer link… It is ONLY for SW-3200-8GP-4S+(AC5 chip). For AC3 mo[dels…] | 客户自有型号名 SW-3200-8GP-4S+（= Saga 4+8 PoE 工业机 AC5 版）；固件按客户型号单独打包——软件层绑定 | `gmail_s（clendenan.ca 19 封，jsonl client 字段为空，按域名重扫）` |
| 2025-11-19 | 去 | Simon → James（NMS-MIB.rar + SWITCH-MIBS-release-7.3.0.docx） | Based on our conversation on LinkedIn, please see attached MIBs information. Let's talk again after your review. | James 要把设备接进自己的 NMS（后来 2026-07 要做 MQTT）——与 Angora 一样走「OID/管理系统接入」这条绑定路径 | `gmail_s（clendenan.ca 19 封，jsonl client 字段为空，按域名重扫）` |
| 2026-06-22 | 去 | Simon → James Clendenan（Quotation STS-20260622-001，DAP North Vancouver） | STI-21616DGGPM-PCB (customer P/N SW-3200-16GP-2SM; PCB ONLY, AC5, no optics/PSU/enclosure, "Support mqtt and lldp-med") × 4 @ $230 = $920; STI-21616DGGPM standalone unit (DIN, no enclosure/PSU) × 2 @ $240 = $480; "Put customer model name on WEB UI and label"; UPS air to Canada $180 incl. insurance; bank $25; TOTAL $1,605. | 他的 ODM 形态：买裸板（PCB）装进自己的机箱，型号用他的 SW-3200-16GP-2SM，WEB UI 与标签印他的名——这就是 8/26 他提电源板改 Molex/JST、加温度传感器的由来；裸板 $230 比老表整机 $220 还贵（MQTT/LLDP-MED 定制固件 + 小量） | `Drive Extra Info `Quotation__STS-20260622-001.xls`` |
| 2026-07-21 | 来 | James Clendenan | Will test the ac5 update tomorrow and then we can work on the mqtt setup | AC5 迁移 + MQTT 对接在推进 | `aa61c45fc8e5eb33` |
| 2026-07-21 | 去 | Simon → James | 1. AC3 models are almost out of stock now, we are fully transitioning to AC5 models. The WEB UI an[d…] | AC3→AC5 切换通知；08-07 补发两个 BIN（AC3 lite-hotfix-7.3.13「final, there will not be any updates」+ AC5）；08-26 新料号报价 STSC-20260826-001 → 08-30 PI STSC20260830010（USD 版 08-31） | `gmail_s（clendenan.ca 19 封，jsonl client 字段为空，按域名重扫）` |
| 2026-08-06 | 来 | James Clendenan | Can you send me this again? I missed getting it before it expired.（AC5 固件 WeTransfer 链接过期） | WeTransfer 7 天过期——给客户固件别只用临时链接 | `gmail_s 9efe5d1b1132a14a` |
| 2026-08-07 | 去 | Simon（S 邮箱） | It is 2 BINs: 1. AC3 version: lite-hotfix-7.3.13 — This is final, there will not be any updates, just maintenance and support. We are doing AC5 version now. 2. For AC5 version, please use this for now: ac5-hotfix-7.4.2 | AC3 固件终版 = lite-hotfix-7.3.13（只维护不更新）；AC5 当时 7.4.2——给老客户的固件口径 | `gmail_s 3e84bddd5a4fd519` |
| 2026-08-26 | 去 | Simon | Please check below WeTransfer link for the AC5 BIN info… attached quotation with new part number | 第 4 单前置 | `ba36e2ca75bc3155` |
| 2026-08-26 | 来 | James（JCSL-Custom_power_pcb.docx） | Request 1 – Modify the Power PSU circuit board to have power and alarm contacts exit the BACK of the module… Molex MiniFit-JR for power, JST for alarm. Request 2: Add thermal sensor (i2c/i3c) to Power board… if facilities exist in the marvell software. Request 3: Add 2 pcs of fan headers… 40mm PC fan using PWM and TAC support in OS (Noctua 4-pin 5V). Request 4: additional DC-DC buck convertor to provide 75w of 12v DC… to power the PC… Must meet FCC Part 15 Class B, CE, RoHS | James 的产品是「Saga 4+8 板 + 自家 PC 模块」的一体机：要求电源板改连接器方向、加温度传感器、PWM 风扇头、12V/75W 给 PC 供电——这是 PCB 级 ODM 需求，不是贴牌；第 4 单（P20260831-03 未税 ¥20,160，12 台 @ $335）之后，这张需求单就是下一单的入口 | `Drive PI 文件夹（data/pi_2026-10/text） 10_James` |
| 2026-08-26 | 来 | James（长期需求.docx） | Do you have any plans for a 2.5g or mgig poe+ switch? Managed, L2 or L2+. Dual power would be great as well. I see it also in broadcast and outdoor cameras. Rack mount more common. But needs pwm fan control too | 长期需求 = 2.5G/mGig PoE+ 管理型 + 双电源 + 机架 + PWM 风扇控制。**AC5 线没有多千兆铜口**（DG 只是 2.5G 光口，规则 ⑰）；正对他四个条件的是 CENTEC VastLakes 表（2026/Q2）上的 STH-8DX24VP-HSI（24×2.5/5G PoE++ + 8×25G/10G SFP28，双 CRPS + 热插拔风扇模块，机架）或 STH-2C24XP-HSI（24×10G mGig PoE++ + 2×100G）；商用 0–40℃；仓内无价、现货未知（Q-54/Q-56）——这是能正面回他的一句「有」，别再含糊 | `Drive PI 文件夹（data/pi_2026-10/text） 10_James` |
| 2026-08-31 | 来 | James Clendenan | [image0.jpeg] Sent（回 Simon 08-30「a copy of the revised PI in USD」） | 付款凭证截图——12 × SW-3200-16GP-2SX @ $335 = $4,020 的那单 | `gmail_s 3287d81fe10e8f5f` |
| 2026-09-07 | 内 | Saga 出口报关资料（PI 包，买单_STSC20260830010.xlsx） | 出口货物确认函：工业交换机 SW-3200-16GP-2SX × 12 台 @ 335 = 4,020 USD，1 纸箱，总毛重 20 kg，净重 14.4 kg，158×115×54 mm，Metal，无品牌，8517622990，一般贸易，目的国加拿大 | 第四单（12 台，PI STSC20260830010）的实际发运口径：单台净重 1.2 kg、整单一箱 20 kg——报 DAP 运费时可直接用；「无品牌」= 他要的中性外观 | `data/pi_2026-10/text/…10_加拿大_James…买单_STSC20260830010.xlsx (fccde3ae)` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：LinkedIn/WeChat 侧对话不在邮件里（Simon U28）；UL PSU 承诺的后续

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **发信窗口（CA 全库 681 封群发的打开标签，对方本地时间；均值 5.7%）**：周五 12–14 点 7.8%（51 封）、周二 12–14 点 7.8%（51 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **日历窗口**：对方：2026-12-24 圣诞–元旦（12-24 → 01-04） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-27 查）：**

- `clendenan.ca` → 自建 / 同域名邮件服务器（MX：dopey.clendenan.ca）。自建邮件服务器：有自己的 IT（可能灰名单 → 首封延迟几小时才进箱），像素可用；读信的是技术人，参数先于价格

**假日避让（加拿大 · 按下一步「2026-11」窗口 2026-11-01→2026-11-30）：**

- 窗口内无该国法定假日
- 【商业季】11-23→11-30：感恩节周 + 黑五 / 网一：11-26 法定、11-27 实际放假；零售 / 电商类客户整周最忙，别推销

**公司底数 · 第 85 批（加拿大 · 联邦 / 省登记可查但研究档无法定名与省份线索；本行为「无登记源」记录（据第 79 批研究档），2026-10-27 查；）：**

- 法定名 / 登记号：James Clendenan Systems Ltd. · — · 状态 **（登记状态不可免费核）** · 成立 — · —
- 注册地址：—
- 规模档：—
- 账目：—
- 高管：James Clendenan — 单据联系人（研究档）
- 控制人 / 股东：—
- **这意味着什么：**
  - **本轮无免费官方登记源**（加拿大 · 联邦 / 省登记可查但研究档无法定名与省份线索）：以研究档事实为准，不臆断股东 / 财务；对外口径照常，不提「核查」
  - 无登记 = 无信用公开 → 付款默认 100% 预付 T/T（成单客户除外）；量级按研究档 staff / 网店体量判
- 备注：无免费登记源；下一轮若找到镜像再补。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | James Clendenan Systems Ltd. | 事实（用户表） |
| 国家 | 加拿大 | 事实（用户表）|
| 网站/域名 | clendenan.ca | 事实（用户表 URL/邮箱域名） |
| 类型 | 系统集成/工程（北温哥华） | 推断（据兴趣/备注关键词） |
| 联系人 | James Clendenan | 事实（用户表） |
| 来源（From） | 补录：PI 包成单客户（T29-U8） | 事实（用户表） |
| 兴趣（Interested in） | 工业 PoE 管理交换机（STI-21616DGGPM 裸板贴牌 SW-3200-16GP-2SM/2SX）、商用 10G 管理（STC-424XGGM）、STI-488XGGPM | 事实（用户表） |
| 用户备注（Remark） | 已成单 4 次（2024-06 4 台 / 2024-12 6 台 / 2026-08-30 12 台 @ $335）；Simon 标签：活跃 · Xtransfer · 轻度绑定；详见 research/SA-078.json | 事实（用户表） |
| 用户分档（Category） | 系统集成/工程（北温哥华） | 事实（用户表） |
| 所在清单 | 补录、已成单、PI成单、Simon:活跃、Xtransfer、成交(PI) | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-22）**　网站状态：
- **是谁**：已成单 4 次（2024-06 4 台 / 2024-12 6 台 / 2026-08-30 12 台 @ $335）；Simon 标签：活跃 · Xtransfer · 轻度绑定；详见 research/SA-078.json
- **类型**：系统集成/工程（北温哥华）
- **【PI】成交单据 STSC20240627010（CI，2024-06-27）：STI-21616DGGPM 共 9 台，USD 1095.0；采购 SmartByte RMB 4908.0；Simon 成本表利润 RMB 1729.39**
  > 来源：PI.zip:10 加拿大 James 活跃 Xtransfer 轻度绑定/CI.xls（抓取 2024-06-27）
- **【PI】成交单据 STSC20241219010（PI，2024-12-19）：STC-424XGGM、STI-488XGGPM 共 6 台，USD 1625.0；采购 SmartByte RMB 7684.0；Simon 成本表利润 RMB 3472.13**
  > 来源：PI.zip:10 加拿大 James 活跃 Xtransfer 轻度绑定/STSC20241219010.xls（抓取 2024-12-19）
- **【PI】成交单据 STSC-20260826-001（Quotation，2026-08-26）：STI-21616XGGPM、SW-3200-16GP-2SX 共 12 台，RMB 28975.0**
  > 来源：PI.zip:10 加拿大 James 活跃 Xtransfer 轻度绑定/STSC-20260826-001.xlsx（抓取 2026-08-26）
- **【PI】成交单据 STSC20260830010（CI，2026-09-07）：Industrial Switch 共 12 台，USD 4020.0；采购 SmartByte RMB 20160.0**
  > 来源：PI.zip:10 加拿大 James 活跃 Xtransfer 轻度绑定/发票_STSC20260830010.xlsx（抓取 2026-09-07）
- **【PI】PI 包文件夹「加拿大 James 活跃 Xtransfer 轻度绑定」：Simon 标签 活跃，收款 Xtransfer，轻度绑定；单号 4 个，2024-06-27 → 2026-09-07，销售 USD 6740.0 / RMB 0，Simon 成本统计利润合计 RMB 5201.52**
  > 来源：PI.zip:10 加拿大 James 活跃 Xtransfer 轻度绑定（抓取 2026-10-22）
- **【S 邮箱原文】2024-06-27 Simon 向 James 发 Invoice 并承诺「I am now working on the UL listed PSU. 52~57VDC output. 250W~300W power budget」；James 2024-06-28 回复在 24–36 小时内付款；UL 需求只落在 PSU 配件，不在交换机**
  > I am now working on the UL listed PSU. 52~57VDC output. 250W~300W power budget. I will let you know if I have news.
  > 来源：（S 邮箱 2024-06-27 07:25Z Simon→james@clendenan.ca 主题 Invoice，data/gmail_s/messages/2024/2024-06.jsonl）（抓取 2026-10-22）
- **【公开平台核查（T29-U18）】Control Ready 官网：加拿大应急/活动响应技术方案，SCOUT（Smart Connection Operations United Toolkit）便携 Wi-Fi/电话/数据箱，BARK（Boundary Alert Response Kit）拖车传感告警，POST 应急数字标牌；均「Designed and Built in Canada with local components and suppliers」**
  > SCOUT … Resilient, to-go Wi-Fi, phone, and data storage solutions for event management—all in convenient grab-and-go cases … Built in Canada with local canadian components and suppliers
  > 来源：https://www.controlready.ca/（抓取 2026-10-23）
- **【公开平台核查（T29-U18）】Control Ready About：James Clendenan Systems Ltd. 2012-09 创立；James = Queen's 计算机工程，曾任职 Pixar Canada / Sophos / HootSuite / 奥运转播 OBS；专长 ISP 与中小企业网管**
  > James Clendenan Systems Ltd. was launched by James Clendenan in September 2012 … His past experience include stints with Pixar Canada, Sophos, HootSuite, and the Olympic Broadcasting Service
  > 来源：https://www.controlready.ca/about（抓取 2026-10-23）
- **【公开平台核查（T29-U18）】Alignable 商家页：北温哥华，电信/计算机服务/ISP；托管网络起价 15$/设备/月；光纤熔接、固定无线、电话系统**
  > Managed Networks Starting at 15$/device/month for monitoring and configuration services … Networking, Wi-Fi, Fixed Wireless, Fiber Optics splicing and repair
  > 来源：https://www.alignable.com/north-vancouver-bc/james-clendenan-systems-ltd（抓取 2026-10-23）
- **【Simon 口述】绑定等级：轻度绑定（基于沟通、订单和实际使用）；也是微信/领英渠道唯一的成单客户**
  > Angora james这些都是轻度绑定，都是基于沟通，客户订单和实际使用等等角度来衡量的……这个主要就是指加拿大成单的James 其他的似乎没了
  > 来源：docs/requirements/对话全记录.md § T29-U28（抓取 2026-10-23）
- **【Simon 文档】绑定等级（文档）：轻度绑定——「前期客户投入了较大精力，产品也没啥问题」**
  > 加拿大 James　轻度绑定 = 前期客户投入了较大精力，产品也没啥问题
  > 来源：Extra Info.zip 根目录《客户绑定情况分析.docx》（data/extra_info_2026-10/text/Extra_Info__客户绑定情况分析.docx__6d196b92.json）（抓取 2026-10-22）
- **KP**：James Clendenan（单据联系人）james@clendenan.ca 〔PI.zip 单据〕
- **调研后定级**：A（原自动 A）——PI 包成单客户，Simon 标签 活跃：活跃/可发展 → A（值得长期跟进）
- 备注： ｜ 针对性加厚 2026-10-22（UL PSU 线索，T29-U13 ②）

### 加厚挖掘（2026-10-23 · 公开平台核查（T29-U18，针对性：只核活跃平台与触达通道））

- **触达通道（公开）**：公开动态平台（监控中，T29-U18）: 新品牌 Control Ready（controlready.ca，Squarespace）：SCOUT 移动办公箱 / BARK 移动告警套件 / POST 应急数字标牌；Alignable 商家页；LinkedIn 个人页（James Clendenan）
- **近况信号**：
  - 2026-10-23 核查：James 另起品牌 Control Ready——面向应急/活动响应的「拎走即用」套件（SCOUT Wi-Fi+电话+存储箱、BARK 拖车传感告警、POST 标牌），宣称 Built in Canada with local components → 套件里需要小型宽温 PoE/工业交换机；可把 STI-154GP / STI-288DGGPM 作为 SCOUT 箱内件推荐（注意其「本地元件」话术，供货以中性包装）
- **风险/边界**：【2026-10-22 第二遍复盘】S 邮箱全库 13,583 封里唯一的 UL 需求来自本户（UL listed 52–57 VDC 250–300 W PSU，2024-06）；Simon 2023-12 曾向 Mencom 问 UL DIN 电源 → 跟进时可直接给 MEAN WELL UL 版电源型号 + 价格（Drive《SmartByte》有 MEAN WELL 价目表），交换机本体不承诺 UL。
- **Saga 对位结论**：P1 待核型（无标准对应）（25% 档）——成单客户，按实际成交型号续单；贴牌/裸板需求按 OEM 30% 档单独核价

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 成交记录（PI 包 · 自动汇总）

- **Simon 的标签**（PI 包文件夹名）：**活跃**　|　收款：Xtransfer　|　轻度绑定　|　买方抬头：James Clendenan Systems Ltd.
- **单号** 4 个（2024-06-27 → 2026-09-07）　|　**销售** USD 6,740　|　**Simon 成本表利润** RMB 5,202

| 单号 | 日期 | 单据 | 型号 | 数量 | 金额 | 采购（卖方 / RMB） | Simon 成本表（成本 / 收款 / 利润 RMB） |
|---|---|---|---|---|---|---|---|
| STSC20240627010 | 2024-06-27 | CI | STI-21616DGGPM | 9 | USD 1095.0 | SmartByte / 4908.0 | 6238.26 / 7967.65 / 1729.39 |
| STSC20241219010 | 2024-12-19 | PI | STC-424XGGM、STI-488XGGPM | 6 | USD 1625.0 | SmartByte / 7684.0 | 8367.78 / 11839.91 / 3472.13 |
| STSC-20260826-001 | 2026-08-26 | Quotation | STI-21616XGGPM、SW-3200-16GP-2SX | 12 | RMB 28975.0 | — | — |
| STSC20260830010 | 2026-09-07 | CI | Industrial Switch | 12 | USD 4020.0 | SmartByte / 20160.0 | — |

> 口径：同一单号多份文件取 CI > PI（最新修订）> Quotation；Quotation 行不计入销售合计；明细见 `data/pi_orders/销售单据明细.csv`、采购价见 `采购合同明细.csv`；原件在 Release `files-pi_2026-10`。

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：19 封（去 13 / 来 6）　|　**期间**：2024-06-27 → 2026-08-31　|　**最后去信**：2026-08-31
- **对方邮箱**：james@clendenan.ca
- **最后一封来信**：2026-08-31 james@clendenan.ca「Re: Information」：[图:image0.jpeg]Sent James -- Sent from my phone. Mobile: 604-910-5745

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Information | 2026-08-26 | 2026-08-31 | 1 | 3 | 4 |
| Information | 2026-07-21 | 2026-08-07 | 2 | 2 | 0 |
| MIBs Info | 2025-11-19 | 2025-11-19 | 0 | 1 | 2 |
| 4+8 PCB layout | 2024-12-18 | 2025-08-28 | 1 | 3 | 3 |
| Invoice | 2024-06-27 | 2024-07-18 | 2 | 4 | 3 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：成单精选层　|　**自动源**：5 个　|　**数据截至**：2026-10-28T08:44:48Z　|　**最近变化**：2026-10-23T02:54:23Z
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SA-078/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [controlready_home](https://www.controlready.ca/) | html | HTTP 200 | 2026-10-23T02:54:23Z | 2495 字符；首行：Control Ready |
| [controlready_scout](https://www.controlready.ca/scout) | html | HTTP 200 | 2026-10-23T02:54:23Z | 1423 字符；首行：SCOUT: Smart Connection Operations United Toolkit — Control Ready |
| [controlready_about](https://www.controlready.ca/about) | html | HTTP 200 | 2026-10-23T02:54:23Z | 2264 字符；首行：About — Control Ready |
| [jcs_home](https://www.clendenan.ca/) | html | ConnectionError: HTTPConnectionPool(host='clendenan.ca', por | 2026-10-23T02:54:23Z | 老域名（2026-10-23 02:40Z 沙箱侧抓取失败，待运行器核实）；2026-10-23 首轮 https://clendenan.ca/ 连接失败，改 www + htt |
| [auto_home](https://clendenan.ca/) | html | ConnectionError: HTTPSConnectionPool(host='clendenan.ca', po | - | 官网首页（T27 快照状态 unknown） |

- **人工定期看（登录墙，不自动抓）**：LinkedIn 个人页：James Clendenan（Queen's 计算机工程；前 Pixar Canada / Sophos / HootSuite / OBS）；Alignable 商家页（反爬 429，人工看）: https://www.alignable.com/north-vancouver-bc/james-clendenan-systems-ltd

## 联系方式（已有 · 原值照录）

- 邮箱：`james@clendenan.ca`〔企业邮箱；来源：用户表原值〕
- 电话：`+16049105745`〔电话/WhatsApp 状态未记；原值见来源表〕
- 电话：`+2026083012`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：James Clendenan
- 职位（原值）：Owner
- 网站/域名：clendenan.ca
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| James Clendenan | 单据联系人 | james@clendenan.ca | 调研核实（公开页） | PI.zip 单据 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 补录客户.jsonl#(补录):5 | PI-004 | James Clendenan Systems Ltd. | 加拿大 | James Clendenan | 补录：PI 包成单客户（T29-U8） | 工业 PoE 管理交换机（STI-21616DGGPM 裸板贴牌 SW-3200-16GP-2SM/2SX）、商用 10G 管理（STC-424XGGM）、STI-488XGGPM | james@clendenan.ca +1 604 910 5745 https://clendenan.ca | 已成单 4 次（2024-06 4 台 / 2024-12 6 台 / 2026-08-30 12 台 @ $335）；Simon 标签：活跃 · Xtransfer · 轻度绑定；详见 research/SA-078.json Owner | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-448DGGPM | 48 口 PoE 走量款 | $308.0 USD EXW（㉕ 封顶：25% 档 $321.4 高于 2026-06 Saga 列表价 $308.0，按列表价；SmartByte LT-S8352GP-4GX48GT 1720 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | 据用户表兴趣/备注推断；档位 25%（系统集成/工程（北温哥华）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-448DGGPM），备选型不进首触。

- **第 1 次**：老客户回访——问上次所购型号的使用情况 + 告知 Marvell 新款（STC-448DGGPM）；只问一个问题：当前在采购的主力型号与月量。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有成交史，信任与开户成本已付；北美主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STC-448DGGPM 按 25% 档报价，做现供应商的第二货源
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

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：WhatsApp / 私信一句话（复制即发；不发邮件）

```text
For the MQTT setup, what exactly does SCOUT need from the switch side — periodic port/PoE status publish, or alarms only? (And on the power-board rework: which of the four requests is a must-have for the next batch?)

(第二条，可同日发) James — on your August question about a 2.5G/mGig PoE switch: yes. It is not on our published list (we publish the 10G/25G/100G CENTEC models), but on request we can supply a CENTEC 24 x 2.5/5G multi-gig PoE++ unit with 8 x 25G/10G SFP28 uplinks, dual hot-swap power modules and hot-swap fan modules, 1U rack (and a 24 x 10G multi-gig PoE++ version with 2 x 100G). Commercial temperature, L3 software. There is also a cheaper single-PSU path: 24 x 2.5G PoE++ (400 W) + 6 x 10G SFP+, L3, on our commercial Realtek line at $396 USD EXW. Want the datasheets, or is this a 2027 topic for SCOUT?
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-11**（14 天）：无回复 → 换通道再试一次；仍无 → 降 B。有任何回复 → 当即更新 research JSON 并重渲染。

## 变更日志

- 2026-10-28：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 A，分数 98）

---

*建档日期：2026-10-28　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
