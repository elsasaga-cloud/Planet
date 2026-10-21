# Core and Clad

> **评级 B**　|　巴林　|　档案编号 `SB-125`　|　优先级 ★★　|　状态：成交过·维护
>
> **类型**：系统集成/工程商（推断）　|　**历史关系**：成交/下单过；推送 1 次（2025-10-08 → 2025-10-08）　|　**所在清单**：E冷名单(巴林)　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-125
rating: B
rating_auto: B
score: 51
country: 巴林
region: 中东
website: none
type: 系统集成/工程商
tier_tags: ["E冷名单(巴林)"]
deal: yes
replies: 0
followups: 1
first_contact: 2025-10-08
last_contact: 2025-10-08
p1: STI-110GE
price_tier: 25%
research: pending
sources: 1
updated: 2026-10-21
```

## SALES BRIEF（压缩模型）

- **是谁**：巴林的系统集成/工程商；兴趣/在卖：2011年买过2次收发器
- **为什么是 B 级**：+50 有成单/下单/买过记录（用户备注或跟进表）；-6 E 冷名单（按国家群发）；+2 兴趣仅 MC/SFP/配件（边缘品类）；+0 仅免费邮箱；+3 区域 中东/巴林；+5 最近活动 2025；-3 跟进表最近平台标记 E（已降为群发）
- **历史互动**：成交/下单过；推送 1 次（2025-10-08 → 2025-10-08）
- **P1（下一步唯一主推）**：STI-110GE — 工业迷你 1 光 1 电（MC 位）；$23.4 USD EXW（25% 档，SmartByte LT-IMC30G-E 125 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价）
- **第一问（只问一个）**：Are PoE / industrial switches something you still source today, or has that line been dropped?
- **最大未知**：公司网站（表内无域名，无法核实是否仍在运营）；网页调研未做（公司规模/业务/在卖品牌待核）
- **下一步**：放入慢跟队列（4–6 周一次）；有回复即重评

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Core and Clad | 事实（用户表） |
| 其他名称写法 | Telecom Solutions | 事实（用户表） |
| 国家 | 巴林 | 事实（用户表）|
| 网站/域名 | — | 事实（用户表 URL/邮箱域名） |
| 类型 | 系统集成/工程商 | 推断（据兴趣/备注关键词） |
| 联系人 | Mr. Ebrahim Y. Alsada / 采购 | 事实（用户表） |
| 来源（From） | intersec 2011 | 事实（用户表） |
| 兴趣（Interested in） | 2011年买过2次收发器 | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | E冷名单(巴林) | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），写入 `data/saga_clients/research/SB-125.json` 后由渲染器并入本节。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 1 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-10-08 | 2025.10.8 | dac |  | E |  | 巴林.xlsx#1 |

## 联系方式（已有 · 原值照录）

- 邮箱：`core.and.clad@gmail.com`〔免费邮箱；来源：用户表原值〕
- 联系人（原值）：Mr. Ebrahim Y. Alsada / 采购
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Mr. Ebrahim Y. Alsada | — | core.and.clad@gmail.com | 用户表原值 | Clients/ 表 |

- **通道建议**：仅免费邮箱：可发，但优先找官网公开的企业邮箱（见调研 KP）

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E/2026.08.04/巴林.xlsx#总表:2 | 1 | Core and Clad <br>Telecom Solutions | 巴林 | Mr. Ebrahim Y. Alsada<br>采购 | intersec 2011 | 2011年买过2次收发器 | core.and.clad@gmail.com |  | 1 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-110GE | 工业迷你 1 光 1 电（MC 位） | $23.4 USD EXW（25% 档，SmartByte LT-IMC30G-E 125 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 据用户表兴趣/备注推断；档位 25%（系统集成/工程商） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $145.7 USD EXW（25% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $188.7 USD EXW（25% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-110GE），备选型不进首触。

- **第 1 次**：老客户回访——问上次所购型号的使用情况 + 告知 Marvell 新款（STI-110GE）；只问一个问题：当前在采购的主力型号与月量。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有成交史，信任与开户成本已付
- **W**：中东：物流/收款/汇率摩擦高于主攻区；没有可靠直达通道
- **O**：P1 STI-110GE 按 25% 档报价，做现供应商的第二货源
- **T**：深圳同行（ONV / Utepo / 迈威等）价格战；汇率与海运波动吃掉 20–30% 的价差

## 触达与风险红线

1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。
2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。
3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。
4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。
5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（在卖/在用交换机或 PoE） | ✅ |
| 决策人识别 | ✅ |
| 触达通道 | ⚠️ 仅免费邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ✅ 有成交史（量待确认） |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 公司网站（表内无域名，无法核实是否仍在运营）
- [ ] 网页调研未做（公司规模/业务/在卖品牌待核）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STI-110GE - industrial mini Gigabit media converter (Marvell-based, neutral label)

```text
Hi Ebrahim,

Thank you again for your earlier order with us - this is a short update rather than a cold mail.

We supply a Marvell-based industrial mini Gigabit media converter (1 fiber + 1 copper) - model STI-110GE - that fits the same slot as the usual Taiwan-grade units at a lower landed cost, and we can ship it with neutral packaging. Current price: $23.4 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Are PoE / industrial switches something you still source today, or has that line been dropped?

If useful, I can send one unit for a 30-day side-by-side test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 发送前检查：① 不出现「Made in China」或原产地；② 不承诺未实测指标（PoE 功率/温宽）；③ 落款换成发件人姓名；④ 一次只问一个问题；⑤ 价格为 USD EXW 快照，过窗先核价；⑥ 只用表内/公开原值邮箱，不猜地址；⑦ 发出后在「新跟进记录」补一行并告知日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-20**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-21：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 51）

---

*建档日期：2026-10-21　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
