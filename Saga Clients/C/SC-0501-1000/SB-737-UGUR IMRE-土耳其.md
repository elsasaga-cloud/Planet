# UGUR IMRE
**官方名称（调研核实）**：Uğur İmre（分销商，TR；无域名）

> **评级 C**　|　土耳其　|　档案编号 `SB-737`　|　优先级 —　|　状态：名单内·未触达
>
> **P 池并入（C 档，等级不动）：☆ P 池 · 观察档（试单 / 回访后转正或退回 C）**（批 AB-01 · 2026-10-29 · 下次巡检 2026-12-28）：☆ P 池观察（P 观察候选，B 档并池 · 等级不动）：真回 ✔ 但 未坐实 → 观察；命中 3/6（成单/样品 — · 真回 ✔ · WA — · 对位 ✔ 交换机 · 登记 未坐实 · 体量 未取（疑微型））　|　标签：oem_target（贴牌卖交换机的渠道商 —— OEM 专项对象，留 C）
>
> **类型**：品牌商/贴牌需求（OEM/ODM）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：ISAF2025展会、表:Ady　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-737
rating: C
rating_auto: B
sieve: pool_watch  # 闸 3 AB1 2026-10-29
rating_research: C  # B-PASS-01 2026-10-31 B 池分层「不 OK 的下放 C 储备」：最后一句硬婉拒（R-）
name_official: "Uğur İmre（分销商，TR；无域名）"
score: 32
country: 土耳其
region: 土耳其
website: none
type: 品牌商/贴牌需求（OEM/ODM）
tier_tags: ["ISAF2025展会", "表:Ady"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
p1: STC-28GPM
price_tier: 20%
research: done
site_snapshot: none
sources: 2
updated: 2026-10-31
```

## SALES BRIEF（压缩模型）

- **是谁**：ISAF 记录：Uğur İmre（Ady 客户；无邮箱/域名）——分销商，不需要 OEM；要工业级 PoE 交换机；现场报价「2 光 8 电瑞昱（Realtek）带 PoE 带网管 + 内置 DC48V 电源 $70」，回复 Not bad；微信没通过；无后续跟进。仅表内信息；分销 20%。报价映射：2 SFP + 8 GE PoE 管理型 Realtek 商用 = STC-28GPM（列表 $62.2）；若需工业 DIN 版 = STI-288GPM（$78.9@20%）。（调研 2026-10-21；表内兴趣：Ady客户  分销商 不需要OEM  要工业级POE交换机  报价2光8瑞昱带POE带网管加一个内置DC48V电源70usd, 回复Not bad(微信没通过））
- **为什么是 C 级**：**调研后定级 C**（B-PASS-01 2026-10-31 B 池分层「不 OK 的下放 C 储备」：最后一句硬婉拒（R-））；自动分级 B：+12 ISAF 2025 展会面对面名片；+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；-8 无邮箱，仅电话/WhatsApp；+8 区域 土耳其/土耳其；C 级细分：调研后定级 C
- **历史互动**：名单内·无互动记录
- **P1**：不推（C 级）；若对方主动来询，起手 STC-28GPM（深挖对位：分销 20% 档：STC-28GPM（Realtek 2 SFP + 8 GE PoE L2 管理，内置电源，列表 $62.2；ISAF 现场报 $70 含 DC48V 内置电源版）；工业 DIN 版 STI-288GPM（$78.9）/ 非管理 STI-288GP（$57.4））
- **最大未知**：公司网站（表内无域名，无法核实是否仍在运营）
- **下一步**：2026-11（Simon） A 邮箱首封 + WhatsApp（Simon） 首封 + 一句话

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-737` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（展会名片 + WhatsApp 已加，邮件 0 封）：用户表「Ady客户  分销商 不需要OEM  要工业级POE交换机  报价2光8瑞昱带POE带网管加一个内置DC48V电源70usd, 回复Not bad(微信没通过） / UGUR IM」；S/A 邮箱 0 封；Elsa 箱无可查地址（仓内无此户任何邮箱/域名——用户表/WhatsApp/展会名片户，`from:e.sagatelecom to:` 无从下手；Elsa 群发是否碰过他无法判定，不写「未触达」）（第 74 批(o)）** ｜ 类型：— ｜ 筛子：3（已加 WhatsApp，表内有往来） ｜ 停点：仓库只有用户表一行；往来在 Simon 手机 ｜ 复活：首封邮件（A 邮箱，按 email_hook）+ WhatsApp 一句话 ｜ 通路：土耳其 非主攻 ｜ 节奏：一封 ｜ 证据：gmail_digest：out 0；用户表：「Ady客户  分销商 不需要OEM  要工业级POE交换机  报价2光8瑞昱带POE带网管加一个内置DC48V电源70usd, 回复Not bad(微信没通过）」；研究档 risks：无联系渠道（微信未通过）；无后续跟进
- **现状一句话**：ISAF 记录：Uğur İmre（Ady 客户；无邮箱/域名）——分销商，不需要 OEM；要工业级 PoE 交换机；现场报价「2 光 8 电瑞昱（Realtek）带 PoE 带网管 + 内置 DC48V 电源 $70」，回复 Not bad；微信没通过；无后续跟进。仅表内信息；分销 20%。报价映射：2 SFP + 8 GE PoE 管理型 Realtek 商用 = STC-28GPM（列表 $62.2）；若需工业 DIN 版 = STI-288GPM（$78.9@20%）。
- **对方真实需求（有据）**：分销 20% 档：STC-28GPM（Realtek 2 SFP + 8 GE PoE L2 管理，内置电源，列表 $62.2；ISAF 现场报 $70 含 DC48V 内置电源版）；工业 DIN 版 STI-288GPM（$78.9）/ 非管理 STI-288GP（$57.4）
- **断点 / 为什么停在这里**：无联系渠道（微信未通过）；无后续跟进
- **Saga 现在该推什么**：P1 **STC-28GPM**（20% 档，Realtek 线按 HRUI 2026-09-30 进价 +20% 现算（Q-47 默认，不用 Drive 旧表价）：STC-28GPM $62.2→$71.0；按主表（研究档 saga_fit））——分销 20% 档：STC-28GPM（Realtek 2 SFP + 8 GE PoE L2 管理，内置电源，列表 $62.2；ISAF 现场报 $70 含 DC48V 内置电源版）；工业 DIN 版 STI-288GPM（$78.9）/ 非管理 STI-288GP（$57.4）
- **下一步（具体）**：2026-11（Simon）　A 邮箱首封 + WhatsApp（Simon）　首封 + 一句话
  - 第一问（只问一个）：Uğur Bey, ISAF'ta 'not bad' dediğiniz 2 SFP + 8 port Realtek PoE yönetilebilir switch: dahili güç kaynaklı sürüm EXW 71,0 USD, DIN ray endüstriyel L2 sürümü 78,9 USD (distribütör fiyatı) — ilk parti için 20 mi 50 adet mi düşünelim?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-10-21 | 用户表 | Simon | Ady客户  分销商 不需要OEM  要工业级POE交换机  报价2光8瑞昱带POE带网管加一个内置DC48V电源70usd, 回复Not bad(微信没通过） / UGUR IMRE | 表内备注 | `用户表` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：WhatsApp 往来未入库

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**假日避让（土耳其 · 按下一步「2026-11」窗口 2026-11-01→2026-11-30）：**

- 窗口内无该国法定假日

**公司底数 · 第 99 批（TR · 1 次检索「Uğur İmre güvenlik kamera network distribütör」未命中任何同名企业或个人主页（仅返回 İzmir / İstanbul 安防经销商泛结果）→ 按规程停；研究档：ISAF 展会名录联系人，仅有姓名 + 个人邮箱 + 历史群发记录，2026-10-28 查；）：**

- 法定名 / 登记号：Uğur İmre（ISAF 展会联系人；无公司名 / 无域名）— 未坐实 · 未坐实（无公司主体可核） · 状态 **未核** · 成立 未取 · 未取（疑个人 / 微型经销）
- 行业码 / 经营范围：安防 / 网络经销（ISAF 展会观众名录推定）
- 注册地址：未取
- 规模档：未取（疑微型）
- 账目：—；—
- 高管：Uğur İmre — 本人（ISAF 名录）
- 控制人 / 股东：未取
- **这意味着什么：**
  - **未坐实且无公司主体** → 不再花检索；保留 B 不降（有打开记录）；下一次群发顺带一封 HRUI STC-028GP / STC-228GP 价目即可，**不单独写信、不加厚**
- 备注：未坐实；仅群发带过。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | UGUR IMRE | 推断 |
| 国家 | 土耳其 | 事实（用户表）|
| 网站/域名 | — | 事实（用户表 URL/邮箱域名） |
| 类型 | 品牌商/贴牌需求（OEM/ODM） | 推断（据兴趣/备注关键词） |
| 联系人 | UGUR IMRE | 事实（用户表） |
| 来源（From） | — | 事实（用户表） |
| 兴趣（Interested in） | Ady客户  分销商 不需要OEM  要工业级POE交换机  报价2光8瑞昱带POE带网管加一个内置DC48V电源70usd, 回复Not bad(微信没通过） | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | ISAF2025展会、表:Ady | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：无域名
- **是谁**：ISAF 记录：Uğur İmre（Ady 客户；无邮箱/域名）——分销商，不需要 OEM；要工业级 PoE 交换机；现场报价「2 光 8 电瑞昱（Realtek）带 PoE 带网管 + 内置 DC48V 电源 $70」，回复 Not bad；微信没通过；无后续跟进。仅表内信息；分销 20%。报价映射：2 SFP + 8 GE PoE 管理型 Realtek 商用 = STC-28GPM（列表 $62.2）；若需工业 DIN 版 = STI-288GPM（$78.9@20%）。
- **【用户表】ISAF：分销商；不需 OEM；$70 报价；Not bad；微信未通过**
  > Ady客户  分销商 不需要OEM  要工业级POE交换机  报价2光8瑞昱带POE带网管加一个内置DC48V电源70usd, 回复Not bad(微信没通过） / UGUR IMRE
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Uğur İmre（ISAF 名录联系人本人（无公司主体；官方登记 1 次未命中 → 未坐实）（第 99 批 官方登记核实 2026-10-28））— —（名片在 Ady 处）〔（本地 Clients/ 表格，无公开 URL）〕
- **调研后定级**：C（原自动 B）——B-PASS-01 2026-10-31 B 池分层「不 OK 的下放 C 储备」：最后一句硬婉拒（R-）
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · 无域名 · 仅表内信息）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | 未坐实（无公司名 / 无域名；ISAF 展会名录个人） |
| 成立 | 未取（第 99 批 官方登记核实 2026-10-28） |
| 总部/地址 | 未取 |
| 人数 | 未取 |
| 其他 | 不需要 OEM；微信未通过；第 99 批：**未坐实**；保留 B（有打开）；只随群发带 HRUI 价目，不单独写信、不加厚（第 99 批 官方登记核实 2026-10-28） |

- **业务线**：网络/安防分销（推测）
- **触达通道（公开）**：线下: ISAF 名片（Ady）；微信申请未通过
- **近况信号**：
  - 对 $70 报价回复 Not bad → 价格带接受；需从 Ady 名片补邮箱/电话再跟
- **风险/边界**：无联系渠道（微信未通过）；无后续跟进
- **Saga 对位结论**：P1 STC-28GPM（20% 档）——分销 20% 档：STC-28GPM（Realtek 2 SFP + 8 GE PoE L2 管理，内置电源，列表 $62.2；ISAF 现场报 $70 含 DC48V 内置电源版）；工业 DIN 版 STI-288GPM（$78.9）/ 非管理 STI-288GP（$57.4）
- **邮件切入句（英文）**：Uğur Bey, ISAF'ta 'not bad' dediğiniz 2 SFP + 8 port Realtek PoE yönetilebilir switch: dahili güç kaynaklı sürüm EXW 71,0 USD, DIN ray endüstriyel L2 sürümü 78,9 USD (distribütör fiyatı) — ilk parti için 20 mi 50 adet mi düşünelim?

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## B 分层（B-PASS-01 · 2026-10-31）：**C**

- 依据：最后一句硬婉拒（R-）；身份 登记坐实 · 路径 弱 · 回信 R- · 区域档 focus
- 节奏：B1 重点普通跟 = 分组群发每 6 周 + 一年两次点名；B2 普通跟 = 分组群发每 8 周；C 储备 = 不发、两月巡检，有动静捞回。

## 联系方式（已有 · 原值照录）

- 电话：`+905339626349`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：UGUR IMRE
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Uğur İmre | ISAF 名录联系人本人（无公司主体；官方登记 1 次未命中 → 未坐实）（第 99 批 官方登记核实 2026-10-28） | — / —（名片在 Ady 处） | 调研核实（公开页） | （本地 Clients/ 表格，无公开 URL） |
| UGUR IMRE | — | +905339626349 | 用户表原值 | Clients/ 表 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；无邮箱：只能电话 / WhatsApp / 官网表单

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`p:339626349`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/2025土耳其ISAF客户.xlsx#Ady:24 | 23 |  | Turkey | UGUR IMRE |  | Ady客户  分销商 不需要OEM  要工业级POE交换机  报价2光8瑞昱带POE带网管加一个内置DC48V电源70usd, 回复Not bad(微信没通过） | 90 533 962 63 49 |  | — |
| A/2025土耳其ISAF客户.xlsx#Sheet1:39 | 68 |  | Turkey | UGUR IMRE |  | Ady客户  分销商 不需要OEM  要工业级POE交换机  报价2光8瑞昱带POE带网管加一个内置DC48V电源70usd, 回复Not bad(微信没通过） | 90 533 962 63 49 |  | — |

## 跟进建议

> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。
> 不跟进理由：调研后定级 C。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `SB-737,B,理由` 后重跑即可。

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
| 触达通道 | ⚠️ 仅电话 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **不合格（见 C 级细分）→ 不主动跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 公司网站（表内无域名，无法核实是否仍在运营）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：WhatsApp / 私信一句话（复制即发；不发邮件）

```text
Uğur Bey, ISAF'ta 'not bad' dediğiniz 2 SFP + 8 port Realtek PoE yönetilebilir switch: dahili güç kaynaklı sürüm EXW 71,0 USD, DIN ray endüstriyel L2 sürümü 78,9 USD (distribütör fiyatı) — ilk parti için 20 mi 50 adet mi düşünelim?
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

- 2026-10-31：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 B，分数 32）；人工/调研定级 → C

---

*建档日期：2026-10-31　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
