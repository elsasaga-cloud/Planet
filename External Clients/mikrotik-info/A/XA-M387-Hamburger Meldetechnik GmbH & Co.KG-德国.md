# XA-M387 · Hamburger Meldetechnik GmbH & Co.KG · 德国

> **初判 XA 长期跟进** ｜ 来源 mikrotik-info `A-156`（原评级 A，阶段 01-contacted） ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）

## 1. 初判与理由
- 初判：**XA** — 主攻区（美加/欧/土）+ 渠道型买家 + 有可用商务邮箱（含实名 KP）
- 标记：S箱已群发
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Hamburger Meldetechnik GmbH & Co.KG |
| 国家 / 城市 | 德国 / Hamburg |
| ISO | DE |
| 网站 | https://www.hmt-hamburg.com |
| 类型 / 角色 | 集成商/代理（Allied Telesis） |
| 在卖品牌（反向信号） | Allied Telesis（Marvell Prestera 接入层） |
| 自有品牌 | 否 |
| 切入点（来源库） | Marvell Prestera 接入层切入 |
| 组织 / 模式（来源库推断） | 公司/工作室（有官网） / 工程/集成项目制 |
| 他们首推（仅参考，不照搬） | STC-424XGGPM-280W |
| 来源库优先级 / 状态 | ★★★ / 01-已跟进一轮（用户报告；具体日期/收件人未逐户记录） |
| 来源库之来源 | Allied Telesis 官方伙伴定位器（?country=germany） |
| 来源库备注 | 伙伴等级：Resell。 【2026-09-27 联系方式核验】公开邮箱·一方/伙伴来源。实际抓取官网联系页，明文 mailto 地址；剔除第三方目录混入的 hkt 错域名。 来源：[1](https://www.hmt-hamburg.com/kontakt) |
| 来源库评级依据 | 【人工定级】A —— 自动规则已跳过；人工指定 |
| 来源库人工定级 | A |
| 来源文件 | `profile/A/A-156-Hamburger Meldetechnik GmbH & Co.KG-德国.md` @ elsasaga-cloud/mikrotik-info@a60f11f8 (arena/01a0c3ef-mikrotik-info)（更新 2026-10-12） |

来源库「基本事实」表（原样）：

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Hamburger Meldetechnik GmbH & Co.KG（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 德国 / Hamburg | 事实 |
| 网站 | https://www.hmt-hamburg.com | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 3. 联系方式
- 邮箱：info@hmt-hamburg.com（首选）
- 来源库入口字段：info@hmt-hamburg.com [Publicly listed; delivery not tested]; https://www.hmt-hamburg.com

来源库「联系方式」段原文：

> - **邮箱**：info@hmt-hamburg.com
>   - 状态：既有/公开
> - **电话**：—
> - 来源等级：official（R41–R48 联系方式台账口径）
> - **原始联系字段**：info@hmt-hamburg.com [Publicly listed; delivery not tested]; https://www.hmt-hamburg.com
> - **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
>   - **Erk Foth**(Geschäftsführer(2003 创铺即任至今=业主级直达))— 官网官网 unternehmen+openregister+Kompass+northdata 四源 〔已有(公司官方公开件/登记册自曝);源:https://www.hmt-hamburg.com/ueber-uns/unternehmen〕

## 4. 关键人（KP）
| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 | 性质 |
|---|---|---|---|---|---|
| Erk Foth | Geschäftsführer(2003 创铺即任至今=业主级直达) | 官网官网 unternehmen+openregister+Kompass+northdata 四源 | official-self-published·谱/leads-only(直发需 opt-in) | https://www.hmt-hamburg.com/ueber-uns/unternehmen | 实名 |

## 5. 证据与来源 URL（来源库）
- https://www.hmt-hamburg.com/ueber-uns/unternehmen
- https://www.hmt-hamburg.com

## 6. 已知触达
- Saga S 箱群发：「24 Port PoE Managed Switch」→ info@hmt-hamburg.com，首次 2026-09-29，最后 2026-09-29，去信 1，来信 0（对账源 `data/gmail_s/2026-09_10群发名单_未入库.csv`；来信含自动回复，需人工看）

## 7. 我方产品线提示
- SmartByte 商用管理型（Marvell）为主 + Saga STI 工业系列补位（MikroTik/Allied/工业品牌渠道，缺的是性价比管理型与工业 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
