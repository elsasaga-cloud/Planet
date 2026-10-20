# AGENT-README（Planet 仓库操作手册）

> 每轮开工：读宪法 → 本文件 → 总账最新章 → 对话全记录最近几轮 → README 进度。回复首行 `📋 上下文已加载（…）`。

## 1. 任务与边界（一分钟版）

- 客户 = PLANET Technology 在欧洲 + 美加的**独立**渠道（分销/电商/安防经销/工业经销/集成商/贴牌品牌商）。PLANET 本体与其关联公司 = 信号源，禁止触达。
- 我方 = Saga Telecom（大陆贸易商 SOHO，SmartByte Marvell 方案为核心）。不做云管理/轨交/IP67/消费级；无 UL。详见 `docs/reference/Saga公司画像与边界.md`。
- 评级 A/B/C 规则不改；编号 `PA-/PB-/PC-xxx` 冻结只追加；档案不手改。
- 报价 = SmartByte CNY × (1.2/1.25/1.3) ÷ 汇率；MD 写 Saga 型号，无对应写 SmartByte 并注明。
- 每轮必写：`docs/requirements/对话全记录.md`（原文 + 两个时间戳）、`用户要求总账.md`（PR-xx）、README 进度、审计 errors 0。

## 2. 流水线

```bash
# 0) 环境（沙箱重置后）
python3 -m venv /home/user/.venv_planet && /home/user/.venv_planet/bin/pip install openpyxl pdfplumber
PY=/home/user/.venv_planet/bin/python

# 1) 价格表（用户更新 xlsx/pdf 或汇率变动时重跑；--rate/--rate-date 传新汇率）
$PY scripts/pricing.py --rate 6.69 --rate-date 2026-10-17

# 2) 挖掘：web_search / fetch_page → 写 batch/<YYYY-MM-DD>_<批名>.json（结构见 batch/2026-10-19_W01_*.json）
#    每户必有：_code（预留编号，按 add_batch 分配结果回填）、rating、rating_basis、evidence[{claim,quote,url,date,level}]、contacts[]（只记公开邮箱）
#    批次必有：queries[]、skipped[{name,reason}]、pending_next_wave[]

# 3) 入表 → 渲染 → 审计
cd scripts && $PY add_batch.py && $PY render.py && $PY audit.py && cd ..

# 4) 自检写入
grep -c "" data/客户名单_Planet渠道_2026-10.csv ; ls profile/A profile/B profile/C | wc -l

# 5) 记账：对话全记录（Txx）、总账（PR-xx）、README 进度表、docs/audit/全仓审计.md 已由 audit.py 生成
# 6) git add -A && git commit && git push origin arena/3f35b9b3-planet
```

### 编号分配约定

`add_batch.py` 按 CSV 现有最大号 +1 分配；批次 JSON 里的 `_code` 用于 `render.py` 回找证据，因此**写 JSON 前先看 CSV 当前最大号**，预留的 `_code` 必须与 `add_batch.py` 实际分配一致（同一批内按 A/B/C 各自顺序排列即可一致）。若不一致，以 CSV 为准修正 JSON 的 `_code` 后重跑 render。

### 升降级

改 CSV `评级`（或用户填 `人工定级`）→ `render.py` 自动把档案移到新目录，编号不变。在 CSV `备注` 记「YYYY-MM-DD 由 B→A：原因」。

## 3. 文件地图

| 路径 | 作用 |
|---|---|
| `docs/requirements/对话全记录.md` | ★ 宪法级：逐轮原文 + 时间戳 |
| `docs/requirements/用户要求总账.md` | PR-xx 要求台账 + INH-xx 继承规则 |
| `docs/rules/报价与型号规则.md` | 公式、档位、型号书写、已知矛盾 |
| `docs/rules/客户分级与去重规则.md` | ABC、编号、去重键、CSV 26 列定义 |
| `docs/rules/客户档案结构与内容规则.md` | Mikrotik R56 v2 骨架原文（继承） |
| `docs/reference/价格表_三档加价_USD.md` + `data/价格主表.csv` | 135 个 SmartByte 型号 × 三档 USD × Saga 对位 |
| `docs/reference/PLANET_PoE产品线与Saga对照.md` | PLANET 型号 → Saga 对位与「无对应」清单 |
| `docs/reference/从Mikrotik仓库继承的规则摘要.md` | 读两仓库的结论 |
| `docs/reference/Saga公司画像与边界.md` | 用户背景 docx 的结构化版 |
| `docs/methodology/Planet客户挖掘方法论.md` | M1–M10 方法与国家顺序 |
| `docs/methodology/死路与死链备案.md` | 404/登录墙/匿名页 + 信号源名单 + 区域外命中 |
| `data/Mikrotik仓库已有PLANET相关客户_对照.csv` | 跨仓去重参照 46 行（W09 +1 行：A-482 IPC2U；此前 45 行：W03 +8 行，W04 改写 8 行说明，W05 改写 7 行，W06 +5 行：A-541/A-270/A-546/A-096/A-553，W07 +2 行：B-201/B-274） |
| `docs/requirements/待统一处理问题清单.md` | T07 起所有待用户裁定事项（Q-xx 冻结编号 + 默认处理）；Agent 不再逐轮提问 |

## 4. 操作记录

| 日期 (UTC) | 轮 | 动作 | 结果 |
|---|---|---|---|
| 2026-10-19 14:31–15:05 | PR-01 | 合并 origin/main 上传件；克隆并通读 Mikrotik 仓库；读价格表/背景；建骨架与规则；pricing.py 生成三档表；W01 挖掘 15 户（web_search ×15、fetch_page ×12）；add_batch/render/audit | CSV 15 行，profile 15 份，audit errors 0 |
| 2026-10-19 15:05–15:35 | PR-02 | T03 落账（对话全记录 / 总账 PR-02-01…04 / 报价规则档位固化 / PC-005 人工定级 C）；W02 挖掘（web_search ≈60 次，depth 1；Mikrotik 主表 1032 行 grep 去重）；批次 JSON 由 `/home/user/_scratch/build_w02.py`（仓库外 scratch）生成；add_batch（added=25 merged=4）/render（40）/audit；修 3 条 Mikrotik 证据 URL（本地路径 → GitHub blob URL） | CSV 40 行，profile 40 份，audit errors 0 |
| 2026-10-19 15:28–15:46 | PR-02 · W03 | T04「继续挖」落账；W03 挖掘（web_search ≈35 次，depth 1；Mikrotik 主表 grep 含域名 token，新增同户 6 组）；批次 JSON 由 `/home/user/_scratch/build_w03.py` 生成；add_batch（added=13 merged=7）/render（53）/audit；**直接修补**：W01 JSON PB-001 mikrotik_ref、W02 JSON PA-009 contacts/rating_basis（steffo@ 标发不过去 + 新增 fredrik.brunzell@）、CSV PA-009 入口单元格（add_batch 对既有行只填空列，故手改）；README/总账/死路/方法论/对照 CSV 同步 | CSV 53 行，profile 53 份，audit errors 0 |
| 2026-10-19 15:47–16:05 | PR-02 · W04 | T05「继续挖 着重北美+欧洲+土耳其」落账（总账 PR-02-05、INH-02 注记）；W04 挖掘（web_search ≈30 次 depth 1 + fetch_page ×2：PTUSA where-to-buy、Pulse 联系 PDF）；Mikrotik 主表 grep（土耳其 11 行均非 PLANET；C-089/C-085/C-067/C-015 补邮箱重评；A-497/A-480/A-469/A-032 并档）；批次 JSON 由 `/home/user/_scratch/build_w04.py` 生成；add_batch（added=13 merged=0）/render（66）/audit；README（进度行 + A 类 + 作战方案 8 划掉/9 新增）/总账/死路 §1§3§4/方法论 §五 W04/对照 CSV 8 行「对照说明」改写（不加行）| CSV 66 行，profile 66 份，audit errors 0 |
| 2026-10-19 16:06–16:20 | PR-02 · W05 | T06 落账（对话全记录 T06、总账 PR-02-06、规则 §4.3 T06 例外；CSV 直接改：PC-011 评级/人工定级 B + 5 户备注；W04 JSON 由 build_w04.py 重生成并重跑 add_batch=跳过既有行）；W05 挖掘（web_search 15 次；Mikrotik 主表**全列** grep PLANET → 新命中 5 行）；批次 JSON 由 `/home/user/_scratch/build_w05.py` 生成；add_batch（added=5）/render（71）/audit；README/总账/死路/方法论/对照 CSV（7 行说明改写，不加行）| CSV 71 行，profile 71 份，audit errors 0 |
| 2026-10-20 01:08–01:20 | PR-02 · W06 | 沙箱重置后 `git reset --soft origin/arena/3f35b9b3-planet` 对齐、重克隆 Mikrotik 参照；T07 落账（对话全记录 T07、总账 PR-02-07、新建 待统一处理问题清单 Q-01…Q-10，本轮追加 Q-11/Q-12）；W06 挖掘（web_search 13 次 depth 1；Mikrotik 工业品牌渠道行 69 行候选 → 分组域名查询）；批次 JSON 由 `/home/user/_scratch/build_w06.py` 生成；add_batch（added=4 merged=1）/render（75）/audit；CSV 直接改 PB-005 对照 A-541（W01 JSON 同步）；对照 CSV +5 行；README/总账/死路/方法论 | CSV 75 行，profile 75 份，audit errors 0 |
| 2026-10-20 02:00–02:15 | PR-02 · W07 | 沙箱第二次重置后同法对齐（`git reset --soft origin/…` + 重克隆 Mikrotik 参照）；T08「继续挖」落账（对话全记录 T08 / T08-R）；W07 挖掘（web_search 17 次 depth 1 + fetch_page 1：Mikrotik「分销（MikroTik 官方）/WISP」行 ≈110 域名 12 组分组查询 → 2 命中）；批次 JSON 由 `/home/user/_scratch/build_w07.py` 生成；add_batch（added=2 merged=0）/render（77）/audit；对照 CSV +2 行（45）；README/总账/死路/方法论 | CSV 77 行，profile 77 份，audit errors 0 |
| 2026-10-20 02:17–02:27 | PR-02 · W08 | T09「继续挖」落账（对话全记录 T09 / T09-R）；W08 挖掘（web_search 21 次 depth 1 + fetch_page 8 段：安防分销 dealer-only 角度 PL/TR/ES/DE/UK/US + 新矿脉 M12 美国海关提单反查 ImportGenius/ImportYeti）；批次 JSON 由 `/home/user/_scratch/build_w08.py` 生成；add_batch（added=3 merged=0）/render（80）/audit；PC-012 C 级细分与 M11→M12 来源字样在 CSV + 批次 JSON 中直接订正（add_batch 不重跑已入库批次）；对照 CSV 不变（45）；README/总账/问题清单 Q-13 Q-14/死路/方法论 §一 M12 + §五 W08 | CSV 80 行，profile 80 份，audit errors 0 |
| 2026-10-20 02:30–02:50 | PR-02 · W09 | T10「继续挖」落账（对话全记录 T10 / T10-R）；W09 挖掘（web_search 20 次 depth 1 + fetch_page 6 段：M12 延伸 ImportKey/ImportYeti/Volza、去型号本地语安防批发 CZ/HU/FR/NL/SE/ES/TR/DE、BE/CH/GR/IE/DK 20 域名复核、Oprema 核身、linhawstore 回查 ×3）；批次 JSON 由 `/home/user/_scratch/build_w09.py` 生成（3 新户 + PB-002/PB-018 补证条）；add_batch（added=3 merged=2）/render（83）/audit；**PB-053 事后更正**直接改 W08 JSON + 主表（信号/切入点/评级依据/备注/证据 +2 条）；PB-055 跨仓证据 URL 改为 GitHub 文件链接以过审计；对照 CSV +1 行（A-482）；`scripts/render.py` 问候语修正（占位联系人 → Hi there，44 份 profile 重渲染）；README/总账/死路/方法论 §一 M12 边界 + §五 W09 | CSV 83 行，profile 83 份，对照 CSV 46 行，audit errors 0 |
| 2026-10-20 02:52–03:15 | PR-02 · W10 | T11「继续搞」落账（对话全记录 T11 / T11-R）；W10：A 级主证据页回查 10 段 fetch（8 现役 / 1 URL 老化更新 / 1 JS 不可抓）；web_search 8 次（IT / PL 去型号安防 + 核身 ×2 + DE M11 + CLR Networks + Lin Haw 进口商页）；批次 JSON 由 `/home/user/_scratch/build_w10.py` 生成（2 新户 + 9 条 A 级回查补证条）；add_batch（added=2 merged=9）/render（85）/audit；事后更正直接改 JSON + 主表：PB-053（W08 JSON，第二次：最近一票 2017-04-04）、PB-054（W09 JSON：CLR 线 ODM 切入）、PA-010（W02 JSON：旧 URL 标注）；Q-15 追加；`scripts/render.py` 并档户邮件块改为『本仓不发』+ 同户警示；README/总账/死路/方法论 §五 W10 | CSV 85 行，profile 85 份，对照 CSV 46 行，audit errors 0 |
| 2026-10-20 03:18–03:40 | PR-02 · W11 | 沙箱第三次重置后恢复（git reset --soft origin 分支，重克隆 Mikrotik 仓库）；T12「继续搞」落账（对话全记录 T12 / T12-R）；W11：A 级剩余 6 户回查 fetch 9 段（RFOG / Aspectis / Direktronik ×2 / PROFIcomms ×2 现役；Young ×3 失败）；web_search 6 次（CZ / HU / TR / FR 去型号安防批发各 1 + FR 新户核身 ×2）+ 新户核身 fetch 4 段；批次 JSON 由 `/home/user/_scratch/build_w11.py` 生成（2 新户 + 5 条回查/补证条，含 Mikrotik 同户 grep 断言）；add_batch（added=2 merged=5）/render（87）/audit；`scripts/render.py` 并档户「跟进步骤」改『Mikrotik 侧回复后再定』预案块 + 邮件样板识别「批发/进口商」类型；README/总账/死路/方法论 §五 W11 | CSV 87 行，profile 87 份，对照 CSV 46 行，audit errors 0 |
| PR-02 · T13 Drive/Gmail | 2026-10-20 | 用户 T13「drive 和 email 已接入，主要是 drive，好好构思一下咋处理」→ **Drive 盘点 + 三层入库方案 + Tier1 入库 14 篇 + 中文速查 + Gmail 索引级盘点**：① Drive 8 顶层目录逐层列出（整盘 200 行会截断），`data/drive_manifest.csv` 56 行；② `docs/drive/00-Drive盘点与入库方案.md`（Tier1 全文 / Tier2 索引+按需抓 docx / Tier3 仅索引；二进制不进 Git）；③ `docs/drive/MUST-KNOW/` 12 篇英文原文 MD + STOS 节选 + 证书索引；④ `docs/reference/Saga商务条款速查.md`；⑤ Gmail：3,675 封，Replied 51 会话，Elsa 月度群发 ≈12 主题，PA-006 Kyma 2025-02 曾触达，多域名 OR 检索不可靠 → 下一轮分页 `in:sent` 建触达表；⑥ Q-18…Q-21 立项 | 87（不变） | errors: 0 |
| PR-02 · T14 SmartByte 官网 | 2026-10-20 | 用户 T14「以 SmartByte 官网为准，抓吧入库」→ **P0 阶段**：fetch_page 16 次（首页、sitemap 5 块、6 个公司/政策页、固件 7.5 全文、Managed Industrial 第 1 页 3 块、详情页样本）；入库 `docs/smartbyte/00-…方案.md` + `公司与政策页_2026-10-20.md` + `data/smartbyte_官网型号索引.csv`（13 行，基型号归一匹配）；速查表保修/DOA/OEM 按官网改写；Drive 方案标注 Q3 旧版；Q-22（保修传递）/ Q-23（Elsa 发件）立项；经验：品类页分页 ≈12 型号/页、chunk 0 为导航 + 4 个型号、chunk 1 为其余 8 个 + 分页；官网衍生型后缀 -D/-SD/-U/-nBT 需归一到价格主表基型号 | 87（不变） | errors: 0 |

## 5. 已知坑（本仓库）

- `fetch_page` 对 planet.com.tw 可用，但导航链接不在 markdown 里；案例研究页匿名。
- `web_search` 返回体积大：用 `depth 1`，一次只查一家的联系方式（`<域名> contact email`），比逐页 fetch 省上下文。
- 第三方名录（cylex/zoominfo/rocketreach）的人名只记「第三方名录级·待核」，不写邮箱；LinkedIn 只记入口。
- CSV 字段含逗号，`cut -d,` 看列会错位，用 Python csv 模块。
