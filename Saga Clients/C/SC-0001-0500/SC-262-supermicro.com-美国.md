# supermicro.com
**官方名称（调研核实）**：Super Micro Computer, Inc.（美国 San Jose；服务器巨头）— 3 位具名 KP：Michael Chao、Elizabeth Wang (Arch)、Deepali Velayuthan（Global Director BD）

> **评级 C**　|　美国　|　档案编号 `SC-262`　|　优先级 —　|　状态：有回复·跟进中
>
> **类型**：服务器/边缘计算巨头（疑为户外边缘机柜内嵌 PoE 板需求）（推断）　|　**历史关系**：实质回复 1 次；推送 1 次（2025-09-18 → 2025-09-18）　|　**所在清单**：A已回复　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-262
rating: C
rating_auto: C
name_official: "Super Micro Computer, Inc.（美国 San Jose；服务器巨头）— 3 位具名 KP：Michael Chao、Elizabeth Wang (Arch)、Deepali Velayuthan（Global Director BD）"
score: 31
country: 美国
region: 北美
website: supermicro.com
type: 服务器/边缘计算巨头（疑为户外边缘机柜内嵌 PoE 板需求）
tier_tags: ["A已回复"]
deal: no
replies: 1
followups: 1
first_contact: 2025-09-18
last_contact: 2025-09-18
s_mail: 12 msgs (out 8 / in 4), 2025-06-18 -> 2026-03-30
p1: 无现成；最接近 = 工业 5 口 DIN（STI-054GP 4×GE PoE + 1×GE 上联, -40~+75℃）；Microfit 板级需定制
price_tier: 30%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：A 邮箱群发 8 封；2025-09-18「Mini Industrial PoE Switch」群发引出 2 人同日真回：Michael Chao 问输入电源/温度/户外合规；Elizabeth Wang 问 -34~74℃ 户外机柜能否；Alan 09-19 答 -40~+75℃ + IP40 + 测温照片；Elizabeth 09-23 追问「3× 10/100/1000M + 802.3at PoE with Microfit Connector」有没有、公司介绍、认证、产地 → Alan 09-23 答「无现成型号，可开发，需评估数量/技术可行性」+ CE/FCC/RoHS/REACH/UKCA + 广东制造 → 无回；11-06、2026-03-30 两次推送无回。巨头规则（supermicro.com 在 GIANT_DOMAINS）自动 C。（调研 2026-10-24；表内兴趣：核心交换机）
- **为什么是 C 级**：+22 实质回复 1 次；+18 在「已回复」名单（A/E Replied）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国；+5 最近活动 2025；-45 巨头/品牌厂商/运营商/军工（INH 规则：体量不匹配或非客户）；C 级细分：体量过大/品牌厂商/运营商
- **历史互动**：实质回复 1 次；推送 1 次（2025-09-18 → 2025-09-18）；最近一次客户回复：2025-09-18：INFO
- **P1**：不推（C 级）；若对方主动来询，起手 无现成；最接近 = 工业 5 口 DIN（STI-054GP 4×GE PoE + 1×GE 上联, -40~+75℃）；Microfit 板级需定制（深挖对位：ODM 板级 + 巨头准入 + 无 UL：三重门槛；只值一封收尾信问数量与 UL 是否硬条件）
- **最大未知**：年走量与现供应商
- **下一步**：2026-11 A 邮箱 → elizabethwang@supermicro.com（回 2025-09-23 原线程「Mini Industrial PoE Switch」），抄 michaelc@ 一封收尾信（巨头例外档，仅此一封）：承认上次停在「要数量」；给最接近的现成品（STI-054GP 4×GE PoE + 1×GE 上联 -40~+75℃）作参照；问三件事：需求是否还在、数量级、UL 是否硬条件（Saga 认证为 CE/FCC/RoHS/REACH/UKCA，无 UL——先说清，别让对方浪费时间）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SC-262` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（A 邮箱 8 去 4 来：2025-09-18/23 三位具名 KP 围绕「户外机柜内 3 口 GE PoE Microfit 板」连问 4 封；Alan 两次答复后对方不回；巨头规则 C）** ｜ 类型：巨头 ODM 试探 ｜ 筛子：3（规格层面，无数量） ｜ 停点：我们答「可开发但要数量」——他们没给；UL 没谈到就断了 ｜ 复活：一封收尾信：问需求是否还在 + 数量级 + UL 是否硬条件；仅此一封 ｜ 通路：美国（主攻）；巨头例外档 ｜ 节奏：一次收尾，之后不群发 ｜ 证据：gmail_a 2025-06-18 → 2026-03-30；digest in 4 / out 8；flags giant=1
- **现状一句话**：Supermicro 工程/架构侧 2025-09 问 -34~74℃ 户外机柜用的 3 口 GE 802.3at PoE 板（Microfit 连接器）；Alan 答无现成可开发、认证 CE/FCC/RoHS/REACH/UKCA、广东制造；对方未给数量，13 个月无回。
- **对方真实需求（有据）**：嵌入式/板级 3×GE PoE at 交换（Microfit 连接器），宽温 -34~74℃，户外机柜内；供应商资质（认证、产地、公司背景）。
- **断点 / 为什么停在这里**：「需要数量才能评估」+ 无 UL——美国巨头准入的两道门，一道没过。
- **Saga 现在该推什么**：P1 **无现成；板级定制（SmartByte/HRUI 工业线评估）；最近似现成品 STI-054GP（4×GE PoE + 1×GE RJ45 上联，-40~+75℃，主表 $42.9）**（30% 档，档位：OEM 30%（ODM，板级定制按项目另议）｜STI-054GP $42.9 EXW（主表 @6.69；2025 对 SB-164 报过 $33）；板级定制无价）——巨头规则 C（Q-55 默认不升）；需求真实但三重门槛（板级定制 / 巨头准入 / 无 UL）——收尾信只问三件事：还在不在、数量级、UL 是否硬条件；任何一个答案为否即停｜已发资料（勿重发）：测温照片 ×4 + Outdoor Cabinet.png(2025-09-19)、PROFILE_Saga Telecom.pdf(2025-09-23)、Product Link_2026Q2(2026-03-30)
  - 复购/在买项：若；成；为；板；级；供；应；商； ；=； ；年；量；级；；；概；率；低
  - 做不了 / 要先核的：数；量；；；U；L； ；要；求；；；用；在；哪；款；产；品；；；三；位； ；K；P； ；谁；拍；板
- **下一步（具体）**：2026-11　A 邮箱 → elizabethwang@supermicro.com（回 2025-09-23 原线程「Mini Industrial PoE Switch」），抄 michaelc@　一封收尾信（巨头例外档，仅此一封）：承认上次停在「要数量」；给最接近的现成品（STI-054GP 4×GE PoE + 1×GE 上联 -40~+75℃）作参照；问三件事：需求是否还在、数量级、UL 是否硬条件（Saga 认证为 CE/FCC/RoHS/REACH/UKCA，无 UL——先说清，别让对方浪费时间）
  - 第一问（只问一个）：Elizabeth — picking up the 3×GE 802.3at PoE / Microfit board from September 2025: is that requirement still live, and roughly what annual quantity? One thing to say up front: our certifications are CE/FCC/RoHS/REACH/UKCA, not UL — if UL is mandatory for that cabinet, tell me and we both save time.

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-09-18 | 来 | Michael Chao | May I know the input power and temperature specification? Any compliance for outdoor use? | 工程侧第一问 | `q` |
| 2025-09-18 | 来 | Elizabeth Wang (Arch) | Do you have something which can survive under -34 to 74 degrees which can survive inside outdoor cabinet? | 户外机柜宽温 | `q` |
| 2025-09-19 | 去 | Alan | our industrial models stand in -40 to 75 degrees. Please see attached photos… our industrial models are IP40-rated and commonly used in outdoor cabinets. | 口径正确（-40~+75 / IP40） | `reply` |
| 2025-09-23 | 来 | Elizabeth Wang (Arch) | Do you have " 3X 10/100/1000M Ethernet Ports, 802.3at PoE with Microfit Connector" ? Can you tell me more about Saga Telecom ? What kind of certification have you passed for your product? Where do you manufacture? | 板级规格 + 供应商资质三问 | `rfq` |
| 2025-09-23 | 去 | Alan | there is no ready model for this specification, we can develop it. But need to evaluate it, like the quantity you need, future demand, technical feasibility etc.… CE/FCC/RoHS/Reach/UKCA… manufactured in Guangdong province | 答复后无回——断点 | `reply` |
| 2025-11-06 | 去 | Alan | （Re: Mini Industrial PoE Switch 推送 Booster PoE Switch.png） | 与板级需求无关的推送 | `push` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：数量 / 目标产品；UL 是否硬条件；Deepali（BD 总监）只出现过自动回复，是否知情不明

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | supermicro.com（取自域名，公司全名待核） | 推断 |
| 国家 | 美国 | 事实（用户表）|
| 网站/域名 | supermicro.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 服务器/边缘计算巨头（疑为户外边缘机柜内嵌 PoE 板需求） | 推断（据兴趣/备注关键词） |
| 联系人 | Elizabeth | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | 核心交换机 | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | A已回复 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-24）**　网站状态：正常（supermicro.com）
- **是谁**：A 邮箱群发 8 封；2025-09-18「Mini Industrial PoE Switch」群发引出 2 人同日真回：Michael Chao 问输入电源/温度/户外合规；Elizabeth Wang 问 -34~74℃ 户外机柜能否；Alan 09-19 答 -40~+75℃ + IP40 + 测温照片；Elizabeth 09-23 追问「3× 10/100/1000M + 802.3at PoE with Microfit Connector」有没有、公司介绍、认证、产地 → Alan 09-23 答「无现成型号，可开发，需评估数量/技术可行性」+ CE/FCC/RoHS/REACH/UKCA + 广东制造 → 无回；11-06、2026-03-30 两次推送无回。巨头规则（supermicro.com 在 GIANT_DOMAINS）自动 C。
- **类型**：服务器/边缘计算巨头（疑为户外边缘机柜内嵌 PoE 板需求）
- **规模**：巨头
- **【邮件】工程侧问输入电源/温度/户外合规**
  > May I know the input power and temperature specification? Any compliance for outdoor use?
  > 来源：data/gmail_a/messages/<year>/<month>.jsonl（抓取 2025-09-18）
- **【邮件】-34~74℃ 户外机柜**
  > Do you have something which can survive under -34 to 74 degrees which can survive inside outdoor cabinet?
  > 来源：data/gmail_a/messages/<year>/<month>.jsonl（抓取 2025-09-18）
- **【邮件】具体规格：3×GE 802.3at PoE + Microfit 连接器（板级）**
  > Do you have " 3X 10/100/1000M Ethernet Ports, 802.3at PoE with Microfit Connector" ? Can you tell me more about Saga Telecom ? What kind of certification have you passed for your product? Where do you manufacture?
  > 来源：data/gmail_a/messages/<year>/<month>.jsonl（抓取 2025-09-23）
- **KP**：Elizabeth Wang (Arch)（）elizabethwang@supermicro.com 〔data/gmail_a/messages/<year>/<month>.jsonl〕
- **KP**：Michael Chao（）michaelc@supermicro.com 408-817-0345（信尾）〔data/gmail_a/messages/<year>/<month>.jsonl〕
- **KP**：Deepali Velayuthan（）deepaliv@supermicro.com 〔data/gmail_a/messages/<year>/<month>.jsonl〕
- 备注：巨头规则 → C 不动（Q-55 默认）；但需求是真的：3 口 GE 802.3at PoE + Microfit 连接器 = 板级/嵌入式 PoE 交换（装进他们的户外边缘机柜/设备），-34~74℃。Saga 的回答停在「可开发，需数量」——他们没给数量。美国巨头几乎必问 UL（Saga 无 UL，《背景信息》不做 UL）→ 天然断点。

### 加厚挖掘（2026-10-24 · 邮件证据 + 官网常识）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Super Micro Computer, Inc. |
| 成立 | 1993 |
| 总部/地址 | San Jose, CA |
| 其他 | 服务器/存储/边缘计算 |

- **触达通道（公开）**：role: 工程/架构/BD 三线；region: 美国
- **风险/边界**：UL/供应商准入（美国巨头）——Saga 无 UL；板级定制需 SmartByte/HRUI 评估，数量不明；3 位 KP 分属不同部门，内部决策链不明
- **Saga 对位结论**：P1 无现成；最接近 = 工业 5 口 DIN（STI-054GP 4×GE PoE + 1×GE 上联, -40~+75℃）；Microfit 板级需定制（30% 档）——ODM 板级 + 巨头准入 + 无 UL：三重门槛；只值一封收尾信问数量与 UL 是否硬条件
- **邮件切入句（英文）**：（见 mail_review.draft_en）

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 1 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-09-18 | 2025.9.18 | 22mini | INFO | A |  | A Replied 09.04.xlsx#22 |

## 联系方式（已有 · 原值照录）

- 邮箱：`elizabethwang@supermicro.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`deepaliv@supermicro.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`michaelc@supermicro.com`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Elizabeth
- 网站/域名：supermicro.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Elizabeth Wang (Arch) | — | elizabethwang@supermicro.com | 调研核实（公开页） | data/gmail_a/messages/<year>/<month>.jsonl |
| Michael Chao | — | michaelc@supermicro.com / 408-817-0345（信尾） | 调研核实（公开页） | data/gmail_a/messages/<year>/<month>.jsonl |
| Deepali Velayuthan | — | deepaliv@supermicro.com | 调研核实（公开页） | data/gmail_a/messages/<year>/<month>.jsonl |
| Elizabeth | — | elizabethwang@supermicro.com / deepaliv@supermicro.com | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A Replied 09.04.xlsx#总表:23 | 22 | https://www.supermicro.com/en/products/networking/switches | 美国 | Elizabeth | 谷歌 | 核心交换机 | ElizabethWang@supermicro.com<br>deepaliv@supermicro.com<br>michaelc@supermicro.com |  | 1 条 |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：体量过大/品牌厂商/运营商。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SC-262,B,理由` 后重跑即可。

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
| 采购量/预算 | ❓ 未确认（有回复但未报量） |
| 商业资格结论 | **不合格（见 C 级细分）→ 不主动跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: Mini Industrial PoE Switch — the 3×GE PoE / Microfit board, one year later

```text
Hi Elizabeth,

Last September we stopped at "we can develop it, but we need the quantity". Picking that up properly:

- Nearest ready unit for reference: a 4 x GE 802.3at PoE + 1 x GE uplink industrial switch, -40 to +75 C, IP40 (tested photos were in my September mail). A 3 x GE board-level version with a Microfit connector is a custom build on the same platform.
- Certifications up front: CE/FCC/RoHS/REACH/UKCA. We do not hold UL. If UL is mandatory for that outdoor cabinet, please tell me and we both save time.

One question: is the requirement still live, and roughly what annual quantity are we talking about? That is the one number the engineering evaluation needs.

Thank you.
Alan
Saga Telecom - sagatele.com
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- 不复核。对方主动来询 → 在 `data/saga_clients/人工定级.csv` 写一行升级后重跑。

## 变更日志

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 31）

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
