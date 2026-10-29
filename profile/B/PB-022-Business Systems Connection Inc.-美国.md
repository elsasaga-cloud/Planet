# Business Systems Connection Inc.

> **评级 B**　|　美国 · Fenton, MO　|　档案编号 `PB-022`　|　优先级 ★★☆　|　状态：10-已触达(S邮箱 去1·0回复)
>
> **类型**：分销商（WISP/网络分销：Ubiquiti / MikroTik / Cambium / PLANET，1997 年起，2–10 人）+ 自有品牌 Lysora　|　**PLANET 关联**：在售 PLANET GS-4210-24P4C（$522）、IGS-5225-8P4S-12V（$809.60）、IGS-4215-8P2T2S；DigiKey 市场卖家　|　结构版本：v2（继承 Mikrotik R56 骨架 · Planet 仓库 2026-10-19 起）
>
> ⚠️ **Mikrotik 仓库已有档案 A-532**：本档只补 PLANET 侧证据；联系策略以先建档案为准，勿重复首触。
>
> **C 池三闸筛选（Planet 仓同法，`data/sieve_planet.json`）：留 Planet 仓原档（只巡检不入池）**（随 `SB-1013`）（闸 0 · DUP-AB · 2026-10-29）：与 SB-1013（Saga B 级，本轮不筛 A/B）同一公司（同域名 bizsyscon.com）→ 随主档，不单独判；A/B 升级讨论时一并

```yaml structured_profile
code: PB-022
rating: B
country: 美国
type: 分销商（WISP/网络分销：Ubiquiti / MikroTik / Cambium / PLANET，1997 年起，2–10 人）+ 自有品牌 Lysora
planet_models: ["GS-4210-24P4C", "IGS-5225-8P4S-12V", "IGS-4215-8P2T2S"]
p1: STI-488DGGPM
price_tier: 20%
stage: 10-已触达(S邮箱 去1·0回复)
mikrotik_ref: A-532
updated: 2026-10-29
```

## SALES BRIEF（压缩模型）

- **是谁**：圣路易斯郊区的微型 WISP 分销商，自有品牌 Lysora，PLANET 是其工业 PoE 货源之一
- **为什么值得跟**：需求：PLANET + 自有品牌；触达 sales@ 通用（具名 Joseph Barros / James Shaw / Nijaz Mustedanagic 邮箱被遮蔽）；体量微型；Mikrotik A-532 同户——本仓不重复首触，B 并档
- **P1（首触唯一主推）**：STI-488DGGPM — 同位其在售 IGS-5225-8P4S（工业 8 PoE + 4 SFP）；$147.1 USD EXW（20% 档，SmartByte LT-IS6312GP-4GX8GT 820 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：Which Lysora or PLANET industrial PoE size do your WISP customers take most, 8+4 SFP or 8+2?
- **最大未知**：Mikrotik 侧是否已首触及结果；Lysora 现有 ODM
- **下一步**：并档户：首触由 Mikrotik 仓库（A-532）发出，本仓不发；Mikrotik 侧有回复且涉及 PLANET 线时，再据本档补一封对位邮件

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Business Systems Connection Inc. | 事实（网页自述） |
| 国家/城市 | 美国 / Fenton, MO | 事实 |
| 网站 | bizsyscon.com | 事实 |
| 类型 | 分销商（WISP/网络分销：Ubiquiti / MikroTik / Cambium / PLANET，1997 年起，2–10 人）+ 自有品牌 Lysora | 事实（厂商/官网口径） |
| PLANET 关联 | 在售 PLANET GS-4210-24P4C（$522）、IGS-5225-8P4S-12V（$809.60）、IGS-4215-8P2T2S；DigiKey 市场卖家 | 事实（见下节证据） |
| 自有品牌 | 是（Lysora） | 事实 |

## PLANET 关联证据（原文 + URL + 抓取日期）

- **【卖方目录】PLANET 商用与工业 PoE 在售**
  > GS-4210-24P4C $522 … IGS-5225-8P4S-12V $809.60（商品页，检索摘要）
  > 来源：https://www.bizsyscon.com/（抓取 2026-10-19）
- **【Mikrotik 仓库】A-532（人工定级 A，sales@bizsyscon.com，自有品牌 Lysora）**
  > 客户名单_反向信号_2026-09.csv 行 A-532
  > 来源：https://github.com/SimonSaga-202306/mikrotik-info/blob/arena/01a0c3ef-mikrotik-info/客户名单_反向信号_2026-09.csv（抓取 2026-10-19）

## 在卖/在用 PLANET 型号 → Saga 对位

| PLANET 型号（证据所见） | Saga 对位 | 说明 |
|---|---|---|
| GS-4210-24P4C | STC-424DGGPM-280W | 24 PoE |
| IGS-5225-8P4S-12V | STI-488DGGPM | 工业 8 PoE + 4 SFP（PLANET 为 12V 升压版，Saga 需核 12V 输入） |
| IGS-4215-8P2T2S | STI-288DGGPM | 8 PoE + 2 SFP |

## 需求与场景（推断标签）

- PoE 接入供电（安防/AP）；工业/宽温 DIN（【推断】依据在卖品类）

## 联系方式（已有/猜测分标）

- **Joseph Barros**（（名录口径，角色待核））：— / 636-600-1400 〔具名无公开直邮（遮蔽，不猜）；源：名录摘要〕
- **—（销售）**（sales）：sales@bizsyscon.com / 636-600-1400 〔公开（官网）；Mikrotik 仓库 A-532 已记录；源：https://www.bizsyscon.com/〕
- **邮箱纪律**：只记公开找到的地址；未做 SMTP 验证（不可验），MX 状态：未查。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> ⚠ 并档户（Mikrotik **A-532**）：首触由 Mikrotik 仓库发出，下列台阶仅为 PLANET 线对位**预案**，**启动时点 = Mikrotik 侧回复后再定**；本仓不按自己的节奏发第 1 封。全程只推 P1（STI-488DGGPM），备选型不进邮件。

### 第 1 次跟进 · Mikrotik 侧回复后再定 · PLANET 线对位

- **推什么**：STI-488DGGPM
- **切入点**：自有品牌 Lysora 已是贴牌货（NSI 加拿大也分销 Lysora）→ OEM 对象；Mikrotik 仓库 A-532 已记录 sales@bizsyscon.com，勿重复首触
- **要问的问题**：Which Lysora or PLANET industrial PoE size do your WISP customers take most, 8+4 SFP or 8+2?
- **随附/动作**：无附件；规格页链接一条

### 第 2 次跟进 · 样机

- **推什么**：STI-488DGGPM（1 台）
- **切入点**：30 天并行测试，不要求承诺
- **要问的问题**：Which site/customer would you test it on?
- **随附/动作**：L2+ 特性表 1 页（ERPS/QinQ/IGMP/PoE watchdog）

### 第 3 次跟进 · 贴牌与批量

- **推什么**：STI-488DGGPM + 贴牌方案
- **切入点**：中性包装、客户型号、固件 UI 定制
- **要问的问题**：What MOQ and label format would make sense for a first run?
- **随附/动作**：贴牌流程 1 页；报价前核价

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-488DGGPM | 主场景 | $147.1 USD EXW（20% 档，SmartByte LT-IS6312GP-4GX8GT 820 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 同位其在售 IGS-5225-8P4S（工业 8 PoE + 4 SFP）；档位 20%：分销 20%；Lysora 贴牌另按 30% |
| 备选2 | STI-288DGGPM | 工业 8 PoE + 2 SFP | $139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

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

> 本户 = Mikrotik 仓库 **A-532**，按《客户分级与去重规则》§4 与 T06 裁决，首触只发一次、以 Mikrotik 仓库为准。本档只提供 PLANET 侧证据与对位（P1 STI-488DGGPM，$147.1 USD EXW（20% 档，SmartByte LT-IS6312GP-4GX8GT 820 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价））。Mikrotik 侧首触有回复且涉及 PLANET 线时，再据本档补一封对位邮件；届时话术另写，不用通用样板。

## 跟进记录

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 首次触达前留空；用户在仓库外发出邮件后告诉我日期与渠道，我来更新本档并重评 stage。

## 下次复核

- 首触发出后 **14 天**无回复 → 复核是否降频；有任何回复 → 当即重评 stage 与评级。
- 报价纪律：价格为 USD EXW 快照（汇率 2026-10-17），过窗先核价再报价。

---

*建档日期：2026-10-19　|　入库批次：2026-10-19_W02_品牌页与型号反查_EU-UK-CZ-IT-HU-CA-US　|　原始证据：batch/2026-10-19_W02_品牌页与型号反查_EU-UK-CZ-IT-HU-CA-US.json　|　渲染：scripts/render.py 2026-10-29*
