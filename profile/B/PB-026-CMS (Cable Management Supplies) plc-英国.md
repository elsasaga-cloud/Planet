# CMS (Cable Management Supplies) plc

> **评级 B**　|　英国 · Crawley, West Sussex（原 Farnborough）　|　档案编号 `PB-026`　|　优先级 ★★☆　|　状态：00-未触达
>
> **类型**：分销商（1993 年起；布线基础设施、网络、IP 物理安防与 AV 产品分销；约 15 人；现为 Norbain SD 旗下——「Norbain Holdings Ltd T/A CMSPLC」）　|　**PLANET 关联**：官网品牌页「PLANET TECHNOLOGY CORPORATION」在售 FNSW-2401 / FNSW-1601 / GSD-503 / FT-802；Switching & Networking 页品牌为 Allied Telesis / Antiference / Netgear / Planet　|　结构版本：v2（继承 Mikrotik R56 骨架 · Planet 仓库 2026-10-19 起）

```yaml structured_profile
code: PB-026
rating: B
country: 英国
type: 分销商（1993 年起；布线基础设施、网络、IP 物理安防与 AV 产品分销；约 15 人；现为 Norbain SD 旗下——「Norbain Holdings Ltd T/A CMSPLC」）
planet_models: ["FNSW-2401", "FNSW-1601", "GSD-503", "FT-802"]
p1: STC-424DGGPM-280W
price_tier: 20%
stage: 00-未触达
mikrotik_ref: none
updated: 2026-10-20
```

## SALES BRIEF（压缩模型）

- **是谁**：英国南部的布线/安防/AV 小分销，Norbain 旗下，PLANET 低端非管理交换机在售
- **为什么值得跟**：需求：PLANET 低端在售 + IP 安防/布线渠道；触达：sales@cmsplc.com 公开（官网 + Allied Telesis 伙伴页）；体量 15 人（PitchBook）可赢，但母公司 Norbain SD 为大分销→集团采购可能上收；B
- **P1（首触唯一主推）**：STC-424DGGPM-280W — 其 IP 物理安防线最缺的是 24 口 PoE 管理型（现有 PLANET 在售仅非管理 FE/GE）；$134.5 USD EXW（20% 档，SmartByte LT-S8328GP-4GX24GT-S 750 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：When installers buy switches for IP cameras from CMS, do they take unmanaged units or ask for a managed PoE+ option you don't currently list?
- **最大未知**：Norbain 集团是否统一采购；年交换机台数
- **下一步**：未触达；按本档首触邮件由用户在仓库外发出，回复后更新本档

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | CMS (Cable Management Supplies) plc | 事实（网页自述） |
| 国家/城市 | 英国 / Crawley, West Sussex（原 Farnborough） | 事实 |
| 网站 | cmsplc.com | 事实 |
| 类型 | 分销商（1993 年起；布线基础设施、网络、IP 物理安防与 AV 产品分销；约 15 人；现为 Norbain SD 旗下——「Norbain Holdings Ltd T/A CMSPLC」） | 事实（厂商/官网口径） |
| PLANET 关联 | 官网品牌页「PLANET TECHNOLOGY CORPORATION」在售 FNSW-2401 / FNSW-1601 / GSD-503 / FT-802；Switching & Networking 页品牌为 Allied Telesis / Antiference / Netgear / Planet | 事实（见下节证据） |
| 自有品牌 | 否 | 事实 |

## PLANET 关联证据（原文 + URL + 抓取日期）

- **【卖方目录】PLANET 品牌页在售**
  > PLANET TECHNOLOGY CORPORATION - 24P 100TX SWITCH … Code: FNSW-2401 In Stock - 5P 1000MBPS GB METAL … Code: GSD-503 … Norbain Holdings Ltd T/A - CMSPLC South Corner, Old Brighton Road, Crawley
  > 来源：https://www.cmsplc.com/brand/planet-technology-corporation（抓取 2026-10-19）
- **【公司自述】联系方式**
  > phone us on 01252 379379 … Email sales@cmsplc.com … Planet Switches
  > 来源：https://www.cmsplc.com/contact（抓取 2026-10-19）
- **【第三方】规模与归属**
  > Year Founded 1993 · Employees 15 · Parent Company Norbain SD · Distributors/Wholesale（PitchBook）
  > 来源：https://pitchbook.com/profiles/company/100254-79（抓取 2026-10-19）
- **【第三方】业务描述**
  > Established in 1993, CMS is one of the UK's largest Distributors of Cabling Infrastructure, Network, IP Physical Security and AV Solutions（LinkedIn）
  > 来源：https://www.linkedin.com/company/cms-plc（抓取 2026-10-19）
- **【第三方】Allied Telesis 伙伴页列 CMS 为 Reseller**
  > CMS (Cable Management Supplies) plc … Email sales@cmsplc.com Tel +44 1252 379379 Organisation Type Reseller
  > 来源：https://www.alliedtelesis.com/us/en/cms-cable-management-supplies-plc（抓取 2021-08-24）

## 在卖/在用 PLANET 型号 → Saga 对位

| PLANET 型号（证据所见） | Saga 对位 | 说明 |
|---|---|---|
| FNSW-2401 | STC-424DGGM | PLANET 为 24 口 FE 非管理；Saga 无 FE 档，以 24×GE 管理型 STC-424DGGM 作升级替代（注明） |
| FNSW-1601 | STC-424DGGPM-280W | 同口数/同上联近似对位，非功能等价 |
| GSD-503 | — | 5 口桌面 GE 非管理：Saga 暂无对应型号 |
| FT-802 | STC-424DGGPM-280W | 同口数/同上联近似对位，非功能等价 |

## 需求与场景（推断标签）

- PoE 接入供电（安防/AP）；万兆上行（【推断】依据在卖品类）

## 联系方式（已有/猜测分标）

- **—（销售）**（sales）：sales@cmsplc.com / +44 1252 379379 〔公开（官网 contact 页 / Allied Telesis 伙伴页）；源：https://www.cmsplc.com/contact〕
- **邮箱纪律**：只记公开找到的地址；未做 SMTP 验证（不可验），MX 状态：未查。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W），备选型不进邮件。

### 第 1 次跟进 · 第二货源/贴牌试探

- **推什么**：STC-424DGGPM-280W
- **切入点**：小型布线+安防分销（15 人）但母公司 Norbain 是英国大安防分销——CMS 自身决策链短；在售 PLANET 为低端非管理，Saga 商用 PoE 可做其「安防 PoE」升级档
- **要问的问题**：When installers buy switches for IP cameras from CMS, do they take unmanaged units or ask for a managed PoE+ option you don't currently list?
- **随附/动作**：无附件；规格页链接一条

### 第 2 次跟进 · 样机

- **推什么**：STC-424DGGPM-280W（1 台）
- **切入点**：30 天并行测试，不要求承诺
- **要问的问题**：Which site/customer would you test it on?
- **随附/动作**：L2+ 特性表 1 页（ERPS/QinQ/IGMP/PoE watchdog）

### 第 3 次跟进 · 贴牌与批量

- **推什么**：STC-424DGGPM-280W + 贴牌方案
- **切入点**：中性包装、客户型号、固件 UI 定制
- **要问的问题**：What MOQ and label format would make sense for a first run?
- **随附/动作**：贴牌流程 1 页；报价前核价

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W | 主场景 | $134.5 USD EXW（20% 档，SmartByte LT-S8328GP-4GX24GT-S 750 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 其 IP 物理安防线最缺的是 24 口 PoE 管理型（现有 PLANET 在售仅非管理 FE/GE）；档位 20%：分销走量 → 20% |
| 备选2 | STC-424DGGM | 24 口 GE 管理非 PoE（对位 FNSW-2401 升级） | $82.5 USD EXW（20% 档，SmartByte LT-S8328G-4GX24GT-S 460 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-28DGGPM | 8 口 PoE+2 SFP | $80.7 USD EXW（20% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

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

## 首触邮件（英文样板 · 可直接发送）

**主题**：Managed 24-port PoE+ to extend your PLANET switch line

```text
Hi there,

Your PLANET range stops at unmanaged FE/GE units; a managed 24-port PoE+ at distributor pricing fills the gap your IP-security installers ask for.

We build Marvell-based L2+ PoE switches (ERPS <20 ms ring, IGMP snooping, 802.1Q/QinQ, PoE watchdog, CLI/SNMP) that fit the same slot as the PLANET GS-4210/GS-5220 class at a lower landed cost, and we can ship under your own label with neutral packaging. The unit I would start with for your line is STC-424DGGPM-280W at $134.5 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: When installers buy switches for IP cameras from CMS, do they take unmanaged units or ask for a managed PoE+ option you don't currently list?

If useful, I can send one unit to your office for a 30-day side-by-side test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
```

> 发送前检查：① 不出现「Made in China」或原产地；② 不承诺未实测指标；③ 落款换成你自己的名字与公司；④ **一次只问一个问题**；⑤ 货币 USD 并带快照日期；⑥ 分销商勿贬低 PLANET，只谈第二货源/贴牌。

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
