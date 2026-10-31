# TECside BV

> **评级 B**　|　比利时　|　档案编号 `SB-263`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：LED/AV 安装商（比利时，2.5G/10G 交换机 RFQ）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：询盘流水　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-263
rating: B
rating_auto: B
score: 48
country: 比利时
region: 欧洲
website: tecside.be
type: LED/AV 安装商（比利时，2.5G/10G 交换机 RFQ）
tier_tags: ["询盘流水"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STC-28DGGPM
price_tier: 25%
research: done
site_snapshot: ok  # 2026-10-21
sources: 1
updated: 2026-10-31
```

## SALES BRIEF（压缩模型）

- **是谁**：比利时 TECside BV（鲁汶：定制 LED 照明、专业视听安装、自动化系统（餐饮、电视、零售、娱乐）；阿里巴巴 RFQ「4 光 8 电 10G 光 2.5G 网」；KP Giovanni Desramault）；表内未跟进。（调研 2026-10-21；表内兴趣：—）
- **为什么是 B 级**：+12 主动询盘（阿里巴巴/自建站/转介）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/比利时；+5 最近活动 2026
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：Realtek 商用线（`data/hrui_STC对照表.csv`）：STC-18XGDGPW 1×10G SFP + 8×2.5G PoE 100W 网管 $66 / STC-108XGDGP 同口型非网管 $63.8 / STC-84XGWE 4×10G SFP + 8×10G mGig 铜 网管非 PoE $204；Marvell 位 STC-28DGGPM（2.5G 只在 SFP） — RFQ 8×2.5G + 4×10G SFP+（该规格在价格主表中待核）→ 先报 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$84.1 @25%）/ 24 GE + 4×10G STC-424XGGM（$132.7）作 AV-over-IP 位｜需求台账 #12：Marvell 主表无 2.5G 铜口（DG = 2.5G 光口），2.5G 铜口在 Realtek 线（STC-18XGDGPW $66 等）——一句话里直接说清，不把 STC-28DGGPM 的 2.5G SFP 当成他要的 2.5G 口｜第 53 批：CENTEC 表最小多千兆铜口 PoE++ 机型是 STH-8DX8XP16DP-HSI（16×2.5G PoE++ + 8×10G mGig PoE++ + 8×25G），没有 8 口小机——他的 8 口需求两条线都没有，直说｜第 55 批：Realtek 线有 2.5G 铜口 PoE（SB-001 2024-08 已卖过 STC-08XGWE $185），他的 8×2.5G 需求在 Realtek 线上有近似机，三层答法（Marvell/Realtek/CENTEC）；按主表（研究档 saga_fit）
- **第一问（只问一个）**：Giovanni, regarding your 8 x 2.5G + 4 x 10G SFP+ requirement for AV installations, a straight answer in three lines: our Marvell line has 2.5G only on the SFP/SFP+ cages (copper access 1G); our commercial Realtek line does have 2.5G copper — 8 x 2.5G PoE + 1 x 10G SFP web-managed at $66 USD EXW, or 8 x 10G multi-gig copper + 4 x 10G SFP+ web-managed (non-PoE) at $204 USD EXW (2026-10 price table, valid 15 days); and multi-gig PoE++ rack units sit on the CENTEC line from 16 ports. IGMP snooping on all, CE/RoHS, neutral brand — which of the two Realtek units is closer to the AV job, or is 4 x 10G SFP+ with PoE mandatory in one box?
- **最大未知**：具体需求型号（表内兴趣列为空）
- **下一步**：待 Simon 排期（首封） A 邮箱 → orders@tecside.be（Giovanni Desramault） 首封：按 email_hook 一问（第 75 批(i) 2026-10-25：英文信稿已写 `draft_en`）（全量审计 2026-10-25 U57：署名对齐渠道邮箱）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-263` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未发信（S/A 邮箱均无往来；来源：用户表「4光8电 10G光 2.5G网 / from: 阿里巴巴RFQ」；Elsa 箱：`to:.be` 穷举 16 条（2026-10-25，锚批 Bcc 头已读）未见 tecside.be → 三箱（S/A/E）均未发（第 74 批(f)））** ｜ 类型：LED/AV 安装商（比利时，2.5G/10G 交换机 RFQ） ｜ 筛子：—（未入筛） ｜ 停点：从未触达 ｜ 复活：首封（具名 KP 优先，用研究档 email_hook） ｜ 通路：比利时（欧洲全域主攻） ｜ 节奏：首封后看打开 ｜ 证据：gmail_digest：out 0；用户表：「4光8电 10G光 2.5G网 / from: 阿里巴巴RFQ」；研究档 risks：RFQ 规格（8×2.5G + 4×10G）在 Saga 价格主表中待核（可能需 SmartByte 型号，注明）；AV 安装商单项目量小；仅 orders@
- **现状一句话**：比利时 TECside BV（鲁汶：定制 LED 照明、专业视听安装、自动化系统（餐饮、电视、零售、娱乐）；阿里巴巴 RFQ「4 光 8 电 10G 光 2.5G 网」；KP Giovanni Desramault）；表内未跟进。
- **对方真实需求（有据）**：RFQ 8×2.5G + 4×10G SFP+（该规格在价格主表中待核）→ 先报 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$84.1 @25%）/ 24 GE + 4×10G STC-424XGGM（$132.7）作 AV-over-IP 位
- **断点 / 为什么停在这里**：RFQ 规格（8×2.5G + 4×10G）在 Saga 价格主表中待核（可能需 SmartByte 型号，注明）；AV 安装商单项目量小；仅 orders@
- **Saga 现在该推什么**：P1 **Realtek 商用线（`data/hrui_STC对照表.csv`）：STC-18XGDGPW 1×10G SFP + 8×2.5G PoE 100W 网管 $66 / STC-108XGDGP 同口型非网管 $63.8 / STC-84XGWE 4×10G SFP + 8×10G mGig 铜 网管非 PoE $204；Marvell 位 STC-28DGGPM（2.5G 只在 SFP）**（25% 档，按主表（研究档 saga_fit））——RFQ 8×2.5G + 4×10G SFP+（该规格在价格主表中待核）→ 先报 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$84.1 @25%）/ 24 GE + 4×10G STC-424XGGM（$132.7）作 AV-over-IP 位｜需求台账 #12：Marvell 主表无 2.5G 铜口（DG = 2.5G 光口），2.5G 铜口在 Realtek 线（STC-18XGDGPW $66 等）——一句话里直接说清，不把 STC-28DGGPM 的 2.5G SFP 当成他要的 2.5G 口｜第 53 批：CENTEC 表最小多千兆铜口 PoE++ 机型是 STH-8DX8XP16DP-HSI（16×2.5G PoE++ + 8×10G mGig PoE++ + 8×25G），没有 8 口小机——他的 8 口需求两条线都没有，直说｜第 55 批：Realtek 线有 2.5G 铜口 PoE（SB-001 2024-08 已卖过 STC-08XGWE $185），他的 8×2.5G 需求在 Realtek 线上有近似机，三层答法（Marvell/Realtek/CENTEC）
  - 做不了 / 要先核的：Simon《STH计划》：铜口 CENTEC 机（STH1G/2.5G/5G，含 Multi-Gig PoE++）暂不宣传、点名才给；主推 10G/25G/XLite/100G/400G/800G
- **下一步（具体）**：待 Simon 排期（首封）　A 邮箱 → orders@tecside.be（Giovanni Desramault）　首封：按 email_hook 一问（第 75 批(i) 2026-10-25：英文信稿已写 `draft_en`）（全量审计 2026-10-25 U57：署名对齐渠道邮箱）
  - 第一问（只问一个）：Giovanni, regarding your 8 x 2.5G + 4 x 10G SFP+ requirement for AV installations, a straight answer in three lines: our Marvell line has 2.5G only on the SFP/SFP+ cages (copper access 1G); our commercial Realtek line does have 2.5G copper — 8 x 2.5G PoE + 1 x 10G SFP web-managed at $66 USD EXW, or 8 x 10G multi-gig copper + 4 x 10G SFP+ web-managed (non-PoE) at $204 USD EXW (2026-10 price table, valid 15 days); and multi-gig PoE++ rack units sit on the CENTEC line from 16 ports. IGMP snooping on all, CE/RoHS, neutral brand — which of the two Realtek units is closer to the AV job, or is 4 x 10G SFP+ with PoE mandatory in one box?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-10-21 | 用户表 | Simon | 4光8电 10G光 2.5G网 / from: 阿里巴巴RFQ | 表内备注 | `用户表` |
| 2026-10-21 | 查 | Agent 官网快照 LT-T03 | LED Verlichting & Audiovisuele Oplossingen België — TECside: Maatwerk LED verlichting, professionele audiovisuele installaties en unieke lichtcreaties voor horeca, TV, retail en entertainment. ✓ Eigen werkplaats in Leuven ✓ België | 官网快照（Actions 抓取）：在线 / 业务线 / 在卖品牌证据（非邮件事实，不计真回） | `` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：无邮件往来

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **规模与贴牌线索（官网快照 2026-10-21）**：站点地图 128 条 URL；官网语言 nl-BE（信照样英文，首句可用对方语言问候）；社媒：https://www.facebook.com/solutiontoyourchallenge/、https://www.instagram.com/tecside_belgium/、https://www.linkedin.com/company/35625353。
- **日历窗口**：对方：2026-12-24 圣诞–元旦 ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-29 查）：**

- `tecside.be` → Zoho Mail（MX：mx.zoho.eu、mx2.zoho.eu、mx3.zoho.eu）。中小企业云邮箱（Zoho Mail）：过滤中等、像素一般可用；这类公司邮箱通常老板或销售本人收，信要短、带型号和一口价

**假日避让（比利时 · 按下一步「群发 / 待排期 → 未来 30 天」窗口 2026-10-31→2026-11-30）：**

- 法定假日：11-01 All Saints' Day；11-11 Armistice Day —— 假日前一个工作日下午、当天、长假后第一个上午都别发

**公司底数 · 第 111 批（BE · 1 次检索：companyweb.be（Tecside BV；BE 0795.233.912；Kolonel Begaultlaan 11 3012 Leuven；Established 22-12-2022；Last balance 2024；Micro 2,2 FTE；Specialised services in sound, image and lighting）+ pappers.be（TECside 0567.983.696 Gewone commanditaire vennootschap；Hoegaardsestraat 122；oprichting 20/11/2014；gesloten 30/06/2023）+ tecsideshop.be/contact（Giovanni Desramault founder - sales giovanni@tecside.be；Bert Hellemans installatie technieker）+ tecside.be（maatwerk LED；AV；DMX / DALI / KNX）；2026-10-28，2026-10-28 查；https://www.companyweb.be/en/0795233912/tecside）：**

- 法定名 / 登记号：Tecside BV（tecside.be / tecsideshop.be；Kolonel Begaultlaan 11, 3012 Leuven；ondernemingsnummer BE 0795.233.912）— 2022-12-22 设立（前身 TECside Comm.V 0567.983.696，2014-11-20 起，2023-06-30 关闭）的定制 LED 照明 + 专业视听安装商（餐饮 / 电视演播 / 零售 / 健身；DMX / DALI / KNX；自有 CNC 车间；LED 灯带按自家规格代工）；微型 2.2 FTE（2024 年报）；创始人 / 销售 Giovanni Desramault（giovanni@tecside.be；= 研究档 KP，orders@）；安装技师 Bert Hellemans；阿里巴巴 RFQ「4 光 8 电 10G 光 2.5G 网」；未发过信 · BE 0795.233.912 · 状态 **Actief** · 成立 2022-12-22（前身 2014-11-20） · BV
- 行业码 / 经营范围：定制 LED 照明 + 视听安装（鲁汶）
- 注册地址：Kolonel Begaultlaan 11, 3012 Leuven
- 规模档：微型（2.2 FTE）
- 账目：2024 年报已交（微型 2.2 FTE）；—
- 高管：Giovanni Desramault — founder / sales（tecsideshop.be）= 拍板人 / 收件人（giovanni@tecside.be 优于 orders@）
- 高管：Bert Hellemans — 安装技师
- 控制人 / 股东：Giovanni Desramault（推定）
- 曾用名：TECside Comm.V（0567.983.696，2014–2023）
- **这意味着什么：**
  - **微型 AV 安装商但有具体 RFQ（8× 2.5G + 4× 10G SFP+）→ 集成 25% small，一页纸一次（切口：直接回应 RFQ 规格——若主表有 2.5G 多千兆型号则报之，否则报 STC-2224GP / STC-4424GCPM + 10G 上联说明 + MOQ 1；荷语引子，Giovanni 直呼）；回信 → 加厚**
  - 发信前核主表 2.5G 型号是否存在（无则不许编）；发信窗口 Thu 12–14 CET
- 备注：集成 25% small；一页纸一次（回 RFQ）；坐实（企业号 + 成立日 + 创始人）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | TECside BV | 事实（用户表） |
| 国家 | 比利时 | 事实（用户表）|
| 网站/域名 | tecside.be | 事实（用户表 URL/邮箱域名） |
| 类型 | LED/AV 安装商（比利时，2.5G/10G 交换机 RFQ） | 推断（据兴趣/备注关键词） |
| 联系人 | Giovanni Desramault | 事实（用户表） |
| 来源（From） | 2026.9.28 | 事实（用户表） |
| 兴趣（Interested in） | — | 事实（用户表） |
| 用户备注（Remark） | 4光8电 10G光 2.5G网 / from: 阿里巴巴RFQ | 事实（用户表） |
| 所在清单 | 询盘流水 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线（tecside.be，快照 2026-10-21）
- **是谁**：比利时 TECside BV（鲁汶：定制 LED 照明、专业视听安装、自动化系统（餐饮、电视、零售、娱乐）；阿里巴巴 RFQ「4 光 8 电 10G 光 2.5G 网」；KP Giovanni Desramault）；表内未跟进。
- **类型**：LED/AV 安装商（比利时，2.5G/10G 交换机 RFQ）
- **【官网快照】官网标题：LED Verlichting & Audiovisuele Oplossingen België**
  > TECside: Maatwerk LED verlichting, professionele audiovisuele installaties en unieke lichtcreaties voor horeca, TV, retail en entertainment. ✓ Eigen werkplaats in Leuven ✓ België
  > 来源：https://tecside.be/（抓取 2026-10-21）
- **【用户表】表内兴趣/备注**
  > 4光8电 10G光 2.5G网 / from: 阿里巴巴RFQ
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【官网快照】TECside 定位**
  > LED Verlichting & Audiovisuele Oplossingen België ; Maatwerk LED verlichting, professionele audiovisuele installaties ; Eigen werkplaats in Leuven
  > 来源：https://tecside.be/（抓取 2026-10-21）
- **【用户表】4 光 8 电 10G 2.5G RFQ**
  > 4光8电 10G光 2.5G网 / from: 阿里巴巴RFQ
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Giovanni Desramault（founder / sales（tecsideshop.be；giovanni@tecside.be 优于 orders@）= 拍板人 / 收件人（第 111 批 官方登记核实 2026-10-28））orders@tecside.be 〔用户表〕
- 备注：LT-T03 官网快照加厚（2026-10-21）：site_contacts/deep/facts。
（无首轮调研；由 deepen.py 建档） ｜ 规则加厚 2026-10-21（autodeep.py；T 档 T4）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（人工复核：官网快照逐家核对 + 表内；T4/T5 信号优先） + 官网快照（LT-T03 2026-10-21））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Tecside BV（BE 0795.233.912；Kolonel Begaultlaan 11, 3012 Leuven；前身 TECside Comm.V 0567.983.696 2014–2023） |
| 成立 | 2022-12-22（前身 2014-11-20）（第 111 批 官方登记核实 2026-10-28） |
| 总部/地址 | 比利时 |
| 其他 | 官网 tecside.be，语言 nl-BE，快照状态 ok；角色判定来源：官网文案；第 111 批：定制 LED 照明 + 视听安装微型公司（2.2 FTE；阿里 RFQ 8× 2.5G + 4× 10G SFP+）→ **集成 25% small，一页纸一次（直接回应 RFQ：主表若有 2.5G 多千兆型号则报之，否则 STC-2224GP / STC-4424GCPM + 10G 上联说明 + MOQ 1；荷语引子）；回信 → 加厚**；发信前核主表 2.5G 型号（第 111 批 官方登记核实 2026-10-28） |

- **业务线**：LED 照明 / 视听安装 / 自动化（比利时）
- **触达通道（公开）**：role: LED/AV 安装商（比利时，2.5G/10G 交换机 RFQ）；region: 比利时；contact: orders@tecside.be
- **近况信号**：
  - 官网：TECside: Maatwerk LED verlichting, professionele audiovisuele installaties en unieke lichtcreaties voor horeca, TV, retail en entertainment ; Eigen werkplaats in Leuven
  - 表内：4 光 8 电 10G 光 2.5G 网 / from: 阿里巴巴 RFQ；KP Giovanni Desramault
- **风险/边界**：RFQ 规格（8×2.5G + 4×10G）在 Saga 价格主表中待核（可能需 SmartByte 型号，注明）；AV 安装商单项目量小；仅 orders@
- **Saga 对位结论**：P1 STC-28DGGPM（25% 档）——RFQ 8×2.5G + 4×10G SFP+（该规格在价格主表中待核）→ 先报 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$84.1 @25%）/ 24 GE + 4×10G STC-424XGGM（$132.7）作 AV-over-IP 位
- **邮件切入句（英文）**：Giovanni, regarding your 8 × 2.5G + 4 × 10G SFP+ switch requirement for AV installations: we supply Marvell-based L2+ switches (8-GE/PoE + 2 SFP; 24-GE + 4 × 10G SFP+) with IGMP for AV-over-IP from single units, CE/RoHS, EXW USD — how many units and is PoE needed on the 2.5G ports?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://tecside.be/　语言：nl-BE　站点地图 URL 数：128
- **标题**：LED Verlichting & Audiovisuele Oplossingen België
- **描述**：TECside: Maatwerk LED verlichting, professionele audiovisuele installaties en unieke lichtcreaties voor horeca, TV, retail en entertainment. ✓ Eigen werkplaats in Leuven ✓ België
- **首页栏目**：Creatieve Verlichting en Audiovisuele Oplossingen / Ontdek onze unieke verlichtings- en audiovisuele oplossingen. / Maatwerk verlichting / Audiovisuele Oplossingen / Automatisatie systemen / Creatieve Lichtsignalisatie / Zij vertrouwen ons al / Waarvoor staan wij?
- **站内公开邮箱**：solution@tecside.be
- **站内公开电话**：+32 (0)16 79 15 20, +32 16 79 15 20
- **社媒**：https://www.facebook.com/solutiontoyourchallenge/, https://www.instagram.com/tecside_belgium/, https://www.linkedin.com/company/35625353, https://www.youtube.com/@tecside_lighting9653
- **已抓子页**：[Winkelverlichting België / Energie zuinige LED verlichting /](https://tecside.be/branches/winkelverlichting)；[Contact TECside / LED Verlichting op maat Leuven](https://tecside.be/contact)
- 首页正文摘录：Onze diensten Maatwerk verlichting Unieke licht creaties, maatwerk en off-the-shelf oplossingen Licht en geluid met impact High end audiovisuele oplossingen om uw klanten in de juiste sfeer te brengen Automatisatie Betrouwbare, gebruiksvriendelijke en schaalbare besturingssystemen Signage Toonaangevende licht creaties om uw merk tot leven te brengen Sectoren TV en studio Impactvolle licht oplossingen voor studio's Ho
- 数据文件：`data/saga_clients/site_snapshots/SB-263.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## B 分层（B-PASS-01 · 2026-10-31）：**B2**

- 依据：OK，待首触反馈；身份 登记坐实 · 路径 活 · 回信 none · 区域档 focus
- 节奏：B1 重点普通跟 = 分组群发每 6 周 + 一年两次点名；B2 普通跟 = 分组群发每 8 周；C 储备 = 不发、两月巡检，有动静捞回。

## 商业情报·挖底（A 类 · 截至 2026-10-30 · 1 条）

> 规则（Simon 2026-10-30）：A 类挖个底掉——年报 / 领英 / KP / 人事变动 / 展会 / 论坛 / GitHub …能挂上的都进仓库；一轮一轮补。未得也记，免得重复查。

**登记**

- 2026-10-30：BE · 1 次检索：companyweb.be（Tecside BV；BE 0795.233.912；Kolonel ：Tecside BV（tecside.be / tecsideshop.be；Kolonel Begaultlaan 11, 3012 Leuven；ondernemingsnum · BE 0795.233.912 · Actief · 成立 2022-12-22 · Kolonel Begaultlaan 11, 3012 Leuven — <https://www.companyweb.be/en/0795233912/tecside>　*登记库镜像（公司底数 2026-10-27 批次）*

待挖：年报/财务、领英公司页、KP、人事变动、展会/活动、新闻/招标、GitHub/技术足迹（下一轮）

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：5 个　|　**数据截至**：2026-10-29T15:11:51Z　|　**最近变化**：2026-10-29T15:11:51Z
- **最近变化摘要**：2026-10-29 sitemap：新增 112 条：2026-10-26 radio1-2022-studio-vrt；2026-10-26 villa-sporza；2026-10-26 villa-sporza
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-263/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://tecside.be/) | html | HTTP 200 | 2026-10-26T07:56:19Z | 5332 字符；首行：LED-verlichting & audiovisuele oplossingen \| TECside |
| [sitemap](https://tecside.be/sitemap.xml) | sitemap | HTTP 200 | 2026-10-29T15:11:51Z | 192 个 URL；最新 lastmod 2026-10-26 |
| [news_1](https://tecside.be/blog-2) | html | HTTP 200 | 2026-10-26T07:56:19Z | 1788 字符；首行：Blog: tips over LED-verlichting en AV \| TECside |
| [news_2](https://tecside.be/onze-projecten) | html | HTTP 200 | 2026-10-26T07:56:19Z | 3454 字符；首行：Projecten: LED-verlichting en AV in de praktijk \| TECside |
| [youtube](https://www.youtube.com/@tecside_lighting9653) | youtube_handle | HTTP 200 | 2026-10-24T07:26:33Z | 9 条；最新：2025-09-02T10:48:04+00:00 Dynamic lightning x Spinning room Olympia hasselt |

- **人工定期看（登录墙，不自动抓）**：Facebook: https://www.facebook.com/solutiontoyourchallenge/；Instagram: https://www.instagram.com/tecside_belgium/；LinkedIn: https://www.linkedin.com/company/35625353

## 联系方式（已有 · 原值照录）

- 邮箱：`orders@tecside.be`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Giovanni Desramault
- 网站/域名：tecside.be
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Giovanni Desramault | founder / sales（tecsideshop.be；giovanni@tecside.be 优于 orders@）= 拍板人 / 收件人（第 111 批 官方登记核实 2026-10-28） | orders@tecside.be | 调研核实（公开页） | 用户表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 询盘统计表.xlsx#Sheet1:342 |  | TECside BV | 比利时 | Giovanni Desramault | 2026.9.28 |  | orders@tecside.be 2024年使用国际站 | 4光8电 10G光 2.5G网 from: 阿里巴巴RFQ | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：RFQ 8×2.5G + 4×10G SFP+（该规格在价格主表中待核）→ 先报 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$84.1 @25%）/ 24 GE + 4×10G STC-424XGGM（$132.7）作 AV-over-IP 位 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（LED/AV 安装商（比利时，2.5G/10G 交换机 RFQ）） |
| 备选2 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-28DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：欧洲主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STC-28DGGPM 按 25% 档报价，做现供应商的第二货源
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

- [ ] 具体需求型号（表内兴趣列为空）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Your Alibaba request for 8 x 2.5G + 4 x 10G SFP+ - what we have and what we do not

```text
Hi Giovanni,

You asked on Alibaba for a switch with 8 x 2.5G copper + 4 x 10G SFP+ and did not get a proper answer from us - apologies, here it is.

Straight answer: an 8 x 2.5G copper unit is not in our range. What we build for AV-over-IP installations, with IGMP snooping and QoS, Marvell-based, CE/RoHS, from single units: 24 x Gigabit + 4 x 10G SFP+ uplinks, L2+ managed - model STC-424XGGM - $132.7 USD EXW (MOQ 1, 15-day validity); 8 x Gigabit PoE+ + 2 x SFP, L2+ - STC-28DGGPM - $84.1.

One question: is the 2.5G on the copper ports a hard requirement for your endpoints, or would gigabit access with 10G uplinks do the job?

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

- **2026-11-30**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-31：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 48）

---

*建档日期：2026-10-31　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
