# Software Specification（HOS 功能表，170 行）

> 首见于 <https://hohunet.com/product/s2648-6x-1g-10g/>（抓取 2026-10-21T04:14:16Z）；同一张表的型号在各产品页链接到此。列 EB / MS / MA = license 档（○ = 支持）。

| § | Feature List |
|---|---|
| Feature | Description / S2624-4X / S2648-6X |
| Type | Sub Type / Feature / Description / S2624-4X / S2648-6X |
| Ethernet basic features | Ethernet / Interface / Ethernet interface operating modes(full duplex, half duplex, and auto-negotiation) / ● / ● |
| Ethernet basic features | Ethernet / Interface / Ethernet interface operating rates / ● / ● |
| Ethernet basic features | Ethernet / Interface / Jumbo Frame / ● / ● |
| Ethernet basic features | Ethernet / Interface / Port enable/disable / ● / ● |
| Ethernet basic features | Ethernet / Flow-control / Flow-control tx/rx / ● / ● |
| Ethernet basic features | Ethernet / Storm-control / Port based storm-control / ● / ● |
| Ethernet basic features | Ethernet / Storm-control / Unknow-unicast/unknow-multicast/broadcast storm-control / ● / ● |
| Ethernet basic features | Ethernet / Port-isolate / Port-isolate / ● / ● |
| Ethernet basic features | Ethernet / Forward mode / Store-and-forward / ● / ● |
| Ethernet basic features | Ethernet / Forward mode / Cut-through / ● / ● |
| Ethernet basic features | VLAN / VLAN Access mode / Access/Trunk/Hybrid / ● / ● |
| Ethernet basic features | VLAN / VLAN Access mode / Default VLAN / ● / ● |
| Ethernet basic features | VLAN / VLAN Classification / VLAN Classification(port based/mac based/ip based/protocal based) / ● / ● |
| Ethernet basic features | VLAN / QinQ / Basic QinQ / ● / ● |
| Ethernet basic features | VLAN / QinQ / Flexible QinQ / ● / ● |
| Ethernet basic features | VLAN / QinQ / VLAN Swap / ● / ● |
| Ethernet basic features | MAC / MAC Address Table / Automatic learning and aging of MAC addresses / ● / ● |
| Ethernet basic features | MAC / MAC Address Table / Hardware Learning / ● / ● |
| Ethernet basic features | MAC / MAC Address Table / Static and dynamic MAC address entries / ● / ● |
| Ethernet basic features | MAC / MAC Address Table / blackhole MAC / ● / ● |
| Ethernet basic features | LAG / Link aggregation / Static-LAG & LACP / ● / ● |
| Ethernet basic features | LAG / Link aggregation / LAG load balance（SIP/DIP/SMAC/DMAC） / ● / ● |
| Ethernet Ring protection features | STP / STP / Spanning-Tree Protocol / ● / ● |
| Ethernet Ring protection features | STP / RSTP / Rapid Spanning-Tree Protocol / ● / ● |
| Ethernet Ring protection features | STP / MSTP / Multi-instance Spanning-Tree Protocol / ● / ● |
| Ethernet Ring protection features | STP / Spanning-Tree Protocol Protection / BPDU Filter/Guard / ● / ● |
| Ethernet Ring protection features | STP / Spanning-Tree Protocol Protection / Root Guard / ● / ● |
| Ethernet Ring protection features | STP / Spanning-Tree Protocol Protection / Loop Guard / ● / ● |
| Ethernet Ring protection features | ERPS / ERPS / Single Ring / ● / ● |
| Ethernet Ring protection features | ERPS / ERPS / Sub Ring / ● / ● |
| Ethernet Ring protection features | Loopback Detect / Loopback Detect / Loopback-detection / ● / ● |
| Layer2 Multicast | Layer2 Multicast / IGMP Snooping / IGMPv1/v2/v3 Snooping / ● / ● |
| Layer2 Multicast | Layer2 Multicast / IGMP Snooping / Fast leave / ● / ● |
| Layer2 Multicast | Layer2 Multicast / IGMP Snooping / Static IGMP snooping group / ● / ● |
| Layer2 Multicast | Layer2 Multicast / MVR / MVR（Multicast VLAN Registration） / ● / ● |
| IPv4 Forwarding | ARP / ARP / Static and dynamic ARP entries / ● / ● |
| IPv4 Forwarding | ARP / ARP / Aging of ARP entries / ● / ● |
| IPv4 Forwarding | ARP / ARP / Gratuitous ARP / ● / ● |
| IPv4 Forwarding | ARP / ARP proxy / basic ARP-Proxy / ● / ● |
| IPv4 Forwarding | ARP / ARP proxy / local ARP-Proxy / ● / ● |
| IPv4 Forwarding | IPv4 Unicast Routing / IPv4 Static Routes / IPv4 Static Routes / ● / ● |
| IPv4 Forwarding | IPv4 Unicast Routing / uRPF / uRPF check / ● / ● |
| IPv4 Forwarding | IPv4 Unicast Routing / RIP / RIPv1/v2 / ○ / ● |
| IPv4 Forwarding | IPv4 Unicast Routing / OSPFv2 / OSPFv2 / ○ / ● |
| IPv4 Forwarding | IPv4 Unicast Routing / IS-IS / IS-IS / ○ / ● |
| IPv4 Forwarding | IPv4 Unicast Routing / BGP / BGP / ● / ● |
| IPv4 Forwarding | IPv4 Unicast Routing / ICMP / ICMP redirect / ● / ● |
| IPv4 Forwarding | IPv4 Unicast Routing / ICMP / ICMP unreachables / ● / ● |
| IPv4 Forwarding | IPv4 Unicast Routing / ECMP / ECMP / ● / ● |
| IPv4 Forwarding | IPv4 Multicast Routing / IGMP / IGMPv1/v2/v3 / ● / ● |
| IPv4 Forwarding | IPv4 Multicast Routing / IGMP / IGMP-Proxy / ● / ● |
| IPv4 Forwarding | IPv4 Multicast Routing / IGMP / IGMP SSM Mapping / ● / ● |
| IPv4 Forwarding | IPv4 Multicast Routing / PIM / PIM-SM / ● / ● |
| IPv4 Forwarding | IPv4 Multicast Routing / PIM / PIM-SSM / ● / ● |
| IPv4 Forwarding | IPv4 Multicast Routing / PIM / PIM-DM / ● / ● |
| IPv6 Forwarding | IPv6 Basic Protocol / ICMPv6 / ICMPv6 / ● / ● |
| IPv6 Forwarding | IPv6 Basic Protocol / NDP / NDP / ● / ● |
| IPv6 Forwarding | IPv6 Basic Protocol / PMTU / PMTU / ● / ● |
| IPv6 Forwarding | IPv6 Unicast Routing / IPv6 Static Routes / IPv6 Static Routes / ● / ● |
| IPv6 Forwarding | IPv6 Unicast Routing / RIPng / RIPng / ● / ● |
| IPv6 Forwarding | IPv6 Unicast Routing / BGP4+ / BGP4+ / ● / ● |
| IPv6 Forwarding | IPv6 Unicast Routing / OSPFv3 / OSPFv3 / ● / ● |
| IPv6 Forwarding | IPv6 Unicast Routing / IS-IS / IS-IS / ● / ● |
| IPv6 Forwarding | IPv6 Multicast Routing / MLD v1/v2 / MLD v1/v2 / ● / ● |
| IPv6 Forwarding | IPv6 Multicast Routing / MLD v1/v2 Snooping / MLD v1/v2 Snooping / ● / ● |
| Reliability | BFD / BFD / BFD for OSPFv2 / ● / ● |
| Reliability | VRRP / VRRP / VRRP / ● / ● |
| Reliability | VRRP / VRRP / Track for VRRP / ● / ● |
| Reliability | Smart Link / FlexLink / FlexLink / ● / ● |
| Reliability | Smart Link / Monitorlink / Monitorlink / ● / ● |
| ethernet OAM | EFM / EFM (802.3ah) / Auto detection / ● / ● |
| ethernet OAM | EFM / EFM (802.3ah) / Network fault detetion / ● / ● |
| ethernet OAM | EFM / EFM (802.3ah) / Network fault handle / ● / ● |
| ethernet OAM | EFM / EFM (802.3ah) / remote loopback / ● / ● |
| ethernet OAM | CFM / CFM (802.1ag) / Hardware CCM detect / ● / ● |
| ethernet OAM | CFM / CFM (802.1ag) / MAC Ping / ● / ● |
| ethernet OAM | CFM / CFM (802.1ag) / MAC Trace / ● / ● |
| ethernet OAM | Y.1731 / Y.1731 / Latency and jitter measure / ● / ● |
| QoS features | QoS / Traffic classification / Traffic classification based on COS/DSCP (simple classification) / ● / ● |
| QoS features | QoS / Traffic classification / Traffic classification based on ACL ( complex classification) / ● / ● |
| QoS features | QoS / Traffic classification / Traffic classification based on inner header of the tunnel packets / ● / ● |
| QoS features | QoS / Traffic behaviors / Queue scheduling / ● / ● |
| QoS features | QoS / Traffic behaviors / Remark the priority fields(COS/DSCP) of the packet based on ACL / ● / ● |
| QoS features | QoS / Traffic behaviors / Flow redirection / ● / ● |
| QoS features | QoS / Traffic behaviors / Flow mirror / ● / ● |
| QoS features | QoS / Traffic policing / Traffic policing based on direction(in/out) of Port / ● / ● |
| QoS features | QoS / Traffic policing / Traffic policing based on direction(in/out) of VLAN / ● / ● |
| QoS features | QoS / Traffic policing / Traffic policing based on direction(in/out) of flow / ● / ● |
| QoS features | QoS / Traffic policing / Traffic policing based on direction(in/out) of aggregated flow / ● / ● |
| QoS features | QoS / Traffic shaping / Queue based traffic shaping / ● / ● |
| QoS features | QoS / Traffic shaping / Port based traffic shaping / ● / ● |
| QoS features | QoS / Congestion management / SP（Strict Priority）scheduling / ● / ● |
| QoS features | QoS / Congestion management / WRR（Weighted Round Robin）scheduling / ● / ● |
| QoS features | QoS / Congestion management / SP + WRR mixed scheduling / ● / ● |
| QoS features | QoS / Traffic statistics / Packet counts and bytes statistics based on traffic classification / ● / ● |
| QoS features | QoS / Traffic statistics / Packet counts and bytes statistics based on the color after traffic policing / ● / ● |
| QoS features | QoS / Traffic statistics / Forwarded and discarded packet counts and bytes statistics / ● / ● |
| Security and management | System Security / SSH / SSHv1/v2 / ● / ● |
| Security and management | System Security / RADIUS / RADIUS / ● / ● |
| Security and management | System Security / TACACS+ / TACACS+ / ● / ● |
| Security and management | System Security / AAA / Authentication / ● / ● |
| Security and management | System Security / AAA / Accounting / ● / ● |
| Security and management | System Security / Dot1x / Port based dot1x / ● / ● |
| Security and management | System Security / Dot1x / MAC based dot1x / ● / ● |
| Security and management | System Security / ACL / MAC/IP ACL / ● / ● |
| Security and management | System Security / ACL / Basic Mode ACL / ● / ● |
| Security and management | System Security / ACL / Port/VLAN/L4-Port ACL / ● / ● |
| Security and management | System Security / ACL / Time Range / ● / ● |
| Security and management | System Security / ARP Inspection / ARP Inspection / ● / ● |
| Security and management | System Security / IP Source Guard / IP Source Guard / ● / ● |
| Security and management | System Security / Port Security / Limitation on MAC address learning on interface / ● / ● |
| Security and management | System Security / VLAN Security / Limitation on MAC address learning on VLAN / ● / ● |
| Security and management | System Security / Rate limit / Rate limit / ● / ● |
| Security and management | System Security / CPU Traffic Limit / CPU Traffic Limit / ● / ● |
| Security and management | System Security / Prevent DDOS attack / Prevent DDOS attack (ICMP Flood/Smurf/Fraggle/LAND/SYN Flood) / ● / ● |
| Security and management | System Security / Login filter / CLI/WEB/SNMP/Telnet/SSH filtering / ● / ● |
| Security and management | Network Management / DHCP / DHCP Server / ● / ● |
| Security and management | Network Management / DHCP / DHCP Relay / ● / ● |
| Security and management | Network Management / DHCP / DHCP Snooping / ● / ● |
| Security and management | Network Management / DHCP / DHCP Option60 / ● / ● |
| Security and management | Network Management / DHCP / DHCP Option82 / ● / ● |
| Security and management | Network Management / RMON / RMON / ● / ● |
| Security and management | Network Management / sFlow / RFC3176 sFlow / ● / ● |
| Security and management | Network Management / SNTP / SNTP（Simple Network Time Protocol） / ● / ● |
| Security and management | Network Management / LLDP / LLDP / ● / ● |
| Configuration and maintenance | Terminal Services / Command Line Interface / Configurations through CLI (Command Line Interface) / ● / ● |
| Configuration and maintenance | Terminal Services / Help information / Help information in English / ● / ● |
| Configuration and maintenance | Terminal Services / Terminal service / Vty Terminal service / ● / ● |
| Configuration and maintenance | Terminal Services / Terminal service / Console Terminal service / ● / ● |
| Configuration and maintenance | Configuration Management / Management interface / Inband management interface and configuration / ● / ● |
| Configuration and maintenance | Configuration Management / Management interface / Outband management interface and configuration / ● / ● |
| Configuration and maintenance | Configuration Management / User privilege management / privileged user proirity and privileged commands / ● / ● |
| Configuration and maintenance | Configuration Management / SNMP / Network management based on SNMPv1/v2c/v3 / ● / ● |
| Configuration and maintenance | Configuration Management / SNMP / Public and private MIB / ● / ● |
| Configuration and maintenance | Configuration Management / SNMP / Public and private Trap / ● / ● |
| Configuration and maintenance | Configuration Management / WEB / Configuration and management based on WEB UI / ● / ● |
| Configuration and maintenance | Configuration Management / Restore factory default configuration / Restore factory default configuration / ● / ● |
| Configuration and maintenance | File System / File system / File system / ● / ● |
| Configuration and maintenance | File System / Upload and download / Upload and download files through FTP or TFTP / ● / ● |
| Configuration and maintenance | File System / Upload and download / Upload and download files through Xmodem / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Debug / per-module Debug features / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Debug / ICMP Debug / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Log & Alarm / CPU usage display and alarm / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Log & Alarm / Memory usage display and alarm / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Log & Alarm / Device temperature、PSU、FAN、status display and alarm / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Log & Alarm / User operation logs / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Log & Alarm / Management of logs, alarms, and debugging information / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / VCT / VCT（Virtual Cable Test） / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / system diagnostics / Detailed Diagnostic-information collection / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Reboot / Manual reboot / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Reboot / Schedule Reboot / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Reboot / Reboot Information logging / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Network diagnostics / Ping / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Network diagnostics / IPv6 Ping / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Network diagnostics / Traceroute / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Mirror / Port mirror / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Mirror / Flow mirror / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Mirror / Remote mirror / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Mirror / Multi-destination mirror（m:n） / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / CPU statistics / To CPU/From CPU packets statistics / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Loopback / port loopback / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / Loopback / hardware loopback（internal/external） / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / System time / Time configuration / ● / ● |
| Configuration and maintenance | Debugging And Maintenance / System time / Timezone / ● / ● |
| Configuration and maintenance | Version Upgrade / System soft ware upgrade / upgrade with the local image file / ● / ● |
| Configuration and maintenance | Version Upgrade / System soft ware upgrade / upgrade with the remote TFTP server / ● / ● |
| Configuration and maintenance | Version Upgrade / Uboot upgrade / Online upgrade Uboot / ● / ● |