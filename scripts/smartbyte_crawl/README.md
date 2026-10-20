# SmartByte 官网整站归档（T15）

- `crawl.py`：归档器。BFS 抓取 www.smartbyte-switch.com 全部同域页面（起点 sitemap.xml + 首页），原样保存 HTML 到 `data/smartbyte_site_raw/html/`，附件（规格书等）下载后用 pdftotext 抽文本到 `data/smartbyte_site_raw/datasheet_text/`，PDF 总量 ≤60 MB 时一并入库到 `datasheets/`；图片只进构建产物/Release，不入 git。三份清单：`pages_manifest.jsonl` / `downloads_manifest.jsonl` / `images_manifest.jsonl`，汇总 `summary.json`，日志 `crawl_log.txt`。
- `smartbyte-crawl.yml`：GitHub Actions 工作流。**代理的 GitHub 连接没有 `workflows` 权限**（推送被拒：`refusing to allow a GitHub App to create or update workflow … without workflows permission`），所以需要 Simon 在 GitHub 网页把它保存为 `.github/workflows/smartbyte-crawl.yml`（分支 `arena/3f35b9b3-planet`）；保存后自动运行，约 15–30 分钟，结果以一条 `T15: SmartByte 官网整站原始归档` 提交回本分支，二进制在 Actions 构建产物与 Release `smartbyte-site-YYYYMMDD`。
- 之后由 `build.py`（待写）把原始 HTML 解析成：每型号一个 Markdown（`docs/smartbyte/products/`）、全量型号索引 CSV、品类/政策/新闻页 Markdown。
- 礼貌抓取：robots.txt 为 `Allow: /`；UA 自报 `SagaTelecom-site-archiver`；每请求间隔 0.8 s；只抓同域。
