# Planet 客户挖掘方法论（v1 · 2026-10-19）

> 目标：找出 **PLANET Technology 在欧洲 + 美国/加拿大的客户**——独立分销商、电商、安防/工业自动化经销、集成商、把 PLANET 白牌贴成自有品牌的品牌商——并按 Mikrotik 仓库规则定级建档。PLANET 本身与其自营/关联公司**不是客户**（宪法第七条）。
>
> 工具现实：沙箱 `curl` 只能到 github/npm/pypi；**只能用 `fetch_page`（逐页）与 `web_search`（摘要）**，无法批量脚本抓取。因此方法设计为「检索 → 逐页核证 → 批次 JSON 落盘」。

## 零 · 起点与信号源地图（已核实 2026-10-19）

| 入口 | 状态 | 能拿到什么 |
|---|---|---|
| <https://www.planet.com.tw/en/products/power-over-ethernet>（用户给的起点） | ✅ 可抓 | PoE 产品分类与型号（用于「型号反查」与「PLANET→Saga 对照」） |
| planet.com.tw「Where to Buy / 经销商定位器」 | ❌ **不存在公开页**（`/en/where-to-buy`、`/en/partner/where-to-buy` 均 404；Partner Zone 需登录） | 无 → 必须靠外部检索 |
| <https://planetechusa.com/where-to-buy/>（PLANET 北美分销 Versa Technology 的转售名单） | ✅ 可抓 | 美国转售商 5 家（Pulse Supply、Black Box、Graybar、Anixter/Wesco、Platinum Micro）+ 拉美 1 家；多为巨头 → C |
| planet.com.tw 案例研究（8 篇） | ✅ 可抓但**匿名** | 只有国家与型号，不披露集成商名 → 死路 |
| PLANET 各国官方分销商自建站（planet-germany.de、planet.spectra.de、4power.it、aikomtech.com、planet.neteon.net…） | ✅ 可抓 | 品牌页 + 联系方式；部分站有「经销商/合作伙伴」页可二次挖 |
| PLANET LinkedIn（planet-technology-hq）、Facebook | 登录墙 | 只能靠 web_search 摘要 |

## 一 · 方法清单（按预期 A 率排序）

### M1 · 型号反查（Model Reverse Lookup）— 预期产出最大

用 PLANET PoE/工业交换机**具体型号**做检索词，命中的欧美网页即「在卖/在用 PLANET」的公司：

```
"GS-4210-24P4C"  site:.de | .fr | .it | .es | .nl | .pl | .co.uk | .se | .dk | .no | .fi | .at | .ch | .be | .cz | .pt | .ie | .com
"GS-5220-24P4X" / "GS-4210-8P2S" / "IGS-5225-8P2S" / "IGS-6325-8T8S4X" / "FGSW-2624HPS" / "GSW-2620VHP" / "ISW-1600T" / "BSP-360" / "IGS-10020PT"
```
- 命中类型：电商（B/C）、安防经销（B）、集成商写的项目/博客（**A 候选**）、招标文件（公共采购 → 守界 C）。
- 每个型号 × 每个国家 TLD 一次检索；结果页逐个 `fetch_page` 核证「确实列有 PLANET 产品」+ 抓联系方式。

### M2 · 品牌页反查（Brand Page Lookup）

各语种「PLANET 官方分销/授权经销」检索：

```
"PLANET Technology" distributor Germany / "offizieller PLANET Distributor" / "PLANET Technology" Großhändler
"distributore ufficiale PLANET Technology" / "distribuidor oficial PLANET Technology" / "distributeur officiel PLANET Technology"
"PLANET Technology" "autoryzowany dystrybutor" / "officiële distributeur PLANET" / "PLANET Technology" återförsäljare / forhandler / jälleenmyyjä
"PLANET Technology" "authorized distributor" UK / Ireland / USA / Canada
```
- 命中多为分销商（B/C），但其站内常有「我们的合作伙伴/安装商」页 → 二次挖集成商（A 候选）。

### M3 · 分销商的下游反查（Distributor → Installer）

对 M2 找到的每家分销商，找站内「Partner / Reseller / Installer / Referenzen / Case study」页；再用 `"<分销商名>" PLANET installer|Systemintegrator|installatore` 检索。

### M4 · 项目与博客反查（Integrator Content）

```
"PLANET" switch "IGS-" (installation | project | Referenz | réalisation | realizacja | caso de éxito) site:.de|.fr|.it|.es|.pl|.nl|.co.uk
"PLANET Technology" PoE switch CCTV installer / "we installed" / "we use PLANET switches"
```
- 直接命中集成商 → A 候选（需找到具名人）。

### M5 · 展会与活动同台（Trade Show Co-exhibitors）

`"PLANET Technology" (SPS | Security Essen | IFSEC | ISC West | SICUR | Intersec Europe | Sicurezza Milano | Hannover Messe | embedded world) partner|distributor|stand`
- 命中展位合作方 → 多为分销商。

### M6 · 招聘/岗位信号（HR Signal）

`"PLANET" switches (Netzwerktechniker | network engineer | Systemintegrator) job` —— 谁在招会配 PLANET 设备的人，谁就在用。低产出，作补充。

### M7 · 白牌/OEM 反查（Rebrand Detection）

PLANET 大量给欧美品牌 OEM（外形/规格同款、不同 logo）。检索 `"24-Port 10/100/1000T 802.3at PoE + 4-Port Gigabit TP/SFP Combo Managed Switch"`（PLANET 固定描述句式）排除 planet 域名 → 命中的品牌商 = **最优先客户（OEM/ODM 需求）**。同理用 `"Intelligent PoE" "PoE Alive Check"`、`"PD Alive Check"` 等 PLANET 专有术语。

### M8 · 跨仓交叉（Cross-repo）

Mikrotik 仓库 26 行 PLANET 相关户只做去重参照，不重挖；若本仓库发现新 PLANET 证据，只补证据不改对方档案。

### M9 · 国家工商登记核名（继承 R64）

Companies House（UK）、northdata/Handelsregister（DE/AT/CH）、pappers（FR）、registroimprese（IT）、KRS（PL）、proff/allabolag（北欧）、OpenCorporates（US）——用于法人、规模、具名董事；不用于猜邮箱。

### M10 · 竞品分销重叠（Competitor Overlap）

同时代理 ORing/EtherWAN/Moxa/Edgecore/Zyxel 的分销商，PLANET 往往也在其货架；用 `"PLANET" "ORing" distributor` 等组合检索。

## 二 · 国家顺序与配额

按 Saga 目标区（INH-02）与 PLANET 渠道深度：

1. **第一梯队**：DE、UK、IT、ES、FR、NL、PL、US、CA
2. **第二梯队**：AT、CH、BE、SE、DK、NO、FI、CZ、PT、IE、GR、HU、SK
3. **不主动挖**（INH-11）：SI、HR、RS、RO、BG、EE、LV、LT、LU、IS；UA 守界。

每批 ≈ 10–20 户，含完整证据；宁少勿假。

## 三 · 单户最低证据

1. PLANET 关联证据：URL + 原文（品牌页 / 商品页 / 项目页），抓取日期。
2. 公司基本面：国家、城市、网站、类型、是否自有品牌。
3. 联系入口：公开邮箱（具名优先）/ 电话 / 表单；来源 URL。没有就写「待补证」。
4. 初评与依据（一句话）。
5. 首推 Saga 型号（按其在卖的 PLANET 型号对位，见 `docs/reference/PLANET_PoE产品线与Saga对照.md`）。

## 四 · 产出与记账

- 每批：`batch/<YYYY-MM-DD>_<批名>.json` → `scripts/add_batch.py` 入主表 → `scripts/render.py` 出档案 → `scripts/audit.py` → README 进度 → 对话全记录/总账。
- 每批 JSON 必须有 `skipped`（含原因）与 `queries`（检索词清单，保证可复现）。

## 五 · 实战经验累积（每轮追加）

### W02（2026-10-19，≈60 次 web_search，+25 户，A 7）

- **什么有效**：① M2 品牌页反查在 **UK/IE/CZ/HU/CA** 命中率最高（每国 2–4 户专业经销）；② **安防批发商**（ALARM ABSOLON、NSI、Power Bizt.、Aspectis、W3CAM）普遍在官网 kontakt 页公开具名销售直邮 → A 率高；③ **工商/名录核名**（northdata、nordicnet、pappers、societe.com、ufficiocamerale）一次查询即可拿到规模/年份/负责人，用于「体量可赢」判断；④ **Mikrotik 主表 grep** 必做（本轮 3 组重合：BSC、Jampel、100MEGA），避免重复首触。
- **什么无效**：① `site:` + 精确型号 = 0 结果；② 「appoints distributor / white label」新闻查询 = 同名噪音；③ AT/CH/BE/NL 的「distributor + PLANET」只出泛电商；④ 美国 WISP 分销商无 PLANET；⑤ 美国集成商直接检索无 PLANET 命中（需改走 M3/M4）。
- **A 的三种形态（本轮归纳）**：(a) 具名直邮公开的安防/工业分销（Absolon、Aspectis、Jampel）；(b) ≤10 人微型公司，info@/sales@ 即老板（Kyma、iOC Tech）；(c) 已有自有品牌的分销商（NSI/Norelco、Direktronik、BSC/Lysora、BTS）——贴牌切入，30% 档。
- **证据纪律提醒**：web_search 摘要可作证据但必须标「检索摘要」；凡标「待补证/原文待 fetch 核对」的，下一轮用 `fetch_page` 补原文再首触（Kyma、Absolon、Aspectis、BTS、NSI OEM 页、Jampel 旧站邮箱）。

### W03（2026-10-19，≈35 次 web_search，+13 户，A 3；W02 pending 9 项清零）

- **什么有效**：① **M11（新增）官方代表/授权页措辞反查**：`represented in Spain and Portugal by`（Anatronic）、`distributore autorizzato di Planet`（SIR.tel）、`produsenter`/`forhandler`（Leteng）、`dystrybutorem Planet Technology`（VERSIM）、`Exkluzivním partnerem`（ASM）——各语种的「授权/代表/独家」措辞比「distributor」命中专业经销更准；② **团队页（/team、/Yhteystiedot、/rolunk/elerhetosegeink）**直接给出采购经理/产品经理具名（SIR.tel Gioia Mantoan、Young Pásztor András、Microdata 4 位销售）；③ **会员/伙伴名录的第三方公开直邮**（lyskultur.no → Leteng 总经理；highseclabs where2buy → Leteng 销售经理；Softing → Direktronik）属「真公开」，可用；④ **Mikrotik grep 加域名 token**（connectdata、compass、azenn）又捞出 3 组同户——W02 只按公司名 grep 漏了 Direktronik/Connect Data。
- **什么无效**：① M7 两种措辞全噪音；② 美国集成商 case study / authorized dealer 无命中；③ DK/AT/CH/BE/NL 仍只出电商；④ CA/UK 入口已穷尽；⑤ RocketReach/zoominfo 人名只能作「待核」，不能作触达依据。
- **首触前必做（本轮教训）**：**先读 Mikrotik 同户整行的「状态/备注」**——Direktronik 的 steffo@ 在 Mikrotik 侧 9 月已退信，W02 却把它列为 A 的直邮依据；规则：凡 Mikrotik 同户，退信/停用通道原样继承为「发不过去」，主通道随 Mikrotik 侧。
- **集团视角**：Lagercrantz 集团同时拥有 Direktronik（SE）与 Leteng（NO）——子公司各自采购、规模 20–30 人、都在卖 PLANET → 可赢，但两户首触节奏要错开。
- **A 的第四种形态**：(d) 具名采购经理但无直邮、销售邮箱公开的活跃授权分销（SIR.tel）——以 `Attn:` 走 sales@；若用户要求 A 必须直邮则降 B。

