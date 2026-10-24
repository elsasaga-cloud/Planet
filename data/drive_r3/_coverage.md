# Drive《SmartByte》全量入库 · 覆盖率报告

- 生成时间：2026-10-24T03:34:07Z；索引：1461 个文件（3.3 GB），manifest：1461 条
- 状态含义：**ok** = 抽到正文（Word 段落+表格 / Excel 逐行 / PDF 逐页(或 OCR) / PPT 逐页 / 图片 OCR 有字）；**meta** = 只有元数据+缩略图（无文字的图片/视频/设计源文件，或空文档）；**dup** = 与另一文件 sha256 完全相同，指向 same_as；**fail** = 下载或解析失败（见下表）；**pending** = 本次未处理
- 原件备份：GitHub Release `drive-r3-20261022`（私有仓库，按顶层文件夹分卷 zip）

## 按类型

| 类型 | ok | meta | dup | fail | pending | 合计 |
|---|---|---|---|---|---|---|
| 图片 | 82 | 264 | 897 | 0 | 0 | 1243 |
| Word | 149 | 0 | 2 | 0 | 0 | 151 |
| PDF | 49 | 0 | 1 | 0 | 0 | 50 |
| 视频 | 0 | 10 | 1 | 0 | 0 | 11 |
| Excel | 3 | 0 | 2 | 0 | 0 | 5 |
| 配置 | 0 | 1 | 0 | 0 | 0 | 1 |

## 按顶层文件夹

| 文件夹 | ok | meta | dup | fail | pending | 合计 | 备份 |
|---|---|---|---|---|---|---|---|
| Anda Telecom 共享（副本，供入库） | 4 | 1 | 0 | 0 | 0 | 5 | ✅ smartbyte_drive_Anda_Telecom_part01.zip |
| MUST KNOW | 48 | 47 | 1 | 0 | 0 | 96 | ✅ smartbyte_drive_MUST_KNOW_part01.zip |
| Marvell Based Commercial Managed Switch | 27 | 38 | 99 | 0 | 0 | 164 | ✅ smartbyte_drive_Marvell_Based_Commercial_Managed_Switch_part01.zip |
| Marvell Based Industrial Managed Switch | 135 | 64 | 483 | 0 | 0 | 682 | ✅ smartbyte_drive_Marvell_Based_Industrial_Managed_Switch_part01.zip, smartbyte_drive_Marvell_Based_Industrial_Managed_Switch_retry202610240324_part01.zip |
| Marvell Based Industrial Unmanaged Switch | 65 | 125 | 320 | 0 | 0 | 510 | ✅ smartbyte_drive_Marvell_Based_Industrial_Unmanaged_Switch_part01.zip, smartbyte_drive_Marvell_Based_Industrial_Unmanaged_Switch_retry202610240327_part01.zip |
| Saga Telecom Resource Library | 4 | 0 | 0 | 0 | 0 | 4 | ✅ smartbyte_drive_Saga_Telecom_Resource_Library_part01.zip |

## 失败清单（0）

无。

## 仅元数据的非图片文件（1）

| 路径 | 类型 | 抽取方式 | 说明 |
|---|---|---|---|
| Drive第三轮/Marvell Based Industrial Unmanaged Switch/STI-050GE/6.jpg.baiduyun.uploading.cfg | 配置 | none | no extractor for .cfg |

## 体量

- 抽取正文合计 2,802,966 字符；图片 OCR 有字 82 张；缩略图 356 张
- 运行记录：[{"started": "2026-10-22T12:21:15Z", "todo": 1461, "workers": 6, "backup": true, "ocr": true, "finished": "2026-10-22T12:33:34Z", "processed": 1461}, {"started": "2026-10-24T03:23:19Z", "todo": 850, "workers": 6, "backup": true, "ocr": true, "finished": "2026-10-24T03:34:07Z", "processed": 850}]
