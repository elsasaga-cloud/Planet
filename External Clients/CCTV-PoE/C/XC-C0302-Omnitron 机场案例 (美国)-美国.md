# XC-C0302 · Omnitron 机场案例 (美国) · 美国

> **初判 XC 暂不管** ｜ 来源 CCTV-PoE `profile/new-customers-batch-35.md`:33 ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）
>
> **C 池三闸筛选（External 同法，`data/external_clients/sieve_x.json`）：⛔ 已过筛 · 永久 pass**（闸 0 · G0-1 · 2026-10-29）：来源库「终端触点」= 文档里提到的终端 / 市场主体名称（商场、球场、连锁、项目），原文无邮箱、电话、网址、WA 等任何联系线索 —— 不再研究 / 不群发 / 不监控；撤销只在客户主动找上门时由 Simon 拍板

## 1. 初判与理由
- 初判：**XC** — 终端用户 / 渠道触点（机场、大学、超市、政府、军队…走集成商与框架采购，不是 Saga 的直接买家）
- 标记：profile批次文件、多处出现×2、终端触点
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Omnitron 机场案例 (美国) |
| 国家 / 城市 | 美国 |
| ISO | US |
| 网站 | — |
| 类型 / 角色 | B类 - 机场 WiFi + 监控 |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 35 — 矩阵式深挖：洁净室 + 机场 + NDAA/TAA + 中美洲 + 太平洋岛国 + 南亚 + WISP + 危险环境 > ✈️ 二、机场/航空 PoE |
| 来源库字段·类型 | B类 - 机场 WiFi + 监控 |
| 来源库字段·产品 | iConverter + OmniConverter PoE media converters |
| 来源库字段·方案 | 光纤从核心 PoP 到 IDF, PoE 交换机 + WiFi AP + IP 摄像头 |
| 来源库字段·拓扑 | Hub and spoke (每个 concourse 4 个 IDF) |
| 来源库字段·挑战 | 停车场户外摄像头需硬化设备, 长距离需光纤 |
| 来源库字段·开发策略 | 美国机场 PoE 光纤方案 |
| 来源库字段·置信度 | ★★★★★ |
| 来源库字段·案例 | 主要国际机场WiFi+监控, iConverter千兆媒体转换器19模块机箱+SNMP管理, 18路千兆光纤分发, OmniConverter PoE媒体转换器光纤转铜+PoE+供电WiFi AP |
| 来源库字段·特点 | 远程重启WiFi AP (光纤端口关闭/断开), 无需物理访问设备, 无需昂贵AC电源插座 |
| 来源文件 | `profile/new-customers-batch-35.md` 第 33 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |
| 同一家在来源库其他位置 | `profile/new-customers-batch-44.md`:129（Batch 44 — 危险环境+交通PoE：ATEX防爆 + 交通路口 + 机场） |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> 3. Omnitron 机场案例 (美国)
> - **类型**: B类 - 机场 WiFi + 监控
> - **产品**: iConverter + OmniConverter PoE media converters
> - **方案**: 光纤从核心 PoP 到 IDF, PoE 交换机 + WiFi AP + IP 摄像头
> - **拓扑**: Hub and spoke (每个 concourse 4 个 IDF)
> - **挑战**: 停车场户外摄像头需硬化设备, 长距离需光纤
> - **开发策略**: 美国机场 PoE 光纤方案
> - **置信度**: ★★★★★
>
> ——另见 `profile/new-customers-batch-44.md`:129：
> 17. Omnitron 机场案例 (美国)
> - **类型**: B类 - 机场PoE
> - **案例**: 主要国际机场WiFi+监控, iConverter千兆媒体转换器19模块机箱+SNMP管理, 18路千兆光纤分发, OmniConverter PoE媒体转换器光纤转铜+PoE+供电WiFi AP
> - **特点**: 远程重启WiFi AP (光纤端口关闭/断开), 无需物理访问设备, 无需昂贵AC电源插座
> - **开发策略**: 美国机场PoE专家 ★★★★★
> 
> ---

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
