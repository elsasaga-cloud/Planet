# etictelecom.com
**官方名称（调研核实）**：Etic Telecom（etictelecom.com，法国）

> **评级 B**　|　法国　|　档案编号 `SB-910`　|　优先级 ★★　|　状态：有回复·跟进中
>
> **类型**：经销/集成（类型待核）（推断）　|　**历史关系**：实质回复 1 次；推送 22 次（2024-03-23 → 2025-12-29）　|　**所在清单**：S重点、用户判定不行　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-910
rating: B
rating_auto: B
name_official: "Etic Telecom（etictelecom.com，法国）"
score: 28
country: 法国
region: 欧洲
website: etictelecom.com
type: 经销/集成（类型待核）
tier_tags: ["S重点", "用户判定不行"]
deal: no
replies: 1
followups: 22
first_contact: 2024-03-23
last_contact: 2025-12-29
s_mail: 27 msgs (out 26 / in 1), 2024-05-22 -> 2026-09-08
p1: STI-288DGGPM
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-21
sources: 2
updated: 2026-10-27
```

## SALES BRIEF（压缩模型）

- **是谁**：法国工业通信设备制造商（1985 年起）：工业 VPN 路由器 IPL 系列、机器远程维护盒 RAS、SHDSL/SPE 以太网延长器 XSLAN/XELAN、VPN 集中器 SIG，以及**军规战术 SHDSL 交换机 XSMIL**（Airbus Defence & Space 选用）；市场为水务、能源、交通、城市基础设施与工业 4.0。其产品线没有常规千兆管理 PoE 交换机。用户表：S 重点，1 次实质回复，22 次跟进，**用户已判定「不行」**；联系人 Charles Chaussonnier。（调研 2026-10-21；表内兴趣：工业FS 外壳比较统一）
- **为什么是 B 级**：+22 实质回复 1 次；+25 在 Simon 的 S 重点名单；-60 用户已归入「不行及不太相关的」；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/法国；+5 最近活动 2025；+5 跟进表最近平台标记 S
- **历史互动**：实质回复 1 次；推送 22 次（2024-03-23 → 2025-12-29）；最近一次客户回复：2024-05-22：10 50 100个的价格
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STI-42424XGGPM 三档 DAP 价 — 法国品牌商 + 真询价｜已发资料（勿重发）：STI-4240XGGM(2024-05-22)、CLI Manual(2024-05-22)、Marvell Based Web Manual(2024-05-22)、Product Link_2026Q2(2026-03-02)、Saga Feature List_7.5.x_L2+(2026-06-22)；已发单据：Quotation(2024-05-22)；还没给过：Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）；按主表 OEM 30% 档 + 百运网 DAP；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-10-24 $65（10G Media Converter）、2024-11-20 $300（48 Port PoE Managed Switch）、2025-10-29 $280（10G Enterprise SFP Switch）、2026-07-20 $1500（24 Port 10G SFP+ Switch）、2026-09-08 $170（24 Port PoE Managed Switch）；群发里他已看到的价（续，第 66 批全量复核）：2025-01-03 $240（24 Port Fiber Switch）
- **第一问（只问一个）**：Charles — here is the 10/50/100 ladder on DAP-France terms for the 24-port DIN L3 PoE; is this still a live requirement for your router bundles?
- **最大未知**：年走量与现供应商
- **下一步**：现在 S 邮箱 → charles.chaussonnier@etictelecom.com 重报三档 DAP；附件：10 / 50 / 100 pcs 三档 DAP 表——Simon 先按百运网报价算到 Lyon 的运费再填，信里只写「attached sheet」

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-910` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：轻度绑定→未闭环（唯一一封来信 2024-05-22「What is the price DDP for 10, 50, 100 units?」= 三档量询价；Simon 当天给了 EXW 报价并声明不含清关；之后 Simon 两次追问无回，再 20+ 封群发无回；Elsa 箱：`to:etictelecom.com` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 26 / 来 1）（第 74 批(k)））** ｜ 类型：法国工业路由器/远程访问制造商（Etic Telecom；Charles = 采购/产品）——第一档品牌商，问的是 DDP 三档价 = 真在做成本模型 ｜ 筛子：3（三档量询价） ｜ 停点：他要 DDP，Saga 给 EXW + 「不含清关」——对法国品牌商这等于没报；没有 10/50/100 的阶梯也没有到门成本 ｜ 复活：重报一次：按 10/50/100 三档 + 百运网 DAP 法国（DAP 不是 DDP，但把运费与大致关税写清） ｜ 通路：FR 主攻 ｜ 节奏：一封重报 ｜ 证据：k=1e2c24b00883813d（DDP 10/50/100）；320115425c459bcb（EXW 报价 + NOT including customs）；096d6be144a97e35（追问 + Marvell 话术）
- **现状一句话**：客户问了一个采购经理才会问的问题（三档量的到门价），Saga 回了一张不含清关的 EXW 报价单，然后用「Marvell 是最贵的方案」追问——方向反了。
- **对方真实需求（有据）**：DIN 24 口 L3 管理 PoE（10G 上联）作为其工业路由器的配套。
- **断点 / 为什么停在这里**：贸易条款与阶梯价。
- **Saga 现在该推什么**：P1 **STI-42424XGGPM 三档 DAP 价**（30% 档，按主表 OEM 30% 档 + 百运网 DAP；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-10-24 $65（10G Media Converter）、2024-11-20 $300（48 Port PoE Managed Switch）、2025-10-29 $280（10G Enterprise SFP Switch）、2026-07-20 $1500（24 Port 10G SFP+ Switch）、2026-09-08 $170（24 Port PoE Managed Switch）；群发里他已看到的价（续，第 66 批全量复核）：2025-01-03 $240（24 Port Fiber Switch））——法国品牌商 + 真询价｜已发资料（勿重发）：STI-4240XGGM(2024-05-22)、CLI Manual(2024-05-22)、Marvell Based Web Manual(2024-05-22)、Product Link_2026Q2(2026-03-02)、Saga Feature List_7.5.x_L2+(2026-06-22)；已发单据：Quotation(2024-05-22)；还没给过：Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）
  - 做不了 / 要先核的：D；A；P； ；运；费；按；百；运；网；当；期；报；价； ；→； ；阶；梯；表；由； ；S；i；m；o；n； ；填；；；仓；库；不；编；运；费
- **下一步（具体）**：现在　S 邮箱 → charles.chaussonnier@etictelecom.com　重报三档 DAP；附件：10 / 50 / 100 pcs 三档 DAP 表——Simon 先按百运网报价算到 Lyon 的运费再填，信里只写「attached sheet」
  - 第一问（只问一个）：Charles — here is the 10/50/100 ladder on DAP-France terms for the 24-port DIN L3 PoE; is this still a live requirement for your router bundles?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-05-22 | 来 | Charles Chaussonnier | What is the price DDP for 10, 50, 100 units? | 三档量询价 | `1e2c24b00883813d` |
| 2024-05-22 | 去 | Simon | Please see attached quotation. Please know that the quotation is NOT including customs clearance cost at your side. | 条款错位 | `320115425c459bcb` |
| 2024-06-21 | 去 | Saga（Simon） | Hi, Charles, How are you? Any update about our offer last time? Not sure if you care about chip solution, we are using Marvell chip, basically one of the most expensive solutions on the market. Let me recommend a new unmanaged model(paralleled to the market prices). Feature: Support DIP dialing and… | Saga 实质答复原文（主题「Re: 24 port managed switch」；第 20 批从 gmail_s 回补）——承诺/口径以此为准 | `096d6be144a97e35` |

## 多维画像（数据推导 · 第 79 批 · 2026-10-27）

> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。

- **时机与节律**：真人来信 1 封（2024-05-22 → 2024-05-22）；**他们回信中位 0.1 小时**（1 次，100% 在 24 小时内）；我方回信中位 1.4 小时（1 次）。
- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：群发 22 封（2024-05-22 → 2026-09-08），打开标签 2 次（近 12 个月 0，最后 2025-02-17）；打开过：「24 port managed switch」×1（2024-05-22）、「48 Port SFP Switch」×1（2025-02-17）；从未打开：「90W PoE Managed Switch」、「10G Media Converter」、「48 Port PoE Managed Switch」。
- **报价轨迹**（S/A 去信里「价 + 型号/描述同句」：1:1 0 条 + 个性化群发价 6 条，2024-10-24 → 2026-09-08；「今天」= 价格主表 2026-10-17 汇率、30% 档、不高于 2026-06 列表价；只列每个型号/描述最近一次，最多 8 行）：

  | 日期 | 型号 / 原句 | 当时 | 今天应报 | 变化 | 性质 | 主题 | 消息 key |
  |---|---|---|---|---|---|---|---|
  | 2026-09-08 | 「*Price: 170USD/PC*」 | $170 | —（原句无型号） | — | 群发价 | 24 Port PoE Managed Switch | `4f6cb988e33104e2` |
  | 2026-07-20 | 「*Price: 1500USD/PC*」 | $1500 | —（原句无型号） | — | 群发价 | 24 Port 10G SFP+ Switch | `8093def8e5ae3cea` |
  | 2025-10-29 | 「It is a price-competitive aggregation switch(280usd/pc)」 | $280 | —（原句无型号） | — | 群发价 | 10G Enterprise SFP Switch | `d743477f3e331ade` |
  | 2025-01-03 | 「Price: 240usd/pc」 | $240 | —（原句无型号） | — | 群发价 | 24 Port Fiber Switch | `0063084ea01ffd95` |
  | 2024-11-20 | 「*Price is very competitive, 300usd/pc*」 | $300 | —（原句无型号） | — | 群发价 | 48 Port PoE Managed Switch | `453bbe90765ccb94` |
  | 2024-10-24 | 「*Price: 65usd/pc, 1*10G SFP+1*100M/1G/2.5G/10G Ethernet, unmanaged,」 | $65 | —（原句无型号） | — | 群发价 | 10G Media Converter | `f9cf7931e9982e4a` |

  「个性化群发价」= 同一句价发给 ≥5 家的信（Simon 的手工群发），对方未必读过，但它就是对方邮箱里躺着的「上次报价」。
- **品类覆盖与缺口**：官网兴趣：工业（industrial 72 / automation 0）；我们 1:1 从未报过价、也没成交；打开过的群发主题落在：10G 汇聚；**还没碰过的一类：工业** → 下封信可加一句 STI-288GP（8 口千兆 PoE+ 2 SFP 工业非管理，$62.2 EXW）。
- **规模与贴牌线索（官网快照 2026-10-21）**：站点地图 427 条 URL；站内可见品牌 2 个（Schneider、Siemens）；官网语言 en-GB（信照样英文，首句可用对方语言问候）。
- **写信的人（来信签名机械抽取）**：Charles Chaussonnier（charles.chaussonnier@etictelecom.com，1 封，2024-05-22 → 2024-05-22）。
- **日历窗口**：对方：2026-12-24 圣诞–元旦 ｜ 我方春节停产：2027-02-06 春节，SmartByte / HRUI 工厂约 01-30 → 02-20 停工；要赶年前出货须 **2027-01-10 前下单**（4–7 个工作日交期 + 年前物流拥堵）。

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | etictelecom.com（取自域名，公司全名待核） | 推断 |
| 国家 | 法国 | 事实（用户表）|
| 网站/域名 | etictelecom.com | 事实（用户表 URL/邮箱域名） |
| 类型 | 经销/集成（类型待核） | 推断（据兴趣/备注关键词） |
| 联系人 | Charles | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | 工业FS 外壳比较统一 | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | S重点、用户判定不行 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | FS | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：法国工业通信设备制造商（1985 年起）：工业 VPN 路由器 IPL 系列、机器远程维护盒 RAS、SHDSL/SPE 以太网延长器 XSLAN/XELAN、VPN 集中器 SIG，以及**军规战术 SHDSL 交换机 XSMIL**（Airbus Defence & Space 选用）；市场为水务、能源、交通、城市基础设施与工业 4.0。其产品线没有常规千兆管理 PoE 交换机。用户表：S 重点，1 次实质回复，22 次跟进，**用户已判定「不行」**；联系人 Charles Chaussonnier。
- **在卖/在用品牌**：Etic Telecom（自产）
- **【官网】产品线构成**
  > Our product lines Machine Access Box RAS Family Industrial VPN router IPL Family Ethernet extender XSLAN/XELAN Family VPN servers SIG Family SHDSL tactical switch XSMIL family
  > 来源：https://www.etictelecom.com/en/（抓取 2024-01-03）
- **【官网】公司历史与市场**
  > Etic Telecom designs and markets safe, simple, robust and low consumption products … Since 1985, we have been active in the water, energy, transportation, urban infrastructure and industry 4.0 markets. Etic Telecom is a European player designing and selling Telecom Products (routers, VPN servers, gateways, SHDSL switches, modem).
  > 来源：https://www.etictelecom.com/en/about-us/（抓取 2024-08-20）
- **【官网新闻】国防客户（守界依据）**
  > Airbus Defense & Space chooses Etic Telecom technologies … has chosen Etic Telecom technologies (IPL routers and Ethernet extender XSLAN) for networking barracks and mobile operational equipment.
  > 来源：https://www.etictelecom.com/en/airbus-defense-space-chooses-etic-telecom-technologies/（抓取 2020-07-09）
- **【用户表】S 重点；1 次实质回复；22 次跟进；用户判定不行；联系人 Charles Chaussonnier**
  > （用户表字段）
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Charles Chaussonnier（联系人（用户表））charles.chaussonnier@etictelecom.com —〔用户表〕
- 备注：（无首轮调研；由 deepen.py 建档）

### 加厚挖掘（2026-10-21 · B 级加厚 v1（官网产品线核对））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Etic Telecom |
| 成立 | 1985 |
| 总部/地址 | France（官网未列详细地址于摘要） |
| 其他 | 自研自产，欧洲玩家；产品线 RAS / IPL / XSLAN-XELAN / SIG / XSMIL；配置手册公开（SHDSL 交换机 XSLAN+1xxx/2xxx/4xxx，XSMIL-4200 军规 4 口） |

- **业务线**：工业 VPN 路由器与远程维护（IPL / RAS / SIG）；SHDSL / SPE 以太网延长器（XSLAN / XELAN）；军规战术通信（XSMIL；守界：不参与）

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| Etic Telecom | IPL-E-100 / IPL-E-400 / IPL-E-220 | 工业路由器 IP31 金属壳 DIN 导轨，10 条 VPN，SPI 防火墙，−20~+70 ℃，QoS/VLAN | —（路由器，Saga 无） | https://www.etictelecom.com/en/etic-product/ipl-e-100/（2024-12-09） |
| Etic Telecom | XSLAN+1xxx/2xxx/4xxx · XSMIL-4200 | 工业级 1/2/4 口 SHDSL 以太网交换机；XSMIL-4200 军规 | —（SHDSL 介质，Saga 无） | https://www.etictelecom.com/wp-content/uploads/2021/01/DOC_DEV_XS_Setup_guide_C.pdf（2021-01-01） |

- **触达通道（公开）**：网站: https://www.etictelecom.com/en/
- **近况信号**：
  - 唯一可能的切入点：其工业路由器/延长器需要配套的 DIN 导轨千兆管理 PoE 交换机（产品线空白）→ OEM 补线（Etic 标或中性）；但用户已判定「不行」，仅作低频备案
- **风险/边界**：军规/国防客户（Airbus Defence & Space、XSMIL）→ 守界，仅限水务/能源等民用线；制造商兼潜在竞争者；用户判定不行 → 不主动推进
- **Saga 对位结论**：P1 STI-288DGGPM（30% 档）——若重启：以 OEM（Etic 标）补其产品线空白——STI-288DGGPM DIN 导轨 8 PoE+ + 2 SFP 管理机，与 IPL 路由器同柜；OEM 30% 档；默认不推进（用户判定不行）
- **邮件切入句（英文）**：（用户已判定不行，默认不发；若重启）Alongside the IPL routers your water and energy customers deploy, a DIN-rail 8-port PoE+ managed switch in Etic packing would fill the one slot your range does not cover — would a sample for your lab be useful?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://www.etictelecom.com/en/　语言：en-GB　站点地图 URL 数：427
- **标题**：Home / Etic Telecom
- **首页栏目**：Our solutions / Our product lines / Why choose Etic telecom / Our news / New M2Me Smartphone in 2026 / EticSIM: Simplified IoT Connectivity / EticCUBE solution: 4G antenna extension up to 100m / CSPN – ANSSI Evaluation
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：industrial 72、telecom 42、switch 31、ethernet 22、scada 4、surveillance 1、cable 1
- **站内出现的品牌**：Schneider, Siemens　（「（！）」= Saga 自家/供应商品牌已在其站内出现）
- **站内型号串**（正则抽取，含非交换机）：RS232, RS485, XSMIL-BP4200IB, XSMIL-FD4200, XELAN-FD200, IPL-E-100, IPL-EW-100, IPL-C-100, IPL-C-400, IPL-C-220, IPL-CW-400, IPL-CW-220
- **站内公开邮箱**：contact@etictelecom.com, info@etictelecom.de
- **站内公开电话**：+33 (04) 76 04 20 00, +49 (0)7221 396555-1, +49 7221 3965551
- **产品类页面**：https://www.etictelecom.com/en/industrial-equipment-networking/；https://www.etictelecom.com/en/shdsl-switches-for-bilbao-water-network/；https://www.etictelecom.com/en/shdsl-switch-for-the-ring-of-paris-city/；https://www.etictelecom.com/de/shdsl-switches-for-bilbao-water-network-2/；https://www.etictelecom.com/de/shdsl-switch-for-the-ring-of-paris-city-2/；https://www.etictelecom.com/fr/switch-shdsl-pour-le-peripherique-parisien/
- **已抓子页**：[Industrial equipment networking / Etic Telecom](https://www.etictelecom.com/en/industrial-equipment-networking/)；[Industrial VPN router (IPL Family) / Etic Telecom](https://www.etictelecom.com/en/nos-gammes/industrial-router-ipl-family/)；[Archives des SHDSL tactical switch (XSMIL family) / Etic Tel](https://www.etictelecom.com/en/nos-gammes/durcie-tactical-shdsl-switch-xsmil-family/)；[Product documentation / Etic Telecom](https://www.etictelecom.com/en/products-documents-download/)；[Contact / Etic Telecom](https://www.etictelecom.com/en/contact/)；[About us / Etic Telecom](https://www.etictelecom.com/en/about-us/)
- 首页正文摘录：About us Our range of products Machine Access Box (RAS Family) Industrial VPN router (IPL Family) Ethernet extender (XSLAN/XELAN Family) VPN servers (SIG Family) SHDSL tactical switch (XSMIL family) Our solutions Machine remote maintenance Industrial equipment networking Raising an alert Data storage & dashboard in the Cloud Tactical equipment networking Our news Supports Product documentation Virtual showroom Legal 
- **自动对位建议**：STI-280GE（官网快照对位：工业/自动化词频 76、无 PoE 侧重 → DIN 8 GE + 2 SFP 非 PoE 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SB-910.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 22 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2024-03-23 | 2024.3.23 | 发了工业电电源价格册 |  | Email |  | S 09.08.xlsx#17 |
| 2024-05-02 | 2024.5.2 | 发了5电口信息 |  | Email |  | S 09.08.xlsx#17 |
| 2024-05-22 | 2024.5.22 | 发了4光24导轨式信息 | 10 50 100个的价格 | Email |  | S 09.08.xlsx#17 |
| 2024-06-21 | 2024.6.21 | 发了2光4小壳信息 |  | Email |  | S 09.08.xlsx#17 |
| 2024-07-29 | 2024.7.29 | 2光8 auto |  | Email |  | S 09.08.xlsx#17 |
| 2024-08-30 | 2024.8.30 | 8电口 |  | Email |  | S 09.08.xlsx#17 |
| 2024-09-30 | 930 | 28bt |  | Email |  | S 09.08.xlsx#17 |
| 2024-10-24 | 1024 | 10gmc |  | Email |  | S 09.08.xlsx#17 |
| 2024-11-20 | 1120 | 48口 |  | Email |  | S 09.08.xlsx#17 |
| 2024-12-11 | 1211 | 22迷你 |  | Email |  | S 09.08.xlsx#17 |
| 2025-01-03 | 1.3 | 24fiber |  | Email |  | S 09.08.xlsx#17 |
| 2025-02-17 | 2025.2.17 | 52 |  | S |  | S 09.08.xlsx#17 |
| 2025-04-08 | 4.8 | bypass |  | S |  | S 09.08.xlsx#17 |
| 2025-04-29 | 429 | 芯片 |  | S |  | S 09.08.xlsx#17 |
| 2025-05-27 | 527 | Alarm |  | S |  | S 09.08.xlsx#17 |
| 2025-06-25 | 625 | 16电 |  | S |  | S 09.08.xlsx#17 |
| 2025-07-28 | 728 | 24poe |  | S |  | S 09.08.xlsx#17 |
| 2025-08-27 | 827 | 28bt |  | S |  | S 09.08.xlsx#17 |
| 2025-09-29 | 929 | 28poe |  | S |  | S 09.08.xlsx#17 |
| 2025-10-29 | 1029 | dac |  | S |  | S 09.08.xlsx#17 |
| 2025-11-27 | 1127 | solar |  | S |  | S 09.08.xlsx#17 |
| 2025-12-29 | 1229 | taiwan |  | S |  | S 09.08.xlsx#17 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：27 封（去 26 / 来 1）　|　**期间**：2024-05-22 → 2026-09-08　|　**最后去信**：2026-09-08
- **对方邮箱**：charles.chaussonnier@etictelecom.com、contact@etictelecom.com
- **最后一封来信**：2024-05-22 charles.chaussonnier@etictelecom.com「RE: 24 port managed switch」：Hello, What is the price DDP for 10, 50, 100 units? Best Regards. Charles. De : Simon <s.sagatelecom@gmail.com> Envoyé : mercredi 22 mai 2024 14:30 À : contact@etictelecom.com Objet : 24 port managed switch Hi, How are you? There is a din rail 24 Port L3 manag
- **邮件里报过的价**：2026-09-08 $170；2026-07-20 $1500；2025-10-29 $280；2025-01-03 $240；2024-11-20 $300；2024-10-24 $65

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 24 Port PoE Managed Switch | 2026-09-08 | 2026-09-08 | 0 | 1 | 1 |
| 24 Port 10G SFP+ Switch | 2026-07-20 | 2026-07-20 | 0 | 1 | 1 |
| Firmware 7.5 L2+ Feature Update | 2026-06-22 | 2026-06-22 | 0 | 1 | 2 |
| Updated Ethernet Switches Links | 2026-03-02 | 2026-03-02 | 0 | 1 | 1 |
| OEM Core Switching Solution | 2026-01-29 | 2026-01-29 | 0 | 1 | 1 |
| Optional Marvell Chipset Solutions | 2025-12-29 | 2025-12-29 | 0 | 1 | 1 |
| Booster PoE Switch | 2025-11-27 | 2025-11-27 | 0 | 1 | 1 |
| 10G Enterprise SFP Switch | 2025-10-29 | 2025-10-29 | 0 | 1 | 1 |
| 8 Port Industrial PoE Switch | 2025-09-29 | 2025-09-29 | 0 | 1 | 1 |
| 90W PoE Managed Switch | 2025-08-27 | 2025-08-27 | 0 | 1 | 1 |
| Industrial PoE Switch | 2025-07-28 | 2025-07-28 | 0 | 1 | 1 |
| 16 Port Ethernet Switch | 2025-06-25 | 2025-06-25 | 0 | 1 | 1 |
| …共 22 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：3 个　|　**数据截至**：2026-10-26T07:56:19Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-910/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://www.etictelecom.com/en/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 4801 字符；首行：Home \| Etic Telecom |
| [sitemap](https://www.etictelecom.com/sitemap_index.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |
| [news_1](https://www.etictelecom.com/en/our-news/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 4031 字符；首行：Our news \| Etic Telecom |

## 联系方式（已有 · 原值照录）

- 邮箱：`contact@etictelecom.com`〔企业邮箱；来源：用户表原值〕
- 邮箱：`charles.chaussonnier@etictelecom.com`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Charles
- 网站/域名：etictelecom.com
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Charles Chaussonnier | 联系人（用户表） | charles.chaussonnier@etictelecom.com / — | 调研核实（公开页） | 用户表 |
| Charles | — | contact@etictelecom.com / charles.chaussonnier@etictelecom.com | 用户表原值 | Clients/ 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:etictelecom.com`, `e:contact@etictelecom.com`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| S 09.08.xlsx#总表:18 | 17 | https://www.etictelecom.com/en/nos-gammes/ethernet-extender-xslan-family/ | 法国 | Charles | 谷歌 | 工业FS 外壳比较统一 | contact@etictelecom.com<br>charles.chaussonnier@etictelecom.com |  | 22 条 |
| 不行及不太相关的.xlsx#总表:691 |  | https://www.etictelecom.com/en/nos-gammes/ethernet-extender-xslan-family/ | 法国 |  | 谷歌 | 工业FS 外壳比较统一 | contact@etictelecom.com |  | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-288DGGPM | 深挖对位：若重启：以 OEM（Etic 标）补其产品线空白——STI-288DGGPM DIN 导轨 8 PoE+ + 2 SFP 管理机，与 IPL 路由器同柜；OEM 30% 档；默认不推进（用户判定不行） | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（经销/集成（类型待核）） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288DGGPM），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STI-288DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 1 次实质回复（对方认识我们）；欧洲主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STI-288DGGPM 按 30% 档报价，做现供应商的第二货源
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
| 现用/在卖交换品牌 | ✅ FS |
| 采购量/预算 | ❓ 未确认（有回复但未报量） |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：24-port DIN L3 PoE — 10/50/100 pcs, DAP France

```text
Hi, Charles,

In May 2024 you asked for DDP prices for 10/50/100 units of the 24-port DIN-rail L3 managed PoE with 10G uplinks, and we only answered EXW. Here is the proper answer.

- Base: STI-42424XGGPM (L3), 24x GbE PoE + 4x 10G SFP+, -40 to +70 C at 240 W PoE budget (-40 to +60 C at 370 W) — $517 USD/pc EXW (2026-10 table, valid 15 days).
- 10 / 50 / 100 pcs: tiered prices on the attached sheet.
- Terms: DAP France via our forwarder (sea or air, your choice); import VAT/duty handled by you or your broker — we do not do DDP into the EU.

One question: is this still a live requirement for your router bundles, and which quantity should I firm up first?

Thank you.
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

- **2026-11-26**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-27：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 B，分数 28）

---

*建档日期：2026-10-27　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
