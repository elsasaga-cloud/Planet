# Connect Data – Sintel (Connect Data SARL)

> **评级 B**　|　法国 · Bièvres (91)　|　档案编号 `PB-030`　|　优先级 ★★☆　|　状态：00-未触达
>
> **类型**：分销商（1981 年起；面向运营商/集成商/经销商的电信与网络方案分销：Perle、PLANET、RAD、Radwin、Ruckus；集团约 20 人、营收约 €15M；OP GLOBE 集团成员）　|　**PLANET 关联**：官网品牌页 PLANET：「gamme complète de switchs et convertisseurs Ethernet pour les environnements industriels … complément de gamme idéal pour les produits radio Radwin, CommScope Ruckus」　|　结构版本：v2（继承 Mikrotik R56 骨架 · Planet 仓库 2026-10-19 起）
>
> ⚠️ **Mikrotik 仓库已有档案 A-254**：本档只补 PLANET 侧证据；联系策略以先建档案为准，勿重复首触。

```yaml structured_profile
code: PB-030
rating: B
country: 法国
type: 分销商（1981 年起；面向运营商/集成商/经销商的电信与网络方案分销：Perle、PLANET、RAD、Radwin、Ruckus；集团约 20 人、营收约 €15M；OP GLOBE 集团成员）
planet_models: ["PLANET 工业交换机与介质转换器（品牌页）"]
p1: STI-288DGGPM
price_tier: 20%
stage: 00-未触达
mikrotik_ref: A-254
updated: 2026-10-20
```

## SALES BRIEF（压缩模型）

- **是谁**：巴黎南郊的电信/网络分销商，给运营商和集成商配 Radwin/Ruckus 无线与 Perle/PLANET 工业交换机
- **为什么值得跟**：需求：PLANET 工业线作为无线配套在售 + 运营商/集成商渠道；触达：sales@connectdata.fr 公开（官网 contact，[at] 还原与 mailto 一致）；体量 20 人、€15M 可赢；Mikrotik 仓库 A-254 已建档 → 本仓 B 并档
- **P1（首触唯一主推）**：STI-288DGGPM — PLANET 在其目录是 Radwin/Ruckus 无线配套的工业交换机 → 工业 8 口 PoE 对位；$139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：For Radwin/Ruckus deployments, do your integrators take PLANET's 8-port industrial PoE+ most, or the 4-port compact units?
- **最大未知**：Mikrotik 侧是否已首触（A-254 未触达）；Perle 与 PLANET 的分工
- **下一步**：未触达；按本档首触邮件由用户在仓库外发出，回复后更新本档

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Connect Data – Sintel (Connect Data SARL) | 事实（网页自述） |
| 国家/城市 | 法国 / Bièvres (91) | 事实 |
| 网站 | connectdata.fr | 事实 |
| 类型 | 分销商（1981 年起；面向运营商/集成商/经销商的电信与网络方案分销：Perle、PLANET、RAD、Radwin、Ruckus；集团约 20 人、营收约 €15M；OP GLOBE 集团成员） | 事实（厂商/官网口径） |
| PLANET 关联 | 官网品牌页 PLANET：「gamme complète de switchs et convertisseurs Ethernet pour les environnements industriels … complément de gamme idéal pour les produits radio Radwin, CommScope Ruckus」 | 事实（见下节证据） |
| 自有品牌 | 否 | 事实 |

## PLANET 关联证据（原文 + URL + 抓取日期）

- **【卖方目录】PLANET 品牌页：工业交换机补位**
  > Connect data propose une gamme complète de switchs et convertisseurs Ethernet pour les environnements industriels. Les switchs Planet sont un complément de gamme idéal pour les produits radio Radwin, CommScope Ruckus.
  > 来源：https://www.connectdata.fr/marque/planet/（抓取 2026-03-10）
- **【公司自述】规模、营收、品牌组合、集团**
  > Notre groupe CONNECT DATA – SINTEL emploie une vingtaine de personnes et réalise un CA d'environ 15 millions d'euros … LES MARQUES CONNECT DATA PERLE PLANET QU WIRELESS RAD RADWIN RUCKUS NETWORKS … Le groupe OP GLOBE est constitué de 10 PME
  > 来源：https://www.connectdata.fr/societe/（抓取 2026-06-30）
- **【公司自述】联系方式**
  > Demande de devis sales[at]connectdata.fr sales[at]sintel.fr +33 1 60 13 70 10 … Route de Gisy, Parc Burospace 21 91570 BIEVRES
  > 来源：http://www.connectdata.fr/contact/（抓取 2026-06-30）
- **【Mikrotik 仓库】A-254 同户（A，Perle 授权分销）**
  > A-254 Connect Data 法国 Bievres 分销/集成商（Perle 授权）… sales@connectdata.fr（官网明确[at]/mailto还原）
  > 来源：https://github.com/SimonSaga-202306/mikrotik-info/blob/arena/01a0c3ef-mikrotik-info/客户名单_反向信号_2026-09.csv（抓取 2026-10-19）

## 在卖/在用 PLANET 型号 → Saga 对位

| PLANET 型号（证据所见） | Saga 对位 | 说明 |
|---|---|---|
| PLANET 工业交换机与介质转换器（品牌页） | STI-288DGGPM | 同口数/同上联近似对位，非功能等价 |

## 需求与场景（推断标签）

- PoE 接入供电（安防/AP）；万兆上行（【推断】依据在卖品类）

## 联系方式（已有/猜测分标）

- **—（销售/询价）**（sales）：sales@connectdata.fr / +33 1 60 13 70 10 〔公开（官网 contact 页，[at] 形式）；源：http://www.connectdata.fr/contact/〕
- **—（ADV）**（Administration des ventes）：adv@connectdata.fr / +33 1 60 13 70 21 〔公开（官网 service-logistique 页，[at] 形式）；源：https://www.connectdata.fr/service/service-logistique/〕
- **邮箱纪律**：只记公开找到的地址；未做 SMTP 验证（不可验），MX 状态：未查。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288DGGPM），备选型不进邮件。

### 第 1 次跟进 · 第二货源/贴牌试探

- **推什么**：STI-288DGGPM
- **切入点**：Mikrotik 仓库 A-254（A，Perle 授权）同户——本仓只补 PLANET 侧证据并并档，不重复首触；其 PLANET 定位为「工业交换机补位」→ Saga 工业线对位
- **要问的问题**：For Radwin/Ruckus deployments, do your integrators take PLANET's 8-port industrial PoE+ most, or the 4-port compact units?
- **随附/动作**：无附件；规格页链接一条

### 第 2 次跟进 · 样机

- **推什么**：STI-288DGGPM（1 台）
- **切入点**：30 天并行测试，不要求承诺
- **要问的问题**：Which site/customer would you test it on?
- **随附/动作**：L2+ 特性表 1 页（ERPS/QinQ/IGMP/PoE watchdog）

### 第 3 次跟进 · 贴牌与批量

- **推什么**：STI-288DGGPM + 贴牌方案
- **切入点**：中性包装、客户型号、固件 UI 定制
- **要问的问题**：What MOQ and label format would make sense for a first run?
- **随附/动作**：贴牌流程 1 页；报价前核价

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288DGGPM | 主场景 | $139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | PLANET 在其目录是 Radwin/Ruckus 无线配套的工业交换机 → 工业 8 口 PoE 对位；档位 20%：分销走量 → 20% |
| 备选2 | STI-488DGGPM | 工业 8 口 PoE + 4 SFP | $147.1 USD EXW（20% 档，SmartByte LT-IS6312GP-4GX8GT 820 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W | 商用 24 口 PoE | $134.5 USD EXW（20% 档，SmartByte LT-S8328GP-4GX24GT-S 750 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率（`docs/rules/报价与型号规则.md`）；Saga 商用线无 802.3bt、无 LCD、无云管理——不对标 PLANET 的 UPoE/LCD/NMS 型号。

## SWOT

- **S**：已在卖台系 PoE 交换机，接受亚洲供货与价位；Saga 可贴牌+功能定制
- **W**：Saga 为贸易商、官网弱、无 UL/bt；需以样机与规格说话
- **O**：PLANET 断货/涨价/型号停产时的第二货源；自有品牌贴牌
- **T**：对 PLANET 忠诚度高；深圳同行低价竞争

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**：PLANET 本身与其关联公司只是信号源；对 PLANET 渠道不贬低 PLANET，只谈「第二货源 / 贴牌 / 功能定制」。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据；Saga 商用线 **无 802.3bt**，不要对标 PLANET 的 bt/UPoE 型号。
4. 不承诺 UL、EN50155、IP67、云管理——Saga 没有。
5. 样机先送测，再谈价格；大集团先问清采购层级。

**停止开发条件（命中任一即停）**：3 次定向触达无任何实质回复；确认现用平台完全满足需求；只愿比价不愿谈场景；决策者确认接触不到；对方书面拒绝。

**本户特别红线**：客户含运营商/公共网络——只谈民用/商用接入层

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（在卖/在用 PoE 交换机） | ✅ |
| 决策人识别 | ✅ |
| 触达通道 | ✅ 有公开邮箱 |
| 现用交换品牌 | ✅ PLANET（证据所见） |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- [ ] 年用量与最常出的 PLANET 型号
- [ ] 是否接受贴牌/第二货源
- [ ] 采购决策人与付款口径
- [ ] 对 bt/LCD/云管理等 Saga 缺口的依赖程度

## 首触邮件：本仓不发（Mikrotik 同户并档）

> 本户 = Mikrotik 仓库 **A-254**，按《客户分级与去重规则》§4 与 T06 裁决，首触只发一次、以 Mikrotik 仓库为准。本档只提供 PLANET 侧证据与对位（P1 STI-288DGGPM，$139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价））。Mikrotik 侧首触有回复且涉及 PLANET 线时，再据本档补一封对位邮件；届时话术另写，不用通用样板。

## 跟进记录

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 首次触达前留空；用户在仓库外发出邮件后告诉我日期与渠道，我来更新本档并重评 stage。

## 下次复核

- 首触发出后 **14 天**无回复 → 复核是否降频；有任何回复 → 当即重评 stage 与评级。
- 报价纪律：价格为 USD EXW 快照（汇率 2026-10-17），过窗先核价再报价。

---

*建档日期：2026-10-19　|　入库批次：2026-10-19_W03_品牌页反查与Mikrotik并档_HU-IT-NO-ES-FI-UK-PL-CA-FR-CZ　|　原始证据：batch/2026-10-19_W03_品牌页反查与Mikrotik并档_HU-IT-NO-ES-FI-UK-PL-CA-FR-CZ.json　|　渲染：scripts/render.py 2026-10-20*
