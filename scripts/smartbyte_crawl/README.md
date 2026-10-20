# SmartByte 官网整站归档（T15）

- `crawl.py`：归档器。BFS 抓取 www.smartbyte-switch.com 全部同域页面（起点 sitemap.xml + 首页），原样保存 HTML 到 `data/smartbyte_site_raw/html/`，附件（规格书等）下载后用 pdftotext 抽文本到 `data/smartbyte_site_raw/datasheet_text/`，PDF 总量 ≤60 MB 时一并入库到 `datasheets/`；图片只进构建产物/Release，不入 git。三份清单：`pages_manifest.jsonl` / `downloads_manifest.jsonl` / `images_manifest.jsonl`，汇总 `summary.json`，日志 `crawl_log.txt`。
- `smartbyte-crawl.yml`：GitHub Actions 工作流。**代理的 GitHub 连接没有 `workflows` 权限**（推送被拒：`refusing to allow a GitHub App to create or update workflow … without workflows permission`），所以需要 Simon 在 GitHub 网页把它保存为 `.github/workflows/smartbyte-crawl.yml`（分支 `arena/3f35b9b3-planet`）；保存后自动运行，约 15–30 分钟，结果以一条 `T15: SmartByte 官网整站原始归档` 提交回本分支，二进制在 Actions 构建产物与 Release `smartbyte-site-YYYYMMDD`。
- 之后由 `build.py`（待写）把原始 HTML 解析成：每型号一个 Markdown（`docs/smartbyte/products/`）、全量型号索引 CSV、品类/政策/新闻页 Markdown。
- 礼貌抓取：robots.txt 为 `Allow: /`；UA 自报 `SagaTelecom-site-archiver`；每请求间隔 0.8 s；只抓同域。

## v2（2026-10-20）：墙钟预算 + 断点续抓

Actions 运行 #1（提交 edcef60，12:36 开始）在作业上限 170 分钟处被 GitHub 杀掉（页面显示 cancelled），而 zip / 上传 / 提交步骤都排在抓取之后，所以**什么都没落地**。`crawl.py` 改为：

- `TIME_BUDGET_MIN`（默认 140）：页面阶段最多用预算 55%，附件阶段累计 85%，图片阶段用满 100%；到点优雅收尾、照常写三份清单 + `summary.json` 并以 0 退出 → 后续 zip / upload-artifact / commit / release 一定执行。
- 断点续抓：`data/smartbyte_site_raw/crawl_state.json`（队列、已见集合、附件与图片清单、各轮记录）随清单一起提交回分支；下一轮（Actions 页 **Run workflow**，或再推一次 `crawl.py`）从队列继续，已抓成功的 URL 不重抓；网络失败 / 5xx 的页面自动重试，404 不重试。`summary.json` 的 `complete=true` 才算抓完，否则 `how_to_continue` 写明怎么续。
- 每 25 页 / 20 个附件 / 100 张图写一次盘；`crawl_log.txt` 跨轮追加；每条清单记录带 `run`（Actions 运行号）。上一轮抓到的二进制在上一轮的 Release / 构建产物里，清单里的 `run` 字段指明去哪一轮找。
- 本地自测：`CRAWL_HOST=127.0.0.1:8765 CRAWL_SCHEME=http TIME_BUDGET_MIN=0.04 python crawl.py out bin`，再用大预算跑第二遍验证续抓（已在沙箱用 14 页假站点验证：预算截停 → 续抓补齐 → 第三轮空跑）。
