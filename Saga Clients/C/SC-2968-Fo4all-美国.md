# Fo4all

> **评级 C**　|　美国　|　档案编号 `SC-2968`　|　优先级 —　|　状态：WhatsApp 已加·未回复
>
> **类型**：电商/网店（推断）　|　**历史关系**：WhatsApp 已加　|　**所在清单**：群发(之前OK现在群发)、用户判定不行　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-2968
rating: C
rating_auto: C
score: -77
country: 美国
region: 北美
website: fiberopticforall.com
type: 电商/网店
tier_tags: ["群发(之前OK现在群发)", "用户判定不行"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 7 msgs (out 7 / in 0), 2024-06-21 -> 2024-10-24
p1: STI-110GE
price_tier: 20%
research: pending
site_snapshot: none
sources: 2
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：美国的电商/网店；兴趣/在卖：MC, patchcords(online shop) fiber-optic products；MC, patchcords(online shop)  fiber-optic products
- **为什么是 C 级**：-6 群发批次名单；-60 用户已归入「不行及不太相关的」；-8 部分邮箱发不过去（有 WhatsApp 兜底）；-3 WhatsApp 加不上；+2 兴趣仅 MC/SFP/配件（边缘品类）；-15 兴趣只在 Saga 不做的品类（VC/光端机/DWDM/OTDR/CCTV/云管理等）；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国；-10 来源为 2010–2015 年展会且无后续记录；C 级细分：用户判定不行/不相关
- **历史互动**：WhatsApp 已加
- **P1**：不推（C 级）；若对方主动来询，起手 STI-110GE（工业迷你 1 光 1 电（MC 位））
- **最大未知**：网页调研未做（公司规模/业务/在卖品牌待核）
- **下一步**：不跟进；仅归档防重复开发

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Fo4all | 事实（用户表） |
| 国家 | 美国 | 事实（用户表）|
| 网站/域名 | fiberopticforall.com / fo4all.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 电商/网店 | 推断（据兴趣/备注关键词） |
| 联系人 | Radu Matei / Biz Dev | 事实（用户表） |
| 来源（From） | cebit 2010 | 事实（用户表） |
| 兴趣（Interested in） | MC, patchcords(online shop)<br>fiber-optic products / MC, patchcords(online shop)<br> fiber-optic products | 事实（用户表） |
| 用户备注（Remark） | 1-503-789-8090 已加<br>发不过去Whatsapp / 1-503-789-8090<br>加不上 | 事实（用户表） |
| 所在清单 | 群发(之前OK现在群发)、用户判定不行 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），写入 `data/saga_clients/research/SC-2968.json` 后由渲染器并入本节。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`radu.matei@fo4all.com`〔企业邮箱；用户备注含「发不过去」——发送前核对是哪一个地址；来源：用户表原值〕
- 电话：`+15037898090`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Radu Matei / Biz Dev
- 网站/域名：fiberopticforall.com
- 网站/域名：fo4all.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Radu Matei | — | radu.matei@fo4all.com / +15037898090 | 用户表原值·WhatsApp 已加 | Clients/ 表 |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；企业邮箱可直发；备注含「发不过去」：发送前核对是哪一个地址，退信地址保留不删

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:fiberopticforall.com`, `d:fo4all.com`, `e:radu.matei@fo4all.com`, `n:US|fo4all`, `p:037898090`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| E/群发/之前OK现在群发 08.17.xlsx#总表:51 | 50 | www.fiberopticforall.com<br>Fo4all | 美国 | Radu Matei<br>Biz Dev | cebit 2010 | MC, patchcords(online shop)<br>fiber-optic products | radu.matei@fo4all.com | 1-503-789-8090 已加<br>发不过去Whatsapp | — |
| 不行及不太相关的.xlsx#总表:700 |  | www.fiberopticforall.com<br>Fo4all | 美国 | Radu Matei<br>Biz Dev | cebit 2010 | MC, patchcords(online shop)<br> fiber-optic products | radu.matei@fo4all.com | 1-503-789-8090<br>加不上 | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：用户判定不行/不相关。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-2968,B,理由` 后重跑即可。

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

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 C，分数 -77）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
