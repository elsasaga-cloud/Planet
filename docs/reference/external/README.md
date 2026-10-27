# docs/reference/external · 外部三仓搬入的小件

| 文件 | 来源 | 用途 |
|---|---|---|
| `mikrotik-info_死路与死链备案_2026-09.md` | mikrotik-info@a60f11f8 `死路与死链备案_2026-09.md` | 他们踩过的坑，查源前先看 |
| `Edgecore_EOL替换矩阵.md` | Edgecore@729187d `docs/sales/EOL替换矩阵.md` | Edgecore 停产型号 → Saga 替换（用前对照 `data/价格主表.csv`） |
| `Edgecore_认证关税速查表_2026-10-18.md` | Edgecore@729187d `docs/sales/认证关税速查表_2026-10-18.md` | 27 国认证/关税速查（冲突以本库 docs/reference 为准） |
| `CCTV-PoE_Agent搜索客户方法论.md` | CCTV-PoE@9be1416 `Agent搜索客户方法论.docx`（转文本） | Simon 汇编的找客户方法论，供第 2 步研究参考 |

原件搬到仓库根目录（2026-10-27，来自 CCTV-PoE@9be1416）：`Price List_Marvell Based Commercial Managed Switch.xls`、`Price List_Realtek Based Commercial Switch.xls`、`Price List_Commercial Web Managed Switch.xls`、`洪瑞报价-欧林克 26818.xls`。
价格仍以 `data/价格主表.csv` / `data/价格主表_HRUI.csv` 与 ㉕ 规则为准，这些原件只做底账。

## 2026-10-27 关仓前清点补入（T29-U79）

三仓即将设为 private，可读件按仓搬入本目录（清点总表：`docs/external_repos/关仓前清点_2026-10-27.md`）：

| 目录 | 内容 |
|---|---|
| `Edgecore/` | `Edgecore客户数据库.xlsx`（渠道伙伴 198 / 案例客户 30 / 目标评估 60 / 重点联系 11；sheet 转 CSV 在 `data/external_repos/edgecore_xlsx/`）、`Edgecore_L2Plus_Switches.xlsx`；`原文/` = 37 个 md/csv/py（宪法-对话记录、用户要求总账、docs/sales 15、docs/intel 5、抓取脚本 2…） |
| `mikrotik-info/` | `客户分级跟进表_2026-09.xlsx`、`MikroTik_vs_SmartByte_替代对照表.xlsx`、`MikroTik_L2Plus_Switches.xlsx`；`原文/` = 35 个（根目录 24 份策略 MD、`客户名单_反向信号_2026-09.csv`、`docs/requirements/用户要求总账.md` 391 KB、`docs/evidence/客户溯源_A/B/C.md`、`docs/sales/A类_*`、抓取脚本） |
| `CCTV-PoE/` | `Agent搜索客户方法论.docx` 原件；`原文/` = 19 个（03 清单 1.2 MB、01/02/04、smartbyte 01–04、exhibition 6、README/SESSION-SUMMARY/AGENT-*） |

搬到仓库根目录的新二进制件（Planet 此前没有）：`Marvell Based CLI Manual.docx`、`Marvell Based Web Manual.docx`、`Saga Feature List_7.5.x_L2+.xlsx`、`Saga Feature List_7.5.x_L3.xlsx`、`Price List_Marvell Based Industrial Unmanaged Switch.xls`、`SmartByte Managed Industrial Ethernet switch  pricelist on CNY for Simon-20240227.xlsx`、`SmartByte managed Ethernet switch pricelist for Simon-20240516 更新.xlsx`。
三仓全部文本的压缩包：`data/external_repos/archive/`。原文夹里的价格 / 型号说法仍以 `data/价格主表.csv` 与 ㉕ 规则为准。
