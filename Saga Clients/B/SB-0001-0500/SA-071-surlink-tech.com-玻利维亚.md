# surlink-tech.com
**官方名称（调研核实）**：Sur-Link Technology（圣克鲁斯，玻利维亚）

> **评级 B**　|　玻利维亚　|　档案编号 `SA-071`　|　优先级 ★★　|　状态：有回复·跟进中
>
> **P 池并入（B 档，等级不动）：★ P 池 · 正式入池（资产池，终身跟进 + 每 2 个月巡检）**（批 AB-01 · 2026-10-29 · 下次巡检 2026-12-28）：★ P 池正式（P 核心，A 档并池 · 等级不动）：A 档默认入池（长期跟进）；真回 ✔；命中 2/6（成单/样品 — · 真回 ✔ · WA — · 对位 ✔ 交换机 · 登记 未坐实 · 体量 —）　|　标签：core（核心：成单 / 样品 / PI 或 A 档）、prepay
>
> **类型**：批发分销商（布线/光纤/网络）（推断）　|　**历史关系**：实质回复 1 次；推送 2 次（2025-07-02 → 2025-10-01）　|　**所在清单**：E已回复　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SA-071
rating: B
rating_auto: A
sieve: pool  # 闸 3 AB1 2026-10-29
rating_research: B  # Q-76 LT-01 2026-10-29：A→B 普通跟（核心证据不足：B2 真回/WA/有打开/展会+对位；B6 对位（冷，任何区域））；仍在长期客户群，有
name_official: "Sur-Link Technology（圣克鲁斯，玻利维亚）"
score: 61
country: 玻利维亚
region: 拉美
website: surlink-tech.com
type: 批发分销商（布线/光纤/网络）
tier_tags: ["E已回复"]
deal: no
replies: 1
followups: 2
first_contact: 2025-07-02
last_contact: 2025-10-01
s_mail: 8 msgs (out 8 / in 0), 2024-06-28 -> 2025-01-10
p1: none
price_tier: 20%
research: done
site_snapshot: http_error  # 2026-10-29
sources: 1
updated: 2026-10-29
```

## SALES BRIEF（压缩模型）

- **是谁**：玻利维亚圣克鲁斯的技术产品批发分销商（布线 Cat6/Cat6a、光纤 SM/MM、ADSS 五金、机柜；Corning 玻利维亚分销商），官网列出销售团队邮箱/手机；E 渠道已回复，需求 550 只 90 W 工业 PoE 注入器（2017 年起用阿里国际站）。（调研 2026-10-21；表内兴趣：550个90W 工业PoE injector 2017年使用国际站）
- **为什么是 B 级**：**调研后定级 B**（Q-76 LT-01 2026-10-29：A→B 普通跟（核心证据不足：B2 真回/WA/有打开/展会+对位；B6 对位（冷，任何区域））；仍在长期客户群，有真人往来 / 成单即回 A）；自动分级 A：+22 实质回复 1 次；+18 在「已回复」名单（A/E Replied）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-4 区域 拉美/玻利维亚；+5 最近活动 2025；-3 跟进表最近平台标记 E（已降为群发）
- **历史互动**：实质回复 1 次；推送 2 次（2025-07-02 → 2025-10-01）；最近一次客户回复：2025-07-02：全系列电口信息
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-25）**：HRUI/Realtek 非管理 PoE 全口数（Simon 决定是否开线） — 他要的是 550 只 90W 注入器（非 Saga 品类）+ 南美批发价位 → 只有 HRUI/Realtek 非管理 PoE 线能对位，是否开线 Simon 定；在此之前不主动；—；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-08-22 $65（10G media converter）；群发里他已看到的价（续，第 66 批全量复核）：2024-06-28 $220（48 port managed switch）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-05-11 $280（10G Enterprise SFP Switch = STC-4168XGGCM 双 AC，Elsa 箱 2 轮 2025-10-01→2026-05-11；$280 仍是 Simon 在用的群发价（NYNEX 实付 $265.2）——别写主表 377–408 档）；2026-08-04 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-08-04；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170）
- **第一问（只问一个）**：Are PoE / industrial switches something you still source today, or has that line been dropped?
- **最大未知**：官网当前状态异常（HTTP 错误）——公司是否仍在运营待核
- **下一步**：— — 首封前知悉：Elsa 已 1:1 去信 6 轮（2025-10-01→2026-08-04，客户回过信（2025-07-03）），此前还经锚 Bcc 触达（第 74 批(m)）；不主动；若 Simon 开 Realtek 线则一次对位表

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-25）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SA-071` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-25。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未绑定（Elsa 邮箱 2025-07-02 Eduardo Miranda 要 5/8/16/24 口非管理 PoE（10/100 与千兆）「with your standard brand name and standard carton box」+ 图片 → Elsa 07-03 回复 → 无下文）；Elsa 1:1 去信 6 轮 2025-10-01→2026-08-04（To 仅本户 emiranda@surlink-tech.com；头 msg 19fcd49e5fd77ab5 核对无 Bcc，称呼「Hi, Eduardo」= 个性化逐月 1:1 名单；主题 Booster PoE Switch、Marvell Industrial Alert System、Industrial PoE Switch、24 Port PoE Managed Switch…；客户来过信：Elsa 回 2025-07-03 Re:「16 Port Ethernet Switch」；此前经 锚 businesswise1@hotmail.com 的 Bcc 收到 5 轮（2025-02-12→2025-07-02）→ 回信后被 Elsa 从 Bcc 名单剔出、转入 1:1 名单）（第 74 批(m) `from:e.sagatelecom to:` 全程 complete，直收 7 条）；Elsa 群发 BCC 已触达 2025-07-02「16 Port Ethernet Switch」（稿内无价，第 74 批(p) 已读稿），拉美-2（锚 businesswise1 hotmail；2025-02-12 起月轮，11 轮） 批次 To businesswise1@hotmail.com，0 回（第 74 批 Bcc 头核对 msg 197cbb5832cf968b）** ｜ 类型：玻利维亚圣克鲁斯批发分销（布线/光纤/网络，Gerente Eduardo Miranda）——南美非主攻 ｜ 筛子：0（邮件层无人工回复） ｜ 停点：Elsa 回复后无下文（回复正文未入库）；用户表「550 只 90W 注入器」需求在邮件无痕 ｜ 复活：其再次询价 ｜ 通路：BO 非主攻 ｜ 节奏：不主动 ｜ 证据：邮件：去信 8 封（2024-06-28 → 2025-01-10），来信 0；Opened 标签 0 次；收件人 emiranda@surlink-tech.com；data/gmail_e/bcc_batches_2026.json；批次时间线：同批次（To businesswise1@hotmail.com）本户见于 2025-07-02 名单；2026-09-07 最新一轮名单已不含此地址 → 中途被剔除（退信 / 退订 / 手工）；该批次最早 2025-02-12 起共 11 轮，更早轮次 Bcc 未读
- **现状一句话**：Eduardo 的来信是一张清楚的采购清单：非管理 PoE 全口数、Saga 标准品牌与标准彩盒、要图片——是批发商选品。Elsa 回了，之后无回。
- **对方真实需求（有据）**：非管理 PoE 5/8/16/24 口（商用，标准包装）。
- **断点 / 为什么停在这里**：回复后静默；价格段（南美批发）可能不匹配 Marvell。
- **Saga 现在该推什么**：P1 **HRUI/Realtek 非管理 PoE 全口数（Simon 决定是否开线）**（20% 档，—；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-08-22 $65（10G media converter）；群发里他已看到的价（续，第 66 批全量复核）：2024-06-28 $220（48 port managed switch）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-05-11 $280（10G Enterprise SFP Switch = STC-4168XGGCM 双 AC，Elsa 箱 2 轮 2025-10-01→2026-05-11；$280 仍是 Simon 在用的群发价（NYNEX 实付 $265.2）——别写主表 377–408 档）；2026-08-04 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-08-04；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170））——他要的是 550 只 90W 注入器（非 Saga 品类）+ 南美批发价位 → 只有 HRUI/Realtek 非管理 PoE 线能对位，是否开线 Simon 定；在此之前不主动
- **下一步（具体）**：—　—　首封前知悉：Elsa 已 1:1 去信 6 轮（2025-10-01→2026-08-04，客户回过信（2025-07-03）），此前还经锚 Bcc 触达（第 74 批(m)）；不主动；若 Simon 开 Realtek 线则一次对位表

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-07-02 | 来（Elsa 箱） | Ing. Eduardo Miranda（Gerente） | Switch 10 100 non manageable poe / 10 100 1000 non manageable poe 5 ports 8 ports 16 ports 24 ports Must be with your standart brand name and standart carton box. Need to have pictures | 采购清单 | `E 197cbce0cb34789f` |
| 2025-07-02 | 去 | Elsa 群发（BCC；To businesswise1@hotmail.com，拉美-2（锚 businesswise1 hotmail；2025-02-12 起月轮，11 轮） 批次） | 16 Port Ethernet Switch — （头部未取正文；见 Elsa 箱） | Elsa 箱群发 BCC 触达证据（命中地址 emiranda@surlink-tech.com, surlink-tech.com）；S/A digest 看不到 Elsa 的 BCC，之前据此写的「未发信/未触达」不成立 | `elsa_bcc` |
| 2025-07-03 | 去 | Elsa | Please see attached quotation including 1, prices 2, photos 3, packing info. It is about unit price. If you are doing a bulk purchase, lets discuss the final prices.（附 Quotation.xls，3.7 MB） | Elsa 次日回了整张报价单（5/8/16/24 口非管理 PoE）→ 无下文；报价单数字在附件里，连接器不拉附件 | `gmail_e 197cf9203e1b9d65` |
| 2025-10-01 | out | Elsa → emiranda@surlink-tech.com | 10G Enterprise SFP Switch（Elsa 1:1 逐月名单第 1/6 轮；To 仅本户；正文价 280usd/pc，第 74 批(p) 读稿 msg 19984c1d62ba38d6 / 19df5ef64e6ba213） | 第 74 批(m) `from:e.sagatelecom to:emiranda@surlink-tech.com` 全程 complete：6 轮直收；客户曾来信（见 Re: 行） | `elsa_1to1` |
| 2025-12-03 | out | Elsa → emiranda@surlink-tech.com | Booster PoE Switch（Elsa 1:1 逐月名单第 2/6 轮；To 仅本户） | 第 74 批(m) `from:e.sagatelecom to:emiranda@surlink-tech.com` 全程 complete：6 轮直收；客户曾来信（见 Re: 行） | `elsa_1to1` |
| 2025-12-29 | out | Elsa → emiranda@surlink-tech.com | Marvell Industrial Alert System（Elsa 1:1 单发；To 仅本户，非 BCC 批次） | 本户在 Elsa 的 1:1 名单里；未见回复（Elsa 箱 Replied 标签无） | `elsa_1to1` |
| 2026-04-03 | out | Elsa → emiranda@surlink-tech.com | Industrial PoE Switch（Elsa 1:1 逐月名单第 4/6 轮；To 仅本户） | 第 74 批(m) `from:e.sagatelecom to:emiranda@surlink-tech.com` 全程 complete：6 轮直收；客户曾来信（见 Re: 行） | `elsa_1to1` |
| 2026-05-11 | out | Elsa → emiranda@surlink-tech.com | 10G Enterprise SFP Switch（Elsa 2026 年 1:1 名单重发；To 仅本户；正文价 280usd/pc，第 74 批(p) 读稿 msg 19984c1d62ba38d6 / 19df5ef64e6ba213） | 本户在 Elsa 的 1:1 名单里（非 BCC 批次）；未见回复（Elsa 箱 Replied 标签无） | `elsa_1to1` |
| 2026-08-04 | out | Elsa → emiranda@surlink-tech.com | 24 Port PoE Managed Switch（Elsa 1:1 逐月名单第 6/6 轮；To 仅本户；正文价 170usd/pc，第 74 批(p) 读稿 msg 1a05bfb71364077f） | 第 74 批(m) `from:e.sagatelecom to:emiranda@surlink-tech.com` 全程 complete：6 轮直收；客户曾来信（见 Re: 行） | `elsa_1to1` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：「550 只 90W 注入器」出处未见；（已核 2026-10-24，第 73 批）Elsa 07-03 回 Quotation.xls（单价 + 照片 + 装箱，「批量再谈」）；表内数字仍未入库（附件需 Takeout）

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 8 封（2024-06-28 → 2025-01-10），打开标签 0 次；**最近连续 8 封没打开**（近 180 天发 0 封 0 打开）→ 群发对这户已失效，停两个月，改一句 1:1 或换收件人。
- **报价轨迹**（S/A 去信里「价 + 型号/描述同句」：1:1 0 条 + 个性化群发价 2 条，2024-06-28 → 2024-08-22；「今天」= 价格主表 2026-10-17 汇率、20% 档、不高于 2026-06 列表价；只列每个型号/描述最近一次，最多 8 行）：

  | 日期 | 型号 / 原句 | 当时 | 今天应报 | 变化 | 性质 | 主题 | 消息 key |
  |---|---|---|---|---|---|---|---|
  | 2024-08-22 | 「Price: 65usd/pc, 1×10G SFP+1×100M/1G/2.5G/10G Ethernet, unmanaged, non」 | $65 | —（原句无型号） | — | 群发价 | 10G media converter | `76ecfbf55a0061c3` |
  | 2024-06-28 | 「Price is very competitive, 220usd/pc」 | $220 | —（原句无型号） | — | 群发价 | 48 port managed switch | `316f44fd7347db4e` |

  「个性化群发价」= 同一句价发给 ≥5 家的信（Simon 的手工群发），对方未必读过，但它就是对方邮箱里躺着的「上次报价」。
- **日历窗口**：我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-29 查）：**

- `surlink-tech.com` → 同域名 MX → 托管在 gcomhost.com（MX：_dc-mx.08cd7b53df1b.surlink-tech.com）。主机商附带邮箱（同域名 MX → 托管在 gcomhost.com）：过滤弱、几乎不丢信，但常是老板自己收、没人代读 → 短、直接、一行型号 + 价格 + 一个问题

**假日避让（玻利维亚 · 按下一步「群发 / 待排期 → 未来 30 天」窗口 2026-10-29→2026-11-28）：**

- 法定假日：11-02 All Souls' Day —— 假日前一个工作日下午、当天、长假后第一个上午都别发

**公司底数 · 第 85 批（玻利维亚 · SEPREC（原 Fundempresa）需付费证书；本行为「无登记源」记录（据第 79 批研究档），2026-10-27 查；）：**

- 法定名 / 登记号：Sur-Link Technology Bolivia · — · 状态 **（登记状态不可免费核）** · 成立 — · —
- 行业码 / 经营范围：技术产品批发分销商：Cat5e/6/6A（Corning、Nexans、3M）、光纤 SM/MM、ADSS 五金、最后一公里、BASOR 桥架、Toten 机柜、线槽；**Corning 官方玻利维亚分销商（Carrier and Enterprise）**；官网按产品线列出销售团队（公开）
- 注册地址：Av. Guapay Nro. 2675 esq. Calle 10（Canal Cotoca, entre 2do y 3er anillo）, Santa Cruz de la Sierra（+591 3 312 3371 / 314 5932 / 3 347 7677；手机 77008888）
- 规模档：—
- 账目：—
- 高管：Eduardo Miranda — （官网列为主要联系人；Corning 分销联系人）（研究档）
- 高管：Ivan Ortega — Ventas（销售）（研究档）
- 控制人 / 股东：—
- **这意味着什么：**
  - **本轮无免费官方登记源**（玻利维亚 · SEPREC（原 Fundempresa）需付费证书）：以研究档事实为准，不臆断股东 / 财务；对外口径照常，不提「核查」
  - 无登记 = 无信用公开 → 付款默认 100% 预付 T/T（成单客户除外）；量级按研究档 staff / 网店体量判
- 备注：无免费登记源；下一轮若找到镜像再补。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | surlink-tech.com（取自域名，公司全名待核） | 推断 |
| 国家 | 玻利维亚 | 事实（用户表）|
| 网站/域名 | surlink-tech.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 批发分销商（布线/光纤/网络） | 推断（据兴趣/备注关键词） |
| 联系人 | Eduardo Miranda | 事实（用户表） |
| 来源（From） | RFQ<br>2023.5.26 | 事实（用户表） |
| 兴趣（Interested in） | 550个90W 工业PoE injector<br>2017年使用国际站 | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | E已回复 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：玻利维亚圣克鲁斯的技术产品批发分销商（布线 Cat6/Cat6a、光纤 SM/MM、ADSS 五金、机柜；Corning 玻利维亚分销商），官网列出销售团队邮箱/手机；E 渠道已回复，需求 550 只 90 W 工业 PoE 注入器（2017 年起用阿里国际站）。
- **类型**：批发分销商（布线/光纤/网络）
- **规模**：小型（待补证）
- **在卖/在用品牌**：Corning（分销）, Corning, Nexans, 3M, Toten, BASOR
- **【官网】圣克鲁斯公司，地址/电话与销售联系人（Ivan Ortega、Mauricio Eguez 等）**
  > Sur - Link Technology (Bolivia) Av Guapay Nro. 2675… Telf.: +591-3-312-3371… Sr Ivan Ortega iortega@surlink-tech.com +591-74953834 · Sr Mauricio Eguez ventas05@surlink-tech.com
  > 来源：https://www.surlink-tech.com/（抓取 2026-10-21）
- **【Facebook】技术产品批发分销商：Cat6a/Cat6/Cat5e、光纤、ADSS 五金、机柜**
  > Distribuidor mayorista de tecnologia: Cat6a cat6 cat5e Fibra óptica sm mm Ferreteria adss Racks
  > 来源：https://www.facebook.com/p/SUR-LINK-technology-bolivia-100063766464860/（抓取 2026-10-21）
- **【Corning】Corning 光通信玻利维亚分销商，联系人 emiranda@surlink-tech.com**
  > Guapay # 2675… Santa Cruz de la Sierra, Bolivia… Email: emiranda@surlink-tech.com
  > 来源：https://www.corning.com/optical-communications/cala/en/home/support/distributors/bolivia.html（抓取 2026-10-21）
- **【原厂名录】Corning 官方玻利维亚分销商（Carrier and Enterprise）**
  > Location Title: Sur-Link Technology Bolivia … Business Classification: Carrier and Enterprise Country: Bolivia … Address Line 1: Av. Guapay # 2675 esquina Calle 10 Canal Cotoca entre Segundo y Tercer Anillo … Phone No: +591 3 3477677 … Email: emiranda@surlink-tech.com Website Link: http://www.surlink-tech.com/
  > 来源：https://www.corning.com/optical-communications/cala/en/home/support/distributors/bolivia.html（抓取 2026-10-21）
- **【官网】销售团队与分工（公开）**
  > Ventas Fibra Optica Silvia Salas ADSS y Ferreteria 63486474 Andres Flores ADSS, Ferreteria, Ultima milla 68821306 Ventas Cableado Estructurado Daniel Menacho Rejillas BASOR, Cableado Estructurado, Gabinetes Toten 63338212 … Mauricio Eguez Coming, Nexans, Cat5e Cat6 Cat6a
  > 来源：https://www.surlink-tech.com/contacto.php（抓取 2026-10-21）
- **【官网】负责人联系方式**
  > Sur - Link Technology (Bolivia) Av Guapay Nro. 2675, esq calle 10 … Telf.: +591-3-312-3371, 314-5932 Sr Eduardo Miranda +591-75009995 emiranda@surlink-tech.com
  > 来源：https://surlink-tech.com/ubicacion.php（抓取 2026-10-21）
- **KP**：Eduardo Miranda（（官网列为主要联系人；Corning 分销联系人））emiranda@surlink-tech.com +591 75009995〔官网 + Corning 分销商页〕
- **KP**：Ivan Ortega（Ventas（销售））iortega@surlink-tech.com +591 74953834〔官网〕
- **KP**：Mauricio Eguez（Ventas — Corning / Nexans / Cat5e-6A）ventas05@surlink-tech.com +591 74951389〔https://www.surlink-tech.com/〕
- **KP**：Daniel Menacho（Ventas — 结构化布线 / BASOR 桥架 / Toten 机柜）kmenacho@surlink-tech.com +591 63338212〔http://www.surlink-tech.com/empresa.php〕
- **KP**：Silvia Salas（Ventas Fibra Óptica — ADSS / 五金）ssalas@surlink-tech.com +591 63486474〔https://www.surlink-tech.com/contacto.php〕
- **调研后定级**：B（原自动 A）——Q-76 LT-01 2026-10-29：A→B 普通跟（核心证据不足：B2 真回/WA/有打开/展会+对位；B6 对位（冷，任何区域））；仍在长期客户群，有真人往来 / 成单即回 A
- 备注：LT-T03 官网快照加厚（2026-10-29）：fail#2。
LT-T03 官网快照加厚（2026-10-21）：fail#1。
550 只 90 W 注入器为明确量化需求且已回复；分销商身份可带后续 PoE 交换机。南美非主攻区但无需额外投入。先向 SmartByte 核实是否有 90 W（802.3bt）注入器及价格；若无，用 STC-28DGGPM（bt 版本核对）替代方案报价，分销价阶 20%。

### 加厚挖掘（2026-10-21 · 深挖 v2（官网 + Corning 官方经销名录核对））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Sur-Link Technology Bolivia |
| 总部/地址 | Av. Guapay Nro. 2675 esq. Calle 10（Canal Cotoca, entre 2do y 3er anillo）, Santa Cruz de la Sierra（+591 3 312 3371 / 314 5932 / 3 347 7677；手机 77008888） |
| 其他 | 技术产品批发分销商：Cat5e/6/6A（Corning、Nexans、3M）、光纤 SM/MM、ADSS 五金、最后一公里、BASOR 桥架、Toten 机柜、线槽；**Corning 官方玻利维亚分销商（Carrier and Enterprise）**；官网按产品线列出销售团队（公开） |

- **业务线**：结构化布线 / 光纤 / 机柜 批发；Corning 分销；结构化布线批发（Corning / Nexans / 3M）；光纤 ADSS / 五金 / 最后一公里（ISP 客户）；机柜（Toten）/ 桥架（BASOR）/ 线槽

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| （需求） | 90W 工业 PoE 注入器 ×550 | E 渠道已回复，数量 550 | —（90W bt 注入器需 SmartByte 核型/外采） | （本地 Clients/ 表格，无公开 URL）（用户表） |

- **触达通道（公开）**：网站: https://www.surlink-tech.com/；直邮: emiranda@surlink-tech.com（用户表）；电话: +591 3 347 7677 / 312 3371（官网与 Corning 名录公开）；Facebook: https://www.facebook.com/p/SUR-LINK-technology-bolivia-100063766464860/
- **近况信号**：
  - 550 只 90W 注入器——批量明确；玻利维亚不在主攻区但量大
  - Corning 官方分销 + ADSS/最后一公里团队 → 客户群是 ISP 与布线承包商；550 台 90W PoE 注入器需求应来自 ISP/PTZ 项目，后续可延伸到 bt 级 PoE 交换机（2026-10-21）
- **风险/边界**：90W 工业注入器不在 Saga 标准型谱；玻利维亚物流/付款
- **Saga 对位结论**：P1 待核型（无标准对应）（20% 档）——550 × 90W 工业 PoE 注入器：需 SmartByte 核型或外采配套；可顺带报 STI-288DGGPM 作 PoE 交换方案替代；分销 20% 档
- **邮件切入句（英文）**：For the 550 units of 90W industrial PoE injectors, I am confirming the bt injector part number and MOQ pricing with the factory now; if a switch-based design is acceptable, the 8-port 90W-capable industrial PoE switch can be quoted immediately as an alternative.

### 官网快照（自动摘要 · 抓取 2026-10-29 · 状态：HTTP 错误）

- 尝试域名：surlink-tech.com
  > https://surlink-tech.com/ http 403 ct=text/html; charset=utf-8
  > https://www.surlink-tech.com/ http 403 ct=text/html; charset=utf-8
  > http://surlink-tech.com/ http 403 ct=text/html; charset=utf-8
- **提示**：抓取失败不代表公司不在；人工打开一次即可。
- 数据文件：`data/saga_clients/site_snapshots/SA-071.json`

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 2 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-07-02 | 2025.7.2 | 群发了16电 | 全系列电口信息 | E |  | E Replied 2026.08.04.xlsx#11 |
| 2025-10-01 | 101 | dac |  | E |  | E Replied 2026.08.04.xlsx#11 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：8 封（去 8 / 来 0）　|　**期间**：2024-06-28 → 2025-01-10　|　**最后去信**：2025-01-10
- **对方邮箱**：emiranda@surlink-tech.com
- 对方从未回信（全部为我方去信）
- **邮件里报过的价**：2024-08-22 $65；2024-06-28 $220

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Mini Industrial PoE Switch | 2025-01-10 | 2025-01-10 | 0 | 1 | 1 |
| 8 Port Industrial PoE Switch | 2024-12-19 | 2024-12-19 | 0 | 1 | 1 |
| 8 Port Ethernet Switch | 2024-11-29 | 2024-11-29 | 0 | 1 | 1 |
| Industrial PoE Switch | 2024-11-06 | 2024-11-06 | 0 | 1 | 1 |
| 90W PoE Managed Switch | 2024-09-26 | 2024-09-26 | 0 | 1 | 1 |
| 10G media converter | 2024-08-22 | 2024-08-22 | 0 | 1 | 1 |
| PoE Switch | 2024-07-25 | 2024-07-25 | 0 | 1 | 1 |
| 48 port managed switch | 2024-06-28 | 2024-06-28 | 0 | 1 | 1 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-29T15:11:51Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SA-071/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://surlink-tech.com/) | html | HTTP 403 | 2026-10-23T04:20:51Z | 官网首页（T27 快照状态 http_error） |

## 联系方式（已有 · 原值照录）

- 邮箱：`emiranda@surlink-tech.com`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Eduardo Miranda
- 网站/域名：surlink-tech.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Eduardo Miranda | （官网列为主要联系人；Corning 分销联系人） | emiranda@surlink-tech.com / +591 75009995 | 调研核实（公开页） | 官网 + Corning 分销商页 |
| Ivan Ortega | Ventas（销售） | iortega@surlink-tech.com / +591 74953834 | 调研核实（公开页） | 官网 |
| Mauricio Eguez | Ventas — Corning / Nexans / Cat5e-6A | ventas05@surlink-tech.com / +591 74951389 | 调研核实（公开页） | https://www.surlink-tech.com/ |
| Daniel Menacho | Ventas — 结构化布线 / BASOR 桥架 / Toten 机柜 | kmenacho@surlink-tech.com / +591 63338212 | 调研核实（公开页） | http://www.surlink-tech.com/empresa.php |
| Silvia Salas | Ventas Fibra Óptica — ADSS / 五金 | ssalas@surlink-tech.com / +591 63486474 | 调研核实（公开页） | https://www.surlink-tech.com/contacto.php |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E Replied 2026.08.04.xlsx#总表:12 | 11 | https://surlink-tech.com/ | 玻利维亚 | Eduardo Miranda | RFQ<br>2023.5.26 | 550个90W 工业PoE injector<br>2017年使用国际站 | emiranda@surlink-tech.com |  | 2 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | 待核型（无标准对应，向 SmartByte 核） | 深挖对位：550 × 90W 工业 PoE 注入器：需 SmartByte 核型或外采配套；可顺带报 STI-288DGGPM 作 PoE 交换方案替代；分销 20% 档 | — | 深挖对位；档位 20%（批发分销商（布线/光纤/网络）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $80.7 USD EXW（20% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：20% 档 $139.9 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），20% 档公式为 $181.2——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STC-424DGGPM-280W 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；20% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 1 次实质回复（对方认识我们）
- **W**：拉美：物流/收款/汇率摩擦高于主攻区
- **O**：P1 — 按 20% 档报价，做现供应商的第二货源；规模（调研）：小型（待补证）
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
| 采购量/预算 | ❓ 未确认（有回复但未报量） |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 官网当前状态异常（HTTP 错误）——公司是否仍在运营待核
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Follow-up on your switch requirement (model confirmation in progress)

```text
Hi Eduardo,

Picking up our earlier exchange about PoE / industrial switches. For the 550 units of 90W industrial PoE injectors, I am confirming the bt injector part number and MOQ pricing with the factory now; if a switch-based design is acceptable, the 8-port 90W-capable industrial PoE switch can be quoted immediately as an alternative.

One question: is the port mix fixed by the design, or can we propose an equivalent layout?

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 该需求无 Saga 标准型号对应（见「产品决策」P1 待核型）：此样板只确认需求与核型进度，不报价；核型后再出带型号/价格的版本。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-28**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-29：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 A，分数 61）；人工/调研定级 → B

---

*建档日期：2026-10-29　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
