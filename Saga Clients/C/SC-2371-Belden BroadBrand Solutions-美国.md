# Belden BroadBrand Solutions

> **评级 C**　|　美国　|　档案编号 `SC-2371`　|　优先级 —　|　状态：WhatsApp 已加·未回复
>
> **类型**：系统集成/工程商（推断）　|　**历史关系**：WhatsApp 已加　|　**所在清单**：DWDM线索、询盘流水　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-2371
rating: C
rating_auto: C
score: -28
country: 美国
region: 北美
website: opterna.com
type: 系统集成/工程商
tier_tags: ["DWDM线索", "询盘流水"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: none
price_tier: 25%
research: pending
site_snapshot: none
sources: 2
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：美国的系统集成/工程商；兴趣/在卖：主要是无源配件
- **为什么是 C 级**：+12 主动询盘（阿里巴巴/自建站/转介）；-8 DWDM/光传输线索：Saga 不做 DWDM（Hohunet 线为交换机）；-15 兴趣只在 Saga 不做的品类（VC/光端机/DWDM/OTDR/CCTV/云管理等）；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国；+5 最近活动 2025；-45 巨头/品牌厂商/运营商/军工（INH 规则：体量不匹配或非客户）；C 级细分：体量过大/品牌厂商/运营商
- **历史互动**：WhatsApp 已加
- **P1**：不推（C 级）；若对方主动来询，起手 STC-424DGGPM-280W（DWDM/OTDR：Saga 不做）
- **最大未知**：网页调研未做（公司规模/业务/在卖品牌待核）
- **下一步**：不跟进；仅归档防重复开发

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Belden BroadBrand Solutions | 事实（用户表） |
| 国家 | 美国（另见：印度） | 事实（用户表）|
| 网站/域名 | opterna.com / belden.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 系统集成/工程商 | 推断（据兴趣/备注关键词） |
| 联系人 | Sanjith S | 事实（用户表） |
| 来源（From） | 富通天下 / 2025.2.19 | 事实（用户表） |
| 兴趣（Interested in） | 主要是无源配件 | 事实（用户表） |
| 用户备注（Remark） | DWDM / from: 自建站 | 事实（用户表） |
| 所在清单 | DWDM线索、询盘流水 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），写入 `data/saga_clients/research/SC-2371.json` 后由渲染器并入本节。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`bbs.cs@belden.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`sanjith.swaminathan@belden.com`〔企业邮箱；来源：用户表原值〕
- 电话：`+919778410574`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Sanjith S
- 网站/域名：opterna.com
- 网站/域名：belden.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Sanjith S | — | bbs.cs@belden.com / sanjith.swaminathan@belden.com / +919778410574 | 用户表原值·WhatsApp 已加 | Clients/ 表 |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:belden.com`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| DWDM CENTEC_ALAN 08.13.xlsx#总表:138 | 137 | https://www.opterna.com/sub_category_grid/44 | 美国 |  | 富通天下 | 主要是无源配件 | bbs.cs@belden.com |  | — |
| 询盘统计表.xlsx#Sheet1:110 |  | Belden BroadBrand Solutions | 印度 | Sanjith S | 2025.2.19 |  | sanjith.swaminathan@belden.com 91 97784 10574 已加 | DWDM from: 自建站 | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：体量过大/品牌厂商/运营商。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-2371,B,理由` 后重跑即可。

## 触达与风险红线

1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。
2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。
3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。
4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。
5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（在卖/在用交换机或 PoE） | ❓ 表内兴趣不含交换机关键词 |
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

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 C，分数 -28）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
