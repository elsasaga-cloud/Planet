# Software Specification（HOS 功能表，289 行）

> 首见于 <https://hohunet.com/product/s3708-2g-si-8port-poe-gigabit-ethernet-l3-switchwith-81g-base-tpoe30w210g-sfpdual-fixed-power-modulessingle-fixed-fan-module/>（抓取 2026-10-21T04:12:38Z）；同一张表的型号在各产品页链接到此。列 EB / MS / MA = license 档（○ = 支持）。

| Type | Sub Type | Feature | Description | EB | MS | MA | REMARK |
|---|---|---|---|---|---|---|---|
| Ethernet basic features | Ethernet | interface | Ethernet interface operating modes(full duplex, half duplex, and auto-negotiation) | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | interface | Ethernet interface operating rates | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | interface | Jumbo Frame | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | interface | port-xconnect | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | Flow-control | Flow-control tx/rx | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | storm-control | Port based storm-control | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | storm-control | VLAN based storm-control | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | Port-block | Port-block(know/unknown unicast; know/unknown multicast/broadcast) | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | Port-isolate | L2/L3/All Port-isolate | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | Port-isolate | Uni-direction isolate | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | L2 Protocol Tunnel | L2 Protocol Tunnel(support CFM/DOT1X/SLOW-PROTO/STP | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | Forward mode | Store-and-forward | ◯ | ◯ | ◯ |  |
| Ethernet basic features | Ethernet | Forward mode | Cut-through | ◯ | ◯ | ◯ | Not available on E361 platform |
| Ethernet basic features | VLAN | VLAN Access mode | Access/Trunk | ◯ | ◯ | ◯ |  |
| Ethernet basic features | VLAN | VLAN Access mode | Default VLAN | ◯ | ◯ | ◯ |  |
| Ethernet basic features | VLAN | VLAN Classification | VLAN Classification(port based/mac based/IP based/protocol based) | ◯ | ◯ | ◯ |  |
| Ethernet basic features | VLAN | QinQ | Basic QinQ | ◯ | ◯ | ◯ |  |
| Ethernet basic features | VLAN | QinQ | Selective QinQ | ◯ | ◯ | ◯ |  |
| Ethernet basic features | VLAN | QinQ | VLAN Mapping(1:1 VLAN Translation) | ◯ | ◯ | ◯ |  |
| Ethernet basic features | VLAN | VLAN Statistics | VLAN Statistics | ◯ | ◯ | ◯ |  |
| Ethernet basic features | VLAN | Private VLAN | Private VLAN | ◯ | ◯ | ◯ |  |
| Ethernet basic features | VLAN | Voice VLAN | Voice VLAN | ◯ | ◯ | ◯ |  |
| Ethernet basic features | VLAN | Guest VLAN | Guest VLAN | ◯ | ◯ | ◯ |  |
| Ethernet basic features | VLAN | GVRP | GVRP | ◯ | ◯ | ◯ |  |
| Ethernet basic features | MAC | MAC Address Table | Automatic learning and aging of MAC addresses | ◯ | ◯ | ◯ |  |
| Ethernet basic features | MAC | MAC Address Table | Hardware Learning | ◯ | ◯ | ◯ |  |
| Ethernet basic features | MAC | MAC Address Table | Static and dynamic MAC address entries | ◯ | ◯ | ◯ |  |
| Ethernet basic features | MAC | MAC Address Table | Blackhole MAC | ◯ | ◯ | ◯ |  |
| Ethernet basic features | MAC | MAC Flapping detect | MAC Flapping detect | ◯ | ◯ | ◯ |  |
| Ethernet basic features | MAC | Port Bridge | Port Bridge | ◯ | ◯ | ◯ |  |
| Ethernet basic features | LAG | Link aggregation | Static-LAG & LACP | ◯ | ◯ | ◯ |  |
| Ethernet basic features | LAG | Link aggregation | LAG load balance(SLB) | ◯ | ◯ | ◯ |  |
| Ethernet basic features | LAG | Link aggregation | LAG load balance(DLB) | ◯ | ◯ | ◯ | Not available on E361 platform |
| Ethernet basic features | LAG | Link aggregation | LAG load balance(RR) | ◯ | ◯ | ◯ |  |
| Ethernet basic features | LAG | Link aggregation | LAG Self-healing | ◯ | ◯ | ◯ |  |
| Ethernet basic features | LAG | Link aggregation | Link aggregation weighting | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | xSTP | STP | Spanning-Tree Protocol | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | xSTP | RSTP | Rapid Spanning-Tree Protocol | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | xSTP | MSTP | Multi-instance Spanning-Tree Protocol | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | xSTP | Spanning-Tree Protocol Protection | BPDU Filter/Guard | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | xSTP | Spanning-Tree Protocol Protection | Root Guard | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | xSTP | Spanning-Tree Protocol Protection | Loop Guard | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | xSTP | Spanning-Tree Protocol Protection | Anti TC-BPDU attack | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | ERPS | ERPS | Single ERPS ring | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | ERPS | ERPS | tangent ERPS rings | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | ERPS | ERPS | intersecting ERPS rings | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | ERPS | ERPS | compatible with RRPP | ◯ | ◯ | ◯ |  |
| Ethernet Ring protection features | Loop back Detect | Loop back Detect | Loop back detection | ◯ | ◯ | ◯ |  |
| Layer2 Multicast | Layer2 Multicast | IGMP Snooping | IGMPv1/v2/v3 Snooping | ◯ | ◯ | ◯ |  |
| Layer2 Multicast | Layer2 Multicast | IGMP Snooping | Fast leave | ◯ | ◯ | ◯ |  |
| Layer2 Multicast | Layer2 Multicast | IGMP Snooping | Static IGMP snooping group | ◯ | ◯ | ◯ |  |
| Layer2 Multicast | Layer2 Multicast | MVR | MVR(Multicast VLAN Registration) | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | ARP | ARP | Static and dynamic ARP entries | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | ARP | ARP | Aging of ARP entries | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | ARP | ARP | Gratuitous ARP | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | ARP | ARP proxy | basic ARP-Proxy | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | ARP | ARP proxy | local ARP-Proxy | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | IPv4 Static Routes | IPv4 Static Routes | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | IPv4 Static Routes | Black hole Routes | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | IPv4 Static Routes | co-work with IP SLA | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | IPv4 Static Routes | VRF(Virtual Routing and Forwarding) | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | IPv4 Static Routes | uRPF check | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | RIP | RIPv1/v2 | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | OSPFv2 | OSPFv2 | X | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | IS-IS | IS-IS | X | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | BGP | IBGP | X | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | BGP | EBGP | X | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | Route policy | Route-map | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | Route policy | IPv4 prefix-list | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | PBR | PBR(Policy-based Routing) | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | ICMP | ICMP redirect | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | ICMP | ICMP unreachable | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | ECMP | ECMP(SLB) | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | ECMP | ECMP(DLB) | ◯ | ◯ | ◯ | Not available on E361 platform |
| IPv4 Forwarding | IPv4 Unicast Routing | ECMP | ECMP(RR) | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Unicast Routing | ECMP | ECMP Self-healing | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Multicast Routing | IGMP | IGMPv1/v2/v3 | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Multicast Routing | IGMP | IGMP-Proxy | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Multicast Routing | IGMP | IGMP SSM Mapping | ◯ | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Multicast Routing | PIM | PIM-SM | X | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Multicast Routing | PIM | PIM-SSM | X | ◯ | ◯ |  |
| IPv4 Forwarding | IPv4 Multicast Routing | PIM | PIM-DM | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Basic Protocol | ICMPv6 | ICMPv6 | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Basic Protocol | NDP | NDP | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Unicast Routing | IPv6 Static Routes | IPv6 Static Routes | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Unicast Routing | RIPng | RIPng | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Unicast Routing | OSPFv3 | OSPFv3 | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Unicast Routing | IS-IS | IS-IS | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Unicast Routing | BGP4+ | BGP4+ | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Multicast Routing | MLD v1/v2 | MLD v1/v2 | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Multicast Routing | MLD v1/v2 Snooping | MLD v1/v2 Snooping | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Multicast Routing | MVR6 | MVR6 | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Multicast Routing | PIM-SM v6 | PIM-SM v6 | X | ◯ | ◯ |  |
| IPv6 Forwarding | IP Tunnel | IPv6 over IPv4 Tunnel | IPv6 over IPv4 Tunnel | X | ◯ | ◯ |  |
| IPv6 Forwarding | IP Tunnel | 6to4 Tunnel | 6to4 Tunnel | X | ◯ | ◯ |  |
| IPv6 Forwarding | IP Tunnel | ISATAP Tunnel | ISATAP Tunnel | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Service | DHCPv6 | DHCPv6 Server | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Service | DHCPv6 | DHCPv6 Relay | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Service | DHCPv6 | DHCPv6 Snooping | X | ◯ | ◯ |  |
| IPv6 Forwarding | IPv6 Service | IPv6 Prefix List | IPv6 Prefix-list | X | ◯ | ◯ |  |
| Device reliability features | BFD | BFD | BFD for Static route | X | ◯ | ◯ |  |
| Device reliability features | BFD | BFD | BFD for OSPFv2 | X | ◯ | ◯ |  |
| Device reliability features | BFD | BFD | BFD for VRRP/Track | X | ◯ | ◯ |  |
| Device reliability features | BFD | BFD | BFD for PBR | X | ◯ | ◯ |  |
| Device reliability features | VRRP | VRRP | VRRP | ◯ | ◯ | ◯ |  |
| Device reliability features | VRRP | VRRP | Track for VRRP | ◯ | ◯ | ◯ |  |
| Device reliability features | Smart Link | Smart Link | multi-instance | ◯ | ◯ | ◯ |  |
| Device reliability features | Smart Link | Smart Link | load balance | ◯ | ◯ | ◯ |  |
| Device reliability features | Smart Link | Smart Link | Multi-Link | ◯ | ◯ | ◯ |  |
| Device reliability features | Smart Link | Smart Link | Monitor-link | ◯ | ◯ | ◯ |  |
| Device reliability features | MLAG | MLAG | MLAG basic | ◯ | ◯ | ◯ |  |
| Device reliability features | MLAG | MLAG | MLAG orphan Port | ◯ | ◯ | ◯ |  |
| Device reliability features | Stacking | Stacking | Maximum number of stacked devices: 8 Stack port: Any port or AGG | ◯ | ◯ | ◯ | Requires a special licence |
| ethernet OAM | EFM | EFM (802.3ah) | Auto detection | X | ◯ | ◯ |  |
| ethernet OAM | EFM | EFM (802.3ah) | Network fault detection | X | ◯ | ◯ |  |
| ethernet OAM | EFM | EFM (802.3ah) | Network fault handle | X | ◯ | ◯ |  |
| ethernet OAM | EFM | EFM (802.3ah) | remote loop back | X | ◯ | ◯ |  |
| ethernet OAM | CFM | CFM (802.1ag) | Hardware CCM detect | X | ◯ | ◯ |  |
| ethernet OAM | CFM | CFM (802.1ag) | MAC Ping | X | ◯ | ◯ |  |
| ethernet OAM | CFM | CFM (802.1ag) | MAC Trace | X | ◯ | ◯ |  |
| ethernet OAM | Y.1731 | Y.1731 | Loss measure(LM) | X | ◯ | ◯ | Not available on E670、E780 platform |
| ethernet OAM | Y.1731 | Y.1731 | Latency and Jitter measure(DM) | X | ◯ | ◯ |  |
| PoE features | PoE | System Power management | Power supply on-spot detection | ◯ | ◯ | ◯ |  |
| PoE features | PoE | System Power management | Power supply capability detection | ◯ | ◯ | ◯ |  |
| PoE features | PoE | System Power management | Power capability auto configuration (PSE) | ◯ | ◯ | ◯ |  |
| PoE features | PoE | Power Supply Management | Legacy PD detection | ◯ | ◯ | ◯ |  |
| PoE features | PoE | Power Supply Management | PD max power management | ◯ | ◯ | ◯ |  |
| PoE features | PoE | Power Supply Management | PD priority management | ◯ | ◯ | ◯ |  |
| PoE features | PoE | Power Supply Management | Power Supply Task Plan management(Not ready) | ◯ | ◯ | ◯ |  |
| PoE features | PoE | Power Supply Management | PD Mandatory power supply | ◯ | ◯ | ◯ |  |
| PoE features | PoE | operations management | PSE log | ◯ | ◯ | ◯ |  |
| PoE features | PoE | operations management | PSE Chipset temperature inquire | ◯ | ◯ | ◯ |  |
| PoE features | PoE | operations management | PSE firmware update | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic classification | Traffic classification based on COS/DSCP (simple classification) | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic classification | Traffic classification based on ACL ( complex classification) | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic classification | Traffic classification based on inner header of the tunnel packets | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic behaviors | Queue scheduling | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic behaviors | Remark the priority fields(COS/DSCP) of the packet based on ACL | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic behaviors | Remark the priority fields(COS/DSCP) of the packet based on Table Map | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic behaviors | Flow redirection | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic behaviors | Flow mirror | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic policing | Traffic policing based on direction(in/out) of Port | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic policing | Traffic policing based on direction(in/out) of VLAN | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic policing | Traffic policing based on direction(in/out) of flow | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic policing | Traffic policing based on direction(in/out) of aggregated flow | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic shaping | Queue based traffic shaping | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic shaping | Port based traffic shaping | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Congestion management | SP(Strict Priority)scheduling | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Congestion management | WDRR(Weighted Deficit Round Robin)scheduling | ◯ | ◯ | ◯ | Not currently supported on E780 platform |
| QoS features | QoS | Congestion management | SP + WDRR mixed scheduling | ◯ | ◯ | ◯ | Not available on E780 platform |
| QoS features | QoS | Congestion avoidance | TD(Tail Drop) | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Congestion avoidance | WRED(Weighted Random Early Detection) | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic statistics | Packet counts and bytes statistics based on traffic classification | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic statistics | Packet counts and bytes statistics based on the color after traffic policing | ◯ | ◯ | ◯ |  |
| QoS features | QoS | Traffic statistics | Forwarded and discarded packet counts and bytes statistics | ◯ | ◯ | ◯ |  |
| QoS features | QoS | ECN (Explicit congestion | ECN tags based on Tail Drop | X | ◯ | ◯ | Not available on E780 platform |
| QoS features | QoS | ECN (Explicit congestion | ECN tags based on WRED | X | ◯ | ◯ |  |
| Data Center | VARP | Virtual gateway | VARP(Virtual-ARP) | ◯ | ◯ | ◯ |  |
| Data Center | VARP | Virtual gateway | VARP subnet | ◯ | ◯ | ◯ |  |
| Data Center | Tunnel | VxLAN | Manual configure VxLAN tunnel | X | ◯ | ◯ |  |
| Data Center | Tunnel | VxLAN | VxLAN distributed gateway | X | ◯ | ◯ |  |
| Data Center | Tunnel | VxLAN | VxLAN active-active access | X | ◯ | ◯ |  |
| Data Center | Tunnel | VxLAN | Interconnect across Data Centers based on VxLAN | X | ◯ | ◯ |  |
| Data Center | Tunnel | VxLAN | Edit DSCP in VxLan outer header | X | ◯ | ◯ |  |
| Data Center | Tunnel | VxLAN | BGP EVPN | X | ◯ | ◯ |  |
| Data Center | Tunnel | VxLAN | Support to enable/disable overlay split horizon per-VNI | X | ◯ | ◯ |  |
| Data Center | Tunnel | GRE Tunnel | GRE Tunnel | X | ◯ | ◯ |  |
| Data Center | Tunnel | NVGRE Tunnel | NVGRE Tunnel | X | ◯ | ◯ |  |
| Data Center | Tunnel | GENEVE Tunnel | GENEVE Tunnel | X | ◯ | ◯ |  |
| Data Center | DCB | DCBX | LLDP support DCBX TLV | X | ◯ | ◯ |  |
| Data Center | DCB | PFC | PFC | X | ◯ | ◯ |  |
| Metro Feature | MPLS | LDP | LDP | X | X | ◯ |  |
| Metro Feature | MPLS | MPLS Forwarding | MPLS Forwarding | X | X | ◯ |  |
| Metro Feature | MPLS | VPWS | VPWS (L2VPN) | X | X | ◯ |  |
| Metro Feature | MPLS | VPLS | VPLS (L2VPN) | X | X | ◯ |  |
| Metro Feature | MPLS | L3VPN | L3VPN | X | X | ◯ |  |
| Metro Feature | MPLS | MPLS OAM | MPLS OAM | X | X | ◯ |  |
| Metro Feature | MPLS | MPLS Stats | MPLS Stats | X | X | ◯ |  |
| Metro Feature | MPLS | ACL | ACL | X | X | ◯ |  |
| Metro Feature | MPLS | Qos | Qos | X | X | ◯ |  |
| Security and management | System Security | SSH | SSHv1/v2 | ◯ | ◯ | ◯ |  |
| Security and management | System Security | SSH | RSA Key generation | ◯ | ◯ | ◯ |  |
| Security and management | System Security | RADIUS | RADIUS | ◯ | ◯ | ◯ |  |
| Security and management | System Security | TACAS+ | TACAS+ | ◯ | ◯ | ◯ |  |
| Security and management | System Security | AAA | Authentication | ◯ | ◯ | ◯ |  |
| Security and management | System Security | AAA | Authorization | ◯ | ◯ | ◯ |  |
| Security and management | System Security | AAA | Accounting | ◯ | ◯ | ◯ |  |
| Security and management | System Security | Dot1x | Port based dot1x | ◯ | ◯ | ◯ |  |
| Security and management | System Security | Dot1x | MAC based dot1x | ◯ | ◯ | ◯ |  |
| Security and management | System Security | Dot1x | Guest VLAN | ◯ | ◯ | ◯ |  |
| Security and management | System Security | ACL | MAC/IP ACL | ◯ | ◯ | ◯ |  |
| Security and management | System Security | ACL | Basic Mode ACL | ◯ | ◯ | ◯ |  |
| Security and management | System Security | ACL | Port-group ACL | ◯ | ◯ | ◯ |  |
| Security and management | System Security | ACL | VLAN-group ACL | ◯ | ◯ | ◯ |  |
| Security and management | System Security | ACL | IPv6 ACL | ◯ | ◯ | ◯ |  |
| Security and management | System Security | ACL | ACL UDF | ◯ | ◯ | ◯ |  |
| Security and management | System Security | ACL | Time Range | ◯ | ◯ | ◯ |  |
| Security and management | System Security | ARP Inspection | ARP Inspection | ◯ | ◯ | ◯ |  |
| Security and management | System Security | IP Source Guard | IP Source Guard | ◯ | ◯ | ◯ |  |
| Security and management | System Security | Port Security | Limitation on MAC address learning on interface | ◯ | ◯ | ◯ |  |
| Security and management | System Security | VLAN Security | Limitation on MAC address learning on VLAN | ◯ | ◯ | ◯ |  |
| Security and management | System Security | Control Plane Policy (COPP) | Black list/wihte list | ◯ | ◯ | ◯ |  |
| Security and management | System Security | Control Plane Policy (COPP) | Rate limit | ◯ | ◯ | ◯ |  |
| Security and management | System Security | CPU Traffic Limit | CPU Traffic Limit | ◯ | ◯ | ◯ |  |
| Security and management | System Security | Prevent DDOS attack | Prevent DDOS attack (ICMP Flood/Smurf/Fraggle/LAND/SYN Flood) | ◯ | ◯ | ◯ |  |
| Security and management | System Security | Login filter | Telnet/SSH ACL filtering | ◯ | ◯ | ◯ |  |
| Security and management | System Security | Login filter | Telnet/SSH IPv6 ACL filtering | ◯ | ◯ | ◯ |  |
| Security and management | System Security | MAC Security | MacSec(802.1AE) | ◯ | ◯ | ◯ | Not available on E670 platform |
| Security and management | System Security | Link-Flapping detection | Link-Flapping detection | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | DHCP | DHCP Server | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | DHCP | DHCP Relay | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | DHCP | DHCP Snooping | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | DHCP | DHCP Client | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | DHCP | DHCP Option82 | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | DHCP | DHCP Option252 | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | RMON | RMON | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | sFlow | sFlow v4/v5 | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | IP SLA | IP SLA | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | IPFIX | IPFIX | X | ◯ | ◯ |  |
| Security and management | Network Management | EFD | Elephant Flow Detection | ◯ | ◯ | ◯ | Not available on E670 platform |
| Security and management | Network Management | NTP | NTP(Network Time Protocol) | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | PTP（IEEE 1588） | TC（Support P2P/E2E、Ethernet/Udp Transport） | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | PTP（IEEE 1588） | BC/OC(Support OneStep/TwoStep、Request-response/Peer-delay Ethernet/Udp Transport) | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | Err-disable | Err-disable detection and recovery | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | DNS | Static DNS Client | ◯ | ◯ | ◯ |  |
| Security and management | Network Management | LLDP | LLDP |  |  |  |  |
| Security and management | Network Management | Dying-Gasp | Support syslog/snmp-trap/eth-oam warning | ◯ | ◯ | ◯ | Only E361 platform support |
| Security and management | Terminal Services | Command Line Interface | Configurations through CLI (Command Line Interface) | ◯ | ◯ | ◯ |  |
| Security and management | Terminal Services | Help information | Banner configuration | ◯ | ◯ | ◯ |  |
| Security and management | Terminal Services | Help information | Help information in English | ◯ | ◯ | ◯ |  |
| Security and management | Terminal Services | Terminal service | Vty Terminal service | ◯ | ◯ | ◯ |  |
| Security and management | Terminal Services | Terminal service | Console Terminal service | ◯ | ◯ | ◯ |  |
| Security and management | Terminal Services | Management interface | In-band management interface and configuration | ◯ | ◯ | ◯ |  |
| Security and management | Terminal Services | Management interface | Out-band management interface and configuration | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Configuration Management | SNMP | Network management based on SNMPv1/v2c/v3 | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Configuration Management | SNMP | Public and private MIB | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Configuration Management | SNMP | Public and private Trap | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Configuration Management | WEB | Configuration and management based on WEB UI | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Configuration Management | Cloud Management | Automatic device connection management | ◯ | ◯ | ◯ | Needs to be used with the DHCS Cloud Management system. DHCS can be deployed on public clouds or in a private environment. |
| Configuration and maintenance | Configuration Management | Cloud Management | DHDP（Dahu Discovery Protocol） | ◯ | ◯ | ◯ | Needs to be used with the DHCS Cloud Management system. DHCS can be deployed on public clouds or in a private environment. |
| Configuration and maintenance | Configuration Management | Cloud Management | Zero-configuration deployment | ◯ | ◯ | ◯ | Needs to be used with the DHCS Cloud Management system. DHCS can be deployed on public clouds or in a private environment. |
| Configuration and maintenance | Configuration Management | Cloud Management | Automatic network topology | ◯ | ◯ | ◯ | Needs to be used with the DHCS Cloud Management system. DHCS can be deployed on public clouds or in a private environment. |
| Configuration and maintenance | Configuration Management | Cloud Management | Network monitoring and alarm notification | ◯ | ◯ | ◯ | Needs to be used with the DHCS Cloud Management system. DHCS can be deployed on public clouds or in a private environment. |
| Configuration and maintenance | Configuration Management | Cloud Management | Configuration and one-click rollback | ◯ | ◯ | ◯ | Needs to be used with the DHCS Cloud Management system. DHCS can be deployed on public clouds or in a private environment. |
| Configuration and maintenance | Configuration Management | Cloud Management | Cross-network tunneling connection to network device(web/ssh/telnet) | ◯ | ◯ | ◯ | Needs to be used with the DHCS Cloud Management system. DHCS can be deployed on public clouds or in a private environment. |
| Configuration and maintenance | Configuration Management | Cloud Management | Scheduled tasks deployment | ◯ | ◯ | ◯ | Needs to be used with the DHCS Cloud Management system. DHCS can be deployed on public clouds or in a private environment. |
| Configuration and maintenance | Configuration Management | NETCONF | Configuration and management based on NETCONF | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Configuration Management | RPC-API | Configuration and management based on RPC-API | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Configuration Management | Smart Config | Smart Config(Automatically configuration when system start) | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Configuration Management | system profile configuration | change the system specifications by choose different STM Profiles | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Configuration Management | Restore factory default configuration | Restore factory default configuration | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | File System | File system | File system(support directory and file management) | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | File System | Upload and download | Upload and download files through FTP or TFTP | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | File System | Upload and download | Upload and download files through Xmodem | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Debug | per-module Debug features | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Debug | ICMP Debug | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | BHM | Software process monitor: BHM(Beat Heart Monitor) | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | BHM | Hardware Watch Dog | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Log & alarm | CPU usage display and alarm | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Log & alarm | Memory usage display and alarm | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Log & alarm | Device temperature, PSU, FAN, status display and alarm | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Log & alarm | User operation logs | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Log & alarm | Management of logs, alarms, and debugging information | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | VCT | VCT(Virtual Cable Test) | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | system diagnostics | Detailed Diagnostic-information collection | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Reboot | Manual reboot | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Reboot | Schedule Reboot | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Reboot | Reboot Information logging | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | network diagnostics | Ping | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | network diagnostics | IPv6 Ping | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | network diagnostics | Trace route | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | mirror | Port mirror | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | mirror | Flow mirror | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | mirror | Remote mirror | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | mirror | Multi-destination mirror(m:n) | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | mirror | Use CPU as mirror source | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | mirror | Use CPU as mirror destination and analyze packet | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | mirror | ERSPAN | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | CPU statistics | To CPU/From CPU packets statistics | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | L2 Ping | layer2 network connectivity detection – L2Ping (MAC Ping/Trace) | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | UDLD | UDLD(Unidirectional Link Detection) | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | unidirectional | unidirectional forwarding of the fiber | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Loop back | port loop back | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | Loop back | hardware loop back(internal/external) | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | System time | Time configuration | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Debugging And Maintenance | System time | Timezone | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | Software | System software upgrate | Update via TFTP | ◯ | ◯ | ◯ |  |
| Configuration and maintenance | upgrate | Uboot upgrate | Uboot upgrate | ◯ | ◯ | ◯ |  |