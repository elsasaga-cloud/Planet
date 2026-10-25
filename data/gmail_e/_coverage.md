# Elsa 邮箱（e.sagatelecom@gmail.com）连接器路径入库 — 覆盖说明

> 方式：Arena Gmail 连接器逐封读取（`list_messages` 建索引 → `get_message_text(include_quoted=false)` 取正文），由代理手工转录为 JSON；**不是** Takeout 导出。
> 裁定依据：T29-U23（2026-10-23 06:15Z）Simon「Elsa邮箱你不是连接了吗 没办法直接读取内容啥的？还是需要我导出？」→ 方案 (b)。

## 邮箱构成（连接器 2026-10-23 06:01Z–06:20Z 读数）
| 范围 | 封数 / 线程 | 说明 |
|---|---|---|
| 全邮箱 | 3,685 / 3,298 | 仍在增长 |
| SENT | 3,224 / 3,169 | 2025-02→2026-09 群发（16 个主题模板） |
| CATEGORY_PERSONAL | 153 / 131 | 真人来信（含退信/自动回复/未答复） |
| CATEGORY_UPDATES | 297 | 大多是退信通知 |
| `Replied` 标签 | **189 / 51 线程** | Elsa 实际回复过的往来线程 = 本次入库主体 |
| `Daily` 标签 | 487 / 237 | 日常群发批次标记 |

## 进度
| 项 | 状态 | 文件 |
|---|---|---|
| `Replied` 索引（189 封 / 51 线程，7 页） | ✅ 189/189（06:25Z） | `index_replied.jsonl` |
| `Replied` 来信正文（客户→Elsa，67 封） | ✅ 67/67（2026-10-23T07:03Z；sales@eurotechindia.com 两封正文为空，见文件 note） | `text/<id>.json` |
| `Replied` Elsa 回复正文（101 封，其中首封群发为模板） | ⏳ 38/101（2026-10-24T16:22Z，+SB-1009 ×2 +SB-1275 +SB-971 ×2 +SC-1835 03-31「SKD is fine with us」；A/B 档 Elsa「Re:」回复已全部入库，余下 63 封 = 各线程首封群发模板 + C 档 14 封，第 73 批：A/B 档 51 线程里所有「Re:」回复——SB-746 / SB-973 ×2 / SB-427 ×2 / SB-656 / SB-164 / SA-118 / SA-076 ×2 / SA-023 / SB-121 ×3 / SB-099 / SB-462 / SB-178 ×6 / SA-081 ×2 / SB-029 ×2 / SA-147 / SA-116 / SA-046 / SB-580 / SB-960 / SB-261；余下 = 各线程首封群发模板 + C 档） | `text/<id>.json` |
| 退信（21 封）：仅记录被退地址 | ⏳ | 索引 labels 含 `D` 可识别 |
| 个人类未进 `Replied` 的来信 | ✅ 已枚举（2026-10-24T16:15Z，第 73 批）：`-from:e.sagatelecom -label:Replied` 共 ≈201 封，剔除退信/自动回复/工单/问卷后真人来信仅 9 封，全部入 `text/`：th-it.com 2026-09-08 婉拒（SB-325）；3lines.com.sa ×3（SB-580，C；2026-02-08 RFQ 附件已拉到 `attachments/`）；tescom.co.tz 2025-08-23（SB-164 第一问，无人答）；rkahir65@gmail.com 2025-07-26 要价（SB-297，**我方欠答**）；bandasonkelly@gmail.com「I am」（SC-2857，C）；weg.net 模板回复；eurotechindia 第三封空正文。其余 = chipdip.ru / zscom.ru / triple-s.no / telecamera.ru / msy / pbtech / r-stahl / actcorp / techgates / Baltic Networks / satmetrix 等自动应答 | `text/<id>.json`，`attachments/` |
| 附件原件 | ❌ 不经连接器拉（base64 逐件，体积大） | 需要时 Takeout |
| 发件群发日志 3,224 封 | ❌ 连接器 ≈108 页不可行 | Takeout 可选 |

## 字段
`id / thread_id / message_id_header / from / to / cc / subject / date / labels / text / text_source / char_count / attachments[{filename,mime_type,size}] / note / fetched / method`
（`labels` 里 `Replied` = `Label_308850763726262064`；索引行 labels 缩写 S=SENT P=PERSONAL U=UPDATES I=IMPORTANT R=Replied D=Daily T=TRASH STAR=STARRED）

## Elsa 群发的 BCC 结构（第 73 批(o)，2026-10-24 16:35Z）

- Elsa 每封群发 = 1 个 To + 15–40 个 **Bcc**（`get_message(metadata)` 核对 `19bd4c1a8a5c8f66` 印度批 Bcc 34、`1a05bfb71364077f` PL 批 28、`1a06ba5722292bab` UK 批 38、`1a057bf756774b15` IT 批 25、`19ff11f7aa952525` CH/US 批 15、`19ffb43006420c22` 北欧 批 31、`19e1b893e9c06378` 杂批 31）。Sent 3,224 封 ≈ 10 万人次触达；最近一轮「24 Port PoE Managed Switch」（2026-08-03→09-10）317 封，正文「Price: 170USD/PC」。
- 连接器 `list_messages` 的 `to:` / `bcc:` 都能命中 Bcc 收件人，但结果只显示 To 首收件人 → 多域 OR 查询无法判定是哪个域命中；逐户单域查询可判（0 = complete:true）。
- 本轮读到的 6 个 Bcc 头落在 `bcc_batches_2026.json`，与客户库比对命中 150 户（B 51 / C 99）→ 51 户研究档已改绑定 + 事实（`k: elsa_bcc`）。
- 抽样结论：土耳其近期首封 11 户 0/11（Elsa 几乎不发土耳其；仅 2026-05 杂批里有 fotech/gsl/irtibatmerkezi）；美国 makonetworks/softwareeffect/virtualprotective/microfasttech 0/4，但美国**有**专批（premiertek / nssi / allisontecusa / solimedia 四批 ≈ 100 地址）；欧洲 PL×2 / UK / IT / DE / CZ / ES / SK / 北欧 / IS / CH 批全部读到。至 16:43Z 共读 25 封 Bcc 头（24 封属本轮 317 封 + 1 封 2026-05 10G）→ 命中 484 户（A 3 / B 119 / C 362），124 份研究档已改；本轮欧美批次基本读齐，余下 ~290 封为亚非拉 1:1 + 俄批（`campaign_24poe_heads`）。往前 ~2,900 封老群发一封没读（Q-60）。

## Elsa 触达史补全（第 74 批，2026-10-25 01:53Z–02:48Z）

- **锚户时间线**：`from:e.sagatelecom to:<锚域>` 一条查询 = 该锚的全部轮次（Elsa 每轮固定 1 To + 同批 Bcc）。读头 60 封 / 锚 36 个（`bcc_batches_2026.json` `batches[]` + `anchors{}`）→ 命中 **757 户（A 4 / B 166 / C 587）**，`elsa_bcc_apply.py` 幂等套用；锚户自己按精确地址改「Elsa 群发 To 直收 N 轮」（10 户，含 SB-973）。
- **国别 TLD 穷举**（`in:sent to:.xx`，≤201 条即 complete）：PL / DE / UK / ES / FR / NL / CZ / AT / BE / SE / FI / NO / DK / CH / PT / IE / HU / RO / GR / CA / NZ 21 国读完（`elsa_sent_tld_probe_2026-10-25.json`）；`.it` `.tr` 201+ 未完（TR 逐户 11/11 为 0，Elsa 基本不发土耳其）；巴尔干/波罗的海 OR 不完整。美国四批（premiertek / nssi / allisontecusa / solimedia）+ 加拿大批读齐。
- **非锚 1:1 普查**（`in:sent` 排除 39 锚域 + 9 地址，按日期窗分页抄录）：566 行存 `elsa_sent_nonanchor_2026-10-25.json`（全主题；`_note` 记窗口与未爬 `next_page_token`）。结构：首封 **2025-02-10**；2025-02-10→03-14 ≈260 封全球 1:1；之后月度「锚 + Bcc」；1:1 名单重发波 2025-12-10→17「Booster PoE Switch」、2025-12-29/31「Marvell Industrial Alert System」、2026-05-07→21「10G Enterprise SFP Switch」、2026-08-06→31「24 Port PoE」、2026-09-07→15「16 Port Industrial PoE Switch」；末封 **2026-09-15**。命中 430 户（A 7 / B 117 / C 306）→ A/B 139 户写 `elsa_1to1` 事实 + 绑定段。未抄窗口：2025-03-15→12-10（201+）、2026-01-01→05-07 与 05-21→08-06、2026-08-07 22:04→08-10 的第 2 页起。
- 合计：A/B 1,226 户中 **Elsa 已核实触达 297 户（A 10 / B 287）**；其余 B ≈600 户「未发信/未触达」= S/A 口径 + 欧美土已被 TLD 穷举反向排除。Replied 标签在普查里只见 2 条真回复（bandasonkelly 2026-08-19、lezdco 2026-05-15）。
