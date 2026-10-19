# Paragon Networks Ltd

> **评级 B**　|　英国 · London（电话区号 0208）　|　档案编号 `PB-007`　|　优先级 ★　|　状态：00-未触达
>
> **类型**：分销商/电商（网络产品在线经销，PLANET 工业交换机专区）　|　**PLANET 关联**：网店设「Industrial Ethernet Switches by Planet Technology」分类，在售 IGS-801T £85、IGS-620TF £135、WGS-804HP £190　|　结构版本：v2（继承 Mikrotik R56 骨架 · Planet 仓库 2026-10-19 起）

```yaml structured_profile
code: PB-007
rating: B
country: 英国
type: 分销商/电商（网络产品在线经销，PLANET 工业交换机专区）
planet_models: ["IGS-801T", "IGS-620TF", "WGS-804HP"]
p1: STI-288GP
price_tier: 20%
stage: 00-未触达
mikrotik_ref: none
updated: 2026-10-19
```

## SALES BRIEF（压缩模型）

- **是谁**：伦敦小型网络产品电商，PLANET 工业交换机专区
- **为什么值得跟**：需求面：PLANET 工业交换机专区在售（商品页级）；触达：enquiries@paragonnetworks.co.uk 通用邮箱；体量小；无具名人 → B
- **P1（首触唯一主推）**：STI-288GP — 对位其在售 WGS-804HP（8 口含 4 PoE 壁挂）与 IGS-801T（工业 8 口）之间的工业 8 口 PoE 非管理机，20% 档 $57.4；$57.4 USD EXW（20% 档，SmartByte LT-IS3010GP-2GX8GT 320 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：Of the PLANET industrial switches you list, which one sells most, and what landed price would make a 3-year-warranty alternative worth listing?
- **最大未知**：采购决策人与年用量未确认；现用 PLANET 型号的毛利与断货痛点未确认
- **下一步**：未触达；按本档首触邮件由用户在仓库外发出，回复后更新本档

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Paragon Networks Ltd | 事实（网页自述） |
| 国家/城市 | 英国 / London（电话区号 0208） | 事实 |
| 网站 | paragonnetworks.co.uk | 事实 |
| 类型 | 分销商/电商（网络产品在线经销，PLANET 工业交换机专区） | 事实（厂商/官网口径） |
| PLANET 关联 | 网店设「Industrial Ethernet Switches by Planet Technology」分类，在售 IGS-801T £85、IGS-620TF £135、WGS-804HP £190 | 事实（见下节证据） |
| 自有品牌 | 否 | 事实 |

## PLANET 关联证据（原文 + URL + 抓取日期）

- **【卖方目录】PLANET 工业交换机专区与三款在售价格**
  > Call +44 0208 906 6816 Email enquiries@paragonnetworks.co.uk … £85.00 IGS-801T - Planet Industrial 8-Port 10/100/1000Mbps Gigabit Ethernet Switch … £135.00 IGS-620TF … £190.00 WGS-804HP
  > 来源：https://www.paragonnetworks.co.uk/shop/industrial-ethernet-switches-360-c（抓取 2026-10-19）

## 在卖/在用 PLANET 型号 → Saga 对位

| PLANET 型号（证据所见） | Saga 对位 | 说明 |
|---|---|---|
| IGS-801T | STI-080GE | 工业 8×GE 非管理，-40~75°C |
| IGS-620TF | STI-240GE | 工业 4×GE + 2 SFP 非管理 |
| WGS-804HP | STI-088GP（近似） | PLANET 为 8 口含 4 PoE 壁挂；Saga 为 8 口全 PoE |

## 需求与场景（推断标签）

- PoE 接入供电（安防/AP）；工业/宽温 DIN；万兆上行（【推断】依据在卖品类）

## 联系方式（已有/猜测分标）

- **—（咨询）**（enquiries）：enquiries@paragonnetworks.co.uk / +44 208 906 6816 〔公开（网店页眉）；源：https://www.paragonnetworks.co.uk/shop/industrial-ethernet-switches-360-c〕
- **邮箱纪律**：只记公开找到的地址；未做 SMTP 验证（不可验），MX 状态：未查。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288GP），备选型不进邮件。

### 第 1 次跟进 · 第二货源/贴牌试探

- **推什么**：STI-288GP
- **切入点**：英国小型网络电商，PLANET 工业线有专区 → 工业非管理/壁挂 PoE 小盒的第二货源，价格战优势明显
- **要问的问题**：Of the PLANET industrial switches you list, which one sells most, and what landed price would make a 3-year-warranty alternative worth listing?
- **随附/动作**：无附件；规格页链接一条

### 第 2 次跟进 · 样机

- **推什么**：STI-288GP（1 台）
- **切入点**：30 天并行测试，不要求承诺
- **要问的问题**：Which site/customer would you test it on?
- **随附/动作**：L2+ 特性表 1 页（ERPS/QinQ/IGMP/PoE watchdog）

### 第 3 次跟进 · 贴牌与批量

- **推什么**：STI-288GP + 贴牌方案
- **切入点**：中性包装、客户型号、固件 UI 定制
- **要问的问题**：What MOQ and label format would make sense for a first run?
- **随附/动作**：贴牌流程 1 页；报价前核价

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-288GP | 主场景 | $57.4 USD EXW（20% 档，SmartByte LT-IS3010GP-2GX8GT 320 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 对位其在售 WGS-804HP（8 口含 4 PoE 壁挂）与 IGS-801T（工业 8 口）之间的工业 8 口 PoE 非管理机，20% 档 $57.4；档位 20%：电商 → 20% |

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

- [ ] 法人全名与规模（Companies House 待核）
- [ ] 采购负责人
- [ ] 年走量

## 首触邮件（英文样板 · 可直接发送）

**主题**：Industrial 8-port PoE switch, 3-year warranty, second source for your PLANET range

```text
Hi —（咨询）,

You carry PLANET PoE switches in 英国, so your customers already accept Taiwan-grade pricing and lead times.

We build Marvell-based L2+ PoE switches (ERPS <20 ms ring, IGMP snooping, 802.1Q/QinQ, PoE watchdog, CLI/SNMP) that fit the same slot as the PLANET GS-4210/GS-5220 class at a lower landed cost, and we can ship under your own label with neutral packaging. The unit I would start with for your line is STI-288GP at $57.4 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Of the PLANET industrial switches you list, which one sells most, and what landed price would make a 3-year-warranty alternative worth listing?

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

*建档日期：2026-10-19　|　入库批次：2026-10-19_W01_官方分销与品牌页_DE-IT-FR-ES-PL-UK-US　|　原始证据：batch/2026-10-19_W01_官方分销与品牌页_DE-IT-FR-ES-PL-UK-US.json　|　渲染：scripts/render.py 2026-10-19*
