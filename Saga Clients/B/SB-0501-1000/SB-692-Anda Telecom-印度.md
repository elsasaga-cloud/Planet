# Anda Telecom
**官方名称（调研核实）**：Anda Telecom Private Limited（诺伊达）

> **评级 B**　|　印度　|　档案编号 `SB-692`　|　优先级 ★★　|　状态：WhatsApp 已加·未回复
>
> **类型**：电信/ISP/网络运营（推断）　|　**历史关系**：WhatsApp 已加；推送 4 次（2025-02-14 → 2025-10-02）　|　**所在清单**：DWDM线索、E已回复　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-692
rating: B
rating_auto: B
name_official: "Anda Telecom Private Limited（诺伊达）"
score: 33
country: 印度
region: 南亚
website: andatelecom.com
type: 电信/ISP/网络运营
tier_tags: ["DWDM线索", "E已回复"]
deal: no
replies: 0
followups: 4
first_contact: 2025-02-14
last_contact: 2025-10-02
s_mail: 9 msgs (out 9 / in 0), 2024-06-19 -> 2025-02-14
p1: STI-288GPM
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-21
sources: 2
updated: 2026-10-27
```

## SALES BRIEF（压缩模型）

- **是谁**：印度诺伊达（+91 120）电信级光纤产品公司：自有 **ATMIS-** 系列管理 / 工业接入交换机（ATMIS-6208PI = 2 SFP + 8 PoE 工业、6216PI、6408PI、402G）、PDH / E1 转换、光复用器、MC、VoIP；表内 Director Harish Gupta「已有回复」，对台式 EDFA 很有兴趣（画了应用图），从 ONV 与其他国内厂采购，也买 AOA（光模块）。自有型号 = 贴牌 → OEM 30%。（调研 2026-10-21；表内兴趣：对EDFA台式很有兴趣 画了一个应用图；从ONV买 也有其他国内的 也买AOA的）
- **为什么是 B 级**：+12 备注记录了对方问价/要资料/见面等互动；+18 在「已回复」名单（A/E Replied）；-8 DWDM/光传输线索：Saga 不做 DWDM（Hohunet 线为交换机）；+10 有企业邮箱；+5 有可核实的公司网站/域名；-6 区域 南亚/印度；+5 最近活动 2025；-3 跟进表最近平台标记 E（已降为群发）
- **历史互动**：WhatsApp 已加；推送 4 次（2025-02-14 → 2025-10-02）
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-288GPM — 对位 ATMIS-6208PI → STI-288GPM 贴 ATMIS 标（OEM 30%）；6216PI → STI-21616GP；6408PI → STI-488GP。已打开的主题（1/9 封有打开记录）：「10G media converter」(2024-08-08) → 读者兴趣偏「10G 汇聚/L3」；与 P1 同类，继续｜需求台账 #1（2026-10-24 改正）：「Stacking is mandatory」的正确答法不是只说没有——AC5 没有，但 CENTEC STH1G（STH-2QX4DX48GP，≤8 台）有；信里两层都说；按主表（研究档 saga_fit）；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-12-27 $300（48 Port PoE Managed Switch）；群发里他已看到的价（续，第 66 批全量复核）：2024-08-08 $65（10G Media Converter）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-05-11 $280（10G Enterprise SFP Switch = STC-4168XGGCM 双 AC，Elsa 箱 3 轮 2025-10-02→2026-05-11；$280 仍是 Simon 在用的群发价（NYNEX 实付 $265.2）——别写主表 377–408 档）；2026-08-04 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-08-04；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170）
- **第一问（只问一个）**：Subhash — on stacking: our Marvell access units do not stack (redundancy there is ERPS G.8032 + 10G uplinks). Where stacking is mandatory we have the CENTEC-based STH-2QX4DX48GP, 48×1G PoE++ + 4×25G + 2×40G, stacking up to 8 units as one logical switch. Is stacking a tender clause in your projects, and at what port count?
- **最大未知**：年走量与现供应商
- **下一步**：2026-11 Elsa 邮箱 → subhash@andatelecom.com（抄 harish@） 首封前知悉：Elsa 已 1:1 去信 9 轮（2025-05-05→2026-08-04，0 回）（第 74 批(m)）；只问一句（第 75 批(ak) 2026-10-25：信稿复检修正——「ERPS G.8032 rings (<20 ms)」→「ring redundancy」）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-692` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（Elsa 邮箱 3 封来信：2025-06-17 Harish Gupta 董事催内部「Nitin/Subhash please reply」；2026-08-04 Subhash 两封——先要 datasheet，收到后答「will check… no a days Stacking is mandatory」；S/A 邮箱 9 封 1 次打开 0 回）；Elsa 1:1 去信 9 轮 2025-05-05→2026-08-04（To 仅本户 harish@andatelecom.com / info@andatelecom.com（按地址：harish@andatelecom.com 4 轮 / info@andatelecom.com 5 轮）；头 msg 19fcb2494a8853cf 核对无 Bcc，称呼「Hi, Harish」= 个性化逐月 1:1 名单；主题 Booster PoE Switch、Marvell Industrial Alert System、Updated Ethernet Switches Links、24 Port PoE Managed Switch…；0 回（Elsa 箱无 Re: 行））（第 74 批(m) `from:e.sagatelecom to:` 全程 complete，直收 9 条）** ｜ 类型：— ｜ 筛子：3（要了规格书、给了卡点） ｜ 停点：2026-08-04 对方「will check」后无下文（Elsa 侧） ｜ 复活：一封实话：AC5 固件堆叠的真实边界（见 SB-826 口径）+ 问「堆叠是标书硬条款还是运维习惯」 ｜ 通路：IN 次级（点名） ｜ 节奏：季度 ｜ 证据：gmail_digest：out 9，Opened 标签 1（Simon 群发追踪）；用户表：「兴趣：对EDFA台式很有兴趣 画了一个应用图;从ONV买 也有其他国内的 也买AOA的」；研究档 risks：EDFA 为其兴趣点（Saga 无）；Elsa 邮箱 `data/gmail_e/text/`（Replied 线程，客户→Elsa 正文；Elsa 回复正文未入库）
- **现状一句话**：印度诺伊达（+91 120）电信级光纤产品公司：自有 **ATMIS-** 系列管理 / 工业接入交换机（ATMIS-6208PI = 2 SFP + 8 PoE 工业、6216PI、6408PI、402G）、PDH / E1 转换、光复用器、MC、VoIP；表内 Director Harish Gupta「已有回复」，对台式 EDFA 很有兴趣（画了应用图），从 ONV 与其他国内厂采购，也买 AOA（光模块）。自有型号 = 贴牌 → OEM 30%。
- **对方真实需求（有据）**：对位 ATMIS-6208PI → STI-288GPM 贴 ATMIS 标（OEM 30%）；6216PI → STI-21616GP；6408PI → STI-488GP。
- **断点 / 为什么停在这里**：堆叠（stacking）被视为必需；AC5 口径与 Versitron 同题
- **Saga 现在该推什么**：P1 **STI-288GPM**（30% 档，按主表（研究档 saga_fit）；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-12-27 $300（48 Port PoE Managed Switch）；群发里他已看到的价（续，第 66 批全量复核）：2024-08-08 $65（10G Media Converter）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-05-11 $280（10G Enterprise SFP Switch = STC-4168XGGCM 双 AC，Elsa 箱 3 轮 2025-10-02→2026-05-11；$280 仍是 Simon 在用的群发价（NYNEX 实付 $265.2）——别写主表 377–408 档）；2026-08-04 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-08-04；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170））——对位 ATMIS-6208PI → STI-288GPM 贴 ATMIS 标（OEM 30%）；6216PI → STI-21616GP；6408PI → STI-488GP。已打开的主题（1/9 封有打开记录）：「10G media converter」(2024-08-08) → 读者兴趣偏「10G 汇聚/L3」；与 P1 同类，继续｜需求台账 #1（2026-10-24 改正）：「Stacking is mandatory」的正确答法不是只说没有——AC5 没有，但 CENTEC STH1G（STH-2QX4DX48GP，≤8 台）有；信里两层都说
- **下一步（具体）**：2026-11　Elsa 邮箱 → subhash@andatelecom.com（抄 harish@）　首封前知悉：Elsa 已 1:1 去信 9 轮（2025-05-05→2026-08-04，0 回）（第 74 批(m)）；只问一句（第 75 批(ak) 2026-10-25：信稿复检修正——「ERPS G.8032 rings (<20 ms)」→「ring redundancy」）
  - 第一问（只问一个）：Subhash — on stacking: our Marvell access units do not stack (redundancy there is ERPS G.8032 + 10G uplinks). Where stacking is mandatory we have the CENTEC-based STH-2QX4DX48GP, 48×1G PoE++ + 4×25G + 2×40G, stacking up to 8 units as one logical switch. Is stacking a tender clause in your projects, and at what port count?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2023-12-13 | 备 | Saga 内部印度线索表 List_2023.12.13.xlsx（存于 Fastball/Rishi 文件夹） | 名单行：「96 https://www.andatelecomindia.com/ 印度 外贸邦 MC Switch 周边产品 harish@andatelecom.com ‘91（0）935025 7173 已加」 | Saga 自己的线索表里对本户的一手备注（来源/兴趣点/是否已加 WhatsApp/展会现场对话）——比群发打开率更硬的证据；写下一封邮件时直接引用这里的兴趣点 | `Drive PI 文件夹 2_印度_Rishi` |
| 2025-02-14 | 去 | A/S 群发 | 48 Port PoE Managed Switch、24V poe switch | 9 封 / 1 次打开 / 0 回｜首封 2024-06-19 → 末封 2025-02-14（9 去 / 0 来） | `gmail_digest` |
| 2025-05-05 | out | Elsa → info@andatelecom.com | 90W PoE Managed Switch（Elsa 1:1 逐月名单第 1/9 轮；To 仅本户） | 第 74 批(m) `from:e.sagatelecom to:harish@andatelecom.com` 全程 complete：9 轮直收；0 回 | `elsa_1to1` |
| 2025-06-17 | 来 | Harish Gupta（Director, ANDA Telecom） | Dear Nitin/Subhash Please reply. | 董事把 Elsa 的 16 口信转给采购两人 = 内部有兴趣 | `gmail_e` |
| 2025-06-17 | out | Elsa → info@andatelecom.com | 16 Port Ethernet Switch（Elsa 1:1 逐月名单第 2/9 轮；To 仅本户） | 第 74 批(m) `from:e.sagatelecom to:harish@andatelecom.com` 全程 complete：9 轮直收；0 回 | `elsa_1to1` |
| 2025-10-02 | out | Elsa → info@andatelecom.com | 10G Enterprise SFP Switch（Elsa 1:1 逐月名单第 3/9 轮；To 仅本户；正文价 280usd/pc，第 74 批(p) 读稿 msg 19984c1d62ba38d6 / 19df5ef64e6ba213） | 第 74 批(m) `from:e.sagatelecom to:harish@andatelecom.com` 全程 complete：9 轮直收；0 回 | `elsa_1to1` |
| 2025-12-04 | out | Elsa → info@andatelecom.com | Booster PoE Switch（Elsa 1:1 逐月名单第 4/9 轮；To 仅本户） | 第 74 批(m) `from:e.sagatelecom to:harish@andatelecom.com` 全程 complete：9 轮直收；0 回 | `elsa_1to1` |
| 2025-12-29 | out | Elsa → info@andatelecom.com | Marvell Industrial Alert System（Elsa 1:1 单发；To 仅本户，非 BCC 批次） | 本户在 Elsa 的 1:1 名单里；之后 Elsa 箱 Replied 标签见 2026-08-04 来信 | `elsa_1to1` |
| 2026-03-02 | out | Elsa → harish@andatelecom.com | Updated Ethernet Switches Links（Elsa 1:1 逐月名单第 6/9 轮；To 仅本户） | 第 74 批(m) `from:e.sagatelecom to:harish@andatelecom.com` 全程 complete：9 轮直收；0 回 | `elsa_1to1` |
| 2026-04-03 | out | Elsa → harish@andatelecom.com | 10G Enterprise SFP Switch（Elsa 1:1 逐月名单第 7/9 轮；To 仅本户；正文价 280usd/pc，第 74 批(p) 读稿 msg 19984c1d62ba38d6 / 19df5ef64e6ba213） | 第 74 批(m) `from:e.sagatelecom to:harish@andatelecom.com` 全程 complete：9 轮直收；0 回 | `elsa_1to1` |
| 2026-05-11 | out | Elsa → harish@andatelecom.com | 10G Enterprise SFP Switch（Elsa 2026 年 1:1 名单重发；To 仅本户；正文价 280usd/pc，第 74 批(p) 读稿 msg 19984c1d62ba38d6 / 19df5ef64e6ba213） | 本户在 Elsa 的 1:1 名单里（非 BCC 批次）；之后 Elsa 箱 Replied 标签见 2026-08-04 来信 | `elsa_1to1` |
| 2026-08-04 | 来 | Subhash（ANDA Telecom） | First share us data sheet for the same | 24 口 PoE（AC5）信当天要规格书 | `gmail_e` |
| 2026-08-04 | 来 | Subhash | we will check and update you soon, You have mentioned some Not supported features (no a days Stacking is mandatory) | 卡点 = 堆叠；Elsa 的规格书里明写了不支持项（诚实），对方以堆叠为必需 | `gmail_e` |
| 2026-08-04 | 去 | Elsa | Please check attached datasheet.（附件 = STC-424XGGPM-280W.docx） | Subhash 要的规格书 = 24 口 PoE 管理机 STC-424XGGPM-280W；他看完才说「stacking is mandatory」——比对对象就是这款 | `gmail_e 19fcc40506a0a404` |
| 2026-08-04 | out | Elsa → harish@andatelecom.com | 24 Port PoE Managed Switch（Elsa 1:1 逐月名单第 9/9 轮；To 仅本户；正文价 170usd/pc，第 74 批(p) 读稿 msg 1a05bfb71364077f） | 第 74 批(m) `from:e.sagatelecom to:harish@andatelecom.com` 全程 complete：9 轮直收；0 回 | `elsa_1to1` |
| 2026-10-21 | 用户表 | Simon | 兴趣：对EDFA台式很有兴趣 画了一个应用图;从ONV买 也有其他国内的 也买AOA的 | 表内备注 | `用户表` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：（已核 2026-10-24，第 73 批）Elsa 2026-08-04 规格书 = STC-424XGGPM-280W.docx（连接器读 Elsa 回复正文）

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 9 封（2024-06-19 → 2025-02-14），打开标签 1 次（近 12 个月 0，最后 2024-08-08）；打开过：「10G media converter」×1（2024-08-08）；从未打开：「24V poe switch」、「48 Port PoE Managed Switch」、「PoE managed switch」。
- **报价轨迹**（S/A 去信里「价 + 型号/描述同句」：1:1 0 条 + 个性化群发价 2 条，2024-08-08 → 2024-12-27；「今天」= 价格主表 2026-10-17 汇率、30% 档、不高于 2026-06 列表价；只列每个型号/描述最近一次，最多 8 行）：

  | 日期 | 型号 / 原句 | 当时 | 今天应报 | 变化 | 性质 | 主题 | 消息 key |
  |---|---|---|---|---|---|---|---|
  | 2024-12-27 | 「*Price is very competitive, 300usd/pc*」 | $300 | —（原句无型号） | — | 群发价 | 48 Port PoE Managed Switch | `51626efe54a57586` |
  | 2024-08-08 | 「Price: 65usd/pc, 1*10G SFP+1*100M/1G/2.5G/10G Ethernet, unmanaged, non」 | $65 | —（原句无型号） | — | 群发价 | 10G media converter | `75996942f78a56bc` |

  「个性化群发价」= 同一句价发给 ≥5 家的信（Simon 的手工群发），对方未必读过，但它就是对方邮箱里躺着的「上次报价」。
- **品类覆盖与缺口**：官网兴趣：工业（industrial 9 / automation 1）；我们 1:1 从未报过价、也没成交；打开过的群发主题落在：10G 汇聚；**还没碰过的一类：工业** → 下封信可加一句 STI-288GP（8 口千兆 PoE+ 2 SFP 工业非管理，$62.2 EXW）。
- **规模与贴牌线索（官网快照 2026-10-21）**：社媒：https://www.facebook.com/、https://www.linkedin.com/、https://www.twitter.com/。
- **同国同档参照（IN，30% 档、主推线「工业 PoE 管理型」，共 2 户有动静，列前 3）**：SA-032 sundartechno.com（A，同档：成交 STI-0160GE）；SB-641 apolloinfoways.in（B，同档：回过 3 次（最近 2025-01-06），1:1 报过 1 次）。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-11-08 排灯节 Diwali（11-08 前后一周生意半停）；2026-12-25 圣诞 ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Anda Telecom | 事实（用户表） |
| 国家 | 印度 | 事实（用户表）|
| 网站/域名 | andatelecom.com / andatelecomindia.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 电信/ISP/网络运营 | 推断（据兴趣/备注关键词） |
| 联系人 | Harish Gupta / Director   已有回复! / harish@andatelecom.com / subhash@andatelecom.com | 事实（用户表） |
| 来源（From） | 光博会2024 / 富通天下 | 事实（用户表） |
| 兴趣（Interested in） | 对EDFA台式很有兴趣<br>画了一个应用图 / 从ONV买 也有其他国内的<br>也买AOA的 | 事实（用户表） |
| 用户备注（Remark） | 91935 02 57173 已加<br>91-99686 50294 / 回复里有详细联系方式 | 事实（用户表） |
| 所在清单 | DWDM线索、E已回复 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | ONV | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线（andatelecom.com，快照 2026-10-21）
- **是谁**：印度诺伊达（+91 120）电信级光纤产品公司：自有 **ATMIS-** 系列管理 / 工业接入交换机（ATMIS-6208PI = 2 SFP + 8 PoE 工业、6216PI、6408PI、402G）、PDH / E1 转换、光复用器、MC、VoIP；表内 Director Harish Gupta「已有回复」，对台式 EDFA 很有兴趣（画了应用图），从 ONV 与其他国内厂采购，也买 AOA（光模块）。自有型号 = 贴牌 → OEM 30%。
- **在卖/在用品牌**：ATMIS（自有）, ONV, AOA
- **【官网快照】产品：管理 / 工业接入交换机 ATMIS-6408PI / 402G / 6208PI / 6208S / 6216PI / 6216S、光复用器、PDH、MC、E1；+91 120 410 9590**
  > ACCESS SWITCHES Managed Industrial OPTICAL MULTIPLEXER PDH CONVERTERS Media Converters E1 Converters… models ATMIS-6408PI, ATMIS-402G, ATMIS-6208PI, ATMIS-6216PI
  > 来源：https://andatelecom.com/（抓取 2026-10-21）
- **【用户表】对 EDFA 台式很有兴趣，画了应用图；从 ONV 买，也有其他国内的，也买 AOA 的；Director Harish Gupta 已有回复**
  > 兴趣：对EDFA台式很有兴趣 画了一个应用图;从ONV买 也有其他国内的 也买AOA的
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Harish Gupta（）harish@andatelecom.com +91 93502 57173〔（本地 Clients/ 表格，无公开 URL）〕
- **KP**：Subhash（）subhash@andatelecom.com +91 99686 50294〔（本地 Clients/ 表格，无公开 URL）〕
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（官网快照核对：自有型号 OEM））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Anda Telecom Private Limited |
| 成立 | （待核） |
| 总部/地址 | Noida, Uttar Pradesh, India |
| 其他 | 从 ONV / AOA 等中国厂采购贴牌 |

- **业务线**：电信级光传输（PDH、E1、光复用、EDFA 需求）；ATMIS 工业 / 管理接入交换机（贴牌）；MC / VoIP

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| ATMIS | ATMIS-6208PI | 工业 2 SFP + 8 PoE 管理（推断，ONV 代工） | Saga STI-288GPM（$85.5 @30%） | https://andatelecom.com/access-switches-industrial.php（2026-10-21） |
| ATMIS | ATMIS-6216PI | 工业 16 PoE | Saga STI-21616GP | https://andatelecom.com/access-switches-industrial.php（2026-10-21） |

- **触达通道（公开）**：role: 品牌商（贴牌采购）；region: 印度
- **近况信号**：
  - 整条 ATMIS 工业线 = 中国代工 → Marvell 版可直接替换 ONV
  - Director 已回复过
- **风险/边界**：EDFA 为其兴趣点（Saga 无）；ONV 价格基准低；印度 BIS
- **Saga 对位结论**：P1 STI-288GPM（30% 档）——对位 ATMIS-6208PI → STI-288GPM 贴 ATMIS 标（OEM 30%）；6216PI → STI-21616GP；6408PI → STI-488GP。
- **邮件切入句（英文）**：Harish, we can't help on the EDFA — but for the ATMIS-6208PI / 6216PI class we build the same 2-SFP + 8/16-PoE industrial units on Marvell under your label from small lots; shall I quote those two against your current ONV cost?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://andatelecom.com/　语言：未标　站点地图 URL 数：0
- **标题**：Anda Telecom Private Limited
- **首页栏目**：ANDA TELECOM PRIVATE LIMITED / Anda Telecom Private Limited / Our Clients / Our Popular Products / Sign up for our newsletter / About Us / Useful Links / Contact Details
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：telecom 56、fiber 16、switch 12、industrial 9、media converter 7、poe 6、automation 1、cctv 1、surveillance 1、ftth 1
- **站内型号串**（正则抽取，含非交换机）：ATMIS-6408PI, ATMIS-402G, ATMIS-6208PI, ATMIS-6208S, ATMIS-6216PI, ATMIS-6216S, ATMIS-6408PIV2, ATS-2900-3200, ATS-2900-8020, ATS-2900-2528C, ATS-2900-2528P, ATS-2900-2928E
- **站内公开邮箱**：info@andatelecom.com, info@andatelecomindia.com
- **站内公开电话**：+91 120 4109590, +91 9350345252, +91 9871650366
- **社媒**：https://www.facebook.com/, https://www.linkedin.com/, https://www.twitter.com/
- **已抓子页**：[Access Switches - Industrial](https://andatelecom.com/access-switches-industrial.php)；[Access Switches - Managed](https://andatelecom.com/access-switches-managed.php)；[VOIP Series](https://andatelecom.com/voip.php)；[About Us](https://andatelecom.com/about.php)；[Contact Us](https://andatelecom.com/contact.php)
- 首页正文摘录：Welcome to Anda Telecom Private Limited. Your one stop destination for high-quality Telecom grade and fiber optic products. Home Products ACCESS SWITCHES Managed Industrial OPTICAL MULTIPLEXER PDH CONVERTERS Media Converters E1 Converters Other Interface Converters VOIP Products EXTENDERS Small Form-factor Pluggable SURGE PROTECTION TESTING EQUIPMENTS OTDR POWER METER SPLICING MACHINE TOOLKIT ENCRIPSTION DIVICE RUGGE
- **自动对位建议**：STI-288GP（官网快照对位：工业/自动化词频 10、PoE 6 → DIN 8 PoE+ 2 SFP 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SB-692.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| ONV | 深圳/国内白牌或品牌供应商 | 对方已在买中国货：以 Marvell 芯片 + L2+ 功能 + 交期为差异点做第二货源 |

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 4 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-02-14 | 2025.2.14 | 48口 |  | A |  | E Replied 2026.08.04.xlsx#9 |
| 2025-06-17 | 617 | 16电 |  | E |  | E Replied 2026.08.04.xlsx#9 |
| 2025-10-02 | 102 | dac |  | E |  | E Replied 2026.08.04.xlsx#9 |
| ? | 55 | 28bt |  | E |  | E Replied 2026.08.04.xlsx#9 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：9 封（去 9 / 来 0）　|　**期间**：2024-06-19 → 2025-02-14　|　**最后去信**：2025-02-14
- **对方邮箱**：info@andatelecom.com、info@andatelecomindia.com
- 对方从未回信（全部为我方去信）
- **邮件里报过的价**：2024-12-27 $300；2024-08-08 $65

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 48 Port PoE Managed Switch | 2025-02-14 | 2025-02-14 | 0 | 1 | 1 |
| 48 Port PoE Managed Switch | 2024-12-27 | 2024-12-27 | 0 | 1 | 1 |
| 2.5G Web Managed Switch | 2024-11-14 | 2024-11-14 | 0 | 1 | 1 |
| Power Converter | 2024-10-01 | 2024-10-01 | 0 | 1 | 1 |
| 24V poe switch | 2024-09-05 | 2024-09-05 | 0 | 1 | 1 |
| 10G media converter | 2024-08-08 | 2024-08-08 | 0 | 1 | 1 |
| Industrial fiber switch | 2024-07-16 | 2024-07-16 | 0 | 1 | 1 |
| 24V poe switch | 2024-07-12 | 2024-07-12 | 0 | 1 | 1 |
| PoE managed switch | 2024-06-19 | 2024-06-19 | 0 | 1 | 1 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-26T07:56:19Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-692/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://andatelecom.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 2283 字符；首行：Anda Telecom Private Limited |

- **人工定期看（登录墙，不自动抓）**：Facebook: https://www.facebook.com/；X/Twitter: https://www.twitter.com/；LinkedIn: https://www.linkedin.com/

## 联系方式（已有 · 原值照录）

- 邮箱：`harish@andatelecom.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`harish@andatelecomindia.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`subhash@andatelecom.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`info@andatelecom.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`info@andatelecomindia.com`〔企业邮箱；来源：用户表原值〕
- 电话：`+919350257173`〔WhatsApp 已加；原值见来源表〕
- 电话：`+919968650294`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Harish Gupta / Director   已有回复!
- 联系人（原值）：harish@andatelecom.com / subhash@andatelecom.com
- 网站/域名：andatelecom.com
- 网站/域名：andatelecomindia.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Harish Gupta | — | harish@andatelecom.com / +91 93502 57173 | 调研核实（公开页） | （本地 Clients/ 表格，无公开 URL） |
| Subhash | — | subhash@andatelecom.com / +91 99686 50294 | 调研核实（公开页） | （本地 Clients/ 表格，无公开 URL） |
| harish@andatelecom.com | — | harish@andatelecom.com / harish@andatelecomindia.com / +919350257173 | 用户表原值·WhatsApp 已加 | Clients/ 表 |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:andatelecom.com`, `d:andatelecomindia.com`, `e:harish@andatelecom.com`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| DWDM CENTEC_ELSA  08.10.xlsx#总表:3 | 2 | Anda Telecom<br>https://andatelecom.com/ | 印度 | Harish Gupta<br>Director   已有回复! | 光博会2024 | 对EDFA台式很有兴趣<br>画了一个应用图 | harish@andatelecom.com<br>harish@andatelecomindia.com | 91935 02 57173 已加<br>91-99686 50294 | — |
| E Replied 2026.08.04.xlsx#总表:10 | 9 | https://andatelecom.com/ | 印度 | harish@andatelecom.com<br>subhash@andatelecom.com | 富通天下 | 从ONV买 也有其他国内的<br>也买AOA的 | info@andatelecom.com<br>info@andatelecomindia.com | 回复里有详细联系方式 | 4 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-288GPM | 深挖对位：对位 ATMIS-6208PI → STI-288GPM 贴 ATMIS 标（OEM 30%）；6216PI → STI-21616GP；6408PI → STI-488GP。 | $85.5 USD EXW（30% 档，SmartByte LT-IS3210GP-2GX8T 440 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（电信/ISP/网络运营） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STI-288GPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：WhatsApp 直达
- **W**：南亚：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STI-288GPM 按 30% 档报价，做现供应商的第二货源；对位其在用/在卖的 ONV：涨价、断货或交期拉长时切入
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
| 需求面成立（在卖/在用交换机或 PoE） | ❓ 表内兴趣不含交换机关键词 |
| 决策人识别 | ✅ |
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ✅ ONV |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：ANDA ATMIS series — the stacking point

```text
Hi Subhash,

Following your 4 August note ("no a days Stacking is mandatory") — a straight answer rather than another datasheet (you have the STC-424XGGPM-280W sheet Elsa sent on 4 August):

Our AC5-based units do not offer Catalyst-style hardware stacking (no dedicated stack ports, no single-image chassis). Where stacking is a written requirement, we have the CENTEC-based STH-2QX4DX48GP (48 x 1G PoE++ + 4 x 25G + 2 x 40G) that stacks up to 8 units as one logical switch. On the AC5 access units, what you get instead is ring redundancy and 10G SFP+ uplinks, which is how most of our European integrators build the same redundancy.

So the one question: is stacking a written clause in your tenders, or an operations preference? If it is a clause, the STH-2QX4DX48GP is the unit to discuss (ANDA label possible); if it is a preference, I can map ATMIS-6208PI / 6216PI / 6408PI line by line to our industrial PoE models with your label.

Best regards,
Elsa
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

- 2026-10-27：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 B，分数 33）

---

*建档日期：2026-10-27　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
