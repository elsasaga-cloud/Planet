# ivolta.pl

> **评级 B**　|　波兰　|　档案编号 `SB-1208`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：安防网店（波兰，Utepo 在售）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：群发(筛选后质量一般的_群发)、表:PL　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-1208
rating: B
rating_auto: B
score: 25
country: 波兰
region: 欧洲
website: ivolta.pl
type: 安防网店（波兰，Utepo 在售）
tier_tags: ["群发(筛选后质量一般的_群发)", "表:PL"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STC-28DGGPM
price_tier: 20%
research: done
site_snapshot: ok  # 2026-10-21
sources: 1
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：波兰 iVolta.pl（报警与 CCTV 网店：SATEL、Hikvision、Uniview、Dahua、Ajax、Bosch；表内「PoE 交换机，很多摄像头，很多牌子的产品，有 Utepo 的」「质量一般」）；表内未跟进。（调研 2026-10-21；表内兴趣：PoE交换机  很多摄像头 很多牌子的产品 有utepo的）
- **为什么是 B 级**：-6 群发批次名单；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/波兰
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-25）**：STC-28DGGPM — 现售 Utepo PoE → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$80.7 @20%）；非管理 8/16 PoE 位 HRUI STC-028GP / STC-2216GPM（列表价，注明）；首触锚价 STC-28DGGPM $80.7 EXW（主表档位（PDF 上限 $99）；第 72 批 2026-10-24）；按主表（研究档 saga_fit）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-09-01 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-09-01；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170）
- **第一问（只问一个）**：Alongside the Utepo PoE switches in your shop, we supply neutral-brand Marvell-based 8-PoE + 2 SFP L2+ and budget 8/16-port PoE units for camera kits from small lots, CE/RoHS, EXW USD — which port count do your installer customers buy most? Reference: STC-28DGGPM at $80.7 USD EXW (MOQ 1, 15-day validity).
- **最大未知**：年走量与现供应商
- **下一步**：待 Simon 排期（首封） A 邮箱 → kontakt@ivolta.pl（无具名 KP；公用地址） 首封前知悉：Elsa 已 BCC 群发触达（最近 2026-09-01「24 Port PoE Managed Switch」，$170），开头按 ㉝ 写「我们发过几封 X 主题的信、你没有理由回」，别当完全陌生；同款 24-PoE 要报 $180 就先说 8–9 月那封是 $170、汇率 7.2→6.7。 首封：按 email_hook 一问（第 75 批(d) 2026-10-25：英文信稿已写 `draft_en`）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-25）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-1208` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-25。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：Elsa 群发 BCC 已触达 2026-09-01「24 Port PoE Managed Switch」，正文「Price: 170USD/PC」，PL-2 批次 To j.zaczek@mbs-systems.pl，0 回（第 73 批(o) Bcc 头核对 msg 1a05caee1683faef）；S/A 箱：S/A 邮箱均无往来；来源：用户表「PoE交换机 很多摄像头 很多牌子的产品 有utepo的」** ｜ 类型：安防网店（波兰，Utepo 在售） ｜ 筛子：—（未入筛） ｜ 停点：Elsa 群发 BCC 触达过（最近 2026-09-01）无回；S/A 箱从未单独发过 ｜ 复活：首封（具名 KP 优先，用研究档 email_hook） ｜ 通路：PL 次级重点 ｜ 节奏：首封后看打开 ｜ 证据：gmail_digest：out 0；用户表：「PoE交换机 很多摄像头 很多牌子的产品 有utepo的」；研究档 risks：网店/多品牌（Hikvision 自带 PoE）；现售 Utepo 价格基准低；表内「质量一般」；仅 kontakt@，未跟进过；data/gmail_e/bcc_batches_2026.json；批次时间线：同批次（To j.zaczek@mbs-systems.pl）2025-04-03→2026-09-01 共 11 轮群发（L3 Managed Switch、Industrial PoE Switch、Commercial Network Switch、16 Port Ethernet Switch、8 Port Industrial PoE Switch、Mini Industrial PoE Switch、10G Enterprise SFP Switch、OEM Core Switching Solution、Updated Ethernet Switches Links、24 Port PoE Managed Switch），本户在首尾两轮 Bcc 名单内，名单稳定、中间轮次按同名单推断
- **现状一句话**：波兰 iVolta.pl（报警与 CCTV 网店：SATEL、Hikvision、Uniview、Dahua、Ajax、Bosch；表内「PoE 交换机，很多摄像头，很多牌子的产品，有 Utepo 的」「质量一般」）；表内未跟进。
- **对方真实需求（有据）**：现售 Utepo PoE → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$80.7 @20%）；非管理 8/16 PoE 位 HRUI STC-028GP / STC-2216GPM（列表价，注明）
- **断点 / 为什么停在这里**：网店/多品牌（Hikvision 自带 PoE）；现售 Utepo 价格基准低；表内「质量一般」；仅 kontakt@，未跟进过
- **Saga 现在该推什么**：P1 **STC-28DGGPM**（20% 档，首触锚价 STC-28DGGPM $80.7 EXW（主表档位（PDF 上限 $99）；第 72 批 2026-10-24）；按主表（研究档 saga_fit）；Elsa 箱群发里他已看到的价（第 74 批(p) 逐稿读正文，稿价全程不变）：2026-09-01 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，Elsa 箱 1 轮 2026-09-01；现价轮 $180——同款写 $180 先说 8–9 月那封是 $170））——现售 Utepo PoE → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$80.7 @20%）；非管理 8/16 PoE 位 HRUI STC-028GP / STC-2216GPM（列表价，注明）
- **下一步（具体）**：待 Simon 排期（首封）　A 邮箱 → kontakt@ivolta.pl（无具名 KP；公用地址）　首封前知悉：Elsa 已 BCC 群发触达（最近 2026-09-01「24 Port PoE Managed Switch」，$170），开头按 ㉝ 写「我们发过几封 X 主题的信、你没有理由回」，别当完全陌生；同款 24-PoE 要报 $180 就先说 8–9 月那封是 $170、汇率 7.2→6.7。 首封：按 email_hook 一问（第 75 批(d) 2026-10-25：英文信稿已写 `draft_en`）
  - 第一问（只问一个）：Alongside the Utepo PoE switches in your shop, we supply neutral-brand Marvell-based 8-PoE + 2 SFP L2+ and budget 8/16-port PoE units for camera kits from small lots, CE/RoHS, EXW USD — which port count do your installer customers buy most? Reference: STC-28DGGPM at $80.7 USD EXW (MOQ 1, 15-day validity).

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-04-03 | 去 | Elsa 群发（BCC；To j.zaczek@mbs-systems.pl，PL-2 批次） | L3 Managed Switch — This is a Marvell-based L3 Managed 24 port DIN PoE Switch. 1, PoE af/at/bt, 370W budget, max 60℃ 2, Support DI/DO/RS485, USB, Alarm 3, Customizable We | Elsa 箱群发 BCC 触达证据（命中地址 ivolta.pl, kontakt@ivolta.pl）；S/A digest 看不到 Elsa 的 BCC，之前据此写的「未发信/未触达」不成立 | `elsa_bcc` |
| 2026-09-01 | 去 | Elsa 群发（BCC；To j.zaczek@mbs-systems.pl，PL-2 批次） | 24 Port PoE Managed Switch — Marvell AC5 L2+ 24 PoE af/at + 10G uplinks, OEM/Web GUI; Price: 170USD/PC | Elsa 箱群发 BCC 触达证据（命中地址 ivolta.pl, kontakt@ivolta.pl）；S/A digest 看不到 Elsa 的 BCC，之前据此写的「未发信/未触达」不成立 | `elsa_bcc` |
| 2026-10-21 | 用户表 | Simon | PoE交换机 很多摄像头 很多牌子的产品 有utepo的 | 表内备注 | `用户表` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：无邮件往来

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | ivolta.pl（取自域名，公司全名待核） | 推断 |
| 国家 | 波兰 | 事实（用户表）|
| 网站/域名 | ivolta.pl | 事实（用户表 URL/邮箱域名） |
| 类型 | 安防网店（波兰，Utepo 在售） | 推断（据兴趣/备注关键词） |
| 联系人 | 质量一般 | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | PoE交换机  很多摄像头<br>很多牌子的产品 有utepo的 | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | 群发(筛选后质量一般的_群发)、表:PL | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线（ivolta.pl，快照 2026-10-21）
- **是谁**：波兰 iVolta.pl（报警与 CCTV 网店：SATEL、Hikvision、Uniview、Dahua、Ajax、Bosch；表内「PoE 交换机，很多摄像头，很多牌子的产品，有 Utepo 的」「质量一般」）；表内未跟进。
- **类型**：安防网店（波兰，Utepo 在售）
- **在卖/在用品牌**：Hikvision, Uniview, Dahua, Ajax, Bosch, Utepo, SATEL
- **【官网快照】官网标题：Systemy alarmowe i monitoringu CCTV | Sklep iVolta.pl；品类词 安防监控（CCTV / 门禁） / 网络交换 / PoE**
  > W sklepie iVolta.pl oferujemy sprawdzone systemy alarmowe i monitoringu CCTV, jak również kompleksowe urządzenia pozwalające na zabezpieczenie mienia.
  > 来源：https://ivolta.pl/（抓取 2026-10-21）
- **【用户表】表内兴趣/备注**
  > PoE交换机 很多摄像头 很多牌子的产品 有utepo的
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【官网快照】iVolta 定位**
  > Systemy alarmowe i monitoringu CCTV | Sklep iVolta.pl ; oferujemy sprawdzone systemy alarmowe i monitoringu CCTV
  > 来源：https://ivolta.pl/（抓取 2026-10-21）
- **【用户表】PoE 交换机；有 Utepo 的**
  > PoE交换机  很多摄像头 很多牌子的产品 有utepo的；质量一般
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- 备注：（无首轮调研；由 deepen.py 建档） ｜ 规则加厚 2026-10-21（autodeep.py；T 档 T4）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（人工复核：官网快照逐家核对 + 表内；T4/T5 信号优先））

| 公司事实 | 内容 |
|---|---|
| 总部/地址 | 波兰 |
| 其他 | 官网 ivolta.pl，语言 pl，快照状态 ok；角色判定来源：用户表 |

- **业务线**：报警 / CCTV 网店
- **触达通道（公开）**：role: 安防网店（波兰，Utepo 在售）；region: 波兰；contact: kontakt@ivolta.pl
- **近况信号**：
  - 官网：W sklepie iVolta.pl oferujemy sprawdzone systemy alarmowe i monitoringu CCTV；kw hikvision 76 / nvr 25 / uniview 15 / dahua 12 / poe 10
  - 表内：PoE 交换机 很多摄像头 很多牌子的产品 有 utepo 的；质量一般
- **风险/边界**：网店/多品牌（Hikvision 自带 PoE）；现售 Utepo 价格基准低；表内「质量一般」；仅 kontakt@，未跟进过
- **Saga 对位结论**：P1 STC-28DGGPM（20% 档）——现售 Utepo PoE → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$80.7 @20%）；非管理 8/16 PoE 位 HRUI STC-028GP / STC-2216GPM（列表价，注明）
- **邮件切入句（英文）**：Alongside the Utepo PoE switches in your shop, we supply neutral-brand Marvell-based 8-PoE + 2 SFP L2+ and budget 8/16-port PoE units for camera kits from small lots, CE/RoHS, EXW USD — which port count do your installer customers buy most?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://ivolta.pl/　语言：pl　站点地图 URL 数：818
- **标题**：Systemy alarmowe i monitoringu CCTV / Sklep iVolta.pl
- **描述**：W sklepie iVolta.pl oferujemy sprawdzone systemy alarmowe i monitoringu CCTV, jak również kompleksowe urządzenia pozwalające na zabezpieczenie mienia.
- **首页栏目**：Systemy alarmowe i monitoringu CCTV / Autonomiczna czujka dymu SDA-250 SATEL / Zestaw sys. alarm.: PRF16LTE, ANT-LTE-I, OPU-4 P PERFECTA 16 LTE SET-A SATEL / Głośnik sufitowy IPS301015-S UNIVIEW / Moduł podstawowy z 20 czujnikami – odstęp 2,5 m TORSUS COMPACT 50 DEA / Akademia zabezpieczeń – szkolenia / SATEL BE WAVE: Poznaj nowe centrale alarmowe HYBRID i WIRE - Rzeszów / Konwerter wyjściowy AVIO analog/Dante (1-kanałowy) ADP-DAO-0X1 MONACOR
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：hikvision 76、nvr 25、uniview 15、cctv 14、dahua 12、poe 10、tp-link 3、integrator 2、switch 1、ethernet 1、camera 1
- **站内出现的品牌**：Hikvision, Uniview, Dahua, Ajax, Bosch　（「（！）」= Saga 自家/供应商品牌已在其站内出现）
- **站内型号串**（正则抽取，含非交换机）：DS-2CD20123G2-LIUY, DS-2CD1047G3-LIU, NEMA-4X, IP-64, SO-MF2, INT-TSH210, IPC-HDW3849H-ZAS-PV-PRO, DS-1275ZJ-SUS, DS-1280ZJ-XS, DS-7104NI-Q1, DS-7108NI-Q1, DS-7604NXI-K1
- **站内公开邮箱**：hsrc@hikvision.com, info.pl@hikvision.com, kontakt@ivolta.pl, volta@volta.com.pl
- **站内公开电话**：007-2013 2014-2026
- **社媒**：https://pl.linkedin.com/company/volta-sp.-z-o.o./, https://www.facebook.com/voltapolska?ref=hl, https://www.youtube.com/user/VoltaCCTV/
- **产品类页面**：https://ivolta.pl/Multiswitche/761/produkty/；https://ivolta.pl/Inne/644/produkty/；https://ivolta.pl/Inne/769/produkty/；https://ivolta.pl/Inne/732/produkty/；https://ivolta.pl/ROP-y/282/produkty/；https://ivolta.pl/prox/1046/produkty/
- **已抓子页**：[Kontakt / Sklep iVolta.pl](https://ivolta.pl/contact/)；[Kamera IP 4Mpix ColorVu 3.0 IR+LED 30m 2.8mm mikr DS-2CD1047](https://ivolta.pl/ds-2cd1047g3-liu-2-8mm-kamera-ip-4mpix-colorvu-3-0-ir-led-30m-2-8mm-mikr/53679/produkt/)；[Kamera IP 12Mpix AcuSense IP67, IR+LED 40m 2.8mm DS-2CD20123](https://ivolta.pl/ds-2cd20123g2-liuy-sl-2-8mm-kamera-ip-12mpix-acusense-ip67-ir-led-40m-2-8mm/53705/produkt/)；[Porównywarka produktów / Sklep iVolta.pl](https://ivolta.pl/compare/)；[Sklep iVolta.pl](https://ivolta.pl/aktualnosci/)；[Monitoring / Sklep iVolta.pl](https://ivolta.pl/monitoring/940/produkty/)
- 首页正文摘录：Logowanie × 22 295 06 06 Pon. - Pt. 8:00 - 16:00 kontakt@ivolta.pl PL PL PLN PLN EUR USD Logowanie W przypadku logowania klientów indywidualnych (nie B2B) jako login prosimy podać adres e-mail. Login * Hasło * Zaloguj się Nie posiadam konta, zarejestruj się! Zapomniałem hasła Zapomniałem loginu (Tylko klienci B2B) Porównywarka produktów 0,00 zł MENU Szukaj PL PLN Język: PL Waluta: PLN EUR USD W przypadku logowania kl
- **自动对位建议**：STC-424DGGPM-280W（官网快照对位：PoE 词频 10、监控 40 → 24 口 PoE L2+ 走量款；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SB-1208.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：4 个　|　**数据截至**：2026-10-24T07:26:33Z　|　**最近变化**：2026-10-24T07:26:33Z
- **最近变化摘要**：2026-10-24 youtube：恢复可达（上轮 YouTube 404（对运行器 IP 的拦截，非频道不存在；设 YT_API_KEY 走官方 API 可绕过））
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-1208/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://ivolta.pl/) | html | HTTP 200 | 2026-10-24T07:26:33Z | 12092 字符；首行：Systemy alarmowe i monitoringu CCTV \| Sklep iVolta.pl Logowanie |
| [sitemap](https://ivolta.pl/sitemap.xml) | sitemap | HTTP 200 | 2026-10-24T07:26:33Z | 900 个 URL；最新 lastmod - |
| [news_1](https://ivolta.pl/blog) | html | HTTP 200 | 2026-10-23T04:20:51Z | 8930 字符；首行：Blog iVolta – Nowości, porady i trendy z branży zabezpieczeń \| Sklep iVolta.pl |
| [youtube](https://www.youtube.com/user/VoltaCCTV) | youtube_handle | HTTP 200 | 2026-10-24T07:26:33Z | 15 条；最新：2026-06-01T14:25:23+00:00 Radiacode field test - strage rogue radiation source fou |

- **人工定期看（登录墙，不自动抓）**：Facebook: https://www.facebook.com/voltapolska?ref=hl；LinkedIn: https://pl.linkedin.com/company/volta-sp.-z-o.o./

## 联系方式（已有 · 原值照录）

- 邮箱：`kontakt@ivolta.pl`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：质量一般
- 网站/域名：ivolta.pl
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| —（未具名） | 公司级 | kontakt@ivolta.pl | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E/群发/筛选后质量一般的_群发.xlsx#PL:40 | 39 | https://ivolta.pl/pfs3106-4p-60-switch-przemyslowy-4-portowy-PoE-10-100mbps-1-port-uplink-10-100-1000mbps-1-port-sfp/17398/produkt/ | 波兰 | 质量一般 | 谷歌 | PoE交换机  很多摄像头<br>很多牌子的产品 有utepo的 | kontakt@ivolta.pl |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：现售 Utepo PoE → 8 口 PoE+ 2 SFP L2+ STC-28DGGPM（$80.7 @20%）；非管理 8/16 PoE 位 HRUI STC-028GP / STC-2216GPM（列表价，注明） | $80.7 USD EXW（20% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 20%（安防网店（波兰，Utepo 在售）） |
| 备选2 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：20% 档 $139.9 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），20% 档公式为 $181.2——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-28DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；20% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：欧洲主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STC-28DGGPM 按 20% 档报价，做现供应商的第二货源
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

**主题**：Neutral-brand PoE switches next to Utepo in your shop

```text
Hello iVolta team,

Over the past months you had a few product mails from us - most recently "24 Port PoE Managed Switch" on 1 September 2026 - and there was no reason to answer a mass mail. This one is specific.

Alongside the Utepo PoE switches in your shop: an 8 x Gigabit PoE+ + 2 x SFP L2+ managed switch, Marvell-based, neutral packing, CE/RoHS - model STC-28DGGPM - $80.7 USD EXW at distributor price (MOQ 1, 15-day validity); a budget 8-PoE + 2 uplink unmanaged unit for camera kits, STC-028GP, is $25.1.

One question: which PoE port count do your installer customers buy most - 4, 8 or 24?

Best regards,
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

- **2026-11-24**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 25）

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
