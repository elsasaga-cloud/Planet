# Saga 商务条款速查（销售口径，中文）

> 依据：Google Drive `MUST KNOW/` 12 份 PDF（2026-02 版，英文原文见 `docs/drive/MUST-KNOW/`）+ `Certification/` 索引。本表是**给写邮件/回客户问题时查的中文摘要**，对外引用请以英文原文为准。  
> 与仓库既有规则冲突处用 ⚠ 标出，并在 `docs/requirements/待统一处理问题清单.md` 立项，裁决前按仓库规则执行。  
> 更新：2026-10-20（T13 建；T14 按 SmartByte 官网改写保修/DOA/OEM 条目）。  
> **真源优先级（T14 用户裁定）**：SmartByte 官网（2026-09 改版） > SmartByte 2026-09 价格表 > Saga Drive（2026 Q3 旧版）。官网摘录见 `docs/smartbyte/公司与政策页_2026-10-20.md`。

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
