
### 5.4 Saga 暂无对应、不要承诺的产品形态（范围护栏）

Saga **没有**（信稿 / 报价里出现即错，客户点名问时按 §9.4 两层答法）：反向 PoE、PoE 注入器 / 分离器单卖、光模块 / SFP 单卖（只随整机）、Bypass / TAP（Saga 无对应型号，只能沿用 LT- 型号且标注）、GPON / OLT / ONT、Wi-Fi / AP、M12 轨交、HDMI、百兆介质转换器以外的 MC（只有 STC-110XGE 为 10G MC）、WDM、升压 PoE（Booster 线未进价表）、机柜 / 配件、路由器、定制 ODM 开发、PoE BT 整机（只有 -2BT/-4BT 部分口）、L3 工业机以外的 L3 功能承诺、被动 PoE 整机（只有 -24V/-Auto 三款）、KC 认证、云管理 / 控制器 / REST API、堆叠（AC5 线；CENTEC STH1G 可堆叠 ≤8 台 / 360 Gbps 是另一层）、2.5G **铜口**（AC5 线 2.5G 只在 SFP/SFP+ 笼子；CENTEC 有 Multi-Gig 铜口但无价无现货；Realtek 商用线有 2.5G/10G 铜口 → 待 SB-263 裁定）、SFP28+ 高速 Marvell、SDK / 源码（「source code mode is NEVER an option」）、Cisco 私有协议（CDP/HSRP）、NAT / TSN / MPLS（AC5）/ SD-WAN / BFD / IP SLA / PIM-DM / RIPng / PBR（AC5）。

---

## 6. 技术能力与边界

### 6.1 AC5 7.5 L2+ 功能表（已核，`Saga Feature List_7.5.x_L2+.xlsx`）

HTTPS ☑ · SNMP v1/v2c/v3 ☑ · SSH2 ☑ · SFTP/SCP Client+Server ☑ · sFlow ☑ · MQTT ☑ · PIM-SM ☑（仅 CLI）· ERPS <20 ms ☑（单环/相切/相交）· LACP 64 组 ☑ · 静态路由 v4/v6 ☑ · IGMP Snooping / VLAN / QoS / ACL（AC5 3K–6K 条 vs Realtek 256–512）· LLDP · Syslog · Voice VLAN · PoE watchdog / 定时 / 250 m 延长（工业 PoE）。**无** MLAG / OSPF / RIP / VRRP / NAT（L2+ 档）；L3 型号另有 RIP/OSPF（按型号表）。「高阶管理 = 可编程 + API」是早期思路，**现行口径不卖 API**。

### 6.2 硬件事实

- 工作温度：非 PoE / PoE ≤240W **-40 ~ +75 ℃**（部分 +70 ℃）；370W 机型 -40 ~ +60 ℃；防护 **IP40**（NOT IP67/IP68）；CENTEC 0 ~ 40 ℃（Netaş 曾指不够）。
- 工业机 DC 12–58 V（部分 12–75 V）冗余输入、极性反接/过载保护；PoE 机 DC 44–57 V；`-U` 机架型 AC/DC 冗余。
- PoE：802.3af/at 标配；bt 60–90 W 只在 `-2BT/-4BT` 衍生型的 1–2/1–4 口；PoE 机 GUI 只显示 **PD 侧**电压/功率，不显示交换机自身输入电压。
- 单台重量/尺寸（报 DAP 直接用）：STI-21616DGGPM/XGGPM 158×115×54 mm 净 1.2 kg（12 台/箱 20 kg）；STI-288DGGPM 1.2 kg；8 口管理型与 STI-21616DGGPM 同尺寸（一款彩盒通用）；STC-424XGGPM ≈3.4–3.5 kg，440×180/205×44 mm；STC-448XGGPM ≈5.6 kg；STC-2224GFP-24V 2.9/3.6 kg，440×290×45 mm；SmartByte 原箱 8 PoE+2 SFP 两台/箱 3 kg，24/48 口机 10.6 kg（53.5×20.5×40.8 cm）；ANW-2116-PG 8 台/箱 21 kg。
- 芯片（Case 1 德国客户问答）：Marvell 98DX336S + 88E1680 + 88E1548（AC3 代）；PoE 用独立小板；无 TSN、无 virtual stacking；10G 收发器 LT-MC80X 用 Marvell 88X3310 PHY。
- 出货前 **5 个工作日稳定性测试**（公司政策；常订型号 STI-244GP、STI-050GE 只做 8 小时老化）。

### 6.3 OEM / ODM 菜单（对外英文可直接用）

"Company logo / Packaging / Front panel (PVC mask) / Product label / Model name / Serial number / User manual / Default login IP / SNMP OID customization / Web GUI language — all mature options. We can also discuss firmware customization for specific project requirements, subject to technical evaluation."

| 项目 | 口径 |
|---|---|
| 免费、1 台也做 | logo、型号名、SN、MAC 段、默认登录 IP、SNMP OID、Web UI logo、标签、彩盒去 Made in China |
| 收费 / 有 MOQ | Web UI 配色/字体（「改码量大，样单不做」）、PVC 面膜丝印（整批开模，余料 Saga 代存；SA-006 $50 一次性）、定制彩盒 **$2.5/套、200 套起**（盒 + 异形泡棉 + 顶片 + 说明书）、特殊包装 |
| SKD / CKD / ODM | SKD 可做；CKD/ODM 需评估；**源代码不开放**；SDK/API 不作为卖点（2025-11 曾说「part of our TTC services」——不再使用） |
| 功能开发 | 只在**有订金 / 订单确认后**排期，否则不给时间表（AC5 加 SFTP 先例） |
| 中性包装 | 可做中性包装 / 标签；不打 Made in China；不出现 Saga 以外品牌痕迹（INH-04） |
| 文件 | COO 产地证 $15/份；其他认证文件复印件免费；**只发 Saga 名义证书**，SmartByte 名义（LT- 型号）证书不外发 |
| 自有 PEN | NYNEX 2025-03 发现 SmartByte 通用 MIB 含其他 OEM 企业 OID（.57430 / .56813 / .171 D-Link）；Q-35/Q-45 按 T29-U15 口径：**不申请不更换**（宣传 SmartByte 品牌是合作约定、订单归 Saga）；OEM 菜单里 SNMP OID 写 "Private MIB under your own IANA PEN (please send us your PEN) or under Saga's enterprise tree" |

### 6.4 Not-to-Do 清单（边界即资本）

合并版：云管理 / 控制器、EN50155 轨交 / 车载、IP67、消费级 / 家用路由、UL / E-mark / KC 行业、SFP28 及以上高速 Marvell、L3 组播级固件、SDK / 源码、国内公账单、视频营销 / Facebook / YouTube / 付费广告、极低价客户、「无未来的贸易商」、不尊重工程时间的、拉开会不买的、不稳定需求的项目型、无法连续复购的产品、OEM 贴牌的超重活、硬件售后「换新，不修」。客户需求命中清单 → 直接写「停点：边界」，不设计绕路。

### 6.5 认证登记（Saga 名义，可外发）

| 类别 | 证书号 / 报告号 | 日期 | 机构 | 标准 | 覆盖 |
|---|---|---|---|---|---|
| CE-EMC | JAT24070502534EC-1 / ER-1 | 2024-07-05 | 东莞骏安 Jun'an | EMC 2014/30/EU；EN 55032:2015+A11:2020；EN 55035:2017+A11:2020；EN IEC 61000-3-2/-3-3 | Ethernet Switch 24 型 |
| CE-LVD | JAT24070502534SC-1 / SR-1 | 2024-07-05 | 东莞骏安 | LVD 2014/35/EU；EN IEC 62368-1:2024 | 同上 |
| RoHS | JAT24070502534RC-1 / RR-1 | 2024-07-05 | 东莞骏安 | 2011/65/EU & (EU)2015/863 & 2017/2102 | 同上 |
| REACH | — / JAT24070502534CR-1 | 2024-07-05 | 东莞骏安 | SVHC 240 项 | 同上 |
| UKCA-EMC / LVD | JAT24070502535EC-1 / SC-1 | 2024-07-05 | 东莞骏安 | BS EN 55032 / 55035 / 61000-3 / BS EN IEC 62368-1:2024 | 同上 |
| FCC SDoC | NCT24028321XE1-1 | 2024-07-11 | 深圳中测通 NCT | 47 CFR Part 15 Subpart B | 同上 |
| 介质转换器 CE/FCC/RoHS | HK2104211224E / HK2104210402S / HK2104211225E / HK2104210399R | 2021-04-29 | 深圳华科 HUAK | 同上系列 | Media Converters |
| 介质转换器 UKCA | HTT202210092ER / LR | 2022-10-17 | 深圳华通 HTT | BS EN 55032 / 62368-1 | 主测 STC-110XGE |

- 证书覆盖的型号范围需人工打开 PDF 确认后再对外承诺（原件在 Drive `MUST KNOW/Certification/`，索引 `docs/drive/Certification/认证证书索引.md`；登记表 `docs/reference/证书登记表_2026-10-22.md/.csv`）。
- 认证口径（统一）：持有 CE / FCC / RoHS / REACH / UKCA；**无 UL**（2024-01 曾对 AirLive 说过「CE/UL compliant」——错，不再用）；TAA/GSA 不满足；日本 PSE/VCCI 可以客户名义办、费用客户自担（PSE 电源用 MEAN WELL GST120A48/240A48）；KC/BIS/EAC 由客户方办；UKCA 只对 GB 客户提。

来源：`docs/对外口径一致性_2026-10-24.md` #3/#5/#10/#22、`docs/reference/Saga商务条款速查.md` §4/§5/§9/§11、`docs/reference/证书登记表_2026-10-22.md`、`docs/Saga理念摘读_2026-10-23.md` A29。

---

## 7. 商务条款（销售口径）

### 7.1 交期与起订

| 项目 | 口径 |
|---|---|
| 生产启动 | 收到货款后开始（银行到账 1–2 个工作日） |
| 标准品 | ≤50 台 **4–7 个工作日**（Simon 现行对客户：「3–5 working days」+ 5 天老化；NYNEX 2026-09「3 weeks (15 working days) after order confirmed」）；定制/大单另议 |
| 大单 | 备料约 3 周（PCB、PoE 芯片、AC5 芯片）；**≥25% 订金起备料**；优先谈分批交付；250 台 ≈ 40 个自然日；1K 台 3–6 周 |
| 运输 | 快递 DHL/FedEx/UPS 4–7 天；海运/空运按单询价；下单到收货 ≈10–15 个自然日 |
| MOQ | **1 台**；定制（贴牌 / 面膜 / 固件）MOQ 按项目 |
| 样品 | **不免费**（"Saga Telecom do NOT do FREE SAMPLES"）；按 partner price 收费、样品款抵扣首个批量订单；5 个工作日出货；建议 ≥2 台。唯一例外：2026-04 对日本 UNEAX 说过「lending a piece is OK」（对方未接；对 UNEAX 不要改口） |

### 7.2 付款

| 项目 | 口径 |
|---|---|
| 币种 / 条款 | **USD EXW**（仓库规则）；Drive FAQ 写 DAP/DDP 为主 → 客户要到门价时按 DAP 单独核算运费；非欧盟客户常用 DAP / FOB 深圳 |
| 方式 | T/T（默认）、PayPal（+5%，样机 / 小额）、Xtransfer（Angora / James / NYNEX / Netaş）、EUR 账户（NYNEX 2026-09 三币报价 USD 6.71 / EUR 7.6 / RMB 2,015）、HK 账户收 TRY、RMB 经中国付款代理（俄罗斯 / 土耳其部分） |
| 比例 | 标准品批量 **50% 预付 + 50% 发货前**；定制/OEM 100% 预付；小额/样品 100% 预付；要求锁定排期需预付 25% 物料押金 |
| 手续费 | T/T 银行费 $25/单（买方承担）；PayPal 5% |
| 首笔外汇 | 中国银行对首笔境外来款要**买方股东信息**（一个股东即可，只首笔）——新客户首付前先说 |
| 有效期 | 报价 15 天；汇率剧烈波动重新定价；TRY 报价只给 3–7 天 |
| 国内 | 国内客户只接私账（支付宝 / 微信 / 银行卡），不接公账 |
| 待清路径 | RU / BY / KZ / UZ 收款路径未清前不报价（Backlog） |

### 7.3 保修与售后

| 项目 | 口径 |
|---|---|
| 保修期（对外） | **商用 STC 1 年 / 工业 STI 3 年 / DIN 电源 3 年 / 介质转换器与 PoE 配件 1 年 / CENTEC STH 1 年**，自交付日起，终身技术支持；SmartByte 官网 5 年是工厂政策，**不引用** |
| DOA | 发货后 3 个月内到货即坏 = DOA：往返运费与更换由工厂承担；保内客户寄回自付、工厂承担回寄与维修；保外全部客户承担 |
| RMA | **每 100 台同型号随货送 2 台备件**（或等值 2% 货款抵扣）；**不接受退货**，坏机以备件 / 下单补发处理；「硬件售后：换新，不修」 |
| 支持 | 邮件 + 远程（Web/CLI 日志）；固件升级免费；不含现场服务 |
| 除外 | 雷击、过压、进水、私自改装、SN 涂改、未授权维修 |

### 7.4 物流与清关实务（只记实际发生过的）

| 项目 | 做法 |
|---|---|
| 两条物流线 | ① **客户自己的广州货代**（Mbata 尼日利亚：Saga 只送到广州仓，发货信息单写「品名 / 数量 / 重量 / HS 8517622990 / 品牌 无 / 不带电不带磁」）；② **Saga 自己的深圳买单报关线**（James 加拿大、Angora 土耳其、Sugito 马来西亚、NYNEX 德国、Rishi 印度…）：填「出口货物确认函 / 货物情况说明表」 |
| HS 编码 | 交换机 **8517622990**；光模块 8517795000；光纤清洁笔 8517799000 |
| 品牌栏 | OEM/贴牌客户一律「**无品牌**」；自有品牌出货写「Saga Telecom · 境内自主品牌 · 生产厂家 Zhengzhou Saga Telecom Co., Ltd.」 |
| 报关费 | 大货运费基础上再加 ≈250 元（150 报关 + 100 保险） |
| 大单运费 | Angora 176 台 = 23 箱 471.9 kg，运费 22,426 RMB ≈ 127 RMB/台（≈$18），把毛利从 ~24% 压到 15.9% → 同规模报价时**运费单列、空运/海运分开报** |
| 印度清关 | FedEx 需收货人先在 kyc.fedex.com 上传 GSTIN + 身份/地址证明 + POA，否则卡海关 |
| 装箱单 | 工厂 PACKING LIST 开给 Zhengzhou Saga Telecom（Consignee），再由 Saga 转出口；客户只看到 Saga 的 CI/PL |
| 出口管制分类 | **EAR99 · NLR · CCATS 不适用 · HTS 8517622990 · 原产国 China**（对 Netaş 已填；大企业供应商入库问 ECCN 照此答） |
| 个人数据 | Netaş《Annex 1》已签：客户方个人数据只用于履约、不转第三方 → Netaş 联系人不进群发、不转给工厂 |
| 客户资料夹 | 成单客户一户一个 Google Drive 订单文件夹，把对方指定人加为编辑，请其上传测试报告 |

### 7.5 Simon 2026-09/10 现行口径（S 邮箱原话，可直接复用）

| 项目 | 英文原话 |
|---|---|
| 群发主推 | "Marvell AC5 based L2+ switch: 24 Port PoE af/at + 10G Fiber Uplinks + OEM and customizable Web GUI — Price: 180USD/PC" |
| 样品 | "Normally evaluation units are provided at a partner price, and the sample cost will be credited toward your first commercial order. For long-term partners we can discuss additional support based on the project and cooperation plan." |
| 分销 | "For now, we do not have a distributor in the UK. We are certainly open to discussing a distributorship after we get to know each other and see good cooperation." |
| 控制器 / API 问法 | 先反问 "REST API / SNMP-based / SSH-CLI automation / NETCONF / other controller platform?"——实际可承诺 SNMP + CLI/SSH + Web；**无云控制器、无 REST API**，下一封应直说 |
| 资料包 | 先发 `Saga Feature List_7.5.x_L2+.xlsx` + `Product Link_2026Q3.pdf`；深谈再发 `STC-424XGGPM-280W.docx` + `Marvell Based CLI/Web Manual.docx` + `SWITCH-MIBS-release.docx` |
| 涨价 | "in recent days, PCB and material costs are rising. This is one of the very competitive models."（统一说法：2026 年 PCB/RAM 成本 + 汇率，AC5 整线约 +$15；**不说「高价是为了筛选客户」**） |

来源：`docs/reference/Saga商务条款速查.md` §1–§3/§8/§10/§11、`docs/对外口径一致性_2026-10-24.md` #6–#9/#12、`docs/Saga理念摘读_2026-10-23.md` A24。

---

## 8. 定价规则（两套并存，都是底线不是策略）

### 8.1 公式（仓库规则，用户 2026-10-19 认可）

```
报价 USD（EXW）= SmartByte 未税人民币价 × (1 + 档位) ÷ USD/CNY 近期汇率
档位 ∈ { 20%, 25%, 30% }      汇率快照 1 USD = 6.69 CNY（2026-10-17；报价当天重核）
```

| 客户类型 | 档位 | 理由 |
|---|---|---|
| 分销商 / 电商 / 明显比价型 | **20%** | 走量、价格敏感、与台系品牌正面比价 |
| 集成商 / 项目型 / 方案商 | **25%** | 看方案可行性，让利空间保留在 25% 内 |
| OEM/ODM 深度定制、小批量技术型（CLI/MIB/私有 UI） | **30%** | 定制与技术支持成本高，Saga 核心差异化 |

### 8.2 芯片线 / 账户类型底线（《计划.docx》，Simon 原话）

- **Realtek ≥ 20 个点**（特殊客户或量大可压至 15）；**Marvell ≥ 25 个点**（可压至 20）；**CENTEC ≥ 35 个点**（必要时可加至 50 甚至更高）。
- 小单 **3 成左右**（按型号 / 数量 / 国家调整，**不低于 2.5 成**，含运费杂费）；大单私账 2–2.5 成；大单公账扣 10 个点税后**不低于 15 个点**。
- 封顶：「给我 100，我最多卖 130」（**30% 天花板**）；「Mbata 就是 20 个点，不能再低了」。
- 两套口径（按客户类型 20/25/30 vs 按芯片线 20/25/35）并存，写档案时注明选哪一档、为什么。

### 8.3 价格书写与有效期

`$xx USD EXW（快照 YYYY-MM-DD，15 天有效，报价前核价）`；首触邮件只报 **一个** P1 价格、只写 Saga 型号；同名 L2+/L3 注档位；对照表标「核对」的条目报价前与 SmartByte 确认规格。

### 8.4 价格异议处理

价格异议一律不让步（iotsistem、Aironix、case.uk 先例）；来信只有「target price / extremely expensive / cheaper alternative」而无任何技术问题 → 价格流客户 → 降级或 PASS，不在档案里设计「让价方案」。折扣「基于数量且在样品测试之后，只有客户对质量满意时谈价才有意义；分销商给最好价」。

### 8.5 常用价格锚（USD，CNY 6.69，20% 档为主）

Realtek 商用线以 §5.3.2 为准（例：STC-028GP = ZX900-AFG-82N，CNY 170 → $30.5 / 31.8 / 33.0；2023-11 首版曾报 $24.5；STC-2224GP = ZX900-AFG-2422S-300 CNY 490 → $87.9 / 91.6 / 95.2）· STC-424DGGM $82.5 · STC-424DGGPM-280W $134.5 · STC-424XGGM $127.4 · **STC-424XGGPM-280W $181.2（群发 $180）** · STC-448XGGM $263.7 · STC-448XGGPM $335.4 · STC-4168XGGCM $376.7（L3 列表 $413）· STI-280GE $46.6 · STI-288GPM $78.9 · STI-288DGGPM $139.9 · STI-21616DGGPM $240.4 · STI-21616XGGPM $297.8 · STI-488XGGPM $165 · STI-42424XGGPM-4BT $430.5 · STC-110XGE $65 · **STH-2C24XF-HSI $1,500（含 MA $1,250）· STH-2C6QX $1,200 · STH-2C24XE-HSI $1,700（2026-07 现货）· STH-8C48DX-HSI $4,800 · STH-32C-HSI $6,000**。

### 8.6 CENTEC（STH）报价锚（无成本价，只有对外锚）

| 平台 | 代表型号 | 锚 |
|---|---|---|
| XLite | STH-2C6QX-HSI/-SFI（6×40G + 2×100G） | $1,200（2026 Q2 价表） |
| XLite | STH-2C24XF-HSI（24×10G SFP+ + 2×100G） | HSI $1,250 含 MA（2026-06 对 SA-060）；群发 $1,500；SFI 无 DC 输入 |
| VastLakes STH10G | STH-2C24XE-HSI（24×10G Multi-Gig 铜 + 2×100G） | $1,700（2026-07 现货） |
| BigFlow / PeakNetX | STH-8C48DX-HSI（48×25G + 8×100G）/ STH-32C-HSI / STH-32QC（32×400G） | $4,800 / $6,000 / 400G 随 ITM 单 6 台 + 36 × 400G-SR4 @ $300 |
| STH1G（可堆叠 ≤8） | STH-2QX4DX48GP-HSI 等 5 款 | **仓内无任何价格（Q-54）** |
| Multi-Gig 铜口 PoE++（STH2.5G/5G/10G 20 余款） | STH-8DX24VP-HSI、STH-2C24XP-HSI、STH-2QX4DX8XP40DP-HSI… | **无价、现货未知（Q-56）**，不主动报 |

STOS 功能按许可分层：**EB 基础 / MS 高级 / MA 城域 / ST 堆叠**；EB 即有 RIPv1/v2、PBR、IP SLA、VRRP、ERPS、QinQ、sFlow、IPFIX；MLAG / VXLAN-EVPN / MPLS / BGP-OSPF 在高层许可。2026-01 群发写过 CENTEC「Full L3 features (VXLAN, EVPN, MPLS, Stacking etc.)」——Stacking 是否删除待核。

### 8.7 价表版本与已知矛盾（报价前必看）

- 仓内三代 Marvell 价表：① Drive `Extra Info/Price/2026 Price List_*.xls`（老抬头；STI-288DGGPM $125、STC-424XGGPM-280W $180、STC-4168XGGCM $375）= Angora 2024-11 成交价 = **Simon 2025–26 所有实际报价的量级**；② 仓库根目录三份《Price List_Marvell Based …》PDF（2026-06-22，新抬头，85/94 款 = ① × 1.10：$137.5 / $198 / $413）= `价格主表` 的「Saga列表价USD」，但 2026-06→10 四个月外发里**几乎没用过**；③ 仓库公式价（本表 USD 列）。
- 118 款对照：+20% 档中位数 = ② 列表价的 90%；**12 款 +20% 档 ≤ 列表价 70%**（STI-480XGGM $150.7 vs $253、STI-488XGGPM $165 vs $269.5、STC-4816XGCGPM $358.7 vs $611、STI-050GE $17 vs $34.1…）→ Q-59 待 Simon 定（跟着 SmartByte 降还是守列表价；默认按档位）；10 款 +20% 档 > 列表价（2.5G-SFP 工业 DGG 家族，如 STI-288DGGPM $139.9 vs $137.5——列表价按旧汇率 ≈7.1 算）。
- 非管理工业线成本表是 2024-01 的，算出的档位价（STI-054GP $31–34、STI-244GP $35–38）比 Simon 2026-04 实报（$33 / $45）还低——**不可靠，报前核**。
- 群发里的低价（Elsa $170 / STI-21616GP $165 / STI-488XGGBPM $215）是**旧汇率引流价**（U28），不是现行报价基准。
- HRUI 线：Drive 2026 Q3 美元表 61 款对洪瑞 2026-09-30 新进价的隐含加价 47 款可对照里 **39 款 < 20%、2 款为负**（Q-47）——Realtek 线报价必须按新进价重算。
- Simon 实际毛利（PI 包 `成本统计.xlsx`）：Angora 大单 ~24% → 运费后 15.9%；NYNEX 2024–2026 USD 19.6k 利润 RMB 7,082；Obmac 一单 265 台 USD 9,350 利润 RMB 23,118；利润点来源「13 + 5（返点）+ 20 个点价格 = 接近 40 个点」（出口退税 13% + 返点 5% + 加价 20%）。内部数字，**不外发**。

来源：`docs/rules/报价与型号规则.md`、`docs/reference/价格表_三档加价_USD.md`、`docs/reference/价格表_HRUI_三档加价_USD.md`、`docs/reference/CENTEC_产品表与报价锚_2026-10-24.md`、`docs/对外口径一致性_2026-10-24.md` #15/#19–#21、`docs/成单客户_毛利复盘_内部_2026-10-24.md`、`docs/Saga理念摘读_2026-10-23.md` A11。

---

## 9. 品牌口径与对外话术

### 9.1 固定四句（英文，逐字，不改写）

| 场景 | 原文 |
|---|---|
| 邮件签名 / 落款 | `<名字>` / https://sagatele.com/ / **An Engineering & Supply-Chain-First Telecom Partner** / **Built to Last, Continuous Supply, Evolving Together** |
| 一句话介绍 | **Tailored Managed Networking Solutions — A Scalable Path from Access to Core** |
| 三个关键词 | **Architectural Stability, Continuous Supply, and Lifecycle Continuity** |
| 使命 | Ensure that the journey from the first access switch to a mature, high-speed core remains scalable, coherent, stable, and low-friction |

仓库信稿签名统一：**「Saga Telecom - sagatele.com」**（首触样板落款 "Saga Telecom — An Engineering & Supply-Chain-First Telecom Partner · PoE / industrial switch OEM-ODM supplier (neutral packing available) · https://sagatele.com/"）。

### 9.2 口号史（知道就行，别用旧的）

3C「Connecting, Converting, Creating」→「Saga Telecom, OEM Factory / Tailored Managed Networking Solutions Provider / Built to Last, Continuous Supply, Evolving Together」→ 2026-07-29 中间句改为「An Engineering & Supply-Chain-First Telecom Partner」（「solutions 太泛化了，本身我们只有硬件」「叫 partner 比较亲切」）；「**OEM factory 不要加了，有点 low**」；第三句不变。2025–2026 签名「Saga Telecom/OEM Factory」127 封已发出——不翻案，新材料一律新口径。

### 9.3 理念语录（Roadmap / 官网原句，可直接引用）

- Continuity Over Novelty — "Upgrading from Access to Core is treated as a system extension rather than a replacement. By maintaining familiar workflows, we ensure that as bandwidth increases, operational complexity does not."
- Rational Technology Selection — "Silicon choice is an engineering decision, not a marketing one. Access Layer: Anchored on Marvell platforms selected for their industrial pedigree, field-proven stability, and mature ecosystem. Aggregation & Core Layer: Built on CENTEC solutions introduced only after comprehensive validation of ecosystem maturity, long-term supply alignment, and backbone-grade reliability."
- "A single, accountable technical contact across the entire network lifecycle."
- "These are not isolated hardware SKUs, but a coherent, scalable system that can evolve with network demands."
- "The transition from Access → Aggregation/Core is often the highest-risk point in a network's lifecycle."
- 官网："Built to engineer, not just to sell." / "We commit to Marvell and CENTEC architectures and go deep — not broad." / "Chip inventory, held on purpose." / "Strategic inventory isn't a cost center. It's the product." / "We're not a marketing-driven company. We put resources into engineering and inventory because that's where we actually create value for clients." / "Typical response within one business day. We don't use contact forms — direct email gets a faster, more useful reply."
- "We are backing our clients and following the market trend. Let's evolve together!!"
- 官网 At-a-Glance：Positioning = Engineering & Supply-Chain-First；Chipset Platforms = Marvell · CENTEC · Realtek；Customization = OEM / ODM / SKD / CKD；Supply Model = Strategic Inventory · Fast Lead Time；Certifications = CE · FCC · RoHS · REACH · UKCA；We Don't = Rail / transit certified (EN50155)、IP67、Consumer / home routers（UL 与 KC 官网写「available on request for qualified projects」——比仓库「无 UL」松，原样保留但信稿按仓库口径）。

### 9.4 口径规则 R1–R7 + 用词表

| # | 规则 |
|---|---|
| R1 | 自我定位只用 §9.1 四句；不自称 factory / manufacturer / we build；统一 "we supply / our Marvell-based portfolio / our manufacturing partner's facility"；About 文案「不要说是贸易商，换个说法」；对外不说 SOHO，说 "a specialized networking solutions provider" |
| R2 | **禁用** SmartByte 标语与工厂自述（"Genuine Source Factory • Robust R&D Support"、"SmartByte is specializing in R & D…"、Factory Tour 图文） |
| R3 | SmartByte 官网只借事实（型号、端口、PoE 预算、固件版本、认证、保修年限按 Saga 口径） |
| R4 | 网址只写 sagatele.com |
| R5 | 不主动承诺云管理（CENTEC DHCS 客户点名问时只答 "exists, self-hosted DHCS, not part of our standard offer"） |
| R6 | 芯片口径：接入层 Marvell、汇聚/核心 CENTEC；「CENTEC 不是 access 是 core」；不写 SKU 之外的性能承诺 |
| R7 | 客户语言英文、仓库笔记中文；英文引用照抄原句 |

- **用词白名单**：engineering-driven、supply-chain-first、architectural stability、lifecycle continuity、strategic inventory、low-friction deployment、predictable delivery。
- **禁用词 / banned phrases（信稿审计直接报错）**：cheap、best price、leading manufacturer、high quality with low price、professional service、list price、in stock（CENTEC 400G 群发写过，实际交期要核）、free samples、trading company、OEM Factory、NDAA、TAA、UL、GSA、general agent、we manufacture、Marvell ecosystem、SONiC、ONIE、"I researched your website"、产地、竞品名字。
- **信稿结构规则**：单一 P1、只问 **ONE question**、英文、付费样品、不写电话（WhatsApp 只给跳转）、UKCA 只对 GB、非欧盟 → DAP / FOB 深圳、模型必须在有效型号集合内。
- **两层答法**（客户问「有没有 X」）：第一层 Marvell AC5 线有/无；第二层 CENTEC 线有/无（查 `CENTEC_产品表与报价锚` + `客户功能需求台账` 看谁问过、当年怎么答）。例：多千兆铜口——"Marvell line: 2.5G/10G on the fiber cages only; our commercial Realtek line has 2.5G/10G copper; CENTEC Multi-Gig PoE++ models exist on request."

### 9.5 敏感问题的统一答法（口径表 #1–#22 精华）

| 主题 | 统一口径 |
|---|---|
| Saga ↔ SmartByte 关系 | "SmartByte is our Marvell-platform manufacturing partner; Saga owns the product definition, firmware branding (including the private MIB) and after-sales. The firmware you receive is built for Saga and does not carry third-party OEM identifiers." 合规部门追问以 Peter 2025-03-25 的说明为准；不主动翻 2024 年「completely self-developed」旧话 |
| 堆叠 | 接入 AC5 **不堆叠**；可堆叠线 = CENTEC STH-2QX4DX48GP-HSI（≤8 台 / 360 Gbps，ST 许可） |
| 源码 / SDK / API | "source code mode is NEVER an option"；SKD 可谈；API/SDK 不卖；转介第三方（Joey）做 CKD/源码不背书 |
| L3 / 协议边界 | L2+（AC5 7.5）静态路由 v4/v6 + PIM-SM；L3 型号另有 RIP/OSPF；不做 NAT / 云管 / TSN / MPLS（AC5）/ SD-WAN / BFD / IP SLA / Cisco 私有协议 |
| 代理 / 分销身份 | 可与客户签区域分销（客户当 Saga 的代理，"after we get to know each other"）；Saga 自己不自称任何上游总代；不接触客户的下游（SI/ISP）；无海外分公司 |
| 第三方转介 | 可转介不背书；轨交 / 源码 / 云管三类一律转出（轨交 M12 → Inmax） |
| 对 MikroTik 用户 | 不比功能（RouterOS 脚本 / REST API / 云 NMS 我们没有），只说三件真事：OEM 贴牌 + 定制 Web GUI/默认配置、同为 Marvell Prestera、可作部分项目的替代；$130 级别 |
| 涨价 | PCB/RAM + 汇率，AC5 整线约 +$15 |
| 光模块 | 不单卖；随整机按 §5.1 价位 |
| Realtek 线 | 只在客户自己说 Realtek / 低价 / 功能简单时给；「management functions are even worse than Marvell」（Alan 原话） |
| 日本 / 美国政府 / 韩国 | PSE/VCCI 客户名义办费用自担；TAA/GSA 不满足；KC 客户方办 |
| 国内冲突 | 项目可能与 SmartByte 国内客户重叠（大型校园 / 运营商 / 无软件裸机）→ 标「待 Simon 判断冲突」，不推进（Q-49） |

### 9.6 FAQ 英文一句话（可直接贴）

- Lead time: "Standard models ship in 4–7 working days after payment, plus 4–7 days by express."
- Samples: "Samples are charged at unit price and fully deductible from your first bulk order."
- Warranty: "1-year warranty on commercial models (STC) and 3-year on industrial models (STI) and DIN power supplies, from the delivery date, with lifetime technical support."
- Payment: "T/T 50% deposit, balance before shipment; PayPal accepted with 5% fee."
- Spares: "2 free spare units per 100 pcs of the same model instead of RMA returns."
- OEM: "Logo, label, carton and Web-UI logo customization are free of charge; neutral packing available."
- Distributorship: "We are certainly open to discussing a distributorship after we get to know each other and see good cooperation."
- Export classification: "EAR99, NLR; HTS 8517.62.2990; country of origin China."

来源：`docs/reference/Saga品牌口径与宣传语录.md`、`docs/对外口径一致性_2026-10-24.md`、`docs/reference/Saga商务条款速查.md` §6–§9、`docs/Saga理念摘读_2026-10-23.md` A10/A25、`scripts/saga_clients/audit_ab.py`（banned phrases）。
