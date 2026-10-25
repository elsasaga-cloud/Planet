# ZhenHui Optical（Tina，163 邮箱）
**官方名称（调研核实）**：ZhenHui Optical（发件名；huili0126@163.com，Tina，+86 15989404908）

> **评级 C**　|　中国大陆　|　档案编号 `SC-3418`　|　优先级 —　|　状态：名单内·未触达
>
> **类型**：国内贸易商（替其客户采购）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：补录、Q-44复跑、国内　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-3418
rating: C
rating_auto: C
name_official: "ZhenHui Optical（发件名；huili0126@163.com，Tina，+86 15989404908）"
score: -15
country: 中国大陆
region: 中国大陆
website: none
type: 国内贸易商（替其客户采购）
tier_tags: ["补录", "Q-44复跑", "国内"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 5 msgs (out 2 / in 3), 2026-01-20 -> 2026-01-20
p1: STH-2C24XF-HSI（CENTEC 24×10G + 2×100G，$1,350 起；冗余按双机 + 堆叠/MLAG 方案）
price_tier: 30%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：国内光通信贸易商。Alan 2026-01-20 群发 CENTEC 核心/汇聚（OEM Core Switching Solution），Tina 回问公司在哪、有没有带冗余配置的核心交换机（10G 以上上联，含 SFP/光模块/管理模块），随后两次要电话，Alan 答只走邮件，她回「那就到此为止」。（调研 2026-10-24；表内兴趣：2026-01-20 问核心交换机：「Must be configured for redundancy. Uplinks of 10GB or higher (include all accessories, SFPs, transcei）
- **为什么是 C 级**：+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+0 仅免费邮箱；-40 区域 中国大陆/中国大陆；+5 最近活动 2026；C 级细分：中国大陆（非出口客户）
- **历史互动**：名单内·无互动记录
- **P1**：不推（C 级）；若对方主动来询，起手 STH-2C24XF-HSI（CENTEC 24×10G + 2×100G，$1,350 起；冗余按双机 + 堆叠/MLAG 方案）（深挖对位：国内贸易商转卖，按 OEM 30% 档；但国内单按《计划》走私账）
- **最大未知**：公司网站（表内无域名，无法核实是否仍在运营）
- **下一步**：不排（国内、已断） 若做：Simon 私账电话 / 微信 仅当 Simon 决定接国内线索时打一次电话；邮件不再发

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SC-3418` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：J1 无绑定（已断）** ｜ 类型：一次群发引出的询问，当天断 ｜ 筛子：国内贸易商，不在重点区域 ｜ 停点：对方已结束对话 ｜ 复活：不主动；若 Simon 愿意私账接国内线索，可用 +86 15989404908 微信/电话一次 ｜ 通路：国内：私账电话/微信 ｜ 节奏：不排 ｜ 证据：2026-01-20 三封往来
- **现状一句话**：2026-01-20 一天内 3 来 3 去，Tina 两次要电话，Alan 拒，对话结束。无后续。
- **对方真实需求（有据）**：冗余核心交换机、10G 以上上联、含 SFP/光模块/管理模块（替其客户采购）。
- **断点 / 为什么停在这里**：Alan 不给电话（Saga 对外不留电话的规矩）→ 对方终止。
- **Saga 现在该推什么**：P1 **STH-2C24XF-HSI 双机 + 堆叠（CENTEC），或 STH-8C48DX-HSI（48×25G + 8×100G）**（30% 档，CENTEC 锚价：2C24XF $1,350 / 8C48DX $4,800（见 CENTEC 锚表）；国内报价应报 RMB 且走私账）——她的客户要「冗余核心」——CENTEC 线才对得上；AC5 不堆叠
  - 做不了 / 要先核的：她客户是谁、规模多大一概不知
- **下一步（具体）**：不排（国内、已断）　若做：Simon 私账电话 / 微信　仅当 Simon 决定接国内线索时打一次电话；邮件不再发
  - 第一问（只问一个）：（国内）你们客户的核心是几台、要不要堆叠，预算区间多少？

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-01-20 | 去 | Alan → Tina | I am introducing our CENTEC-based core and aggregation switches. 1, A cost-effective alternative to Cisco or Huawei models 2, Multiple models(10G~800G) 3, Full L3 features(VXLAN, EVPN, MPLS, Stacking etc.) | 群发「OEM Core Switching Solution」 | `gmail_a（引用于 2fbf61891a3405e7）` |
| 2026-01-20 | 来 | Tina | Do you have Core Switches, Must be configured for redundancy. Uplinks of 10GB or higher (Include all accessories, SFPs, Transceivers, and management modules required) | 具体需求 + 手机号 | `gmail_a 2fbf61891a3405e7` |
| 2026-01-20 | 来 | Tina | Pls share me your phone number don't just send email. | 要电话 | `gmail_a 5d594ad7fc42e728` |
| 2026-01-20 | 去 | Alan → Tina | Generally, we just talk on emails and do not do personal contact. What is the point anyway? | 拒给电话，口气偏硬 | `gmail_a 21ea204c3742ba0e` |
| 2026-01-20 | 来 | Tina | If you think you just can do the biz via email. then let's end our conversation here. | 对话终止 | `gmail_a 9934d8c01aedb256` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：公司全称/所在地（163 邮箱，无签名档）

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | ZhenHui Optical（Tina，163 邮箱） | 事实（用户表） |
| 国家 | 中国大陆 | 事实（用户表）|
| 网站/域名 | — | 事实（用户表 URL/邮箱域名） |
| 类型 | 国内贸易商（替其客户采购） | 推断（据兴趣/备注关键词） |
| 联系人 | Tina | 事实（用户表） |
| 来源（From） | 补录：A 邮箱有人工往来但不在客户表（Q-44 A+S 复跑，T29-U45 第 64 批） | 事实（用户表） |
| 兴趣（Interested in） | 2026-01-20 问核心交换机：「Must be configured for redundancy. Uplinks of 10GB or higher (include all accessories, SFPs, transceivers, management modules)」——Alan 当天群发 CENTEC 核心/汇聚（OEM Core Switching Solution）引来的 | 事实（用户表） |
| 用户备注（Remark） | Tina 连要两次电话号（「don't just send email」），Alan 答「we just talk on emails and do not do personal contact」，她回「then let's end our conversation here」——线索当场断。国内客户按《计划》走私账、不在重点区域；留 C 只做记录：Saga 对外不留电话是规矩，但国内买家要电话是常态，这类要么私账跟、要么放 | 事实（用户表） |
| 用户分档（Category） | 国内光通信贸易商（为其客户找核心交换机） | 事实（用户表） |
| 所在清单 | 补录、Q-44复跑、国内 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-24）**　网站状态：无网站线索（163 邮箱）
- **是谁**：国内光通信贸易商。Alan 2026-01-20 群发 CENTEC 核心/汇聚（OEM Core Switching Solution），Tina 回问公司在哪、有没有带冗余配置的核心交换机（10G 以上上联，含 SFP/光模块/管理模块），随后两次要电话，Alan 答只走邮件，她回「那就到此为止」。
- **类型**：国内贸易商（替其客户采购）
- **规模**：未知
- **【mail】有具体需求（冗余核心、10G+ 上联、含配件）**
  > Do you have Core Switches, Must be configured for redundancy. Uplinks of 10GB or higher (Include all accessories, SFPs, Transceivers, and management modules required)
  > 来源：gmail_a k=2fbf61891a3405e7（抓取 2026-01-20）
- **【mail】因不给电话而断**
  > If you think you just can do the biz via email. then let's end our conversation here.
  > 来源：gmail_a k=9934d8c01aedb256（抓取 2026-01-20）
- **KP**：Tina（业务）huili0126@163.com +86 15989404908〔gmail_a 2026-01-20 签名〕
- 备注：Q-44 A+S 复跑补录（第 64 批）。国内、非重点区域，留 C 作记录。值得 Simon 知道的一点：这条线索是被「只走邮件、不留电话」的规矩断掉的——对国内买家，要么私账接电话，要么就别发。


## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 联系方式（已有 · 原值照录）

- 邮箱：`huili0126@163.com`〔免费邮箱；来源：用户表原值〕
- 电话：`+8615989404908`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Tina
- 职位（原值）：业务
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Tina | 业务 | huili0126@163.com / +86 15989404908 | 调研核实（公开页） | gmail_a 2026-01-20 签名 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；仅免费邮箱：可发，但优先找官网公开的企业邮箱（见调研 KP）

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 补录客户.jsonl#(补录):16 | AS-补录-2026-10-24-02 | ZhenHui Optical（Tina，163 邮箱） | 中国 | Tina | 补录：A 邮箱有人工往来但不在客户表（Q-44 A+S 复跑，T29-U45 第 64 批） | 2026-01-20 问核心交换机：「Must be configured for redundancy. Uplinks of 10GB or higher (include all accessories, SFPs, transceivers, management modules)」——Alan 当天群发 CENTEC 核心/汇聚（OEM Core Switching Solution）引来的 | huili0126@163.com +86 15989404908 | Tina 连要两次电话号（「don't just send email」），Alan 答「we just talk on emails and do not do personal contact」，她回「then let's end our conversation here」——线索当场断。国内客户按《计划》走私账、不在重点区域；留 C 只做记录：Saga 对外不留电话是规矩，但国内买家要电话是常态，这类要么私账跟、要么放 业务 | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：中国大陆（非出口客户）。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-3418,B,理由` 后重跑即可。

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
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **不合格（见 C 级细分）→ 不主动跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 公司网站（表内无域名，无法核实是否仍在运营）
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

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 -15）

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
