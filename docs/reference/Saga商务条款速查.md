# Saga 商务条款速查（销售口径，中文）

> 依据：Google Drive `MUST KNOW/` 12 份 PDF（2026-02 版，英文原文见 `docs/drive/MUST-KNOW/`）+ `Certification/` 索引。本表是**给写邮件/回客户问题时查的中文摘要**，对外引用请以英文原文为准。  
> 与仓库既有规则冲突处用 ⚠ 标出，并在 `docs/requirements/待统一处理问题清单.md` 立项，裁决前按仓库规则执行。  
> 更新：2026-10-20（T13 建；T14 按 SmartByte 官网改写保修/DOA/OEM 条目）。  
> **真源优先级（T14 用户裁定）**：SmartByte 官网（2026-09 改版） > SmartByte 2026-09 价格表 > Saga Drive（2026 Q3 旧版）。 **Realtek 线进价真源** = 《洪瑞报价-天龙2026930.xls》（2026-09-30，`docs/reference/价格表_HRUI_三档加价_USD.md`）> PI 包采购合同成交价 > 微信口径。官网摘录见 `docs/smartbyte/公司与政策页_2026-10-20.md`。

## 1. 交期与起订
| 项目 | 口径 | 原文出处 |
|---|---|---|
| 生产启动 | 收到货款后开始（银行到账 1–2 个工作日） | FAQ / Order Procedure |
| 生产周期 | 标准品 ≤50 台：4–7 个工作日；定制/大单另议 | FAQ |
| 运输 | 快递 DHL/FedEx/UPS 4–7 天；海运/空运按单询价 | FAQ / TTC |
| 合计 | 下单到收货 ≈10–15 个自然日（标准品） | 推算 |
| MOQ | 1 台起订 | FAQ |
| 样品 | **不免费**；样品款在后续批量订单中抵扣；样品 5 个工作日出货；建议一次要 ≥2 台（含备用） | FAQ / After-sales |

## 2. 价格与付款
| 项目 | 口径 |
|---|---|
| 报价币种/条款 | 仓库规则：**USD EXW**（`docs/rules/报价与型号规则.md`）。⚠ Drive FAQ 写的是"Incoterms focus on **DAP**, sometimes DDP"→ Q-18，裁决前邮件仍写 EXW，客户要求到门价时再按 DAP 单独核算运费 |
| 付款方式 | T/T 或 PayPal |
| 付款比例 | 标准品批量：50% 预付 + 50% 发货前；定制/OEM：100% 预付；小额/样品：100% 预付 |
| 手续费 | T/T 银行费 $25/单（买方承担）；PayPal 加收 5% |
| 严格排期 | 若客户要求锁定排期，需预付 25% 物料押金 |
| 报价有效期 | 仓库格式：`$xx USD EXW（快照日期，15 天有效，报价前核价）` |

## 3. 保修与售后
| 项目 | 口径 |
|---|---|
| 保修期 | **官网（真源）：工业 6 系列 5 年 / 工业 3 系列 3 年；商用 3 年；ODM 项目另议**，自 SmartByte 发货日起算。Drive 旧版写 STC 1 年 / STI 3 年 / STH 1 年 → Q-22 待 Simon 确认对外传递口径 |
| DOA | 发货后 3 个月内到货即坏 = DOA：往返运费与更换费用由工厂承担；保内：客户寄回运费自付、工厂承担回寄与维修；保外：全部客户承担（官网 Warranty & RMA） |
| RMA | 每 100 台同型号随货送 2 台备件（或等值 2% 货款抵扣）；**不接受退货**，坏机以备件/下单补发方式处理 |
| 支持方式 | 邮件 + 远程（Web/CLI 日志）；固件升级免费；不含现场服务 |
| 人为/环境损坏 | 不在保修范围（雷击、过压、进水、私自改装） |

## 4. OEM / ODM 能力
| 项目 | 口径 |
|---|---|
| 免费定制 | 官网：软件定制 **No MOQ**（logo、产品型号名、SN、登录 IP、MAC、SNMP OID）；标签/外壳/包装定制；硬件定制覆盖 1G–100G；Drive 补充：Web UI logo 免费 |
| 需 MOQ 的定制 | Web UI 配色/字体、PVC 面膜（MOQ 300）、特殊包装 |
| SKD/CKD/ODM | SKD 可做；CKD/ODM 需评估；**源代码不开放** |
| 中性包装 | 可做中性包装/标签（仓库规则：不打 Made in China，不出现 Saga 以外品牌痕迹） |
| 文件 | COO 产地证 $15/份；其他认证文件复印件免费 |
| 客户资料 | 下单后为每个客户建 Drive 共享目录（规格书、固件、发票） |

## 5. 认证
- 现有：**CE（EMC EN 55032/55035/61000-3-2/-3 + LVD EN 62368-1）、FCC、RoHS、REACH 240、UKCA（EMC+LVD）**，2024-07 同批测试（报告号 JAT24070502534/-35、FCC NCT24028321X），证书在 Drive `MUST KNOW/Certification/`（索引：`docs/drive/Certification/认证证书索引.md`）。
- 没有：UL / cUL / EN 50155 / IP67 / ATEX。客户硬性要求 → 按继承规则降级或 PASS 并写原因。
- 证书覆盖的型号范围需人工打开 PDF 确认后再对外承诺。

## 6. 公司口径（对外一句话）
- 定位：Tailored Managed Networking Solutions Provider；slogan "Built to Last, Continuous Supply, Evolving Together"。
- 渠道：无海外分公司/独家代理，欢迎代理/分销（"best prices for distributorship"）。
- 技术路线（Technical Sales White Paper 2026-04-28）：Marvell AC5 为主推平台（ACL 3K–6K vs Realtek 256–512，硬件 L3，主线 switchdev），AC5+ 25G / SONiC 在路线图。
- ⚠ 官网域名：MUST KNOW PDF 落款 sagatelecom.com.cn，STOS 清单落款 sagatele.com，Simon 口述 sagatele.com → Q-19，邮件签名暂不写网址或只写 sagatele.com。
- ⚠ 云管理：STOS 清单列 "Cloud Management ○"，继承规则是"Saga 不做云管理" → Q-19，裁决前不主动承诺。

## 7. 常见问答模板（英文一句话，可直接贴）
- Lead time: "Standard models ship in 4–7 working days after payment, plus 4–7 days by express."
- Samples: "Samples are charged at unit price and fully deductible from your first bulk order."
- Warranty（2026-10-24 第 59 批按 Drive《Warranty Policy》+ 75 份实发 PI 普查改正，见口径表 #6）: "1-year warranty on commercial models (STC) and 3-year on industrial models (STI) and DIN power supplies, from the delivery date, with lifetime technical support." CENTEC STH 同商用 1 年。官网 5 年不引用。
- Payment: "T/T 50% deposit, balance before shipment; PayPal accepted with 5% fee."
- Spares: "2 free spare units per 100 pcs of the same model instead of RMA returns."
- OEM: "Logo, label, carton and Web-UI logo customization are free of charge; neutral packing available."

## 8. 2026-09/10 S 邮箱实际口径（Simon 原话，PR-02-31 复盘 2026-10-22 补）
> 来源：`data/gmail_s/messages/2026/2026-09.jsonl`、`2026-10.jsonl`（Milliseconds Evolution SB-1337、Fikes Media SB-1336、Vi-Link SA-011 等线程）。这是**现在正在用的**说法，与上面官网/Drive 口径有差异时以此为准、差异列入 Q-35。

| 项目 | Simon 现行口径（英文可直接复用） | 出处 |
|---|---|---|
| 群发主推 | "Marvell AC5 based L2+ switch: 24 Port PoE af/at + 10G Fiber Uplinks + OEM and customizable Web GUI — **Price: 180USD/PC**"（= STC-424XGGPM-280W，20% 档） | 2026-09-28 → 10-20 群发 813 封同主题「24 Port PoE Managed Switch」 |
| 样品 | "Normally evaluation units are provided at a **partner price**, and the sample cost will be **credited toward your first commercial order**. For long-term partners we can discuss additional support based on the project and cooperation plan." → 随后直接开 2 台样品形式发票（STSC-20261017-001） | 2026-10-03 / 10-17 致 Milliseconds |
| 分销 | "For now, we do not have a distributor in the UK. We are certainly open to discussing a distributorship **after we get to know each other and see good cooperation**." | 2026-09-30 致 Milliseconds |
| OEM 菜单 | "Company logo / Packaging / Front panel (PVC mask) / Product label / Model name / Serial number / User manual / Default login IP / SNMP OID customization / Web GUI language — all mature options. We can also discuss **firmware customization** for specific project requirements, **subject to technical evaluation**." | 2026-10-04 致 Fikes Media |
| 控制器/API 问法 | 先反问："REST API / SNMP-based / SSH-CLI automation / NETCONF / other controller platform?"（Saga 线实际可承诺：SNMP + CLI/SSH + Web；**无云控制器、无 REST API**，下一封应直说） | 2026-10-04 致 Fikes Media |
| 资料包 | 先发 `Saga Feature List_7.5.x_L2+.xlsx` + `Product Link_2026Q3.pdf`（Q4 版将更新）；深谈再发 `STC-424XGGPM-280W.docx` + `Marvell Based CLI/Web Manual.docx` + `SWITCH-MIBS-release.docx` | 2026-09-30 / 10-04 |
| 涨价提醒 | "in recent days, PCB and material costs are rising. This is one of the very competitive models." | 2026-10-03 |
| 签名 | "- Simon  https://sagatele.com/  An Engineering & Supply-Chain-First Telecom Partner  Built to Last, Continuous Supply, Evolving Together" | 全部 2026-09/10 群发 |

- **SNMP 企业号（PEN）提醒**：NYNEX（SA-013）2025-03 测试时发现 SmartByte 通用 MIB 内含其他 OEM 客户的企业 OID（.57430 / .56813 / .171 D-Link），要求 Saga/SmartByte 申请自己的 IANA PEN 并说明 OEM 数据是固件写死还是独立分区。对欧洲系统集成商这是合规题 → Q-35（建议 Saga 自己免费申请 PEN，并要求 Saga 版固件只含 Saga 树）。

## 9. Q-35 落地：Saga 自有 IANA PEN 与 OEM 固件边界（T29-U11 裁定「按默认」，2026-10-22）
**为什么**：欧洲集成商/运营商验收时会 `snmpwalk` 看 `sysObjectID` 与私有 MIB 的企业号归属；NYNEX 2025-03 已经因为 SmartByte 通用 MIB 里混有别家 OEM 的企业 OID（.57430 东莞华容、.56813 福州 Dockeer、.171 D-Link）追问「Saga 与 SmartByte 什么关系、OEM 数据是不是写死在固件里」（证据：`data/saga_clients/research/SA-013.json` evidence #14）。

**Simon 要做的（约 15 分钟，免费）**
1. 打开 IANA PEN 申请表 `https://pen.iana.org/pen/PenApplication.page`，填：Organization = Zhengzhou Saga Telecom Equipment Co., Ltd.（与营业执照英文名一致）；地址；Contact = Simon（姓名 / 职务 / 电话 / 邮箱用 sagatele.com 域名邮箱，不要用 Gmail）。
2. 提交后 IANA 通常 1–3 周内邮件回复分配的号码 `n`，Saga 的企业树即 `1.3.6.1.4.1.n`；把号码记到本节和 `README` 公司信息处。
3. 拿到号码后，给 SmartByte（Peter / 研发窗口）发一封「Saga 版固件 MIB 规范」邮件，要求（可直接贴英文）：
   - "Please build the Saga-branded firmware with `sysObjectID` and all private MIB objects under our enterprise tree `1.3.6.1.4.1.<n>`; remove every other OEM's enterprise OID from the MIB files shipped with our firmware."
   - "Please confirm whether OEM data (logo, model name, default IP, SNMP OIDs, sysDescr/sysName defaults) is compiled into the firmware image or kept in a separate configuration partition, and whether it survives a firmware upgrade."
   - "Please provide per-model `sysObjectID`/`sysDescr` values and a Saga-named MIB module (e.g. `SAGA-SWITCH-MIB`) so that our customers' NMS templates reference Saga, not SmartByte or third parties."
4. 在拿到 Saga PEN 之前，OEM 菜单里的 "SNMP OID customization" 改写为：**"Private MIB under your own IANA PEN (please send us your PEN) or under Saga's enterprise tree"**，避免客户测试时发现第三方 OID。

**对外一句话（客户问「你们和 SmartByte 什么关系」时）**：
"SmartByte is our Marvell-platform manufacturing partner; Saga owns the product definition, firmware branding (including the private MIB under our own enterprise number) and after-sales. The firmware you receive is built for Saga and does not carry third-party OEM identifiers."

## 10. 物流与清关实务（PI 包出货资料归纳，2026-10-24 第 70 批）

> 来源：Drive PI 包 20 个成单户文件夹里的「买单报关 / 发货信息 / 装箱单 / 入仓标签」（`data/pi_2026-10/text/`）。只记实际发生过的做法。

| 项目 | 实际做法（证据） |
|---|---|
| 两条物流线 | ① **客户自己的广州货代**（Mbata 尼日利亚：3rd 单 申娟·越秀宇航通讯大厦；4th 单 Tony Uhutex·瑶台西街美泰城；10th/11th/14 台 陈静怡 Serena·花都东湖村仓；末端收货人 VALENTINE, Lagos）——Saga 只负责送到广州仓，发货信息单写「品名 / 数量 / 重量 / HS 8517622990 / 品牌 无 / 不带电不带磁」。② **Saga 自己的深圳买单报关线**（James 加拿大、Angora 土耳其、Sugito 马来西亚、NYNEX 德国、Rishi 印度…）：填「出口货物确认函 / 货物情况说明表」→ 深圳联邦（UPS/FedEx/DHL）入仓标签 `WE0xxxxxxxxx_国家_入仓标签.PDF` → 运单；PI 写 **DAP but without customs clearance**（SA-012 英国）。 |
| HS 编码 | 交换机 **8517622990**；光模块 8517795000（Pythias 赞比亚单）；光纤清洁笔 8517799000（Rishi 印度单）。 |
| 品牌栏 | OEM/贴牌客户一律「**无品牌**」（James 2nd 单起、Angora 全部、Mbata 全部）；自有品牌出货写「Saga Telecom · 境内自主品牌 · 生产厂家 Zhengzhou Saga Telecom Co., Ltd.」（James 1st 单、Pythias、Sugito）。两种都发生过，按客户要的外观定。 |
| 单台重量/尺寸（报 DAP 直接用） | STI-21616DGGPM/XGGPM（James SW-3200-16GP）**158×115×54 mm，净 1.2 kg**，12 台一箱 20 kg；STI-288DGGPM 1.2 kg；STC-424XGGPM ≈3.4–3.5 kg，440×180/205×44 mm；STC-448XGGPM ≈5.6 kg；ANW-2116-PG（STC-424DGGPM-280W 16 口版）8 台一箱 21 kg（53.5×40×40.8 cm）；STC-2224GFP-24V 2.9/3.6 kg，440×290×45 mm；SmartByte 原箱：8 PoE+2 SFP 两台一箱 3 kg（31×23.5×18.5 cm），24/48 口机 10.6 kg（53.5×20.5×40.8 cm）。 |
| 大单运费的分量 | Angora 176 台 = 23 箱 471.9 kg，运费 22,426 RMB ≈ 127 RMB/台（≈$18），把毛利从 ~24% 压到 15.9%——同规模报价时运费单列、空运/海运分开报。 |
| 印度清关 | FedEx 需要收货人先在 kyc.fedex.com 上传 **GSTIN + 身份/地址证明 + 清关授权书（POA）**，拿到运单号后才能办（SA-016 United Control Engineers 2024-04，GSTIN 09AACCU4195M1ZP）；没做 KYC 货会卡在海关。 |
| 装箱单 | 工厂（SmartByte）出 PACKING LIST 给 Zhengzhou Saga Telecom（Consignee），再由 Saga 转出口——**工厂单据上出现的是 Saga 的郑州抬头，不是客户**；客户看到的只有 Saga 的 CI/PL。 |
| 出口管制分类（客户合规表） | 对 Netaş 已填：**EAR99 · NLR (No License Required, EAR §734) · CCATS 不适用 · HTS 8517622990 · 原产国 China**（STI-488DGGPM-2BT，2025-12-03）；国防相关/大企业供应商入库问 ECCN 时照此答。⚠ 该表 certify 句残留模板公司名 JERA ELEKTRONİK，下次更新改为 Zhengzhou Saga Telecom。 |
| 个人数据（KVKK/GDPR 类附件） | Netaş《Annex 1 个人数据附加协议》已签：客户方个人数据只用于履约、不转第三方/不出境——Netaş 联系人不进群发名单，不转给工厂。 |

## 11. 成单户往来里核出的实操口径（第 71 批 (m)，2026-10-24；全部有邮件原话，见各户研究档 `facts`）
| 项目 | 口径 | 出处 |
|---|---|---|
| 首笔外汇入账 | 中国银行对首笔境外来款要**买方股东信息**（一个股东即可；只首笔要）——新客户首付前先说，别等款到了再临时要护照/商业登记 | SA-168 2024-05-21 `gmail_s 08d71191c7529e7c` |
| 出货前老化 | 样机/订单出货前 **5 个工作日稳定性测试**（公司政策）——交期承诺要把这 5 天算进去 | SB-473 2026-01-14 `gmail_a 917809e3aa72885e` |
| 功能开发排期 | 「加功能」只在**有订金/订单确认后**排期，否则不给时间表（AC5 加 SFTP 的先例） | SA-168 2024-06-18 `gmail_s cfb663aad0d6b99b` |
| 大单产能 | 备料约 **3 周**（PCB、PoE 芯片、AC5 芯片）；**≥25% 订金起备料**；优先谈**分批交付**；250 台 ≈ 40 个自然日 | SA-168 2025-05-10 / 2024-06-18 |
| 软件贴牌 | logo / 型号名 / MAC / 登录 IP / SNMP OID **免费，1 台也做**；**界面配色不在内**（改码量大，样单不做） | SA-168 2024-04-29 / 2024-05-06 |
| 前面板 PVC 丝印 | **收费**（整批开模），余料 Saga 仓库代存供后续订单；MAC 段免费 | SA-168 2024-10-20 |
| 定制彩盒 | **$2.5/套，200 套起**（盒 + 异形泡棉 + 顶片 + 说明书）；8 口管理型（L2+/L3）与 STI-21616DGGPM 同尺寸 **158×115×54 mm**，一款盒通用 | SA-168 2024-12-13 `gmail_s a17daefafab4939f` |
| 「能不能读输入电压」 | PoE 机 GUI 只显示 **PD 侧**电压/功率，不显示交换机自身输入；非 PoE 机没有此项 | SA-168 2024-07-26 |
| 固件版本口径 | AC3 终版 **lite-hotfix-7.3.13**（只维护不更新）；AC5 线 2026-08 给客户的是 ac5-hotfix-7.4.2，7.5 为 AC5 Lite（98DX2515/2518）发布版——写信前看该户机型是哪一代 | SA-169 2026-08-07 `gmail_s 3e84bddd5a4fd519` |
| 2024-11 的「六个不做」 | NAT / 堆叠 / SD-WAN / TSN / MPLS / 云管理（AC3 时代原话；MPLS 现在 CENTEC 线有，其余仍不做）；当时还主动说「同芯片 98DX226S 的第三方能做，可代采」 | SA-168 2024-11-07 `gmail_s f4e695a067e95cd9` |
| 客户资料夹 | 成单客户一户一个 Google Drive 订单文件夹（Angora / Vi-Link / James / Netaş 都有），把对方指定人加为编辑，请其上传测试报告 | SA-011 2024-04-29 · SB-473 2026-01-24 |

