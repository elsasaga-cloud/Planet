# larch-networks.com

> **评级 B**　|　以色列　|　档案编号 `SB-359`　|　优先级 ★★　|　状态：名单内·未触达
>
> **类型**：网络软硬件方案商 + 自有品牌工业交换机（中国 ODM 采购）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：A已回复　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-359
rating: B
rating_auto: B
score: 44
country: 以色列
region: 中东
website: larch-networks.com
type: 网络软硬件方案商 + 自有品牌工业交换机（中国 ODM 采购）
tier_tags: ["A已回复"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 38 msgs (out 24 / in 14), 2025-05-21 -> 2026-07-02
p1: STI-488XGGPM
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-21
sources: 1
updated: 2026-10-27
```

## SALES BRIEF（压缩模型）

- **是谁**：以色列 Larch Networks（定制网络软硬件开发：系统工程 / SONiC（Hardware-Accelerated BFD+）；自有品牌工业交换机 LN-1508G(P)-4XGF-I(-M)（8 GE/PoE + 4×10G SFP+ 工业）、LN-2308GP-2GE-I，16×PoE / 48×PoE 工业页；表内「DCN / 中科德能的工业 FS」= 现由中国 ODM 供货；KP Alexander Cheskis、Andrey Zarudniy；参展 Electronica India 2026）；表内无跟进记录。（调研 2026-10-21；表内兴趣：dcn 工业FS 中科德能的）
- **为什么是 B 级**：+18 在「已回复」名单（A/E Replied）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+3 区域 中东/以色列
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-488XGGPM-2BT（4×10G SFP+ + 8×GE PoE，2 通道光旁路，L2+，-40~75℃；2025-12-09 报 $295） — C10/C11：这户的价值是**情报**（他们知道谁在做 8,000 台项目、SONiC 市场动向），不是订单。已打开的主题（21/24 封有打开记录）：「Re: Supported SONiC for Saga Ethernet 」(2026-05-27)、「Re: Supported SONiC for Saga Ethernet 」(2026-06-03)、「Re: Supported SONiC for Saga Ethernet 」(2026-06-05)、「Re: Request for DX1518/DX1548 Chips」(2026-07-02) → 读者兴趣偏「旁路/Booster」；当前 P1 属「10G 汇聚/L3」，下一封按「旁路/Booster」给，不按 P1｜对外统一口径（#2/#12）：2026-03-31 Alan 反问「Do you require Marvell SDK/BSP support」暗示可给 BSP——Saga 不提供 SDK/BSP，对 Larch（SONiC/白盒）只谈整机或 PCBA；2026-05-27「AC5 整线 +$15（内存涨价）」是对外涨价基准；$295 USD EXW（2025-12-09 口径）；现以 `列表价 USD EXW（2026-10-17 快照，15 天有效）` 重报，bypass -2FBP 档 $283.7 @30% 为主表锚；历史报价（邮件原话，老汇率）：2025-12-09 STI-488XGGPM-2BT 295usd；2025-12-01 STI-488XGGBPM 215usd
- **第一问（只问一个）**：Andrey — the 2-channel bypass PoE unit you priced in December ($295): is a paid evaluation sample still useful for your customer, or has that requirement closed?
- **最大未知**：年走量与现供应商
- **下一步**：被动（Q-49）；若对方再来信，先把旁路机样机这条线接上 A 邮箱（alexander@ / azarudniy@ / oksana@larch-networks.com） 不主动发；来信时只谈旁路/Booster PoE 样机，不碰校园项目与 SONiC（第 76 批(c) 2026-10-25：型号笔误 STI-488XGGPM2B-2BT → STI-488XGGPM-2BT）

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-359` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达→边界户（A 邮箱 2025-05 → 2026-07 来 14 去 24，三位 KP：Alexander Cheskis / Andrey Zarudniy（Sales）/ Oksana Loi；四轮实质：① 2025-05 光旁路交换机技术问答（98DX2515 口径）② 2025-12 旁路 PoE STI-488XGGPM-2BT 报 $295，对方要样机与批量价后无单 ③ 2026-03-30 其客户 8,000 台校园 L2（24×1G + 4×10G SFP+，目标 $250）→ Alan 03-31「与我们一个国内客户冲突，内部决定，到此为止」（Q-49）④ 2026-05/06 Larch 推销 SONiC 商业支持并邀 6-10/11 线上会 → Alan 06-05 婉拒（Saga 高速线用 CENTEC，Marvell 线只做 SMB L2+/L3）；07-02 求购 DX1518/DX1548 芯片 10 颗 → 无货)；Elsa 箱：`to:larch-networks.com` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 24 / 来 14）（第 74 批(n)）** ｜ 类型：以色列 SONiC/NOS 软件服务商 + 渠道（Larch Networks；既是潜在客户也是潜在供应商） ｜ 筛子：2（技术问答 + 询价 + 项目需求；未付样） ｜ 停点：两头都停：Saga 拒了 8,000 台项目（国内客户冲突）、拒了 SONiC 合作与芯片；对方对 $295 旁路机没有下文 ｜ 复活：只在 Larch 来信时回（Q-49 边界）；若 Simon 判定 8,000 台项目不构成冲突，Andrey 03-31 的追问「client = 买家还是中国工厂？」还没被正面回答 ｜ 通路：IL 部分（收款/物流无先例） ｜ 节奏：最后来信 2026-07-02（芯片求购）；Alan 最后回 2026-07-02 ｜ 证据：A 邮箱 k=c3ec0dc5b8622bbb / 827e3f81f687bb3b / f0fca5051f786b75 / 48f6b22ac0e2c199 / f77f97cdc39f10a5；第 19 批回补来信原文 8 条（gmail_s/gmail_a）
- **现状一句话**：Larch Networks（以色列，SONiC/NOS 商业支持 + 硬件渠道）是少数会追着 Saga 问芯片型号、RAM/Flash、样机与批量价的对手盘。2025-12 对旁路 PoE 机问到 $295 单价即止；2026-03-30 带来 8,000 台校园 L2 项目（24×1G + 4×10G、可换 PSU、冗余风扇、USB 管理、目标 $250），Alan 次日以「国内客户冲突」停掉；2026-05 起对方转为推销 SONiC 方案并要 AC5 现货清单、约线上会，Alan 给了 AC5 过渡全貌（商用 8/24/48 口已量产、工业全系列 AC5 样机）但拒绝会议；07-02 求购 DX1518/DX1548 芯片被拒。
- **对方真实需求（有据）**：① 旁路 PoE 工业管理机（已报 $295）② 8,000 台校园 L2 交换机（已拒）③ 把 Saga 的 Marvell 线作为 SONiC 落地硬件（Saga 不要）④ Marvell 芯片现货（无）
- **断点 / 为什么停在这里**：不是对方不买，而是 Saga 两次说不（项目冲突、SONiC 方向）。剩下的唯一商业线是旁路/Booster PoE 机的样机——对方 2025-12-09 明确要「sample and bulk price」，Alan 给了单价 $295 但没推样机付款流程，线就冷了。
- **Saga 现在该推什么**：P1 **STI-488XGGPM-2BT（4×10G SFP+ + 8×GE PoE，2 通道光旁路，L2+，-40~75℃；2025-12-09 报 $295）**（25% 档，$295 USD EXW（2025-12-09 口径）；现以 `列表价 USD EXW（2026-10-17 快照，15 天有效）` 重报，bypass -2FBP 档 $283.7 @30% 为主表锚；历史报价（邮件原话，老汇率）：2025-12-09 STI-488XGGPM-2BT 295usd；2025-12-01 STI-488XGGBPM 215usd）——C10/C11：这户的价值是**情报**（他们知道谁在做 8,000 台项目、SONiC 市场动向），不是订单。已打开的主题（21/24 封有打开记录）：「Re: Supported SONiC for Saga Ethernet 」(2026-05-27)、「Re: Supported SONiC for Saga Ethernet 」(2026-06-03)、「Re: Supported SONiC for Saga Ethernet 」(2026-06-05)、「Re: Request for DX1518/DX1548 Chips」(2026-07-02) → 读者兴趣偏「旁路/Booster」；当前 P1 属「10G 汇聚/L3」，下一封按「旁路/Booster」给，不按 P1｜对外统一口径（#2/#12）：2026-03-31 Alan 反问「Do you require Marvell SDK/BSP support」暗示可给 BSP——Saga 不提供 SDK/BSP，对 Larch（SONiC/白盒）只谈整机或 PCBA；2026-05-27「AC5 整线 +$15（内存涨价）」是对外涨价基准
  - 做不了 / 要先核的：不卖芯片、不做 SONiC 移植、不碰国内冲突项目——三条都已书面说过，别再开口
- **下一步（具体）**：被动（Q-49）；若对方再来信，先把旁路机样机这条线接上　A 邮箱（alexander@ / azarudniy@ / oksana@larch-networks.com）　不主动发；来信时只谈旁路/Booster PoE 样机，不碰校园项目与 SONiC（第 76 批(c) 2026-10-25：型号笔误 STI-488XGGPM2B-2BT → STI-488XGGPM-2BT）
  - 第一问（只问一个）：Andrey — the 2-channel bypass PoE unit you priced in December ($295): is a paid evaluation sample still useful for your customer, or has that requirement closed?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-05-22 | 来 | alexander@larch-networks.com | Hi Alan, Thank you for sharing this — the Optical Bypass Switch is definitely of interest to us. To evaluate further, could you kindly share more tech | 来信原文（主题「Re: Managed Optical Bypass Switch」；第 19 批从 gmail_a 回补，之前只有计数没有原话） | `6029bd8a3ce4a534` |
| 2025-05-23 | 去 | Alan → Alexander Chesnokov（Larch） | 1, Marvell 98DX2515 CPU: ARM V8 1.2G FLASH: 512MB RAM: 512MB 2, Please see attached datasheet. 3, Sorry, I am not at the exhibition. But we can have some online meetings | AC5 Lite 平台硬件规格首次对外（98DX2515 / A72 1.2G / 512M）——Larch 做 SONiC/白盒，问芯片就是在评估能否跑自己的 NOS；后来 2026-06-05 Alan 拒绝 SONiC 会议一致 | `gmail_a 2025-05-23 Re: Managed Optical Bypass Switch` |
| 2025-07-23 | 去 | Saga（Alan） | Hi, Alexander, How are you? We are doing Marvell Alleycat5 chip for tailored networking solutions. 1, Support Web GUI change(Logo, model name, MAC, SN, SNMP, OID) 2, Added interesting features(Sftp, Https, L3 Routing) 3, Prestera 98DX25xx and 98DX35xx series [image: Web GUI] Lets talk about it if yo… | Saga 实质答复原文（主题「Re: Managed Optical Bypass Switch」；第 20 批从 gmail_a 回补）——承诺/口径以此为准 | `d8a5be10fcec6d02` |
| 2025-11-28 | 来 | alexander@larch-networks.com | Hi Alan, That’s very interesting — especially the Marvell-based design and the 12–54V PoE booster concept. Let’s discuss more details — which Marvell | 来信原文（主题「Re: Booster PoE Switch」；第 19 批从 gmail_a 回补，之前只有计数没有原话） | `21ed9f8ba13a5507` |
| 2025-12-01 | 去 | Saga（Alan） | Hi, Alexander, 1, yes, we can supply a demo unit for your study and testing. 2, please see attached datasheet(2026/Q1 version). STI-488XGGBPM 215usd/pc Industrial PoE Managed Switch 4*1G/2.5G/10G SFP+8*10/100/1000M RJ45/PoE +1*Console Port+1*USB Port 8*PoE af/ | 历史报价点（主题「Re: Booster PoE Switch」；第 20 批从 gmail_a 回补）：STI-488XGGBPM 215usd | `3a03a13e6ecdd2d5` |
| 2025-12-08 | 来 | azarudniy@larch-networks.com | Hello Alan! Alex told me that you have some Baypass devices. Could you please share the deteils. Thanks Best regards, Andrey Sales manager. https://la | 来信原文（主题「Re: Booster PoE Switch」；第 19 批从 gmail_a 回补，之前只有计数没有原话） | `22c03a7535263d1a` |
| 2025-12-09 | 来 | azarudniy@larch-networks.com | Alan, Greate! Please also provide the sample and bulk price with some HW Specification (what the chipset, PHY, flash, memory ?) Best regards, Andrey S | 来信原文（主题「Re: Booster PoE Switch」；第 19 批从 gmail_a 回补，之前只有计数没有原话） | `fd4f4163ed089c3f` |
| 2025-12-09 | 去 | Saga（Alan） | Hi, Andrey, 1, Unit price: 295usd/pc STI-488XGGPM-2BT 4*1G/2.5G/10G SFP+8*100/1000M RJ45/PoE +1*Console Port 2*PoE af/at/bt, 6*PoE af/at, 240W, L2+ Managed, Active PoE DC48V output, Support Bypass feature(2 channels) DC44V~DC57V, (Removable 4-PIN Industrial | 历史报价点（主题「Re: Booster PoE Switch」；第 20 批从 gmail_a 回补）：STI-488XGGPM-2BT 295usd | `2c412f7579125bdb` |
| 2025-12-10 | 来 | Alexander Chesnokov（Larch Networks） | And can you send the info about bypass switch? | Booster PoE 群发之后主动要旁路（bypass）资料——Larch 的兴趣点有两个：8,000 台校园项目（后判国内冲突，Q-49）和旁路机；旁路是不冲突的那条 | `gmail_a 2025-12-10 Re: Booster PoE Switch` |
| 2026-03-30 | 来 | Alexander（Larch） | a customer of ours needs 8,000 units of a Campus L2 switch… 24× 1G ETH + 4× 10G SFP+ • PSU: Field-replaceable, 1× AC 100–240V • Fans: Internal redundant | A 邮箱最大数量需求 | `c3ec0dc5b8622bbb` |
| 2026-03-31 | 去 | Alan | it seems to be in conflict with one of our clients. They are also following up with this project. so we have to stop here!! | C11 让路 | `827e3f81f687bb3b` |
| 2026-03-31 | 去 | Alan | target price 250usd/pc is a little difficult… Client means a domestic client who is working on this project I have to stop here, its an internal decision | 国内冲突 + 价格两重原因（E23） | `f0fca5051f786b75` |
| 2026-03-31 | 来 | Andrey Zarudniy（Larch Networks，销售经理） | By the word clients, do you mean the client who buys this equipment from you, or is it the factory in China that is your client? Maybe this is a different project. | Alan 说「与我们一个客户冲突」时，对方追问「你的客户是买家还是中国工厂」——Saga 的边界话术在客户眼里是含糊的；下次说「与现有渠道约定冲突」即可，不必解释是谁 | `gmail_a 2026-03-31 Re: Updated Ethernet Switches Links` |
| 2026-05-22 | 来 | Alexander | Larch Networks can help switch vendors add a commercially supported SONiC option without building a full in-house NOS team | 角色翻转：对方成了供应商 | `48f6b22ac0e2c199` |
| 2026-05-25 | 来 | alexander@larch-networks.com | Hi Alan, Thanks for the candid reply — fully understood on the CENTEC track for high-speed. Let me flip the question. On the Marvell side, we're activ | 来信原文（主题「Re: Supported SONiC for Saga Ethern」；第 19 批从 gmail_a 回补，之前只有计数没有原话） | `231732b0e66a97ce` |
| 2026-05-25 | 去 | Saga（Alan） | Hi, Alex, Thanks for your info. 1. We are switching from AC3 and AC5 chipset for ALL models, this is almost done. You are a professional at Marvell and must know that AC5 is a very good balance option on cost & performance. And AC5 will be our long-term anchored solution. 2. As I explained in point… | Saga 实质答复原文（主题「Re: Supported SONiC for Saga Ethernet Sw」；第 20 批从 gmail_a 回补）——承诺/口径以此为准 | `3c888655608fcc01` |
| 2026-05-25 | 去 | Saga（Alan） | Hi, Alexander, Thanks for your info and the introduction to Larch Networks’ SONiC offering. 1. At the moment, our Marvell based models are mainly focusing L2+/L3 SMBs and enterprise network, lower-speed deployments. As you may notice, our high-speed networks is about CENTEC chip, a famous domestic c… | Saga 实质答复原文（主题「Re: Supported SONiC for Saga Ethernet Sw」；第 20 批从 gmail_a 回补）——承诺/口径以此为准 | `36ef0d39b4e679c2` |
| 2026-05-26 | 来 | alexander@larch-networks.com | Hi Alan, Thanks — this is very useful context on the AC3 to AC5 transition and the L2+/L3, 1G/10G positioning. To size this properly on our side, coul | 来信原文（主题「Re: Supported SONiC for Saga Ethern」；第 19 批从 gmail_a 回补，之前只有计数没有原话） | `4722032cae2191bd` |
| 2026-05-27 | 去 | Alan | AC3 to AC5 transition is almost done for ALL models… commercial models, 8 / 24 / 48 Port L2+/L3 models, AC5 is fully ready and in normal production… industrial models, ALL models got AC5-ready samples | Saga 产品线状态的权威书面版本（2026-05） | `ddbe426f9e94bdd4` |
| 2026-06-02 | 来 | oksana@larch-networks.com | Hi Alan, Would you be available to meet with us on June 10 or 11? What time would be convenient for you? Thanks in advance, BR, Oksana Loi. On Wed, Ma | 来信原文（主题「Re: Supported SONiC for Saga Ethern」；第 19 批从 gmail_a 回补，之前只有计数没有原话） | `76c0582f1181f61b` |
| 2026-06-03 | 来 | oksana@larch-networks.com | Hi Alan, The exhibition is going very well, and we have a lot of visitors. As Alex mentioned earlier, we would like to arrange a short online meeting | 来信原文（主题「Re: Supported SONiC for Saga Ethern」；第 19 批从 gmail_a 回补，之前只有计数没有原话） | `ce5ef79be8ca9c8c` |
| 2026-06-05 | 去 | Saga（Alan） | Hi, Oksana, Thanks for your information. 1. Good to know that everything is going well there! 2. In previous emails, we discussed high-speed network switches(Marvell based and CENTEC based) and L2 / L3 Ethernet switches for SMBs. Your focus is on Marvell SONiC for high-speed networks. But we are cur… | Saga 实质答复原文（主题「Re: Supported SONiC for Saga Ethernet Sw」；第 20 批从 gmail_a 回补）——承诺/口径以此为准 | `d637bcde75ed85d8` |
| 2026-07-02 | 来 | Oksana（Larch） | We urgently need 10 pieces of DX1518/DX1548 chips… Could you please let us know if you have any of these chips in stock? | 芯片请求被拒（Marvell 采购审查） | `f77f97cdc39f10a5` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：Q-49：「国内客户冲突」的边界待 Simon 判；06-10/11 线上会最终是否发生：A 邮箱无记录（Alan 06-05 婉拒后无会议邮件）

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **时机与节律**：真人来信 11 封（2025-11-28 → 2026-07-02）；多在 3 月（3） / 5 月（3） / 6 月（2）；对方本地时间中位 13:06，四分位 09:30–15:30（= 北京时间 19:06）；周二最多（4）；**他们回信中位 11.1 小时**（9 次，78% 在 24 小时内）；我方回信中位 5.4 小时（11 次）。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 3 封（2025-05-21 → 2026-03-30），打开标签 3 次（近 12 个月 2，最后 2026-03-30）；打开过：「Managed Optical Bypass Switch」×1（2025-05-21）、「Booster PoE Switch」×1（2025-11-27）、「Updated Ethernet Switches Links」×1（2026-03-30）。
- **品类覆盖与缺口**：官网兴趣：工业（industrial 65 / automation 0） / 10G 汇聚（10g 30 / sfp 40）；我们 1:1 从未报过价、也没成交；打开过的群发主题落在：PoE；**还没碰过的一类：工业** → 下封信可加一句 STI-288GP（8 口千兆 PoE+ 2 SFP 工业非管理，$59.8 EXW）。
- **规模与贴牌线索（官网快照 2026-10-21）**：站点地图 79 条 URL；社媒：https://www.facebook.com/larch.networks/、https://www.linkedin.com/company/larch-networks。
- **写信的人（来信签名机械抽取）**：Alexander Cheskis — CEO, Larch Networks（alexander@larch-networks.com，6 封，2025-11-28 → 2026-05-26）；Oksana Loy（oksana@larch-networks.com，3 封，2026-06-02 → 2026-07-02）；Andrey Zarudniy（azarudniy@larch-networks.com，2 封，2026-03-31 → 2026-03-31）。
- **他们嘴里的词（11 封来信、去引用后 5,288 字符的词频）**：话题（次数，最近一次）：管理型 / L2+ / L3 ×5（2026-05-26）、价格 / 折扣 ×5（2026-05-26）、固件 / 软件 ×5（2026-06-03）、PoE ×4（2026-05-26）、10G ×4（2026-05-26）、质保 / 售后 ×4（2026-07-02）；芯片 / 供应商词：Marvell ×5、CENTEC ×1；**提过的数量**：8,000（2026-03-30，「…cific request: a customer of ours needs 8,000 units of a Campus L2 swit…」，`c3ec0dc5b8622bbb`）；10（2026-07-02，「…ciate your assistance. We urgently need 10 pieces of DX1518/DX1548 ch…」，`f77f97cdc39f10a5`）。
- **最后一球**：1:1 对话 4 段，最长一段 10 封 / 跨 13 天（2026-05-22 → 2026-06-05，「Supported SONiC for Saga Ethernet Switches | COMPU」）；最后一句是我们说的（2026-07-02，116 天前，「Re: Request for DX1518/DX1548 Chips」，`9386d851165248d5`）→ 球在对方手里；按他们过去中位 11.1 小时回信（9 次），这次 116 天没回 ≈ 常态的 251 倍 → **值得追一句**（不是催，是换个问法）。
- **日历窗口**：对方：2026-12-04 光明节（12-04 → 12-12，非全休） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-27 查）：**

- `larch-networks.com` → Google Workspace（MX：aspmx.l.google.com、alt1.asmpx.l.google.com、alt2.asmpx.l.google.com、alt3.asmpx.l.google.com）。Gmail → Gmail 同生态投递最稳；但 Gmail 图片代理会预抓像素 → 「已打开」偏高，别把 open 当成读过；三个发信箱别同一天给这个域发

**假日避让（以色列 · 按下一步「群发 / 待排期 → 未来 30 天」窗口 2026-10-27→2026-11-26）：**

- 窗口内无该国法定假日

**公司底数 · 第 90 批（IL · 1 次检索：官网 team / at-a-glance（2009 成立，联合创始人 CEO Alexander Cheskis；Marvell ROS 战略伙伴、Marvell 硬件 bring-up、基辅开发办公室、100+ 客户、硬件 / 机械部门）+ Tracxn（联合创始人 Eddie Preskovsky）+ Wikipedia（前身 Niram Systems，2008）+ LinkedIn（11–50）+ BusinessWire 2021-03（IP Infusion 合作）/ 2024-10（Xsight Labs 选为 hardened SONiC 卓越中心）+ 2025-08 加入 SONiC Foundation + RocketReach（Cheskis 履历 Radware / PacketLight / Crescendo），2026-10-27 查；https://larch-networks.com/about-larch-networks/at-a-glance/）：**

- 法定名 / 登记号：Larch Networks Ltd.（原 Niram Systems；Rosh HaAyin, Israel） · ח.פ. 未取（镜像未命中；下轮 israeli-companies 按名查） · 状态 **Active（2025-08 新闻）** · 成立 2008/2009（前身 Niram Systems） · Ltd.（私营，未融资；两位创始人持股）
- 行业码 / 经营范围：**网络产品开发外包 + 白盒交换机 NOS**：Marvell ROS / Open ROS、SONiC（hardened / rugged）、IP Infusion OcNOS 集成、Marvell 芯片硬件 bring-up、加固交换机 / 工业网络、家庭自动化；客户 = 运营商 / 工业 / 安防 / 军方 / 数据中心
- 注册地址：Rosh HaAyin, Central District, Israel（开发办公室 Kyiv）
- 规模档：11–50 人（LinkedIn）
- 账目：—（私营）；—
- 高管：Alexander CHESKIS — 联合创始人 / CEO（市场 + 销售）= 老板 = 联系人（研究档 KP alexander@）
- 高管：Eddie PRESKOVSKY — 联合创始人（Tracxn 记为 co-CEO）
- 高管：Andrey ZARUDNIY — 研究档 KP
- 控制人 / 股东：Cheskis + Preskovsky
- 曾用名：Niram Systems
- **这意味着什么：**
  - **硬发现：Larch 不是渠道，是以色列的 Marvell 交换机软件 / 硬件开发商（Marvell ROS 官方伙伴 + SONiC 卓越中心，有自己的硬件部门）—— 他们给客户做定制交换机时需要「现成的 Marvell 硬件平台」，这正是我们 Marvell L2+/L3（STI-480XGGM、STC-448XGGPM）和 CENTEC STH 的另一种卖法：当硬件平台卖给 NOS 公司** → 写 Cheskis 本人（老板 = 联系人）：OEM 30%（Marvell 线）/ CENTEC ≥35%（STH-2C24XF-HSI $1,500 / 8C48DX $4,800 级），提供 U-Boot / SDK 接入和硬件文档，**仅商用 / 数据中心 / 工业用途，不做军规版本**；IL 周日–周四，周二 10–12
  - 不说：不提其军方客户；不说「竞品」；不提 Open ROS 授权问题
  - 复查：官网 news 季看一次（新芯片伙伴 = 新硬件需求）
- 备注：研究档 facts 回填 founded / staff / hq；KP 角色 Cheskis CEO。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | larch-networks.com（取自域名，公司全名待核） | 推断 |
| 国家 | 以色列 | 事实（用户表）|
| 网站/域名 | larch-networks.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 网络软硬件方案商 + 自有品牌工业交换机（中国 ODM 采购） | 推断（据兴趣/备注关键词） |
| 联系人 | Alexander Cheskis / Andrey Zarudniy | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | dcn 工业FS 中科德能的 | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | A已回复 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | 中科德能, FS | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线（larch-networks.com，快照 2026-10-21）
- **是谁**：以色列 Larch Networks（定制网络软硬件开发：系统工程 / SONiC（Hardware-Accelerated BFD+）；自有品牌工业交换机 LN-1508G(P)-4XGF-I(-M)（8 GE/PoE + 4×10G SFP+ 工业）、LN-2308GP-2GE-I，16×PoE / 48×PoE 工业页；表内「DCN / 中科德能的工业 FS」= 现由中国 ODM 供货；KP Alexander Cheskis、Andrey Zarudniy；参展 Electronica India 2026）；表内无跟进记录。
- **类型**：网络软硬件方案商 + 自有品牌工业交换机（中国 ODM 采购）
- **在卖/在用品牌**：DCN, 中科德能
- **【官网快照】官网标题：Larch Networks — Tailor-made Network Software and Hardware Development；品类词 安防监控（CCTV / 门禁） / 工业自动化 / OT 网络 / 数据中心 / 企业 IT / 光纤 / 媒体转换 / 网络交换 / PoE**
  > Larch Networks is a company specializing in systems engineering, deployment, and implementation. The team is made up of experienced professionals with a strong background in managing complex projects, designing systems, and integrating fabr
  > 来源：https://larch-networks.com/（抓取 2026-10-21）
- **【用户表】表内兴趣/备注**
  > dcn 工业FS 中科德能的
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【官网快照】系统工程 / 部署 / 实施，定制网络软硬件**
  > Larch Networks is a company specializing in systems engineering, deployment, and implementation.
  > 来源：https://larch-networks.com/（抓取 2026-10-21）
- **【用户表】DCN / 中科德能工业 FS**
  > dcn 工业FS 中科德能的
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Alexander Cheskis（）alexander@larch-networks.com 〔用户表〕
- **KP**：Andrey Zarudniy（）azarudniy@larch-networks.com 〔用户表〕
- **KP**：Oksana Loy（来信署名人（职务未在邮件署名里出现））oksana@larch-networks.com 〔S/A 邮箱来信 2026-06-02 → 07-02 来信 3 封（第 72 批从邮件表头补）〕
- **KP**：Eddie Preskovsky（联合创始人（Tracxn 记为 co-CEO）—— 抄送（第 90 批 官方登记核实 2026-10-27）） 〔https://www.larch-networks.com/〕
- 备注：（无首轮调研；由 deepen.py 建档） ｜ 规则加厚 2026-10-21（autodeep.py；T 档 T5）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（人工复核：官网快照逐家核对 + 表内；T4/T5 信号优先））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Larch Networks Ltd.（原 Niram Systems；ח.פ. 未取 —— 下轮 israeli-companies 按名查） |
| 成立 | 2008/2009（前身 Niram Systems）（第 90 批 官方登记核实 2026-10-27） |
| 总部/地址 | Rosh HaAyin, Central District, Israel（第 90 批 官方登记核实 2026-10-27） |
| 人数 | 11–50（LinkedIn）；开发办公室 Kyiv（第 90 批 官方登记核实 2026-10-27） |
| 其他 | 官网 larch-networks.com，语言 en-US，快照状态 ok；角色判定来源：官网文案 |

- **业务线**：定制网络软件 / 硬件开发（SONiC）；自有品牌工业交换机（LN 系列）

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| Larch（自有） | LN-1508GP-4XGF-I-M | 工业 8 PoE + 4×10G SFP+ 管理 | STI-488XGGPM | https://larch-networks.com/larch-networks-devices/industrial-switches/8xpoe-industrial-switch/（2026-10-21） |
| Larch（自有） | LN-2308GP-2GE-I | 工业 8 PoE + 2 GE | STI-288GP / STI-288GPM | https://larch-networks.com/（2026-10-21） |

- **触达通道（公开）**：role: 网络软硬件方案商 + 自有品牌工业交换机（中国 ODM 采购）；region: 以色列；contact: alexander@larch-networks.com、azarudniy@larch-networks.com
- **近况信号**：
  - 产品页 /larch-networks-devices/industrial-switches/8xpoe-industrial-switch/、/16xpoe-industrial-switch/、/48xpoe-industrial-switch/
  - 站内型号 LN-1508G-4XGF-I-M / LN-1508GP-4XGF-I-M / LN-2308GP-2GE-I
  - 官网：Electronica India 2026 参展；Hardware-Accelerated BFD+ for SONiC
  - KP：Alexander Cheskis、Andrey Zarudniy（表内邮箱）
- **风险/边界**：以色列（T5 非主攻区）；物流/保险条件需核；自有软件栈（SONiC/BFD+）：可能要求开放平台/SDK，Saga 需与 SmartByte 确认固件开放度；现供应商为 DCN/中科德能：价格基准已低
- **Saga 对位结论**：P1 STI-488XGGPM（30% 档）——自有 LN-1508GP-4XGF-I-M（工业 8 PoE + 4×10G SFP+ 管理）→ Saga STI-488XGGPM（工业 8 PoE + 4×10G L2+，$178.7 @30%）；8 PoE + 2 GE 位 STI-288DGGPM；现供应商 DCN/中科德能 = 已接受中国 ODM，可谈二供
- **邮件切入句（英文）**：Alexander, for the LN-1508GP-4XGF class industrial switches (8 PoE + 4×10G SFP+), we can be a second ODM source on a Marvell platform — your firmware/SONiC requirements discussed case by case — from small lots with CE/RoHS/FCC; which model in the LN range needs a second source first?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://larch-networks.com/　语言：en-US　站点地图 URL 数：79
- **标题**：Larch Networks — Tailor-made Network Software and Hardware Development
- **描述**：Larch Networks is a company specializing in systems engineering, deployment, and implementation. The team is made up of experienced professionals with a strong background in managing complex projects, designing systems, and integrating fabrication processes.
- **首页栏目**：Hardware-Accelerated BFD+ for SONiC / Electronica India 2026
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：switch 169、industrial 65、poe 48、sfp 40、10g 30、ethernet 14、data center 14、surveillance 5、wireless 2、2.5g 1、cable 1
- **站内型号串**（正则抽取，含非交换机）：LN-1508G-4XGF-I-M, LN-1508GP-4XGF-I-M, LN-1508G-4XGF-I, LN-1508GP-4XGF-I, LN-2308GP-2GE-I, LN-2348GP-4XGF-IR, LN-2304M-P-2GF-I, LN-2308M-P-2GF-I, LN-2304GP-2GF-I, LN-2308GP-2GF-I, LN-2308GP-4GF-I, LN-2308G-4GF-I
- **站内公开邮箱**：55-966-1282info@larch-networks.com, info@larch-networks.com
- **站内公开电话**：+972 (3) 901-6117, +972 (3) 901-6118, +972 55-966-1282
- **社媒**：https://www.facebook.com/larch.networks/, https://www.linkedin.com/company/larch-networks
- **产品类页面**：https://larch-networks.com/larch-networks-devices/industrial-switches/8xpoe-industrial-switch/；https://larch-networks.com/larch-networks-devices/industrial-switches/16xpoe-industrial-switch/；https://larch-networks.com/larch-networks-devices/industrial-switches/48xpoe-industrial-switch/；https://larch-networks.com/larch-networks-devices/industrial-switches/8xpoe-industrial-switch-2/；https://larch-networks.com/industrial-switches/；https://larch-networks.com/sonic-switch/
- **已抓子页**：[Industrial Switches Archives – Larch Networks — Network Prod](https://larch-networks.com/category/larch-networks-devices/industrial-switches/)；[Industrial Switches by Larch Networks](https://larch-networks.com/industrial-switches/)；[Contacts – Larch Networks — Network Product Development](https://larch-networks.com/about-larch-networks/contacts/)；[Network Switch Modules – Larch Networks — Network Product De](https://larch-networks.com/network-switch-modules/)；[Campus and Access Switches Archives – Larch Networks — Netwo](https://larch-networks.com/category/larch-networks-devices/campus-and-access-switches/)；[Larch Networks Team – Larch Networks — Network Product Devel](https://larch-networks.com/about-larch-networks/team/)
- 首页正文摘录：Home About Us 10 switches running Larch Hardened SONiC and Dorado Cruz orchestrating and monitoring solution allow creation of accessible AI systems. Larch networks At a Glance News and Events Larch Networks Team Career at Larch Networks Contacts Business Latest Case : Hardware-Accelerated BFD+ for SONiC Clients Case Studies Partners SONIC/SAI Development Hardened SONiC NOS SONiC Based Product Development SONiC Adopt
- **自动对位建议**：STI-288GP（官网快照对位：工业/自动化词频 65、PoE 48 → DIN 8 PoE+ 2 SFP 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SB-359.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| 中科德能 | 深圳/国内白牌或品牌供应商 | 对方已在买中国货：以 Marvell 芯片 + L2+ 功能 + 交期为差异点做第二货源 |
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：a.sagatelecom　|　**邮件**：38 封（去 24 / 来 14）　|　**期间**：2025-05-21 → 2026-07-02　|　**最后去信**：2026-07-02
- **对方邮箱**：a.gribenko@larch-networks.com、alexander@larch-networks.com、azarudniy@larch-networks.com、imurzina@larch-networks.com、info@larch-networks.com、oksana@larch-networks.com
- **最后一封来信**：2026-07-02 oksana@larch-networks.com「Request for DX1518/DX1548 Chips」：Dear Alan, I hope you are doing well. We would greatly appreciate your assistance. We urgently need 10 pieces of DX1518/DX1548 chips (any variant is acceptable) for our customer. Could you please let us know if you have any of these chips in stock? If so, woul

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Request for DX1518/DX1548 Chips | 2026-07-02 | 2026-07-02 | 1 | 1 | 2 |
| Supported SONiC for Saga Ethernet Switches \| COMPUTEX | 2026-05-22 | 2026-06-05 | 5 | 5 | 4 |
| Updated Ethernet Switches Links | 2026-03-30 | 2026-03-31 | 3 | 4 | 7 |
| Booster PoE Switch | 2025-11-27 | 2026-02-02 | 4 | 7 | 14 |
| Managed Optical Bypass Switch | 2025-05-21 | 2025-10-27 | 1 | 7 | 25 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：5 个　|　**数据截至**：2026-10-27T08:02:45Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-359/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://larch-networks.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 4658 字符；首行：Larch Networks — Tailor-made Network Software and Hardware Development |
| [sitemap](https://larch-networks.com/sitemap_index.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |
| [news_1](https://larch-networks.com/category/blog/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 2723 字符；首行：News and Events Archives – Larch Networks — Network Product Development |
| [news_2](https://larch-networks.com/blog/electronica-india-2026/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 2650 字符；首行：Electronica India 2026 – Larch Networks — Network Product Development |
| [feed_auto](https://larch-networks.com/feed/) | rss | HTTP 200 | 2026-10-23T04:20:51Z | 10 条；最新：Tue, 20 Oct 2026 08:32:36 Larch Networks and Amphenol Demonstrate TSN for Aerospac |

- **人工定期看（登录墙，不自动抓）**：LinkedIn: https://www.linkedin.com/company/larch-networks；Facebook: https://www.facebook.com/larch.networks/

## 联系方式（已有 · 原值照录）

- 邮箱：`alexander@larch-networks.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`azarudniy@larch-networks.com`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Alexander Cheskis / Andrey Zarudniy
- 网站/域名：larch-networks.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Alexander Cheskis | — | alexander@larch-networks.com | 调研核实（公开页） | 用户表 |
| Andrey Zarudniy | — | azarudniy@larch-networks.com | 调研核实（公开页） | 用户表 |
| Oksana Loy | 来信署名人（职务未在邮件署名里出现） | oksana@larch-networks.com | 调研核实（公开页） | S/A 邮箱来信 2026-06-02 → 07-02 来信 3 封（第 72 批从邮件表头补） |
| Eddie Preskovsky | 联合创始人（Tracxn 记为 co-CEO）—— 抄送（第 90 批 官方登记核实 2026-10-27） | — | 调研核实（公开页） | https://www.larch-networks.com/ |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A Replied 09.04.xlsx#总表:32 | 31 | https://larch-networks.com/2023/11/07/l3-48-ports-managed-switches/ | 以色列 | Alexander Cheskis<br>Andrey Zarudniy | 谷歌 | dcn 工业FS 中科德能的 | alexander@larch-networks.com<br>azarudniy@larch-networks.com |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-488XGGPM | 深挖对位：自有 LN-1508GP-4XGF-I-M（工业 8 PoE + 4×10G SFP+ 管理）→ Saga STI-488XGGPM（工业 8 PoE + 4×10G L2+，$178.7 @30%）；8 PoE + 2 GE 位 STI-288DGGPM；现供应商 DCN/中科德能 = 已接受中国 ODM，可谈二供 | $178.8 USD EXW（30% 档，SmartByte LT-IS6312XGP-4XS8GT 920 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（网络软硬件方案商 + 自有品牌工业交换机（中国 ODM 采购）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-488XGGPM），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STI-488XGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：自有品牌/贴牌需求 = 现成 OEM 客户
- **W**：中东：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STI-488XGGPM 按 30% 档报价，做现供应商的第二货源；贴牌 + 定制 UI/型号 → 30% 档与长期绑定；对位其在用/在卖的 中科德能：涨价、断货或交期拉长时切入
- **T**：深圳同行（ONV / Utepo / 迈威等）价格战；现有品牌分销协议可能限制同品类采购；汇率与海运波动吃掉 20–30% 的价差

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
| 现用/在卖交换品牌 | ✅ 中科德能, FS |
| 采购量/预算 | ❓ 未确认 |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STI-488XGGPM - industrial DIN-rail L2+ managed switch (Marvell-based, neutral label)

```text
Hi Alexander,

We have been in touch before about PoE and industrial switches; instead of a catalogue, here is one concrete option. For the LN-1508GP-4XGF class industrial switches (8 PoE + 4×10G SFP+), we can be a second ODM source on a Marvell platform — your firmware/SONiC requirements discussed case by case — from small lots with CE/RoHS/FCC; which model in the LN range needs a second source first?

We supply a Marvell-based industrial DIN-rail L2+ managed switch, 8x Gigabit PoE+ plus 4x10G SFP+ - model STI-488XGGPM - that fits the same slot as the units you source today at a lower landed cost, and we can ship it under your own label with neutral packaging. Current price: $178.8 USD EXW (price snapshot 2026-10-17, valid 15 days).

If useful, one unit at the unit price for a 30-day side-by-side test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 发送前检查：① 不出现「Made in China」或原产地；② 不承诺未实测指标（PoE 功率/温宽）；③ 落款换成发件人姓名；④ 一次只问一个问题；⑤ 价格为 USD EXW 快照，过窗先核价；⑥ 只用表内/公开原值邮箱，不猜地址；⑦ 发出后在「新跟进记录」补一行并告知日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-26**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-27：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 44）

---

*建档日期：2026-10-27　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
