# PLANET PoE 产品线 → Saga 对位表（v1 · 2026-10-19）

> 来源：用户给定起点 <https://www.planet.com.tw/en/products/power-over-ethernet> 及其子页（2026-10-19 `fetch_page` 抓取），加上本轮客户证据页中出现的型号。对位原则：**同口数 / 同上联 / 同 PoE 等级的近似**，不是功能等价（PLANET 的 LCD 触屏、802.3bt/UPoE、ONVIF、云 NMS、EN50155、太阳能 PoE，Saga 均无——话术避开）。价格按 `docs/rules/报价与型号规则.md` 公式，型号书写按 Saga 优先规则。

## 1. PLANET PoE 分类树（起点页实抓）

| PLANET 分类 | 子类 | 代表型号（页面所见） | Saga 可对位？ |
|---|---|---|---|
| Layer 3 Managed PoE Switches | 802.3bt L3 / 802.3at L3 | SGS-6341-24P4X（bt）、GS-6322-48UP4X（bt） | at 档可对位 STC-424XGGPM(L3)/STC-448XGGPM(L3)；bt 档**无** |
| Layer 2/2+ Managed PoE Switches | 802.3bt L2/L4 | GS-4210-8UP2X、GS-4210-24UP4X、GS-4210-16UP8T4X、GS-4210-8UP2S、AVS-4210-8HP2X/24HP4X | **无**（Saga 商用线无 bt） |
|  | 802.3at L2+ | GS-5220-8P2T2S（及 GS-5220-24P4X 系） | STC-28DGGPM / STC-424XGGPM-280W·440W |
|  | 802.3at L2/L4 | GS-4210-16P2S、GS-4210-24P4C/24PL4C、GS-4210-24P2S、GS-4210-16P4C、GS-4210-8P2S、GS-4210-48P4S | STC-28DGGPM / STC-424DGGPM-280W·440W / STC-448DGGPM；16 口商用 PoE **Saga 无**（SmartByte 亦无）→ 用 24 口替代并说明 |
|  | 802.3at L2/L4 Fast Ethernet | FGSW-2624HPS 等 | **无**（Saga 商用线无 FE PoE 管理型；工业非管理 STI-188FP 近似） |
| Layer 2 Smart PoE Switches | 802.3at Web Smart | GSW-2620HP、FGSW-2622VHP、GSD-1222VHP（LCD） | STC-424DGGPM-280W（功能更多价更低）；LCD 无 |
| LCD PoE Switches | bt / at | GS-5220-24UPL4XV 等 | **无** |
| Unmanaged PoE Switches | bt / at GE / at FE | GSW-2620VHP、GSD-804P、GSD-908HP、POE-176-95（注入器） | 商用非管理 Saga **无**（SmartByte 亦无商用非管理线）；工业非管理 STI-088GP/STI-288GP 可作替代并说明 |
| Long Reach PoE Solution | UTP/Coax 延长 | LRP-1622CS、LRP-111U-KIT | **无** |
| PoE Injector Hubs / Injector·Splitter / Extender / PoE Media Converter | — | UPOE-1600G、HPOE-2400G、IPOE-E174 | **无**（介质转换器部分可用 STI-111GP/STI-122GP 工业 PoE MC 近似） |
| Industrial Power over Ethernet | EN50155 L3 / 机架 L3 / DIN L3 / DIN L2+ 等 | IGS-6325-16P4S、IGS-6325-8T8S4X、IGS-5225-8P4S、IGS-5225-8P2S、WGS-5225-8P2S、WGS-4215-8P2S、IGS-10020HPT、IGS-624HPT、ITS-5216-8P2TB-WV | DIN L2+：STI-288DGGPM / STI-488DGGPM / STI-21616DGGPM / STI-42424XGGPM；DIN L3：STI-448XGGGM(L3)…；**EN50155/M12 守界不对标** |
| Renewable Energy PoE System | 太阳能 PoE | BSP-360 | **无** |
| PoE Network Interface Card | — | ENW-9740P | **无** |

## 2. 常见 PLANET 型号 → Saga 型号速查（本轮证据页出现者）

| PLANET 型号 | 规格要点 | Saga 对位 | 20% 档 USD | 说明 |
|---|---|---|---:|---|
| GS-4210-8P2S | 8×GE PoE+ + 2×SFP，L2/L4 | STC-28DGGPM | $80.7 | Saga 为 L2+、240W、2×1G/2.5G SFP |
| GS-4210-8P2T2S | 8×GE PoE+ + 2 GE + 2 SFP | STC-28DGGPM | $80.7 | 少 2 个 GE 上联 |
| GS-4210-16P2S / 16P4C | 16×GE PoE+ + 2/4 上联 | （无 16 口商用 PoE）→ STC-424DGGPM-280W | $134.5 | 写「Saga/SmartByte 均无 16 口商用 PoE 管理型，以 24 口替代」 |
| GS-4210-24P4C / 24PL4C / 24P2S | 24×GE PoE+ + 4 Combo / 2 SFP | STC-424DGGPM-280W | $134.5 | 预算更高用 -440W（$215.2） |
| GS-4210-48P4S | 48×GE PoE+ + 4 SFP | STC-448DGGPM | $308.5 | 440W |
| GS-5220-24P4X 系 | 24×GE PoE+ + 4×10G，L2+ | STC-424XGGPM-280W | $181.2 | 用户主力 $180 价位；440W 版 $— 按表 |
| GS-4210-xxUPxx / AVS-4210 | 802.3bt | — | — | **Saga 暂无对应型号**；SmartByte 商用线亦无 → 不对标 |
| GSW-2620HP / GSW-2620VHP | 24×GE PoE+ + 2 SFP，smart/非管理 | STC-424DGGPM-280W | $134.5 | 以管理型替代非管理/smart，功能溢出 |
| FGSW-2622VHP / FGSW-2624HPS | 24×FE PoE+ | — | — | Saga 商用线无 FE PoE；写明并建议千兆升级 |
| GSD-804P / GSD-908HP | 8 口桌面，4/8 PoE | STC-28DGGPM 或 STI-088GP | $80.7 / $42.2 | 桌面非管理 Saga 无，用管理型或工业非管理替代并说明 |
| IGS-5225-8P4S | 工业 L2+ 8×GE PoE + 4 SFP | STI-488DGGPM | $147.1 | DIN，240W，3 年保 |
| IGS-5225-8P2S / WGS-5225-8P2S / WGS-4215-8P2S | 工业 L2+ 8×GE PoE + 2 SFP | STI-288DGGPM | $139.9 | PLANET WGS 为壁挂，Saga 为 DIN |
| IGS-10020HPT | 工业 L2+ 8 PoE + 2 TP + 2 SFP | STI-488DGGPM（近似） | $147.1 | 上联形态不同 |
| IGS-6325-16P4S | 工业 L3 16 PoE + 4 SFP | STI-21616XGGPM(L3) | $— 按表 | Saga 上联为 2×10G |
| IGS-6325-8T8S4X | 工业 L3 8T + 8S + 4×10G | STI-448XGGGM(L3)（近似） | $— | Saga 为 8T + 4S + 4×10G |
| XGS3-24042 | 24×GE + 4×10G L3（冗余电源） | STC-424XGGM(L3) | $— | — |
| SGS-6340-16XR | 16×10G SFP+ L3 | — | — | **Saga/SmartByte 均无全万兆汇聚** |
| IGS-801T / IGS-620TF | 工业非管理 8×GE / 4×GE+2 SFP | STI-080GE / STI-240GE | $31.4 / $28.0 | — |
| ITS-5216-8P2TB-WV 等 ITS/EN50155 | 轨交 M12 | — | — | **守界**：Saga 不做轨交 |
| UPOE-1600G / HPOE-2400G / POE-176-95 | PoE 注入器/集线 | — | — | 无对应 |
| BSP-360 | 太阳能 PoE | — | — | 无对应 |

> 20% 档 USD 取自 `data/价格主表.csv`（汇率 6.69，2026-10-17）；「$— 按表」表示该行请直接查价格主表对应 SmartByte 型号（L3 档等）。

## 3. 话术层面的要点

- 对 PLANET 渠道**不贬低 PLANET**；只谈：第二货源、贴牌（中性包装 + 客户型号）、功能定制（Web UI/CLI/MIB）、3 年工业保、ERPS<20ms、芯片库存与交期。
- 遇到客户主销 bt/UPoE、LCD、FE PoE、Long Reach、太阳能 PoE、EN50155 → 如实说 Saga 无对应，不硬推。
