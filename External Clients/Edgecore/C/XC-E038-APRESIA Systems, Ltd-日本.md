# XC-E038 · APRESIA Systems, Ltd. · 日本

> **初判 XC 暂不管** ｜ 来源 Edgecore `C-003`（原评级 C，阶段 01-blocked-unverified） ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）

## 1. 初判与理由
- 初判：**XC** — 品牌原厂 / 供应商 / 同行，不是买家
- 标记：原厂或同行
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | APRESIA Systems, Ltd. |
| 国家 / 城市 | 日本 |
| ISO | JP |
| 网站 | https://www.apresiasystems.co.jp/ |
| 类型 / 角色 | 自有品牌网络设备制造商 |
| 细分（来源库） | generic |
| 他们首推（仅参考，不照搬） | — |
| 来源文件 | `profile/C/C-003-APRESIA-Systems-Ltd-日本.md` @ elsasaga-cloud/Edgecore@729187d (arena/6214ebb8-edgecore)（更新 2026-10-27） |

## 3. 联系方式
- 邮箱：yamada.taro@apresiasystems.co.jp（首选）
- 电话：+81-3-6369-0400（内部用，不进外发材料）

来源库「联系方式」段原文：

> - **电话**：+81-3-6369-0400（官网总部总机）；03-6369-0401（2026-10-18名录历史快照）
> - **邮箱**：未取得公开采购邮箱；用户试发的`yamada.taro@apresiasystems.co.jp`未经仓库核验且已被拦截，不作联系方式，禁止继续拼个人变体。
> - **官网/表单**：https://www.apresiasystems.co.jp/ ；产品门户https://www.apresia.jp/ ；英文Contact Us表单https://www.apresia.jp/form/inquiry_en.php?type=19

## 4. 关键人（KP）
> - **最高负责人已确认**：Masahiko Suenaga（末永 正彦），President & CEO（官网公司概要）。产品/采购KP仍未定位；总裁与Hirokawa、Koji Hirono等技术活动人员均不自动升格为采购KP。

## 5. 证据与来源 URL（来源库）
- 无

> - `Edgecore客户数据库.py`：APRESIA Systems, Ltd.的Tokyo地址与电话；文件自述采集时间为2026-10-18 17:30。
> - 旧`profile/C/C-003-日本商社群体-日本.md`（R17终局已删除，删除前基线`173faaf`）：分销/自有品牌、OEM目标及日本认证门槛标注。
> - `docs/product/认证需求速查.md`：日本PSE/VCCI与持证路径核验要求。

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱
- 来源库核验 / 退信摘录：
  - R17终局复核与保留裁决（2026-10-19）
    - - **KP/邮箱口径**：产品/采购KP和公开邮箱仍未定位。公开标准会议名单中的技术参会者不升格为采购KP，个人邮箱不按域名拼造。
  - R23 存量客户全量加厚（2026-10-25）
    - - **域名与托管指纹**：主域`apresiasystems.co.jp`为A与MX均存在；网站IPv4 `49.212.198.11`（AS9371 SAKURA-C - SAKURA Internet Inc., JP），未见AAAA；邮件入口 `apresiasystems-co-jp.mail.protection.outlook.com`（平台特征：Microsoft 365）；NS托管特征为Amazon Route 53。
    - - **邮件认证与发信系统信号**：SPF已发布（Microsoft 365、日本邮件服务商、ShareStage、Satori Mail、Salesforce，结尾`~all`）；DMARC `p=none`。SPF include只说明该域授权过的发信系统，不证明采购量或具体邮箱可投递。
    - - **关联/候选域状态**：`apresia.jp`=A-noMX（无公开MX）。关联域均按档内上下文人工保留，未经主体归属再核者不据此新增联系方式。
    - - **官网公司概要定版**：APRESIA Systems官网确认公司2016-09-08设立，总部为Tokyo、Chuo-ku、Tsukiji 2-3-4（Metro City Tsukiji Shintomicho Bldg. 8F），总机+81-3-6369-0400，President & CEO为Takeshi Yamada，资本金3.10亿日元（2022-06-01口径），员工350名（2026-03-31口径）；业务为信息系统硬件/软件的制造、编程、销售与维护。2020年由ORIX接管、2022年设台湾代表处。旧名录电话03-6369-0401与官网总机末位不同，现以官网040
    - - **产品与联系路径定版**：官网Our Business明确其开发和制造以太网交换机与光传输设备，覆盖SOHO、企业至大型运营商，并提供最长10年延保/24×7支持；这闭合“自有交换设备厂商”属性，但350人、自研自产及ORIX旗下属性同时意味着外部OEM空间仍须单独证明。官网Contact Us指向`apresia.jp`英文询盘表单，未公开采购邮箱。P4 Workshop 2019的Hirokawa、公开代码中的Koji Hirono仅为技术活动证据；President Takeshi Yamada亦不等于采购KP。来源：https://www.apresiasystems.co.jp
    - - **最新回执收口**：用户2026-10-25转来`yamada.taro@apresiasystems.co.jp`“Message blocked”。该址此前未在仓库核验，GitHub精确代码检索为0；被拦截不证明邮箱不存在、人员离职或其为采购人。停止个人地址变体，后续只经官网表单/总机确认采购接口。
    - - **跟进与证据边界**：用户已表示存量客户基本完成一轮跟进；未逐档回传送达/回复结果的，本轮不虚构已送达和已回复。DNS为2026-10-25经8.8.8.8查询快照，结构化底稿见`batch/contact_research-2026-10-25_R23_存量客户全量加厚.json`。Agent不发信。
  - R24 质量复核与纠错加厚（2026-10-25）
    - - **R24 前质量快照**：实质行 54、跨档出现 ≤3 档的专属行 52、≤10 档的稀有行 52、外链来源域 3 个、全档去重邮箱 1 个；启发式审计分 63/100（主体 15/15、联系 3/20、KP 8/15、业务专属度 15/20、证据 14/20、可执行性 8/10、风险扣分 0）。该分只用于找薄弱档，不证明每条历史事实都正确。
    - - **联系/KP 定版**：首选邮箱为 无已确认可执行的公开商务首选邮箱（状态 `no_public_business_email_located`）；KP 状态 `named_executive_only_procurement_kp_not_located`，结构化抽到：Takeshi Yamada。自动抽取不替代原文的来源、日期和限定语；个人邮箱仅在公开披露且主体一致时保留。
    - - **外部事实边界**：本档本轮没有新增可核验的外部公司事实；既有官网、厂商名录、登记、新闻稿和第三方材料继续按原段来源与日期分层。R23 的 DNS/GitHub 只证明基础设施或技术活动，不证明采购量、人员在职或交易意愿。
    - - **未闭合项**：公开可执行商务邮箱未闭合；最高负责人已实名，但采购执行人未闭合；现行采购型号、月量和认证要求未由客户确认。
    - - **下一证据路径**：停止个人邮箱变体；经官网 Contact Us 表单或总机确认采购接口，并核 OEM 空间与 PSE/VCCI 责任。
    - - **证据纪律**：未核实内容不得拼造邮箱、人物、职务或交易关系；第三方员工/营收估算只作单源线索，官网自述与审计/登记事实分开；用户“基本跟进完了”仍不转写为逐档已送达或已回复。Agent 不发信。
  - R25 运营化加厚与定向复核（2026-10-27）
    - - **适配与证据坐标**：R24 证据完整度 C、质量基线 63/100、专属行 56（专属证据密度强）；联系状态 `no_public_business_email_located`，主口 `无已确认公开商务首选邮箱`；KP 状态 `named_executive_only_procurement_kp_not_located`。档内最晚显式日期 2026-10-25 只作时间坐标，不等于证据发布日期或在职证明。
    - - **触达顺序与停发规则**：先经表单/总机索取商务口与实名负责人。下一证据路径：只经官网英文表单或总机确认采购接口、是否存在外部 OEM/ODM 及 PSE/VCCI 持证责任；停止个人邮箱变体，总裁不作采购 KP。 Agent 不发信、不排期；若主口已拦截/失败，不原样重发或并行轰炸人事、支持、财务口。
    - - **风险与未闭合项**：风险标志：无 R24 已登记的专项风险（不等于无交易风险）。未闭合：公开可执行商务邮箱未闭合；最高负责人已实名，但采购执行人未闭合；现行采购型号、月量和认证要求未由客户确认。
    - - **定向外部补挖**：**最高负责人纠错**：APRESIA Systems 官网英文 About 与日文公司信息现行页面均列 President / 代表取締役社長为 **Masahiko Suenaga（末永 正彦）**，不是档内 R23/R24 所写 Takeshi Yamada；本轮已纠正档首与 KP 段。此前被拦截的 `yamada.taro@...` 本就未经公开来源核验，与总裁姓名亦无可证关系，继续禁止个人邮箱变体。来源：https://www.apresiasystems.co.jp/english/aboutus.html 与 https://www.apresiasys
    - - **定向外部补挖**：官网 News 2026 年仍持续发布新品：2 月 NP2200 系列 L2 交换机、7 月多千兆 60W 供电智能 L2、9–10 月 KOKOMO 网关与 AN-ManagerStation sFlow 选项，证明自有交换/网络产品线正在更新，不支持“产品已停”的假设。联系页仍只有表单，未公开采购邮箱。下一步只能经英文询盘表单或总机确认外部 OEM/ODM 是否存在、采购接口及 PSE/VCCI 持证责任；总裁不升格为采购 KP。来源：https://www.apresia.jp/news/ 与 https://www.apresia.jp/form/inquir
    - - **R25结论边界**：运营化条目是基于档内既有证据与本轮定向来源的工作框架，不证明现行采购意愿、人员在职、邮箱可投递或订单量；新增外部事实只以本段逐项来源与限定语为准。

## 7. 我方产品线提示
- OEM / 贴牌 + 低价标品（Edgecore 渠道已习惯白牌/开放网络，拿价格与贴牌能力切）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
