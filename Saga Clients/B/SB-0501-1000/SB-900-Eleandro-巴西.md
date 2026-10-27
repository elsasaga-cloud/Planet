# Eleandro
**官方名称（调研核实）**：Eleandro（巴西；仅 WhatsApp +55 54）

> **评级 B**　|　巴西　|　档案编号 `SB-900`　|　优先级 ★★　|　状态：WhatsApp 已加·未回复
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：WhatsApp 已加；推送 6 次（2025-01-02 → 2025-10-06）　|　**所在清单**：WA跟进　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-900
rating: B
rating_auto: B
name_official: "Eleandro（巴西；仅 WhatsApp +55 54）"
score: 28
country: 巴西
region: 拉美
website: none
type: 经销/集成（类型待核）
tier_tags: ["WA跟进"]
deal: no
replies: 0
followups: 6
first_contact: 2025-01-02
last_contact: 2025-10-06
p1: STC-28DGGPM
price_tier: 25%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-27
```

## SALES BRIEF（压缩模型）

- **是谁**：巴西南里奥格兰德（+55 54）联系人 Eleandro，主动问过千兆 MC 与商用 PoE 价格；无邮箱无公司；WA 6 次无实质回复。（调研 2026-10-21；表内兴趣：主动问了GMC和商业POE价格）
- **为什么是 B 级**：+12 备注记录了对方问价/要资料/见面等互动；+15 WhatsApp 已加并有跟进表；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；-8 无邮箱，仅电话/WhatsApp；-4 区域 拉美/巴西；+5 最近活动 2025
- **历史互动**：WhatsApp 已加；推送 6 次（2025-01-02 → 2025-10-06）
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-28DGGPM — 商用 PoE 询价 → STC-28DGGPM；GMC → STI-110GE。；按主表（研究档 saga_fit）
- **第一问（只问一个）**：Are PoE / industrial switches something you still source today, or has that line been dropped?
- **最大未知**：公司网站（表内无域名，无法核实是否仍在运营）
- **下一步**：不动 — —

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-900` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未发信（S/A 邮箱均无往来；来源：用户表「兴趣：主动问了GMC和商业POE价格」）；Elsa 箱无可查地址（仓内无此户任何邮箱/域名——用户表/WhatsApp/展会名片户，`from:e.sagatelecom to:` 无从下手；Elsa 群发是否碰过他无法判定，不写「未触达」）（第 74 批(o)）** ｜ 类型：— ｜ 筛子：—（未入筛） ｜ 停点：从未触达 ｜ 复活：不动（非主攻区；J5：有证据再动）；WhatsApp 已加 → 唤醒走 WhatsApp 一句话，不走邮件 ｜ 通路：巴西 非主攻 ｜ 节奏：不动 ｜ 证据：gmail_digest：out 0；用户表：「兴趣：主动问了GMC和商业POE价格」；研究档 risks：无邮箱；巴西进口税高、ANATEL 认证
- **现状一句话**：巴西南里奥格兰德（+55 54）联系人 Eleandro，主动问过千兆 MC 与商用 PoE 价格；无邮箱无公司；WA 6 次无实质回复。
- **对方真实需求（有据）**：商用 PoE 询价 → STC-28DGGPM；GMC → STI-110GE。
- **断点 / 为什么停在这里**：无邮箱；巴西进口税高、ANATEL 认证
- **Saga 现在该推什么**：P1 **STC-28DGGPM**（25% 档，按主表（研究档 saga_fit））——商用 PoE 询价 → STC-28DGGPM；GMC → STI-110GE。
- **下一步（具体）**：不动　—　—

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-10-21 | 用户表 | Simon | 兴趣：主动问了GMC和商业POE价格 | 表内备注 | `用户表` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：无邮件往来；用户表状态「WhatsApp 已加·未回复」与三邮箱证据矛盾：S/A 邮箱为「未发信」，Elsa 邮箱全量真人来信（Replied 67 封 + 非 Replied 9 封，第 73 批按邮箱/域名逐户比对）亦无此户 → 这条「回复/已加」发生在邮件之外（WhatsApp/平台私信），证据在 Simon 手机；邮件侧不要据此加码

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **同国同档参照（BR，25% 档、主推线「商用 2.5G PoE 管理型」，共 1 户有动静，列前 3）**：SB-1137 Infotec Comercio de Equipament（B，同线：回过 4 次（最近 2024-11-19））。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-11-15 共和国日；2026-12-24 圣诞–元旦 ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Eleandro | 推断 |
| 国家 | 巴西 | 事实（用户表）|
| 网站/域名 | — | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Eleandro | 事实（用户表） |
| 来源（From） | 主动联系 | 事实（用户表） |
| 兴趣（Interested in） | 主动问了GMC和商业POE价格 | 事实（用户表） |
| 用户备注（Remark） | 55 54 8141-3288 已加 | 事实（用户表） |
| 所在清单 | WA跟进 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：无域名、无邮箱
- **是谁**：巴西南里奥格兰德（+55 54）联系人 Eleandro，主动问过千兆 MC 与商用 PoE 价格；无邮箱无公司；WA 6 次无实质回复。
- **【用户表】主动问了 GMC 和商业 POE 价格**
  > 兴趣：主动问了GMC和商业POE价格
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Eleandro（） +55 54 8141 3288〔（本地 Clients/ 表格，无公开 URL）〕
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · 无域名 · 仅表内信息）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | （未知） |
| 总部/地址 | 巴西（RS） |
| 其他 | 仅 WhatsApp |

- **触达通道（公开）**：role: （疑安装商）；region: 巴西
- **风险/边界**：无邮箱；巴西进口税高、ANATEL 认证
- **Saga 对位结论**：P1 STC-28DGGPM（25% 档）——商用 PoE 询价 → STC-28DGGPM；GMC → STI-110GE。
- **邮件切入句（英文）**：（无邮箱；WhatsApp 报 STC-28DGGPM $84 + GMC $23）

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 6 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-01-02 | 2025.1.2 | mini |  | Whatsapp |  | Whatsapp_S跟进 2026.08.04.xlsx#4 |
| 2025-03-12 | 312 | 工业16 24口出货图 |  | Whatsapp |  | Whatsapp_S跟进 2026.08.04.xlsx#4 |
| 2025-05-23 | 523 | 4 8 16口工业PoE |  | Whatsapp |  | Whatsapp_S跟进 2026.08.04.xlsx#4 |
| 2025-06-25 | 625 | 洪瑞商业PoE组合图 |  | Whatsapp |  | Whatsapp_S跟进 2026.08.04.xlsx#4 |
| 2025-07-22 | 722 | 商业24 48口图 |  | Whatsapp |  | Whatsapp_S跟进 2026.08.04.xlsx#4 |
| 2025-10-06 | 106 | dac |  | Whatsapp |  | Whatsapp_S跟进 2026.08.04.xlsx#4 |

## 联系方式（已有 · 原值照录）

- 电话：`+555481413288`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Eleandro
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Eleandro | — | +55 54 8141 3288 | 调研核实（公开页） | （本地 Clients/ 表格，无公开 URL） |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；无邮箱：只能电话 / WhatsApp / 官网表单

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| Whatsapp_S跟进 2026.08.04.xlsx#总表:5 | 4 |  | 巴西 | Eleandro | 主动联系 | 主动问了GMC和商业POE价格 |  | 55 54 8141-3288 已加 | 6 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：商用 PoE 询价 → STC-28DGGPM；GMC → STI-110GE。 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（经销/集成（类型待核）） |
| 备选2 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-28DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：WhatsApp 直达
- **W**：拉美：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STC-28DGGPM 按 25% 档报价，做现供应商的第二货源
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
| 触达通道 | ✅ WhatsApp 已加 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 公司网站（表内无域名，无法核实是否仍在运营）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STC-28DGGPM - 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks (Marvell-based, neutral label)

```text
Hello,

We have been in touch before about PoE and industrial switches; instead of a catalogue, here is one concrete option.

We supply a Marvell-based 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks - model STC-28DGGPM - that fits the same slot as the units you source today at a lower landed cost, and we can ship it under your own label with neutral packaging. Current price: $84.1 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Are PoE / industrial switches something you still source today, or has that line been dropped?

If useful, one unit at the unit price for a 30-day side-by-side test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 研究档备注（未并入正文）：（无邮箱；WhatsApp 报 STC-28DGGPM $84 + GMC $23）

> 发送前检查：① 不出现「Made in China」或原产地；② 不承诺未实测指标（PoE 功率/温宽）；③ 落款换成发件人姓名；④ 一次只问一个问题；⑤ 价格为 USD EXW 快照，过窗先核价；⑥ 只用表内/公开原值邮箱，不猜地址；⑦ 发出后在「新跟进记录」补一行并告知日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-26**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-27：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 28）

---

*建档日期：2026-10-27　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
