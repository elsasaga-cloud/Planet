# 从 Mikrotik 仓库继承的规则与方法摘要（阅读记录 · 2026-10-19）

> 用户要求（PR-01-01）：完整阅读 `SimonSaga-202306/mikrotik-info` 的 main 与 `arena/01a0c3ef-mikrotik-info` 分支，只学逻辑/规则/要求，不重新爬数据。本文件是阅读结论，供本仓库任何 Agent 不必再回读 318 次提交即可掌握口径。参考克隆在沙箱 `/home/user/_ref/mikrotik-info`（分支 HEAD `2fd1b0a4`，R73），**未复制数据到本仓库**。

## 1. 读了什么

| 文件 | 读取方式 | 结论用途 |
|---|---|---|
| `AGENT-CONSTITUTION.md` / `AGENT-README.md` / `README.md` | 全文 | 本仓库宪法与 README 结构 |
| `docs/requirements/用户要求总账.md`（1,796 行，R01–R72 + 附录 R64–R67） | 全文分 8 段读完 | 继承规则 INH-01…17；总账体例 |
| `docs/rules/客户档案结构与内容规则.md`（R56 v2 骨架） | 全文 | 原样复制到 `docs/rules/` |
| `Saga产品目录与SmartByte替换对照_2026-09-28.md` | 全文 | 型号对照基线（本仓库用新价格表重算） |
| `Marvell生态获客方法论_2026-09.md`（30 法 + 零·五条） | 前 20 KB + 关键节 | 方法论继承与 PLANET 待挖判断 |
| `死路与死链备案_2026-09.md` | 前 12 KB | 死链规避 |
| 主表 `客户名单_反向信号_2026-09.csv`（1,032 行 × 22 列） | 表头 + 样例 + `grep -i planet` 26 行 | CSV 架构；跨仓去重参照 |
| `profile/A/A-002…md`（v2 样板，277 行） | 全文 | 档案渲染目标形态 |
| `docs/audit/2026-10-12_R73_C类AB加厚进度.md` + `git log` | 全文 / 最近 12 条 | 最新轮次（R73：C-031—C-055 加厚）；总账止于 R72 |
| `scripts/`、`batch/`、`docs/sales|evidence|history`、`tests/` | 目录清单 | 流水线形态（make_profiles → render_v2；B 类单独渲染；audit；tests） |
| main 分支上传件（A-069/A-311 回复、Gmail PDF、Feature List、MikroTik_L2Plus_Switches.xlsx、芯片抓取脚本、出货地/价值分析 MD） | 文件名清单（内容与本任务无直接关系，未逐字读） | 知道存在即可 |

## 2. Mikrotik 仓库 73 轮的主线（压缩）

1. **R01–R37 挖掘**：按「品牌 → 其欧美渠道/顾问名录」反向挖：ORing 64、Antaira 9、Westermo 14、ComNet 7、HMS/N-Tron/Red Lion 111、MikroTik 官方分销 246、MikroTik 认证顾问 200（`mikrotik.com/consultants/europe/{country}`）、Allied Telesis、Perle、Netonix、Moxa、Belden。总 1,032 户：A 580 / B 167 / C 285。
2. **R38–R53 联系方式研究**：逐户找邮箱/电话/KP；定级规则固化：A=真实需求+直达人；B=有邮箱；C=无邮箱/过大/区域外。集成商 A 率 34.5%，分销商 3.7%。
3. **R54–R57 加厚**：A 类 10 维调研 + 恰好 3 步跟进计划；R55 六维深挖（芯片/KP/SWOT）；R56 外部 7 份 AI 评审后定 v2 骨架 17 节；B 类 167 全量深挖。
4. **R58–R63**：供应链反向法新挖；去重合并；编号冻结；型号纠正（STC-424DG→STC-424XGGPM-280W，$180/台）；退信处理；B→A 升级。
5. **R64–R67**：具名 KP 猎捕（web_search + 各国工商登记：Companies House / northdata / pappers / KRS / proff / allabolag…）；"不再是 sales/info 通用邮箱"；推土机式 100 户深挖；证据补钉。
6. **R69–R73**：退信台账；C 类清理（删大陆公司、重编号 C-001+）；一轮跟进完成（744 户，A-069/A-311 回复）；A/B 全量策略；C 类按 A/B 深度加厚到 C-055。

## 3. 对 PLANET 的直接结论

- 方法论文件第 46/54/282 行：**「PLANET ⏳ 待挖（最大一块）… 预计 +50~80 家欧洲分销商」**；第 366 行又写「PLANET/Moxa/EtherWAN/Advantech 经销商名录 ❌ 前几轮已挖完」——两处矛盾。主表核对：含 PLANET 信号的仅 26 行（其中 ~13 行是 PLANET 授权渠道，多为 C）。**结论：PLANET 渠道在 Mikrotik 仓库并未系统挖过**，本仓库从零系统做，但要与这 26 行去重（见 `data/Mikrotik仓库已有PLANET相关客户_对照.csv`）。
- 已知 PLANET 相关户（跨仓参照）：Aikom Technology（IT，A-032）、TRIOTRONIK（AT，A-469）、Fiber24（DE，A-480）、Proficomms（CZ，A-497）、Instant Byte（ES，A-564）、Globall Distribution（CA，C-015）、Planet Shop（GR，C-023）、ABP TECH（US，C-067）、Black Box（US，C-071）、Platinum Micro（US，C-085）、Pulse Supply（US，C-089）、Connectec（UK，C-107）、Netceed UK（C-115）、Saratota（UK，C-116）、Ekanet（ES，C-124）、shop4power.nl（NL，C-259）等。

## 4. 继承的硬规则

见 `docs/requirements/用户要求总账.md` 表「INH-01…17」与 `AGENT-CONSTITUTION.md`。要点：台厂不是客户；零臆造；邮箱只记公开找到的；编号冻结；档案由脚本渲染；README 每轮更新并 grep 自检；价格 USD EXW 快照格式；首触单一 P1、一问；中性包装。

## 5. 继承的流水线形态（本仓库精简版）

```
web_search / fetch_page（逐页，不能批量 curl）
   → batch/<日期>_<批名>.json（原始证据：公司、URL、原文摘录、抓取日期、初评与依据、skipped/merged）
   → scripts/add_batch.py（去重、编号、写主表 CSV）
   → scripts/render.py（按 v2 骨架渲染 profile/A|B|C/*.md，B/C 用精简骨架）
   → scripts/audit.py（编号唯一、CSV↔profile 对账、空字段、URL 格式）→ errors: 0
   → README.md / AGENT-README.md 进度更新 → 对话全记录 / 总账 → commit → push
```

## 6. Mikrotik 仓库记录的坑（本仓库照避）

- `str.replace` 静默失败 → 写后 `grep -c` 验证。
- 子串去重误杀同名不同法人 → 国家 + 法律后缀键。
- 沙箱重置丢 openpyxl → 用 `.venv_planet`/重装。
- 批次 JSON 加载顺序后者覆盖前者 → 新批追加在末尾、合并不覆盖。
- 幻觉名单 → 每个名字必须能回溯到检索结果。
- JS 渲染的经销商定位器（Extreme/Zyxel/Belden/Ubiquiti/MikroTik 培训中心）抓不到 → 用 web_search 摘要绕行。
- LinkedIn 员工页登录墙 → 只记入口，不编人名。
