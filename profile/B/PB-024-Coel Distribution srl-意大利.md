# Coel Distribution srl

> **评级 B**　|　意大利 · Muggiò (MB)　|　档案编号 `PB-024`　|　优先级 ★★☆　|　状态：00-未触达
>
> **类型**：分销商（1994 年起；结构化布线、网络、电信与连接产品分销，服务安装商与系统集成商；11–50 人，营收 €9.4M 2023）　|　**PLANET 关联**：官网品牌页「Planet Networking」+ 产品页 IGS-801T（COD. COEL PLT0086）、WGS-803、WGS-5225-8T2SV 在售；首页品牌墙列 Planet Networking　|　结构版本：v2（继承 Mikrotik R56 骨架 · Planet 仓库 2026-10-19 起）
>
> ⚠️ **Mikrotik 仓库已有档案 A-191**：本档只补 PLANET 侧证据；联系策略以先建档案为准，勿重复首触。

```yaml structured_profile
code: PB-024
rating: B
country: 意大利
type: 分销商（1994 年起；结构化布线、网络、电信与连接产品分销，服务安装商与系统集成商；11–50 人，营收 €9.4M 2023）
planet_models: ["IGS-801T", "WGS-803", "WGS-5225-8T2SV", "IGS-614HPT（品牌页 4 PoE+2 SFP）"]
p1: STI-288DGGPM
price_tier: 20%
stage: 00-未触达
mikrotik_ref: A-191
updated: 2026-10-20
```

## SALES BRIEF（压缩模型）

- **是谁**：米兰北郊的布线+网络分销商，给安装商/集成商供货，PLANET 工业小交换机在其目录中有自有货号
- **为什么值得跟**：需求：PLANET 工业线在售 + 布线/网络分销渠道；触达：info@coeldistribution.it（官网 contattaci）；体量 11–50 人、€9.4M，可赢；Mikrotik 仓库 A-191 已建档 → 本仓 B 并档，首触以 Mikrotik 仓库为准
- **P1（首触唯一主推）**：STI-288DGGPM — 其在售 WGS-5225-8T2SV / IGS-801T 属 8 口工业档；Saga 工业 8 口 PoE L2+ 为同价位带的上位替代；$139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：Do your installers take the PLANET industrial 8-port units mainly unmanaged (IGS-801T) or managed (WGS-5225)?
- **最大未知**：Mikrotik 侧是否已首触（A-191 状态未触达）；PLANET 占比
- **下一步**：未触达；按本档首触邮件由用户在仓库外发出，回复后更新本档

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Coel Distribution srl | 事实（网页自述） |
| 国家/城市 | 意大利 / Muggiò (MB) | 事实 |
| 网站 | coeldistribution.it | 事实 |
| 类型 | 分销商（1994 年起；结构化布线、网络、电信与连接产品分销，服务安装商与系统集成商；11–50 人，营收 €9.4M 2023） | 事实（厂商/官网口径） |
| PLANET 关联 | 官网品牌页「Planet Networking」+ 产品页 IGS-801T（COD. COEL PLT0086）、WGS-803、WGS-5225-8T2SV 在售；首页品牌墙列 Planet Networking | 事实（见下节证据） |
| 自有品牌 | 否 | 事实 |

## PLANET 关联证据（原文 + URL + 抓取日期）

- **【卖方目录】PLANET 品牌页**
  > Planet Networking … Via Fratelli Bandiera, 9A 20835 Muggiò (MB) Tel. +39 039.578.831
  > 来源：https://www.coeldistribution.it/brands/planet-networking/（抓取 2026-10-19）
- **【卖方目录】IGS-801T 在售（自有货号）**
  > IGS-801T Planet Networking COD. COEL: PLT0086 PRODUTTORE: IGS-801T … Industriale
  > 来源：https://www.coeldistribution.it/igs-801t/（抓取 2025-10-18）
- **【公司自述】联系方式与法人**
  > Coel Distribution srl +39 039 578 831 … Email: info@coeldistribution.it C.F. e P. IVA: 11989650152
  > 来源：https://www.coeldistribution.it/contattaci/（抓取 2024-12-04）
- **【第三方】规模、成立、客户群**
  > Dimensioni dell'azienda: 11-50 dipendenti · Sede principale: Muggiò · Data di fondazione: 1994（LinkedIn）；reportaziende：Fatturato 2023: € 9.413.657
  > 来源：https://www.reportaziende.it/coel_distribution_srl_mb_11989650152（抓取 2026-10-19）
- **【Mikrotik 仓库】A-191 同户（人工 A，info@ 公开）**
  > A-191 Coel Distribution srl 意大利 集成商/代理（Allied Telesis）… info@coeldistribution.it [Publicly listed; delivery not tested]
  > 来源：https://github.com/SimonSaga-202306/mikrotik-info/blob/arena/01a0c3ef-mikrotik-info/客户名单_反向信号_2026-09.csv（抓取 2026-10-19）

## 在卖/在用 PLANET 型号 → Saga 对位

| PLANET 型号（证据所见） | Saga 对位 | 说明 |
|---|---|---|
| IGS-801T | STI-080GE | 8×GE 工业非管理（Saga 暂无对应型号，沿用 SmartByte 型号 STI-080GE） |
| WGS-803 | STI-288DGGPM | 同口数/同上联近似对位，非功能等价 |
| WGS-5225-8T2SV | STI-288DGGPM | PLANET 为 8GE+2SFP 壁挂管理型（非 PoE）；Saga 以 8 口 PoE L2+ 工业覆盖并带 PoE |
| IGS-614HPT（品牌页 4 PoE+2 SFP） | STI-288DGGPM | 同口数/同上联近似对位，非功能等价 |

## 需求与场景（推断标签）

- PoE 接入供电（安防/AP）；工业/宽温 DIN；万兆上行（【推断】依据在卖品类）

## 联系方式（已有/猜测分标）

- **—（总机）**（info）：info@coeldistribution.it / +39 039 578 831 〔公开（官网 contattaci 页）；源：https://www.coeldistribution.it/contattaci/〕
- **邮箱纪律**：只记公开找到的地址；未做 SMTP 验证（不可验），MX 状态：未查。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> ⚠ 并档户（Mikrotik **A-191**）：首触由 Mikrotik 仓库发出，下列台阶仅为 PLANET 线对位**预案**，**启动时点 = Mikrotik 侧回复后再定**；本仓不按自己的节奏发第 1 封。全程只推 P1（STI-288DGGPM），备选型不进邮件。

### 第 1 次跟进 · Mikrotik 侧回复后再定 · PLANET 线对位

- **推什么**：STI-288DGGPM
- **切入点**：Mikrotik 仓库 A-191（人工 A，info@）同户——本仓只补 PLANET 侧证据并并档，不重复首触；其 PLANET 在售偏工业非管理（IGS-801T/WGS-803）→ Saga 工业线可对位
- **要问的问题**：Do your installers take the PLANET industrial 8-port units mainly unmanaged (IGS-801T) or managed (WGS-5225)?
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
| **P1（首触唯一）** | STI-288DGGPM | 主场景 | $139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 其在售 WGS-5225-8T2SV / IGS-801T 属 8 口工业档；Saga 工业 8 口 PoE L2+ 为同价位带的上位替代；档位 20%：分销走量 → 20% |
| 备选2 | STI-080GE | 工业 8 口非 PoE（对位 IGS-801T） | $31.4 USD EXW（20% 档，SmartByte LT-IS3008G-8GT 175 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-424DGGPM-280W | 商用 24 口 PoE 项目 | $134.5 USD EXW（20% 档，SmartByte LT-S8328GP-4GX24GT-S 750 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

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

> 本户 = Mikrotik 仓库 **A-191**，按《客户分级与去重规则》§4 与 T06 裁决，首触只发一次、以 Mikrotik 仓库为准。本档只提供 PLANET 侧证据与对位（P1 STI-288DGGPM，$139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价））。Mikrotik 侧首触有回复且涉及 PLANET 线时，再据本档补一封对位邮件；届时话术另写，不用通用样板。

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
