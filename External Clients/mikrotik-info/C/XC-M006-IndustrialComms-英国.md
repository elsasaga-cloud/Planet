# XC-M006 · IndustrialComms · 英国

> **初判 XC 暂不管** ｜ 来源 mikrotik-info `A-267`（原评级 A，阶段 01-contacted） ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）
>
> **C 池三闸筛选（External 同法，`data/external_clients/sieve_x.json`）：★ P 池 · 正式入池**（随 Saga `SC-331`）（闸 0 · DUP · 2026-10-29）：与 Saga SC-331 同一公司（经 industrialcomms.com）→ 随 Saga 档：pool（闸 3，★ P 池正式入池（档位 ○）：○ 工业分销 20%：Industrial Communication Products Ltd（Toddington 2008；Advantech / INSYS 英国分销；铁路占比高）部分坐实；分销 ✔ ）

## 1. 初判与理由
- 初判：**XC** — 与 Saga Clients 重叠（SC-331，经 industrialcomms.com）→ 以 Saga 档为准，本条不单独跟
- 标记：重复=Saga
- 与 Saga Clients 重叠：**SC-331**（Saga 评级 C，经域名 industrialcomms.com）→ 以 Saga 档为主；本条只保留来源库事实
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | IndustrialComms |
| 国家 / 城市 | 英国 |
| ISO | GB |
| 网站 | https://www.industrialcomms.com |
| 类型 / 角色 | 专业分销 |
| 在卖品牌（反向信号） | EtherWAN |
| 自有品牌 | 否 |
| 切入点（来源库） | ⭐英国T1：熟悉工业交换机，缺低价第二供应源 |
| 组织 / 模式（来源库推断） | 公司/工作室（有官网） / 工程/集成项目制 |
| 他们首推（仅参考，不照搬） | STC-424XGGPM-280W |
| 来源库优先级 / 状态 | ★★★ / 01-已跟进一轮（用户报告；具体日期/收件人未逐户记录） |
| 来源库之来源 | 反向信号/2026-09 |
| 来源库备注 | 交通/公用事业/监控；【2026-09-22 补】经 EtherWAN（台厂，1996 年创立，现被德国 Phoenix Contact 收购）渠道名录确认为其分销商。站点明示经销 EtherWAN 加固型工业交换机（-40~+75℃、5–48 口、非网管/网管/三层）、90W PoE、光纤介质转换器与 VDSL2 延长器，面向交通、公用事业、IP 监控与关键基础设施；地址 Toddington, Bedfordshire。；【2026-09-23】另经 Atop（台厂）渠道确认其为 Atop 英国分销商——串口服务器、Modbus/IEC 61850 协议网关、EN 50155 与 IEC 61850-3 交换机。 【2026-09-27 A260–A279联络核验】来源等级：official-company。官网联系页与EtherWAN产品页正文均给sales@industrialcomms.com与+44 (0)203 086 9569；公司名Industrial Communication Products Ltd、Toddington地址与旧记录一致。EtherWAN分销身份在本轮抓取的EtherWAN产品页复见。 证据：[1](https://www.industrialcomms.com/pages/contact-us) [2](https://www.industrialcomms.com/pages/etherwan) [3](https://www.modernrailways.com/companies/industrial-communication-products-ltd) 仅覆盖所述联络/关联事实，不证明投递、在职、采购权、芯片或需求；批次：batch/contact_research_2026-09-27_A260-A279.json#A-267 |
| 来源库评级依据 | 有明确交换/供电需求（交换专长、PoE/监控/门禁、工业/楼宇），三星重点 |
| 来源文件 | `profile/A/A-267-IndustrialComms-英国.md` @ elsasaga-cloud/mikrotik-info@a60f11f8 (arena/01a0c3ef-mikrotik-info)（更新 2026-10-12） |

来源库「基本事实」表（原样）：

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | IndustrialComms（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 英国 | 事实 |
| 网站 | https://www.industrialcomms.com | 事实 |
| 类型 | 专业分销 | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | EtherWAN | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 3. 联系方式
- 邮箱：sales@industrialcomms.com（首选）
- 邮箱：官网联系页与etherwan产品页正文均给sales@industrialcomms.com与（公开）
- 来源库入口字段：sales@industrialcomms.com（官网联系页正文）；原入口：官网+LinkedIn

来源库「联系方式」段原文：

> - **邮箱**：sales@industrialcomms.com
>   - 状态：既有/公开
> - **电话**：—
> - 来源等级：official-company（R41–R48 联系方式台账口径）
> - **原始联系字段**：sales@industrialcomms.com（官网联系页正文）；原入口：官网+LinkedIn
> - **具名 KP 通道(R66/R64 捕件,已有/猜测分标)**:
>   - **Graham Bull**(CEO(Advantech 2021 分件官方引语))— designsolutionsmag.co.uk 件(引语) 〔已有(公司官方公开件/登记册自曝);源:https://designsolutionsmag.co.uk/advantech-chooses-industrialcomms-as-uk-distributor/〕

## 4. 关键人（KP）
| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 | 性质 |
|---|---|---|---|---|---|
| Graham Bull | CEO(Advantech 2021 分件官方引语) | designsolutionsmag.co.uk 件(引语) | official-self-published·谱/leads-only(直发需 opt-in) | https://designsolutionsmag.co.uk/advantech-chooses-industrialcomms-as-uk-distributor/ | 实名 |

## 5. 证据与来源 URL（来源库）
- https://designsolutionsmag.co.uk/advantech-chooses-industrialcomms-as-uk-distributor/
- https://www.industrialcomms.com

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
