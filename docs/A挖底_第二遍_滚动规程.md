# A 类「挖个底掉」· 第二遍滚动规程（2026-10-31）

> Simon（T29-U138/U139）：情报档长期滚动、建 workflow 定期爬看更新、一轮一轮补到挖不出为止。本页是第二遍怎么滚的操作口径；第一遍（122 户 100% 建档）已于 2026-10-30 收口。

## 1. 自动层（日跑，不用人）
| 步骤 | 工具 | 产出 | 频率 |
|---|---|---|---|
| 新闻 / 申报 / IR / 招聘页 / GitHub 组织 | `scripts/web_watch/watch.py`（源来自 `targets_intel.json`，`intel_targets.py` 生成；A 户 + 挖过的 B 户，≈600 源） | `data/customer_watch/state.json` + 变化日志 | 每天 02:23Z 起（GitHub Actions `customer-watch.yml`） |
| 年报全文 / 10-K / 展会名录 | `watch.py` 的 `intel_docs()`，队列 `data/saga_clients/intel_fetch_queue.json`（`intel/fairs.py` 维护 15 个展会的 10times 参展商页，关键词 = 全部 A 户辨识词） | `data/saga_clients/intel_docs/<code>/*.txt + *.hits.json`，展会在 `_fairs/` | 随日跑；每份文档按 `refresh_days` 重抓（年报 365、展会 30） |
| 官网 / 社媒 / 快照 | 既有 A/B 层监控 + `site_snapshot` | 同上 | 每天 |

日跑现在**先提交巡检结果再做补快照/加厚/文档抓取并二次提交**（2026-10-31 改），后段超时不会丢整轮。

## 2. 入库层（每轮会话第一件事）
```
python3 scripts/saga_clients/intel/ingest_watch.py     # 新条目 → 研究档 intel（WATCH / WATCH-DOC / WATCH-FAIR 批次）+ docs/A情报_变动摘要_<日期>.md
python3 scripts/saga_clients/intel/next_round.py       # 过期/缺失维度 → docs/A挖底_下一轮.md（含建议查询词）
```
- 标题级信息（新闻 / 疑似参展）入库时标「未逐条核读」；用于写信前看一眼原文。
- 游标 `data/saga_clients/intel_ingest_state.json`，重复跑不重复入。

## 3. 人工层（每轮按工单挖）
- 顺序：土耳其 → 北美 → 欧洲 → 俄语区 → 南亚 → 亚太 → 中东 → 非洲 → 拉美；每户最多 3 个维度/轮。
- 维度阈值：年报/财务 365 天 · 登记 365 · 领英公司页 180 · KP 180 · 人事变动 90 · 展会/活动 365 · GitHub 180 · 供应商/品牌关系 365。
- 每条事实：日期 + 原文引文 + URL + 中文要点（`intel_store.add`，批次 `INTEL-nn`，脚本放 `scripts/saga_clients/intel_batches/`）；查过未得也记（`found=False`），免得重复查。
- 上市/有账目的户（Netaş、Actelis、HFCL、Direktronik、Impakt、FCNET、Etic、LivEye、EL.SI.、STS Italia、TAV、Companies House 6 户…）：年报里**采购相关段落**（供应商政策、资本开支、网络设备投入、付款周期）必摘。
- 发现「不是极为 OK」的证据（微型 / 结构性采购障碍 / 守界 / 巨头子公司 / 项目型终端）→ `patches/p80_a_deep2.py` 追加批次下放 B，报告 §4b 供捞回。

## 4. 周期性重扫
- GitHub 技术足迹：`python3 scripts/saga_clients/intel/github_scan.py` 删除 `data/saga_clients/intel_github_<日期>.json` 后重跑（每 180 天）。
- 登记库：A 季度复核（`docs/公司底数_作业规程.md`）；新入 A 的户「新入库即查」。
- 进度板：`python3 scripts/saga_clients/intel/progress.py` → `docs/A挖底_进度.md`。

## 5. 验收口径（第二遍「跑通」的标志）
1. 日跑提交里出现 `intel_*` 源的状态与 `intel_docs/` 文件；2. `ingest_watch.py` 产出非空变动摘要；3. 展会名录至少命中 1 户并经人工核实；4. 年报全文关键词窗口入到对应户的「年报/财务」。
