# pixelcube

> **评级 C**　|　印度　|　档案编号 `SC-783`　|　优先级 —　|　状态：WhatsApp 已加·未回复
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：WhatsApp 已加　|　**所在清单**：AI评估(IN)·DONE　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-783
rating: C
rating_auto: C
score: 16
country: 印度
region: 南亚
website: pixelcube.in
type: 经销/集成（类型待核）
tier_tags: ["AI评估(IN)·DONE"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STC-424DGGPM-280W
price_tier: 20%
research: pending
sources: 1
updated: 2026-10-21
```

## SALES BRIEF（压缩模型）

- **是谁**：印度的经销/集成（类型待核）；兴趣/在卖：能否做SKD,price list(所有系列)，待两周，想来公司看
- **为什么是 C 级**：+2 在 AI 客户评估名单；+15 AI/Claude 评估 A；+0 仅免费邮箱；+5 有可核实的公司网站/域名；-6 区域 南亚/印度；C 级细分：低价值区域冷线索
- **历史互动**：WhatsApp 已加
- **P1**：不推（C 级）；若对方主动来询，起手 STC-424DGGPM-280W（无明确兴趣记录：按 Saga 走量款起手）
- **最大未知**：网页调研未做（公司规模/业务/在卖品牌待核）
- **下一步**：不跟进；仅归档防重复开发

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | pixelcube | 事实（用户表） |
| 国家 | 印度 | 事实（用户表）|
| 网站/域名 | pixelcube.in | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Siranjivij | 事实（用户表） |
| 来源（From） | CPSE 2023 | 事实（用户表） |
| 兴趣（Interested in） | 能否做SKD,price list(所有系列)，待两周，想来公司看 | 事实（用户表） |
| 用户备注（Remark） | Wechat: siran-pixel | 事实（用户表） |
| 用户 AI 评估 | AI 35% A | 事实（用户表 AI评估结果/CALUDE评估结果列） |
| 所在清单 | AI评估(IN)·DONE | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

### 用户 AI / Claude 评估原文

- **AI**（AI客户评估_IN 08.31.xlsx）：
  > 35% A
  > 印度公司，CPSE 2023展会接触，询问SKD（半散件组装）模式、要求全系列价格表，表示想来公司实地考察，有实际合作意向
  > 发送完整产品价格表，重点介绍OEM/ODM/SKD合作模式、芯片库存充足、交期快；邀请来访/安排线上会议深入沟通定制需求
  > 商业PoE全系列（8/16/24/48口）、工业PoE交换机
  > CPSE展会面对面接触，已加微信，沟通基础好；主动询问SKD模式说明有深度合作意向（品牌商/方案商角色）；愿意来公司考察表示合作意愿强；但公司信息有限（官网信息较少），实际规模和业务深度需进一步确认

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），写入 `data/saga_clients/research/SC-783.json` 后由渲染器并入本节。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`pixelcube.siran@gmail.com`〔免费邮箱；来源：用户表原值〕
- 电话：`+917338877496`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Siranjivij
- 网站/域名：pixelcube.in
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| AI客户评估/DONE/AI客户评估_IN 08.31.xlsx#总表:26 | 25 | pixelcube<br>www.pixelcube.in | 印度 | Siranjivij | CPSE 2023 | 能否做SKD,price list(所有系列)，待两周，想来公司看 | pixelcube.siran@gmail.com<br>91 73388 77496 已加 | Wechat: siran-pixel | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：低价值区域冷线索。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-783,B,理由` 后重跑即可。

## 触达与风险红线

1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。
2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。
3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。
4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。
5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。

## 变更日志

- 2026-10-21：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 16）

---

*建档日期：2026-10-21　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
