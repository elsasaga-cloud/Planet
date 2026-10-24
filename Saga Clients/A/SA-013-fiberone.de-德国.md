# fiberone.de
**官方名称（调研核实）**：fiberONE（NYNEX satellite OHG, Darmstadt）

> **评级 A**　|　德国　|　档案编号 `SA-013`　|　优先级 ★★★　|　状态：成交过·活跃（Simon）
>
> **类型**：运营商/ISP（终端 + 自有 logo 贴牌需求）（推断）　|　**历史关系**：成交/下单过；实质回复 1 次；推送 2 次（2024-11-09 → 2025-05-29）　|　**所在清单**：A优质名单(其他优质欧洲客户)、AI评估(EU)·DONE、成交(PI)、Simon:活跃、Xtransfer　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SA-013
rating: A
rating_auto: A
rating_research: A  # PI 包成单客户，Simon 标签 活跃 → A
name_official: "fiberONE（NYNEX satellite OHG, Darmstadt）"
score: 112
country: 德国
region: 欧洲
website: fiberone.de
type: 运营商/ISP（终端 + 自有 logo 贴牌需求）
tier_tags: ["A优质名单(其他优质欧洲客户)", "AI评估(EU)·DONE", "成交(PI)", "Simon:活跃", "Xtransfer"]
deal: yes
replies: 1
followups: 2
first_contact: 2024-11-09
last_contact: 2025-05-29
s_mail: 104 msgs (out 59 / in 45), 2024-11-09 -> 2026-10-17
p1: STC-28DGGPM
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-21
sources: 2
updated: 2026-10-24
```

## SALES BRIEF（压缩模型）

- **是谁**：德国达姆施塔特的光纤接入运营商品牌（NYNEX satellite OHG 旗下，11–50 人，2015 年起），在法兰克福/莱茵美因地区自建 FTTB/FTTH 网络（10G 对称），为楼宇提供千兆接入；B2B 提供专线、波长、楼宇网络。用户表：兴趣 SFP/MC 周边并要「自己的 logo」（贴牌），1 次实质回复，邮件中有详细联系方式。（调研 2026-10-22；表内兴趣：SFP MC 周边产品 自己的logo）
- **为什么是 A 级**：**调研后定级 A**（PI 包成单客户，Simon 标签 活跃 → A）；自动分级 A：+50 有成单/下单/买过记录（用户备注或跟进表）；+22 实质回复 1 次；+6 在 A/DONE 优质国家名单（已做过整轮推送）；+2 在 AI 客户评估名单；-15 AI/Claude 评估 C；+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+2 兴趣仅 MC/SFP/配件（边缘品类）；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 欧洲/德国；+5 最近活动 2025；+5 跟进表最近平台标记 S
- **历史互动**：成交/下单过；实质回复 1 次；推送 2 次（2024-11-09 → 2025-05-29）；最近一次客户回复：2024-11-09：非PoE, 全光，100G
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-4168XGGCM（在产第 6 单） — 唯一较深绑定客户，每一单都在加深（OID/MIB/固件进入他们的 LibreNMS/Oxidized 运维体系）；价值 = 长期现金流 + 工程背书；第 6 单 20 台 @2,015 RMB 基数（S 邮箱 2026-09/10）；下一单报价按 SmartByte 当期价 ×1.3 ÷ 汇率快照——OEM 品牌商档（他们以 fiberONE 名义部署）
- **第一问（只问一个）**：Is the 2×10G + 4×2.5G lite-managed media converter (1,000 initial / 2,000 per year) still on your FTTH roadmap for 2027?
- **最大未知**：年走量与现供应商
- **下一步**：第 6 单交付后 1 周（预计 2026-11 上旬） S 邮箱（Simon 主线） 交付回访 + 一句话重提媒体转换器需求是否仍在（1,000/2,000 年量），附 HRUI 线可行与否的结论

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SA-013` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：较深（6 单复购 + LibreNMS 提交 SmartByte OID + 客户系统依赖 MIB/固件 + 坚持 SmartByte 原名）** ｜ 类型：德国 ISP/FTTH 运营商 NYNEX satellite OHG（fiberONE）（技术流，工程师 Frederik Kriewitz 直接对接） ｜ 筛子：3（多次 PI/T/T、EUR 付款、固件/MIB 迭代、工程反馈） ｜ 停点：无明显停点；但两次更大机会流失：230 台项目（2026-01-20「we used our existing supply because you initially quoted a long lead time」）与 1,000+2,000/年 低成本 2×10G+4×2.5G 媒体转换器（2025-10-21，Marvell 无合适芯片替代 RTL8373） ｜ 复活：已在复购中（2026-10-15 第 6 单 20×STC-4168XGGCM EUR 付款、10-17 投产）；下一级 = 交期承诺 + 媒体转换器方案（Realtek 线可否？） ｜ 通路：DE 已通（USD/EUR T/T 到同一账户、DHL；Peter 直接处理技术） ｜ 节奏：最后 2026-10-17 Simon「got the payment and are producing」；实质往来 2024 → 2026-10 持续；S 邮箱 45 来 / A 邮箱无 ｜ 证据：S 邮箱 k=c921dc47fd9370bb / 8f79a607c3cc831e / 3c32c9ad46e6235d / 61065505a331e5fd / c24584352bd15931 / 60ac95de9259a792
- **现状一句话**：NYNEX（Frederik Kriewitz）是全库唯一「较深」绑定：2025-03 测试反馈即要求 SmartByte 申请 IANA PEN 并把私有 OID 挂到自己树下（后以 SmartByte PEN 56166 落地，LibreNMS 26.1 按 sysObjectID 识别「SmartByte」）；2025-09 为 230 台项目问 AC5 新机（风扇/双电源监控）→ 样机 1 台 → 11–12 月 MIB/固件三轮迭代到「working as expected」；2026-01-20 告知 230 台因 Saga 最初交期长而用了现有供应；2026-09-29 第 6 单 20×STC-4168XGGCM（双 AC，同上单），要 EUR 付款、因涨价需另取 3 家比价，10-15 付款并坚持 **SmartByte 原名 + SNMP 厂商 OID**，10-17 投产。
- **对方真实需求（有据）**：① 1G SFP 下联 + 10G 上联接入机（STC-4168XGGCM 双 AC）——持续；② 风扇/双 PSU 状态、温度、CPU/内存全部可 SNMP 读（ENTITY-SENSOR-MIB 标准化建议）；③ **低成本 2×10G + 4×2.5G 轻管理媒体转换器/ONT，首单 1,000、之后 2,000/年**（FTTH 1G→10G 升级，老路由器只支持 1G）；④ 交期短（230 台项目因交期丢）。
- **断点 / 为什么停在这里**：无停点；真正的瓶颈是**交期与价格基数**（2026-09-29「Due to the price increase I'll have to get 3 more comparison quotes」）以及 Saga 没有接住媒体转换器那条 1,000+2,000/年 的线（Marvell 无对应芯片；Realtek RTL8373 正是他点名的方案——这是 HRUI 线可能的切入点，但要 Simon 判断是否违背「Marvell 口号筛子」）。
- **Saga 现在该推什么**：P1 **STC-4168XGGCM（在产第 6 单）**（30% 档，第 6 单 20 台 @2,015 RMB 基数（S 邮箱 2026-09/10）；下一单报价按 SmartByte 当期价 ×1.3 ÷ 汇率快照——OEM 品牌商档（他们以 fiberONE 名义部署））——唯一较深绑定客户，每一单都在加深（OID/MIB/固件进入他们的 LibreNMS/Oxidized 运维体系）；价值 = 长期现金流 + 工程背书
  - 复购/在买项：STC-4168XGGCM 双 AC（第 5、6 单）；2025-09 AC5 样机 1 台
  - 做不了 / 要先核的：媒体转换器 2×10G+4×2.5G：Marvell 无合适低成本芯片，Realtek RTL8373 方案是否走 HRUI 线——Simon 决定（不违背 U29：价在 `价格主表_HRUI.csv`）；交期：SmartByte 机箱/批次交期是丢 230 台的原因，下一单前要先给出可承诺交期；PEN/OID 维持 SmartByte（Q-45 默认不动）
- **下一步（具体）**：第 6 单交付后 1 周（预计 2026-11 上旬）　S 邮箱（Simon 主线）　交付回访 + 一句话重提媒体转换器需求是否仍在（1,000/2,000 年量），附 HRUI 线可行与否的结论
  - 第一问（只问一个）：Is the 2×10G + 4×2.5G lite-managed media converter (1,000 initial / 2,000 per year) still on your FTTH roadmap for 2027?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-03-26 | 来 | Frederik Kriewitz（NYNEX） | Can you please request your own SmartByte SNMP enterprise OID at iana.org… and move the various custom enterprise OIDs to this OID tree | 客户推动 OID 规范化 = 把 Saga/SmartByte 写进自己运维体系 | `c921dc47fd9370bb` |
| 2025-03-27 | 来 | Frederik Kriewitz | we've PEN no. 44770 registered with IANA but for now we would prefer that you use your SmartByte PEN… Please use your standard Model Numbers | 坚持 SmartByte 原名/OID 的起点（Q-45） | `8f79a607c3cc831e` |
| 2025-09-10 | 来 | Frederik Kriewitz | we've a larger project where we need 230 Switches (1G SFP downlink, 10G uplinks)… Your old models didn't support fan monitoring/dual PSU status monitoring | 大项目需求 + 硬件监控要求 | `3c32c9ad46e6235d` |
| 2025-10-21 | 来 | Frederik Kriewitz | Demand: initial order 1000 units, after that 2000 units per year. It needs to be lite managed (only basic L2 features like vlans, etc.) | 未接住的年量需求（媒体转换器） | `61065505a331e5fd` |
| 2025-12-18 | 来 | Frederik Kriewitz | with this data update the OID was updated, working as expected now | 固件/MIB 迭代闭环 | `e2c8e6b4f49f56e3` |
| 2026-01-20 | 来 | Frederik Kriewitz | For the 230pcs project we used our existing supply because you initially quoted a long lead time | 交期丢单的原话 | `c24584352bd15931` |
| 2026-09-29 | 来 | Frederik Kriewitz | quote for 20 x STC-4168XGGCM switches (dual AC PSUs, same as last order)… Due to the price increase I'll have to get 3 more comparison quotes | 第 6 单 + 价格敏感度上升 | `afced0c9af361141` |
| 2026-10-15 | 来 | Frederik Kriewitz | payment has been made… We would prefer to have them with original SmartByte product names/IDs. Please make sure that the SmartByte and SNMP vendor OIDs are used | 较深绑定的最新证据 | `60ac95de9259a792` |

- **还缺的证据（等 A 邮箱 / Extra Info）**：A 邮箱无 NYNEX 往来（已核）；Peter 侧技术邮件在 S 邮箱抄送中，微信部分见 OCR 重建

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | fiberone.de（取自域名，公司全名待核） | 推断 |
| 国家 | 德国 | 事实（用户表）|
| 网站/域名 | fiberone.de / nynex.de | 事实（用户表 URL/邮箱域名） |
| 类型 | 运营商/ISP（终端 + 自有 logo 贴牌需求） | 推断（据兴趣/备注关键词） |
| 联系人 | Frederik Kriewitz / 已成单 | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | SFP MC 周边产品 自己的logo | 事实（用户表） |
| 用户备注（Remark） | 邮件中有详细的联系方式 | 事实（用户表） |
| 用户 AI 评估 | Claude 5% C；AI 35% B | 事实（用户表 AI评估结果/CALUDE评估结果列） |
| 所在清单 | A优质名单(其他优质欧洲客户)、AI评估(EU)·DONE、成交(PI)、Simon:活跃、Xtransfer | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

### 用户 AI / Claude 评估原文

- **Claude**（AI客户评估_EU 09.15.xlsx）：
  > 5% C
  > 德国区域性光纤宽带运营商（法兰克福/达姆施塔特地区），shop.fiberone.de为其面向终端用户的配套设备商城（FRITZ!Box路由器、光纤终端设备等），属ISP运营商旗下终端消费品商城；与交换机采购完全无关，非B2B采购目标
- **AI**（AI客户评估_EU 09.15.xlsx）：
  > 35% B
  > 德国网络配件分销商/电商，自有品牌logo，主营SFP、光纤收发器及周边产品，已有成单记录
  > 已成单客户，保持定期联系，推送新品SKU及PoE交换机产品线，尝试扩展品类合作
  > 8口PoE交换机、L2+管理型交换机
  > 已成单（说明信任基础已建立）；核心产品为SFP/MC周边（交换机为配菜）；德国客户对品质要求高但已有合作基础；有多个联系人可多线推进；扩品类有一定概率但非其主营

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-22）**　网站状态：在线
- **是谁**：德国达姆施塔特的光纤接入运营商品牌（NYNEX satellite OHG 旗下，11–50 人，2015 年起），在法兰克福/莱茵美因地区自建 FTTB/FTTH 网络（10G 对称），为楼宇提供千兆接入；B2B 提供专线、波长、楼宇网络。用户表：兴趣 SFP/MC 周边并要「自己的 logo」（贴牌），1 次实质回复，邮件中有详细联系方式。
- **类型**：运营商/ISP（终端 + 自有 logo 贴牌需求）
- **规模**：11–50 人（LinkedIn）
- **【官网】法人与品牌关系**
  > fiberONE — a brand of NYNEX satellite OHG … Robert-Bosch-Straße 20 64293 Darmstadt … Email: info@fiberone.de
  > 来源：https://fiberone.de/impressum/en/（抓取 2026-10-21）
- **【官网（新闻）】规模：数千套住宅接入，最大项目 1,100 套，自建 AON 网络**
  > Jüngster Meilenstein: die Wohnstadt Asemwald in Stuttgart, mit über 1.100 Wohnungen das bislang größte Projekt im Netz … 10 Gbit/s symmetrisch
  > 来源：https://fiberone.de/presse/（抓取 2026-10-21）
- **【第三方（LinkedIn）】11–50 人，2015 年**
  > Branche: Telekommunikation · Größe: 11–50 Beschäftigte · Hauptsitz: Darmstadt · Gegründet: 2015
  > 来源：https://de.linkedin.com/company/nynexfiberone（抓取 2026-10-21）
- **【注册/RIPE】Frederik Kriewitz = NYNEX satellite OHG 的 RIPE 联系人，地址与电话公开**
  > person: Frederik Kriewitz address: NYNEX satellite OHG Robert-Bosch-Str. 20 64293 Darmstadt Germany phone: +49 6151 50074-009 e-mail: f.kriewitz@nynex.de nic-hdl: NX123
  > 来源：https://ipinfo.io/AS200519/178.17.236.0/23（抓取 2026-10-21）
- **【官网】公司 2000 年创立、运营商 + 集成商、自有 AS62023**
  > NYNEX satellite OHG ist ein inhabergeführter Netzbetreiber und Systemintegrator aus Darmstadt, gegründet im Oktober 2000 von Andreas Buxbaum und Gunter Frank … in einem eigenen Netz mit eigenem autonomem System (AS62023)
  > 来源：https://nynex.de/leistungen.html（抓取 2026-10-21）
- **【官网】2026 年 26 周年并上线 nynex.ai；fiberONE 光纤自 2015 年**
  > Chronik der NYNEX satellite OHG, Darmstadt: VSAT-Netze seit 2000, Glasfaser mit fiberONE seit 2015, KI-Infrastruktur mit nynex.ai seit 2026
  > 来源：https://nynex.de/geschichte.html（抓取 2026-10-21）
- **【公开文件】Kriewitz 与 Frank 代表 NYNEX/fiberONE 署名政策意见书（决策层）**
  > Mit freundlichen Grüßen aus Darmstadt, Frederik Kriewitz/Gunter Frank NYNEX satellite OHG/fiberONE Darmstadt, 31. August 2025
  > 来源：https://bmds.bund.de/fileadmin/BMDS/Dokumente/Gesetzesvorhaben/NYNEX_Stellungnahme_Eckpunktepapier_fiberONE_BMDS_31-August-2025.pdf（抓取 2025-08-31）
- **【PI】成交单据 STSC20241121015（PI，2024-11-21）：STC-4168XGGCM、STC-424XGGM 共 2 台，USD 600.0；采购 SmartByte RMB 2350.0；Simon 成本表利润 RMB 1284.06**
  > 来源：PI.zip:15 德国 Frederik 活跃 Xtransfer 可发展/STSC20241121015.xls（抓取 2024-11-21）
- **【PI】成交单据 STSC20250915015（PI，2025-09-15）：STC-4168XGGCM 共 1 台，USD 420.0；采购 SmartByte RMB 1600.0；Simon 成本表利润 RMB 797.77**
  > 来源：PI.zip:15 德国 Frederik 活跃 Xtransfer 可发展/STSC20250915015.xls（抓取 2025-09-15）
- **【PI】成交单据 STSC-20260929-001（PI，2026-09-29）：STC-4168XGGCM 共 20 台，USD 6725.0**
  > 来源：PI.zip:15 德国 Frederik 活跃 Xtransfer 可发展/STSC-20260929-001.xlsx（抓取 2026-09-29）
- **【PI】成交单据 STSC-20260930-001（PI，2026-09-30）：STC-4168XGGCM 共 20 台，USD 5944.5**
  > 来源：PI.zip:15 德国 Frederik 活跃 Xtransfer 可发展/STSC-20260930-001.xlsx（抓取 2026-09-30）
- **【PI】成交单据 STSC20261006015（PI，2026-10-06）：STC-4168XGGCM 共 20 台，USD 5944.5；采购 SmartByte RMB 34000.0；Simon 成本表利润 RMB 5000**
  > 来源：PI.zip:15 德国 Frederik 活跃 Xtransfer 可发展/STSC20261006015.xlsx（抓取 2026-10-06）
- **【PI】PI 包文件夹「德国 Frederik 活跃 Xtransfer 可发展」：Simon 标签 活跃，收款 Xtransfer；单号 5 个，2024-11-21 → 2026-10-06，销售 USD 19634.0 / RMB 0，Simon 成本统计利润合计 RMB 7081.83**
  > 来源：PI.zip:15 德国 Frederik 活跃 Xtransfer 可发展（抓取 2026-10-22）
- **【Gmail 往来（S 邮箱）】合规审查：NYNEX 测试 LT-S8328XG 时发现 SmartByte 通用 MIB 内含 3 家其他 OEM 客户/品牌的企业 OID（.57430 Dongguan Huarong、.56813 Fuzhou Dockeer、.171 D-Link），要求说明 Saga 与 SmartByte 关系以报备合规部门；SmartByte 承认「忘了删其他 OEM 客户的 OID」，并提出按客户自有 OID 定制固件；NYNEX 自有 IANA PEN 44770，但要求 SmartByte 先申请自己的 PEN 并把私有 OID 迁到自己的树下，还追问 OEM 数据（产品 ID / PEN 前缀 / logo）是写死在固件还是独立 OEM 配置分区**
  > The MIB enterprise IDs (.1.3.6.1.4.1.57430.* and .1.3.6.1.4.1.56813.* and .1.3.6.1.4.1.171.*) are registered to two other companies … How is smart bytes/saga telecom related to these companies? … Can you please request your own SmartByte SNMP enterprise OID at https://www.iana.org/assignments/enterprise-numbers/ … Is the OEM data like the product ID, SNMP PEN prefix, company logo, etc. hardcoded in the firmware (separate firmware file for each OEM)?
  > 来源：data/gmail_s/messages/2025/2025-03.jsonl（主题 RE: Testing Feedback，f.kriewitz@nynex.de ↔ peter@smartbyte.com.cn，抄 S 邮箱）（抓取 2025-03-27）
- **【S 邮箱原文】2026-09-29 NYNEX 询价 20 × STC-4168XGGCM（双 AC 电源，同上次订单）含运到德国；Simon 当日答材料涨价（PCB / RAM）、汇率 6.71、可 EUR 结算**
  > can you please share a quote for 20 x STC-4168XGGCM switches (dual AC PSUs, same as last order) including shipping to Germany.
  > 来源：（S 邮箱 key afced0c9af361141，2026-09-29T13:36Z；回信 key 38d19aa9fadaae82）（抓取 2026-10-22）
- **【S 邮箱原文】2026-09-30 Simon 报最终价：2,015 RMB/台 = 300 USD（1:6.71）= 265.2 EUR（1:7.6）；交期 3 周 / 15 个工作日（下单后起算）；客户称因涨价需再找 3 家比价**
  > Best offer is 2015RMB/PC USD offer: 300USD/PC … EUR offer: 265.2EUR/PC … Production time: 3 weeks, it is 15 working days. AFTER the order is confirmed!
  > 来源：（S 邮箱 key 074a700ad4b10bf7，2026-09-30T05:50Z）（抓取 2026-10-22）
- **【S 邮箱原文】2026-10-06 NYNEX 要欧元账户 → Simon 发 invoice + 银行确认（同一账户收 USD / EUR）；2026-10-15 NYNEX 付款并要求成品用 SmartByte 原始产品名 / ID 与 SmartByte SNMP 厂商 OID；Simon 同意「let's do SmartByte information」；2026-10-17 确认收款、投产**
  > payment has been made (see attachment). One additional note: We would pfeffere to have them with original SmartByte product names/IDs. Please make sure that the SmartByte and SNMP vendor OIDs are used.
  > 来源：（S 邮箱 key 60ac95de9259a792 / 81f8fe275f461480 / 95b7153bc20857f6，2026-10-15～17）（抓取 2026-10-22）
- **【GitHub 公开仓库】Frederik Kriewitz 本人是 LibreNMS 贡献者：PR #18681「Add support for SmartByte OS」2026-01-11 合并，sysObjectID .1.3.6.1.4.1.56166，测试夹具用 Saga 的 STC-4168XGGCM V1.1（序列号 202509160001 = 2025-09 那单）→ NYNEX 用 LibreNMS 纳管 Saga 交换机，并替 Saga/SmartByte 做了上游适配；其 2026-10-15「必须用 SmartByte OID」的技术原因即在此**
  > @copyright 2025 Frederik Kriewitz / @author Frederik Kriewitz <frederik@kriewitz.eu> … sysDescr: Product STC-4168XGGCM V1.1 Version hotfix/7.4.7 (r1540 af525c9)
  > 来源：https://github.com/librenms/librenms/pull/18681 ；LibreNMS/OS/Smartbyte.php；tests/data/smartbyte_stc-4168xggcm.json（抓取 2026-10-22）
- **【GitHub 公开仓库】Kriewitz 还向 Oxidized（开源配置备份）提交了 smartbyte 模型（2026-01-23 合并，测试数据同为 STC-4168XGGCM 7.4.7）→ NYNEX 用 LibreNMS + Oxidized 两套工具把 Saga 交换机当长期在网设备运维**
  > smartbyte: new model for SmartByte switches — Frderik Kriewitz, 2026-01-23；spec/model/data/smartbyte#STC-4168XGGCM_7.4.7#output.txt
  > 来源：https://github.com/ytti/oxidized/blob/master/lib/oxidized/model/smartbyte.rb（抓取 2026-10-22）
- **【S 邮箱原文 + GitHub 对齐】LibreNMS 支持的来龙去脉：2025-02-11 测试反馈（无 PSU/风扇/温度监控、SNMP 基础、缺 LLDP-V2-MIB/DDM，选 BDCOM S2900）→ 2025-12-10 指出固件企业号=0、旧固件为 57430（Fuzhou Dockeer）→ 2025-12-17 Simon 发修复固件 hotfix/7.4.7 r1540（OID=56166）→ 12-18 确认生效 → 12-19 Frederik 开 LibreNMS PR #18681（2026-01-11 合并，26.1.0 发布）。show version 显示 System MAC fc:cd:2f:d0:4f:db（SmartByte MA-M 块内）、PID STC-4168XGGCM V1.1、SN 202509160001**
  > Vendor OID is still 0 … System MAC Address: fc:cd:2f:d0:4f:db PID: STC-4168XGGCM, Hardware Version: V1.1, Serial Number: 202509160001 … Thank you, with this data update the OID was updated, working as expected now.
  > 来源：data/gmail_s/messages/2025/2025-12.jsonl（f.kriewitz@nynex.de 2025-12-10 / 12-17 / 12-18）+ https://github.com/librenms/librenms/pull/18681（抓取 2026-10-22）
- **【S 邮箱原文（三方线程）】Peter（SmartByte）2025-03-26 书面向 NYNEX 说明关系：SmartByte 是 OEM/ODM 工厂，Saga 是其欧洲市场的代表伙伴，今后要买 SmartByte 产品「contact Simon directly」；Frederik 2025-03-25 称要向 compliance department 报备；2025-03-27 NYNEX 自有 PEN 44770 但选择用 SmartByte PEN 并要求用 SmartByte 标准型号**
  > Saga Telecom is our partner who represent SmartByte to promote SmartByte's products all over the Europe market. If you are interests in SmartByte's products in future, you can contact Simon directly.
  > 来源：data/gmail_s/messages/2025/2025-03.jsonl（peter@smartbyte.com.cn 2025-03-26；f.kriewitz@nynex.de 2025-03-25/27）（抓取 2025-03-26）
- **【微信 OCR（Simon↔Peter 2024-11-15）】NYNEX 首次询问时自述有 SONiC 移植经验（Broadcom），问 Marvell 芯片/CPU/内存与软件是否自研；Peter 答平台 Marvell 98DX336S / Flash 512M / DRAM 512M / ARM v7 800M、软件自研；100G 为 Aldrin2/Falcon 但系他客户 NDA 定制不卖；双 AC 样品机壳 +200 RMB**
  > We've some experience with porting the open source SONiC network operation system to Broadcom devices. As there's some basic marvel support it might be easy to add support for your hardware.
  > 来源：data/wechat_smartbyte_ocr/Weixin Image_2026-10-20_140337_791.txt（抓取 2024-11-15）
- **【Simon 口述】绑定等级：较深绑定——客户把 SmartByte/Saga 设备写进了自己的运维工具链（freddy36 向 LibreNMS / Oxidized 提交 SmartByte 支持），切换成本高**
  > 尤其是德国那个 我让你爬了它的github 它提交了很多信息 这就是比较深一些的绑定了。客户很难换或者换了成本极高 这就是较深绑定
  > 来源：docs/requirements/对话全记录.md § T29-U28（抓取 2026-10-23）
- **【Simon 文档】绑定等级（文档当时）：轻度绑定——「SmartByte 也背书了」；2026-10-23 Simon 口述升为较深（GitHub 提交 LibreNMS/Oxidized 支持）**
  > 德国 Frederik　轻度绑定 = Smartbyte也背书了
  > 来源：Extra Info.zip 根目录《客户绑定情况分析.docx》（data/extra_info_2026-10/text/Extra_Info__客户绑定情况分析.docx__6d196b92.json）（抓取 2026-10-22）
- **KP**：Frederik Kriewitz（Systems Engineer / 网络负责人（RIPE 联系人、政策文件署名人；成单联系人））f.kriewitz@nynex.de +49 6151 50074-009〔https://ipinfo.io/AS200519/178.17.236.0/23 + 用户表〕
- **KP**：Gunter Frank（创始人/合伙人（1999/2000 创立）） 〔https://nynex.de/company/〕
- **调研后定级**：A（原自动 A）——PI 包成单客户，Simon 标签 活跃 → A
- 备注：A 维持：运营商持续采购楼宇接入交换机（48 口/L2+/2.5G 上联）与贴牌 MC/SFP；P1 改 STC-448XGGPM 或 STC-424XGGPM-280W（10G 上联）。
【2026-10-22 复盘补】NYNEX 2025-03 的 SNMP/MIB 合规追问是「工程型缓冲层」的真实考题：欧洲客户会用 snmpwalk 核 OID 归属。Saga 应自己申请一个 IANA PEN（免费、在线表单、约 1–2 周）并要求 SmartByte 在 Saga 版固件里只保留 Saga PEN 下的私有 MIB；给 NYNEX/德国客户的 OEM 说明要能回答「OEM 数据是固件内写死还是独立配置分区」。对应 Q-35。 ｜ 针对性加厚 2026-10-22（S 邮箱 2026-09/10 第 6 单，T29-U13 ②） ｜ 【Simon 2026-10-22 口径】NYNEX 由 Peter 技术跟进、只能在 Saga 下单；宣传 SmartByte 品牌是合作约定 → 之前「Saga 自申 PEN」建议作废。维护计划见 docs/成单客户_NYNEX_维护计划_2026-10-22.md ｜ 【2026-10-22T15:48Z】GitHub 监控上线（宪法第九条）：scripts/github_watch/watch.py，每轮必跑，变化见 data/github_watch/变化日志.md

### 加厚挖掘（2026-10-21 · 深挖 v1）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | NYNEX satellite OHG（品牌 fiberONE） |
| 成立 | 2000-10（Andreas Buxbaum 与 Gunter Frank 创立）；fiberONE 光纤业务 2015 年起 |
| 总部/地址 | Robert-Bosch-Str. 20, 64293 Darmstadt, Germany |
| 人数 | 11–50（LinkedIn） |
| 注册/税号 | RIPE：AS62023（NYNEX），IP 段 NYNEX-fiberONE；联系人句柄 NX123 = Frederik Kriewitz |
| 股权/集团 | 自有网络运营商 + 系统集成商（VSAT、光纤、IP 中转）；2026 年新增 nynex.ai 自建 AI 基础设施 |
| 其他 | 2025-08-31 以 NYNEX/fiberONE 名义向德国联邦数字部提交 TKG 修法意见书（Kriewitz/Frank 署名） |

- **业务线**：VSAT 卫星网络（Ku/Ka）；fiberONE：法兰克福/莱茵美因 FTTB/FTTH 自建网，楼宇千兆/10G 对称接入；B2B 专线、波长、楼宇网络；IP 中转/自有 AS；nynex.ai（2026 起）

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| fiberONE（自有 logo 需求） | 楼宇接入侧 SFP / MC / 接入交换机 | 用户表：兴趣 SFP、MC 及周边并要「自己的 logo」；FTTB 楼宇侧需要带 SFP 上联的小口数 PoE/非 PoE 接入机 | STC-28DGGPM | https://fiberone.de/（用户表 + 2026-10-21） |

- **触达通道（公开）**：直邮: f.kriewitz@nynex.de（RIPE 公开，成单联系人）/ m.kopp@nynex.de / s.valaei@nynex.de（用户表）；电话: +49 6151 50074-009（RIPE 公开）；网站: https://fiberone.de/ · https://nynex.de/；LinkedIn: https://de.linkedin.com/company/nynexfiberone
- **近况信号**：
  - 2025-08-31：Kriewitz/Frank 署名提交 TKG 修法意见书——Kriewitz 为公司决策层之一（https://bmds.bund.de/…/NYNEX_Stellungnahme_Eckpunktepapier_fiberONE_BMDS_31-August-2025.pdf）
  - 2026-10：公司 26 周年，上线 nynex.ai 自建 AI 基础设施，品牌族 nynex.de/fiberONE/nynex.ai 完整（https://nynex.de/geschichte.html）
  - 用户表：已成单（Frederik Kriewitz），要自有 logo
  - 2026-01-11：Frederik Kriewitz 向 LibreNMS 提交并合并 SmartByte OS 支持（PR #18681），测试机为 Saga STC-4168XGGCM —— 客户在为供应商做上游生态适配，是深度绑定信号；跟进时可致谢并提供 MIB 更新 / 新机型 snmprec
  - 2026-10-22 GitHub 全量盘点（data/github_watch/）：freddy36 共 89 个 PR / 17 个 issue；网管相关 PR 揭示 NYNEX 在用/测过的设备：BDCOM（2024-04→2026-01，含 FS 贴牌 BDCOM）、FS 贴牌 Centec（LibreNMS #16175 2024-07）、Centec CNOS（Oxidized #2023 2020-01、#3892「CNOS: improve support」2026-08-19 合并 2026-09-22 → 2026 年仍在部署 Centec 设备）、Fiberstore S3900（2019/2024）、Edge-Core EdgeCOS（2019→2026-01）、GCOM BNPS（2017）、Mellanox（2020）、NUT/APC UPS、Checkmk（自有仓库 check_mk_extensions ★12）。SmartByte 相关：LibreNMS #18681（2025-12-19→2026-01-11）、#18856 fix opticalVoltage（2026-01-23）、Oxidized #3734（2026-01-23→02-13）。
  - 2026-10-22：他在 LibreNMS #18955（FS S3410 = FS 贴牌 Ruijie，2026-01-30→02-24）里以审阅者身份指导别人 → 他是 LibreNMS 社区里 FS.com（Fiberstore）贴牌设备的权威；NYNEX 大量采购 FS.com（欧洲仓、现货）—— 2026-01「230 台因交期给了现有供应商」的现有供应商很可能就是 FS.com 系。
  - 2026-10-22：GitHub star/following 画像：2024-09 star krusic22/SFP-Transceiver-Flashing（改写 SFP EEPROM/厂商锁 → 他们自己刷光模块兼容码，Saga 供 SFP 时要给可编码/不锁码的）；2026-03 star denog/denog-wg-access（DENOG 德国运营商社区成员）；star rtbrick/bngblaster、inex/IXP-Manager、snabb、trex；following bisdn（白盒 NOS 厂商）。近 90 天公开事件仅 1 条（2026-09-22 Oxidized PR 合并）。
  - Simon 2026-10-22（T29-U16）决定：CENTEC 线自己想办法；备货与 Peter 私下谈；7.5 固件出货前确认；备件 OK；授权书不主动提（客户提再说）；「欧洲代理」只是说辞，Saga 体量不是总代。
- **风险/边界**：运营商自建网 → 对设备稳定性与固件（VLAN/QinQ/IGMP）要求高，需提供管理型固件说明；自有 logo = OEM 30% 档，但 ISP 采购对价格敏感，首单可按 25% 项目档试探；【2026-10-22 第二遍复盘 F11】第 6 单（20 × STC-4168XGGCM，2026-10-15 付款、10-17 投产）成交单价 2,015 RMB/台，**低于《价格主表》该型号 SmartByte 未税 CNY 2,100**（即三档公式的基数）；PI 包 5 单合计利润 7,081 RMB / USD 19,634 ≈ 5% —— 与「+20/25/30%」规则冲突，两者都保留：要么 SmartByte 对 Saga 的实际进价低于 2024-05 价目表，要么 Saga 对老客让利到贴本。客户最终选择 SmartByte 原名 + SmartByte OID（放弃 Saga 贴牌），对「Saga 品牌」定位是一个真实反馈。
- **Saga 对位结论**：P1 STC-28DGGPM（30% 档）——FTTB 楼宇接入：8 口千兆 + 2 SFP 管理型（可贴 fiberONE logo）是楼层/地下室接入的标准位；配 STI-110GE 千兆 MC 作单户光电转换；SFP 由 Saga 配套供货
- **邮件切入句（英文）**：For the FTTB building side the 8-port gigabit unit with two SFP uplinks is the one we already ship under customer logos, so I am quoting it in fiberONE neutral packing together with the gigabit media converter you took before.

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://fiberone.de/　语言：de　站点地图 URL 数：49
- **标题**：Internetanbieter Rhein-Main â Glasfaser bis 10 Gbit/s / fiberONE
- **描述**：Internetanbieter Rhein-Main: Glasfaser symmetrisch bis 10 Gbit/s, unter 1 ms zum DE-CIX, keine Drosselung. Ab 30 â¬/Monat inkl. MwSt. bei 24 Monaten Laufzeit.
- **首页栏目**：Home Speed Home Â® Lichtgeschwindigkeit, wo du zu Hause bist. / Kein geteiltes Kupfer. Deine eigene Faser. / Symmetrisch in beide Richtungen / Keine Drosselung, kein Limit / Licht statt Strom / Dein eigener Laser. Deine eigene Leitung. / Upload und Download im direkten Vergleich / NÃ¤her am Internet geht nicht.
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：fiber 59、ftth 5、10g 4、ethernet 1、gigabit 1、2.5g 1、wifi 1、ubiquiti 1
- **站内出现的品牌**：Bosch　（「（！）」= Saga 自家/供应商品牌已在其站内出现）
- **站内型号串**（正则抽取，含非交换机）：PIB-1G-24, PIB-5G-24, PIB-2, PIB-10G-24
- **站内公开邮箱**：datenschutz@fiberone.de, dne4@fiberone.de, info@fiberone.de
- **已抓子页**：[Produktinformationsblatt â fiberONE 1G â 24 Monate](https://fiberone.de/dokumente/produktinformationsblaetter/pib-fiberone-1g-24m.html)；[Produktinformationsblatt â fiberONE 5G â 24 Monate](https://fiberone.de/dokumente/produktinformationsblaetter/pib-fiberone-5g-24m.html)；[Produktinformationsblatt â fiberONE 2,5G â 24 Monate](https://fiberone.de/dokumente/produktinformationsblaetter/pib-fiberone-25g-24m.html)；[Produktinformationsblatt â fiberONE 10G â 24 Monate](https://fiberone.de/dokumente/produktinformationsblaetter/pib-fiberone-10g-24m.html)；[Kontakt â fiberONE / Beratung, Wohnungswirtschaft & GeschÃ](https://fiberone.de/kontakt/)
- 首页正文摘录：fiber ONE Tarife Wohnungswirtschaft GeschÃ¤ftskunden Support Shop DE EN ä¸­æ VerfÃ¼gbarkeit prÃ¼fen â° Glasfaser Home Speed Home Â® Lichtgeschwindigkeit, wo du zu Hause bist. Glasfaser-Internet bis 10 Gbit/s â deine eigene Faser, dein eigener Anschluss Maustaste gedrückt halten — und die Photonen in den Warp schicken In Frankfurt steht einer der grÃ¶Ãten Internetknoten der Welt â wir legen ihn dir bis vor den
- 数据文件：`data/saga_clients/site_snapshots/SA-013.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 2 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2024-11-09 | 2024.11.9 | 群发了48口引流管理 | 非PoE, 全光，100G | Email |  | 其他优质欧洲客户 2.26.xlsx#12 |
| 2025-05-29 | 2025.5.29 | alarm |  | S |  | 其他优质欧洲客户 2.26.xlsx#12 |

## 成交记录（PI 包 · 自动汇总）

- **Simon 的标签**（PI 包文件夹名）：**活跃**　|　收款：Xtransfer　|　买方抬头：NYNEX satellite OHG
- **单号** 5 个（2024-11-21 → 2026-10-06）　|　**销售** USD 19,634　|　**Simon 成本表利润** RMB 7,082

| 单号 | 日期 | 单据 | 型号 | 数量 | 金额 | 采购（卖方 / RMB） | Simon 成本表（成本 / 收款 / 利润 RMB） |
|---|---|---|---|---|---|---|---|
| STSC20241121015 | 2024-11-21 | PI | STC-4168XGGCM、STC-424XGGM | 2 | USD 600.0 | SmartByte / 2350.0 | 3051.04 / 4335.1 / 1284.06 |
| STSC20250915015 | 2025-09-15 | PI | STC-4168XGGCM | 1 | USD 420.0 | SmartByte / 1600.0 | 2172.38 / 2970.15 / 797.77 |
| STSC-20260929-001 | 2026-09-29 | PI | STC-4168XGGCM | 20 | USD 6725.0 | — | — |
| STSC-20260930-001 | 2026-09-30 | PI | STC-4168XGGCM | 20 | USD 5944.5 | — | — |
| STSC20261006015 | 2026-10-06 | PI | STC-4168XGGCM | 20 | USD 5944.5 | SmartByte / 34000.0 | 39000 / 44000 / 5000 |

> 口径：同一单号多份文件取 CI > PI（最新修订）> Quotation；Quotation 行不计入销售合计；明细见 `data/pi_orders/销售单据明细.csv`、采购价见 `采购合同明细.csv`；原件在 Release `files-pi_2026-10`。

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：104 封（去 59 / 来 45）　|　**期间**：2024-11-09 → 2026-10-17　|　**最后去信**：2026-10-17
- **对方邮箱**：f.kriewitz@nynex.de、info@fiberone.de
- **最后一封来信**：2026-10-15 f.kriewitz@nynex.de「Re: Saga Marvell AC5 Series Fully Ready」：Hello Simon, payment has been made (see attachment). One additional note: We would pfeffere to have them with original SmartByte product names/IDs. Please make sure that the SmartByte and SNMP vendor OIDs are used. Best Regards Frederik Kriewitz NYNEX satellit
- **邮件里报过的价**：2026-09-30 $300；2025-11-15 $265；2025-11-15 $300；2025-10-22 $25；2025-10-22 $35；2025-10-22 $30；2025-09-15 $265；2024-11-21 $265

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Saga Marvell AC5 Series Fully Ready | 2026-08-26 | 2026-10-17 | 4 | 6 | 12 |
| Marvell Alleycat5 Solution | 2025-06-23 | 2026-06-22 | 16 | 25 | 50 |
| Marvell Industrial Alert System | 2025-05-29 | 2025-05-29 | 0 | 1 | 1 |
| Testing Feedback | 2025-02-06 | 2025-04-01 | 12 | 11 | 45 |
| 48 Port PoE Managed Switch | 2024-11-09 | 2025-01-06 | 12 | 17 | 48 |
| [NX#10565698] RE: 48 Port PoE Managed Swit [...] | 2024-11-09 | 2024-11-09 | 1 | 0 | 0 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：成单精选层　|　**自动源**：7 个　|　**数据截至**：2026-10-23T06:51:07Z　|　**最近变化**：2026-10-23T06:51:07Z
- **最近变化摘要**：2026-10-23 auto_home：内容变化：+4 −23 行
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SA-013/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [nynex_home](https://www.nynex.de/) | html | HTTP 200 | 2026-10-23T02:54:23Z | 6753 字符；首行：NYNEX – Expand your business. We connect it. · Satellit, Glasfaser & IP-Transit |
| [fiberone_home](https://www.fiberone.de/) | html | HTTP 200 | 2026-10-23T06:51:07Z | 21974 字符；首行：Internetanbieter Rhein-Main – Glasfaser bis 10 Gbit/s \| fiberONE |
| [peeringdb](https://www.peeringdb.com/api/net?asn=200519) | json | HTTP 200 | 2026-10-23T02:54:23Z | data.0.name="fiberONE.de"; data.0.info_prefixes4=0; data.0.info_prefixes6=0; data.0.update |
| [auto_home](https://fiberone.de/) | html | HTTP 200 | 2026-10-23T06:51:07Z | 21974 字符；首行：Internetanbieter Rhein-Main – Glasfaser bis 10 Gbit/s \| fiberONE |
| [auto_sitemap](https://fiberone.de/sitemap.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 49 个 URL；最新 lastmod - |
| [auto_news_1](https://fiberone.de/news/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 1513 字符；首行：News — fiberONE \| Aktuelles aus dem Glasfaser-Ausbau |
| [auto_news_2](https://fiberone.de/referenzen/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 2169 字符；首行：Referenzen — fiberONE \| Glasfaser in Frankfurts Türmen & Quartieren |

- **人工定期看（登录墙，不自动抓）**：GitHub freddy36 → scripts/github_watch（每轮必跑）

## 联系方式（已有 · 原值照录）

- 邮箱：`f.kriewitz@nynex.de`〔企业邮箱；来源：用户表原值〕
- 邮箱：`m.kopp@nynex.de`〔企业邮箱；来源：用户表原值〕
- 邮箱：`s.valaei@nynex.de`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Frederik Kriewitz / 已成单
- 网站/域名：fiberone.de
- 网站/域名：nynex.de
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Frederik Kriewitz | Systems Engineer / 网络负责人（RIPE 联系人、政策文件署名人；成单联系人） | f.kriewitz@nynex.de / +49 6151 50074-009 | 调研核实（公开页） | https://ipinfo.io/AS200519/178.17.236.0/23 + 用户表 |
| Gunter Frank | 创始人/合伙人（1999/2000 创立） | — | 调研核实（公开页） | https://nynex.de/company/ |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:fiberone.de`, `d:nynex.de`, `e:f.kriewitz@nynex.de`, `e:m.kopp@nynex.de`, `e:s.valaei@nynex.de`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/DONE/其他优质欧洲客户 2.26.xlsx#总表:13 | 12 | https://shop.fiberone.de/collections/all | 德国 | Frederik Kriewitz<br>已成单 | 谷歌 | SFP MC 周边产品 自己的logo | f.kriewitz@nynex.de<br>m.kopp@nynex.de      Marcel Kopp<br>s.valaei@nynex.de     Saffa Valaei | 邮件中有详细的联系方式 | 2 条 |
| AI客户评估/DONE/AI客户评估_EU 09.15.xlsx#总表:6 | 5 | https://shop.fiberone.de/collections/all | 德国 | Frederik Kriewitz<br>已成单 | 谷歌 | SFP MC 周边产品 自己的logo | f.kriewitz@nynex.de<br>m.kopp@nynex.de      Marcel Kopp<br>s.valaei@nynex.de     Saffa Valaei | 邮件中有详细的联系方式 | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：FTTB 楼宇接入：8 口千兆 + 2 SFP 管理型（可贴 fiberONE logo）是楼层/地下室接入的标准位；配 STI-110GE 千兆 MC 作单户光电转换；SFP 由 Saga 配套供货 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（运营商/ISP（终端 + 自有 logo 贴牌需求）） |
| 备选2 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $151.6 USD EXW（30% 档，SmartByte LT-IS6310GP-2GX8GT 780 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $196.3 USD EXW（30% 档，SmartByte LT-S8328XGP-4XS24GT-S 1010 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM），备选型不进首触。

- **第 1 次**：老客户回访——问上次所购型号的使用情况 + 告知 Marvell 新款（STC-28DGGPM）；只问一个问题：当前在采购的主力型号与月量。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有成交史，信任与开户成本已付；有 1 次实质回复（对方认识我们）；欧洲主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STC-28DGGPM 按 30% 档报价，做现供应商的第二货源；规模（调研）：11–50 人（LinkedIn）
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
| 采购量/预算 | ✅ 有成交史（量待确认） |
| 商业资格结论 | **技术上合格 / 商业上有互动证据（成交或实质回复或面谈）→ 值得长期跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STC-28DGGPM - 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks (Marvell-based, neutral label)

```text
Hi Frederik,

Thank you again for your earlier order with us - this is a short update rather than a cold mail. For the FTTB building side the 8-port gigabit unit with two SFP uplinks is the one we already ship under customer logos, so I am quoting it in fiberONE neutral packing together with the gigabit media converter you took before.

We supply a Marvell-based 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks - model STC-28DGGPM - that fits the same slot as your fiberONE（自有 logo 需求） 楼宇接入侧 SFP / MC / 接入交换机 at a lower landed cost, and we can ship it with neutral packaging. Current price: $87.4 USD EXW (price snapshot 2026-10-17, valid 15 days).

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

- 2026-10-24：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 A，分数 112）

---

*建档日期：2026-10-24　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
