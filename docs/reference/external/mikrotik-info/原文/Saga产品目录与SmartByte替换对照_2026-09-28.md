# Saga 产品目录全解与 SmartByte 替换对照（2026-09-28）

> 依据用户 2026-09-28 上传的三份 Saga 价格表整理（`Price List_Marvell Based Commercial Managed Switch.xls`、`Price List_Marvell Based Industrial Managed Switch.pdf`、`Price List_Marvell Based Industrial Unmanaged Switch.xls`），加上已有的两份固件特性表（`Saga Feature List_7.5.x_L2+.xlsx`、`Saga Feature List_7.5.x_L3.xlsx`）。
> **规则（用户 R55）：客户 MD 里的推荐产品一律换成 Saga；Saga 目录里暂时没有对应规格时，继续沿用 SmartByte，并在旁边明确标注。B、C 级本次不动。**
> 价格均为 **EXW 美元**；报价单注明「prices are valid for 15 days」——MD 中出现的价格只是 **2026-09-28 快照**，报价前必须回落到这份表重新核价。

---

## 一、Saga 品牌与三份价格表总览

| 项 | 内容 |
|---|---|
| 品牌行 | **Saga Telecom, OEM Factory** — "Tailored Managed Networking Solutions Provider" |
| 口号 | "Built to Last, Continuous Supply, Evolving Together" |
| 通用条款 | EXW；报价 15 天有效；**<50pcs 交期 5–7 个工作日**；支持定制（Customization is available） |
| 保修 | **商用管理型 1 年**；**工业线（管理+非管理）3 年** |
| 电源/附件 | 商用型**价格已含电源适配器**（AC 型内置 AC-DC；DC 型 5–16V 随附适配器）；**工业线价格不含**工业电源适配器与光模块 |
| 商用 Must-Know | 环保无铅金属壳；**PoE 仅支持 af/at，全线无 802.3bt 90W**；电源分 AC / DC 输入 |
| 工业非管理 Must-Know | 冗余电源带**反接/过压保护**；非 PoE 输入 DC12–58V、PoE 输入 DC44–57V；支持 10K jumbo + 1M 大包缓存 |
| 资料链接 | 商用管理型 https://drive.google.com/drive/folders/1P8-2u6TkNK2Fu98bv92SNd73WbXkyl2L ｜ 工业管理型 https://drive.google.com/drive/folders/18wELd5rPvpYWkcJHD-P9qEMrL0tCSmhn ｜ 工业非管理 https://drive.google.com/drive/folders/1i0qtbohGJXpaLzUYj4Kr682JMpil2H6u |

**命名规律（读型号不求人）**：`STC-` = 商用管理型；`STI-` = 工业型。数字段=端口布局；`M`=Managed；`P`=PoE；`D`=1G/2.5G SFP；`X`=含 10G SFP；`-BT`=混入 802.3bt 90W 端口；`-U`=机架 1U AC 输入；`-C`=SFP/RJ45 Combo；`F`=百兆光。例：`STC-424XGGPM-440W` = 4×1G/2.5G/10G SFP + 24×GE PoE af/at 440W 管理型，$264。

---

## 二、Saga 完整型号梯队（EXW 美元快照 2026-09-28）

### 2.1 商用管理型（STC-，保 1 年，含电源）

| 档位 | 型号 | 规格要点 | 价格 |
|---|---|---|---|
| 8口 非PoE | STC-28DGGM / -U | 2×2.5G SFP+8×GE，DC/机架AC | $84.7 / $93.5 |
| 8口 非PoE 4光 | STC-48DGGM / -U | 4×2.5G SFP+8×GE | $88.0 / $99.0 |
| 8口 PoE | STC-28DGGPM / -U | PoE af/at 240/200W | $99.0 / $110.0 |
| 8口 PoE 4光 | STC-48DGGPM / -U | PoE af/at 240/200W | $102.3 / $115.5 |
| **24口 非PoE** | STC-424XGGM | 4×2.5G SFP+24×GE，机架 | $110.0 |
| **24口 非PoE 万兆上联** | STC-424XGGM | 4×10G SFP+24×GE | $143.0 |
| 48口 非PoE | STC-448DGGM / STC-448XGGM | 4×2.5G/10G SFP+48×GE | $220.0 / $286.0 |
| **24口 PoE 主力** | **STC-424XGGPM-280W / -440W** | 4×2.5G SFP+24×GE PoE af/at，PoE 管理+watchdog | **$165.0 / $220.0** |
| **24口 PoE 万兆上联** | **STC-424XGGPM-280W / -440W** | 4×10G SFP+24×GE PoE af/at | **$198.0 / $264.0** |
| 48口 PoE | STC-448DGGPM / STC-448XGGPM | PoE af/at 440W | $308.0 / $368.5 |
| L3 非PoE | STC-424XGGM / STC-448XGGM | 4×10G SFP，L3 | $294.8 / $511.5 |
| L3 全光 | STC-448XGGMO | 4×10G SFP+48×1G SFP | $687.5 |
| L3 混光 | STC-4168XGGCM / STC-4816XGCGM | 16×SFP+8Combo / 8Combo+16×GE | $412.5 / $353.1 |
| L3 PoE | STC-424XGGPM / STC-448XGGPM / STC-4816XGCGPM | PoE af/at 440W，L3 | $374.0 / $583.0 / $610.5 |

### 2.2 工业管理型（STI-…M，DIN 轨，冗余 DC，保 3 年，不含电源/光模块）

| 档位 | 型号 | 规格要点 | 价格 |
|---|---|---|---|
| L2 精简管理 4/8口 | STI-240FM / 240GM / 280GM | ERPS、VLAN 等精简集；官方定位「低管理要求的 CCTV 项目」 | $55 / $66 / $77 |
| L2 精简管理 PoE | STI-244FPM / 244GPM / 288GPM | PoE af/at 120/240W | $66 / $77 / $88 |
| **L2+ 全功能 4/8口** | STI-240DGGM / 280DGGM | 2×2.5G SFP+4/8×GE，ERPS<20ms | $110 / $121 |
| **L2+ 4/8口 PoE** | STI-244DGGPM / 288DGGPM | PoE af/at 120/240W | $121 / $137.5 |
| L2+ PoE 带bt | STI-244DGGPM-2BT / 288DGGPM-2BT | 2×bt 90W+其余 af/at，240W | $143 / $154 |
| L2+ 8口4光 | STI-480DGGM / 488DGGPM / 488DGGPM-2BT | 4×2.5G SFP+8×GE（PoE 240W） | $132 / $148.5 / $180 |
| **L2+ 8口 万兆上联** | **STI-480XGGM / 488XGGPM** | **4×10G SFP+8×GE**（PoE 240W） | **$253 / $269.5** |
| L2+ 16口 | STI-2160DGGM / 21616DGGPM / 2160XGGM / 21616XGGPM | 16×GE（PoE 240W），含 10G 版 | $220 / $242 / $291.5 / $324.5 |
| L2+ 光混 8+4 | STI-448DGGGM / 448DGGGPM / 448XGGGM / 448XGGGPM | 4×GE SFP+4/8×GE（PoE 240W），10G 版 | $220 / $236.5 / $275 / $297 |
| **L2+ 24口** | **STI-4240DGGM / 42424DGGPM / -4BT / 4240XGGM / 42424XGGPM / -4BT** | 24×GE（PoE 240/370W），DC12–75V | **$330 / $363 / $407 / $385 / $423.5 / $456.5** |
| L2+ 24口 机架 | STI-4240DGGM-U / 42424DGGPM-U / -2BT / 4240XGGM-U / 42424XGGPM-U / -2BT | 1U AC100–240V（双AC/双DC/AC+DC 可选） | $363 / $407 / $440 / $412.5 / $451 / $484 |
| L2+ 光汇聚机架 | STI-4168DGGCM-U / 4168XGGCM-U | 16×SFP+8Combo | $467.5 / $511.5 |
| L3（RIP/OSPF/BGP4/ECMP/VRRP） | STI-488XGGGM / 4160XGGM / 41616XGGPM / -4BT / 4240XGGM / 42424XGGPM / -4BT | DIN 轨 L3 | $451 / $462 / $495 / $528 / $478.5 / $517 / $550 |
| L3 机架 | STI-4240XGGM-U / 42424XGGPM-U / -2BT / 4816XGCGM-U / 4816XGCGPM-U / -2BT / 4168XGGCM-U / 4480XGGM-U | 1U L3，48口顶配 | $506 / $550 / $583 / $572 / $605 / $638 / $605 / $847 |

### 2.3 工业非管理型（STI-E/P，DIP 拨码功能，保 3 年）

- 介质转换器（MC）：STI-110FE $23.1 起；PoE 版 STI-111GP $36.3（af/at 30W，250m 延伸，PoE watchdog）。
- 5/8/16口 电口：STI-050GE $34.1 / STI-080GE $55.0 / STI-0160GE $115.5；百兆版再低 $6–11。
- 带光口：4+1 STI-140GE $37.4；8+1 STI-180GE $59.4；**4+2 STI-240GE $40.7**；**8+2 STI-280GE $63.8**；8+4 STI-480GE $115.5（链路聚合）。
- PoE（af/at，250m 延伸，watchdog）：5口 STI-054GP $42.9；8口 STI-088GP $66.0；16口 STI-01616GP $143；4+2 STI-244GP $49.5；**8+2 STI-288GP $74.8**；8+4 STI-488GP $132；16+2 STI-21616GP $203.5。
- DIP 功能集：端口隔离 / 流控 / QoS / 风暴抑制 / 250m 延伸 / PoE watchdog / LFP / 光纤冗余 / 链路聚合（按型号）。
- 电口非 PoE 输入 DC12–58V、PoE DC44–57V；10K jumbo；1M buffer。

---

## 三、芯片与固件（特性表原文结论）

| 固件 | 芯片 | 关键能力 | 关键缺口（推介时避坑） |
|---|---|---|---|
| 7.5.x **L2+** | Marvell 98DX2515/2518（AC5 Lite） | 静态路由 4096 条、QinQ（含 flow-based）、ERPS<20ms、Private VLAN、Voice VLAN、480 ACL、DAI、802.1X/RADIUS/TACACS、sFlow、MQTT、HTTPS、SSH 公钥、双分区、PoE 排程/Legacy/反供电、af/at/bt | — |
| 7.5.x **L3** | Marvell 98DX336S（PC3）/ 98DX2538（AC5+） | 在 L2+ 基础上加 RIP/OSPFv2/IS-IS/BGP4/ECMP/VRRP；1500 ACL；4K 组播表 | **无 Voice VLAN / Private VLAN / Super VLAN**；PC3 无 DHCP Relay、无 HTTPS、无 DAI/防网关欺骗；无 RIPng/OSPFv3/PIM/MPLS；无 SSH 公钥登录；无 RSPAN（AC5+） |
| 工业 L2 精简系（STI-2x0FM/GM、2x4FPM/GPM、288GPM） | 官方注：「支持有限但有用的功能：ERPS、VLAN、PoE 管理；适合低管理要求的 CCTV 安防项目」 | 精简集 | 无 L2+ 全集 |

**推介话术影响**：要 Voice VLAN（IP 电话项目）→ 推 L2+ 系；要 HTTPS 网管 → 推 L2+ 系或 L3 的 AC5+ 版；要动态路由/VRRP → 才上 L3。

---

## 四、SmartByte → Saga 全量替换对照（R55 起执行）

> 「→」右边为新 MD/CSV 中使用的 Sagify 写法；EXW 价格快照。**Saga 无对应时保留 SmartByte 并加标注**。

| SmartByte 旧型号 | 场景 | Saga 替换 | 说明 |
|---|---|---|---|
| LT-S8328XGP-4XS24GT-S | 商用 24口 PoE + 4×10G 主力 | **STC-424XGGPM-440W**（$264，af/at 440W） | ⚠️ bt 90W Saga 商用线没有；客户明确要 bt 时回 `LT-S8328XGP-4XS24GT-S` 并标注「Saga 暂无对应，沿用 SmartByte」 |
| LT-S8328GP-4GX24GT(-S) | 商用 24口 PoE 标杆/首梯 | **STC-424XGGPM-440W**（$220）；预算紧用 **-280W**（$165） | 同上 bt 缺口 |
| LT-S8328XG-4XS24GT-S | 商用 24口 非PoE + 4×10G | **STC-424XGGM**（$143） | — |
| LT-S8328G-4XS24GT-S | 商用 24口 非PoE | **STC-424XGGM**（$110） | — |
| LT-S8328XG-4XS8GT-S | 商用 8口小接入 | **STC-48DGGM-U**（$99，4×2.5G SFP+8×GE） | 10G 上联的 8口商用 Saga 暂无；坚持 10G 上联回 SmartByte 并标注 |
| LT-S8528XG(-4XS24GT) | 商用 L3 24/48口 | **STC-424XGGM（L3）**（$294.8）/ **STC-448XGGM**（$511.5） | — |
| LT-S6326G-2X24GT 等汇聚 | 万兆/全光汇聚 | **Saga 无全万兆汇聚**：就近 STC-448XGGMO（L3 48×1G SFP+4×10G，$687.5）或 STC-4168XGGCM-U（$511.5）；坚持 24×10G → 保留 SmartByte 并标注 | ⚠️ 标注位 |
| LT-IS6310G(-2GX8GT) | 工业非管理 8口+2光 | **STI-280GE**（$63.8，3年保） | — |
| LT-IS6306G(-2GX4GT) | 工业非管理 4口+2光 | **STI-240GE**（$40.7） | — |
| LT-IS6310GP-2GX8GT | 工业非管理 8口PoE+2光 | **STI-288GP**（$74.8） | — |
| LT-IS6312G(-4GX8GT) | 工业管理 8口 | **STI-480DGGM**（$132，ERPS<20ms） | — |
| LT-IS6312XG-4XS8GT | 工业管理 8口 + 4×10G | **STI-480XGGM**（$253） | — |
| LT-IS6312XGP-4XS8GT | 工业管理 8口PoE + 4×10G | **STI-488XGGPM**（$269.5，240W） | — |
| LT-IS6312XGP-4XS8GT-2BT | 工业 8口PoE 含 90W | **STI-288DGGPM-2BT**（$154，2×bt+6×af/at，2.5G 上联） | 4×10G 上联+bt 组合 Saga 暂无；需要该组合回 SmartByte 并标注 |
| LT-IS6318GP-2GX16GT | 工业管理 16口PoE | **STI-21616DGGPM**（$242） | — |
| LT-IS6318XG-2XS16GT | 工业管理 16口PoE 万兆 | **STI-21616XGGPM**（$324.5） | — |
| LT-IS6320G-4GX16GT-D | 工业管理 16口 | **STI-2160DGGM**（$220） | — |
| LT-IS6328XG-4XS24GT(-D) | 工业 L2+/L3 24口+4×10G | **STI-4240XGGM**（L2+ $385 / L3 $478.5 同型号两档，报价注明档位） | — |
| LT-IS6328XGP-4XS24GT | 工业 24口PoE+4×10G | **STI-42424XGGPM**（$423.5） | — |
| LT-IS6328XGP-4XS24GT-4BT | 工业 24口PoE 含 4×90W | **STI-42424XGGPM-4BT**（$456.5） | — |
| 通用 fallback 泛称（LTE/LT-…） | — | 按上表就近；找不到规格等价 → 保留 SmartByte 原文并加「（Saga 暂无对应，沿用 SmartByte）」 | — |

**一句话规则**：能换 Saga 就换（附 EXW 快照价+15 天有效期提醒）；换不了就留 SmartByte 并明码标注原因（bt 90W / 全万兆汇聚 / 10G 8口商用）。

---

## 五、对客户推销侧的影响（写进 MD 时引用）

1. **CCTV 梯**：L2 精简工业系（STI-288GPM $88）= 官方自认「适合低管理要求 CCTV 项目」→ 低端 CCTV 更便宜；要 PoE 管理/watchdog 上 L2+ STI-288DGGPM（$137.5）或商用 STC-424XGGPM-280W（$165）。
2. **bt 90W 实话**：商用无 bt；工业只有混插 BT 版（最多 22×af/at+2×bt、20+4、12+4）。高功率 PTZ/射灯/AP 超过 30W 的场景，Saga 只能工业线顶或回 SmartByte——**绝不能口头承诺商用 90W**。
3. **价格锚**：24口 PoE 商用 $180–264 EXW，比旧 SmartByte 话术里的「同价带亚洲厂」更有落点；工业 3 年保是硬卖点（商用 1 年）。
4. **报价纪律**：价格表注明 15 天有效、EXW、不含运费关税；工业不含电源与光模块——**报价信里永远带这一条免责**。
5. **Marvell 叙事不变**：全线 Marvell 芯（AC5 Lite/PC3/AC5+），与 MikroTik 系客户的「芯片透明」话题无缝衔接。
