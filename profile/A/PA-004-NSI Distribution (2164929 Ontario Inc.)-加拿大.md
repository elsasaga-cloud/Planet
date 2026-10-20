# NSI Distribution (2164929 Ontario Inc.)

> **评级 A**　|　加拿大 · Brampton, ON　|　档案编号 `PA-004`　|　优先级 ★★★　|　状态：00-未触达
>
> **类型**：安防分销商（加拿大安防批发，9 个分部）+ 自有品牌（Norelco SafeCam）/自述 OEM 服务　|　**PLANET 关联**：PLANET 品牌页 17 款（GSW-2620HP、8 口 PoE+2 上联、16 口 PoE+2 RJ45+2 SFP、24 口非 PoE 等）；同时分销 Lysora（美国 BSC 的自有品牌）　|　结构版本：v2（继承 Mikrotik R56 骨架 · Planet 仓库 2026-10-19 起）

```yaml structured_profile
code: PA-004
rating: A
country: 加拿大
type: 安防分销商（加拿大安防批发，9 个分部）+ 自有品牌（Norelco SafeCam）/自述 OEM 服务
planet_models: ["GSW-2620HP", "GS-4210-24P4C（8/16/24 口 PoE 系列，品牌页未列全型号）"]
p1: STC-424DGGPM-280W
price_tier: 20%
stage: 00-未触达
mikrotik_ref: none
updated: 2026-10-20
```

## SALES BRIEF（压缩模型）

- **是谁**：多伦多郊区的安防批发商，全国 9 个门店卖摄像机/门禁/网络给安装商；自己已经做贴牌品牌，PLANET 是其 PoE 交换机货源之一
- **为什么值得跟**：需求面：PLANET 品牌页 17 款 PoE 在售 + 已分销两家贴牌品牌；触达：Norm Matinnia 直邮 norm@nsidistribution.com（官网门店页/招聘页公开）；体量：区域安防批发 9 分部，可赢；区域加拿大（一线）
- **P1（首触唯一主推）**：STC-424DGGPM-280W — 对位其在售 GSW-2620HP / GS-4210-24P4C 一档（24×GE PoE+ + 4 上联，280W），是安防批发最走量的尺寸；$134.5 USD EXW（20% 档，SmartByte LT-S8328GP-4GX24GT-S 750 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：Is the 24-port PoE+ with 4 uplinks your highest-volume PLANET SKU across the branches, or do the 8/16-port units move faster?
- **最大未知**：Norelco 现有交换机贴牌来源（是否已有深圳供应商）；9 分部年 PoE 台数
- **下一步**：未触达；按本档首触邮件由用户在仓库外发出，回复后更新本档

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | NSI Distribution (2164929 Ontario Inc.) | 事实（网页自述） |
| 国家/城市 | 加拿大 / Brampton, ON | 事实 |
| 网站 | nsidistribution.com | 事实 |
| 类型 | 安防分销商（加拿大安防批发，9 个分部）+ 自有品牌（Norelco SafeCam）/自述 OEM 服务 | 事实（厂商/官网口径） |
| PLANET 关联 | PLANET 品牌页 17 款（GSW-2620HP、8 口 PoE+2 上联、16 口 PoE+2 RJ45+2 SFP、24 口非 PoE 等）；同时分销 Lysora（美国 BSC 的自有品牌） | 事实（见下节证据） |
| 自有品牌 | 是（Norelco SafeCam；官网自述提供 OEM 设计与制造服务） | 待补证 |
| 法人 | 2164929 Ontario Inc. o/a NSI Distribution | 事实/自述 |
| 分部 | 9（加拿大全境） | 事实/自述 |

## PLANET 关联证据（原文 + URL + 抓取日期）

- **【卖方目录】PLANET 品牌页 17 款在售**
  > Planet Technology #### 17 Products 8 Port Gigabit POE Switch + 2 Uplinks … 16 Port Gigabit POE Switch + 2 RJ45 + 2 SFP … GSW-2620HP
  > 来源：https://www.nsidistribution.com/Brands/Planet-Technology-Corporation（抓取 2026-10-19）
- **【公司自述】自述提供 OEM 设计与制造服务，并有自有品牌 Norelco SafeCam**
  > offers OEM design and manufacturing services（检索摘要，原文页待 fetch 核对）
  > 来源：https://www.nsidistribution.com/（抓取 2026-10-19）
- **【公司自述】Norm Matinnia 直邮在官网公开**
  > norm@nsidistribution.com（门店页与招聘页均列出；招聘页另列 carlo@/paul@/mike@/david@）
  > 来源：https://www.nsidistribution.com/our-stores（抓取 2026-10-19）
- **【第三方】分销 Lysora（Business Systems Connection 的自有品牌）**
  > Lysora … distributed by NSI Distribution（检索摘要）
  > 来源：https://www.nsidistribution.com/（抓取 2026-10-19）
- **【卖方目录】【W10 回查】品牌页在线，但商品列表为 JS 加载、抓取结果为空 → 在售款数待补证（不改评级）**
  > # Planet Technology … Filters … Loading... … Nothing found … Request Quote Request special pricing for your next project.
  > 来源：https://www.nsidistribution.com/Brands/Planet-Technology-Corporation（抓取 2026-10-20）

## 在卖/在用 PLANET 型号 → Saga 对位

| PLANET 型号（证据所见） | Saga 对位 | 说明 |
|---|---|---|
| GSW-2620HP | STC-424DGGPM-280W | PLANET 为 24 口 PoE 非管理+2 SFP；Saga 为 L2+ 管理型，功能上覆盖 |
| GS-4210-24P4C（8/16/24 口 PoE 系列，品牌页未列全型号） | STC-424DGGPM-280W | 同口数/同上联近似对位，非功能等价 |

## 需求与场景（推断标签）

- 24/16/8 口 PoE 商用、贴牌、北美 FCC（Saga 有）、UL（Saga 无——若硬性要求则降级）（【推断】依据在卖品类）

## 联系方式（已有/猜测分标）

- **Norm Matinnia**（Sales and Product Development（zoominfo 口径；官网门店页列为联系人））：norm@nsidistribution.com / 1-800-668-3402 〔公开（官网 /our-stores 与 /careers 页）；源：https://www.nsidistribution.com/our-stores〕
- **Amanda Matinnia**（Sales and Purchasing（zoominfo 口径））：— 〔具名无公开邮箱（不猜）；源：zoominfo 摘要〕
- **—（销售）**（sales）：sales@nsidistribution.com / 1-800-668-3402 〔公开（官网）；源：https://www.nsidistribution.com/〕
- **邮箱纪律**：只记公开找到的地址；未做 SMTP 验证（不可验），MX 状态：未查。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Norm Matinnia | Sales and Product Development（zoominfo 口径；官网门店页列为联系人） | norm@nsidistribution.com / 1-800-668-3402 | 公开（官网 /our-stores 与 /careers 页） | https://www.nsidistribution.com/our-stores |
| Amanda Matinnia | Sales and Purchasing（zoominfo 口径） | — | 具名无公开邮箱（不猜） | zoominfo 摘要 |
| —（销售） | sales | sales@nsidistribution.com / 1-800-668-3402 | 公开（官网） | https://www.nsidistribution.com/ |

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W），备选型不进邮件。

### 第 1 次跟进 · 第二货源对位

- **推什么**：STC-424DGGPM-280W
- **切入点**：GSW-2620HP 同位且带 L2+ 管理；贴牌中性包装
- **要问的问题**：Is the 24-port PoE+ with 4 uplinks your highest-volume PLANET SKU across the branches, or do the 8/16-port units move faster?
- **随附/动作**：无附件；一句话带过 ERPS/IGMP/PoE 看门狗/CLI-SNMP

### 第 2 次跟进 · 样机到 Brampton

- **推什么**：STC-424DGGPM-280W（1 台）
- **切入点**：30 天并行测试，不要求承诺；兼容其在用 SFP
- **要问的问题**：Which site or customer could take one unit for a 30-day side-by-side test?
- **随附/动作**：L2+ 特性表 1 页

### 第 3 次跟进 · 贴牌/批量条件

- **推什么**：STC-28DGGPM（8 口 PoE+2 SFP）+ 贴牌方案
- **切入点**：中性包装、客户型号、固件 UI 定制；MOQ/付款/EXW 运费路径
- **要问的问题**：What order size per quarter would make a first run worth it for you?
- **随附/动作**：贴牌流程 1 页；报价前核价

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STC-424DGGPM-280W | 主场景 | $134.5 USD EXW（20% 档，SmartByte LT-S8328GP-4GX24GT-S 750 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 对位其在售 GSW-2620HP / GS-4210-24P4C 一档（24×GE PoE+ + 4 上联，280W），是安防批发最走量的尺寸；档位 20%：分销走量 → 20%；Norelco 贴牌定制另按 30% |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP（对位其 8 Port PoE + 2 Uplinks） | $80.7 USD EXW（20% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |
| 备选3 | STC-448DGGPM | 48 口 PoE 大项目 | $308.5 USD EXW（20% 档，SmartByte LT-S8352GP-4GX48GT 1720 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率（`docs/rules/报价与型号规则.md`）；Saga 商用线无 802.3bt、无 LCD、无云管理——不对标 PLANET 的 UPoE/LCD/NMS 型号。

## SWOT

- **S**：贴牌经验现成；具名直邮；安防渠道 PoE 用量大
- **W**：北美可能要求 UL/cUL（Saga 无）；已有 Lysora 作为贴牌货源
- **O**：Lysora 本身是贴牌货—Saga 可成为其上游或替代
- **T**：加拿大关税/合规顾虑；PLANET 通过 Globall/iOC 多渠道供货价格战

## 触达与风险红线

**通用红线（所有客户适用）**

1. 包装、外观、说明书**全部中性**，不出现「Made in China」，贴客户自己的型号。
2. **台厂不是客户**：PLANET 本身与其关联公司只是信号源；对 PLANET 渠道不贬低 PLANET，只谈「第二货源 / 贴牌 / 功能定制」。
3. PoE 功率与工业温宽是最容易当场翻车的两项，口头承诺必须落到实测数据；Saga 商用线 **无 802.3bt**，不要对标 PLANET 的 bt/UPoE 型号。
4. 不承诺 UL、EN50155、IP67、云管理——Saga 没有。
5. 样机先送测，再谈价格；大集团先问清采购层级。

**停止开发条件（命中任一即停）**：3 次定向触达无任何实质回复；确认现用平台完全满足需求；只愿比价不愿谈场景；决策者确认接触不到；对方书面拒绝。

**本户特别红线**：安防批发含报警/门禁（生命安全类），只谈网络交换机；不碰其门禁/报警线

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

- [ ] 是否要求 UL/cUL
- [ ] Norelco 交换机现有供应商
- [ ] 年 PoE 台数
- [ ] 是否接受 EXW 直采

## 首触邮件（英文样板 · 可直接发送）

**主题**：24-port PoE+ switch under the NSI/Norelco label, second source to GSW-2620HP

```text
Hi Norm,

Your PLANET page already lists 17 PoE models next to Norelco SafeCam, so a second-source PoE switch under your own label is a natural fit for your nine branches.

We supply Marvell-based L2+ PoE switches (ERPS <20 ms ring, IGMP snooping, 802.1Q/QinQ, PoE watchdog, CLI/SNMP) that fit the same slot as the PLANET GS-4210/GS-5220 class at a lower landed cost, and we can ship under your own label with neutral packaging. The unit I would start with for your line is STC-424DGGPM-280W at $134.5 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Is the 24-port PoE+ with 4 uplinks your highest-volume PLANET SKU across the branches, or do the 8/16-port units move faster?

If useful, I can send one unit to your office for a 30-day side-by-side test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom — An Engineering & Supply-Chain-First Telecom Partner
PoE / industrial switch OEM-ODM supplier (neutral packing available) · https://sagatele.com/
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

*建档日期：2026-10-19　|　入库批次：2026-10-19_W02_品牌页与型号反查_EU-UK-CZ-IT-HU-CA-US　|　原始证据：batch/2026-10-19_W02_品牌页与型号反查_EU-UK-CZ-IT-HU-CA-US.json, batch/2026-10-20_W10_证据老化回查与安防收尾_IT-PL.json　|　渲染：scripts/render.py 2026-10-20*
