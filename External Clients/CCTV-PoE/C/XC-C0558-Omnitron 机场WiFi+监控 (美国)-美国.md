# XC-C0558 · Omnitron 机场WiFi+监控 (美国) · 美国

> **初判 XC 暂不管** ｜ 来源 CCTV-PoE `profile/new-customers-batch-54.md`:19 ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）

## 1. 初判与理由
- 初判：**XC** — 终端用户 / 渠道触点（机场、大学、超市、政府、军队…走集成商与框架采购，不是 Saga 的直接买家）
- 标记：profile批次文件、终端触点
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Omnitron 机场WiFi+监控 (美国) |
| 国家 / 城市 | 美国 |
| ISO | US |
| 网站 | — |
| 类型 / 角色 | B类 - 机场PoE光纤backhaul |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 54 — 关键基础设施PoE：机场航空 + 铁路地铁 + 污水处理 + 电网变电站 + 政府军事 > ✈️ 一、机场航空 PoE |
| 来源库字段·类型 | B类 - 机场PoE光纤backhaul |
| 来源库字段·案例 | 主要国际机场升级网络支持WiFi+视频监控增长需求, 克服铜缆距离限制光纤路由到航站楼+大厅+停车结构+跑道WiFi AP+摄像头 |
| 来源库字段·方案 | 光纤从中央互联网PoP核心→IDF (电气网络间) 跨机场, 每IDF PoE交换机+多WiFi AP连接, 每大厅4 IDF千兆hub-spoke拓扑, ~半数交换机需媒体转换器chassis光纤连接AP, 选择Omnitron iConverter高密度光纤分发, iConverter千兆媒体转换器19模块chassis+SNMP管理模块, 每交换机最多18千兆光纤到AP |
| 来源库字段·优势 | OmniConverter PoE media converters紧凑+成本效益商业+温度加固, 光纤距离扩展PoE设备, 多种端口配置灵活点对点或菊花链 |
| 来源库字段·开发策略 | 美国机场PoE光纤backhaul (iConverter高密度) ★★★★★ |
| 来源文件 | `profile/new-customers-batch-54.md` 第 19 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> 2. Omnitron 机场WiFi+监控 (美国)
> - **类型**: B类 - 机场PoE光纤backhaul
> - **案例**: 主要国际机场升级网络支持WiFi+视频监控增长需求, 克服铜缆距离限制光纤路由到航站楼+大厅+停车结构+跑道WiFi AP+摄像头
> - **方案**: 光纤从中央互联网PoP核心→IDF (电气网络间) 跨机场, 每IDF PoE交换机+多WiFi AP连接, 每大厅4 IDF千兆hub-spoke拓扑, ~半数交换机需媒体转换器chassis光纤连接AP, 选择Omnitron iConverter高密度光纤分发, iConverter千兆媒体转换器19模块chassis+SNMP管理模块, 每交换机最多18千兆光纤到AP
> - **优势**: OmniConverter PoE media converters紧凑+成本效益商业+温度加固, 光纤距离扩展PoE设备, 多种端口配置灵活点对点或菊花链
> - **开发策略**: 美国机场PoE光纤backhaul (iConverter高密度) ★★★★★

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
