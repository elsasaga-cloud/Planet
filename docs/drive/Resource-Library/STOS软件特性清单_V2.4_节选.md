# Saga Software Feature List_EN_V2.4.pdf（节选）

> 来源：Google Drive `Saga Telecom Resource Library/Saga Software Feature List_EN_V2.4.pdf`（文件 id `1l645q1AklHmGQ1HmVAjrX0I14qfbClii`）  
> 链接：https://drive.google.com/file/d/1l645q1AklHmGQ1HmVAjrX0I14qfbClii/view  
> 抓取：2026-10-20 通过 Drive 连接器 `read_file_text` 提取（工具只返回前约 30%，其余截断）；本文为**结构化节选**，逐项功能表以 Drive 原件为准。  
> 判断：文档抬头为 STOS（Saga Telecom OS）V2.4 / 固件 V3.0.22 / 2025-12-12，含 EB / MS / MA 三档 license，覆盖 VxLAN-EVPN、MPLS、BGP、MLAG、堆叠 8 台等——这是 **CENTEC 高速（STH 系列）平台**的软件清单；Marvell 商用/工业管理型（STC/STI）另有 `Saga Feature List_7.5.x_L2+.xlsx` / `_L3.xlsx`（见 Drive 对应目录，暂未入库，见 00-Drive盘点与入库方案）。

## 文档基本信息
- 名称：Saga Software Feature List（STOS）V2.4；对应固件版本 V3.0.22；发布 2025-12-12。
- License 三档：**EB**（基础）/ **MS**（中级）/ **MA**（高级，含 MPLS 等运营商特性）。表中 ● = 支持，○ = 可选/需许可或后续版本，— = 不支持。
- 网站落款：sagatele.com（与 MUST KNOW 系列 PDF 中的 sagatelecom.com.cn 不一致，已记入 Q-19）。

## 功能大类（节选，按原文顺序）
| 大类 | 要点（节选） |
|---|---|
| L2 交换 | VLAN（802.1Q/QinQ/Voice VLAN/Private VLAN）、MAC 管理、LACP/静态聚合、STP/RSTP/MSTP、风暴抑制、端口隔离、镜像、巨帧 |
| 环网 | ERPS（G.8032）、专有快速环、BFD 联动 |
| 组播 | IGMP v1/v2/v3 Snooping、MLD Snooping、IGMP Proxy、PIM-SM/SSM（MS/MA） |
| IPv4/IPv6 路由 | 静态、RIP、OSPFv2/v3、IS-IS、BGP4/BGP4+（eBGP/iBGP）、策略路由、ECMP、VRF-Lite |
| 可靠性 | BFD、VRRP/VRRPv3、MLAG、堆叠（最多 8 台）、ISSU（○） |
| OAM | 802.3ah / 802.1ag CFM、Y.1731、sFlow、NetStream（○） |
| PoE 管理 | 端口供电管理、PoE 看门狗、定时供电（PoE 型号） |
| QoS | 8 队列、SP/WRR/DRR、CAR、流量整形、DSCP/802.1p 重标记、分层 QoS（MA） |
| VxLAN / EVPN | VxLAN 二层网关、集中式/分布式三层网关、BGP-EVPN（MS/MA） |
| MPLS | LDP、MPLS L2VPN（VPWS/VPLS）、L3VPN、TE（**仅 MA**） |
| 安全 | ACL（L2/L3/L4、IPv6）、802.1X、MAC 认证、Portal、DHCP Snooping、IP Source Guard、DAI、AAA（RADIUS/TACACS+）、SSH v2、CPU 防护 |
| 时间同步 | NTP、SNTP、**PTP（1588v2，BC/TC）**、SyncE（○） |
| 管理 | CLI（Console/Telnet/SSH）、Web、SNMP v1/v2c/v3、RMON、Syslog、NETCONF/YANG（○）、ZTP、USB 升级 |
| **Cloud Management** | 原文标注 **○ \*8**（可选项，带脚注 8；脚注内容在截断部分，未读到）——与本仓库继承规则 INH「Saga 不做云管理」冲突，已记 Q-19，默认仍按"不主动承诺云管理"执行 |
| RPC-API | RESTCONF/gRPC（○） |

## 对销售的用法
1. 客户问"你们软件支持什么" → 先分平台：STC/STI（Marvell）答 L2+/L3 功能（看 7.5.x xlsx），STH（CENTEC）答本清单。
2. 涉及 MPLS/EVPN/BGP 等运营商特性 → 只在 STH 上承诺，并说明 license 档位（MA）。
3. 云管理：**不要主动写进邮件**，客户追问时回答"可按项目评估"，等 Q-19 由 Simon 裁决。
