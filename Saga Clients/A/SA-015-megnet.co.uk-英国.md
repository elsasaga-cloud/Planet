# megnet.co.uk
**官方名称（调研核实）**：Megnet Limited（London）

> **评级 A**　|　英国　|　档案编号 `SA-015`　|　优先级 ★★★　|　状态：有回复·跟进中
>
> **类型**：分销商 + 自有品牌（Chimera，OEM 采购）（推断）　|　**历史关系**：实质回复 1 次；推送 13 次（2025-02-19 → 2025-12-29）　|　**所在清单**：S重点　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SA-015
rating: A
rating_auto: A
name_official: "Megnet Limited（London）"
score: 94
country: 英国
region: 欧洲
website: megnet.co.uk
type: 分销商 + 自有品牌（Chimera，OEM 采购）
tier_tags: ["S重点"]
deal: no
replies: 1
followups: 13
first_contact: 2025-02-19
last_contact: 2025-12-29
s_mail: 26 msgs (out 22 / in 4), 2024-12-23 -> 2026-09-08
p1: STI-110GE
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-21
sources: 1
updated: 2026-10-29
```

## SALES BRIEF（压缩模型）

- **是谁**：英国伦敦的兼容光模块/网络配件分销商（2003 年起，11–50 人），自有品牌 Chimera（MSA 兼容光模块、DAC/AOC、MC、交换机），供应全球经销商、分销商和制造商，宣称可触达 400 万+ 产品。用户表：S 重点，自己的品牌、有人卖他们的，MC/SFP/AOC 等较多，1 次实质回复。（调研 2026-10-21；表内兴趣：自己的品牌 有人卖他们的 MC SFP AOC等较多）
- **为什么是 A 级**：+22 实质回复 1 次；+25 在 Simon 的 S 重点名单；+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+2 兴趣仅 MC/SFP/配件（边缘品类）；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/英国；+5 最近活动 2025；+5 跟进表最近平台标记 S
- **历史互动**：实质回复 1 次；推送 13 次（2025-02-19 → 2025-12-29）；最近一次客户回复：1.16：5个商业24 48口
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-424DGGPM-280W / STC-448XGGPM（24/48 PoE+ + 10G 上联，Voice VLAN since 7.4.0） — J2：功能缺口已闭合是最硬的复活理由；一句话即可。已打开的主题（8/22 封有打开记录）：「24 Port Fiber Switch」(2025-08-27)、「Re: Price and lead time」(2025-12-01)、「Re: Price and lead time」(2025-12-02)、「Firmware 7.5 L2+ Feature Update」(2026-06-22) → 读者兴趣偏「PoE 接入」；当前 P1 属「10G 汇聚/L3」，下一封按「PoE 接入」给，不按 P1｜已发资料（勿重发）：STC-448XGGPM(2025-01-18)、Marvell Based CLI Manual(2025-01-18)、Marvell Based Web Manual(2025-01-18)、Saga Software Function List-release 7.(2025-03-19)、Product Link_2026Q2(2026-03-02)、Saga Feature List_7.5.x_L2+(2026-06-22)；还没给过：Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）；按 20% 分销档（若贴 Chimera 标 → 30%）；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2026-07-20 $1500（24 Port 10G SFP+ Switch）、2026-09-08 $170（24 Port PoE Managed Switch）；**第 63 批基准统一（规则 ㉕）**：STC-424XGGPM-280W 由列表价 $198 改为群发现价 $180（他 2026-09-08 收到的群发是 $170，信里点明）；STC-448XGGPM 由列表价 $369 改为 20% 档 $335.4（第 66 批全量复核发现他其实收过 2025-01-16 的 $300 轮——信里已加一句「老汇率」说明；Simon 愿意的话可按 $300 兑现，毛利 7%）。$170 若 Simon 愿意兑现，毛利只剩 12.6%；群发里他已看到的价（续，第 66 批全量复核）：2025-01-16 $300（48 Port PoE Managed Switch）、2025-08-27 $240（24 Port Fiber Switch）、2025-10-29 $280（10G Enterprise SFP Switch）
- **第一问（只问一个）**：Voice VLAN is now in firmware 7.4+/7.5 on the AC5 24/48-port PoE+ models — is that tender (or a similar one) still open?
- **最大未知**：年走量与现供应商
- **下一步**：2026-11 S 邮箱 → jitendra@megnet.co.uk（招标）+ nasim@megnet.co.uk（注入器） 给 Jitendra 一句「Voice VLAN 已上线」+ 问招标是否还开；给 Nasim 一句问测试单

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SA-015` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未绑定（两次具体询价都止于 Saga 答复之后；Elsa 箱：`to:.uk` 穷举 34 条（2026-10-25，锚批 Bcc 头已读）未见 megnet.co.uk → Elsa 箱从未发过本户，往来只在 S/A 箱（去 22 / 来 4）（第 74 批(f)））** ｜ 类型：英国光模块/配件分销 + 自有品牌 Chimera——第三档分销 + 贴牌；Jitendra（产品）/ Nasim（运营经理） ｜ 筛子：2（2025-01-16 招标规格 24/48 口 PoE+ L2；2025-12-01 60W 注入器测试单） ｜ 停点：① 2025-01 规格缺 Voice VLAN（Simon：3 月才有）→ 无下文；② 2025-12-02 注入器 15 USD/pc 报价后无回音 ｜ 复活：Voice VLAN 已随固件 7.4.0 上线（AC5；7.5 再加 IPv6/PIM-SM）→ 招标项可重答；注入器一句话问测试单 ｜ 通路：UK（UKCA 有） ｜ 节奏：2024-12 → 2026-09 去信 22 封；最后来信 2025-12-01 ｜ 证据：k=188c2faf926a981d / d0cedc0a81dda002 / d825f54e656a802d / 9e11d7829cad23f3 / c006113d9ba7a08c
- **现状一句话**：Megnet 两次来的都是真需求：2025-01 Jitendra 发来 5 项招标规格（24/48 口 PoE+、2×10G SFP+、802.1q/LACP/IPv6/Voice VLAN/SNMPv3/SSHv2），Simon 答「item 3 没有可开发，其余 4 项缺 Voice VLAN，3 月就绪」，对方没再回；2025-12 Nasim 要 HT2500-PSE-BT60 60W 注入器测试单价，Simon 次日报 15 USD/pc（3–5 天交期），对方没再回。Voice VLAN 现已在 7.4.0 固件里。
- **对方真实需求（有据）**：招标型 L2 接入 PoE+ 交换机（24/48 口 + 10G 上联，Voice VLAN/SNMPv3/SSHv2/IPv6）；60W PoE++ 单口注入器。
- **断点 / 为什么停在这里**：第一次是功能缺口（现已补齐，但没人告诉他）；第二次是测试单无下文（15 USD 的东西不值得追，但一句话值）。
- **Saga 现在该推什么**：P1 **STC-424DGGPM-280W / STC-448XGGPM（24/48 PoE+ + 10G 上联，Voice VLAN since 7.4.0）**（20% 档，按 20% 分销档（若贴 Chimera 标 → 30%）；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2026-07-20 $1500（24 Port 10G SFP+ Switch）、2026-09-08 $170（24 Port PoE Managed Switch）；**第 63 批基准统一（规则 ㉕）**：STC-424XGGPM-280W 由列表价 $198 改为群发现价 $180（他 2026-09-08 收到的群发是 $170，信里点明）；STC-448XGGPM 由列表价 $369 改为 20% 档 $335.4（第 66 批全量复核发现他其实收过 2025-01-16 的 $300 轮——信里已加一句「老汇率」说明；Simon 愿意的话可按 $300 兑现，毛利 7%）。$170 若 Simon 愿意兑现，毛利只剩 12.6%；群发里他已看到的价（续，第 66 批全量复核）：2025-01-16 $300（48 Port PoE Managed Switch）、2025-08-27 $240（24 Port Fiber Switch）、2025-10-29 $280（10G Enterprise SFP Switch））——J2：功能缺口已闭合是最硬的复活理由；一句话即可。已打开的主题（8/22 封有打开记录）：「24 Port Fiber Switch」(2025-08-27)、「Re: Price and lead time」(2025-12-01)、「Re: Price and lead time」(2025-12-02)、「Firmware 7.5 L2+ Feature Update」(2026-06-22) → 读者兴趣偏「PoE 接入」；当前 P1 属「10G 汇聚/L3」，下一封按「PoE 接入」给，不按 P1｜已发资料（勿重发）：STC-448XGGPM(2025-01-18)、Marvell Based CLI Manual(2025-01-18)、Marvell Based Web Manual(2025-01-18)、Saga Software Function List-release 7.(2025-03-19)、Product Link_2026Q2(2026-03-02)、Saga Feature List_7.5.x_L2+(2026-06-22)；还没给过：Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）
  - 做不了 / 要先核的：7.4/7.5 是否同时满足 SNMPv3 + SSHv2 + IPv6 全项——按 7.5 特性表核一遍再说
- **下一步（具体）**：2026-11　S 邮箱 → jitendra@megnet.co.uk（招标）+ nasim@megnet.co.uk（注入器）　给 Jitendra 一句「Voice VLAN 已上线」+ 问招标是否还开；给 Nasim 一句问测试单
  - 第一问（只问一个）：Voice VLAN is now in firmware 7.4+/7.5 on the AC5 24/48-port PoE+ models — is that tender (or a similar one) still open?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-01-16 | 来 | Jitendra | Item 1 - Level 2 access switch 24 ports Gigabit PoE+… minimum 2 ports UpLink 10Gbps SFP+… 802.1q, LACP, IPv6, Voice VLAN, SNMPv3 and SSHv2, spanning tree, DHCP | 招标规格 | `188c2faf926a981d` |
| 2025-01-18 | 去 | Simon | item 3 is not available, but we can develop it. For the other 4 items, Voice Vlan is not available, but its being developed and will be ready on March. | 功能缺口 | `d0cedc0a81dda002` |
| 2025-08-27 | 内 | Gmail 退信（S 邮箱） | rajiv@megnet.co.uk 永久退信：554 5.7.1 <rajiv@megnet.co.uk>: Relay access denied | 该地址已失效——群发名单与 next_move 都不要再用它；若是具名 KP，多半已离职 | `gmail_s 96c81bffd7353dcd` |
| 2025-08-27 | 内 | Gmail 退信（S 邮箱） | purchasing@megnet.co.uk 永久退信：554 5.7.1 <purchasing@megnet.co.uk>: Relay access denied | 该地址已失效——群发名单与 next_move 都不要再用它；若是具名 KP，多半已离职 | `gmail_s 154c349e1af1c4db` |
| 2025-08-27 | 内 | Gmail 退信（S 邮箱） | becca@megnet.co.uk 永久退信：554 5.7.1 <becca@megnet.co.uk>: Relay access denied | 该地址已失效——群发名单与 next_move 都不要再用它；若是具名 KP，多半已离职 | `gmail_s e58d6e9a2e344dc9` |
| 2025-12-01 | 来 | Nasim Chaudhari（Operations Manager） | HT2500-PSE-BT60 – 60W PoE++ Single-Port Injector This will be a test unit, and if it works on the customer's end, we will proceed with a bulk order. | 第二次需求 | `d825f54e656a802d` |
| 2025-12-02 | 去 | Simon | 15Usd/pc Metal shell, 1G/2.5G speed, AC100-240V in; POWER+PSE；802.3af/at/BT MAX65W… Production time: 3~5 working days | 报价 | `c006113d9ba7a08c` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：Voice VLAN 在 7.4.0 的证据来自 SmartByte 固件说明（`docs/smartbyte/新闻与固件说明_2026-10-20.md`）——是否覆盖 Megnet 要的 24/48 口具体型号，报前核

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **时机与节律**：真人来信 3 封（2025-01-16 → 2025-12-01）；多在 12 月（2）；对方本地时间中位 11:12（= 北京时间 19:12）；周一最多（2）；**他们回信中位 0.8 小时**（2 次，100% 在 24 小时内）；我方回信中位 18.1 小时（3 次）。
- **发信窗口（GB 全库 1094 封群发的打开标签，对方本地时间；均值 5.0%）**：周四 12–14 点 11.9%（42 封）、周二 14–16 点 7.8%（103 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 18 封（2024-12-23 → 2026-09-08），打开标签 4 次（近 12 个月 1，最后 2026-06-22）；打开过：「48 Port PoE Managed Switch」×1（2025-01-16）、「90W PoE Managed Switch」×1（2025-02-19）、「24 Port Fiber Switch」×1（2025-08-27）、「Firmware 7.5 L2+ Feature Update」×1（2026-06-22）；从未打开：「8 Port Industrial PoE Switch」、「Marvell Software Function List」、「Managed Optical Bypass Switch」；近 180 天发 3 封、打开 1 次 → 还在读，主题沿着打开过的那类走。
- **报价轨迹**（S/A 去信里「价 + 型号/描述同句」：1:1 1 条 + 个性化群发价 5 条，2025-01-16 → 2026-09-08；「今天」= 价格主表 2026-10-17 汇率、20% 档、不高于 2026-06 列表价；只列每个型号/描述最近一次，最多 8 行）：

  | 日期 | 型号 / 原句 | 当时 | 今天应报 | 变化 | 性质 | 主题 | 消息 key |
  |---|---|---|---|---|---|---|---|
  | 2026-09-08 | 「Price: 170USD/PC」 | $170 | —（原句无型号） | — | 群发价 | 24 Port PoE Managed Switch | `690f0845232f4568` |
  | 2026-07-20 | 「Price: 1500USD/PC」 | $1500 | —（原句无型号） | — | 群发价 | 24 Port 10G SFP+ Switch | `e4a47cd229bec118` |
  | 2025-12-02 | 「15Usd/pc」 | $15 | —（原句无型号） | — | 1:1 | Price and lead time | `c006113d9ba7a08c` |
  | 2025-10-29 | 「It is a price-competitive aggregation switch(280usd/pc)」 | $280 | —（原句无型号） | — | 群发价 | 10G Enterprise SFP Switch | `69b59336b4834456` |
  | 2025-08-27 | 「Price: 240usd/pc」 | $240 | —（原句无型号） | — | 群发价 | 24 Port Fiber Switch | `243ec12cb648c9fa` |
  | 2025-01-16 | 「Price is very competitive, 300usd/pc」 | $300 | —（原句无型号） | — | 群发价 | 48 Port PoE Managed Switch | `1276c8432cfb0d22` |

  「个性化群发价」= 同一句价发给 ≥5 家的信（Simon 的手工群发），对方未必读过，但它就是对方邮箱里躺着的「上次报价」。
- **规模与贴牌线索（官网快照 2026-10-21）**：站点地图 1165 条 URL（≥500 = 大目录 / 网店体量）；站内可见品牌 1 个（Cisco）；社媒：https://twitter.com/MegnetLtd、https://twitter.com/intent/tweet?text=https://megnet.co.uk/megnet-solution/industrial-park-video-surveillance-solution/、https://twitter.com/intent/tweet?text=https://megnet.co.uk/megnet-solution/large-shopping-mall-wireless-network-solution/。
- **写信的人（来信签名机械抽取）**：Nasim Chaudhari — Operations Manager（nasim@megnet.co.uk，2 封，2025-12-01 → 2025-12-01）；Jitendra Sain — Assistant Manager - Operations（jitendra@megnet.co.uk，1 封，2025-01-16 → 2025-01-16）。
- **他们嘴里的词（3 封来信、去引用后 13,376 字符的词频）**：话题（次数，最近一次）：PoE ×16（2025-12-01）、10G ×10（2025-01-16）、管理型 / L2+ / L3 ×5（2025-01-16）、价格 / 折扣 ×1（2025-12-01）、MOQ / 交期 ×1（2025-12-01）、认证 ×1（2025-12-01）。
- **渠道反应**：S 箱（Simon） 去 21（1:1 4 / 群发 17）回 3，最近回 2025-12-01；A 箱（Alan） 去 1（1:1 0 / 群发 1）回 0，从未回 → 只对 S 箱 Simon 有反应，下一封别换箱。
- **最后一球**：1:1 对话 2 段，最长一段 4 封 / 跨 0 天（2025-12-01 → 2025-12-02，「Price and lead time」）；最后一句是我们说的（2025-12-02，328 天前，「Re: Price and lead time」，`c006113d9ba7a08c`）→ 球在对方手里。
- **同国同档参照（GB，20% 档、主推线「商用 10G PoE 管理型」，共 2 户有动静，列前 3）**：SB-160 linx-com.com（B，同档：回过 5 次（最近 2025-05-15））；SB-905 TELTRONIX | BRITICOM（B，同档同线：回过 2 次（最近 2025-07-07））。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-12-24 圣诞–元旦（12-24 → 01-04；Boxing Day 12-28 补休） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 进口记录（公开海关数据 · 第 81 批 · 2026-10-27）

> 来源：**HMRC Find UK Traders（英国官方）**。英国官方数据：2016 年起非欧盟来源、2022 年起含欧盟来源的进口，按「注册公司名 × 8 位商品编码 × 月份」公示；没有供应商、数量、金额；部分公司因保密被剔除。 查询日 2026-10-27。

- 报关主体 **MEGNET LTD（20 Mortlake High St, London SW14 8JN）**；最近记录 **2025-10（85176200）**；[来源页](https://www.uktradeinfo.com/traders/megnet-ltd-69190)
- HMRC 进口商名录共 **212 条「商品编码 × 年」行**（搜索页 5 页），从螺纹件 / 梯子 / 打印机到 8471 电脑整机、8504 电源、8517 全系列——典型 IT 经销 / 现货商画像，什么都进。
- **8517 62 00（交换 / 路由 / 数据传输设备）进口月份**：2016 年 1/4/6–12 月；2017 年 **全年 12 个月**；2018 年 4、7 月；2019 年 7 月；2020 年 9 月；2022 年 11–12 月；**2025 年 10 月**（最新一行）。另有 4 行未标月份（多为欧盟来源行）。
- 8471 80 00（电脑部件）2018–2023 几乎逐年全年有进口，2024 年 1–3 月、2025 年 4、8 月——主业仍是电脑 / 服务器部件，交换机是「顺手进」。
- 8517 69 10 视频电话 2016 年 5 月起、8517 61 00 基站、8517 18 00 话机——通信设备全品类都在进口清单里。
- **涉及商品编码**：85176200、85176990、85176100、85171100、85171200、85171300、85171800、8471（整机/部件多码）、8504、8544
- **对 Saga 的含义**：Megnet 自己做非欧盟直接进口（含 2025-10 的 8517 62 00），说明有报关 / 清关通道，不用我们解决进口门槛；但它是「什么都进」的经销商，交换机只是品类之一，最合适的话术是「同一报关批次顺带一两款管理型 PoE 补货」，不是整柜。给它报 DAP 没意义，EXW / FOB 深圳即可。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-29 查）：**

- `megnet.co.uk` → Microsoft 365（MX：megnet-co-uk.mail.protection.outlook.com）。M365 对陌生发件人最严：Gmail 发过去的群发多半落「其他 / 垃圾」，Safe Links 会预取像素 → 「打开」数不可信；这户只走 1:1、首封纯文本、≤1 个链接、不带附件

**假日避让（英国 · 按下一步「2026-11」窗口 2026-11-01→2026-11-30）：**

- 窗口内无该国法定假日

**公司底数 · 第 82 批（UK Companies House，2026-10-27 查；https://find-and-update.company-information.service.gov.uk/company/04748999）：**

- 法定名 / 登记号：MEGNET LTD. · 04748999 · 状态 **Active** · 成立 2003-04-30 · Private limited company
- 行业码 / 经营范围：82990 Other business support service activities n.e.c.
- 注册地址：Mortlake Business Centre, 20 Mortlake High Street, London SW14 8JN（商务中心地址，非自有办公室）
- 规模档：小型（small entities regime）· 单董事
- 账目：最近账目截至 2025-04-30（2025-06-10 提交）；类型 Total exemption full accounts，FRS 102 1A 小型公司制度（营业额 < £10.2m，免审计）；有形固定资产 £7,403（2024：£9,870）；下期账目截至 2026-04-30，2027-01-31 前交；确认声明 2026-04-30 已交（2026-05-01，「with updates」）
- 高管：Omar Ismat MIQDADI — 唯一在任董事，1973-04 生，英国籍，2003-11-17 上任（公司成立半年后从 Megdadi 家族接手）；其余 3 人均已辞任（2003/2009）
- 控制人 / 股东：见 PSC 页（未抓）
- 抵押 / 诉讼 / 担保：2021-06-07 登记 1 项抵押（charge 047489990001，MR01 2021-06-11）——通常是银行贷款 / 融资额度
- 曾用名：RELATIVE NETWORK TECHNOLOGY LTD（2003-04-30→05-15）
- **这意味着什么：**
  - 22 年老公司、一人董事、账目走小型公司免审计口径，年报按时交（2024 账目 2025-01-09 交、2025 账目提前到 6 月交）
  - SIC 挂的是 82990「其他商务支持服务」而不是 46510/62090 IT 批发或 IT 服务——登记口径与网站的 IT 分销定位不一致，说明是老登记没改，不是转行
  - 2021-06 新登记一项抵押：有融资安排 → 对账期（T/T 50/50 vs 30 天账期）会敏感
  - HMRC 进口记录（第 81 批）显示 2025-10 仍有非欧盟 8517 62 00 进口 → 公司活着且在进口交换机
- 备注：董事 = 实际拍板人：Omar Miqdadi。给 Megnet 的信抬头应对他本人而不是 info@。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | megnet.co.uk（取自域名，公司全名待核） | 推断 |
| 国家 | 英国 | 事实（用户表）|
| 网站/域名 | megnet.co.uk | 事实（用户表 URL/邮箱域名） |
| 类型 | 分销商 + 自有品牌（Chimera，OEM 采购） | 推断（据兴趣/备注关键词） |
| 联系人 | Rajiv | 事实（用户表） |
| 来源（From） | — | 事实（用户表） |
| 兴趣（Interested in） | 自己的品牌 有人卖他们的<br>MC SFP AOC等较多 | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | S重点 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：英国伦敦的兼容光模块/网络配件分销商（2003 年起，11–50 人），自有品牌 Chimera（MSA 兼容光模块、DAC/AOC、MC、交换机），供应全球经销商、分销商和制造商，宣称可触达 400 万+ 产品。用户表：S 重点，自己的品牌、有人卖他们的，MC/SFP/AOC 等较多，1 次实质回复。
- **类型**：分销商 + 自有品牌（Chimera，OEM 采购）
- **规模**：11–50 人（LinkedIn）
- **在卖/在用品牌**：Chimera
- **【第三方（LinkedIn）】定位与规模；自有品牌 Chimera 与 ISO 工厂合作生产**
  > We are specialist suppliers of compatible fibre optic transceivers and related networking solutions products since 2003 … Our global brand Chimera is an in-house brand of compatible products; produced in partnership with leading ISO compliant industry manufacturers. · Company size: 11-50 employees · Headquarters: London
  > 来源：https://uk.linkedin.com/company/megnet-limited-specialist-global-supplier-of-compatible-network-solutions（抓取 2026-10-21）
- **【官网】产品范围含交换机与 MC**
  > OEM Networking Products : SFP, QSFP, AOC, DAC, and Switches … Media Converters
  > 来源：https://megnet.co.uk/（抓取 2026-10-21）
- **【官网】Chimera PoE MC 型号与网店价格/条件**
  > CHMC-302P-SFP-3S20-LC $10.55 … Product Category · Media Converter Condition · OEM Warranty · Lifetime Warranty Brand · Chimera … 2-port 10/100Base-T PoE/PoE+ to 100Base Fx SM 20km LC,with external power supply
  > 来源：https://megnet.co.uk/product/chmc-302p-sfp-3s20-lc/（抓取 2026-10-21）
- **【LinkedIn】公司规模/成立/专长（含 switches、media converters）**
  > Megnet Limited | 5,083 followers … Company size: 11-50 employees … Founded: 2003 … Specialties: SFP, Memory, Patch Cords, … media converters, … AOC cables, DAC Cables, switches
  > 来源：https://uk.linkedin.com/company/megnet-limited-specialist-global-supplier-of-compatible-network-solutions（抓取 2026-10-21）
- **【官网】Chimera 全线终身保修**
  > we offer a lifetime warranty on all Chimera Networking products
  > 来源：https://megnet.co.uk/warranty/（抓取 2026-07-02）
- **KP**：—（报价热线） +44 845 130 1585〔https://dev.megnet.co.uk/〕
- **KP**：Jitendra Sain（Assistant Manager - Operations（邮件签名））jitendra@megnet.co.uk 〔S/A 邮箱来信 2025-01-16 来信 1 封（第 72 批从邮件表头补）〕
- **KP**：Nasim Chaudhari（来信署名人（职务未在邮件署名里出现））nasim@megnet.co.uk 〔S/A 邮箱来信 2025-12-01 来信 2 封（第 72 批从邮件表头补）〕
- **KP**：Omar Ismat Miqdadi（唯一在任董事（2003-11 起）—— 实际拍板人；邮箱待核（现有入口 info@ / sales@）（第 82 批 Companies House 核实 2026-10-27）） 〔https://find-and-update.company-information.service.gov.uk/company/04748999/officers〕
- 备注：A 确认：Chimera 品牌需要 MC/交换机货源；P1 = STI-110GE（MC 贴牌）→ 带入 STC-28DGGPM/424 系列；30% OEM 档。

### 加厚挖掘（2026-10-21 · 深挖 v1）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | MEGNET LTD.（Companies House 04748999，2003-04-30 成立，Active；SIC 82990；2021-06 有 1 项抵押登记） |
| 成立 | 2003 |
| 总部/地址 | London, UK |
| 人数 | 11–50（LinkedIn，5,083 followers） |
| 其他 | 自称 Chimera 品牌全球唯一制造商/供应商；Chimera 全线终身保修；网店以 USD 标价、库存 1,000,000（占位值）；Chimera 产品也经 Netceed UK 等分销 |

- **业务线**：兼容光模块（MSA/Cisco 等兼容）；Chimera 媒体转换器（百兆 PoE MC、千兆、10G XG100）；DAC/AOC、跳线、内存；交换机（LinkedIn 专长列出）

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| Chimera | CHMC-302P-SFP-3S20-LC | 2 口 10/100 PoE/PoE+ → 100Base-FX SM 20km LC MC，外接电源，网店 $10.55（占位价） | STI-110GE（PoE MC 版待核） | https://megnet.co.uk/product/chmc-302p-sfp-3s20-lc/（2026-10-21） |
| Chimera | CHMC-102P-8M0.5-UK | PoE MC（百兆，多模 500 m） | STI-110GE | https://megnet.co.uk/product/chmc-102p-8m0-5-uk/（2026-03-04） |
| Chimera | CHMC-XG100-8M0.3-UK / -3S10-UK | 10GBASE-T → 10G SFP+ MC（经 Netceed UK 分销） | —（10G MC 待 SmartByte 核型） | https://uk-store.netceed.com/chimera-media-converter-10gbase-t-to-10gbase-sr-300mtr-multimode-sfp-lc-chmc-xg100-8m0-3-uk.html（2026-10-21） |
| Chimera | CHT-CIS-SFP-1G-TE | 1000BASE-T 铜 SFP（Cisco 兼容） | —（配套） | https://megnet.co.uk/product-category/media-converter/（2026-10-21） |

- **触达通道（公开）**：网站/网店: https://megnet.co.uk/（Get Quote / Download Datasheet）；直邮: rajiv@megnet.co.uk / purchasing@megnet.co.uk（用户表）；LinkedIn: https://uk.linkedin.com/company/megnet-limited-specialist-global-supplier-of-compatible-network-solutions
- **近况信号**：
  - 网店 MC 类目价格有效期至 2026-11-23——目录持续维护（2026-10-21）
  - Chimera 10G MC 已进入 Netceed（大型运营商分销）渠道——有二级分销体量
  - 用户表：S 重点，1 次实质回复，自己的品牌、有人卖他们的
- **风险/边界**：Chimera 终身保修 → 对 ODM 来源的失效率与备件有硬要求；采购经理（purchasing@）导向价格，MC 单价极低（$10 级），利润薄
- **Saga 对位结论**：P1 STI-110GE（30% 档）——Chimera 已有百兆 PoE MC 与 10G MC，千兆 RJ45→SFP MC（STI-110GE）与 8 口千兆 PoE+2 SFP（STC-28DGGPM）是其「switches」专长下的补位 SKU；贴 Chimera 标 30% 档，批量可降
- **邮件切入句（英文）**：Between the CHMC-302P fast-Ethernet PoE converters and the XG100 10G units, a gigabit RJ45-to-SFP converter in Chimera packing is the SKU most buyers ask for, so I am quoting that first with an 8-port gigabit PoE switch as the second line.

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://megnet.co.uk/　语言：en　站点地图 URL 数：1165
- **标题**：Megnet / Compatible & OEM Network Transceivers, DAC & AOC
- **描述**：Multi-vendor network hardware distributor. Compatible & OEM transceivers, DAC/AOC cables, RAM, hard drives & optics. Next-day UK & Europe delivery.
- **首页栏目**：CHPC-LC-FC-15M-OS1-DPX / CHPC-LC-FC-15M-OM5-DPX / CHPC-LC-FC-20M-OS1-SPX / CHPC-LC-FC-20M-OS1-DPX / CHPC-LC-FC-20M-OS2-SPX / CHPC-LC-FC-20M-OM1-SPX / CHPC-LC-FC-20M-OM1-DPX / CHPC-LC-FC-20M-OM3-SPX
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：data center 127、surveillance 76、wireless 51、10g 39、industrial 34、media converter 31、sfp 27、telecom 21、automation 14、camera 9、ethernet 6、nvr 6
- **站内出现的品牌**：Cisco　（「（！）」= Saga 自家/供应商品牌已在其站内出现）
- **站内型号串**（正则抽取，含非交换机）：CHPC-LC-FC-15M-OS1-DPX, CHPC-LC-FC-15M-OM5-DPX, CHPC-LC-FC-20M-OS1-SPX, CHPC-LC-FC-20M-OS1-DPX, CHPC-LC-FC-20M-OS2-SPX, CHPC-LC-FC-20M-OM1-SPX, CHPC-LC-FC-20M-OM1-DPX, CHPC-LC-FC-20M-OM3-SPX, CHT-JUN-SFP-10G, QSFP28, APC-LC-50M-OM3-SPX, APC-5M-OM1-SPX
- **站内公开邮箱**：sales@megnet.co.uk
- **站内公开电话**：+44 08451301585
- **社媒**：https://twitter.com/MegnetLtd, https://twitter.com/intent/tweet?text=https://megnet.co.uk/megnet-solution/industrial-park-video-surveillance-solution/, https://twitter.com/intent/tweet?text=https://megnet.co.uk/megnet-solution/large-shopping-mall-wireless-network-solution/, https://www.facebook.com/sharer/sharer.php?u=https://megnet.co.uk/megnet-solution/industrial-park-video-surveillance-solution/, https://www.facebook.com/sharer/sharer.php?u=https://megnet.co.uk/megnet-solution/large-shopping-mall-wireless-network-solution/, https://www.linkedin.com/company/megnet-limited-specialist-global-supplier-of-compatible-network-solutions/
- **产品类页面**：https://megnet.co.uk/rj45-switches/；https://megnet.co.uk/network-switch/；https://megnet.co.uk/10gb-ethernet-switch/；https://megnet.co.uk/cisco-mds-9000-series-switches/；https://megnet.co.uk/all-products/；https://megnet.co.uk/products-verification/
- **已抓子页**：[Market News / OEM Networking Industry Insights / Megnet](https://megnet.co.uk/category/oem-networking-products-latest-updates-market-news/)；[Product News Archives - Megnet](https://megnet.co.uk/category/product-news-networking-hardware-updates-megnet/)；[Large Shopping Mall Wireless Network Solution / Megnet](https://megnet.co.uk/megnet-solution/large-shopping-mall-wireless-network-solution/)；[Networking Tips & Tricks / Megnet Knowledge Centre](https://megnet.co.uk/category/industry-announcements-product-updates-product-releases/)；[Shop Network Hardware / Transceivers, DAC, AOC & Optics](https://megnet.co.uk/shop/)；[Industrial Park Video Surveillance Solution / Megnet](https://megnet.co.uk/megnet-solution/industrial-park-video-surveillance-solution/)
- 首页正文摘录：Call us 24/7 +44 08451301585 Next Day Delivery Across - UK & Europe, KSA & UAE Life Time Guarantee and Up to 80% Cost saving . About Us Contact Us Login/Register Remember Me 0 $ 0.00 Your cart is currently empty All Products Quick view CHPC-LC-FC-15M-OS1-DPX Quick view CHPC-LC-FC-15M-OM5-DPX Quick view CHPC-LC-FC-20M-OS1-SPX Quick view CHPC-LC-FC-20M-OS1-DPX Quick view CHPC-LC-FC-20M-OS2-SPX Quick view CHPC-LC-FC-20M
- **自动对位建议**：STI-280GE（官网快照对位：工业/自动化词频 39、无 PoE 侧重 → DIN 8 GE + 2 SFP 非 PoE 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SA-015.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 13 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-02-19 | 2025.2.19 | 28bt |  | S |  | S 09.08.xlsx#1 |
| 2025-03-21 | 3.21 | list |  | S |  | S 09.08.xlsx#1 |
| 2025-04-28 | 428 | bypass |  | S |  | S 09.08.xlsx#1 |
| 2025-05-27 | 527 | Alarm |  | S |  | S 09.08.xlsx#1 |
| 2025-06-25 | 625 | 16电 |  | S |  | S 09.08.xlsx#1 |
| 2025-07-28 | 728 | 22mini |  | S |  | S 09.08.xlsx#1 |
| 2025-08-27 | 827 | 24fiber |  | S |  | S 09.08.xlsx#1 |
| 2025-09-29 | 929 | 24poe |  | S |  | S 09.08.xlsx#1 |
| 2025-10-29 | 1029 | dac |  | S |  | S 09.08.xlsx#1 |
| 2025-11-27 | 1127 | solar |  | S |  | S 09.08.xlsx#1 |
| 2025-12-29 | 1229 | taiwan |  | S |  | S 09.08.xlsx#1 |
| ? | 1223 | 28poe |  | Email |  | S 09.08.xlsx#1 |
| ? | 1.16 | 48口 | 5个商业24 48口 | S |  | S 09.08.xlsx#1 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：26 封（去 22 / 来 4）　|　**期间**：2024-12-23 → 2026-09-08　|　**最后去信**：2026-09-08
- **对方邮箱**：becca@megnet.co.uk、jitendra@megnet.co.uk、nasim@megnet.co.uk、omar@megnet.co.uk、purchasing@megnet.co.uk、rajiv@megnet.co.uk
- **最后一封来信**：2025-12-01 nasim@megnet.co.uk「Price and lead time」：Hi Team, Please share your best price, lead time, and warranty details for the following unit: HT2500-PSE-BT60 – 60W PoE++ Single-Port Injector This will be a test unit, and if it works on the customer’s end, we will proceed with a bulk order. Kindly advise at
- **邮件里报过的价**：2026-09-08 $170；2026-07-20 $1500；2025-12-02 $15；2025-10-29 $280；2025-08-27 $240；2025-01-16 $300

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 24 Port PoE Managed Switch | 2026-09-08 | 2026-09-08 | 0 | 1 | 1 |
| 24 Port 10G SFP+ Switch | 2026-07-20 | 2026-07-20 | 0 | 1 | 1 |
| Firmware 7.5 L2+ Feature Update | 2026-06-22 | 2026-06-22 | 0 | 1 | 2 |
| Updated Ethernet Switches Links | 2026-03-02 | 2026-03-02 | 0 | 1 | 1 |
| OEM Core Switching Solution | 2026-01-29 | 2026-01-29 | 0 | 1 | 1 |
| Optional Marvell Chipset Solutions | 2025-12-29 | 2025-12-29 | 0 | 1 | 1 |
| Price and lead time | 2025-12-01 | 2025-12-02 | 2 | 2 | 16 |
| Booster PoE Switch | 2025-11-27 | 2025-11-27 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-29 | 2025-10-29 | 0 | 1 | 1 |
| Industrial PoE Switch | 2025-09-29 | 2025-09-29 | 0 | 1 | 1 |
| 24 Port Fiber Switch | 2025-08-27 | 2025-08-27 | 3 | 1 | 4 |
| Mini Industrial PoE Switch | 2025-07-28 | 2025-07-28 | 0 | 1 | 1 |
| …共 21 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：A 级面层　|　**自动源**：3 个　|　**数据截至**：2026-10-28T08:44:48Z　|　**最近变化**：2026-10-28T08:44:48Z
- **最近变化摘要**：2026-10-28 home：内容变化：+28 −28 行
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SA-015/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://megnet.co.uk/) | html | HTTP 200 | 2026-10-28T08:44:48Z | 8067 字符；首行：Megnet \| Compatible & OEM Network Transceivers, DAC & AOC |
| [sitemap](https://megnet.co.uk/sitemap_index.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |
| [feed_auto](https://megnet.co.uk/feed/) | rss | HTTP 200 | 2026-10-23T04:20:51Z | 10 条；最新：Wed, 22 May 2024 14:13:14 Scaling New Heights: ARI-QSFP+ 100G for Cloud Computing  |

- **人工定期看（登录墙，不自动抓）**：LinkedIn: https://www.linkedin.com/company/megnet-limited-specialist-global-supplier-of-compatible-network-solutions/；X/Twitter: https://twitter.com/MegnetLtd

## 联系方式（已有 · 原值照录）

- 邮箱：`rajiv@megnet.co.uk`〔企业邮箱；来源：用户表原值〕
- 邮箱：`purchasing@megnet.co.uk`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Rajiv
- 网站/域名：megnet.co.uk
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| — | 报价热线 | +44 845 130 1585 | 调研核实（公开页） | https://dev.megnet.co.uk/ |
| Jitendra Sain | Assistant Manager - Operations（邮件签名） | jitendra@megnet.co.uk | 调研核实（公开页） | S/A 邮箱来信 2025-01-16 来信 1 封（第 72 批从邮件表头补） |
| Nasim Chaudhari | 来信署名人（职务未在邮件署名里出现） | nasim@megnet.co.uk | 调研核实（公开页） | S/A 邮箱来信 2025-12-01 来信 2 封（第 72 批从邮件表头补） |
| Omar Ismat Miqdadi | 唯一在任董事（2003-11 起）—— 实际拍板人；邮箱待核（现有入口 info@ / sales@）（第 82 批 Companies House 核实 2026-10-27） | — | 调研核实（公开页） | https://find-and-update.company-information.service.gov.uk/company/04748999/officers |
| Rajiv | — | rajiv@megnet.co.uk / purchasing@megnet.co.uk | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| S 09.08.xlsx#总表:2 | 1 | https://megnet.co.uk/product-category/media-converters/ | 英国 | Rajiv |  | 自己的品牌 有人卖他们的<br>MC SFP AOC等较多 | rajiv@megnet.co.uk<br>purchasing@megnet.co.uk |  | 13 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-110GE | 深挖对位：Chimera 已有百兆 PoE MC 与 10G MC，千兆 RJ45→SFP MC（STI-110GE）与 8 口千兆 PoE+2 SFP（STC-28DGGPM）是其「switches」专长下的补位 SKU；贴 Chimera 标 30% 档，批量可降 | $24.3 USD EXW（30% 档，SmartByte LT-IMC30G-E 125 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（分销商 + 自有品牌（Chimera，OEM 采购）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-110GE），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STI-110GE 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 1 次实质回复（对方认识我们）；自有品牌/贴牌需求 = 现成 OEM 客户；欧洲主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STI-110GE 按 30% 档报价，做现供应商的第二货源；贴牌 + 定制 UI/型号 → 30% 档与长期绑定；规模（调研）：11–50 人（LinkedIn）
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

**主题**：L2 PoE+ access switch tender — Voice VLAN is now in firmware

```text
Hi, Jitendra,

In January 2025 your tender needed Voice VLAN, SNMPv3, SSHv2 and IPv6 on 24/48-port PoE+ access switches, and we had to say "Voice VLAN under development". It has been in firmware since 7.4 (now 7.5) on the Marvell AC5 24/48-port PoE+ models with 10G uplinks.

- 24x GbE PoE+ 280 W + 4x 10G SFP+, L2+ — $180 USD EXW (our 8 September mail said $170; that batch is gone, $180 is the current one)
- 48x GbE PoE+ 440 W + 4x 10G SFP+, L2+ — $335 USD EXW (the $300 in our 2024/25 mails was at the old exchange rate)
(2026-10 price table, valid 15 days from this mail)

Separately, Nasim: the 60 W PoE++ injector test unit (15 USD) from December — did it pass at the customer, and is the bulk requirement still there?

One question: is that tender, or a similar one, still open?

Thank you.
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

- **2026-11-12**（14 天）：无回复 → 换通道再试一次；仍无 → 降 B。有任何回复 → 当即更新 research JSON 并重渲染。

## 变更日志

- 2026-10-29：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 A，分数 94）

---

*建档日期：2026-10-29　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
