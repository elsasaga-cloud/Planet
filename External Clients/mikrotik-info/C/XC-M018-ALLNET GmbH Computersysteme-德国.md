# XC-M018 · ALLNET GmbH Computersysteme · 德国

> **初判 XC 暂不管** ｜ 来源 mikrotik-info `B-138`（原评级 B，阶段 01-contacted） ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）

## 1. 初判与理由
- 初判：**XC** — 与 Saga Clients 重叠（SA-019，经 allnet.de）→ 以 Saga 档为准，本条不单独跟
- 标记：重复=Saga
- 与 Saga Clients 重叠：**SA-019**（Saga 评级 A，经域名 allnet.de）→ 以 Saga 档为主；本条只保留来源库事实
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | ALLNET GmbH Computersysteme |
| 国家 / 城市 | 德国 |
| ISO | DE |
| 网站 | shop.allnet.de |
| 类型 / 角色 | 分销（MikroTik 官方） |
| 在卖品牌（反向信号） | MikroTik（Master+VAD） |
| 自有品牌 | 否 |
| 切入点（来源库） | ALLNET 集团德国总部（法/意为同一集团）→ 一次谈三国 |
| 组织 / 模式（来源库推断） | 分销/批发商（有官网） / 分销 stocking |
| 他们首推（仅参考，不照搬） | CONSULT-OEM |
| 来源库优先级 / 状态 | ★★★ / 01-已跟进一轮（用户报告；具体日期/收件人未逐户记录） |
| 来源库之来源 | 2026-09-22 |
| 来源库备注 | Germering；自有品牌，做 OEM 有基础 |
| 来源库评级依据 | 通用分销商信号，无差异化切入点，慢慢跟 |
| 来源文件 | `profile/B/B-138-ALLNET GmbH Computersysteme-德国.md` @ elsasaga-cloud/mikrotik-info@a60f11f8 (arena/01a0c3ef-mikrotik-info)（更新 2026-10-12） |

来源库「基本事实」表（原样）：

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | ALLNET GmbH Computersysteme（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 | 事实 |
| 网站 | shop.allnet.de | 事实 |
| 类型 | 分销（MikroTik 官方） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | MikroTik（Master+VAD） | 事实（名录/自报口径） |
| 组织性质 | 分销/批发商（有官网） | 【推断】 |
| 商业模式 | 分销 stocking | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |
| R55·背景深描 | 1991 创 35 年;Germering München 郊;€94.5M;Bauer 独家执;谱系全球(B-001/B-115/italia/fr) | 事实+【推断】混合，见证据摘录 |
| R55·芯片与在用型号 | 计算/网络/软件产品;自有品牌+DropShipping;Home Automation/Stromversorgung/VoIP | 事实+【推断】混合，见证据摘录 |
| 批注 | R65 B 升 v2(来源:R57-BC 备护深挖转写;P1=判位备档参考位,评级不动,不出信守档) | 【推断】 |

## 3. 联系方式
- 邮箱：sales@allnet.de（首选）
- 电话：+49 89 89422222；+49 89 894222-22（内部用，不进外发材料）
- 来源库入口字段：+49 89 89422222 / sales@allnet.de

来源库「联系方式」段原文：

> - **邮箱**：sales@allnet.de
>   - 状态：既有/公开
> - **电话**：+49 89 89422222
> - 来源等级：official-channel（R41–R48 联系方式台账口径）
> - **原始联系字段**：+49 89 89422222 / sales@allnet.de
> - **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
>   - **Wolfgang Marcus Bauer**(Geschäftsführer & Inhaber(董事总经理/业主))— 经 +49 89 894222-22 总线 〔猜测(leads-only·LinkedIn/谱面带核,直发需 opt-in);源:https://www.wer-zu-wem.de/firma/allnet-computer.html〕

## 4. 关键人（KP）
| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 | 性质 |
|---|---|---|---|---|---|
| Wolfgang Marcus Bauer | Geschäftsführer & Inhaber(董事总经理/业主) | 经 +49 89 894222-22 总线 | wer-zu-wem + Lieferanten + DnB 三源实名 | https://www.wer-zu-wem.de/firma/allnet-computer.html | 实名 |

## 5. 证据与来源 URL（来源库）
- https://www.wer-zu-wem.de/firma/allnet-computer.html

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 7. 我方产品线提示
- SmartByte 商用管理型（Marvell）为主 + Saga STI 工业系列补位（MikroTik/Allied/工业品牌渠道，缺的是性价比管理型与工业 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
