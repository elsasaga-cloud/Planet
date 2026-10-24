# Gmail（a 邮箱）Takeout 全量入库 · 覆盖率报告

- 生成时间：2026-10-24T03:00:45Z；状态：**done**；本邮箱地址：a.sagatelecom@gmail.com
- 来源：1 个文件，合计 13.37 GB：`All_mail_Including_Spam_and_Trash-002_1_.mbox` 13.37 GB
- 批次 1：1 个文件 / mbox 条目 1 个 / 流总长 13.37 GB，已处理到偏移 13.37 GB，20,521 封，✅ 完成
- 规则：**full** = 全文（非群发 / 本邮箱发出 / 本邮箱回过的线程 / 对方是 Saga Clients 里的客户 / 加星 / 重要）；**snippet** = 群发与通知类只留头部 + 前 600 字；附件按 sha256 去重抽正文（≤25 MB，文档类；图片 OCR=开）
- 原件备份：`All_mail_Including_Spam_and_Trash-002_1_.mbox` → Release `gmail-a-20261024` 7 卷 ✅

## 总量

| 指标 | 数 |
|---|---|
| messages | 14,847 |
| full | 14,847 |
| snippet | 0 |
| out | 14,500 |
| in | 347 |
| bulk | 139 |
| with_client | 14,692 |
| parse_err | 0 |
| attachments | 16,017 |
| att_unique | 339 |
| att_ok | 215 |
| att_meta | 65 |
| att_fail | 0 |
| att_skip | 59 |
| text_chars | 10,615,196 |
| att_chars | 3,406,210 |

## 按年

| 年 | 封数 | 发出 | 收到 | 全文 | 群发 |
|---|---|---|---|---|---|
| 2025 | 6,146 | 5,983 | 163 | 6,146 | 62 |
| 2026 | 8,701 | 8,517 | 184 | 8,701 | 77 |

## 标签（前 30）

| 标签 | 封数 |
|---|---|
| Archived | 14,782 |
| Sent | 14,480 |
| Opened | 1,011 |
| Replied | 486 |
| Daily | 359 |
| Important | 308 |
| Category Personal | 267 |
| Category Updates | 104 |
| Trash | 45 |
| Unread | 23 |
| Category Promotions | 17 |
| Drafts | 16 |
| Template Response | 16 |
| Inbox | 2 |
| Starred | 1 |

## 对方域名（前 40，排除本邮箱与免费邮箱）

| 域名 | 封数 | 客户编号 |
|---|---|---|
| netas.com.tr | 265 | SB-473 |
| nsidistribution.com | 90 | SB-553 |
| larch-networks.com | 88 | SB-318 |
| iacontrol.co.za | 78 | SC-368 |
| powertec.com.au | 60 | SC-2271 |
| dcbnet.com | 57 | SC-027 |
| vostok.ae | 53 | SC-1221 |
| patton.com | 53 | SB-854 |
| digisys.fr | 52 | SC-1252 |
| qtech.ru | 50 | SB-951 |
| iotsistem.com | 48 | SA-074 |
| wirewerks.com | 48 | SB-330 |
| dss-kuwait.com | 48 | SB-529 |
| telco.ge | 48 | SC-1489 |
| deps.ua | 48 | SC-2493 |
| a2s.pl | 47 | SB-389 |
| itmsystems.net | 46 | SB-842 |
| infinitecables.com | 46 | SB-538 |
| petawise.com | 46 | SB-367 |
| wire.tech | 45 | SB-077 |
| dmsimfg.com | 45 | SB-528 |
| enssecurity.com | 45 | SB-900 |
| silvernet.com | 44 | SB-862 |
| enercon.co.il | 44 | SB-1067 |
| gogreenit.net | 42 | SA-012 |
| luckyjoint.com.sg | 42 | SB-320 |
| lightem.com | 42 | SC-2542 |
| tkhsecurity.com | 42 | SB-564 |
| gwsecurityusa.com | 42 | SB-028 |
| scoop.co.za | 42 | SC-390 |
| duxnet.co.za | 42 | SC-1255 |
| maxcomcorp.com | 40 | SB-012 |
| ubiqnet.co.kr | 40 | SB-509 |
| hdcabling.co.za | 39 | SC-365 |
| davantel.com | 39 | SB-692 |
| dasannetworks.com | 38 | SB-936 |
| deonet.co.kr | 38 | SB-144 |
| elpknew.com | 38 | SC-133 |
| inscapedata.com | 36 | SB-359 |
| winstonele.com | 36 | SB-876 |

## 关联到 Saga Clients 的往来

- 命中客户编号 1510 个：A 61 / B 713 / C 736；明细见 `clients_link.json`、`contacts.csv`

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
