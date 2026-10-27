# 外部三仓文本全量归档（关仓前，2026-10-27）

Simon 关仓（转 private）前的最后快照。每个 `.tar.xz` = 该仓库该提交下 **全部 git 跟踪文本文件**（MD / CSV / JSON / PY / 配置），目录结构原样；二进制原件（xls/xlsx/docx/pdf）不在包里，已逐个比对哈希：与 Planet 已有文件相同的不再复制，新的已复制到 Planet 根目录或 `docs/reference/external/<库>/`（清单见 `docs/external_repos/关仓前清点_2026-10-27.md`）。

| 包 | 来源 | 内容 |
|---|---|---|
| `Edgecore_729187d_文本全仓.tar.xz` | elsasaga-cloud/Edgecore 分支 arena/6214ebb8-edgecore @ 729187d | 291 文件：profile/A|B|C、batch/ 25 轮研究 JSON、docs/、scripts/、宪法-对话记录 |
| `mikrotik-info_a60f11f8_文本全仓.tar.xz` | elsasaga-cloud/mikrotik-info 分支 arena/01a0c3ef-mikrotik-info @ a60f11f8 | 1,478 文件：客户名单 CSV、profile/A|B|C、batch/ 271 JSON、docs/evidence 溯源、docs/requirements 用户要求总账、scripts/ 80 |
| `CCTV-PoE_9be1416_文本全仓.tar.xz` | elsasaga-cloud/CCTV-PoE 分支 arena/01a0c908-cctv-poe @ 9be1416 | 142 文件：01–04、03 清单 2.7 万行、profile/ 106、smartbyte/、exhibition/ |

解包：`tar -xJf <包> -C <目录>`。沙盒里要查某户原文时从这里解，不再依赖 GitHub（mikrotik-info / CCTV-PoE 在 2026-10-27 12:17Z 已 404）。
