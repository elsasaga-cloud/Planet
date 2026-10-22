# Drive《SmartByte》全量入库 · 覆盖率报告

- 生成时间：2026-10-22T12:25:33Z；索引：1461 个文件（3.3 GB），manifest：96 条
- 状态含义：**ok** = 抽到正文（Word 段落+表格 / Excel 逐行 / PDF 逐页(或 OCR) / PPT 逐页 / 图片 OCR 有字）；**meta** = 只有元数据+缩略图（无文字的图片/视频/设计源文件，或空文档）；**dup** = 与另一文件 sha256 完全相同，指向 same_as；**fail** = 下载或解析失败（见下表）；**pending** = 本次未处理
- 原件备份：GitHub Release `drive-r3-20261022`（私有仓库，按顶层文件夹分卷 zip）

## 按类型

| 类型 | ok | meta | dup | fail | pending | 合计 |
|---|---|---|---|---|---|---|
| 图片 | 12 | 38 | 0 | 0 | 1193 | 1243 |
| Word | 0 | 0 | 0 | 0 | 151 | 151 |
| PDF | 36 | 0 | 0 | 0 | 14 | 50 |
| 视频 | 0 | 9 | 1 | 0 | 1 | 11 |
| Excel | 0 | 0 | 0 | 0 | 5 | 5 |
| 配置 | 0 | 0 | 0 | 0 | 1 | 1 |

## 按顶层文件夹

| 文件夹 | ok | meta | dup | fail | pending | 合计 | 备份 |
|---|---|---|---|---|---|---|---|
| Anda Telecom 共享（副本，供入库） | 0 | 0 | 0 | 0 | 5 | 5 | — |
| MUST KNOW | 48 | 47 | 1 | 0 | 0 | 96 | ✅ smartbyte_drive_MUST_KNOW_part01.zip |
| Marvell Based Commercial Managed Switch | 0 | 0 | 0 | 0 | 164 | 164 | — |
| Marvell Based Industrial Managed Switch | 0 | 0 | 0 | 0 | 682 | 682 | — |
| Marvell Based Industrial Unmanaged Switch | 0 | 0 | 0 | 0 | 510 | 510 | — |
| Saga Telecom Resource Library | 0 | 0 | 0 | 0 | 4 | 4 | — |

## 失败清单（0）

无。

## 仅元数据的非图片文件（0）

无。

## 体量

- 抽取正文合计 844,345 字符；图片 OCR 有字 12 张；缩略图 59 张
- 运行记录：[{"started": "2026-10-22T12:21:15Z", "todo": 1461, "workers": 6, "backup": true, "ocr": true}]
