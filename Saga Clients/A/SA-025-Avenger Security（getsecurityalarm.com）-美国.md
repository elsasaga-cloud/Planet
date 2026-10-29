# Avenger Security（getsecurityalarm.com）
**官方名称（调研核实）**：Avenger Security / Security Tekton（Austin & Hutto, Texas）

> **评级 A**　|　美国　|　档案编号 `SA-025`　|　优先级 ★★★　|　状态：有回复·跟进中
>
> **类型**：安防集成/安装商（小型，自装自用采购）（推断）　|　**历史关系**：实质回复 2 次；推送 2 次（2025-06-12 → 2025-09-08）　|　**所在清单**：A已回复、补录、归属补洞　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SA-025
rating: A
rating_auto: A
name_official: "Avenger Security / Security Tekton（Austin & Hutto, Texas）"
score: 84
country: 美国
region: 北美
website: getsecurityalarm.com
type: 安防集成/安装商（小型，自装自用采购）
tier_tags: ["A已回复", "补录", "归属补洞"]
deal: no
replies: 2
followups: 2
first_contact: 2025-06-12
last_contact: 2025-09-08
s_mail: 20 msgs (out 18 / in 2), 2025-01-23 -> 2026-09-08
p1: STC-28DGGPM
price_tier: 25%
research: done
site_snapshot: ok  # 2026-10-21
sources: 2
updated: 2026-10-29
```

## SALES BRIEF（压缩模型）

- **是谁**：德州奥斯汀的员工持股安防监控服务商（商业/住宅报警、消防报警、门禁、云视频监控、UL 中心站监控），服务奥斯汀/休斯敦/达拉斯/圣安东尼奥，<$5M 营收。用户表：A 已回复，2 次实质回复，兴趣商业 PoE，电话 (512) 563-5361。（调研 2026-10-21；表内兴趣：商业PoE；2025-06-12 要 16 口 DIN 千兆交换机价；2025-09-09 要 STI-244GP 价与发货地（「used this PoE in solar configurations, like the overcur）
- **为什么是 A 级**：+30 实质回复 2 次（问价/要资料/问型号等）；+18 在「已回复」名单（A/E Replied）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国；+5 最近活动 2025
- **历史互动**：实质回复 2 次；推送 2 次（2025-06-12 → 2025-09-08）；最近一次客户回复：2025-09-08：Price
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-244GP — 他点名的就是 STI-244GP 这档；安装商 25%；太阳能站点 → 强调 44–57V 宽压 + 过流/DIP；STI-244GP $35 EXW（Alan 2025-09-09 已报；主表 25% 档 $36.6、列表 $49.5——沿用 $35）；STI-0160GE 16 口 DIN 千兆非管理 $100（Alan 2025-05-28 对加拿大 SC-2150 实报；SA-010 2025-02 $105；规则 ㉕ 非管理工业线不用档位价 $95.3）；备选 STI-054GP（4 PoE + 1 GE）$39 更省；群发里他已看到的价：2026-08-10 $170（24 Port PoE Managed = STC-424XGGPM-280W，现价轮 $180）、2025-10-02 $280（10G Enterprise SFP Switch）
- **第一问（只问一个）**：Brandon — picking up your September note on the solar sites: STI-244GP (2 SFP + 4 GbE PoE, 44–57 V DC, DIP, −40 to +75 °C) is $35 EXW; 2 pcs by DHL to Austin lands in about a week — how many solar/off-grid sites are you fitting this season, and shall I send two for the next one?
- **最大未知**：年走量与现供应商
- **下一步**：现在（一封针对性信） A 邮箱 → brandonwadams@gmail.com（抄 brandon@getsecurityalarm.com） 首封前知悉：Elsa 仅 2025-02-28 单发过 1 封「Mini Industrial PoE Switch」，之后没再碰他（第 74 批(m)）；把 09-09 那封补完整：价 + 2 台/10 台 DHL 运费 + 3–5 工作日交期，问太阳能站点数量

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SA-025` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（A 邮箱 2 次真人回复，都从私人 gmail brandonwadams@gmail.com「Avenger Security」发来：2025-06-12 要 16 口 DIN 千兆价、2025-09-09 要 STI-244GP 价与发货地并说「used this PoE in solar configurations」；Alan 09-09 报 $35 后沉默；此后 9 封群发无回）；Elsa 1:1 去信 1 封（2025-02-28「Mini Industrial PoE Switch」；To 仅本户 info@getsecurityalarm.com；Bcc 未逐封读头；同类名单抽读 24 封均无 Bcc；此后再未进 Elsa 任何名单——全箱 `from:e.sagatelecom to:info@getsecurityalarm.com` 仅此 1 条，complete）（第 74 批(m)）** ｜ 类型：奥斯汀安防安装商（Avenger Security / getsecurityalarm.com），太阳能供电站点用工业 PoE ｜ 筛子：2（两次问价） ｜ 停点：第一次问价（06-12）Alan 只回了下载链接 PDF、没在正文给价；第二次（09-09）给了 $35 与「从中国发」后他没再回——小安装商、单次需求量小，$35 + 国际运费对 4 口机不划算是最可能的原因 ｜ 复活：直接写到他的 gmail（公司邮箱 brandon@/info@ 从没回过）：把 4 口与 16 口两款价和运费档位写在正文里，问他这一季有几个太阳能站点，建议 2 台样机 DHL ｜ 通路：US 主攻 ｜ 节奏：一次针对性信 → 再无回则回到季度群发 ｜ 证据：gmail_a a3355bc71b5e758d / 1ac6cb596346a3a9 / 88fd4f417fdf19ba / 2c55cbead61c8075；私人邮箱 2026-10-24 第 70 批并入实体（补录行 AS-补录-2026-10-24-03）
- **现状一句话**：德州奥斯汀的安防安装商 Avenger Security（getsecurityalarm.com；Brandon Walter Adams，Owner，2004 年创立；报警/门禁/视频监控，服务奥斯汀/休斯敦/达拉斯/圣安东尼奥）。他用的是私人 gmail 回信，所以之前被记成「0 来信」——实际两次开口都是问价：2025-06 问 16 口 DIN 千兆（Alan 只给了链接），2025-09 问 2 光 4 PoE 工业机 STI-244GP，并说自己在太阳能配置里用过这类 PoE、喜欢过流保护；Alan 答 $35/pc、从中国 DHL/UPS/FedEx 发、输入 3A max、DC44–57V、带 DIP。之后他没下文，Saga 又群发了 9 封（2025-10 → 2026-09）。
- **对方真实需求（有据）**：太阳能/离网安防站点用的小口数 DIN PoE 交换机（2 SFP + 4 GE PoE，DC 44–57V，过流保护，-40~75℃）；偶尔 16 口 DIN 千兆（车载/工业自动化那封引出的）。单量小（安装商按项目买）。
- **断点 / 为什么停在这里**：两次问价都没形成「价 + 运费 + 交期」一封信：06-12 没给价，09-09 给了价没给运费档位——对美国小安装商，4 口机 $35 之外的 DHL 运费才是决定项。
- **Saga 现在该推什么**：P1 **STI-244GP**（25% 档，STI-244GP $35 EXW（Alan 2025-09-09 已报；主表 25% 档 $36.6、列表 $49.5——沿用 $35）；STI-0160GE 16 口 DIN 千兆非管理 $100（Alan 2025-05-28 对加拿大 SC-2150 实报；SA-010 2025-02 $105；规则 ㉕ 非管理工业线不用档位价 $95.3）；备选 STI-054GP（4 PoE + 1 GE）$39 更省；群发里他已看到的价：2026-08-10 $170（24 Port PoE Managed = STC-424XGGPM-280W，现价轮 $180）、2025-10-02 $280（10G Enterprise SFP Switch））——他点名的就是 STI-244GP 这档；安装商 25%；太阳能站点 → 强调 44–57V 宽压 + 过流/DIP
  - 复购/在买项：06-12 问 16 口 DIN GE 价；09-09 问 STI-244GP 价与发货地
  - 做不了 / 要先核的：运费档位（2 台 / 10 台 DHL 到 Austin）要先查，不然这封信又只剩价
- **下一步（具体）**：现在（一封针对性信）　A 邮箱 → brandonwadams@gmail.com（抄 brandon@getsecurityalarm.com）　首封前知悉：Elsa 仅 2025-02-28 单发过 1 封「Mini Industrial PoE Switch」，之后没再碰他（第 74 批(m)）；把 09-09 那封补完整：价 + 2 台/10 台 DHL 运费 + 3–5 工作日交期，问太阳能站点数量
  - 第一问（只问一个）：Brandon — picking up your September note on the solar sites: STI-244GP (2 SFP + 4 GbE PoE, 44–57 V DC, DIP, −40 to +75 °C) is $35 EXW; 2 pcs by DHL to Austin lands in about a week — how many solar/off-grid sites are you fitting this season, and shall I send two for the next one?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-02-28 | out | Elsa → info@getsecurityalarm.com | Mini Industrial PoE Switch（Elsa 1:1 单发；To 仅本户，非 BCC 批次） | 本户在 Elsa 的 1:1 名单里；未见回复（Elsa 箱 Replied 标签无） | `elsa_1to1` |
| 2025-06-11 | 去 | Saga（群发） | 「16 Port Ethernet Switch」被打开（Mailtrack Opened 标签） | 唯一的互动痕迹 | `ea72575dc36805b9` |
| 2025-06-12 | 来 | Brandon（Avenger Security，brandonwadams@gmail.com） | Alan, Hope all is well, Can you send me the pricing, Let me know（答「16 Port Ethernet Switch」DIN 千兆群发） | 第一次开口就是问价——来自私人 gmail，之前未归属本户 | `gmail_a a3355bc71b5e758d` |
| 2025-06-12 | 去 | Saga（Alan） | Please see attached downlink links which contain full information. Photos, datasheets, user manuals, prices etc.（附 Download Link_Alan.pdf） | 问价只回了链接包、正文没有价——第一次断点 | `gmail_a 1ac6cb596346a3a9` |
| 2025-09-08 | 去 | Saga（群发） | 「Industrial PoE Switch」被打开（Mailtrack Opened 标签） | 唯一的互动痕迹 | `a993a01057d0d553` |
| 2025-09-09 | 来 | Brandon（brandonwadams@gmail.com） | I have used this POE in solar configurations, I like the overcurrent protection. Can you send pricing, Where is the product located, shipped from?（答「Industrial PoE Switch」STI-244GP 群发） | 点明用途（太阳能配置）与在意点（过流保护）+ 两个采购问题（价、发货地）——这是本户最实的一句话 | `gmail_a 88fd4f417fdf19ba` |
| 2025-09-09 | 去 | Saga（Alan） | 1, yes, it is 3A max for input current. For over-current protection, its bigger than this… DIP is also an interesting function. 2, it will be shipped from China via DHL/UPS/FedEx. 3, price is 35usd/pc. STI-244GP: 2*Gigabit SFP+4*10/100/1000M RJ45, PoE af/at, 120W, Unmanaged, Support DIP, DC44V~DC57V (Removable 4 PIN Terminal Block), -40℃ to 75℃, Din mounted, Without optical module, without power adapter | 给了价没给运费档位；此后 Brandon 沉默，Saga 再群发 9 封无回 | `gmail_a 2c55cbead61c8075` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：DHL 2 台/10 台到 Austin 的运费档位（发信前查）；他 2025-09 说「used this PoE in solar configurations」——用的是谁家的（没问）

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **发信窗口（US 全库 2491 封群发的打开标签，对方本地时间；均值 5.4%）**：周三 08–10 点 13.6%（44 封）、周二 08–10 点 11.1%（63 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **本国来询季节（US 全库 53 个「户·月」真人来信）**：8 月 17.0% / 11 月 11.3% / 1 月 11.3%——本户来信太少，按本国节奏排下一步。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 15 封（2025-01-23 → 2026-09-08），打开标签 2 次（近 12 个月 0，最后 2025-09-08）；打开过：「16 Port Ethernet Switch」×1（2025-06-11）、「Industrial PoE Switch」×1（2025-09-08）；从未打开：「Marvell Industrial Alert System」、「8 Port Industrial PoE Switch」、「Marvell Alleycat5 Solution」；**最近连续 9 封没打开**（近 180 天发 3 封 0 打开）→ 群发对这户已失效，停两个月，改一句 1:1 或换收件人。
- **规模与贴牌线索（官网快照 2026-10-21）**：站点地图 97 条 URL；站内可见品牌 2 个（Aruba、Ubiquiti）；社媒：https://www.facebook.com/masterintegrators、https://www.instagram.com/securityprophet/、https://x.com/Get_Security。
- **同国同档参照（US，25% 档、主推线「工业 PoE 非管理」，共 3 户有动静，列前 3）**：SA-060 gofiberx.com（A，同档：回过 4 次（最近 2026-06-05））；SA-058 alphanetcom.com（A，同档：1:1 报过 1 次）；SB-119 wirestar.net（B，同档：1:1 报过 1 次）。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-11-26 感恩节（周四–周日四天基本停摆）；2026-12-24 圣诞–元旦（12-24 → 01-04 多数公司半停） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 进口记录（公开海关数据 · 第 80 批 · 2026-10-27）

> 来源：ImportYeti 整理的 **美国海关（CBP）海运提单**，2015-01 起；只覆盖海运到美国港口的货，**空运 / 快递 / 陆运看不见，欧洲 / 土耳其 / 加拿大按公司查不到**。美国提单**没有货值**，只有到港日 / 发货人 / 重量 / 件数 / 品名 / 估算海运费——所以「金额」一栏给不出，量只能用重量与箱数估。查询日 2026-10-27。

- **查无**：ImportYeti 公司页没有此户（company/avenger-security 404）。美国海运提单库查无（company 页 404）→ 小批量交换机走空运/快递属常态，海运库看不见
- 查无 ≠ 不进口：可能用别的报关主体名、走空运 / 快递、或申请了舱单保密（ImportYeti FAQ）。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-27 查）：**

- `getsecurityalarm.com` → 主机商 cPanel 类邮箱（MX：mx.getsecurityalarm.com.cust.b.hostedemail.com）。主机商附带邮箱（主机商 cPanel 类邮箱）：过滤弱、几乎不丢信，但常是老板自己收、没人代读 → 短、直接、一行型号 + 价格 + 一个问题
- `gmail.com` → Google Workspace（MX：gmail-smtp-in.l.google.com、alt1.gmail-smtp-in.l.google.com、alt2.gmail-smtp-in.l.google.com、alt3.gmail-smtp-in.l.google.com）。Gmail → Gmail 同生态投递最稳；但 Gmail 图片代理会预抓像素 → 「已打开」偏高，别把 open 当成读过；三个发信箱别同一天给这个域发

**假日避让（美国 · 按下一步「现在 → 两周内」窗口 2026-10-29→2026-11-12）：**

- 法定假日：11-11 Veterans Day —— 假日前一个工作日下午、当天、长假后第一个上午都别发

**公司底数 · 第 85 批（USA · BBB 登记（成立 / 注册 / 别名 / 管理层）+ Texas 执照（官网公示 B12519 / B03064001 / ACR-2370373）+ allbiz（TX 备案号 0800828533）+ LinkedIn / RocketReach / Yelp，2026-10-27 查；https://www.bbb.org/us/tx/hutto/profile/security-system-monitors/avenger-security-services-inc-0825-90033586）：**

- 法定名 / 登记号：AVENGER SECURITY SERVICES, INC.（别名 Central Security / GetSecurityAlarm.com / DCS Systems, Inc.） · Texas Filing No. 0800828533 · Texas Private Security License B12519 / B03064001 · Texas Fire Alarm License ACR-2370373 · 状态 **经营中（Yelp 2026-09、LinkedIn 2026-04 活跃）** · 成立 业务始于 2005-05-27（BBB；LinkedIn 2004 / Yelp 2001 口径）；Business Incorporated 2007-06-12 · Corporation（Texas）· 独资（Owner Brandon W. Adams）
- 行业码 / 经营范围：德州持牌报警 / 消防报警 / 门禁 / 视频监控安装与监控服务商（RMR 月费模式）；兼「批发其他机械设备」登记；门店 Hutto（总部）、Round Rock、College Station、San Antonio（安装合伙人 Jay Phipps）
- 注册地址：501 West Creekbend Cove, Hutto, TX 78634
- 规模档：微型（LinkedIn 11–50 为渠道口径；实际老板 + 安装技师）
- 账目：私人公司不公开；allbiz 估 $500k；Texas 特许税申报 5-15
- 高管：Brandon Walter ADAMS — Founding Owner / Principal（UT Austin 土木工程；德州私人保安 + 消防报警双执照持有人）= 研究档 KP → **老板 = 联系人**
- 高管：Jay PHIPPS — Owner and Installer（San Antonio，合伙 / 加盟安装商）
- 控制人 / 股东：Brandon W. Adams
- 曾用名：DCS Systems, Inc.（BBB 别名）
- **这意味着什么：**
  - **老板 = 联系人，微型报警安装商（RMR 月费模式）**：买交换机是给自己安装的监控 / 门禁项目配套，每单 1–5 台 → 集成 25% 档但量极小；推即插即用 PoE（STC-028GP / STC-228GP），不推管理型
  - 德州持牌报警公司对「UL Listed 监控中心」很在意（Yelp 自述），但那是监控中心资质不是交换机；我们不提 UL，只给 FCC / CE / RoHS
  - 报价零售化：按 1 台 / 5 台 / 10 台三档 + 百运网 DAP 小包裹含运费价，T/T 100% 预付或 PayPal（由 Simon 定）；老板本人回信快、决策快
  - 老板 2000 年起另有「Corporate America RMR 营销」业务（LinkedIn 自述花 $10M 做直邮），不是设备买家主业 → 长期价值低，群发节奏即可

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Avenger Security（getsecurityalarm.com） | 事实（用户表） |
| 国家 | 美国 | 事实（用户表）|
| 网站/域名 | getsecurityalarm.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 安防集成/安装商（小型，自装自用采购） | 推断（据兴趣/备注关键词） |
| 联系人 | Brandon Walter Adams / Owner / Brandon Walter Adams | 事实（用户表） |
| 来源（From） | 谷歌 / 补录：A 邮箱真人回复来自私人 gmail，原实体只有公司邮箱（第 70 批归属补洞） | 事实（用户表） |
| 兴趣（Interested in） | 商业PoE / 2025-06-12 要 16 口 DIN 千兆交换机价；2025-09-09 要 STI-244GP 价与发货地（「used this PoE in solar configurations, like the overcurrent protection」） | 事实（用户表） |
| 用户备注（Remark） | C: (512) 563-5361 / 同一实体 SA-025；本行只为把 brandonwadams@gmail.com 并入该实体邮箱，便于往来归属 | 事实（用户表） |
| 用户分档（Category） | 安防安装商（奥斯汀） | 事实（用户表） |
| 所在清单 | A已回复、补录、归属补洞 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：德州奥斯汀的员工持股安防监控服务商（商业/住宅报警、消防报警、门禁、云视频监控、UL 中心站监控），服务奥斯汀/休斯敦/达拉斯/圣安东尼奥，<$5M 营收。用户表：A 已回复，2 次实质回复，兴趣商业 PoE，电话 (512) 563-5361。
- **类型**：安防集成/安装商（小型，自装自用采购）
- **规模**：<$5M（ZoomInfo）
- **在卖/在用品牌**：Eagle Eye Networks, Brivo, Alula, Honeywell
- **【官网】业务与联系方式**
  > Austin commercial security: access control, fire alarms, video surveillance, and UL-listed 24/7 monitoring … email: info@getsecurityalarm.com
  > 来源：https://getsecurityalarm.com/（抓取 2026-10-21）
- **【官网（关联站）】员工持股，双牌照，电话与用户表一致**
  > Learn about Avenger Security, Austin’s employee-owned security monitoring company. Dual licensed for private security & fire alarm. … 512-563-5361 … Email: info@getsecurityalarm.com
  > 来源：https://securitytekton.com/pages/about-us（抓取 2026-10-21）
- **【官网】公司背景 / 执照 / 地址 / 电话 / 创始人**
  > Avenger Security is a private, employee-owned and operated security monitoring service provider based in Austin, Texas. Since 2004 … Texas Private Security License: B12519 & B03064001 … Texas Fire Alarm License: ACR 2370373 … Established: 2004 by Brandon Walter Adams … Address: 501 West Creekbend Cove, Hutto, Texas 78634 … Phone: 512-610-2698
  > 来源：https://securitytekton.com/pages/about-us（抓取 2026-10-21）
- **【官网】云视频 = Eagle Eye Networks + PoE IP 摄像机**
  > Avenger Security delivers professional cloud video surveillance powered by Eagle Eye Networks. Replace legacy DVR/NVR limitations with a secure, flexible, and scalable cloud VMS that supports leading PoE IP cameras and many existing analog systems via bridge.
  > 来源：https://securitytekton.com/pages/video-surveillance-austin（抓取 2026-10-21）
- **【官网】门禁 = Brivo OnAir 与 Eagle Eye 联动**
  > Avenger Security integrates Brivo OnAir with Eagle Eye Networks cloud video surveillance to attach door video clips to activity logs
  > 来源：https://securitytekton.com/pages/access-control-service（抓取 2026-10-21）
- **KP**：—（总机 → 实际收件人 = Owner Brandon Walter Adams（TX 登记 0800828533，2007-05；微型报警装机商）（第 85 批 官方登记核实 2026-10-27））info@getsecurityalarm.com +1 512-563-5361〔https://securitytekton.com/pages/about-us〕
- **KP**：Brandon Walter Adams（Founder / Owner（2004 创立，官网 About））—（未公开） +1 512-610-2698（公司）〔https://securitytekton.com/pages/about-us〕
- 备注：A 维持（美国本土集成商 + 2 次实质回复），但单量小（自装项目用 8/16 口 PoE）；P1 = STC-28DGGPM，25% 集成商档；注意 UL：仅报 CE/FCC（Saga 无 UL）。

### 加厚挖掘（2026-10-21 · 深挖 v2（官网 securitytekton.com + 目录核对））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | AVENGER SECURITY SERVICES INC（Texas 0800828533；Hutto TX；Owner Brandon Walter Adams） |
| 成立 | 2004（创始人 Brandon Walter Adams；LinkedIn/Yelp 口径 2010） |
| 总部/地址 | 501 West Creekbend Cove, Hutto, TX 78634（+1 512-610-2698）；休斯敦分部 11200 Broadway St Ste 2743, Pearland TX 77584（+1 281-954-3400） |
| 人数 | 1–5（第 85 批 官方登记核实 2026-10-27） |
| 营收 | <$5M（ZoomInfo） |
| 其他 | 员工持股；德州双证（私人安防 B12519 & B03064001；消防报警 ACR 2370373）；云视频 = Eagle Eye Networks（PoE IP 摄像机 + 旧模拟桥接），门禁 = Brivo OnAir，报警 Alula/Honeywell Vista；「无长期合同、无信用审查」；官网 securitytekton.com（2025-10 仍更新）与 getsecurityalarm.com / avengersecurityhouston.com 并行 |

- **业务线**：商业/住宅入侵报警与 UL 中心站监控；消防报警；门禁；云视频监控（IP 摄像机 → 需 PoE 接入）；云视频监控安装（Eagle Eye Networks，PoE IP 摄像机）；云门禁（Brivo OnAir，$10–20/门/月）；盗警/消防报警 + UL 中心站监控（消防部分守界：不供生命安全链路设备）

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| （安装商自用） | 商业 PoE 交换机（用户表兴趣） | 摄像机/门禁点位供电 | STC-28DGGPM | （本地 Clients/ 表格，无公开 URL）（用户表） |

- **触达通道（公开）**：网站: https://securitytekton.com/；直邮: brandon@getsecurityalarm.com / info@getsecurityalarm.com（用户表）；电话: +1 512-610-2698（奥斯汀）/ +1 281-954-3400（休斯敦）；LinkedIn: https://www.linkedin.com/company/central-security（322 followers）
- **近况信号**：
  - 用户表：A 已回复，2 次实质回复，兴趣商业 PoE
  - Eagle Eye 云 VMS 模式每站点仍需本地 PoE 交换机（桥接器 + 摄像机）——8/24 口 PoE 为标配耗材；两城运营、2025-10 仍在发博客（活跃）
- **风险/边界**：安装商自用量小（每项目 1–3 台）；美国商业楼宇低压安装常要求 UL 列名设备（Saga 无 UL）→ 只能供非强制场景；消防报警部分守界（生命安全）；消防报警/UL 监控为其业务一部分——Saga 只供摄像机/门禁侧 PoE 交换机，不进入消防链路（守界）
- **Saga 对位结论**：P1 STC-28DGGPM（25% 档）——安装商每站点 8–24 口 PoE 自用：STC-28DGGPM（8 PoE+2 SFP）为主，STC-424DGGPM-280W 为大站点；集成商 25% 档
- **邮件切入句（英文）**：For the Eagle Eye bridge and PoE camera drops you install around Austin and Houston, the Marvell-based 8-port PoE+ with 2 SFP uplinks at EXW cost is the unit I am quoting, 24-port for the larger sites.

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://securitytekton.com/　语言：en　站点地图 URL 数：97
- **标题**：Avenger Security / Austin, TX — Access Control, Fire & Monitoring
- **描述**：Austin commercial security: access control, fire alarms, video surveillance, and UL-listed 24/7 monitoring. No long-term contracts. Local install & service.
- **首页栏目**：Country/region / Item added to your cart / Commercial Security & Fire Alarm Services in Austin & Central Texas / Security & Life-Safety Services for Your Building / Access Control / Commercial Fire Alarms / Burglar Alarms / Video Surveillance
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：access control 48、surveillance 44、camera 14、wireless 10、cable 8、integrator 3、industrial 1、wholesale 1
- **站内出现的品牌**：Aruba, Ubiquiti　（「（！）」= Saga 自家/供应商品牌已在其站内出现）
- **站内型号串**（正则抽取，含非交换机）：TL880LT, ANCP3005Q, PG9984P, PG9936, DW-433, PG9303, HS2064, B-BUC3-37-SF25, HS2032, ACR-2370373
- **站内公开邮箱**：brandon@getsecurityalarm.com, info@getsecurityalarm.com
- **社媒**：https://www.facebook.com/masterintegrators, https://www.instagram.com/securityprophet/, https://x.com/Get_Security
- **产品类页面**：https://securitytekton.com/sitemap_products_1.xml?from=6779095548081&amp;to=9176524095665
- **已抓子页**：[Collections – Avenger Security](https://securitytekton.com/collections)；[Security System Products & Equipment / Avenger Security](https://securitytekton.com/collections/all)；[About Avenger Security / Austin TX Security Integrator](https://securitytekton.com/pages/about-us)；[Contact Avenger Security / Austin TX Security & Fire](https://securitytekton.com/pages/contact-us)；[Austin Security Company & Texas Service Areas / Avenger – Av](https://securitytekton.com/pages/store-locator)；[Contact information – Avenger Security](https://securitytekton.com/policies/contact-information)
- 首页正文摘录：Skip to content 5 Year Workmanship Warranty No Multi-Year Alarm Contract Commercial Burglar Alarm Monitoring Cloud Managed Access Control Full Service Video Surveillance Austin & Central Texas Service Fire Alarm Monitoring & Inspections Alarm System Permits LOCATIONS ACCESS CONTROL FIRE ALARM BURGLAR ALARM VIDEO SURVEILLANCE PRODUCTS SEARCH Country/region United States / USD $ Search Canada USD $ United States USD $ 
- 数据文件：`data/saga_clients/site_snapshots/SA-025.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 2 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-06-12 | 2025.6.12 | 16电 | Price | A |  | A Replied 09.04.xlsx#5 |
| 2025-09-08 | 2025.9.8 | 24PoE | Price | A |  | A Replied 09.04.xlsx#5 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：20 封（去 18 / 来 2）　|　**期间**：2025-01-23 → 2026-09-08　|　**最后去信**：2026-09-08
- **对方邮箱**：brandon@getsecurityalarm.com、brandonwadams@gmail.com、info@getsecurityalarm.com
- **最后一封来信**：2025-09-09 brandonwadams@gmail.com「Re: Industrial PoE Switch」：Alan, I have used this POE in solar configurations, I like the overcurrent protection Can you send pricing, Where is the product located, shipped from? Let me know, Respectfully Submitted, On Mon, Sep 8, 2025 at 10:00 AM Alan from Saga Telecom < a.sagatelecom@

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 16 Port Industrial PoE Switch | 2026-09-08 | 2026-09-08 | 0 | 1 | 1 |
| 24 Port PoE Managed Switch | 2026-08-10 | 2026-08-10 | 0 | 1 | 1 |
| Saga Q3 Product Links | 2026-07-20 | 2026-07-20 | 0 | 1 | 2 |
| Updated Ethernet Switches Links | 2026-03-30 | 2026-03-30 | 0 | 1 | 0 |
| Marvell Industrial Alert System | 2025-12-26 | 2025-12-26 | 0 | 1 | 1 |
| Optional Marvell Chipset Solutions | 2025-12-09 | 2025-12-09 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-13 | 2025-11-13 | 0 | 1 | 1 |
| 90W PoE Managed Switch | 2025-10-24 | 2025-10-24 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-02 | 2025-10-02 | 0 | 1 | 1 |
| Industrial PoE Switch | 2025-09-08 | 2025-09-09 | 1 | 2 | 4 |
| Marvell Industrial Alert System | 2025-08-11 | 2025-08-11 | 0 | 1 | 1 |
| 16 Port Ethernet Switch | 2025-06-11 | 2025-07-14 | 1 | 3 | 6 |
| …共 15 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：A 级面层　|　**自动源**：2 个　|　**数据截至**：2026-10-28T08:44:48Z　|　**最近变化**：2026-10-28T08:44:48Z
- **最近变化摘要**：2026-10-28 home：内容变化：+0 −1 行
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SA-025/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://securitytekton.com/) | html | HTTP 200 | 2026-10-28T08:44:48Z | 13050 字符；首行：Avenger Security \| Austin, TX — Access Control, Fire & Monitoring |
| [sitemap](https://securitytekton.com/sitemap.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |

- **人工定期看（登录墙，不自动抓）**：X/Twitter: https://x.com/Get_Security；Facebook: https://www.facebook.com/masterintegrators；Instagram: https://www.instagram.com/securityprophet/

## 联系方式（已有 · 原值照录）

- 邮箱：`info@getsecurityalarm.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`brandon@getsecurityalarm.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`brandonwadams@gmail.com`〔免费邮箱；来源：用户表原值〕
- 电话：`+5125635361`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Brandon Walter Adams / Owner
- 联系人（原值）：Brandon Walter Adams
- 职位（原值）：Owner
- 网站/域名：getsecurityalarm.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| — | 总机 → 实际收件人 = Owner Brandon Walter Adams（TX 登记 0800828533，2007-05；微型报警装机商）（第 85 批 官方登记核实 2026-10-27） | info@getsecurityalarm.com / +1 512-563-5361 | 调研核实（公开页） | https://securitytekton.com/pages/about-us |
| Brandon Walter Adams | Founder / Owner（2004 创立，官网 About） | —（未公开） / +1 512-610-2698（公司） | 调研核实（公开页） | https://securitytekton.com/pages/about-us |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:getsecurityalarm.com`, `e:brandon@getsecurityalarm.com`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A Replied 09.04.xlsx#总表:6 | 5 | https://getsecurityalarm.com/products/8-PoE-port-switch-with-2-port-uplink?variant=42832283500721&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&srsltid=AfmBOoqZe3XZl0SDYPw5y_7Z7_SClJ6xLf5U2GwEua_nCeEPWR5x4JC_jLU | 美国 | Brandon Walter Adams<br>Owner | 谷歌 | 商业PoE | info@getsecurityalarm.com<br>brandon@getsecurityalarm.com | C: (512) 563-5361 | 2 条 |
| 补录客户.jsonl#(补录):17 | AS-补录-2026-10-24-03 | Avenger Security（getsecurityalarm.com） | 美国 | Brandon Walter Adams | 补录：A 邮箱真人回复来自私人 gmail，原实体只有公司邮箱（第 70 批归属补洞） | 2025-06-12 要 16 口 DIN 千兆交换机价；2025-09-09 要 STI-244GP 价与发货地（「used this PoE in solar configurations, like the overcurrent protection」） | brandonwadams@gmail.com; brandon@getsecurityalarm.com https://getsecurityalarm.com | 同一实体 SA-025；本行只为把 brandonwadams@gmail.com 并入该实体邮箱，便于往来归属 Owner | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：安装商每站点 8–24 口 PoE 自用：STC-28DGGPM（8 PoE+2 SFP）为主，STC-424DGGPM-280W 为大站点；集成商 25% 档 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（安防集成/安装商（小型，自装自用采购）） |
| 备选2 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STC-28DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 2 次实质回复（对方认识我们）；北美主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STC-28DGGPM 按 25% 档报价，做现供应商的第二货源；规模（调研）：<$5M（ZoomInfo）
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
| 商业资格结论 | **技术上合格 / 商业上有互动证据（成交或实质回复或面谈）→ 值得长期跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: Industrial PoE Switch — the solar-site switch, with price and shipping this time

```text
Hi Brandon,

Last September you asked about the DIN-rail PoE switch for your solar configurations and I only half-answered, so here is the whole thing in one place.

STI-244GP — 2 x gigabit SFP + 4 x gigabit PoE+ (120 W), 44–57 V DC input on a removable terminal block, over-current protection, DIP switch, −40 to +75 °C, DIN mount: $35 USD EXW per unit.
Shipping: from China by DHL/UPS/FedEx, about a week door to door to Austin; I will put the exact freight for 2 pcs and for 10 pcs on the quote.
If you also still want the 16-port DIN gigabit switch you asked about in June: $100 USD EXW (unmanaged, 12–58 V DC).

Prices valid 15 days; CE/FCC/RoHS; 3-year warranty on the industrial units.

One question: how many solar or off-grid sites are you fitting this season? If there is one coming up, I will send two units so you can put one on the bench and one on a site.

Thank you.
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

- **2026-11-12**（14 天）：无回复 → 换通道再试一次；仍无 → 降 B。有任何回复 → 当即更新 research JSON 并重渲染。

## 变更日志

- 2026-10-29：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 A，分数 84）

---

*建档日期：2026-10-29　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
