# TJ Computer
**官方名称（调研核实）**：TJ Computer（泰国；Peter Ponganan Ruenboon）

> **评级 B**　|　泰国　|　档案编号 `SB-034`　|　优先级 ★★　|　状态：有回复·跟进中
>
> **类型**：小型经销商（推断）　|　**历史关系**：实质回复 1 次；推送 1 次（2025-03-18 → 2025-03-18）　|　**所在清单**：A已回复　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-034
rating: B
rating_auto: A
rating_research: B  # 微型经销商、5 口非管理交换机客单价极低、WA 不通 → 慢跟。
name_official: "TJ Computer（泰国；Peter Ponganan Ruenboon）"
score: 68
country: 泰国
region: 亚太
website: tj2003.net
type: 小型经销商
tier_tags: ["A已回复"]
deal: no
replies: 1
followups: 1
first_contact: 2025-03-18
last_contact: 2025-03-18
s_mail: 20 msgs (out 18 / in 2), 2025-02-12 -> 2026-09-07
p1: STC-28DGGPM
price_tier: 25%
research: done
site_snapshot: unreachable  # 2026-10-21
sources: 1
updated: 2026-10-27
```

## SALES BRIEF（压缩模型）

- **是谁**：泰国电脑 / CCTV 店（tj2003.net 失效；tjcomputercctv@ 邮箱），Peter（Ponganan Ruenboon），需求 5 电口并要具体产品信息，2025-03 对 2 光 8 PoE 回复 Interested。（调研 2026-10-21；表内兴趣：5电口 需要具体的产品信息）
- **为什么是 B 级**：**调研后定级 B**（微型经销商、5 口非管理交换机客单价极低、WA 不通 → 慢跟。）；自动分级 A：+22 实质回复 1 次；+18 在「已回复」名单（A/E Replied）；-3 WhatsApp 加不上；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+3 区域 亚太/泰国；+5 最近活动 2025
- **历史互动**：实质回复 1 次；推送 1 次（2025-03-18 → 2025-03-18）；最近一次客户回复：2025-03-18：Interested
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-244GP / 5 口非管理（一次给齐） — 不主动。已打开的主题（7/18 封有打开记录）：「Managed Optical Bypass Switch」(2025-05-14)、「Re: Managed Optical Bypass Switch」(2025-05-15)、「Commercial PoE Switch」(2025-06-20)、「16 Port Ethernet Switch」(2025-07-14) → 读者兴趣偏「工业」；与 P1 同类，继续；—；群发里他已看到的价（续）：2026-08-11 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，2026-07-22→09-08 那轮；现价轮是 $180）——同款信稿写 $180 要点明 9 月前那封是 $170；群发里他已看到的价（续，第 66 批全量复核）：2025-04-23 $300（48 Port PoE Managed Switch）、2025-08-13 $240（24 Port Fiber Switch）、2025-10-15 $280（10G Enterprise SFP Switch）
- **第一问（只问一个）**：Are PoE / industrial switches something you still source today, or has that line been dropped?
- **最大未知**：官网当前状态异常（域名不可达（DNS/连接失败））——公司是否仍在运营待核
- **下一步**：不动 A 邮箱 来信时一次给 STI-244GP 资料

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-034` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未绑定（两次「interested / 多少钱」→ bypass 款 300 USD → 停；Elsa 箱：`to:tj2003.net` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 18 / 来 2）（第 74 批(n)））** ｜ 类型：泰国小经销（Peter）——第四档；TH 非主攻 ｜ 筛子：2 ｜ 停点：2025-05-15 STI-488XGGPM2B-2BT 300 USD 后无回 ｜ 复活：不主动 ｜ 通路：TH ｜ 节奏：2025-02 → 2026-09 去信 18 封；最后来信 2025-05-14 ｜ 证据：k=2c5f175a9c8a8571 / 02da3feea2aac332 / 60215e5a3bb8a816；A 邮箱外发报价单正文（`data/gmail_a/attachments/text/`，2026-10-24 对表）
- **现状一句话**：Peter 对 8 口工业 PoE 回「interested」、对 bypass 回「多少钱」，Alan 报 300 USD（4×10G + 8 PoE，2 通道 bypass，L2+）后无回。
- **对方真实需求（有据）**：8 口工业 PoE；bypass。
- **断点 / 为什么停在这里**：泰国小经销的价格段与 Marvell 不匹配。
- **Saga 现在该推什么**：P1 **STI-244GP / 5 口非管理（一次给齐）**（25% 档，—；群发里他已看到的价（续）：2026-08-11 $170（24 Port PoE Managed Switch = STC-424XGGPM-280W，2026-07-22→09-08 那轮；现价轮是 $180）——同款信稿写 $180 要点明 9 月前那封是 $170；群发里他已看到的价（续，第 66 批全量复核）：2025-04-23 $300（48 Port PoE Managed Switch）、2025-08-13 $240（24 Port Fiber Switch）、2025-10-15 $280（10G Enterprise SFP Switch））——不主动。已打开的主题（7/18 封有打开记录）：「Managed Optical Bypass Switch」(2025-05-14)、「Re: Managed Optical Bypass Switch」(2025-05-15)、「Commercial PoE Switch」(2025-06-20)、「16 Port Ethernet Switch」(2025-07-14) → 读者兴趣偏「工业」；与 P1 同类，继续
- **下一步（具体）**：不动　A 邮箱　来信时一次给 STI-244GP 资料

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-03-18 | 去 | Alan（Quotation.pdf，Buyer TJ Computer / Peter Ponganan Ruenboon，EXW，Destination Thailand） | STI-288GP 2×SFP + 8×GE PoE af/at 240W 非管理 ×1 $60.00 | 泰国 1 台样机报价（未付）；与 52 Networks 同款 $58 同期 | `gmail_a att 2025-03-18` |
| 2025-03-18 | 来 | พงษ์อนันต์（泰国） | interested（回 Alan 2025-03-18「8 Port Industrial PoE Switch」） | 一词回复「interested」——泰国小集成商的典型反应；A 邮箱之后有无跟进见 digest；可作 WhatsApp 线索 | `gmail_a 2025-03-18 Re: 8 Port Industrial PoE Switch` |
| 2025-05-14 | 来 | Peter（TJ Computer） | ราคาเท่าไหร่?（多少钱？） | bypass 询价 | `02da3feea2aac332` |
| 2025-05-15 | 去 | Alan | 300usd/pc STI-488XGGPM2B-2BT… 2 channels single fiber Bypass ports… L2+ managed, Marvell chip | 报价后停 | `60215e5a3bb8a816` |

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **时机与节律**：真人来信 1 封（2025-03-18 → 2025-03-18）；**他们回信中位 5.2 小时**（1 次，100% 在 24 小时内）；我方回信中位 4.6 小时（1 次）。
- **发信窗口（TH 全库 447 封群发的打开标签，对方本地时间；均值 4.5%）**：周二 10–12 点 6.1%（49 封）、周一 10–12 点 3.4%（59 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 15 封（2025-02-12 → 2026-09-07），打开标签 4 次（近 12 个月 0，最后 2025-07-14）；打开过：「8 Port Industrial PoE Switch」×1（2025-03-18）、「Managed Optical Bypass Switch」×1（2025-05-14）、「Commercial PoE Switch」×1（2025-06-20）、「16 Port Ethernet Switch」×1（2025-07-14）；从未打开：「Industrial PoE Switch」、「48 Port PoE Managed Switch」、「24 Port Fiber Switch」；**最近连续 9 封没打开**（近 180 天发 3 封 0 打开）→ 群发对这户已失效，停两个月，改一句 1:1 或换收件人。
- **写信的人（来信签名机械抽取）**：พงษ์อนันต์ รื่นบุญ（tjcomputercctv@tj2003.net，1 封，2025-03-18 → 2025-03-18）。
- **渠道反应**：S 箱（Simon） 去 1（1:1 0 / 群发 1）回 0，从未回；A 箱（Alan） 去 17（1:1 3 / 群发 14）回 1，最近回 2025-03-18 → 只对 A 箱 Alan 有反应，下一封别换箱。
- **最后一球**：1:1 对话 1 段，最长一段 3 封 / 跨 5 天（2025-03-18 → 2025-03-24，「Re: 8 Port Industrial PoE Switch」）；最后一句是我们说的（2025-05-15，530 天前，「Re: Managed Optical Bypass Switch」，`60215e5a3bb8a816`）→ 球在对方手里。
- **同国同档参照（TH，25% 档、主推线「工业 PoE 非管理」，共 1 户有动静，列前 3）**：SA-080 PBA Forever Technology Co., Lt（A，同档：成交 STC-05XGWE、STC-08XGWE、STC-108XGDGP）。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-12-05 国王诞辰；2026-12-31 新年（12-31 → 01-02） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | TJ Computer | 事实（用户表） |
| 国家 | 泰国 | 事实（用户表）|
| 网站/域名 | tj2003.net | 事实（用户表 URL/邮箱域名） |
| 类型 | 小型经销商 | 推断（据兴趣/备注关键词） |
| 联系人 | Peter(Ponganan Ruenboon) | 事实（用户表） |
| 来源（From） | 2023.7.6 | 事实（用户表） |
| 兴趣（Interested in） | 5电口 需要具体的产品信息 | 事实（用户表） |
| 用户备注（Remark） | 0622179229 加不上 | 事实（用户表） |
| 所在清单 | A已回复 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：域名不可达（tj2003.net）
- **是谁**：泰国电脑 / CCTV 店（tj2003.net 失效；tjcomputercctv@ 邮箱），Peter（Ponganan Ruenboon），需求 5 电口并要具体产品信息，2025-03 对 2 光 8 PoE 回复 Interested。
- **类型**：小型经销商
- **规模**：微型（待补证）
- **【用户记录】5 电口需求，需要具体产品信息；WA 加不上**
  > 5电口 需要具体的产品信息；0622179229 加不上（用户 Clients 表摘录）
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【官网快照】tj2003.net 不可达**
  > status unreachable
  > 来源：http://tj2003.net/（抓取 2026-10-21）
- **【用户表】5 电口 需要具体的产品信息；2025-03 28PoE→Interested**
  > 兴趣：5电口 需要具体的产品信息；回复：Interested
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Peter (Ponganan Ruenboon)（）tjcomputercctv@tj2003.net（2025-03 / 05 来信地址；署名 พงศ์นันท์ รื่นบุญ (ปีเตอร์)）；tjcomputer2003@gmail.com 08-0069-1918 / 06-2217-9229（2025-05-14 签名）〔A 邮箱来信表头 + 签名〕
- **调研后定级**：B（原自动 A）——微型经销商、5 口非管理交换机客单价极低、WA 不通 → 慢跟。
- 备注：邮件一次性给 STI-244GP/5 口型号资料即可。

### 加厚挖掘（2026-10-21 · B 级加厚 v1（快照不可达 + 表内））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | TJ Computer（2003） |
| 成立 | 2003（域名推断） |
| 总部/地址 | 泰国 |
| 其他 | CCTV 业务 |

- **业务线**：电脑 / CCTV 零售安装
- **触达通道（公开）**：role: 零售 / 安装商；region: 泰国
- **近况信号**：
  - 对 2 光 8 PoE Interested；5 口需求
- **风险/边界**：小店小量；域名失效
- **Saga 对位结论**：P1 STC-28DGGPM（25% 档）——2 光 8 PoE Interested → STC-28DGGPM；5 口 → STI-050GE / 商用 5 口按 HRUI 另询。
- **邮件切入句（英文）**：Peter, you were interested in the 8-PoE + 2-SFP unit — $84 EXW at 1 pc; for the 5-port need, do you want PoE or plain gigabit? I'll send both sheets.

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：域名不可达（DNS/连接失败））

- 尝试域名：tj2003.net
  > https://tj2003.net/ conn: HTTPSConnectionPool(host='tj2003.net', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("HTTPS
  > https://www.tj2003.net/ conn: HTTPSConnectionPool(host='www.tj2003.net', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("H
  > http://tj2003.net/ conn: HTTPConnectionPool(host='tj2003.net', port=80): Max retries exceeded with url: / (Caused by NameResolutionError("HTTPCon
- **提示**：域名不可达 → 表内域名可能拼错/过期；跟进前核对邮箱域名。
- 数据文件：`data/saga_clients/site_snapshots/SB-034.json`

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 1 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-03-18 | 2025.3.18 | 28PoE | Interested | A |  | A Replied 09.04.xlsx#42 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：20 封（去 18 / 来 2）　|　**期间**：2025-02-12 → 2026-09-07　|　**最后去信**：2026-09-07
- **对方邮箱**：tjcomputer2003@gmail.com、tjcomputercctv@tj2003.net
- **最后一封来信**：2025-05-14 tjcomputercctv@tj2003.net「Re: Managed Optical Bypass Switch」：ราคาเท่าไหร่? ขอบคุณครับ ขอแสดงความนับถือ พงศ์นันท์ รื่นบุญ (ปีเตอร์) มือถือ : 08-0069-1918, 06-2217-9229 E-mail : tjcomputercctv@tj2003.net <tjcomputercctv@tj2003.net> ในวันที่ พ. 14 พ.ค. 2025 เวลา 15:30 Alan from Saga Telecom < a.sagatelecom@gmail.com> เขียน

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 16 Port Industrial PoE Switch | 2026-09-07 | 2026-09-07 | 0 | 1 | 1 |
| 24 Port PoE Managed Switch | 2026-08-11 | 2026-08-11 | 0 | 1 | 1 |
| Saga Q3 Product Links | 2026-07-15 | 2026-07-15 | 0 | 1 | 2 |
| Updated Ethernet Switches Links | 2026-03-30 | 2026-03-30 | 0 | 1 | 1 |
| Marvell Industrial Alert System | 2025-12-24 | 2025-12-24 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-19 | 2025-11-19 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-15 | 2025-10-15 | 0 | 1 | 1 |
| Mini Industrial PoE Switch | 2025-09-15 | 2025-09-15 | 0 | 1 | 1 |
| 24 Port Fiber Switch | 2025-08-13 | 2025-08-13 | 0 | 1 | 1 |
| 16 Port Ethernet Switch | 2025-07-14 | 2025-07-14 | 0 | 1 | 1 |
| Commercial PoE Switch | 2025-06-20 | 2025-06-20 | 0 | 1 | 1 |
| Managed Optical Bypass Switch | 2025-05-14 | 2025-05-15 | 1 | 2 | 4 |
| …共 15 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-26T07:56:19Z
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-034/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://tj2003.net/) | html | ConnectionError: HTTPSConnectionPool(host='tj2003.net', port | - | 官网首页（T27 快照状态 unreachable） |

## 联系方式（已有 · 原值照录）

- 邮箱：`tjcomputer2003@gmail.com`〔免费邮箱；来源：用户表原值〕
- 邮箱：`tjcomputercctv@tj2003.net`〔企业邮箱；来源：用户表原值〕
- 电话：`+0622179229`〔WhatsApp 加不上；原值见来源表〕
- 联系人（原值）：Peter(Ponganan Ruenboon)
- 网站/域名：tj2003.net
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Peter (Ponganan Ruenboon) | — | tjcomputercctv@tj2003.net（2025-03 / 05 来信地址；署名 พงศ์นันท์ รื่นบุญ (ปีเตอร์)）；tjcomputer2003@gmail.com / 08-0069-1918 / 06-2217-9229（2025-05-14 签名） | 调研核实（公开页） | A 邮箱来信表头 + 签名 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A Replied 09.04.xlsx#总表:43 | 42 | TJ Computer | 泰国 | Peter(Ponganan Ruenboon) | 2023.7.6 | 5电口 需要具体的产品信息 | tjcomputer2003@gmail.com<br>tjcomputercctv@tj2003.net | 0622179229 加不上 | 1 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：2 光 8 PoE Interested → STC-28DGGPM；5 口 → STI-050GE / 商用 5 口按 HRUI 另询。 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（小型经销商） |
| 备选2 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：25% 档 $145.7 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），25% 档公式为 $188.7——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STC-28DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 1 次实质回复（对方认识我们）
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STC-28DGGPM 按 25% 档报价，做现供应商的第二货源；规模（调研）：微型（待补证）
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
| 采购量/预算 | ❓ 未确认（有回复但未报量） |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 官网当前状态异常（域名不可达（DNS/连接失败））——公司是否仍在运营待核
- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STC-28DGGPM - 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks (Marvell-based, neutral label)

```text
Hi Peter,

Picking up our earlier exchange about PoE / industrial switches. You were interested in the 8-PoE + 2-SFP unit — $84 EXW at 1 pc; for the 5-port need, do you want PoE or plain gigabit? I'll send both sheets.

We supply a Marvell-based 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks - model STC-28DGGPM - that fits the same slot as the units you source today at a lower landed cost, and we can ship it under your own label with neutral packaging. Current price: $84.1 USD EXW (price snapshot 2026-10-17, valid 15 days).

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

- 2026-10-27：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 A，分数 68）；人工/调研定级 → B

---

*建档日期：2026-10-27　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
