# technetix.com
**官方名称（调研核实）**：Technetix Ltd.（英国 West Sussex；宽带/光纤接入设备品牌商；KP Mark Basham, VP Product Management – Fiber Access）

> **评级 B**　|　英国　|　档案编号 `SB-1121`　|　优先级 ★★　|　状态：有回复·跟进中
>
> **P 池并入（B 档，等级不动）：○ P 池 · 正式入池（资产池，终身跟进 + 每 2 个月巡检）**（批 AB-01 · 2026-10-29 · 下次巡检 2026-12-28）：○ P 池正式（P 正式候选，B 档并池 · 等级不动）：真回 ✔ + 对位 ✔ + 坐实 ✔；命中 4/6（成单/样品 — · 真回 ✔ · WA — · 对位 ✔ 交换机 · 登记 ✔ · 体量 集团级（HFC / 宽带接入）
>
> **类型**：OEM 品牌商（光纤/宽带接入设备）（推断）　|　**历史关系**：实质回复 2 次；推送 2 次（2025-04-22 → 2026-01-21）　|　**所在清单**：DC线索　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-1121
rating: B
rating_auto: C
sieve: pool  # 闸 3 AB1 2026-10-29
rating_research: B  # AB-FINAL-01 2026-10-30 A 级终评：降 B：排除：巨头
name_official: "Technetix Ltd.（英国 West Sussex；宽带/光纤接入设备品牌商；KP Mark Basham, VP Product Management – Fiber Access）"
score: 18
country: 英国
region: 欧洲
website: technetix.com
type: OEM 品牌商（光纤/宽带接入设备）
tier_tags: ["DC线索"]
deal: no
replies: 2
followups: 2
first_contact: 2025-04-22
last_contact: 2026-01-21
s_mail: 24 msgs (out 22 / in 2), 2024-06-20 -> 2026-08-10
p1: 无直接对位；2.5G 需求 → STI-288DGGPM / STC-28DGGPM（2.5G 铜口 + 10G SFP+，SFP+ 不跑 2.5G）；CENTEC STH10G 仅 1G/10G
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-29
sources: 1
updated: 2026-10-31
```

## SALES BRIEF（压缩模型）

- **是谁**：A 邮箱群发 22 封中两次具名真回：2025-04-22 要规格书/Marvell 芯片型号/能否定制设计/公司介绍 PPT（答：STI-488XGGPM 规格书 + 98DX2515）；2026-01-21 对 CENTEC 群发追问 10G SFP+ 能否跑 2.5G、SFP+ 口最大供电、有无 REST/JSON 管理接口、样机多快（Alan 01-22 答：NO / 见 STH10G 第 6 页 / 「RESTful API with JSON… planned and available in Q2」/ 样机 3~5 工作日）→ 无回；2026-08-10 单发 24 口 PoE $170 → 无回。巨头规则（technetix.com 在 GIANT_DOMAINS）自动 C。（调研 2026-10-24；表内兴趣：基本不用PoE 要10G工业管理收发器 3层工业交换机。8/12/16个SFP+, 主做工业品，问了芯片）
- **为什么是 B 级**：**调研后定级 B**（AB-FINAL-01 2026-10-30 A 级终评：降 B：排除：巨头）；自动分级 C：+30 实质回复 2 次（问价/要资料/问型号等）；+0 数据中心交换机线索（Hohunet/CENTEC 线）；-3 WhatsApp 加不上；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/英国；+5 最近活动 2026；-45 巨头/品牌厂商/运营商/军工（INH 规则：体量不匹配或非客户）
- **历史互动**：实质回复 2 次；推送 2 次（2025-04-22 → 2026-01-21）；最近一次客户回复：2026-01-21：问了一些问题
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-25）**：2.5G 问题的正确答案：Marvell AC5 线的 SFP+ 笼子本来就是 1G/2.5G/10G（STC-424XGGM、STI-480XGGM 等），DG 型号的 SFP 是 1G/2.5G——他问的「10G SFP+ 能否跑 2.5G」在 AC5 线上是 YES，Alan 的「NO」只对 CENTEC STH10G 成立；AC5 线无 2.5G 铜口；Realtek 商用线有（STC-18XGDGE/-PW、STC-624XGDGM 等，有价）；CENTEC VastLakes 表有 24/48 口 2.5G/5G/10G Multi-Gig 铜口（含 PoE++，无价）——收尾信第 2 点可带一句 — OEM 30%（品牌商定制）｜对外统一口径（#2/#15/#12）：2026-01-22 的「1, NO」只对 CENTEC STH10G 对；AC5 线 SFP+ = 1G/2.5G/10G（主表规格栏），这一点要补上。STOS V2.4 只有「RPC-API management」，无 REST/JSON——2026-01-22 的 Q2 承诺要主动收尾，写法「the programmable interface shipped as an RPC-based API, not REST/JSON; I will not dress it up」；巨头规则 C 不动（Q-55 默认），只发一封｜已发资料（勿重发）：Saga Software Function List-release 7.3.0(2025-03-24)、STI-488XGGPM.pdf(2025-04-23)、BigFlow V2.1 / STH10G Series / Function List V2.4(2026-01-22)；Realtek 线按 HRUI 2026-09-30 进价 +30% 现算（Q-47 默认，不用 Drive 旧表价）：STC-624XGDGPM $396→$466.4；STC-424XGGM $143 / STI-480XGGM $253 EXW（主表 @6.69）；2026-08-10 推过 24 口 PoE $170
- **第一问（只问一个）**：Mark — closing two loops from January: (1) the programmable interface on the CENTEC line shipped as an RPC-based management API, not the REST/JSON interface I said would come in Q2 — please do not plan on REST; (2) my "NO" on 2.5G was only for the CENTEC STH10G — on our Marvell line the SFP+ cages are 1G/2.5G/10G. What is the application behind the 2.5G requirement?
- **最大未知**：年走量与现供应商
- **下一步**：2026-11 A 邮箱 → mark.basham@technetix.com（回 2026-01-22 原线程「OEM Core Switching Solution」） 一封收尾信（巨头例外档，仅此一封）：①REST/JSON Q2 承诺——现状是 RPC-API，不是 REST，直说；②「SFP+ 跑 2.5G」在 CENTEC 线是 NO，在 Marvell AC5 线是 YES（1G/2.5G/10G SFP+），1 月答漏了；③只问一个问题：2.5G 那条需求背后是什么应用；不推 $170 的 24 口（第 77 批 2026-10-25 T29-U56「值得捞的处理一下」）：升 B 不改信稿；仍只此一封、不群发

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-25）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-1121` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-25。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（A 邮箱 22 去 2 来，两次都是 VP Mark Basham 具名、带 4~5 个具体技术问题；2026-01-22 Alan 答复含「REST/JSON API Q2 可用」承诺后无回；巨头规则 C → 第 77 批升 B，仅一封收尾信）** ｜ 类型：品牌商 VP 自问 ｜ 筛子：3~4（具体问题层面，未到型号/数量） ｜ 停点：我们的答复一个「NO」（SFP+ 不跑 2.5G）+ 一个未兑现的承诺（REST Q2）——他没再回 ｜ 复活：一封收尾信：交代 REST 承诺现状 + 2.5G 的正确对位机型；不带新品，不群发 ｜ 通路：英国（四大主攻之一）；巨头例外档 ｜ 节奏：一次收尾，之后半年 ｜ 证据：gmail_a 2025-03-24 → 2026-08-10（22 去 2 来）；digest in 2 / out 22；flags giant=1, wa_failed=1
- **现状一句话**：英国宽带设备品牌商 Technetix 的产品 VP 两次具名提问（2025-04 定制设计/芯片；2026-01 CENTEC 线 2.5G/供电/REST/样机）。Alan 2026-01-22 答「REST/JSON API Q2 可用」，Q2 已过，STOS V2.4 功能表没有 REST——承诺悬着；此后只收到群发与一封 $170 推送。
- **对方真实需求（有据）**：光纤接入侧的交换/汇聚：10G SFP+ 口能否 2.5G、SFP+ 供电、程序化管理接口（REST/JSON）、快速样机；更早的问题是「能否定制设计」。
- **断点 / 为什么停在这里**：2026-01-22 的答复：一个 NO + 一个未兑现的 Q2 承诺；之后 9 个月没人交代。
- **Saga 现在该推什么**：P1 **2.5G 问题的正确答案：Marvell AC5 线的 SFP+ 笼子本来就是 1G/2.5G/10G（STC-424XGGM、STI-480XGGM 等），DG 型号的 SFP 是 1G/2.5G——他问的「10G SFP+ 能否跑 2.5G」在 AC5 线上是 YES，Alan 的「NO」只对 CENTEC STH10G 成立；AC5 线无 2.5G 铜口；Realtek 商用线有（STC-18XGDGE/-PW、STC-624XGDGM 等，有价）；CENTEC VastLakes 表有 24/48 口 2.5G/5G/10G Multi-Gig 铜口（含 PoE++，无价）——收尾信第 2 点可带一句**（30% 档，Realtek 线按 HRUI 2026-09-30 进价 +30% 现算（Q-47 默认，不用 Drive 旧表价）：STC-624XGDGPM $396→$466.4；STC-424XGGM $143 / STI-480XGGM $253 EXW（主表 @6.69）；2026-08-10 推过 24 口 PoE $170）——OEM 30%（品牌商定制）｜对外统一口径（#2/#15/#12）：2026-01-22 的「1, NO」只对 CENTEC STH10G 对；AC5 线 SFP+ = 1G/2.5G/10G（主表规格栏），这一点要补上。STOS V2.4 只有「RPC-API management」，无 REST/JSON——2026-01-22 的 Q2 承诺要主动收尾，写法「the programmable interface shipped as an RPC-based API, not REST/JSON; I will not dress it up」；巨头规则 C 不动（Q-55 默认），只发一封｜已发资料（勿重发）：Saga Software Function List-release 7.3.0(2025-03-24)、STI-488XGGPM.pdf(2025-04-23)、BigFlow V2.1 / STH10G Series / Function List V2.4(2026-01-22)
  - 复购/在买项：品；牌；商；若；立；项；为；定；制；，；才；有；复；购
  - 做不了 / 要先核的：他；的；具；体；应；用；（；为；什；么；要； ；S；F；P；+； ；跑； ；2；.；5；G；）；；；T；e；c；h；n；e；t；i；x； ；供；应；商；准；入；要；求；；；R；E；S；T； ；是；否；仍；是；硬；条；件；；；S；i；m；o；n；《；S；T；H；计；划；》；：；1；G；/；2；.；5；G；/；5；G； ；铜；口； ；C；E；N；T；E；C； ；机；「；暂；不；宣；传；、；信；息；备；好；」；→； ；信；稿；只；答；「；o；n； ；r；e；q；u；e；s；t； ；/； ；n；o；t； ；o；n； ；p；u；b；l；i；s；h；e；d； ；l；i；s；t；」；，；不；主；推；；；估；算；带；见； ；C；E；N；T；E；C； ；锚；表； ；§；5；.；3；，；对；客；户；仍； ；p；r；i；c；e； ；o；n； ；r；e；q；u；e；s；t
- **下一步（具体）**：2026-11　A 邮箱 → mark.basham@technetix.com（回 2026-01-22 原线程「OEM Core Switching Solution」）　一封收尾信（巨头例外档，仅此一封）：①REST/JSON Q2 承诺——现状是 RPC-API，不是 REST，直说；②「SFP+ 跑 2.5G」在 CENTEC 线是 NO，在 Marvell AC5 线是 YES（1G/2.5G/10G SFP+），1 月答漏了；③只问一个问题：2.5G 那条需求背后是什么应用；不推 $170 的 24 口（第 77 批 2026-10-25 T29-U56「值得捞的处理一下」）：升 B 不改信稿；仍只此一封、不群发
  - 第一问（只问一个）：Mark — closing two loops from January: (1) the programmable interface on the CENTEC line shipped as an RPC-based management API, not the REST/JSON interface I said would come in Q2 — please do not plan on REST; (2) my "NO" on 2.5G was only for the CENTEC STH10G — on our Marvell line the SFP+ cages are 1G/2.5G/10G. What is the application behind the 2.5G requirement?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-04-22 | 来 | Mark Basham（VP Product Management, Fiber Access） | Do you have a data sheet… What Marvell chip is in the switch? Can you do custom designs? Do you have an overview slide deck for Saga telecom | 品牌商 VP 的定制意向问句 | `interest` |
| 2025-04-23 | 去 | Alan | please see attached datasheet. 2, Marvell 98DX 2515… Profile: About us>Factory Information>google link. Customization: in the datesheet itself, web gui or manufacturing | 答了，但没问他要做什么 | `reply` |
| 2026-01-21 | 来 | Mark Basham | Are the 10G SFP+ ports able to run at 2.5Gbps? What the max power that can be drawn by the SFP+ ports? Is there a management interface such as REST, or JSON. Can you send me a data sheet please. And finally how quickly can I get a sample if the answers to above are positive? | 四个硬问题 + 样机意愿 | `rfq` |
| 2026-01-22 | 去 | Alan | 1, NO 2, Please check the power consumption on page 6(STH10 Series) 3, A RESTful management API with JSON data format is planned and available in Q2. 4, Please see attached information. 5, For samples, 3~5 working days is good. We are still improving some features, this takes a while. | REST Q2 承诺——未兑现（STOS V2.4 无 REST） | `promise` |
| 2026-01-22 | 内 | （仓内核对 2026-10-24） | 主表规格栏：STC-424XGGM「4*1G/2.5G/10G SFP+」、STI-480XGGM「4*1G/2.5G/10GBase-X SFP+」；STI-288DGGPM 规格书「DG: 2.5 Gigabit based for optical ports」 | Alan 的「1, NO」只对 CENTEC；AC5 线 SFP+ 可跑 2.5G——收尾信要补 | `check` |
| 2026-08-10 | 去 | Alan | 24 Port PoE af/at… 10G Fiber Uplinks… Price: 170USD/PC. Do you need some samples for testing? | 与他的问题无关的推送；无回 | `push` |
| 2026-10-25 | 研 | 第 77 批复核 | C→B：品牌商 VP 两次具名提问 + 我方未兑现承诺待交代 | T29-U56；仍按 Q-55 只发一封收尾信 | `—` |
| 2026-10-29 | 查 | Agent 官网快照 LT-T03 | Welcome to Technetix - Technetix — You will be redirected to your local region. If you are not, please select your region below: | 官网快照（Actions 抓取）：在线 / 业务线 / 在卖品牌证据（非邮件事实，不计真回） | `` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：Technetix 当前产品线中哪一段需要 2.5G/SFP+ 供电（官网未爬）；REST 承诺的来源（Alan 当时依据什么说 Q2）；WhatsApp 加不上（flags.wa_failed）的时间与号码

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **时机与节律**：真人来信 1 封（2026-01-21 → 2026-01-21）；**他们回信中位 1.8 小时**（1 次，100% 在 24 小时内）；我方回信中位 14.6 小时（1 次）。
- **发信窗口（GB 全库 1094 封群发的打开标签，对方本地时间；均值 5.0%）**：周四 12–14 点 11.9%（42 封）、周二 14–16 点 7.8%（103 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **本国来询季节（GB 全库 27 个「户·月」真人来信，样本小）**：1 月 14.8% / 5 月 11.1% / 6 月 11.1%——本户来信太少，按本国节奏排下一步。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 20 封（2024-06-20 → 2026-08-10），打开标签 3 次（近 12 个月 1，最后 2026-01-21）；打开过：「24 Port Fiber Switch」×1（2024-12-18）、「Managed Optical Bypass Switch」×1（2025-04-22）、「OEM Core Switching Solution」×1（2026-01-21）；从未打开：「Marvell Industrial Alert System」、「48 port managed switch」、「2.5G Network Switch」。
- **报价轨迹**（S/A 去信里「价 + 型号/描述同句」：1:1 0 条 + 个性化群发价 3 条，2024-06-20 → 2025-01-09；「今天」= 价格主表 2026-10-17 汇率、30% 档、不高于 2026-06 列表价；只列每个型号/描述最近一次，最多 8 行）：

  | 日期 | 型号 / 原句 | 当时 | 今天应报 | 变化 | 性质 | 主题 | 消息 key |
  |---|---|---|---|---|---|---|---|
  | 2025-01-09 | 「Price is very competitive, 300usd/pc」 | $300 | —（原句无型号） | — | 群发价 | 48 Port PoE Managed Switch | `d58048ef1253134f` |
  | 2024-12-18 | 「Price: 240usd/pc」 | $240 | —（原句无型号） | — | 群发价 | 24 Port Fiber Switch | `ab451bbbef6b8078` |
  | 2024-06-20 | 「Price is very competitive, 220usd/pc」 | $220 | —（原句无型号） | — | 群发价 | 48 port managed switch | `1f3bcb7422ccdd6f` |

  「个性化群发价」= 同一句价发给 ≥5 家的信（Simon 的手工群发），对方未必读过，但它就是对方邮箱里躺着的「上次报价」。
- **写信的人（来信签名机械抽取）**：Mark Basham（mark.basham@technetix.com，1 封，2026-01-21 → 2026-01-21）。
- **他们嘴里的词（1 封来信、去引用后 568 字符的词频）**：话题（次数，最近一次）：10G ×3（2026-01-21）、2.5G ×1（2026-01-21）、光纤 / 媒体转换 ×1（2026-01-21）、样品 ×1（2026-01-21）。
- **渠道反应**：S 箱（Simon） 去 8（1:1 0 / 群发 8）回 0，从未回；A 箱（Alan） 去 14（1:1 2 / 群发 12）回 1，最近回 2026-01-21 → 只对 A 箱 Alan 有反应，下一封别换箱。
- **最后一球**：1:1 对话 1 段，最长一段 2 封 / 跨 0 天（2026-01-21 → 2026-01-22，「RE: OEM Core Switching Solution」）；最后一句是我们说的（2026-01-22，277 天前，「Re: OEM Core Switching Solution」，`98ca2068f3737796`）→ 球在对方手里。
- **同国同档参照（GB，30% 档，共 1 户有动静，列前 3）**：SA-017 parallaxdigital.co.uk（A，同档：回过 2 次（最近 2024-10-24））。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-12-24 圣诞–元旦（12-24 → 01-04；Boxing Day 12-28 补休） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 进口记录（公开海关数据 · 第 81 批 · 2026-10-27）

> 来源：**HMRC Find UK Traders（英国官方）**。英国官方数据：2016 年起非欧盟来源、2022 年起含欧盟来源的进口，按「注册公司名 × 8 位商品编码 × 月份」公示；没有供应商、数量、金额；部分公司因保密被剔除。表里「月份」只对非欧盟来源标注，无月份行多为欧盟来源（GB←EU 只公示到年）。 查询日 2026-10-27。

- 报关主体 **TECHNETIX LTD（Technetix Group，Winnersh / 宽带 HFC 设备品牌商）**；最近记录 **2026-08（85176200 / 85177900 / 85176990）**；[来源页](https://www.uktradeinfo.com/traders/technetix-ltd-60921)
- HMRC 共 **422 行（9 页）**：从硅胶、软管、电阻、电容、IC、PCB、连接器到整机——是**自己做产品的制造商**在进口料件 + 亚洲代工成品，不是经销商。
- **8517 62 00 进口月份**：2018 年 7 个月、2020 年 **全年 12 个月**、2021 年 11 个月、2023 年 10 个月、2024 年 10 个月、**2026 年 1/3/4/6/7/8 月**（2025 行在前页未逐行读，节奏同样密集）→ 几乎每月都有 8517 62 00 到货，这是它自家 HFC 放大器 / 节点 / 网关的亚洲代工成品。
- 8517 79 00（通信设备零件）2022–2026 **逐月**都有（2026 年 1–8 月连续 8 个月）；8517 69 90 2025 年 6/8/10/11 月、2026 年 7/8 月；同轴电缆 8544 20 00 2026 年 1–3 月、8536 69 10 同轴插座 2025 年 10 个月——全部围绕同轴宽带（CATV / DOCSIS）生态。
- **涉及商品编码**：85176200、85176990、85177900、85177100、85255000、85291080、85366910、85369010、85369095、85442000、85444210、8533/8534/8535/8536/8542（元器件全系列）、3910 硅胶、3917 软管
- **对 Saga 的含义**：Technetix 是宽带（HFC / DOCSIS）设备品牌商，自己有亚洲代工链，每月都在进口 8517 62 00 成品——它不会从我们这买「交换机现货」；唯一有价值的路径是 ODM：给它的光节点 / 机房配套的工业以太网交换或 PoE 供电模块报 OEM 30% 档。热度只有 31，这条线放到 B 慢慢跟进即可，别投入群发之外的精力。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-29 查）：**

- `technetix.com` → Mimecast 企业网关（MX：eu-smtp-inbound-1.mimecast.com、eu-smtp-inbound-2.mimecast.com）。企业级邮件网关（Mimecast 企业网关）：链接重写 + 附件沙箱 → 像素失效、附件常被隔离，冷邮件到达率最低；这户靠回原线程 / LinkedIn / 对方来信，不靠新开线程群发

**假日避让（英国 · 按下一步「2026-11」窗口 2026-11-01→2026-11-30）：**

- 窗口内无该国法定假日

**公司底数 · 第 84 批（UK · Companies House（公司页 + 高管页，2026-10-27 抓取），2026-10-27 查；https://find-and-update.company-information.service.gov.uk/company/02484988）：**

- 法定名 / 登记号：TECHNETIX LIMITED · 02484988 · 状态 **Active** · 成立 1990-03-26 · Private limited company · 母公司 TECHNETIX GROUP LIMITED（05303822，2004-12-03 成立，同址）；关联 TECHNETIX NETWORKS LIMITED（03240196，2018-02-27 注销）
- 行业码 / 经营范围：26110 电子元件制造；26400 消费电子制造；46520 电子与通信设备批发
- 注册地址：Innovation House, Technetix Business Park, Muddleswood Road, Albourne, Hassocks, West Sussex BN6 9EB
- 规模档：集团级（HFC / 宽带接入设备制造商，欧洲多国子公司）
- 账目：最近账目至 2025-12-31 已报（全账，非微型）；下一期至 2026-12-31；2027-09-30；确认声明下期 2027-02-19（到期 2027-03-05）
- 高管：BROADHURST, Paul Antony — Director（1991 年前即在任，1960 年生；创始人 / 长期掌舵人；身份已核验）
- 高管：DEAKIN, Philip James — Director（2024-01-30 起，1969 年生）
- 高管：PLOWMAN, Thomas William — Secretary（2023-10-31 起）；29 名历任高管 / 26 人已辞任（公司秘书频繁更替）
- 控制人 / 股东：TECHNETIX GROUP LIMITED（05303822）为直接母公司（PSC 页未抓取，待下一轮）
- 抵押 / 诉讼 / 担保：未抓取
- 曾用名：TECHNETIX PLC（1990-05-30 → 2004-11-30）；CHARTSCALE LIMITED（1990-03-26 → 1990-05-30）
- **这意味着什么：**
  - **制造商集团（HFC 有线宽带设备，SIC 26110）而非分销商**：交换机对他们是配套 / 子系统件（头端机房、光节点管理口）→ OEM / 配套 30% 线，提案写「Technetix-labelled Ethernet access / management switches」，不是整线替换
  - 创始人 Paul Broadhurst 1991 年前即任董事、仍在任；2024-01 新增董事 Deakin → 可能是接班 / 财务线；研究档 KP 若非董事，先走采购经办，提案要能让经办人转给董事
  - 英国 UKCA + CE / RoHS；集团采购走供应商审核（ISO 9001 / 工厂资料）—— 备齐再谈价；付款：集团账期 30–60 天是常态，首单仍坚持 T/T 预付或 LC
  - 账目年 12 月止、9 月底前公示：2026-10 之后可读 2025 全账（Companies House 免费 PDF），下一轮抓营收 / 员工数
- 备注：B 档 GB 首户（第 84 批 B 欧美土起步）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | technetix.com（取自域名，公司全名待核） | 推断 |
| 国家 | 英国 | 事实（用户表）|
| 网站/域名 | technetix.com | 事实（用户表 URL/邮箱域名） |
| 类型 | OEM 品牌商（光纤/宽带接入设备） | 推断（据兴趣/备注关键词） |
| 联系人 | Mark | 事实（用户表） |
| 来源（From） | IFSEC fair <br>2023 | 事实（用户表） |
| 兴趣（Interested in） | 基本不用PoE<br>要10G工业管理收发器 3层工业交换机。8/12/16个SFP+, 主做工业品，问了芯片 | 事实（用户表） |
| 用户备注（Remark） | 44 7827 990840 <br>加不上  比较专业 | 事实（用户表） |
| 所在清单 | DC线索 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-24）**　网站状态：正常（technetix.com）
- **是谁**：A 邮箱群发 22 封中两次具名真回：2025-04-22 要规格书/Marvell 芯片型号/能否定制设计/公司介绍 PPT（答：STI-488XGGPM 规格书 + 98DX2515）；2026-01-21 对 CENTEC 群发追问 10G SFP+ 能否跑 2.5G、SFP+ 口最大供电、有无 REST/JSON 管理接口、样机多快（Alan 01-22 答：NO / 见 STH10G 第 6 页 / 「RESTful API with JSON… planned and available in Q2」/ 样机 3~5 工作日）→ 无回；2026-08-10 单发 24 口 PoE $170 → 无回。巨头规则（technetix.com 在 GIANT_DOMAINS）自动 C。
- **类型**：OEM 品牌商（光纤/宽带接入设备）
- **规模**：（集团数百人；未核）
- **【邮件】VP 产品管理问定制设计与公司介绍**
  > What Marvell chip is in the switch? Can you do custom designs? Do you have an overview slide deck for Saga telecom
  > 来源：data/gmail_a/messages/<year>/<month>.jsonl（抓取 2025-04-22）
- **【邮件】CENTEC 线四问：2.5G on SFP+ / SFP+ 供电 / REST·JSON / 样机速度**
  > Are the 10G SFP+ ports able to run at 2.5Gbps? What the max power that can be drawn by the SFP+ ports? Is there a management interface such as REST, or JSON… how quickly can I get a sample
  > 来源：data/gmail_a/messages/<year>/<month>.jsonl（抓取 2026-01-21）
- **【邮件（去）】Alan 承诺 REST/JSON API「Q2 可用」**
  > 1, NO 2, …page 6(STH10 Series) 3, A RESTful management API with JSON data format is planned and available in Q2. 4, … 5, For samples, 3~5 working days
  > 来源：data/gmail_a/messages/<year>/<month>.jsonl（抓取 2026-01-22）
- **KP**：Mark Basham（）mark.basham@technetix.com +44 1444 251260 / m +44 7827 990840（信尾；对外材料不写电话）〔data/gmail_a/messages/<year>/<month>.jsonl〕
- **调研后定级**：B（原自动 C）——AB-FINAL-01 2026-10-30 A 级终评：降 B：排除：巨头
- 备注：LT-T03 官网快照加厚（2026-10-29）：site_contacts/deep/facts。
巨头规则（INH：体量不匹配）→ C 不动；但这是仓内少有的英国品牌商 VP 两次具名提问，按 Q-55「巨头例外档」处理：档案齐全，只允许一封收尾信（把 2026-01-22 的 REST 承诺交代清楚），不进群发。flags.wa_failed=1（WhatsApp 加不上）。｜第 77 批：C→B（见 override_reason）；收尾信不变，2026-11 发。

### 加厚挖掘（2026-10-24 · 邮件证据 + 官网常识 + 官网快照（LT-T03 2026-10-29））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | TECHNETIX LIMITED（Companies House 02484988；SIC 26110 / 26400 / 46520；账目至 2025-12-31 已报，下期 2027-09-30 到期）（第 84 批 官方登记核实 2026-10-27） |
| 总部/地址 | Albourne, West Sussex, UK |
| 其他 | 宽带/光纤接入设备（信尾 Fiber Access） |

- **触达通道（公开）**：role: VP Product Management；region: 英国
- **风险/边界**：巨头采购流程（供应商准入/UL/合规）小贸易商难进；2026-01-22 对他说了「RESTful API JSON Q2 可用」——STOS V2.4（2026/Q2）功能表只有「RPC-API management」，无 REST/JSON 字样：承诺未兑现或措辞不符，需交代；他真正的兴趣（2.5G on SFP+、SFP+ 供电）指向光纤接入侧的特殊用法，Saga 标准机型不对位
- **Saga 对位结论**：P1 无直接对位；2.5G 需求 → STI-288DGGPM / STC-28DGGPM（2.5G 铜口 + 10G SFP+，SFP+ 不跑 2.5G）；CENTEC STH10G 仅 1G/10G（30% 档）——品牌商/定制意向，但巨头体量；先把承诺交代清楚，再看他是否还有话
- **邮件切入句（英文）**：（见 mail_review.draft_en）

### 官网快照（自动摘要 · 抓取 2026-10-29 · 状态：在线）

- **首页**：https://technetix.com/　语言：en-US　站点地图 URL 数：1
- **标题**：Welcome to Technetix - Technetix
- **描述**：You will be redirected to your local region. If you are not, please select your region below:
- **首页栏目**：Welcome to Technetix / You will be redirected to your local region. / If you are not, please select your region below:
- **社媒**：https://americas.technetix.com/, https://emea.technetix.com, https://technetix.com/
- 首页正文摘录：Skip to content Welcome to Technetix You will be redirected to your local region. If you are not, please select your region below: Americas EMEA ©2026 Technetix. All Rights Reserved.
- 数据文件：`data/saga_clients/site_snapshots/SB-1121.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 2 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-04-22 | 2025.4.22 | bypass | 问了一些问题 | A |  | DC Switches 08.10.xlsx#23 |
| 2026-01-21 | 2026.1.21 | CENTEC | 问了一些问题 | A |  | DC Switches 08.10.xlsx#23 |

## B 分层（B-PASS-01 · 2026-10-31）：**B2**

- 依据：巨头：不追，标记；身份 登记坐实 · 路径 活 · 回信 R+ · 区域档 focus
- 节奏：B1 重点普通跟 = 分组群发每 6 周 + 一年两次点名；B2 普通跟 = 分组群发每 8 周；C 储备 = 不发、两月巡检，有动静捞回。

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：24 封（去 22 / 来 2）　|　**期间**：2024-06-20 → 2026-08-10　|　**最后去信**：2026-08-10
- **对方邮箱**：mark.basham@technetix.com
- **最后一封来信**：2026-01-21 mark.basham@technetix.com「RE: OEM Core Switching Solution」：Hello Alan, Thanks for the info. Are the 10G SFP+ ports able to run at 2.5Gbps? What the max power that can be drawn by the SFP+ ports? Is there a management interface such as REST, or JSON. Can you send me a data sheet please. And finally how quickly can I ge
- **邮件里报过的价**：2025-01-09 $300；2024-12-18 $240；2024-06-20 $220

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 24 Port PoE Managed Switch | 2026-08-10 | 2026-08-10 | 0 | 1 | 1 |
| OEM Core Switching Solution | 2026-01-21 | 2026-01-22 | 1 | 2 | 6 |
| Marvell Industrial Alert System | 2025-12-22 | 2025-12-22 | 0 | 1 | 1 |
| Optional Marvell Chipset Solutions | 2025-11-24 | 2025-11-24 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-05 | 2025-11-05 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-10 | 2025-10-10 | 0 | 1 | 1 |
| 16 Port Ethernet Switch | 2025-09-17 | 2025-09-17 | 0 | 1 | 1 |
| Marvell Networking Solutions | 2025-08-14 | 2025-08-14 | 0 | 1 | 1 |
| L3 Managed Switch | 2025-07-04 | 2025-07-04 | 0 | 1 | 1 |
| Marvell Industrial Alert System | 2025-06-06 | 2025-06-06 | 0 | 1 | 1 |
| Managed Optical Bypass Switch | 2025-04-22 | 2025-04-23 | 1 | 2 | 9 |
| Marvell Software Function List | 2025-03-24 | 2025-03-24 | 0 | 1 | 2 |
| …共 20 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：2 个　|　**数据截至**：2026-10-29T15:11:51Z　|　**最近变化**：2026-10-29T15:11:51Z
- **最近变化摘要**：2026-10-29 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-1121/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://technetix.com/) | html | HTTP 200 | 2026-10-29T15:11:51Z | 215 字符；首行：Welcome to Technetix - Technetix |
| [sitemap](https://technetix.com/sitemap_index.xml) | sitemap | 待首轮 | — | 站点地图（2026-10-21 时 1 条） |

## 联系方式（已有 · 原值照录）

- 邮箱：`mark.basham@technetix.com`〔企业邮箱；来源：用户表原值〕
- 电话：`+447827990840`〔WhatsApp 加不上；原值见来源表〕
- 联系人（原值）：Mark
- 网站/域名：technetix.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Mark Basham | — | mark.basham@technetix.com / +44 1444 251260 / m +44 7827 990840（信尾；对外材料不写电话） | 调研核实（公开页） | data/gmail_a/messages/<year>/<month>.jsonl |
| Mark | — | mark.basham@technetix.com / +447827990840 | 用户表原值 | Clients/ 表 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| DC Switches 08.10.xlsx#总表:24 | 23 | https://emea.technetix.com/ | 英国 | Mark | IFSEC fair <br>2023 | 基本不用PoE<br>要10G工业管理收发器 3层工业交换机。8/12/16个SFP+, 主做工业品，问了芯片 | mark.basham@technetix.com | 44 7827 990840 <br>加不上  比较专业 | 2 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | 无直接对位；2.5G 需求 → STI-288DGGPM / STC-28DGGPM（2.5G 铜口 + 10G SFP+，SFP+ 不跑 2.5G）；CENTEC STH10G 仅 1G/10G | 深挖对位：品牌商/定制意向，但巨头体量；先把承诺交代清楚，再看他是否还有话 | 价格待核（价格主表无此型号） | 深挖对位；档位 30%（OEM 品牌商（光纤/宽带接入设备）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（无直接对位；2.5G 需求 → STI-288DGGPM / STC-28DGGPM（2.5G 铜口 + 10G SFP+，SFP+ 不跑 2.5G）；CENTEC STH10G 仅 1G/10G），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + 无直接对位；2.5G 需求 → STI-288DGGPM / STC-28DGGPM（2.5G 铜口 + 10G SFP+，SFP+ 不跑 2.5G）；CENTEC STH10G 仅 1G/10G 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 2 次实质回复（对方认识我们）；自有品牌/贴牌需求 = 现成 OEM 客户；欧洲主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 无直接对位；2.5G 需求 → STI-288DGGPM / STC-28DGGPM（2.5G 铜口 + 10G SFP+，SFP+ 不跑 2.5G）；CENTEC STH10G 仅 1G/10G 按 30% 档报价，做现供应商的第二货源；贴牌 + 定制 UI/型号 → 30% 档与长期绑定；规模（调研）：（集团数百人；未核）
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
| 采购量/预算 | ❓ 未确认（有回复但未报量） |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: OEM Core Switching Solution — closing two loops from January

```text
Hello Mark,

Two things from my January reply that I owe you a straight update on.

1. The management interface: I wrote that a RESTful API with JSON would be available in Q2. What shipped in the 2026/Q2 software is an RPC-based management API plus SNMP v3 and CLI — not REST/JSON. Please do not plan on REST from our side; I would rather say so than let the Q2 line stand.

2. 2.5G on SFP+: my "NO" was correct only for the CENTEC STH10G. On our Marvell AC5 line the SFP+ cages run at 1G/2.5G/10G (for example 24 x GbE + 4 x SFP+, or the industrial 8 x GbE + 4 x SFP+ at -40 to +75 C), and the DG models carry 1G/2.5G SFP. I should have said that in January. Copper ports on that line are 1G; if the requirement is multi-gig copper, we have two ways: the commercial Realtek line (8 x 2.5G PoE + 10G SFP web-managed at $66 USD EXW, 24 x 2.5G PoE++ L3 at $466.4 USD EXW, single PSU) or, on request and not on our published list, CENTEC-based 24/48 x 2.5G/5G/10G Base-T units with PoE++ and dual PSU.

One question: what is the application behind the 2.5G requirement — ONT/CPE uplinks, or something else? That tells me whether a sample (3-5 working days) is worth your time.

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

- **2026-11-30**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-31：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 C，分数 18）；人工/调研定级 → B

---

*建档日期：2026-10-31　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
