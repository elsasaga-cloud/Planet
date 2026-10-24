# Fikes Media

> **评级 B**　|　美国　|　档案编号 `SB-1336`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：媒体/IT 集成小公司（业主直营）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：补录、S邮箱回复、OEM意向、待回复　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-1336
rating: B
rating_auto: B
rating_research: B  # 具名 Owner 实质回复 + OEM 意向，但规模小、API 诉求未必能满足、追问未回 → B
name_official: "Fikes Media"
score: 58
country: 美国
region: 北美
website: fikesmedia.com
type: 媒体/IT 集成小公司（业主直营）
tier_tags: ["补录", "S邮箱回复", "OEM意向", "待回复"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 4 msgs (out 3 / in 1), 2026-10-03 -> 2026-10-19
p1: STC-424XGGPM-280W
price_tier: 30%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：美国小公司（Owner Christopher Fikes，电话区号 409 = 德州 Beaumont 一带），2026-10-03 回复群发表示有兴趣，关心 OEM 定制层级与控制器 API 集成；Simon 10-04 发完整 OEM 清单 + MIB + 规格书 + CLI/Web 手册并反问控制器架构，10-19 追问样品，客户未回。S 邮箱 4 封。（调研 2026-10-22；表内兴趣：24 口 PoE L2+（STC-424XGGPM-280W）的 OEM 定制 + 控制器 API 集成（REST/SNMP/CLI 待明确））
- **为什么是 B 级**：**调研后定级 B**（具名 Owner 实质回复 + OEM 意向，但规模小、API 诉求未必能满足、追问未回 → B）；自动分级 B：+10 谈到样品/测样；+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国；+5 最近活动 2026
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-22）**：STC-424XGGPM-280W — OEM 自有品牌 → 30% 档；控制器集成只能承诺 SNMP/CLI，先把这一点说死再谈样机；$196.3 USD EXW（CNY 1010 ×1.3；Simon 群发价 $180 可作首单价）
- **第一问（只问一个）**：Which controller or NMS do you plan to integrate with - would SNMP + SSH-CLI automation cover it, or is a REST API a must?
- **最大未知**：年走量与现供应商
- **下一步**：本周一封，之后不追 S 邮箱同线程 直接回答 API 问题（有 SNMP v1/v2c/v3 + SSH CLI，可用脚本/Ansible 管理；无 REST / 云），附 MIB 文件已给；样机 2 台 $180 抵首单

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-22）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-1336` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-22。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **现状一句话**：德州 Fikes Media（业主 Christopher Fikes）2026-10-03 回群发：「This actually does have my interest. What levels of customization are offered? I would be interested if there was **api availability for controller integration**」；Simon 10-04 发完整 OEM 菜单 + 规格书 + MIB + CLI/Web 手册并反问 API 类型；10-19 追「arrange 2 samples?」无回应。
- **对方真实需求（有据）**：可贴牌的 24 口 PoE 交换机 + **能被自家控制器集成的 API**（他是小型媒体/IT 服务商，想做自有品牌的可控网络）。
- **断点 / 为什么停在这里**：Saga/SmartByte 线没有 REST API 和云控制器，只有 SNMP + CLI/SSH + Web；Simon 10-04 的回复把问题抛回去（REST / SNMP / NETCONF?），对方没接。真实答案应直接给：SNMP + SSH-CLI 可脚本化，无 REST。
- **Saga 现在该推什么**：P1 **STC-424XGGPM-280W**（30% 档，$196.3 USD EXW（CNY 1010 ×1.3；Simon 群发价 $180 可作首单价））——OEM 自有品牌 → 30% 档；控制器集成只能承诺 SNMP/CLI，先把这一点说死再谈样机
  - 做不了 / 要先核的：无 REST API / 无云控制器（Q-19 口径）；SNMP 私有 MIB 应在 Saga 自己的 PEN 下（Q-35）；OEM 菜单里的「SNMP OID customization」措辞按 §9 改
- **下一步（具体）**：本周一封，之后不追　S 邮箱同线程　直接回答 API 问题（有 SNMP v1/v2c/v3 + SSH CLI，可用脚本/Ansible 管理；无 REST / 云），附 MIB 文件已给；样机 2 台 $180 抵首单
  - 第一问（只问一个）：Which controller or NMS do you plan to integrate with - would SNMP + SSH-CLI automation cover it, or is a REST API a must?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-10-03 | 来 | Christopher Fikes, Owner | This actually does have my interest. What levels of customization are offered? I would be interested if there was api availability for controller integration. | 唯一来信：OEM + API | `af638fab0ab5ad29` |
| 2026-10-19 | 去 | Simon → Christopher | Any feedback about our product information? Maybe arrange 2 samples for testing? | 追样无回 | `4575b20b172d85a4` |

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Fikes Media | 事实（用户表） |
| 国家 | 美国 | 事实（用户表）|
| 网站/域名 | fikesmedia.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 媒体/IT 集成小公司（业主直营） | 推断（据兴趣/备注关键词） |
| 联系人 | Christopher Fikes | 事实（用户表） |
| 来源（From） | 补录：S 邮箱 2026-10 群发（Apollo 名单）回复客户（T29-U10 复盘发现） | 事实（用户表） |
| 兴趣（Interested in） | 24 口 PoE L2+（STC-424XGGPM-280W）的 OEM 定制 + 控制器 API 集成（REST/SNMP/CLI 待明确） | 事实（用户表） |
| 用户备注（Remark） | S 邮箱 4 封（2026-10-03 → 10-19）：10-03 回复「This actually does have my interest. What levels of customization are offered? …api availability for controller integration」；10-04 Simon 发 OEM 清单（logo/包装/面板/标签/型号/序列号/手册/默认 IP/SNMP OID/Web 语言）+ MIB 文件 + 规格书 + CLI/Web 手册并反问控制器架构；10-19 Simon 追问样品，客户未回；详见 research JSON | 事实（用户表） |
| 用户分档（Category） | 媒体/IT 集成小公司（业主直营） | 事实（用户表） |
| 所在清单 | 补录、S邮箱回复、OEM意向、待回复 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-22）**　网站状态：未核（本轮只用 S 邮箱证据）
- **是谁**：美国小公司（Owner Christopher Fikes，电话区号 409 = 德州 Beaumont 一带），2026-10-03 回复群发表示有兴趣，关心 OEM 定制层级与控制器 API 集成；Simon 10-04 发完整 OEM 清单 + MIB + 规格书 + CLI/Web 手册并反问控制器架构，10-19 追问样品，客户未回。S 邮箱 4 封。
- **类型**：媒体/IT 集成小公司（业主直营）
- **规模**：小（Owner 直接回信）
- **【email】有兴趣 + 问 OEM 层级 + 要 API/控制器集成**
  > This actually does have my interest. What levels of customization are offered? I would be interested if there was api availability for controller integration. If you have some specification sheets and models available I would love to see them.
  > 来源：data/gmail_s/messages/2026/2026-10.jsonl（抓取 2026-10-03）
- **【email】Simon 回复的 OEM 菜单（可复用口径）**
  > Company logo / Packaging / Front panel (PVC mask) / Product label / Model name / Serial number / User manual / Default login IP / SNMP OID customization / Web GUI language… firmware customization for specific project requirements, subject to technical evaluation（附 SWITCH-MIBS-release.docx、Saga Feature List_7.5.x_L2+.xlsx、STC-424XGGPM-280W.docx、CLI/Web Manual）
  > 来源：data/gmail_s/messages/2026/2026-10.jsonl（抓取 2026-10-04）
- **【email】Simon 追问样品，未回**
  > Any feedback about our product information? Maybe arrange 2 samples for testing?
  > 来源：data/gmail_s/messages/2026/2026-10.jsonl（抓取 2026-10-19）
- **KP**：Christopher Fikes（Owner）cfikes@fikesmedia.com 409.877.4220〔S 邮箱签名〕
- **调研后定级**：B（原自动 B）——具名 Owner 实质回复 + OEM 意向，但规模小、API 诉求未必能满足、追问未回 → B
- 备注：API/控制器集成是关键未知：Saga 线（SmartByte Marvell AC5）有 SNMP/CLI/Web，无云控制器 REST API——下一封应直说 SNMP + CLI 自动化可做、REST/云控不做，别吊着。


## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：4 封（去 3 / 来 1）　|　**期间**：2026-10-03 → 2026-10-19　|　**最后去信**：2026-10-19
- **对方邮箱**：cfikes@fikesmedia.com、sales@fikesmedia.com
- **最后一封来信**：2026-10-03 cfikes@fikesmedia.com「Re: 24 Port PoE Managed Switch」：This actually does have my interest. What levels of customization are offered? I would be interested if there was api availability for controller integration. If you have some specification sheets and models available I would love to see them. Thank you Christ

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 24 Port PoE Managed Switch | 2026-10-03 | 2026-10-19 | 1 | 3 | 9 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-23T04:20:51Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-1336/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://fikesmedia.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 2761 字符；首行：Home |

## 联系方式（已有 · 原值照录）

- 邮箱：`cfikes@fikesmedia.com`〔企业邮箱；来源：用户表原值〕
- 电话：`+4098774220`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Christopher Fikes
- 职位（原值）：Owner
- 网站/域名：fikesmedia.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Christopher Fikes | Owner | cfikes@fikesmedia.com / 409.877.4220 | 调研核实（公开页） | S 邮箱签名 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 补录客户.jsonl#(补录):9 | GM-002 | Fikes Media | 美国 | Christopher Fikes | 补录：S 邮箱 2026-10 群发（Apollo 名单）回复客户（T29-U10 复盘发现） | 24 口 PoE L2+（STC-424XGGPM-280W）的 OEM 定制 + 控制器 API 集成（REST/SNMP/CLI 待明确） | cfikes@fikesmedia.com O: 409.877.4220 https://www.fikesmedia.com | S 邮箱 4 封（2026-10-03 → 10-19）：10-03 回复「This actually does have my interest. What levels of customization are offered? …api availability for controller integration」；10-04 Simon 发 OEM 清单（logo/包装/面板/标签/型号/序列号/手册/默认 IP/SNMP OID/Web 语言）+ MIB 文件 + 规格书 + CLI/Web 手册并反问控制器架构；10-19 Simon 追问样品，客户未回；详见 research JSON Owner | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-424XGGPM-280W | 深挖对位：明确问 OEM 定制 → OEM/ODM 30% 档；若只是自用/项目则 25% | $196.3 USD EXW（30% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（媒体/IT 集成小公司（业主直营）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $151.6 USD EXW（30% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-424XGGPM-280W 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：北美主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STC-424XGGPM-280W 按 30% 档报价，做现供应商的第二货源；规模（调研）：小（Owner 直接回信）
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
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: 24 Port PoE Managed Switch - straight answer on API / controller integration

```text
Hi Christopher,

A straight answer to your API question, so you can decide quickly:

- Available today: SNMP v1/v2c/v3 (full private MIB supplied), SSH CLI and Telnet for scripted automation (Ansible / Python work fine), syslog, and a Web GUI that can carry your logo and model name.
- Not available: a REST API or a cloud controller. If your controller needs REST, we are not the right fit and I would rather say so now.

If SNMP + CLI is enough, two evaluation units of the STC-424XGGPM-280W at USD 180 each (credited to your first order) can ship within a week.

One question: which controller or NMS are you integrating with?

Best regards,
Simon
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-23**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 58）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
