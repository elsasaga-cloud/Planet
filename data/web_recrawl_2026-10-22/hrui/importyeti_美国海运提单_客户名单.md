# HRUI 美国海运提单（ImportYeti，美国海关 CBP 数据）— 供应商页 + 客户页
- 供应商页 URL: https://www.importyeti.com/supplier/shenzhen-hongrui-optical-technology （抓取 fetch_page chunk 0/1/2/4，2026-10-22T13:01–13:03Z；ImportYeti synced 10/21/2026）
- 客户页 URL: https://www.importyeti.com/company/spectrumvoip （chunk 0，2026-10-22T13:01Z）
- 发现途径：web_search `importyeti.com "Shenzhen Hongrui Optical Technology"`（2026-10-22T13:00Z）
- 说明：只覆盖美国**海运**进口提单（无空运、无快递、无非美国家）；HS 编码由 ImportYeti 从品名推断，不准。

## 供应商卡片（原样）
- Shenzhen Hongrui Optical Technology — 2Nd Floor Wangrong Industrial Park No 11 Jiujiu Industrial Road Way Xihuan Road Shajing Street Bao An District Shenzhen China（另有 6 个地址变体；网站 www.hruitech.com）
- Last Shipment Spotted **10/14/2026**；Total Sea Shipments **44**（2018-07 → 2026-10）；Avg. TEU per Shipment 2.12；Est. Shipping Spend $134,175.88（79% coverage）；出发国 China 40 / Hong Kong 4
- 月度出货频率（历年合计）：Jan 6 / Feb 4 / Mar 4 / Apr 3 / May 3 / Jun 4 / Jul 3 / Aug 6 / Sep 2 / Oct 4 / Nov 1 / Dec 4
- 联系邮箱 1 个（锁定，最后出现于 2021-05-31 提单 MFGTHKLGB3834051）

## 美国客户名单（Customers 表，原样）
| 美国进口商 | 地点 | 海运票数 | 品名 / HS |
|---|---|---|---|
| **GW Security** (Gw Security Inc) | South El Monte, CA | 14 | Poe Switch, Poe Switch Plts；HS 7318.15 / 8536.50 / 8517.62 |
| **Component Specialties** (Components Specialties Inc) | Amityville, NY | 9 | Poe Switch, Poe Switch Poe Injector, Poe Switch Sfp Module；HS 8536.50 / 8409.99 / 8517.62 |
| **Spectrumvoip** (Spectrumvoip Inc) | Irving, TX（2900 Gateway Dr, Ste 620, Irving, TX 75063） | 9（客户页写 10，另 1 票来自 Zhejiang Valiant Power 轮胎） | Port Poe Switch, Poe Switch；HS 8536.50 / 8517.62 |
| **Tycon Systems** (Tycon Systems Inc) | Riverton, UT | 4 | Poe Switch（HS 8517.62） |
| **Great Wall Security** | US | 3 | Poe Switch（HS 8536.50） |
| **Spanish Fork City** | Spanish Fork, UT | 1 | Fiber Media Converter（HS 8504.40） |
| **PoE Texas** | US | 1 | Poe Switch（HS 8536.50） |
| **CCTV Supply Inc** | Buffalo Grove, IL | （最早一票 2018-07-11，194 kg / 8 ctn） | Poe Switch |
（表格有 "Show More"，可能还有少量客户未展开）

## 近期提单明细（Most Recent Sea Shipments，原样节选）
| 到港日 | 提单号 | 客户 | 重量 kg | 件数 | 品名 | 航线 / 估算运费 |
|---|---|---|---|---|---|---|
| 10/14/2026 | PSEAZLGB26092040 / OOLU2337600571 | Gw Security Inc | 2,240 | 170ctn | Poe Switch Plts | Asia–US Pacific $8,231.96 |
| 10/12/2026 | FLXT00004143869A / EGLV010600873330 | Components Specialties Inc | 950 | 71ctn | Poe Switch | Asia–US Transatlantic |
| 09/05/2026 | FLXT00004061230A | Components Specialties Inc | 142 | 11ctn | Poe Switch | Transatlantic |
| 07/19/2026 | FLXT00003948491A | Components Specialties Inc | 143 | 11ctn | Poe Switch | Transatlantic |
| 06/18/2026 | FLXT00003861331A / ZIMUSHH32100505 | Components Specialties Inc | 524 | 38ctn | Poe Switch Sfp Module | Transatlantic |
| 04/22/2026 | FLXT00003787498A | Components Specialties Inc | 398 | 31ctn | Poe Switch | Transatlantic |
| 04/08/2026 | OSTIMASZ26030085 / EGLV149601244389 | Gw Security Inc | 2,200 | 170ctn | Poe Switch Plts | Pacific $2,185.72 |
| 02/27/2026 | FLXT00003676680A | Components Specialties Inc | 667 | 51ctn | Poe Switch | Transatlantic |
| 02/13/2026 | PSEAZLAX26012520 / EGLV149600116077 | Gw Security Inc | 1,300 | 100ctn | Poe Switch | Pacific $2,701.94 |
| 01/18/2026 | FLXT00003604353A | Components Specialties Inc | 439 | 34ctn | Poe Switch Poe Injector | Transatlantic |
| 12/15/2025 | FLXT00003449644A / ZIMUSHH31929215 | Components Specialties Inc | 270 | 21ctn | Poe Switch | Transatlantic |
| 11/02/2025 | FLXT00003420339A | Components Specialties Inc | 430 | 33ctn | Poe Switch | Transatlantic |
| 06/20/2025 | OSTIMASZ25060009 | Gw Security Inc | 2,920 | 225ctn | Poe Switch Plts | Pacific $3,047.5 |
| 01/21/2025 | OSTIMASZ24120168 | Gw Security Inc | 1,640 | 126ctn | Poe Switch Plts | Pacific $4,832.54 |
| 09/05/2024 | OSTIMASZ24080033 | Gw Security Inc | 1,982 | 157ctn | Poe Switch Plts | Pacific $6,945.12 |
| 03/28/2024 | OSTIMASZ24030002 / ONEYSZPE33263400 | Gw Security Inc | 2,200 | 171ctn | Poe Switch Plts | Pacific |
| 01/31/2024 | CHKMMZLMSA248500 / EGLV010301193311 | Tycon Systems Inc | 570 | 29ctn | Poe Switch（PO:6456，HTS 8517.62.32） | Pacific $1,852.88 |
| 01/02/2024 | PEVHPL2023125358 / OOLU2729074793 | Spectrumvoip Inc | 3,011 | 200ctn | Poe Switch | Pacific $1,754.3 |
| 12/04/2023 | OSTIMASZ23110069 | Gw Security Inc | 2,180 | 176ctn | Poe Switch Plts | Pacific |
| 08/24/2023 | CHKMMZLMSA237652 | Tycon Systems Inc | 90 | 5ctn | Poe Switch | Pacific |
| 08/06/2023 | NAQAPL2023075616 / COSU6359939850 | Spectrumvoip Inc | 2,418 | 100ctn | Poe Switch | Pacific |
| 08/05/2023 | SSUBMASZ2307050B / ONEYSZPDB1812700 | Gw Security Inc | 2,344 | 170ctn | Poe Switch | Pacific |
| 04/14/2023 | NAQAPL2023036368 / COSU8036392910 | Spectrumvoip Inc | 2,423 | 100ctn | Poe Switch | Pacific $1,308.04 |
| 03/31/2023 | OSTIMASZ23030010 | Gw Security Inc | 2,379 | 185ctn | Poe Switch Plts | Pacific $1,335.6 |
| 12/11/2022 | CCFEPL2022115636 | Spectrumvoip Inc | 1,781 | 75ctn | Poe Switch | Pacific |
| 10/02/2022 | OSTIMASZ22080030 / OOLU8810157312 | Gw Security Inc | 2,447 | 190ctn | Poe Switch Plts | Pacific $5,127 |
| 08/12/2022 | CHKMMZLMSA214874 / COSU6338919690 | Tycon Systems Inc | 156 | 10ctn | Poe Switch | Pacific |
| 06/02/2022 | OSTISZLGB2241027 / ONEYSZPCA3318800 | Gw Security Inc | 1,860 | 137ctn | Poe Switch Plts | Pacific $9,037.56 |
| 06/01/2022 | PEVHPL2022045697 / HLCUSZX2203CAVS9 | Spectrumvoip Inc | 1,727 | 75ctn | Poe Switch | Pacific |
| 02/01/2022 | PEVHPL2021126597 / ONEYCANB68986501 | Spectrumvoip | 1,730 | 75ctn | | Pacific |
| 08/13/2021 | SNYLPL2021075360 / EGLV010101148612 | Spectrumvoip | 1,685 | 75pkg | | Pacific |
| 03/02/2021 | CHKMPL2021025074 | Spectrumvoip | 1,382 | 60ctn | 8 Port Poe Switch HS 8517623200 | Pacific |
| 05/20/2020 | CHKMPL2020045718 | Spectrumvoip | 1,300 | 60ctn | Poe Switch HS 8517.62.0020 | Pacific |
| 07/11/2018 | BNXCCCG8614491 / OOLU2605422290 | Cctv Supply Inc (Buffalo Grove, IL) | 194 | 8ctn | Poe Switch | Pacific $1,608.02 |

## Spectrumvoip 客户页补充（原样）
- Spectrumvoip — 2900 Gateway Dr, Ste 620, Irving, TX 75063；Total Sea Shipments 10（2020-05 → 2025-10，Last Shipment Spotted 10/21/2025）；供应商：Shenzhen Hongrui Optical Technology 9 票（Port Poe Switch, Poe Switch）+ Zhejiang Valiant Power Technology 1 票（轮胎）；航线 Yantian→Long Beach 5、Nansha→Los Angeles 1、Hong Kong→Long Beach 1、Hong Kong→Los Angeles 1、Yantian→Los Angeles 1；Top 10 Relationships 图中同一供应商的其他公司：Pye Barker Fire & Safety、Preferred Good International Trade、Nexgen Global Services、Stallion Infrastructure Services、24/7 Onsite Cameras（这些是与 Spectrumvoip 共享供应商关系图的公司，不一定直接从 HRUI 进货，原样记录）

## 对 Saga 的含义（代理备注，不改变任何客户分级）
- HRUI 自 2018 年起持续对美**直销**整柜 PoE 交换机：GW Security（安防监控品牌商，每票 100–225 箱）、Component Specialties / Speco 体系（纽约 Amityville，2025-11 起几乎每月一票，还买 PoE injector + SFP）、Spectrumvoip（VoIP 服务商，自用 PoE 交换机）、Tycon Systems（犹他州 PoE 品牌 Tycon Power）、Great Wall Security、PoE Texas、CCTV Supply。
- 这些公司已直接拿 HRUI 工厂价，Saga 以 HRUI 为底的 STC 报价无价格优势 → **不作为开发目标**（若已在 `Saga Clients/` 名单中，仅作备注，不改级）；但它们证明「美国安防 / VoIP / PoE 品牌商会整柜买深圳 Realtek 方案」，是 Saga 向同类美国中小品牌推 Marvell 方案（SmartByte）时的市场证据。
- 2026 年 HRUI 对美出货仍在增长（Last Month's Total Shipments +140% YoY 提示），关税环境下仍走海运，说明美国买家未因关税停购。
- 可用 ImportYeti 同法查 SmartByte / Hohunet（见同目录其他文件）。
