# Fiberone Broadband Services

> **评级 C**　|　尼日利亚　|　档案编号 `SC-1072`　|　优先级 —　|　状态：名单内·未触达
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：DWDM线索　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-1072
rating: C
rating_auto: C
score: 11
country: 尼日利亚
region: 非洲
website: fob.ng
type: 经销/集成（类型待核）
tier_tags: ["DWDM线索"]
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

- **是谁**：尼日利亚的经销/集成（类型待核）；兴趣/在卖：交换机WDM等都看了比较懂 3个人一起，Simon加了Larry微信，另外一个人拍了Whatsapp照片
- **为什么是 C 级**：-8 DWDM/光传输线索：Saga 不做 DWDM（Hohunet 线为交换机）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；-6 区域 非洲/尼日利亚；+2 最近活动 2024；C 级细分：低价值区域冷线索
- **历史互动**：名单内·无互动记录
- **P1**：不推（C 级）；若对方主动来询，起手 STC-424DGGPM-280W（24 口 PoE L2+ 走量款）
- **最大未知**：网页调研未做（公司规模/业务/在卖品牌待核）
- **下一步**：不跟进；仅归档防重复开发

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Fiberone Broadband Services | 事实（用户表） |
| 国家 | 尼日利亚 | 事实（用户表）|
| 网站/域名 | fob.ng | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Larry | 事实（用户表） |
| 来源（From） | 光博会2024 | 事实（用户表） |
| 兴趣（Interested in） | 交换机WDM等都看了比较懂<br>3个人一起，Simon加了Larry微信，另外一个人拍了Whatsapp照片 | 事实（用户表） |
| 用户备注（Remark） | 234  803 071 1172<br>Mokheji | 事实（用户表） |
| 所在清单 | DWDM线索 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），写入 `data/saga_clients/research/SC-1072.json` 后由渲染器并入本节。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`wale.olawoye@fob.ng`〔企业邮箱；来源：用户表原值〕
- 邮箱：`adetola.akinmade@fob.ng`〔企业邮箱；来源：用户表原值〕
- 邮箱：`lanre.ore@fob.ng`〔企业邮箱；来源：用户表原值〕
- 电话：`+2348030711172`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Larry
- 网站/域名：fob.ng
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| DWDM CENTEC_ELSA  08.10.xlsx#总表:5 | 4 | Fiberone Broadband Services<br>https://fob.ng/ | 尼日利亚 | Larry | 光博会2024 | 交换机WDM等都看了比较懂<br>3个人一起，Simon加了Larry微信，另外一个人拍了Whatsapp照片 | wale.olawoye@fob.ng<br>adetola.akinmade@fob.ng<br>lanre.ore@fob.ng | 234  803 071 1172<br>Mokheji | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：低价值区域冷线索。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-1072,B,理由` 后重跑即可。

## 触达与风险红线

1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。
2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。
3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。
4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。
5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。

## 变更日志

- 2026-10-21：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 11）

---

*建档日期：2026-10-21　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
