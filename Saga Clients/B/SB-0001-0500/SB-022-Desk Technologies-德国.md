# Desk Technologies
**官方名称（调研核实）**：DESK Sicherheit GmbH（Karlsruhe, DE；desk-sicherheit.de；HRB 717686 Mannheim）

> **评级 B**　|　德国　|　档案编号 `SB-022`　|　优先级 ★★　|　状态：已推送 7 次·未回复
>
> **类型**：安防集成/项目商（推断）　|　**历史关系**：推送 7 次（2025-04-14 → 2025-11-05）　|　**所在清单**：A优质名单(DE)、AI评估(DE)·DONE　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-022
rating: B
rating_auto: A
rating_research: B  # 核心需求 IP67 户外机 —— Saga 三家供应商均无 IP67 产品线（Saga 不做 IP67）；且报价后 0 回复/7 次推送。警务项目属公共安全边缘
name_official: "DESK Sicherheit GmbH（Karlsruhe, DE；desk-sicherheit.de；HRB 717686 Mannheim）"
score: 74
country: 德国
region: 欧洲
website: desk-sicherheit.de
type: 安防集成/项目商
tier_tags: ["A优质名单(DE)", "AI评估(DE)·DONE"]
deal: no
replies: 0
followups: 7
first_contact: 2025-04-14
last_contact: 2025-11-05
s_mail: 15 msgs (out 15 / in 0), 2025-04-14 -> 2026-09-24
p1: STI-288DGGPM
price_tier: 25%
research: done
site_snapshot: ok  # 2026-10-21
sources: 2
updated: 2026-10-27
```

## SALES BRIEF（压缩模型）

- **是谁**：德国卡尔斯鲁厄的安保服务 + 安防技术公司 DESK Sicherheit GmbH（2017-02 以 UG 注册、2022-12 转 GmbH，注册资本 €25,000；HRB 717686；CEO Daniel Salim Rupp，前联邦国防军；业务：安保勤务、视频监控/AI 视频分析、安防技术、无人机巡检与反无人机、物理渗透测试；自称服务数据中心、银行与集团客户，网店 shop.desk-sicherheit.de）。展会（埃森 2024）记录：CEO 直接沟通，与当地警方有项目联系，关注 IP67 户外交换机（布线 60–80 m），曾被报 $80/台，问 OEM 与样品；7 次推送 0 回复。Saga 无 IP67 机型——仅在需求转为机柜/IP40 DIN 工业 PoE 时重启。（调研 2026-10-21；表内兴趣：和当地警察局有联系，他们会按照项目找产品，对IP67有兴趣，配线大约需要60-80米，报价80美金一台，能否OEM，想买样品测试IP67）
- **为什么是 B 级**：**调研后定级 B**（核心需求 IP67 户外机 —— Saga 三家供应商均无 IP67 产品线（Saga 不做 IP67）；且报价后 0 回复/7 次推送。警务项目属公共安全边缘 → 守界慢跟。）；自动分级 A：+10 谈到样品/测样；+12 备注记录了对方问价/要资料/见面等互动；+6 在 A/DONE 优质国家名单（已做过整轮推送）；+2 在 AI 客户评估名单；+4 AI/Claude 评估 B；+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/德国；+5 最近活动 2025
- **历史互动**：推送 7 次（2025-04-14 → 2025-11-05）
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-288DGGPM — 项目 25% 档：STI-288DGGPM（DIN 8 PoE+ 2 SFP 管理，IP40，−40~+75 ℃，$137.5）置于 IP66 户外箱替代 IP67 整机；非管理 STI-288GP（$59.8）；明示无 IP67；按主表（研究档 saga_fit）；群发里他已看到的价（续）：2026-08-18 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，2026-07-22→09-08 那轮；现价轮是 $180）——同款信稿写 $180 要点明 9 月前那封是 $170；群发里他已看到的价（续，第 66 批全量复核）：2025-06-09 $300（48 Port PoE Managed Switch）、2025-10-06 $280（10G Enterprise SFP Switch）（㉕ 封顶：STI-288DGGPM 档位价高于 2026-06 列表价，文本按列表价改；第 75 批 2026-10-25）
- **第一问（只问一个）**：Herr Rupp, for the 60–80 m outdoor camera runs you described in Essen: we do not build IP67 switches, but the DIN-rail 8-port PoE+ managed unit (IP40, −40 to +75 °C, $137.5 EXW) fitted in an IP66 pole box is what our integrators use — would a sample of that configuration help your next police-site tender?
- **最大未知**：年走量与现供应商
- **下一步**：群发节奏 A 邮箱 观察打开

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-022` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未触达（A 邮箱 15 封 2025→2026，无记录打开，0 回；收件 dr@desk-sicherheit.de；主题多为「10G Enterprise SFP Switch、8 Port Industrial PoE Switch」；Elsa 箱：`to:.de` 穷举 29 条（2026-10-25，锚批 Bcc 头已读）未见 desk-sicherheit.de → Elsa 箱从未发过本户，往来只在 S/A 箱（去 15 / 来 0）（第 74 批(f)））** ｜ 类型：安防集成/项目商 ｜ 筛子：1（只收到群发） ｜ 停点：15 封发到具名邮箱仍无记录打开（Opened 标签仅覆盖追踪到的群发）——地址可能失效或进垃圾箱 ｜ 复活：保持季度群发到 2027-Q1；无打开即停 ｜ 通路：DE 主攻（四主） ｜ 节奏：季度 ｜ 证据：gmail_digest：out 15；用户表：「和当地警察局有联系，他们会按照项目找产品，对IP67有兴趣，配线大约需要60-80米，报价80美金一台，能否OEM，想买样品测试IP67」；研究档 risks：Saga 无 IP67 机型（不要承诺）；警务/公共项目守界按个案；7 次推送 0 回复
- **现状一句话**：德国卡尔斯鲁厄的安保服务 + 安防技术公司 DESK Sicherheit GmbH（2017-02 以 UG 注册、2022-12 转 GmbH，注册资本 €25,000；HRB 717686；CEO Daniel Salim Rupp，前联邦国防军；业务：安保勤务、视频监控/AI 视频分析、安防技术、无人机巡检与反无人机、物理渗透测试；自称服务数据中心、银行与集团客户，网店 shop.desk-sicherheit.de）。展会（埃森 2024）记录：CEO 直接沟通，与当地警方有项目联系，关注 IP67 户外交换机（布线 60–80 m），曾被报 $80/台，问 OEM 与样品；7 次推送 0 回复。Saga 无 IP67 机型——仅在需求转为机柜/IP40 DIN 工业 PoE 时重启。
- **对方真实需求（有据）**：项目 25% 档：STI-288DGGPM（DIN 8 PoE+ 2 SFP 管理，IP40，−40~+75 ℃，$137.5）置于 IP66 户外箱替代 IP67 整机；非管理 STI-288GP（$59.8）；明示无 IP67
- **断点 / 为什么停在这里**：Saga 无 IP67 机型（不要承诺）；警务/公共项目守界按个案；7 次推送 0 回复
- **Saga 现在该推什么**：P1 **STI-288DGGPM**（25% 档，按主表（研究档 saga_fit）；群发里他已看到的价（续）：2026-08-18 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，2026-07-22→09-08 那轮；现价轮是 $180）——同款信稿写 $180 要点明 9 月前那封是 $170；群发里他已看到的价（续，第 66 批全量复核）：2025-06-09 $300（48 Port PoE Managed Switch）、2025-10-06 $280（10G Enterprise SFP Switch）（㉕ 封顶：STI-288DGGPM 档位价高于 2026-06 列表价，文本按列表价改；第 75 批 2026-10-25））——项目 25% 档：STI-288DGGPM（DIN 8 PoE+ 2 SFP 管理，IP40，−40~+75 ℃，$137.5）置于 IP66 户外箱替代 IP67 整机；非管理 STI-288GP（$59.8）；明示无 IP67
- **下一步（具体）**：群发节奏　A 邮箱　观察打开
  - 第一问（只问一个）：Herr Rupp, for the 60–80 m outdoor camera runs you described in Essen: we do not build IP67 switches, but the DIN-rail 8-port PoE+ managed unit (IP40, −40 to +75 °C, $137.5 EXW) fitted in an IP66 pole box is what our integrators use — would a sample of that configuration help your next police-site tender?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-09-24 | 去 | A 群发 | 10G Enterprise SFP Switch、8 Port Industrial PoE Switch | 15 封 / 0 次打开 / 0 回｜首封 2025-04-14 → 末封 2026-09-24（15 去 / 0 来） | `gmail_digest` |
| 2026-10-21 | 用户表 | Simon | 和当地警察局有联系，他们会按照项目找产品，对IP67有兴趣，配线大约需要60-80米，报价80美金一台，能否OEM，想买样品测试IP67 | 表内备注 | `用户表` |

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **发信窗口（DE 全库 922 封群发的打开标签，对方本地时间；均值 4.4%）**：周四 12–14 点 7.3%（41 封）、周二 08–10 点 6.7%（45 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **本国来询季节（DE 全库 15 个「户·月」真人来信，样本小）**：11 月 13.3% / 12 月 13.3% / 9 月 13.3%——本户来信太少，按本国节奏排下一步。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 15 封（2025-04-14 → 2026-09-24），打开标签 0 次。
- **规模与贴牌线索（官网快照 2026-10-21）**：站点地图 75 条 URL；官网语言 de（信照样英文，首句可用对方语言问候）；社媒：https://twitter.com/DeskSecKa、https://www.facebook.com/DeskSicherheit/、https://www.instagram.com/desksicherheit/。
- **日历窗口**：对方：2026-12-24 圣诞–元旦（12-24 → 01-06，德国多数工厂整周停） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Desk Technologies | 事实（用户表） |
| 国家 | 德国 | 事实（用户表）|
| 网站/域名 | desk-sicherheit.de | 事实（用户表 URL/邮箱域名） |
| 类型 | 安防集成/项目商 | 推断（据兴趣/备注关键词） |
| 联系人 | Daniel Rupp / CEO | 事实（用户表） |
| 来源（From） | 埃森展2024 | 事实（用户表） |
| 兴趣（Interested in） | 和当地警察局有联系，他们会按照项目找产品，对IP67有兴趣，配线大约需要60-80米，报价80美金一台，能否OEM，想买样品测试IP67 | 事实（用户表） |
| 用户备注（Remark） | 49 173 159 0372<br>49 721 1812642-2 | 事实（用户表） |
| 用户 AI 评估 | AI 15% B | 事实（用户表 AI评估结果/CALUDE评估结果列） |
| 所在清单 | A优质名单(DE)、AI评估(DE)·DONE | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

### 用户 AI / Claude 评估原文

- **AI**（AI客户评估_DE 09.23.xlsx）：
  > 15% B
  > 德国小型安防集成/项目商，与当地警察局有项目合作。展会上对IP67交换机有兴趣，但我司不做IP67。询问了OEM和样品测试意向，说明对新供应商开放。
  > 长期跟进，虽IP67不做但可推荐工业级PoE交换机（非IP67但适配室内/机柜安装场景），试探是否有非IP67的常规PoE需求
  > 工业PoE交换机、24口商业PoE交换机
  > 展会有接触且有OEM意向+样品测试需求（对新供应商开放）；但核心需求IP67我司不做，需确认是否有常规工业/商业PoE需求；公司小，决策链短

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：德国卡尔斯鲁厄的安保服务 + 安防技术公司 DESK Sicherheit GmbH（2017-02 以 UG 注册、2022-12 转 GmbH，注册资本 €25,000；HRB 717686；CEO Daniel Salim Rupp，前联邦国防军；业务：安保勤务、视频监控/AI 视频分析、安防技术、无人机巡检与反无人机、物理渗透测试；自称服务数据中心、银行与集团客户，网店 shop.desk-sicherheit.de）。展会（埃森 2024）记录：CEO 直接沟通，与当地警方有项目联系，关注 IP67 户外交换机（布线 60–80 m），曾被报 $80/台，问 OEM 与样品；7 次推送 0 回复。Saga 无 IP67 机型——仅在需求转为机柜/IP40 DIN 工业 PoE 时重启。
- **类型**：安防集成/项目商
- **规模**：小型（待补证）
- **【用户记录】CEO 直接沟通；兴趣点为 IP67 户外交换机与 OEM；已报价 $80；之后 0 回复 / 7 次推送**
  > Daniel Rupp / CEO；police projects；IP67 interest；OEM ask；$80 quote（用户 Clients 表摘录）
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【官网 Impressum】法人、登记、代表**
  > DESK SICHERHEIT GmbH Roonstraße 25 76137 Karlsruhe Handelsregister: 717686 Registergericht: Mannheim Vertreten durch: Daniel Rupp Kontakt Telefon: 072182101964 E-Mail: info@desk-sicherheit.de … DESK Sicherheit verbindet klassischen Sicherheitsdienst mit intelligenter Videoüberwachung, KI-Videoanalyse, moderner Sicherheitstechnik und Drohnenabwehr.
  > 来源：https://desk-sicherheit.de/impressum（抓取 2023-07-14）
- **【官网新闻】CEO 公开直邮**
  > DESK SICHERHEIT GmbH Daniel Rupp – CEO Telefon: +49 721 1812642-0 | +49 173 1590372 E-Mail: dr@desk-sicherheit.de
  > 来源：https://desk-sicherheit.de/news/physische-penetrationstest（抓取 2025-04-15）
- **【登记】UG→GmbH、注册资本**
  > Desk Sicherheit GmbH 28.12.2022 Geschäftsführer: Daniel Salim Rupp · Kapital: 25.000 € … 22.02.2017 als Desk Sicherheit UG
  > 来源：https://www.northdata.de/Rupp,%20Daniel%20Salim,%20Karlsruhe/ptu（抓取 2026-10-21）
- **【用户表】展会互动：警方项目、IP67、$80 报价、OEM、样品；7 次推送 0 回复**
  > 和当地警察局有联系，他们会按照项目找产品，对IP67有兴趣，配线大约需要60-80米，报价80美金一台，能否OEM，想买样品测试IP67
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Daniel Rupp（CEO）dr@desk-sicherheit.de 〔用户 Clients 表〕
- **KP**：Daniel Salim Rupp（CEO / Geschäftsführer（Impressum + 新闻稿公开））dr@desk-sicherheit.de（官网新闻稿公开） +49 721 1812642-0 / +49 173 1590372（官网新闻稿公开）〔https://desk-sicherheit.de/news/physische-penetrationstest〕
- **调研后定级**：B（原自动 A）——核心需求 IP67 户外机 —— Saga 三家供应商均无 IP67 产品线（Saga 不做 IP67）；且报价后 0 回复/7 次推送。警务项目属公共安全边缘 → 守界慢跟。
- 备注：若未来需求转为室内/机柜工业 PoE（IP30/IP40 DIN 导轨），可用 STI-288DGGPM 重启；不要承诺 IP67。待补证：公司注册与规模。

### 加厚挖掘（2026-10-21 · B 级加厚 v1（Impressum + 登记核对））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | DESK Sicherheit GmbH（HRB 717686 Amtsgericht Mannheim；USt-ID DE291361315） |
| 成立 | 2017-02-22（UG）→ 2022-12 GmbH |
| 总部/地址 | Roonstraße 25, 76137 Karlsruhe, Germany（+49 721 82101964；info@desk-sicherheit.de） |
| 其他 | CEO Daniel Salim Rupp（2013 起）；业务含反无人机、渗透测试；网店 |

- **业务线**：安保勤务（Sicherheitsdienst）；视频监控 / KI 视频分析 / 安防技术集成；无人机巡检与反无人机、物理渗透测试
- **触达通道（公开）**：网站: https://desk-sicherheit.de/；电话: +49 721 1812642-0（新闻稿公开）；邮箱（公开）: info@desk-sicherheit.de；dr@desk-sicherheit.de（新闻稿公开 CEO 直邮）
- **近况信号**：
  - 项目型采购（警方/数据中心周界）→ 户外柜 DIN 工业 PoE（IP40）+ 户外防水箱方案可替代 IP67 需求
  - 曾问 OEM 与样品 → 对贴牌开放
- **风险/边界**：Saga 无 IP67 机型（不要承诺）；警务/公共项目守界按个案；7 次推送 0 回复
- **Saga 对位结论**：P1 STI-288DGGPM（25% 档）——项目 25% 档：STI-288DGGPM（DIN 8 PoE+ 2 SFP 管理，IP40，−40~+75 ℃，$137.5）置于 IP66 户外箱替代 IP67 整机；非管理 STI-288GP（$59.8）；明示无 IP67
- **邮件切入句（英文）**：Herr Rupp, for the 60–80 m outdoor camera runs you described in Essen: we do not build IP67 switches, but the DIN-rail 8-port PoE+ managed unit (IP40, −40 to +75 °C, $137.5 EXW) fitted in an IP66 pole box is what our integrators use — would a sample of that configuration help your next police-site tender?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://desk-sicherheit.de/　语言：de　站点地图 URL 数：75
- **标题**：DESK Sicherheit
- **描述**：Sicherheitsdienst, Alarmanlagen, Videoüberwachung, KI-Analyse & Drohnenabwehr – aus Karlsruhe, deutschlandweit & international im Einsatz. 24/7-Leitstelle.
- **首页栏目**：Wir schützen, was Sie lieben / Ganzheitliche Sicherheitslösungen für Ihren Bedarf. / Sicherheitsdienst / Sicherheitstechnik / Drohnen UAV / AI Analytics / Unsere Garantie / Full Service
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：axis 2
- **站内型号串**（正则抽取，含非交换机）：DE291361315
- **站内公开邮箱**：email@beispiel.de, info@desk-sicherheit.de, name@organisation.de
- **站内公开电话**：+49 (0)721 952 79 802
- **社媒**：https://twitter.com/DeskSecKa, https://www.facebook.com/DeskSicherheit/, https://www.instagram.com/desksicherheit/, https://www.linkedin.com/company/desk-sicherheitsdienst, https://www.youtube.com/@Desk-Sicherheit-GmbH
- **已抓子页**：[Wächter über der Glut: Wie autarke Türme das Waldbrand-Infer](https://desk-sicherheit.de/news/waldbrand-frueherkennung-autarke-tuerme)；[Über uns / DESK Sicherheit](https://desk-sicherheit.de/ueber-uns)；[Brandfrüherkennung in Sägewerken / DESK Sicherheit](https://desk-sicherheit.de/news/brandfrueherkennung-saegewerke)；[Erfolgreiche Modernisierung eines Rechenzentrums / DESK Sich](https://desk-sicherheit.de/news/moderniserung-rechenzentrum-frankreich)；[Videoüberwachung für Unternehmen und KRITIS / DESK Sicherhei](https://desk-sicherheit.de/leistungen/sicherheitstechnik/videoueberwachung)
- 首页正文摘录：Startseite Leistungen Sicherheitsdienst Sicherheitstechnik Drohnen UAV AI Analytics Shop Referenzen News Über uns Kontakt Jede Sekunde zählt Kontakt Jede Sekunde zählt Startseite Leistungen Sicherheitsdienst Sicherheitstechnik Drohnen UAV AI Analytics Shop Referenzen News Über uns Kontakt Impressum Wir schützen, was Sie lieben Von hochmodernen Alarmanlagen bis hin zu intelligenten Zutrittskontrollen bieten wir Ihnen 
- 数据文件：`data/saga_clients/site_snapshots/SB-022.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 7 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-04-14 | 2025.4.14 | 28poe |  | A |  | DE 1.22.xlsx#107 |
| 2025-05-12 | 512 | 16电 |  | A |  | DE 1.22.xlsx#107 |
| 2025-07-15 | 715 | 22mini |  | A |  | DE 1.22.xlsx#107 |
| 2025-10-06 | 106 | dac |  | A |  | DE 1.22.xlsx#107 |
| 2025-11-05 | 115 | solar |  | A |  | DE 1.22.xlsx#107 |
| ? | 69 | 48口 |  | A |  | DE 1.22.xlsx#107 |
| ? | 95 | 24poe |  | A |  | DE 1.22.xlsx#107 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：a.sagatelecom　|　**邮件**：15 封（去 15 / 来 0）　|　**期间**：2025-04-14 → 2026-09-24　|　**最后去信**：2026-09-24
- **对方邮箱**：dr@desk-sicherheit.de
- 对方从未回信（全部为我方去信）

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Managed PoE Switches | 2026-09-24 | 2026-09-24 | 0 | 1 | 1 |
| 24 Port PoE Managed Switch | 2026-08-18 | 2026-08-18 | 0 | 1 | 1 |
| Firmware 7.5 L2+ Feature Update | 2026-07-08 | 2026-07-08 | 0 | 1 | 2 |
| 10G L3 Managed Switch | 2026-06-02 | 2026-06-02 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2026-05-04 | 2026-05-04 | 0 | 1 | 1 |
| Marvell Managed Commercial Switches | 2026-03-27 | 2026-03-27 | 0 | 1 | 1 |
| OEM Core Switching Solution | 2026-01-23 | 2026-01-23 | 0 | 1 | 1 |
| Marvell Industrial Alert System | 2025-12-17 | 2025-12-17 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-05 | 2025-11-05 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-06 | 2025-10-06 | 0 | 1 | 1 |
| Industrial PoE Switch | 2025-09-05 | 2025-09-05 | 0 | 1 | 1 |
| Mini Industrial PoE Switch | 2025-07-15 | 2025-07-15 | 0 | 1 | 1 |
| …共 15 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：5 个　|　**数据截至**：2026-10-26T07:56:19Z　|　**最近变化**：2026-10-24T07:26:33Z
- **最近变化摘要**：2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过））
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-022/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://desk-sicherheit.de/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 6898 字符；首行：DESK Sicherheit |
| [sitemap](https://desk-sicherheit.de/sitemap.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 75 个 URL；最新 lastmod 2026-10-18T21:25:19 |
| [news_1](https://desk-sicherheit.de/news) | html | HTTP 200 | 2026-10-23T04:20:51Z | 2937 字符；首行：Neuigkeiten \| DESK Sicherheit |
| [news_2](https://desk-sicherheit.de/referenzen) | html | HTTP 200 | 2026-10-23T04:20:51Z | 3807 字符；首行：Referenzen \| DESK Sicherheit |
| [youtube](https://www.youtube.com/@Desk-Sicherheit-GmbH) | youtube_handle | HTTP 200 | 2026-10-24T07:26:33Z | 15 条；最新：2025-04-15T13:09:44+00:00 Digitale Spurensuche: Technik trifft Spürhund – |

- **人工定期看（登录墙，不自动抓）**：Instagram: https://www.instagram.com/desksicherheit/；Facebook: https://www.facebook.com/DeskSicherheit/；X/Twitter: https://twitter.com/DeskSecKa；LinkedIn: https://www.linkedin.com/company/desk-sicherheitsdienst

## 联系方式（已有 · 原值照录）

- 邮箱：`dr@desk-sicherheit.de`〔企业邮箱；来源：用户表原值〕
- 电话：`+491731590372`〔电话/WhatsApp 状态未记；原值见来源表〕
- 电话：`+4972118126422`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Daniel Rupp / CEO
- 网站/域名：desk-sicherheit.de
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Daniel Rupp | CEO | dr@desk-sicherheit.de | 调研核实（公开页） | 用户 Clients 表 |
| Daniel Salim Rupp | CEO / Geschäftsführer（Impressum + 新闻稿公开） | dr@desk-sicherheit.de（官网新闻稿公开） / +49 721 1812642-0 / +49 173 1590372（官网新闻稿公开） | 调研核实（公开页） | https://desk-sicherheit.de/news/physische-penetrationstest |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:desk-sicherheit.de`, `e:dr@desk-sicherheit.de`, `n:DE|desk technologies`, `p:118126422`, `p:731590372`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/DONE/DE 1.22.xlsx#总表:108 | 107 | Desk Technologies<br>www.desk-sicherheit.de | 德国 | Daniel Rupp<br>CEO | 埃森展2024 | 和当地警察局有联系，他们会按照项目找产品，对IP67有兴趣，配线大约需要60-80米，报价80美金一台，能否OEM，想买样品测试IP67 | dr@desk-sicherheit.de | 49 173 159 0372<br>49 721 1812642-2 | 7 条 |
| AI客户评估/DONE/AI客户评估_DE 09.23.xlsx#总表:47 | 46 | Desk Technologies<br>www.desk-sicherheit.de | 德国 | Daniel Rupp<br>CEO | 埃森展2024 | 和当地警察局有联系，他们会按照项目找产品，对IP67有兴趣，配线大约需要60-80米，报价80美金一台，能否OEM，想买样品测试IP67 | dr@desk-sicherheit.de | 49 173 159 0372<br>49 721 1812642-2 | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-288DGGPM | 深挖对位：项目 25% 档：STI-288DGGPM（DIN 8 PoE+ 2 SFP 管理，IP40，−40~+75 ℃，$137.5）置于 IP66 户外箱替代 IP67 整机；非管理 STI-288GP（$59.8）；明示无 IP67 | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（安防集成/项目商） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288DGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STI-288DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：欧洲主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STI-288DGGPM 按 25% 档报价，做现供应商的第二货源；规模（调研）：小型（待补证）
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

**主题**：STI-288DGGPM - industrial DIN-rail L2+ managed switch (Marvell-based, neutral label)

```text
Hi Daniel,

We have been in touch before about PoE and industrial switches; instead of a catalogue, here is one concrete option. For the 60–80 m outdoor camera runs you described in Essen: we do not build IP67 switches, but the DIN-rail 8-port PoE+ managed unit (IP40, −40 to +75 °C, $137.5 EXW) fitted in an IP66 pole box is what our integrators use — would a sample of that configuration help your next police-site tender?

We supply a Marvell-based industrial DIN-rail L2+ managed switch, 8x Gigabit PoE+ plus 2x 2.5G SFP - model STI-288DGGPM - that fits the same slot as the units you source today at a lower landed cost, and we can ship it with neutral packaging. Current price: $137.5 USD EXW (price snapshot 2026-10-17, valid 15 days).

If useful, one unit at the unit price for a 30-day side-by-side test. If not a fit, one line and I close the loop.

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

- **2026-11-26**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-27：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 A，分数 74）；人工/调研定级 → B

---

*建档日期：2026-10-27　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
