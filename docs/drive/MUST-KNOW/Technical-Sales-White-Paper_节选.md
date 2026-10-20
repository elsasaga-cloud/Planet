# Technical Sales White Paper.pdf

> 来源：Google Drive `MUST KNOW/Technical Sales White Paper.pdf`（文件 id `1qh9W6ton_UPefqzTIYlnRBrcBLOMvNW-`，169 KB，Drive 修改时间 2026-04-29）  
> 链接：https://drive.google.com/file/d/1qh9W6ton_UPefqzTIYlnRBrcBLOMvNW-/view  
> 抓取：2026-10-20 通过 Drive 连接器 `read_file_text` 提取；英文原文逐句保留，仅做换行/列表整理，不改措辞。  
> **节选**：全文约 2 万字符，连接器单次提取上限内只拿到约 70%（§1–§6、§7.1 开头、§8、§9 前半）；§7.2–7.4 与 §9 末尾未抓取。需要全文时按链接打开 Drive 原件。

Document Version: 1.0 · Last Updated: 2026.04.28 · Intended Audience: Technical Sales Engineers, Pre-Sales Consultants · Classification: Internal Sales Reference / Customer-Facing White Paper

# Marvell AC5/AC5+ Competitive Analysis

## 1. Market Landscape & Competitive Positioning
Market Segment: Enterprise Access / SMB Managed Switches. Low-end pressure: Realtek RTL9303/RTL9313. Same-tier: Marvell AC5/AC5+ vs Microchip LAN969x. High-end downward pressure: Broadcom BCM56170. Regional consideration (China market): CENTEC (China mainland company) CTC8096 — domestic substitution pressure, relevant in gov/carrier projects.

One-line summary per vendor
- Realtek RTL9313 — Price is the only weapon — hits a wall at L2
- Marvell AC5 — Best-integrated enterprise SoC — full features, single chip, Linux-native
- Marvell AC5+ — AC5 upgraded — 25G ports, larger tables, SONiC-ready
- Microchip LAN969x — TSN/PTP champion, but limited ecosystem and market share
- Broadcom BCM56170 — High-end enterprise king — powerful but expensive
- CENTEC CTC8096 — Domestic alternative — policy-driven, maturing SDK, higher power

## 2. Hardware & Platform Overview
| Specification | Realtek RTL9313 | Marvell AC5 (98DX25xx) | Marvell AC5+ (98DX35xx) | Microchip LAN969x | Broadcom BCM56170 |
|---|---|---|---|---|---|
| Market Segment | SOHO / Low-end SMB | SMB / Enterprise Access | SMB/Enterprise / Whitebox | Industrial / Enterprise | Enterprise / DC Access |
| Switching Capacity | 65 Gbps | ~100 Gbps | ~200 Gbps | ~65 Gbps | ~200 Gbps |
| Max Port Speed | 10GE | 10GE | 25GE | 10GE | 25GE |
| Integrated CPU | MIPS/ARM | ARM Cortex-A55 | ARM Cortex-A55 | ARM Cortex-A53 | ARM Cortex-A9 |
| CPU Architecture / Cores | 32-bit / 1–2 | 64-bit / 2 | 64-bit / 4 | 64-bit / 2 | 64-bit / 2 |
| Process Node | 28nm | 12nm | 12nm | 16nm | N/A |
| Typical Power | 5–8W | 8–12W | 12–18W | 5–8W | 15–20W |
| Chip Price Range | Low ($5–15) | Mid ($20–45) | Mid-High ($40–70) | Mid ($20–40) | High ($50–100+) |
| Total BOM Cost | Lowest | Low-Mid | Mid | Mid | High |

Chip price ranges are indicative estimates only and subject to market conditions and volume pricing.

Key Sales Point — Software & Ecosystem Gap vs BCM56170: BCM56170 is also a single-chip SoC — BOM cost is comparable at the chip level. The gap is in software and ecosystem: → AC5+ has official SONiC/sonic-buildimage support; BCM56170 does not. → Marvell switchdev is mainline kernel — zero ramp-up for Linux engineers; Broadcom SDK requires NDA and months of onboarding. → AC5 has broader distribution and stronger FAE coverage at SMB account sizes — Broadcom support quality scales with account size.

## 3. Feature Capability Comparison
### 3.1 Layer 2
| L2 Feature | RTL9313 | AC5 | AC5+ | LAN969x | BCM56170 |
|---|---|---|---|---|---|
| MAC Table (FDB) | 16K | 32K | 64K | 16K | 64K |
| VLAN Support | 4K | 4K | 4K | 4K | 4K |
| MSTP Instances | 16 | 64 | 64 | 64 | 64 |
| LAG Groups × Members | 8×8 | 16×8 | 32×8 | 16×8 | 32×8 |
| LACP (802.3ad) / 802.1Q | ✅ | ✅ | ✅ | ✅ | ✅ |
| QinQ (802.1ad) | Basic | Full | Full | Full | Full |
| MACsec (802.1AE) | ❌ | ✅ | ✅ | Partial | ✅ |
| OAM (802.3ah/1ag) | Basic | ✅ | ✅ | Strong | ✅ |
| PTP / IEEE1588 | Basic | ✅ | ✅ | Best-in-class | ✅ |

Note: L2 feature parity is relatively high across vendors. Differentiation starts at L3 and above.

### 3.2 Layer 3 — Where the Gap Opens Up
Key Sales Point — Killing Realtek at L3: If the customer needs hardware L3 routing, Realtek is eliminated immediately. Realtek's "L3" is largely software-forwarded through the CPU — performance degrades sharply under real traffic load. AC5 delivers true hardware-accelerated L3 at full line rate.

| L3 Feature | RTL9313 | AC5 | AC5+ | LAN969x | BCM56170 |
|---|---|---|---|---|---|
| Hardware L3 Routing | Weak/SW-based | Full HW | Full HW | Hardware | Full HW |
| IPv4 Route Table (LPM) | 1K–2K | 8K–16K | 16K–32K | 4K–8K | 16K–32K |
| IPv6 Route Table | 512 | 4K–8K | 8K–16K | 2K–4K | 8K–16K |
| ECMP | Basic | ✅ | Enhanced | ✅ | ✅ |
| VRF (Multi-VRF) | ❌ | ✅ | ✅ | Limited | ✅ |
| MPLS | ❌ | Basic | ✅ | ❌ | ✅ |
| VXLAN Termination | ❌ | ✅ | ✅ | Limited | ✅ |
| BFD | ❌ | ✅ | ✅ | ✅ | ✅ |

### 3.3 ACL / Security / QoS — Enterprise RFP Checklist
| Security/QoS Feature | RTL9313 | AC5 | AC5+ | LAN969x | BCM56170 |
|---|---|---|---|---|---|
| ACL/TCAM Rules | 256–512 | 3K–6K | 6K–12K | 1K–2K | 6K–12K |
| ACL Match Fields | Basic 5-tuple | Rich (L2–L4+) | Rich (L2–L4+) | Moderate | Most Comprehensive |
| Hardware Policer | Basic | Full | Full | ✅ | Full |
| QoS Queues per Port | 4–8 | 8 | 8 | 8 | 8 |
| Queue Scheduling | SP Basic | SP+WRR+WFQ | SP+WRR+WFQ | SP+WRR | SP+WRR+DWRR |
| Traffic Shaping | Port-level | Port+Queue | Port+Queue | Port+Queue | Port+Queue |
| Secure Boot | ❌ | ✅ | ✅ | Limited | ✅ |
| Hardware Crypto Engine | ❌ | ✅ | ✅ | ❌ | ✅ |
| DHCP Snooping | SW | HW-assisted | HW-assisted | ✅ | HW |
| Dynamic ARP Inspection / 802.1X | SW / Basic | ✅ | ✅ | ✅ | ✅ |

Key Sales Point — ACL is an RFP Killer: Enterprise procurement RFPs almost always specify minimum ACL rule counts. Realtek at 256–512 rules fails most enterprise RFPs outright. AC5 at 3K–6K rules comfortably meets enterprise requirements. This is your single strongest technical argument against Realtek.

### 3.4 Software Platform — The Deciding Factor for Development Teams
| Software Dimension | RTL9313 | Marvell AC5/AC5+ | LAN969x | BCM56170 |
|---|---|---|---|---|
| Operating System | 32-bit Linux | 64-bit Linux | 64-bit Linux | 64-bit Linux |
| Kernel Version | 4.x (aging) | 5.x/6.x Mainline | 5.x | 5.x |
| Mainline Kernel Driver | None | prestera driver merged | Partial | Closed |
| SDK Approach | RTK SDK (closed) | CPSS + switchdev | MESA (partial open) | OpenNSL/SDKLT (closed) |
| Standard Linux Tools | Not supported | iproute2/bridge/tc | Supported | Limited |
| SONiC Support | ❌ | ✅ (AC5+ officially supported) | ❌ | Most mature |
| SAI Interface | ❌ | ✅ | ❌ | Most mature |
| OpenWrt Support | Mature | Limited | Limited | ❌ |
| Learning Curve | Low | Medium | Medium | High (steepest) |
| Documentation Quality | Fair | Medium (NDA required) | Good (open docs) | Poor (strict NDA) |

Key Sales Point — Standard Linux Matters: AC5's switchdev driver is merged into the mainline Linux kernel. Customer's existing Linux engineers can start on day one — no proprietary OS to learn, no vendor lock-in on the software stack. Compare this to Broadcom where SDK access requires strict NDA and months of ramp-up time.

### 3.5 Supply Chain & Commercial Comparison
| Commercial Dimension | Realtek | Marvell AC5/AC5+ | Microchip | Broadcom |
|---|---|---|---|---|
| Distribution (China) | Extensive | Arrow/WPG/others | Limited | Arrow/WPG |
| Sample Availability | Fast (2–4 wks) | Medium (4–8 wks) | Slow (8–12 wks) | Slow (8–12 wks) |
| FAE Support Quality | Fair | Strong | Fair | Varies by account size |
| Reference Design | Moderate | Complete (schematic+PCB) | Limited | Complete (restricted) |
| Product Lifecycle | 5–8 years | 8–10 years | 5–8 years | 8–10 years |
| EOL Notification | Inconsistent | Formal process (12 months) | Fair | Formal process |
| Supply Stability | Good | Good | Fair | Good |
| Domestic Sub. Risk | None | Moderate | None | Moderate |

## 4. Table Capacity Summary
(FDB 16K/32K/64K/16K/64K; IPv4 LPM 1–2K/8–16K/16–32K/4–8K/16–32K; IPv6 512/4–8K/8–16K/2–4K/8–16K; ACL 256–512/3–6K/6–12K/1–2K/6–12K; LAG groups 8/16/32/16/32 — order: RTL9313 / AC5 / AC5+ / LAN969x / BCM56170)

## 5. China Market: CENTEC CTC8096 Head-to-Head
CENTEC is unavoidable in China's government, carrier, and state-owned enterprise segments, address it directly rather than avoiding the topic. CTC8096 vs AC5: ~100 Gbps both; 32nm vs 12nm; SDK maturing vs multi-generation production-proven; bug fix turnaround slow vs fast; SONiC claimed/limited vs officially supported; mainline Linux driver ❌ vs ✅; production deployments limited vs hundreds of customers globally; chip price low (policy-subsidized) vs mid; domestic policy advantage strong vs ❌; export/global suitability limited vs strong.

Recommended talking track: Step 1 acknowledge honestly (CENTEC wins domestic policy-driven projects). Step 2 pivot to facts (lower power 12nm vs 32nm; production-proven SDK; mainline kernel driver; faster bug resolution). Step 3 practical strategy: many customers run both — AC5 for export and commercial-grade products, CENTEC for domestic policy-compliance models.

## 6. Competitive Decision Tree
Need L3 routing? NO → Realtek RTL9313 (cost-optimized L2). YES → budget sufficient & performance critical? Constrained → does 25G or SONiC matter? YES → Marvell AC5+ (or Broadcom); NO → **Marvell AC5 ← primary recommendation (sweet spot)**. Is TSN/Industrial/strict PTP required? YES → Microchip LAN969x (best TSN); NO → Broadcom BCM56170 (high-end enterprise / DC access).

## 7. Vendor Competitive Response Guide (节选)
7.1 vs Realtek — Their strength → your counter: Low chip price → Total BOM is comparable once you factor in software dev cost for working around Realtek's L3 limitations. Simple SDK → Marvell switchdev = standard Linux, same simplicity, more capability. Large China ecosystem → AC5 has extensive China customer base with proven production deployments.
7.x vs Microchip (结尾可见部分) — Win condition: supply chain stability, ecosystem breadth, SONiC support. Microchip has limited FAE coverage and longer sample lead times.

## 8. AC5 vs AC5+ — Internal Selection Guide
| Criteria | Choose AC5 | Choose AC5+ |
|---|---|---|
| Port Speed | Up to 10GE uplinks | 25GE uplinks needed |
| Route Table | 8K–16K IPv4 sufficient | Need 16K–32K IPv4 |
| ACL Scale | 3K–6K sufficient | Need 6K–12K |
| SONiC | Not required | SONiC deployment planned |
| CPU Workload | Standard protocols | Complex protocol stacks, NFV |
| Target Market | Cost-sensitive SMB | Enterprise, whitebox, future-proof |
| Roadmap | Current-gen product | Platform for next 3–5 years |

## 9. Marvell AC5/AC5+ Key Advantages Summary (节选)
① Single-Chip Integration — CPU + Switch Engine + SerDes + DDR Controller in one SoC → comparable BOM to BCM56170 with no software onboarding overhead; 20% smaller PCB footprint; simplified power design. ② Modern Software Platform — 64-bit Linux, mainline kernel 5.x/6.x, switchdev, SAI; SONiC-ready (AC5+). ③ Enterprise-Grade Feature Set — hardware L3, 3K–12K ACL, full QoS, Secure Boot; MACsec, hardware crypto, DAI, DHCP snooping. ④ Flexible Port Configuration — 1G/2.5G/5G/10G/25G same SerDes, software-defined; covers 24-port to 48-port families. ⑤ Low Power, High Reliability — 12nm, 8–12W typical, industrial SKU available, fanless in most deployments, -40 to 105°C. ⑥ Supply Chain Confidence (后文截断)
