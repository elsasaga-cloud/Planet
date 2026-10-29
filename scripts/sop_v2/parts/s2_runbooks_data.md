## 4. 剧本骨架（每个剧本都长这样）

```
Rnn · 名字
目的 ｜ 触发（Simon 说了什么 / 什么状态下跑）｜ 前置检查 ｜ 步骤（▶ 命令 → ✅ 预期）｜ ❓ 判定表 ｜ 🔁 失败处理 ｜ 📒 台账 ｜ 🏁 完成标准 ｜ ⛔ 常见错法
```
三个库的「身份」先记死（搞错库 = 全错）：

| 库 | 编号前缀 | 真相源（只改这里） | 渲染产物（⛔ 永远不手改） | 渲染脚本 |
|---|---|---|---|---|
| Saga 客户库（S 邮箱 / A 邮箱 / 历史表） | `SA-` `SB-` `SC-` | `data/saga_clients/research/<编号>.json`、`人工定级.csv`、`人工归并.csv`、`补录客户.jsonl`、`registry/*.json`、`sieve.json` | `Saga Clients/A|B|C/<编号>-<公司>-<国家>.md`、`entities.json`、`客户主表.csv` | `scripts/saga_clients/build.py` + `render.py` |
| External Clients（CCTV / Edgecore / Mikrotik 三个老仓） | `XA-` `XB-` `XC-` + 仓字母（`XB-C0001` = CCTV 仓） | `data/external_clients/{cctv,edgecore,mikrotik}.json`（原始，不改）、`overrides.json`（改级 / 复核）、`research/<编号>.json`（研究卡） | `External Clients/<仓>/A|B|C/*.md` | `scripts/external_clients/render.py` |
| Planet 渠道仓（本仓最早的 129 户） | `PA-` `PB-` `PC-` | `data/客户名单_Planet渠道_2026-10.csv`（列 `人工定级` / `长期群复核` / `备注`）、`batch/*.json`（新批） | `profile/*.md`、`docs/客户名单*.md` | `scripts/render.py`（在 `scripts/` 下跑）+ `scripts/audit.py` |

---

## 5. 剧本 R01–R12 · 客户数据类

### R01 · 给 Saga 库新增一户（补录）

- **目的**：Simon 给了一个新客户（邮件里冒出来的、PI 上的、他口述的），要进 Saga 库拿编号。
- **触发**：原话含「这个客户」「入库」「加进去」，且不在三库里。
- **前置检查**：
  1. ▶ `grep -ril "<域名或公司名关键词>" data/saga_clients/entities.json data/external_clients/*.json data/客户名单_Planet渠道_2026-10.csv | head` → ✅ 空 = 确实没有；有 → 走 R04 / R05 而不是新增。
  2. ▶ `grep -c . data/saga_clients/补录客户.jsonl` 记住行数。
- **步骤**：
  1. 在 `data/saga_clients/补录客户.jsonl` 末尾追加一行 JSON（字段：`no`（格式 `AS-补录-<日期>-<序>`）、`company`、`country`（中文国名）、`category`、`person`、`position`、`from`（一句话：从哪来的 + 证据位置）、`interest`、`contact`（邮箱，必须是公开页 / 来信里出现过的）、`mobile`、`website`、`remark`）。⛔ 不许写你猜的邮箱。
  2. ▶ `cd scripts/saga_clients && python3 build.py | tail -1` → ✅ 打印统计 JSON 结尾 `}`；再 ▶ `grep -n "<公司名>" ../../data/saga_clients/客户主表.csv | head -2` → ✅ 看到新编号（等级由 `build.py` 规则给，多数先落 C；Simon 定级 / PI 证据 / `grade_override` 再升）。
  3. 建研究档：写 `data/saga_clients/research/<新编号>.json`（最少字段：`code`、`name_official`、`type`、`size`、`summary`、`evidence[{claim, quote, url, date}]`、`kp[]`、`saga_fit{p1, tier, why}`、`mail_review{binding, situation, need, breakpoint, saga_now, next_move, facts[], proof_gaps[]}`、`researched_at`）。A/B 必须有 `mail_review.facts`（审计硬项）。
  4. 跑 **R02 渲染链**。
- ❓ 等级：按 D-01 A/B v5 判定表；拿不准 → C 储备（`grade_override` 不写）。
- 🔁 `build.py` 报 KeyError → 多半是 jsonl 某行不是合法 JSON（`python3 -c "import json;[json.loads(l) for l in open('data/saga_clients/补录客户.jsonl',encoding='utf-8') if l.strip() and not l.startswith('#')]"`）。
- 📒 README 项 + 对话全记录；若 Simon 定了级 → `人工定级.csv` 追加一行 `编号,等级,理由（含原话）,日期`。
- 🏁 `客户主表.csv` 有该编号；`Saga Clients/<级>/` 下有 MD；`audit_full.py` hard 0。

### R02 · Saga 渲染链 + 三审计（任何 Saga 数据改动后必跑）

- **触发**：改了 `research/*.json`、`人工定级.csv`、`人工归并.csv`、`补录客户.jsonl`、`registry/*.json`、`sieve.json` 任一。
- **步骤**（在 `scripts/saga_clients/` 下，顺序不能换）：

| # | ▶ 命令 | ✅ 预期（2026-10-29 基线） |
|---|---|---|
| 1 | `python3 renumber.py --snapshot-md` | 最后一行 `MD 快照 4647 份 → /tmp/renumber_old_md.json` |
| 2 | `python3 build.py` | 打印统计 JSON，最后一行是 `}`；无 Traceback |
| 3 | `python3 render.py` | 最后一行 `{'A': 169, 'B': 1225, 'C': 3253}`（数字随改动变；A/B 之和应 ≈ 名册 Saga 部分） |
| 4 | `python3 renumber.py --restore-dates` | 最后一行 `日期还原：N；无需改：M；内容确有差异：K`（K = 真改动的档案数，应等于你改的户数量级） |
| 5 | `python3 audit_full.py` | 最后一行以 `hard 0 soft 370` 开头，后接 `report docs/requirements/全量审计_机检_<日期>.md`（soft 基线 370，上升要看原因；退出码 1 = 有 hard） |
| 6 | `python3 audit.py` | 最后一行含 `rows 6246 missing 0 dup_assigned 0 ghost 0`、`ents 4647 no_md 0 wrong_dir 0 orphan 0`、`cand 49`（四个 0 必须是 0） |
| 7 | （改了 A/B 信稿 / 价格时）`python3 audit_ab.py` | 结尾统计无新增「错」项 |
| 8 | `cd ../.. && python3 scripts/lt_roster.py` | 最后一行 `roster 2045 {'A': 170, 'B': 1875, 'q': 0} queue 0 {}` |

- 🔁 第 2 步 Traceback `calendar` 相关 → 该目录下 `calendar.py` 遮蔽了标准库：绝不 `sys.path.insert` 这个目录，用 `importlib.util.spec_from_file_location` 载入。
- 🔁 第 5 步 `hard N>0` → 打开报告，按条修（常见：A/B 研究档缺 `mail_review.facts`；信稿价不在允许集合；型号不在价格表）。**不许**用改审计阈值来「修」。
- 🔁 第 4 步 `内容确有差异` 远大于你改的户数 → 你可能改了共享渲染规则；看 `git diff --stat "Saga Clients" | tail -1`，确认是预期的再继续。
- 🏁 八步全绿；`git status --short | wc -l` 与预期一致。

### R03 · Planet 渠道仓：新批入库 / 改一户 / 渲染

- **触发**：Simon 给 Planet 仓新客户；或 Planet 客户复核改级。⛔ Planet「矿脉挖掘」仍处暂停（T22 / T29-U28），不要去 PLANET 官网挖新经销商。
- **新批步骤**：
  1. 写 `batch/<YYYY-MM-DD>_<批名>.json`，结构抄最近一个（`ls batch | tail -1`，如 `2026-10-20_W22_…json`）：顶层 `batch / date / method[] / tools / customers[] / merged[] / pending_next_wave[] / skipped[{name, reason}]`；`customers[]` 每户英文键（`name, short_name, country, city, website, type, signal, own_brand, hook, angle, p1, p1_reason, tier, contacts, who, priority, rating(A|B|C), rating_basis, source, evidence, facts, notes…`），`add_batch.py` 负责映射到 CSV 中文列（`scripts/common.py` `COLUMNS`）；去重键 = 国家 + 规范化公司名；不建档的户写进 `skipped` 并给理由（留痕）。
  2. ▶ `python3 scripts/add_batch.py batch/<文件>.json` → ✅ 打印新增 / 合并数；运营列（人工定级 / 状态 / 日期 / 档案编号）永不被覆盖。
  3. ▶ `cd scripts && python3 render.py | tail -1` → ✅ `rendered 129 profiles`（数字 = 总户数）。
  4. ▶ `cd .. && python3 scripts/audit.py | tail -1` → ✅ `- **errors: 0**　warnings: 0`。
- **改一户**（复核 / 改级）：只改 CSV 的 `人工定级`（A/B/C）、`长期群复核`（追加 `留B·LT-Rnn` / `打回C·LT-Rnn` / `升A·LT-Rnn`）、`备注`（追加理由 + URL + 日期）；用 python `csv.DictReader/DictWriter`（`encoding='utf-8-sig'`，`newline=''`），模板见 `scripts/lt_review_x_p_003.py`。然后第 3–4 步 + `lt_roster.py` + 追加 `data/长期客户群_复核记录.csv`。
- 🔁 `audit.py` 报编号重复 → 你手工填了 `档案编号`；删掉让 `add_batch.py` 分配。
- 🏁 render 户数 = CSV 行数；audit errors 0；roster 行数变化等于你改的户。

### R04 · 改级（升 / 降 / 打回）三库各走各的门

| 库 | 怎么改 | ⛔ 不许 |
|---|---|---|
| Saga | ① Simon 原话定级 → `data/saga_clients/人工定级.csv` 追加 `编号,等级,理由（含原话 + 轮次）,日期`（最高优先级）；② 证据定级 → `research/<编号>.json` 写 `grade_override: "A|B|C"` + `override_reason` + `override_history[]`；PI 标签 活跃 / 可发展 会强制 A（`build.py` 内置） | 直接改 `entities.json` / `客户主表.csv` / MD；在 `人工定级.csv` 里替 Simon 发明理由 |
| External | `data/external_clients/overrides.json[编号] = {grade, reason, date, batch, from, review{status, prio, date, batch, note}}`（原值留 `from`） | 改 `cctv/edgecore/mikrotik.json` 原始数据 |
| Planet | CSV 列 `人工定级`（空 = 用 `评级` 列机器值）+ `长期群复核` + `备注` | 改 `评级` 列 |

- ❓ 用 **D-01**（A/B v5）与 **D-02**（打回 / 永久 pass）判定；每次改级必须有「理由 + 证据 + 日期 + 批次」四件。
- 📒 `data/长期客户群_复核记录.csv` 追加一行（8 列：编号 / 公司 / 国家 / 复核前等级 / 复核后等级 / 批次 / 日期 / 结论与理由）；README；总账。
- 🏁 渲染后该户 MD 在新等级目录；`lt_roster.py` 数字相应变化。

### R05 · 加厚一户（Saga 深挖 / 补证据）

- **触发**：「深挖 / 加厚 / 审核 / 交叉检查」；`lt_gap_audit` 列出「研究深度缺」；A 级季度复核。
- **前置**：▶ `python3 -c "import json;r=json.load(open('data/saga_clients/research/<编号>.json',encoding='utf-8'));print(r.get('deep'),len(r.get('evidence',[])),len((r.get('mail_review') or {}).get('facts',[])))"` → 知道现状。
- **证据来源优先级**：① 仓库里已有（`grep -ril "<域名>" data/ docs/ "Saga Clients"`、`data/gmail_s/`、`data/gmail_a/` jsonl）→ ② 官网快照 `data/saga_clients/site_snapshots/<编号>.json` → ③ `web_search depth 1` 摘要 → ④ `fetch_page` 官方页（只读第 0 块）→ ⑤ 登记机关（R08）。⛔ 没证据不写；「待补证」要写成 `proof_gaps`。
- **写入**：▶ `cd scripts/saga_clients && python3 deepen.py <<'EOF'` … `EOF`（数组；字段见 `deepen.py` 文档串：`deep{done_at, level}`、`company_facts`、`business_lines`、`products_seen`、`channels`、`signals`、`risks`、`saga_fit{p1,tier,why}`、`email_hook`、`evidence_add[]`、`kp_add[]`、`brands_add[]`、`notes_add`）。heredoc 里 ⛔ 不要用 f-string 花括号；中文路径走 python。
- **每条 evidence 四件**：`claim`（中文一句）、`quote`（原文引文 ≤ 300 字）、`url`、`date`（抓取日 YYYY-MM-DD）。
- ❓ 加厚后要不要改级 → D-01；要不要改 `saga_fit.p1` → 必须是价格主表 `Saga对应型号` ∪ HRUI 型号 ∪ STH 列表里的型号。
- 然后 **R02**。
- 🏁 `deep.level` 更新；`evidence` 条数增加；`audit_full` hard 0；MD 里能看到新事实。

### R06 · 复核一批长期客户（LT-R 批）

- **触发**：「再过一遍」「筛一下」「不行的打回 C」；`lt_roster.py` 的 `queue N>0`；缺口盘点「复核缺」。
- **前置**：▶ `python3 scripts/lt_roster.py | tail -1` 看 `queue`；▶ `ls scripts/saga_clients/lt_review_batches/ | tail -3` 得到下一个批号（`lt_r_0NN.py`，批名 `LT-Rnn`）。
- **步骤**：
  1. 取队列：`data/长期客户群_复核队列_2026-10-29.csv`（或按 Simon 指定范围）一批 12–40 户。
  2. 每户按 R05 的来源优先级看证据（先仓库内，再快照，再搜索；每户 ≤ 1 次 `web_search`），记下 `(quote, url)`。
  3. 判定：查 **D-02**；结论三选一 `留B` / `打回C` / `升A`；理由句式固定：`<事实 1>；<事实 2> → <结论>（路径 = xx；可逆条件 = xx）`。
  4. 写批文件 `scripts/saga_clients/lt_review_batches/lt_r_0NN.py`：抄上一批骨架，`BATCH = 'LT-Rnn'`，`V = {'SB-xxx': ('留B', '理由', [('引文', 'URL'), ...]), ...}`，末尾 `run(BATCH, V)`。
  5. ▶ `python3 -c "import ast;ast.parse(open('scripts/saga_clients/lt_review_batches/lt_r_0NN.py',encoding='utf-8').read())"` → ✅ 无输出。
  6. ▶ `python3 scripts/saga_clients/lt_review_batches/lt_r_0NN.py | tail -3` → ✅ 打印写入户数；**再跑一遍** → ✅ 写入 0（幂等）。
  7. External / Planet 户另写 `scripts/lt_review_x_p_00N.py`（抄 `lt_review_x_p_003.py`：External 改 `overrides.json[code]['review']`，Planet 改 CSV 三列，两者都追加复核记录 CSV）。
  8. **R02** 全链 + External `render.py` / Planet `render.py`（按涉及的库）+ `lt_roster.py`。
- 🔁 `run()` 抛 `AssertionError` 编号不存在 → 编号写错（B 户编号可能仍是 `SC-` 前缀！用 `entities.json` 的 grade 选户，不用前缀猜）。
- 🔁 DNS 结果 `nxdomain` 作为打回理由前，必须**第二次查询**（早上一轮曾误报 3 户）。
- 📒 复核记录 CSV（库自动追加）、README、总账 PR 行状态、对话全记录。
- 🏁 批文件已提交；`lt_roster.py` queue 减少相应数；复核记录行数 = 原 + 本批户数。

### R07 · External Clients 研究卡 + 渲染

- **触发**：External 库某户要加厚 / 复核 / 改级。
- **步骤**：
  1. 读原始：▶ `python3 -c "import json;d=json.load(open('data/external_clients/mikrotik.json',encoding='utf-8'));print([x for x in d if x.get('code')=='XB-M0001'][:1])"`（cctv / edgecore 同理）。
  2. 写卡：`from research_store import put`（`scripts/external_clients/research_store.py`；必填 `code, name, round, researched_at, alive, summary, type_final, saga_line, evidence, touch_status, grade_final, grade_reason_final, next_move`；`deep` 必须是布尔 `True/False`，⛔ 不要写字符串 `'False'`）。批量写法抄 `scripts/external_clients/lt_cards_003.py`。
  3. 改级走 `overrides.json`（R04）。
  4. ▶ `python3 scripts/external_clients/render.py | tail -3` → ✅ 三行 `mikrotik-info {'B': 423, 'C': 619} deleted 0 researched 631` / `edgecore … ` / `CCTV-PoE {'B': 111, 'C': 2961} deleted 250 researched 343`（数字随改动变）。
  5. `lt_roster.py`。
- ⛔ 这三个库来自 CCTV / Edgecore / Mikrotik 老仓：**CCTV 代理永不再跑**；按 Saga 的真实情况重定级；仓库私有不删。
- 🏁 `research/<编号>.json` 存在且 `put` 不报错；MD 在新等级目录；roster 数字对。

### R08 · 公司底数登记（官方工商 / 年报）

- **触发**：缺口盘点「登记底数缺」；新入库 A/B；A 级季度复核（下一次 2027-01）。
- **规程**：`docs/公司底数_作业规程.md` §0 通用规则、§1 分国来源表（哪国查哪个官网 / API、每国的坑）、§2 每轮步骤 —— **先读 §1 对应国家那一行再动手**。
- **步骤**：
  1. ▶ `cd scripts/saga_clients && python3 registry_store.py` → ✅ 一行 `1487 ['SA-001', …]`（已做户数 + 编号列表；1,487 基线）。
  2. 先从 `research/<编号>.json` 的 `company_facts` 捞现成登记号（ИНН / NIP / KRS / IČO / CIN / P.IVA / HRB / Company No.），有号直接走 API / 直链。
  3. 取数 → 新建 `scripts/saga_clients/registry_batches/b<N>_<国家缩写>.py`（抄最近一批，如 `b136_c.py` / `b99_de_gb_pl.py`；`ls | sort -V | tail -1` 取下一个号）：`registry_store.put(code, key='<国 key>', batch=N, name=, iso=, source=, url=, number=, status=, incorporated=, company_type=, sic=[], address=, accounts=, size_band=, officers=[], prev_names=[], lines=[...], notes=, fetched='YYYY-MM-DD')`；`lines` 里写 3–5 条「这意味着什么」+ 下次复查月份。
  4. 「老板 = 联系人？」写回 KP：`scripts/saga_clients/patches/batch<N>_kp.py`（幂等 TAG，抄上一个）。
  5. 跑脚本两遍（第二遍应 0 写入）→ **R02**。
- ❓ 「1 查未得即停」：一个国家来源查不到 → 记 `notes='<来源> 未得 <日期>'`，不要换五个站死磕。
- ⛔ 永远不对客户说「我们查了你的登记 / 董事 / 财报」；不在信里引用亏损 / 诉讼。
- 🏁 `registry/<key>_<日期>.json` 多了该户；MD「公司底数」节出现；规程 §3 进度表加一行。

### R09 · 挖具名关键人（KP）

- **触发**：缺口盘点「邮箱·具名 KP 缺」；要写个人信前。
- **顺序**：① 往来邮件签名（`grep -ril "<域名>" data/gmail_s/messages data/gmail_a/messages`，再打开命中的月份文件看签名）→ ② 官网 About / Team / Impressum（快照 JSON 或 `fetch_page`）→ ③ 登记机关高管（R08 的 `officers`）→ ④ LinkedIn 搜索摘要（只记姓名 + 职位 + URL，⛔ 不去猜邮箱格式）。
- **写入**：`kp_add[{name, role, email(仅公开 / 来信出现过), phone, source(URL), date}]` 经 `deepen.py`；External 写 `contacts.kp[]`；Planet 写 `入口/联系方式` + `备注`。
- ❓ 具名 KP > `info@`；WhatsApp 客户不算「缺邮箱」；公开页只有表单也不算缺口。
- 🏁 `kp` 至少 1 条带 `source`；渲染后 MD「关键人」节可见。

### R10 · 缺口盘点 + 名册 + 补快照清单（长期客户群总检）

| 步骤 | ▶ 命令 | ✅ 预期 / 产物 |
|---|---|---|
| 1 | `python3 scripts/lt_roster.py` | 最后一行 `roster 2045 {...} queue 0 {}`；`docs/长期客户群_名册_2026-10-29.md`、`data/长期客户群_复核队列_2026-10-29.csv` |
| 2 | `python3 scripts/lt_gap_audit.py --no-dns` | `data/长期客户群_深挖缺口_<日期>.csv` + `docs/长期客户群_深挖缺口_<日期>.md`（七维：研究深度 / 登记底数 / 官网快照 / 域名·MX / 邮箱·具名 KP / 复核 / 跨库重复） |
| 3 | 去掉 `--no-dns`（装了 dnspython、且想刷新 External / Planet 域名体检时） | 多写 `data/external_clients/mx_check_<日期>.json`、`data/planet_mx_check_<日期>.json` |
| 4 | `python3 scripts/lt_snapshot_list.py` | `snapshot list 751 → …/data/长期客户群_补快照清单_2026-10-29.json {'X': 640, 'P': 111}`（数字随快照消费减少）→ 供 Actions `customer-watch` 顺手抓 |

- ❓ 缺口表怎么用：每行「还缺什么」→ 对应剧本（研究深度 → R05；登记 → R08；快照 → R11；域名 → R12；KP → R09；复核 → R06；跨库重复 → 并档记备注）。
- 🏁 三份产物时间戳是今天；README 写明「缺 X 项 / 已清 Y 项」。

### R11 · 官网快照 → 加厚（消费 Actions 产物）

- **触发**：`customer-watch` 跑完（每晚 02:23Z 自动，或 Simon 手动 Run workflow）后机器人提交落到本分支。
- **步骤**：
  1. ▶ `git fetch -q origin arena/3f35b9b3-planet && git log --oneline origin/arena/3f35b9b3-planet -3` → ✅ 看到 `github-actions` 提交（含 `site_snapshots`）→ `git pull -q --rebase origin arena/3f35b9b3-planet`。
  2. ▶ `python3 -c "import json;r=json.load(open('data/saga_clients/site_snapshots/_report.json'));print({k:(len(v) if isinstance(v,list) else v) for k,v in r.items()})"` → ✅ 成功 / DNS / 超时 / HTTP 计数。
  3. ▶ `python3 scripts/saga_clients/lt_snapshot_thicken.py --dry | tail -5` → ✅ 列出将更新的户数（三库）。
  4. ▶ `python3 scripts/saga_clients/lt_snapshot_thicken.py | tail -5` → ✅ 实写；**再跑一遍** → 0（每份快照按 `fetched_at` 只消费一次）。
  5. **R02** + External / Planet 渲染 + `lt_roster.py` + `lt_snapshot_list.py`。
  6. 失败户：▶ `ls data/长期客户群_快照打回候选_*.csv` → 只有**连续两晚**都失败、且 DNS 复查 nxdomain 的户才进 R06 打回候选；单晚失败不动。
- ⛔ 沙箱不能访问客户网站——不要在沙箱里跑 `site_snapshot.py` 对真实域名；本地测试一律 `--snap-dir /tmp/xxx`。
- 🏁 `snap_thicken` 字段出现在对应研究档；`website_status` 占位被替换；两遍幂等。

### R12 · 邮箱 / 域名体检 + 死域处理

- **触发**：缺口盘点「域名·MX 异常」；复核前；退信。
- **步骤**：
  1. ▶ `python3 -c "import dns.resolver" || pip install -q --break-system-packages dnspython`。
  2. Saga：▶ `cd scripts/saga_clients && python3 mx_check.py --grades AB --only-missing --workers 16 | tail -2` → ✅ 写 `data/saga_clients/mx_check_<日期>.json`（`domains[dom] = {mx: [[pref, host]…], a: […], status: ok|no_mx|dead|nxdomain, cls, checked}`）。
  3. External / Planet：R10 第 3 步。
  4. 异常域复查（必做）：▶ `python3 - <<'EOF'` 用 `dns.resolver.resolve(dom, 'MX'/'A'/'NS')` 各查一次并打印 → 两次都 NXDOMAIN 才算死。
- ❓ **D-03 死域处理表**：死 + 有备用路径（WA / 私人 gmail / 真回过）→ 留 B，路径改写进 `lt_review.note`；死 + 无路径 + 非对位 → 打回 C 储备（可逆：补到邮箱即回 B）；死 + 成单客户 → 不动，记 Q；`no_mx` 但 A 记录在 → 不算死（可能只是不收公网邮件），记「待观察」。
- ⛔ 手工补缓存时必须完整写 `mx/a/status/cls/checked` 五键，否则 `render.py` 崩。
- 🏁 `mx_check_<日期>.json` 覆盖所有 A/B 域；异常户都有复查记录；打回户进了 R06 批。
