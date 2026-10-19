# 价格表 · SmartByte 人民币 → 三档加价 → 美元 EXW（生成日 2026-10-19）

> 由 `scripts/pricing.py` 从用户上传的 4 份 SmartByte xlsx 与 3 份 Saga PDF 自动生成；**不要手改本文件**，改规则请改脚本或对照表后重跑。

## 规则与快照

- **公式**：报价 USD = SmartByte 未税 CNY × (1 + 档位) ÷ 汇率；档位 20% / 25% / 30%（用户 2026-10-19）。
- **汇率快照**：1 USD = **6.69 CNY**（2026-10-17；来源：macrotrends.net / exchange-rates.org（2026-10-17 收盘 6.6912/6.6908）；Bloomberg 2026-10-16 6.6865）。报价当日须重新核汇率。
- **价格有效期**：SmartByte 管理型两表 2026-09-01 → 2026-12-30；非管理型表 2024-01-11 更新；Bypass 表 2025-03-12。**报价前核价**。
- **条款**：EXW；商用线（STC-）保 1 年、含电源适配器；工业线（STI-）保 3 年、**不含**工业电源与光模块；PoE 均为 af/at（bt 仅 SmartByte -BT 衍生型，Saga 工业线部分型号有 -2BT/-4BT）。
- **档位默认**：分销/走量/比价 → 20%；集成商/项目 → 25%；OEM/ODM 深度定制或小批量技术型 → 30%。档案里写明所选档位与理由。
- **型号书写**：MD/邮件写 Saga 型号；下表「Saga对应型号」为空或标「暂无对应」者，写 SmartByte 型号并注明「Saga 暂无对应型号，沿用 SmartByte 型号」。
- **统计**：SmartByte 型号 135 个；有 Saga 对应 118 个；无对应 17 个；**按今日汇率 +20% 已高于 Saga PDF 列表价的型号 9 个**（Saga PDF 列表价似按旧汇率/旧成本计算，建议用户刷新 Saga PDF）。

## 速查（最常用 P1 候选）

| SmartByte | Saga 型号 | CNY | +20% | +25% | +30% | Saga PDF 列表价 |
|---|---|---:|---:|---:|---:|---:|
| LT-S8310GP-2GX8GT | STC-28DGGPM | 450 | $80.7 | $84.1 | $87.4 | $99.0 |
| LT-S8328GP-4GX24GT-S | STC-424DGGPM-280W | 750 | $134.5 | $140.1 | $145.7 | $165.0 |
| LT-S8328XGP-4XS24GT-S | STC-424XGGPM-280W | 1010 | $181.2 | $188.7 | $196.3 | $198.0 |
| LT-S8328XG-4XS24GT-S | STC-424XGGM | 710 | $127.4 | $132.7 | $138.0 | $143.0 |
| LT-S8328G-4GX24GT-S | STC-424DGGM | 460 | $82.5 | $85.9 | $89.4 | $110.0 |
| LT-IS3010GP-2GX8GT | STI-288GP | 320 | $57.4 | $59.8 | $62.2 | $74.8 |
| LT-IS6310GP-2GX8GT | STI-288DGGPM | 780 | $139.9 | $145.7 | $151.6 | $137.5 |
| LT-IS6312XGP-4XS8GT | STI-488XGGPM | 920 | $165.0 | $171.9 | $178.8 | $269.5 |
| LT-IS6318GP-2GX16GT | STI-21616DGGPM | 1340 | $240.4 | $250.4 | $260.4 | $242.0 |
| LT-IS6328XGP-4XS24GT | STI-42424XGGPM | 2200 | $394.6 | $411.1 | $427.5 | $423.5 |

## 全表

| SmartByte 型号 | 规格摘要 | CNY | +20% | +25% | +30% | Saga 对应型号 | Saga 列表价 | 档位/备注 | 对照说明 |
|---|---|---:|---:|---:|---:|---|---:|---|---|
| **Layer 2 Managed  Industrial Ethernet Switches Full Gigabit Series** |  |  |  |  |  |  |  |  |  |
| LT-IS3206F-2FX4TX | ● 4*10/100Base-T RJ45 ports, 1*100Base-X SFP ports / ● DC 12~58V input | 280 | $50.2 | $52.3 | $54.4 | STI-240FM | $55.0 | L2 | 4×FE + 2×100M SFP，L2 管理 |
| LT-IS3206FP-2FX4TX | PoE 衍生型（同主型规格 + PoE） | 320 | $57.4 | $59.8 | $62.2 | STI-244FPM | $66.0 | L2 | 4×FE PoE + 2×100M SFP，L2 管理，120W |
| LT-IS3206G-2GX4GT | ● 4*10/100/1000Base-T RJ45 ports, 2*100/1000Base-X SFP ports / ● DC 12 | 320 | $57.4 | $59.8 | $62.2 | STI-240GM | $66.0 | L2 | 4×GE + 2×1G SFP，L2 管理 |
| LT-IS3206GP-2GX4GT | PoE 衍生型（同主型规格 + PoE） | 360 | $64.6 | $67.3 | $70.0 | STI-244GPM | $77.0 | L2 | 4×GE PoE + 2×1G SFP，L2 管理，120W |
| LT-IS3210G-2GX8GT | ● 8*10/100/1000Base-T RJ45 ports, 2*1000/2500Base-X SFP ports / ● DC 1 | 380 | $68.2 | $71.0 | $73.8 | STI-280GM | $77.0 | L2 | 8×GE + 2×SFP，L2 管理（SmartByte 标 2.5G SFP，Saga 标 1G SFP——核对） |
| LT-IS3210GP-2GX8T | PoE 衍生型（同主型规格 + PoE） | 440 | $78.9 | $82.2 | $85.5 | STI-288GPM | $88.0 | L2 | 8×GE PoE + 2×SFP，L2 管理，240W |
| **Layer 2+ Managed  Industrial Ethernet Switches Full Gigabit Series** |  |  |  |  |  |  |  |  |  |
| LT-IS6306G-2GX4GT | ● 4*10/100/1000Base-T RJ45 ports, 2*1G/2.5GBase-X SFP ports / ● DC 12~ | 660 | $118.4 | $123.3 | $128.3 | STI-240DGGM | $110.0 | L2+ | 4×GE + 2×1G/2.5G SFP，L2+ |
| LT-IS6306GP-2GX4GT | PoE 衍生型（同主型规格 + PoE） | 720 | $129.1 | $134.5 | $139.9 | STI-244DGGPM | $121.0 | L2+ | 4×GE PoE + 2×1G/2.5G SFP，L2+，120W |
| LT-IS6306GP-2GX4GT-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 820 | $147.1 | $153.2 | $159.3 | STI-244DGGPM-2BT | $143.0 | L2+ | 4×GE PoE（2 口 bt）+ 2×2.5G SFP，L2+，240W |
| LT-IS6310G-2GX8GT | ●8*10/100/1000Base-T RJ45 ports, 2*1G/2.5GBase-X SFP slots / ● DC 12~5 | 700 | $125.6 | $130.8 | $136.0 | STI-280DGGM | $121.0 | L2+ | 8×GE + 2×1G/2.5G SFP，L2+ |
| LT-IS6310GP-2GX8GT | PoE 衍生型（同主型规格 + PoE） | 780 | $139.9 | $145.7 | $151.6 | STI-288DGGPM | $137.5 | L2+ | 8×GE PoE + 2×1G/2.5G SFP，L2+，240W |
| LT-IS6310GP-2GX8GT-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 880 | $157.8 | $164.4 | $171.0 | STI-288DGGPM-2BT | $154.0 | L2+ | 8×GE PoE（2 口 bt）+ 2×2.5G SFP，L2+，240W |
| LT-IS6312G-4GX8GT | ●8*10/100/1000Base-T RJ45 ports, 4*1G/2.5GBase-X SFP slots / ● DC 12~5 | 740 | $132.7 | $138.3 | $143.8 | STI-480DGGM | $132.0 | L2+ | 8×GE + 4×1G/2.5G SFP，L2+ |
| LT-IS6312GP-4GX8GT | PoE 衍生型（同主型规格 + PoE） | 820 | $147.1 | $153.2 | $159.3 | STI-488DGGPM | $148.5 | L2+ | 8×GE PoE + 4×1G/2.5G SFP，L2+，240W |
| LT-IS6312GP-4GX8GT-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 920 | $165.0 | $171.9 | $178.8 | STI-488DGGPM-2BT | $165.0 | L2+ | 8×GE PoE（2 口 bt）+ 4×2.5G SFP，L2+，240W |
| LT-IS6316G-8GX8GT | ●8*10/100/1000Base-T RJ45 ports, 4*100/1000M SFP, 4*1G/2.5G SFP / ● DC | 1100 | $197.3 | $205.5 | $213.8 | STI-448DGGGM | $220.0 | L2+ | 8×GE + 4×1G SFP + 4×2.5G SFP，L2+（SmartByte 备注 AC5 停产可出 AC3） |
| LT-IS6316GP-8GX8GT | PoE 衍生型（同主型规格 + PoE） | 1180 | $211.7 | $220.5 | $229.3 | STI-448DGGGPM | $236.5 | L2+ | 8×GE PoE + 4×1G SFP + 4×2.5G SFP，L2+，240W |
| LT-IS6318G-2GX16GT | ●16*10/100/1000Base-T RJ45 ports, 2*1G/2.5GBase-X SFP slots / ● DC 12~ | 1180 | $211.7 | $220.5 | $229.3 | STI-2160DGGM | $220.0 | L2+ | 16×GE + 2×1G/2.5G SFP，L2+ |
| LT-IS6318GP-2GX16GT | PoE 衍生型（同主型规格 + PoE） | 1340 | $240.4 | $250.4 | $260.4 | STI-21616DGGPM | $242.0 | L2+ | 16×GE PoE + 2×1G/2.5G SFP，L2+，240W |
| LT-IS6320G-4GX16GT-D | ●16*10/100/1000Base-T RJ45 ports, 4*1G/2.5GBase-X SFP slots ,DI/DO/RS4 | 1560 | $279.8 | $291.5 | $303.1 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 16×GE + 4×2.5G SFP + DI/DO/RS485：Saga 无 4×2.5G 上联的 16 口型（就近 STI-2160DGGM 为 2×SFP）——沿用 SmartByte 型号并注明 |
| LT-IS6320GP-4GX16GT-D | PoE 衍生型（同主型规格 + PoE） | 1760 | $315.7 | $328.8 | $342.0 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 16×GE PoE + 4×2.5G SFP + DI/DO：Saga 暂无对应——沿用 SmartByte 型号并注明 |
| LT-IS6320GP-4GX16GT-D-4BT | PoE++ 衍生型 | 1960 | $351.6 | $366.2 | $380.9 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 16×GE PoE（4 口 bt）+ 4×2.5G SFP + DI/DO：Saga 暂无对应——沿用 SmartByte 型号并注明 |
| LT-IS6328G-4GX24GT-D | ●24*10/100/1000Base-T RJ45 ports, 4*1G/2.5GBase-X SFP slots,DI/DO/RS48 | 1660 | $297.8 | $310.2 | $322.6 | STI-4240DGGM | $330.0 | L2+ | 24×GE + 4×1G/2.5G SFP，L2+，DIN |
| LT-IS6328GP-4GX24GT | PoE 衍生型（同主型规格 + PoE） | 1900 | $340.8 | $355.0 | $369.2 | STI-42424DGGPM | $363.0 | L2+ | 24×GE PoE + 4×1G/2.5G SFP，L2+，DIN |
| LT-IS6228GP-4GX24GT-4BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2100 | $376.7 | $392.4 | $408.1 | STI-42424DGGPM-4BT | $407.0 | L2+ | 24×GE PoE（4 口 bt）+ 4×2.5G SFP，L2+，DIN（SmartByte 表内型号疑为 LT-IS6328GP-4GX24GT-4BT 之笔误——报价前核对） |
| LT-IS6328G-4GX24GT-U-D | ●24*10/100/1000Base-T RJ45 ports, 4*1G/2.5GBase-X SFP slots / ● AC/DC  | 1800 | $322.9 | $336.3 | $349.8 | STI-4240DGGM-U | $363.0 | L2+ | 24×GE + 4×1G/2.5G SFP，L2+，1U 机架 AC |
| LT-IS6328GP-4GX24GT-U | PoE 衍生型（同主型规格 + PoE） | 2100 | $376.7 | $392.4 | $408.1 | STI-42424DGGPM-U | $407.0 | L2+ | 24×GE PoE + 4×1G/2.5G SFP，L2+，1U 机架，370W |
| LT-IS6328GP-4GX24GT-U-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2200 | $394.6 | $411.1 | $427.5 | STI-42424DGGPM-U-2BT | $440.0 | L2+ | 24×GE PoE（2 口 bt）+ 4×2.5G SFP，L2+，1U 机架 370W |
| LT-IS6328G-20GX8GC-D | ●16*100/1000Base-X SFP slots, 8*1000Base Combo, 4*1G/2.5G SFP slots /  | 2350 | $421.5 | $439.1 | $456.7 | STI-4168DGGCM-U | $467.5 | L2+ | 16×SFP + 8×Combo + 4×2.5G SFP，L2+（Saga 为机架 AC 型，SmartByte 为 -D 型——核对形态） |
| **Layer 2+ Managed  Industrial Ethernet Switches with 10G Uplink Series** |  |  |  |  |  |  |  |  |  |
| LT-IS6312XG-4XS8GT | ●8*10/100/1000Base-T RJ45 ports, 4*1G/2.5G/10GBase-X SFP+ slots / ● DC | 840 | $150.7 | $157.0 | $163.2 | STI-480XGGM | $253.0 | L2+ | 8×GE + 4×10G SFP+，L2+ |
| LT-IS6312XGP-4XS8GT | PoE 衍生型（同主型规格 + PoE） | 920 | $165.0 | $171.9 | $178.8 | STI-488XGGPM | $269.5 | L2+ | 8×GE PoE + 4×10G SFP+，L2+，240W |
| LT-IS6312XGP-4XS8GT-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 1020 | $183.0 | $190.6 | $198.2 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 8×GE PoE（2 口 bt）+ 4×10G：Saga 无 bt + 4×10G 组合（就近 STI-288DGGPM-2BT 为 2×2.5G 上联）——沿用 SmartByte 型号并注明 |
| LT-IS6316XG-4XS4GX8GT | ●8*10/100/1000Base-T RJ45 ports, 4*1000Base-X SFP, 4*1G/2.5G/10GBase-X | 1400 | $251.1 | $261.6 | $272.0 | STI-448XGGGM | $275.0 | L2+（另有 L3 档） | 8×GE + 4×1G SFP + 4×10G SFP+，L2+ 档（L3 档 $363） |
| LT-IS6316XGP-4XS4GX8GT | PoE 衍生型（同主型规格 + PoE） | 1480 | $265.5 | $276.5 | $287.6 | STI-448XGGGPM | $297.0 | L2+（另有 L3 档） | 8×GE PoE + 4×1G SFP + 4×10G，L2+，240W（L3 档 $385） |
| LT-IS6318XG-2XS16GT | ●16*10/100/1000Base-T RJ45 ports, 2*1G/2.5G/10GBase-X SFP+ slots / ● D | 1500 | $269.1 | $280.3 | $291.5 | STI-2160XGGM | $291.5 | L2+（另有 L3 档） | 16×GE + 2×10G SFP+，L2+ 档（L3 档 $385） |
| LT-IS6318XGP-2XS16GT | PoE 衍生型（同主型规格 + PoE） | 1660 | $297.8 | $310.2 | $322.6 | STI-21616XGGPM | $324.5 | L2+（另有 L3 档） | 16×GE PoE + 2×10G SFP+，L2+，240W（L3 档 $412.5） |
| LT-IS6320XG-4XS8GX8GT-D | ●8*10/100/1000Base-T RJ45 ports, 8*100/1000Base-X SFP, 4*1G/2.5G/10GBa | 1780 | $319.3 | $332.6 | $345.9 | STI-488DGGGM | $352.0 | L2+ | 8×GE + 8×SFP + 4×上联：Saga STI-488DGGGM 上联为 2.5G 非 10G——10G 上联刚需时沿用 SmartByte 并注明 |
| LT-IS6328XG-4XS24GT-D | ●24*10/100/1000Base-T RJ45 ports, 4*1G/2.5G/10GBase-X SFP+ slots / ● D | 1960 | $351.6 | $366.2 | $380.9 | STI-4240XGGM | $385.0 | L2+（另有 L3 档） | 24×GE + 4×10G SFP+，L2+ 档（L3 档 $478.5），DIN |
| LT-IS6328XGP-4XS24GT | PoE 衍生型（同主型规格 + PoE） | 2200 | $394.6 | $411.1 | $427.5 | STI-42424XGGPM | $423.5 | L2+（另有 L3 档） | 24×GE PoE + 4×10G SFP+，L2+ 档（L3 档 $517），DIN |
| LT-IS6328XGP-4XS24GT-4BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2400 | $430.5 | $448.4 | $466.4 | STI-42424XGGPM-4BT | $456.5 | L2+（另有 L3 档） | 24×GE PoE（4 口 bt）+ 4×10G，L2+ 档（L3 档 $550） |
| LT-IS6328XG-4XS24GT-U-D | ●24*10/100/1000Base-T RJ45 ports, 4*1G/2.5G/10GBase-X SFP slots / ● AC | 2100 | $376.7 | $392.4 | $408.1 | STI-4240XGGM-U | $412.5 | L2+（另有 L3 档） | 24×GE + 4×10G SFP+，L2+ 档（L3 档 $506），1U 机架 |
| LT-IS6328XGP-4XS24GT-U | PoE 衍生型（同主型规格 + PoE） | 2400 | $430.5 | $448.4 | $466.4 | STI-42424XGGPM-U | $451.0 | L2+（另有 L3 档） | 24×GE PoE + 4×10G SFP+，L2+ 档（L3 档 $550），1U 机架 370W |
| LT-IS6328XGP-4XS24GT-U-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2500 | $448.4 | $467.1 | $485.8 | STI-42424XGGPM-U-2BT | $484.0 | L2+（另有 L3 档） | 24×GE PoE（2 口 bt）+ 4×10G，1U 机架，L2+ 档（L3 档 $583） |
| LT-IS6328XG-4XS16GX8GC-D | ●16*100/1000Base-X SFP slots, 8*1000Base Combo, 4*1G/2.5G/10G Base-X S | 2650 | $475.3 | $495.1 | $514.9 | STI-4168XGGCM-U | $511.5 | L2+（另有 L3 档） | 16×SFP + 8×Combo + 4×10G，L2+ 档（L3 档 $605）；Saga 为机架型 |
| **L3 Managed Industrial Ethernet Switch with 10G uplink series** |  |  |  |  |  |  |  |  |  |
| LT-IS6516XG-4XS4GX8GT | Industrial L3,  8*10/100/1000Base-T RJ45,4*100/1000Base-X SFP, 4*1G/2. | 1900 | $340.8 | $355.0 | $369.2 | STI-448XGGGM(L3) | $363.0 | L3 | 工业 L3：8×GE + 4×1G SFP + 4×10G |
| LT-IS6516XGP-4XS4GX8GT | PoE 衍生型（同主型规格 + PoE） | 1980 | $355.2 | $370.0 | $384.8 | STI-448XGGGPM(L3) | $385.0 | L3 | 工业 L3 PoE：8×GE PoE + 4×1G SFP + 4×10G |
| LT-IS6518XG-2XS16GT | Industrial L3,  16*10/100/1000Base-T RJ45, 2*1G/2.5G/10G SFP+ | 2000 | $358.7 | $373.7 | $388.6 | STI-2160XGGM(L3) | $385.0 | L3 | 工业 L3：16×GE + 2×10G |
| LT-IS6518XGP-2XS16GT | PoE 衍生型（同主型规格 + PoE） | 2160 | $387.4 | $403.6 | $419.7 | STI-21616XGGPM(L3) | $412.5 | L3 | 工业 L3 PoE：16×GE PoE + 2×10G |
| LT-IS6520XG-4XS8GX8GT | Industrial L3,  8*10/100/1000Base-T RJ45, 8*100/1000Base-X SFP, 4*1G/2 | 2280 | $409.0 | $426.0 | $443.0 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 工业 L3：8×GE + 8×SFP + 4×10G——Saga L3 档无此端口组合，沿用 SmartByte 并注明 |
| LT-IS6520XG-4XS16GT | Industrial L3,  16*10/100/1000Base-T RJ45, 4*1G/2.5G/10G SFP+ | 2350 | $421.5 | $439.1 | $456.7 | STI-4160XGGM | $462.0 | L3 | 工业 L3：16×GE + 4×10G |
| LT-IS6520XGP-4XS16GT | PoE 衍生型（同主型规格 + PoE） | 2510 | $450.2 | $469.0 | $487.7 | STI-41616XGGPM | $495.0 | L3 | 工业 L3 PoE：16×GE PoE + 4×10G |
| LT-IS6520XGP-4XS16GT-4BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2710 | $486.1 | $506.4 | $526.6 | STI-41616XGGPM-4BT | $528.0 | L3 | 工业 L3 PoE（4 口 bt）：16×GE + 4×10G（Saga 该型为 1U 机架 AC——核对形态） |
| LT-IS6528XG-4XS24GT | Industrial L3,  24*10/100/1000Base-T RJ45, 4*1G/2.5G/10G SFP+ | 2460 | $441.3 | $459.6 | $478.0 | STI-4240XGGM(L3) | $478.5 | L3 | 工业 L3：24×GE + 4×10G，DIN |
| LT-IS6528XGP-4XS24GT | PoE 衍生型（同主型规格 + PoE） | 2700 | $484.3 | $504.5 | $524.7 | STI-42424XGGPM(L3) | $517.0 | L3 | 工业 L3 PoE：24×GE PoE + 4×10G，DIN |
| LT-IS6528XGP-4XS24GT-4BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 2900 | $520.2 | $541.9 | $563.5 | STI-42424XGGPM-4BT(L3) | $550.0 | L3 | 工业 L3 PoE（4 口 bt）：24×GE + 4×10G |
| LT-IS6528XG-4XS24GT-U | Industrial L3,  24*10/100/1000Base-T RJ45, 4*1G/2.5G/10G SFP+, rack-mo | 2600 | $466.4 | $485.8 | $505.2 | STI-4240XGGM-U(L3) | $506.0 | L3 | 工业 L3：24×GE + 4×10G，1U 机架 |
| LT-IS6528XGP-4XS24GT-U | PoE 衍生型（同主型规格 + PoE） | 2900 | $520.2 | $541.9 | $563.5 | STI-42424XGGPM-U(L3) | $550.0 | L3 | 工业 L3 PoE：24×GE PoE + 4×10G，1U 机架 |
| LT-IS6528XGP-4XS24GT-U-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 3000 | $538.1 | $560.5 | $583.0 | STI-42424XGGPM-U-2BT(L3) | $583.0 | L3 | 工业 L3 PoE（2 口 bt）：24×GE + 4×10G，1U 机架 |
| LT-IS6528XG-4XS16GT8GC-U | Industrial L3,  16*10/100/1000Base-T RJ45, 8*gigabit Combo, 4*1G/2.5G/ | 2900 | $520.2 | $541.9 | $563.5 | STI-4816XGCGM-U | $572.0 | L3 | 工业 L3：16×GE + 8×Combo + 4×10G，1U 机架 |
| LT-IS6528XGP-4XS16GT8GC-U | PoE 衍生型（同主型规格 + PoE） | 3060 | $548.9 | $571.7 | $594.6 | STI-4816XGCGPM-U | $605.0 | L3 | 工业 L3 PoE：16×GE PoE + 8×Combo + 4×10G，1U 机架 |
| LT-IS6528XGP-4XS16GT8GC-U-2BT | PoE++ 衍生型（1–2/1–4 口 bt 60–90W） | 3160 | $566.8 | $590.4 | $614.1 | STI-4816XGCGPM-U-2BT | $638.0 | L3 | 工业 L3 PoE（2 口 bt）：16×GE + 8×Combo + 4×10G |
| LT-IS6528XG-4XS16GX8GC-U | Industrial L3,  16*100/1000Base-X SFP, 8*gigabit Combo, 4*1G/2.5G/10G  | 3100 | $556.1 | $579.2 | $602.4 | STI-4168XGGCM-U(L3) | $605.0 | L3 | 工业 L3：16×SFP + 8×Combo + 4×10G，1U 机架 |
| LT-IS6552XG-4XS48GT-U | Industrial L3,  48*10/100/1000Base-T RJ45, 4*1G/2.5G/10G SFP+, rack-mo | 4500 | $807.2 | $840.8 | $874.4 | STI-4480XGGM-U | $847.0 | L3 | 工业 L3：48×GE + 4×10G，1U 机架（SmartByte 标已停产——报价前确认） |
| **Layer 3 Managed Ethernet Switches, 10G uplink series  (Supports static and dynam** |  |  |  |  |  |  |  |  |  |
| LT-S8528XG-4XS24GT | 4*10G/2.5G/1G SFP+ ports ，24*10/100/1000M RJ45 ports, without SFP modu | 1500 | $269.1 | $280.3 | $291.5 | STC-424XGGM(L3) | $295.0 | L3 | 24×GE + 4×10G SFP+，L3；Saga PDF 中 L3 档与 L2+ 档同型号名、不同价 |
| LT-S8528XGP-4XS24GT | 4*10G/2.5G/1G SFP+ ports ，24*10/100/1000M RJ45 ports, without SFP modu | 1900 | $340.8 | $355.0 | $369.2 | STC-424XGGPM(L3) | $374.0 | L3 | 24×GE PoE + 4×10G SFP+，440W，L3 |
| LT-IS8528XG-4XS16GT8GC | 4*10G/2.5G/1G SFP+ slots，16*10/100/1000M RJ45 ports，8*GE COMBO ports,  | 1600 | $287.0 | $299.0 | $310.9 | STC-4816XGCGM | $353.0 | L3 | 16×GE + 8×Combo + 4×10G，L3（SmartByte 备注 AC5 停产，可用原价出 AC3） |
| LT-IS8528XGP-4XS16GT8GC | 4*10G/2.5G/1G SFP+ slots，16*10/100/1000M RJ45 ports，8*GE COMBO ports,  | 2000 | $358.7 | $373.7 | $388.6 | STC-4816XGCGPM | $611.0 | L3 | 16×GE PoE + 8×Combo + 4×10G，L3，440W |
| LT-S8528XG-4XS16GX8GC | 4*10G/2.5G/1G SFP+ slots，16*1G SFP ports，8*GE COMBO ports, without SFP | 2100 | $376.7 | $392.4 | $408.1 | STC-4168XGGCM | $413.0 | L3 | 16×1G SFP + 8×Combo + 4×10G，L3 |
| LT-S8552XG-4XS48GT | 4*10G/2.5G/1G SFP+ ports ，48*10/100/1000M RJ45 ports, without SFP modu | 2600 | $466.4 | $485.8 | $505.2 | STC-448XGGM(L3) | $512.0 | L3 | 48×GE + 4×10G SFP+，L3 |
| LT-S8552XGP-4XS48GT | 4*10G/2.5G/1G SFP+ ports ，48*10/100/1000M RJ45 ports, without SFP modu | 3100 | $556.1 | $579.2 | $602.4 | STC-448XGGPM(L3) | $583.0 | L3 | 48×GE PoE + 4×10G SFP+，L3，440W |
| LT-S8552XG-4XS48GX | 4*1G/2.5G/10G SFP+ ports ，48*1G SFP ports, without SFP module,  Layer  | 3500 | $627.8 | $654.0 | $680.1 | STC-448XGGMO | $688.0 | L3 | 48×1G SFP + 4×10G SFP+，L3（全光） |
| **Layer 2+ Managed Ethernet Switch Non-PoE/PoE Series(Support DHCP server, IPv4/IP** |  |  |  |  |  |  |  |  |  |
| LT-S8310G-2GX8GT | L2+,  8*10/100/1000Base-T + 4*1G/2.5G SFP | 380 | $68.2 | $71.0 | $73.8 | STC-28DGGM | $85.0 | L2+ | 8×GE + 2×1G/2.5G SFP，L2+；SmartByte 备注：成本回落前暂停出货 |
| LT-S8310GP-2GX8GT | L2+, 8*10/100/1000Base-T PoE + 4*1G/2.5G SFP, 120W  power supply | 450 | $80.7 | $84.1 | $87.4 | STC-28DGGPM | $99.0 | L2+ | 8×GE PoE + 2×1G/2.5G SFP，L2+；Saga 标 240W 预算，SmartByte 标 120W 电源——报价前核对电源规格 |
| LT-S8328G-4GX24GT-S | L2 +, 24*10/100/1000Base-T + 4*1G/2.5G SFP, AC5爆款 | 460 | $82.5 | $85.9 | $89.4 | STC-424DGGM | $110.0 | L2+ | 24×GE + 4×1G/2.5G SFP，L2+（AC5 爆款） |
| LT-S8328GP-4GX24GT-S | L2 +, 24*10/100/1000Base-T PoE + 4*1G/2.5G SFP, AC5爆款,280W power suppl | 750 | $134.5 | $140.1 | $145.7 | STC-424DGGPM-280W | $165.0 | L2+ | 24×GE PoE + 4×1G/2.5G SFP，280W，L2+ |
| LT-S8328GP-4GX24GT | L2 +, 24*10/100/1000Base-T PoE + 4*1G/2.5G SFP,440W power supply | 1200 | $215.2 | $224.2 | $233.2 | STC-424DGGPM-440W | $220.0 | L2+ | 24×GE PoE + 4×1G/2.5G SFP，440W，L2+ |
| LT-S8328XG-4XS24GT-S | L2 +, 24*10/100/1000Base-T PoE + 4*1G/2.5G/10G SFP+, AC5 爆款 | 710 | $127.4 | $132.7 | $138.0 | STC-424XGGM | $143.0 | L2+（另有 L3 档） | 24×GE + 4×10G SFP+，L2+ 档（Saga 同型号另有 L3 档 $295） |
| LT-S8328XGP-4XS24GT-S | L2 +, 24*10/100/1000Base-T PoE + 4*1G/2.5G/10G SFP+, AC5爆款,280W power  | 1010 | $181.2 | $188.7 | $196.3 | STC-424XGGPM-280W | $198.0 | L2+ | 24×GE PoE + 4×10G SFP+，280W，L2+（用户 R61 口径：对外 $180/台） |
| LT-S8352G-4GX48GT | L2+, 48*10/100/1000Base-T + 4*1G/2.5G SFP | 1320 | $236.8 | $246.6 | $256.5 | STC-448DGGM | $220.0 | L2+ | 48×GE + 4×1G/2.5G SFP，L2+ |
| LT-S8352GP-4GX48GT | L2+, 48*10/100/1000Base-T PoE+ 4*1G/2.5G SFP, 440W power supply; 850W  | 1720 | $308.5 | $321.4 | $334.2 | STC-448DGGPM | $308.0 | L2+ | 48×GE PoE + 4×1G/2.5G SFP，440W，L2+ |
| LT-S8352XG-4XS48GT | L2+, 48*10/100/1000Base-T + 4*1G/2.5G SFP | 1470 | $263.7 | $274.7 | $285.7 | STC-448XGGM | $286.0 | L2+（另有 L3 档） | 48×GE + 4×10G SFP+，L2+ 档（Saga 同型号另有 L3 档 $512） |
| LT-S8352XGP-4XS48GT | L2+, 48*10/100/1000Base-T PoE+ 4*1G/2.5G/10G SFP+, 440W power supply;  | 1870 | $335.4 | $349.4 | $363.4 | STC-448XGGPM | $369.0 | L2+（另有 L3 档） | 48×GE PoE + 4×10G SFP+，440W，L2+ 档（L3 档 $583） |
| **Unmanaged Ultra-compact Industrial Fast Media Converters(PoE/Non-PoE)** |  |  |  |  |  |  |  |  |  |
| LT-IMC30F-E | ● 1*10/100Base-TX RJ45 port, 1*100Base-FX SFP(/SC/ST/FC optional) fibe | 110 | $19.7 | $20.6 | $21.4 | STI-110FE | $23.1 |  | 1×FE + 1×100M SFP |
| LT-IMC30FP-E | ● 1*10/100Base-TX RJ45 PoE/PoE+ port, 1*100Base-FX SFP(/SC/ST/FC optio | 140 | $25.1 | $26.2 | $27.2 | STI-111FP | $29.7 |  | 1×FE PoE + 1×100M SFP |
| LT-IMC30F-1FX2TX-E | ● 2*10/100Base-TX RJ45 port, 1*100Base-FX SFP(/SC/ST/FC optional) fibe | 120 | $21.5 | $22.4 | $23.3 | STI-120FE | $26.4 |  | 2×FE + 1×100M SFP |
| LT-IMC30FP-1FX2TX-E | ● 2*10/100Base-TX RJ45 PoE/PoE+ port, 1*100Base-FX SFP(/SC/ST/FC optio | 150 | $26.9 | $28.0 | $29.1 | STI-122FP | $33.0 |  | 2×FE PoE + 1×100M SFP |
| LT-IMC30F-2FX2TX-E | ● 2*10/100Base-TX RJ45 port, 2*100Base-FX SFP port / ● DC 12~58V input | 140 | $25.1 | $26.2 | $27.2 | STI-220FE | $29.7 |  | 2×FE + 2×100M SFP |
| LT-IMC30FP-2FX2TX-E | ● 2*10/100Base-TX RJ45 PoE/PoE+ port, 2*100Base-FX SFP port / ● DC 44~ | 170 | $30.5 | $31.8 | $33.0 | STI-222FP | $36.3 |  | 2×FE PoE + 2×100M SFP |
| **Unmanaged Ultra-compact Industrial Gigabit Media Converters(PoE/Non-PoE)** |  |  |  |  |  |  |  |  |  |
| LT-IMC30G-E | ●1*10/100/1000Base-T RJ45 port, 1*100/1000Base-X SFP(/SC/ST/FC optiona | 125 | $22.4 | $23.4 | $24.3 | STI-110GE | $29.7 |  | 1×GE + 1×1G SFP |
| LT-IMC30GP-E | ● 1*10/100/1000Base-T RJ45 PoE/PoE+  port, 1*100/1000Base-X SFP(/SC/ST | 155 | $27.8 | $29.0 | $30.1 | STI-111GP | $36.3 |  | 1×GE PoE + 1×1G SFP |
| LT-IMC30G-1GX2GT-E | ● 2*10/100/1000Base-T RJ45 ports, 1*100/1000Base-X SFP(/SC/ST/FC optio | 135 | $24.2 | $25.2 | $26.2 | STI-120GE | $29.7 |  | 2×GE + 1×1G SFP |
| LT-IMC30GP-1GX2GT-E | ● 2*10/100/1000Base-T RJ45 PoE/PoE+ ports, 1*100/1000Base-X SFP(/SC/ST | 165 | $29.6 | $30.8 | $32.1 | STI-122GP | $36.3 |  | 2×GE PoE + 1×1G SFP |
| LT-IMC30G-2GX2GT-E | ● 2*2*10/100/1000Base-T RJ45 ports, 2*100/1000Base-X SFP ports / ● DC  | 155 | $27.8 | $29.0 | $30.1 | STI-220GE | $36.3 |  | 2×GE + 2×1G SFP |
| LT-IMC30GP-2GX2GT-E | ● 2*10/100/1000Base-T RJ45 PoE ports, 2*100/1000Base-X SFP ports / ● D | 185 | $33.2 | $34.6 | $35.9 | STI-222GP | $39.6 |  | 2×GE PoE + 2×1G SFP |
| **Unmanaged Industrial Ethernet Switches** |  |  |  |  |  |  |  |  |  |
| LT-IS3005F-1FX4TX | ● 4*10/100Base-TX RJ45 ports, 1*100Base-FX SFP(/SC/ST/FC optional) fib | 130 | $23.3 | $24.3 | $25.3 | STI-140FE | $29.7 |  | 4×FE + 1×100M SFP |
| LT-IS3005F-5TX-M | ● 5*10/100Base-TX RJ45 ports / ● DC 12~36V input, redundant power supp | 85 | $15.2 | $15.9 | $16.5 | STI-050FE | $27.5 |  | 5×FE（Saga 为 DC12-58V；SmartByte -M 为 12-36V——核对） |
| LT-IS3005F-5TX-E | ● 5*10/100Base-TX RJ45 ports（NO.5 is the uplink port) / ● DC 12~58V in | 122 | $21.9 | $22.8 | $23.7 | STI-050FE | $27.5 |  | 5×FE |
| LT-IS3006F-2FX4TX | ● 4*10/100Base-TX RJ45 ports, 2*100Base-FX SFP fiber ports / ● DC 12~5 | 140 | $25.1 | $26.2 | $27.2 | STI-240FE | $33.0 |  | 4×FE + 2×100M SFP |
| LT-IS3008F-8TX | ● 8*10/100M RJ45 ports(No.8 is uplink port) / ● DC 12~58V input, redun | 136 | $24.4 | $25.4 | $26.4 | STI-080FE | $44.0 |  | 8×FE |
| LT-IS3009F-1FX8TX | ● 8*10/100Base-TX RJ45 ports, 1*100Base-FX SFP(/SC/ST/FC optional) fib | 155 | $27.8 | $29.0 | $30.1 | STI-180FE | $48.4 |  | 8×FE + 1×100M SFP |
| LT-IS3005G-5GT-M | ● 5*10/100/1000Base-TX RJ45 ports / ● DC 12~36V input, redundant power | 95 | $17.0 | $17.8 | $18.5 | STI-050GE | $34.1 |  | 5×GE（电压范围核对） |
| LT-IS3005G-5GT | ● 4*10/100/1000Base-T RJ45 ports downlink, 1*10/100/1000Base-T RJ45 po | 134 | $24.0 | $25.0 | $26.0 | STI-050GE | $34.1 |  | 5×GE |
| LT-IS3005G-1GX4GT | ● 4*10/100/1000M RJ45 ports, 1*1000Base-X SFP(/SC/ST/FC optional) fibe | 150 | $26.9 | $28.0 | $29.1 | STI-140GE | $37.4 |  | 4×GE + 1×1G SFP |
| LT-IS3006G-1GT1GX4GT | ● 4*10/100/1000M RJ45 ports downlink, 1*1000Base-X SFP port and 1*10/1 | 170 | $30.5 | $31.8 | $33.0 | STI-150GE | $42.9 |  | 5×GE + 1×1G SFP |
| LT-IS3006G-2GX4GT | ● 4*10/100/1000M RJ45 ports, 2*1000Base-X SFP fiber ports / ● DC 12~58 | 156 | $28.0 | $29.1 | $30.3 | STI-240GE | $40.7 |  | 4×GE + 2×1G SFP |
| LT-IS3008G-8GT | ● 8*10/100/1000M RJ45 ports(No.8 is uplink port) / ● DC 12~58V input,  | 175 | $31.4 | $32.7 | $34.0 | STI-080GE | $55.0 |  | 8×GE |
| LT-IS3010G-2GX8GT | ●8*10/100/1000M RJ45 ports, 2*1000Base-X SFP (/SC/ST/FC optional) fibe | 260 | $46.6 | $48.6 | $50.5 | STI-280GE | $63.8 |  | 8×GE + 2×1G SFP |
| LT-IS6016G-16GT | ●16*10/100/1000Base-T RJ45 ports / ● Redundant power DC 12-58V input w | 510 | $91.5 | $95.3 | $99.1 | STI-0160GE | $115.5 |  | 16×GE |
| LT-IS6018G-2GX16GT | ●16*10/100/1000Base-T RJ45 ports, 2*1000Base-X SFP slots / ● Redundant | 790 | $141.7 | $147.6 | $153.5 | STI-2160GE | $170.5 |  | 16×GE + 2×1G SFP |
| **Unmanaged Industrial PoE Switches** |  |  |  |  |  |  |  |  |  |
| LT-IS3005FP-1FX4TX | ●4*10/100Base-TX RJ45 PoE ports, 1*100Base-FX SFP(/SC/ST/FC optional)  | 170 | $30.5 | $31.8 | $33.0 | STI-144FP | $37.4 |  | 4×FE PoE + 1×100M SFP |
| LT-IS3005FP-5TX | ●4*10/100Base-TX RJ45 PoE ports downlink , 1*10/100Base-TX RJ45 port u | 162 | $29.1 | $30.3 | $31.5 | STI-054FP | $35.2 |  | 4×FE PoE + 1×FE 上联 |
| LT-IS3006FP-2FX4TX | ● 4*10/100Base-TX RJ45 ports, 2*100Base-FX SFP fiber ports / ● DC 44~5 | 180 | $32.3 | $33.6 | $35.0 | STI-244FP | $40.7 |  | 4×FE PoE + 2×100M SFP |
| LT-IS3008FP-8TX | ● 8*10/100M RJ45 ports(No.8 is uplink port) / ● DC 44~57V input, redun | 196 | $35.2 | $36.6 | $38.1 | STI-088FP | $51.7 |  | 8×FE PoE |
| LT-IS3009FP-1FX8TX | ● 8*10/100Base-TX RJ45 ports, 1*100Base-FX SFP(/SC/ST/FC optional) fib | 215 | $38.6 | $40.2 | $41.8 | STI-188FP | $56.1 |  | 8×FE PoE + 1×100M SFP |
| LT-IS3005GP-5GT | ● 4*10/100/1000Base-T PoE downlink, 1*10/100/1000Base-T RJ45 uplink /  | 174 | $31.2 | $32.5 | $33.8 | STI-054GP | $42.9 |  | 4×GE PoE + 1×GE 上联 |
| LT-IS3005GP-1GX4GT | ● 4*10/100/1000Base-T PoE downlink, 1*1000Base-X SFP uplink / ● DC 44~ | 190 | $34.1 | $35.5 | $36.9 | STI-144GP | $46.2 |  | 4×GE PoE + 1×1G SFP |
| LT-IS3006GP-1GT1GX4GT | ● 4*10/100/1000M RJ45 ports downlink, 1*1000Base-X SFP port and 1*10/1 | 210 | $37.7 | $39.2 | $40.8 | STI-154GP | $51.7 |  | 4×GE PoE + 1×GE + 1×1G SFP |
| LT-IS3006GP-2GX4GT | ● 4*10/100/1000Base-T RJ45 PoE ports, 2*1000Base-X SFP ports / ● DC 44 | 196 | $35.2 | $36.6 | $38.1 | STI-244GP | $49.5 |  | 4×GE PoE + 2×1G SFP |
| LT-IS3008GP-8GT | ● 8*10/100/1000Base-T PoE ports / ● DC 44~57V input, redundant power s | 235 | $42.2 | $43.9 | $45.7 | STI-088GP | $66.0 |  | 8×GE PoE |
| LT-IS3010GP-2GX8GT | ● 8*10/100/1000Base-T RJ45 PoE ports, 2*1000Base-X SFP ports / ● DC 44 | 320 | $57.4 | $59.8 | $62.2 | STI-288GP | $74.8 |  | 8×GE PoE + 2×1G SFP |
| LT-IS6012GP-4GX8GT | ● 8*10/100/1000Base-T RJ45 PoE ports, 4*1000Base-X SFP ports / ● DC 44 | 600 | $107.6 | $112.1 | $116.6 | STI-488GP | $132.0 |  | 8×GE PoE + 4×1G SFP（Saga PDF 规格行写 2 port Fiber，型号名为 488——报价前核对） |
| LT-IS6016GP-16GT | ● 16*10/100/1000Base-T RJ45 PoE/PoE+ ports / ● DC 44~57V input, redund | 670 | $120.2 | $125.2 | $130.2 | STI-01616GP | $143.0 |  | 16×GE PoE |
| LT-IS6018GP-2GX16GT | ● 16*10/100/1000Base-T RJ45 PoE ports, 2*1000Base-X SFP slots / ● DC 4 | 950 | $170.4 | $177.5 | $184.6 | STI-21616GP | $203.5 |  | 16×GE PoE + 2×1G SFP |
| **1 channel single fiber Bypass** |  |  |  |  |  |  |  |  |  |
| LT-IS6312G-4GX8GT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 por | 960 | $172.2 | $179.4 | $186.5 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| LT-IS6312GP-4GX8GT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE | 1040 | $186.5 | $194.3 | $202.1 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| LT-IS6312GP-4GX8GT-2BT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE | 1140 | $204.5 | $213.0 | $221.5 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| LT-IS6312XG-4XS8GT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 por | 1160 | $208.1 | $216.7 | $225.4 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| LT-IS6312XGP-4XS8GT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE | 1240 | $222.4 | $231.7 | $241.0 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| LT-IS6312XGP-4XS8GT-2BT-FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE | 1340 | $240.4 | $250.4 | $260.4 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| **2 channels single fiber Bypass or 1 channel dual fiber Bypass** |  |  |  |  |  |  |  |  |  |
| LT-IS6312G-4GX8GT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 por | 1260 | $226.0 | $235.4 | $244.8 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| LT-IS6312GP-4GX8GT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE | 1340 | $240.4 | $250.4 | $260.4 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| LT-IS6312GP-4GX8GT-2BT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE | 1440 | $258.3 | $269.1 | $279.8 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| LT-IS6312XG-4XS8GT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 por | 1460 | $261.9 | $272.8 | $283.7 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| LT-IS6312XGP-4XS8GT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE | 1540 | $276.2 | $287.7 | $299.3 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |
| LT-IS6312XGP-4XS8GT-2BT-2FBP | L2+ Managed industrial Bypass switch with 8*10/100/1000Base-T RJ45 PoE | 1640 | $294.2 | $306.4 | $318.7 | （Saga 暂无对应，沿用 SmartByte 型号） | — |  | 光纤 Bypass 系列：Saga 三份价格表均无 Bypass 型号——沿用 SmartByte 型号并注明 |

## Saga PDF 原始列表价（USD EXW，抽取自 3 份 PDF，供对照）

| Saga 型号 | 档 | 列表价 | 规格摘要 |
|---|---|---:|---|
| STC-28DGGM | L2+ | $85.0 | 2*1G/2.5G SFP+8*10/100/1000M RJ45+1*Console Port L2+ managed, DC input(5V~16V), with power |
| STC-28DGGM-U | L2+ | $94.0 | 2*1G/2.5G SFP+8*10/100/1000M RJ45+1*Console Port L2+ managed, AC input, Rack compatible |
| STC-28DGGPM | L2+ | $99.0 | 2*1G/2.5G SFP+8*10/100/1000M RJ45+1*Console Port PoE af/at, 240W budget, L2+ managed, DC52 |
| STC-28DGGPM-U | L2+ | $110.0 | 2*1G/2.5G SFP+8*10/100/1000M RJ45+1*Console Port PoE af/at, 200W budget, L2+ managed, AC i |
| STC-4168XGGCM | L3 | $413.0 | 4*1G/2.5G/10G SFP+16*100/1000M SFP+8*Gigabit SFP/RJ45(Combo ports)+1*USB Port+1*Console Po |
| STC-424DGGM | L2+ | $110.0 | 4*1G/2.5G SFP+24*10/100/1000M RJ45+1*Console Port L2+ managed, AC input, Rack compatible |
| STC-424DGGPM-280W | L2+ | $165.0 | 4*1G/2.5G SFP+24*10/100/1000M RJ45+1*Console Port L2+ managed, PoE af/at, 280W budget, Sup |
| STC-424DGGPM-440W | L2+ | $220.0 | 4*1G/2.5G SFP+24*10/100/1000M RJ45+1*Console Port L2+ managed, PoE af/at, 440W budget, Sup |
| STC-424XGGM | L2+ | $143.0 | 4*1G/2.5G/10G SFP+24*10/100/1000M RJ45+1*Console Port L2+ managed, AC input, Rack compatib |
| STC-424XGGM | L3 | $295.0 | 4*1G/2.5G/10G SFP+24*10/100/1000M RJ45+1*Console Port L3 managed, AC input, Rack compatibl |
| STC-424XGGPM | L3 | $374.0 | 4*1G/2.5G/10G SFP+24*10/100/1000M RJ45+1*Console Port L3 managed, PoE af/at, 440W budget,  |
| STC-424XGGPM-280W | L2+ | $198.0 | 4*1G/2.5G/10G SFP+24*10/100/1000M RJ45+1*Console Port L2+ managed, PoE af/at, 280W budget, |
| STC-424XGGPM-440W | L2+ | $264.0 | 4*1G/2.5G/10G SFP+24*10/100/1000M RJ45+1*Console Port L2+ managed, PoE af/at, 440W budget, |
| STC-448DGGM | L2+ | $220.0 | 4*1G/2.5G SFP+48*10/100/1000M RJ45+1*Console Port L2+ managed, AC input, Rack compatible |
| STC-448DGGPM | L2+ | $308.0 | 4*1G/2.5G SFP+48*10/100/1000M RJ45+1*Console Port L2+ managed, PoE af/at, 440W budget, Sup |
| STC-448XGGM | L2+ | $286.0 | 4*1G/2.5G/10G SFP+48*10/100/1000M RJ45+1*Console Port L2+ managed, AC input, Rack compatib |
| STC-448XGGM | L3 | $512.0 | 4*1G/2.5G/10G SFP+48*10/100/1000M RJ45+1*Console Port L3 managed, AC input, Rack compatibl |
| STC-448XGGMO | L3 | $688.0 | 4*1G/2.5G/10G SFP+48*100/1000M SFP+1*USB Port+1*Console Port L3 managed, AC input, Rack co |
| STC-448XGGPM | L2+ | $369.0 | 4*1G/2.5G/10G SFP+48*10/100/1000M RJ45+1*Console Port L2+ managed, PoE af/at, 440W budget, |
| STC-448XGGPM | L3 | $583.0 | 4*1G/2.5G/10G SFP+48*10/100/1000M RJ45+1*Console Port L3 managed, PoE af/at, 440W budget,  |
| STC-4816XGCGM | L3 | $353.0 | 4*1G/2.5G/10G SFP+8*Gigabit SFP/RJ45(Combo ports)+16*10/100/1000M RJ45+1*USB Port+1*Consol |
| STC-4816XGCGPM | L3 | $611.0 | 4*1G/2.5G/10G SFP+8*Gigabit SFP/RJ45(Combo ports)+16*10/100/1000M RJ45+1*USB Port+1*Consol |
| STC-48DGGM | L2+ | $88.0 | 4*1G/2.5G SFP+8*10/100/1000M RJ45+1*Console Port L2+ managed, DC input(5V~16V), with power |
| STC-48DGGM-U | L2+ | $99.0 | 4*1G/2.5G SFP+8*10/100/1000M RJ45+1*Console Port L2+ managed, AC input, Rack compatible |
| STC-48DGGPM | L2+ | $102.0 | 4*1G/2.5G SFP+8*10/100/1000M RJ45+1*Console Port PoE af/at, 240W budget, L2+ managed, DC52 |
| STC-48DGGPM-U | L2+ | $116.0 | 4*1G/2.5G SFP+8*10/100/1000M RJ45+1*Console Port PoE af/at, 200W budget, L2+ managed, AC i |
| STI-0160GE | — | $115.5 | 16*10/100/1000M Ethernet, DIP function 1. Port isolation; 2. Flow control; 3. QoS; 4. Broa |
| STI-01616GP | — | $143.0 | 16*10/100/1000M PoE, DIP function 1. Link aggregation; 2. 250m long distance; 3. QoS; 4. P |
| STI-050FE | — | $27.5 | 5*10/100M Ethernet, DIP function 1. Port isolation; 2. Flow control; 3. QoS; 4. Broadcast  |
| STI-050GE | — | $34.1 | 5*10/100/1000M Ethernet, DIP function 1. Port isolation; 2. Flow control; 3. QoS; 4. Broad |
| STI-054FP | — | $35.2 | 5*10/100M PoE, DIP function 1. Port isolation; 2. 250m long distance; 3. QoS; 4. PoE watch |
| STI-054GP | — | $42.9 | 4*10/100/1000M PoE + 1*10/100/1000M Ethernet, DIP function 1. Port isolation; 2. 250m long |
| STI-080FE | — | $44.0 | 8*10/100M Ethernet, DIP function 1. Port isolation; 2. Flow control; 3. QoS; 4. Broadcast  |
| STI-080GE | — | $55.0 | 8*10/100/1000M Ethernet, DIP function 1. Port isolation; 2. Flow control; 3. QoS; 4. Broad |
| STI-088FP | — | $51.7 | 8*10/100M PoE, DIP function 1. Port isolation; 2. 250m long distance; 3. QoS; 4. PoE watch |
| STI-088GP | — | $66.0 | 8*10/100/1000M PoE, DIP function 1. Port isolation; 2. 250m long distance; 3. QoS; 4. PoE  |
| STI-110FE | — | $23.1 | 1*10/100M Ethernet + 1 port 100M Fiber, DIP functions 1. LFP; 2. Flow control; 3. Broadcas |
| STI-110GE | — | $29.7 | 1*10/100/1000M Ethernet + 1 port 100/1000M Fiber, DIP function 1. LFP; 2. Flow control; 3. |
| STI-111FP | — | $29.7 | 1*10/100M PoE + 1 port 100M Fiber, PoE af/at Compliant, 30W budget, DIP functions 1. LFP;  |
| STI-111GP | — | $36.3 | 1*10/100/1000M PoE + 1 port 100/1000M Fiber, PoE af/at Compliant, 30W budget, DIP function |
| STI-120FE | — | $26.4 | 2*10/100M Ethernet + 1 port 100M Fiber, DIP functions 1. Port isolation; 2. Flow control;  |
| STI-120GE | — | $29.7 | 2*10/100/1000M Ethernet + 1 port 100/1000M Fiber, DIP function 1. Port isolation; 2. Flow  |
| STI-122FP | — | $33.0 | 2*10/100M PoE + 1 port 100M Fiber, PoE af/at Compliant, 60W budget, DIP functions 1. Port  |
| STI-122GP | — | $36.3 | 2*10/100/1000M PoE + 1 port 100/1000M Fiber, PoE af/at Compliant, 60W budget, DIP function |
| STI-140FE | — | $29.7 | 4*10/100M Ethernet + 1 port 100M Fiber, DIP functions 1. Port isolation; 2. Flow control;  |
| STI-140GE | — | $37.4 | 4*10/100/1000M Ethernet + 1 port 1000M Fiber, DIP functions 1. Port isolation; 2. Flow con |
| STI-144FP | — | $37.4 | 4*10/100M PoE + 1 port 100M Fiber, DIP functions 1. Port isolation; 2. 250m long distance; |
| STI-144GP | — | $46.2 | 4*10/100/1000M PoE + 1 port 1000M Fiber, DIP functions 1. Port isolation; 2. 250m long dis |
| STI-150GE | — | $42.9 | 5*10/100/1000M Ethernet + 1 port 1000M Fiber, DIP function 1. Port isolation; 2. Flow cont |
| STI-154GP | — | $51.7 | 4*10/100/1000M PoE + 1*10/100/1000M Ethernet + 1 port 1000M Fiber, DIP function 1. Port is |
| STI-180FE | — | $48.4 | 8*10/100M Ethernet + 1 port 100M Fiber, DIP functions 1. Port isolation; 2. Flow control;  |
| STI-180GE | — | $59.4 | 8*10/100/1000M Ethernet + 1 port 1000M Fiber, DIP functions 1. Port isolation; 2. Flow con |
| STI-188FP | — | $56.1 | 8*10/100M PoE + 1 port 100M Fiber, DIP functions 1. Port isolation; 2. 250m long distance; |
| STI-188GP | — | $70.4 | 8*10/100/1000M PoE + 1 port 1000M Fiber, DIP functions 1. Port isolation; 2. 250m long dis |
| STI-2160DGGM | L2+ | $220.0 | 2*100M/1G/2.5G SFP+16*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, Redundant DC12V~58 |
| STI-2160GE | — | $170.5 | 16*10/100/1000M Ethernet + 2 port 1000M Fiber, DIP function 1. Link aggregation; 2. Flow c |
| STI-2160XGGM | L2+ | $291.5 | 2*100M/1G/2.5G/10G SFP+16*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, Redundant DC12 |
| STI-2160XGGM | L3 | $385.0 | 2*100M/1G/2.5G/10G SFP+16*10/100/1000M RJ45 L3 Managed, Non-PoE, Din Rail, Redundant DC12V |
| STI-21616DGGPM | L2+ | $242.0 | 2*100M/1G/2.5G SFP+16*10/100/1000M PoE L2+ Managed, PoE af/at, 240W budget, Din Rail, Redu |
| STI-21616GP | — | $203.5 | 16*10/100/1000M PoE + 2 port 1000M Fiber, DIP functions 1. Link aggregation; 2. 250m long  |
| STI-21616XGGPM | L2+ | $324.5 | 2*100M/1G/2.5G/10G SFP+16*10/100/1000M PoE L2+ Managed, PoE af/at, 240W budget, Din Rail,  |
| STI-21616XGGPM | L3 | $412.5 | 2*100M/1G/2.5G/10G SFP+16*10/100/1000M PoE L3 Managed, PoE af/at, 240W budget, Din Rail, R |
| STI-220FE | — | $29.7 | 2*10/100M Ethernet + 2 port 100M Fiber, DIP function 1. Fiber redundant; 2. Flow control;  |
| STI-220GE | — | $36.3 | 2*10/100/1000M Ethernet + 2 port 100/1000M Fiber, DIP function 1. Fiber redundant; 2. Flow |
| STI-222FP | — | $36.3 | 2*10/100M PoE + 2 port 100M Fiber, PoE af/at Compliant, 60W budget, DIP function 1. Fiber  |
| STI-222GP | — | $39.6 | 2*10/100/1000M PoE + 2 port 100/1000M Fiber, PoE af/at Compliant, 60W budget, DIP function |
| STI-240DGGM | L2+ | $110.0 | 2*100M/1G/2.5G SFP+4*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, Redundant DC12V~58V |
| STI-240FE | — | $33.0 | 4*10/100M Ethernet + 2 port 100M Fiber, DIP functions 1. Port isolation; 2. Flow control;  |
| STI-240FM | L2 | $55.0 | 2*100M SFP+4*10/100M RJ45 L2 Managed, Non-PoE, Din Rail, Redundant DC12V~58V Input |
| STI-240GE | — | $40.7 | 4*10/100/1000M Ethernet + 2 port 1000M Fiber, DIP function 1. Port isolation; 2. Flow cont |
| STI-240GM | L2 | $66.0 | 2*100M/1000M SFP+4*10/100/1000M RJ45 L2 Managed, Non-PoE, Din Rail, Redundant DC12V~58V In |
| STI-244DGGPM | L2+ | $121.0 | 2*100M/1G/2.5G SFP+4*10/100/1000M PoE L2+ Managed, PoE af/at, 120W budget, Din Rail, Redun |
| STI-244DGGPM-2BT | L2+ | $143.0 | 2*100M/1G/2.5G SFP+4*10/100/1000M PoE L2+ Managed, 2*PoE af/at+2*PoE af/at/bt, 240W budget |
| STI-244FP | — | $40.7 | 4*10/100M PoE + 2 port 100M Fiber, DIP functions 1. Port isolation; 2. 250m long distance; |
| STI-244FPM | L2 | $66.0 | 2*100M SFP+4*10/100M PoE L2 Managed, PoE af/at, 120W budget, Din Rail, Redundant DC44V~57V |
| STI-244GP | — | $49.5 | 4*10/100/1000M PoE + 2 port 1000M Fiber, DIP functions 1. Port isolation; 2. 250m long dis |
| STI-244GPM | L2 | $77.0 | 2*100M/1000M SFP+4*10/100/1000M PoE L2 Managed, PoE af/at, 120W budget, Din Rail, Redundan |
| STI-260FE | — | $44.0 | 6*10/100M Ethernet + 2 port 100M Fiber, DIP functions 1. Port isolation; 2. Flow control;  |
| STI-266FP | — | $51.7 | 6*10/100M PoE + 2 port 100M Fiber, DIP functions 1. Port isolation; 2. 250m long distance; |
| STI-280DGGM | L2+ | $121.0 | 2*100M/1G/2.5G SFP+8*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, Redundant DC12V~58V |
| STI-280GE | — | $63.8 | 8*10/100/1000M Ethernet + 2 port 1000M Fiber, DIP functions 1. Port isolation; 2. Flow con |
| STI-280GM | L2 | $77.0 | 2*100M/1000M SFP+8*10/100/1000M RJ45 L2 Managed, Non-PoE, Din Rail, Redundant DC12V~58V In |
| STI-288DGGPM | L2+ | $137.5 | 2*100M/1G/2.5G SFP+8*10/100/1000M PoE L2+ Managed, PoE af/at, 240W budget, Din Rail, Redun |
| STI-288DGGPM-2BT | L2+ | $154.0 | 2*100M/1G/2.5G SFP+8*10/100/1000M PoE L2+ Managed, 6*PoE af/at+2*PoE af/at/bt, 240W budget |
| STI-288GP | — | $74.8 | 8*10/100/1000M PoE + 2 port 1000M Fiber, DIP functions 1. Port isolation; 2. 250m long dis |
| STI-288GPM | L2 | $88.0 | 2*100M/1000M SFP+8*10/100/1000M PoE L2 Managed, PoE af/at, 240W budget, Din Rail, Redundan |
| STI-4160XGGM | L3 | $462.0 | 4*100M/1G/2.5G/10G SFP+16*10/100/1000M RJ45 L3 Managed, Non-PoE, Din Rail, Redundant DC12V |
| STI-41616XGGPM | L3 | $495.0 | 4*100M/1G/2.5G/10G SFP+16*10/100/1000M PoE L3 Managed, PoE af/at, 240W/370W budget, Din Ra |
| STI-41616XGGPM-4BT | L3 | $528.0 | 4*100M/1G/2.5G/10G SFP+16*10/100/1000M PoE L3 Managed, 12*PoE af/at+4*PoE af/at/bt, 370W b |
| STI-4168DGGCM-U | L2+ | $467.5 | 4*100M/1G/2.5G SFP+16*100M/1G SFP+8*1G SFP/RJ45 Combo L2+ Managed, Non-PoE, 1U Rack, AC100 |
| STI-4168XGGCM-U | L2+ | $511.5 | 4*100M/1G/2.5G/10G SFP+16*100M/1G SFP+8*1G SFP/RJ45 Combo L2+ Managed, Non-PoE, 1U Rack, A |
| STI-4168XGGCM-U | L3 | $605.0 | 4*100M/1G/2.5G/10G SFP+16*100M/1G SFP+8*1G SFP/RJ45 Combo L3 Managed, Non-PoE, 1U Rack, AC |
| STI-4240DGGM | L2+ | $330.0 | 4*100M/1G/2.5G SFP+24*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, Redundant DC12V~75 |
| STI-4240DGGM-U | L2+ | $363.0 | 4*100M/1G/2.5G SFP+24*10/100/1000M RJ45 L2+ Managed, Non-PoE, 1U Rack, AC100V~240V Input ( |
| STI-4240XGGM | L2+ | $385.0 | 4*100M/1G/2.5G/10 SFP+24*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, Redundant DC12V |
| STI-4240XGGM | L3 | $478.5 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M RJ45 L3 Managed, Non-PoE, Din Rail, Redundant DC12V |
| STI-4240XGGM-U | L2+ | $412.5 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M RJ45 L2+ Managed, Non-PoE, 1U Rack, AC100V~240V Inp |
| STI-4240XGGM-U | L3 | $506.0 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M RJ45 L3 Managed, Non-PoE, 1U Rack, AC100V~240V Inpu |
| STI-42424DGGPM | L2+ | $363.0 | 4*100M/1G/2.5G SFP+24*10/100/1000M PoE L2+ Managed, 24*PoE af/at, 240W/370W budget Din Rai |
| STI-42424DGGPM-4BT | L2+ | $407.0 | 4*100M/1G/2.5G SFP+24*10/100/1000M PoE L2+ Managed, 20*PoE af/at+4*PoE af/at/bt, 240W/370W |
| STI-42424DGGPM-U | L2+ | $407.0 | 4*100M/1G/2.5G SFP+24*10/100/1000M PoE L2+ Managed, 24*PoE af/at, 370W budget 1U Rack, AC1 |
| STI-42424DGGPM-U-2BT | L2+ | $440.0 | 4*100M/1G/2.5G SFP+24*10/100/1000M PoE L2+ Managed, 22*PoE af/at+2*PoE af/at/bt, 370W budg |
| STI-42424XGGPM | L2+ | $423.5 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M PoE L2+ Managed, 24*PoE af/at, 240W/370W budget Din |
| STI-42424XGGPM | L3 | $517.0 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M PoE L3 Managed, PoE af/at, 240W/370W budget, Din Ra |
| STI-42424XGGPM-4BT | L2+ | $456.5 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M PoE L2+ Managed, 20*PoE af/at+4*PoE af/at/bt, 240W/ |
| STI-42424XGGPM-4BT | L3 | $550.0 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M PoE L3 Managed, 20*PoE af/at+4*PoE af/at/bt, 370W b |
| STI-42424XGGPM-U | L2+ | $451.0 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M PoE L2+ Managed, 24*PoE af/at, 370W budget 1U Rack, |
| STI-42424XGGPM-U | L3 | $550.0 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M PoE L3 Managed, 24*PoE af/at, 370W budget 1U Rack,  |
| STI-42424XGGPM-U-2BT | L2+ | $484.0 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M PoE L2+ Managed, 22*PoE af/at+2*PoE af/at/bt, 370W  |
| STI-42424XGGPM-U-2BT | L3 | $583.0 | 4*100M/1G/2.5G/10G SFP+24*10/100/1000M PoE L3 Managed, 22*PoE af/at+2*PoE af/at/bt, 370W b |
| STI-4480XGGM-U | L3 | $847.0 | 4*100M/1G/2.5G/10G SFP+48*10/100/1000M RJ45 L3 Managed, Non-PoE, 1U Rack, AC100V~240V Inpu |
| STI-448DGGGM | L2+ | $220.0 | 4*100M/1G/2.5G SFP+4*100M/1G SFP+8*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, Redun |
| STI-448DGGGPM | L2+ | $236.5 | 4*100M/1G/2.5G SFP+4*100M/1G SFP+8*10/100/1000M PoE L2+ Managed, PoE af/at, 240W budget, D |
| STI-448XGGGM | L2+ | $275.0 | 4*100M/1G/2.5G/10G SFP+4*100M/1G SFP+8*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, R |
| STI-448XGGGM | L3 | $363.0 | 4*100M/1G/2.5G/10G SFP+4*100M/1G SFP+8*10/100/1000M RJ45 L3 Managed, Non-PoE, Din Rail, Re |
| STI-448XGGGPM | L2+ | $297.0 | 4*100M/1G/2.5G/10G SFP+4*100M/1G SFP+8*10/100/1000M PoE L2+ Managed, PoE af/at, 240W budge |
| STI-448XGGGPM | L3 | $385.0 | 4*100M/1G/2.5G/10G SFP+4*100M/1G SFP+8*10/100/1000M PoE L3 Managed, PoE af/at, 240W budget |
| STI-480DGGM | L2+ | $132.0 | 4*100M/1G/2.5G SFP+8*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, Redundant DC12V~58V |
| STI-480GE | — | $115.5 | 8*10/100/1000M Ethernet + 4 port 1000M Fiber, DIP function 1. Link aggregation; 2. Flow co |
| STI-480XGGM | L2+ | $253.0 | 4*100M/1G/2.5G/10G SFP+8*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, Redundant DC12V |
| STI-4816XGCGM-U | L3 | $572.0 | 4*100M/1G/2.5G/10G SFP+8*1G SFP/RJ45 Combo+16*10/100/1000M RJ45 L3 Managed, Non-PoE, 1U Ra |
| STI-4816XGCGPM-U | L3 | $605.0 | 4*100M/1G/2.5G/10G SFP+8*1G SFP/RJ45 Combo+16*10/100/1000M PoE L3 Managed, 16*PoE af/at, 3 |
| STI-4816XGCGPM-U-2BT | L3 | $638.0 | 4*100M/1G/2.5G/10G SFP+8*1G SFP/RJ45 Combo+16*10/100/1000M PoE L3 Managed, 14*PoE af/at+2* |
| STI-488DGGGM | L2+ | $352.0 | 4*100M/1G/2.5G SFP+8*100M/1G SFP+8*10/100/1000M RJ45 L2+ Managed, Non-PoE, Din Rail, Redun |
| STI-488DGGPM | L2+ | $148.5 | 4*100M/1G/2.5G SFP+8*10/100/1000M PoE L2+ Managed, PoE af/at, 240W budget, Din Rail, Redun |
| STI-488DGGPM-2BT | L2+ | $165.0 | 4*100M/1G/2.5G SFP+8*10/100/1000M PoE L2+ Managed, 6*PoE af/at+2*PoE af/at/bt, 240W budget |
| STI-488GP | — | $132.0 | 8*10/100/1000M PoE + 2 port 1000M Fiber, DIP functions 1. Link aggregation; 2. 250m long d |
| STI-488XGGGM | L3 | $451.0 | 4*100M/1G/2.5G/10G SFP+8*100M/1G SFP+8*10/100/1000M RJ45 L3 Managed, Non-PoE, Din Rail, Re |
| STI-488XGGPM | L2+ | $269.5 | 4*100M/1G/2.5G/10G SFP+8*10/100/1000M PoE L2+ Managed, PoE af/at, 240W budget, Din Rail, R |
| STI-880GE | — | $137.5 | 8*10/100/1000M Ethernet + 8 port 1000M Fiber, DIP functions 1. Port isolation; 2. Flow con |
| STI-888GP | — | $159.5 | 8*10/100/1000M PoE + 8 port 1000M Fiber, WITHOUT DIP functions |
