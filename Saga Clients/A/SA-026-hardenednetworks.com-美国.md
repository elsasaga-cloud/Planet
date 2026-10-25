# hardenednetworks.com
**官方名称（调研核实）**：Hardened Networks / ITS Express（hardenednetworks.com · expresssupply.net，US）

> **评级 A**　|　美国　|　档案编号 `SA-026`　|　优先级 ★★★　|　状态：有回复·跟进中
>
> **类型**：品牌商/贴牌需求（OEM/ODM）——ITS 加固交换机自有品牌（推断）　|　**历史关系**：实质回复 3 次；推送 10 次（2024-05-07 → 2025-03-03）　|　**所在清单**：A优质名单(US)　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SA-026
rating: A
rating_auto: A
name_official: "Hardened Networks / ITS Express（hardenednetworks.com · expresssupply.net，US）"
score: 84
country: 美国
region: 北美
website: hardenednetworks.com
type: 品牌商/贴牌需求（OEM/ODM）——ITS 加固交换机自有品牌
tier_tags: ["A优质名单(US)"]
deal: no
replies: 3
followups: 10
first_contact: 2024-05-07
last_contact: 2025-03-03
s_mail: 29 msgs (out 21 / in 8), 2024-05-07 -> 2026-02-12
p1: STI-288DGGPM
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-21
sources: 1
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：美国交通 ITS 领域的自有品牌加固交换机供应商（HN-8012-24 V3、HN-AIS-8300、80 系列 V3：L3 OSPF/BGP、4×USFP+ 10G、ESFP 2.5G 等），与 ITS Express 同一体系；产品页 2026-07 仍在更新。用户表：3 次实质回复，兴趣工业 FS / 工业 MC / Bypass，用自己的 logo。（调研 2026-10-21；表内兴趣：工业FS 工业MC Bypass  自己的logo）
- **为什么是 A 级**：+30 实质回复 3 次（问价/要资料/问型号等）；+6 在 A/DONE 优质国家名单（已做过整轮推送）；+12 自有品牌/贴牌需求（OEM/ODM 首选客户类型）；+8 兴趣在交换机/PoE/工业/MC 等 Saga 主线；+10 有企业邮箱；+5 有可核实的公司网站/域名；+8 区域 北美/美国；+5 最近活动 2025
- **历史互动**：实质回复 3 次；推送 10 次（2024-05-07 → 2025-03-03）；最近一次客户回复：2025-03-03：只用博通方案
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：CENTEC 全 L3：他 2024-05-09 要的「1U full L3，24 铜 + 8 光 + QSFP+ 上联」= STH-2QX4DX24GE-HSI（24×1G + 4×25G SFP28 + 2×40G QSFP+，OSPF/BGP/MPLS/VXLAN，双热插拔 PSU；仓内无价 Q-54）；10G 汇聚另有 STH-2C24XF-HSI（2026-06 对 FiberX 报 $1,250 含 MA 许可；群发 $1,500）——仅当 Mark 对 Broadcom 松口 — C 层：不为单一客户开第四条芯片线；只问一次「Broadcom 是否写进客户规格」。已打开的主题（16/21 封有打开记录）：「Re: 48 Port SFP Switch」(2025-02-10)、「Marvell Alleycat5 Solution」(2025-03-03)、「Re: Marvell Alleycat5 Solution」(2025-04-28)、「Marvell Industrial Alert System」(2025-12-29) → 读者兴趣偏「10G 汇聚/L3」；当前 P1 属「DC 核心/CENTEC」，下一封按「10G 汇聚/L3」给，不按 P1｜已发资料（勿重发）：DIN Power Adapter(2024-07-30)、Marvell Based CLI Manual(2025-01-27)、Marvell Based Web Manual(2025-01-27)、STC-448XGGPM(2025-01-27)、STC-4816XGCGM(2025-01-28)、Product Link_2026Q2(2026-02-12)；还没给过：7.5 Feature List、Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）｜需求台账 #13/#1：2024-05 的「不可用」现在可用（STH1G），一句话补上；价按 Q-54「按数量报」；CENTEC 线按 ≥35% 底线（E1）与 30% 表价取高者
- **第一问（只问一个）**：Mark — in May 2024 you asked for a 1U full-L3 unit with 24 copper + fiber + QSFP+ uplinks and I had nothing; today that is STH-2QX4DX24GE-HSI on our CENTEC line (24×1G + 4×25G SFP28 + 2×40G QSFP+, OSPF/BGP/MPLS). Is Broadcom written into your customers' ITS specs, or would it qualify if it clears your lab test?
- **最大未知**：年走量与现供应商
- **下一步**：2026-11（一次） A 邮箱 → mark@expresssupply.net 一句话问 Broadcom 是客户规格硬条款还是偏好；若偏好 → 付样 1 台 CENTEC

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SA-026` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未绑定（边界户：芯片线；Elsa 箱：`to:hardenednetworks.com OR to:expresssupply.net` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 21 / 来 8）（第 74 批(g)））** ｜ 类型：美国 ITS 自有品牌加固交换机（HN 系列）+ Juniper/Fortinet 代理；Mark Schulting——第一档 OEM 类型 ｜ 筛子：2（给过精确规格：32 口全 L3 1U 8 光 24 电 + QSFP+；「all 10 gig fiber… buying in bulk」） ｜ 停点：Broadcom 芯片硬要求（2025-02-05 / 03-03 / 04-28 三次「I need a broadcom chipset」）；Saga 线 = Marvell / CENTEC / Realtek；Simon 2025-02-10 转报两款 Broadcom 全光（1,000 / 4,000 USD）无回音；Alan 2025-04-28「we focus on Marvell… Broadcom is for high-end market only」 ｜ 复活：只有 Mark 接受 CENTEC 全 L3（OSPF/BGP/MPLS/VXLAN）——Alan 2026-01-16 的 CENTEC 推介无回复；Saga 无 Broadcom 货源 ｜ 通路：US ｜ 节奏：2024-05 → 2026-02 去信 21 封；最后来信 2025-04-28 ｜ 证据：k=d0066f467b2afcd7 / 185a3765640a0e3f / 5f00be3e081f8769 / 898769c94b9fc197 / eb80eea25e1a3bb5 / e8d9d485eebf828f / 231c410bdb6b62d3；第 19 批回补来信原文 3 条（gmail_s/gmail_a）
- **现状一句话**：Mark 是少数主动说「buying in bulk」的美国品牌商：2024-05 要 32 口全 L3 机架（8 光 24 电 + QSFP+），2025-01 看中 12 光 24 电款要规格书、问「all 10 gig fiber 1g/2.5g/10g」，然后连问三次 Broadcom。Simon 先给 CENTEC（「a good domestic brand」）、再临时找了两款 Broadcom 全光报 1,000/4,000 USD，Alan 最后定调「we focus on Marvell」。2026-01 Alan 再推 CENTEC 核心机，无回。
- **对方真实需求（有据）**：全 L3 10G 光口交换机（批量），芯片 Broadcom；ITS 加固。
- **断点 / 为什么停在这里**：芯片线边界（概念层 C 系列）。Saga 曾为他破例找 Broadcom 货源，又收回——口径摇摆比拒绝更伤。
- **Saga 现在该推什么**：P1 **CENTEC 全 L3：他 2024-05-09 要的「1U full L3，24 铜 + 8 光 + QSFP+ 上联」= STH-2QX4DX24GE-HSI（24×1G + 4×25G SFP28 + 2×40G QSFP+，OSPF/BGP/MPLS/VXLAN，双热插拔 PSU；仓内无价 Q-54）；10G 汇聚另有 STH-2C24XF-HSI（2026-06 对 FiberX 报 $1,250 含 MA 许可；群发 $1,500）——仅当 Mark 对 Broadcom 松口**（30% 档，CENTEC 线按 ≥35% 底线（E1）与 30% 表价取高者）——C 层：不为单一客户开第四条芯片线；只问一次「Broadcom 是否写进客户规格」。已打开的主题（16/21 封有打开记录）：「Re: 48 Port SFP Switch」(2025-02-10)、「Marvell Alleycat5 Solution」(2025-03-03)、「Re: Marvell Alleycat5 Solution」(2025-04-28)、「Marvell Industrial Alert System」(2025-12-29) → 读者兴趣偏「10G 汇聚/L3」；当前 P1 属「DC 核心/CENTEC」，下一封按「10G 汇聚/L3」给，不按 P1｜已发资料（勿重发）：DIN Power Adapter(2024-07-30)、Marvell Based CLI Manual(2025-01-27)、Marvell Based Web Manual(2025-01-27)、STC-448XGGPM(2025-01-27)、STC-4816XGCGM(2025-01-28)、Product Link_2026Q2(2026-02-12)；还没给过：7.5 Feature List、Product Link 2026Q3（下一封可带，但只带与其需求相关的那一页）｜需求台账 #13/#1：2024-05 的「不可用」现在可用（STH1G），一句话补上；价按 Q-54「按数量报」
  - 做不了 / 要先核的：2025-02-10 两款 Broadcom 的货源（非 SmartByte/HRUI）未入库——若再问起，不要承诺；Simon《STH计划》：铜口 CENTEC 机（STH1G/2.5G/5G，含 Multi-Gig PoE++）暂不宣传、点名才给；主推 10G/25G/XLite/100G/400G/800G
- **下一步（具体）**：2026-11（一次）　A 邮箱 → mark@expresssupply.net　一句话问 Broadcom 是客户规格硬条款还是偏好；若偏好 → 付样 1 台 CENTEC
  - 第一问（只问一个）：Mark — in May 2024 you asked for a 1U full-L3 unit with 24 copper + fiber + QSFP+ uplinks and I had nothing; today that is STH-2QX4DX24GE-HSI on our CENTEC line (24×1G + 4×25G SFP28 + 2×40G QSFP+, OSPF/BGP/MPLS). Is Broadcom written into your customers' ITS specs, or would it qualify if it clears your lab test?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2024-05-09 | 来 | Mark Schulting | I'm in need of a 32 port model full layer 3 1u 8 fiber 24 copper with a qsfp+ uplink | 首个精确需求 | `d0066f467b2afcd7` |
| 2024-10-31 | 去 | Saga（Simon） | Hi, Mark, How are you? I would like to show you a power booster that transforms 1*DC12V~DC48V input to 2*DC52.4V output. *It is very useful in solar power solution where most PV generated power is between DC12V~DC24V.* This power converter increases the voltage and make possible powering standard Po… | Saga 实质答复原文（主题「Re: L3 managed switch」；第 20 批从 gmail_s 回补）——承诺/口径以此为准 | `f56f98bcf2e0a850` |
| 2024-12-18 | 来 | 用户表（Simon 跟进记录；渠道 Email） | 用户表跟进：推「8c48xf」→ 对方「需要BCM芯片」 | Simon 自己的跟进表里有回应记录，邮箱里看不到（多为 WhatsApp/微信）——证明渠道活着；按原文留存，不扩写 | `Clients/A/DONE/US.xlsx no.150 1218` |
| 2025-01-26 | 来 | mark@expresssupply.net | WE would not be interested in this switch . However, we are looking for another vendor to supply us some full layer 3 switches | 来信原文（主题「Re: 48 Port SFP Switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `e17a1b0f28d7f22f` |
| 2025-01-27 | 来 | mark@expresssupply.net | it appears you have a 12 fiber 24 copper. Can you send me a spec sheet on this one -- With kind regards, Mark Express Supply Inc. 407-497-8614 Hardene | 来信原文（主题「Re: 48 Port SFP Switch」；第 19 批从 gmail_s 回补，之前只有计数没有原话） | `77637aa387e80868` |
| 2025-01-28 | 来 | Mark | Do you have all 10 gig fiber 1g/2.5g/10g I am interested in buying in bulk | 批量意向 | `185a3765640a0e3f` |
| 2025-01-28 | 去 | Saga（Simon） | Hi, Mark, Do you mean something like attached photos? There is a rich port combination for your choice. *Just one thing* *Its CENTEC Chip based, a good domestic brand(see below link)* https://www.centec.com/silicon?category=Ethernet-Switch-Silicon… | Saga 实质答复原文（主题「Re: 48 Port SFP Switch」；第 20 批从 gmail_s 回补）——承诺/口径以此为准 | `f6d6159512661dd7` |
| 2025-02-05 | 来 | Mark | I need a broadcom chipset | 边界出现 | `5f00be3e081f8769` |
| 2025-02-10 | 去 | Simon | I got 2 models for you, Broadcom chipset. 1, 1000usd/pc, 2*40G+24*10G… 2, 4000usd/pc, 6*40G+48*10G | 破例找货（来源未入库） | `eb80eea25e1a3bb5` |
| 2025-03-03 | 来 | mark@expresssupply.net | We use Broadcom With Kind Regards, Mark Express Supply Inc. 407-497-8614 mschulting@expresssupply.net Hardened Networks / ITS Express Switches and Adv | 来信原文（主题「Re: Marvell Alleycat5 Solution」；第 19 批从 gmail_a 回补，之前只有计数没有原话） | `c7ad8300f3fcf7eb` |
| 2025-04-28 | 来 | Mark | Do you have broadcom based solution? | 第三次 | `898769c94b9fc197` |
| 2025-04-28 | 去 | Alan | Sorry to tell you that we focus on Marvell… Broadcom is for high-end market only, the market is small... | 口径收回 | `e8d9d485eebf828f` |
| 2026-01-16 | 去 | Saga（Alan） | Hi, Mark, How are you? I am introducing our CENTEC-based core and aggregation switches. 1, A cost-effective alternative to Cisco or Huawei models 2, Multiple models(10G~800G) available for various network scales 3, Full L3 features(VXLAN, EVPN, MPLS, Stacking etc.) suitable for core and aggregation… | Saga 实质答复原文（主题「Re: Marvell Alleycat5 Solution」；第 20 批从 gmail_a 回补）——承诺/口径以此为准 | `231c410bdb6b62d3` |

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | hardenednetworks.com（取自域名，公司全名待核） | 推断 |
| 国家 | 美国 | 事实（用户表）|
| 网站/域名 | hardenednetworks.com / expresssupply.net | 事实（用户表 URL/邮箱域名） |
| 类型 | 品牌商/贴牌需求（OEM/ODM）——ITS 加固交换机自有品牌 | 推断（据兴趣/备注关键词） |
| 联系人 | 重要 Mark Schulting / 别跟了 只用博通方案 | 事实（用户表） |
| 来源（From） | 谷歌 | 事实（用户表） |
| 兴趣（Interested in） | 工业FS 工业MC Bypass <br>自己的logo | 事实（用户表） |
| 用户备注（Remark） | — | 事实（用户表） |
| 所在清单 | A优质名单(US) | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | FS | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线
- **是谁**：美国交通 ITS 领域的自有品牌加固交换机供应商（HN-8012-24 V3、HN-AIS-8300、80 系列 V3：L3 OSPF/BGP、4×USFP+ 10G、ESFP 2.5G 等），与 ITS Express 同一体系；产品页 2026-07 仍在更新。用户表：3 次实质回复，兴趣工业 FS / 工业 MC / Bypass，用自己的 logo。
- **类型**：品牌商/贴牌需求（OEM/ODM）——ITS 加固交换机自有品牌
- **规模**：未见人数（专业小品牌）
- **在卖/在用品牌**：Hardened Networks, ITS Express
- **【官网】自有品牌加固 L3 交换机产品线（含 10G USFP+、2.5G ESFP、SHA-256）**
  > Hardened Networks/ITS Express Ethernet Switches · 80 Series V3 Switches -Hardened Full Layer 3 OSPF/PIM/VRRP/BGP -4 USFP+ Ports 1000Mb/2.5Gb/10Gb … HN-8012-24 V3 -Now Hardened Base Layer 3 … -V3 Technology -SHA-256 authentication
  > 来源：https://hardenednetworks.com/products/（抓取 2026-10-21）
- **【官网】HN-8012-24 V3 / 24+ V3 规格**
  > HN-8012-24 V3 -Now Hardened Base Layer 3 -4 USFP+ Ports 100Mb/1000Mb/2.5Gb/10Gb … -4 ESFP Ports … -16 Copper Ports 10Mb/100Mb/1000Mb TX -176 GB Back-Plane … HN-8012-24+ V3 … -Bypass fiber ports … -FIPS-197 compliant AES-256 encryption
  > 来源：https://hardenednetworks.com/products/（抓取 2026-07-01）
- **【官网 PDF】AIS-8300 交通摄像机：802.3bt 51W、NEMA TS2、UL、FL APL**
  > Power IEEE802.3bt, Type 3, class 6, max 51 watt … -Safety: RoHS, UL … -Others: NEMA TS2 … -FL APL Approval # 682-002-025 … ITS EXPRESS By Hardened Networks
  > 来源：https://hardenednetworks.com/wp-content/uploads/2025/07/HN-AIS-8300-2.5-20251507.pdf（抓取 2025-07-01）
- **【分销站】HN8012-24+ bypass/环网特性**
  > Built-in bypass fiber ports with switching time <10ms … Fast ITS ring recovery time< 10ms over 250 units of connections … Ring Protocols: STP, RSTP, MSTP, RPVST +, R-RVST+, ITS- Ring, Moxa/ Herschman/ Advatech Rings
  > 来源：https://expresssupply.us/hn8012-24plus/（抓取 2026-10-21）
- **KP**：Mark Schulting（来信署名人（职务未在邮件署名里出现））mark@expresssupply.net；mschulting@expresssupply.net（2025-02-05 来信用此地址） 〔S/A 邮箱来信 2024-05-09 → 2025-04-28 来信 7 封（另一地址 mschulting@expresssupply.net 2025-02-05）（第 72 批从邮件表头补）；A 邮箱 2025-02 来信表头〕
- 备注：A 确认（美国自有品牌工业交换机 + 3 次实质回复 + 明确贴牌）：P1 = STI-488XGGPM（工业 L2+ 8 PoE + 4×10G）对位其 HN 系列入门款，30% OEM 档；Bypass 需求需向 SmartByte 确认有无 bypass 款（无则如实说明）。

### 加厚挖掘（2026-10-21 · 深挖 v1）

| 公司事实 | 内容 |
|---|---|
| 法定名称 | Hardened Networks / ITS Express（expresssupply.us） |
| 总部/地址 | USA（ITS 交通领域） |
| 其他 | 自有品牌 HN 加固交换机（V3：Hardened Base L3、4×USFP+ 10G、4×ESFP 2.5G、16×GE、176G 背板、SHA-256/AES-256、ITS-Ring、Moxa/Hirschmann/Cisco 环兼容）+ AIS-8300 4K 交通摄像机（NEMA TS2、FL APL 682-002-025、UL） |

- **业务线**：ITS 加固交换机 HN-8012-24 V3 / 8012-24+ V3（bypass 光口）/ HN-8042 V3 / HN-3416 / HN-3488；ITS 交通摄像机 AIS-8300（802.3bt 51W）；ITS 配套（expresssupply.us 分销）

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| Hardened Networks | HN-8012-24 V3 / HN-8012-24+ V3 | L3 加固：4×USFP+（100M–10G）+ 4×ESFP（100M–2.5G）+ 16×GE，176G 背板，+ 型含 bypass 光口 <10ms，ITS-Ring 250 节点 | STC-424XGGM(L3)（机架位）/ 工业 10G L3 待 SmartByte 核型 | https://hardenednetworks.com/products/（2026-07-01） |
| Hardened Networks | HN-8042 V3 | 4×SFP+ 10G + 16×GE，156G 背板，Hardened Base L3，超 NEMA TS-2 | （同上） | https://hardenednetworks.com/wp-content/uploads/2025/05/HN-8042-20252305.pdf（2025-05） |
| ITS Express | AIS-8300 | 4K 31x 交通摄像机，802.3bt Type3 51W，NEMA TS2，UL，IP66/IK10 | —（PD 侧，需 bt 口交换机） | https://hardenednetworks.com/wp-content/uploads/2025/07/HN-AIS-8300-2.5-20251507.pdf（2025-07） |

- **触达通道（公开）**：网站: https://hardenednetworks.com/ · https://expresssupply.us/；直邮: mark@expresssupply.net / sales@expresssupply.net（用户表）
- **近况信号**：
  - 产品页 2026-07-01 更新 V3 系列；2025-05/07 发布 HN-8042 与 AIS-8300 PDF——持续迭代自有品牌（2026-10-21）
  - 用户表：3 次实质回复，兴趣工业 FS / 工业 MC / Bypass，用自己的 logo
- **风险/边界**：ITS 公共项目：NEMA TS2 + UL + Buy America 是硬门槛，Saga 工业机无 NEMA/UL——只能供其非公共/测试或 MC/bypass 等配套；Bypass 光口与 L3 10G 工业机不在 Saga 标准型谱，需 SmartByte 定制评估
- **Saga 对位结论**：P1 STI-288DGGPM（30% 档）——HN 主力为 10G L3 加固机（Saga 无直接对位，需 SmartByte 核型）；可供的是其环网末端 8 口 PoE DIN（STI-288DGGPM，支持 bt 摄像机需核功率）与工业 MC（STI-110GE）；贴 HN 标 30% 档
- **邮件切入句（英文）**：Below the HN-8012-24 class core units, the 8-port gigabit PoE DIN switch and the gigabit media converter are the two edge pieces we can build in Hardened Networks packing, so I am quoting those rather than the 10G L3 platform for now.

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://hardenednetworks.com/　语言：en-US　站点地图 URL 数：10
- **标题**：Home - Hardened Networks
- **描述**：Learn More Checkout Our Products Checkout Our Products Learn More About Us Learn More About Us Learn More About Us Technical Support
- **首页栏目**：Network Connections You Can Trust / Discover Our Latest Product / Advanced Imagers Series AIS-8300 / Our Products
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：sfp 23、2.5g 12、10g 7、switch 4、camera 3、poe 2、fiber 1、ethernet 1
- **站内型号串**（正则抽取，含非交换机）：SHA-256, FIPS-197, AES-256, HN-AIS-8300, HN-8012-24, HN-8042, AIS-8300, HN-8004-16, HN-3488, HN-3416
- **站内公开邮箱**：sales@expresssupply.net
- **产品类页面**：https://hardenednetworks.com/products/
- **已抓子页**：[Products - Hardened Networks](https://hardenednetworks.com/products/)；[Contact Us - Hardened Networks](https://hardenednetworks.com/contact-us/)
- 首页正文摘录：Skip to content Home Products Support Contact Us Search for: Home admin 2026-06-26T19:36:33+00:00 Network Connections You Can Trust Network Connections You Can Trust Discover Our Latest Product Advanced Imagers Series AIS-8300 The Advanced Imagers series delivers a new generation of stunning low-light, night color camera performance for the ITS/Traffic and Law Enforcement industries. Advanced engines, state-of-the-ar
- **自动对位建议**：STC-424XGGM（官网快照对位：10G/2.5G 词频 19、交换机 4 → 24 GE + 4×10G L2+ 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SA-026.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

| 备注所见品牌 | 含义 | Saga 切入 |
|---|---|---|
| FS | 台系/欧美/品牌工业或商用网络品牌 | 按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌） |

## 历史跟进记录（原表照录）

合并自 1 张跟进表，共 10 条（原值照录，日期已按年份递推补全）：

| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |
|---|---|---|---|---|---|---|
| 2024-05-07 | 2024.5.7 | 发了3层管理448信息 | 问了100G的 | Email |  | US.xlsx#150 |
| 2024-05-28 | 2024.5.28 | 发2光8BT信息 |  | Email |  | US.xlsx#150 |
| 2024-07-03 | 2024.7.3 | 4光24导轨式 |  | Email |  | US.xlsx#150 |
| 2024-07-30 | 2024.7.30 | 工业电源价格册 |  | Email |  | US.xlsx#150 |
| 2024-08-23 | 2024.8.23 | 8电口 |  | Email |  | US.xlsx#150 |
| 2024-09-24 | 924 | 100G |  | Email |  | US.xlsx#150 |
| 2024-11-01 | 111 | PC |  | Email |  | US.xlsx#150 |
| 2024-11-26 | 1126 | 154 |  | Email |  | US.xlsx#150 |
| 2024-12-18 | 1218 | 8c48xf | 需要BCM芯片 | Email |  | US.xlsx#150 |
| 2025-03-03 | 2025.3.3 | 芯片 | 只用博通方案 | A |  | US.xlsx#150 |

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom+a.sagatelecom　|　**邮件**：29 封（去 21 / 来 8）　|　**期间**：2024-05-07 → 2026-02-12　|　**最后去信**：2026-02-12
- **对方邮箱**：mark@expresssupply.net、mschulting@expresssupply.net、sales@expresssupply.net
- **最后一封来信**：2025-04-28 mark@expresssupply.net「Re: Marvell Alleycat5 Solution」：Do you have broadcom based solution?
- **邮件里报过的价**：2025-02-10 $1000；2025-02-10 $4000

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| Updated Ethernet Switches Links | 2026-02-12 | 2026-02-12 | 0 | 1 | 1 |
| Marvell Alleycat5 Solution | 2025-03-03 | 2026-01-16 | 2 | 3 | 6 |
| Marvell Industrial Alert System | 2025-12-29 | 2025-12-29 | 0 | 1 | 1 |
| 48 Port SFP Switch | 2025-01-23 | 2025-02-10 | 5 | 6 | 14 |
| 48 Port 10G Core Switch | 2024-12-17 | 2024-12-17 | 0 | 1 | 1 |
| Industrial PoE Switch | 2024-11-25 | 2024-11-25 | 0 | 1 | 1 |
| L3 managed switch | 2024-05-07 | 2024-10-31 | 1 | 8 | 27 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：A 级面层　|　**自动源**：3 个　|　**数据截至**：2026-10-25T07:41:18Z　|　**最近变化**：2026-10-23T04:20:51Z
- **最近变化摘要**：2026-10-23 首轮基线
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SA-026/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://hardenednetworks.com/) | html | HTTP 200 | 2026-10-23T04:20:51Z | 3435 字符；首行：Home - Hardened Networks |
| [sitemap](https://hardenednetworks.com/sitemap_index.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |
| [feed_auto](https://hardenednetworks.com/feed/) | rss | HTTP 200 | 2026-10-23T04:20:51Z | 1 条；最新：Fri, 31 May 2019 15:37:33 Hello world! |

## 联系方式（已有 · 原值照录）

- 邮箱：`mark@expresssupply.net`〔企业邮箱；来源：用户表原值〕
- 邮箱：`sales@expresssupply.net`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：重要 Mark Schulting / 别跟了 只用博通方案
- 网站/域名：hardenednetworks.com
- 网站/域名：expresssupply.net
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Mark Schulting | 来信署名人（职务未在邮件署名里出现） | mark@expresssupply.net；mschulting@expresssupply.net（2025-02-05 来信用此地址） | 调研核实（公开页） | S/A 邮箱来信 2024-05-09 → 2025-04-28 来信 7 封（另一地址 mschulting@expresssupply.net 2025-02-05）（第 72 批从邮件表头补）；A 邮箱 2025-02 来信表头 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户只有 1 行原始记录。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| A/DONE/US.xlsx#总表:151 | 150 | https://hardenednetworks.com/products/ | 美国 | 重要 Mark Schulting<br>别跟了 只用博通方案 | 谷歌 | 工业FS 工业MC Bypass <br>自己的logo | mark@expresssupply.net<br>sales@expresssupply.net |  | 10 条 |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STI-288DGGPM | 深挖对位：HN 主力为 10G L3 加固机（Saga 无直接对位，需 SmartByte 核型）；可供的是其环网末端 8 口 PoE DIN（STI-288DGGPM，支持 bt 摄像机需核功率）与工业 MC（STI-110GE）；贴 HN 标 30% 档 | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（品牌商/贴牌需求（OEM/ODM）——ITS 加固交换机自有品牌） |
| 备选2 | STC-28DGGPM | 8 口 PoE + 2 SFP L2+ 小接入 | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STI-288DGGPM），备选型不进首触。

- **第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + STI-288DGGPM 一条规格链接；只问一个问题。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有 3 次实质回复（对方认识我们）；自有品牌/贴牌需求 = 现成 OEM 客户；北美主攻区，复购与口碑可外溢
- **W**：Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局
- **O**：P1 STI-288DGGPM 按 30% 档报价，做现供应商的第二货源；贴牌 + 定制 UI/型号 → 30% 档与长期绑定；规模（调研）：未见人数（专业小品牌）
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
| 商业资格结论 | **技术上合格 / 商业上有互动证据（成交或实质回复或面谈）→ 值得长期跟进** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：Broadcom-based solution — straight answer, and the one thing we can offer

```text
Hi, Mark,

Straight answer to your April 2025 question: we do not build on Broadcom, and I should not have hinted otherwise in February. Our ranges are Marvell (access) and CENTEC (full L3: OSPF/BGP, MPLS, VXLAN/EVPN, MLAG).

For an ITS-hardened 10G optical aggregation role the CENTEC 24x10G + 2x100G L3 unit is the relevant box; it is quoted per project (DC power, MA license options).

One question: is "Broadcom" written into your customers' ITS specs, or would a CENTEC full-L3 unit qualify if it clears your lab test? If the former, I will stop sending you switch mail; if the latter, I will send the spec sheet and a test-unit price.

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

- **2026-11-08**（14 天）：无回复 → 换通道再试一次；仍无 → 降 B。有任何回复 → 当即更新 research JSON 并重渲染。

## 变更日志

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 1 行原始记录归并；自动评级 A，分数 84）

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
