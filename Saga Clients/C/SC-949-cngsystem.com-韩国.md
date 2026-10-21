# cngsystem.com

> **评级 C**　|　韩国　|　档案编号 `SC-949`　|　优先级 —　|　状态：发不过去
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：A优质名单(KR)、AI评估(KR)　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-949
rating: C
rating_auto: C
score: 13
country: 韩国
region: 亚太
website: cngsystem.com
type: 经销/集成（类型待核）
tier_tags: ["A优质名单(KR)", "AI评估(KR)"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STC-424DGGPM-280W
price_tier: 20%
research: pending
sources: 2
updated: 2026-10-21
```

## SALES BRIEF（压缩模型）

- **是谁**：韩国的经销/集成（类型待核）；兴趣/在卖：CENTEC Switch
- **为什么是 C 级**：+6 在 A/DONE 优质国家名单（已做过整轮推送）；+2 在 AI 客户评估名单；+4 AI/Claude 评估 B；-25 邮件发不过去且无 WhatsApp 通道；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+3 区域 亚太/韩国；C 级细分：发不过去
- **历史互动**：名单内·无互动记录
- **P1**：不推（C 级）；若对方主动来询，起手 STC-424DGGPM-280W（24 口 PoE L2+ 走量款）
- **最大未知**：网页调研未做（公司规模/业务/在卖品牌待核）
- **下一步**：不跟进；仅归档防重复开发

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | cngsystem.com（取自域名，公司全名待核） | 推断 |
| 国家 | 韩国 | 事实（用户表）|
| 网站/域名 | cngsystem.com / dialogic.co.kr | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | 发不过去 | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | CENTEC Switch | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 用户 AI 评估 | AI 25% B | 事实（用户表 AI评估结果/CALUDE评估结果列） |
| 所在清单 | A优质名单(KR)、AI评估(KR) | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

### 用户 AI / Claude 评估原文

- **AI**（AI客户评估_KR.xlsx）：
  > 25% B
  > 韩国网络设备公司，官网有Centec芯片方案交换机
  > 发送Centec系列核心/汇聚交换机产品线邮件，强调同芯片方案+价格竞争力
  > Centec L3核心交换机、10G SFP+汇聚交换机
  > 官网有Centec Switch与我司汇聚/核心产品线芯片方案一致；但邮箱发不过去（备注），实际跟进有障碍

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），写入 `data/saga_clients/research/SC-949.json` 后由渲染器并入本节。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`support@dialogic.co.kr`〔企业邮箱；用户备注含「发不过去」——发送前核对是哪一个地址；来源：用户表原值〕
- 联系人（原值）：发不过去
- 网站/域名：cngsystem.com
- 网站/域名：dialogic.co.kr
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:cngsystem.com`, `d:dialogic.co.kr`, `e:support@dialogic.co.kr`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/DONE/KR.xlsx#总表:80 | 79 | http://www.cngsystem.com/centech.aspx | 韩国 | 发不过去 | 谷歌 | CENTEC Switch | support@dialogic.co.kr |  | — |
| AI客户评估/AI客户评估_KR.xlsx#总表:38 | 37 | http://www.cngsystem.com/centech.aspx | 韩国 | 发不过去 | 谷歌 | CENTEC Switch | support@dialogic.co.kr |  | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：发不过去。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-949,B,理由` 后重跑即可。

## 触达与风险红线

1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。
2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。
3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。
4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。
5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。

## 变更日志

- 2026-10-21：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 C，分数 13）

---

*建档日期：2026-10-21　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
