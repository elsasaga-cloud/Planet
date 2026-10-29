@@F_ROWS
| 2026-10-27 T29-U76–U81 | 外部仓库 | 关仓前复查 → 原值抽取 → 独立目录 + X 编号 → 研究卡 + overrides → 发送包（A7 / D4）；六点默认 |
| 2026-10-28 T29-U84–U112 | 双线 | External R04–R13（波 2 / 波 3）；公司底数第 101–118 批（规程 §3）；「任务时间拉长」U85/U86；U112 最后一批 |
| 2026-10-29 T29-U113–U114 | 节奏 | 「多搞一些 任务时间拉长 40 分钟甚至 1 个小时」→ 每轮 40–60 分钟（E9） |
| 2026-10-29 02:22Z–11:18Z T29-U115–U124 | **C 池三闸** | 方案先行（U116「评估一下任务量 设计一个方案」）；闸 0 刚性三条 + Simon 四条否决（U117）；闸 1–3；External XC / Planet 仓同法（C8 / M4 / M5） |
| 2026-10-29 11:53Z–12:38Z T29-U125–U127 | A/B 新标准 | 诊断表 → A1–A6 / B1–B6 → 三口径模拟 → 讨论稿 + HTML 工作台（B6 / M3） |
| 2026-10-29 12:54Z T29-U128 | **Q-76 单一体系** | 五点裁定：A/B 长期跟 / C 捞出直接 B / 三库同尺 / 规模不设硬指标 / 「再去过一遍 = 调研 + 加厚」（B5 / B7 / C9） |
| 2026-10-29 13:32Z–14:15Z T29-U129–U130 | 复核收口 | LT-R07 External 669 / LT-R08 Planet 23；Q-77 分层默认方案（B8 / D5 / M10） |
| 2026-10-29 14:22Z–15:00Z T29-U131 | **缺口盘点** | 七维一户一行；快照清单 751 → customer-watch 顺手补抓 → thicken 幂等；LT-R09 域名二次验证（C10 / C11 / C12 / M6 / M7） |
| 2026-10-29 15:15Z T29-U132 | 事实层 | 《Saga 全景信息包（给其他 Agent）》MD + HTML，生成器模式（E8） |
| 2026-10-29 15:40Z 起 T29-U133 | 方法层 | 先误做成命令手册（`方法论_V2_像素级SOP`，留作附录）→ Simon「你搞错了」→ 本增补版：Ⅰ 思维方法 M1–M14 + A7 / B5–B8 / C8–C13 / D4–D5 / E6–E10（M1 / M14） |
@@G_NOTE
> **2026-10-29 更新**：本预案已于 2026-10-27 11:4xZ–13:0xZ（T29-U77–U81）执行，落地方法见 **§A7**；与预案的差异：编号前缀用 `XA/XB/XC + 仓字母`（不是 `X1-001`）；定级没有先用「热 / 温 / 冷」而是直接按 Saga 真实情况 A/B/C（Simon U81），后来 Q-76 三库同尺；Q-66 三问全部按默认（README 自判产品线 / 先全抽不过滤 / Mikrotik 不碰）。原文保留如下，供对照。
@@MAP_ROWS
| 长期客户群（Q-76） | `docs/长期客户群_方案与复核_2026-10-29.md`、`长期客户群_名册_2026-10-29.md`、`长期客户群_深挖缺口_2026-10-29.md`；`data/长期客户群_复核记录.csv`（1,219）、`长期客户群_复核队列_2026-10-29.csv`、`长期客户群_补快照清单_2026-10-29.json`、`长期客户群_快照打回候选_*.csv`；`scripts/lt_roster.py`、`lt_gap_audit.py`、`lt_snapshot_list.py`、`saga_clients/lt_snapshot_thicken.py`、`saga_clients/lt_review_batches/`、`lt_review_x_p_00N.py` |
| C 池三闸 / P 池 | `docs/C池三闸筛选_方案_2026-10-29.md`、`docs/P池_资产池名册_2026-10-29.md`、`docs/P池_巡检清单_2026-12-28.md`；`data/saga_clients/sieve.json`、`P池_巡检表_2026-10-29.csv`；`scripts/saga_clients/sieve.py`、`sieve_batches/`、`scripts/external_clients/sieve_x.py`、`scripts/sieve_p.py`、`scripts/web_watch/checklist.py` |
| A/B 新标准 | `docs/AB判定_新标准_讨论稿_2026-10-29.md`；`data/saga_clients/AB新标准_模拟_2026-10-29.csv`、`AB并池_预演_2026-10-29.csv` |
| External Clients | `External Clients/<repo>/A|B|C/`；`data/external_clients/{cctv,edgecore,mikrotik}.json`、`overrides.json`、`research/`（1,096）；`scripts/external_clients/{extract_*,research_store,render,board,sieve_x}.py`、`cards/`；`docs/external_repos/第2步_*`、`docs/跟进总台.md`、`docs/发送包/` |
| Planet 仓 | `data/客户名单_Planet渠道_2026-10.csv`（129；列 `人工定级` / `长期群复核`）、`batch/*.json`、`profile/`；`scripts/{add_batch,render,audit,p_roster}.py` |
| 给其他 Agent 的三本 | 事实 `docs/Saga全景信息包_给其他Agent_2026-10-29.md`（`scripts/saga_intro/`）；方法 = 本文（`scripts/methodology_v2/`）；命令 `docs/方法论_V2_像素级SOP_2026-10-29.md`（`scripts/sop_v2/`） |
| 公司底数（续） | `data/saga_clients/registry/*.json`（1,487 行，第 82–136 批）；`scripts/saga_clients/registry_batches/`、`patches/batchNN_kp.py`；`docs/公司底数_作业规程.md` §3 进度 |
@@START_ITEMS
11. 动手前先复述：一句话任务 + 可验证的验收标准，写在回复第一行（M1）；被纠偏先认、不辩、不删、重做、记账（M14）。
12. 「都搞完了吗」一律先建维度表再回答（M7）；回答用刚跑出的数字，不用记忆（M13）。
13. 负面结论（死域 / 404 / 退信 / 快照失败）二次独立验证后才能成为打回或 pass 理由（M6）；不可逆的只有永久 pass，其余都写可逆条件（M5）。
14. 三库同一把尺：等级看 grade 不看编号前缀；任何等级变动后重跑 `lt_roster.py`（B5）；台账幂等、PR 行按编号最大插（E7）。
@@FOOTER
*— 初版 2026-10-27 10:34Z 起草；增补版 2026-10-29 生成（时间戳见头部）。初版原件 `docs/方法论_全集_2026-10-27.md` 保留不改。—*
