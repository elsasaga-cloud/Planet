# Software Specification（HOS 功能表，70 行）

> 首见于 <https://hohunet.com/product/s2648p-4x-10g-uplink-48-ports-gigabit-l3-management-ethernet-poe-switch/>（抓取 2026-10-21T04:14:21Z）；同一张表的型号在各产品页链接到此。列 EB / MS / MA = license 档（○ = 支持）。

| Basic Function | Support hardware watchdog, factory reset, system and port LED |
|---|---|
| Basic Function | Support global information, statistical information, log information |
| Basic Function | Support User management, alarm management, configuration management |
| Basic Function | Support Port rate, duplex, flow control, maximum frame length configuration |
| Basic Function | Support Port mirroring, port speed limit, port energy saving |
| PoE Function | Support PoE time management |
| PoE Function | Support PoE automatic monitoring and watchdog |
| PoE Function | Support PoE Port power supply and power configuration |
| Layer 3 Interface | Support Layer 3 Interface |
| Layer 3 Interface | Support IPv4, IPv6 address Configuration |
| Layer 3 Interface | Support ARP Configuration |
| Layer 3 Interface | Support ND Configuration |
| Layer 3 Routing | Support IPv4 static routing |
| Layer 3 Routing | Support IPv6 static routing |
| Layer 3 Routing | Support RIP V1/V2 |
| Layer 3 Routing | Support OSPF |
| DHCP | Support DHCP server |
| DHCP | Support DHCP Relay |
| DHCP | Support DHCP Snooping |
| VLAN | Support 4K VLAN |
| VLAN | Support 802.1Q VLAN, based on port VLAN |
| VLAN | Support Access, Trunk, Hybrid VLAN mode |
| VLAN | Support GVRP (VLAN registration protocol) |
| VLAN | Support MAC VLAN, IP VLAN |
| VLAN | Support Voice VLAN |
| MAC address | Support MAC address automatic learning and aging |
| MAC address | Support Static, dynamic, filtered address table |
| Security Feature | Password protection |
| Security Feature | Support Restrict user access based on port number, IP address, MAC address |
| Security Feature | Support HTTPS, SSH V1/V2 |
| Security Feature | Support VLAN-IP-MAC-PORT binding |
| Security Feature | Support ARP detection, IP source protection, DoS protection |
| Security Feature | Support DHCP Snooping, DHCP Attack protection |
| Security Feature | Support 802.1X Certification |
| Security Feature | Support AAA (Authentication, Authorization, Accounting), Support RADIUS protocol, TACASC+ |
| Security Feature | Support Port security, port isolation |
| Access Control | Support L2(Layer 2)～L4(Layer 4) Packet filtering function |
| Access Control | Support Port mirroring, flow rate limiting, QoS remarking |
| QOS | Support 8 ports queues |
| QOS | Support Port priority, 802.1P priority, DSCP priority |
| QOS | Support Port priority, 802.1P priority, DSCP priority |
| STP | Support STP(IEEE 802.1d), RSTP(IEEE 802.1w) and MSTP(IEEE 802.1s) protocol |
| STP | Support Multi-instance, Support Aggregate interface |
| STP | Support BPDU protection |
| Multicast | Support IGMP v1/v2/v3 Snooping |
| Multicast | Support MLD v1/v2 Snooping |
| Multicast | Support Layer 2 multicast fast leave mechanism, querier |
| Multicast | Support Layer 2 IPv4 static multicast |
| Multicast | Support Layer 2 IPv6 static multicast |
| Multicast | Support IGMP v1/v2/v3 Layer 3 multicast |
| Storm Suppression | Support multicast suppression |
| Storm Suppression | Support broadcast storm suppression |
| Storm Suppression | Support unknown unit-cast suppression |
| Loop Protection | Support loop protection |
| Link Aggregation | Support Static Aggregation |
| Link Aggregation | Support LACP Dynamic Aggregation |
| Link Aggregation | Support based on IP, MAC, mixed load-balancing modes |
| Link Aggregation | Maximum support 8 aggregation groups (8 ports per aggregation group) |
| IPv6 | Support IPv6 Ping, IPv6 Traceroute, IPv6 Telnet |
| IPv6 | Support IPv6 SSH |
| IPv6 | Support IPv6 HTTP, IPv6 HTTPS |
| Management & Maintenance | Support WEB Management (HTTP、HTTPS) |
| Management & Maintenance | Support CLI (Telnet, SSH V1/V2, Local serial port) |
| Management & Maintenance | Support SNMP V1/V2/V3 |
| Management & Maintenance | Support RMON V2 |
| Management & Maintenance | Support LLDP Device discovery |
| Management & Maintenance | Support SNTP Time synchronization |
| Management & Maintenance | Support CPU Monitoring, Memory Monitoring |
| Management & Maintenance | Support System log, classification warning |
| Management & Maintenance | Support Ping, Trace route detection, cable detection |