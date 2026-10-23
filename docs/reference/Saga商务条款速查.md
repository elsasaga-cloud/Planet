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
- Warranty（Q-22 裁决前的保守写法）: "3-year warranty on commercial models and 3-year (up to 5-year on the 6-series) on industrial models, from the shipping date."
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
