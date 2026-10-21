# Lilnic GROUP Limited

> **评级 C**　|　肯尼亚　|　档案编号 `SC-2104`　|　优先级 —　|　状态：WhatsApp 已加·未回复
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：WhatsApp 已加　|　**所在清单**：群发(杂)　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-2104
rating: C
rating_auto: C
score: -14
country: 肯尼亚
region: 非洲
website: none
type: 经销/集成（类型待核）
tier_tags: ["群发(杂)"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STC-448DGGPM
price_tier: 20%
research: pending
sources: 1
updated: 2026-10-21
```

## SALES BRIEF（压缩模型）

- **是谁**：肯尼亚的经销/集成（类型待核）；兴趣/在卖：4光8工业大壳 2光6大壳 2光8大壳
- **为什么是 C 级**：-6 群发批次名单；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+0 仅免费邮箱；-6 区域 非洲/肯尼亚；-10 最近活动 2022（陈旧）；C 级细分：陈旧线索无互动
- **历史互动**：WhatsApp 已加
- **P1**：不推（C 级）；若对方主动来询，起手 STC-448DGGPM（48 口 PoE 走量款）
- **最大未知**：公司网站（表内无域名，无法核实是否仍在运营）；网页调研未做（公司规模/业务/在卖品牌待核）
- **下一步**：不跟进；仅归档防重复开发

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Lilnic GROUP Limited | 事实（用户表） |
| 国家 | 肯尼亚 | 事实（用户表）|
| 网站/域名 | — | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Mr.Nicholas Makwae Matagaro | 事实（用户表） |
| 来源（From） | 2022.2.14 | 事实（用户表） |
| 兴趣（Interested in） | 4光8工业大壳 2光6大壳 2光8大壳 | 事实（用户表） |
| 用户备注（Remark） | 25470117 4840 <br>已加 | 事实（用户表） |
| 所在清单 | 群发(杂) | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），写入 `data/saga_clients/research/SC-2104.json` 后由渲染器并入本节。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`nicholasmakwae@gmail.com`〔免费邮箱；来源：用户表原值〕
- 电话：`+254701174840`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Mr.Nicholas Makwae Matagaro
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E/群发/杂  08.13.xlsx#总表:84 |  | Lilnic GROUP Limited | 肯尼亚 | Mr.Nicholas Makwae Matagaro | 2022.2.14 | 4光8工业大壳 2光6大壳 2光8大壳 | nicholasmakwae@gmail.com | 25470117 4840 <br>已加 | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：陈旧线索无互动。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-2104,B,理由` 后重跑即可。

## 触达与风险红线

1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。
2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。
3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。
4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。
5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。

## 变更日志

- 2026-10-21：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 -14）

---

*建档日期：2026-10-21　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
