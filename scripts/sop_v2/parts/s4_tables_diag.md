## 7. 判定表汇编（❓ 剧本里引用的全部表）

### D-01 · A / B / C 定级（A/B v5「宽留冷」口径，Q-76 单一体系，三库同尺）

先问四个事实（都要有证据）：**成单 / 付样 / PI 几次？真人真回几次（扣掉否定回复）？WA 加了没 / 展会见过没？对位（在卖或在用交换机 / 收发器 / PoE）？** 然后从上往下第一条命中即定：

| 结论 | 规则 | 命中条件 |
|---|---|---|
| **A（精华跟）** | A1 | 复购（成单 ≥ 2）**或** 邮件绑定深度 ≥ 中度 |
| A | A2 | 成单 / 付样 / PI ≥ 1 **+** 真人往来（真回 ≥ 1 或 WA 已加 或 展会面谈） |
| A | A3 | 真人往来 + 对位 + 四主区（TR/US/GB/DE）或波兰 + （登记坐实 或 自有品牌） |
| A | A4 | Simon 点名（S 重点 / 状态含「（Simon）」/ `人工定级.csv`） |
| A | A5 | 自有品牌 + 对位 + 任一真人往来（OEM 品牌商，任何区域） |
| A | A6 | 真人真回 ≥ 3 + 对位，任何区域 |
| **B（长期培育：发送包 + 两月巡检）** | B1 | 成单 / 样品 / PI 但 gg / 凉 |
| B | B2 | 真回 ≥ 1 / WA / 打开 ≥ 2 / 展会 + 对位 |
| B | B3 | 自有品牌 + 对位 |
| B | B4 | 四主区 / 波兰 + 对位 + 登记坐实 |
| B | B5 | 四主区 / 波兰 + 对位的冷户 |
| B | B6 | 对位的冷户，任何区域（「留冷」） |
| **C（储备：只巡检、不发）** | — | 其余：不对位 / 守界 UA·IR·SY / 注销 / 无路径 / 研究后判不了 |
| **永久 pass** | — | 只有 D-04 三条刚性之一 |

- 人工定级 > PI 标签（活跃 / 可发展 → A）> 证据规则；B 记录编号可能仍是 `SC-`（按 grade 选，不按前缀）。
- Q-77 默认分层（待 Simon 裁定）：A 精华跟（季度个人信 + 两月巡检）；B1 重点普通跟 ≈ 300–450（自牌 / OEM / 已进口 / 官方分销）；B2 普通跟 ≈ 1,500–1,700（群发窗口）；C 储备巡检。

### D-02 · 复核结论（LT-R 批每户三选一）

| 结论 | 同时满足 | 写法 |
|---|---|---|
| **留B** | ① 行业内（安防 / IT / 网络 / 工业网络的分销、集成、安装、自有品牌、网店，或终端但有复购）② 对位 ③ 有成单可能（进口中国 / 台湾同类记录、渠道名录、商品页、成单 / 样品 / 回信 / 具体需求 任一）④ 有路径（可用邮箱 / WA / 真回过） | `留B` + 理由 + 「路径 = …」 |
| **打回C** | 四类之一：微型网店 / 一人店且无进口证据；登记休眠 / 主体不明 / 经营范围对不上；未坐实 + 无路径（邮箱 fail、域名死）；红旗（仲裁 / 执行 / 制裁待核）+ 收款未清、纯光端机终端 + 区域外、非本行业 / 非采购主体 | `打回C` + 理由 + 「可逆条件 = 补到邮箱 / 回信 / 收款路径」 |
| **升A** | D-01 A1–A6 任一且证据在研究档 | `升A` + 命中规则号 |
| 边界口径 | 微型 + 有进口证据 = 留 B（预付 100%）；q33_hold ★ 品牌商留 B「只盯不发」；巨头留 B 长线；RU/BY/KZ 留 B「只盯 + 季度一封」；全退信留 B 补路径；「待核」判不了 → 继续待过，**不乱打回** | — |

### D-03 · 死域 / 邮箱异常处理

见 R12：死 + 备用路径 = 留 B；死 + 无路径 + 非对位 = 打回 C（可逆）；成单户不动、记 Q；`no_mx` 但有 A 记录 = 待观察；任何 nxdomain 必须二次查询。

### D-04 · 永久 pass（Gate 0，只有这三条，「一旦入选 永不考虑」）

| 刚性条件 | 证据要求 |
|---|---|
| 无邮箱 **且** 无 WhatsApp（任何路径都没有） | 表 / 研究档 / 公开页三处都查过 |
| 全部邮箱退信 **且** 无备用地址 | 退信记录 + 官网 / 名录无其他地址 |
| 明确婉拒 / 要求停发 | 原文引文 + 日期 |

⛔ **不是**永久 pass 的（Simon 明确否决）：乌克兰（守界，留 C）；巨头运营商（难但不 pass）；品类不对位的光端机 / DWDM / 光模块（Simon 日职可用，留 C 标 dayjob_fit）；「研究后定 C」→ 重判，真差才 pass。拿不准 = C 储备。

### D-05 · 守界 / 不碰 / 特殊区域

| 情况 | 处理 |
|---|---|
| UA / IR / SY | 守界：C 储备，不发、不删 |
| 轨交主营、UL / E-mark / KC 强制场景（KR 需 KC） | PASS 产品线（不报价），户留 C |
| 云管理 / 消费级 / IP67 / 路由 / Wi-Fi / GPON / HDMI / M12 / 机架 / 单独注入器·分离器 / 反向 PoE / 无源 PoE（-24V/-Auto 除外） | Saga 无此品类：不承诺、不拼凑；信里不提 |
| Q-33 经销体系现供客户（在卖 HRUI / SmartByte 外壳） | 「不碰，标记」`q33_hold`：只巡检、不群发；仍过三闸 |
| 巨头 / 运营商 | 留 B 长线或 C；永不 pass；信稿不卖「领先厂商」 |
| RU / BY / KZ / UZ | 留 B「只盯 + 季度一封」；收款路径待 Simon（Q 清单） |
| 2.5G 机型、RMB 报价、Versa / Planet USA | 等 SB-263 / 待 Simon / C |

### D-06 · 入库落点

见 R13 的落点表。

### D-07 · 报价档位与格式

见 R21：20 / 25 / 30；地板 Realtek ≥ 20 / Marvell ≥ 25 / CENTEC ≥ 35；格式 `$xx USD EXW（快照日期，15 天有效）`；Realtek 数字只从 `data/价格主表_HRUI.csv`。

### D-08 · 这事到底该不该做（省时间 + 长期复利 两把尺）

| 问 | 做 | 不做 |
|---|---|---|
| 能省 Simon 的时间吗？ | 自动化、台账、复制即发的稿、一句话报告 | 要他逐条确认的清单、要他去问供应商 |
| 有长期复利吗？ | 入库、证据、规则、脚本、可逆的分级 | 一次性手改渲染件、只在聊天里存在的结论 |
| 两个都不沾 | → 不做；若 Simon 点名要 → 做最小版 + 立 Q | |

---

## 8. 诊断树（症状 → 原因 → 处理）

| # | 症状 | 最常见原因 | 处理 |
|---|---|---|---|
| X-01 | `git log` 只剩 `Initial commit` | 沙箱重置 | R18-A |
| X-02 | `git push` 被拒 | Actions 机器人推了快照 | R18-B |
| X-03 | `git pull --rebase` 说有未提交改动 | 渲染链刚改了审计报告 / 名册 | 先提交（这些就是本轮产物），再拉 |
| X-04 | `build.py` Traceback 提到 `calendar` | 本目录 `calendar.py` 遮蔽标准库 | 不要 `sys.path.insert` 该目录；`importlib` 按路径载入 |
| X-05 | `audit_full.py` `hard N` | A/B 研究档缺 `mail_review.facts`；信稿型号 / 价不在集合；日期在未来 | 修数据，不改阈值 |
| X-06 | `render.py` KeyError `mx` / `checked` | 手工补的 MX 缓存缺键 | 补齐 `mx/a/status/cls/checked` |
| X-07 | `research_store.put` AssertionError | 缺必填键 / `deep` 是字符串 | 对照 REQUIRED；`deep` 用布尔 |
| X-08 | 复核库 `run()` 找不到编号 | 用前缀猜编号（B 户仍是 `SC-`）；External / Planet 户混进 Saga 批 | 用 `entities.json` grade 选；跨库户走 `lt_review_x_p_00N.py` |
| X-09 | `changelog.py` 超时 | 没加 `timeout 900` | `timeout 900 python3 scripts/changelog.py`（约 140 s） |
| X-10 | bash 里中文路径乱码 / 找不到文件 | shell 引号 / 编码 | 用 python 处理中文路径 |
| X-11 | `curl` / `pip` 失败 | 沙箱只放行 github / pypi / npm；curl 全封 | 用 `fetch_page` / `web_search`；pip 用 `--break-system-packages` |
| X-12 | `fetch_page` 返回很多块 | 页面大 | 只读第 0 块；能用 `web_search depth 1` 摘要就不 fetch |
| X-13 | DNS 一轮全 `nxdomain` / 超时 | 并发过高 / 临时故障 | `--workers 8` 重跑；单域二次查询后再下结论 |
| X-14 | HTML 表格没渲染 | python-markdown 要求表前空行；或没装 `markdown`（降级转换） | parts 里表前留空行；`pip install markdown` 后重建 |
| X-15 | README 项插错位置 | 用「最后一行」而不是「最后一个编号项」 | 用配方 D 的正则定位 |
| X-16 | 总账 / Q 行重复 | 脚本跑了两遍且无存在性检查 | 先 `grep -c`，再插 |
| X-17 | 渲染后 `内容确有差异` 几千份 | 改了共享渲染规则 / 日期 | 看 `git diff --stat`；非预期就 `git checkout -- "Saga Clients"` 回滚再查 |
| X-18 | `lt_roster.py` 数字与预期差很多 | External `overrides.json` 结构写坏 / Planet CSV 列错位 | `python3 -c "import json;json.load(open('data/external_clients/overrides.json'))"`；CSV 用 DictWriter 保列序 |
| X-19 | 快照失败一大片 | 运行器单晚网络问题 | 不动；只在连续两晚失败 + DNS 死才打回 |
| X-20 | `gh` 403 / 推 workflow 被拒 | 沙箱令牌权限 | 写 YAML 到 docs 让 Simon 粘贴；Actions 由他点 |
| X-21 | heredoc 里 python 报 `{` 语法错 | f-string 里有字面花括号 / 反斜杠 | 不用 f-string 或用 `{{ }}`；表达式里不放反斜杠 |
| X-22 | 测试把失败记录写进了真实快照目录 | `site_snapshot` 本地测试没加 `--snap-dir` | 用 `--snap-dir /tmp/x`；已写入的 `git checkout --` 回滚 |

---

## 9. ⛔ 禁区（一条都不能碰；碰了先回滚再报告）

1. 手改渲染产物：`Saga Clients/**`、`External Clients/**`、`profile/**`、`entities.json`、`客户主表.csv`、`docs/发送包/**`、`变更日志.md`、任何 `build.py` 生成的 MD/HTML。
2. 覆盖 / 删除 / 重命名 V0 答卷与任何旧版本文件；新版本永远是新文件。
3. 发明事实：没来源的邮箱、人名、价格、证书、成立年、员工数；把 Simon 的备注当作「客户说的」。
4. 给客户写：电话、152 手机、s. 邮箱、中文、竞品名、「我们查了你的登记」、禁词表任一词、两个问题。
5. 让 Simon 去问 Peter / HRUI / 任何供应商要价；让他做 Agent 能做的事。
6. 主动发信（任何邮箱）；用 E 箱首触（Elsa 首触未定）。
7. 永久 pass 任何不满足 D-04 三条刚性条件的户；把 C 当垃圾删掉。
8. 重新挖 Mikrotik / 重跑 CCTV 代理 / 在 Planet 暂停期挖 PLANET 经销商。
9. Git：切分支、碰 `main`、`--force`、`reset --hard` 掉未推送工作、提交 `__pycache__` / `/tmp` 产物 / 密钥。
10. 一轮问 Simon 多个问题；不给默认就问；问他已经答过的。
11. 编造时间戳；台账跳过任一件；对话全记录改旧行。
12. 用记忆回答「搞定没」—— 必须跑命令看当前数字。
13. 把 S/A 邮箱接 Arena 连接器写进建议。
14. 用「应该 / 大概 / 可能已经」收尾一个步骤。
15. 在报告里堆术语、堆解释、重复上一轮说过的话。

---

## 10. 质量门（交付前 12 项自检，全部 ✔ 才能收工）

| # | 自检 | 怎么验 |
|---|---|---|
| 1 | 产出文件存在、大小合理 | `ls -la`；MD `grep -c "^## "` |
| 2 | 数字与声称一致 | 刚跑的命令输出截到报告里 |
| 3 | 渲染链全绿 | R02 八步 / External / Planet |
| 4 | 幂等 | 批脚本第二遍 0 写入 |
| 5 | 每条新事实有 quote + url + date | 抽 3 条 `grep` |
| 6 | 没有手改产物 | `git diff --stat` 里的渲染件变动可由脚本解释 |
| 7 | 没有禁词 / 禁事实 | 信稿过 `audit_ab.py`；对外文件跑下方「禁词检查」命令，输出为 0 |
| 8 | 台账四件 + 变更日志 | 四个 `grep -c` 都 = 1；changelog 行数增加 |
| 9 | 推送成功 | `ls-remote` = `HEAD` |
| 10 | 时间戳真实 | 来自 `date -u` |
| 11 | 报告是大白话、有「你要做啥」 | 对照 §3.2 模板 |
| 12 | 没有留下疑问给 Simon 超过 1 个 | 其余进 Q 清单 |

禁词检查（对外英文文件 / 信稿）：
```
grep -ciE "list price|in stock|free sample|trading company|oem factory|ndaa|taa|general agent|we manufacture|marvell ecosystem|sonic|onie|cheap|best price|leading manufacturer" <文件>
```

---

## 11. 与《方法论全集》的关系、本书如何更新、待补剧本

- **V1 = `docs/方法论_全集_2026-10-27.md`**（42 KB，2026-10-27 10:34Z @ `d9d20f297`）：按「解决什么 → 怎么做 → 坑 → 文件 → 诞生」讲了 A1–A6 入库 / B1–B4 客户库 / C1–C7 加厚 / D1–D3 对外 / E1–E5 基础设施 / F / G + 开工十条。它停在 10-27 的公司底数轮，**没有**：C 池三闸、P 池、长期客户群（Q-76 / Q-77）、A/B v5、External / Planet 同尺、LT-R 复核规则、快照 → 加厚、缺口盘点、Actions ALL / cron、全景信息包、本书。
- **《方法论全集》2026-10-29 增补版**（`docs/方法论_全集_2026-10-29.md`）= 正本：在 V1 之上加了 §Ⅰ 思维方法 M1–M14 与 20 个新法（A7 / B5–B8 / C8–C13 / D4–D5 / E6–E10），讲「怎么想、为什么」。
- **本书 = 它的命令级附录**：只写「现在怎么做」。V1 继续作为历史与原理读物；本书引用到的方案细节以原方案文档为准（`docs/C池三闸筛选_方案_2026-10-29.md`、`docs/长期客户群_方案与复核_2026-10-29.md`、`docs/AB判定_新标准_讨论稿_2026-10-29.md`、`docs/公司底数_作业规程.md`、`docs/methodology/死路与死链备案.md`、`docs/教程_云盘大文件入库管道_给其他Agent_2026-10-24.md`）。
- **怎么更新本书**：改 `scripts/sop_v2/parts/s1–s4.md` → `python3 scripts/sop_v2/build.py` → 新日期产出新文件（旧日期文件保留）。每当一个剧本的命令 / 预期输出 / 判定变了，就在同一轮更新对应 part（否则下一个 agent 会照着错的做）。
- **待补剧本**（出现新流程时在此登记再写正文）：R26 PI / 成单录入（`data/pi_orders/*.csv` + 毛利复盘）；R27 供应商价表更生成（`pricing.py` / `pricing_hrui.py` + 汇率）；R28 C 池三闸再筛（`sieve.py --gate0 / --queue`，当前已筛完，下轮新 C 进来再跑）；R29 全景信息包更新（`scripts/saga_intro/parts` + build）。

---

## 12. 来源清单（本书每条都能在仓库里找到依据）

- 规则与原话：`AGENT-CONSTITUTION.md`、`AGENT-README.md`、`docs/requirements/用户要求总账.md`（PR-01…PR-02-77、INH-01…17）、`docs/requirements/对话全记录.md`、`docs/requirements/待统一处理问题清单.md`（Q-01…Q-77）。
- 流程原文：`docs/方法论_全集_2026-10-27.md`、`docs/公司底数_作业规程.md`、`docs/C池三闸筛选_方案_2026-10-29.md`、`docs/长期客户群_方案与复核_2026-10-29.md`、`docs/长期客户群_深挖缺口_2026-10-29.md`、`docs/AB判定_新标准_讨论稿_2026-10-29.md`、`docs/教程_云盘大文件入库管道_给其他Agent_2026-10-24.md`、`scripts/drive_ingest/操作步骤.md`、`scripts/gmail_ingest/操作步骤.md`、`docs/methodology/死路与死链备案.md`、`docs/rules/*.md`。
- 脚本（命令与预期输出均为 2026-10-29 实跑）：`scripts/saga_clients/{renumber,build,render,audit_full,audit,audit_ab,deepen,add_research,research_store,registry_store,mx_check,gmail_digest,sieve,lt_snapshot_thicken,site_snapshot}.py`、`scripts/saga_clients/lt_review_batches/{lt_review_lib,lt_r_006}.py`、`scripts/{lt_roster,lt_gap_audit,lt_snapshot_list,lt_review_x_p_003,add_batch,render,audit,changelog,pricing,pricing_hrui}.py`、`scripts/external_clients/{render,research_store,board,lt_cards_003}.py`、`scripts/web_watch/{watch,checklist}.py`、`scripts/saga_intro/build.py`、`.github/workflows/*.yml`。
- 事实类背景：`docs/Saga全景信息包_给其他Agent_2026-10-29.md`（§0–§19）。
