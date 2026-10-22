# SmartByte 在开源监控生态与 IEEE OUI 里的痕迹（GitHub 侧爬，2026-10-22T13:34Z）

> 来源：GitHub REST API（沙箱可直连 github.com）。T29-U13 ③ 「所有相关网站」补充。原样入库。

## 1. LibreNMS 原生支持「SmartByte OS」—— 由 NYNEX 的 Frederik Kriewitz 贡献，测试机是 Saga 的 STC-4168XGGCM
| 事实 | 依据 |
|---|---|
| LibreNMS 主仓 PR **#18681「Add support for SmartByte OS」**，作者 **Frederik Kriewitz <frederik@kriewitz.eu>**（= SA-013 NYNEX satellite OHG 的 f.kriewitz@nynex.de），合并 **2026-01-11**；文件 `LibreNMS/OS/Smartbyte.php`（© 2025 Frederik Kriewitz）、`resources/definitions/os_detection/smartbyte.yaml`（text: 'SmartByte'，type: network，**sysObjectID .1.3.6.1.4.1.56166**）、`os_discovery/smartbyte.yaml`（ENTITY-MIB 型号/版本/序列号；NMS-SYS-MIB 温度表 .56166.1.2.4.1.2、NMS-OPTICAL-MIB 光模块 DDM .56166.1.8.2.1.10、风扇/电源状态） | `repos/librenms/librenms/commits?path=LibreNMS/OS/Smartbyte.php`；文件内容 |
| 测试夹具 `tests/data/smartbyte_stc-4168xggcm.json` / `tests/snmpsim/smartbyte_stc-4168xggcm.snmprec`：**sysDescr = "Product STC-4168XGGCM V1.1 Version hotfix/7.4.7 (r1540 af525c9)"，hardware = STC-4168XGGCM，serial 202509160001 / EC4BD14642** —— 用的是 **Saga 型号名**（NYNEX 2025-09-15 那单的机器，序列号 20250916） | 文件内容 |
| 含义：全球最常用的开源 NMS 之一已把 Saga/SmartByte 交换机当独立 OS 识别（按 .56166 判定）→ ① NYNEX 2026-10-15 坚持要「SmartByte OID」的技术原因就在这里（他们的 LibreNMS 靠 sysObjectID .56166 识别）；② Saga 可以对外说「LibreNMS natively supported（OS: SmartByte, since v25.x/2026-01）」；③ 若 Saga 日后换成自己的 PEN，LibreNMS 识别会失效（Q-02/PEN 决策要考虑） | 推断 |

## 2. netdata：SNMP trap 档案「shenzhen-smartbyte-technology-co-ltd」
- `netdata/netdata` 2026-06-11 Costa Tsaousis「go.d: add profile-based SNMP trap ingestion (#22652)」自动生成 `snmp.trap-profiles/default/shenzhen-smartbyte-technology-co-ltd.yaml`（vendor 名由 MIB 目录生成；mib_count 1、trap_count 6；varbinds fanIndex .56166.1.2.5.1.1、fanSpeedStatus、powerIndex .56166.1.2.3.1.1、powerState …）；另有 `netdata/learn` 文档页「Shenzhen Smartbyte Technology Co Ltd SNMP Traps」。
- 含义：SmartByte 的 NMS-SYS-MIB 已进入公共 MIB 目录（netdata 用的 MIB 库），企业名登记为 **Shenzhen Smartbyte Technology Co., Ltd**。

## 3. Tencent BlueKing Lite：`switch_smartbyte` Telegraf SNMP 采集插件
- `TencentBlueKing/bk-lite` 2026-10-05 zhongmingFan「feat(monitor): 新增 switch_smartbyte SNMP 采集插件，采集 NMS-SYS CPU/内存/温度/风扇/电源」，2026-10-21 再修；目录 `server/apps/monitor/support-files/plugins/Telegraf/snmp/switch_smartbyte/`（metrics.json + toml.j2）。
- 含义：国内腾讯蓝鲸轻量版把 SmartByte 当独立交换机类型 → SmartByte 在国内有被纳管的客户规模（间接证据）。

## 4. IEEE OUI / MA-M 登记
- **SmartByte：MA-M 块 FC:CD:2F:D（FCCD2FD）**，登记名「Shenzhen Smartbyte Technology Co., Ltd.」，地址「6th Floor, Building D, Huiqing Science and Technology Park, No. 8 Dafu Industrial Zone, Guanlan Street, Longhua District, Shenzhen 518110」（IEEE MA-M 2020-08-30 快照，`angelcamposm/mac-vendor-lookup/storage/ieee/oui_mam_20200830.csv`）→ 与证书上的「观澜大富工业区惠庆科技园」一致，并给出楼栋 D 栋 6 楼（证书写 1602 室 —— 冲突原样保留）。
- **Hohunet：OUI D8:5B:22**，登记名「Shenzhen Hohunet Technology Co., Ltd」（`MR-JK-37/netpulse` oui_database、`pre-history/pg-oui` vendors、systemd hwdb 补丁）。
- HRUI：未在 OUI 列表命中（可能用板厂/客户 OUI）。

## 5. 对 Saga 的用法（建议，未裁决）
- 给欧美工程型客户的资料里加一句：「Natively detected by LibreNMS (OS 'SmartByte', sysObjectID .1.3.6.1.4.1.56166) and netdata SNMP-trap profiles」—— 这是 NYNEX 替 Saga 做的背书，且是 Saga 型号名出现在上游测试数据里。
- 同时意味着 Saga 品牌独立性进一步变弱：上游生态认的是 SmartByte 的 PEN，不是 Saga。
