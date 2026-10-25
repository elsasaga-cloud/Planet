# arnoldomohr@gmail.com
**官方名称（调研核实）**：Arnoldo Beltetón Mohr（Solution Architect / Project Manager；gmail；国别未填，姓氏 Beltetón 常见于危地马拉——待证）

> **评级 B**　|　未填　|　档案编号 `SC-2186`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：方案商 / 项目经理（为终端客户找 Cisco 替代）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：DC线索　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-2186
rating: B
rating_auto: C
rating_research: B  # 5 封实质来信（2026-01 ×2、03 ×3），带终端客户具体型号（C9300L-48P-4X 等价 + 堆叠）进入 CENTEC STH1G 选型，停在「
name_official: "Arnoldo Beltetón Mohr（Solution Architect / Project Manager；gmail；国别未填，姓氏 Beltetón 常见于危地马拉——待证）"
score: -18
country: 未填
region: 未知
website: none
type: 方案商 / 项目经理（为终端客户找 Cisco 替代）
tier_tags: ["DC线索"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 26 msgs (out 21 / in 5), 2024-06-16 -> 2026-03-12
p1: STH-2QX4DX48GP-HSI（CENTEC STH1G，48×PoE++ + 4×25G + 2×40G，堆叠 ≤8）
price_tier: 30%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：A 邮箱 2025-04 起 8 轮群发；2026-01-15 对「OEM Core Switching Solution」真回：CENTEC「could be a great alternative in our market」，2 月有高端交换机项目；2026-03-10 带客户需求来：若干台 Cisco C9300L-48P-4X 等价物（48×1G PoE+ + 4×10G SFP+），要堆叠（StackWise-320，8 台 / 320 Gbps）；Alan 03-11 二选一（无堆叠→STC-448XGGPM；要堆叠→CENTEC STH-2QX4DX48GP-HSI，附 STH1G Series.pdf），03-12 给出堆叠参数（最多 8 台、360 Gbps、2×40G+4×25G 光口堆叠、链/环）并问数量 → 至今无回（7 个月）。（调研 2026-10-24；表内兴趣：—）
- **为什么是 B 级**：**调研后定级 B**（5 封实质来信（2026-01 ×2、03 ×3），带终端客户具体型号（C9300L-48P-4X 等价 + 堆叠）进入 CENTEC STH1G 选型，停在「数量？」；gmail 地址导致自动 C，按证据升 B（慢慢跟进）。）；自动分级 C：+0 数据中心交换机线索（Hohunet/CENTEC 线）；+0 仅免费邮箱；-15 只有免费邮箱、无公司名无网站（个人买家特征）；-3 区域 未知/未填
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STH-2QX4DX48GP-HSI（48×PoE++ 90W + 4×25G + 2×40G，双热插拔 1200W，堆叠 ≤8）；预算紧则 STH-2QX4DX48GP-SFI（PoE+ 30W，单电源） — 对外统一口径（#1）：接入 AC5 不堆叠；可堆叠 48 口 PoE 只能是 CENTEC STH1G（ST 许可，≤8 台）——这户是仓内把 STH1G 谈到参数层面的唯一客户｜已发资料（勿重发）：STH1G Series.pdf、Vastlake/STOS 链接（2026-03-11/12）｜档位说明（原 tier 字段文字「OEM 30%（方案商 / 私标）——CENTEC 底线 ≥35% 并行」移此）：OEM 30%（方案商 / 私标）——CENTEC 底线 ≥35% 并行；他见过的实价：STC-2224GFP-24V $90（2024-11-24 样品价）；仓内无 STH1G 价；CENTEC 线已有价仅 32C $6,000 / 2C6QX $1,200 / 8C48DX $4,800 EXW（2026 Q2）
- **第一问（只问一个）**：Arnoldo — is the C9300L-48P-4X replacement still open, and roughly how many units (8-unit stacks × how many sites)? With that I can give you the EXW price for STH-2QX4DX48GP-HSI rather than a datasheet.
- **最大未知**：公司网站（表内无域名，无法核实是否仍在运营）；具体需求型号（表内兴趣列为空）
- **下一步**：2026-11 A 邮箱 → arnoldomohr@gmail.com（回 2026-03-12 原线程「OEM Core Switching Solution」） 一封对表信：STH-2QX4DX48GP-HSI 对 C9300L-48P-4X 四行对表（PoE 预算、上联、堆叠 8 台/360G、L3 特性），价格先给「按数量报」而不是空着——Simon 需先定 STH1G 的 EXW 区间（仓内无价）；只问一个问题：项目还在不在 + 数量级别（第 76 批(b) 2026-10-25：audit_ab 硬错误修正：tier 字段规范为数字）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SC-2186` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（A 邮箱 5 封实质来信：2026-01-15/01-19 对 CENTEC 表兴趣 + 2 月项目；03-10/03-11 带终端客户 C9300L-48P-4X 等价 + 堆叠 8 台需求；Alan 03-12 给 STH-2QX4DX48GP-HSI 堆叠参数并问数量 → 无回 7 个月）；Elsa 1:1 去信 1 封（2025-02-18「16 Port Ethernet Switch」DIN 16 口千兆稿，To 仅 arnoldomohr@gmail.com，头 19518491f1515deb 无 Bcc，称呼「Hi, Mr. Arnoldo」）——他 2026-01 才在 A 邮箱主动写 CENTEC，比 Elsa 这封晚 11 个月；全箱 `from:e.sagatelecom to:arnoldomohr@gmail.com` 仅此 1 条，complete** ｜ 类型：方案商（为终端客户选型） ｜ 筛子：4~5（具体型号 + 堆叠参数层面） ｜ 停点：停在「what is the quantity you need?」（2026-03-12 去）——他要先回客户，后无音；STH1G 无价也让我们没法主动给数 ｜ 复活：一封「STH1G 对 C9300L 对表 + 一个问题」；不发新品群发 ｜ 通路：拉美（疑危地马拉）非主攻；CENTEC 敲门砖案例 ｜ 节奏：季度 ｜ 证据：gmail_a 2026-01-15 → 2026-03-12（17 封：9 群发、3 实质去信、5 来信）；附件 STH1G Series.pdf（2026-03-11 去，sha df9670bdd28f51ac）；digest in 5 / out 21
- **现状一句话**：方案商 Arnoldo（Solution Architect）2026-01 对 CENTEC 感兴趣，03-10 带来终端客户需求：若干台 Cisco C9300L-48P-4X 等价（48×1G PoE+ + 4×10G SFP+），03-11 明确要堆叠（8 台 / StackWise-320）。Alan 当天给出二选一，03-12 锁定 CENTEC STH-2QX4DX48GP-HSI 并给堆叠参数，问数量——此后无回。
- **对方真实需求（有据）**：Cisco C9300L-48P-4X 的可堆叠等价物（48×PoE+ + 10G 上联，8 台堆叠），要价格和数量级别的对表。
- **断点 / 为什么停在这里**：我们问「数量」时没给价，他回客户拿不到数就断了；且 STH1G 仓内无价，Simon 得自己定一个区间才能重启。
- **Saga 现在该推什么**：P1 **STH-2QX4DX48GP-HSI（48×PoE++ 90W + 4×25G + 2×40G，双热插拔 1200W，堆叠 ≤8）；预算紧则 STH-2QX4DX48GP-SFI（PoE+ 30W，单电源）**（30% 档，他见过的实价：STC-2224GFP-24V $90（2024-11-24 样品价）；仓内无 STH1G 价；CENTEC 线已有价仅 32C $6,000 / 2C6QX $1,200 / 8C48DX $4,800 EXW（2026 Q2））——对外统一口径（#1）：接入 AC5 不堆叠；可堆叠 48 口 PoE 只能是 CENTEC STH1G（ST 许可，≤8 台）——这户是仓内把 STH1G 谈到参数层面的唯一客户｜已发资料（勿重发）：STH1G Series.pdf、Vastlake/STOS 链接（2026-03-11/12）｜档位说明（原 tier 字段文字「OEM 30%（方案商 / 私标）——CENTEC 底线 ≥35% 并行」移此）：OEM 30%（方案商 / 私标）——CENTEC 底线 ≥35% 并行
  - 复购/在买项：若；成；，；终；端；客；户；项；目；制；；；方；案；商；可；带；下；一；个；项；目
  - 做不了 / 要先核的：国；别；/；公；司；实；体；；；终；端；客；户；是；否；已；定；；；数；量；；；S；T；H；1；G； ；价
- **下一步（具体）**：2026-11　A 邮箱 → arnoldomohr@gmail.com（回 2026-03-12 原线程「OEM Core Switching Solution」）　一封对表信：STH-2QX4DX48GP-HSI 对 C9300L-48P-4X 四行对表（PoE 预算、上联、堆叠 8 台/360G、L3 特性），价格先给「按数量报」而不是空着——Simon 需先定 STH1G 的 EXW 区间（仓内无价）；只问一个问题：项目还在不在 + 数量级别（第 76 批(b) 2026-10-25：audit_ab 硬错误修正：tier 字段规范为数字）
  - 第一问（只问一个）：Arnoldo — is the C9300L-48P-4X replacement still open, and roughly how many units (8-unit stacks × how many sites)? With that I can give you the EXW price for STH-2QX4DX48GP-HSI rather than a datasheet.

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-11-23 | 来 | Arnoldo（arnoldomohr@gmail.com，S 邮箱） | 「Yes I need some samples for testing, can you send to me?」（回 11-15 的 24 口被动 PoE 群发） | 与 Alan 2026 年的 CENTEC/堆叠对话是同一个人——他从 2024-11 就在 S 邮箱里要样品；两年两条线都停在「要东西 → 给条件 → 无回」 | `k=2725966d7f583826（S 邮箱 2024-11-23 17:47Z Re: 24 Port Passive PoE Switch）` |
| 2024-11-24 | 去 | Simon（附 Passive PoE.pdf） | 「Its not free samples, we do not do free samples. **90usd/pc, STC-2224GFP-24V** 2×1G SFP + 2×GE 上联 + 24×100M PoE 下联，非管理，被动 PoE 300W，AC，1U，含电源线。Please let me know if you decide to proceed」+ 被动 PoE 手册《Passive PoE.pdf》（2024 版）内含价表：STC-024FP-24V $14 / 014GP-24V $20 / 028FP-24V $20 / 028GP-24V $31 / 1116CGFP-24V $51 / 2216GP-24V $84 / 2224GP-24V $92 / 0224GFP-24V $84 / 2024GP-24V $90（24V 被动 PoE，AC 输入，1U）；条款：批量 50/50，T/T 每笔 $25，PayPal 5% | 样品价 $90 给了就无回——这位的模式是「免费样品 / 高端项目」两头问，没有付费动作；2026-03 的 8 台堆叠需求也无回。下一步只回不追 | `k=c9057ef48518bc9c（S 邮箱 2024-11-24 01:46Z）；附件 sha=052eecb9f79ac4d7` |
| 2025-02-18 | out | Elsa → arnoldomohr@gmail.com | 16 Port Ethernet Switch（Elsa 1:1 第 1/1 轮；To 仅本户） | 第 74 批(o) `from:e.sagatelecom to:arnoldomohr@gmail.com` 全程 complete：1 行；To=本户 ⇒ 1:1 直收 | `elsa_1to1` |
| 2026-01-15 | 来 | Arnoldo Beltetón Mohr | The OEM switch proposal looks very interesting. I think it would be worthwhile to learn more about CENTEC, as it could be a great alternative in our market | CENTEC 敲门砖在他的市场成立 | `interest` |
| 2026-01-19 | 来 | Arnoldo | I'm interested in learning more about CENTEC, as I have a project in February that requires high-end switches | 2 月项目——Alan 01-20 答 10G~800G 都有、等规格、Simon 可谈 | `project` |
| 2026-03-10 | 来 | Arnoldo（Solution Architect） | I have a client who's requesting several switches similar to the Cisco C9300L-48P-4X… 48x1G PoE+ Base-T/4x10G SFP+/Network Essentials. I'd like to get in touch to see if we have a good option with Centec or SAGA. Do you think we can move forward and get a quote? | 终端客户型号明确；要报价 | `rfq` |
| 2026-03-11 | 去 | Alan | Need to know if your client needs "stacking" feature. This is important. If no, let's just do Marvell solution. STC-448XGGPM, 10G L3 with PoE. If yes, we need to go with CENTEC solution… STH-2QX4DX48GP-HSI. The fiber uplink is about 25G/40G, but it can be configured as 10G.（附 STH1G Series.pdf） | 二选一分叉；AC5 不堆叠的口径在此已用对 | `offer` |
| 2026-03-11 | 来 | Arnoldo | Yes, my client needs stacking, since the c9300l-48P-4X is a fixed-uplink switch that supports stacking up to 8 units using StackWise-320 technology… total stack bandwidth of 320 Gbps… if you have something equivalent or superior it's very good. | 堆叠是硬需求，标尺 = 8 台 / 320G | `need` |
| 2026-03-12 | 去 | Alan | Yes, let's do CENTEC solution… we will focus on STH-2QX4DX48GP-HSI. About stacking: 1. max 8 units; 2. bandwidth max 360Gbps, uplinks 2*40G and 4*25G; 3. fiber uplinks for stacking; 4. both chain and ring… what is the quantity you need? | 对表完成但没给价——断点 | `offer` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：国别/公司（gmail，信中只说 our market）；03-12 之后是否有 WhatsApp/会议等线外接触——仓内无；STH1G EXW 价（主表无）

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | arnoldomohr@gmail.com | 推断 |
| 国家 | 未填 | 事实（用户表）|
| 网站/域名 | — | 事实（用户表 URL/邮箱域名） |
| 类型 | 方案商 / 项目经理（为终端客户找 Cisco 替代） | 推断（据兴趣/备注关键词） |
| 联系人 | Mr. Arnoldo Beltetón / Project Manager | 事实（用户表） |
| 来源（From） | MIC | 事实（用户表） |
| 兴趣（Interested in） | — | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | DC线索 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-24）**　网站状态：无域名（gmail）
- **是谁**：A 邮箱 2025-04 起 8 轮群发；2026-01-15 对「OEM Core Switching Solution」真回：CENTEC「could be a great alternative in our market」，2 月有高端交换机项目；2026-03-10 带客户需求来：若干台 Cisco C9300L-48P-4X 等价物（48×1G PoE+ + 4×10G SFP+），要堆叠（StackWise-320，8 台 / 320 Gbps）；Alan 03-11 二选一（无堆叠→STC-448XGGPM；要堆叠→CENTEC STH-2QX4DX48GP-HSI，附 STH1G Series.pdf），03-12 给出堆叠参数（最多 8 台、360 Gbps、2×40G+4×25G 光口堆叠、链/环）并问数量 → 至今无回（7 个月）。
- **类型**：方案商 / 项目经理（为终端客户找 Cisco 替代）
- **在卖/在用品牌**：Cisco C9300L-48P-4X
- **【邮件】对 CENTEC 表兴趣：「great alternative in our market」**
  > The OEM switch proposal looks very interesting. I think it would be worthwhile to learn more about CENTEC, as it could be a great alternative in our market
  > 来源：gmail_a data/gmail_a/messages/2026/2026-01.jsonl / 2026-03.jsonl（线程 OEM Core Switching Solution）（抓取 2026-01-15）
- **【邮件】2 月有高端交换机项目**
  > I have a project in February that requires high-end switches
  > 来源：gmail_a data/gmail_a/messages/2026/2026-01.jsonl / 2026-03.jsonl（线程 OEM Core Switching Solution）（抓取 2026-01-19）
- **【邮件】终端客户要 Cisco C9300L-48P-4X 等价物并要报价**
  > client who's requesting several switches similar to the Cisco C9300L-48P-4X… 48x1G PoE+ Base-T/4x10G SFP+… get a quote?
  > 来源：gmail_a data/gmail_a/messages/2026/2026-01.jsonl / 2026-03.jsonl（线程 OEM Core Switching Solution）（抓取 2026-03-10）
- **【邮件】堆叠是硬需求（8 台 / StackWise-320）**
  > my client needs stacking… up to 8 units using StackWise-320… 320 Gbps
  > 来源：gmail_a data/gmail_a/messages/2026/2026-01.jsonl / 2026-03.jsonl（线程 OEM Core Switching Solution）（抓取 2026-03-11）
- **【邮件（去）】Alan 锁定 STH-2QX4DX48GP-HSI 并给堆叠参数，问数量**
  > max 8 units… 360Gbps… 2*40G and 4*25G… chain and ring… what is the quantity you need?
  > 来源：gmail_a data/gmail_a/messages/2026/2026-01.jsonl / 2026-03.jsonl（线程 OEM Core Switching Solution）（抓取 2026-03-12）
- **KP**：Arnoldo Beltetón Mohr（）arnoldomohr@gmail.com 〔gmail_a data/gmail_a/messages/2026/2026-01.jsonl / 2026-03.jsonl（线程 OEM Core Switching Solution）〕
- **调研后定级**：B（原自动 C）——5 封实质来信（2026-01 ×2、03 ×3），带终端客户具体型号（C9300L-48P-4X 等价 + 堆叠）进入 CENTEC STH1G 选型，停在「数量？」；gmail 地址导致自动 C，按证据升 B（慢慢跟进）。
- 备注：国别未填：信中「our market」未点名；姓氏 Beltetón 多见于危地马拉（待证）。非欧美土主攻，但是仓内唯一一个把 STH1G（CENTEC 48×1G PoE 堆叠线）谈到参数层面的客户（另一个是 SB-924 Versitron，只发未回）。

### 加厚挖掘（2026-10-24 · 仅邮件证据 · 无域名）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | （未知；gmail 联系人） |
| 总部/地址 | （未填） |
| 其他 | Solution Architect 署名；2026-03 为终端客户选型 |

- **触达通道（公开）**：role: 方案商 / 项目经理；region: （未填；疑危地马拉）
- **风险/边界**：终端客户是否已选其他品牌不明（03-12 后无回）；STH1G 仓内无价（主表/CENTEC Q2 xls 均无 STH-2QX4DX 行）——报价要 Simon 自己定；gmail 联系人，公司实体不明
- **Saga 对位结论**：P1 STH-2QX4DX48GP-HSI（CENTEC STH1G，48×PoE++ + 4×25G + 2×40G，堆叠 ≤8）（30% 档）——终端客户要 C9300L-48P-4X 可堆叠等价——接入 AC5 不堆叠，只能走 CENTEC STH1G；仓内无价。
- **邮件切入句（英文）**：（见 mail_review.draft_en）

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：26 封（去 21 / 来 5）　|　**期间**：2024-06-16 → 2026-03-12　|　**最后去信**：2026-03-12
- **对方邮箱**：arnoldomohr@gmail.com
- **最后一封来信**：2026-03-11 arnoldomohr@gmail.com「Re: OEM Core Switching Solution」：Hi Alan, Yes, my client needs stacking, since the c9300l-48P-4X is a fixed-uplink switch that supports stacking up to 8 units using StackWise-320 technology. It provides a total stack bandwidth of 320 Gbps. This allows for a total switching capacity of up to 4

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| OEM Core Switching Solution | 2026-01-15 | 2026-03-12 | 4 | 6 | 14 |
| Optional Marvell Chipset Solutions | 2025-12-04 | 2025-12-04 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-07 | 2025-11-07 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-03 | 2025-10-03 | 0 | 1 | 1 |
| 90W PoE Managed Switch | 2025-09-01 | 2025-09-01 | 0 | 1 | 1 |
| Industrial PoE Switch | 2025-07-24 | 2025-07-24 | 0 | 1 | 1 |
| Managed Optical Bypass Switch | 2025-05-30 | 2025-05-30 | 0 | 1 | 1 |
| Marvell Alleycat5 Solution | 2025-04-28 | 2025-04-28 | 0 | 1 | 1 |
| 8 Port Industrial PoE Switch | 2025-01-06 | 2025-01-06 | 0 | 1 | 1 |
| 24 Port Passive PoE Switch | 2024-11-15 | 2024-11-24 | 1 | 2 | 4 |
| 2.5G Web Managed Switch | 2024-10-17 | 2024-10-17 | 0 | 1 | 1 |
| 24V/48V PoE Switch | 2024-09-03 | 2024-09-03 | 0 | 1 | 1 |
| …共 15 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 联系方式（已有 · 原值照录）

- 邮箱：`arnoldomohr@gmail.com`〔免费邮箱；来源：用户表原值〕
- 联系人（原值）：Mr. Arnoldo Beltetón / Project Manager
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Arnoldo Beltetón Mohr | — | arnoldomohr@gmail.com | 调研核实（公开页） | gmail_a data/gmail_a/messages/2026/2026-01.jsonl / 2026-03.jsonl（线程 OEM Core Switching Solution） |
| Mr. Arnoldo Beltetón | — | arnoldomohr@gmail.com | 用户表原值 | Clients/ 表 |

- **通道建议**：仅免费邮箱：可发，但优先找官网公开的企业邮箱（见调研 KP）

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| DC Switches 08.10.xlsx#总表:21 | 20 |  |  | Mr. Arnoldo Beltetón<br>Project Manager | MIC |  | arnoldomohr@gmail.com |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STH-2QX4DX48GP-HSI（CENTEC STH1G，48×PoE++ + 4×25G + 2×40G，堆叠 ≤8） | 深挖对位：终端客户要 C9300L-48P-4X 可堆叠等价——接入 AC5 不堆叠，只能走 CENTEC STH1G；仓内无价。 | 价格待核（价格主表无此型号） | 深挖对位；档位 30%（方案商 / 项目经理（为终端客户找 Cisco 替代）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STH-2QX4DX48GP-HSI（CENTEC STH1G，48×PoE++ + 4×25G + 2×40G，堆叠 ≤8）），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STH-2QX4DX48GP-HSI（CENTEC STH1G，48×PoE++ + 4×25G + 2×40G，堆叠 ≤8） 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：名单内已有联系记录，不是零起点
- **W**：没有可靠直达通道
- **O**：P1 STH-2QX4DX48GP-HSI（CENTEC STH1G，48×PoE++ + 4×25G + 2×40G，堆叠 ≤8） 按 30% 档报价，做现供应商的第二货源
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
| 需求面成立（在卖/在用交换机或 PoE） | ❓ 表内兴趣不含交换机关键词 |
| 决策人识别 | ✅ |
| 触达通道 | ⚠️ 仅免费邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 公司网站（表内无域名，无法核实是否仍在运营）
- [ ] 具体需求型号（表内兴趣列为空）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: OEM Core Switching Solution — STH-2QX4DX48GP-HSI vs C9300L-48P-4X, is the project still open?

```text
Hi, Arnoldo,

In March we settled on the CENTEC-based STH-2QX4DX48GP-HSI as the stackable alternative to the C9300L-48P-4X, and I owe you a cleaner comparison than a datasheet:

- Access: 48 x 1G PoE++ (90 W per port, 1200 W dual hot-swap PSU) vs 48 x 1G PoE+ on the Cisco
- Uplinks: 4 x 25G SFP28 + 2 x 40G QSFP+ (25G ports can run at 10G) vs 4 x 10G SFP+
- Stacking: up to 8 units, ring or chain over the fiber ports, 360 Gbps vs StackWise-320
- Software: L3 with OSPF/BGP/PIM, VXLAN-EVPN, MPLS, MACsec, SNMP v3/CLI/Web; your own logo and model name on the unit

If the budget is tighter, the -SFI version (PoE+ 30 W, single PSU) is the lighter option.

One question: is the C9300L replacement still open, and roughly how many units (how many 8-unit stacks, how many sites)? With that I will give you the EXW unit price instead of a range.

Thank you.
Alan
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-24**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 -18）；人工/调研定级 → B

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
