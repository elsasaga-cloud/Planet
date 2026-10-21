# Software Specification（HOS 功能表，67 行）

> 首见于 <https://hohunet.com/product/s2624-4x-10gb-uplink-24-port-gigabit-managed-ethernet-switch/>（抓取 2026-10-21T04:14:17Z）；同一张表的型号在各产品页链接到此。列 EB / MS / MA = license 档（○ = 支持）。

| Basic function | Support hardware watchdog, factory reset, system and port LED |
|---|---|
| Basic function | Support global information, statistical information, log information |
| Basic function | Support User management, alarm management, configuration management |
| Basic function | Support Port rate, duplex, flow control, maximum frame length configuration |
| Basic function | Support Port mirroring, port speed limit, port energy saving |
| Layer 3 Interface | Support Layer 3 interface |
| Layer 3 Interface | Support IPv4, IPv6 address configuration |
| Layer 3 Interface | Support ARP configuration |
| Layer 3 Interface | Support ND configuration |
| Layer 3 Routing | Support IPv4 static routing |
| Layer 3 Routing | Support IPv6 static routing |
| Layer 3 Routing | Support RIP V1/V2 |
| Layer 3 Routing | Support OSPF |
| DHCP | Support DHCP server |
| DHCP | Support DHCP relay |
| DHCP | Support DHCP Snooping |
| VLAN | Support 4K VLAN |
| VLAN | Support 802.1Q VLAN，baesd on port VLAN |
| VLAN | SupportAccess、Trunk、Hybrid VLAN mode |
| VLAN | Support GVRP (VLAN registration protocol) |
| VLAN | Support MAC VLAN 、IP VLAN |
| VLAN | Support Voice VLAN |
| MAC Address | Support MAC address automatic learning and aging |
| MAC Address | Support Static, dynamic, filtered address table |
| Security features | Password protection |
| Security features | Support Restrict user access based on port number, IP address, MAC address |
| Security features | Support HTTPS、SSH V1/V2 |
| Security features | Support IP-MAC-PORT-VLAN binding |
| Security features | Support ARP detection, IP source protection, DoS protection |
| Security features | Support DHCP Snooping、DHCP Attack protection |
| Security features | Support 802.1X Certification |
| Security features | Support AAA (Authentication, Authorization, Accounting), Support RADIUS protocal, TACACS+ |
| Security features | Support Port security, port isolation |
| Access control | Support L2(Layer 2)～L4(Layer 4) Packet filtering function |
| Access control | Support Port mirroring, flow rate limiting, QoS remarking |
| QOS | Support 8 port queues |
| QOS | Support Port priority, 802.1P priority, DSCP priority |
| QOS | Support SP, WRR Priority scheduling algorithm |
| Spanning tree | Support STP(IEEE 802.1d), RSTP(IEEE 802.1w) and MSTP(IEEE 802.1s) protocal |
| Spanning tree | Support Multi-instance, Support Aggregate interface |
| Spanning tree | Support BPDU protection |
| Multicast | Support IGMP v1/v2/v3 Snooping |
| Multicast | Support MLD v1/v2 Snooping |
| Multicast | Support Layer 2 multicast fast leave mechanism, querier |
| Multicast | Support Layer 2 IPv4 static multicast |
| Multicast | Support Layer 2 IPv6 static multicast |
| Multicast | Support IGMP v1/v2/v3 Layer 3 multicast |
| Storm suppression | Support multicast suppression |
| Storm suppression | Support broadcast storm suppression |
| Storm suppression | Support unknown unicast suppression |
| Ring protection | Support Ring protection |
| Link Aggregation | Support Static Aggregation |
| Link Aggregation | Support LACP Dynamic Aggregation |
| Link Aggregation | Support based on IP, MAC, mixed load-balancing modes |
| Link Aggregation | Maximum support 32 aggregation groups (8 ports per aggregation group) |
| IPv6 | Support IPv6 Ping、IPv6 Traceroute、IPv6 Telnet |
| IPv6 | Support IPv6 SSH |
| IPv6 | Support IPv6 HTTP 、IPv6 HTTPS |
| Management and Maintenance | Support WEB Management (HTTP、HTTPS) |
| Management and Maintenance | Support CLI (Telnet, SSH V1/V2, Local serial port) |
| Management and Maintenance | Support SNMP V1/V2/V3 |
| Management and Maintenance | Support RMON V2 |
| Management and Maintenance | Support LLDP Device discovery |
| Management and Maintenance | Support SNTP Time synchronization |
| Management and Maintenance | Support CPU Monitoring, Memory Monitoring |
| Management and Maintenance | Support System log, classification warning |
| Management and Maintenance | Support Ping, Traceroute detection, cable detection |