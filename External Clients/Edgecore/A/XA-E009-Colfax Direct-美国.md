# XA-E009 · Colfax Direct · 美国

> **现判 XA 长期跟进** ｜ 来源 Edgecore `A-054`（原评级 A，阶段 00-lead） ｜ 导入 2026-10-27 ｜ 研究状态：已研究（W1-R01 2026-10-27）→ 下一动作 第二封

## 1. 初判与理由
- 初判：**XA** — 主攻区（美加/欧/土）+ 渠道型买家 + 有可用商务邮箱
- 标记：S箱已群发
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Colfax Direct |
| 国家 / 城市 | 美国 / Sunnyvale CA |
| ISO | US |
| 网站 | colfaxdirect.com |
| 类型 / 角色 | SI/VAR/集成商 |
| 细分（来源库） | generic |
| 他们首推（仅参考，不照搬） | STC-424XGGPM-280W |
| 来源库优先级 / 状态 | 00-未触达 |
| 来源文件 | `profile/A/A-054-Colfax-Direct-美国.md` @ elsasaga-cloud/Edgecore@729187d (arena/6214ebb8-edgecore)（更新 2026-10-27） |

来源库「基本事实」表（原样）：

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Colfax Direct | 事实（官方名录） |
| 国家/城市 | 美国 / Sunnyvale CA | 事实（官方名录） |
| 电话 | (408) 730 2275 | 事实（官方名录） |
| 渠道角色 | SI/VAR/集成商（NA-R） | 事实（官方名录口径） |
| 备注 | 官方SI+网店 | 事实（本轮记录） |
| 商业模式 | SI/VAR/集成商，转售/集成 Edgecore 并可能代理多品牌 | 【推断】 |
| 决策链 | 见后段「触达名单」及 R15/R18 定版；本行旧模板口径已失效 | 事实/线索分层 |

## 3. 联系方式
- 邮箱：sales@colfaxdirect.com（首选）
- 邮箱：support@colfaxdirect.com（首选）
- 邮箱：sales@colfax-intl.com（首选）

来源库「联系方式」段原文：

> - **电话**：(408) 730 2275（官方名录）
> - **邮箱**：sales@colfaxdirect.com（官网）；support@colfaxdirect.com；母公司口 sales@colfax-intl.com（官网）
> - **网站**：colfaxdirect.com/colfax-intl.com（R2 官网核验 2026-10-18）

## 4. 关键人（KP）
> - **Gautam Shah** — Chief Executive Officer【D&B Key Principal 单源】
> 
> - 邮箱：sales@colfaxdirect.com（R15 批5 核验 2026-10-19，完整来源见联系方式段）
> - LinkedIn/电话：(408) 730 2275（官方名录）

## 5. 证据与来源 URL（来源库）
- https://www.edge-core.com/where-to-buy/NorthAmerica-reseller/（2026-10-18

> - https://www.edge-core.com/where-to-buy/NorthAmerica-reseller/（2026-10-18 检索，官方渠道名录）；批次：batch/contact_research_2026-10-18_R1_官方渠道全量.json

## 6. 已知触达
- Saga S 箱群发：「24 Port PoE Managed Switch」→ sales@colfaxdirect.com，首次 2026-10-19，最后 2026-10-19，去信 1，来信 0（对账源 `data/gmail_s/2026-09_10群发名单_未入库.csv`；来信含自动回复，需人工看）
- 来源库跟进记录：

| 列1 | 列2 | 列3 | 列4 | 列5 | 列6 |
|---|---|---|---|---|---|
| — | — | — | — | — | — |
- 来源库核验 / 退信摘录：
  - R18 A类增量加厚（2026-10-19）
    - - **现行域名与邮件基础设施**：主域名 `colfaxdirect.com` 于 2026-10-19 经公共 DNS（8.8.8.8）实查：A 记录 `147.182.238.244`；MX `0 colfaxdirect-com.mail.protection.outlook.com`；邮件平台特征为 **Microsoft 365 / Exchange Online Protection**。判定：**A与MX均存在**。
    - - **官方渠道快照对账**：仓库留存的 Edgecore 官方渠道快照（2026-10-18，分区 `northamerica-reseller`）载：地址 **750 Palomar Avenue, Sunnyvale, CA 94085**；电话 (408) 730 2275；渠道定位 SI·VAR·经销商/线上电商。此项用于补齐主体地址并与档内电话对账；若与本档 R15 后段更新的登记/官网字段冲突，以后段为准。
    - - **口径边界**：DNS 阳性仅证明域名与收信基础设施在查询时存在，不证明任一具体邮箱可投递、人员仍在职或有采购意愿；KP/邮箱仍以本档 R15 定版为准。结构化底稿见 `batch/contact_research-2026-10-19_R18_A类增量加厚.json`。首触仍由用户执行，Agent 不发信。
  - R23 存量客户全量加厚（2026-10-25）
    - - **域名与托管指纹**：主域`colfaxdirect.com`为A与MX均存在；网站IPv4 `147.182.238.244`（AS14061 DIGITALOCEAN-ASN - DigitalOcean, LLC, US），未见AAAA；邮件入口 `colfaxdirect-com.mail.protection.outlook.com`（平台特征：Microsoft 365）；NS托管特征为hover.com。
    - - **邮件认证与发信系统信号**：SPF已发布（Microsoft 365，结尾`-all`）；未见公开DMARC政策。SPF include只说明该域授权过的发信系统，不证明采购量或具体邮箱可投递。
    - - **跟进与证据边界**：用户已表示存量客户基本完成一轮跟进；未逐档回传送达/回复结果的，本轮不虚构已送达和已回复。DNS为2026-10-25经8.8.8.8查询快照，结构化底稿见`batch/contact_research-2026-10-25_R23_存量客户全量加厚.json`。Agent不发信。
  - R24 质量复核与纠错加厚（2026-10-25）
    - - **R24 前质量快照**：实质行 95、跨档出现 ≤3 档的专属行 27、≤10 档的稀有行 28、外链来源域 1 个、全档去重邮箱 3 个；启发式审计分 64/100（主体 12/15、联系 18/20、KP 10/15、业务专属度 11/20、证据 8/20、可执行性 7/10、风险扣分 -2）。该分只用于找薄弱档，不证明每条历史事实都正确。
    - - **联系/KP 定版**：首选邮箱为 `sales@colfaxdirect.com`（状态 `public_primary_email_recorded`）；KP 状态 `named_single_candidate`，结构化抽到：Gautam Shah。自动抽取不替代原文的来源、日期和限定语；个人邮箱仅在公开披露且主体一致时保留。
    - - **本轮纠错**：认证口径已按 U31 改为“UL 无；CE/FCC 按型号核实”；商用 PoE 模板已按 U28 收紧为 802.3af/at PoE+。`$198/¥1212` 与 `docs/sales/P1产品价格快照.md` 的 STC-424XGGPM-280W 旧内部价/成本加价链一致，但只作内部历史参考，正式报价前必须重新核成本、汇率与有效期。
    - - **未闭合项**：专属经营事实偏薄；用户逐档送达/回复结果未回填；现行采购型号、月量和认证要求未由客户确认；风险旗需在报价前处理：品类偏HPC/数据中心。
    - - **下一证据路径**：以客户回复或询价确认现行采购型号、月量、认证与进口路径；报价前重新核 SmartByte 成本、汇率和有效期。
    - - **证据纪律**：未核实内容不得拼造邮箱、人物、职务或交易关系；第三方员工/营收估算只作单源线索，官网自述与审计/登记事实分开；用户“基本跟进完了”仍不转写为逐档已送达或已回复。Agent 不发信。
  - R25 运营化加厚与定向复核（2026-10-27）
    - - **决策链工作图**：已实名候选为 Gautam Shah；下一步不是再堆姓名，而是逐人确认谁拥有产品导入、技术验收和 PO 签核权，避免把高管、销售或工程师自动写成采购 KP。
    - - **触达顺序与停发规则**：只走一条已记录主线，不并行轰炸备址。下一证据路径：以客户回复或询价确认现行采购型号、月量、认证与进口路径；报价前重新核 SmartByte 成本、汇率和有效期。 Agent 不发信、不排期；若主口已拦截/失败，不原样重发或并行轰炸人事、支持、财务口。
    - - **风险与未闭合项**：风险标志：品类偏HPC/数据中心。未闭合：专属经营事实偏薄；用户逐档送达/回复结果未回填；现行采购型号、月量和认证要求未由客户确认；风险旗需在报价前处理：品类偏HPC/数据中心。
    - - **R25结论边界**：运营化条目是基于档内既有证据与本轮定向来源的工作框架，不证明现行采购意愿、人员在职、邮箱可投递或订单量；新增外部事实只以本段逐项来源与限定语为准。

## 7. 我方产品线提示
- OEM / 贴牌 + 低价标品（Edgecore 渠道已习惯白牌/开放网络，拿价格与贴牌能力切）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究卡（第 2 步，W1-R01，2026-10-27）

- **结论：XA** — 已在卖 Edgecore 白牌 DC 交换机的美国网店，决策链短，CENTEC 线天然对口；24 口 PoE 那封根本不对路，换 CENTEC 角度再发
- 活着吗：网店活（colfaxdirect.com，按品牌浏览含 Edgecore/Mellanox/Chelsio），2026-10-27
- 一句话：Colfax International（1987 年起的 HPC/AI 服务器厂商，Sunnyvale）的电商部门（2008 起），专卖 HPC/DC 网卡、交换机、线缆、光模块，在售 Edgecore 与 Mellanox/NVIDIA 交换机。10-19 发 sales@ 未回。
- 是什么人：HPC/DC 组件网店（厂商集团下属，自有采购）；规模：母公司 Colfax International 私营；网店团队小
- 在卖/在用：Edgecore、Mellanox/NVIDIA、Chelsio、Netronome、AurCore
- 对口哪条线：CENTEC（网店上架一条低价 10/25/100G 线） — 已经在网店卖 Edgecore 白牌交换机，加一条 Centec 系低价线阻力最小；采购决策在 Colfax 内部，链短
- 找得到人吗：sales@colfaxdirect.com（官网公开，10-19 已发未回）；KP：Gautam Shah（CEO, Colfax International，官方新闻稿引言（2010）+ D&B）
- 已触达：S 箱 2026-10-19 发 sales@ → 已发未回
- 与 Saga Clients：无
- **下一动作：第二封** — 给网店加一条 Centec 系 10/25/100G 低价线；拿 24×10G+2×100G 做锚；型号 STH-2C24XF-HSI；价 USD 1,500 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)；窗口 US 周三 08–10 当地；建议 2026-10-28

证据：
| 类型 | 说明 | 摘录 | 来源 | 日期 |
|---|---|---|---|---|
| 网店 About | Launched in 2008, Colfax Direct is the E-commerce division of Colfax International；Browse by Manufacturer: Chelsio / Edgecore / Mellanox-NVIDIA / Netronome / AurCore |  | https://www.colfaxdirect.com/store/pc/viewcontent.asp?idpage=3 | 2026-10-27 |
| LinkedIn | Colfax Direct provides adapters, switches, cables, SSDs … from Broadcom, Chelsio, Edgecore, Intel, Mellanox… |  | https://www.linkedin.com/company/colfax | 2026-10-27 |
| Edgecore 官网北美 On-Line 名录 | COLFAX DIRECT 750 Palomar Avenue Sunnyvale |  | https://www.edge-core.com/where-to-buy/northamerica-online/ | 2024-12-19 |
| 网店条款 | All deliveries are F.O.B. Sunnyvale（自营库存） |  | https://www.colfaxdirect.com/store/pc/viewcontent.asp?idpage=5 | 2026-10-27 |

草稿（英文，第二封；Simon 发，Agent 不发）：

```text
Subject: A Centec-based 10G/100G line next to Edgecore on colfaxdirect.com

Hi,

I wrote on 19 October under "24 Port PoE Managed Switch"; this is a different angle, so a fresh note rather than a reply.

Colfax Direct already lists Edgecore and NVIDIA switches, so you know the white-box buyer. We build the tier below that on Centec silicon: STH-2C24XF-HSI, 24 x 10G SFP+ + 2 x 100G QSFP28, full L3 (OSPF/BGP, VXLAN), dual hot-swap PSUs, 12-month warranty, USD 1,500 EXW Shenzhen (snapshot 2026-10-27, valid 15 days). Also 48 x 25G + 8 x 100G and 32 x 100G in the same family, FCC/CE.

Would you like the datasheets and a reseller price list to see whether the line fits your catalog?

Simon
Saga Telecom - sagatele.com
```

- 备注：不要提 Mellanox 对比价；只给自己的价。
