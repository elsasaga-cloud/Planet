# Planet — PLANET Technology 欧美渠道客户挖掘（Saga Telecom）

> **一句话**：把 PLANET Technology（台湾）在欧洲 + 美国/加拿大的分销商、集成商、安防/工业经销、贴牌品牌商找出来，按 Mikrotik 仓库同一套规则定级建档，供 Saga 以「Marvell 方案 PoE/工业交换机第二货源 + 贴牌 + 功能定制」切入。
>
> **先读**：`AGENT-CONSTITUTION.md` → `AGENT-README.md` → `docs/requirements/用户要求总账.md` → `docs/requirements/对话全记录.md`。

## 进度（每轮更新）

| 轮次 | 日期 | 内容 | 客户池 | 审计 |
|---|---|---|---|---|
| PR-01 | 2026-10-19 | 读完 Mikrotik 两仓库规则；读上传价格表/背景；建仓库骨架、规则、价格三档表、PLANET→Saga 对照、方法论；**W01 第一批 15 户**（DE/IT/FR/ES/PL/UK/US） | **15**（A 3 / B 7 / C 5） | errors: 0 |
| PR-02 | 2026-10-19 | 用户裁决落账（Versa=C、档位规则 OK、PDF 价差搁置、「往死里挖」）；**W02 第二批 +25 户**（UK/IE/DE/IT/CZ/HU/SE/NO/FR/PL/CA/US，web_search ≈60 次）+ 4 户既有档补具名 KP（Spectra/Neteon/Paragon/W3CAM）；Mikrotik 仓库 1032 行 grep 去重（命中 BSC=A-532、Jampel=C-031、100MEGA=A-499/C-173） | **40**（A 10 / B 22 / C 8） | errors: 0 |
| PR-02 · W03 | 2026-10-19 | 用户「继续挖」→ **W03 第三批 +13 户**（HU/IT/NO/ES/FI/UK/PL/CA/FR/CZ，web_search ≈35 次）+ 7 户既有档补证（Direktronik 退信通道更正、Spectra/Exertis/Coel/Connect Data/Compass 补 Mikrotik 对照、BTS/ACTION/100MEGA/Kyma 补品牌站与进口证据）；Mikrotik grep 新增同户 6 组（Young=A-233、Coel=A-191、Connect Data=A-254、Direktronik=A-054、Spectra=C-026/C-149、Compass=C-028、Exertis Azenn=C-185）；W02 pending 9 项全部处置 | **53**（A 13 / B 30 / C 10） | errors: 0 |
| PR-02 · W04 | 2026-10-19 | 用户「继续挖，着重北美（US/CA）+ 欧洲 + 土耳其」→ **W04 第四批 +13 户**（TR 3 / US 2 / CA 1 / CZ 1 / DE 1 / AT 1 / IT 1 / NL 1 / TRNC 1，web_search ≈30 次 + fetch_page ×2）：PTUSA 官方 Where-to-Buy 下游 Pulse Supply（总裁/销售 VP 直邮 → **A**）与 Platinum Micro；Mikrotik「B下放·无邮箱」4 行补邮箱重评（C-089 / C-085 / C-067 / C-015）；Mikrotik PLANET 关联 A 行并档 4 组（A-497 PROFIcomms 补到 PLANET 线 PM 直邮 → **A**、A-480 Fiber24、A-469 TRIOTRONIK、A-032 Aikom）；**土耳其首批 3 户**（Bimel / Rima / Ergen）；荷兰白牌 Alarmsysteemexpert（Movok VK-SWITCH → OEM 角度）；Akçaba 复核为北塞浦路斯 → C 区域边缘待裁定 | **66**（A 15 / B 40 / C 11） | errors: 0 |
| PR-02 · W05 | 2026-10-19 | 用户 T06 裁决落账（Akçaba PC-011 → B；5 户同户首触从 Planet 仓发；UL/TAA 第二封前核）→「继续挖吧」**W05 第五批 +5 户**（TR 1 / UK 2 / ES 1 / NL 1，web_search 15 次）：Mikrotik 主表改**全列** grep 后新命中 PLANET 关联行（Nokta A-462、Connectec C-107、Saratota C-116、CiudadWireless A-562、Shop4Power C-259）——两户「无邮箱」C 补邮箱重评 B、一户「自有品牌太难」C 按 OEM 机会重评 B、两户 A 并档；LinITX / Comms Express / Instant Byte / ALLNET 核无 PLANET 证据不并档；土耳其二轮饱和（仅比价站）；hypernet → 马尼拉区域外 | **71**（A 15 / B 46 / C 10） | errors: 0 |

- 主表：`data/客户名单_Planet渠道_2026-10.csv`（26 列，前 22 列与 Mikrotik 仓库一致）
- 档案：`profile/A|B|C/`，索引 `profile/00-索引.md`
- 原始证据：`batch/2026-10-19_W01_*.json`
- W01 A 类：**PA-001 4Power（IT，自有品牌 4Net）**、**PA-002 Cartronic Group（ES，具名 KP 直邮）**、**PA-003 RFOG POLAND（PL，业主直邮）**
- W02 A 类：**PA-004 NSI Distribution（CA，安防批发 9 分部 + 自有品牌 Norelco，Norm Matinnia 直邮）**、**PA-005 Jampel（IT，PLANET 官方分销 + Moxa，PM Stefano Cinti 直邮·待核）**、**PA-006 Kyma（IT，30 年进口 PLANET + 已进口中国 3onedata，3 人家族企业业主直达）**、**PA-007 ALARM ABSOLON（CZ，1989 年起安防批发，销售 Tikovský 直邮）**、**PA-008 Aspectis（HU，IP 安防 VAD，总经理 Laczkó 直邮）**、**PA-009 Direktronik（SE，自有品牌分销商；~~steffo@~~ 已退信 → W03 更正为 fredrik.brunzell@ 主通道，Mikrotik A-054）**、**PA-010 iOC Tech（CA，PLANET 授权分销 2–10 人，Director 具名）**
- W02 原始证据：`batch/2026-10-19_W02_*.json`（29 条：25 新户 + 4 补证；skipped 15 组、pending 9 项、queries 14 组）
- W03 A 类：**PA-011 Young B.T.S.（HU，PLANET 线产品经理 Pásztor András 直邮；Mikrotik A-233 缺邮箱——本仓补齐）**、**PA-012 SIR.tel.（IT，1991 年起 PLANET 授权分销、价目表季更，采购经理 Gioia Mantoan 具名 + sales@）**、**PA-013 Leteng（NO，AV/IT 分销，新任总经理 Øyvind Jacobsen 直邮 + 销售经理 Borgar 直邮；设中国采购岗；与 Direktronik 同属 Lagercrantz）**
- W03 更正：**PA-009 Direktronik 的 steffo@ 在 Mikrotik 侧 2026-09-29 已退信** → 标「发不过去」保留，主通道改 **fredrik.brunzell@direktronik.se**（Softing 名录公开，经 Mikrotik A-054）
- W03 原始证据：`batch/2026-10-19_W03_*.json`（20 条：13 新户 + 7 补证；skipped 17 组、pending 11 项、queries 13 组）
- W04 A 类：**PA-014 Pulse Supply（US，PTUSA 官方 USA Reseller 首位；官网 PDF 公开总裁 Salvatore Costantino / 销售 VP Bobby Baine / VP Michael Banschbach 直邮；Mikrotik C-089「无邮箱」→ 本仓补齐升 A；守界：不碰其核电/SMR 线）**、**PA-015 PROFIcomms（CZ，PLANET/ComNet/Microsens 线产品与销售经理 David Matula 直邮，官网品牌页公开；Mikrotik A-497 仅 info@ → 首触从哪个仓发由用户定）**
- W04 土耳其（T05 新增区域）：PB-031 Bimel（Ankara，80 人，PL- 自有货号全线）、PB-032 Rima Elektronik（İstanbul，监控集成商）、PB-033 Ergen Elektronik（Antalya，Dahua+PLANET）；**Akçaba 实为北塞浦路斯 Lefkoşa → PC-011 区域边缘，用户一句话可升 B**
- W04 原始证据：`batch/2026-10-19_W04_*.json`（13 条；skipped 12 组、pending 8 项、queries 6 组）
- T06 裁决：**Akçaba PC-011 升 B**（人工定级 B，编号不改）；**Pulse / PROFIcomms / Platinum / ABP / Globall 首触从 Planet 仓发**（规则 §4.3 T06 例外）
- W05（+5，全 B）：PB-041 Nokta Elektronik（TR，并档 A-462）、PB-042 Connectec（UK，PLANET 授权分销 + 安装商贸易柜台，补 sales@）、PB-043 Saratota（UK，PLANET 为首位代理线 + planet-direct.co.uk，补 sales@）、PB-044 CiudadWireless（ES，自有品牌 eRize 工业 DIN PoE → OEM 30%，并档 A-562）、PB-045 Shop4Power（NL，「Planet Ethernet Specialist」+ E-Link）
- W05 原始证据：`batch/2026-10-19_W05_*.json`（5 条；skipped 10 组、pending 7 项、queries 13 组）

## 作战方案（用户问「看看如何搞」· 2026-10-19 版）

1. **信号源现实**：PLANET 官网**没有公开的经销商定位器**（`where-to-buy` 404，Partner Zone 需登录，案例研究匿名）；北美总代 planetechusa.com 的转售名单只有 5 家巨头。→ 只能靠 `web_search` + `fetch_page` 逐页挖（沙箱 curl 不通），方法见 `docs/methodology/Planet客户挖掘方法论.md`（M1 型号反查、M2 品牌页反查、M3 分销商下游、M4 项目/博客、M7 白牌反查等 10 法）。
2. **目标与顺序**：第一梯队 DE/UK/IT/ES/FR/NL/PL/US/CA → 第二梯队 AT/CH/BE/北欧/CZ/PT/IE/GR/HU/SK；小国不主动挖；轨交/军工/公共采购守界。
3. **定级**：A = 真实 PoE/交换需求 + 具名直达人 + 体量可拿下；B = 有邮箱可群发；C = 无邮箱/过大/区域外/不对口。编号 `PA-/PB-/PC-` 冻结只追加。与 Mikrotik 仓库 26 行 PLANET 相关户去重（`data/Mikrotik仓库已有PLANET相关客户_对照.csv`）。
4. **每批 10–20 户**：批次 JSON（证据原文 + URL + 日期 + skipped 原因）→ `add_batch.py` → `render.py` → `audit.py`（errors 0）→ README/总账/对话全记录 → push。
5. **报价与型号**：Saga 卖价 = SmartByte CNY × (1.20/1.25/1.30) ÷ 汇率（6.69 @2026-10-17）；MD 写 Saga 型号，无对应时写 SmartByte 型号并注明。三档全表 `docs/reference/价格表_三档加价_USD.md`（135 型号；**9 个型号按今日汇率 +20% 已高于 Saga PDF 列表价**，建议刷新 PDF）。
6. ~~**下一批（W02）计划**~~ **W02 已完成（2026-10-19）**：PLANET Germany GmbH 核为独立微型公司（B）；lwl-shop24 / WoodComm / planet.pl / ISTC 均已处置（B / B / C 巨头 / 跳过-区域外）；NL/BE/AT/CH 品牌页检索**无专业经销命中**（只剩泛电商与聚合站，已 skip）；M1 型号反查以自然语言多语种查询有效（`site:` + 型号为 0 结果），主要命中电商而非集成商；Spectra/Neteon 补到具名 KP。
7. ~~**下一批（W03）计划**~~ **W03 已完成（2026-10-19）**：pending 9 项全处置（Young→A、Microsam→B、Digitx→B、CAPS/Abix/Ropere-Suntech→skip 电商、planet-ca.com→信号源）；北欧 FI 命中 Microdata（B）、NO 命中 Leteng（A）、DK 仍无专业经销；M7 白牌（rebranded/baugleich）两种措辞均为噪音；美国集成商 M3/M4 两种措辞均无命中。原计划：① 美国/加拿大安防与工业集成商（M3 分销商下游：Neteon / M/A Rugged / NSI / iOC 的「客户案例」页；M4 `"Planet" "IGS-" case study`）；② 法国/西班牙/葡萄牙二轮（Abix、accessoires-informatiques、Microsam-CA、Young B.T.S.-HU、CAPS-NL、Digitx-IT 等 pending 9 项逐个核）；③ 北欧 DK/FI 型号反查（丹麦语/芬兰语）；④ M7 白牌反查：以 PLANET 机型外观/固件特征搜欧美自有品牌（Lysora、Norelco、Direktronik、4Net 已是线索）；⑤ 为 W01/W02 的 B 类找具名 KP（FEN、Ballicom、ProVu、WoodComm）；⑥ 用 `fetch_page` 补齐 W02 标「检索摘要/待补证」的原文（Kyma、Absolon、Aspectis、BTS、NSI OEM 页）。

8. ~~**下一批（W04）计划**~~ **W04 已完成（2026-10-19，区域指令：US/CA + 欧洲 + 土耳其）**：③ 美国改走 PTUSA 官方 Where-to-Buy 下游（Pulse Supply→A、Platinum Micro→B）+ Mikrotik「无邮箱」C 行补邮箱（ABP、Globall）——投标/规格书与 rep-firm 措辞均为噪音；② 德国 Systemhaus 二轮无新命中，但连带命中 TRIOTRONIK（AT）；④ NL 安装商角度命中 Alarmsysteemexpert（白牌 Movok），BE Wilcon 无 PLANET 证据，DK 仍只有电商；⑤⑥⑦ 与 ① 首触前硬化顺延 W05。原计划：① **首触前硬化**：对 13 户 A 用 `fetch_page` 逐页核原文（W02/W03 标「检索摘要/待核」处：Young 联系页在职、SIR.tel 团队页、Leteng 总经理页、Jampel 旧站邮箱、Kyma/Absolon/Aspectis/BTS/NSI OEM 页），核毕才进入首触池；② **德国 Systemhaus 二轮**（M3：BTS NETWORK 自述客户群「Ingenieurbüros / Elektrogroßhandel / Systemhäuser」→ 搜其案例页；M10：Moxa/ORing 德国伙伴与 PLANET 重叠）；③ **美国**改走投标/规格书路径（`"Planet" "IGS-" bid tabulation` / IPVM、Reddit 口碑帖反查安装商）与 Neteon/M/A Rugged 案例页；④ **丹麦/荷兰/比利时** M3：Hikvision/UNV/Dahua 安装商名录 × PLANET；⑤ myTelecom（FR）、Tech Plaza（PT）、Coditek（ES）、cctv.net（US）、hypernet/satronel 区域核；⑥ 为 B 类补具名 KP（FEN、Ballicom、ProVu、WoodComm、Microdata、VERSIM）；⑦ 三仓并档：把本仓补到的邮箱（Young pasztor.andras@）回填 Mikrotik 侧需用户在 Mikrotik 仓库操作——本仓只记录。
9. ~~**下一批（W05）计划**~~ **W05 已完成（2026-10-19）**：③ Mikrotik PLANET 关联行核验 → Nokta / CiudadWireless 并档，Connectec / Saratota / Shop4Power 重评 B；LinITX / Comms Express / Instant Byte 无 PLANET 证据；④ ALLNET 无 PLANET 证据（OEM 线索留 Mikrotik 仓）；② 土耳其二轮饱和（Parnet 待取证、Kartal 为电商）；①⑤⑥⑦⑧ 顺延 W06。原计划：① **首触前硬化**（顺延）：15 户 A 用 `fetch_page` 逐页核原文，核毕进入首触池；② **土耳其二轮**：Parnet（多款 PLANET 在售，核是否专业经销）、Bimel 的 PLANET 产品经理具名、伊兹密尔/布尔萨安防分销 × PLANET；③ **Mikrotik PLANET 关联 A 行逐一核品牌页**（Instant Byte ES A-564、ELMAT IT A-353、LinITX UK A-059、Comms Express UK A-550）→ 有 PLANET 侧证据即并档；④ **ALLNET GmbH（DE）** 自有品牌交换机 OEM 目标评估（体量偏大，先看是否有 OEM/ODM 采购入口）；⑤ Alarmsysteemexpert 的 Movok/VK-SWITCH 白牌归属核实（若为第三方品牌商则建该品牌商档）；⑥ 美国三户（Pulse / Platinum / ABP）的 UL/TAA 门槛核（Saga 无 UL）——第二封邮件前必核；⑦ B 类补具名 KP（FEN、Ballicom、ProVu、WoodComm、Microdata、VERSIM、Bimel）；⑧ DK/CH/GR/PT/BE 改走 Hikvision/Dahua 伙伴名录 × PLANET 或暂停。
10. **下一批（W06）计划**：① **首触前硬化**：15 户 A 用 `fetch_page` 逐页核原文（Young / SIR.tel / Leteng / Jampel / Kyma / Absolon / Aspectis / BTS / NSI / Pulse PDF 在职 / PROFIcomms 联系页），核毕进入首触池——**挖掘已进入收益递减区（W04 +13 → W05 +5），建议 W06 以硬化 + 首触准备为主**；② 取证补缺：CiudadWireless PLANET 产品页、Parnet PLANET 产品页（→ B）、Alarmsysteemexpert Movok 归属、Shop4Power E-Link 归属；③ 美国三户 UL/TAA 核（第二封前）；④ B 类补具名 KP（FEN、Ballicom、ProVu、WoodComm、Microdata、VERSIM、Bimel、Connectec）；⑤ 剩余入口：Hikvision/Dahua 伙伴名录 × PLANET（DK/CH/GR/PT/BE），Mikrotik 全表再过一遍「ORing/EtherWAN/Lantech 授权」行（台厂工业交换机同类渠道，可能同时卖 PLANET）。

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
batch/                           每批原始证据 JSON（W01–W05）
profile/A|B|C/                   渲染档案（勿手改）
scripts/                         pricing.py / add_batch.py / render.py / audit.py / common.py
*.xlsx *.pdf *.docx              用户上传原件（价格表、Saga 背景）
```

## 环境

`python3 -m venv .venv_planet && .venv_planet/bin/pip install openpyxl pdfplumber`（仅 `pricing.py` 需要；其余脚本纯标准库）。沙箱外网仅 `fetch_page`/`web_search` 工具可达。
