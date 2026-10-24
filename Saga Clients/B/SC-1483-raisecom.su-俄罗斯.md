# raisecom.su
**官方名称（调研核实）**：DEALER Co Ltd（raisecom.su，圣彼得堡；Raisecom 俄罗斯经销；KP Dmitry Deikun、Kovzur Max – Technical manager）

> **评级 B**　|　俄罗斯　|　档案编号 `SC-1483`　|　优先级 ★★　|　状态：成交过·维护
>
> **类型**：俄罗斯经销/项目商（Raisecom 代理）（推断）　|　**历史关系**：成交/下单过；WhatsApp 已加　|　**所在清单**：用户判定不行　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SC-1483
rating: B
rating_auto: C
rating_research: B  # 两位具名 KP、三个带规格的项目询价、我们已报价两款；俄罗斯次要市场 → B 慢慢跟进（自动 C 系无后续回复评分）。
name_official: "DEALER Co Ltd（raisecom.su，圣彼得堡；Raisecom 俄罗斯经销；KP Dmitry Deikun、Kovzur Max – Technical manager）"
score: 5
country: 俄罗斯
region: 俄语区
website: raisecom.su
type: 俄罗斯经销/项目商（Raisecom 代理）
tier_tags: ["用户判定不行"]
deal: yes
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 12 msgs (out 7 / in 5), 2024-05-07 -> 2024-06-20
p1: STC-4168XGGCM（L3，4×10G SFP+ + 16×SFP + 8 Combo，$413）对他的「L3 商用 8–12 SFP+ + 12–24 GE」；工业 STI-4168XGGCM-U(L3) $605
price_tier: 25%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：S 邮箱 2024-05/06 两轮项目询价：05-07 Kovzur 要 CLI 手册（给了，候选 STI-480XGGM，18W）；06-20 Dmitry：「lost several projects」后给新小项目——L3 机架工业机 24×SFP + 8 Combo + 4×10G 双 AC（1 台）+ L2 DIN 2×SFP+8×PoE 240W；Simon 报 STI-4168XGGCM-U $550 / STI-288DGGPM $120；Dmitry 又问 L3 商用 8–12 SFP+ + 12–24 GE → Simon「没有正好的，近似 Realtek 6×10G+24×2.5G L2+」→ 无回。（调研 2026-10-24；表内兴趣：—）
- **为什么是 B 级**：**调研后定级 B**（两位具名 KP、三个带规格的项目询价、我们已报价两款；俄罗斯次要市场 → B 慢慢跟进（自动 C 系无后续回复评分）。）；自动分级 C：+50 有成单/下单/买过记录（用户备注或跟进表）；-60 用户已归入「不行及不太相关的」；+10 有企业邮箱；+5 有可核实的公司网站/域名；+0 区域 俄语区/俄罗斯
- **历史互动**：成交/下单过；WhatsApp 已加
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-4168XGGCM（L3）$413；STI-4168XGGCM-U $511.5 / (L3) $605；STI-288DGGPM $137.5 — 已发资料（勿重发）：CLI 手册(2024-05-07)、STI-480XGGM 资料(2024-05-07)、Realtek 6×10G+24×2.5G 规格书(2024-06-20)；对俄付款在回信后谈；2024-06-20 报过 $550 / $120（老汇率 7.2）——再报前对表：同款 2026-10 表 $511.5（L2+）或 $605（L3）、$137.5；**第 63 批基准统一（规则 ㉕）**：STC-4168XGGCM 由列表价 $413 改为 25% 档 $392.4；他没收过 $240/$280 群发；工业 -U 两档 $511.5 / $605 = 列表价 ≤ 档位价，封顶保留
- **第一问（只问一个）**：Dmitry — in June 2024 I had nothing for your "L3 commercial, 8-12 SFP+ and 12-24 GE" request; today we do: 4 x 10G SFP+ + 16 x 1G SFP + 8 x combo, L3, $413 USD EXW. Do you have a project this winter where it fits?
- **最大未知**：具体需求型号（表内兴趣列为空）
- **下一步**：2026-12 S 邮箱 → ddmitry@raisecom.su（回 2024-06-20 原线程「L2 managed switch」） 一句话：2024 年答「没有」的 L3 商用 8–12 SFP+ + 12–24 GE 现在有（STC-4168XGGCM，4×10G SFP+ + 16×SFP + 8 Combo，L3，$413 EXW）；问有没有新项目

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SC-1483` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（S 邮箱 2024-05/06 两轮 5 封来信、两位具名 KP、三个带规格项目；Simon 报价两款后对方无回；2024-06 后无再互动）** ｜ 类型：经销/项目 ｜ 筛子：4（规格 + 报价层面） ｜ 停点：最后一问我们答「没有正好的」+ Realtek 近似——对方没回；之后只有群发 ｜ 复活：一句话：当年没有的 L3 商用款现在有（STC-4168XGGCM $413）；问有没有新项目 ｜ 通路：俄罗斯（次要） ｜ 节奏：季度 ｜ 证据：gmail_s 2024-05-07 ×5、2024-06-20 ×6；digest in 5
- **现状一句话**：Raisecom 俄罗斯经销 DEALER Co 的 Dmitry/Kovzur 在 2024-05/06 拿三个项目规格来问，Simon 报了 STI-4168XGGCM-U $550 和 STI-288DGGPM $120，最后一个 L3 商用需求答「没有」。此后两年只群发。
- **对方真实需求（有据）**：项目制：L3 工业机架（24×SFP+8 Combo+4×10G 双 AC）、L2 DIN PoE（2×SFP+8×PoE 240W）、L3 商用（8–12 SFP+ + 12–24 GE）。
- **断点 / 为什么停在这里**：2024-06-20「没有正好的」之后没人再问他有没有新项目。
- **Saga 现在该推什么**：P1 **STC-4168XGGCM（L3）$413；STI-4168XGGCM-U $511.5 / (L3) $605；STI-288DGGPM $137.5**（经销 25%% 档，2024-06-20 报过 $550 / $120（老汇率 7.2）——再报前对表：同款 2026-10 表 $511.5（L2+）或 $605（L3）、$137.5；**第 63 批基准统一（规则 ㉕）**：STC-4168XGGCM 由列表价 $413 改为 25% 档 $392.4；他没收过 $240/$280 群发；工业 -U 两档 $511.5 / $605 = 列表价 ≤ 档位价，封顶保留）——已发资料（勿重发）：CLI 手册(2024-05-07)、STI-480XGGM 资料(2024-05-07)、Realtek 6×10G+24×2.5G 规格书(2024-06-20)；对俄付款在回信后谈
  - 复购/在买项：项；目；制
  - 做不了 / 要先核的：是；否；还；在；做；项；目；；；付；款；路；径；；；L；2； ；D；I；N； ；2；×；S；F；P； ；+； ；8；×；P；o；E； ；2；4；0；W； ；项；目；的； ；R；e；a；l；t；e；k； ；工；业；线；对；位；：；S；T；I；-；2；8；8；G；P；M；-；2；B；T；（；2；0；2；5；-；0；4； ；表； ；$；1；1；0；，；v；s； ；M；a；r；v；e；l；l； ；S；T；I；-；2；8；8；D；G；G；P；M； ；$；1；3；7；.；5；）；—；—；只；在；他；再；来；问；价；时；给；，；不；主；动；（；d；o；c；s；/；r；e；f；e；r；e；n；c；e；/；价；格；表；_；R；e；a；l；t；e；k；工；业；线；_；S；a；g；a；对；外；_；2；0；2；5；.；m；d；）
- **下一步（具体）**：2026-12　S 邮箱 → ddmitry@raisecom.su（回 2024-06-20 原线程「L2 managed switch」）　一句话：2024 年答「没有」的 L3 商用 8–12 SFP+ + 12–24 GE 现在有（STC-4168XGGCM，4×10G SFP+ + 16×SFP + 8 Combo，L3，$413 EXW）；问有没有新项目
  - 第一问（只问一个）：Dmitry — in June 2024 I had nothing for your "L3 commercial, 8-12 SFP+ and 12-24 GE" request; today we do: 4 x 10G SFP+ + 16 x 1G SFP + 8 x combo, L3, $413 USD EXW. Do you have a project this winter where it fits?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-05-07 | 来 | Kovzur Max（Technical manager） | Can you send us command line guide for this switch? | 技术经理看 CLI——真评估 | `q` |
| 2024-06-20 | 来 | Dmitry Deikun | Unfortunately, we lost several projects. Now we have small project: L3 rack-mount manageable industrial switch: 24*1000/1000M SFP 8*10/100/1000BASE-TX RJ45 (COMBO) 4*100M/1000M/10000M SFP+ AC/D: dual AC inputs 1unit; L2 manageable industrial switch: 2*Gigabit SFP+8*10/100/1000M RJ45 POE af/at, 240W, Din mounting | 带规格项目 | `rfq` |
| 2024-06-20 | 去 | Simon | Item 1: STI-4168XGGCM-U 550usd/pc… L3 Managed, Non-PoE, 1U Rack, AC100V~240V DUAL input, Marvell Chip; Item 2: STI-288DGGPM 120usd/pc 2*100M/1G/2.5G SFP+8*10/100/1000M PoE L2+ 240W Din Rail | 已报价（老汇率） | `quote` |
| 2024-06-20 | 来 | Dmitry Deikun | We have one more project. Customer need L3 Commercial Managed Switch 8-12 SFP+ and 12-24GE. AC/D Do you have anything suitable? | 第三需求——当年答没有 | `rfq` |
| 2024-06-20 | 去 | Simon | Sorry, we do not have a model that is exactly good for it. A close model is Realtek chip, 6*10G SFP+24*2.5G Ethernet, L2+ | 断点 | `reply` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：公司规模/是否仍活跃（raisecom.su 未爬）；2024 两款报价是否曾成单（仓内无 PI → 未成）

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | raisecom.su（取自域名，公司全名待核） | 推断 |
| 国家 | 俄罗斯 | 事实（用户表）|
| 网站/域名 | raisecom.su | 事实（用户表 URL/邮箱域名） |
| 类型 | 俄罗斯经销/项目商（Raisecom 代理） | 推断（据兴趣/备注关键词） |
| 联系人 | Dmitry Deikun | 事实（用户表） |
| 来源（From） | 成单客户 | 事实（用户表） |
| 兴趣（Interested in） | — | 事实（用户表） |
| 用户备注（Remark） | 7 981 853-94-40 已加 | 事实（用户表） |
| 所在清单 | 用户判定不行 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-24）**　网站状态：未爬（raisecom.su）
- **是谁**：S 邮箱 2024-05/06 两轮项目询价：05-07 Kovzur 要 CLI 手册（给了，候选 STI-480XGGM，18W）；06-20 Dmitry：「lost several projects」后给新小项目——L3 机架工业机 24×SFP + 8 Combo + 4×10G 双 AC（1 台）+ L2 DIN 2×SFP+8×PoE 240W；Simon 报 STI-4168XGGCM-U $550 / STI-288DGGPM $120；Dmitry 又问 L3 商用 8–12 SFP+ + 12–24 GE → Simon「没有正好的，近似 Realtek 6×10G+24×2.5G L2+」→ 无回。
- **类型**：俄罗斯经销/项目商（Raisecom 代理）
- **规模**：（未核）
- **【邮件】项目规格 ①L3 工业机架 ②L2 DIN PoE**
  > L3 rack-mount manageable industrial switch: 24*1000/1000M SFP 8*10/100/1000BASE-TX RJ45 (COMBO) 4*100M/1000M/10000M SFP+ AC/D: dual AC inputs 1unit; L2 manageable industrial switch: 2*Gigabit SFP+8*10/100/1000M RJ45 POE af/at, 240W, Din mounting
  > 来源：data/gmail_a|gmail_s/messages/<year>/<month>.jsonl（抓取 2024-06-20）
- **【邮件】第三个需求：L3 商用 8–12 SFP+ + 12–24 GE**
  > Customer need L3 Commercial Managed Switch 8-12 SFP+ and 12-24GE. AC/D Do you have anything suitable?
  > 来源：data/gmail_a|gmail_s/messages/<year>/<month>.jsonl（抓取 2024-06-20）
- **【邮件（去）】Simon 报价**
  > Item 1: STI-4168XGGCM-U 550usd/pc… Item 2: STI-288DGGPM 120usd/pc
  > 来源：data/gmail_a|gmail_s/messages/<year>/<month>.jsonl（抓取 2024-06-20）
- **KP**：Dmitry Deikun（）ddmitry@raisecom.su 〔data/gmail_a|gmail_s/messages/<year>/<month>.jsonl〕
- **KP**：Kovzur Max（）mk@raisecom.su +7 812 764 28 85（信尾）〔data/gmail_a|gmail_s/messages/<year>/<month>.jsonl〕
- **调研后定级**：B（原自动 C）——两位具名 KP、三个带规格的项目询价、我们已报价两款；俄罗斯次要市场 → B 慢慢跟进（自动 C 系无后续回复评分）。
- 备注：最后一问（L3 商用 8–12 SFP+ + 12–24 GE）当年答「没有」——现在主表有 STC-4168XGGCM（4×10G SFP+ + 16×1G SFP + 8 Combo，L3，$413）和 STC-4816XGCGM（$353），接近他要的；2024 报的 $550（STI-4168XGGCM-U）在 2026-10 主表为 $511.5（L2+）/ $605（L3）。

### 加厚挖掘（2026-10-24 · 邮件证据）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | DEALER Co Ltd（信尾） |
| 总部/地址 | St. Petersburg |
| 其他 | raisecom.su |

- **触达通道（公开）**：role: 经销/项目；region: 俄罗斯（圣彼得堡）
- **风险/边界**：对俄付款/物流；2024 项目早已过去；需新项目；Raisecom 代理身份——可能只在 Raisecom 没有的缝隙里找货
- **Saga 对位结论**：P1 STC-4168XGGCM（L3，4×10G SFP+ + 16×SFP + 8 Combo，$413）对他的「L3 商用 8–12 SFP+ + 12–24 GE」；工业 STI-4168XGGCM-U(L3) $605（25% 档）——当年说没有的东西现在有——一句话重开
- **邮件切入句（英文）**：（见 mail_review.draft_en）

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：12 封（去 7 / 来 5）　|　**期间**：2024-05-07 → 2024-06-20　|　**最后去信**：2024-06-20
- **对方邮箱**：ddmitry@raisecom.su、mk@raisecom.su
- **最后一封来信**：2024-06-20 ddmitry@raisecom.su「Re: L2 managed switch」：Hi, Simon! Unfortunately, we lost several projects. Now we have small project: L3 rack-mount manageable industrial switch: 24*1000/1000M SFP 8*10/100/1000BASE-TX RJ45 (COMBO) 4*100M/1000M/10000M SFP+ AC/D: dual AC inputs 1unit L2 manageable industrial switch: 
- **邮件里报过的价**：2024-06-20 $550（STI-288DGGPM STI-4168XGGCM-U）；2024-06-20 $120（STI-288DGGPM STI-4168XGGCM-U）；2024-05-07 $220

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| L2 managed switch | 2024-05-07 | 2024-06-20 | 5 | 7 | 8 |

## 联系方式（已有 · 原值照录）

- 邮箱：`ddmitry@raisecom.su`〔企业邮箱；来源：用户表原值〕
- 电话：`+79818539440`〔WhatsApp 已加；原值见来源表〕
- 联系人（原值）：Dmitry Deikun
- 网站/域名：raisecom.su
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Dmitry Deikun | — | ddmitry@raisecom.su | 调研核实（公开页） | data/gmail_a\|gmail_s/messages/<year>/<month>.jsonl |
| Kovzur Max | — | mk@raisecom.su / +7 812 764 28 85（信尾） | 调研核实（公开页） | data/gmail_a\|gmail_s/messages/<year>/<month>.jsonl |

- **通道建议**：首选 WhatsApp 短消息（已加），邮件只做正式报价；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 不行及不太相关的.xlsx#总表:487 |  |  | 俄罗斯 | Dmitry Deikun | 成单客户 |  | ddmitry@raisecom.su | 7 981 853-94-40 已加 | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-4168XGGCM（L3，4×10G SFP+ + 16×SFP + 8 Combo，$413）对他的「L3 商用 8–12 SFP+ + 12–24 GE」；工业 STI-4168XGGCM-U(L3) $605 | 深挖对位：当年说没有的东西现在有——一句话重开 | 价格待核（价格主表无此型号） | 深挖对位；档位 25%（俄罗斯经销/项目商（Raisecom 代理）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $145.7 USD EXW（25% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $188.7 USD EXW（25% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-4168XGGCM（L3，4×10G SFP+ + 16×SFP + 8 Combo，$413）对他的「L3 商用 8–12 SFP+ + 12–24 GE」；工业 STI-4168XGGCM-U(L3) $605），备选型不进首触。

- **第 1 次**：老客户回访——问上次所购型号的使用情况 + 告知 Marvell 新款（STC-4168XGGCM（L3，4×10G SFP+ + 16×SFP + 8 Combo，$413）对他的「L3 商用 8–12 SFP+ + 12–24 GE」；工业 STI-4168XGGCM-U(L3) $605）；只问一个问题：当前在采购的主力型号与月量。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有成交史，信任与开户成本已付；WhatsApp 直达
- **W**：俄语区：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STC-4168XGGCM（L3，4×10G SFP+ + 16×SFP + 8 Combo，$413）对他的「L3 商用 8–12 SFP+ + 12–24 GE」；工业 STI-4168XGGCM-U(L3) $605 按 25% 档报价，做现供应商的第二货源；规模（调研）：（未核）
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
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ✅ 有成交史（量待确认） |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 具体需求型号（表内兴趣列为空）
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: L2 managed switch — the L3 commercial model you asked for in 2024 exists now

```text
Hi, Dmitry,

In June 2024 you asked for an L3 commercial switch with 8-12 SFP+ and 12-24 GE, and I had nothing exact. Today we do:

- 4 x 10G SFP+ + 16 x 1G SFP + 8 x GE combo, L3 (OSPF/RIP, static), 1U, Marvell — $392 USD EXW
- Industrial version with dual AC input (the one I quoted at $550 then): now $511.5 L2+ / $605 L3 on the 2026-10 list
(valid 15 days from this mail.)

One question: do you have a project this winter where one of these fits? If payment to Russia is the obstacle, tell me and I will explain the route we use.

Thank you.
Simon
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

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 5）；人工/调研定级 → B

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
