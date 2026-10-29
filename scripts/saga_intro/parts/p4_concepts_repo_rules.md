
---

## 15. 概念词典与内部术语表

### 15.1 Saga 的 13 个核心概念（C1–C13，概念层）

| # | 概念 | 一句话定义 | 在数据里长什么样 |
|---|---|---|---|
| C1 | 两层三供应商（Saga = 接口层） | Saga 不是产品公司，是接口层：三家供应商在下、客户在上，Saga 提供统一命名 / 资料 / 条款 / 对接人 | PI「Manufacturer: Zhengzhou Saga Telecom」+「Marvell Chip」；STC/STI/STH 覆盖三家来源 |
| C2 | 三道筛子 | 口号「Marvell 管理型」→ Drive 自助资料 → Template 条款；过滤优先于转化 | 群发附件永远是 Product Link PDF；客户能引用型号/价表 = 过第 2 道；付样 / PI / 标签 = 第 3 道 |
| C3 | 顺手单 vs 拼命单 | 只做边际努力小、复购可能大的单；不为一次性大单改变运营方式 | Larch 8,000 台被主动停止；需要新认证 / 新物流 / 新付款 / 新固件的客户权重下调 |
| C4 | 技术流绑定 | 让型号、CLI/MIB、固件行为、规格书进入客户系统；放弃 API/SDK 伪绑定 | NYNEX LibreNMS OID；Go Green IT 博客 + bug 报告；Netaş 样机留在终端客户 |
| C5 | 中性与隐身 | 设备中性无中文；SmartByte 隐身在 Saga 后、Saga 隐身在客户品牌后 | Angora Verge、Fastball FBC-204GP、Mbata BNSC-、James SW-3200 |
| C6 | 价格被动 → 利润底线制 | 不定价不谈价，只守底线（20/25/30 与 20/25/35 两套）+ 30% 封顶 | 价格异议不让步；「target price」无技术问题 = 价格流 → 降级 |
| C7 | 国家 = 运行方式 | 能不能做看收款 / 物流 / 合规通路是否已有，不看需求大小 | TR TRY+WA；RU 货代；NG 客户货代；US/EU PayPal/T/T+DAP；JP PSE |
| C8 | 群发 = 引流到资料 | 让 1% 点开 Drive 自我筛选，不是促成回复 | 14,500 → 1,011 → 208 → 91 → ≈10 → 4 |
| C9 | 三个名字 = 一个流程 | Elsa 首触 → Alan 报价/PI → Simon 早期关系/收款 | STEC / STAG / STSC；「My friend Simon sent you some info… I will take over」 |
| C10 | 边界即资本 | Not-to-Do 清单是让一个人持续可运营的方法 | 命中清单 → 「停点：边界」，不绕路 |
| C11 | 供应商关系优先于客户机会 | 冲突时 Saga 让路；CENTEC 敲门砖但 Peter 产品优先 | Larch 让路；可能与 SmartByte 国内客户重叠 → 「待 Simon 判断冲突」 |
| C12 | 慢是武器 | 固定成本极低，可以等客户替换周期；每次触达增加熟悉度不增加成本 | 群发连续两年；Netaş 4 个月后再发特性表；每户节奏记录 |
| C13 | 信息资产化 | 资料一次做好、季度更新、所有客户共用；既是筛子也是绑定工具 | Resource Library（Roadmap.pdf、STOS V2.4、7.5.x 特性表）；加厚产出是结构化字段 |

因果链：约束（一人 / 无库存 / 不能打价 / 认证有限 / 不做国内 / 供应商优先）→ C10 → C3；→ C2（C8 把人引到筛子，C13 做筛子）→ 少客户 → C4 绑定；→ C6 → C12 → 十年现金流；→ C7；→ C5 → OEM 品牌商最优先；→ C1 → C11；→ C9。

### 15.2 内部术语表（仓库 / 对话里反复出现的黑话）

| 术语 | 含义 |
|---|---|
| **P 池 / 资产池 / 长期客户群** | 三库并池后的长期跟进群（A + B），U115–U117 起的主线「把客户挖干净 → 长期客户资产池」 |
| **精华跟 / 普通跟** | A = 精华跟（季度个人信 + 两月巡检 + 回信 48 h）；B = 普通跟（群发 + 点名） |
| **C 储备** | C ≠ 垃圾；不发、两月巡检、来信即回 B；只有永久 pass 才是 bye |
| **永久 pass** | Gate 0 刚性三条（无邮箱且无 WA / 弹回且无备用 / 明确婉拒），「一旦入选 永不考虑」 |
| **三闸（Gate 0/1/2）** | C 池筛选：闸 0 机筛永久 pass；闸 1 人工批量复核；闸 2 Planet/External 补证；报告在 `docs/requirements/C池闸*` |
| **坐实 / 部分坐实 / 登记底数** | 在官方登记源核到法人主体；付费墙只到部分坐实；「1 查未得即停」 |
| **桌面卡 / 研究档 / 加厚 / 快照后加厚** | 桌面卡 = 一页公司事实卡（External `research/<code>.json`）；研究档 = Saga `research/<code>.json`；加厚 = 补证据字段；快照后加厚 = 用官网快照 `site_snapshots/<code>.json` 再补 `site_contacts` / `snap_thicken` |
| **五项全齐** | 桌面卡 / 官网快照 / 快照后加厚 / 公司登记 / 具名 KP 都有 |
| **副档 / 主档（dup_of）** | 跨库同一公司：副档随主档，不单独计数（名册 2,045 唯一） |
| **对位 / 非对位 / dayjob_fit** | 对位 = 行业与品类与 Saga 交换机对得上；非对位但 Simon 本职可用的（光端机 / DWDM / 光模块）= dayjob_fit，不永久 pass |
| **守界** | 乌克兰 / 伊朗 / 叙利亚、军工、公共采购、生命安全、轨交——留 C 不发 |
| **巨头** | 大分销 / 大运营商 / 大厂（`build.py GIANT_DOMAINS` -45 分）→ C，但不是永久 pass（Supermicro 例外争议 Q-55） |
| **gg** | Simon 的标签「已凉」= 难复购；8 家成单 gg 永不 A |
| **q33_hold** | Q-33 reseller / 洪瑞经销体系客户：不碰、标记、只巡检 |
| **人工定级 / grade_override / overrides.json** | 三库各自的人工覆盖机制（Planet CSV `人工定级` 列 / Saga 研究档 `grade_override` / External `overrides.json`）；PI 活跃·可发展强制 A |
| **四主区** | 土耳其 / 美国 / 英国 / 德国（+ 波兰次重点） |
| **门面机型** | 品牌站 / 产品站 / 群发主推的 9+3 款（§5.2） |
| **两层答法** | 客户问「有没有 X」：先 Marvell AC5 线，再 CENTEC 线 |
| **口径表 #n** | `docs/对外口径一致性_2026-10-24.md` 第 n 行的统一口径 |
| **INH-xx / PR-xx-yy / Q-xx / T29-Uxx / 第 n 批** | 继承规则 / 用户要求总账编号 / 待裁定问题 / 对话轮次 / 变更日志批次 |
| **发送包 / 跟进总台 / 名册 / 缺口表** | 周发送包（W44）/ `docs/跟进总台.md` / `docs/长期客户群_名册_*.md` / `docs/长期客户群_深挖缺口_*.md` |
| **打回候选（快照）** | 两个不同夜晚官网抓取都失败才成为打回候选；单夜失败只记录；**永不自动打回** |
| **MS / MC / TS / TC** | 《计划》状态码：Manufacture Stock / Manufacture Customize / Trade Stock / Trade Customize |
| **STSC / STAG / STEC** | PI 单号前缀 = 经手账号 Simon / Alan / Elsa |
| **Must-Read / A Word / Order Procedure / TTC / CCF** | Drive Template 条款文件；TTC = Saga 对外服务条款名（OEM/ODM/SKD/CKD）；CCF = Commercial Contract Framework |

来源：`docs/Saga内在逻辑与概念_2026-10-24.md` §2/§3、`docs/长期客户群_方案与复核_2026-10-29.md`、`docs/requirements/待统一处理问题清单.md`、本会话记忆。

---

## 16. 仓库地图（elsasaga-cloud/Planet，分支 arena/3f35b9b3-planet）

### 16.1 目录

| 路径 | 内容 |
|---|---|
| `AGENT-CONSTITUTION.md` / `AGENT-README.md` / `README.md` | 宪法（开工先读 / 对话全记录 / 零臆造 / 不可手改 / README 自检 / GitHub 监控…）；操作记录；每轮进度表（第 167 轮） |
| `docs/requirements/` | **对话全记录.md**（每轮原文 + 时间戳，只增不删）、**用户要求总账.md**（PR-xx + INH-01…17）、**待统一处理问题清单.md**（Q-01…Q-77）、**变更日志.md**（995 行提交记录）、AB加厚审计、C池三闸报告 |
| `docs/reference/` | Saga 画像 / 品牌口径 / 商务条款 / 官网全文 / 价格表三档 (SmartByte·HRUI·CENTEC·Realtek 工业·2.5G-10G·2023 首版) / 群发价台账 / 群发剔除名单 / 证书登记表 / 实际进价与毛利 / PLANET 对照 / 继承规则摘要 |
| `docs/rules/` | 客户分级与去重规则、客户档案结构与内容规则、报价与型号规则 |
| `docs/methodology/` | Planet 客户挖掘方法论、死路与死链备案 |
| `docs/smartbyte/`、`docs/suppliers/{HRUI,Hohunet}`、`docs/drive/{MUST-KNOW,Certification,Resource-Library}` | 供应商与 Drive 入库资料 |
| `docs/gmail/` | 三邮箱盘点、A 邮箱总览与真实往来、S 邮箱核对、Elsa 来询未回 |
| `docs/` 根 | Saga 理念摘读 / 内在逻辑与概念 / 对外口径一致性 / 方法论全集 / 两家公司逻辑 HTML / 理解与方向 V0·V1 HTML / 成单客户三件 / 客户功能需求台账 / 各国发信窗口 / 假日避让 / AB 判定讨论稿 / 长期客户群方案·名册·缺口 / 公司底数作业规程 / P 池总名册 / 跟进总台 / **本文** |
| `Saga Clients/A|B|C/` · `External Clients/<repo>/A|B|C/` · `profile/A|B|C/` | 三库渲染档案（**只读，脚本生成**） |
| `data/saga_clients/` | `entities.json`、`客户主表.csv`、`research/`、`registry/`、`site_snapshots/`、`site_digest.json`、`sieve.json`、`编号映射`、`人工定级.csv` |
| `data/external_clients/` | `{cctv,edgecore,mikrotik}.json`、`overrides.json`、`research/` |
| `data/客户名单_Planet渠道_2026-10.csv` + `batch/*.json` | Planet 库真源 |
| `data/价格主表.csv` / `价格主表_HRUI.csv` / `hohunet_STH对照表.csv` / `hrui_STC对照表.csv` | 价格与型号真源 |
| `data/gmail_{s,a,e}/`、`data/pi_2026-10/`、`data/pi_orders/`、`data/drive_r3/`、`data/smartbyte_*`、`data/hrui_*`、`data/hohunet_*`、`data/sagatele_site/`、`data/wechat_smartbyte_ocr/` | 原始入库资料（邮件 / PI 包 / Drive / 官网抓取 / 微信 OCR） |
| `data/长期客户群_*.csv`、`data/customer_watch/`、`data/github_watch/` | 长期群复核记录、监控产物 |
| 仓库根目录 xls/pdf/docx | SmartByte / HRUI 原始价表、Saga 价表 PDF、特性表 7.5.x、CLI/Web 手册、《Saga公司背景信息.docx》 |

### 16.2 脚本与链路

| 链 | 命令 |
|---|---|
| Saga 库 | `cd scripts/saga_clients && python3 renumber.py --snapshot-md && python3 build.py && python3 render.py` → `renumber.py --restore-dates` → `audit_full.py`（hard 0 / soft 370 基线）+ `audit.py` |
| External 库 | `python3 scripts/external_clients/render.py` |
| Planet 库 | `cd scripts && python3 render.py`（129）；`python3 scripts/audit.py` → errors: 0 |
| 长期群 | `python3 scripts/lt_roster.py`（名册 2,045）、`python3 scripts/lt_gap_audit.py [--no-dns]`（缺口）、`python3 scripts/lt_snapshot_list.py`（补快照清单）、`python3 scripts/saga_clients/lt_snapshot_thicken.py [--dry]`（快照消费 → 加厚 + 打回候选）、`p_roster.py`、`web_watch/checklist.py` |
| 价格 | `scripts/pricing.py`（主表三档）、`scripts/pricing_hrui.py` |
| 入库 | `scripts/gmail_ingest/`、`scripts/drive_ingest/`、`scripts/pi_orders/parse_pi.py`、`scripts/smartbyte_crawl/`、`scripts/suppliers_crawl/`、`scripts/wechat_ocr.py` |
| 监控 | `scripts/web_watch/watch.py`（`--layer all|a|b|…` 大小写不敏感；`snapshot_missing()` / `snapshot_thicken()` / `git_commit()` 带 pull --rebase；`--selftest`）、`scripts/github_watch/watch.py` |
| 台账 | `python3 scripts/changelog.py`（变更日志批次号，~130 s）；README / 总账 / Q 清单手工追加（幂等检查） |
| 本文 | `python3 scripts/saga_intro/build.py` → `docs/Saga全景信息包_<日期>.md/.html` |

### 16.3 GitHub Actions（`.github/workflows/`，沙箱不能推工作流文件、`gh` 403）

| 工作流 | 触发 | 作用 |
|---|---|---|
| `customer-watch.yml` | cron 02:23Z 每夜 + 手动 `workflow_dispatch`（输入 `layer`） | 监控源巡检 + 缺失官网快照补抓 + 快照加厚，bot 自动 commit/push 到本分支（timeout 90 min） |
| `saga-clients-snapshot.yml` | 手动 / 定时 | Saga 客户官网快照 |
| `drive-smartbyte-ingest.yml` | 手动 | Drive 入库 |
| `smartbyte-crawl.yml` | 手动 | SmartByte 官网全量抓取 |

- Actions bot 随时可能推送到本分支 → 任何 push 前 `git fetch && git pull --rebase`；Actions 改过的研究档 / Planet CSV 不要覆盖，rebase 后重跑渲染链。
- 沙箱：2 CPU / 3 GB；外网只有 github / pypi / npm；`curl` 被封用 `fetch_page`；客户网站不可达（靠 Actions）；pip 安装会随重置消失；**沙箱频繁重置 → 尽早 commit**。

### 16.4 Git 配方

```
git -c user.name=elsasaga-cloud -c user.email=elsasaga-cloud@users.noreply.github.com commit -m "..."
git fetch -q origin arena/3f35b9b3-planet && git pull -q --rebase origin arena/3f35b9b3-planet
git push -q origin arena/3f35b9b3-planet && git ls-remote origin arena/3f35b9b3-planet
```

`main` 是 orphan，**永远不要 rebase/merge main**；破坏性 git 操作需 Simon 许可；commit 信息里转义 `$`；中文 / 空格路径用 python 处理。

来源：`AGENT-CONSTITUTION.md`、`AGENT-README.md`、`README.md`、`scripts/*/操作步骤.md`。

---

## 17. 规则总表（写任何东西前过一遍）

### 17.1 继承硬规则 INH-01…17

| # | 规则 |
|---|---|
| INH-01 | Saga = 小型贸易商（SOHO），预算小、不投广告；长期跟进为主 |
| INH-02 | 目标：Marvell 方案接入层交换机；地区欧洲 + 美国/加拿大 + 土耳其；A 类优先，数量不是目标 |
| INH-03 | 台厂不是客户（PLANET 本身及其办事处）；只挖其欧美分销商 / 集成商 / 方案商 |
| INH-04 | 中性包装 / 贴客户型号；不出现 Made in China |
| INH-05 | ABC 定级：A = 真实可追溯需求 + 可直达的人；B = 有邮箱可群发；C = 无邮箱 / 过大 / 区域外 / 不对口；`人工定级` 优先 |
| INH-06 | 编号冻结、只追加；不重排、不回填、不复用（Saga 库 2026-10-25 一次性重编为例外，映射表留存） |
| INH-07 | 集成商 / 顾问优先于分销商；巨头分销直接 C |
| INH-08 | 邮箱只记真实公开找到的；不猜不拼；优先具名 KP，通用邮箱兜底 |
| INH-09 | 每个事实带证据（原文 + URL + 日期），否则「待补证」；事实 / 推断 / 假设分层 |
| INH-10 | 同国 + 法律后缀去重；每个跳过的名字说明原因 |
| INH-11 | 小国不主动挖；乌克兰 / 军工 / 公共采购 / 生命安全标「守界」只做民用商用 |
| INH-12 | 价格格式 `$xx USD EXW（快照日期，15 天有效，报价前核价）` |
| INH-13 | 首触：单一 P1、只问一个问题、不写 "I researched your website"、不提产地；客户英文、笔记中文 |
| INH-14 | 跟进在仓库外进行；仓库只记用户报告的回复 / 退信；退信不删邮箱 |
| INH-15 | 不手改档案；批次 JSON + 脚本渲染；每轮更新 README 并 grep 自检 |
| INH-16 | 破坏性 git 需许可；时间戳未知如实写明，不编造 |
| INH-17 | Saga 不做云管理 / 轨交 / IP67 / 消费级；无 UL / E-mark / KC——命中即降级或 PASS |

### 17.2 Simon 的常设指令（节选，按时间）

- 每轮对话原文 + 时间戳进 `对话全记录.md`；提炼进总账；决策进 Q 清单按默认执行，不一轮一问（T07）。
- 档案与邮件用 Saga 型号；SmartByte 兜底注明；报价 20/25/30；Versa / Planet USA = C。
- 区域：US/CA + 全欧洲 + 土耳其；四主区 + 波兰；V0「TR/中东/东南亚/非洲主战场」是错的；Planet 挖掘暂停不是搁置。
- Drive 为主、SmartByte 官网为真源；Drive 内容全部入库后 Drive 已删除；Elsa 首触未定 → 不发；Actions 跑着也不闲着。
- 客户去重完成；渲染只从 JSON；A 长期跟 / B 慢慢跟 / C 储备（U115 修正「C 垃圾」）；T27 待核留着。
- S/A Gmail 连不上连接器——不要再建议。
- 「啥都入库 不要漏掉」；加厚不套公式、证据为本；**永不覆盖/删除 V0，V1 新文件**；不唠叨；每次复核带时间戳 + commit。
- NYNEX 安排（Saga 推 SmartByte、Peter 技术）；CENTEC 跟进 / 备货 / 固件是 Simon 的事；不说 Saga 是欧洲总代；监控 `freddy36`。
- 成单客户每个活跃平台都挖都监控；HTML 先、MD 定向加厚后。
- 物流两条线；三账号一人；gg = 难复购；绑定深度证据可升但注明 Simon 原级；减少群发是战略取舍；CENTEC 敲门砖；WeChat/LinkedIn 只 James；WhatsApp 客户不写代号；群发低价是旧汇率；加厚顺序 A → B 欧美土 → 其他。
- **永远不要让 Simon 去问 Peter/HRUI 要价格**；grep 证据再说「缺」；「省你的时间 + 有没有长期复利」。
- 回答大白话：搞定 / 没搞定 + 你要做啥 / 不用做啥；批量大、任务长（40–60 分钟一轮）。
- External Clients：按仓库分目录；CCTV agent 永不再跑；按 Saga 实际情况重评；旧仓私有不删；每轮文字报告。
- C 池：先设计再做、不着急；A 90 太少以后再议；闸 0 刚性；乌克兰 / 巨头 / 不对位 / 研究后定 C 不是永久 pass；External 4,351 同池、Planet 也要搞；两月一次监控覆盖面广。
- 《计划》/《背景信息》红线：对外无 152 手机 / s. 邮箱；国内单只私账；芯片线底线；网站永不中文；无电话只 WhatsApp 跳转；slogan 不变；去掉 OEM Factory；不自称贸易商；CENTEC = 核心线之一；LinkedIn 必须；30% 封顶；目标顺序 OEM 品牌商 > 有进口经验 > 分销 > 小集成；轨交主营 PASS；无 UL/E-mark/KC。

### 17.3 Agent 作业守则与踩过的坑

- 价格 / 型号：有效型号集合之外不写；2.5G 等待 SB-263 裁定；RMB 报价待 Simon；Realtek 线按 2026-09-30 新进价；非管理工业线旧成本不可靠。
- 邮箱：`emails_live` 镜像 `emails`；Simon 备注不是 pass 依据；公开页邮箱只进 facts / `site_contacts` / `kp[].email`，**绝不自动写入实体邮箱**；绝不发明邮箱。
- 分级：按 entities grade 选，不按前缀（SC- 可以是 B）；跨库计数以名册 `dup_of` 为准；grade 只经 `grade_override` / `overrides.json` / `人工定级` 改。
- 域名：External `domain_prev`；Planet `网站` 可能带子路径（`host_of`/`reg_domain`）；DNS `nxdomain/dead` 复查两次；域名修正后重生成补快照清单。
- 快照：本地测试用 `--snap-dir /tmp/...`；失败记录含域名；单夜失败不打回；消费端已去膨胀。
- 台账：幂等存在性检查；README 可能无尾换行；PR 行 5 格、Q 行 8 格；CSV `utf-8-sig`；对话全记录只追加、真实 `date -u`。
- 脚本：`ast.parse` 后跑两遍；f-string 内无反斜杠；heredoc 里 f-string 不能有字面 `{}`；`scripts/saga_clients/calendar.py` 会遮蔽标准库 → 用 `importlib` 按路径加载；MX 缓存格式 `[[pref, host], …]`。
- 渲染：`renumber.py --snapshot-md` 前、`--restore-dates` 后；`board.py` 会重排发送包不要重跑；清理 `__pycache__`；HTML 交付物只用内联 CSS（预览沙箱无网）。
- 调研：注册库「1 查未得即停」；A 季度复核；死路见 `docs/methodology/死路与死链备案.md`；不重爬 Mikrotik；不再搜已做过的 registry（从文件重推导）。

来源：`docs/requirements/用户要求总账.md`、`docs/requirements/对话全记录.md`、`AGENT-CONSTITUTION.md`、本会话记忆。

---

## 18. 未决事项（Q 清单与 backlog，默认执行中）

| 编号 | 事项 | 默认 |
|---|---|---|
| Q-77 | §6 默认分层 A / B1 / B2 / C 储备（§11.3） | 默认执行，Simon 一句话可改 |
| Q-75 / Q-73 / Q-62 / Q-63 / Q-64 | U125–U129 期间的分层与并池细则 | 按默认 |
| Q-59 | 12 款 +20% 档远低于列表价：跟 SmartByte 降还是守列表价 | 按档位规则 |
| Q-54 / Q-56 | STH1G 可堆叠线、CENTEC Multi-Gig 铜口 PoE++ 无价 | 不主动报价 |
| Q-52 | Realtek/HRUI 线是否对海外老客户开放（NYNEX FTTH 10G ONT/MC 1,000+/年、$30–40） | 只在客户点名 Realtek 时给 |
| Q-49 / Q-48 / Q-50 | 国内冲突边界 / 「深」绑定画像 / CENTEC DC 线地位 | 按概念层推断执行 |
| Q-47 / Q-42 / Q-41 | HRUI 隐含加价不足 20% / ZX ↔ HR ↔ STC 对照不全 / 三档是否下调 | 按新进价重算；默认档位 |
| Q-51 | 交给 Angora 的 Turkey Client List 64 家（53 在库）Saga 是否继续直发 | 待 Simon |
| Q-46 | 《销售额 & 利润.xlsx》密码保护 | 待 Simon |
| Q-35 / Q-45 | 自有 PEN / MAC 块 | 不申请不更换（T29-U15） |
| Backlog | civil_only 3；SC-2143；StarNet；RU/KZ/BY/UZ 收款；2.5G（SB-263）；SB-583 RMB；W44 发送包；SC-1177 WA；TR 微信；gmail-only 户；SC-3066/3067；RVi；SC-455 / SC-259 / SC-1714 问 Simon；XC-C0157；reg_pending Akçaba / Smartplus / Sapphire / IT Warehouse + US 20；SC-729（ООО «Мицар»）；КОМИКОН；XC-E063；SB-595；gg 8；G1 33；P 池监控扩面；SC-634 补路径；可逆打回名单复核；`build.py` 对位标志回填；ipc2u.de nxdomain；SB-582 国别；SB-110 FB gmail 不自动加；134 快照失败户二夜复核；**Actions 跑完后：Saga 链 + External/Planet 渲染 + 名册 + 缺口审计 + 看 `data/长期客户群_快照打回候选_<日>.csv`** |

来源：`docs/requirements/待统一处理问题清单.md`、本会话记忆。

---

## 19. 来源清单（本文每一句都能回到这些文件）

| 主题 | 文件 |
|---|---|
| 公司画像 / 边界 | `docs/reference/Saga公司画像与边界.md`、`Saga公司背景信息.docx`（根目录） |
| 品牌口径 / 语录 / 官网 | `docs/reference/Saga品牌口径与宣传语录.md`、`docs/reference/Saga官网_sagatele.com_全文_2026-10-22.md`、`data/sagatele_site/` |
| 商务条款 / 物流 / 口径 | `docs/reference/Saga商务条款速查.md`、`docs/对外口径一致性_2026-10-24.md`、`docs/drive/MUST-KNOW/*.md` |
| 理念与概念 | `docs/Saga理念摘读_2026-10-23.md`（A1–A38 / D1–D14 / E1–E26）、`docs/Saga内在逻辑与概念_2026-10-24.md`、`docs/理解与方向_V1_深度串联_2026-10-24.html`、`docs/两家公司逻辑与方向_SmartByte-Saga.html`、`docs/方法论_全集_2026-10-27.md` |
| 价格 / 型号 | `data/价格主表.csv`、`data/价格主表_HRUI.csv`、`docs/reference/价格表_*.md`、`docs/reference/CENTEC_产品表与报价锚_2026-10-24.md`、`docs/reference/实际进价与毛利_校验_2026-10-22.md`、`docs/reference/规格书有_价格表无_型号清单_2026-10-22.md`、`docs/rules/报价与型号规则.md` |
| 认证 | `docs/reference/证书登记表_2026-10-22.md/.csv`、`docs/drive/Certification/认证证书索引.md` |
| 供应商 | `docs/smartbyte/*`、`docs/smartbyte_wechat_summary.md`、`docs/suppliers/HRUI/*`、`docs/suppliers/Hohunet/*` |
| 成单客户 | `docs/成单客户_PI复盘_2026-10.md`、`docs/成单客户_活跃平台与监控_2026-10-23.md`、`docs/成单客户_毛利复盘_内部_2026-10-24.md`、`docs/成单客户_NYNEX_维护计划_2026-10-22.md`、`data/pi_orders/*.csv` |
| 客户需求 / 窗口 | `docs/客户功能需求台账_2026-10-24.md`、`docs/各国发信窗口与来询季节_2026-10-27.md`、`docs/各国假日避让_2026-11_2027-03.md` |
| 分级 / 长期群 | `docs/rules/客户分级与去重规则.md`、`docs/rules/客户档案结构与内容规则.md`、`docs/AB判定_新标准_讨论稿_2026-10-29.md`、`docs/长期客户群_方案与复核_2026-10-29.md`、`docs/长期客户群_名册_2026-10-29.md`、`docs/长期客户群_深挖缺口_2026-10-29.md`、`docs/公司底数_作业规程.md`、`docs/P池_总名册.md`、`docs/跟进总台.md` |
| 规则 / 台账 | `AGENT-CONSTITUTION.md`、`docs/requirements/用户要求总账.md`、`docs/requirements/待统一处理问题清单.md`、`docs/requirements/对话全记录.md`、`docs/requirements/变更日志.md`、`docs/reference/从Mikrotik仓库继承的规则摘要.md` |
| Gmail | `docs/gmail/*`、`data/gmail_{s,a,e}/` |
