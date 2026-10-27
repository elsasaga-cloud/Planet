# MikroTik 类客户切入深度分析（2026-09）

> 依据：本仓库全部文件（GPT 讨论记录、MikroTik 抓取 Excel、Saga Feature List 7.5.x L2+/L3、Marvell CLI/Web 手册、SmartByte 2026.09–12 价格表）+ SmartByte 官网实测（2026-09）+ MikroTik 官网/文档实测（2026-09）。
> 所有价格：MikroTik = 官网 Suggested price（MSRP）；SmartByte = 你手上的未税 RMB 进价。美元换算按 **7.10** 估算，可在配套 Excel 里改。

---

## 0. 先纠正几个关键事实（比继续讨论打法更重要）

### 0.1 你给的链接是 **CSS326**，不是 CRS326 —— 两个东西差一个数量级

| | **CSS326-24G-2S+RM**（你发的链接） | **CRS326-24G-2S+RM**（Frank 邮件里的） |
|---|---|---|
| MSRP | **$159** | **$209** |
| 操作系统 | **SwOS only**（纯 Web UI） | RouterOS / SwOS 双启动 |
| 交换芯片 | Marvell **98DX3216** | Marvell 98DX3236 |
| CPU / RAM / Flash | 无独立 CPU 描述 / — / **2 MB** | ARM 双核 800MHz / 512MB / 16MB |
| CLI / SSH / Telnet | **无** | 有（RouterOS） |
| 串口 Console | **无** | RJ45 |
| SNMP | v1/v2c **只读**，**无 Trap**，不能写配置 | v1/v2c/v3、Trap、可写 |
| LLDP | **不支持**（只有 MNDP） | 支持 LLDP/CDP/MNDP |
| 生成树 | **仅 RSTP** | STP/RSTP/MSTP（硬件） |
| VLAN / ACL 上限 | **250 VLAN / 32 条 ACL** | 4K / 硬件 ACL |
| L3 | **无**（连默认网关都没有） | 静态/动态路由，98DX3236 支持基础 L3 硬件卸载（不支持 NAT/Fasttrack 卸载） |
| ERPS G.8032 | 无 | **无**（论坛 2013 年起 feature request，至今未实现） |
| QinQ | 无 | **有**（802.1ad provider bridge，CRS3xx 硬件卸载） |
| PoE | PoE-in 被动供电（给自己） | PoE-in 被动供电（给自己） |
| 温度 | -20 ~ 70°C | **-40 ~ 60°C** |
| 认证 | CE / EAC / RoHS | CE / EAC / RoHS |

**结论：**
- 如果客户拿 **CSS326** 比，你的 **LT-S8328XG-4XS24GT-S**（进价 RMB 710 ≈ $100，卖 $130）是**降维打击**：价格更低、4×10G 上联、完整 CLI/SSH/SNMPv3+Trap/LLDP/ERPS/QinQ/静态路由/MQTT。CSS326 一旦要接 NMS 就是死穴（没 Trap、SNMP 只读、无 LLDP）。
- 如果客户拿 **CRS326（RouterOS）** 比，规格战没意义 —— RouterOS 有 QinQ、MSTP、L3 卸载、脚本、API。**唯一硬差异是 ERPS、4×10G、PoE++ 产品线、工业款、OEM。**
- GPT 之前那张对比表里写 CRS326 "QinQ 有限 / L3 有限 / ERPS ❌"，其中 QinQ 和 L3 是**错的**，别拿去跟 RouterOS 用户讲，会被当外行。

### 0.2 你 Excel 里的芯片数据有几处需要修

| 型号 | 你的 Excel | MikroTik 官网 |
|---|---|---|
| CSS326-24G-2S+RM | 98DX3236 | **98DX3216** |
| CSS610-8G-2S+IN | 一行 98DX3236、一行 88E6193X | **88E6193X**（SwOS Lite，64KB flash） |
| CSS610-8G-2S+IN 价格 | $89 / $119 两行 | **$119** |
| CRS326-24G-2S+RM 价格 | $219 | **$209** |
| CRS328-24P-4S+RM 价格 | $499 / $489 两行 | **$489** |

另外同一型号因为两种 slug（`CRS326-24G-2SplusRM` 与 `crs326_24g_2s_rm`）被抓了两遍，导致 72 行里有十几行重复、价格不一致。建议按 product_code 去重，以在线抓取值为准。

### 0.3 SmartByte 官网 2026 年已经彻底改版 —— GPT 那句"营销偏弱"过时了

现在官网首页标语就是 **"Custom Marvell-Based Ethernet Switch OEM/ODM Solutions"**，并且新增：
- **White Box Hardware** 系列（10G / 25G / 100G Uplink）
- **SKD & CKD** 页面
- **Firmware Update Highlights** 公开 release notes（5.x → 7.5.x，含 hotfix 级别）
- OEM/ODM 页明确：**软件定制 No MOQ**（Logo、型号、SN、登录 IP、MAC、**SNMP OID**）
- 工业款 5 年保修、商业款 3 年
- 产品页有完整 Product selector（按 L3/L2+/Bypass/Boost/DI-DO-RS485/温湿度传感器筛选）

这意味着两件事：
1. **话术可以直接借用**，你不用再自己"包装"；
2. **去中介化风险明显上升**。Frank 这种人会 Google，"Marvell OEM switch" 一搜就到 SmartByte。第 8 节专门讲你作为贸易商的价值怎么立住。

### 0.4 温度是个坑：商业款 0~50°C，会被 CRS326 反杀

CRS326 标称 -40~60°C，CSS326 -20~70°C；你的 **商业款 LT-S8328XG 只有 0~50°C**。WISP 的塔站机柜、户外箱、SIMREX 的交通机柜，一问温度你就输。**对 WISP / ITS / 工业客户必须直接推工业款（LT-IS6xxx：-40~75°C、IP40、DIN 导轨、双 DC 12–58V、IEC 61000-4 系列 EMC、MTBF>200k h、5 年保修）**，别拿商业款去比。

### 0.5 "没 UL" 不是相对 MikroTik 的劣势

MikroTik 交换机也只有 CE/EAC/RoHS。SmartByte 有 CCC/CE/UKCA/RoHS/REACH/FCC，实际比 MikroTik 还多一项 FCC。这条在你的 SWOT 里可以划掉（对 MikroTik 客群而言）。

---

## 1. 三者一张表（24 口接入这一档）

| 维度 | CSS326-24G-2S+RM | CRS326-24G-2S+RM | **SmartByte LT-S8328XG-4XS24GT-S** |
|---|---|---|---|
| 你的成本 / 对方 MSRP | $159 | $209 | **RMB 710 ≈ $100 进价 → 建议售价 ~$130** |
| 上联 | 2×SFP+ | 2×SFP+ | **4×SFP+（1G/2.5G/10G 自适应）** |
| 交换容量 | 88 Gbps | 88 Gbps | 128 Gbps / 190 Mpps |
| CPU / RAM / Flash | — / — / 2MB | ARM 2×800MHz / 512MB / 16MB | Marvell AC5 1.2GHz / 512MB / 512MB |
| 管理 | Web only | Web/Winbox/CLI/SSH/API/REST | Web/HTTPS、Cisco 风格 CLI、Console、Telnet/SSH（含公钥登录） |
| SNMP | v1/v2c 只读，无 Trap | v1/v2c/v3 + Trap | v2c/v3 + Trap + RMON + sFlow + **私有 OID 可定制** |
| 主动上报 | 无 | Syslog/Trap/脚本 | Syslog(3 服务器)/Trap/**MQTT**/Dying Gasp/Relay 告警 |
| 环网 | RSTP | STP/RSTP/MSTP | STP/RSTP/MSTP + **ERPS G.8032 <20ms（主环/子环）** |
| L3 | 无 | 静态/动态路由 + 基础 HW 卸载 | IPv4/IPv6 静态路由、DHCP Server/Relay |
| QinQ | 无 | 有 | 有（端口/VLAN/流三种） |
| 安全 | 32 条 ACL、Port lock | 完整 | ACL(时间段)/802.1X/MAC 认证/DHCP Snooping/IPSG/DAI/AAA(RADIUS+TACACS) |
| 文件传输 | Web 备份 | FTP/SFTP/SCP | TFTP/FTP/**SCP/SFTP**、双分区固件 |
| 温度 | -20~70°C | -40~60°C | **0~50°C（商业款短板）** |
| 保修 | 1 年（欧盟 2 年） | 1 年（欧盟 2 年） | **3 年**（工业款 5 年） |
| 软件更新承诺 | 产品寿命或≥5 年 | 同左 | 公开 release notes，7.x 持续迭代 |
| OEM | 不可能 | 不可能 | **软件定制 No MOQ** |

---

## 2. MikroTik 交换机生态"真实的空白"（可验证，不是拍脑袋）

按可验证程度排序，这些是你能拿到台面上讲的：

| # | 空白 | 证据 | 你能补什么 |
|---|---|---|---|
| 1 | **ERPS G.8032 不支持** | 论坛 feature request 2013、2015 年起，RouterOS 至今只有 (R/M)STP | ERPS 主环/子环，<20ms；对 ISP 光纤环、交通/电力环网是刚需 |
| 2 | **802.3bt PoE++ 几乎没有** | CRS328-24P-4S+ 是 af/at 450W；CRS354-48P af/at；只有 CRS320-8P-8B 的 8 个"B"口是 bt | 工业 8 口 90W×8/480W 预算（LT-IS6312GP-4GX8GT-8BT）、-2BT/-4BT 变体、PoE 看门狗(PD Alive)、PoE 定时、优先级、告警阈值 |
| 3 | **没有工业 DIN 导轨管理型交换机** | MikroTik 无 DIN 导轨、双 DC、-40~75°C、IEC 61000-4 等级的管理型交换机；netPower 是户外反向 PoE 产品 | LT-IS3xxx/6xxx 全线；DI/DO/RS485 串口服务器；光纤 Bypass；温湿度传感器；Boost PoE |
| 4 | **SwOS（CSS）线管理能力极弱** | 无 CLI/SSH/LLDP/Trap、SNMP 只读、250 VLAN/32 ACL | 客户从 CSS 升级到"能进 NMS 的交换机"时，你比 CRS 便宜 |
| 5 | **不做 OEM/白牌** | MikroTik 只卖自己品牌（RouterBOARD 裸板给集成商是另一回事） | 软件定制 No MOQ、外壳/包装/SKD/CKD |
| 6 | **NMS 集成友好度** | RouterOS 强，但 MikroTik 私有 MIB 覆盖有限；SwOS 无 Trap | 标准 MIB + 私有 MIB（CPU/内存/温度/光模块 DDM/PoE/风扇）、Trap 列表、MQTT、sFlow、RMON |
| 7 | **保修** | 1 年（欧盟法定 2 年） | 商业 3 年 / 工业 5 年 |
| 8 | **供货记忆** | 2021–2023 芯片荒时 MikroTik 交换机长期缺货，WISP 群体记忆犹新 | "Supported by Marvell original factory" + 芯片库存 + 快交期是可讲的 |

---

## 3. MikroTik 的护城河 —— 不要碰的地方

| 不要碰 | 原因 |
|---|---|
| RouterOS 软件能力（脚本、API、REST、Winbox、The Dude、CAPsMAN） | Frank 说的 "throughput tests to MT wireless devices" 就是 RouterOS `/tool bandwidth-test`；你没有对等物，承认它 |
| 路由器业务（CCR / RB / hAP） | 完全不同赛道 |
| 全 SFP+ 汇聚 | CRS309-1G-8S+ $229（8×SFP+）、CRS317-1G-16S+ $499（16×SFP+）、CRS326-24S+2Q+ $599；SmartByte 价格表里没有对等的全 10G 盒子 |
| 25G / 100G | CRS504-4XQ $499、CRS510 $599，价格离谱；White Box 100G 系列打不过 |
| 8 口价格底线 | CSS610-8G-2S+ $119、CRS305-1G-4S+ $149；你商业 8 口 L2+（LT-S8310G RMB 380）目前"成本回落前暂停出货" |
| 全光 SFP 边缘 | CRS328-4C-20S-4S+ $299（20 SFP + 4 Combo + 4 SFP+）；你对应 LT-IS6328XG-4XS16GX8GC-D RMB 2650 ≈ $373 —— MikroTik 便宜一半 |
| Homelab / 个人 / 论坛群体 | 价格极敏感、品牌忠诚、非你的客户 |

**一句话定位（对外）：**
> *Keep your MikroTik routing platform. Upgrade your switching layer where MikroTik doesn't go: ERPS rings, PoE++ budgets, industrial DIN-rail, integration-ready SNMP/MQTT, and your own brand.*

---

## 4. MikroTik 客群分层与切入打法（核心）

### 4.1 类型 A：WISP / 小型 ISP 运营商（用 MikroTik 做路由，交换机"能用就行"）

- **画像**：MikroTik CCR/RB 做核心和 PPPoE，塔站/机柜里用 CRS3xx 或 CSS 做接入，Ubiquiti/Cambium/MikroTik 无线混用。欧洲典型：波兰、捷克、意大利、西班牙、德国乡村；美国 WISPA 会员。
- **痛点**：塔站 -40°C；48V DC 直流供电（CRS 是 10–30V 被动 PoE-in，得配转换）；光纤环路只能靠 RSTP（大环收敛数秒）；给 AP/CPE 供电要 PoE++；CSS 没 Trap 接不了 LibreNMS/Zabbix。
- **切入 SKU**（都用工业款）：
  - 塔站小节点：**LT-IS6312XG-4XS8GT**（8G + 4×10G SFP+，RMB 840 ≈ $118）/ PoE 版 **-4XS8GT** RMB 920 / **-2BT** RMB 1020
  - 更小：**LT-IS6310G-2GX8GT**（8G + 2×2.5G SFP，RMB 700 ≈ $99）
  - 汇聚点：**LT-IS6328XG-4XS24GT-D**（24G + 4×10G + DI/DO/RS485，RMB 1960）
- **价格锚**：不要跟 CRS305/CSS610 比 8 口价格，比"塔站总成本"：工业 DIN + 双 48V 直流输入 + 4KV 浪涌 + -40~75°C，省掉他们自己做的机柜加固、DC-DC 转换和 PoE 注入器。
- **话术**：*"Your CRS handles routing; our industrial switches handle the tower — dual 12–58V DC input, -40~75°C, ERPS ring, and PoE++ for your radios. SNMP traps and LLDP go straight into your LibreNMS/Zabbix."*
- **渠道**：LinkedIn 关键词 `WISP` `Wireless ISP` `fixed wireless` `MTCNA` `MTCRE` `RouterOS`；美国 WISPA 会员名录；波兰 KIKE 会员；MikroTik 官网 `mikrotik.com/consultants` 公开的顾问名单（这些人给几十家 WISP 做集成）。

### 4.2 类型 B：MikroTik 分销商 / 经销商 / 培训机构

- **画像**：`mikrotik.com/buy` 按国家列出的官方分销商和经销商。他们不只卖 MikroTik，还卖 Ubiquiti、Cambium、TP-Link Omada、光模块、机柜；很多有自己的"house brand"配件线。
- **痛点**：MikroTik 不给 OEM、利润薄、PoE++/工业需求接不住只能转给 PLANET/ORing（贵）。
- **切入方式**：**卖"house brand 交换机线"而不是卖交换机**。SmartByte 软件定制 No MOQ（Logo/型号/SN/登录 IP/MAC/SNMP OID）+ 外壳丝印 + 包装 —— 让分销商用 20–50 台起步做自己品牌的 PoE++/工业/ERPS 系列，补 MikroTik 目录的空白。
- **首推 SKU**：LT-S8328XG-4XS24GT-S（$130 卖价对标 CRS326 $209）+ LT-S8328XGP-4XS24GT-S（24 PoE + 4×10G，280W，RMB 1010 ≈ $142）+ 工业 8 口 PoE++。
- **话术**：*"We don't compete with your MikroTik line — we fill the gaps in it, under your brand, with no software MOQ."*

### 4.3 类型 C：自建 NMS / 云平台的方案商（Frank / SIMREX 型）—— 价值最高

- **画像**：有自己的 Cloud NMS、脚本、行业客户（ITS/SCADA/公用事业）；硬件是"节点"。Frank 说的 6/12 口 $90–120 "including hardened metal packaging"，对应的很可能是 **CRS106-1C-5S（6 口，$89）/ CRS112-8G-4S-IN（12 口，$119）** 这类老款 QCA 芯片 RouterOS 小交换机 + 他自己做的加固外壳。
- **你的直接对位**：
  - 6 口：**LT-IS6306G-2GX4GT**（4G + 2×SFP，RMB 660 ≈ $93）
  - 12 口：**LT-IS6312G-4GX8GT**（8G + 4×SFP，RMB 740 ≈ $104）或 **LT-IS6312XG-4XS8GT**（4×10G，RMB 840）
  - 这两款**出厂就是 IP40 金属 DIN 导轨、双 DC、-40~75°C、IEC 61000-4 EMC** —— 他的 $90–120 里包含了他自己的加固工作，你的进价 $93–104 已经加固完。加你 30% 后 $120–135，跟他持平，但他省了加固工时和二次品控。
- **杀手锏（GPT 没发现的）**：Web 手册里有 **Serial Server（RS485 串口服务器）** 和 **IO Control（DI/DO）**。SIMREX 做交通/ITS/SCADA —— 交通机柜里大量 RS-485 旧控制器、门磁/温度干接点。**一台交换机同时承载以太网 + 串口透传 + 干接点告警**，这是 CRS 做不到、且正中他行业的。对应型号带 `-D` 后缀（LT-IS6320G-4GX16GT-D、LT-IS6328XG-4XS24GT-D 等）。
- **NMS 集成三件套**（他要的 "API" 在第一阶段其实是这个）：
  1. SNMP v2c/v3 + 完整 Trap（linkUp/Down、PoE 状态、电源、温度、ERPS 状态）+ 私有 MIB（CPU/内存/光模块 DDM/风扇）
  2. **MQTT**（L2+ 7.5.x Feature List 已勾选）—— 设备主动向云端发布遥测，天然穿 NAT/防火墙，正对他吹的 "discovery works through gateways and firewalls"。**需要向 SmartByte 索要 MQTT topic/payload 文档。**
  3. Cisco 风格 CLI + SSH 公钥登录 + SCP/SFTP + 双分区 —— netmiko/Ansible 直接能用，批量升级安全
- **不要做**：承诺 REST API（现在没有）。可以说 "REST API is on the customization roadmap for OEM partners" —— 前提是先问过 SmartByte。

### 4.4 类型 D：用 CRS 当"便宜管理交换机"的工业 / 安防集成商

- **画像**：CCTV 工程商、工厂 SI、市政项目商。买 CRS326/CRS328-24P 是因为便宜 + 有管理，不用 RouterOS 高级功能。
- **痛点**：项目要 ERPS 环、PoE++（球机/PTZ/无线回传）、宽温、5 年保修、投标要"工业级"字样。
- **切入**：直接工业款替换 + 5 年保修 + ERPS + PoE 看门狗（摄像头死机自动断电重启，CRS 没有）。
- **价格锚**：CRS328-24P-4S+RM $489（af/at，450W，-20~60°C，2 风扇）vs 你的 LT-S8328XGP-4XS24GT-S（280W）RMB 1010 ≈ $142 / 工业 LT-IS6328XGP-4XS24GT RMB 2200 ≈ $310（-4BT 版 RMB 2400）。

### 4.5 不要碰：Homelab / 个人 / 论坛

forum.mikrotik.com、r/mikrotik 对厂商推销极其反感，只会招黑。这些地方只做"倾听"（看抱怨 → 提炼痛点）和被动曝光（见第 7 节 LibreNMS 模板打法）。

---

## 5. 型号替代对照（摘要，完整版见配套 Excel）

| MikroTik | MSRP | 最接近的 SmartByte | 进价 RMB | ≈进价 USD | 建议售价(+30%) | 你赢在 | 你输在 / 注意 |
|---|---|---|---|---|---|---|---|
| CSS326-24G-2S+RM | $159 ✅ | LT-S8328XG-4XS24GT-S | 710 | $100 | $130 | 全面碾压：4×10G、CLI/SSH、Trap、LLDP、ERPS、L3 | 温度 0~50 vs -20~70 |
| CRS326-24G-2S+RM | $209 ✅ | LT-S8328XG-4XS24GT-S | 710 | $100 | $130 | 4×10G、ERPS、MQTT、3 年保修、OEM | RouterOS 生态、-40°C |
| CRS326-24G-2S+IN（桌面） | $199* | LT-S8328G-4GX24GT-S（4×2.5G SFP） | 460 | $65 | $84 | 价格 | 上联只有 2.5G |
| CRS328-24P-4S+RM | $489 ✅ | LT-S8328XGP-4XS24GT-S（280W） | 1010 | $142 | $185 | 价格、PoE 看门狗/定时、ERPS | PoE 预算 280 vs 450W；440W 版只有 2.5G 上联(LT-S8328GP-4GX24GT RMB 1200) |
| CRS328-24P-4S+RM（工业替代） | $489 | LT-IS6328XGP-4XS24GT / -4BT | 2200 / 2400 | $310 / $338 | $403 / $439 | -40~75°C、PoE++、DIN、5 年 | 贵 |
| CRS354-48G-4S+2Q+RM | $599* | LT-S8352XG-4XS48GT | 1470 | $207 | $269 | 价格、ERPS | 没有 40G QSFP+ |
| CRS354-48P-4S+2Q+RM | —* | LT-S8352XGP-4XS48GT（440W/850W 可选） | 1870 | $263 | $342 | 850W 选项、PoE 管理 | 没有 40G |
| CSS610-8G-2S+IN | $119 ✅ | LT-S8310XG-2XS8GT（8G + 2×10G） | 待询价 | — | — | 全管理 | 商业 8 口 L2+ 目前暂停出货 |
| CSS610-8P-2S+IN | $139* | LT-S8310GP-2GX8GT（120W） | 450 | $63 | $82 | 价格、PoE 管理 | 上联 2.5G SFP 非 10G |
| CRS106-1C-5S（Frank 6 口） | $89* | LT-IS6306G-2GX4GT（工业） | 660 | $93 | $121 | 已加固、双 DC、-40~75、ERPS | 4 电口 vs 5 光口，形态不同 |
| CRS112-8G-4S-IN（Frank 12 口） | $119* | LT-IS6312G-4GX8GT（工业） | 740 | $104 | $135 | 同上 + 4×2.5G SFP | 略贵 |
| CRS112-8P-4S-IN | $199* | LT-IS6312GP-4GX8GT / -2BT | 820 / 920 | $115 / $130 | $150 / $169 | PoE++ 选项、工业 | — |
| CRS310-8G+2S+IN（8×2.5GbE） | $149* | 无对等（你没有 2.5G 电口） | — | — | — | — | 放弃 |
| CRS310-1G-5S-4S+IN | $195* | LT-IS6316XG-4XS4GX8GT（8G+4SFP+4SFP+） | 1400 | $197 | $256 | 工业、ERPS | 贵、形态不同 |
| CRS318-16P-2S+RM / netPower 16P | $329* | LT-IS6318XGP-2XS16GT（工业） | 1660 | $234 | $304 | 工业、PoE 管理 | 贵；netPower 是户外反向 PoE，不同物种 |
| CRS320-8P-8B-4S+RM（8 at + 8 bt） | $299–489* | LT-IS6320GP-4GX16GT-D-4BT | 1960 | $276 | $359 | DI/DO/RS485、工业 | 只有 4 个 bt 口 |
| CRS328-4C-20S-4S+RM | $299* | LT-IS6328XG-4XS16GX8GC-D | 2650 | $373 | $485 | 工业 | **MikroTik 便宜一半，放弃** |
| CRS305 / CRS309 / CRS317 / CRS326-24S+2Q+ / CRS5xx | $149–749 | 无对等 | — | — | — | — | **全 SFP+/25G/100G 放弃** |

✅ = 2026-09 官网实测；* = 你抓取的数据，建议核实。

---

## 6. 对 Frank / SIMREX 的回复建议（基于新发现）

**思路变化：**
1. 承认 CRS 比较合理，并明确指出你之前的 $1500 是核心层，不同赛道；
2. 直接给 6/12 口的工业对位型号（他现在最在用的规格），强调"出厂即加固"；
3. 抛出 **RS485 串口服务器 + DI/DO + ERPS** 这三个正中 ITS 场景的点；
4. 把 "API" 落地成 **SNMP Trap + 私有 MIB + MQTT + SSH/SCP 自动化**，并问清他现有 NMS 用什么协议采集；
5. 提出寄样，不谈大单。

**英文草稿（短，工程师风格）：**

> Hi Frank,
>
> Fair point on the CRS326 — the $1,500 unit I shared earlier is our L3 core/aggregation platform, a different category. For what you actually run (6- and 12-port hardened nodes), the closer match is our industrial L2+ line:
>
> - 6-port: LT-IS6306G (4×GbE + 2×SFP) · 12-port: LT-IS6312G (8×GbE + 4×SFP) or LT-IS6312XG (4×10G SFP+)
> - Ships already hardened: IP40 metal DIN-rail, dual 12–58 VDC inputs, -40~75 °C, IEC 61000-4 surge/ESD, 5-year warranty — so nothing to re-package on your side. Marvell Prestera silicon, same family as CRS3xx.
>
> Three things MikroTik switches don't do that matter for ITS/SCADA cabinets:
> 1. G.8032 ERPS ring, <20 ms failover (RouterOS is still RSTP/MSTP only)
> 2. Built-in RS-485 serial server + DI/DO dry contacts on the -D models — legacy controllers and cabinet alarms ride the same box
> 3. 802.3bt 90 W PoE++ with PD watchdog (auto power-cycle a hung radio/camera) and PoE scheduling
>
> On integration: SNMP v2c/v3 with a full private MIB and trap list (link, PoE, power, temperature, ERPS state), syslog, LLDP, sFlow, and MQTT publish for outbound telemetry through NAT/firewalls. CLI is Cisco-style over SSH with key auth and SCP/SFTP, so netmiko/Ansible work out of the box; firmware is dual-partition for safe remote upgrades. We don't have a REST API today — if that's a hard requirement for your NMS, tell me what you poll/push now (SNMP? RouterOS API?) and I'll scope it with our R&D.
>
> Happy to send one 12-port unit for you to put on your bench next to a CRS. Which power and uplink (SFP or SFP+) do you want?
>
> Simon

---

## 7. 30 / 60 / 90 天动作清单

### 30 天：把"已有能力"产品化（零研发）
1. **MikroTik ↔ SmartByte 对照表 PDF**（配套 Excel 导出 2 页，给销售和客户用）
2. **Integration Package v1**（文件夹）：
   - `01_SNMP/`：MIB 文件、OID 速查表、Trap 列表（从 SWITCH-MIBS-release-7.3.0.docx 提取）
   - `02_CLI/`：命令速查（从 Marvell Based CLI Manual 提取 VLAN/ERPS/PoE/SNMP/备份 五章）、`netmiko` 示例脚本、Ansible `network_cli` playbook 样例（批量配 VLAN + SNMP + 备份）
   - `03_Firmware/`：双分区升级指南、TFTP/SCP 升级步骤、回滚
   - `04_Telemetry/`：MQTT 说明（**先向 SmartByte 索要 topic/payload 文档**）
   - `05_NMS/`：LibreNMS/Zabbix 模板（哪怕先只用标准 IF-MIB + 私有温度/PoE OID）
3. **两台样机策略**：备 LT-S8328XG-4XS24GT-S 和 LT-IS6312XG-4XS8GT 各 2 台现货，谁提 MikroTik 就寄。
4. **向 SmartByte 确认的问题**（见第 9 节）。

### 60 天：建名单
- LinkedIn Sales Navigator 关键词分三组：
  - WISP 组：`WISP` `wireless ISP` `fixed wireless` `tower` `backhaul` `RouterOS` `MTCNA` `MTCRE` `MTCINE`
  - 渠道组：`MikroTik distributor` `MikroTik reseller` `MikroTik partner` `MikroTik training`
  - 方案商组：`network management platform` `cloud NMS` `SCADA communication` `ITS` `traffic management` `telemetry` `remote monitoring`
- 公开名单直接扫：`mikrotik.com/buy`（按国家分销商）、`mikrotik.com/consultants`（顾问）、WISPA 会员目录（美）、KIKE（波兰）。
- 评分卡（网站关键词）：MikroTik +3 / WISP +3 / PoE +2 / fiber +2 / OEM 或 private label +3 / 有自己 dashboard 截图 +3。目标 200 家精准公司，不追数量。

### 90 天：做 inbound
- 把 LibreNMS OS 定义 / Zabbix 模板**开源发布**（GitHub + LibreNMS 社区 PR）。WISP 群体几乎人手一套 LibreNMS，模板被合并 = 免费长期曝光，而且这是社区接受的"厂商参与"方式。
- 把土耳其客户 NMS 接入案例匿名化写成一页 case study。
- MUM（MikroTik User Meeting）以**参会者**身份去一场（欧洲站），不要摆摊。

---

## 8. 去中介化风险与你的价值（务实版）

SmartByte 官网现在把 OEM、White Box、SKD/CKD、固件 release notes 全公开了。Frank 类客户 30 分钟就能找到源头。你要在以下几点让客户觉得"从 Simon 买比直接找工厂省事且更安全"：

1. **多供应商组合**：Marvell 接入（SmartByte）+ Centec L3 核心，一张 PO 覆盖接入到核心 —— 工厂给不了。
2. **Integration Package 与英文文档**：工厂给的是研发文档（SWITCH-MIBS-7.3.0.docx 那种），你给的是客户能直接用的 MIB/Trap/CLI/Ansible/LibreNMS 包。这是真实的增值。
3. **小批量现货 + 预配置**：几台起发、出厂前按客户模板刷配置/固件/Logo（软件定制 No MOQ 是工厂政策，但执行和验收要人盯）。
4. **欧洲时区 + 英文技术支持 + RMA 中转**：工厂说工程师能英文沟通，但响应时区和 RMA 物流是你的。
5. **保密**：工厂 OEM 页写了 NDA，你要在合同层面把客户名单和定制 UI 归你。

同时，**和 SmartByte 谈清楚渠道规则**：你带进来的 OEM 客户，工厂不直接接。趁现在 Frank/SIMREX 还只是线索，先把规则谈定。

---

## 9. 需要向 SmartByte 确认的清单（下次沟通直接发）

1. **MQTT**：topic 结构、payload 格式（JSON？）、可发布的对象（端口状态/PoE/温度/告警？）、支持 TLS？有无文档。
2. **私有 MIB**：7.5.x 最新 MIB 文件；"Customized SNMP OID" 具体指企业 OID 前缀可换成客户的（白牌 MIB）？
3. **Trap 完整列表**：含 ERPS 状态、PoE 事件、Dying Gasp、Relay warning、温度阈值。
4. **CLI 兼容性**：是否与 netmiko `cisco_ios` driver 基本兼容（prompt/paging/`terminal length 0`）；有无 `show running-config` 完整导出。
5. **SSH 公钥登录**：支持哪些 key 类型（RSA/ED25519）；能否禁用密码登录。
6. **REST API**：有无路线图；OEM 客户付费定制的报价量级。
7. **Web UI "Page Package Management"**：是否等于可整体替换 Web 皮肤/菜单（白牌 UI）；定制费用。
8. **Serial Server（RS485）**：支持 TCP Server/Client/UDP？波特率范围？Modbus RTU→TCP 网关？哪些型号带。
9. **商业 8 口 L2+（LT-S8310G/GP）恢复出货时间**；LT-S8310XG-2XS8GT 与 LT-S8312XG-4XS8GT 的价格。
10. **24 PoE + 4×10G + 440W/850W** 组合是否可做（现价格表里 XGP 只有 280W 的 -S 版）。
11. **AC5 停产、AC3 替代**：AC3（98DX3236 家族，与 CRS326 同芯片）版本的功能差异清单，避免客户拿到 AC3 后发现某功能只在 AC5 上有（release notes 里 7.5.0 明确 "Only Marvell AC5 hardware support"）。
12. **渠道保护**：你引入的 OEM 客户的直采政策。

---

## 10. 一页纸结论

- **别再跟 MikroTik 打规格战**，尤其不要拿 QinQ/L3 当差异（RouterOS 都有）。可讲的硬差异只有五个：**ERPS、PoE++ 产品线、工业 DIN 全系、Integration Ready（Trap/私有 MIB/MQTT/SSH 自动化）、OEM No MOQ**。
- **分清 CSS 和 CRS**：客户说 CSS，你直接碾压；客户说 CRS，你讲"补空白"。
- **对 WISP/ITS/工业客户一律推工业款**，商业款 0~50°C 会被 CRS326 的 -40°C 打脸。
- **Frank 的真实规格是 6/12 口小节点**，你的 LT-IS6306G / LT-IS6312G 出厂即加固，进价 $93–104，正好在他 $90–120 的成本带上；再加 RS485 串口服务器 + DI/DO + ERPS 这三点是他行业的刚需。
- **最便宜的增长杠杆**是把已有的 MIB/CLI/固件能力整理成 Integration Package，再做一个 LibreNMS/Zabbix 模板开源出去。
- **去中介化是真实风险**，靠"多供应商组合 + 文档 + 现货预配置 + 欧洲时区支持 + 渠道保护协议"立住。
