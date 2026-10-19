# Exertis Connect (France)

> **评级 C**　|　法国 · —　|　档案编号 `PC-004`　|　优先级 —　|　状态：00-未触达
>
> **类型**：分销商（Exertis/DCC 集团法国网络批发）　|　**PLANET 关联**：批发目录含 PLANET IGS-801T 等　|　结构版本：v2（继承 Mikrotik R56 骨架 · Planet 仓库 2026-10-19 起）
>
> ⚠️ **Mikrotik 仓库已有档案 C-185**：本档只补 PLANET 侧证据；联系策略以先建档案为准，勿重复首触。

```yaml structured_profile
code: PC-004
rating: C
country: 法国
type: 分销商（Exertis/DCC 集团法国网络批发）
planet_models: ["IGS-801T"]
p1: STI-080GE
price_tier: 20%
stage: 00-未触达
mikrotik_ref: C-185
updated: 2026-10-19
```

## SALES BRIEF（压缩模型）

- **是谁**：分销商（Exertis/DCC 集团法国网络批发）；批发目录含 PLANET IGS-801T 等
- **为什么值得跟**：Exertis 为 DCC plc 旗下泛欧分销巨头（INH-07 名单内）
- **P1（首触唯一主推）**：STI-080GE — 按其在卖的 PLANET 型号对位；$31.4 USD EXW（20% 档，SmartByte LT-IS3008G-8GT 175 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：Which PoE switch model do you sell most often today, and roughly how many units a year?
- **最大未知**：采购决策人与年用量未确认；现用 PLANET 型号的毛利与断货痛点未确认
- **下一步**：未触达；按本档首触邮件由用户在仓库外发出，回复后更新本档

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Exertis Connect (France) | 事实（网页自述） |
| 国家/城市 | 法国 / — | 事实 |
| 网站 | exertis-connect.fr | 事实 |
| 类型 | 分销商（Exertis/DCC 集团法国网络批发） | 事实（厂商/官网口径） |
| PLANET 关联 | 批发目录含 PLANET IGS-801T 等 | 事实（见下节证据） |
| 自有品牌 | 否 | 事实 |

## PLANET 关联证据（原文 + URL + 抓取日期）

- **【卖方目录】Exertis Connect 批发目录列 PLANET IGS-801T**
  > Planet Switch Indust Gigabit -40/75° - 8 ports 10/100/1000 : Grossiste Switchs. Exertis Connect est le grossiste informatique spécialisé Réseau actif … Part number · IGS-801T
  > 来源：https://www.exertis-connect.fr/fr/314808.html（抓取 2026-10-19）
- **【第三方】W03 补证：2026-06-01 起 Exertis Connect 与 Azenn 合并为 Azenn Connect（300 人、约 €160M），PLANET 仍在售（FSD-1008HP / IGS-824UPT）**
  > Depuis le 1er juin, les distributeurs spécialisés … Azenn et Exertis Connect ont fusionné pour donner naissance à Azenn Connect. Cette entité emploie désormais 300 collaborateurs pour un chiffre d'affaires d'environ 160 millions d'euros.
  > 来源：https://www.distributique.com/actualites/lire-azenn-connect-rassemble-les-activites-d-azenn-et-exertis-connect-37313.html（抓取 2026-06-15）
- **【卖方目录】Azenn Connect 在售 PLANET**
  > Planet FSD-1008HP switch 10" 10P 10/100 dont 8 poe+ 120W - Switchs- Azenn Connect, grossiste informatique
  > 来源：https://www.azenn-connect.fr/fr/411108.html（抓取 2026-10-19）
- **【Mikrotik 仓库】C-185 Exertis Azenn 同集团**
  > C-185 Exertis Azenn 法国 分销（ComNet 授权）… 太难·规模过大/决策链长
  > 来源：https://github.com/SimonSaga-202306/mikrotik-info/blob/arena/01a0c3ef-mikrotik-info/客户名单_反向信号_2026-09.csv（抓取 2026-10-19）

## 在卖/在用 PLANET 型号 → Saga 对位

| PLANET 型号（证据所见） | Saga 对位 | 说明 |
|---|---|---|
| IGS-801T | STI-080GE | 工业 8×GE 非管理 |

## 需求与场景（推断标签）

- PoE 接入供电（安防/AP）；工业/宽温 DIN；万兆上行（【推断】依据在卖品类）

## 联系方式（已有/猜测分标）

- 入口：待补证
- **邮箱纪律**：只记公开找到的地址；未做 SMTP 验证（不可验），MX 状态：未查。

## 跟进步骤（最多 3 次 · 成功/退出标准）

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-080GE），备选型不进邮件。

### 第 1 次跟进 · 第二货源/贴牌试探

- **推什么**：STI-080GE
- **切入点**：—（集团巨头）
- **要问的问题**：Which PoE switch model do you sell most often today, and roughly how many units a year?
- **随附/动作**：无附件；规格页链接一条

### 第 2 次跟进 · 样机

- **推什么**：STI-080GE（1 台）
- **切入点**：30 天并行测试，不要求承诺
- **要问的问题**：Which site/customer would you test it on?
- **随附/动作**：L2+ 特性表 1 页（ERPS/QinQ/IGMP/PoE watchdog）

### 第 3 次跟进 · 贴牌与批量

- **推什么**：STI-080GE + 贴牌方案
- **切入点**：中性包装、客户型号、固件 UI 定制
- **要问的问题**：What MOQ and label format would make sense for a first run?
- **随附/动作**：贴牌流程 1 页；报价前核价

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1（首触唯一）** | STI-080GE | 主场景 | $31.4 USD EXW（20% 档，SmartByte LT-IS3008G-8GT 175 CNY × 1.20 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 按其在卖的 PLANET 型号对位；档位 20%：分销/电商走量 |

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
| 决策人识别 | ❓ 未具名 |
| 触达通道 | ❓ 仅表单/电话 |
| 现用交换品牌 | ✅ PLANET（证据所见） |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待首触信号）** |

## Unknowns（待问清单 · 首触后逐项消除）

- [ ] 年用量与最常出的 PLANET 型号
- [ ] 是否接受贴牌/第二货源
- [ ] 采购决策人与付款口径
- [ ] 对 bt/LCD/云管理等 Saga 缺口的依赖程度

## 跟进记录

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 首次触达前留空；用户在仓库外发出邮件后告诉我日期与渠道，我来更新本档并重评 stage。

## 下次复核

- 首触发出后 **14 天**无回复 → 复核是否降频；有任何回复 → 当即重评 stage 与评级。
- 报价纪律：价格为 USD EXW 快照（汇率 2026-10-17），过窗先核价再报价。

---

*建档日期：2026-10-19　|　入库批次：2026-10-19_W01_官方分销与品牌页_DE-IT-FR-ES-PL-UK-US　|　原始证据：batch/2026-10-19_W01_官方分销与品牌页_DE-IT-FR-ES-PL-UK-US.json, batch/2026-10-19_W03_品牌页反查与Mikrotik并档_HU-IT-NO-ES-FI-UK-PL-CA-FR-CZ.json　|　渲染：scripts/render.py 2026-10-19*
