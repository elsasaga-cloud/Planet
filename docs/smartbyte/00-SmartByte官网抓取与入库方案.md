# 00 · SmartByte 官网抓取与入库方案（T14，2026-10-20）

> 用户 T14 裁定：Drive 资料是 2026 Q3（7–9 月）旧版；**SmartByte 官网（2026-09 改版）为最新、以官网为准**。本文记录站点结构、已抓取内容、入库规则与后续分阶段计划。  
> 抓取方式：沙箱 bash 不能直连该域名，全部通过 `fetch_page` 逐页抓取（每页 1–6 个分块，导航占每块约一半篇幅）。所有入库文本均带 URL + 抓取日期；图片/PDF 只记 URL。

## 一、站点结构（2026-10-20 抓取 `sitemap.xml`，共 5 块）
- 顶栏：Home / Industrial Ethernet / Commercial Ethernet / White Box / About（Company Profile · Factory Tour · Contact Us）/ Support（OEM/ODM · Warranty & RMA Policy · SKD & CKD · Firmware Update Highlights）。
- 口号："Genuine Source Factory • Robust R&D Support — Custom Marvell-Based Ethernet Switch OEM/ODM Solutions"。
- 产品中心 19 个品类（URL 见下表）；每个品类页分页（例：Managed Industrial Ethernet Switch 共 5 页，`?ClassID=689212&responseModuleId=729023884&PageNo=n`），每页约 12 个型号，列表项含 **标题 + 型号（LT-…）+ 详情 URL**。
- 站点地图共约 **220 个产品详情 URL**（slug 即标题，如 `/8-10-100-1000Base-T-4-1G-2-5GBase-X-SFP-L2-Managed-Industrial-PoE-Switch-PG12134586`，另有 `/ProductDetail/<id>.html` 形式约 35 个）+ 2 个新闻列表页 + 8 篇 NewsDetail（4 篇为固件更新说明）。
- 产品详情页结构：标题 / 型号 / **Download Annex（规格书 PDF，`index.php?c=Front/DownDetail&a=downloadFujian&…`）** / Overview / Features / Technical specification / Structure diagram / Order information（共 6 块，第 0 块含型号 + 概述 + 特性要点）。
- 产品筛选器维度：Function（Layer 3 / L2+/L2 / Bypass / Boost / DI-DO-RS485 / Temp-humidity Sensor / Unmanaged）、Ports（2–4 / 5–12 / 16–20 / 28–52 / 54–56）、PoE（Non / af-at / bt 60–90W）、Power Supply（No / External / Internal Fixed / Hot-Swap）、Speed（FE / Full Gigabit / 10G / 25G / 100G Uplink）。

| 大类 | 品类 | URL |
|---|---|---|
| Industrial Ethernet | Managed Industrial Ethernet Switch | https://www.smartbyte-switch.com/Managed-Industrial-Switch |
| | Managed Industrial PoE Switch | https://www.smartbyte-switch.com/Managed-Industrial-PoE-Switch- |
| | Managed Industrial PoE++ Switch | https://www.smartbyte-switch.com/Managed-Industrial-PoE-Switch-- |
| | Managed Industrial Boost PoE Switch | https://www.smartbyte-switch.com/Managed-Industrial-Boost-PoE-Switch |
| | Managed Industrial Fiber Bypass Switch | https://www.smartbyte-switch.com/Managed-Industrial-Fiber-Bypass-Switch |
| | Unmanaged Industrial Ethernet Switch | https://www.smartbyte-switch.com/Unmanaged-Industrial-Ethernet-Switch |
| | Unmanaged Industrial PoE/PoE++ Switch | https://www.smartbyte-switch.com/Unmanaged-Industrial-PoE/PoE/Switch |
| | Industrial Media Converter | https://www.smartbyte-switch.com/Industrial-Media-Converter |
| | Industrial PoE Media Converter | https://www.smartbyte-switch.com/Industrial-PoE-Media-Converter |
| | Industrial Boost Power Supply | https://www.smartbyte-switch.com/Industrial-Boost-Power-Supply |
| Commercial Ethernet | Managed Ethernet Switch | https://www.smartbyte-switch.com/Managed-Ethernet-Switch |
| | Managed PoE Switch | https://www.smartbyte-switch.com/Managed-PoE-Switch |
| | Managed PoE++ Switch | https://www.smartbyte-switch.com/Managed-PoE-Switch- |
| | Managed Switch with Hot-swap PS | https://www.smartbyte-switch.com/Managed-Switch-with-Hot-swap-PS |
| | Managed PoE/PoE++ Switch with Hot-swap PS | https://www.smartbyte-switch.com/Managed-PoE/PoE-Switch-with-Hot-swap-PS |
| | Media converter | https://www.smartbyte-switch.com/Media-converter |
| White Box Hardware | 10G Uplink Series | https://www.smartbyte-switch.com/10G-Uplink-Series |
| | 25G Uplink Series | https://www.smartbyte-switch.com/25G-Uplink-Series |
| | 100G Uplink Series | https://www.smartbyte-switch.com/100G-Uplink-Series |

## 二、入库规则（沿用 T13 三层法，官网为真源）
| 层级 | 范围 | 形式 | 状态 |
|---|---|---|---|
| Tier 1 全文 | About / Warranty & RMA / OEM-ODM / SKD-CKD / Contact / Firmware highlights | `docs/smartbyte/公司与政策页_2026-10-20.md`（英文原文要点 + URL） | ✅ 本轮 |
| Tier 2 型号索引 | 19 个品类的全部型号（型号 / 标题 / 品类 / 详情 URL / 规格书 URL） | `data/smartbyte_官网型号索引.csv`，按品类分页逐步补齐；与 `data/价格主表.csv` 的 135 个 LT- 型号按型号精确匹配 | 🔄 本轮 13 行（Managed Industrial 第 1 页 + 1 个详情样本），其余见计划 |
| Tier 3 详情页 | 单个型号的 Overview / Features / 规格表 | 只在写档案/邮件需要时抓该型号详情页第 0–2 块，摘要写入对应客户档案证据，不整站镜像 | 按需 |
| 不入库 | 图片、规格书 PDF 原件 | 记 URL | — |

**真源优先级（T14 起）**：SmartByte 官网 > SmartByte 2026-09 价格表（`data/价格主表.csv` 来源文件，价格有效期 2026-09-01～12-30）> Saga Drive（Q3 旧版）> 仓库既有推断。冲突一律记入 `docs/requirements/待统一处理问题清单.md`。

## 三、本轮已发现的"官网 ≠ Drive/仓库"差异
1. **保修**：官网 Warranty & RMA = 工业 6 系列 **5 年** / 3 系列 **3 年**；商用全部 **3 年**；ODM 项目另议；DOA 3 个月。Drive（Saga Warranty Policy）= STC 1 年 / STI 3 年 / STH 1 年。→ 速查表已改为官网口径，Q-22 请 Simon 确认 Saga 对外是否原样传递。
2. **OEM 软件定制 No MOQ**（logo / 型号名 / SN / 登录 IP / MAC / SNMP OID）与 Drive 口径一致；官网另明确硬件定制覆盖 1G–100G、SKD/CKD 为标准服务。
3. **公司事实**：SmartByte Technology Co., Ltd；2020 年深圳创立（OEM 页另称"since 2015"，以 About 为准）；工厂 >8,000 m²，ISO9001/14001；98% 产品用 Marvell 芯片；认证 CE/UKCA/FCC/RoHS/REACH/CCC；制造基地惠州惠阳区镇隆镇利和优客创新基地 1 栋 7–8 层，研发中心福州海西科技园华健大厦 2 栋；联系人 peter@smartbyte.com.cn，+86-755-28687362，手机/WhatsApp +86-137-1429-3521。
4. **路线图**：2025 AC3→AC5 升级完成、DI/DO/RS485 与 Booster PoE 上市；2026 固件 V7.5.0、Centec 平台管理型交换机、首款 TSN 工业交换机（Ironman）、MQTT/1588 PTP/Modbus/Profinet；**2027 EN50155 系列**（仓库规则"不做轨交/EN50155"维持，2027 前不承诺）。
5. **固件 7.5.0 仅 Marvell AC5 硬件支持**（IGMP/PIM-SM CLI、Time Range 联动 ACL/PoE、密码复杂度、端口隔离 32 组、Web 管理 DHCP relay/ARP 防欺骗/DHCP server/voice VLAN 等）——对客户谈"持续固件演进"的依据。

## 四、后续计划（分阶段，每阶段 1 个回合）
- **P1（下一回合）**：Managed Industrial Ethernet Switch 第 2–5 页 + Managed Industrial PoE / PoE++ 品类 → 型号索引约 +80 行，并与价格主表匹配（匹配到的补"官网 URL"列）。
- **P2**：商用 6 个品类 + Boost / Bypass / Unmanaged 工业品类 → 约 +90 行。
- **P3**：White Box 3 个品类 + 媒体转换器 + 工业电源（Tier 2 仅索引，不做 Saga 对照）；4 篇固件说明全文；Factory Tour 图片 URL 清单。
- 替代捷径：价格主表的 135 个 LT- 型号本身就是 SmartByte 2026-09 价格表（即 9 月更新后的在售清单），索引的主要增量是官网 URL / 规格书链接 / 新品（如 DI/DO/RS485、Temp-humidity Sensor、Boost、Bypass 衍生型）；若 Simon 能向 SmartByte 索取 9 月版产品总表 xlsx，P1–P3 可一次完成。

---

## T15 升级：全站原样归档（用户 2026-10-20「把官网所有的信息都 copy 下来入库，所有信息」）

**目标**：官网全部内容原样入库，不做取舍——≈220 个产品页（含 Overview / Features / 规格表 / 订购信息）、19 个品类页全部分页、公司/政策/新闻页、每个型号的规格书附件（Download Annex）、图片。

**通道判断**
- Arena 沙箱对 smartbyte-switch.com 无出网权限（只放行 github / pypi / npm），`fetch_page` 每页 2–6 块、每块 ≈5k token，220 个产品页 ≈ 1,300 次调用，整站需十几个回合——可行但极慢。
- 改为 **GitHub Actions 运行器整站抓取**：`scripts/smartbyte_crawl/crawl.py`（BFS 同域全站 + 附件 + 图片 + 三份清单，pdftotext 抽文本），工作流样板 `scripts/smartbyte_crawl/smartbyte-crawl.yml`。代理的 GitHub 连接**没有 workflows 权限**（推送 `.github/workflows/` 被拒），需 Simon 在 GitHub 网页端一键保存该文件（链接见 `scripts/smartbyte_crawl/一键添加工作流链接.txt`），保存即触发，约 15–30 分钟，结果自动提交回本分支 `data/smartbyte_site_raw/`，规格书 PDF 与图片打包进 Actions 构建产物 + Release `smartbyte-site-YYYYMMDD`（PDF 总量 ≤60 MB 时也直接入库 `datasheets/`）。
- 归档落地后在沙箱运行 `build.py`（待写）：原始 HTML → `docs/smartbyte/products/<型号>.md`（每型号一页，原文照录 + 基型号匹配价格主表 + Saga 对应型号）、`data/smartbyte_官网型号索引.csv` 全量、品类页/政策页/新闻页 Markdown。

**T15 已用 fetch_page 补齐的非产品页（原文照录）**：固件 5.x / 6.x / 7.0–7.3.x 三篇全文 + 4 篇旧站公司简介（内容相同）→ `新闻与固件说明_2026-10-20.md`；Factory Tour 28 张图注与图片 URL → `公司与政策页_2026-10-20.md` 附录；全站页头/页脚公共信息照录一次。至此 **非产品页 14/14 全部入库**；产品页与品类页等待 Actions 归档（或退回 fetch_page 逐页）。

**入库目录约定（T15 起）**

| 层 | 位置 | 内容 |
|---|---|---|
| 原始层 | `data/smartbyte_site_raw/` | 原样 HTML、sitemap、robots、三份清单（pages / downloads / images）、规格书文本、summary、日志；PDF 视体积入库或进 Release |
| 整理层 | `docs/smartbyte/products/`、`docs/smartbyte/*.md`、`data/smartbyte_官网型号索引.csv` | 可读 Markdown + 索引（由 build.py 从原始层生成，不手改） |
| 规则层 | `docs/reference/Saga商务条款速查.md`、`docs/rules/*` | 只收会影响报价/话术/边界的结论（官网 > 价格表 > Drive） |
