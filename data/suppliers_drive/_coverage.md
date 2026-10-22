# Drive《SmartByte》全量入库 · 覆盖率报告

- 生成时间：2026-10-22T08:43:40Z；索引：453 个文件（1.2 GB），manifest：189 条
- 状态含义：**ok** = 抽到正文（Word 段落+表格 / Excel 逐行 / PDF 逐页(或 OCR) / PPT 逐页 / 图片 OCR 有字）；**meta** = 只有元数据+缩略图（无文字的图片/视频/设计源文件，或空文档）；**dup** = 与另一文件 sha256 完全相同，指向 same_as；**fail** = 下载或解析失败（见下表）；**pending** = 本次未处理
- 原件备份：GitHub Release `drive-suppliers-20261022`（私有仓库，按顶层文件夹分卷 zip）

## 按类型

| 类型 | ok | meta | dup | fail | pending | 合计 |
|---|---|---|---|---|---|---|
| 图片 | 10 | 112 | 51 | 0 | 194 | 367 |
| Word | 3 | 0 | 0 | 0 | 63 | 66 |
| PPT | 12 | 0 | 0 | 0 | 2 | 14 |
| PDF | 1 | 0 | 0 | 0 | 4 | 5 |
| 视频 | 0 | 0 | 0 | 0 | 1 | 1 |

## 按顶层文件夹

| 文件夹 | ok | meta | dup | fail | pending | 合计 | 备份 |
|---|---|---|---|---|---|---|---|
| (root) | 9 | 0 | 0 | 0 | 0 | 9 | ✅ smartbyte_drive_root_part01.zip |
| STH100G | 0 | 0 | 0 | 0 | 6 | 6 | — |
| STH10G | 4 | 38 | 24 | 0 | 0 | 66 | ✅ smartbyte_drive_STH10G_part01.zip |
| STH2.5G | 4 | 14 | 4 | 0 | 0 | 22 | ✅ smartbyte_drive_STH2.5G_part01.zip |
| STH25G | 2 | 11 | 1 | 0 | 0 | 14 | ✅ smartbyte_drive_STH25G_part01.zip |
| STH400G | 0 | 0 | 0 | 0 | 8 | 8 | — |
| STH5G | 3 | 21 | 3 | 0 | 0 | 27 | ✅ smartbyte_drive_STH5G_part01.zip |
| STH800G | 2 | 3 | 0 | 0 | 0 | 5 | ✅ smartbyte_drive_STH800G_part01.zip |
| XLite | 2 | 25 | 19 | 0 | 0 | 46 | ✅ smartbyte_drive_XLite_part01.zip |
| Commercial Ethernet Switch | 0 | 0 | 0 | 0 | 66 | 66 | — |
| Commercial Managed Switch | 0 | 0 | 0 | 0 | 66 | 66 | — |
| Commercial PoE Switch | 0 | 0 | 0 | 0 | 101 | 101 | — |
| Commercial Web Managed Switch | 0 | 0 | 0 | 0 | 17 | 17 | — |

## 失败清单（0）

无。

## 仅元数据的非图片文件（0）

无。

## 体量

- 抽取正文合计 3,652,396 字符；图片 OCR 有字 10 张；缩略图 122 张
- 运行记录：[{"started": "2026-10-22T08:37:54Z", "todo": 453, "workers": 6, "backup": true, "ocr": true}]
