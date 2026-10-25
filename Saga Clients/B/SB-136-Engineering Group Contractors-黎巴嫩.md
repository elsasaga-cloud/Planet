# Engineering Group Contractors
**官方名称（调研核实）**：Engineering Group Contractors (EGC)（黎巴嫩；表内误归阿联酋）

> **评级 B**　|　黎巴嫩　|　档案编号 `SB-136`　|　优先级 ★★　|　状态：WhatsApp 已加·未回复
>
> **类型**：系统集成/工程商（推断）　|　**历史关系**：WhatsApp 已加；推送 19 次（2024-05-10 → 2025-10-27）　|　**所在清单**：A优质名单(阿联酋 沙特阿拉伯)、AI评估(阿联酋 沙特阿拉伯)·DONE　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-136
rating: B
rating_auto: B
name_official: "Engineering Group Contractors (EGC)（黎巴嫩；表内误归阿联酋）"
score: 50
country: 黎巴嫩
country_table: 阿联酋  # 表内原填；调研纠正为 黎巴嫩（research JSON country_fix）
region: 中东
website: egc-lb.com
type: 系统集成/工程商
tier_tags: ["A优质名单(阿联酋 沙特阿拉伯)", "AI评估(阿联酋 沙特阿拉伯)·DONE"]
deal: no
replies: 0
followups: 19
first_contact: 2024-05-10
last_contact: 2025-10-27
s_mail: 22 msgs (out 22 / in 0), 2024-07-05 -> 2026-09-29
p1: STI-288GPM
price_tier: 25%
research: done
site_snapshot: ok  # 2026-10-21
sources: 2
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：黎巴嫩（+961 3）弱电 / 电气承包商：防雷接地、消防报警（EN54 网络卡）、监控安防、网络设计安装、PABX、智能家居 / BMS、自动门、应急照明；GM Mohammad Hammoud 谈过 30 台交换机环网、VC（视频 / 数据光端机）、2 光 10 电、BNC 转网，「基本都懂」；WA 19 次无实质回复。表内国家为阿联酋，域名 / 电话指向黎巴嫩（country_fix 黎巴嫩）。（调研 2026-10-21；表内兴趣：1,谈了switch,着重问了30个switch环网 2，问了VC，说之前用过，不过用的基本都是视频和数据，其他的功能用的少 3，问了2光10电，基本都懂，问了BNC转网 整体上比较专业）
- **为什么是 B 级**：+12 备注记录了对方问价/要资料/见面等互动；+6 在 A/DONE 优质国家名单（已做过整轮推送）；+2 在 AI 客户评估名单；+15 AI/Claude 评估 A；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+3 区域 中东/阿联酋；+5 最近活动 2025；-16 推送 19 次无任何回复（聋名单）
- **历史互动**：WhatsApp 已加；推送 19 次（2024-05-10 → 2025-10-27）
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-288GPM — 30 节点环网 → 工业管理 ERPS 机 STI-288GPM（$82.2 @25%）；2 光 10 电 ≈ STI-288GPM / 商用 STC-28DGGPM；BNC 转网不供。；按主表（研究档 saga_fit）；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-09-02 $65（10G media converter）；群发里他已看到的价（续）：2026-07-23 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，2026-07-22→09-08 那轮；现价轮是 $180）——同款信稿写 $180 要点明 9 月前那封是 $170；群发里他已看到的价（续，第 66 批全量复核）：2025-05-27 $300（48 Port PoE Managed Switch）、2026-04-28 $280（10G Enterprise SFP Switch）
- **第一问（只问一个）**：Mr. Hammoud, for the 30-switch ring you described — our managed industrial 8-PoE + 2-SFP runs ERPS (<50 ms) and is $82 EXW each at 1 pc; payment T/T in advance via any bank you can use. Is the ring for cameras or a mixed data site?
- **最大未知**：年走量与现供应商
- **下一步**：2027-Q1（换人后） A 邮箱 → 具名 KP 换收件人再发一封（第 75 批(aj) 2026-10-25：英文信稿已写 `draft_en`（2027-Q1 用）；钩子「ERPS <50 ms」不写——只写 ring redundancy，环网用 STI-288DGGPM；2 光 10 电明说无；VC/BNC 不供）（全量审计 2026-10-25 U57：署名对齐渠道邮箱）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-136` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未触达（A/S 邮箱 22 封 2024→2026，无记录打开，0 回；收件 egc@egc-lb.com；主题多为「10G L3 Managed Switch、24 Port PoE Managed Switch」；Elsa 箱：`to:egc-lb.com` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 22 / 来 0）（第 74 批(n)））** ｜ 类型：— ｜ 筛子：1（只收到群发） ｜ 停点：22 封发到具名邮箱仍无记录打开（Opened 标签仅覆盖追踪到的群发）——地址可能失效或进垃圾箱 ｜ 复活：停发群发；若要继续，换具名邮箱 + 只问一句；WhatsApp 已加 → 唤醒走 WhatsApp 一句话，不走邮件 ｜ 通路：黎巴嫩 非主攻 ｜ 节奏：一封 ｜ 证据：gmail_digest：out 22；用户表：「兴趣：1,谈了switch,着重问了30个switch环网 2，问了VC… 3，问了2光10电，基本都懂，问了BNC转网」；研究档 risks：黎巴嫩：外汇 / 银行危机 → 仅 T/T 预付或第三国付款
- **现状一句话**：黎巴嫩（+961 3）弱电 / 电气承包商：防雷接地、消防报警（EN54 网络卡）、监控安防、网络设计安装、PABX、智能家居 / BMS、自动门、应急照明；GM Mohammad Hammoud 谈过 30 台交换机环网、VC（视频 / 数据光端机）、2 光 10 电、BNC 转网，「基本都懂」；WA 19 次无实质回复。表内国家为阿联酋，域名 / 电话指向黎巴嫩（country_fix 黎巴嫩）。
- **对方真实需求（有据）**：30 节点环网 → 工业管理 ERPS 机 STI-288GPM（$82.2 @25%）；2 光 10 电 ≈ STI-288GPM / 商用 STC-28DGGPM；BNC 转网不供。
- **断点 / 为什么停在这里**：黎巴嫩：外汇 / 银行危机 → 仅 T/T 预付或第三国付款
- **Saga 现在该推什么**：P1 **STI-288GPM**（25% 档，按主表（研究档 saga_fit）；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-09-02 $65（10G media converter）；群发里他已看到的价（续）：2026-07-23 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，2026-07-22→09-08 那轮；现价轮是 $180）——同款信稿写 $180 要点明 9 月前那封是 $170；群发里他已看到的价（续，第 66 批全量复核）：2025-05-27 $300（48 Port PoE Managed Switch）、2026-04-28 $280（10G Enterprise SFP Switch））——30 节点环网 → 工业管理 ERPS 机 STI-288GPM（$82.2 @25%）；2 光 10 电 ≈ STI-288GPM / 商用 STC-28DGGPM；BNC 转网不供。
- **下一步（具体）**：2027-Q1（换人后）　A 邮箱 → 具名 KP　换收件人再发一封（第 75 批(aj) 2026-10-25：英文信稿已写 `draft_en`（2027-Q1 用）；钩子「ERPS <50 ms」不写——只写 ring redundancy，环网用 STI-288DGGPM；2 光 10 电明说无；VC/BNC 不供）（全量审计 2026-10-25 U57：署名对齐渠道邮箱）
  - 第一问（只问一个）：Mr. Hammoud, for the 30-switch ring you described — our managed industrial 8-PoE + 2-SFP runs ERPS (<50 ms) and is $82 EXW each at 1 pc; payment T/T in advance via any bank you can use. Is the ring for cameras or a mixed data site?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-09-29 | 去 | A/S 群发 | 10G L3 Managed Switch、24 Port PoE Managed Switch | 22 封 / 0 次打开 / 0 回｜首封 2024-07-05 → 末封 2026-09-29（22 去 / 0 来） | `gmail_digest` |
| 2026-10-21 | 用户表 | Simon | 兴趣：1,谈了switch,着重问了30个switch环网 2，问了VC… 3，问了2光10电，基本都懂，问了BNC转网 | 表内备注 | `用户表` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：用户表状态「WhatsApp 已加·未回复」与三邮箱证据矛盾：S/A 邮箱为「未触达」，Elsa 邮箱全量真人来信（Replied 67 封 + 非 Replied 9 封，第 73 批按邮箱/域名逐户比对）亦无此户 → 这条「回复/已加」发生在邮件之外（WhatsApp/平台私信），证据在 Simon 手机；邮件侧不要据此加码

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Engineering Group Contractors | 事实（用户表） |
| 国家 | 黎巴嫩 | 事实（用户表）|
| 网站/域名 | egc-lb.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 系统集成/工程商 | 推断（据兴趣/备注关键词） |
| 联系人 | Mohammad Hammoud   GM | 事实（用户表） |
| 来源（From） | IFSEC fair 2023 | 事实（用户表） |
| 兴趣（Interested in） | 1,谈了switch,着重问了30个switch环网<br>2，问了VC，说之前用过，不过用的基本都是视频和数据，其他的功能用的少<br>3，问了2光10电，基本都懂，问了BNC转网<br>整体上比较专业 | 事实（用户表） |
| 用户备注（Remark） | 961 3 317173<br>已加 | 事实（用户表） |
| 用户 AI 评估 | AI 40% A | 事实（用户表 AI评估结果/CALUDE评估结果列） |
| 所在清单 | A优质名单(阿联酋 沙特阿拉伯)、AI评估(阿联酋 沙特阿拉伯)·DONE | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

### 用户 AI / Claude 评估原文

- **AI**（AI客户评估_阿联酋 沙特阿拉伯 10.01.xlsx）：
  > 40% A
  > 黎巴嫩/阿联酋中小型工程集成商，GM级别在IFSEC 2023面对面深入交流，询问30台交换机环网方案+VC+2光10电工业交换机，技术水平较专业
  > 发送ERPS环网方案+2光10电工业PoE报价+VC产品线；强调环网技术支持（ERPS）+项目配套能力+批量价格优势
  > ERPS环网交换机、工业PoE交换机（2光10电）、24口PoE交换机
  > GM直接技术交流且问了具体方案（30台环网，技术型客户=我司主场）；项目型需求弱化贸易商身份；专业度高，对BNC转网等都了解；已加WhatsApp

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线（egc-lb.com，快照 2026-10-21）
- **是谁**：黎巴嫩（+961 3）弱电 / 电气承包商：防雷接地、消防报警（EN54 网络卡）、监控安防、网络设计安装、PABX、智能家居 / BMS、自动门、应急照明；GM Mohammad Hammoud 谈过 30 台交换机环网、VC（视频 / 数据光端机）、2 光 10 电、BNC 转网，「基本都懂」；WA 19 次无实质回复。表内国家为阿联酋，域名 / 电话指向黎巴嫩（country_fix 黎巴嫩）。
- **【官网快照】业务：防雷接地、消防报警、监控、网络设计安装、PABX、BMS；EGC Lebanon；型号 KX-TDA100D（松下 PABX）、J-NET-EN54 网络卡**
  > Lightning, protection, safety, Security… EGC Lebanon… NETWORK DESIGN AND INSTALLATION… SURVEILLANCE AND SECURITY SYSTEMS… FIRE ALARM SYSTEMS… KX-TDA100D… J-NET-EN54-SC-003
  > 来源：https://egc-lb.com/（抓取 2026-10-21）
- **【用户表】谈了 switch，着重问 30 个 switch 环网；问 VC（之前用过，基本视频和数据）；问 2 光 10 电、BNC 转网，基本都懂**
  > 兴趣：1,谈了switch,着重问了30个switch环网 2，问了VC… 3，问了2光10电，基本都懂，问了BNC转网
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Mohammad Hammoud（）egc@egc-lb.com +961 3 317 173〔（本地 Clients/ 表格，无公开 URL）〕
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（官网快照核对 + country_fix 黎巴嫩））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Engineering Group Contractors (EGC) |
| 成立 | （待核） |
| 总部/地址 | Lebanon（电话 +961 3） |
| 其他 | 消防 / 防雷 / 弱电多线；表内国家误为阿联酋 |

- **业务线**：消防报警 / 应急照明（守界：消防系统本身不供，网络配套可）；防雷接地；监控 / 网络设计安装 / PABX / BMS
- **触达通道（公开）**：role: 弱电总包 / 集成商；region: 黎巴嫩
- **近况信号**：
  - 具体项目：30 台交换机环网（ERPS 工业管理机）
  - 懂 VC / BNC 转网 → 老旧同轴改造场景（Saga 无 BNC 转网，缺口）
- **风险/边界**：黎巴嫩：外汇 / 银行危机 → 仅 T/T 预付或第三国付款；消防 / 生命安全系统守界（只供网络层）；WA 19 次无回复
- **Saga 对位结论**：P1 STI-288GPM（25% 档）——30 节点环网 → 工业管理 ERPS 机 STI-288GPM（$82.2 @25%）；2 光 10 电 ≈ STI-288GPM / 商用 STC-28DGGPM；BNC 转网不供。
- **邮件切入句（英文）**：Mr. Hammoud, for the 30-switch ring you described — our managed industrial 8-PoE + 2-SFP runs ERPS (<50 ms) and is $82 EXW each at 1 pc; payment T/T in advance via any bank you can use. Is the ring for cameras or a mixed data site?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://egc-lb.com/　语言：en　站点地图 URL 数：0
- **标题**：Home - Engineering Group Contractors (EGC)
- **描述**：Lightning, protection, safety, Security, arrestors, arresters, EGC, EGC Lebanon,Video, Phone, video phone, PABX, Smart Home, Automatic Gates, Automation, Home Automation, BMS, Building Management System, Engineering Group Contractors, Furse, Panasonic, Security Systems, Lebanon, Services, Grounding,
- **首页栏目**：ELECTRONIC REPAIR AND MAINTENANCE / ELECTRICAL REPAIR AND MAINTENANCE / NETWORK DESIGN AND INSTALLATION / SURVEILLANCE AND SECURITY SYSTEMS / LIGHTNING PROTECTION AND GROUNDING / FIRE ALARM SYSTEMS / HOME AUTOMATION / SMATV AND IPTV SYSTEMS
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：surveillance 10、camera 8、cctv 8、fiber 4、cable 3、switch 2、automation 2、nvr 2、fibre 1、wifi 1、distributor 1
- **站内型号串**（正则抽取，含非交换机）：RS422, KX-TDA100D, J-NET-EN54-SC-003, J-NET-EN54-SC-004, J-NET-EN54-SC-004-L, J-NET-EN54-REP, JNR-V4-1, JNR-V4-2, INT-FO-P2P-D, INT-FO-P2P-S, RS422-P2P, AA0001
- **社媒**：https://wa.me/96170, https://www.facebook.com/EGC-558090151231448, https://www.instagram.com/egc/, https://www.linkedin.com/company/11494922, https://www.youtube.com/channel/UCtgjtBRlmZKlsdxCeyvSFPw, https://x.com/EGCLebanon
- **已抓子页**：[Fire Alarm Systems - Interfaces - Network Card - Products - ](https://egc-lb.com/products/fire-alarm-systems/interfaces/network-card)；[Products - Engineering Group Contractors (EGC)](https://egc-lb.com/products)；[Products - Engineering Group Contractors (EGC)](https://egc-lb.com/products/fire-alarm-systems)；[Products - Engineering Group Contractors (EGC)](https://egc-lb.com/products/emergency-lighting)；[Fire Alarm Systems - Modules - Products - Engineering Group ](https://egc-lb.com/products/fire-alarm-systems/modules)；[Fire Alarm Systems - Modules - Products - Engineering Group ](https://egc-lb.com/products/fire-alarm-systems/detectors)
- 首页正文摘录：Products All Fire Alarm Systems All Control Panels All Addressable Conventional Extinguishing Accessories Interfaces All Addressable Conventional Network Card Modules All Addressable Door Release All Addressable Conventional Detectors All Addressable Conventional Beam Detectors Accessories Manual Call Points All Addressable Conventional Audible and Visual All Addressable Conventional Emergency Lighting All Accessorie
- **自动对位建议**：STC-28DGGPM（官网快照对位：交换机词频 2、无 PoE/工业侧重 → 8 口 L2+ 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SB-136.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 19 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2024-05-10 | 2024.5.10 | 发了3层管理448信息 |  | Email |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2024-06-07 | 2024.6.7 | 发了48口引流信息 |  | Email |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2024-07-05 | 2024.7.5 | 2层2光8PoE管理 |  | Email |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2024-08-06 | 2024.8.6 | 工业154 |  | Email |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2024-09-02 | 2024.9.2 | 10G MC |  | Email |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2024-10-10 | 1010 | 24passive |  | Email |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2024-11-06 | 116 | 28bt |  | Email |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2024-12-04 | 124 | 22mini |  | Email |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2024-12-24 | 1224 | 28poe |  | Email |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2025-01-20 | 120 | 4 24 |  | Email |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2025-02-27 | 2025.2.27 | 2 16 |  | A |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2025-04-07 | 4.7 | 芯片 |  | A |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2025-04-28 | 428 | bypass |  | A |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2025-05-27 | 527 | 48口 |  | A |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2025-06-23 | 623 | 16电 |  | A |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2025-07-22 | 722 | 24 48口商业图 |  | Whatsapp |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2025-08-28 | 828 | 4 8 16口poE |  | Whatsapp |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2025-09-24 | 924 | dac |  | Whatsapp |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |
| 2025-10-27 | 1027 | solar |  | Whatsapp |  | 阿联酋 沙特阿拉伯  2.3.xlsx#23 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：22 封（去 22 / 来 0）　|　**期间**：2024-07-05 → 2026-09-29　|　**最后去信**：2026-09-29
- **对方邮箱**：egc@egc-lb.com
- 对方从未回信（全部为我方去信）
- **邮件里报过的价**：2024-09-02 $65

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Managed PoE Switches | 2026-09-29 | 2026-09-29 | 0 | 1 | 1 |
| 24 Port PoE Managed Switch | 2026-08-19 | 2026-08-19 | 0 | 1 | 1 |
| 24 Port PoE Managed Switch | 2026-07-23 | 2026-07-23 | 0 | 1 | 1 |
| 10G L3 Managed Switch | 2026-06-18 | 2026-06-18 | 0 | 1 | 1 |
| 10G L3 Managed Switch | 2026-05-25 | 2026-05-25 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2026-04-28 | 2026-04-28 | 0 | 1 | 1 |
| Industrial PoE Switch | 2026-04-09 | 2026-04-09 | 0 | 1 | 1 |
| Marvell Managed Commercial Switches | 2026-03-23 | 2026-03-23 | 0 | 1 | 1 |
| Marvell Industrial Alert System | 2025-12-31 | 2025-12-31 | 0 | 1 | 1 |
| 16 Port Ethernet Switch | 2025-06-25 | 2025-06-25 | 0 | 1 | 1 |
| 48 Port PoE Managed Switch | 2025-05-27 | 2025-05-27 | 0 | 1 | 1 |
| Managed Optical Bypass Switch | 2025-04-28 | 2025-04-28 | 0 | 1 | 1 |
| …共 22 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：3 个　|　**数据截至**：2026-10-25T07:41:18Z　|　**最近变化**：2026-10-24T07:26:33Z
- **最近变化摘要**：2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过））
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-136/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://egc-lb.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 2783 字符；首行：Home |
| [news_1](https://egc-lb.com/news) | html | HTTP 200 | 2026-10-23T04:20:51Z | 1850 字符；首行：News |
| [youtube](https://www.youtube.com/feeds/videos.xml?channel_id=UCtgjtBRlmZKlsdxCeyvSFPw) | rss | HTTP 200 | 2026-10-24T07:26:33Z | 2 条；最新：2018-03-22T11:59:11+00:00 Furse Your total solution to earthing, lightning & surge  |

- **人工定期看（登录墙，不自动抓）**：Facebook: https://www.facebook.com/EGC-558090151231448；X/Twitter: https://x.com/EGCLebanon；LinkedIn: https://www.linkedin.com/company/11494922；Instagram: https://www.instagram.com/egc/；WhatsApp: https://wa.me/96170

## 联系方式（已有 · 原值照录）

- 邮箱：`egc@egc-lb.com`〔企业邮箱；来源：用户表原值〕
- 电话：`+9613317173`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Mohammad Hammoud   GM
- 网站/域名：egc-lb.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Mohammad Hammoud | — | egc@egc-lb.com / +961 3 317 173 | 调研核实（公开页） | （本地 Clients/ 表格，无公开 URL） |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；邮件已推送 19 次无回复 → 换通道（电话 / LinkedIn / 官网表单），不要再发同模板

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:egc-lb.com`, `e:egc@egc-lb.com`, `n:AE|engineering group contractors`, `p:613317173`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/DONE/阿联酋 沙特阿拉伯  2.3.xlsx#总表:24 | 23 | Engineering Group Contractors<br>https://egc-lb.com/ | 阿联酋 | Mohammad Hammoud   GM | IFSEC fair 2023 | 1,谈了switch,着重问了30个switch环网<br>2，问了VC，说之前用过，不过用的基本都是视频和数据，其他的功能用的少<br>3，问了2光10电，基本都懂，问了BNC转网<br>整体上比较专业 | egc@egc-lb.com | 961 3 317173<br>已加 | 19 条 |
| AI客户评估/DONE/AI客户评估_阿联酋 沙特阿拉伯 10.01.xlsx#总表:21 | 20 | Engineering Group Contractors<br>https://egc-lb.com/ | 阿联酋 | Mohammad Hammoud   GM | IFSEC fair 2023 | 1,谈了switch,着重问了30个switch环网<br>2，问了VC，说之前用过，不过用的基本都是视频和数据，其他的功能用的少<br>3，问了2光10电，基本都懂，问了BNC转网<br>整体上比较专业 | egc@egc-lb.com | 961 3 317173<br>已加 | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-288GPM | 深挖对位：30 节点环网 → 工业管理 ERPS 机 STI-288GPM（$82.2 @25%）；2 光 10 电 ≈ STI-288GPM / 商用 STC-28DGGPM；BNC 转网不供。 | $82.2 USD EXW（25% 档，SmartByte LT-IS3210GP-2GX8T 440 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（系统集成/工程商） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STI-288GPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：WhatsApp 直达
- **W**：已推送 19 次无回复，邮件通道疲劳；中东：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STI-288GPM 按 25% 档报价，做现供应商的第二货源
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
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：The 30-switch ring you described - the right unit, and what we do not carry

```text
Dear Mr. Hammoud,

We talked about a ring of about 30 switches, video-over-fibre, a 2-fibre + 10-copper unit and BNC-to-Ethernet; the mails you had since were general product mails. Here is the specific answer. For the ring: DIN-rail 8 x Gigabit PoE+ + 2 x SFP, L2+ managed with ring redundancy, Marvell-based, -40 to 75 C, CE/RoHS - model STI-288DGGPM - $137.5 USD EXW (MOQ 1, 15-day validity); without ring, L2 managed - STI-288GPM - $82.2. The 2-fibre + 10-copper layout we do not have as a standard model - the nearest is 8 + 2. Video-over-fibre converters and BNC-to-Ethernet we do not carry. Payment T/T in advance through any bank you can use.

One question: is the ring for cameras only, or a mixed data site - that decides whether the PoE version is needed on every node?

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

- **2026-11-24**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 B，分数 50）

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
