# Marvell 阵营品牌全景图与验证手册

**口径**：接入/汇聚层以太网交换机（L2 / L2+ / 轻 L3，1G–10G 为主），**不含中国大陆厂商**，重点台湾，其次欧洲、美国/加拿大，兼顾日本/韩国/以色列/印度/拉美/澳新。
**日期**：2026-09-21　**用途**：既是竞品地图，更是**客户名单来源**。

## 0. 置信度分级（请务必按这个读）

| 标记 | 含义 | 可怎么用 |
|---|---|---|
| ✅ 已证实 | 有公开可查证据（官方文档 / 内核代码 / 规格书 / 拆机图） | 可以直接写进话术和技术对比表 |
| ● 高概率 | 行业共识 + 规格指纹推断，我未拿到一手证据 | 内部参考，可用于提问，不要对外断言 |
| ○ 待验证 | 我不确定，列入核查清单 | 用第 6 节方法 10 分钟自查后再用 |
| ‡ | 已 EOL / 已停产，作**替换目标**而非竞争目标 | 替换型开发的富矿 |

> 一句话提醒：**没有任何一家厂商会主动宣传自己用什么芯片**。这份表的价值一半在名单，一半在第 6 节的验证方法。

---

## 1. 已证实使用 Marvell 的厂商（可直接引用）

| 厂商 | 国家 | 证据（可查） | 涉及芯片 | 对你的意义 |
|---|---|---|---|---|
| **MikroTik** | 拉脱维亚（欧盟） | MikroTik 官方帮助文档《Marvell Prestera switch chip features》逐型号列出 | 98DX3236 / 98DX3257 / 98DX226S / 98DX2528 / 98DX8332 / 98DX4310 | 核心对标对象，上一份手册已展开 |
| **Allied Telesis** | 日本/新西兰总部，美国总部在 Bothell, WA | Linux 内核 pinctrl 驱动补丁作者邮箱为 `alliedtelesis.co.nz`，补丁明确支持 **98DX3236 / 98DX3336 / 98DX4251** | Prestera DX（含集成 CPU 的 AC3 家族） | ⭐ **本轮最重要发现**。欧美 L2/L3 接入层老牌，英/德/北欧渠道深，价格 3–5×，大量老型号 EOL → 替换池 |
| **Edgecore（Accton）** | 台湾 | 其网络平台 SAF51001I 官方规格书："8 x RJ-45 GbE port for LAN, through **Marvell 98DX3236**" | 98DX3236（嵌入式 LAN 侧） | 证明台湾 ODM 体系熟 Marvell/CPSS；但其交换机主线是 Broadcom + SONiC，别当主攻 |
| **Marvell 官方参考设计** | — | RD-AC3X-48G4X2XL-A（98DX3257）、CPSS SDK 4.x | — | 整个生态的软件底座是 **CPSS + Linux**，你的谈资 |

### 由 Allied Telesis 引出的判断

Allied Telesis 的组合是"**欧美品牌 + Marvell + 自研固件（AMF/VCStack/EPSR 环网）+ 高价位 + 产品线长且老化严重（AT-8000/8800/9000、x230/x510/x600、CentreCOM 系列大批 EOL）**"。
这类组合对你意味着三件事：

1. 他们的**存量装机**是现成的替换清单（配置可以 1:1 迁移，VLAN/STP/LACP 概念一致）；
2. 他们的**在售价格**是你的价格锚（24 口 L3 PoE+ 在欧洲通常 €1,500–3,000 级）；
3. 他们的**渠道商**在德国、英国、北欧、澳新都有，正是你 A 类名单来源。

---

## 2. 台湾厂商全景（本轮重点）

### 2.1 先给结论：台湾厂商基本不是你的客户，但有三笔账值得算

- **不是客户的原因**：主流台厂（Moxa / PLANET / Zyxel / D-Link / Advantech / CTC Union / EtherWAN / ORing / Lantech）都是**自有研发 + 自有产线**（CTC Union 官网即写明 in-house R&D and factory in Taipei），他们从中国买低端整机的动机极低；且他们的卖点是品牌溢价与认证（EN50155 / IEC 61850-3 / IEC 62443-4-1 / UL / E-mark），这些你目前缺。
- **但值得算的三笔账**：
  1. **价格锚**：台湾工业 8 口 PoE DIN 导轨机在欧洲零售 €500–900；你同类进价约 US$110–140 → 中间有 3–4 倍空间，这是你"PLANET 的功能、MikroTik 的价格"定位的来源。
  2. **EOL 替换池**：D-Link DGS-1210/1510、Zyxel GS1900/GS2210、PLANET 老款 IGS/GS、Moxa EDS-405A/408A 等大批 EOS → 找还在维护这些设备的集成商，做 drop-in 替换。
  3. **抢渠道**：台厂欧洲官网的 "Where to buy / Distributors / Partners" 页面 = 你的 A 类名单。他们已经在卖同类产品、有客户、有仓库，只差一条更有价格竞争力的第二产品线。

### 2.2 台湾厂商清单

| 公司 | 主打 | 欧洲/北美存在感 | Marvell 可能性 | 对你的角色 | 建议动作 |
|---|---|---|---|---|---|
| **PLANET Technology** | 商业 + 工业 + 电力 + 安防全栈，SKU 极多 | 欧/中东/拉美强 | ○（混合 Realtek/Marvell） | 头号对标（功能定义者） | 抄规格、抄文档结构、抢其渠道 |
| **Moxa** | 工业标杆：铁路 EN50155、电力 IEC 61850-3、海事 | 全球 | ○ | 高端锚，不打正面 | 只打其老项目扩容/备件/项目配套 |
| **EtherWAN** | 工业/ITS/安防，美国 Anaheim + 台北厂 | 美/欧 | ○ | 竞品 + 渠道来源 | 抢其在 ITS 项目的位置 |
| **ORing** | 工业/ITS/铁路，自有 O-Ring + ERPS | 欧/中东 | ○ | 竞品 | 让出铁路/IP67/UL 项目 |
| **CTC Union** | 电信接入 + 工业，EN50155 / IEC 61850-3 / IEC 62443-4-1 | 欧/北美运营商 | ○ | 竞品，认证门槛高 | 关注其 EOL 与运营商项目 |
| **Lantech** | 工业 PoE + EN50155 + 车载 E-mark | 欧洲重 | ○ | 竞品，渠道密集 | 抢渠道；学其"行业 SKU"打法 |
| **Volktek** | ODM + 自有品牌双轨 | 欧/北美 | ●（ODM 常用 Marvell 平台） | 潜在第二供应源 | 可作为你 industrial 线的备份方案对标 |
| **Korenix** | 工业无线 + 交换 | 欧/亚洲 | ○ | 竞品（小） | 观察 |
| **Zyxel** | 商业/SMB + Nebula 云 | 欧/美强 | ○（混合） | 竞品，且云能力强 | 云是你的短板，避其正面 |
| **D-Link** | 商业/消费/SMB | 全球 | ○（混合） | 竞品 + 最大 EOL 替换池 | EOL 替换重点 |
| **Advantech（EKI）** | 工业/嵌入式 | 全球 | ○ | 竞品 | 项目配套 |
| **Nexcom / ATOP / ICP DAS / Axiomtek** | 工业垂直、串口/IO、嵌入式 | 欧/美 | ○ | 细分竞品 | 关注其 ISA/IEC 行业项目 |
| **Connection Technology Systems (CTS) / Handlink / Unex / Ruby Tech / Proscend** | 电信接入、muxponder、media converter、部分整机 ODM | 欧美运营商渠道 | ○ | 潜在 ODM 伙伴 | 若你需要台湾产线备份 |
| **Senao / EnGenius** | SMB 无线 + 交换 | 美 | ○ | 竞品（弱） | 观察 |
| **ADMtek / ASIX / Myson** | 芯片/接口 IP | — | — | 非品牌 | 不在范围 |

### 2.3 台湾厂商里"有可能变成客户"的窄门

- **贸易型台牌 / 海外销售公司**：部分中小台牌的海外销售公司（非工厂）会外包低端线。前提：你能提供 UL / IEC 62443 / 5 年质保 / 本地 RMA 的文件链。
- **台厂的欧洲分销商**（真正的金矿，见 §3.2）。
- **缺产品线的台系小品牌**：只有 8 口、没有 10G 上行、没有 PoE++ 的品牌 —— 你的 LT-IS6312XG（4×10G）和 PoE++ 是现成的补齐 SKU，可做小批量贴牌。

---

## 3. 欧洲（你的主战场之一）

### 3.1 品牌型（竞品 / 高端锚）

| 品牌 | 国家 | 定位 | Marvell | 关系 | 切入点 |
|---|---|---|---|---|---|
| **Hirschmann（Belden）** | 德国 | 工业标杆，Profinet / EN50155，价格 5–10× | ○ | 高端锚，不打正面 | 老项目扩容、备件、非核心网段 |
| **Westermo（Beijer）** | 瑞典 | 铁路/电力/能源，WeOS 自有系统，WeOS 环网 | ●（历史平台含 Marvell） | 高端锚 | 交付周期长的项目抢位 |
| **Phoenix Contact / Weidmüller / Helmholz** | 德国 | 工业自动化自有品牌，渠道极强 | ○ | 渠道型竞品 | 做他们的"以太网模块"补充 |
| **Lancom** | 德国 | 中小企业/政府/教育，德国渠道第一梯队，云管理强 | ○ | 竞品 | 避开其云强项，打本地 CLI/私有部署 |
| **bintec-elmeg / Funkwerk** | 德国 | 语音 + 网络 | ○ | 竞品（细分） | 项目配套 |
| **INSYS icom / Welotec / MB connect line** | 德国 | 工业远程维护/路由器 | ○ | 细分 | 配套交换机机会 |
| **Kontron** | 奥地利/德国 | 嵌入式/工业 | ○ | 竞品（弱） | 观察 |
| **MPL / NetModule / Diggelmann** | 瑞士 | 高可靠/车载/铁路 | ○ | 高端锚 | 让出 |
| **Teltonika Networks** | 立陶宛 | 工业 8G+2SFP，RMS 云，价格低（TSW212 MSRP US$129） | ○ | **价格型直接对手** | 用 4×10G / ERPS / PoE++ / DI-DO / 5 年保拉开 |
| **MikroTik** | 拉脱维亚 | ✅ Marvell | — | 主要对标 | 见上一份手册 |
| **Atlantis Land / Conceptronic / Sitecom / Nedis / Trust / Velleman** | 意大利/荷兰/比利时 | 分销商自有品牌（own-brand） | ○ | ⭐ **OEM 客户池** | 见 §3.2 |

### 3.2 分销商自有品牌（own-brand）＝ 你最佳 OEM 客户池

这类公司**不自己研发**，靠台湾/中国 ODM 贴牌，采购量稳定、决策快、最在意 MOQ 和定制响应速度 —— 正好是你的强项（SmartByte 无 MOQ + 可深定制 UI/功能）。

| 公司 | 国家 | 说明 | 优先级 |
|---|---|---|---|
| **Nedis** | 荷兰 | 欧洲最大的自有品牌消费电子/配件分销商之一，SKU 数万，有网络产品线 | A |
| **Deltaco** | 瑞典 | 北欧自有品牌，网络 + 配件，覆盖北欧零售 | A |
| **LogiLink（2direct）** | 德国 | 自有品牌分销，网络/配件，渠道广 | A |
| **Intellinet（IC Intracom）** | 美国/德国 | 自有品牌网络配件 | A |
| **Equip / LevelOne（Digital Data Communications）** | 德国/台湾 | 自有品牌，交换机线完整 | A |
| **Conrad / Reichelt / Distrelec（RS 集团）** | 德/德/瑞士 | 大分销，均有自有品牌 + 招商采购 | A |
| **Delock / Roline / Value** | 德/瑞士 | 自有品牌 + 贸易 | B |
| **Kjell & Company** | 瑞典 | 北欧零售连锁 + 自有品牌 | B |
| **Allnet / Logilink 类中小贸易品牌** | 德语区 | 大量中小自有品牌 | B |

> **怎么继续扩充这张表**（每个国家都能复制）：搜 `网络交换机` + `自有品牌` / `own brand switch distributor` + 国家；或直接去当地大分销/电商站，把"自有品牌"栏目里所有网络产品记下来，反查公司官网的 "Become a supplier"。德语区、荷兰、北欧最密集，法国/西班牙/意大利相对少但单量大。

### 3.3 中东欧（上一份手册的 T1 国家，这里补品牌线索）

波兰、捷克、斯洛伐克本地几乎没有交换机品牌，市场由 ① 台厂 + ② 西欧品牌 + ③ 中国白牌 三分。所以这里的开发逻辑不是"找品牌"，而是**找正在从中国进口的分销商和集成商**（用海关数据，见开发手册 §2 第 10 条）。

---

## 4. 美国 / 加拿大

| 品牌 | 国家 | 定位 | Marvell | 关系 | 切入点 |
|---|---|---|---|---|---|
| **Allied Telesis** | 美国（Bothell, WA） | ✅ 已证实 Marvell；L2/L3 接入，AMF/VCStack/EPSR | ✅ | 竞品 + 最大替换池 | 老型号 EOL 替换、渠道 |
| **Ubiquiti UniFi** | 美国 | 价格型巨头；USW 系列用 **Realtek**（USW-Aggregation 被社区确认为 RTL9303） | ✘ Realtek | 价格对手 | 打"不想被控制器锁定"的客户 + CLI/SNMP/ERPS |
| **Netgear** | 美国 | 商业 + AV 线（M4250/M4300）强势 | ○ | 竞品 | 避开 AV 线，打 PoE 管理/工业 |
| **Transition Networks** | 美国（MN） | 工业/电信接入 + 媒体转换 | ○ | 竞品 | 项目配套 |
| **Antaira** | 美国（台系 ODM） | 工业，价格中低 | ○ | 直接对手 | 同价位比规格与质保 |
| **Red Lion / N-Tron / Sixnet** | 美国（HMS 集团） | 工业自动化 | ○ | 竞品 | 配套 |
| **GarrettCom（Belden）** | 美国 | 工业现场/变电站 | ○ | 高端锚 | 备件/扩容 |
| **B&B SmartWorx / Advantech B+B** | 美国 | 工业 | ○ | 竞品 | 配套 |
| **ComNet（ACRE）** | 美国 | 安防传输专用 | ○ | 细分竞品 | 安防项目 |
| **Cambium cnMatrix** | 美国 | WISP + 企业，云管理 | ○ | 竞品 | WISP 场景正面打 |
| **EnGenius / Grandstream** | 美（台/美） | SMB 无线 + 交换 | ○ | 竞品（弱） | — |
| **Perle Systems** | **加拿大（多伦多）** | 工业交换机 + 串口设备服务器 + 媒体转换，做工控/ITS/交通 | ○ | 竞品，也可做互补 | 你的 RS485/DI-DO + PoE++ 正好补其空白 |
| **StarTech.com** | **加拿大（多伦多）** | 配件自有品牌巨头，有工业/网络产品 | ○ | ⭐ OEM 客户池 | 走"自有品牌 + 低 MOQ + 定制"路线 |

> **加拿大提醒**：CASL 反垃圾邮件法极严（需明示或默示同意，罚款可达 CAD $1,000 万/条）。加拿大客户**优先用 LinkedIn / 电话 / 展会**接触，邮件只在有"默示同意"依据（对方公开的企业邮箱 + 内容与其职务相关）时发，且必须留痕。详见开发手册 §11。

---

## 5. 其他国家（机会清单，非主攻）

| 地区 | 品牌 | 说明 | 价值 |
|---|---|---|---|
| 日本 | **NEC（UNIVERGE / ProgrammableFlow）** | ● Marvell 概率高，日本政企市占高 | 日本市场难进，观察；但其 EOL 机型在东南亚有存量 |
| 日本 | Yamaha（SWX / RTX）、Buffalo、Contec、Omron | 中小企业/工业 | 观察 |
| 韩国 | Ubiquoss、Dasan(DZS)、Ubiquoss、Handysoft | 运营商接入为主 | 观察 |
| 以色列 | RAD、Telco Systems（现 Ribbon）、Siklu | 运营商/无线 | 观察 |
| 印度 | **MRO-TEK**、Syrotech、本地集成商 | PLI 制造政策、进口替代 | 中长线：本地化组装/散件机会 |
| 巴西 | **Intelbras**（安防/网络巨头，大量中国 OEM）、Datacom、Furukawa 拉美 | 拉美最大市场 | ⭐ Intelbras 这类"自己设计但大量外采"的公司是好客户 |
| 澳新 | Netcomm、本地 ITS 集成商 | — | 用 T2 方式慢慢做 |
| 土耳其 | 本地集成商为主 | 已有 NMS 集成案例 | 复制土耳其案例 |

---

## 6. 验证手册：10 分钟判定一家公司用什么芯片

> 不要相信论坛和 AI 的"某某用 Marvell"。用下面 7 招，按性价比排序。

**第 1 招｜FCC ID 内部照片（最快，3 分钟）**
`fccid.io` 或 `fcc.report` 搜公司名 → 打开设备条目 → **Internal Photos** → 看主芯片丝印。
- `98DX…` / `88E6…` / `88E6190` / `88E6390`（8+2 口形态）= **Marvell**
- `RTL93xx` / `RTL83xx` / `RTL8218` = Realtek
- `BCM5xxxx` / `BCM56xxx` = Broadcom
- 顺便能看到 PoE PSE 芯片（如 `PD69xxx`、`MP3924`、`TPS2388`）、内存、闪存、PCB 层数 —— **一份拆机图=竞品 BOM 估算**。

**第 2 招｜GPL / 开源代码包（5 分钟，证据最硬）**
公司官网 → Support → **GPL / Open Source / Source Code** → 下载固件源码 → `grep -ri "98DX\|prestera\|cpss\|mv88e6\|rtl93"`
（GPL 要求厂商公开 Linux 相关源码，这是上市公司和欧美大厂几乎都会遵守的。）

**第 3 招｜固件镜像解包（15 分钟）**
`binwalk -Me firmware.bin` → 看 `/etc/`、`*.dts`、内核 config、`/lib/modules`。
出现 `mvpp2`、`prestera_pci`、`mv88e6xxx`、`marvell` 即实锤。

**第 4 招｜UART 串口（有样机时，2 分钟）**
拆机找 4 针（VCC/GND/TX/RX）→ USB-TTL → 115200 8N1 → 看 u-boot 打印。
Marvell 平台常见 `Marvell>>` 提示符、`Board: RD-AC3X`、`98DX` 字样。

**第 5 招｜SNMP / 私有 MIB（不拆机，5 分钟）**
抓 `sysObjectID`（1.3.6.1.2.1.1.2）与私有 enterprise OID；下载厂商 MIB 包搜索 `Marvell / Prestera / 98DX / RTL`。

**第 6 招｜"规格指纹"反推（0 分钟，粗判）**

| 指纹 | 大概率 |
|---|---|
| 24×GE + 2×10G SFP+ 一体、VLAN 表 128–4K、MAC 上限 16K、带集成 ARM CPU | Marvell Prestera AC3（98DX3xxx） |
| 8×GE + 2×SFP/1-2×SerDes、轻量管理、CPU 集成 200 MHz | Marvell Link Street 88E6390/6190 |
| 8K–16K MAC、512 KB 包缓存、4096 VLAN、10G 口 storm control 有已知 quirk | Realtek RTL93xx |
| 32K MAC、4096 VLAN、全套 L3 + 堆叠 | Broadcom |

**第 7 招｜直接问（最实用）**
对经销商/工程商说：*"你们这条 L2+ 线是 CPSS（Marvell）还是 Realtek SDK？我们同平台做过，可以给你做第二供应源和 pin-to-pin 替代。"*
工程师比销售诚实，命中率约五成。

---

## 7. 优先级：先打谁

### A 类（本月启动，做 OEM/贴牌为主，12 家）
Nedis（NL）、Deltaco（SE）、LogiLink/2direct（DE）、Intellinet/IC Intracom（DE/US）、Equip/LevelOne（DE）、Conrad 自有品牌（DE）、Distrelec（CH）、StarTech（CA）、ComNet（US）、Antaira（US，竞争+互补）、Intelbras（BR）、Teltonika 互补线（LT，缺 10G/PoE++/ERPS）。

### B 类（替换池，做存量替换）
Allied Telesis（US/EU，✅ Marvell，大量 EOL）、D-Link、Zyxel、Netgear、PLANET 老型号 —— **打的是"正在维护这些设备的集成商"**，不是品牌方。

### C 类（观察/配套）
Moxa、Westermo、Hirschmann、Phoenix Contact —— 不打产品，打备件、扩容、非核心网段、项目配套。

### 不做
Cisco / Aruba / Juniper / Extreme / Arista / Dell（Broadcom/自研，客户群与决策链完全不同）；铁路 IP67 / UL 强制项目。

---

## 8. 最后三句提醒

1. **不要对外讲"我们和 MikroTik 同芯片"。** 客户不买芯片。同平台的正确用法是：你能预判对手的能力上限和已知 bug（例如 98DX3236 在 10G 口上的 egress-rate/storm-control 限制），把它变成技术话术；以及迁移成本低（CLI/MIB 概念一致）。
2. **真正的客户不在"Marvell 阵营"里，在"没有研发、但有品牌和渠道"的公司里。** 分销商自有品牌（own-brand）和缺产品线的区域品牌，才是低 MOQ + 深定制的价值兑现处。
3. **Allied Telesis 值得单独做一页竞品卡**：✅ Marvell、欧美渠道深、价位高、EOL 机型多、EPSR 环网（对标你的 ERPS）。它的存量装机是你未来 12 个月最容易的替换目标。
