# XA-M045 · Michael Jezierski / IndyCar · 美国

> **现判 XC 暂不管** ｜ 来源 mikrotik-info `A-060`（原评级 A，阶段 01-contacted） ｜ 导入 2026-10-27 ｜ 研究状态：已研究（W1-R02 2026-10-27）→ 下一动作 不动

## 1. 初判与理由
- 初判：**XA** — 主攻区（美加/欧/土）+ 渠道型买家 + 有可用商务邮箱
- 研究后改级：XA → **XC**（W1-R02，终端触点，非渠道 → C）；编号不变
- 标记：S箱已群发
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Michael Jezierski / IndyCar |
| 国家 / 城市 | 美国 / Indianapolis |
| ISO | US |
| 网站 | indycar.com |
| 类型 / 角色 | 集成商/顾问（MikroTik 认证） |
| 在卖品牌（反向信号） | MikroTik 认证顾问 MTCNA+MTCRE+MTCIPv6E+MTCSWE |
| 自有品牌 | 否 |
| 切入点（来源库） | MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战 |
| 组织 / 模式（来源库推断） | 公司/工作室（有官网） / 工程/集成项目制 |
| 他们首推（仅参考，不照搬） | STC-424XGGPM-280W |
| 来源库优先级 / 状态 | ★★★ / 01-已跟进一轮（用户报告；具体日期/收件人未逐户记录） |
| 来源库之来源 | 2026-09-22 |
| 来源库备注 | ★★ 持 MTCSWE；**专做美国赛车运动产业与车队（邮箱是 @indycar.com，人在 IndyCar 赛事方）**；业务：Layer 2/3、无线 LAN、PtP、**IP 视频与组播 IP Video & Multicast**、IP 对讲、**Audinate Dante 认证 1/2/3 级（专业音频 over IP）** → 赛事转播+ Dante 音频对交换机的 IGMP Snooping/组播/低时延要求极高，是极高门槛高单价的细分市场 |
| 来源库评级依据 | 有明确交换/供电需求（交换认证 MTCSWE、PoE/监控/门禁、组播/IPTV），且有具体人直联 |
| 来源文件 | `profile/A/A-060-Michael Jezierski - IndyCar-美国.md` @ elsasaga-cloud/mikrotik-info@a60f11f8 (arena/01a0c3ef-mikrotik-info)（更新 2026-10-12） |

来源库「基本事实」表（原样）：

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Michael Jezierski / IndyCar（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Indianapolis | 事实 |
| 网站 | indycar.com | 事实 |
| 类型 | 集成商/顾问（MikroTik 认证） | 事实（CSV 名录口径） |
| 关键人 | Michael Jezierski | 事实 |
| 反向信号（资质/品牌） | MikroTik 认证顾问 MTCNA+MTCRE+MTCIPv6E+MTCSWE | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 3. 联系方式
- 邮箱：mjezierski@indycar.com（首选）
- 电话：+1 317 492 5005（内部用，不进外发材料）
- 来源库入口字段：+1 317 492 5005 / mjezierski@indycar.com

来源库「联系方式」段原文：

> - **邮箱**：mjezierski@indycar.com
>   - 状态：既有/公开
> - **电话**：+1 317 492 5005
> - 来源等级：official-channel（R41–R48 联系方式台账口径）
> - **原始联系字段**：+1 317 492 5005 / mjezierski@indycar.com

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱群发：「24 Port PoE Managed Switch」→ mjezierski@indycar.com，首次 2026-09-28，最后 2026-09-28，去信 1，来信 0（对账源 `data/gmail_s/2026-09_10群发名单_未入库.csv`；来信含自动回复，需人工看）

## 7. 我方产品线提示
- SmartByte 商用管理型（Marvell）为主 + Saga STI 工业系列补位（MikroTik/Allied/工业品牌渠道，缺的是性价比管理型与工业 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究卡（第 2 步，W1-R02，2026-10-27）

- **结论：XC** — 终端触点，非渠道 → C
- 活着吗：来源库 2026-09-28 核对在线；本轮未复查
- 一句话：终端用户内部工程师（赛事方 IndyCar）；MikroTik 认证顾问：自己做方案/集成/运维并自行采购设备 → 用 ERPS/IGMP/VLAN/CLI/MIB 这类技术语言切入，不打价格战
- 是什么人：终端用户内部工程师（赛事方 IndyCar）；规模：未量化
- 在卖/在用：MikroTik 认证顾问 MTCNA、MTCRE、MTCIPv6E、MTCSWE
- 对口哪条线：—
- 找得到人吗：mjezierski@indycar.com（来源库公开邮箱）；KP：无具名
- 已触达：S 箱 2026-09-28 群发「24 Port PoE Managed Switch」→ 已发未回
- 与 Saga Clients：无
- **下一动作：不动** — 分销首触：24 口 PoE + STI 工业线；型号 STC-424XGGPM-280W / STI-288DGGPM；价 USD 170 EXW Shenzhen (snapshot 2026-10-27, valid 15 days) / USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)；建议 不动

证据：
| 类型 | 说明 | 摘录 | 来源 | 日期 |
|---|---|---|---|---|
| 来源库官网/名录核对 | ★★ 持 MTCSWE；专做美国赛车运动产业与车队（邮箱是 @indycar.com，人在 IndyCar 赛事方）；业务：Layer 2/3、无线 LAN、PtP、IP 视频与组播 IP Video & Multicast、IP 对讲、Audinate Dante 认证 1/2/3 级（专业音频 over IP） → 赛事转播+ Dante 音频对交换机的 IGMP Snooping/组播/低时延要求极高，是极高门槛高单价的细分市场 |  | https://indycar.com/ | 2026-09-28 |
| S 箱群发记录 | S 箱 2026-09-28 发 mjezierski@indycar.com「24 Port PoE Managed Switch」，去 1 来 0 |  | data/gmail_s/2026-09_10群发名单_未入库.csv | 2026-09-28 |

- 备注：轻卡：本轮未外查，沿用来源库官网/名录核对。
