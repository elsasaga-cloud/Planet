# comtinu.ru
**官方名称（调研核实）**：Comtinu（俄罗斯；KP Yaroslav, yb@comtinu.ru）

> **评级 B**　|　俄罗斯　|　档案编号 `SB-1122`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：俄罗斯网络项目商（25G/100G 项目）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：DC线索　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-1122
rating: B
rating_auto: C
rating_research: B  # 两次具名真互动均为 25G/100G 数据中心需求（Simon：DC 交换机客户优先）；2025-12 明说「we have 100-25G projects」
name_official: "Comtinu（俄罗斯；KP Yaroslav, yb@comtinu.ru）"
score: 17
country: 俄罗斯
region: 俄语区
website: comtinu.ru
type: 俄罗斯网络项目商（25G/100G 项目）
tier_tags: ["DC线索"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 23 msgs (out 20 / in 3), 2024-05-17 -> 2026-08-10
p1: STH-8C48DX-HSI（48×25G + 8×100G，$4,800 EXW）/ STH-32C-HSI（32×100G，$6,000）
price_tier: 25%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-27
```

## SALES BRIEF（压缩模型）

- **是谁**：S/A 邮箱 2024-05 起 20 余封；两次真互动都指向高速/数据中心：2024-05-17「Do you have 48x25G + 8x100G and 32x40/100G switches?」（Simon 答「not available… coming soon… can help design」）；2025-12-03 先说没有相关项目，Alan 追问「do you sometimes use data center switches? 100G/10G」后答「Yes, we have 100-25G projects. What is your company website?」——Alan 回「still focusing on access switches… It will be CENTEC based」，没给网站、没给 CENTEC 型号与价（而 2025-01-06 已群发过 8C48XF）。此后只有 2026-03 Product Link 与 2026-08 $170 推送。（调研 2026-10-24；表内兴趣：SFP 机架设备(类似WDM)）
- **为什么是 B 级**：**调研后定级 B**（两次具名真互动均为 25G/100G 数据中心需求（Simon：DC 交换机客户优先）；2025-12 明说「we have 100-25G projects」后被我们一句「still focusing on access」放掉；俄罗斯为次要市场，按 B 慢慢跟进。）；自动分级 C：+0 数据中心交换机线索（Hohunet/CENTEC 线）；+2 兴趣仅 MC/SFP/配件（边缘品类）；+10 有企业邮箱；+5 有可核实的公司网站/域名；+0 区域 俄语区/俄罗斯
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STH-8C48DX-HSI（48×25G + 8×100G）；STH-32C-HSI（32×100G） — 需求台账 #13：他是仓内最早（2024-05）明确要 48×25G+8×100G 的人；对俄付款问题在他回信后再谈（RMB via CN agent）｜已发资料（勿重发）：8C48XF.png(2025-01-06)、Product Link_2026Q2(2026-03-12)｜档位说明（原 tier 字段文字「集成商/项目 25%；CENTEC 底线 ≥35% 并行」移此）：集成商/项目 25%；CENTEC 底线 ≥35% 并行；2026 Q2：8C48DX $4,800 / 32C $6,000 / 2C6QX $1,200 EXW
- **第一问（只问一个）**：Yaroslav — in May 2024 you asked for 48x25G + 8x100G and 32x100G; both exist now on our CENTEC-based line (STH-8C48DX-HSI $4,800, STH-32C-HSI $6,000 USD EXW, 2026 Q2 list). When is the 100/25G project you mentioned in December due, and how many units?
- **最大未知**：年走量与现供应商
- **下一步**：2026-11 A 邮箱 → yb@comtinu.ru（回 2025-12-03 原线程「Booster PoE Switch」或新主题「48x25G + 8x100G — the two models you asked for in 2024」） 一封对表信：①网站 sagatele.com（他问过没答）；②他 2024-05-17 问的两款现在的型号与 EXW 价；③只问一个问题：100/25G 项目的时间与台数（第 76 批(b) 2026-10-25：audit_ab 硬错误修正：tier 字段规范为数字）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-1122` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（S/A 邮箱 20+ 去 3 来：2024-05-17 问 48×25G+8×100G / 32×100G；2025-12-03「we have 100-25G projects」+ 问网站——两次都没被接住；Elsa 箱：`to:comtinu.ru` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 20 / 来 3）（第 74 批(l)））** ｜ 类型：DC 项目商 ｜ 筛子：3（型号层面，无数量） ｜ 停点：2025-12-03 Alan 答「still focusing on access switches」——把一个主动说有 25G/100G 项目的人放掉了；网站也没答 ｜ 复活：一封对表信：网站 + 他 2024 问的两款的现价；问项目时间与台数 ｜ 通路：俄罗斯（次要市场）；DC 客户优先 ｜ 节奏：先一封，看回信 ｜ 证据：gmail_s 2024-05-17 ×3；gmail_a 2025-12-03 ×5、2026-03-12、2026-08-10；digest in 3
- **现状一句话**：Yaroslav 2024-05 直接问 48×25G+8×100G 和 32×100G，当时没有；2025-12 说手上有 100/25G 项目并问公司网站，Alan 回「还在专注接入交换机、将来 CENTEC」——既没给网站也没给已有的 CENTEC 型号。至今 10 个月只收到群发。
- **对方真实需求（有据）**：25G/100G 数据中心/核心交换（48×25G+8×100G；32×100G）。
- **断点 / 为什么停在这里**：2025-12-03 我们的回答自己把门关了；他要的东西其实 2025-01 就已在群发里（8C48XF）。
- **Saga 现在该推什么**：P1 **STH-8C48DX-HSI（48×25G + 8×100G）；STH-32C-HSI（32×100G）**（25% 档，2026 Q2：8C48DX $4,800 / 32C $6,000 / 2C6QX $1,200 EXW）——需求台账 #13：他是仓内最早（2024-05）明确要 48×25G+8×100G 的人；对俄付款问题在他回信后再谈（RMB via CN agent）｜已发资料（勿重发）：8C48XF.png(2025-01-06)、Product Link_2026Q2(2026-03-12)｜档位说明（原 tier 字段文字「集成商/项目 25%；CENTEC 底线 ≥35% 并行」移此）：集成商/项目 25%；CENTEC 底线 ≥35% 并行
  - 复购/在买项：项；目；制；；；D；C； ；客；户；单；价；高
  - 做不了 / 要先核的：项；目；时；间；/；台；数；；；付；款；路；径；；；公；司；规；模
- **下一步（具体）**：2026-11　A 邮箱 → yb@comtinu.ru（回 2025-12-03 原线程「Booster PoE Switch」或新主题「48x25G + 8x100G — the two models you asked for in 2024」）　一封对表信：①网站 sagatele.com（他问过没答）；②他 2024-05-17 问的两款现在的型号与 EXW 价；③只问一个问题：100/25G 项目的时间与台数（第 76 批(b) 2026-10-25：audit_ab 硬错误修正：tier 字段规范为数字）
  - 第一问（只问一个）：Yaroslav — in May 2024 you asked for 48x25G + 8x100G and 32x100G; both exist now on our CENTEC-based line (STH-8C48DX-HSI $4,800, STH-32C-HSI $6,000 USD EXW, 2026 Q2 list). When is the 100/25G project you mentioned in December due, and how many units?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-05-17 | 来 | Yaroslav | Do you have 48x25G + 8x100G and 32x40/100G switches? | 精确到端口的 DC 需求 | `rfq` |
| 2024-05-17 | 去 | Simon | Sorry, it is not available at the moment. We have below ones coming soon. We can help design it for you if it is OK for you. | 当时无货 | `reply` |
| 2025-12-03 | 来 | Yaroslav | We are not having appropriate projects so far that will include such switches.（对 Booster PoE 推送） | 接入产品不对他 | `neg` |
| 2025-12-03 | 来 | Yaroslav | Yes, we have 100-25G projects What is your company website? | DC 项目在手 + 要网站 | `need` |
| 2025-12-03 | 去 | Alan | For now, we are still focusing on access switches. It will be CENTEC based=a famous Chinese chip… Please let me know if this is acceptable to you. | 断点：没给网站、没给型号价 | `reply` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：公司实体/规模（comtinu.ru 未爬）；项目时间与台数；付款路径

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **时机与节律**：真人来信 2 封（2024-05-17 → 2025-12-03）；对方本地时间中位 15:42（= 北京时间 20:42）；**他们回信中位 0.1 小时**（2 次，100% 在 24 小时内）；我方回信中位 0.8 小时（2 次）。
- **本国来询季节（RU 全库 17 个「户·月」真人来信，样本小）**：12 月 23.5% / 5 月 23.5% / 1 月 11.8%——本户来信太少，按本国节奏排下一步。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 13 封（2024-05-17 → 2026-08-10），打开标签 4 次（近 12 个月 1，最后 2025-12-03）；打开过：「L3 managed switch」×1（2024-05-17）、「24 Port Fiber Switch」×1（2025-02-28）、「Marvell Alleycat5 Solution」×1（2025-04-08）、「Booster PoE Switch」×1（2025-12-03）；从未打开：「100G Data Center Switch」、「10G Ethernet Web Managed Switch」、「8 Port Ethernet Switch」。
- **报价轨迹**（S/A 去信里「价 + 型号/描述同句」：1:1 0 条 + 个性化群发价 2 条，2024-07-15 → 2025-02-28；「今天」= 价格主表 2026-10-17 汇率、25% 档、不高于 2026-06 列表价；只列每个型号/描述最近一次，最多 8 行）：

  | 日期 | 型号 / 原句 | 当时 | 今天应报 | 变化 | 性质 | 主题 | 消息 key |
  |---|---|---|---|---|---|---|---|
  | 2025-02-28 | 「Price: 240usd/pc」 | $240 | —（原句无型号） | — | 群发价 | 24 Port Fiber Switch | `d2314ebd160508b7` |
  | 2024-07-15 | 「Price is very competitive, 220usd/pc」 | $220 | —（原句无型号） | — | 群发价 | L3 managed switch | `5be9229ad3ae9206` |

  「个性化群发价」= 同一句价发给 ≥5 家的信（Simon 的手工群发），对方未必读过，但它就是对方邮箱里躺着的「上次报价」。
- **写信的人（来信签名机械抽取）**：yb（yb@comtinu.ru，2 封，2024-05-17 → 2025-12-03）。
- **他们嘴里的词（2 封来信、去引用后 142 字符的词频）**：话题（次数，最近一次）：25G/40G/100G+ ×2（2025-12-03）。
- **渠道反应**：S 箱（Simon） 去 11（1:1 4 / 群发 7）回 1，最近回 2024-05-17；A 箱（Alan） 去 9（1:1 3 / 群发 6）回 1，最近回 2025-12-03 → 两箱都回过，按绑定行的渠道走即可。
- **最后一球**：1:1 对话 2 段，最长一段 5 封 / 跨 88 天（2024-05-17 → 2024-08-13，「RE: L3 managed switch」）；最后一句是我们说的（2026-03-12，229 天前，「Re: Booster PoE Switch」，`0e53cf03ef1552e8`）→ 球在对方手里。
- **日历窗口**：对方：2026-11-04 民族统一日；2027-01-01 新年长假（01-01 → 01-10 整体停摆） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | comtinu.ru（取自域名，公司全名待核） | 推断 |
| 国家 | 俄罗斯 | 事实（用户表）|
| 网站/域名 | comtinu.ru | 事实（用户表 URL/邮箱域名） |
| 类型 | 俄罗斯网络项目商（25G/100G 项目） | 推断（据兴趣/备注关键词） |
| 联系人 | Yaroslav | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | SFP 机架设备(类似WDM) | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | DC线索 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-24）**　网站状态：未爬（comtinu.ru）
- **是谁**：S/A 邮箱 2024-05 起 20 余封；两次真互动都指向高速/数据中心：2024-05-17「Do you have 48x25G + 8x100G and 32x40/100G switches?」（Simon 答「not available… coming soon… can help design」）；2025-12-03 先说没有相关项目，Alan 追问「do you sometimes use data center switches? 100G/10G」后答「Yes, we have 100-25G projects. What is your company website?」——Alan 回「still focusing on access switches… It will be CENTEC based」，没给网站、没给 CENTEC 型号与价（而 2025-01-06 已群发过 8C48XF）。此后只有 2026-03 Product Link 与 2026-08 $170 推送。
- **类型**：俄罗斯网络项目商（25G/100G 项目）
- **规模**：（未核）
- **【邮件】2024 即问 48×25G+8×100G / 32×100G**
  > Do you have 48x25G + 8x100G and 32x40/100G switches?
  > 来源：data/gmail_a|gmail_s/messages/<year>/<month>.jsonl（抓取 2024-05-17）
- **【邮件】2025-12 有 100-25G 项目，问公司网站**
  > Yes, we have 100-25G projects What is your company website?
  > 来源：data/gmail_a|gmail_s/messages/<year>/<month>.jsonl（抓取 2025-12-03）
- **【邮件（去）】Alan 的回答没接住**
  > For now, we are still focusing on access switches. It will be CENTEC based=a famous Chinese chip… Please let me know if this is acceptable to you.
  > 来源：data/gmail_a|gmail_s/messages/<year>/<month>.jsonl（抓取 2025-12-03）
- **KP**：Yaroslav（）yb@comtinu.ru 〔data/gmail_a|gmail_s/messages/<year>/<month>.jsonl〕
- **调研后定级**：B（原自动 C）——两次具名真互动均为 25G/100G 数据中心需求（Simon：DC 交换机客户优先）；2025-12 明说「we have 100-25G projects」后被我们一句「still focusing on access」放掉；俄罗斯为次要市场，按 B 慢慢跟进。
- 备注：俄罗斯付款：T/T USD 受限，口径里的「RMB via CN agent」是可行路径——信里不展开，对方问再说。他 2024-05 问的 48×25G+8×100G 正是 STH-8C48DX-HSI（$4,800 EXW）；32×100G = STH-32C-HSI（$6,000）。

### 加厚挖掘（2026-10-24 · 邮件证据）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Comtinu（待核） |
| 总部/地址 | 俄罗斯 |
| 其他 | comtinu.ru |

- **触达通道（公开）**：role: 项目/采购；region: 俄罗斯
- **风险/边界**：对俄付款/物流（制裁）；他问「公司网站」我们没答——sagatele.com 要给；项目时间不明
- **Saga 对位结论**：P1 STH-8C48DX-HSI（48×25G + 8×100G，$4,800 EXW）/ STH-32C-HSI（32×100G，$6,000）（25% 档）——他要的型号 Saga 现在真有价；一封信把 2024 的问题和 2025 的项目接回来
- **邮件切入句（英文）**：（见 mail_review.draft_en）

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：23 封（去 20 / 来 3）　|　**期间**：2024-05-17 → 2026-08-10　|　**最后去信**：2026-08-10
- **对方邮箱**：office@comtinu.ru、yb@comtinu.ru
- **最后一封来信**：2025-12-03 yb@comtinu.ru「RE: Booster PoE Switch」：Hi Alan, Thank you for update. We are not having appropriate projects so far that will include such switches. Best regards Yaroslav
- **邮件里报过的价**：2025-02-28 $240；2024-07-15 $220

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 24 Port PoE Managed Switch | 2026-08-10 | 2026-08-10 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-12-03 | 2026-03-12 | 2 | 4 | 7 |
| 10G Enterprise SFP Switch | 2025-10-23 | 2025-10-23 | 0 | 1 | 1 |
| 16 Port Ethernet Switch | 2025-08-25 | 2025-08-25 | 0 | 1 | 1 |
| Commercial Network Switch | 2025-05-23 | 2025-05-23 | 0 | 1 | 1 |
| Marvell Alleycat5 Solution | 2025-04-08 | 2025-04-08 | 0 | 1 | 1 |
| 24 Port Fiber Switch | 2025-02-28 | 2025-02-28 | 0 | 1 | 1 |
| 48 Port 10G Core Switch | 2025-01-06 | 2025-01-06 | 0 | 1 | 1 |
| Industrial PoE Switch | 2024-12-11 | 2024-12-11 | 0 | 1 | 1 |
| 8 Port Ethernet Switch | 2024-11-19 | 2024-11-19 | 0 | 1 | 1 |
| 10G Ethernet Web Managed Switch | 2024-10-24 | 2024-10-24 | 0 | 1 | 1 |
| 100G Data Center Switch | 2024-09-30 | 2024-09-30 | 0 | 1 | 1 |
| …共 13 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 联系方式（已有 · 原值照录）

- 邮箱：`yb@comtinu.ru`〔企业邮箱；来源：用户表原值〕
- 邮箱：`office@comtinu.ru`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Yaroslav
- 网站/域名：comtinu.ru
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Yaroslav | — | yb@comtinu.ru | 调研核实（公开页） | data/gmail_a\|gmail_s/messages/<year>/<month>.jsonl |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| DC Switches 08.10.xlsx#总表:5 | 4 | https://www.comtinu.ru/product-category/network-monitoring/sfp/ | 俄罗斯 | Yaroslav | 谷歌 | SFP 机架设备(类似WDM) | yb@comtinu.ru<br>office@comtinu.ru |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STH-8C48DX-HSI（48×25G + 8×100G，$4,800 EXW）/ STH-32C-HSI（32×100G，$6,000） | 深挖对位：他要的型号 Saga 现在真有价；一封信把 2024 的问题和 2025 的项目接回来 | 价格待核（价格主表无此型号） | 深挖对位；档位 25%（俄罗斯网络项目商（25G/100G 项目）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STH-8C48DX-HSI（48×25G + 8×100G，$4,800 EXW）/ STH-32C-HSI（32×100G，$6,000）），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STH-8C48DX-HSI（48×25G + 8×100G，$4,800 EXW）/ STH-32C-HSI（32×100G，$6,000） 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：名单内已有联系记录，不是零起点
- **W**：俄语区：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STH-8C48DX-HSI（48×25G + 8×100G，$4,800 EXW）/ STH-32C-HSI（32×100G，$6,000） 按 25% 档报价，做现供应商的第二货源；规模（调研）：（未核）
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
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：48x25G + 8x100G and 32x100G — the two models you asked for in 2024

```text
Hi, Yaroslav,

Two things I owe you from our December exchange.

Our website: https://sagatele.com/

And the two switches you asked about in May 2024 both exist now on our CENTEC-based line:
- STH-8C48DX-HSI: 48 x 25G SFP28 + 8 x 100G QSFP28, L3 with VXLAN-EVPN, MPLS, MLAG, hot-swap PSUs — $4,800 USD EXW
- STH-32C-HSI: 32 x 100G QSFP28 — $6,000 USD EXW
(2026 Q2 list, valid 15 days from this mail; your logo and model name possible.)

One question: when is the 100/25G project you mentioned in December due, and roughly how many units? With that I can confirm lead time and the payment route that works for you.

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

- **2026-11-26**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-27：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 17）；人工/调研定级 → B

---

*建档日期：2026-10-27　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
