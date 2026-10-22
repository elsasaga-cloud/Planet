# Drive《SmartByte》全量入库 · 覆盖率报告

- 生成时间：2026-10-22T02:10:53Z；索引：2385 个文件（5.73 GB），manifest：1765 条
- 状态含义：**ok** = 抽到正文（Word 段落+表格 / Excel 逐行 / PDF 逐页(或 OCR) / PPT 逐页 / 图片 OCR 有字）；**meta** = 只有元数据+缩略图（无文字的图片/视频/设计源文件，或空文档）；**dup** = 与另一文件 sha256 完全相同，指向 same_as；**fail** = 下载或解析失败（见下表）；**pending** = 本次未处理
- 原件备份：GitHub Release `drive-smartbyte-20261022`（私有仓库，按顶层文件夹分卷 zip）

## 按类型

| 类型 | ok | meta | dup | fail | pending | 合计 |
|---|---|---|---|---|---|---|
| 图片 | 104 | 276 | 898 | 0 | 447 | 1725 |
| Word | 417 | 1 | 3 | 0 | 111 | 532 |
| PDF | 38 | 0 | 0 | 0 | 40 | 78 |
| Excel | 14 | 0 | 1 | 1 | 11 | 27 |
| 视频 | 0 | 4 | 0 | 0 | 5 | 9 |
| Publisher 排版源文件 | 4 | 0 | 0 | 0 | 0 | 4 |
| PPT | 0 | 0 | 0 | 0 | 3 | 3 |
| CorelDRAW 设计稿 | 2 | 0 | 0 | 0 | 0 | 2 |
| DXF 工程图 | 1 | 0 | 0 | 0 | 1 | 2 |
| XMind 思维导图 | 1 | 0 | 0 | 0 | 0 | 1 |
| 压缩包 | 0 | 0 | 0 | 0 | 1 | 1 |
| Photoshop 源文件 | 0 | 0 | 0 | 0 | 1 | 1 |

## 按顶层文件夹

| 文件夹 | ok | meta | dup | fail | pending | 合计 | 备份 |
|---|---|---|---|---|---|---|---|
| (root) | 19 | 0 | 0 | 0 | 0 | 19 | ✅ smartbyte_drive_root_part01.zip |
| 工业管理 | 219 | 69 | 590 | 0 | 0 | 878 | ✅ smartbyte_drive_industrial_managed_part01.zip, smartbyte_drive_industrial_managed_part02.zip |
| 工业非管理 | 72 | 126 | 253 | 0 | 0 | 451 | ✅ smartbyte_drive_industrial_unmanaged_part01.zip |
| 商业管理 | 30 | 27 | 59 | 0 | 0 | 116 | ✅ smartbyte_drive_commercial_managed_part01.zip |
| MC | 30 | 41 | 0 | 1 | 0 | 72 | ✅ smartbyte_drive_media_converter_part01.zip |
| Managed Industrial Ethernet Switch_最新资料 | 152 | 0 | 0 | 0 | 0 | 152 | ✅ smartbyte_drive_managed_industrial_latest_part01.zip |
| Bypass | 10 | 0 | 0 | 0 | 0 | 10 | ✅ smartbyte_drive_bypass_part01.zip |
| User Manual | 8 | 0 | 0 | 0 | 0 | 8 | ✅ smartbyte_drive_user_manual_part01.zip |
| Certification | 23 | 0 | 0 | 0 | 0 | 23 | ✅ smartbyte_drive_certification_part01.zip |
| PCB Information | 4 | 18 | 0 | 0 | 0 | 22 | ✅ smartbyte_drive_pcb_information_part01.zip |
| Case | 2 | 0 | 0 | 0 | 0 | 2 | ✅ smartbyte_drive_case_part01.zip |
| 管理界面图 | 12 | 0 | 0 | 0 | 0 | 12 | ✅ smartbyte_drive_ui_screenshots_part01.zip |
| 组合图 | 0 | 0 | 0 | 0 | 7 | 7 | — |
| 素材 | 0 | 0 | 0 | 0 | 11 | 11 | — |
| Factory Information | 0 | 0 | 0 | 0 | 32 | 32 | — |
| 暂时不用的 | 0 | 0 | 0 | 0 | 570 | 570 | — |

## 失败清单（1）

| 路径 | 类型 | 大小 | 错误 |
|---|---|---|---|
| SmartByte/MC/Price List.xlsx | Excel | 2328576 | BadZipFile: File is not a zip file |

## 仅元数据的非图片文件（1）

| 路径 | 类型 | 抽取方式 | 说明 |
|---|---|---|---|
| SmartByte/工业管理/源信息/工业级管理型中性产品图片 & 结构尺寸/6系/24+4-rack mount/中性机械结构图/缺AC 品字尾 + DC 机型 结构图.doc | Word | soffice→docx→python-docx(段落+表格+文本框+页眉页脚) |  |

## 体量

- 抽取正文合计 9,206,564 字符；图片 OCR 有字 104 张；缩略图 390 张
- 运行记录：[{"started": "2026-10-22T01:55:11Z", "todo": 2385, "workers": 6, "backup": true, "ocr": true}]
