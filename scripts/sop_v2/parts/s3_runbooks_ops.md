## 6. 剧本 R13–R25 · 入库 / 对外 / 基础设施类

### R13 · 「啥都入库，不要漏掉」通用入库（Simon 给了任何材料）

- **触发**：Simon 丢来文件 / 链接 / 聊天截图 / 口述事实。
- **判定去哪**（❓ D-06 入库落点表）：

| 材料 | 落点 | 之后 |
|---|---|---|
| 客户往来（邮件 / WA 截图 / PI） | `data/saga_clients/research/<编号>.json` 的 `mail_review.facts[{date, dir(来/去/查), who, quote, why, k}]`；PI 另加 `data/pi_orders/*.csv` 一行 | R02 |
| 价格 / 供应商报价 | `data/价格主表.csv` 或 `data/价格主表_HRUI.csv`（经 `scripts/pricing.py` / `pricing_hrui.py` 重生成，⛔ 不手改 CSV）+ `docs/reference/价格表_*.md` | 全景信息包 §8.5 锚价同步 |
| 公司 / 品牌口径、Simon 的理念 | `docs/reference/Saga*.md` 对应文件追加小节（带日期 + 轮次） | 全景信息包 parts 同步 |
| 规则 / 决定 | `docs/requirements/用户要求总账.md` PR 行 + `docs/rules/*.md` | 本书对应剧本 |
| 供应商资料 | `docs/suppliers/<供应商>/` | — |
| 大文件（xlsx / pdf / 视频 / 压缩包） | 走 R14；原件进仓（Git 可承受），超大文件只留索引 | — |
| 微信聊天 / 截图 | `scripts/wechat_ocr.py` / `wechat_transcript.py` → `docs/drive/…` 文本；事实再按上表分流 | — |

- **铁律**：每条事实带 `quote + url/来源 + date`；没来源写「待补证」；中文记录，英文只出现在对外稿；不改 V0 文件，新版本 = 新文件。
- 🏁 Simon 给的每一件东西都能在仓库里 `grep` 到；README 写「入库 N 件：…」。

### R14 · Drive / 大文件入库（走 Actions 运行器）

- **为什么**：沙箱不能访问 Drive 直链 / 外网；大文件由 GitHub Actions 运行器下载并提交。
- **步骤**（细节与原文模板在 `docs/教程_云盘大文件入库管道_给其他Agent_2026-10-24.md`、`scripts/drive_ingest/操作步骤.md`）：
  1. Simon 把文件夹设「知道链接的任何人 · 查看者」（这一步只能他做 → 写进报告「你要做啥」）。
  2. 把 Drive 文件夹 ID 写进 `scripts/drive_ingest/` 的清单；workflow `.github/workflows/drive-smartbyte-ingest.yml`（⛔ 沙箱推不动 `.github/workflows/`，改 workflow 必须 Simon 在 GitHub 网页粘贴）。
  3. Simon 点 Run workflow → 等机器人提交 → `git pull --rebase`。
  4. 产物索引：`python3 scripts/drive_smartbyte_index.py` / `drive_r3_index.py` → `docs/drive/` 下 MUST-KNOW 摘要；大文件事实按 R13 分流。
- 🏁 `docs/drive/` 有索引 + 摘要；原件路径在 README 项里；Drive 内容入仓后 Simon 才删 Drive（T23/T28）。

### R15 · Gmail 查证（三个邮箱怎么查）

| 邮箱 | 能不能连 | 怎么查 |
|---|---|---|
| E（Elsa）| 可以：本会话 `list_connector_tools gmail` → 用其搜索工具 | 只查、不发；结果按 R13 落 `mail_review.facts` |
| S（Simon 主） | ⛔ 不能连 Arena（T28-U2，别再建议） | 已入库：`data/gmail_s/messages/<年>/<年-月>.jsonl` + `contacts.csv` + `报价史.csv` + `attachments/`；`grep -ril "<域名>" data/gmail_s/messages` |
| A（Simon 副） | 同上 | `grep -ril "<域名>" data/gmail_a/messages`（2025-03~08 分片待补） |

- 更新摘要：▶ `cd scripts/saga_clients && python3 gmail_digest.py | tail -1` → `data/saga_clients/gmail_digest.json`（render 用）。
- ⛔ 不把邮件正文整段贴进客户 MD；只摘 `quote ≤ 300 字 + 日期 + 方向`；自动回复 / 退信 / 订阅类只记状态不记内容。
- 🏁 每条 facts 有 `k`（线索键，如 `gmail_s 2024-11-09`）。

### R16 · 写一个新脚本 / 一次性批处理（派生脚本规范）

| # | 规矩 | 怎么做 |
|---|---|---|
| 1 | 位置 | 批处理：`scripts/saga_clients/<系列>_<编号>.py`（如 `lt_review_batches/lt_r_010.py`、`registry_batches/b124.py`、`patches/batch124_kp.py`）；跨库：`scripts/lt_*.py`；工具：各库目录 |
| 2 | 文档串 | 第一段写：任务编号（T29-Uxx）、日期、Simon 原话、输入 / 输出路径、幂等说明 |
| 3 | 幂等 | 写前查「已有同 TAG / 同批次 / 同 fetched_at」→ 跳过；**跑两遍第二遍 0 写入** |
| 4 | 只动真相源 | 改 JSON / CSV / overrides；⛔ 不碰 MD、`entities.json`、`客户主表.csv`、`docs/发送包` |
| 5 | 读写编码 | CSV `encoding='utf-8-sig', newline=''`；JSON `ensure_ascii=False, indent=1` 跟原文件风格 |
| 6 | 导入 | ⛔ `sys.path.insert(scripts/saga_clients)`（`calendar.py` 遮蔽标准库）→ 用 `importlib.util.spec_from_file_location` |
| 7 | 语法自检 | `python3 -c "import ast;ast.parse(open('<文件>',encoding='utf-8').read())"` |
| 8 | 试运行 | 有 `--dry` 先 `--dry`；测试产物写 `/tmp`；不要在仓库留 `/tmp` 路径 |
| 9 | 日志 | 结尾 `print` 一行统计（写入 N / 跳过 M），便于台账引用 |
| 10 | 收尾 | 清 `__pycache__`；脚本本身提交（可追溯）；README 项写脚本路径 |

- 🏁 两遍幂等 + 渲染链全绿 + 脚本已提交。

### R17 · 台账（四配方见 §3.1）

补充边界：

- 对话全记录：**逐字**，含错别字；不翻译、不润色；Agent 要点里写文件路径与数字。
- 总账 INH-01…17 是继承规则表（行 107–133 附近），⛔ 不改；新规则另起 PR 行并注明「补充 INH-xx」。
- `变更日志.md` 只由 `scripts/changelog.py` 生成（从 git log），⛔ 手改。
- 规程 / 方案类文档有「进度」节的（`公司底数_作业规程.md` §3、`C池三闸筛选_方案` 进度），每轮追加一行 `- 下一轮（…）`/ 批次行。

### R18 · Git：沙箱恢复、冲突、机器人并发

**A. 沙箱被重置**（症状：`git log` 只剩 `2199cbf Initial commit`，脚本 / 数据都在但 pip 包没了）
```
cd /home/user/Planet
git fetch -q origin arena/3f35b9b3-planet
rm -f .git/index.lock
git reset -q --hard origin/arena/3f35b9b3-planet && git clean -qfd
git log --oneline -1           # ✅ 应是你上次推送的哈希
pip install -q --break-system-packages dnspython markdown   # 需要时
```
⛔ 只有在「本地没有任何未推送工作」时才 `reset --hard`；否则先 `git stash` / 先提交。

**B. push 被拒（non-fast-forward）** = Actions 机器人推了快照
```
git fetch -q origin arena/3f35b9b3-planet
git pull -q --rebase origin arena/3f35b9b3-planet   # 机器人只碰 data/saga_clients/site_snapshots、data/customer_watch
git push -q origin arena/3f35b9b3-planet
git ls-remote origin arena/3f35b9b3-planet | cut -c1-12
```
冲突时：机器人文件取 `theirs`（`git checkout --theirs <文件> && git add <文件> && git rebase --continue`），自己的台账取 `ours` 后重新追加。

**C. 永远不做**：切换 / 新建 / 推送到别的分支；与 `main` rebase / merge（`main` 是孤儿分支）；`git push --force`；删 `.git`；提交 `node_modules` / `__pycache__` / `/tmp` 产物；`git add` 含密钥文件。

**D. 提交信息格式**：`T29-Uxx：<主题>；<关键数字>；<台账四件>`；含 `$` 用单引号包住整段。

### R19 · Q 立项（不问 Simon 的问题怎么处理）

1. 判断：这个问题**是否影响本轮方向**？不影响 → 按常识做，收工报告「顺带」一句话。影响 → 下一步。
2. 写默认值：默认 = 最保守、可逆、不花 Simon 时间的那个（例：拿不准等级 → C 储备；拿不准价 → 报档位价并标「报前核」；拿不准发不发 → 不发）。
3. 按 §3.1 配方 C 追加 `Q-NN` 行；在执行处留痕（研究档 `notes` / 总账 PR 行写「按 Q-NN 默认」）。
4. 报告里最多提**一个**问题，且先给默认：「我先按 X 做了，你要是想 Y 说一声」。
- ⛔ 一轮问三个问题；「请确认」式空转；把 Simon 已经明说的事再问一遍（先 `grep` 对话全记录）。

### R20 · 写一封对外信稿（英文）

- **前置**：读该户 MD 全文 + `mail_review`（绑定 / 情况 / 需求 / 断点 / 下一动作）+ 上次去信日期 + 国别窗口（`docs/各国发信窗口与来询季节_2026-10-27.md`）。
- **骨架**（≤ 120 词）：① 一句对方的具体事实（来自 facts，不吹）→ ② 一款型号 + 一个价（R21 格式）→ ③ **只问一个问题** → ④ 签名 `Saga Telecom - sagatele.com`（无电话、无 s. 邮箱）。
- **自检清单（逐条勾）**：
  1. 型号 ∈ 价格主表 `Saga对应型号` ∪ HRUI 型号 ∪ STH 列表；
  2. 价格 = 档位价（分销 20 / 集成 25 / OEM 30），格式 `$xx USD EXW（快照日期，15 天有效）`，Realtek 线从 `data/价格主表_HRUI.csv` 取；
  3. 无禁词：list price / in stock / free samples / trading company / OEM Factory / NDAA / TAA / UL / GSA / general agent / we manufacture / Marvell ecosystem / SONiC / ONIE / cheap / best price / leading manufacturer / ERPS / CLI / watchdog / Elsa；
  4. 不提竞品名；不说「我们查了你的登记」；非 EU 不写 UKCA（只 GB）；非欧 → DAP / FOB 深圳；
  5. 样品付费；MOQ 1；T/T 50/50；
  6. 一封一问；全英文；称呼用具名 KP（没有就 `Hello <公司> team`）。
- **落点**：Saga 户 → `mail_review.draft_en{subject, body}`；External → 研究卡 `draft_en`；然后 R02 / External render + `audit_ab.py`（信稿项 hard 0）。Agent **不发信**，发送包由 R25 汇总给 Simon。
- 🏁 `audit_ab.py` 无该户 hard 项；信稿出现在 MD「信稿」节。

### R21 · 报价计算（任何价格数字出口前）

1. ▶ `grep -i "<型号>" data/价格主表.csv data/价格主表_HRUI.csv | head -3` → ✅ 找到 `CNY未税` 与三档 USD（已按汇率 6.69 @2026-10-17 算好）。
2. 档位：分销商 20% ｜ 集成商 25% ｜ OEM 30%；地板：Realtek ≥ 20 / Marvell ≥ 25 / CENTEC ≥ 35；封顶 30%（两套并存，取满足地板的那档）。
3. 手算公式：`USD = CNY × (1 + 档位) ÷ 6.69`，取 1 位小数；写法 `$181.2 USD EXW（2026-10-17，15 天有效）`。
4. 找不到型号 → 不报数，写「报前核」+ 立 Q；STH（CENTEC）用 `docs/reference/CENTEC_产品表与报价锚_2026-10-24.md` 锚价区间。
- ⛔ 凭记忆写价；告诉 Simon「去问 Peter / HRUI」；RMB 报价（国内单只走私账 → 待 Simon）；2.5G 机型（等 SB-263）。

### R22 · 文档交付（MD + HTML + 预览）

- **模式**（抄 `scripts/saga_intro/build.py`）：内容拆成 `parts/*.md` → `build.py` 拼接 + 自动表 + 头部（标题 / UTC+北京时间 / `git rev-parse --short HEAD`）+ `## ` 目录 → 写 `docs/<名>_<日期>.md` 与自包含 `.html`（内联 CSS、无外链脚本）。本书自身的生成器：`scripts/sop_v2/build.py`。
- **步骤**：
  1. ▶ `pip install -q --break-system-packages markdown`（没网 / 装不上则 build 自动降级为内置转换）。
  2. 写 / 改 parts；▶ `python3 scripts/<生成器>/build.py` → ✅ 打印 chars / lines / tables 两边一致。
  3. ▶ `grep -c "<table" docs/<名>.html` 与 MD 表数核对；`grep -c "<script" docs/<名>.html` → 0。
  4. 预览：`start_process` `python3 -m http.server 8080 --bind 0.0.0.0 --directory /home/user/Planet/docs`；`present_file docs/<名>.html`。
- ⛔ 手改生成出来的 MD / HTML；覆盖旧版本（新版本 = 新文件名，旧版保留并在新版头部链到旧版）；无时间戳。
- 🏁 MD 与 HTML 同日同哈希；README 项写两个路径 + 生成器路径。

### R23 · GitHub Actions 检查与触发

| workflow | 干什么 | 触发 |
|---|---|---|
| `customer-watch.yml` | 抓监控源 + 顺手补官网快照（`scripts/web_watch/watch.py` → `data/customer_watch/`、`data/saga_clients/site_snapshots/`），自动提交到本分支 | cron 每晚 02:23Z；Simon 手动 Run workflow（可选 layer / ALL） |
| `saga-clients-snapshot.yml` | 全量官网快照（`site_snapshot.py`） | 手动 |
| `drive-smartbyte-ingest.yml` | Drive 大文件入库 | 手动 |
| `smartbyte-crawl.yml` | SmartByte 官网抓取 | 手动 |

- **沙箱能做的**：`python3 scripts/web_watch/watch.py --selftest`（✅ 最后一行 `selftest OK · customers=1405 layers={…} sources=2987`）；看结果 `git log --oneline origin/arena/3f35b9b3-planet -5 | grep -i "actions\|watch\|snapshot"`；读 `data/customer_watch/当前状态.md` / `变化日志_AB.md`。
- **沙箱不能做的**：`gh`（403）；推 `.github/workflows/`；用 curl 访问外网。要改 workflow → 把完整 YAML 写进 `docs/` 让 Simon 网页粘贴（报告「你要做啥」）。
- 🔁 机器人没提交：看 Actions 页（Simon）；常见原因 = 没有变化（正常）或超时；不要连续手动触发多次。
- 🏁 本轮消费了最新机器人提交（R11），且报告里写明「快照 N / 成功 M / 失败 K」。

### R24 · 两月监控轮（P 池 / 长期客户群巡检）

1. ▶ `python3 scripts/web_watch/checklist.py --date <巡检日>` → `docs/P池_巡检清单_<日>.md`（六格：官网 / 社媒 / 新闻·展会 / 招聘 / GitHub / MX）。
2. 自动层：`data/customer_watch/变化日志_AB.md` 近 60 天；GitHub 存在性 `data/saga_clients/github_presence.json`（`scripts/github_watch/`）。
3. 人工层：每户按清单勾；有动静（换品牌 / 招聘网络工程师 / 新展会 / 官网改版 / 域名死）→ 回写 `P池_巡检表_*.csv` 的「上次巡检 / 备注」→ 需要升降级走 R04。
4. 周期：下一次 2026-12-28；覆盖面要广（社媒、GitHub、官网、展会）。
- 🏁 巡检表每户「上次巡检」= 本次日期；动静户进 R06 / R05。

### R25 · 周发送包 / 跟进总台

- ▶ `python3 scripts/external_clients/board.py --date <周一日期> | tail -1` → `docs/跟进总台.md` + `docs/发送包/<ISO周>.md`（只读 JSON，⛔ 手改）。
- 发前核：每封在 R20 自检表下过一遍；称呼人名核一眼；窗口按国别（FR 周四 12–14 之类）。
- Agent 不发信；报告写「本周 N 封在 `docs/发送包/<周>.md`，复制即发；Elsa 首触未定 → E 箱不发」。
- 🏁 发送包里每封都有：收件 / 从哪个箱 / 主题 / 正文 / 档案路径。
