# Gmail（a 邮箱）Takeout 全量入库 · 覆盖率报告

- 生成时间：2026-10-24T04:55:57Z；状态：**done**；本邮箱地址：a.sagatelecom@gmail.com
- 来源：8 个文件，合计 26.74 GB：`All_mail_Including_Spam_and_Trash-002_1_.mbox` 13.37 GB；`All_mail_Including_Spam_and_Trash-002_1_.mbox.part01` 1.93 GB；`All_mail_Including_Spam_and_Trash-002_1_.mbox.part02` 1.93 GB；`All_mail_Including_Spam_and_Trash-002_1_.mbox.part03` 1.93 GB；`All_mail_Including_Spam_and_Trash-002_1_.mbox.part04` 1.93 GB；`All_mail_Including_Spam_and_Trash-002_1_.mbox.part05` 1.93 GB；`All_mail_Including_Spam_and_Trash-002_1_.mbox.part06` 1.93 GB；`All_mail_Including_Spam_and_Trash-002_1_.mbox.part07` 1.78 GB
- 批次 1：7 个文件 / mbox 条目 7 个 / 流总长 13.37 GB，已处理到偏移 13.37 GB，20,521 封，✅ 完成
- 一致性自检：流中读到 20,521 封 = 分片里 20,521 封；22 个分片长度与记录一致 ✅
- 规则：**full** = 全文（非群发 / 本邮箱发出 / 本邮箱回过的线程 / 对方是 Saga Clients 里的客户 / 加星 / 重要）；**snippet** = 群发与通知类只留头部 + 前 600 字；附件按 sha256 去重抽正文（≤25 MB，文档类；图片 OCR=开）
- 原件备份：`All_mail_Including_Spam_and_Trash-002_1_.mbox` → Release `gmail-a-20261024` 7 卷 ✅

## 总量

| 指标 | 数 |
|---|---|
| messages | 20,521 |
| full | 20,521 |
| snippet | 0 |
| out | 19,880 |
| in | 641 |
| bulk | 380 |
| with_client | 20,204 |
| parse_err | 0 |
| attachments | 21,841 |
| att_unique | 339 |
| att_ok | 215 |
| att_meta | 65 |
| att_fail | 0 |
| att_skip | 59 |
| text_chars | 13,578,054 |
| att_chars | 3,406,210 |

## 按年

| 年 | 封数 | 发出 | 收到 | 全文 | 群发 |
|---|---|---|---|---|---|
| 2025 | 11,820 | 11,363 | 457 | 11,820 | 303 |
| 2026 | 8,701 | 8,517 | 184 | 8,701 | 77 |

## 标签（前 30）

| 标签 | 封数 |
|---|---|
| Archived | 20,456 |
| Sent | 19,860 |
| Opened | 1,706 |
| Daily | 804 |
| Replied | 608 |
| Important | 588 |
| Category Personal | 458 |
| Category Updates | 269 |
| Trash | 45 |
| Category Promotions | 37 |
| Unread | 23 |
| Drafts | 16 |
| Template Response | 16 |
| Inbox | 2 |
| Starred | 1 |

## 对方域名（前 40，排除本邮箱与免费邮箱）

| 域名 | 封数 | 客户编号 |
|---|---|---|
| netas.com.tr | 265 | SB-473 |
| nsidistribution.com | 108 | SB-553 |
| qtech.ru | 102 | SB-951 |
| iacontrol.co.za | 102 | SC-368 |
| powertec.com.au | 92 | SC-2271 |
| larch-networks.com | 88 | SB-318 |
| dcbnet.com | 75 | SC-027 |
| digisys.fr | 74 | SC-1252 |
| vostok.ae | 69 | SC-1221 |
| patton.com | 68 | SB-854 |
| deps.ua | 68 | SC-2493 |
| dss-kuwait.com | 64 | SB-529 |
| telco.ge | 64 | SC-1489 |
| infinitecables.com | 62 | SB-538 |
| petawise.com | 61 | SB-367 |
| wire.tech | 60 | SB-077 |
| dmsimfg.com | 60 | SB-528 |
| harting.com | 60 | SB-1113 |
| wirewerks.com | 57 | SB-330 |
| luckyjoint.com.sg | 57 | SB-320 |
| motherwell.net.au | 57 | SC-3023 |
| gwsecurityusa.com | 57 | SB-028 |
| enssecurity.com | 56 | SB-900 |
| tkhsecurity.com | 55 | SB-564 |
| duxnet.co.za | 55 | SC-1255 |
| maxcomcorp.com | 54 | SB-012 |
| dasannetworks.com | 54 | SB-936 |
| ubiqnet.co.kr | 54 | SB-509 |
| lightem.com | 54 | SC-2542 |
| deonet.co.kr | 54 | SB-144 |
| addpac.com | 54 | SC-140 |
| scoop.co.za | 54 | SC-390 |
| elpknew.com | 54 | SC-133 |
| ksm.com.au | 53 | SB-1077 |
| elimopt.co.kr | 52 | SB-494 |
| enercon.co.il | 52 | SB-1067 |
| texim-europe.com | 51 | SC-986 |
| hdcabling.co.za | 51 | SC-365 |
| davantel.com | 51 | SB-692 |
| abctech.cz | 51 | SB-519 |

## 关联到 Saga Clients 的往来

- 命中客户编号 1609 个：A 63 / B 720 / C 826；明细见 `clients_link.json`、`contacts.csv`

## 附件类型

| 扩展名 | 个数（去重后） | 抽到正文 | 仅元数据 | 失败 | 跳过 |
|---|---|---|---|---|---|
| .png | 112 | 36 | 30 | 0 | 46 |
| .pdf | 99 | 99 | 0 | 0 | 0 |
| .jpg | 70 | 28 | 32 | 0 | 10 |
| .docx | 28 | 28 | 0 | 0 | 0 |
| .xlsx | 12 | 12 | 0 | 0 | 0 |
| .pptx | 5 | 5 | 0 | 0 | 0 |
| .xls | 3 | 3 | 0 | 0 | 0 |
| .gif | 3 | 1 | 1 | 0 | 1 |
| .doc | 2 | 2 | 0 | 0 | 0 |
| .bz2 | 1 | 0 | 0 | 0 | 1 |
| .txt | 1 | 1 | 0 | 0 | 0 |
| .rar | 1 | 0 | 1 | 0 | 0 |
| .jpeg | 1 | 0 | 1 | 0 | 0 |
| (无) | 1 | 0 | 0 | 0 | 1 |

## 解析失败（0）

无。

## 附件抽取失败（0）

无。

## 运行记录

- {"started": "2026-10-24T02:22:16Z", "limit": 0, "bulk_mode": "full", "attach": true, "ocr": true, "more_batches": false, "ended": "2026-10-24T03:00:45Z", "messages_this_run": 20521, "stopped_early": false}
- {"started": "2026-10-24T04:38:02Z", "limit": 0, "bulk_mode": "full", "attach": true, "ocr": true, "more_batches": false, "ended": "2026-10-24T04:55:57Z", "messages_this_run": 20521, "stopped_early": false}
