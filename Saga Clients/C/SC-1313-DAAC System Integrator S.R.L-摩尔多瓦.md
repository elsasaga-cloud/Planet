# "DAAC System Integrator" S.R.L.

> **评级 C**　|　摩尔多瓦　|　档案编号 `SC-1313`　|　优先级 —　|　状态：名单内·未触达
>
> **类型**：安防集成/经销（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：群发(杂)　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-1313
rating: C
rating_auto: C
score: 8
country: 摩尔多瓦
region: 俄语区
website: daac-system.md
type: 安防集成/经销
tier_tags: ["群发(杂)"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STI-110GE
price_tier: 20%
research: pending
sources: 1
updated: 2026-10-21
```

## SALES BRIEF（压缩模型）

- **是谁**：摩尔多瓦的安防集成/经销；兴趣/在卖：WEM MC video conference, surveillance, network security
- **为什么是 C 级**：-6 群发批次名单；-3 WhatsApp 加不上；+2 兴趣仅 MC/SFP/配件（边缘品类）；+10 有企业邮箱；+5 有可核实的公司网站/域名；+0 区域 俄语区/摩尔多瓦；C 级细分：群发冷名单无回应
- **历史互动**：名单内·无互动记录
- **P1**：不推（C 级）；若对方主动来询，起手 STI-110GE（工业迷你 1 光 1 电（MC 位））
- **最大未知**：网页调研未做（公司规模/业务/在卖品牌待核）
- **下一步**：不跟进；仅归档防重复开发

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | "DAAC System Integrator" S.R.L. | 事实（用户表） |
| 国家 | 摩尔多瓦 | 事实（用户表）|
| 网站/域名 | daac-system.md | 事实（用户表 URL/邮箱域名） |
| 类型 | 安防集成/经销 | 推断（据兴趣/备注关键词） |
| 联系人 | Mr. Andrei Cornea / Mr. Alexander Carajia | 事实（用户表） |
| 来源（From） | sales | 事实（用户表） |
| 兴趣（Interested in） | WEM MC video conference, surveillance, network security | 事实（用户表） |
| 用户备注（Remark） | T 373 22 509 743<br>加不上 | 事实（用户表） |
| 所在清单 | 群发(杂) | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），写入 `data/saga_clients/research/SC-1313.json` 后由渲染器并入本节。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`andrei.cornea@daac-system.md`〔企业邮箱；来源：用户表原值〕
- 邮箱：`alexander.carajia@daac-system.md`〔企业邮箱；来源：用户表原值〕
- 电话：`+37322509743`〔WhatsApp 加不上；原值见来源表〕
- 联系人（原值）：Mr. Andrei Cornea / Mr. Alexander Carajia
- 网站/域名：daac-system.md
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Mr. Andrei Cornea | — | andrei.cornea@daac-system.md / alexander.carajia@daac-system.md / +37322509743 | 用户表原值 | Clients/ 表 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E/群发/杂  08.13.xlsx#总表:159 |  | "DAAC System Integrator" S.R.L. | 摩尔多瓦 | Mr. Andrei Cornea<br>Mr. Alexander Carajia | sales | WEM MC video conference, surveillance, network security | Andrei.Cornea@daac-system.md<br>Alexander.Carajia@daac-system.md | T 373 22 509 743<br>加不上 | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：群发冷名单无回应。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-1313,B,理由` 后重跑即可。

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
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **不合格（见 C 级细分）→ 不主动跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 网页调研未做（公司规模/业务/在卖品牌待核）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

> C 级不出邮件样板（不主动跟进）。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- 不复核。对方主动来询 → 在 `data/saga_clients/人工定级.csv` 写一行升级后重跑。

## 变更日志

- 2026-10-21：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 8）

---

*建档日期：2026-10-21　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
