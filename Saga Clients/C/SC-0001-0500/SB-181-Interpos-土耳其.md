# Interpos
**官方名称（调研核实）**：İnterpos Bilgi Teknolojileri Elektronik San. ve Tic. A.Ş.（İstanbul Ataşehir, TR；inter-pos.com）

> **评级 C**　|　土耳其　|　档案编号 `SB-181`　|　优先级 —　|　状态：WhatsApp 已加·未回复
>
> **P 池并入（C 档，等级不动）：留 C 储备**（批 LT-R05S · 2026-10-29 · 下次巡检 2026-12-28）：复核打回（LT-R05S）：伊斯坦布尔零售自动化 / POS 设备公司 İnterpos（展会名片，没交谈）：POS 非本行业 → C 储备｜原：☆ P 池观察（P 观察候选，B 档并池 · 等级不动）：真回 ✔ 但 未坐实对位 未知 → 观察；命中 2/6（成单/样品 — · 真回 ✔ · WA ✔ · 对位 未知 · 登记 未坐实 · 体量 10–19 人（ZoomIn）
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：WhatsApp 已加　|　**所在清单**：ISAF2025展会、表:Simon　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-181
rating: C
rating_auto: B
sieve: keep_C  # 闸 3 AB1 2026-10-29
rating_research: C  # Q-76 LT-R05S 2026-10-29 复核打回 C 储备：伊斯坦布尔零售自动化 / POS 设备公司 İnterpos（展会名片，没交谈）：POS 非
name_official: "İnterpos Bilgi Teknolojileri Elektronik San. ve Tic. A.Ş.（İstanbul Ataşehir, TR；inter-pos.com）"
score: 52
country: 土耳其
region: 土耳其
website: inter-pos.com
type: 经销/集成（类型待核）
tier_tags: ["ISAF2025展会", "表:Simon"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STC-028GP
price_tier: 20%
research: done
site_snapshot: ok  # 2026-10-21
sources: 2
updated: 2026-10-29
```

## SALES BRIEF（压缩模型）

- **是谁**：伊斯坦布尔 Ataşehir 的零售自动化/POS 设备公司 İnterpos（1995 年成立；POS 收银机、EFT-POS、电子秤、打印机、条码系统；11–50 人、营收 $1–10M；董事长/总裁 Hulusi Kültür（ex-Inter Mühendislik、Inter Hong Kong）；兼 Tadiran 电池土耳其代理；İçerenköy Mah. Prof. Dr. Necmettin Erbakan Cad. Kayışdağı İş Merkezi K:8 No:91；+90 216 469 64 00）。ISAF 记录：没做交谈、给了名片；WhatsApp 已加（+90 532 264 89 90）；无后续跟进。零售终端网络需要小型 PoE/非 PoE 交换机 → 分销/配套 20%。（调研 2026-10-21；表内兴趣：没做交谈，给了名片）
- **为什么是 C 级**：**调研后定级 C**（Q-76 LT-R05S 2026-10-29 复核打回 C 储备：伊斯坦布尔零售自动化 / POS 设备公司 İnterpos（展会名片，没交谈）：POS 非本行业 → C 储备；c_sub=储备·复核打回 ；回信 / 询价即回 B）；自动分级 B：+12 备注记录了对方问价/要资料/见面等互动；+12 ISAF 2025 展会面对面名片；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 土耳其/土耳其；+5 最近活动 2025；C 级细分：储备·复核打回
- **历史互动**：WhatsApp 已加
- **P1**：不推（C 级）；若对方主动来询，起手 STC-028GP（深挖对位：配套/分销 20% 档：STC-028GP（Saga Realtek 线 8 GE PoE + 2 上联非管理，列表 $24.2）与 STC-08GE（8 GE 桌面，$10.5）作 POS 门店配套；管理型 STC-28DGGPM（$80.7））
- **最大未知**：年走量与现供应商
- **下一步**：2026-11（Simon） A 邮箱首封 + WhatsApp（Simon） 首封 + 一句话

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-181` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（展会名片 + WhatsApp 已加，邮件 0 封）：用户表「没做交谈，给了名片 / 90 53226 48990 已加」；S/A 邮箱 0 封；Elsa 箱：`to:inter-pos.com` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → 三箱（S/A/E）均未发（第 74 批(i)）** ｜ 类型：— ｜ 筛子：3（已加 WhatsApp，表内有往来） ｜ 停点：仓库只有用户表一行；往来在 Simon 手机 ｜ 复活：首封邮件（A 邮箱，按 email_hook）+ WhatsApp 一句话 ｜ 通路：土耳其 非主攻 ｜ 节奏：一封 ｜ 证据：gmail_digest：out 0；用户表：「没做交谈，给了名片 / 90 53226 48990 已加」；研究档 risks：主业 POS，交换机为边缘品类；ISAF 未交谈；无后续跟进
- **现状一句话**：伊斯坦布尔 Ataşehir 的零售自动化/POS 设备公司 İnterpos（1995 年成立；POS 收银机、EFT-POS、电子秤、打印机、条码系统；11–50 人、营收 $1–10M；董事长/总裁 Hulusi Kültür（ex-Inter Mühendislik、Inter Hong Kong）；兼 Tadiran 电池土耳其代理；İçerenköy Mah. Prof. Dr. Necmettin Erbakan Cad. Kayışdağı İş Merkezi K:8 No:91；+90 216 469 64 00）。ISAF 记录：没做交谈、给了名片；WhatsApp 已加（+90 532 264 89 90）；无后续跟进。零售终端网络需要小型 PoE/非 PoE 交换机 → 分销/配套 20%。
- **对方真实需求（有据）**：配套/分销 20% 档：STC-028GP（Saga Realtek 线 8 GE PoE + 2 上联非管理，列表 $24.2）与 STC-08GE（8 GE 桌面，$10.5）作 POS 门店配套；管理型 STC-28DGGPM（$80.7）
- **断点 / 为什么停在这里**：主业 POS，交换机为边缘品类；ISAF 未交谈；无后续跟进
- **Saga 现在该推什么**：P1 **STC-028GP**（20% 档，Realtek 线按 HRUI 2026-09-30 进价 +20% 现算（Q-47 默认，不用 Drive 旧表价）：STC-028GP $24.2→$25.1；按主表（研究档 saga_fit））——配套/分销 20% 档：STC-028GP（Saga Realtek 线 8 GE PoE + 2 上联非管理，列表 $24.2）与 STC-08GE（8 GE 桌面，$10.5）作 POS 门店配套；管理型 STC-28DGGPM（$80.7）
- **下一步（具体）**：2026-11（Simon）　A 邮箱首封 + WhatsApp（Simon）　首封 + 一句话
  - 第一问（只问一个）：Hulusi Bey, POS ve yazarkasa kurulumlarınızın yanında satabileceğiniz 8 port gigabit PoE + 2 uplink masaüstü switch fiyatı 25,1 USD EXW, 8 port gigabit 10,5 USD; Hong Kong şirketiniz üzerinden faturalandırma mümkün — ilk deneme partisi için 20 adet yeterli mi?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-10-21 | 用户表 | Simon | 没做交谈，给了名片 / 90 53226 48990 已加 | 表内备注 | `用户表` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：WhatsApp 往来未入库

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-29 查）：**

- `inter-pos.com` → 主机商 cPanel 类邮箱（MX：mail.intercomponents.com）。主机商附带邮箱（主机商 cPanel 类邮箱）：过滤弱、几乎不丢信，但常是老板自己收、没人代读 → 短、直接、一行型号 + 价格 + 一个问题

**假日避让（土耳其 · 按下一步「2026-11」窗口 2026-11-01→2026-11-30）：**

- 窗口内无该国法定假日

**公司底数 · 第 86 批（Türkiye · ZoomInfo 公司档（员工 / 营收档 / President 1995 至今）+ 研究档（成立日 1995-04-10；LinkedIn），2026-10-27 查；https://www.zoominfo.com/p/Hulusi-Ku%CC%88ltu%CC%88r/1540298018）：**

- 法定名 / 登记号：İNTERPOS BİLGİ TEKNOLOJİLERİ ELEKTRONİK SAN. VE TİC. A.Ş. · Ticaret Sicil / Vergi No 待补（A.Ş. 高管仅 Ticaret Sicil Gazetesi） · 状态 **Faal（展会名片 + 官网）** · 成立 1995-04-10 · A.Ş.（股份公司）· 私人持有
- 行业码 / 经营范围：POS / 电子设备制造 + IT 技术（Manufacturing 分类）；Ataşehir İstanbul
- 注册地址：İçerenköy Mah. Prof. Dr. Necmettin Erbakan Cad. Kayışdağı İş Merkezi K:8 No:91, 34752 Ataşehir / İstanbul
- 规模档：10–19 人（ZoomInfo）
- 账目：ZoomInfo 档 $1–5M；TR 年报 4 月（A.Ş. 大会）
- 高管：Hulusi KÜLTÜR — Yönetim Kurulu Başkanı / President（1995 创立至今，30 年）= 研究档 KP → **老板 = 联系人**（展会名片）
- 高管：Levent Gülerman / Özgür Kavrak — 同事（ZoomInfo）
- 控制人 / 股东：Hulusi Kültür（创始人；比例待核）
- **这意味着什么：**
  - **老板 = 联系人（董事长 Hulusi Kültür，30 年 A.Ş.，10–19 人，$1–5M）**，展会名片 + WhatsApp 已加、邮件 0 封：POS 设备制造商买交换机是配自家 POS / 零售网络方案 → OEM 30%（İnterpos 标）或集成 25%；WhatsApp 线由 Simon 直接跟（规则：WhatsApp 客户不走邮件编码）
  - A.Ş. 高管公开需 Ticaret Sicil Gazetesi（付费）→ 不补；土耳其 CE + TSE 由进口方办

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Interpos | 事实（用户表） |
| 国家 | 土耳其 | 事实（用户表）|
| 网站/域名 | inter-pos.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Hulusi Kultur / Hulusi Kultur / CEO | 事实（用户表） |
| 来源（From） | ISAF 2025 | 事实（用户表） |
| 兴趣（Interested in） | 没做交谈，给了名片 | 事实（用户表） |
| 用户备注（Remark） | 902164696400(114)    <br>90 53226 48990 已加 | 事实（用户表） |
| 所在清单 | ISAF2025展会、表:Simon | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：伊斯坦布尔 Ataşehir 的零售自动化/POS 设备公司 İnterpos（1995 年成立；POS 收银机、EFT-POS、电子秤、打印机、条码系统；11–50 人、营收 $1–10M；董事长/总裁 Hulusi Kültür（ex-Inter Mühendislik、Inter Hong Kong）；兼 Tadiran 电池土耳其代理；İçerenköy Mah. Prof. Dr. Necmettin Erbakan Cad. Kayışdağı İş Merkezi K:8 No:91；+90 216 469 64 00）。ISAF 记录：没做交谈、给了名片；WhatsApp 已加（+90 532 264 89 90）；无后续跟进。零售终端网络需要小型 PoE/非 PoE 交换机 → 分销/配套 20%。
- **在卖/在用品牌**：Tadiran（电池代理）
- **【LinkedIn】公司信息与 KP 邮箱**
  > İnterpos Bilgi Teknolojileri Elektronik San. ve Tic. A.Ş. … Şirket büyüklüğü: 11 - 50 çalışan … Genel Merkez: İstanbul, Ataşehir … Kuruluş: 1995 … Uzmanlık Alanları: Posyazarkasa, Yazarkasa, EFT-Pos, Terazi, Yazıcı, Barkod Sistemleri ve Perakende … Hulusi K. Y.K.B İnterpos AŞ. hkultur@inter-pos.com
  > 来源：https://tr.linkedin.com/company/interpos-bilgi-teknolojileri-elektronik-san-ve-tic-a-%C5%9F-（抓取 2026-10-21）
- **【名录】地址、规模、总裁履历**
  > Hulusi Kültür is the President at İnterpos Bilgi Teknolojileri Elektronik San ve Tic AŞ … Previously, Hulusi was the Director at Inter (Hongkong) Ltd. … It employs 10to19 people and has 1Mto5M of revenue … no 91 İçerenköy Mah. Prof.dr. Necmettin Erbakan Cad. Kayışdağı İş Merkezi K 8 … +90 2164696400
  > 来源：https://www.zoominfo.com/p/Hulusi-Ku%CC%88ltu%CC%88r/1540298018（抓取 2026-10-21）
- **【厂商名录】Tadiran 代理**
  > Tel: +90(216) 469 64 00 Fax: +90(216) 469 64 06 info@inter-pos.com www.inter-pos.com Contact Person: Hulusi Kültür
  > 来源：https://tadiranbat.com/distributors/sales-network-international/（抓取 2025-10-06）
- **【用户表】ISAF：给名片未交谈；WhatsApp 已加**
  > 没做交谈，给了名片 / 90 53226 48990 已加
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Hulusi Kültür（Yönetim Kurulu Başkanı / President（1995 创立至今 30 年）= 老板 = 联系人；A.Ş. 10–19 人、$1–5M（ZoomInfo）（第 86 批 官方登记核实 2026-10-27））hkultur@inter-pos.com（LinkedIn 公开 + 用户表） +90 532 264 89 90（用户表，WhatsApp 已加）〔https://tr.linkedin.com/company/interpos-bilgi-teknolojileri-elektronik-san-ve-tic-a-%C5%9F-〕
- **调研后定级**：C（原自动 B）——Q-76 LT-R05S 2026-10-29 复核打回 C 储备：伊斯坦布尔零售自动化 / POS 设备公司 İnterpos（展会名片，没交谈）：POS 非本行业 → C 储备；c_sub=储备·复核打回 ；回信 / 询价即回 B
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（名录核对））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | İNTERPOS BİLGİ TEKNOLOJİLERİ ELEKTRONİK SAN. VE TİC. A.Ş.（1995-04-10；Ataşehir İstanbul） |
| 成立 | 1995-04-10 |
| 总部/地址 | İçerenköy Mah. Prof. Dr. Necmettin Erbakan Cad. Kayışdağı İş Merkezi K:8 No:91, 34752 Ataşehir / İstanbul（+90 216 469 64 00；info@inter-pos.com） |
| 人数 | 10–19（ZoomInfo）（第 86 批 官方登记核实 2026-10-27） |
| 其他 | POS/收银机/EFT-POS/电子秤/条码；Tadiran 电池代理；有香港关联公司 Inter (Hongkong) Ltd. |

- **业务线**：零售自动化设备（POS、收银机、EFT-POS、秤、打印机、条码）；Tadiran 锂电池分销
- **触达通道（公开）**：网站: https://www.inter-pos.com/；电话: +90 216 469 64 00（公开）；邮箱（公开）: info@inter-pos.com；LinkedIn: https://tr.linkedin.com/company/interpos-bilgi-teknolojileri-elektronik-san-ve-tic-a-%C5%9F-
- **近况信号**：
  - POS/零售门店组网 → 5/8 口千兆与 8 口 PoE 小机为配套 SKU；有香港公司 → 熟悉中国采购、可走 HK 结算
- **风险/边界**：主业 POS，交换机为边缘品类；ISAF 未交谈；无后续跟进
- **Saga 对位结论**：P1 STC-028GP（20% 档）——配套/分销 20% 档：STC-028GP（Saga Realtek 线 8 GE PoE + 2 上联非管理，列表 $24.2）与 STC-08GE（8 GE 桌面，$10.5）作 POS 门店配套；管理型 STC-28DGGPM（$80.7）
- **邮件切入句（英文）**：Hulusi Bey, POS ve yazarkasa kurulumlarınızın yanında satabileceğiniz 8 port gigabit PoE + 2 uplink masaüstü switch fiyatı 25,1 USD EXW, 8 port gigabit 10,5 USD; Hong Kong şirketiniz üzerinden faturalandırma mümkün — ilk deneme partisi için 20 adet yeterli mi?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://inter-pos.com/　语言：en　站点地图 URL 数：0
- **标题**：We’re Revamping Our Website – Designed for a Smarter Experience
- **首页栏目**：We’re Revamping Our Website – Designed for a Smarter Experience / Get in Touch
- 首页正文摘录：We’re Revamping Our Website – Designed for a Smarter Experience To provide you with better service, we are revamping our website with updated content and enhanced usability. We're simplifying technical documentation, streamlining product access and optimizing mobile responsiveness. With our new layout: • You'll reach in-demand product categories more easily. • Discover content aligned with global trade standards. • E
- 数据文件：`data/saga_clients/site_snapshots/SB-181.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-29T08:41:09Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-181/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://inter-pos.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 650 字符；首行：We’re Revamping Our Website – Designed for a Smarter Experience |

## 联系方式（已有 · 原值照录）

- 邮箱：`hkultur@inter-pos.com`〔企业邮箱；来源：用户表原值〕
- 电话：`+902164696400114`〔WhatsApp 已加；原值见来源表〕
- 电话：`+905322648990`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Hulusi Kultur
- 联系人（原值）：Hulusi Kultur / CEO
- 职位（原值）：CEO
- 网站/域名：inter-pos.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Hulusi Kültür | Yönetim Kurulu Başkanı / President（1995 创立至今 30 年）= 老板 = 联系人；A.Ş. 10–19 人、$1–5M（ZoomInfo）（第 86 批 官方登记核实 2026-10-27） | hkultur@inter-pos.com（LinkedIn 公开 + 用户表） / +90 532 264 89 90（用户表，WhatsApp 已加） | 调研核实（公开页） | https://tr.linkedin.com/company/interpos-bilgi-teknolojileri-elektronik-san-ve-tic-a-%C5%9F- |
| Hulusi Kultur | CEO | hkultur@inter-pos.com / +902164696400114 | 用户表原值·WhatsApp 已加 | Clients/ 表 |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:inter-pos.com`, `e:hkultur@inter-pos.com`, `p:322648990`, `p:696400114`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/2025土耳其ISAF客户.xlsx#Simon:10 | 9 | Interpos | Turkey | Hulusi Kultur |  | 没做交谈，给了名片 | hkultur@inter-pos.com 902164696400(114)    /905322648990 www.inter-pos.com | CEO | — |
| A/ISAF 2025.xlsx#总表:10 | 9 | www.inter-pos.com | 土耳其 | Hulusi Kultur<br>CEO | ISAF 2025 | 没做交谈，给了名片 | hkultur@inter-pos.com | 902164696400(114)    <br>90 53226 48990 已加 | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：储备·复核打回。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SB-181,B,理由` 后重跑即可。

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
| 商业资格结论 | **不合格（见 C 级细分）→ 不主动跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：WhatsApp / 私信一句话（复制即发；不发邮件）

```text
Hulusi Bey, POS ve yazarkasa kurulumlarınızın yanında satabileceğiniz 8 port gigabit PoE + 2 uplink masaüstü switch fiyatı 25,1 USD EXW, 8 port gigabit 10,5 USD; Hong Kong şirketiniz üzerinden faturalandırma mümkün — ilk deneme partisi için 20 adet yeterli mi?
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- 不复核。对方主动来询 → 在 `data/saga_clients/人工定级.csv` 写一行升级后重跑。

## 变更日志

- 2026-10-29：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 B，分数 52）；人工/调研定级 → C

---

*建档日期：2026-10-29　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
