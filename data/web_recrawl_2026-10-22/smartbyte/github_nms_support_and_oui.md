# SmartByte 在开源监控生态与 IEEE OUI 里的痕迹（GitHub 侧爬，2026-10-22T13:34Z）

> 来源：GitHub REST API（沙箱可直连 github.com）。T29-U13 ③ 「所有相关网站」补充。原样入库。

## 1. LibreNMS 原生支持「SmartByte OS」—— 由 NYNEX 的 Frederik Kriewitz 贡献，测试机是 Saga 的 STC-4168XGGCM
| 事实 | 依据 |
|---|---|
| LibreNMS 主仓 PR **#18681「Add support for SmartByte OS」**，作者 **Frederik Kriewitz <frederik@kriewitz.eu>**（= SA-013 NYNEX satellite OHG 的 f.kriewitz@nynex.de），合并 **2026-01-11**；文件 `LibreNMS/OS/Smartbyte.php`（© 2025 Frederik Kriewitz）、`resources/definitions/os_detection/smartbyte.yaml`（text: 'SmartByte'，type: network，**sysObjectID .1.3.6.1.4.1.56166**）、`os_discovery/smartbyte.yaml`（ENTITY-MIB 型号/版本/序列号；NMS-SYS-MIB 温度表 .56166.1.2.4.1.2、NMS-OPTICAL-MIB 光模块 DDM .56166.1.8.2.1.10、风扇/电源状态） | `repos/librenms/librenms/commits?path=LibreNMS/OS/Smartbyte.php`；文件内容 |
| 测试夹具 `tests/data/smartbyte_stc-4168xggcm.json` / `tests/snmpsim/smartbyte_stc-4168xggcm.snmprec`：**sysDescr = "Product STC-4168XGGCM V1.1 Version hotfix/7.4.7 (r1540 af525c9)"，hardware = STC-4168XGGCM，serial 202509160001 / EC4BD14642** —— 用的是 **Saga 型号名**（NYNEX 2025-09-15 那单的机器，序列号 20250916） | 文件内容 |
| 含义：全球最常用的开源 NMS 之一已把 Saga/SmartByte 交换机当独立 OS 识别（按 .56166 判定）→ ① NYNEX 2026-10-15 坚持要「SmartByte OID」的技术原因就在这里（他们的 LibreNMS 靠 sysObjectID .56166 识别）；② Saga 可以对外说「LibreNMS natively supported（OS: SmartByte, since v25.x/2026-01）」；③ 若 Saga 日后换成自己的 PEN，LibreNMS 识别会失效（Q-02/PEN 决策要考虑） | 推断 |

## 1b. Oxidized（配置备份工具）也有「smartbyte」模型 —— 同样是 Kriewitz（13:37Z 补）
- `ytti/oxidized` 2026-01-23 「smartbyte: new model for SmartByte switches」作者 Frederik Kriewitz（提交署名拼作 "Frderik"）；2026-03-31 Robert Cheramy（维护者）修订。`lib/oxidized/model/smartbyte.rb`：命令 `show running-config` / `show version` / `show interface optical-transceiver info` / `show power`，隐藏 SNMP community；测试数据 `spec/model/data/smartbyte#STC-4168XGGCM_7.4.7#…`（又是 Saga 的 STC-4168XGGCM，固件 7.4.7，配置样例含 hostname/logging/snmp-server/ip dns/spanning-tree mode rstp）。
- 含义：NYNEX 把 Saga 交换机纳入了 LibreNMS（监控）+ Oxidized（配置备份）两套主流开源运维链，并把两处上游适配都提交回社区；同一客户在 2026-01 的两周内完成，说明 NYNEX 是把 Saga 机器当**长期在网设备**管理的。
- 派生仓库 `RND-NoriTech/NMS-WHITE-V2`、`kruczek8989/librenms_old_kruczek8989` 为 LibreNMS fork，自然带上 smartbyte 夹具。
- 其他 Saga 型号码（STC-448XGGPM、STI-288DGGPM、STC-424XGGPM）在 GitHub 代码搜索里只出现在 Simon 自己的 `sagatele-site`；"sagatele" 其余命中为过期域名清单噪音。

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

## 6. 补证（2026-10-22T14:45Z）：PR 细节 + S 邮箱时间线对齐
- PR #18681 由 `freddy36`（Frederik Kriewitz）**2025-12-19T15:52Z 创建**，2026-01-11T23:10Z 由维护者 `laf` 合并，9 个文件 +10,530 行：`LibreNMS/OS/Smartbyte.php`、`html/images/os/smartbyte.png`（SmartByte 图标）、**三份 SmartByte 私有 MIB `mibs/smartbyte/NMS`（根 `enterprises 56166`，LAST-UPDATED 2021-05-13）/ `NMS-SYS-MIB`（LAST-UPDATED 2025-12-11 14:10Z）/ `NMS-OPTICAL-MIB`**、os_detection / os_discovery yaml、测试夹具 json + snmprec（2,145 行，30 个接口 gigabitEthernet0/x…）。PR 正文："Shenzhen SmartByte Technology Co.,Ltd manufactures various Marvell chipset based switches." 首个含此支持的发行版 **LibreNMS 26.1.0（2026-01-12）**。
- 夹具里 sysDescr = "Product STC-4168XGGCM V1.1 Version hotfix/7.4.7 (r1540 af525c9)"，entPhysicalModelName = STC-4168XGGCM，entPhysicalSerialNum = 202509160001，sysContact/sysLocation 已打码 `<private>`。
- **S 邮箱对齐（SA-013 线程「Testing Feedback」「Marvell Alleycat5 Solution」）**：2025-02-11 NYNEX 测试反馈——无电源/风扇/温度监控、SNMP 只有基础数据、缺 LLDP-V2-MIB 与光模块 DDM，当时选用 BDCOM S2900-24T4X-2AC / S2900-24S8C4X-2AC；2025-03 Simon 答 AC3→AC5 过渡、AC5 上补齐；2025-12-10 NYNEX：风扇数据有了但 sys 表（CPU/内存/电源/温度）没了，**固件企业号 = 0（保留值），更早固件用 57430 = Fuzhou Dockeer Technology**（问「是 SmartByte 旧名还是另一家 OEM 伙伴？」）；2025-12-17 Simon 发新固件/MIB（WeTransfer，密码 Saga）：sys 表修复、**OID=56166 Smartbyte**、补 0 值映射；同日 NYNEX `show version`：Software hotfix/7.4.7 (r1540 af525c9)，Release 2025-12-11 17:09:22，**System MAC fc:cd:2f:d0:4f:db**，PID STC-4168XGGCM V1.1，SN 202509160001；2025-12-18 确认 OID 生效「working as expected」；**次日 2025-12-19 即开 LibreNMS PR**。2026-01-20：230 台项目因交期用了现有供应商（BDCOM），但「confident that we can use them in upcoming projects」。
- **MAC 直接证据**：fc:cd:2f:d0:4f:db 落在 SmartByte 的 IEEE MA-M 块 FC:CD:2F:D（范围 FC:CD:2F:D0:00:00–FC:CD:2F:DF:FF:FF，2^20 = 1,048,576 个地址）之内 → Saga 出货的机器在 MAC 层可被任何 OUI 查询识别为 Shenzhen Smartbyte Technology。
- 冲突 **C14**：SmartByte 固件 / MIB 血统——旧固件企业号 57430（福州 Dockeer）、新固件 0 → 56166；MIB 根文件 2021-05 建、2025-12 改。Dockeer 与 SmartByte 的关系未证实（同一软件外包方 / 另一 OEM 客户 / 旧公司名三说并存）。
