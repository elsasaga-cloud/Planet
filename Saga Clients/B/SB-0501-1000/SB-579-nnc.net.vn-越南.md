# nnc.net.vn
**官方名称（调研核实）**：NNC（nnc.net.vn，越南）

> **评级 B**　|　越南　|　档案编号 `SB-579`　|　优先级 ★★　|　状态：WhatsApp 已加·未回复
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：WhatsApp 已加　|　**所在清单**：询盘流水　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-579
rating: B
rating_auto: B
name_official: "NNC（nnc.net.vn，越南）"
score: 37
country: 越南
region: 亚太
website: nnc.net.vn
type: 经销/集成（类型待核）
tier_tags: ["询盘流水"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STC-28DGGPM
price_tier: 25%
research: done
site_snapshot: http_error  # 2026-10-21
sources: 1
updated: 2026-10-28
```

## SALES BRIEF（压缩模型）

- **是谁**：越南公司 NNC（业务邮箱 kinhdoanh8@，联系人 Hoa），询盘表来源，无兴趣描述；WA 无实质回复。（调研 2026-10-21；表内兴趣：—）
- **为什么是 B 级**：+12 主动询盘（阿里巴巴/自建站/转介）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+0 区域 亚太/越南；+2 最近活动 2024
- **历史互动**：WhatsApp 已加
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-28DGGPM — 无口型。；按主表（研究档 saga_fit）
- **第一问（只问一个）**：Are PoE / industrial switches something you still source today, or has that line been dropped?
- **最大未知**：具体需求型号（表内兴趣列为空）；官网当前状态异常（HTTP 错误）——公司是否仍在运营待核
- **下一步**：不动 — —

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-579` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未发信（S/A 邮箱均无往来；来源：用户表「（空）」；Elsa 箱：`to:nnc.net.vn` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → 三箱（S/A/E）均未发（第 74 批(n)））** ｜ 类型：— ｜ 筛子：—（未入筛） ｜ 停点：从未触达 ｜ 复活：不动（非主攻区；J5：有证据再动）；WhatsApp 已加 → 唤醒走 WhatsApp 一句话，不走邮件 ｜ 通路：越南 非主攻 ｜ 节奏：不动 ｜ 证据：gmail_digest：out 0；用户表：「（空）」；研究档 risks：身份不明；无需求
- **现状一句话**：越南公司 NNC（业务邮箱 kinhdoanh8@，联系人 Hoa），询盘表来源，无兴趣描述；WA 无实质回复。
- **对方真实需求（有据）**：无口型。
- **断点 / 为什么停在这里**：身份不明；无需求
- **Saga 现在该推什么**：P1 **STC-28DGGPM**（25% 档，按主表（研究档 saga_fit））——无口型。
- **下一步（具体）**：不动　—　—

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-10-21 | 用户表 | Simon | （空） | 表内备注 | `用户表` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：无邮件往来；用户表状态「WhatsApp 已加·未回复」与三邮箱证据矛盾：S/A 邮箱为「未发信」，Elsa 邮箱全量真人来信（Replied 67 封 + 非 Replied 9 封，第 73 批按邮箱/域名逐户比对）亦无此户 → 这条「回复/已加」发生在邮件之外（WhatsApp/平台私信），证据在 Simon 手机；邮件侧不要据此加码

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **同国同档参照（VN，25% 档、主推线「商用 2.5G PoE 管理型」，共 1 户有动静，列前 3）**：SA-031 Truong Son Solutions（A，同档：回过 2 次（最近 2026-07-15））。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2027-02-06 春节 Tết（约 02-05 → 02-11） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-27 查）：**

- `nnc.net.vn` → 自建 / 同域名邮件服务器（MX：mail.nnc.net.vn）。自建邮件服务器：有自己的 IT（可能灰名单 → 首封延迟几小时才进箱），像素可用；读信的是技术人，参数先于价格

**假日避让：** 下一步为「不动」，不排发信，略。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | nnc.net.vn（取自域名，公司全名待核） | 推断 |
| 国家 | 越南 | 事实（用户表）|
| 网站/域名 | nnc.net.vn | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Hoa | 事实（用户表） |
| 来源（From） | 2024.5.23 | 事实（用户表） |
| 兴趣（Interested in） | — | 事实（用户表） |
| 用户备注（Remark） | L3交换机 / from: 自建站 | 事实（用户表） |
| 所在清单 | 询盘流水 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线（快照 HTTP 错误）
- **是谁**：越南公司 NNC（业务邮箱 kinhdoanh8@，联系人 Hoa），询盘表来源，无兴趣描述；WA 无实质回复。
- **【官网快照】nnc.net.vn HTTP 错误**
  > status http_error
  > 来源：http://nnc.net.vn/（抓取 2026-10-21）
- **【用户表】询盘统计表来源，无兴趣描述**
  > （空）
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Hoa（）kinhdoanh8@nnc.net.vn +84 946 129 891〔（本地 Clients/ 表格，无公开 URL）〕
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（快照 HTTP 错误 + 表内））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | NNC（待核） |
| 总部/地址 | Vietnam |

- **触达通道（公开）**：role: （未知）；region: 越南
- **风险/边界**：身份不明；无需求
- **Saga 对位结论**：P1 STC-28DGGPM（25% 档）——无口型。
- **邮件切入句（英文）**：（低优先）

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：HTTP 错误）

- 尝试域名：nnc.net.vn
  > https://nnc.net.vn/ http 404 ct=text/html; charset=iso-8859-1
  > https://www.nnc.net.vn/ http 404 ct=text/html; charset=iso-8859-1
  > http://nnc.net.vn/ http 404 ct=text/html; charset=iso-8859-1
- **提示**：抓取失败不代表公司不在；人工打开一次即可。
- 数据文件：`data/saga_clients/site_snapshots/SB-579.json`

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-28T08:44:48Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-579/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://nnc.net.vn/) | html | HTTP 404 | 2026-10-23T04:20:51Z | 官网首页（T27 快照状态 http_error） |

## 联系方式（已有 · 原值照录）

- 邮箱：`kinhdoanh8@nnc.net.vn`〔企业邮箱；来源：用户表原值〕
- 电话：`+84946129891`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Hoa
- 网站/域名：nnc.net.vn
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Hoa | — | kinhdoanh8@nnc.net.vn / +84 946 129 891 | 调研核实（公开页） | （本地 Clients/ 表格，无公开 URL） |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 询盘统计表.xlsx#Sheet1:19 |  | @nnc.net.vn | 越南 | Hoa | 2024.5.23 |  | kinhdoanh8@nnc.net.vn 849461 29891 已加 | L3交换机 from: 自建站 | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：无口型。 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（经销/集成（类型待核）） |
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
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
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
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 具体需求型号（表内兴趣列为空）
- [ ] 官网当前状态异常（HTTP 错误）——公司是否仍在运营待核
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STC-28DGGPM - 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks (Marvell-based, neutral label)

```text
Hi Hoa,

We have been in touch before about PoE and industrial switches; instead of a catalogue, here is one concrete option.

We supply a Marvell-based 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks - model STC-28DGGPM - that fits the same slot as the units you source today at a lower landed cost, and we can ship it under your own label with neutral packaging. Current price: $84.1 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Are PoE / industrial switches something you still source today, or has that line been dropped?

If useful, one unit at the unit price for a 30-day side-by-side test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 研究档备注（未并入正文）：（低优先）

> 发送前检查：① 不出现「Made in China」或原产地；② 不承诺未实测指标（PoE 功率/温宽）；③ 落款换成发件人姓名；④ 一次只问一个问题；⑤ 价格为 USD EXW 快照，过窗先核价；⑥ 只用表内/公开原值邮箱，不猜地址；⑦ 发出后在「新跟进记录」补一行并告知日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-27**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-28：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 37）

---

*建档日期：2026-10-28　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
