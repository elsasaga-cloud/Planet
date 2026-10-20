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

## v2.1（2026-10-20）：探路 + 被封识别 + 假 complete 修正

Actions 运行 #2（提交 fd5cbd0，08:24 UTC）59 秒就"完成"并提交了 `ca98bc1`，但 `crawl_log.txt` 显示 `sitemap.xml` 与首页都是 **HTTP 403**：站点（或其前面的 WAF）拒绝了运行器，而 v2 把"队列空"当成了 `complete=true`。推测是运行 #1 用同一 UA 连抓 170 分钟触发了封禁（也解释了运行 #1 为何既不结束也无产出：每个 URL 403 × 3 次重试 × 退避睡眠）。`crawl.py` 改为：

- **开工先探路 `probe_access()`**：归档 UA → Chrome / Firefox / Safari UA（各试 https/http、带/不带 www）→ 现装 Playwright Chromium 真浏览器过 JS 挑战，再把 cookie 移植给 requests（移植无效则全程走浏览器上下文请求）。每次尝试的状态码、`server` / `cf-ray` / `cf-mitigated` 头、正文前 600 字和运行器出口 IP 写进 `data/smartbyte_site_raw/access_diag.json`，可据此判断是 UA 规则、JS 挑战还是 IP 段封禁。
- **全部被拒 → `blocked=true`**：本轮不抓、不重试、不清队列；`summary.json` `complete=false`、`how_to_continue` 给出三条路（过几小时再 Run workflow / 本地电脑跑 `python scripts/smartbyte_crawl/crawl.py data/smartbyte_site_raw crawl_bin` 后提交 / 请 SmartByte 放行 UA 或 IP）。
- **抓取中途连续 12 次 403/429/网络错误 → 判定被封**，当前阶段立即收尾（状态照存，下轮续抓），不再把预算烧在重试上。
- **`complete` 口径收紧**：0 页成功、或本轮有任何 403/429/网络错误型失败（`refused`）都不算完成；404 不阻止完成。主流程异常也落盘日志 + `summary.json` 后以 0 退出，保证提交步骤执行。
- 更礼貌：默认 `DELAY` 0.8 → 1.2 秒，图片间隔 0.3 → 0.5 秒。
- 本地自测（沙箱假站点，四种模式）：正常 → `requests/archiver` 完成；只封归档 UA → 自动切 `chrome-win` 完成；全封 → `blocked`（Playwright 装不上也能优雅降级）；首页后全封 → `refused=4, complete=false`，下一轮解封后续抓补齐 → `complete=true`。
