# AGENT-CONSTITUTION（Planet 仓库宪法）

> 适用对象：在本仓库工作的任何 Agent（任何模型、任何会话）。
> 来源：继承 `SimonSaga-202306/mikrotik-info` 仓库宪法 + 用户 2026-10-19 在本仓库新增的宪法级要求（对话全记录）。
> 效力：与用户当轮明确指令冲突时，以用户指令为准，并把覆盖关系写进 `docs/requirements/用户要求总账.md`。

## 第一条 · 开工先读（每轮必做）

1. 按顺序读：`AGENT-CONSTITUTION.md` → `AGENT-README.md` → `docs/requirements/用户要求总账.md`（最近一轮 + 继承规则表）→ `docs/requirements/对话全记录.md`（最近 2–3 轮）→ `README.md` 进度表。
2. 读完后回复开头输出一行：`📋 上下文已加载（宪法/AGENT-README/总账 PR-xx/对话全记录 Txx）`。
3. 不确定的事先问，用 `❓ 需要确认` 开头；不要替用户决定评级规则、报价档位之外的商业策略变更。

## 第二条 · 对话全记录（用户宪法级要求，2026-10-19）

1. **每一轮**用户消息与 Agent 回复都要写入 `docs/requirements/对话全记录.md`（独立文件，只增不删）。
2. 用户消息**尽量原文**；Agent 回复记要点 + 产出文件清单。
3. 每条两个时间戳：**用户消息时间**（平台未给精确时刻则写"会话内，精确时刻未提供 + 推定依据"）与**归档时间**（`date -u`）。**严禁编造时间**。
4. 提炼后的要求进 `用户要求总账.md`，编号 `PR-<轮>-<序>`，带状态与覆盖关系；被覆盖的旧要求标 ⛔ 并指向新编号，不删除。

## 第三条 · 零臆造与证据

1. 每个客户事实带证据：**原文摘录 + URL + 抓取日期**；没有就写「待补证」。
2. 事实 / 推断 / 假设三层分标；厂商名录、公司自述、政府登记、卖方目录、第三方报道分级标注来源。
3. 邮箱只记**公开找到的**；不猜测、不按模式拼、不用第三方数据库拼接；可做 MX 检查，SMTP 不可验要写明。
4. 动态页面的价格/库存只作抓取快照，不等于采购价或销量。
5. 不虚构名单：任何客户名必须能回溯到检索结果或页面。

## 第四条 · 数据结构与不可手改

1. **主表唯一真源**：`data/客户名单_Planet渠道_2026-10.csv`。
2. 原始证据按批次写 `batch/*.json`；档案 `profile/A|B|C/*.md` 由 `scripts/render.py` 渲染，**禁止手改档案**。
3. 编号 `PA-/PB-/PC-` + 三位数字，**冻结、只追加**；升降级不改号（A↔B↔C 迁移时档案移动目录、编号保留，CSV 记迁移历史）。**Saga 历史客户（`SA-/SB-/SC-`）另有一条（T29-U58，2026-10-25）：等级字母 + 段内连号、不跳号；日常 `build.py` 仍按稳定键取号不换号、新户只追加；升降级不自动换号（Q-62）；攒多了由 `scripts/saga_clients/renumber.py` 一次性重排并留映射表。对话全记录 / 变更日志 / V0 里的旧号用 `data/saga_clients/编号映射_2026-10-25.csv` 换算。**
4. 新批次 JSON 追加到加载清单**末尾**；同编号记录合并不覆盖。

## 第五条 · README 与自检

1. 每轮结束前更新 `README.md` 进度表与 `AGENT-README.md` 操作记录，并输出 `✅ README/AGENT-README 已更新`。
2. 所有写入用 `grep -c` 或等效方式验证落盘（Mikrotik 仓库 `str.replace` 静默失败教训）。
3. 每轮跑 `scripts/audit.py`（编号唯一、CSV↔profile 对账、无空评级、URL 格式），目标 `errors: 0`。

## 第六条 · 禁止事项

1. 不联系客户、不发邮件、不拨电话、不寄样、不报价给客户——仓库只产出研究与话术，触达由用户在仓库外执行。
2. 不改 ABC 定级规则、不改编号、不删客户行（删除/合并需用户许可并留痕）。
3. 不对 Mikrotik 仓库重新爬取数据；只读其规则与方法。
4. 不做破坏性 git 操作（force push、reset --hard、删分支）除非用户明示。
5. 不把密钥、密码、个人隐私写入仓库。

## 第七条 · Saga 身份与业务边界（写话术/定级时必须遵守）

1. Saga Telecom（sagatele.com）= 中国大陆贸易公司（SOHO）；核心货源 SmartByte（Marvell 方案接入层）、补充 HRUI（Realtek）、核心层 Hohunet（CENTEC）。
2. **台厂不是客户**：PLANET 及其自营/关联的各地 PLANET 公司不是客户；只挖欧美独立分销商、集成商、方案商、品牌商。
3. 不做云管理、轨交/EN50155、IP67、消费级/家用；认证只有 CE/RoHS/FCC/REACH/UKCA，**无 UL**、无 E-mark/KC——命中即降级或 PASS，并写明原因。
4. 中性包装、贴客户型号；邮件与档案不出现 "Made in China"。
5. 目标优先级（用户背景文档）：① 有 OEM/ODM 需求的品牌商/方案商 → ② 有中国进口经验或在用台系品牌（PLANET/ORing/Edgecore…）的渠道 → ③ 分销商/电商 → ④ 小型集成商/项目商（大集团难拿下）。

## 第八条 · 报价与型号（用户 2026-10-19）

1. 报价 = SmartByte 人民币未税价 × (1.20 / 1.25 / 1.30) ÷ 近期 USD/CNY 汇率，EXW；格式 `$xx USD EXW（快照日期，15 天有效，报价前核价）`。
2. 档位默认：分销/走量/比价型 20%；集成商/项目型 25%；OEM/ODM 深度定制或小批量技术型 30%。每份档案写明所选档位与理由。
3. 档案与邮件里写 **Saga 型号**（STC-/STI-）；Saga 无对应规格时写 SmartByte 型号（LT-）并**显式注明**「Saga 暂无对应型号，沿用 SmartByte 型号」。
4. 汇率与价格快照日期写进每条报价；汇率来源记录在 `docs/rules/报价与型号规则.md`。

## 第九条 · GitHub 监控：freddy36 / NYNEX（用户宪法级要求，2026-10-22 T29-U16）

1. 监控对象：GitHub 用户 **freddy36 = Frederik Kriewitz**（成单客户 SA-008 NYNEX / fiberONE 的技术决策人；LibreNMS PR #18681 / Oxidized PR #3734 把 Saga 卖给他的 STC-4168XGGCM 与 SmartByte 写进了上游）。他的所有公开活动——仓库、分支、提交、PR、issue、评论、star、following、gist——以及上游仓库（librenms/librenms、ytti/oxidized、netdata/netdata、TencentBlueKing/bk-lite）里任何人对 SmartByte 相关文件的改动、全站对 SmartByte / Saga 型号与名字的新命中，都是**极为敏感**的信号。
2. **每轮开工必跑** `python3 scripts/github_watch/watch.py`（约 1 分钟），变化自动追加到 `data/github_watch/变化日志.md`（append-only，无变化也记一行证明查过），快照存 `data/github_watch/snapshots/`，上游文件副本存 `data/github_watch/upstream_files/`。跑完必须 commit + push，提交信息带「github_watch」。
3. 有变化时：当轮回复里**第一条**就向用户汇报（不等用户问），并把解读写进 `data/saga_clients/research/SA-008.json`（evidence/signals，带日期与 URL），`docs/成单客户_NYNEX_维护计划_2026-10-22.md` 追加一行。
4. 监控范围只增不减；新增对象写进 `scripts/github_watch/targets.json` 并在本条款下补一行（带日期）。不得在 GitHub 上与他互动（不 star、不 follow、不评论、不 fork 他的仓库）——只读。
5. Agent 无法向 `.github/workflows/` 推送；定时无人值守监控的模板放在 `scripts/github_watch/workflow_template.yml`，由用户自行决定是否安装。
6. **扩展到全部成单客户（2026-10-23 T29-U18）**：Simon「一共 20 个客户，还有 19 个……github 啊领英啊乱七八糟的，只要是持续更新的平台都尽量挖出来，监控上，只要是 active 的东西都弄都挖都爬」。(a) GitHub 侧：`scripts/github_watch/targets.json` 新增 `customer_accounts`（anwHub = SA-077 Angora、Resonant-Networks + 提交者 acestraxionweb = SB-001 Resonant），与 freddy36 同一脚本、同一频率（每轮开工必跑），变化写 `data/github_watch/变化日志.md`。(b) 网页侧：`scripts/web_watch/targets.json`（20 家 × 63 个源：RSS / 整页 / JSON API / sitemap / GitHub / YouTube）由 `scripts/web_watch/watch.py` 抓取比对——**只能在 GitHub Actions 运行器上跑**（沙箱无外网），触发方式见 `docs/成单客户_活跃平台与监控_2026-10-23.md` §2；产物 `data/customer_watch/{当前状态.md,变化日志.md,snapshots/}` 由运行器自动提交。(c) 每轮开工除跑 github_watch 外，还要读 `data/customer_watch/变化日志.md` 最新一节；有「新增 / 变化 / 失败→恢复」先在回复里报，再把解读写进对应 `data/saga_clients/research/<code>.json`（signals/evidence 带日期与 URL）并重渲染档案。(d) LinkedIn / Facebook / X / Instagram 无法抓取（登录墙），只以链接形式列在清单 `manual` 字段，靠 web 搜索摘要人工跟。(e) 范围只增不减；全部只读——不在任何平台与客户互动（不 star / follow / 评论 / 点赞）。

7. **扩展到 A/B 级全体客户（2026-10-23 T29-U19）**：Simon「成单客户的动态……都要监控起来；A 类客户也要监控，如果可能 B 类客户也要监控……都系统性地爬、监控起来，结果都要入库」。(a) 清单分两层：精选层 `scripts/web_watch/targets.json`（成单 20 家，人工挑源）+ 面层 `scripts/web_watch/targets_auto.json`（由 `discover.py` 从 `entities.json` + 官网快照离线生成，A/B 全体；客户或域名变动后重跑 discover.py 再提交）。(b) 同一 `watch.py` 跑两层（`--layer all`），变化分别进 `data/customer_watch/变化日志.md`（成单）与 `变化日志_AB.md`（A/B），状态 `当前状态.md` / `当前状态_AB.md`，正文快照 `snapshots/<客户码>/`。(c) **每轮开工必读** 两份变化日志的最新一节（与 github_watch 同级）：成单层变化当轮首条汇报；A/B 层只汇报「像需求/人事/产品线变动」的变化，其余留在日志里不打扰用户；有价值的变化回写 `data/saga_clients/research/<code>.json`（evidence 带 URL+日期）并重渲染。(d) 登录墙平台（LinkedIn / Facebook / Instagram / X / WhatsApp）不自动抓，链接列在清单 manual 字段与档案「动态监控」节供人工看。(e) 运行只在 GitHub Actions 运行器上（每日模板 `workflow_template.yml` 由用户安装；装好前靠 crawl.py 触发 + `RUN_ON_CRAWL`），只读不互动；频率不超过每日一轮，单站请求间隔 ≥0.6 s。