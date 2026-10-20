# INTER-COMP.PL KOWALSKI sp. z o.o. (media-konwertery.pl)

> **评级 B**　|　波兰 · Koronowo　|　档案编号 `PB-017`　|　优先级 ★☆☆　|　状态：00-未触达
>
> **类型**：分销商/电商（媒体转换器/工业交换机/IP 摄像机多站电商：media-konwertery.pl、lan.sklep.pl、kamery-ip.com、routery.sklep.pl）　|　**PLANET 关联**：在售 PLANET 工业交换机（IGS-4215-4P4T、IGS-6325、FGSD-1022VHP 等）　|　结构版本：v2（继承 Mikrotik R56 骨架 · Planet 仓库 2026-10-19 起）

```yaml structured_profile
code: PB-017
rating: B
country: 波兰
type: 分销商/电商（媒体转换器/工业交换机/IP 摄像机多站电商：media-konwertery.pl、lan.sklep.pl、kamery-ip.com、routery.sklep.pl）
planet_models: ["IGS-4215-4P4T", "IGS-6325", "FGSD-1022VHP"]
p1: STI-288DGGPM
price_tier: 20%
stage: 00-未触达
mikrotik_ref: none
updated: 2026-10-20
```

## SALES BRIEF（压缩模型）

- **是谁**：波兰北部小镇的专业网络电商群，业主一人决策，专卖转换器与工业交换机
- **为什么值得跟**：需求：PLANET 工业在售；触达 info@ 通用，业主具名无直邮；体量小 → B
- **P1（首触唯一主推）**：STI-288DGGPM — 其工业线以 4/8 口 DIN 为主；8×GE PoE+ + 2 SFP 走量；$139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：Which industrial PoE size sells most on your sites: 4-port, 8-port, or 16-port?
- **最大未知**：年台数；是否经 FEN/ACTION 进货
- **下一步**：未触达；按本档首触邮件由用户在仓库外发出，回复后更新本档

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | INTER-COMP.PL KOWALSKI sp. z o.o. (media-konwertery.pl) | 事实（网页自述） |
| 国家/城市 | 波兰 / Koronowo | 事实 |
| 网站 | media-konwertery.pl | 事实 |
| 类型 | 分销商/电商（媒体转换器/工业交换机/IP 摄像机多站电商：media-konwertery.pl、lan.sklep.pl、kamery-ip.com、routery.sklep.pl） | 事实（厂商/官网口径） |
| PLANET 关联 | 在售 PLANET 工业交换机（IGS-4215-4P4T、IGS-6325、FGSD-1022VHP 等） | 事实（见下节证据） |
| 自有品牌 | 否 | 事实 |

## PLANET 关联证据（原文 + URL + 抓取日期）

- **【卖方目录】PLANET 工业交换机在售**
  > IGS-4215-4P4T … IGS-6325 … FGSD-1022VHP（商品页，检索摘要）
  > 来源：https://www.media-konwertery.pl/（抓取 2026-10-19）
- **【公司自述】法人与地址**
  > INTER-COMP.PL KOWALSKI sp. z o.o., ul. Pogodna 13, 86-010 Koronowo（页脚/联系页，检索摘要）
  > 来源：https://www.media-konwertery.pl/（抓取 2026-10-19）

## 在卖/在用 PLANET 型号 → Saga 对位

| PLANET 型号（证据所见） | Saga 对位 | 说明 |
|---|---|---|
| IGS-4215-4P4T | STI-088GP（近似） | 工业 4 PoE + 4 铜 |
| IGS-6325 | STI-488DGGPM（近似，L3 系列） | PLANET 为 L3 工业；Saga 工业 L2+ |
| FGSD-1022VHP | — | FE PoE：Saga 暂无对应（无 FE PoE 线） |

## 需求与场景（推断标签）

- PoE 接入供电（安防/AP）；工业/宽温 DIN；万兆上行（【推断】依据在卖品类）

## 联系方式（已有/猜测分标）

- **Marek Kowalski**（Właściciel（业主））：— / +48 52 511-88-33 〔具名无公开直邮（不猜）；源：https://www.media-konwertery.pl/〕
- **—（总机）**（info）：info@media-konwertery.pl / info@inter-comp.pl / +48 52 511-88-33 〔公开（官网）；源：https://www.media-konwertery.pl/〕
- **邮箱纪律**：只记公开找到的地址；未做 SMTP 验证（不可验），MX 状态：未查。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288DGGPM），备选型不进邮件。

### 第 1 次跟进 · 第二货源/贴牌试探

- **推什么**：STI-288DGGPM
- **切入点**：小型专业电商，品类正是转换器/工业交换机；业主 Marek Kowalski 具名（无直邮）
- **要问的问题**：Which industrial PoE size sells most on your sites: 4-port, 8-port, or 16-port?
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
| **P1（首触唯一）** | STI-288DGGPM | 主场景 | $139.9 USD EXW（20% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 其工业线以 4/8 口 DIN 为主；8×GE PoE+ + 2 SFP 走量；档位 20%：电商走量 → 20% |
| 备选2 | STI-488DGGPM | 工业 8 PoE + 4 SFP | $147.1 USD EXW（20% 档，SmartByte LT-IS6312GP-4GX8GT 820 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 过后的台阶，不进首触邮件 |

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

**主题**：Industrial 8-port PoE+ DIN switch, second source to IGS-4215/IGS-6325 class

```text
Hi Marek,

media-konwertery.pl is built around converters and industrial switches, so a Marvell-based DIN PoE switch with ERPS fits your catalogue logic exactly.

We supply Marvell-based L2+ PoE switches (ERPS <20 ms ring, IGMP snooping, 802.1Q/QinQ, PoE watchdog, CLI/SNMP) that fit the same slot as the PLANET GS-4210/GS-5220 class at a lower landed cost, and we can ship under your own label with neutral packaging. The unit I would start with for your line is STI-288DGGPM at $139.9 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Which industrial PoE size sells most on your sites: 4-port, 8-port, or 16-port?

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

*建档日期：2026-10-19　|　入库批次：2026-10-19_W02_品牌页与型号反查_EU-UK-CZ-IT-HU-CA-US　|　原始证据：batch/2026-10-19_W02_品牌页与型号反查_EU-UK-CZ-IT-HU-CA-US.json　|　渲染：scripts/render.py 2026-10-20*
