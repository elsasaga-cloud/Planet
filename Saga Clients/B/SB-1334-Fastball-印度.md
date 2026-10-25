# Fastball

> **评级 B**　|　印度　|　档案编号 `SB-1334`　|　优先级 ★★　|　状态：成交过·已凉（Simon: gg）
>
> **类型**：经销/贸易（德里）（推断）　|　**历史关系**：成交/下单过　|　**所在清单**：补录、已成单、PI成单、Simon:gg、成交(PI)　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-1334
rating: B
rating_auto: A
rating_research: B  # PI 包成单客户，Simon 标签 gg：gg（已凉）→ B（成交过·慢慢跟进）
name_official: "Fastball"
score: 77
country: 印度
region: 南亚
website: fastball.in
type: 经销/贸易（德里）
tier_tags: ["补录", "已成单", "PI成单", "Simon:gg", "成交(PI)"]
deal: yes
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 1 msgs (out 0 / in 1), 2023-09-20 -> 2023-09-20
p1: STC-424DGGPM-280W
price_tier: 20%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：已成单 1 次（STSC20231009002，2023-10-09）；Simon 文件夹标签 gg（已凉）；详见 research/SB-1334.json（调研 2026-10-22；表内兴趣：商用 PoE 交换机（2023-10 一单 80 台，USD 260 样品级））
- **为什么是 B 级**：**调研后定级 B**（PI 包成单客户，Simon 标签 gg：gg（已凉）→ B（成交过·慢慢跟进））；自动分级 A：+50 有成单/下单/买过记录（用户备注或跟进表）；+10 谈到样品/测样；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-6 区域 南亚/印度
- **历史互动**：成交/下单过
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：无 — —｜毛利复盘：首单 23.4%（80 台 @19.75 成本）——正常；STC-204GP $24.2（洪瑞 2026-09-30 进价 135 CNY +20%，Q-47 默认；Drive 旧表 $20.4 不用）；—
- **第一问（只问一个）**：Rishi — your IndiaMART page lists a "4 Port Industrial Ethernet Switch FBC-204GP", which matches our STC-204GP (4 × PoE + 2 × SFP). Is it a live stock item for you, or a listing from the 2023 catalogue? If live, the current price is STC-204GP $24.2 USD EXW (MOQ 1, 15-day validity) and I can quote 20/50-pc tiers; if not, I will leave you alone.
- **最大未知**：年走量与现供应商
- **下一步**：2027-Q1（非主攻区，顺带一问；不投入） A 邮箱 → office@fastball.in（Rishi Kumar Bansal） 一问：IndiaMART 上的 FBC-204GP 列表是不是在卖我方 STC-204GP（有则给现价，无则不再发）（第 75 批(aj) 2026-10-25：英文信稿已写 `draft_en`（2027-Q1 用）；按 action「一问」：IndiaMART FBC-204GP 是否我方 STC-204GP；BIS 对方侧）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-1334` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度绑定→已冷（一单 $260 清洁笔 2023-10-09；2023-09-20 Rishi 来信要「authorised distributorship certificate」；PI 包「gg」；之后无往来；Elsa 箱：`to:fastball.in` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → 三箱（S/A/E）均未发（第 74 批(n)））** ｜ 类型：德里经销/贸易（Fastball，Rishi Kumar Bansal）——想做「印度授权分销」的贸易商 ｜ 筛子：5（一次 $260 付款）但品类是光纤清洁笔，不是交换机 ｜ 停点：2023-09 要授权分销证书（Saga 不签区域授权——INH 规则：不做总代/授权）；之后只成交了一单耗材 ｜ 复活：不投入 ｜ 通路：IN ｜ 节奏：不动 ｜ 证据：k=edee4186a39f51b9（2023-09-20 来信）；PI STSC20231009002（Cleaner Pen 1.25mm ×40 + 2.5mm ×40 @2.6 + 运费 52 = $260）
- **现状一句话**：Rishi 2023-09 写来一封「正式确认拿下印度市场，请出具授权分销证书」的信；Saga 没有签。10 月他买了 80 支光纤清洁笔。此后两年无往来。
- **对方真实需求（有据）**：授权分销身份（而非产品）。
- **断点 / 为什么停在这里**：授权诉求 vs Saga 不做区域授权。
- **Saga 现在该推什么**：P1 **无**（20% 档，STC-204GP $24.2（洪瑞 2026-09-30 进价 135 CNY +20%，Q-47 默认；Drive 旧表 $20.4 不用）；—）———｜毛利复盘：首单 23.4%（80 台 @19.75 成本）——正常
  - 复购/在买项：2023-10-09 唯一一单：$260（Simon 利润 RMB 553；PI 复盘 #2，Simon 标 gg）；IndiaMART 仍挂 FBC-204GP（= STC-204GP）
- **下一步（具体）**：2027-Q1（非主攻区，顺带一问；不投入）　A 邮箱 → office@fastball.in（Rishi Kumar Bansal）　一问：IndiaMART 上的 FBC-204GP 列表是不是在卖我方 STC-204GP（有则给现价，无则不再发）（第 75 批(aj) 2026-10-25：英文信稿已写 `draft_en`（2027-Q1 用）；按 action「一问」：IndiaMART FBC-204GP 是否我方 STC-204GP；BIS 对方侧）
  - 第一问（只问一个）：Rishi — your IndiaMART page lists a "4 Port Industrial Ethernet Switch FBC-204GP", which matches our STC-204GP (4 × PoE + 2 × SFP). Is it a live stock item for you, or a listing from the 2023 catalogue? If live, the current price is STC-204GP $24.2 USD EXW (MOQ 1, 15-day validity) and I can quote 20/50-pc tiers; if not, I will leave you alone.

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2023-09-20 | 来 | Rishi Bansal | Please consider this mail as our official acknowledgement regarding Indian market capturing of Saga Telecom product range… Please share the authorised distributorship certificate on saga telecom letterhead | 授权诉求 | `edee4186a39f51b9` |
| 2023-09-20 | 去 | Saga → Fastball（Fastball_Price.xls，Saga 抬头价目表） | STC-05GE $6 / STC-08GE $10 / STC-016GE $33 / STC-024GE-U $50 / STC-15XGDGE $38 / STC-028GFP $20 / STC-1216GFP $40 / STC-1224GFP $55 / STC-024GP $18 / STC-228GP $78 / STC-2024GP $84 / STC-28GM $45 / STC-424XGGM $111 / STC-448XGGM $223 / STC-28GPM $55 / STC-4424GCPM $140 / STC-448XGGPM $350 / STI-014FE $12 / STI-114GE $21 / STI-118GFP $24 / STI-208GP $54 | Saga 为 Fastball 专门做过一份全线价目表（2023 老汇率、未加三档），说明当时是认真考虑过印度分销的；Rishi 要的「authorised distributorship certificate」没签，但价表给了。2023 价 vs 价格主表 2026（STC-424XGGM $143、STC-28DGGPM $99）可见涨幅 | `Drive PI 文件夹（data/pi_2026-10/text） 2_Rishi Fastball_Price.xls` |
| 2023-10-09 | PI | Simon → Fastball | Cleaner Pen 1.25mm LC ×40 @2.6；2.5mm SC ×40 @2.6；Freight 52；TOTAL 260 USD | 唯一成交（耗材） | `PI STSC20231009002` |
| 2023-10-09 | 来 | Rishi（FTTH需求.docx） | Patch cords / Pigtails / FTTH boxes / Home distribution boxes / Wall & Rack mount LIU / Splitters (LGX cassettes, ABS boxes) / Sleeves / VFL / Power meters / FTTH tool kit / Fiber cleaning cassettes and pens / PoE extenders / injectors / adapters / Joint enclosures | Rishi 的主业是 FTTH 无源件（清洁笔那单就是这个清单的一项）；交换机只是顺带。Fastball FBC-204GP = STC-204GP 只是其网站列品。复活只能从「光纤清洁/FTTH 配件 + 一款 PoE」切入，不是管理型交换机 | `Drive PI 文件夹（data/pi_2026-10/text） 2_Rishi FTTH需求.docx` |
| 2023-10-09 | 内 | Simon 成本表（PI 包） | 内部《成本统计.xlsx》：STSC20231009002：成本 1,811 / 收款 2,364 / 利润 553（23.4%） | 利润率 = 利润÷收款；对照 20/25/30 加价 = 16.7%/20%/23% 毛利；详见 docs/成单客户_毛利复盘_内部_2026-10-24.md | `cost_sheet` |
| 2023-12-13 | 去 | Saga 内部（List_2023.12.13.xlsx / New_List.xlsx / Bypass_client_list.xlsx，存于 Rishi 文件夹） | 印度名单：secureye「很多找到的邮箱都试了 fail」、kabirinfotech「买来刷logo」、mahalasaent「requested samples before, but now company distributor Surabhi Info is on it. SILENT follow-up」、sundartechno Manoj Kumar… | Saga 自己做的印度 MC/旁路/工业交换机线索表放在 Fastball 文件夹里 = 当时设想 Fastball 当印度分销去跟这些线索（与给 Angora 土耳其名单同一套路）。Fastball 没成为分销商，名单也没交出去；这些印度户多数已在客户库 C/B | `Drive PI 文件夹（data/pi_2026-10/text） 2_Rishi` |
| 2024-01-15 | 去 | Saga 代采记录《Information.docx》《Customs_Information.docx》（Rishi 配件） | Supplier Lenon（宁波）… Cleaner Pen, HS 8517799000… 40 pc 1.25mm (LC) + 40 pc 2.5mm (SC)… Cost 2.7×80 + 46 ship = 262 USD；采购成本 2.7×80 + 2.5 = 218.5 USD | Saga 为 Rishi 代采过 80 支光纤清洁笔（毛利约 $43）——Fastball 的 FTTH 配件清单（跳线/尾纤/分光器/LIU/VFL/光功率计/PoE 延长器…）Saga 都能代采，但利润薄，只作为交换机单的搭售 | `pi_doc` |
| 2024-01-15 | 去 | Saga→Rishi《Model_List.docx》《Title_Reference.docx》 | Commercial Rack: STC-4168XGGCM / STC-4816XGCGM / STC-4816XGCGPM / STC-424XGGM / STC-424XGGPM / STC-448XGGM / STC-448XGGPM / STC-448XGGM-AF… Industrial Rack: STI-448XGGM / STI-4168XGGCM…；Title_Reference：「5 port unmanaged Ethernet switch / 8 port 10/100M lan switch / … / 27 port hybrid rate poe switch…」共 30+ 条电商式标题 | Saga 给 Rishi 的是「机架型号清单 + 电商标题参考」——Fastball 在印度做线上/分销铺货，要的是可直接上架的标题与型号树；这份清单也是 Saga 现成的 IndiaMART/Amazon 文案底稿 | `pi_doc` |

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Fastball | 事实（用户表） |
| 国家 | 印度 | 事实（用户表）|
| 网站/域名 | fastball.in | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/贸易（德里） | 推断（据兴趣/备注关键词） |
| 联系人 | Rishi Kumar Bansal | 事实（用户表） |
| 来源（From） | 补录：PI 包成单客户（T29-U8） | 事实（用户表） |
| 兴趣（Interested in） | 商用 PoE 交换机（2023-10 一单 80 台，USD 260 样品级） | 事实（用户表） |
| 用户备注（Remark） | 已成单 1 次（STSC20231009002，2023-10-09）；Simon 文件夹标签 gg（已凉）；详见 research/SB-1334.json | 事实（用户表） |
| 用户分档（Category） | 经销/贸易（德里） | 事实（用户表） |
| 所在清单 | 补录、已成单、PI成单、Simon:gg、成交(PI) | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-22）**　网站状态：
- **是谁**：已成单 1 次（STSC20231009002，2023-10-09）；Simon 文件夹标签 gg（已凉）；详见 research/SB-1334.json
- **类型**：经销/贸易（德里）
- **【PI】成交单据 STSC20231009002（CI，2023-10-09）：型号见单据 共 80 台，USD 260.0；Simon 成本表利润 RMB 553.48**
  > 来源：PI.zip:2 印度 Rishi gg/CI.xls（抓取 2023-10-09）
- **【PI】PI 包文件夹「印度 Rishi gg」：Simon 标签 gg；单号 1 个，2023-10-09 → 2023-10-09，销售 USD 260.0 / RMB 0，Simon 成本统计利润合计 RMB 553.48**
  > 来源：PI.zip:2 印度 Rishi gg（抓取 2026-10-22）
- **【公开平台核查（T29-U18）】IndiaMART 产品页：4 Port Industrial Ethernet Switch FBC-204GP, BLACK —— 卖家 Fastball（Rishi Bansal，Ashok Nagar, New Delhi 110093），成立 2021，制造/批发/零售光纤线缆、PLC 分路器、光功率计、接头盒**
  > 4 Port Industrial Ethernet Switch FBC-204GP, BLACK … Established in the year 2021 "Fastball" … Rishi Bansal
  > 来源：https://www.indiamart.com/proddetail/4-port-industrial-ethernet-switch-fbc-204gp-2852734505091.html（抓取 2026-10-23）
- **【公开平台核查（T29-U18）】官网：Jhilmil Industrial Area A-61，销售 +91-9871 753 979，支持 +91-9355 075 075；自述 AI 驱动的电信有线产品公司（预防性维护/按需服务）**
  > Fastball Building, Unit no. A-61, Jhilmil industrial Area, Delhi 110095 Sales +91-9871 753 979, Support +91-9355 075 075
  > 来源：https://fastball.in/（抓取 2026-10-23）
- **【公开平台核查（T29-U18）】splicingmachines.com：Fastball 独家进口 Signal Fire AI-5 / AI-9 熔接机，全印分销（孟买/特伦甘纳/加尔各答/德里/勒克瑙）**
  > Importer · Exclusively Import by FASTBALL in India … Distributor · Available in Mumbai, Telangana, Kolkata, Delhi, Lucknow
  > 来源：https://www.splicingmachines.com/fiber-optic-splicing-machine.html（抓取 2026-10-23）
- **KP**：Rishi Kumar Bansal（单据联系人）office@fastball.in 〔PI.zip 单据〕
- **调研后定级**：B（原自动 A）——PI 包成单客户，Simon 标签 gg：gg（已凉）→ B（成交过·慢慢跟进）

### 加厚挖掘（2026-10-23 · 公开平台核查（T29-U18，针对性：只核活跃平台与触达通道））

- **触达通道（公开）**：公开动态平台（监控中，T29-U18）: 官网 fastball.in（WordPress，RSS）；IndiaMART 店铺 indiamart.com/fastball（产品上新最勤）；TradeIndia 店铺；Rishi Kumar Bansal（CEO/业主，个体 GST 07AJJPR5445G1ZX，2021）
- **近况信号**：
  - 2026-10-23 核查：Fastball 在 IndiaMART 挂有「4 Port Industrial Ethernet Switch FBC-204GP」与「20 port Gigabit fiber optic switch」——FBC-204GP 即我方 STC-204GP 的贴牌命名（FBC = Fastball），说明他们把 Saga/HRUI 的工业 4 口直接上架零售；另主营光纤工具（独家进口 Signal Fire AI-5/AI-9 熔接机）、LIU/ODF、PLC 分路器；对口 = 继续供 FBC- 系列小批量
- **Saga 对位结论**：P1 待核型（无标准对应）（20% 档）——成单客户，按实际成交型号续单；贴牌/裸板需求按 OEM 30% 档单独核价

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 成交记录（PI 包 · 自动汇总）

- **Simon 的标签**（PI 包文件夹名）：**gg**　|　买方抬头：Fastball
- **单号** 1 个（2023-10-09 → 2023-10-09）　|　**销售** USD 260　|　**Simon 成本表利润** RMB 553

| 单号 | 日期 | 单据 | 型号 | 数量 | 金额 | 采购（卖方 / RMB） | Simon 成本表（成本 / 收款 / 利润 RMB） |
|---|---|---|---|---|---|---|---|
| STSC20231009002 | 2023-10-09 | CI | — | 80 | USD 260.0 | — | 1810.93 / 2364.41 / 553.48 |

> 口径：同一单号多份文件取 CI > PI（最新修订）> Quotation；Quotation 行不计入销售合计；明细见 `data/pi_orders/销售单据明细.csv`、采购价见 `采购合同明细.csv`；原件在 Release `files-pi_2026-10`。

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：1 封（去 0 / 来 1）　|　**期间**：2023-09-20 → 2023-09-20　|　**最后去信**：—
- **对方邮箱**：office@fastball.in、rishi@fastball.in
- **最后一封来信**：2023-09-20 rishi@fastball.in「Authorised Distributorship - India」：Hi, Greetings for the day ! Since our team underwent with your various products shared from your respective end, proceeding further, Please consider this mail as our official acknowledgement regarding Indian market capturing of Saga Telecom product range. To s

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Authorised Distributorship - India | 2023-09-20 | 2023-09-20 | 1 | 0 | 0 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：成单精选层　|　**自动源**：2 个　|　**数据截至**：2026-10-24T07:26:33Z　|　**最近变化**：2026-10-23T06:51:07Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-1334/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://fastball.in/) | html | HTTP 200 | 2026-10-23T06:51:07Z | 9609 字符；首行：Fastball |
| [indiamart](https://www.indiamart.com/fastball/) | html | HTTP 429 | 2026-10-23T03:05:43Z | IndiaMART 店铺（有 FBC-204GP 4 口工业交换机 = 贴我方 STC-204GP 同款命名；20 口千兆光纤交换机） |

- **人工定期看（登录墙，不自动抓）**：TradeIndia 店铺；GST 07AJJPR5445G1ZX，个体 proprietorship 2021；站点无 RSS（/feed/ 404、?feed=rss2 返回 HTML）: https://fastball.in/

## 联系方式（已有 · 原值照录）

- 邮箱：`office@fastball.in`〔企业邮箱；来源：用户表原值〕
- 电话：`+919871753979`〔电话/WhatsApp 状态未记；原值见来源表〕
- 电话：`+919810987870`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Rishi Kumar Bansal
- 职位（原值）：负责人
- 网站/域名：fastball.in
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Rishi Kumar Bansal | 单据联系人 | office@fastball.in | 调研核实（公开页） | PI.zip 单据 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 补录客户.jsonl#(补录):3 | PI-002 | Fastball | 印度 | Rishi Kumar Bansal | 补录：PI 包成单客户（T29-U8） | 商用 PoE 交换机（2023-10 一单 80 台，USD 260 样品级） | office@fastball.in +91 98717 53979; +91 98109 87870 | 已成单 1 次（STSC20231009002，2023-10-09）；Simon 文件夹标签 gg（已凉）；详见 research/SB-1334.json 负责人 | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-424DGGPM-280W | 24 口 PoE L2+ 走量款 | $134.5 USD EXW（20% 档，SmartByte LT-S8328GP-4GX24GT-S 750 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 据用户表兴趣/备注推断；档位 20%（经销/贸易（德里）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $80.7 USD EXW（20% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：20% 档 $139.9 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），20% 档公式为 $181.2——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W），备选型不进首触。

- **第 1 次**：老客户回访——问上次所购型号的使用情况 + 告知 Marvell 新款（STC-424DGGPM-280W）；只问一个问题：当前在采购的主力型号与月量。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；20% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有成交史，信任与开户成本已付
- **W**：南亚：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STC-424DGGPM-280W 按 20% 档报价，做现供应商的第二货源
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
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：One question, Rishi - the FBC-204GP on IndiaMART

```text
Hi Rishi,

One question: the FBC-204GP listed under Fastball on IndiaMART - is that our STC-204GP (4 x Gigabit PoE+ + 2 x Gigabit uplinks, 65 W) that you are selling on? If yes, the current price is $24.2 USD EXW at distributor tier (MOQ 1, 15-day validity), and I will keep you on the price updates; if no, I will not write again about it. BIS stays on your side.

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

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 A，分数 77）；人工/调研定级 → B

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
