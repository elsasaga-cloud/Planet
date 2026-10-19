# Planet — PLANET Technology 欧美渠道客户挖掘（Saga Telecom）

> **一句话**：把 PLANET Technology（台湾）在欧洲 + 美国/加拿大的分销商、集成商、安防/工业经销、贴牌品牌商找出来，按 Mikrotik 仓库同一套规则定级建档，供 Saga 以「Marvell 方案 PoE/工业交换机第二货源 + 贴牌 + 功能定制」切入。
>
> **先读**：`AGENT-CONSTITUTION.md` → `AGENT-README.md` → `docs/requirements/用户要求总账.md` → `docs/requirements/对话全记录.md`。

## 进度（每轮更新）

| 轮次 | 日期 | 内容 | 客户池 | 审计 |
|---|---|---|---|---|
| PR-01 | 2026-10-19 | 读完 Mikrotik 两仓库规则；读上传价格表/背景；建仓库骨架、规则、价格三档表、PLANET→Saga 对照、方法论；**W01 第一批 15 户**（DE/IT/FR/ES/PL/UK/US） | **15**（A 3 / B 7 / C 5） | errors: 0 |
| PR-02 | 2026-10-19 | 用户裁决落账（Versa=C、档位规则 OK、PDF 价差搁置、「往死里挖」）；**W02 第二批 +25 户**（UK/IE/DE/IT/CZ/HU/SE/NO/FR/PL/CA/US，web_search ≈60 次）+ 4 户既有档补具名 KP（Spectra/Neteon/Paragon/W3CAM）；Mikrotik 仓库 1032 行 grep 去重（命中 BSC=A-532、Jampel=C-031、100MEGA=A-499/C-173） | **40**（A 10 / B 22 / C 8） | errors: 0 |

- 主表：`data/客户名单_Planet渠道_2026-10.csv`（26 列，前 22 列与 Mikrotik 仓库一致）
- 档案：`profile/A|B|C/`，索引 `profile/00-索引.md`
- 原始证据：`batch/2026-10-19_W01_*.json`
- W01 A 类：**PA-001 4Power（IT，自有品牌 4Net）**、**PA-002 Cartronic Group（ES，具名 KP 直邮）**、**PA-003 RFOG POLAND（PL，业主直邮）**
- W02 A 类：**PA-004 NSI Distribution（CA，安防批发 9 分部 + 自有品牌 Norelco，Norm Matinnia 直邮）**、**PA-005 Jampel（IT，PLANET 官方分销 + Moxa，PM Stefano Cinti 直邮·待核）**、**PA-006 Kyma（IT，30 年进口 PLANET + 已进口中国 3onedata，3 人家族企业业主直达）**、**PA-007 ALARM ABSOLON（CZ，1989 年起安防批发，销售 Tikovský 直邮）**、**PA-008 Aspectis（HU，IP 安防 VAD，总经理 Laczkó 直邮）**、**PA-009 Direktronik（SE，自有品牌分销商，steffo@ 直邮·角色待核）**、**PA-010 iOC Tech（CA，PLANET 授权分销 2–10 人，Director 具名）**
- W02 原始证据：`batch/2026-10-19_W02_*.json`（29 条：25 新户 + 4 补证；skipped 15 组、pending 9 项、queries 14 组）

## 作战方案（用户问「看看如何搞」· 2026-10-19 版）

1. **信号源现实**：PLANET 官网**没有公开的经销商定位器**（`where-to-buy` 404，Partner Zone 需登录，案例研究匿名）；北美总代 planetechusa.com 的转售名单只有 5 家巨头。→ 只能靠 `web_search` + `fetch_page` 逐页挖（沙箱 curl 不通），方法见 `docs/methodology/Planet客户挖掘方法论.md`（M1 型号反查、M2 品牌页反查、M3 分销商下游、M4 项目/博客、M7 白牌反查等 10 法）。
2. **目标与顺序**：第一梯队 DE/UK/IT/ES/FR/NL/PL/US/CA → 第二梯队 AT/CH/BE/北欧/CZ/PT/IE/GR/HU/SK；小国不主动挖；轨交/军工/公共采购守界。
3. **定级**：A = 真实 PoE/交换需求 + 具名直达人 + 体量可拿下；B = 有邮箱可群发；C = 无邮箱/过大/区域外/不对口。编号 `PA-/PB-/PC-` 冻结只追加。与 Mikrotik 仓库 26 行 PLANET 相关户去重（`data/Mikrotik仓库已有PLANET相关客户_对照.csv`）。
4. **每批 10–20 户**：批次 JSON（证据原文 + URL + 日期 + skipped 原因）→ `add_batch.py` → `render.py` → `audit.py`（errors 0）→ README/总账/对话全记录 → push。
5. **报价与型号**：Saga 卖价 = SmartByte CNY × (1.20/1.25/1.30) ÷ 汇率（6.69 @2026-10-17）；MD 写 Saga 型号，无对应时写 SmartByte 型号并注明。三档全表 `docs/reference/价格表_三档加价_USD.md`（135 型号；**9 个型号按今日汇率 +20% 已高于 Saga PDF 列表价**，建议刷新 PDF）。
6. ~~**下一批（W02）计划**~~ **W02 已完成（2026-10-19）**：PLANET Germany GmbH 核为独立微型公司（B）；lwl-shop24 / WoodComm / planet.pl / ISTC 均已处置（B / B / C 巨头 / 跳过-区域外）；NL/BE/AT/CH 品牌页检索**无专业经销命中**（只剩泛电商与聚合站，已 skip）；M1 型号反查以自然语言多语种查询有效（`site:` + 型号为 0 结果），主要命中电商而非集成商；Spectra/Neteon 补到具名 KP。
7. **下一批（W03）计划**：① 美国/加拿大安防与工业集成商（M3 分销商下游：Neteon / M/A Rugged / NSI / iOC 的「客户案例」页；M4 `"Planet" "IGS-" case study`）；② 法国/西班牙/葡萄牙二轮（Abix、accessoires-informatiques、Microsam-CA、Young B.T.S.-HU、CAPS-NL、Digitx-IT 等 pending 9 项逐个核）；③ 北欧 DK/FI 型号反查（丹麦语/芬兰语）；④ M7 白牌反查：以 PLANET 机型外观/固件特征搜欧美自有品牌（Lysora、Norelco、Direktronik、4Net 已是线索）；⑤ 为 W01/W02 的 B 类找具名 KP（FEN、Ballicom、ProVu、WoodComm）；⑥ 用 `fetch_page` 补齐 W02 标「检索摘要/待补证」的原文（Kyma、Absolon、Aspectis、BTS、NSI OEM 页）。

## 目录

```
AGENT-CONSTITUTION.md            宪法（含对话全记录、报价、型号、台厂非客户等条款）
AGENT-README.md                  Agent 操作手册与流水线
README.md                        本文件
docs/requirements/对话全记录.md    ★ 独立带时间戳对话原始记录（只增不删）
docs/requirements/用户要求总账.md  要求台账 PR-xx + 继承规则 INH-xx
docs/rules/                      报价与型号规则 / 客户分级与去重规则 / 客户档案结构与内容规则(继承 R56)
docs/reference/                  从Mikrotik仓库继承的规则摘要 / Saga公司画像与边界 / 价格表_三档加价_USD / PLANET_PoE产品线与Saga对照
docs/methodology/                Planet客户挖掘方法论 / 死路与死链备案
docs/audit/全仓审计.md            scripts/audit.py 输出
data/                            主表 CSV / 价格主表.csv / Mikrotik 对照 CSV
batch/                           每批原始证据 JSON
profile/A|B|C/                   渲染档案（勿手改）
scripts/                         pricing.py / add_batch.py / render.py / audit.py / common.py
*.xlsx *.pdf *.docx              用户上传原件（价格表、Saga 背景）
```

## 环境

`python3 -m venv .venv_planet && .venv_planet/bin/pip install openpyxl pdfplumber`（仅 `pricing.py` 需要；其余脚本纯标准库）。沙箱外网仅 `fetch_page`/`web_search` 工具可达。
