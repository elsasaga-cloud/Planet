# MikroTik 类客户全量作战手册（规格对标 × 国家市场 × 推广话术）

> 版本 2026-09。本手册是前两份文档的合并升级版，**不考虑关税**，只看产品规格、国家、市场、竞品、推广与话术。
> 数据口径：MikroTik 规格与价格 = 官网 Suggested price（标 ✅ 为 2026-09 实测，标 * 为你脚本抓取值，需核实）；SmartByte = 官网 2026 年规格页 + 2026.09–12 价格表；相邻品牌 = 2026 年公开零售价（标 ≈）。
> 配套：`MikroTik_vs_SmartByte_替代对照表.xlsx`（新增"竞品全景"和"MikroTik全产品线"两个 sheet）。

---

## 目录

0. 十条核心判断
1. 市场全景：MikroTik 交换机业务的体量、结构与客户
2. 竞品全景：MikroTik 全产品线分段 + 相邻品牌
3. 规格深度对标（8 张矩阵）
4. 国家 × 市场：按国家的客户画像与切入
5. 四类客户作战卡
6. 话术库（英文话术 + 中文说明）
7. 推广策略与内容资产
8. 产品与供应商侧建议
9. 风险与不打的地方
附录 A：MikroTik 交换机全产品线（去重 49 款）
附录 B：SmartByte 关键 SKU
附录 C：数据来源

---

## 0. 十条核心判断

1. **MikroTik 交换机是"路由器的附属品"**：客户先买 RouterOS 路由器，再顺手买 CRS/CSS。你不是在替换 MikroTik 的路由器，而是在替换他"顺手买"的那台交换机——决策链短、情感依附弱、可替换性高。
2. **分清 CSS 和 CRS**：CSS（SwOS）是傻瓜 Web 交换机，你全面碾压；CRS（RouterOS）有 QinQ/MSTP/L3 卸载/API，你只能"补空白"。别用同一套话术。
3. **对 CRS 只有五张硬牌**：ERPS G.8032、802.3bt PoE++ 产品线、工业 DIN 全系、Integration-ready（Trap/私有 MIB/MQTT/SSH 自动化）、OEM 软件定制 No MOQ。其余都是平手或劣势。
4. **温度是你的第一个坑**：商业款 0~50°C 对 CRS326 的 -40~60°C 必输；WISP/ITS/工业场景一律推工业款（-40~75°C）。
5. **被动 PoE 是你的第二个坑**：WISP 用 CRS/netPower 给 MikroTik 无线设备供 24V 被动 PoE；你只有 802.3af/at/bt。话术里必须主动处理（见 6.4 第 6 条）。
6. **相邻品牌里最危险的不是 MikroTik**：TP-Link Omada SG3428X（同规格、有 ERPS、终身保修、≈$259–367）和 Teltonika TSW212（工业 8 口 $129 MSRP，与 MikroTik 同渠道）分别在商业 24 口和工业 8 口两个主战场卡住你的价格空间。
7. **你的真实定位是"介于 MikroTik/TP-Link 和 PLANET/ORing 之间的工业级白牌"**：功能≈PLANET（ERPS、宽温、DI/DO、Bypass），价格≈MikroTik/TP-Link，外加可贴牌。这个位置目前在欧洲是空的。
8. **地理上盯中东欧 ISP 带**：波兰、捷克、立陶宛三国占 MikroTik 出货 21%，中东欧+波罗的海+乌克兰 28%；西欧 15%；美国 12%（单一最大国）。
9. **最便宜的增长杠杆是文档和模板**，不是广告：MIB/Trap 清单、CLI 速查、netmiko/Ansible 样例、LibreNMS/Zabbix 模板、MQTT 文档。技术型客户看到这些就信一半。
10. **欧盟 CRA（网络弹性法案）是 2027 年的 OEM 敲门砖**：漏洞上报义务 2026-09-11 已生效，全面适用 2027-12-11。贴你牌子的欧洲品牌商在法律上就是"制造商"，谁能给 SBOM、签名固件、漏洞响应流程和 5 年更新承诺，谁就能拿到欧洲 OEM 单。

---

## 1. 市场全景

### 1.1 MikroTik 交换机业务的体量与结构

| 指标 | 数据 | 来源/说明 |
|---|---|---|
| MikroTik 营收 | 2023 €4.02 亿 → 2024 €3.27 亿 → 2025 €3.45 亿 | Lursoft |
| 拉脱维亚 HS 851762 出口（≈MikroTik 分销商进货） | 2024 年 4.22 亿美元 FOB | UN Comtrade |
| 交换机占比（估） | 15–25% → 全球交换机 FOB 约 0.5–0.8 亿美元/年 | 行业惯例估算 |
| 产品线 | CSS（SwOS 傻瓜）/ CRS1xx-3xx（RouterOS+SwOS 双启动）/ netPower（户外反向 PoE）/ CRS4xx（强 CPU 混合路由交换）/ CRS5xx（25/100G） | 官网 |
| 芯片 | Marvell Prestera 为主（98DX3236 AC3、98DX226S/224S、98DX2518 AC5-Lite、98DX8xxx、98DX4310/98CX8410）；老款 QCA85xx；SwOS Lite 用 88E6193X | 官网 + 你的抓取 |
| 认证 | CE / EAC / RoHS（无 UL、无 FCC 列出） | 官网 |
| 保修 | 1 年（欧盟法定 2 年） | — |
| 软件更新承诺 | 产品寿命或≥5 年免费 | 官网 |

**结构性含义**：MikroTik 与你用的是**同一代 Marvell 硅片**（AC3 = 98DX3236 = CRS326/328；AC5-Lite 98DX2518 = CSS318；SmartByte L2+ = 98DX2515/2518，AC3 备选）。对工程师这是可信度脚注："same Marvell Prestera family as CRS3xx"——但别拿芯片当卖点，客户买的是软件和产品形态。

### 1.2 一个 MikroTik 客户的采购清单上，谁和谁在竞争

| 场景 | 客户会同时看的品牌 | 决策关键 |
|---|---|---|
| ISP 机房/塔站 24 口 | MikroTik CRS326/CSS326、TP-Link SG3428X、Ubiquiti USW-Pro-24、二手 Cisco/Juniper | 价格、10G 上联数、VLAN/QinQ、能否进 NMS |
| 塔站/机柜 8–12 口 | MikroTik CRS112/CRS310/netPower、Teltonika TSW2xx、Ubiquiti USW-Industrial、中国直供（Utepo/ONV/HRUI） | 宽温、DC 输入、被动 PoE、价格 |
| 安防/工业 PoE | MikroTik CRS328-24P/CRS320、PLANET IGS/GS 系列、ORing、Ubiquiti、TP-Link SG3428XMP、中国直供 | PoE 预算、PoE++、ERPS、保修、投标资质 |
| 光纤汇聚/全 SFP | MikroTik CRS309/317/326-24S+、CRS328-4C-20S | 价格（MikroTik 无敌） |
| 25/100G | MikroTik CRS504/510/518/520 | 价格（MikroTik 无敌） |

### 1.3 客户是谁（四类，与国家密度）

| 类型 | 画像 | 密度最高的国家 | 你的优先级 |
|---|---|---|---|
| A. WISP / 小型 ISP | RouterOS 做核心与 PPPoE，塔站用 CRS/CSS，无线混用 MikroTik/Ubiquiti/Cambium | 波兰、捷克、斯洛伐克、意大利、西班牙、美国乡村、南非、澳洲、巴西 | ★★★★ |
| B. MikroTik 分销商/经销商/培训中心 | 同时卖 Ubiquiti/TP-Link/Teltonika/光模块；有 house brand 需求 | 所有 T1 国家、阿联酋（面向 MEA）、立陶宛/爱沙尼亚枢纽 | ★★★★★（OEM 主战场） |
| C. 自建 NMS/云平台的方案商 | 有自己的 dashboard，用 RouterOS API/SNMP 采集，行业客户（ITS/SCADA/公用事业/安防） | 美国、德国、英国、土耳其、荷兰、北欧 | ★★★★★（客单价最高） |
| D. 工业/安防集成商 | 把 CRS 当"便宜管理交换机"用，项目制 | 德奥、英国、意西、波兰、中东 | ★★★ |
| ✗ Homelab/个人 | 论坛、Reddit | — | 不碰 |

---

## 2. 竞品全景

### 2.1 MikroTik 交换机产品线分段（去重后 49 款，全表见附录 A）

| 分段 | 代表型号（MSRP） | 芯片/OS | 关键特征 | SmartByte 对位 | 胜负 |
|---|---|---|---|---|---|
| **24 口铜 L2（傻瓜）** | CSS326-24G-2S+RM **$159 ✅** | 98DX3216 / SwOS | 无 CLI/SSH/LLDP/Trap，SNMP 只读，250 VLAN，32 ACL，-20~70°C | LT-S8328XG-4XS24GT-S（¥710≈$100，卖 $130） | ★★★★★ 碾压 |
| **24 口铜 L2/L3（RouterOS）** | CRS326-24G-2S+RM **$209 ✅** / -IN $199* | 98DX3236 / RouterOS+SwOS | 2×SFP+，-40~60°C，QinQ/MSTP/L3 卸载/API | 同上 | ★★★★ 补空白 |
| **24 口 PoE** | CRS328-24P-4S+RM **$489 ✅** | 98DX3236 | af/at + 被动，450W，4×SFP+，-20~60°C，无 bt | LT-S8328XGP-4XS24GT-S（¥1010，280W）/ 工业 LT-IS6328XGP（¥2200） | ★★★★ |
| **48 口** | CRS354-48G-4S+2Q+RM **$599 ✅** / 48P $999* | 98DX3257 + QCA9531 650MHz **64MB RAM** | 4×SFP+ + 2×QSFP+ 40G，CPU 极弱只能当 L2 | LT-S8352XG-4XS48GT（¥1470）/ XGP（¥1870） | ★★★（无 40G） |
| **16 口** | CSS318-16G-2S+IN $139* / CRS318-16P-2S+RM $329* / netPower 16P $279* | 98DX2518 / 98DX3236 / 98DX226S | CSS318 = 你同款芯片但 SwOS | LT-IS6318G/XGP（工业，¥1180–1660） | ★★（无商业 16 口） |
| **8–10 口 SMB** | CSS610-8G-2S+IN **$119 ✅** / CSS610-8P $229* / CRS310-8G+2S+IN $149*（8×2.5G） | 88E6193X / 98DX226S | 8 口价格底线；2.5G 电口你没有 | LT-S8310G/GP（¥380/450，暂停出货）/ LT-S8310XG（询价） | ★★ |
| **8–12 口老款 RouterOS** | CRS106-1C-5S $89* / CRS112-8G-4S-IN $119* / CRS112-8P-4S-IN $209* | QCA8511/8513 400MHz | Frank 型客户在用的规格 | LT-IS6306G（¥660）/ LT-IS6312G（¥740）/ LT-IS6312GP（¥820） | ★★★★（出厂即工业加固） |
| **混合 PoE/bt** | CRS320-8P-8B-4S+RM $299–489* / CRS418-8P-8G-2S+RM $449* | 98DX226S；CRS418 2.2GHz 四核 | CRS418 = MikroTik 新方向：强 CPU + L3 卸载 + 可当路由器/CAPsMAN | LT-IS6320GP-4GX16GT-D-4BT（¥1960） | ★★ |
| **全光 SFP** | CRS328-4C-20S-4S+RM $299–449* / CRS309-1G-8S+ $229–269* / CRS317-1G-16S+ $499* / CRS326-24S+2Q+ $599* / CRS332-32S+ $749* | 98DX3236 / 8208 / 8216 / 8332 | 价格无敌 | LT-IS6328XG-4XS16GX8GC-D（¥2650）贵一倍 | ✗ 不打 |
| **户外反向 PoE** | netPower Lite 7R $99* / CSS610-1Gi-7R-2S+OUT | 98DX3236 / SwOS | FTTB/楼道反向供电 | 无 | ✗ |
| **10G 铜/25G/100G** | CRS304-4XG $199* / CRS312-4C+8XG $349–699* / CRS504 $799* / CRS510 $999* / CRS518 $1595* / CRS520 $2195* | 98DX2528 / 8212 / 4310 / 8525 / CX8410 | — | White Box 10/25/100G 系列价格打不过 | ✗ |

### 2.2 相邻品牌（一个 MikroTik 客户会一起比的）

| 品牌 | 代表型号（≈街价） | 强项 | 弱项 | 对你的威胁 | 你的打法 |
|---|---|---|---|---|---|
| **TP-Link Omada** | SG3428X 24G+4×SFP+ L2+（≈$259–367）；SG3428XMP 24 PoE+ 384W | **有 ERPS**、802.3ah OAM、sFlow、DDM、CLI、SNMP、静态路由、无风扇、Omada 云控、**终身有限保修**、渠道无处不在 | 商业级 0~40/50°C、无工业 DIN 线、无 PoE 看门狗 (部分有)、无 DI/DO、不能 OEM、品牌"消费级"印象 | **高**（商业 24 口主战场） | 不在商业 24 口拼 TP-Link；把 24 口当"敲门 SKU"，靠工业/PoE++/OEM 赚钱 |
| **Ubiquiti UniFi** | USW-24（L2，2×SFP 1G，≈$219–295）；USW-Pro-24（L3，2×SFP+，**$399** 官网）；USW-Pro-24-PoE 400W（≈$699–899）；USW-Industrial（DIN PoE++） | UniFi 控制器/云、UI 极好、品牌强、WISP 圈熟 | 必须用控制器、CLI 弱、无 ERPS（RSTP）、SNMP 弱、无 QinQ、不能 OEM、保修 1 年 | 中（SMB/MSP） | 对"要 CLI/SNMP/ERPS/不想被控制器绑定"的客户 |
| **Teltonika Networks** | TSW212 8G+2×SFP 管理型（**$129 MSRP**）；TSW202 8×PoE+；TSW1xx 非管理 | 立陶宛、**与 MikroTik 同一批分销商**、RMS 云、PROFINET/EtherNet-IP/MRP、7–57V 输入、IoT 品牌 | 8K MAC/512KB 缓存、无 10G、无 ERPS（MRP 是 PROFINET 环）、无 PoE++、无 QinQ/MSTP 级 L2+、无 OEM | **高**（工业 8 口价格） | 用 LT-IS6312XG（4×10G）、PoE++、ERPS、DI/DO、16K MAC/12Mbit 缓存、5 年保修拉开 |
| **PLANET** | IGS-5225-8P4S 工业 8 PoE+ +2 SFP+2×2.5G SFP（**$757–828**）；GS-5220 系列商业 L2+ | 台湾品牌、ERPS <10ms、MSTP、**Modbus TCP、IEEE 1588 透传**、宽温、目录极全、TAA | 价格 5–7×、交期、不能 OEM（有限） | 低（价格带不同） | "PLANET 的功能，MikroTik 的价格"——最好用的一句话 |
| **ORing** | IGS-9084GP 等（≈$900–1200） | 工业标杆：O-Ring <30ms、ERPS、EN50155 铁路、IP67、UL/Class I Div 2 | 价格 8–10×、交期长 | 低 | 不碰铁路/IP67/UL 项目；其他场景用价格 |
| **中国直供** | Utepo / ONV / HRUI / UNIPOE | 更便宜（比你低 10–30%）、目录大 | 软件弱（多为 Realtek/Broadcom 小芯片方案）、无 CLI 或 CLI 不规范、SNMP 私有 MIB 缺、文档差、不做欧美本地支持 | 中（B 类分销商会拿来压价） | 用 Marvell 平台 + Cisco 风格 CLI + 完整 MIB + 7.x 固件迭代 + 3/5 年保修拉开；不比裸价 |

> **位置图**：横轴价格（MikroTik=1.0），纵轴工业/管理能力。中国直供 0.7–0.9 / 低；MikroTik 1.0 / 中（软件强）；TP-Link 1.2–1.7 / 中；Ubiquiti 1.5–2.5 / 中；**SmartByte 0.6–0.7（24 口）~ 1.0（工业 8 口）/ 高**；Teltonika 0.9 / 中低（工业 8 口）；PLANET 3–5 / 高；ORing 5–8 / 最高。你占的是"高能力 × 低价格"的空位。

---

## 3. 规格深度对标

### 3.1 硬件平台（24 口这一档）

| 项目 | CSS326-24G-2S+RM | CRS326-24G-2S+RM | TP-Link SG3428X | Ubiquiti USW-Pro-24 | **SmartByte LT-S8328XG-4XS24GT-S** |
|---|---|---|---|---|---|
| 价格 | $159 ✅ | $209 ✅ | ≈$259–367 | $399 | 进价 ≈$100，卖 $130 |
| 交换芯片 | Marvell 98DX3216 | Marvell 98DX3236 | 未公开 | 未公开 | Marvell AC5 系列 |
| CPU / RAM / Flash | — / — / 2MB | ARM 2×800MHz / 512MB / 16MB | 未公开 | 未公开 | **1.2GHz / 512MB / 512MB** |
| 下行 | 24×GbE | 24×GbE | 24×GbE | 24×GbE | 24×GbE |
| 上行 | 2×SFP+ | 2×SFP+ | **4×SFP+** | 2×SFP+ | **4×SFP+（1/2.5/10G）** |
| 交换容量 / 转发 | 88G | 88G | 128G / 95Mpps | 88G | **128G / 190Mpps** |
| MAC / VLAN / 缓存 | 16K / 250 / — | 16K / 4K / — | 16K / 4K / 12Mbit | 16K / 4K / — | 16K / 4K / 12Mbit |
| Jumbo | 10218 | 10218 | 9K | 9K | 10K |
| Console | 无 | RJ45 | RJ45 + Micro-USB | 无（控制器） | RJ45 115200 |
| 电源 | 10–30V DC / 被动 PoE-in | 10–30V DC / 被动 PoE-in | AC 内置 | AC 内置 | AC 100–240V 内置 |
| 功耗 | 19W | 24W | 23.6W | — | ≤24W |
| 风扇 | 无 | 无 | 无 | 无 | 无（需向工厂确认） |
| 工作温度 | -20~70°C | **-40~60°C** | 0~50°C | -5~40°C | **0~50°C** |
| MTBF | ~200k h | ~200k h | — | — | >100k h |
| 认证 | CE/EAC/RoHS | CE/EAC/RoHS | CE/FCC/RoHS | CE/FCC/IC | CCC/CE/UKCA/RoHS/REACH/FCC |
| 保修 | 1 年（EU 2） | 1 年（EU 2） | **终身有限** | 1 年 | 3 年 |
| OEM | 否 | 否 | 否 | 否 | **是，软件 No MOQ** |

### 3.2 L2 功能矩阵

| 功能 | SwOS (CSS) | RouterOS (CRS3xx) | TP-Link SG3428X | UniFi USW-Pro | Teltonika TSW212 | **SmartByte L2+ 7.5.x** |
|---|---|---|---|---|---|---|
| 802.1Q VLAN | ≤250 | 4K | 4K | 4K | 4K | 4K，access/trunk/hybrid |
| MAC/IP/协议/语音/Private VLAN | 否 | 部分（脚本） | MAC/协议/语音 | 否 | 否 | **全部** |
| QinQ / VLAN 映射 | 否 | **是**（802.1ad HW） | 是 | 否 | 否 | 是（端口/VLAN/流 + 映射） |
| GVRP | 否 | 否 | 是 | 否 | 否 | 是 |
| STP/RSTP/MSTP | RSTP | **全部（HW）** | 全部 | RSTP | STP/RSTP | 全部 + BPDU Guard |
| **ERPS G.8032** | 否 | **否** | **是** | 否 | 否（MRP） | **是，主环/子环，<20ms，节点数不限** |
| LAG/LACP | 16 组 | 是（HW bonding） | 是 | 是 | 是 | 64 组×8 口 |
| IGMP Snooping / 查询器 | 是 | 是 | 是 v1-3 + MLD | 是 | 是 | v1-3 + 快速离开 + 1K 组 + **PIM-SM** |
| 风暴抑制 | 是 | 是（3236 不能区分未知/全部组播） | 是 | 是 | 是 | 是（广播/未知组播/未知单播分开） |
| 镜像 / RSPAN | 镜像 | 镜像 | 镜像 + RSPAN | 镜像 | 镜像 | **7 会话 + RSPAN** |
| LLDP / LLDP-MED | **否**（MNDP） | LLDP/CDP/MNDP | LLDP/MED | LLDP | LLDP | LLDP/MED |
| 环路检测 | 否 | 否（靠 STP） | DLDP/环回检测 | 是 | 是 | 是（端口/VLAN） |
| EFM 802.3ah | 否 | 否 | 是 | 否 | 否 | 是 |
| DHCP Snooping / Opt82 | 否 | 是 | 是 | 是 | 否 | 是 + circuit-id/remote-id 自定义 |
| 端口隔离 | 是 | 是 | 是 | 是 | 是 | 32 组 |
| 限速 | 入向 | 入/出 + Queue | 入/出 | 入/出 | 入/出 | 入/出 + 队列整形 + 策略 QoS 8 队列 |

### 3.3 L3 功能矩阵

| 功能 | RouterOS on CRS3xx | CRS354 (QCA9531/64MB) | CRS418 (2.2GHz 四核) | TP-Link SG3428X | **SmartByte L2+** | **SmartByte L3 (LT-S85xx / LT-IS65xx)** |
|---|---|---|---|---|---|---|
| 静态路由 | 是（HW offload 基础） | CPU 极弱 | 是 + HW offload | 是 | IPv4/IPv6，1K–4K 前缀 | 是 |
| DHCP Server/Relay | 是 | 是 | 是 | Relay | **Server + Relay** | Server + Relay |
| RIP / OSPFv2 / IS-IS / BGP4 | 是（CPU） | 勉强 | 是 | 否 | 否 | **是** |
| VRRP / ECMP | 是 | — | 是 | 否 | 否 | **是** |
| OSPFv3 / PBR / MPLS | 是 | — | 是 | 否 | 否 | 否 |
| L3 HW offload 限制 | 基础路由 only，**无 NAT/Fasttrack 卸载**，路由表小，HW 路由与 HW 防火墙二选一 | — | 同左但 CPU 强 | — | — | 全硬件路由 |
| NAT / 防火墙 / 队列 | 有（CPU） | 有（极弱） | 有（强） | 无 | 无 | 无 |

**结论**：需要"交换机顺便做 NAT/防火墙/流控"的客户，留给 RouterOS（尤其 CRS418）。需要 OSPF/VRRP 汇聚但不做 NAT 的 ISP，LT-S8528XG-4XS24GT（¥1500≈$211）是合理选择。

### 3.4 安全矩阵

| 功能 | SwOS | RouterOS | TP-Link | UniFi | **SmartByte** |
|---|---|---|---|---|---|
| ACL | 32 条 | switch-rule + 防火墙 | IP/MAC/IPv6/时间段 | 基础 | **480 条，IP 标准/扩展、MAC、IPv6、时间段、可绑 VLAN** |
| 802.1X / MAC 认证 | 否 | 802.1X（dot1x 包） | 是 | 是（RADIUS） | 是 + MAC 认证 |
| RADIUS / TACACS+ | 否 | RADIUS | RADIUS/TACACS+ | RADIUS | **RADIUS + TACACS** |
| IPSG / DAI / ARP 检查 | 否 | 部分（脚本） | 是 | 否 | 是 + 防网关欺骗 |
| 端口安全 / MAC 限制 | Port lock | 是 | 是 | 是 | 是（端口/VLAN） |
| DDoS 防护 | 否 | 防火墙 | 是 | 否 | 是 |
| 密码复杂度 / 登录锁定 | 否 | 是 | 是 | 控制器 | 是（7.5.0 新增） |
| 用户权限等级 | 单一 | 组权限 | 4 级 | 控制器 | 0–15 级 |
| HTTPS / SSH 公钥 | HTTPS | 是 | 是 | — | 是 + SHA256/512 |

### 3.5 管理与运维矩阵（最能打的一张表）

| 功能 | SwOS | RouterOS | TP-Link Omada | UniFi | **SmartByte** |
|---|---|---|---|---|---|
| Web UI | 是（简陋） | WebFig | 独立 Web + Omada 云 | 控制器 | HTTP/HTTPS，**可整体换皮（Page Package）** |
| CLI 风格 | 无 | RouterOS 私有语法 | Cisco 风格 | 受限 | **Cisco-IOS 风格**（configure terminal / show / write / copy tftp） |
| Telnet/SSH | 无 | 是 | 是 | SSH 受限 | 是，SSH2 公钥 |
| SNMP | v1/v2c **只读，无 Trap** | v1/v2c/v3 + Trap | v1/v2c/v3 + Trap | 有限 | **v2c/v3 + Trap + RMON + 私有 MIB + 自定义 OID** |
| Syslog | 否 | 是 | 是 | 控制器 | 3 台服务器，IPv4/IPv6 |
| sFlow / NetFlow | 否 | Traffic-Flow | sFlow | 否 | sFlow |
| **MQTT** | 否 | 否（可脚本） | 否 | 否 | **是（7.5.x）** |
| LLDP 拓扑 | 否 | 是 | 是 | 是 | 是 |
| 光模块 DDM | 是 | 是 | 是 | 是 | 是 |
| 线缆检测 | 是 | 是 | 是 | 是 | 是 |
| 一键故障采集 | 否 | supout.rif | 否 | 是 | 是 |
| 双分区固件 | 否 | 否（有备份） | 否 | 否 | **是** |
| 配置导入导出 | Web 备份 | export/import | 是 | 控制器 | FTP/TFTP/USB/SCP/SFTP |
| API / REST / 脚本 | 否 | **API + REST(v7.1+) + 脚本 + Winbox + The Dude + btest** | Omada API | UniFi API | **否**（差距） |
| 云控制器 | 否 | 无（可自建） | Omada 云 | UniFi 云 | 无（差距） |
| Ansible / netmiko | 否 | 有社区模块 | 可用 cisco 驱动 | 否 | 可用 cisco 风格驱动（需验证） |
| 固件节奏 / 公开 release notes | 慢 | 快，公开 | 中 | 快 | 7.x 持续，**官网公开 release notes** |

### 3.6 PoE 矩阵

| 功能 | CRS328-24P-4S+ | CRS320-8P-8B | netPower 16P | TP-Link SG3428XMP | **SmartByte 商业 PoE** | **SmartByte 工业 PoE/PoE++** |
|---|---|---|---|---|---|---|
| 标准 | af/at + **被动 PoE** | 8×at + 8×bt | af/at + 被动 | af/at | af/at（bt 型号可选） | **af/at/bt 90W** |
| 预算 | 450W（3×150W/8 口） | — | 300W* | 384W | 280W（-S）/ 440W / 850W | 480W（8×90W）等 |
| 单口 | 30W | 30/60W | 30W | 30W | 30W | 90W |
| PoE 看门狗 (PD Alive) | 否 | 否 | 否 | 是（部分） | **是** | 是 |
| PoE 定时 | 脚本 | 脚本 | 脚本 | 是 | 是 | 是 |
| 优先级 / 告警阈值 / 预留功率 | 优先级 | 优先级 | 优先级 | 优先级 | **全部** | 全部 |
| 非标 PD（Legacy 模式） | 被动即可 | 被动即可 | 被动即可 | 否 | 是 | 是 |
| Boost PoE（DC 12/24V 升压供 PoE） | 否 | 否 | 否 | 否 | 否 | **是（Boost 系列）** |

> **被动 24V PoE 是 MikroTik 的独门**：WISP 的 SXT/LHG/wAP 老款只吃 12–28V 被动供电。你的交换机只有 48–57V 标准 PoE。应对：新款 MikroTik/Ubiquiti/Cambium 射频基本都支持 802.3af/at；老设备用 48→24V 转换器或 MikroTik 自己的 24V 注入器；永远不要说"我们也能供被动 PoE"。

### 3.7 工业与环境矩阵

| 项目 | CRS326-24G-2S+RM | CRS112/CRS310 | Teltonika TSW212 | PLANET IGS-5225 | **SmartByte 商业 LT-S** | **SmartByte 工业 LT-IS** |
|---|---|---|---|---|---|---|
| 温度 | -40~60 | -20~60 / -40~70 | -40~75 | -40~75 | **0~50** | **-40~75** |
| 安装 | 1U | 桌面 | DIN | DIN | 1U | **DIN / IP40** |
| 电源输入 | 10–30V DC 单 + 被动 PoE-in | 同左 | 7–57V DC | 双 DC 12–48/48–56V | AC 内置 | **双 DC 12–58V（PoE 型 44/52–57V）**，反接/过流保护 |
| 浪涌 / ESD | 未标 | 未标 | 未标 | IEC 61000-4 | 4kV 电源/端口，ESD 6/8kV | **6kV/4kV 电源，6kV/2kV 端口，ESD 8/15kV，EFT 4kV，RS 10V/m** |
| 振动/冲击/跌落 | 未标 | 未标 | — | IEC 60068 | — | IEC 60068-2-6/27/32 |
| MTBF | ~200k h | ~200k h | — | — | >100k h | **>200k h** |
| 保修 | 1 年 | 1 年 | 2 年 | 5 年 | 3 年 | **5 年** |
| DI/DO 干接点 | 否 | 否 | 否 | 部分 | 否 | **-D 型号** |
| RS485 串口服务器 | 否 | 否 | 否 | 部分（Modbus TCP） | 否 | **-D 型号** |
| 温湿度传感器 | 否 | 否 | 否 | 否 | 否 | **-T 型号** |
| 光纤 Bypass | 否 | 否 | 否 | 否 | 否 | **-FBP 型号** |
| 继电器告警 / Dying Gasp | 否 / 否 | 否 / 否 | 否 / 否 | 是 / 部分 | 否 / 是 | **是 / 是** |
| Modbus TCP / IEEE 1588 | 否 | 否 | PROFINET/EtherNet-IP/MRP | **是 / 是** | 否 | **否（向工厂争取）** |

### 3.8 软件生态与"软实力"

| 维度 | MikroTik | TP-Link / Ubiquiti | **SmartByte（经你）** |
|---|---|---|---|
| 社区 | 全球最大之一：论坛、MUM、MTCNA 认证体系、YouTube 教程无数 | 大 | 无 → 靠你和客户共建（Zabbix/LibreNMS 模板开源是起点） |
| 文档 | help.mikrotik.com 完整 | 完整 | 有 CLI/Web 手册（docx）、MIB docx；需整理成可检索的英文站 |
| 更新承诺 | ≥5 年 | 终身/长期 | 需明确书面承诺（配合 CRA：≥5 年安全更新） |
| 安全响应 | 有 CVE 历史，响应快 | 有 | 需建立：漏洞披露邮箱、SBOM、签名固件（向工厂要） |
| 培训 | MTCNA 等 | 认证课程 | 你可做"1 小时上手 + CLI 速查"视频 |
| 品牌 | 强（技术圈） | 强 | 弱 → OEM 客户用自己的牌子反而是优势 |

---

## 4. 国家 × 市场

### 4.1 出货地图（UN Comtrade 2024，拉脱维亚 HS 851762 出口，FOB）

| 区域 | 占比 | 结构 |
|---|---|---|
| 欧洲 | **42.8%** | 中东欧+波罗的海+乌克兰 28.1%（波兰 8.1、立陶宛 7.7、捷克 5.2、爱沙尼亚 2.1、乌克兰 1.9、保加利亚 0.9、匈牙利 0.8…）；西/北/南欧 14.7%（德国 3.8、英国 2.1、意大利 1.9、西班牙 1.7、荷兰 1.5、奥地利 1.1、瑞典 0.7…） |
| 北美 | 13.1% | 美国 12.1%，加拿大 1.1% |
| 中东/土耳其 | 12.3% | 阿联酋 10.2%（转口 MEA/南亚），土耳其 1.8% |
| 亚太 | 12.1% | 香港 3.8%（转口），印尼 2.7%，新加坡/中国各 1.1%，澳大利亚 0.9%，越南/泰国各 0.6% |
| 拉美 | 4.5% | 巴西 1.3%，哥伦比亚 0.9%，智利/秘鲁 0.6%，墨西哥 0.5%，阿根廷 0.4% |
| 非洲 | 3.1% | 南非 2.7% |
| 独联体/中亚 | 3.0% | 哈萨克斯坦 2.6% |

### 4.2 国家作战表（T1 主攻）

| 国家 | MikroTik 密度 | 客户类型 | 市场特征 | 首推 SKU | 渠道与名单 | 语言/合规 |
|---|---|---|---|---|---|---|
| **波兰** | 8.1%，欧洲第一 | A、B | 以千计的地方 ISP（UKE 登记）、成熟 IT 分销、光纤到户大规模建设、WISP 向 FTTH 转型（需要 10G 上联 + ERPS 环） | LT-S8328XG（$130）、LT-S8528XG（L3 汇聚）、LT-IS6312XG（塔站） | KIKE 商会、PLNOG 会议、MikroTik 官方分销商列表（PL）、LinkedIn `ISP` `MikroTik` `MTCNA` + Poland | 波兰语两页资料；WEEE/EPR 由分销商注册；发票 PLN/EUR |
| **捷克 / 斯洛伐克** | 5.2% + 0.3% | A、B、C | 社区 WISP 传统、技术极强、Zabbix 发源地、爱自建监控 | LT-IS6312XG、LT-S8328XG、Integration Package | 捷克 ISP 协会、MikroTik CZ 分销商、Zabbix 社区 | 英语可行；技术文档质量决定一切 |
| **德国 / 奥地利** | 3.8% + 1.1% | B、C、D | SMB/MSP/工业集成，合规要求最高，5 年保修与文档齐全是硬门槛 | 工业 LT-IS 全线、PoE++、OEM | IT 分销商 house brand、工业集成商、Systemhaus | 德语资料；ElektroG/WEEE 注册；GDPR；CRA 准备度会被问 |
| **英国** | 2.1% | B、C、D | 专业分销商多（同时卖 MikroTik/Ubiquiti/TP-Link/第三方）、MSP 密集 | 全线 | 分销商、MSP、UK WISP（如乡村宽带商） | 英语；UKCA 你已有；UK WEEE |
| **意大利** | 1.9% | A | WISP 密集（山区回传）、AIIP 协会 | 工业 8/12 口、ERPS、PoE | AIIP 会员、MikroTik IT 分销商 | 意大利语加分；付款条件谨慎 |
| **西班牙** | 1.7% | A、D | 农村小运营商、安防集成 | 工业 + PoE | 地方运营商协会、安防分销 | 西语资料 |

### 4.3 T2（选择性）

| 国家 | 理由 | 打法 |
|---|---|---|
| **美国** | 单一最大国（12.1%）；WISPA 生态；C 类方案商（SIMREX）客单价高 | 主推工业/PoE++/ERPS/串口服务器；WISPA 会员目录；不碰 CSS 价位段 |
| **土耳其** | 1.8%，你已有 NMS 集成客户 | 案例复制：土耳其 MikroTik 分销商/培训中心 |
| **阿联酋** | 10.2%，MEA 枢纽，英语商务 | 迪拜网络分销商 house brand（PoE/工业线） |
| **南非 / 澳大利亚 / 新西兰** | 英语 WISP 市场 | LinkedIn + 当地 WISP 协会；澳洲 RCM |
| **荷兰 / 北欧** | C 类方案商多（远程监控/IoT） | Integration Package 打法 |

### 4.4 T3（机会型）

立陶宛/爱沙尼亚（枢纽，顺手接触分销商）、哈萨克斯坦/乌兹别克斯坦/乌克兰（密度高但合规/风险）、印尼/孟加拉/越南/泰国（价格战主场）、巴西/哥伦比亚（Anatel 认证、税、葡西语）。

---

## 5. 四类客户作战卡

### 卡 A：WISP / 小型 ISP

- **触发场景**：新建塔站；升级 10G 回传；光纤环路 RSTP 收敛慢；CSS 接不进 LibreNMS；给 PoE++ 设备供电；机柜 -30°C。
- **痛点排序**：① 宽温/直流；② 环网收敛；③ 进 NMS（Trap/LLDP）；④ 10G 上联数量；⑤ 价格。
- **切入 SKU**：LT-IS6312XG-4XS8GT（8G+4×10G，¥840）→ 塔站；LT-IS6310G（¥700）→ 小节点；LT-S8328XG（¥710）→ 机房；LT-S8528XG（¥1500）→ OSPF/VRRP 汇聚。
- **价格锚**：不比 8 口裸价（CRS305 $149/CSS610 $119/TSW212 $129），比"塔站总成本"：工业 DIN + 双 48V 直流 + 4kV 浪涌 + ERPS，省掉他自己做的 DC-DC、注入器、加固。
- **证明材料**：ERPS 断链视频（<20ms）、Zabbix 截图、-40°C 测试报告（向工厂要）、5 年保修书。
- **首次接触**：*"You run RouterOS at the core — keep it. We replace the switch in the tower cabinet: dual 12–58 VDC, -40~75 °C, G.8032 ring, PoE++ for radios, SNMP traps straight into your LibreNMS."*
- **成交路径**：1 台样机 → 1 个塔站 → 1 条环 → 年度框架。
- **常见异议**：被动 PoE（见 6.4）；"CRS326 也有 -40"（用工业款回答）；"没听过"（Marvell + 3/5 年保修 + 样机）。

### 卡 B：MikroTik 分销商 / 经销商 / 培训中心

- **触发场景**：客户问 PoE++/工业/ERPS 他们只能转 PLANET；利润薄；想做自有品牌配件线；MikroTik 缺货史。
- **痛点排序**：① 目录空白（工业、bt、ERPS）；② 利润；③ 差异化；④ 库存周转。
- **切入方式**：卖"house brand 交换机线"，不卖单品。软件定制 No MOQ（Logo/型号/SN/IP/MAC/OID）+ 20–50 台起的硬件丝印/包装。
- **首推组合**：LT-S8328XG + LT-S8328XGP + LT-IS6312GP-2BT + LT-IS6312XG，四款覆盖 80% 询盘。
- **首次接触**：*"We don't compete with your MikroTik line — we fill the gaps in it, under your brand, with no software MOQ: industrial DIN-rail, 802.3bt, G.8032 ring, 5-year warranty."*
- **成交路径**：样机 2 台 → 试销 20 台（你的牌子）→ 50 台贴牌 → 季度滚动。
- **异议**：中国直供更便宜（用 Marvell/CLI/MIB/固件迭代/保修/欧洲支持拉开）；"TP-Link 也有 ERPS"（TP-Link 不能贴牌、无工业线）。

### 卡 C：自建 NMS / 云平台的方案商（SIMREX 型）

- **触发场景**：他们的节点用 CRS106/112 + 自制加固壳；行业 ITS/SCADA/公用事业；要"API"。
- **痛点排序**：① 设备遥测进自家平台；② 现场加固成本；③ 串口/干接点；④ 批量升级安全；⑤ 长期供货一致性。
- **切入 SKU**：LT-IS6306G（¥660）/ LT-IS6312G（¥740）/ LT-IS6312XG（¥840）+ -D 型号（RS485/DI/DO）。
- **集成三件套**：SNMP Trap + 私有 MIB；MQTT 主动上报；SSH 公钥 + SCP + 双分区 → netmiko/Ansible。
- **首次接触**：见前文 Frank 邮件草稿。
- **成交路径**：样机上他们的 bench → 接入他们 NMS（你远程协助 MIB/Trap）→ 10 台试点 → OEM。
- **异议**："没有 REST API"（承认；给 SNMP/MQTT/SSH 路径；问清他现在采什么；报 OEM 定制路线）。

### 卡 D：工业 / 安防集成商

- **触发场景**：投标要"工业级"；PTZ/球机要 PoE++；ERPS 环；5 年保修；摄像头死机要远程断电重启。
- **痛点排序**：① 资质与保修；② PoE 预算与 bt；③ ERPS；④ 价格；⑤ 交期。
- **切入 SKU**：LT-IS6312GP-4GX8GT-8BT（8×90W）、LT-IS6328XGP（24 PoE + 4×10G 工业）、LT-S8328XGP（商业 24 PoE）。
- **首次接触**：*"Industrial PoE++ with PD watchdog, G.8032 ring and 5-year warranty — at the price you pay for a CRS328."*
- **异议**：UL/铁路/IP67（放弃，推荐 ORing）；PLANET 有 Modbus TCP（承认，问是否真用；向工厂争取）。

---

## 6. 话术库

### 6.1 一句话定位（三选一按对象）

- 对 WISP：*"Keep your RouterOS. Upgrade the switch in the cabinet."*
- 对分销商：*"The industrial and PoE++ line MikroTik never made — under your brand."*
- 对方案商：*"Marvell-based managed switches built to be integrated: SNMP, MQTT, SSH, no cloud lock-in."*

### 6.2 电梯陈述

**30 秒**：*"We supply Marvell-based managed switches — same silicon family as MikroTik's CRS3xx — with what MikroTik doesn't do: G.8032 ring under 20 ms, 802.3bt 90 W PoE++, industrial DIN-rail with dual DC and -40 to 75 °C, and full SNMP/MQTT/SSH integration. Three to five-year warranty, white-label with no software MOQ. Our 24-port 4×10G unit lands around 130 dollars."*

**2 分钟**（加上）：*"We're a trading company, not the factory — which is the point. You get one supplier for access and core (Marvell and Centec platforms), stock in small quantities, pre-configured units, English documentation written for operators not engineers, and a European-hours support line. Our integration package includes the MIB files, trap list, Cisco-style CLI reference, netmiko and Ansible samples, and Zabbix/LibreNMS templates, so a switch is in your NMS the day it arrives. We don't compete with RouterOS as a platform; we replace the switches around it."*

### 6.3 按对手的比较话术

| 对手 | 话术要点（英文） | 中文注意 |
|---|---|---|
| **CSS326** | *"Same price class, but you get CLI/SSH, SNMPv3 with traps, LLDP, MSTP and G.8032, QinQ, 480 ACLs, static routing, 4×10G uplinks and a 3-year warranty. SwOS gives you read-only SNMP and no traps — it can't live in an NMS."* | 只在 CSS 场景用"全面碾压"口吻 |
| **CRS326** | *"RouterOS is a great platform — we're not asking you to leave it. Where CRS326 stops is ring protection (RSTP only), PoE++ and industrial packaging. That's what we add, and we come in below CRS326's price with 4×10G."* | 绝不说 RouterOS 没有 QinQ/MSTP/L3 |
| **CRS328-24P** | *"Same 24 PoE ports and 4×10G, plus PD watchdog and PoE scheduling; for 802.3bt or -40 °C we have the industrial line. CRS328 is af/at only, -20 °C, one-year warranty."* | 预算 280W vs 450W 主动说明，提供 440W 版 |
| **TP-Link SG3428X** | *"Feature-for-feature close — TP-Link also has ERPS. The difference is what's around it: industrial DIN-rail models with the same firmware, 802.3bt, DI/DO and RS-485, and white-label. TP-Link can't put your name on it."* | 承认 TP-Link 强，避免在商业 24 口硬碰 |
| **Ubiquiti** | *"If you want a controller-driven UI, UniFi is excellent. If you want CLI, SNMP traps, ERPS, QinQ and no controller dependency, that's us — at about a third of USW-Pro-24."* | 别攻击 UniFi 品牌 |
| **Teltonika TSW212** | *"Good box for 129 dollars. Ours adds 4×10G or 2.5G uplinks, G.8032 ring, 16K MAC / 12 Mbit buffer, PoE++ options, DI/DO/RS-485 and a 5-year warranty — for roughly the same money."* | 同渠道竞争，要有数据 |
| **PLANET / ORing** | *"PLANET-class features — ERPS, MSTP, wide temperature, DIN-rail, relay alarm — at MikroTik-class pricing. If you need EN 50155 rail or UL Class I Div 2, ORing is the right call; for everything else, compare our datasheet."* | 主动让出铁路/UL 项目 |
| **中国直供** | *"Cheaper boxes exist. Ask them for the MIB file, the CLI reference, the release notes for the last two years, and a five-year warranty. We ship those with the switch."* | 不比裸价 |

### 6.4 异议处理（15 条）

| # | 异议 | 回应要点 |
|---|---|---|
| 1 | "MikroTik 更便宜/够用" | 对 CSS：同价更强；对 CRS：$130 vs $209 且 4×10G；再问"够用"是否含 ERPS、PoE++、-40°C、Trap |
| 2 | "我们只用 RouterOS" | 同意；只替换交换层；给"混合拓扑图"：RouterOS 路由 + Saga 交换 + LLDP 互通 |
| 3 | "没听过你们" | Marvell 平台、同芯片家族、3/5 年保修、样机免费、土耳其 NMS 案例、公开 release notes |
| 4 | "没有 API" | 有 SNMP v3/Trap、MQTT、SSH/SCP、Cisco 风格 CLI（netmiko/Ansible）；REST 在 OEM 定制路线；问清对方现用采集方式 |
| 5 | "中国货质量" | Marvell 原厂支持、IXIA 测试、8 小时老化、IEC 61000-4 数据、MTBF >200k h、5 年保修、欧洲 RMA |
| 6 | "我们的射频吃 24V 被动 PoE" | 承认只有 802.3af/at/bt；新款射频支持 af/at；老设备用 48→24V 转换或保留 MikroTik 注入器；PoE 看门狗对射频死机更有价值 |
| 7 | "商业款只有 0~50°C" | 是，所以塔站/机柜推工业款 -40~75°C；商业款只进机房 |
| 8 | "没有 UL" | MikroTik 也没有；有 CE/UKCA/FCC/RoHS/REACH；UL 项目坦诚放弃 |
| 9 | "交期/库存" | 芯片库存、SKD/CKD、欧洲小仓（波兰）；对比 MikroTik 2021–23 缺货史 |
| 10 | "支持时区" | 欧洲工作时间英语支持、远程会话、备件先行 |
| 11 | "固件安全/后门顾虑" | 无云依赖、可关 Telnet/HTTP、SSH 公钥、SHA-512、登录锁定、syslog 审计；SBOM/签名固件在 CRA 准备清单里 |
| 12 | "TP-Link/Ubiquiti 有云管理" | 对，我们不做云锁定；要云用你的 NMS（SNMP/MQTT） |
| 13 | "为什么不直接找工厂" | 多供应商组合（Marvell + Centec）、小批量现货、预配置、英文运维文档、欧洲 RMA、渠道保护 |
| 14 | "PLANET 有 Modbus TCP / 1588" | 承认；问是否真用；列入定制路线 |
| 15 | "你们能撑 5 年吗" | 工厂 2000 年代起、8000 ㎡、自有 PCBA、固件 5.x→7.5 公开记录、5 年保修书面化 |

### 6.5 邮件模板

**① 冷启动 → MikroTik 分销商**
> Subject: The industrial & PoE++ line to sit next to your MikroTik shelf
>
> Hi {Name}, you carry MikroTik and probably get asked for things they don't make: DIN-rail industrial managed switches, 802.3bt 90 W PoE++, G.8032 rings, 24-port units with four 10G uplinks under 150 dollars. We supply exactly that — Marvell-based, Cisco-style CLI, full SNMP/MQTT, 3–5-year warranty, white-label with no software MOQ. Attached: a one-page MikroTik-to-Saga cross-reference. Would two evaluation units be useful? — Simon

**② 冷启动 → WISP**
> Subject: Tower-cabinet switch: dual DC, -40 °C, G.8032, PoE++ — around 120 dollars
>
> Hi {Name}, if your towers run CRS or CSS switches, you may be working around three things: no ring protection beyond RSTP, no 802.3bt, and 10–30 V power. Our LT-IS6312XG is an 8×GbE + 4×10G SFP+ DIN-rail unit, dual 12–58 VDC, -40~75 °C, ERPS under 20 ms, SNMP traps and LLDP into LibreNMS/Zabbix out of the box. Keep RouterOS at the core; we replace the cabinet switch. Happy to send one unit for your bench. — Simon

**③ 样机后跟进**
> Subject: {Model} on your bench — three things to try
>
> Hi {Name}, before you form an opinion, please try: (1) pull a ring link and watch the ERPS log — you should see sub-20 ms; (2) point it at your Zabbix/LibreNMS with the attached template — traps and PoE/temperature OIDs are included; (3) `show running-config` over SSH with key auth. Anything that doesn't behave like your CRS would — tell me, that's the feedback I need. — Simon

**④ OEM 提案**
> Subject: Your own switch line — 20 units to start, no software MOQ
>
> Hi {Name}, based on our call, here is a private-label proposal: your logo, model names, serial format, default IP and SNMP enterprise OID from unit one at no MOQ; silk-screen and packaging from 20 units; web UI re-skin from 50. Warranty 3 years commercial / 5 years industrial under your brand, RMA via our EU address. Draft price list and CRA-readiness note attached. — Simon

### 6.6 LinkedIn 三句

1. *"Saw you run a MikroTik-based network in {country}. We make the industrial/PoE++ switches MikroTik doesn't — sending a cross-reference if useful."*
2. *"Your NMS screenshots look great — do your edge switches push traps/MQTT into it, or do you poll? We build switches for exactly that."*
3. *"Distributor for MikroTik/Ubiquiti in {country}? We fill the DIN-rail / 802.3bt / G.8032 gap under your brand, no software MOQ."*

### 6.7 30 分钟 Demo 剧本

| 分钟 | 内容 | 目的 |
|---|---|---|
| 0–3 | 拓扑：RouterOS 路由器 + 2 台 Saga 交换机成环 + 1 台笔记本 | 展示"共存" |
| 3–8 | SSH 公钥登录，`show version` / `show running-config` / `configure terminal` 建 VLAN + trunk | Cisco 风格 CLI 熟悉感 |
| 8–13 | 拔环上一根光纤，ping 不丢或丢 1 个，`show erps` 看切换时间 | ERPS <20ms |
| 13–18 | Zabbix/LibreNMS 里出现设备，触发 linkDown Trap，看 PoE/温度 OID | Integration-ready |
| 18–22 | PoE 看门狗：拔摄像头网线模拟死机 → 自动断电重启 | 安防/WISP 痛点 |
| 22–26 | 双分区固件升级 + 回滚；`copy running-config tftp:` | 运维安全 |
| 26–30 | 白牌 Web UI 换皮截图 + OEM 流程 + 报价 | 商务收尾 |

---

## 7. 推广策略与内容资产

### 7.1 渠道组合

| 渠道 | 做法 | 预期 |
|---|---|---|
| **Outbound（LinkedIn + 邮件）** | 按国家切片 200 家（波兰 60、捷克斯 40、德奥 40、英国 30、意西 30）+ 美国 30 家方案商；评分卡筛选 | 主渠道，3–5% 回复 |
| **MikroTik 公开名单** | mikrotik.com/buy（约 118 国分销商）、/consultants、/training/centers | B 类与影响者 |
| **行业协会** | KIKE（波兰）、AIIP（意大利）、WISPA（美国）、捷克 ISP 协会 | A 类集中地 |
| **活动（参会不摆摊）** | MUM 欧洲场、PLNOG、WISPAPALOOZA | 认识顾问与分销商 |
| **Inbound 内容** | LibreNMS OS 定义 / Zabbix 模板开源；MikroTik↔Saga 对照 PDF；"CRS326 vs" 技术对比页；MQTT/SNMP 集成指南 | 长尾、可信度 |
| **OEM 客户的客户** | 分销商 house brand 落地后，帮他们做销售培训与资料 | 放大器 |
| **不做** | 论坛/Reddit 推销、Amazon 零售、价格战 | — |

### 7.2 内容资产清单（按优先级）

1. **MikroTik ↔ Saga 对照表 PDF**（2 页，来自 Excel）
2. **Integration Package v1**：MIB 文件 + OID 速查 + Trap 列表 + CLI 速查 + netmiko/Ansible 样例 + 升级/回滚指南 + MQTT 说明 + Zabbix/LibreNMS 模板
3. **一页纸 × 4**：WISP 版 / 分销商 OEM 版 / NMS 集成版 / 工业 PoE++ 版
4. **ERPS 断链演示视频**（60 秒）+ Zabbix 接入视频（3 分钟）
5. **土耳其 NMS 案例**（匿名一页）
6. **CRA 准备度说明**（SBOM、签名固件、漏洞披露流程、更新承诺）——2027 前欧洲 OEM 必问
7. 波兰语/德语两页资料

### 7.3 样机与 POC 政策

- 常备 4 款各 2 台：LT-S8328XG、LT-IS6312XG、LT-IS6312GP-2BT、LT-S8328XGP。
- A/C/D 类：免费 1 台，30 天，不退；B 类：2 台按成本价，试销 20 台后返还差价。
- 每台样机随附：Integration Package U 盘、对照表、快速上手卡（默认 IP/账号、5 条 CLI）。

### 7.4 OEM 套餐设计

| 套餐 | 起订 | 内容 |
|---|---|---|
| Bronze | 1 台 | Logo、型号名、SN 格式、默认 IP、MAC 段、SNMP 企业 OID |
| Silver | 50 台 | + Web UI 换皮（Page Package）、登录页、帮助链接、包装贴纸 |
| Gold | 200 台 | + 外壳丝印/颜色、彩盒、定制默认配置、私有 MIB 命名、固件功能定制评估 |

### 7.5 定价阶梯（建议）

| 分段 | 进价 ¥ | ≈成本 $ | 建议售价 $ | 对标锚 |
|---|---|---|---|---|
| 24G+4×10G 商业 | 710 | 100 | 130（>100 台 120） | CRS326 $209 / SG3428X ≈$259 |
| 24 PoE+4×10G 280W 商业 | 1010 | 142 | 185 | CRS328-24P $489 |
| 工业 8G+4×10G | 840 | 118 | 155 | CRS310-1G-5S-4S+ $199 / TSW212 $129 |
| 工业 8 PoE+4×2.5G | 820 | 115 | 150 | CRS112-8P $209 / IGS-5225 $757 |
| 工业 8×90W PoE++ | 询价 | — | — | CRS320 $299–489 |
| L3 24G+4×10G | 1500 | 211 | 275 | CRS326+RouterOS L3 / CRS354 $599 |
| 48G+4×10G | 1470 | 207 | 269 | CRS354 $599 |

### 7.6 KPI 与 90 天

| 周期 | 动作 | KPI |
|---|---|---|
| 0–30 天 | 对照表 PDF、Integration Package v1、样机备货、向工厂发确认清单 | 资产完成；样机到位 |
| 31–60 天 | 200 家名单 + 评分；首轮 LinkedIn/邮件；MikroTik 分销商名单扫描 T1 国家 | 回复 ≥8 家；样机发出 ≥4 台 |
| 61–90 天 | Zabbix/LibreNMS 模板开源；土耳其案例；OEM 提案 ≥2 份 | POC ≥2；OEM 意向 ≥1 |

---

## 8. 产品与供应商侧建议（向 SmartByte 争取，按优先级）

| # | 事项 | 为什么 | 对标 |
|---|---|---|---|
| 1 | **MQTT topic/payload 文档 + TLS** | C 类客户的钩子；没文档等于没有 | — |
| 2 | **完整私有 MIB + Trap 清单 + Zabbix/LibreNMS 官方模板** | Integration Package 基础 | MikroTik 有官方 MIB |
| 3 | **REST API 路线图**（哪怕只读） | 回答"API"异议 | RouterOS REST |
| 4 | **CRA 准备**：SBOM、签名固件、漏洞披露流程、≥5 年安全更新承诺 | 2027-12 欧盟强制；OEM 客户必问 | 所有欧盟制造商 |
| 5 | **24 PoE + 4×10G + 440W/850W** 商业款 | 正面对 CRS328-24P 450W | CRS328-24P |
| 6 | **2.5G 电口型号**（8×2.5G + 2×10G） | CRS310-8G+2S+ 与 Wi-Fi 6/7 AP 场景 | CRS310-8G+2S+ $149 |
| 7 | **Modbus TCP / IEEE 1588 透传** | 工业投标项 | PLANET |
| 8 | **商业 8 口 L2+ 恢复出货 + 8G+2×10G 定价** | 8 口档缺位 | CSS610 $119 |
| 9 | **Ansible collection / netmiko 驱动验证** | 自动化承诺要有证据 | — |
| 10 | **AC3 替代 AC5 时的功能差异表** | 7.5.0 仅 AC5；避免客户踩坑 | — |
| 11 | **-40°C 测试报告、IEC 61000-4 报告、MTBF 计算书**（英文） | 德国/英国客户会要 | PLANET/ORing 都给 |
| 12 | **渠道保护协议** | 去中介化风险 | — |

---

## 9. 风险与不打的地方

| 风险 | 说明 | 对策 |
|---|---|---|
| 商业款温度 | 0~50°C 被 CRS326 -40 打脸 | 场景分流：机房商业款，其他工业款 |
| 被动 PoE | WISP 老射频 | 6.4 第 6 条；不硬撑 |
| TP-Link 在商业 24 口 | 有 ERPS、终身保修、街价 $259 | 24 口只做敲门 SKU |
| Teltonika 在工业 8 口 | $129 MSRP、同渠道 | 拉开 10G/ERPS/PoE++/DI-DO/5 年 |
| 去中介化 | SmartByte 官网直接卖 OEM | 多供应商组合、文档、现货预配置、欧洲 RMA、渠道保护协议 |
| 固件单一供应商 | AC5 停产转 AC3 | 索要差异表；样机验证 |
| 没有 API/云 | C 类客户硬要求 | SNMP/MQTT/SSH 三件套 + OEM 路线 |
| 品牌弱 | 首单信任 | 样机 + 保修 + 案例 + 开源模板 |
| **不打** | 全光 SFP+/25G/100G、路由器、无线、Homelab、铁路/IP67/UL、8 口裸价战 | — |

---

## 附录 A：MikroTik 交换机全产品线（去重 49 款，价格为你抓取值*，✅ 为实测）

| 型号 | 价格 | 端口 | 芯片 | OS | 温度 | PoE 出 |
|---|---|---|---|---|---|---|
| CSS106-5G-1S | $39.95* | 5×GbE + 1×SFP | QCA8337 | SwOS | -20~70 | 被动 |
| CSS106-1G-4P-1S | $55.95* | 1×GbE + 4×PoE + 1×SFP | QCA8337 | SwOS | -20~70 | 被动 |
| CSS318-16G-2S+IN | $139* | 16×GbE + 2×SFP+ | 98DX2518 | SwOS | -40~70 | — |
| CSS326-24G-2S+RM | **$159 ✅** | 24×GbE + 2×SFP+ | 98DX3216 | SwOS | -20~70 | — |
| CSS610-8G-2S+IN | **$119 ✅** | 8×GbE + 2×SFP+ | 88E6193X | SwOS Lite | -20~60 | — |
| CSS610-8P-2S+IN | $139–229* | 8×PoE + 2×SFP+ | 88E6193X | SwOS Lite | — | af/at 140W |
| CSS610-1Gi-7R-2S+OUT (netPower Lite 7R) | $99* | 1×GbE + 7×反向 PoE + 2×SFP+ | 98DX3236 | SwOS | -40~70 | 反向 |
| CRS106-1C-5S | $89* | 1 Combo + 5×SFP | QCA8511 | RouterOS | -20~60 | — |
| CRS112-8G-4S-IN | $119* | 8×GbE + 4×SFP | QCA8513 | RouterOS | -20~60 | — |
| CRS112-8P-4S-IN | $199–209* | 8×PoE + 4×SFP | QCA8511 | RouterOS | -20~60 | af/at/被动 |
| CRS210-8G-2S+IN | $229* | 8×GbE + 2×SFP+ | QCA8519 | RouterOS | — | — |
| CRS212-1G-10S-1S+IN | $219* | 1×GbE + 10×SFP + 1×SFP+ | QCA8519 | RouterOS | — | — |
| CRS304-4XG-IN | $199* | 4×10G 电口 | 98DX2528 | RouterOS | — | — |
| CRS305-1G-4S+IN | $149* | 1×GbE + 4×SFP+ | 98DX3236 | 双启动 | -40~70 | — |
| CRS309-1G-8S+IN | $229–269* | 1×GbE + 8×SFP+ | 98DX8208 | 双启动 | -40~60 | — |
| CRS310-1G-5S-4S+IN/OUT | $195–249* | 1×GbE + 5×SFP + 4×SFP+ | 98DX226S | 双启动 | -40~60 | — |
| CRS310-8G+2S+IN | $149* | 8×2.5G + 2×SFP+ | 98DX226S | 双启动 | -40~60 | — |
| CRS312-4C+8XG(-RM) | $349–699* | 8×10G 电 + 4 Combo 10G | 98DX8212 | 双启动 | -20~60 | — |
| CRS317-1G-16S+RM | $499* | 1×GbE + 16×SFP+ | 98DX8216 | 双启动 | -20~60 | — |
| CRS318-16P-2S+RM (netPower 16P) | $279–329* | 16×PoE + 2×SFP+ | 98DX3236/226S | 双启动 | -20~60 | af/at/被动 |
| CRS318-1Fi-15Fr-2S (netFiber 9 类) | $169–225* | 15×100M 光 + 1×1G + 2×SFP | 98DX224S/3236 | 双启动 | -20~70 | 反向 |
| CRS320-8P-8B-4S+RM | $299–489* | 8×at + 8×bt + 4×SFP+ | 98DX226S | 双启动 | — | af/at/bt |
| CRS326-24G-2S+IN | $199* | 24×GbE + 2×SFP+ | 98DX3236 | 双启动 | -40~60 | — |
| CRS326-24G-2S+RM | **$209 ✅** | 24×GbE + 2×SFP+ | 98DX3236 | 双启动 | -40~60 | — |
| CRS326-4C+20G+2S+RM | $239* | 20×GbE + 4 Combo + 2×SFP+ | 98DX3236 | 双启动 | -20~60 | — |
| CRS326-4C+20G+2Q+RM | $999* | 20×2.5G + 4 Combo + 2×QSFP+ | 98DX8332 | RouterOS | -20~60 | — |
| CRS326-24S+2Q+RM | $599* | 24×SFP+ + 2×QSFP+ | 98DX8332 | 双启动 | -20~60 | — |
| CRS328-24P-4S+RM | **$489 ✅** | 24×PoE + 4×SFP+ | 98DX3236 | 双启动 | -20~60 | af/at/被动 450W |
| CRS328-4C-20S-4S+RM | $299–449* | 20×SFP + 4 Combo + 4×SFP+ | 98DX3236 | 双启动 | -20~60 | — |
| CRS332-32S+RM | $749* | 32×SFP+ + 6 Combo | 98DX8332 | 双启动 | -20~60 | — |
| CRS354-48G-4S+2Q+RM | **$599 ✅** | 48×GbE + 4×SFP+ + 2×QSFP+ | 98DX3257 + QCA9531 | 双启动 | -20~60 | — |
| CRS354-48P-4S+2Q+RM | $999* | 48×PoE + 4×SFP+ + 2×QSFP+ | 98DX3257 | 双启动 | -20~60 | af/at |
| CRS418-8P-8G-2S+RM | $449–499* | 8×PoE + 8×GbE + 2×SFP+，2.2GHz 四核，双 AC，USB3 | 98DX226S | RouterOS v7 | -20~70 | af/at/被动 150W |
| CRS504-4XQ-IN/OUT | $799–899* | 4×QSFP28 | 98DX4310 | RouterOS v7 | -40~70 | — |
| CRS510-8XS-2XQ-IN | $999* | 8×SFP28 + 2×QSFP28 | 98DX4310 | RouterOS v7 | -40~70 | — |
| CRS518-16XS-2XQ-RM | $1595* | 16×SFP28 + 2×QSFP28 | 98DX8525 | RouterOS v7 | — | — |
| CRS520-4XS-16XQ-RM | $2195* | 4×SFP28 + 16×QSFP28 | 98CX8410 | RouterOS v7 | — | — |
| CRS804 / CRS812 系列 | $1295* | 400G 级 | 98DX7335 | RouterOS v7 | — | — |

> 抓取值中同型号多价并存（如 CRS328-4C-20S $299/$449、CSS610-8P $139/$229、CRS320 $299/$489）系脚本两次抓取不一致，报价前以官网为准。

## 附录 B：SmartByte 关键 SKU（进价 ¥，2026.09–12）

见 Excel `SmartByte关键SKU` sheet。核心：LT-S8328XG-4XS24GT-S 710 / -XGP 1010 / LT-S8328G-4GX24GT-S 460 / -GP 1200 / LT-S8352XG 1470 / -XGP 1870 / LT-S8528XG 1500 / LT-IS6306G 660 / LT-IS6310G 700 / LT-IS6312G 740 / LT-IS6312XG 840 / LT-IS6312GP 820 / -2BT 920 / LT-IS6316XG 1400 / LT-IS6318G 1180 / LT-IS6318XGP 1660 / LT-IS6320G-D 1560 / LT-IS6328XG-D 1960 / LT-IS6328XGP 2200 / -4BT 2400 / LT-IS6328XG-4XS16GX8GC-D 2650 / Bypass 960–1640 / 工业 L3 1900–3100。

## 附录 C：数据来源

- mikrotik.com 产品页（CSS326、CRS326、CRS328-24P、CSS610-8G、CRS354-48G：2026-09 实测），help.mikrotik.com SwOS/CRS3xx/L3HW 文档，forum.mikrotik.com ERPS 请求帖
- smartbyte-switch.com 首页、OEM/ODM、Firmware Highlights、7.5.0 release notes、LT-S8328XG-4XS24GT-S 与 LT-IS6312GP-4GX8GT-8BT 规格页（2026-09）
- 仓库：Saga Feature List 7.5.x L2+/L3、Marvell CLI/Web 手册、SmartByte 价格表、MikroTik 抓取 Excel、GPT/Claude 对话记录
- UN Comtrade（拉脱维亚 HS 851762 出口 2024）、Lursoft（MikroTik 营收）
- 相邻品牌：store.ui.com（USW-Pro-24 $399）、TP-Link SG3428X 零售页（ERPS、$259–367）、PLANET IGS-5225 零售页（$757–828）、Teltonika TSW212 零售页（$129 MSRP）
- 欧盟 CRA：Regulation (EU) 2024/2847，2024-12-10 生效，2026-09-11 起漏洞上报义务，2027-12-11 全面适用
