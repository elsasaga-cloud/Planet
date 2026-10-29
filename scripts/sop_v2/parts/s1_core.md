## 0. 这本书怎么读（30 秒）

- **方法论全集**（`docs/方法论_全集_2026-10-29.md`，初版 10-27 保留）讲「怎么工作、怎么分析、每个方法为什么这么做、怎么诞生的」——那是正本；**本书只是它的命令级附录，只讲「现在照着做」**：每个剧本都是编号步骤 + 可复制命令 + 预期输出 + 失败处理 + 完成标准。判断类问题以方法论为准，命令类以本书为准。
- 事实类信息（Saga 是谁、卖什么、价格、口径、客户数字）**不在本书**，去读 `docs/Saga全景信息包_给其他Agent_2026-10-29.md`。本书只管「手怎么动」。
- 符号：**▶** 要敲的命令 ｜ **✅** 正常时你应该看到什么 ｜ **❓** 判定（查表）｜ **🔁** 失败了怎么办 ｜ **📒** 必须写的台账 ｜ **⛔** 绝对禁止 ｜ **🏁** 完成标准（Definition of Done）。
- 规则：**步骤不能跳、不能换顺序**；每一步的 ✅ 没出现就停下走 🔁，不要「大概没问题」继续；任何「我觉得可以改一下流程」的念头 → 先按原流程做完，再把建议写进 Q 清单。
- 一轮 = Simon 一条消息到你一条回复。每一轮都必须走 **S-00 开工 → 剧本 → S-99 收工**，没有例外（哪怕只是回答一个问题，也要记对话全记录）。

### 0.1 没有剧本可套时：通用解题八步（照这个顺序，不要跳）

| # | 步 | 具体做法 | 产物 |
|---|---|---|---|
| 1 | 复述 | 用一句话写出「Simon 要什么 + 做到什么算完」（验收标准要能用命令验证） | 写在回复开头 |
| 2 | 看现场 | 跑命令**亲眼看到**现状 / 报错（`ls -la`、`grep -c`、脚本的最后几行输出），不凭记忆 | 一段真实输出 |
| 3 | 先查仓库 | `grep -rn "<关键词>" docs scripts data --include=*.md --include=*.py` + 对话全记录 + Q 清单：这事是不是已经做过 / 已有规则 / 已有脚本 | 找到就复用，不重造 |
| 4 | 最小可逆改动 | 只改真相源（JSON / CSV / overrides / parts），一次只改一类；大改先 `--dry` | diff 可解释 |
| 5 | 验证 | 跑两遍（幂等）+ 渲染链 + 审计 + 抽查 3 条 | 全绿 |
| 6 | 留痕 | 台账四件 + 脚本提交 + 拿不准的立 Q 带默认 | `grep -c` 都 = 1 |
| 7 | 报告 | §3.2 模板：搞定 / 没搞定 / 你要做啥 / 不用做啥 | — |
| 8 | 反哺 | 新流程写进本书 §11「待补剧本」或直接新增剧本（改 parts 重建） | 下个 agent 不再踩 |

---

## 1. S-00 · 每轮开工 SOP（10 步，约 3 分钟）

| # | 动作 | ▶ 命令 / 做法 | ✅ 预期 | 🔁 不对时 |
|---|---|---|---|---|
| 1 | 记时间 | `date -u` | 得到 UTC 时刻；后面所有台账用它（北京 = +8h） | — |
| 2 | 确认仓库与分支 | `cd /home/user/Planet && git branch --show-current && git log --oneline -1` | 分支 `arena/3f35b9b3-planet`；最近一条提交是你认得的 | 若 `git log` 只剩 `2199cbf Initial commit` → 沙箱被重置，走 **R18 沙箱恢复** |
| 3 | 同步远端 | `git fetch -q origin arena/3f35b9b3-planet && git status -sb` | `## arena/... [behind N]` 或平；工作区干净 | behind → `git pull -q --rebase origin arena/3f35b9b3-planet`（Actions 机器人可能推过）；有未提交改动 → 先看是什么再决定 |
| 4 | 读五份文件（**不许跳**） | `AGENT-CONSTITUTION.md` → `AGENT-README.md` → `docs/requirements/用户要求总账.md`（最新 PR 行 + INH 表）→ `docs/requirements/对话全记录.md`（`tail -40`，最后 3 轮）→ `README.md` 进度（`tail -3 README.md`：编号项在文件末尾，最后 2 条） | 你能说出：上一轮做到哪、有什么没搞完、Simon 最近的原话是什么 | 读不懂的词查全景信息包 §15 术语表 |
| 5 | 看 Simon 这轮原话 | 逐字读；找出动词（继续 / 出 / 查 / 改 / 告诉我 / 搞定没）和名词（哪个库、哪批客户、哪份文件） | 能用一句话复述任务 | 真有歧义且影响方向 → 不要问，按 **R19 Q 立项**写默认值并执行默认 |
| 6 | 任务分类 | 查 §2 任务分类器 → 得到剧本编号 | 一个主剧本 + 若干附属剧本 | 没有匹配的剧本 → 用 **R16 新脚本 / 新流程规范**自建，并在收工时把新流程写进本书的「待补剧本」节 |
| 7 | 检查环境 | `python3 -c "import dns.resolver, markdown"` | 无输出 = 两个包都在；报 `ModuleNotFoundError` → `pip install -q --break-system-packages dnspython markdown`（沙箱重置后会消失，属正常） | 装不上 → 走不依赖它的路径（HTML 用内置降级转换；DNS 用 `--no-dns`） |
| 8 | 定预算 | 估一下：本轮做多少户 / 多少文件；Simon 要的是「长任务、大批量」（40–60 分钟一轮） | 写在心里的清单：主产出 + 台账 + 报告 | 不要为了「快回复」把活砍到 10 分钟 |
| 9 | 先占坑提交？ | 若预计 >30 分钟且会改很多文件：先做一次小的 WIP 提交（例如只有脚本）并推送 | 沙箱中途重置也不丢 | — |
| 10 | 回复开头 | 第一行输出 `📋 上下文已加载（宪法/AGENT-README/总账 PR-02-xx/对话全记录 T29-Uyy）` | — | — |

⛔ 开工阶段禁止：跳过第 4 步直接干活；用上一轮记忆代替读文件；在 `main` 或别的分支上操作；`git reset --hard` 掉别人的提交。

---

## 2. S-01 · 任务分类器（Simon 说了什么 → 走哪个剧本）

| Simon 的话里出现 | 主剧本 | 附属 |
|---|---|---|
| 「继续」「继续搞」「多搞一些」（没有新主题） | 看对话全记录最后一轮 Agent 的「没搞完的」清单 → 接着做；当前主线 = 长期客户群（R06 复核 / R08 底数 / R09 KP / R11 快照加厚） | R02 渲染链、S-99 |
| 「入库」「这个文件 / 链接 / 压缩包」「Drive」「邮件」 | R14 Drive/大文件入库 或 R15 Gmail 查证入库 | R17 台账 |
| 「这些客户…深挖 / 加厚 / 审核 / 交叉检查」 | R05 加厚（Saga）/ R07 External 卡 / R10 缺口盘点 | R08 底数、R09 KP、R12 邮箱体检、R11 快照 |
| 「定级」「升 / 降」「这个不行」「这个可以」 | R04 改级（三库各自机制） | R06 复核记录、R02 渲染 |
| 「再过一遍」「筛」「不行的进 C」「永久 pass」 | R06 复核批（LT-R 流程 + 判定表 D-01/D-02） | R02、R10 名册 |
| 「新客户」「挖客户」「找 XX 国家 / 行业」 | Planet 仓 → R03 Planet 新批；Saga 库 → R01 新建研究档 | ⛔ 先确认挖掘是否仍处「暂停」（T22/U28：Planet 矿脉暂停） |
| 「报价」「多少钱」「价格表」 | R21 报价计算 | 全景信息包 §8 |
| 「写封信」「草稿」「发什么」 | R20 信稿 | R21、审计 `audit_ab.py` |
| 「出个 HTML」「出 MD」「写个方法论 / 介绍 / 工作台」 | R22 文档交付（MD + HTML + 预览） | R17 |
| 「Actions」「Run workflow」「跑了没」「快照」 | R23 Actions 检查 + R11 快照消费 | — |
| 「监控」「巡检」「两个月」 | R24 监控轮 | — |
| 「发送包」「这周发啥」 | R25 周发送包 | — |
| 「搞定没」「告诉我」「是吧」 | 只核对 + 回答（S-98 报告模板）；核对必须跑命令看数字，不许凭记忆 | S-99 仍要走 |
| 任何「别再问了」「你自己定」 | 一律 R19 Q 立项 + 默认执行 | — |

---

## 3. S-99 · 每轮收工 SOP（14 步，不可省）

| # | 动作 | ▶ 命令 / 做法 | ✅ 预期 |
|---|---|---|---|
| 1 | 产出核验 | 对每个新文件 `ls -la <文件>`；MD 看 `grep -c "^## " <文件>`；CSV 看行数 `python3 -c "import csv;print(sum(1 for _ in csv.DictReader(open('<文件>',encoding='utf-8-sig'))))"` | 文件存在、行数 / 章节数与你声称的一致 |
| 2 | 渲染链（若动了客户数据） | 按 R02（Saga）/ R07（External）/ R03（Planet）的「渲染 + 审计」段跑 | `audit_full.py` hard 0；`scripts/audit.py` `errors: 0`；`lt_roster.py` 打印 `roster NNNN {...}` |
| 3 | 对话全记录 | 追加 Simon 原话 + Agent 要点（§3.1 配方 A） | `grep -c "T29-Uxx" docs/requirements/对话全记录.md` ≥ 2 |
| 4 | 用户要求总账 | 新要求 → 新 `PR-02-NN` 行；旧要求状态变化 → 改该行状态（§3.1 配方 B） | `grep -c "PR-02-NN"` = 1 |
| 5 | Q 清单 | 本轮产生的待裁定事项 → 新 `Q-NN` 行带默认（§3.1 配方 C）；已裁定的填「结果」 | — |
| 6 | README | 进度编号列表追加第 N 项（§3.1 配方 D） | `grep -c "^N\. \*\*"` = 1 |
| 7 | 规程 / 专项文档 | 若剧本本身有变化（新脚本、新判定），更新对应专项文档（`docs/公司底数_作业规程.md` §3、本书「待补剧本」等） | — |
| 8 | 变更日志 | `timeout 900 python3 scripts/changelog.py`（约 140 秒） | 最后一行 `wrote docs/requirements/变更日志.md rows=NNN`，NNN 比上轮大 |
| 9 | 清理 | `find . -name __pycache__ -type d -prune -exec rm -rf {} +`；确认没有 `/tmp` 路径或测试产物混进仓库（`git status --short`） | 只剩你想提交的文件 |
| 10 | 提交 | `git add -A && git -c user.name=elsasaga-cloud -c user.email=elsasaga-cloud@users.noreply.github.com commit -q -m "T29-Uxx：<一句话>"` | 无报错；`$` 要写成 `\$` 或用单引号 |
| 11 | 拉再推 | `git fetch -q origin arena/3f35b9b3-planet && git pull -q --rebase origin arena/3f35b9b3-planet && git push -q origin arena/3f35b9b3-planet` | 无输出即成功 |
| 12 | 验推 | `git ls-remote origin arena/3f35b9b3-planet` 的哈希开头 与 `git rev-parse --short=12 HEAD` 相同 | 两个哈希一致 |
| 13 | 预览（若有 HTML 交付） | `start_process`：`python3 -m http.server 8080 --bind 0.0.0.0 --directory /home/user/Planet/docs`，并 `present_file` 打开 HTML | 端口 8080 在听 |
| 14 | 报告 | 用 §3.2 模板写给 Simon | 大白话；每项「搞定 / 没搞定」+「你要做啥 / 不用做啥」 |

### 3.1 台账四件套 · 精确配方（复制即用；全部幂等）

**配方 A · 对话全记录**（文件只增不删；时间必须是真实 `date -u`，Simon 消息时刻取平台给的时间，没有就写「会话内，精确时刻未提供」）
```python
import pathlib
p = pathlib.Path('docs/requirements/对话全记录.md'); s = p.read_text(encoding='utf-8')
simon = '- **2026-10-29 15:15Z Simon（T29-U132）：** 「<逐字原话>」'
agent = '- **2026-10-29 15:33Z Agent（T29-U132）：** <做了什么 + 产出文件清单 + 没搞完的>'
if simon not in s: s = s.rstrip('\n') + '\n\n' + simon + '\n'
if agent not in s: s = s.rstrip('\n') + '\n' + agent + '\n'
p.write_text(s, encoding='utf-8'); print(s.count('T29-U132'))
```

**配方 B · 用户要求总账 PR 行**（5 格：编号 ｜ 轮次+时间+原话 ｜ 转述 ｜ 性质 ｜ 状态+位置；插在最后一条 `| PR-02-` 之后）
```python
import pathlib
p = pathlib.Path('docs/requirements/用户要求总账.md'); s = p.read_text(encoding='utf-8')
row = '| PR-02-77 | T29-U133 2026-10-29 15:4xZ 「<原话>」 | <转述> | <性质> | 🔄 2026-10-29 15:4xZ：<做到哪 / 文件> |'
if 'PR-02-77' not in s:
    lines = s.split('\n')
    # 注意：PR-02 行分两块（第二块是 PR-02-44…46 老行），要插在「编号最大」的那行之后，不是文件里最后一行 PR-02 之后
    idx = max((i for i, l in enumerate(lines) if l.startswith('| PR-02-')),
              key=lambda i: int(lines[i].split('|')[1].strip().split('-')[-1]))
    lines.insert(idx + 1, row); s = '\n'.join(lines)
p.write_text(s, encoding='utf-8'); print(s.count('PR-02-77'))
```
状态符号：`🔄` 进行中 ｜ `✅` 完成 ｜ `⏳` 等 Simon ｜ `⛔` 被覆盖（指向新编号，不删行）。

**配方 C · Q 清单行**（6 格：编号 ｜ 提出轮次 ｜ 问题 ｜ 影响范围 ｜ 默认处理 ｜ 结果；编号只增不复用）
```python
import pathlib, re
p = pathlib.Path('docs/requirements/待统一处理问题清单.md'); s = p.read_text(encoding='utf-8')
n = max(int(x) for x in re.findall(r'^\| Q-(\d+) ', s, flags=re.M)) + 1
row = f'| Q-{n:02d} | T29-U133（2026-10-29 15:4xZ） | **<问题一句话>** | <影响几户 / 哪条规则> | 默认：<不问 Simon 时怎么做> | 待裁定（默认执行） |'
if f'| Q-{n:02d} ' not in s:
    lines = s.split('\n'); idx = [i for i, l in enumerate(lines) if l.startswith('| Q-')]
    lines.insert(idx[-1] + 1, row); s = '\n'.join(lines)
p.write_text(s, encoding='utf-8'); print(n)
```

**配方 D · README 进度项**（编号列表 `N. **标题（T29-Uxx，日期 时刻Z）。** 正文`；插在最后一个编号项之后）
```python
import pathlib, re
p = pathlib.Path('README.md'); s = p.read_text(encoding='utf-8')
items = list(re.finditer(r'^(\d+)\. \*\*.*$', s, flags=re.M)); last = items[-1]; n = int(last.group(1)) + 1
item = f'{n}. **<标题>（T29-U133，2026-10-29 15:4xZ）。** <做了什么 / 产出路径 / 关键数字>'
if f'{n}. **' not in s:
    s = s[:last.end()] + '\n' + item + s[last.end():]
p.write_text(s, encoding='utf-8'); print(n)
```

⛔ 台账禁忌：`str.replace` 之后不验证（必须 `grep -c`）；`assert count == 1` 卡死整段脚本（用存在性检查）；编造时间；改旧行的原话；删行。

### 3.2 S-98 · 给 Simon 的报告模板（大白话，T29-U41 样式）

```
**搞定 / 没搞定一览**
- <任务 1>：搞定。<一句话结果 + 关键数字 + 文件路径>
- <任务 2>：没搞定（卡在 <原因>）。下一步 <我会怎么做 / 什么时候自动好>
**你要做啥**
- <只有 Simon 能做的事，如「点 Run workflow」「给个链接」>；没有就写「不用做啥」。
**不用做啥**
- <明确告诉他哪些不用管，如「价格不用你去问 Peter」>
**顺带**
- <风险 / 提醒，一两条，不唠叨>
```
规则：不堆术语；数字要是你刚跑命令看到的；不许「应该 / 大概」；不重复上一轮已经说过的解释；不要问 Simon 多个问题（最多一个，且先给默认）。
