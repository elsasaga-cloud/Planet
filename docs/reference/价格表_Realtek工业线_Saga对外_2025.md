# Saga 对外价表 · Realtek 工业线（Hasivo 供，2025 年版；第四张表）

生成：2026-10-24（T29-U45 第 60 批）。来源：Drive `Extra Info/Price/Price List_Realtek Industrial Managed Switch.xlsx`（同内容 PDF 由 Simon 2025-04-27 生成，抬头 Alan 的 A 邮箱）与 `Extra Info/Hasivo/Industrial Ethernet.docx`（2025-02-01，Realtek 系列工业非管理型目录）。已入库文本：`data/extra_info_2026-10/text/Extra_Info__Price__Price_List_Realtek_Industrial_Managed_Switch.xlsx__cd7325a0.json`、`…Extra_Info__Hasivo__Industrial_Ethernet_DONE__Industrial_Ethernet.docx__7ec4866d.json`。

**为什么单独一页**：此前「有没有 X」只查三张表（Marvell 价格主表 / HRUI 商用对照表 / CENTEC 产品表），把「Realtek = 只有商用」当成了事实。其实 Saga 自己 2025 年就对外发布过 **Realtek 工业线**（DIN 导轨、-40~+75℃、3 年保修、双 DC 输入），而且挂在客户可见的 Drive 目录里（Netaş 2026-02-27 就是从那里看到 STI-488XGGPM-2BT / STI-0288XGGPM-2BT / STI-2288XGGGPM-2BT 来问的）。**从现在起「有没有 X」查四张表。**

## 0. 怎么用（口径）

- **价是 2025-04 的 USD 列表价（汇率约 7.2）**，再报前按当日汇率与 Realtek ≥20% 线重核（@6.69 大约 +8%）；格式仍是 `$xx USD EXW（快照日期，15 天有效）`。
- **不是主推**：Simon 自己在 Netaş 线程里的判断（2026-02-27 Alan 原话）「For Realtek, it is even far from enough, the management functions are even worse than Marvell」——所以只在客户**自己说出 Realtek / 要低价 / 功能要求简单**时给（SA-052 型），L3 要 PIM-SM/DM、RIPng、PBR、IS-IS 的项目不要拿它顶。
- **保修 3 年**（工业线规则，见口径表 #6）；**电源与光模块不含**；GUI 加客户型号名免费 MOQ 1，加 Logo 免费 MOQ 50；<50 台交期 5~7 个工作日。
- **PoE 机型共性（列表原话）**：2 个 bt 口 + 2 个口自动识别 24V/48V PD（passive-PoE 项目有用——WISP / MikroTik / Ubiquiti 用户的 24V 设备）；`-UP` 款 12V 输入仍可供 PoE（升压，最大 120W）。
- 和 Marvell 线同名撞车：**STI-480XGGM** 在 Realtek 工业表 $145（L3，4×10G SFP + 8 GE），在 Marvell 价格主表 $253（L3）——报价前写清是哪条线，别让同一客户看到两个价。

## 1. 工业管理型（Realtek，2025-04-27 列表，USD EXW）

| 型号 | 端口 | 管理 | PoE | 电源输入 | 2025-04 价 |
|---|---|---|---|---|---:|
| STI-150GM | 1×GE SFP + 1×GE RJ45 上联 + 4×GE | L2 | — | 冗余 DC12~57V | $80 |
| STI-240GM | 2×GE SFP + 4×GE | L2 | — | 冗余 DC12~57V | $80 |
| STI-280GM | 2×GE SFP + 8×GE | L2 | — | 冗余 DC12~57V | $86 |
| STI-480GM | 4×GE SFP + 8×GE | L2 | — | 冗余 DC12~57V | $110 |
| STI-2280GM | 2×GE SFP + 2×GE RJ45 上联 + 8×GE | L2 | — | 冗余 DC12~57V | $110 |
| STI-1080GM | 10×GE SFP + 8×GE | L2 | — | 冗余 DC12~57V | $160 |
| STI-2160GM | 2×GE SFP + 16×GE | L2 | — | 冗余 DC12~57V | $140 |
| STI-154GPM-2BT | 1×GE SFP + 1×GE 上联 + 4×GE PoE | L2 | 2 af/at + 2 bt，240W | 冗余 DC37~57V | $100 |
| STI-244GPM-2BT | 2×GE SFP + 4×GE PoE | L2 | 2 af/at + 2 bt，240W | 冗余 DC37~57V | $100 |
| STI-288GPM-2BT | 2×GE SFP + 8×GE PoE | L2 | 6 af/at + 2 bt，360W | 冗余 DC37~57V | $110 |
| STI-288GPM-2BT-UP | 同上 + 12V 输入升压（PoE 最大 120W） | L2 | 6 af/at + 2 bt | 冗余 DC37~57V（12V 可用） | $135 |
| STI-488GPM-2BT | 4×GE SFP + 8×GE PoE | L2 | 6 af/at + 2 bt，360W | 冗余 DC37~57V | $140 |
| STI-2288GPM-BT | 2×GE SFP + 2×GE 上联 + 8×GE PoE | L2 | 2 af/at + 2 bt，360W | 冗余 DC37~57V | $150 |
| STI-1088GPM-2BT | 10×GE SFP + 8×GE PoE | L2 | 6 af/at + 2 bt，360W | 冗余 DC37~57V | $205 |
| STI-21616GPM-2BT | 2×GE SFP + 16×GE PoE（列表端口栏笔误写成 10 SFP + 8） | L2 | 14 af/at + 2 bt，360W | 冗余 DC37~57V | $190 |
| STI-480XGGM | 4×10G SFP+（100M/1G/2.5G/10G）+ 8×GE | **L3** | — | 冗余 DC12~57V | $145 |
| STI-028XGGM | 2×10G RJ45 上联 + 8×GE（无光口） | **L3** | — | 冗余 DC12~57V | $180 |
| STI-228XGGGM | 2×10G SFP+ + 2×GE RJ45 上联 + 8×GE | **L3** | — | 冗余 DC12~57V | $160 |
| STI-488XGGPM-2BT | 4×10G SFP+ + 8×GE PoE | **L3** | 6 af/at + 2 bt，360W | 冗余 DC37~57V | $170 |
| STI-0288XGGPM-2BT | 2×10G RJ45 上联 + 8×GE PoE（无光口） | **L3** | 6 af/at + 2 bt，360W | 冗余 DC37~57V | $205 |
| STI-2288XGGGPM-2BT | 2×10G SFP+ + 2×GE 上联 + 8×GE PoE | **L3** | 6 af/at + 2 bt，360W | 冗余 DC37~57V | $190 |

列表备注原话：Prices valid 15 days, NOT including power supply；EXW；**Warranty period: Three years**；Lead time for less than 50pcs: 5~7 working days；Customization available；L2 models fully gigabit, not supporting 2.5G optical speed。**L3 的功能清单仓内没有**（Alan 的判断是比 Marvell 弱）——PIM/RIPng/PBR/IS-IS 一律按「没有」答。

## 2. 工业非管理型（Realtek 系列，2025-02 目录 `Industrial Ethernet.docx`，USD/pc）

| 型号 | 端口 | 2025-02 价 | 备注 |
|---|---|---:|---|
| STI-050FE | 5×10/100M | $19 | |
| STI-080FE | 8×10/100M | $24 | |
| STI-110FE | 1×100M 固定光（1×9）+ 1×FE | $19 | |
| STI-140FE | 1×100M SFP + 4×FE | $27 | |
| STI-240FE | 2×100M SFP + 4×FE | $34 | |
| STI-050GE | 5×GE | $24 | |
| STI-080GE | 8×GE | $34 | |
| STI-110GE | 1×1000M 固定光 + 1×GE | $21 | |
| STI-110GE_SFP | 1×GE SFP + 1×GE | $17 | |
| STI-150GE | 1×GE SFP + 5×GE | $27 | |
| STI-220GE | 2×GE SFP + 2×GE | $24 | |
| STI-240GE | 2×GE SFP + 4×GE | $31 | |
| STI-280GE | 2×GE SFP + 8×GE | $46 | |
| STI-210GE | 2×GE SFP + 10×GE | $53 | |
| STI-220DGGE | 2×2.5G SFP + 2×GE | $32 | |
| STI-240DGGE | 2×2.5G SFP + 4×GE | $38 | |

共性（目录原话）：双 DC12~57V 输入、-40~+75℃、IP40、6KV 浪涌 / 8KV ESD、CE-EMC/LVD、FCC Part 15 B、RoHS、**Warranty 3 Years**、每 100 台送 2 台备机代替 RMA；SFP 与电源不含。**同名撞车**：价格主表（SmartByte 线）也有 STI-110GE $29.7、STI-050GE 等——Thu（SA-011）2026-09 PI 的 STI-110GE 走的是哪条线，看 PI 单价。

## 3. 这页对谁有用（已写进各户 `saga_now.gaps`）

- **SA-052 FARADAY（圣彼得堡）**：2024-05-21「We use Realtek… not hi-end, but reliable」、要 DIN 8 口 L3 管理 PoE 带 watchdog——Marvell STI-488XGGPM 报 $350 被一句「350USD?」顶回。**对位款：STI-488XGGPM-2BT（L3，$170）/ STI-288GPM-2BT（L2，$110）**，watchdog 列表未写（待核）。是否对俄开这条线仍是 Simon 定。
- **SC-1483 DEALER Co（俄罗斯）**：L2 DIN 2×SFP + 8×PoE 240W 项目，2024 报 Marvell $120 → 对位 STI-288GPM-2BT $110（量产再核）。
- **SB-089 Linxcom（500 台项目）**：100 台「8 口 2BT 管理 PoE」有对位（STI-288GPM-2BT $110 vs Marvell STI-288DGGPM-2BT $154）；400 台「24 口 10G 上联 L3 PoE」**没有对位**（Realtek 线最大 16 PoE 且无 L3 PoE 24 口）——只能半套。
- **SB-459 Andy（「我有更便宜的」）**：L3 DIN 24 PoE 无对位；8 口 L3 PoE 有（$170）——但他要的是 24 口，别硬塞。
- **SB-473 Netaş**：2026-02-27 已看过并问过这三款 L3，Alan 已答「功能比 Marvell 还弱」；车载 L3（PIM-SM/DM、RIPng、PBR、IS-IS）不要再拿它答。
- **passive-PoE 24V 场景（WISP / MikroTik / Ubiquiti 用户）**：PoE 款 2 口自动识别 24V/48V PD 是这条线独有的一句话卖点；口径 #17 里对 MikroTik 用户可加这半句（仅限工业 DIN 场景）。

## 4. 不要做的

- 不群发；不替代 Marvell 线做主推（Simon 2025-02 群发里的 L3 工业机仍是 Marvell STI-480XGGM）。
- 不把 L3 的高级路由功能写进任何信稿。
- 同一客户同一型号名两个价（STI-480XGGM $145 vs $253）——报价前写明线别。
