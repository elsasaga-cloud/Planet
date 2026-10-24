# alphanetcom.com
**官方名称（调研核实）**：Alpha Net Communications（San Antonio, TX，美国，1986 年起）

> **评级 A**　|　美国　|　档案编号 `SA-091`　|　优先级 ★★★　|　状态：有回复·跟进中
>
> **类型**：布线承包商/小型系统集成商（推断）　|　**历史关系**：实质回复 1 次；推送 1 次（2025-09-27 → 2025-09-27）　|　**所在清单**：A已回复、群发(筛选后质量一般的_群发)、表:US　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SA-091
rating: A
rating_auto: A
name_official: "Alpha Net Communications（San Antonio, TX，美国，1986 年起）"
score: 70
country: 美国
region: 北美
website: alphanetcom.com
type: 布线承包商/小型系统集成商
tier_tags: ["A已回复", "群发(筛选后质量一般的_群发)", "表:US"]
deal: no
replies: 1
followups: 1
first_contact: 2025-09-27
last_contact: 2025-09-27
s_mail: 25 msgs (out 21 / in 4), 2024-08-24 -> 2026-09-07
p1: STC-424DGGPM-280W
price_tier: 25%
research: done
site_snapshot: ok  # 2026-10-21
sources: 2
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：美国得州圣安东尼奥的结构化布线承包商/小型集成商（1986 年起，1–10 人），服务 1–500 人规模的组织，提供布线、光纤安装、电话系统、无线、摄像、门禁；在售 HPE/Extreme 交换机、Panduit/Hubbell/ICC 布线；A 已回复 1 次（群发 US 表）。（调研 2026-10-21；表内兴趣：工业switch 分销商；有比较多的供应商 产品面广 Networking      switch）
- **为什么是 A 级**：+22 实质回复 1 次；+18 在「已回复」名单（A/E Replied）；-6 群发批次名单；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国；+5 最近活动 2025
- **历史互动**：实质回复 1 次；推送 1 次（2025-09-27 → 2025-09-27）；最近一次客户回复：2025-09-27：Price
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-08XGE（8×10G RJ45 非管理，Saga 对外价 $181.5 USD EXW，`data/hrui_STC对照表.csv`；Realtek 线是否对美国客户开 → Simon 定） — U29 教训：先 grep 仓库——8×10G 电口在 HRUI 线就有；$181.5 USD EXW（对外价表，报前按快照日期重核 15 天有效）
- **第一问（只问一个）**：For your San Antonio projects, would an unmanaged 8×10GBASE-T unit (US$181.5 EXW) solve the 10G need, or must it be managed with SFP+ uplinks?
- **最大未知**：年走量与现供应商
- **下一步**：2026-11 A 邮箱 → nate.cline@ 一句话：8×10GBASE-T 非管理 $181.5 EXW 是否解决；要管理则 24GE+8×10G SFP+ 白牌

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SA-091` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未绑定（询问阶段 3 轮：10G MC 价表、8 口 10G 管理型、24 口 SFP 价格）** ｜ 类型：美国得州布线承包商/小集成商（1–10 人）；Nate Cline——第四档小项目集成商 ｜ 筛子：2 ｜ 停点：产品缺口：2025-04 要「8 口 10G 电 + 2/4×10G SFP 管理型」，Alan 答需量产开发；2025-09-27 STC-4168XGGCM 280 USD 报价后无回音 ｜ 复活：仓库里有 8×10G 电口非管理款 STC-08XGE（HRUI/Realtek 线，Saga 对外价 $181.5 USD EXW）；SmartByte 白牌 LT-S8532XS-8XS24GT（24GE + 8×10G SFP+）——若他的项目只要 10G 接入，可一次报清 ｜ 通路：US ｜ 节奏：2024-08 → 2026-09 去信 21 封；最后来信 2025-09-26 ｜ 证据：k=6350a98e7dcd08eb / 380c4a1eabea9946 / 765a46afe5b24ace / 1a6a105db1142c5f / 75205f906d867c11
- **现状一句话**：Nate 三次主动：2024-08 要 10G MC 价表并问大单折扣；2025-04「I'm looking for a 10 Gig Ethernet Switch with about 8 ports and about 2 or 4 Ports of 10 Gig SFP」（Alan：现无，可开发但要量）；2025-09「How much do they cost?」→ 280 USD STC-4168XGGCM → 无回。他要的 8×10GBASE-T 其实在 HRUI 线有非管理款。
- **对方真实需求（有据）**：8×10G 电口（+2/4 SFP+）小型交换机；10G MC；项目型小批量。
- **断点 / 为什么停在这里**：群发推的是 Marvell 24 口光聚合，他要的是 8 口 10G 电——仓库有对位品（Realtek 线）但没人查。
- **Saga 现在该推什么**：P1 **STC-08XGE（8×10G RJ45 非管理，Saga 对外价 $181.5 USD EXW，`data/hrui_STC对照表.csv`；Realtek 线是否对美国客户开 → Simon 定）**（25% 档，$181.5 USD EXW（对外价表，报前按快照日期重核 15 天有效））——U29 教训：先 grep 仓库——8×10G 电口在 HRUI 线就有
  - 做不了 / 要先核的：Nate 要不要「管理」——一句话问；Realtek 线对美国小集成商是否开
- **下一步（具体）**：2026-11　A 邮箱 → nate.cline@　一句话：8×10GBASE-T 非管理 $181.5 EXW 是否解决；要管理则 24GE+8×10G SFP+ 白牌
  - 第一问（只问一个）：For your San Antonio projects, would an unmanaged 8×10GBASE-T unit (US$181.5 EXW) solve the 10G need, or must it be managed with SFP+ uplinks?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-08-24 | 来 | Nate Cline | Can you send me a price list and I want to ask if I can buy from you in Large Order and would you provide a discount on Large Orders? | 第一轮 | `6350a98e7dcd08eb` |
| 2025-04-04 | 来 | Nate | I'm looking for a 10 Gig Ethernet Switch with about 8 ports and about 2 or 4 Ports of 10 Gig SFP. | 精确需求 | `380c4a1eabea9946` |
| 2025-04-08 | 去 | Alan | it is not available on our list now… OK to do 4*10G+8*10G Ethernet But this requires a decent quantity to develop | 缺口答复 | `765a46afe5b24ace` |
| 2025-09-26 | 来 | Nate | How much do they cost? | 第三轮 | `1a6a105db1142c5f` |
| 2025-09-27 | 去 | Alan | 280usd/pc. STC-4168XGGCM 4*1G/2.5G/10G SFP+16*1G SFP+8*1G SFP/RJ45 Combo | 报价后无回 | `75205f906d867c11` |

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | alphanetcom.com（取自域名，公司全名待核） | 推断 |
| 国家 | 美国 | 事实（用户表）|
| 网站/域名 | alphanetcom.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 布线承包商/小型系统集成商 | 推断（据兴趣/备注关键词） |
| 联系人 | Nathan / Nathan "Nate" Cline / President | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | 工业switch<br>分销商 / 有比较多的供应商 产品面广<br>Networking      switch | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | A已回复、群发(筛选后质量一般的_群发)、表:US | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：美国得州圣安东尼奥的结构化布线承包商/小型集成商（1986 年起，1–10 人），服务 1–500 人规模的组织，提供布线、光纤安装、电话系统、无线、摄像、门禁；在售 HPE/Extreme 交换机、Panduit/Hubbell/ICC 布线；A 已回复 1 次（群发 US 表）。
- **类型**：布线承包商/小型系统集成商
- **规模**：微型（1–10 人）
- **在卖/在用品牌**：HPE, Extreme Networks, Avaya, Cisco, Panduit, Hubbell, ICC
- **【官网】1986 年起服务南得州，布线/光纤/电话/无线/摄像/门禁**
  > Alpha Net Communications provides structured cabling, fiber optic installation, business phone systems, wireless networking, cameras, access control… serving South Texas since 1986
  > 来源：https://www.alphanetcom.com/（抓取 2026-10-21）
- **【官网】在售 Extreme / HP ProCurve 千兆交换机**
  > Extreme Networks Gigabit Switch HP ProCurve Gigabit Switch Service Design and Installation
  > 来源：https://www.alphanetcom.com/san-antonio-structured-cabling.html（抓取 2026-10-21）
- **【第三方】1986 年成立，1–10 人**
  > Alpha Net Communications… Founded: 1986-01-01… Employees: 1-10
  > 来源：https://aeroleads.com/list/top-electronics-companies-in-san-antonio（抓取 2026-10-21）
- **【官网】业务范围、KP、地址与电话**
  > Structured cabling, fiber optic installation, business phone systems, wireless networking, cameras, access control, and network services for San Antonio, Austin, and South Texas … Multi-Gigabit to the desk 1/2.5/5/10/100/1000 10 Gigabit cabling … Nathan "Nate" Cline President … contact@alphanetcom.com … Office 11031 Wye Dr Ste 102 San Antonio, TX 78217 … Office: 210-654-0653
  > 来源：https://www.alphanetcom.com/（抓取 2026-10-21）
- **【官网】在售 Extreme Networks / HP ProCurve 千兆交换机**
  > Extreme Networks Gigabit Switch HP ProCurve Gigabit Switch Service Design and Installation
  > 来源：https://www.alphanetcom.com/san-antonio-structured-cabling.html（抓取 2026-10-21）
- **KP**：（见 Clients 表联系人）（） +1 210-654-0653〔用户 Clients 表 + 官网〕
- **KP**：Nathan "Nate" Cline（President）nate.cline@alphanetcom.com +1 210-654-0653〔https://www.alphanetcom.com/（Contact 区块）〕
- 备注：美国主攻区、集成商、已回复。用户记录称其'工业 switch 分销商、供应商多、产品面广'——官网显示更偏布线承包+项目集成。P1：STC-424DGGPM-280W（摄像/门禁项目 24 口 PoE），项目价阶 25%；需 FCC 文件，不承诺 UL。

### 加厚挖掘（2026-10-21 · 深挖 v2（官网核对 + KP））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Alpha Net Communications |
| 成立 | 1986 |
| 总部/地址 | Office 11031 Wye Dr Ste 102, San Antonio, TX 78217；Warehouse 11313 Lone Shadow Trail, TX 78233；P.O. Box 18122（tel 210-654-0653） |
| 人数 | 4（RocketReach）/ 1–10 |
| 营收 | $10M（RocketReach 口径，存疑） |
| 其他 | 服务 San Antonio / Austin / South Texas：Cat5e–6A/10G 布线、光纤熔接、Avaya Connect 授权伙伴、Yealink VoIP、Wi-Fi 6E/7、IP 摄像机、门禁；在售 Extreme Networks / HP ProCurve 千兆交换机；官网 © 2026 |

- **业务线**：结构化布线与光纤安装；电话系统、无线、摄像、门禁；交换机转售（HPE/Extreme/Avaya/Cisco）

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| HPE / Extreme（转售） | 企业接入交换机 | 项目配套 | STC-424DGGPM-280W（低成本项目位） | https://alphanetcom.com/（2026-10（首轮调研）） |

- **触达通道（公开）**：网站: https://www.alphanetcom.com/；直邮: nate.cline@alphanetcom.com（用户表）；电话: +1 210-654-0653（官网公开）；邮箱（公开）: contact@alphanetcom.com（官网）；nate.cline@alphanetcom.com（phoneinstallers.net 公开 + 用户表）；社媒: Facebook / X @Alpha_NetComs / LinkedIn
- **近况信号**：
  - 用户表：A 已回复 1 次（群发 US 表），兴趣工业 switch，「有比较多的供应商 产品面广」
  - 官网主推「Multi-Gigabit to the desk 1/2.5/5/10G」与 Wi-Fi 6E/7 AP——2.5G PoE 接入有现实需求（2026-10-21）
- **风险/边界**：小承包商，项目型单量小；美国商业楼宇要 UL 的场景不供
- **Saga 对位结论**：P1 STC-424DGGPM-280W（25% 档）——布线承包商摄像/门禁/AP 项目：STC-424DGGPM-280W 主推；Wi-Fi 6E/7 与 multi-gig 布线对应 STC-424XGGPM-280W（2.5G 下行需核）；8 口位 STC-28DGGPM；集成商 25% 档
- **邮件切入句（英文）**：For the camera, access-control and Wi-Fi 6E/7 drops you cable in San Antonio and Austin, the Marvell-based 24-port PoE+ managed switch at EXW cost is the one I am quoting, with the 10G-uplink version for the multi-gig jobs.

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://alphanetcom.com/　语言：en　站点地图 URL 数：8
- **标题**：San Antonio Network Cabling & Fiber Installation / Alpha Net
- **描述**：Alpha Net Communications provides structured cabling, fiber optic installation, business phone systems, wireless networking, cameras, access control, and network services in San Antonio, Austin, and South Texas.
- **首页栏目**：San Antonio Network Cabling, Fiber Optic Installation & Business Phone Systems / CABLING / NETWORKING SERVICES / WIRELESS / Providing Tomorrow's Technology Today / Conferences and Conventions / Alpha Net Services Since 1986 / 210-654-0653
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：fiber 14、wireless 14、gigabit 8、ethernet 4、camera 4、switch 3、access control 3、poe 2、wifi 2、data center 1、cable 1、ubiquiti 1
- **站内公开邮箱**：contact@alphanetcom.com
- **社媒**：https://mobile.twitter.com/Alpha_NetComs, https://www.cybermaxx.com/, https://www.facebook.com/AlphaNetComs/, https://www.linkedin.com/company/alpha-net-communications
- 首页正文摘录：HOME ABOUT SERVICES PRODUCTS DETAILS CONTACT San Antonio Network Cabling, Fiber Optic Installation & Business Phone Systems Alpha Net Communications provides structured cabling, fiber, wireless networking, VoIP phone systems, cameras, access control, and network services for businesses in San Antonio, Austin, and South Texas. CABLING Serving San Antonio and Austin for large and small businesses. We specialize in voic
- **自动对位建议**：STC-424DGGPM-280W（官网快照对位：PoE 词频 2、监控 4 → 24 口 PoE L2+ 走量款；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SA-091.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 1 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2025-09-27 | 2025.9.27 | Dual AC | Price | A |  | A Replied 09.04.xlsx#23 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：25 封（去 21 / 来 4）　|　**期间**：2024-08-24 → 2026-09-07　|　**最后去信**：2026-09-07
- **对方邮箱**：nate.cline@alphanetcom.com
- **最后一封来信**：2025-09-26 nate.cline@alphanetcom.com「Re: 10G Enterprise SFP Switch」：Hi Alan, How much do they cost? Regards, Nate

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 16 Port Industrial PoE Switch | 2026-09-07 | 2026-09-07 | 0 | 1 | 1 |
| 24 Port PoE Managed Switch | 2026-08-11 | 2026-08-11 | 0 | 1 | 1 |
| Saga Q3 Product Links | 2026-07-20 | 2026-07-20 | 0 | 1 | 2 |
| Updated Ethernet Switches Links | 2026-03-30 | 2026-03-30 | 0 | 1 | 1 |
| Marvell Industrial Alert System | 2025-12-19 | 2025-12-19 | 0 | 1 | 1 |
| Optional Marvell Chipset Solutions | 2025-12-02 | 2025-12-02 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-04 | 2025-11-04 | 0 | 1 | 1 |
| 8 Port Industrial PoE Switch | 2025-10-14 | 2025-10-14 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-09-26 | 2025-09-27 | 1 | 2 | 6 |
| Industrial PoE Switch | 2025-09-03 | 2025-09-03 | 0 | 1 | 1 |
| 90W PoE Managed Switch | 2025-07-29 | 2025-07-29 | 0 | 1 | 1 |
| Managed Optical Bypass Switch | 2025-07-09 | 2025-07-09 | 0 | 1 | 1 |
| …共 16 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：A 级面层　|　**自动源**：2 个　|　**数据截至**：2026-10-24T04:35:40Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SA-091/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://alphanetcom.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 8478 字符；首行：San Antonio Network Cabling & Fiber Installation \| Alpha Net |
| [sitemap](https://alphanetcom.com/sitemap.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |

- **人工定期看（登录墙，不自动抓）**：Facebook: https://www.facebook.com/AlphaNetComs/；X/Twitter: https://mobile.twitter.com/Alpha_NetComs；LinkedIn: https://www.linkedin.com/company/alpha-net-communications

## 联系方式（已有 · 原值照录）

- 邮箱：`nate.cline@alphanetcom.com`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Nathan
- 联系人（原值）：Nathan "Nate" Cline / President
- 网站/域名：alphanetcom.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Nathan "Nate" Cline | President | nate.cline@alphanetcom.com / +1 210-654-0653 | 调研核实（公开页） | https://www.alphanetcom.com/（Contact 区块） |
| Nathan | — | nate.cline@alphanetcom.com | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:alphanetcom.com`, `e:nate.cline@alphanetcom.com`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A Replied 09.04.xlsx#总表:24 | 23 | https://www.alphanetcom.com/#team | 美国 | Nathan | 谷歌 | 工业switch<br>分销商 | nate.cline@alphanetcom.com |  | 1 条 |
| E/群发/筛选后质量一般的_群发.xlsx#US:33 | 32 | https://www.alphanetcom.com/ | 美国 | Nathan "Nate" Cline<br>President | 谷歌 | 有比较多的供应商 产品面广<br>Networking      switch | nate.cline@alphanetcom.com |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-424DGGPM-280W | 深挖对位：布线承包商摄像/门禁/AP 项目：STC-424DGGPM-280W 主推；Wi-Fi 6E/7 与 multi-gig 布线对应 STC-424XGGPM-280W（2.5G 下行需核）；8 口位 STC-28DGGPM；集成商 25% 档 | $140.1 USD EXW（25% 档，SmartByte LT-S8328GP-4GX24GT-S 750 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 25%（布线承包商/小型系统集成商） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $84.1 USD EXW（25% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $145.7 USD EXW（25% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选4 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $188.7 USD EXW（25% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.25 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424DGGPM-280W），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STC-424DGGPM-280W 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；25% 档报价。
- 节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 1 次实质回复（对方认识我们）；北美主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STC-424DGGPM-280W 按 25% 档报价，做现供应商的第二货源；规模（调研）：微型（1–10 人）
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
| 商业资格结论 | **技术上合格 / 商业上有互动证据（成交或实质回复或面谈）→ 值得长期跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STC-424DGGPM-280W - 24-port Gigabit PoE+ L2+ managed switch (Marvell-based, neutral label)

```text
Hi Nathan,

Picking up our earlier exchange about PoE / industrial switches. For the camera, access-control and Wi-Fi 6E/7 drops you cable in San Antonio and Austin, the Marvell-based 24-port PoE+ managed switch at EXW cost is the one I am quoting, with the 10G-uplink version for the multi-gig jobs.

We supply a Marvell-based 24-port Gigabit PoE+ L2+ managed switch (280 W PoE budget, 4 uplinks) - model STC-424DGGPM-280W - that fits the same slot as your HPE / Extreme（转售） 企业接入交换机 at a lower landed cost, and we can ship it with neutral packaging. Current price: $140.1 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Which switch model are you buying most often right now, and roughly how many units a month?

If useful, I can send one unit for a 30-day side-by-side test. If not a fit, one line and I close the loop.

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

- **2026-11-07**（14 天）：无回复 → 换通道再试一次；仍无 → 降 B。有任何回复 → 当即更新 research JSON 并重渲染。

## 变更日志

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 A，分数 70）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
