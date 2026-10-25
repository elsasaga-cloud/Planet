# Gmail（s 邮箱）Takeout 全量入库 · 覆盖率报告

- 生成时间：2026-10-22T04:24:33Z；状态：**done**；本邮箱地址：s.sagatelecom@gmail.com
- 来源：2 个文件，合计 6.48 GB：`All_mail_Including_Spam_and_Trash-002.mbox` 6.48 GB；`takeout-20261021T123952Z-1-001.zip` 0.00 GB
- 批次 1：2 个文件 / mbox 条目 1 个 / 流总长 6.48 GB，已处理到偏移 6.48 GB，13,583 封，✅ 完成
- 规则：**full** = 全文（非群发 / 本邮箱发出 / 本邮箱回过的线程 / 对方是 Saga Clients 里的客户 / 加星 / 重要）；**snippet** = 群发与通知类只留头部 + 前 600 字；附件按 sha256 去重抽正文（≤25 MB，文档类；图片 OCR=开）
- 原件备份：`All_mail_Including_Spam_and_Trash-002.mbox` → Release `gmail-s-20261022` 4 卷 ✅；`takeout-20261021T123952Z-1-001.zip` → Release `gmail-s-20261022` 1 卷 ✅

## 总量

| 指标 | 数 |
|---|---|
| messages | 13,583 |
| full | 13,583 |
| snippet | 0 |
| out | 10,966 |
| in | 2,617 |
| bulk | 1,821 |
| with_client | 10,739 |
| parse_err | 0 |
| attachments | 13,460 |
| att_unique | 760 |
| att_ok | 528 |
| att_meta | 136 |
| att_fail | 0 |
| att_skip | 96 |
| text_chars | 15,951,998 |
| att_chars | 8,179,670 |

## 按年

| 年 | 封数 | 发出 | 收到 | 全文 | 群发 |
|---|---|---|---|---|---|
| 2023 | 157 | 5 | 152 | 157 | 110 |
| 2024 | 10,269 | 8,714 | 1,555 | 10,269 | 1,040 |
| 2025 | 1,798 | 1,312 | 486 | 1,798 | 298 |
| 2026 | 1,359 | 935 | 424 | 1,359 | 373 |

## 标签（前 30）

| 标签 | 封数 |
|---|---|
| Archived | 13,179 |
| Sent | 10,923 |
| Opened | 4,212 |
| Daily | 3,416 |
| Important | 2,244 |
| Category Personal | 1,553 |
| Category Updates | 967 |
| Trash | 360 |
| Category Promotions | 311 |
| Unread | 120 |
| Useful | 102 |
| Category Purchases | 29 |
| Drafts | 25 |
| Template Response | 23 |
| Scheduled Send | 17 |
| Category Social | 7 |
| Inbox | 6 |
| Starred | 4 |
| Fastball | 1 |
| Category Forums | 1 |

## 对方域名（前 40，排除本邮箱与免费邮箱）

| 域名 | 封数 | 客户编号 |
|---|---|---|
| angoranetworks.com | 603 |  |
| resonantnetworks.com | 174 | SB-001 |
| by56.com | 160 |  |
| service.bank.za.group | 137 |  |
| nynex.de | 103 | SA-008 |
| e-saudi.net | 70 | SB-451 |
| actelis.com | 67 | SB-831 |
| findlight.net | 67 |  |
| megnet.co.uk | 64 | SA-015 |
| service.alibaba.com | 58 |  |
| message.xtransfer.cn | 56 |  |
| globalsources.com | 55 |  |
| telecamera.ru | 52 | SC-650 |
| optiviewusa.com | 51 | SA-021 |
| simrex.com | 50 | SA-002 |
| alfa.com.tw | 50 | SA-013 |
| versitron.com | 50 | SB-826 |
| megatelindustries.com | 46 | SB-061 |
| alerts.globalsources.com | 46 |  |
| td-fe.ru | 45 | SA-035 |
| americanfibertek.com | 44 | SB-010 |
| etictelecom.com | 43 | SB-910 |
| cxr.com | 43 | SA-011 |
| altus.com.br | 39 | SC-1186 |
| vilinknet.com | 37 | SA-006 |
| optilinknetwork.com | 37 | SC-343 |
| intl.paypal.com | 35 |  |
| regalsecurity.co.za | 33 | SB-042 |
| airpro.in | 33 | SB-857 |
| powertec.com.au | 33 | SC-2495 |
| datacom.com.br | 32 | SC-3103 |
| telco.ge | 30 | SC-1723 |
| thomasnet.com | 29 |  |
| dss-kuwait.com | 29 | SB-530 |
| digisys.fr | 28 | SC-1490 |
| intelbras.com.br | 28 | SC-242 |
| axis.com | 27 | SC-2425 |
| texim-europe.com | 27 | SC-1226 |
| thorfiber.com | 26 | SB-085 |
| antronix.com | 26 | SA-042 |

## 关联到 Saga Clients 的往来

- 命中客户编号 1669 个：A 55 / B 538 / C 1076；明细见 `clients_link.json`、`contacts.csv`

## 附件类型

| 扩展名 | 个数（去重后） | 抽到正文 | 仅元数据 | 失败 | 跳过 |
|---|---|---|---|---|---|
| .pdf | 235 | 235 | 0 | 0 | 0 |
| .png | 234 | 120 | 63 | 0 | 51 |
| .jpg | 120 | 59 | 58 | 0 | 3 |
| .docx | 70 | 70 | 0 | 0 | 0 |
| .p7s | 36 | 0 | 0 | 0 | 36 |
| .xlsx | 14 | 14 | 0 | 0 | 0 |
| .jpeg | 6 | 4 | 2 | 0 | 0 |
| .mp4 | 6 | 0 | 6 | 0 | 0 |
| .zip | 4 | 4 | 0 | 0 | 0 |
| .txt | 4 | 4 | 0 | 0 | 0 |
| .xls | 4 | 4 | 0 | 0 | 0 |
| .vsd | 4 | 4 | 0 | 0 | 0 |
| .psd | 3 | 0 | 3 | 0 | 0 |
| (无) | 2 | 0 | 0 | 0 | 2 |
| .gif | 2 | 1 | 0 | 0 | 1 |
| .dxf | 2 | 2 | 0 | 0 | 0 |
| .ai | 2 | 1 | 1 | 0 | 0 |
| .doc | 2 | 2 | 0 | 0 | 0 |
| .dwg | 1 | 0 | 0 | 0 | 1 |
| .xps | 1 | 0 | 0 | 0 | 1 |
| .mib | 1 | 1 | 0 | 0 | 0 |
| .rar | 1 | 1 | 0 | 0 | 0 |
| .7z | 1 | 0 | 1 | 0 | 0 |
| .heic | 1 | 1 | 0 | 0 | 0 |
| .dat | 1 | 0 | 0 | 0 | 1 |
| .cdr | 1 | 0 | 1 | 0 | 0 |
| .pub | 1 | 1 | 0 | 0 | 0 |
| .webp | 1 | 0 | 1 | 0 | 0 |

## 解析失败（0）

无。

## 附件抽取失败（0）

无。

## 运行记录

- {"started": "2026-10-22T03:32:17Z", "limit": 0, "bulk_mode": "full", "attach": true, "ocr": true, "more_batches": false, "ended": "2026-10-22T03:53:00Z", "messages_this_run": 13583, "stopped_early": false}
- {"started": "2026-10-22T04:07:17Z", "limit": 0, "bulk_mode": "full", "attach": true, "ocr": true, "more_batches": false, "ended": "2026-10-22T04:24:33Z", "messages_this_run": 13583, "stopped_early": false}
