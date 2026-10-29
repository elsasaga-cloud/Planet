# Fikes Media

> **评级 A**　|　美国　|　档案编号 `SB-1114`　|　优先级 ★★★　|　状态：名单内·未触达
>
> **P 池并入（A 档，等级不动）：★ P 池 · 正式入池（资产池，终身跟进 + 每 2 个月巡检）**（批 AB-01 · 2026-10-29 · 下次巡检 2026-12-28）：★ P 池正式（P 核心候选，B 档并池 · 等级不动）：成单 / 样品 / PI ✔（J5 看证据不看地区）；对位 ✔ 交换机；命中 3/6（成单/样品 ✔ · 真回 — · WA — · 对位 ✔ 交换机 · 登记 未坐实 · 体量 微型（1 人；老板另有全职 ）　|　标签：core（核心：成单 / 样品 / PI 或 A 档）、oem_target（贴牌卖交换机的渠道商 —— OEM 专项对象，留 C）
>
> **类型**：媒体/IT 集成小公司（业主直营）（推断）　|　**历史关系**：名单内·无互动记录　|　**所在清单**：补录、S邮箱回复、OEM意向、待回复　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-1114
rating: A
rating_auto: B
sieve: pool  # 闸 3 AB1 2026-10-29
rating_research: A  # Q-76 LT-01 2026-10-29：B→A 核心（精华跟）：A2 成单/样品/PI+真人往来；A3 真人往来+对位+四主区+坐实/自牌；A5 自有品牌+
name_official: "Fikes Media"
score: 58
country: 美国
region: 北美
website: fikesmedia.com
type: 媒体/IT 集成小公司（业主直营）
tier_tags: ["补录", "S邮箱回复", "OEM意向", "待回复"]
deal: no
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 4 msgs (out 3 / in 1), 2026-10-03 -> 2026-10-19
p1: STC-424XGGPM-280W
price_tier: 30%
research: done
site_snapshot: none
sources: 1
updated: 2026-10-29
```

## SALES BRIEF（压缩模型）

- **是谁**：美国小公司（Owner Christopher Fikes，电话区号 409 = 德州 Beaumont 一带），2026-10-03 回复群发表示有兴趣，关心 OEM 定制层级与控制器 API 集成；Simon 10-04 发完整 OEM 清单 + MIB + 规格书 + CLI/Web 手册并反问控制器架构，10-19 追问样品，客户未回。S 邮箱 4 封。（调研 2026-10-22；表内兴趣：24 口 PoE L2+（STC-424XGGPM-280W）的 OEM 定制 + 控制器 API 集成（REST/SNMP/CLI 待明确））
- **为什么是 A 级**：**调研后定级 A**（Q-76 LT-01 2026-10-29：B→A 核心（精华跟）：A2 成单/样品/PI+真人往来；A3 真人往来+对位+四主区+坐实/自牌；A5 自有品牌+对位+真人往来）；自动分级 B：+10 谈到样品/测样；+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国；+5 最近活动 2026
- **历史互动**：名单内·无互动记录
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-424XGGPM-280W — 美国 + 主动；$180（2026-10 对同类客户报价）；**价表版本**：STC-424XGGPM-280W：$180 = 2026-09-21 起群发现价 = 对 Fikes 报的价，一致；2026-06-22 PDF 的 $198 从未发出，后续沿用 $180（口径 #20）
- **第一问（只问一个）**：Christopher — straight answer on integration: SNMP v2/v3 + scriptable SSH/CLI + MQTT status publish (firmware 7.5) today, no REST/cloud controller. Which controller/NMS are you pairing it with — then I can confirm what it can poll/set before we ship 2 samples.
- **最大未知**：年走量与现供应商
- **下一步**：2026-11 上旬（距 10-19 催信 ≥2 周后；本周不发） S 邮箱 → cfikes@fikesmedia.com（同一线程） 一句话补上 10-04 没说死的边界：集成 = SNMP v2/v3 + SSH/CLI 脚本，无 REST/云控制器；问他的控制器是哪个，再决定要不要寄 2 台样

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-1114` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度触达（2026-10-03 一封实质来信「This actually does have my interest. What levels of customization… api availability for controller integration」；Simon 10-04 长回 + 10-19 催样，均无回；Elsa 箱：`to:fikesmedia.com` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 3 / 来 1）（第 74 批(h)））** ｜ 类型：美国小型媒体/IT 集成商（Fikes Media；业主直营）——第四档，但问的是定制 + API ｜ 筛子：2 ｜ 停点：API/控制器集成：Saga 线只有 SNMP/CLI/Web，无 REST/云控——若不直说会吊着（研究档已记） ｜ 复活：直说 SNMP + CLI 自动化可做、REST/云控不做 ｜ 通路：US 主攻 ｜ 节奏：来 1（10-03）/ 去 3（10-03 群发、10-04 长回、10-19 催）；最后动作是 Saga ｜ 证据：k=af638fab0ab5ad29（interest + API）；3c37c75887d3f132（定制清单）
- **现状一句话**：新线索（3 周前），技术诉求明确。
- **对方真实需求（有据）**：24 口 PoE + 10G 上联，可 API 集成。
- **断点 / 为什么停在这里**：API 期望。
- **Saga 现在该推什么**：P1 **STC-424XGGPM-280W**（25% 档，$180（2026-10 对同类客户报价）；**价表版本**：STC-424XGGPM-280W：$180 = 2026-09-21 起群发现价 = 对 Fikes 报的价，一致；2026-06-22 PDF 的 $198 从未发出，后续沿用 $180（口径 #20））——美国 + 主动
  - 做不了 / 要先核的：他的控制器是什么
- **下一步（具体）**：2026-11 上旬（距 10-19 催信 ≥2 周后；本周不发）　S 邮箱 → cfikes@fikesmedia.com（同一线程）　一句话补上 10-04 没说死的边界：集成 = SNMP v2/v3 + SSH/CLI 脚本，无 REST/云控制器；问他的控制器是哪个，再决定要不要寄 2 台样
  - 第一问（只问一个）：Christopher — straight answer on integration: SNMP v2/v3 + scriptable SSH/CLI + MQTT status publish (firmware 7.5) today, no REST/cloud controller. Which controller/NMS are you pairing it with — then I can confirm what it can poll/set before we ship 2 samples.

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2026-10-03 | 来 | Christopher Fikes | This actually does have my interest. What levels of customization are offered? I would be interested if there was api availability for controller integration. | API 诉求 | `af638fab0ab5ad29` |
| 2026-10-04 | 去 | Simon → Christopher Fikes | 1. Customization: logo / Packaging / PVC mask / label / model name / SN / manual / default IP / SNMP OID / Web GUI language… firmware customization subject to technical evaluation. 2. Controller Integration / API: could you share a little more about your controller architecture? REST API / SNMP / SSH-CLI / NETCONF / another platform… 3. Datasheet, Web manual, Feature List, MIB Manual attached. 4. "It's about function, not vendors" on your website… are you mainly evaluating for: consulting lab / customer deployments / private-label (OEM)? | Simon 已经回了定制清单并把 API 问题反问回去（没有直说「无 REST」）；10-19 又催了一次「Any feedback… Maybe arrange 2 samples?」——两封去信无回。档案原来的「现在：直说 API 边界」已过时：现在不该再发第三封，等到 11 月上旬只补一句「SNMP/CLI 即可，REST 没有」 | `gmail_s（fikesmedia.com，jsonl client 字段为空，按域名重扫）` |
| 2026-10-19 | 去 | Simon → Christopher Fikes | Any feedback about our product information? Maybe arrange 2 samples for testing? | 15 天内第二封去信无回；美国 SOHO 咨询商（Owner 一人）10-03 的热情之后沉默——按「只问一句」规则，下一封放到 2026-11 上旬，且要把 10-04 没说清的 API 边界一句说死 | `gmail_s（fikesmedia.com，jsonl client 字段为空，按域名重扫）` |

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **发信窗口（US 全库 2491 封群发的打开标签，对方本地时间；均值 5.4%）**：周三 08–10 点 13.6%（44 封）、周二 08–10 点 11.1%（63 封）。像素统计，只看相对高低；排发信日时落在这两个时段。
- **本国来询季节（US 全库 53 个「户·月」真人来信）**：8 月 17.0% / 11 月 11.3% / 1 月 11.3%——本户来信太少，按本国节奏排下一步。
- **同国同档参照（US，25% 档、主推线「商用 10G PoE 管理型」，共 6 户有动静，列前 3）**：SA-006 Vi-Link（vilinknet.com）（A，同线：成交 STC-110FE、STC-110XGE、STC-14DUR，回过 11 次（最近 2025-05-09），1:1 报过 3 次）；SB-831 actelis.com（B，同线：回过 6 次（最近 2026-03-02），1:1 报过 1 次）；SA-060 gofiberx.com（A，同档：回过 4 次（最近 2026-06-05））。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。
- **日历窗口**：对方：2026-11-26 感恩节（周四–周日四天基本停摆）；2026-12-24 圣诞–元旦（12-24 → 01-04 多数公司半停） ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 第 82 批 · 邮箱域体检 + 假日避让 + 公司底数（2026-10-27）

> 来源：DNS MX / A 查询（`mx_check.py`）、`holidays` 包 + 手工惯例表（`holidays_cal.py` → `docs/各国假日避让_2026-11_2027-03.md`）、官方工商登记（`data/saga_clients/registry/`）、官网快照标价片段。全部可复查；没有的项不写。

**邮箱域体检（DNS MX / A，2026-10-29 查）：**

- `fikesmedia.com` → Google Workspace（MX：ASPMX.L.GOOGLE.com、ALT2.ASPMX.L.GOOGLE.com、ALT1.ASPMX.L.GOOGLE.com、ALT3.ASPMX.L.GOOGLE.com）。Gmail → Gmail 同生态投递最稳；但 Gmail 图片代理会预抓像素 → 「已打开」偏高，别把 open 当成读过；三个发信箱别同一天给这个域发

**假日避让（美国 · 按下一步「现在 → 两周内」窗口 2026-10-29→2026-11-12）：**

- 法定假日：11-11 Veterans Day —— 假日前一个工作日下午、当天、长假后第一个上午都别发

**公司底数 · 第 94 批（US · 1 次检索：Tracxn（2007 年 Christopher Fikes 创立；Silsbee；未融资）+ fikesmedia.com/about（2007；「与老朋友 Mikrotik 的新合作」）+ /contact（105 George St, Silsbee TX 77656；旧址 109 Pinecrest Dr）+ Crunchbase 人物页（Christopher Fikes：Evadale ISD 信息技术主任 2018– + FikesMedia Owner 2007–）+ bizstanding（Fikesmedia.Com, Member Christopher Fikes / Principal, inactive），2026-10-28 查；https://www.fikesmedia.com/about）：**

- 法定名 / 登记号：FikesMedia LLC（fikesmedia.com；Silsbee TX） · TX 登记号未取（TX SoS 付费；bizstanding 镜像显示旧登记 inactive） · 状态 **官网在线（2026）；登记状态存疑（镜像 inactive）** · 成立 2007 · LLC（德州）
- 行业码 / 经营范围：MikroTik 转售 + IT 服务（副业）
- 注册地址：105 George St, Silsbee, TX 77656
- 规模档：微型（1 人；老板另有全职 = 学区 IT 主任 + 兼职教授）
- 账目：—；—
- 高管：Christopher Fikes — Owner（研究档 KP；同时任 Evadale ISD Director of IT）
- 控制人 / 股东：Christopher Fikes 100%（推定）
- **这意味着什么：**
  - **一人副业（老板全职在学区）** → 量极小；分销 20% 线只给一页纸，不投第 2 封
  - 唯一价值：他管一个学区的网络 → 若他回信，问的是「学区项目用 PoE 交换机」而不是经销
  - 德州登记可能已失效（镜像 inactive）→ 不作为可靠底数；不动 B
- 备注：TX SoS 付费未查；不再追。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Fikes Media | 事实（用户表） |
| 国家 | 美国 | 事实（用户表）|
| 网站/域名 | fikesmedia.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 媒体/IT 集成小公司（业主直营） | 推断（据兴趣/备注关键词） |
| 联系人 | Christopher Fikes | 事实（用户表） |
| 来源（From） | 补录：S 邮箱 2026-10 群发（Apollo 名单）回复客户（T29-U10 复盘发现） | 事实（用户表） |
| 兴趣（Interested in） | 24 口 PoE L2+（STC-424XGGPM-280W）的 OEM 定制 + 控制器 API 集成（REST/SNMP/CLI 待明确） | 事实（用户表） |
| 用户备注（Remark） | S 邮箱 4 封（2026-10-03 → 10-19）：10-03 回复「This actually does have my interest. What levels of customization are offered? …api availability for controller integration」；10-04 Simon 发 OEM 清单（logo/包装/面板/标签/型号/序列号/手册/默认 IP/SNMP OID/Web 语言）+ MIB 文件 + 规格书 + CLI/Web 手册并反问控制器架构；10-19 Simon 追问样品，客户未回；详见 research JSON | 事实（用户表） |
| 用户分档（Category） | 媒体/IT 集成小公司（业主直营） | 事实（用户表） |
| 所在清单 | 补录、S邮箱回复、OEM意向、待回复 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-22）**　网站状态：未核（本轮只用 S 邮箱证据）
- **是谁**：美国小公司（Owner Christopher Fikes，电话区号 409 = 德州 Beaumont 一带），2026-10-03 回复群发表示有兴趣，关心 OEM 定制层级与控制器 API 集成；Simon 10-04 发完整 OEM 清单 + MIB + 规格书 + CLI/Web 手册并反问控制器架构，10-19 追问样品，客户未回。S 邮箱 4 封。
- **类型**：媒体/IT 集成小公司（业主直营）
- **规模**：小（Owner 直接回信）
- **【email】有兴趣 + 问 OEM 层级 + 要 API/控制器集成**
  > This actually does have my interest. What levels of customization are offered? I would be interested if there was api availability for controller integration. If you have some specification sheets and models available I would love to see them.
  > 来源：data/gmail_s/messages/2026/2026-10.jsonl（抓取 2026-10-03）
- **【email】Simon 回复的 OEM 菜单（可复用口径）**
  > Company logo / Packaging / Front panel (PVC mask) / Product label / Model name / Serial number / User manual / Default login IP / SNMP OID customization / Web GUI language… firmware customization for specific project requirements, subject to technical evaluation（附 SWITCH-MIBS-release.docx、Saga Feature List_7.5.x_L2+.xlsx、STC-424XGGPM-280W.docx、CLI/Web Manual）
  > 来源：data/gmail_s/messages/2026/2026-10.jsonl（抓取 2026-10-04）
- **【email】Simon 追问样品，未回**
  > Any feedback about our product information? Maybe arrange 2 samples for testing?
  > 来源：data/gmail_s/messages/2026/2026-10.jsonl（抓取 2026-10-19）
- **KP**：Christopher Fikes（Owner（2007–；同时任 Evadale ISD 信息技术主任 2018– + 兼职教授）= 一人副业老板（第 94 批 官方登记核实 2026-10-28））cfikes@fikesmedia.com 409.877.4220〔S 邮箱签名〕
- **调研后定级**：A（原自动 B）——Q-76 LT-01 2026-10-29：B→A 核心（精华跟）：A2 成单/样品/PI+真人往来；A3 真人往来+对位+四主区+坐实/自牌；A5 自有品牌+对位+真人往来
- 备注：API/控制器集成是关键未知：Saga 线（SmartByte Marvell AC5）有 SNMP/CLI/Web，无云控制器 REST API——下一封应直说 SNMP + CLI 自动化可做、REST/云控不做，别吊着。


## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：4 封（去 3 / 来 1）　|　**期间**：2026-10-03 → 2026-10-19　|　**最后去信**：2026-10-19
- **对方邮箱**：cfikes@fikesmedia.com、sales@fikesmedia.com
- **最后一封来信**：2026-10-03 cfikes@fikesmedia.com「Re: 24 Port PoE Managed Switch」：This actually does have my interest. What levels of customization are offered? I would be interested if there was api availability for controller integration. If you have some specification sheets and models available I would love to see them. Thank you Christ

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 24 Port PoE Managed Switch | 2026-10-03 | 2026-10-19 | 1 | 3 | 9 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：A 级面层　|　**自动源**：1 个　|　**数据截至**：2026-10-29T08:41:09Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-1114/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://fikesmedia.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 2761 字符；首行：Home |

## 联系方式（已有 · 原值照录）

- 邮箱：`cfikes@fikesmedia.com`〔企业邮箱；来源：用户表原值〕
- 电话：`+4098774220`〔电话/WhatsApp 状态未记；原值见来源表〕
- 联系人（原值）：Christopher Fikes
- 职位（原值）：Owner
- 网站/域名：fikesmedia.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Christopher Fikes | Owner（2007–；同时任 Evadale ISD 信息技术主任 2018– + 兼职教授）= 一人副业老板（第 94 批 官方登记核实 2026-10-28） | cfikes@fikesmedia.com / 409.877.4220 | 调研核实（公开页） | S 邮箱签名 |

- **通道建议**：有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件；企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| 补录客户.jsonl#(补录):9 | GM-002 | Fikes Media | 美国 | Christopher Fikes | 补录：S 邮箱 2026-10 群发（Apollo 名单）回复客户（T29-U10 复盘发现） | 24 口 PoE L2+（STC-424XGGPM-280W）的 OEM 定制 + 控制器 API 集成（REST/SNMP/CLI 待明确） | cfikes@fikesmedia.com O: 409.877.4220 https://www.fikesmedia.com | S 邮箱 4 封（2026-10-03 → 10-19）：10-03 回复「This actually does have my interest. What levels of customization are offered? …api availability for controller integration」；10-04 Simon 发 OEM 清单（logo/包装/面板/标签/型号/序列号/手册/默认 IP/SNMP OID/Web 语言）+ MIB 文件 + 规格书 + CLI/Web 手册并反问控制器架构；10-19 Simon 追问样品，客户未回；详见 research JSON Owner | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-424XGGPM-280W | 深挖对位：明确问 OEM 定制 → OEM/ODM 30% 档；若只是自用/项目则 25% | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（媒体/IT 集成小公司（业主直营）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-424XGGPM-280W），备选型不进首触。

- **第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 STC-424XGGPM-280W 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：北美主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STC-424XGGPM-280W 按 30% 档报价，做现供应商的第二货源；规模（调研）：小（Owner 直接回信）
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
| 商业资格结论 | **技术上合格 / 商业上有互动证据（成交或实质回复或面谈）→ 值得长期跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Re: 24 Port PoE Managed Switch — one straight answer on API

```text
Hi Christopher,

One straight answer I owe you from my Oct-4 mail: integration today is SNMP v2/v3 (standard + private MIB), scriptable SSH/CLI, and MQTT publish of port/PoE status from firmware 7.5 — there is no REST API or cloud controller. OEM customization (logo, model name, GUI, default config, packaging) is standard.

Which controller or NMS would you pair it with? With that I can confirm exactly what it can poll and set, and we can ship the 2 evaluation units ($180 USD EXW each, credited against a first order).

Best regards,
Simon
Saga Telecom - sagatele.com
```

> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-12**（14 天）：无回复 → 换通道再试一次；仍无 → 降 B。有任何回复 → 当即更新 research JSON 并重渲染。

## 变更日志

- 2026-10-29：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 B，分数 58）；人工/调研定级 → A

---

*建档日期：2026-10-29　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
