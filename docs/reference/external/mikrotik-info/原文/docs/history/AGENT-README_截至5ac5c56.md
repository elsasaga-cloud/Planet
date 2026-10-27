# AGENT-README.md

> **用途**：本文件是 AI Agent 的"对话状态快照"，用于在会话中断、刷新或切换新对话时，让新 Agent 无缝衔接上下文。
> **维护规则**：每次对话结束或阶段性完成后，必须更新本文件。新对话开始时，Agent 必须首先读取本文件。
> **配套文件**：`AGENT-CONSTITUTION.md`（v2.0，含第八条深度审计协议）

---

## 📌 项目概览

| 字段 | 内容 |
|------|------|
| 项目名称 | SmartByte 交换机出海客户开发（MikroTik 生态反向信号挖掘） |
| 仓库路径 | `/home/user/mikrotik-info`（GitHub: SimonSaga-202306/mikrotik-info） |
| 当前主分支 | `main` |
| 工作分支 | `arena/01a0c3ef-mikrotik-info` —— **本会话固定分支，禁止切换到其他分支** |
| 最后更新时间 | 2026-09-22 |
| 最后更新由 | 对话轮次：导入 Agent 宪法 v2.0 + 深度审计 + 补全上下文记录 |

---

## 🎯 项目目标

用户是**中国大陆的小型交换机贸易商（Saga / Saga Telecom）**，转售 SmartByte（深圳三旺/台系方案）的商用 L2+ 与工业交换机，目标市场是**欧洲 + 美国/加拿大**。

本项目通过**逆向挖掘 MikroTik 生态**（官方分销商名录 + 官方认证顾问名录 + HMS/ORing/Antaira/Westermo/ComNet 渠道名录），找出"已经在卖 MikroTik、但缺工业/PoE++/ERPS 产品线"的海外分销商与集成商，形成可直接触达的客户名单，并逐户制定开发策略。

**核心逻辑**：MikroTik 长于路由、短于交换（尤其工业交换机与 PoE++），其渠道商普遍存在产品线缺口 —— 这个缺口就是 SmartByte 的入口。

---

## 🗺️ 当前任务状态

### 🔒 排序铁律（2026-09-27 用户第 38 轮确立，最高优先级，违反会直接破坏用户跟进）

> **任何时候 A 增加的（无论新挖到的、还是从 B/C 提上来的），一律追加到 A 级末尾，
> 不得插入中间、不得重排。**
>
> 原因：用户按编号从前到后跟单，顺序一变他的跟进就乱。
>
> - ✅ 允许：B→A / C→A 升级，新账号一律分配 `A-379`、`A-380`… 顺延
> - ❌ 禁止：以「质量更高」「有邮箱」「国家更好」为由把新 A 插到前面
> - ❌ 禁止：对现有 A 段做任何重新排序
> - ⚠️ **唯一例外：用户主动提出「重新排序/重构顺序」时才可以动**。
>   用户不提，就永远只追加。
>
> 历史：A-050 之后的重排是用户 2026-09-27 明确指示的（一次性、已执行完毕），
> 不构成后续重排的先例。

### 正在进行的任务

```
任务①：挖 A 级无邮箱客户的联系方式（A-080 起顺号挖，用户指示「搞完为止」）
        进度：已顺号处理 A-080..A-199，共 120 条（包括此前批次）。
        最新落库：A-110..A-199 共 90 条：88 条有公开邮箱（87 个去重主邮箱），
                  其中 84 条有官网/公司自营页面/厂商或协会伙伴名录来源，
                  4 条仅第三方目录待核；A-111/A-119 仅表单、电话和社交线索。
        后续：从 A-200 继续，直到全部 A 的待查账号逐条处理完。
        注意：本轮未处理 A-200..A-378；任务①未全部完成，不能提前宣称完成或启动任务②。

任务②：重新筛选 B / C 级，看哪些能升到 A
        前置：任务①完成后开始
        约束：升上来的账号一律追加到 A 级末尾（见上方「排序铁律」）

状态：进行中
```

### 📌 用户第 38 轮裁决（2026-09-27，已生效）

- **跟进记录是线下维护的，不入库。** 用户有回复了才会提、才会要求入库。
  → Agent 不要主动维护/追问「跟进记录」字段，也不要为它设计流程。
- **Bechtle Direct（A-103）不降级、不剔除。** 虽在规模排除名单内，用户裁决保留原级。
  → 此裁决只针对 Bechtle A-103，不能外推成所有存量大公司永久豁免；其他规则不擅改。
- **A-080 Carlos Cárdenas 证书到期风险已告知，用户回复「OK」。**
  → 仅表示用户知悉，不能据此认定证书仍有效。本轮不改评级，保留已有风险提示。

### 已完成的任务（最近 8 条）

- [x] MikroTik 官方**顾问名录**全欧洲 + 美加扫描完毕（200 位顾问 / 36 国，0 遗漏） — 2026-09-22
- [x] 修复评级缺陷 #6：10 行多国标签误判范围外，6 行 C→B — 2026-09-22
- [x] 建 `Marvell生态获客方法论`（30 条分四梯队全保留）+ EOL 替换矩阵 — 2026-09-22
- [x] 客户名单全量审计（合并重复、修正标签、标注跨国集团） — 2026-09-22
- [x] A/B/C 三级评级（A=88 / B=491 / C=149，合计 728） — 2026-09-22
- [x] 导出 `客户分级跟进表_2026-09.xlsx`（4 表，含待填反馈列） — 2026-09-22
- [x] 生成 `profile/` 逐户档案 705 份 + 索引 — 2026-09-22
- [x] 为 85 份 A 级档案补写**可直接发送的首触邮件** — 2026-09-22
- [x] 修复场景判断的三处"自我回读"Bug（详见已知问题） — 2026-09-22
- [x] 导入 Agent 宪法 v2.0 并完成首轮深度审计 — 2026-09-22
- [x] 恢复本地 git（第三次环境重置）+ 全仓深度入库审计（10 种方法） — 2026-09-22
- [x] 修复 profile/00-索引.md 的 12 处损坏链接 — 2026-09-22
- [x] 补写 `三家首发邮件...md` 的 Part H — 2026-09-22

### 待办任务（按优先级，2026-09-27 更新）

- [ ] 🔴 高优：**A-200 起继续顺号挖联系方式，直到 A 全部处理完。**
- [ ] 🔴 后续：**任务①完成后复筛 B/C 能否升 A，升级只在 A 末尾追加。**
- [ ] 用户有回复并要求入库时再录入线下跟进；**此项不阻塞当前挖掘**。
- [x] 本地 git 重置恢复已完成；下面分支全景/旧统计属历史快照，不作为当前状态。
- [x] 补写 `三家首发邮件与反向信号客户名单_2026-09.md` 的 **Part H**（顾问名录/审计/评级/档案系统） — 2026-09-22
- [ ] 🟡 中优：为 B 级 468 家按场景分组，给每组通用打法（用户已暂缓）
- [ ] 🟡 中优：为 C 级 152 家写"怎么啃大公司"打法（用户已暂缓）
- [ ] 🟢 低优：重切 ★★★ 优先级（当前 63% 是三星，等于没有三星）
- [ ] 🟢 低优：补全 364 行缺失城市、63 行缺失网站

---

## 🌿 分支全景图

```
main
└── arena/01a0c3ef-mikrotik-info   ← 当前唯一工作分支
     远程最新：7255573（70 commits）
     本地最新：dcc1ec1（1 commit）  ⚠️ 环境重置导致回退，工作区文件完好
```

**⚠️ 当前 git 状态异常（第三次环境重置）**

| 项 | 实测值 |
|---|---|
| 本地 HEAD | `dcc1ec1`（基线，1 commit） |
| 远程 `origin/arena/01a0c3ef-mikrotik-info` | `7255573`，**70 commits** |
| `git status` | 全部文件显示为未跟踪 `??` |
| 工作区实际内容 | **完好**：CSV 705 行、profile/ 706 文件、根目录 32 项 |
| `git stash list` | 空 |

**结论：无数据丢失，全部历史在远程分支上。**
**恢复方法（需用户确认后方可执行）**：
```bash
pip install openpyxl --break-system-packages   # 重置会清掉已装包
git reset --soft origin/arena/01a0c3ef-mikrotik-info   # 保留工作区与索引
```

**关键 Commit 记录（最近 12 条）**

| Commit | 说明 |
|--------|------|
| `7255573` | Add a ready-to-send first contact mail to each A dossier |
| `775045d` | Add a per-customer dossier under profile/, one file each |
| `27fe4c5` | Export the graded list as a working workbook |
| `cbdf4d4` | Grade the list A/B/C and write per-account strategy for A tier |
| `fc14295` | Add the audit report for the reverse-signal list |
| `85e743c` | Audit fixes: merge duplicates, normalise labels, cross-reference groups |
| `c74a92d` | Final countries: North Macedonia, Kosovo, Montenegro, Malta, Moldova |
| `be293dc` | US consultants: 19 people across 15 companies |
| `f41e24a` | Canadian consultants: 15, including a CCIE and a national ISP veteran |
| `dd51b0a` | Italian consultants: 21 people across 19 companies |
| `775d1c3` | France and Spain consultants, plus a reusable batch import script |
| `24283e3` | Sweep USA (27) and Canada (7): 396 accounts total |

---

## 🏗️ 架构 & 关键文件

```
/home/user/mikrotik-info/
├── AGENT-CONSTITUTION.md          # Agent 宪法 v2.0（含第八条深度审计协议）
├── AGENT-README.md                # 本文件，上下文快照
│
├── 客户名单_反向信号_2026-09.csv    # ★ 主数据源，705 行 × 19 列
├── MikroTik_vs_SmartByte_替代对照表.xlsx  # 主工作簿，16 表（反向信号名单 705 行）
├── 客户分级跟进表_2026-09.xlsx      # ★ A/B/C 分级工作表，4 表
├── 名单审核报告_2026-09.md          # 全量审计结论
├── Marvell生态获客方法论_2026-09.md  # ★ 30 条方法筛选 → 留 10 条，含操作步骤与搜索串
├── MikroTik停产机型替换矩阵_2026-09.md # ★ EOL 双源验证 + 停产型号 → SmartByte 替换表
├── A级客户跟进策略_2026-09.md        # 85 家 A 级逐户策略
│
├── profile/                        # ★ 705 份逐户档案 + 00-索引.md
│     └── A-001-xxx-国家.md … C-152-xxx-国家.md
│
├── scripts/                        # 数据管道
│     ├── add_batch.py              #   JSON 批次导入 CSV + 重建 xlsx
│     ├── audit_groups.py           #   查疑似同集团/同名
│     ├── fix_audit.py              #   审计修复（合并重复、标签归一、关联标注）
│     ├── grade.py                  # ★ A/B/C 评级
│     ├── strategy.py               # ★ 场景检测单一实现 + 打法库（PLAY/SPECS）
│     ├── export_abc.py             #   导出分级工作簿
│     ├── make_profiles.py          #   生成 profile/ 档案
│     └── emails.py                 # ★ 首触邮件生成（英文）
│
├── batch/*.json                    # 19 个国家批次的原始数据
│
└── （根目录其他交付物，均为前期 markdown 分析文档与价目表）
     重点客户深度分析与中性货打法_2026-09.md
     MikroTik客户切入深度分析_2026-09.md
     报价反击表_2026-09.md
     A类客户12家作战卡和开发信_2026-09.md
     三家首发邮件与反向信号客户名单_2026-09.md   ← Part A–H 全齐（H 为 2026-09-22 补写）
     Marvell阵营品牌全景和验证手册_2026-09.md
     MikroTik出口地分析和区域切入优先级_2026-09.md
     Saga客户开发长期作战系统_2026-09.md
     OEM合规包和标准合同模板_2026-09.md
     MikroTik认证及价格抓取.py
     SmartByte 各系列价目表 xlsx（managed / industrial / unmanaged / bypass）
     Saga Feature List_7.5.x_L2+.xlsx、_L3.xlsx
     Marvell Based CLI Manual.docx、Web Manual.docx
```

**重要约定**

- 编码：CSV 为 **UTF-8-BOM**（Excel 直接打开不乱码）；所有 Python 读写均需 `encoding="utf-8-sig"`
- 环境：**每次环境重置后必须重装** `pip install openpyxl --break-system-packages`
- CSV 列序（19 列，新增列只能追加，不得插入）：
  `公司名/国家/城市/网站/类型/信号/是否自有品牌/切入角度/首推型号/联系方式/优先级/状态/来源/首次触达日/最后互动日/下次跟进日/备注/评级/评级依据`
- 去重键：归一化公司名 **或** 网站主域名 —— **同域名会静默丢弃第二人，必须逐条核对 skipped 列表**
- 场景优先级 `ORDER`（`scripts/strategy.py`）：
  `MULTICAST > POE > HOTEL > INDUSTRIAL > CAMPUS > FIBRE > SWITCH > ISP > MTCSWE > INFLUENCE`

---

## 🧠 关键决策 & 背景知识

### 用户身份与硬约束（由用户明确提出，违反即为错误）

- **决策**：用户是**小型贸易商**，预算必须极小 → 不追求大客户、不投广告，靠低成本精准触达
- **决策**：**台系厂商不是客户，只是信号源** → 台湾公司**绝不开发**，只用其渠道脉络做情报
- **★★ 铁律（用户 2026-09-22 二次强调）：台厂不当客户，但一定要【狠挖】它们的客户** ★★
  > 台厂（PLANET / ORing / Moxa / EtherWAN / CTC Union / Korenix / Atop / Advantech）自己在卖交换机，
  > **不会买你的货，发邮件只会暴露价盘、还可能被反向抄价**。
  > 但它们**已经替你把客户筛选好了**：能在欧洲卖台湾工业交换机的人 = 懂工业交换机 + 有终端客户
  > + **已经受够台湾货的三根刺（交期长、MOQ 高、改款慢）** —— 这恰恰就是你的切入点。
  > **正确姿势：台厂官网 → Dealer Locator → 逐国扒 → 那些经销商才是客户。**
  > 已挖：ORing（64 家）、Antaira（9）、Westermo（14）、ComNet（7）、HMS 渠道（111）。
  > **PLANET 是最大的一块没挖的矿，预计单它就能出 50–80 家欧洲分销商。**
- **决策**：**出货完全中性** → 包装/外观/说明书不出现 "Made in China"，贴客户自己的型号
- **决策**：**知名自有品牌分销商难攻** → 放弃"正面突破大分销"路线，改走补位与技术切入
- **决策**：**目标区域只有欧洲 + 美加**（用户原话："其他的不要了"）→ 其他区域一律标"范围外"
- **决策**：**先把客户名单挖完，再进下一步**（用户重复两次："搞完客户list再进行下一步" / "不要搞其他 就是一直挖"）
- **否决**：早期交付物中的"OEM 合规包 + 标准合同模板"已被用户否决，改为"重点账号深度分析"

### 评级口径（用户定义）

- **A = 重点 且 好跟进**：有明确需求信号 + 有具体对接人 + 决策链短
- **B = 慢慢跟**：信号待验证，或只做路由/Hotspot（交换需求弱）
- **C = 难啃**：大公司 / 大集团 / 自有品牌 / 竞品 / 区域外


### 国家/地区覆盖（实测 74 种标签，合计 705 行）

| 国家 | 行数 | 国家 | 行数 |
|---|---|---|---|
| 美国 | 105 | 英国 | 44 |
| 意大利 | 38 | 西班牙 | 36 |
| 波兰 | 33 | 德国 | 30 |
| 希腊 | 30 | 法国 | 29 |
| 乌克兰 | 28 | 加拿大 | 26 |
| 捷克 | 25 | 荷兰 | 24 |
| 匈牙利 | 16 | 罗马尼亚 | 14 |
| 瑞典 | 13 |  |  |

> 注：README 早期草稿曾写"76 种国家标签"，实测为 **74 种**（审计合并与标签归一后）。

### 已踩过的坑（按严重度）

**🔴 坑 1：环境重置会同时清掉 git 历史与已装包（已发生 3 次）**
- 现象：`ModuleNotFoundError: openpyxl` + `git status` 全量 `??` + `git rev-list --count HEAD` 掉回 1
- 误判风险：**不能靠 CSV 行数判断历史是否完好**，必须用 `git rev-list --count HEAD`
- 解决：`pip install openpyxl --break-system-packages` + `git reset --soft origin/arena/01a0c3ef-mikrotik-info`
- 注意：`reset` 属破坏性操作，按宪法第二条须先取得用户确认

**🔴 坑 2：去重会静默吞掉真实的人**
- 已发生：FMS Web（3 人同域名）、Krystof Klima / WIFIPROFI、Benito Stijger / DAEL、Stefan Andersen / Pumait、Hani Rahrouh / Wireless Netware、Joel Blakey + Luke Cuddehay / LinITX
- 其中 **IP ArchiTechs 的英国 Samson Kamwendo 与美国 Thomas Murdock 是同一家公司**（跨 3 国 3 位顾问）
- 规则：**每批导入后必须打印 skipped 列表并逐条人工核对**，不假设 skip 就是真重复

**🔴 坑 3：我们自己的批注被当成客户信号回读（同一 Bug 的三种外衣）**
- (a) `切入角度` 列是我们写的模板话术（"卖 MikroTik 但缺工业/ERPS/PoE++"），曾导致 **246 家分销商全部误判为 A 级**
- (b) 备注里 `【待补】…建议先查证是否已有工业交换机 / PoE++ 产品线` 这句**本身含"工业""PoE"**，把空壳行推上 A 级
- (c) 备注里 `→` 之后是**我们的推论**（如 Carlos Otin 的"→ PoE 接入交换机批量需求"），被当成客户说过的话
- 解决：`scripts/strategy.py` 的 `clean()` 剥掉 `【…】`、`→…`、`★`；评级时整体排除 `切入角度` 列；`【待补】` 行一律降 B

**🔴 坑 4：三份 `scenarios()` 实现各自漂移**
- `make_profiles.py` / `export_abc.py` / `strategy.py` 各写一份，只有 strategy 那份做了清洗
- 后果：**同一客户用不同脚本跑会得出不同场景结论**，且验证脚本与生成器结果不一致（Carlos Otin 反复在 PoE 与酒店之间跳变）
- 解决：删除全部副本，`strategy.scenarios()` 为唯一实现，其余脚本 import

**🟡 坑 5：中文「监控」有歧义**
- 既指**视频监控**（CCTV，真 PoE 需求）也指**网络监控**（NMS，无 PoE 需求）
- 曾把一批 NMS 集成商（K2O Services、Martin Pina、Vadym Klymenko）误判为摄像头客户
- 解决：POE 规则只认 `视频监控 / CCTV / 摄像头 / 门禁 / 报警 / 对讲`

**🟡 坑 6：Dante 被误归为 PoE**
- Dante（Audinate）是专业音频 over IP，核心诉求是**组播与 QoS**，不是供电
- 曾把 Michael Jezierski（IndyCar 赛车转播）判成 PoE 场景
- 解决：Dante 移入 MULTICAST；并将 ORDER 改为 **MULTICAST 优先于 POE**（组播是决定成败项，PoE 是常见项）

**🟡 坑 7：MikroTik 顾问名录分页不可信**
- `totalChunks` 不是卡片数；法国结果在 chunk 0，拉脱维亚在 chunk 1，捷克 chunk 1 已含页脚
- 规则：以 `### Become a Consultant` 页脚作为列表结束标志；**小国必须同时看 chunk 0 与 chunk 1**

**🟡 坑 8：代码级小错**
- `ws[1].cell(...)` → `AttributeError`，须写 `ws.cell(row=1, column=i)`
- 国家字段含斜杠（"克罗地亚/斯洛文尼亚"）→ 文件名变路径 → `FileNotFoundError`，须对 country 也做 `safe()`
- `PLAY` 缺 `MTCSWE` 键 → `KeyError`

**🟡 坑 9：Markdown 链接里不能裸放含圆括号的文件名**
- `make_profiles.py` 生成索引时写成 `- [B-140](B-140-Industrial Personal Computer 2U GmbH (IPC2U)-德国.md)`
- markdown 链接在**第一个 `)` 就截断** → **12 份档案在索引里点不开**（全部是公司名含括号的：IPC2U、TME (Transfer Multisort Elektronik)、IVORY EGG (UK)、Motion (motionworld.com) 等）
- 这直接违反用户"我也好找"的要求
- 解决：链接目标用尖括号包裹 `- [x](<file (a).md>)`（CommonMark / GitHub 均支持）
- **教训：生成任何 markdown 链接前，先问目标串里有没有 `()`、空格、中文**

**🟡 坑 10：审计脚本本身也会骗人（本轮踩了 4 次）**
- `core.quotepath` 默认开启 → 中文路径输出成八进制 `\345...` → 比对全部假失败。修：`git config core.quotepath false`
- 正则 `^##\s*` 中 `\s*` 允许零宽 → 把 `###` 子标题也算成二级标题 → 段数虚高（12 vs 8）。修：`^##(?!#)`
- 字符类 `[^>)]+` 排除了 `)` → 匹配不到含括号的文件名 → 误报"12 个链接损坏"。修：分两段匹配 `<...>` 与普通链接
- `xargs` 遇到含空格/引号的文件名直接崩、静默丢文件。修：改用 Python `os.walk`
- **教训：审计结论不一致时，先怀疑检查工具，再怀疑被检查的对象**

**🔴 坑 11（缺陷 #7）：台厂判定读了我自己写的备注，把台厂的欧洲经销商也判成台厂**
- 备注里我要写"PLANET（**台厂**工业交换机）"来描述它卖什么 —— 评级器读到"台厂"两字，
  就判定**这一行是台厂本体**，直接扔进 C 级
- 后果：新加的 7 家 PLANET 经销商（英/希/加/美）**全部被判"台厂本体，非客户"**；
  连已在库的 Wesco、Graybar（美+加）、Aikom、Saratota 也被牵连
- **与坑 3 完全同构**：拿我们自己写的描述文字当对象身份来匹配
- 解决：新增 `is_taiwan_vendor()`，**只看这一行自己的 国家/类型**，**绝不读备注**。
  修后台厂判定只剩 1 行（Lantech，类型="台厂德国实体"）
- **教训：描述"他卖什么"的文字，不能用来判断"他是谁"**

**🔴 坑 12（缺陷 #8）：规模数字正则命中型号片段与电话号片段**
- `HARD_NOTE` 里的 `8000` 本意是"规模大"，却命中了**电话号码** `+44 1449 888000` 中的 `888000`
  → **把 LinITX（英国 Master+VAD+培训中心+Netonix 分销，有具名联系人）压在 C 级**
- `1M` 本意是"百万级"，却命中型号 `IGS-801M`、`EX-9911M`
- 解决：`(?<![\d.])8000`、`(?<![\d.])1M\b` —— **排除前接数字**，但保留独立出现
  （"约 8000 客户"仍是真实规模信号，不能误伤）
- 修后：LinITX **C → A**（救回），Donato De Meo 保留 C（"8000 客户"是真的）
- **教训：数字类正则必须写"不是什么"，只写"是什么"会吃到型号和电话**

**🟡 坑 13：打补丁时 `\n` 被双重转义，把半截正则变成了注释**
- 我用 Python 字符串插入带 `\n` 的替换文本，结果文件里留下**字面反斜杠-n**，
  导致该行后半段（含 `8000|1M` 那截正则）**整段变成注释而静默失效**
- 表面症状是"改了但没效果"，且 `re.search` 测试全返回"无匹配"
- **教训：改正则后必须立刻做单元验证（正例+反例各测一遍），不能只看重跑有没有报错**

**🟡 坑 11：`make_profiles.py` 没有清理逻辑 → 档案会堆积重复副本**
- 档案名内嵌序号（`B-468-RIDMONT...`），而序号按国家分组排序生成
- **新增/改评级任何一行，其后所有档案的序号都会位移** → 旧文件名的档案不会被删 → 出现同一公司两个编号
- 实测：新增 3 家英国客户后，profile/ 从 709 涨到 **795 份**，其中 `B-468` 与 `B-470` 都是 RIDMONT D.O.O
- 解决：新增 `_clear_stale_dossiers()`，重建前清空 `*.md`；**并带保护闸门**——若任一档案的「跟进记录」已有手工填写的日期行，直接拒绝重建并列出文件
- 原因：用户填的跟进记录无法从 CSV 再生，一旦盲删就永久丢失

### 绕过方案（Workaround）

- **描述**：`git reset --soft origin/...` 作为环境重置后的恢复手段
- **临时原因**：沙箱会周期性丢失 git 历史与 pip 包，远端是唯一持久真相
- **后续清理**：每次重置后第一步先跑 `git rev-list --count HEAD` 校验，再决定是否需要恢复

---

## 📦 关键实体索引（审计锚点，防止后期丢失）

### 主推 SmartByte 型号（CSV 共 18 种，下表为最常推的 5 个）

| 型号 | 主用场景 |
|---|---|
| `LT-S8328GP-4GX24GT-S` | PoE/监控/门禁、酒店/MDU、组播/IPTV、校园（24×千兆 PoE++ + 4×万兆上行） |
| `LT-S8328XGP-4XS24GT-S` | 交换专长、MTCSWE（24×千兆 PoE + 4×万兆，三层硬件卸载） |
| `LT-IS6312XGP-4XS8GT` | 工业/楼宇（导轨、宽温 -40~75℃、ERPS） |
| `LT-S8328XG-4XS24GT-S` | 光纤接入/FTTH、ISP 骨干 |
| `LT-S8328G-4XS24GT-S` | 通用接入、需求待摸底时的默认项 |

### 9 个跨国集团（16 行，最容易重复打电话）

| 集团 | 覆盖 | 备注 |
|---|---|---|
| **Senetic** | 德/波/英/法/意/瑞/瑞典（**7 国 7 行**） | 最大一组，必须先问清国别还是集团采购 |
| **OEM Automatic** | 波/瑞/捷（3 行） | 工业自动化分销 |
| **RBT Technologies** | 斯洛文尼亚/塞尔维亚/克罗地亚（3 行） | 巴尔干三国实体 |
| **Rexel** | 法/意/美（3 行） | 全球电气分销巨头 |
| **LaboTest** | 瑞典+丹麦 / 芬兰（2 行） | |
| **ALIDEX** | 意大利 / 西班牙+葡萄牙（2 行） | |
| **ISP Supplies** | 美国 / 加拿大（2 行） | 同属 MBSI WAV |
| **Tempel Group** | 葡萄牙 / 西班牙（2 行） | |
| **WiFi-Stock** | 英国 / 立陶宛 JSC Katalita（2 行） | |

### 高价值个体账号（已在 A 级，值得单独记住）

- **Jody Lemoine / Tishco Networks**（加拿大）—— **同时持 Cisco CCIE 41436 与 MikroTik 讲师**，能直接读芯片规格
- **Michael Jezierski**（美国，`@indycar.com`）—— IndyCar 赛事方，赛车转播 + **Dante 音频 over IP** + IP 视频组播
- **Carlos Otin / Hotelinking**（西班牙马略卡）—— 酒店 + 多站点 + GPON，曾任被误判为 PoE（坑 3c 的典型）
- **Andrew Drozd / Iron Sentinel**（乌克兰）—— 视频监控 + 报警 + 门禁，真 PoE 刚需
- **Balazs Meretei**（匈牙利）—— MTCSWE，大规模组播（IPTV + 视频监控）
- **Ryszard Labus / SINUX**（波兰）—— BMS / 工业 / 楼宇自动化
- **Urbino Lobo / MiniMeLabs**（葡萄牙马德拉）—— 酒店 + 多住户 MDU + 强制门户，手上有外场工程师数据库
- **Bernhard Kröll / Giganet**（奥地利）—— **23 年** MikroTik 经验 + MTCSWE
- **Sasa Blagojevic**（塞尔维亚）—— 交换专长段落与 IP ArchiTechs / LinkTechs **逐字相同**，属同一技术体系
- **Dennis Burgess / Link Technologies**（美国）—— 北美最大 MikroTik 工程公司之一，交换专长含 EVPN/VXLAN、400G 矩阵
- **Thomas Murdock / IP ArchiTechs**（美国）—— 3 国办公室、6 大洲项目、财富 500 强客户
- **Fibercli**（西班牙）—— 全球最大 MikroTik 工程团队之一，自有培训中心 lo0.es，客户含 IBEX35
- **Veaceslav Samburschii / Academia MikroTik**（罗马尼亚）—— 经营本国 MikroTik 学院
- **Aris Vink / SDC**（荷兰）—— VAD 总代内部售前顾问，即"品类经理"入口
- **Michal Stepanek / 100MEGA i4wifi**（捷克）—— 大分销的**产品经理**，办 mtpc.world 大会

### MikroTik 认证体系（10 张证，用于判断交换需求强弱）

| 证 | 含义 | 对交换需求的指示 |
|---|---|---|
| `MTCNA` | 网络助理（入门） | 无指示 |
| `MTCRE` | 路由 | 弱 |
| `MTCWE` | 无线 | 弱 |
| `MTCTCE` | 流量控制 | 弱 |
| `MTCUME` | 用户管理（Hotspot/PPPoE） | **弱**——这是为什么只持 MTCUME 的顾问归 B 级 |
| `MTCINE` | ISP 互联 | 中 |
| `MTCIPv6E` | IPv6 | 无指示 |
| `MTCSE` | 安全 | 弱 |
| `MTCSWE` | **交换** | **强**——持证人交换是正式专长，A 级核心信号 |
| `MTCEWE` | 企业无线 | 弱 |

### `profile/` 档案结构（未来 Agent 修改前必读）

文件名：`评级-序号-公司名-国家.md`，例 `A-078-Carlos Otin - Hotelinking-西班牙.md`
（国家字段含斜杠的会被替换，如"克罗地亚/斯洛文尼亚"→"克罗地亚-斯洛文尼亚"）

| 段 | A 级 | B/C 级 | 内容 |
|---|---|---|---|
| 一 | ✅ | ✅ | 评级与结论（评级、评级依据、下次复核） |
| 二 | ✅ | ✅ | 公司概览表（公司名/国家/城市/网站/类型/信号/原备注） |
| 三 | ✅ | ✅ | 人员与联系方式（对接人、邮箱、电话、备注中的其他邮箱） |
| 四 | ✅ | ✅ | 品牌与技术栈（持有认证逐条释义、涉及品牌） |
| 五 | ✅ | ✅ | 跟进策略（场景/型号/卖点/怎么开发/风险点；C 级改为"难在哪+切口"） |
| 六 | ✅ | ✅ | 注意点（通用红线 + 本客户特有的 TAA/NDAA、同集团关联） |
| **七** | **首触邮件（可直接发送，英文）** | 跟进记录 | **A 级专属**：主题行 + 正文 + 发送前检查清单 |
| 八 | 跟进记录 | — | 空表格：日期/方式/我方动作/对方回应/下一步 |

> **用户要求**：收到触达反馈后，**由 Agent 更新对应档案的「跟进记录」段并重评级**。
> 反馈录入位置 = 最后一段的空表格；重评级 = 改 `scripts/grade.py` 后重跑，或手工改 CSV 的「评级」列再跑 `export_abc.py` + `make_profiles.py`。

> ⚠️ `make_profiles.py` 会**整目录重建** profile/。手工改过档案的话，重跑前先确认改动来源已写回 CSV/batch，否则会被覆盖。

### batch/ 数据批次（19 个 JSON，顾问名录逐国原始数据）

| 文件 | 国家 | 文件 | 国家 |
|---|---|---|---|
| `at_ch.json` | 奥地利+瑞士 | `it.json` | 意大利 |
| `balkan.json` | 克罗地亚+塞尔维亚+保加利亚 | `last.json` | 北马其顿+科索沃+黑山+马耳他+摩尔多瓦 |
| `be_pt_ie.json` | 比利时+葡萄牙+爱尔兰 | `lt.json` | 立陶宛 |
| `ca.json` | 加拿大 | `lv.json` | 拉脱维亚 |
| `dk.json` | 丹麦 | `ro.json` | 罗马尼亚 |
| `ee.json` | 爱沙尼亚 | `se.json` | 瑞典 |
| `es.json` | 西班牙 | `sk_ba_al.json` | 斯洛伐克+波黑+阿尔巴尼亚 |
| `fi.json` | 芬兰 | `us.json` | 美国 |
| `fr.json` | 法国 | `hu.json` | 匈牙利 |
| `gr.json` | 希腊 | | |

> 用途：CSV 已入库，这些是**原始抓取记录**，用于日后核对或重跑。改动 CSV 前先查对应 batch 文件。

---

## 💬 对话历史摘要

### 对话 1 — 2026-09-21
**主题**：项目启动，MikroTik 客户切入分析 + SmartByte 替代对照表
**产出**：`MikroTik客户切入深度分析_2026-09.md`、`MikroTik_vs_SmartByte_替代对照表.xlsx`、出口地分析（Comtrade 数据）
**遗留问题**：无

### 对话 2 — 2026-09-21
**主题**：Marvell 阵营品牌全景 + 客户开发长期作战系统
**产出**：`Marvell阵营品牌全景和验证手册_2026-09.md`、`Saga客户开发长期作战系统_2026-09.md`
**遗留问题**：无

### 对话 3 — 2026-09-22（上午）
**主题**：A 类客户作战卡 + OEM 合规包 + 合同模板
**产出**：`A类客户12家作战卡和开发信_2026-09.md`、`OEM合规包和标准合同模板_2026-09.md`
**遗留问题**：用户随后**否决**了 OEM 合规包与合同模板路线

### 对话 4 — 2026-09-22
**主题**：用户四项纠偏（小贸易商 / 台厂非客户 / 中性出货 / 大分销难攻）+ 转向重点账号深度分析
**产出**：`三家首发邮件与反向信号客户名单_2026-09.md`（Part A–G）、`报价反击表_2026-09.md`
**遗留问题**：无（Part H 已于对话 14 补写）

### 对话 5–7 — 2026-09-22
**主题**：名录挖掘，客户数 44 → 132 → 216 → 362 → 395
**产出**：ORing / Antaira / Westermo / ComNet / HMS 渠道名录 + MikroTik 官方分销商名录（欧洲 + 美加）
**遗留问题**：无

### 对话 8 — 2026-09-22（主体）
**主题**：HMS 欧洲 + 美国扫完；开启 MikroTik **顾问名录**，逐国扫描至 705 家
**产出**：200 位顾问（类型列实测；德 7 / 波 13 / 捷 5 / 乌 9 / 英 13 / 荷 14 / 法 2 / 西 23 / 意 21 / 匈 6 / 罗 5 / 丹 3 / 瑞 4 / 挪 0 / 芬 1 / 爱 2 / 拉 1 / 立 3 / 美 19 / 加 15 / 希 20 / 奥 4 / 瑞 2 / 比 1 / 葡 5 / 爱 2 / 克 2 / 塞 4 / 斯 0 / 保 3 / 波 1 / 阿 3 / 斯 2 / 北 1 / 科 1 / 黑 1 / 马 1 / 冰 0 / 摩 3）
**产出**：三大发现 —— ① **Link Technologies**（Master+VAD 总代 + 北美最大 MikroTik 工程公司 + 自营网店）② **Hellascom**（希腊第一家 MikroTik 分销商 2001 + 培训中心 2011）③ **Jody Lemoine / Tishco**（同时持 Cisco CCIE 41436 与 MikroTik 讲师）
**遗留问题**：无

### 对话 9 — 2026-09-22
**主题**：名单全量审计 + 修复
**产出**：`名单审核报告_2026-09.md`；合并 2 处真重复；`澳洲`→`澳大利亚`；9 个跨国集团 16 行互标；35 行"无依据三星"标注为待补；43 行区域外标记
**遗留问题**：364 行缺城市、63 行缺网站、三星占比 63% 未重切

### 对话 10 — 2026-09-22
**主题**：A/B/C 评级 + 逐户策略
**产出**：`scripts/grade.py`、`A级客户跟进策略_2026-09.md`
**关键过程**：评级从 302 → 146 → 113 → 99 → 96 → **88 → 85**，每次下降都是抓出一个"自我回读"或"大公司漏判"
**遗留问题**：用户确认"ABC先就这样"

### 对话 11 — 2026-09-22
**主题**：导出分级 xlsx + 生成 profile/ 逐户档案
**产出**：`客户分级跟进表_2026-09.xlsx`、`scripts/export_abc.py`、`scripts/make_profiles.py`、profile/ 705 份
**关键过程**：再抓两个 Bug —— 中文"监控"歧义、"→"推论被回读
**遗留问题**：无

### 对话 12 — 2026-09-22
**主题**：为 85 份 A 级档案补写**可直接发送的首触邮件**
**产出**：`scripts/emails.py`；三处修复（监控歧义、Dante 归类、三份 scenarios 合并为一份）
**关键过程**：修复后 4 家酒店客户归位（酒店 2→6），组播专家不再被当 PoE 买家
**遗留问题**：等用户触达反馈

### 对话 13 — 2026-09-22（本轮）
**主题**：导入 Agent 宪法 v2.0，执行第八条深度审计，生成本文件
**产出**：`AGENT-CONSTITUTION.md`、`AGENT-README.md`、首轮深度审计报告
**遗留问题**：git 本地状态待恢复（需用户确认）

---

## ⚠️ 当前已知问题

| 问题描述 | 严重程度 | 状态 |
|----------|----------|------|
| 本地 git 历史回退到 `dcc1ec1`（第三次环境重置），远程 `7255573` 完好 | 🔴高 | 待用户确认后执行 `reset --soft` |
| `三家首发邮件...md` 的 Part H | 🟢低 | ✅ 已补写（对话 14） |
| ★★★ 占 63%（444/705），三星失去区分度 | 🟡中 | 已标注 35 行为"待补"，整体重切待用户指令 |
| 364 行缺城市、63 行缺网站 | 🟢低 | 已知，待补 |
| ~~评级缺陷 #6：10 行多国标签误判范围外~~ | — | ✅ **已修复**（用户 2026-09-22 确认）：`grade.py` 新增 `in_scope()` 按 `/` 拆分国家；6 行 C→B，4 行因大分销/集团等硬条件**正确留 C**。区域外标记 43 → **33 行（正确值）** |
| 705 行状态全部为"未触达" | 🟢低 | 等用户开始触达 |
| 同域名去重会静默丢弃第二联系人 | 🟡中 | 已加"打印 skipped 并核对"规则；历史遗漏已通过备注合并补救 |
| PR #1 处于 open 状态 | 🟢低 | 未合并，不影响工作 |

---

## 🔍 深度审计记录

| 对话轮次 | 预估信息点 | 已记录 | 待确认 | 审计方法是否全部执行 |
|---------|-----------|--------|--------|---------------------|
| 对话 13 | 约 62 项 | 约 58 项 | 4 项 | ✅ 全部执行 |
| 对话 14（深度入库审计） | 约 45 项 | 43 项 | 2 项 | ✅ 全部执行（10 种方法） |

---

## 🤖 给新 Agent 的交接指令

```
Step 1: 读取本文件，理解全部上下文
Step 2: 执行 git status / git branch -a / git log --oneline -10
Step 3: ★ 额外必做：git rev-list --count HEAD，若为 1 说明环境已重置，
        先 pip install openpyxl --break-system-packages，
        再【向用户申请确认】后执行 git reset --soft origin/arena/01a0c3ef-mikrotik-info
Step 4: 读取"正在进行的任务"，确认下一步行动
Step 5: 检查"深度审计记录"表，若上一轮标注 ⚠️ 部分，优先补齐
Step 6: 向用户简要复述理解到的状态，等待确认后再操作
```

**禁止行为**

- ❌ 不得在未读取本文件前执行任何 git 操作
- ❌ 不得假设分支内容，必须实际读取文件确认
- ❌ 不得在用户确认前自行决定修改方向
- ❌ 不得覆盖用户已有的本地修改
- ❌ 不得跳过第八条深度审计协议直接标记"已更新"
- ❌ **不得切换到 `arena/01a0c3ef-mikrotik-info` 以外的分支**
- ❌ **不得在客户名单"挖完"之前启动分组/策略/下一步工作**（用户已重复强调两次）
- ❌ **不得把台湾厂商当客户开发**
- ❌ **🔒 不得重排 A 级编号**（2026-09-27 铁律）：新增 A 一律追加到末尾（A-379, A-380…），
     禁止以任何理由插入中间或对现有 A 段重排；**只有用户主动提出重构顺序时才可动**
- ❌ **不得主动维护「跟进记录」字段**：该字段由用户线下维护，
     用户有回复并明确要求入库时才写（2026-09-27）
- ❌ **不得擅自降级/剔除 Bechtle A-103**：用户已明确裁决保留原级；不把个案外推为全库豁免。
### 对话 14 — 2026-09-22（本轮，深度入库审计）
**主题**：按宪法第八条执行深度审计，恢复 git，全仓多角度核查"讨论内容是否都入库"
**产出**：
  - 恢复本地 git（`reset --soft` 到 `7255573`），修好 remote fetch refspec 只配了 `main` 的隐患
  - **`AGENT-CONSTITUTION.md`（v2.0）+ `AGENT-README.md`** 新建入库，commit `c06a739`
  - **修复索引 Bug**：12 份含括号文件名的档案在 `00-索引.md` 里链接损坏（坑 9）
  - **补写 Part H**：`三家首发邮件...md` 从 Part A–G 补齐到 A–H（32,265 → 37,962 字）
  - 修正 README 5 处失真数字：顾问 207→200、缺城市 365→364、SKU 5→18 种
**关键过程**：10 种独立审计方法；管道确定性验证（重跑 705 份档案，仅索引变化，其余逐字节未变）
**审计状态**：✅ 已完成第八条深度审计（含第二轮）
**遗留问题**：等用户触达反馈
### 对话 15 — 2026-09-22
**主题**：评估 Claude+GPT 的 30 条获客方法，建方法论，继续挖 Marvell 生态客户
**产出**：
  - `Marvell生态获客方法论_2026-09.md`：30 条 → 砍 20 留 10，每条给操作步骤与搜索串
  - `MikroTik停产机型替换矩阵_2026-09.md`：EOL 双源交叉验证，8 个停产型号 → SmartByte 替换 + 进价
  - 新增 3 家客户（Westbase Networks / Saratota / Netceed UK，均英国）
  - 给 4 家已有账号补 Netonix 信号（LinITX、MS Dist.、WiFi-Stock 英/立）
  - **修复坑 11**：`make_profiles.py` 无清理 → 档案堆积重复副本（795 份 → 708 份），并加保护闸门
**关键判断**：
  - 指出 GPT 头号推荐（Marvell 品牌库）的目标清单踩线——PLANET/ORing/Korenix/Atop 全是台厂，按你的规矩不是客户只是信号源
  - 「招聘/SDK 反推」实测证伪：公开检索拿不到有效职位信息
  - EOL 源 `linknewnet.com` 是把在售的 CRS326/CRS328/CRS520 误标为停产的 SEO 博客，已排除
**遗留问题**：评级缺陷 #6（10 行斜杠国家误判）待用户确认后修复
**审计状态**：✅ 抽查了新行评级、档案去重、索引链接、跨产物一致性
### 对话 16 — 2026-09-22
**主题**：执行用户三项指令（台厂铁律再强调 / 30 条方法全保留 / 按建议修评级缺陷）
**产出**：
  - **修复评级缺陷 #6**：`grade.py` 新增 `in_scope()`（排除式清单，按 `/` 拆分多国标签）
    6 行 C→B（Koning & Hartman、DataLink、Alfa Systems、Westercom、Microstar、SmartSD）；
    4 行正确留 C（Conrad/Reichelt/Distrelec = 大分销、BCS = CCTV 自有品牌、LaboTest/ALIDEX = 集团）
    区域外标记 43 → **33 行（正确值）**
  - **顺带修一处误导**：`hard` 分支的评级依据原本固定写「集团/大公司/…/范围外」，
    导致修好后那 4 行仍显示「范围外」。改为只报**真正触发的条件**
  - `Marvell生态获客方法论_2026-09.md` 重写：30 条**全部保留**，分四梯队，
    冷冻区 12 条每条带「为什么现在不做」+「解冻条件」
  - README 新增**台厂铁律**（用户二次强调，独立成条，含「三根刺」话术）
**关键过程**：
  - 第一次修 `in_scope()` 时**只加了函数、漏改调用点**，重跑后 0 变化 —— 靠 double check 才发现
  - 期间第四次环境重置（openpyxl + git 双双丢失），按 README 坑 1 预案恢复
**审计状态**：✅ 8 项全量复核全绿（CSV / profile / 跟进表 / 主表 / 索引 / 去重 / A 级邮件）
### 对话 17 — 2026-09-22
**主题**：为 A 级中缺乏联系方式的 10 家客户挖具名联系人（发邮件前的准备）
**产出**：10 家全部补齐联系方式，其中 8 家拿到**具名/私人邮箱**
  - **Sarlin Oy Ab（芬兰）**：官网公开完整员工邮箱目录（格式 `firstname.lastname@sarlin.com`），
    拿到 **Mikko Ylilammi（Head of Product Management, Automation & Digital）** —— 按方法论
    「职位优先搜 Product Manager」的理想对象；另有 Niklas Kallberg（Head of Sales, Automation）
  - **Franklin Empire（加拿大）**：François Béland（Sales Manager）、Michel Côté（Assistant Manager
    Automation）；**注意邮箱域名是 feinc.com 而非 franklinempire.com**
  - **Direktronik AB（瑞典）**：Fredrik Brunzell、Stefan Sandstrom（经 Softing 分销商名录）
  - 其余：AA Jones（英国）、Industrial Solutions（加）、Efa Automazione（意）、J A Shomer（美）、
    Aikom（意）、Alejandro Falà（意）
**A 级 87 → 85**：挖到联系方式的同时查明了两家**实际体量**——
  Franklin Empire 是**加拿大最大的独立电气分销商（575 人）**、Cir Toulouse **223 人且隶属 Renold
  集团（20 个实体）**，按 C 级定义（大公司/大集团）**正确降为 C**。联系方式仍已入库，C ≠ 不联系。
**遗留问题**：Industrial Solutions 的 bob@/amy@、J A Shomer 的 czaugg@ 系**按邮箱格式推测，未验证**
**审计状态**：✅ 五方=715、评级一致、无重复、A 级邮件齐全
### 对话 18 — 2026-09-23
**主题**：挖 Moxa（台厂）的欧洲/北美经销商网络 —— 方法论里标记的最大未开采缝隙
**产出**：新增 6 家 + 存量 3 家追加 Moxa 信号，**715 → 721**
  - 新：Sphinx Italia、Jampel（意大利）、Hatteland Technology（挪威，NO/SE/FI 三国网店）、
    Santa Clara Systems、Controller Service and Sales（美国）、Amplicon（英国）
  - 存量追加信号：**Westbase Networks（英国）= Netonix 官方 + Moxa 欧洲分销 + 产品线含
    MikroTik**，三重信号叠加，是当前最直接的工业线切入点；另 Sphinx France、AiRiCOM（B→A）
  - **Jampel** 自称 2012 年起为 Moxa 欧洲销售额第一的分销商，持 Moxa MTSC 认证资质
**待用户裁决的两条 C**：Sphinx Italia、Amplicon（英国）判 C，原因是**我在备注里写的「集团」二字**
  触发了 HARD_NOTE。前者确属 Sphinx 集团（法/意），后者只是我加的**去重提示**（与已存在的
  Amplicon Middle East 区分），属疑似误伤。未擅自修改——同 #7 类问题，等用户定夺。
**⚠️ 第 5 次环境重置（本次会话内）**：仓库被重克隆回初始提交 dcc1ec1，77 个本地提交全丢，
  工作区文件完好但全部显示为未跟踪（`??`）。恢复见「环境重置恢复配方」。

---

## 环境重置恢复配方（已用 5 次，每次都有效）
```bash
git config --add remote.origin.fetch '+refs/heads/arena/*:refs/remotes/origin/arena/*'
git fetch origin arena/01a0c3ef-mikrotik-info
git reset FETCH_HEAD              # 必须是 mixed，--soft 不够
git symbolic-ref HEAD refs/heads/arena/01a0c3ef-mikrotik-info
git config core.quotepath false   # 否则中文路径变八进制
pip install openpyxl --break-system-packages
```
**坑**：`reset --soft` 只移动 HEAD、**不动索引**，会导致索引与工作区错位（同一文件既显示 `D`
又显示 `??` 的双份假象）。必须用 **mixed**（`git reset` 默认模式）。

### 对话 29 — 2026-09-23（用户：1+2+3 全打；再强调 Marvell Prestera / 欧洲+北美 / 只要 A / 不管数量）
**A 147 → 149（+2），合计 880 行**
**① Allied Telesis 英国 300 家代理池 —— 挖到了**
  - **`alliedtelesis.com/gb/en/resellers` 是静态页（非 JS）**，可直接取到全量英国代理 + 电话
    （与 `installers.ui.com`、`/training/centers`、Zyxel 伙伴页等 JS 页不同，**这个能用**）
  - 新增 22 家 ｜ **英国 55 → 77 家，A 9 → 11**
  - ⚠️ 其中 **20 家只有电话、没邮箱** → 按「B 只做群发、没邮箱沉 C」规则全进 C；
    但**这批是集成商型（A 的主产地）**，日后若补邮箱，是最值得优先捞回的一批
  - 主动剔除：Anixter/Wesco、Ingram Micro、TD SYNNEX（过大）
**② Westermo / Antaira 集成商**
  - IPC2U **已在库**（Antaira 官方伙伴，德国，系统集成商）
  - ⚠️ **Antaira Technologies Europe（info@antaira.eu，波兰）是台厂自有的欧洲办公室 → 按台厂规则不收**
  - 结论：Antaira/Westermo 欧洲**分销**名录对话 21 已尽，**集成商**公开源亦见底
**③ 美国 MikroTik 顾问（西海岸 + 东北部）—— ❌ 已挖尽**
  - 搜出的 NCTIK、Andisa IT、IP ArchiTechs、Kyle Heppler、Christopher Fikes **全部已在库**
  - 连同对话 27 的 UK/CA 结论：**MikroTik 顾问/培训中心名录这条脉，欧美主要国家已扫完**
**三条脉状态**
  | 源 | 状态 |
  |---|---|
  | MikroTik 顾问/培训中心名录（欧美） | ❌ 已扫完 |
  | Netonix 渠道 | ✅ 已挖（14 家，Vitesse，用户特批保留，编号 A-106…A-118） |
  | Allied Telesis 渠道 | ⚠️ **英国池已开；德/法/意/西/荷区域页未试** |
  | 台厂（PLANET/Moxa/EtherWAN/Advantech/Antaira/Westermo） | ❌ 分销已尽，集成商公开源见底 |
**下一步最该试**：把 `/gb/en/resellers` 的 URL 格式套到
  **`/de/en/resellers`、`/fr/...`、`/it/...`、`/es/...`、`/nl/...`** —— 若同样是静态页，是下一个大池子
**⚠️ 坑复现（第二次）：`str.replace` 静默失败**
  本轮 README 用 `\n\n---\n\n*本文件由 Agent...` 作锚点，但文件结尾已无 `---` 分隔线 →
  替换未命中且**不报错**，导致「README 已更新」打印了但文件没变，git 报 nothing to commit。
  **改 README 后必须 `grep -c` 验证写入，不能只信打印。**
**当前**：A149 / B344 / C387 = **880**，回归全绿。

---

### 对话 30–31 — 2026-09-23（用户：全挖完，不要停，直到挖完）
**A 258 → 339（+81），合计 993 行**
**✅ 已挖干的国家（Allied Telesis 官方伙伴定位器）**
  | 国家 | 页数 | 新增 | 该国总数 | A 级 |
  |---|---|---|---|---|
  | **德国** | 4/4 ✅ | 59 | 32 → **97** | **71** |
  | **意大利** | 3/3 ✅ | 46 | 44 → **90** | **61** |
  | **法国** | 2/2 ✅ | 10 | 30 → **40** | 11 |
  | 英国 | 1/1 ✅ | 22 | 77 | 34 |
**🔑 钥匙（最重要的一条资产）**
  ```
  /us/en/resellers/?country={国家}            ← 第 1 页
  /us/en/resellers/page/{n}/?country={国家}    ← 翻页
  ```
  该页看着像 JS，其实是**普通服务端分页列表**，可直接 fetch。国家名为小写英文（germany/france/italy/…）。
  每页约 20 家，页尾带分页链接可直接判断总页数。
**剔除标准（已固化为做法）**：ALSO、Arrow、Anixter/Wesco、Bechtle、Ingram Micro、TD SYNNEX、
  Computer Gross、Esprinet、SPIE、Axians、Bouygues、Computacenter、EQUANS、Exertis、
  Johnson Controls、SCC、SNEF —— **跨国集团/超大分销不收**
**❌ 还没挖的国家（下次直接从这里接着做）**
  1. **西班牙 spain / 荷兰 netherlands**（用户点名，本轮上下文用完未做）← **优先**
  2. 比利时 belgium、奥地利 austria、瑞士 switzerland、波兰 poland
  3. 丹麦 denmark、挪威 norway、瑞典 sweden、芬兰 finland
  4. 捷克 czechia、葡萄牙 portugal、爱尔兰 ireland、希腊 greece、匈牙利 hungary
  5. **美国 united-states 第 2 页往后**（目前只取了第 1 页约 24 家）
**人工定级机制（对话 30 建立）**
  - CSV 新增列 **`人工定级`**（末尾第 22 列）。`grade.py` 认它**优先于所有自动规则**：
    跳过自动评级 + 豁免「无邮箱沉 C」+ C 细分标为「人工定级·待处理」
  - 用法：把 `人工定级` 填 A，并在备注加 `【待人工补信息】` → 档案开头会出现
    「🟡 信息不够，需要人工处理」块
  - 目前 **人工定级 A 共 164 家**，全部缺邮箱、待用户人工补
**⚠️ 坑第三次复现：`str.replace` 静默失败** —— 改 README/MD 后必须 `grep -c` 验证写入
**当前**：A339 / B344 / C310 = **993**，回归全绿。

---

### 对话 32 — 2026-09-23（用户：先不管邮箱，继续挖 A，先挖完）
**A 339 → 356（+17），合计 1010 行**（本轮上下文到顶，未做完）
**本轮又挖干 8 个国家/地区**
  | 国家 | 结果 |
  |---|---|
  | 西班牙 spain | 1/1 页，仅 5 条，**2 可用**（Lineas y Cables 为 Integrate Elite） |
  | 荷兰 netherlands | 1/1 页，**3 可用**（Avelution、Kappa Data NL、Pijl Solutions） |
  | 比利时 belgium | 1/1 页，仅 3 条，**1 可用**（Kappa Data Belgium） |
  | 奥地利 austria | 1/1 页，**5 可用**（IT-TRUST、quattroSEC、S.A.B.E.L.、Salzgeber、TEMS） |
  | 瑞士 switzerland | 1/1 页，**2 可用**（DDS Netcom、FIVE Informatik） |
  | 波兰 poland | 1/1 页，**5 可用**（KNT Technology、Nomios PL、Stovaris、Trecom×2） |
  | **美国 united-states** | **2/2 页挖干**，第 2 页 4 家安防型集成商（Security 101 Rochester NY、Silco、Titan Security、Watkins Security） |
  | 捷克 czechia | 1/1 页，**1 可用**（4service s.r.o.） |
  | 瑞典 sweden | 1/1 页，**0 可用**（只有 Arrow ECS + Ingram Micro，全是巨头） |
**⚠️ 重要规律（对齐下一轮的预期）**
  - Allied Telesis 的渠道**高度集中在德国（4 页）、意大利（3 页）、英国（1 页）、美国（2 页）**
  - 其余欧洲小国基本 **1 页、3–7 条，且多为 Arrow/Ingram/TD SYNNEX/Anixter 等巨头**，可用 1–5 家
  - 因此**边际产出正在快速下降**，别再指望小国出量
**❌ 还没查的国家（下次直接照抄这段）**
  `denmark / norway / finland / portugal / ireland / greece / hungary`
  按「小国规律」预估：每国 0–5 家可用，**合计约 5–20 家**，是收尾性质
**🔑 钥匙不变**
  ```
  /us/en/resellers/?country={小写英文国名}
  /us/en/resellers/page/{n}/?country={小写英文国名}
  ```
**当前**：A356 / B344 / C310 = **1010**，回归全绿。A 级中另有**人工定级 190 家**待补邮箱。

---

### 对话 33 — 2026-09-23（用户：1+2 都做；**不要再提邮箱/人工补信息，等他开口**）
**A 356 → 364（+8），合计 1020 行**
**✅ ① Allied Telesis 全线清零（最后一国也扫完）**
  - 本轮补完：**挪威 2**（nLogic、Specto Remote）、**芬兰 1**（Teleste）、
    **葡萄牙 2**（C2F Copper2Fiber、Databox）、**希腊 2**（Digital Sima、LEXIS）、**匈牙利 1**（Young B.T.S.）
  - **丹麦 0 家**（只有 Atea，北欧最大 IT 集团，过大）
  - **爱尔兰 0 家**（只有 Bechtle Direct，过大）
  - ⚠️ **Teleste（芬兰 Turku）本身是视频/接入网络设备厂商 → 可能是竞品而非客户**，已在备注标注，触达前先确认采购角色
  - ⚠️ **主动放弃的欧洲国家**：斯洛文尼亚、克罗地亚、塞尔维亚、罗马尼亚、保加利亚、
    爱沙尼亚、拉脱维亚、立陶宛、卢森堡、冰岛 —— 按「小国规律」预估每国 0–2 家，
    **性价比极低，除非用户要求否则不做**
**② 换厂商：Belden（Hirschmann/GarrettCom）—— 开了个头**
  - 新增 2 家：**Aerco IoT**（英国，Belden 全线分销）、**SOS electronic**（斯洛伐克，Hirschmann 授权分销）
  - 之前已收：Data Connect（美国，Master Stocking Distributor + TAC 中心）、Powertech Controls（美国）
**❌ 记录死路：Extreme Networks 伙伴名录取不到**
  - `extremenetworks.com/partners/partner-locator` 与 `?show-distributors=true` **均为纯 JS 渲染**，
    fetch 只返回徽章说明（Badge 文案），**没有任何伙伴名单**
  - web_search 也搜不到其伙伴名单（官方不静态暴露）→ **Extreme 渠道本轮判死，别再重复试**
**🔑 已验证可用的「静态伙伴页」清单（照这个思路找新厂商）**
  | 厂商 | URL 模式 | 状态 |
  |---|---|---|
  | Alliance/Allied Telesis | `/us/en/resellers/?country={小写国名}` + `/page/{n}/` | ✅ **已全线挖干** |
  | Netonix | `/distributors-resellers/{north-america,europe}.html` | ✅ 已挖 |
  | Extreme Networks | 伙伴定位器 | ❌ **JS，死路** |
  | Zyxel | `/global/en/where-to-buy/locate-partner` | ❌ JS，死路 |
  | Belden | `belden.com/find-a-distributor` | ⚠️ **未试，下轮优先** |
**当前**：A364 / B344 / C312 = **1020**，回归全绿。

---

### 对话 34 — 2026-09-23（用户：继续挖）
**A 364 → 365，合计 1020 行**（本轮大量重复，净增极少）
**❌ Belden 也是死路**
  - `belden.com/find-a-distributor` 及 `us-` / `global-` 子页**均为表单式 JS 搜索**，
    页面永远显示 "0 Results"；加 `?country=Germany&productType=Industrial Networking` 参数**同样无效**
  - 与 Extreme Networks 同类 → **Belden 官方目录本轮判死，别再重复试**
**⚠️ Westermo：静态页但**已挖过**，印证对话 21 的判断**
  - `westermo.com/contact/where-to-buy` **是静态全表**（5 段），可完整抓取
  - 但取到 16 家欧洲伙伴后逐一去重，**15 家已在库** —— 对话 21 记的
    「Antaira/Westermo 欧洲经销商目录已尽（14/14 已在库）」**属实**
  - 且 **英国/美国只有 Westermo 自己的销售办公室**，无独立渠道伙伴
  - 结论：**Westermo 这条脉彻底见底**
**🔑 下一把钥匙（下轮第一优先）：Perle 分销页带 `?countryname=` 参数**
  ```
  https://www.perle.com/howtobuy/distributors.aspx?countryname=Deutschland
  ```
  **该页是静态 HTML，可直接 fetch！**（搜索 snippet 已验证：返回带地址/电话的分销商列表）
  - 已确认德国页内容：Allnet Computersysteme、CDS IT-Systeme、Sphinx Computer Vertriebs、Wesco Anixter
  - ⚠️ 国名用的是**德文/当地语言**（Deutschland 而非 Germany）—— **需先试准国名拼写**：
    `Deutschland / France / Italie / España / Netherlands / United Kingdom / United States / Sverige` 等，
    试不通就抓一次无参页面看下拉选项的真实 value
  - Perle 产品线含 **IDS-710 工业 PoE 交换机（100W 802.3bt）**，与 SmartByte 场景高度吻合
**静态 vs JS 伙伴页总表（下轮照这个挑）**
  | 厂商 | 状态 |
  |---|---|
  | Allied Telesis | ✅ 静态，**已挖干** |
  | Netonix | ✅ 静态，已挖 |
  | Westermo | ✅ 静态，**已挖干** |
  | **Perle** | ✅ **静态，未挖 ← 下轮优先** |
  | Belden | ❌ JS 表单，死路 |
  | Extreme Networks | ❌ JS，死路 |
  | Zyxel | ❌ JS，死路 |
**当前**：A365 / B344 / C311 = **1020**，回归全绿。

---

### 对话 35 — 2026-09-23（用户：继续）
**A 365 → 371（+6），合计 1026 行**
**🔑 Perle 钥匙已验证可用（重要）**
  ```
  https://www.perle.com/howtobuy/distributors.aspx?countryname={英文国名}
  ```
  - **国名用英文**（`United%20States` / `United%20Kingdom` / `France` / `Netherlands`），
    不是德文 —— 修正对话 34 的猜测
  - 静态 HTML，可直接 fetch，返回**名称 / 地址 / 城市 / 邮编 / 电话 / 官网 / 邮件入口**
  - ⚠️ 页首常显示 "Error!"，**不影响内容**，忽略即可
  - 命中率：美国 1 新、英国 2 新（实收 1）、法国 5 新（实收 4）、荷兰 0、意大利 0、西班牙 0
**Perle 各国状态**
  | 国 | 结果 |
  |---|---|
  | 美国 | iComTech（**已在库**）、Express Systems（已在库）、KMJ（已在库）；Ingram/DigiKey/Wesco 过大 → **净 0** |
  | 英国 | **Cogent Distribution 新增**；S-Connect 已在库；Westbase 已在库；Ingram/Arrow/Wesco 过大 |
  | 法国 | **Noriak、Connect Data、EQUIPAGES、PEDAB、Sphinx Connect 新增 5 家**（法国此前仅 11 个 A） |
  | 荷兰 | 0（只有 Wesco Anixter + S-Connect） |
  | 意大利 | **无分销商** |
  | 西班牙 | **无分销商** |
  | 德国 | Allnet / CDS / Sphinx / Wesco —— 基本已在库 |
**⚠️ 去重提醒（易踩坑）**
  - **Sphinx 系是三个不同法人**：Sphinx Italia（意）、Sphinx Computer Vertriebs（德）、
    **Sphinx Connect（法）** —— 已在备注标注**勿合并**
  - **S-Connect 同时覆盖英国与荷兰**（一家公司两个地址），不是重复
**✅ 附带成效：PoE 场景 24 → 30**
  Perle 主推 IDS-710 工业 PoE（100W 802.3bt），其渠道伙伴**天然落在 PoE/监控/门禁场景**，
  是本轮场景增长的最大来源
**❌ Perle 剩下的国家（下轮）**：Canada、Sweden、Norway、Denmark、Finland、Poland、
  Belgium、Austria、Switzerland、Portugal、Ireland
**当前**：A371 / B344 / C311 = **1026**，回归全绿。

---

### 对话 36 — 2026-09-23（用户：继续）
**A 371 → 374（+3），合计 1029 行**（边际产出已明显下降）
**Perle 第二批国家结果**
  | 国 | 结果 |
  |---|---|
  | **瑞典** | **+1 Profcon AB**（Vansbro，+46 281 30600）；Direktronik 已在库；Wesco 过大 |
  | **挪威** | **+1 The Junction**（Drammen，+47 40 40 34 02） |
  | **波兰** | **+1 Microstar sp. z o. o.**（Warsaw，+48 22 8365273） |
  | 加拿大 | **0**（只有 Ingram Micro / Wesco Anixter / 厂商自建 Perle Systems Limited） |
  | 比利时 | **无分销商** |
  | 奥地利 | **无分销商** |
**⚠️ 又一个同名不同法人的坑**
  - **Microstar 出现两次**：Microstar（克罗地亚+斯洛文尼亚，Westermo 渠道）vs
    **Microstar sp. z o. o.（波兰，Perle 渠道）** —— **不是一家**，已在备注标注勿合并
  - 这已是继 Sphinx（意/德/法三家）之后的**第二类同名不同法人**情况
  - **教训：去重要看「国别 + 法人后缀」，不能只看公司名字串**
**❌ Perle 还没查的国家（下轮收尾，预计 0–3 家）**
  `Denmark / Finland / Switzerland / Portugal / Ireland`
  （按已查 11 国的命中率推算，**Perle 这条脉也快见底了**）
**📉 全脉状态总结（重要，决定下一步方向）**
  | 厂商 | 状态 |
  |---|---|
  | Allied Telesis | ✅ 已挖干（四大池：德 97 / 意 90 / 英 77 / 美 2 页） |
  | MikroTik 顾问+培训中心 | ✅ 已扫完（欧美主要国家） |
  | Westermo | ✅ 已挖干 |
  | Netonix | ✅ 已挖（14 家，Vitesse 圈外，特批保留） |
  | **Perle** | ⚠️ **剩 5 国，即将见底** |
  | Belden / Extreme / Zyxel | ❌ JS 死路 |
  | **Transition Networks** | ❓ **唯一还没找到静态目录页的大厂商** |
**当前**：A374 / B344 / C311 = **1029**，回归全绿。

---

### 对话 37 — 2026-09-23（用户：搞完，之后有别的事）
**A 374 → 378（+4），合计 1033 行**
**✅ Perle 全线扫完（最后 5 国）**
  - **芬兰 +1** Timeless Technology（Pori）
  - **葡萄牙 +1** DSSI（Agualva-Cacém）
  - **爱尔兰 +2** Infinite Technology（Dublin）、Electromaster Limited（Tallaght）
  - 丹麦 0（The Junction / S-Connect 均已在库）、瑞士 0（无分销商）
  - **Perle 累计产出约 14 家**，法国单国 5 家最高。PoE 场景 33 → 37
**🔴 重大发现：Transition Networks 已被 Lantronix 收购**
  - `transition.com` **301 重定向到 `lantronix.com`** —— 两家现在是同一家公司、同一渠道
  - 因此「Transition Networks 渠道」== 「Lantronix 渠道」，**不存在独立池子**
  - ✅ 这同时解释了为什么对话 25 从 SEC 年报里挖到的 Lantronix EMEA 名单
    （Sphinx / Atlantik / Jade / transtec / Astradis / Acal）是对的
**⚠️ Lantronix 官方伙伴页 = 低质量源，建议不再投入**
  - 正确入口：`https://www.lantronix.com/to-buy/locate-partner/`
    （注意**不是** `/where-to-buy/`，那个 404）
  - 页面**只渲染 logo 图片**，伙伴名称仅存在于**图片文件名**里
    （Acal-BFi / Accu-Tech / Acromax / ADNet / Braemac / Logicom / Sol / tecnomic / Gresco / …）
  - **无名称文本、无国家、无城市、无电话、无邮箱** —— 只能靠猜，且无国别无法判定是否在欧美范围
  - 筛掉巨头后（Arrow / Ingram / DigiKey / Mouser / Farnell / TD SYNNEX / WESCO /
    Graybar / CDW / Insight / ComputaCenter / Atea / ScanSource）所剩无几
  - **结论：不值得为几张 logo 灌水进库，该源判废**
**🏁 Marvell Prestera 公开渠道目录 —— 全部挖完**
  | 厂商 | 结论 |
  |---|---|
  | Allied Telesis | ✅ 挖干（德 97/意 90/英 77/美 2 页 + 其余欧洲） |
  | MikroTik 顾问 + 培训中心 | ✅ 欧美主要国家扫完 |
  | Westermo | ✅ 挖干 |
  | Perle | ✅ **本轮挖干** |
  | Netonix | ✅ 已挖（Vitesse，特批保留） |
  | Lantronix / Transition Networks | ⚠️ 官方伙伴页只有 logo，**判废** |
  | Belden / Extreme / Zyxel | ❌ JS 死路 |
**再要出量，必须换方法**（不再是「照 URL 批量扫」的机械活），可选方向：
  1. 按场景反查（PoE/酒店/工业 场景下的本地集成商目录）
  2. 挖已入库 1033 家的上下游与客户名单
  3. 展会/协会名录（如 WISP 协会、工业自动化协会会员名录）
**当前**：A378 / B344 / C311 = **1033**，回归全绿。

---

*本文件由 Agent 自动维护，最后一次人工校验：2026-09-23*


### 联系方式补挖进度 — 2026-09-27 续批（A-110..A-199）

- 数据总量未变：A **378** / B **344** / C **311**，1033 条 × 22 列；本轮未增删或升降级。
- **全部 A 既有编号、账号对应关系及表格原行顺序保持不变**；前 49 条全字段不变。
- 原 A-110..119 的 10 条未完成落库批次已复核，另顺号补查 A-120..199 的 80 条。
- 90 条中 88 条取得公开邮箱（87 个去重主地址；A-152/153 共享集团邮箱，不虚报两个独立入口）。
- 4 条仅第三方完整地址：A-118、A-123、A-165、A-167，明确标记待核；不冒充官网确认。
- A-111 无公开邮箱：已抓官网联系页、查公司 LinkedIn，保留域名/表单/电话/Eddie Hing 线索。
- A-119 无公开邮箱：已抓官网首页和联系页，保留域名/表单/电话/ITC Communications LinkedIn。
- **纠错：撤回 A-111 按姓名拼出的邮箱；此前“40 家/30 个邮箱”把推测计入，口径无效。**
- 公开列出 ≠ 邮箱有效或会回复：没有发送邮件、没有 SMTP 测试。只把完整公开地址计入找到，
  不猜姓名格式，不用招聘/隐私/法务/PEC 邮箱充数，不把模板邮箱或所代理厂商邮箱当客户入口。
- 来源逐条写入 CSV 的备注和 profile，另存 `batch/contact_research_2026-09-27_A*.json` 三个批次。
- 有了公开邮箱的本批记录移除过时“抓不到邮箱”段落，但保持 `人工定级=A` 和评级脚本不动。
- 同集团与分支风险只做注记：GU A-152/153/154；Security 101 A-125/126；ACP 只取 Halle 地方入口。
- 下一起点 **A-200**。完成 A 后才重新认真筛选 B/C。新增或升级 A 永远追加，不能因补到邮箱重新排序。

- 本轮一致性校验发现并修复一个旧遗漏：`替代对照表.xlsx/反向信号名单` 仍持有第37轮
  重排前的 327 个尾段编号。按公司名+国家+原行位置逐条匹配后，用**现有 CSV 冻结编号**同步该派生页；
  没有重新分配任何账号编号。跟进表原行顺序、CSV 原行顺序均不变。
- 核验不能只数行或比较编号集合：须比较 `编号→公司名+国家` 以及各基础字段。
  当前 xlsx `档案编号` 的零基索引为 **19**（不是旧交接误记的20）；必须按表头定位，不硬编码。
- 校验通过：1033 条全部原评级/原编号/原行顺序不变；前49条 CSV 全字段和档案逐字节不变；
  90条补挖来源及入口逐一入档；两份 xlsx 的基础字段均与 CSV 一致；对照表其他页单元格未改。
