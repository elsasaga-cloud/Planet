# Software Specification（HOS 功能表，170 行）

> 首见于 <https://hohunet.com/product/10g-uplinks-24-ports-2-5g-multi-gigabit-switch/>（抓取 2026-10-21T04:14:13Z）；同一张表的型号在各产品页链接到此。列 EB / MS / MA = license 档（○ = 支持）。

| Type | Feature |
|---|---|
| MAC Address Table | 32K |
| Jumbo Frame | 12K |
| Flow Control | 802.3x (Full-duplex) / Yes |
| Flow Control | Back-Pressure (Half-duplex) / Yes |
| Spanning Tree | IEEE 802.1D (STP) / Yes |
| Spanning Tree | IEEE 802.1w (RSTP) / Yes |
| Spanning Tree | IEEE 802.1s (MSTP) / 64 instances |
| Spanning Tree | Auto Edge Port / Yes |
| Spanning Tree | BPDU Filtering / Yes |
| Spanning Tree | Self Loop Detection / Yes |
| Link Aggregation | IEEE 802.3ad LACP / Yes |
| Link Aggregation | Static Trunk / Yes |
| Link Aggregation | Max. Group / 64 |
| Link Aggregation | Max. Ports/Group / 8 |
| Link Aggregation | Traffic Load Balancing / Yes |
| § | VLAN |
| Voice VLAN | Static VLAN / 4K |
| Voice VLAN | Port-based / Yes |
| Voice VLAN | IEEE 802.1Q Tagged-based / Yes |
| Voice VLAN | Protocol-based / 8 groups |
| Voice VLAN | MAC-based / 1K (shared) |
| Voice VLAN | OUI Mode (Auto/Manual) / 16 OUI |
| Surveillance VLAN | OUI Mode (Auto/Manual) / 16 OUI |
| QinQ (IEEE 802.1ad) | Basic / Yes |
| GARP VLAN Registration Protocol (GVRP) | Yes |
| § | Multicast |
| Common | Multicast Groups / 1K |
| Common | Immediate Leave / Yes |
| Common | Static/Forbidden Router Port / Yes |
| Common | Static/Forbidden Forward Port / Yes |
| Common | Filtering / 128 profiles |
| Common | Throttling / Yes |
| IGMP Snooping | IGMP v1/v2 / Yes |
| IGMP Snooping | IGMP v3 Basic (BISS) / Yes |
| IGMP Snooping | IGMP v2/v3 Querier / Yes |
| MLD Snooping | MLD v1/v2 / Yes |
| Multicast VLAN Registration (MVR) | Yes |
| § | QoS Features |
| Priority Queue | 8 queues/port |
| Queue Scheduling | WRR / Yes |
| Queue Scheduling | WFQ / Yes |
| Queue Scheduling | Strict Pripority / Yes |
| Queue Scheduling | Hybrid(WRR+SP or WFQ+SP) / Yes |
| Class of Service | Port-based / Yes |
| Class of Service | 802.1p / Yes |
| Class of Service | IP TOS Precedence / Yes |
| IP DSCP | Yes |
| Trusted QoS | Yes |
| Rate Limit | Port-based (Ingress/Egress) / Yes |
| § | Access Control List (ACL) |
| Access Rules | 2048 |
| ACL Type | L2/L3/L4 / Yes |
| ACL Type | MAC-based |
| ACL Type | IPv4-based / 512 |
| ACL Type | IPv6-based |
| § | Security |
| AAA | Authentication / Yes |
| TACACS+ | 8 |
| RADIUS | 8 |
| Authentication Manager | IEEE 802.1X / Yes |
| Authentication Manager | MAC Auth / Yes |
| Authentication Manager | Web Auth / Yes |
| Authentication Manager | Guest VLAN / Yes |
| Authentication Manager | Port-based / Yes |
| Authentication Manager | Host-based / Yes |
| Account Manager | Local Authenticatoin / Yes |
| Account Manager | Multiple User Account / 8 |
| Account Manager | Multi-Level Security / Yes |
| Account Manager | Password Recovery Procedures / Yes |
| Management Access | Management VLAN / Yes |
| Management Access | Management ACL / 256 |
| SSL | SSLv2 / Yes |
| SSL | SSLv3 / Yes |
| SSL | TLSv1 / Yes |
| WebUI | HTTPS / Yes |
| CLI | SSH v1/v2 / Yes |
| Port Security | Dynamic Lock / 256 |
| Storm Control | Broadcast / Yes |
| Storm Control | Unknown Multicast / Yes |
| Storm Control | Unknown Unicast / Yes |
| Spanning Tree | BPDU Guard / Yes |
| Protected Port (Port Isolation) | Yes |
| Black Hole MAC | Yes |
| CPU Defence Engine | Yes |
| DoS Prevention | Yes |
| DHCP Snooping (with Option 82) | Yes |
| Dynamic ARP Inspection | Yes |
| IP Source Guard | 256 |
| IP/MAC/Port Binding (IMPB) | Yes |
| § | IPv6 |
| IPv6 Host | Auto Configuration / Yes |
| IPv6 Host | Static IPv6 Address and Prefix Length / Yes |
| IPv6 Host | Static IPv6 Default Gateway / Yes |
| IPv6 Host | IPv6 Neighbor Discovery (ND) / Yes |
| IPv6 Host | IPv6 Duplicate Address Detection / Yes |
| IPv6 Host | ICMPv6 / Yes |
| IPv6 Application | HTTP/HTTPS / Yes |
| IPv6 Application | TELNET / Yes |
| IPv6 Application | SSH / Yes |
| IPv6 Application | SNMP / Yes |
| IPv6 Application | TFTP / Yes |
| IPv6 Application | Syslog / Yes |
| IPv6 Application | PING / Yes |
| IPv6 Application | DHCPv6 / Yes |
| § | Management |
| CLI | Console / 3 sessions |
| CLI | Telnet (RFC854) |
| WebUI | HTTP / Yes |
| WebUI | v1 / Yes |
| WebUI | v2c / Yes |
| SNMP | v3 / Yes |
| File Management | Firmware Upgrade/Backup / Yes |
| File Management | Dual Images / Yes |
| File Management | Configuration Download/Backup / Yes |
| File Management | Multiple Configurations / Yes |
| Upload/Download | TFTP (RFC783) / Yes |
| Upload/Download | HTTP / Yes |
| Upload/Download | UART / Yes |
| Time Management | Local / Yes |
| Time Management | SNTP / Yes |
| Port Management | Friendly Port Name (Port Description) / Yes |
| Port Management | Error Disabled Recovery / Yes |
| Line Management | Console / Yes |
| Line Management | Telnet (RFC854) / Yes |
| Line Management | SSH v1/v2 / Yes |
| DHCP | Client / Yes |
| DHCP | DHCP SNOOPING / yes |
| DHCP | Server / yes |
| DHCP | Relay / yes |
| DHCP | option82 / yes |
| DNS | Client / Yes |
| Software Reset Button | Yes |
| EEE (802.3az) | Yes |
| RMON Management | 32 entries / type |
| § | Discovery |
| IEEE 802.1AB Link Layer Discovery Protocol (LLDP) | Yes |
| ANSI/TIA-1057 LLDP Media Endpoint Discovery (LLDP-MED) | Yes |
| § | Diagnostics |
| Mirroring | Port-based (Many to One) / 4 sessions |
| Syslog (RFC3164) | Local RAM / Yes |
| Syslog (RFC3164) | Local Flash / Yes |
| Syslog (RFC3164) | Remote Server / 8 |
| System Diagnostics | CPU Utilization / Yes |
| System Diagnostics | Memory Utilization / Yes |
| System Diagnostics | Port Utilization / Yes |
| Port Diagnostics | Cable Test / Yes |
| Port Diagnostics | Fiber Module Status / Yes |
| Network Diagnostics | Ping Test / Yes |
| Network Diagnostics | Traceroute / Yes |
| UDLD | Yes |
| § | MIB |
| RFC1213 MIBII (System & Interface groups) | Yes |
| RFC2819 RMON I (1,2,3, & 9 groups) | Yes |
| RFC1215 Generic Traps | Yes |
| RFC1493 Bridge | Yes |
| RFC2674 Bridge MIB Extensions | Yes |
| RFC2737 Entity | Yes |
| RFC3635 Ethernet-Like | Yes |
| RFC2863 Interface Group | Yes |
| SNMP-Community-MIB | Yes |
| SNMPv3 | Yes |
| POE (S3508P/S3508PB) | POE port config / Yes |
| POE (S3508P/S3508PB) | POE timer / Yes |
| POE (S3508P/S3508PB) | Legacy PD detection / Yes |
| POE (S3508P/S3508PB) | max power management / Yes |
| POE (S3508P/S3508PB) | Priority management / Yes |
| RIP | v1/v2 / Yes |
| OSPF | v1/v2 / Yes |
| Web GUI language | Chinese / English / Yes |