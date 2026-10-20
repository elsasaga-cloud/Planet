# 00 · Google Drive 盘点与入库方案（T13，2026-10-20）

> 目的：Simon 把 Google Drive（主）和 Gmail（次）接进来，要求"好好构思一下咋处理"再 copy 到仓库。本文是盘点结果 + 分层入库规则 + 已完成/待办清单。清单明细见 `data/drive_manifest.csv`（56 行，含 Drive id）。  
> 账号：e.sagatelecom@gmail.com（Drive 根 id `0AJ8a22_hYShqUk9PVA`）。盘点方式：Drive 连接器 `list_files` 逐层列目录（整盘一次性 200 行会被截断，已记入死路）。

## 一、Drive 长什么样（顶层 8 个文件夹）
| # | 文件夹 | 内容 | 规模 | 价值判断 |
|---|---|---|---|---|
| 1 | **MUST KNOW** | 12 份商务/公司 PDF（FAQ、Warranty、After-sales、Order Procedure、TTC、CCF、Misc Fee、How We Do Business、Easy & Transparent、Roadmap、Client Oriented、Technical Sales White Paper，另有汇总版 Business Mode_FULL INFO）+ `Certification/`（CE/FCC/RoHS/Reach/UKCA/MC 证书与报告）+ `Factory Information/`（车间/团队/测试设备照片 21 jpg + 3 mp4） | 文本 ≈1.5 MB；证书 ≈95 MB；照片/视频未统计 | ★★★ 销售每天要用的**商务条款真源** |
| 2 | **Saga Telecom Resource Library** | Roadmap.pdf、Saga Software Feature List_EN_V2.4.pdf（STOS，CENTEC 平台）、Saga Feature List_7.5.x_L2+.xlsx 等 4 份 | 小 | ★★☆ 技术问答依据 |
| 3 | **Marvell Based Commercial Managed Switch** | 6 个品类子目录（每品类 = 若干 `型号/` 照片目录 + `型号.docx` 规格书 1–2 MB）+ Price List PDF + Feature List L2+/L3 xlsx + User/CLI/Web Manual | 数十型号 | ★★★ 主推线（STC） |
| 4 | **Marvell Based Industrial Managed Switch** | 9 个品类子目录（10G L2+ PoE / L2 / L2+ BT / L3 BT / L3 with PoE / L3 without PoE …）+ 同套文档 | 数十型号 | ★★★ 主推线（STI 管理型） |
| 5 | **Marvell Based Industrial Unmanaged Switch** | ≈55 个 STI 型号目录（部分重复）+ ≈55 份型号 docx（1–6 MB）+ Price List | 列表 100 行仍未翻完 | ★★☆ 走量线 |
| 6 | **Realtek Based Commercial Switch** | 4 个品类目录 + Price List | 小 | ★☆☆ 非 Marvell 主线 |
| 7 | **CENTEC Based High-Speed Network** | STH 系列目录 + 手册/pptx | 中 | ★☆☆ 核心/汇聚，不是接入层客户的主菜 |
| 8 | Google AI Studio | 2 字节 json | — | 忽略 |

## 二、分层入库规则（为什么不整盘 copy）
Drive 总量以**二进制**为主（型号 docx ≈150 份、证书报告 ≈95 MB、照片/视频），直接 copy 进 Git 会：撑大仓库、无法 diff、与 Drive 双源漂移。因此按"用得着的程度"分三层：

| 层级 | 范围 | 入库形式 | 已做 |
|---|---|---|---|
| **Tier 1 · 全文/节选入库** | MUST KNOW 12 份商务 PDF、Resource Library 的 STOS 清单、证书索引 | 逐篇转成 MD（英文原文逐句保留 + Drive id/链接/抓取日期头），放 `docs/drive/` | ✅ 12 篇 `docs/drive/MUST-KNOW/`、`Resource-Library/STOS软件特性清单_V2.4_节选.md`、`Certification/认证证书索引.md`；中文销售速查 `docs/reference/Saga商务条款速查.md` |
| **Tier 2 · 结构索引 + 按需抓取** | 三条 Marvell 产品线的品类目录与型号规格书、Feature List xlsx、Price List PDF | 只记录目录结构与 Drive id（manifest）；某型号要写进邮件/档案时，用 `search_files name='<型号>.docx'` 现抓现用，摘出的参数写进对应客户档案的证据里（注明 Drive id） | ✅ 索引；型号总表未建（Q-20 待裁决） |
| **Tier 3 · 仅索引** | Realtek、CENTEC、手册（Mikrotik 仓库已有 CLI/Web Manual）、工厂照片/视频、媒体转换器证书 | manifest 一行，不进 Git | ✅ |
| **不入库** | 任何二进制原件（pdf/docx/xlsx/jpg/mp4） | 以 Drive 链接作为证据引用 | — |

补充规则：
1. 入库 MD 一律带"来源 Drive id + 链接 + 抓取日期"头，方便回溯与刷新。
2. Drive 文件有更新 → 只改对应 MD，不改规则文件；冲突写入 `docs/requirements/待统一处理问题清单.md`。
3. Drive 内容与仓库既有规则冲突时，**仓库规则优先、Drive 作为待裁决事实**（本轮发现 3 处：Incoterms、云管理、官网域名 → Q-18/Q-19）。

## 三、本轮从 Drive 学到的关键事实（已沉淀到速查表）
交期 10–15 天（付款到账 1–2 工作日 + 生产 4–7 工作日 + 快递 4–7 天）、MOQ 1 台、样品不免费但可抵货款、保修 STC 1 年 / STI 3 年 / STH 1 年、T/T 或 PayPal、标准品 50/50、定制 100% 预付、RMA 每 100 台送 2 台备件、OEM logo/包装/Web UI 免费、SKD 可做、源代码不开放、认证 CE/FCC/RoHS/REACH/UKCA（2024-07 同批测试）。详见 `docs/reference/Saga商务条款速查.md`。

## 四、待办（按优先级）
1. **Price List 对账**：Drive 三份 Marvell 价格 PDF（ids 见 manifest）与 `data/价格主表.csv` 对比，只记差异、不改报价规则（T03 已裁决列表价差异不再提）。
2. **Feature List xlsx → CSV**：`Saga Feature List_7.5.x_L2+/L3.xlsx` 导出为 `data/`，用于回答 Marvell 管理型功能问题。
3. **型号总表（Q-20）**：若 Simon 同意，再从 ≈150 份 docx 批量提取端口/PoE 预算/电源/尺寸等字段建 `data/型号总表.csv`；默认不做，按需抓取。
4. Industrial Unmanaged 列表翻页补齐（next_page_token 尚未消费）。
5. Certification PDF 正文的型号覆盖范围（人工打开确认一次即可）。
