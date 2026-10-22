# HRUI「ZX-/SWTG」硬件族的开源生态（GitHub 侧爬，2026-10-22T13:31Z）

> 来源：GitHub REST API（`gh api search/repositories|search/code`，沙箱可直连 github.com），抓取时间 2026-10-22T13:31Z。T29-U13 ③ 范围「所有相关网站」补充项。全部原样入库，不裁决。

## 1. 命中清单（全部为公开仓库）

| 仓库 | 事实 | 抓取依据 |
|---|---|---|
| `brennoo/terraform-provider-hrui`（★56，MPL-2.0，建 2024-10-20，最近推送 2026-09-19） | README：「Terraform provider for **HRUI** (https://www.hruitech.com) switches that are web-managed」；用 **Horaco ZX-SWTG124AS** 开发；「Other brands that are likely to work … same hardware: **HRUI, Horaco, Sodola, XikeStor, AmpCom, KeepLink**」；支持固件 v1.9 / v1.9.1；Terraform Registry + OpenTofu 均已发布 | `repos/brennoo/terraform-provider-hrui/readme` |
| `logicog/RTLPlayground`（★635，建 2025-05-10，推送 2026-10-21）「Firmware development for RTL8372/RTL8373 based 2.5GBit Switches」 | `doc/supported_devices.md` 列出同一 **SWTG0xxAS PCB 族** 的贴牌品牌与 PCB 版本：Horaco HC-SWTG124AS / HC-SWTGW215AS / HC-SWTGW218AS / ZX-SWTG124AS / ZX-SG4T2 / ZX310S-4T2XH；**LIANGUO ZX-SWTGW215AS**（PCB-SWTG115AS-V2.0/2.1）；MokerLink ZX-SWTGW218AS（SWTG118AS-V2.0）；Sodola SL-SWTG124AS-D；XikeStor SKS3200M-4GPY2XF / SKS3200-8E1X；AmpCom WAM902-SWTG018AS；GoodTop GT-ST018M/024M；keepLINK KP-9000 系列；Binardat；Hisource；YuanLey；**TRENDnet TEG-S562**（PCB TEG-S563/EU）等 | `repos/logicog/RTLPlayground/contents/doc/supported_devices.md` |
| `openwrt/openwrt`（主线） | DTS：`rtl9303_horaco_zx-swtgw2c8f.dts`（compatible `horaco,zx-swtgw2c8f`，**RTL9303**，8×10G SFP+ Web 管理）、`rtl9313_horaco_zx-swtgw2c48ns.dts`（`horaco,zx-swtgw2c48ns`，**RTL9313**）、`rtl9303_lianguo_lg-swtgw3c8f.dts`（**与 Horaco 共用同一 dtsi** → Lianguo = 同硬件另一贴牌）；提交 2026-07-14「add SFP thermal zone」、2026-09-28「split Horaco ZX-SWTGW2C8F DTS」—— 主线活跃维护 | `repos/openwrt/openwrt/contents/target/linux/realtek/dts/…`、commits API |
| `up-n-atom/SWTG118AS`（★293，建 2024-01-30，推送 2026-07-08）「SWTG###AS RE」 | SWTG118AS 板逆向指南（RTLPlayground 引用为「Up-N-Atoms 2.5 GBit RTL Switch hacking guide」） | repo meta |
| 其他 | `coolsnowwolf/lede`、`lede-project/source` 同步了上述 DTS；`Anime4000/RTL960x` Docs/2.5Gb.md 提及；`MarkTing2web/SV-Build` 有 `brands/hrui-network.html`（静态页，未读） | search/code 共 159–168 条命中 |

搜索为 0 的：`smartbyte switch`、`hohunet`、`LT-S8328`、`LT-IS6318`、`hrgdkj`、`smartbyte-switch`（仓库搜索均 0）；`hruitech` 代码搜索 5 条（仅 terraform-provider-hrui + 域名清单噪音）。

## 2. 对 Saga 的含义（推断，标注）
1. **HRUI 的 2.5G / 10G Web 管理线 = Amazon/AliExpress 消费品牌（Horaco、Sodola、XikeStor、MokerLink、AmpCom、keepLINK、Lianguo…）的同一硬件族**；Saga 的 STC-15XGDGE/18XGDGE/24XGDGWE/216XGDGWE/80XGWO 等对应 ZX-SWTG015AS/018AS/W224AS/W2216AS/W2C8F —— 这些型号在零售端有公开价格（亚马逊 4×2.5G+2×10G 约 $40–60 档），**是 Saga 对 B 端报价的天花板**，也是客户一搜就能发现的「同款」。
2. 「ZX-」前缀不只是 Saga 合同里的中性码：Horaco / MokerLink / Lianguo 的零售型号本身就叫 ZX-SWTGxxx，说明 **ZX = 这一硬件族的 ODM 原始码**；HRUI 规格书用 ZX 码、官网用 HR 码。ZX 的真正归属（HRUI 自研 PCB，还是 HRUI 也从「Lianguo/联国」等板厂取板）**未证实**，两种可能并存。
3. 开源固件（OpenWrt 主线支持 RTL9303/9313 机型；RTLPlayground 支持 RTL8372/8373 机型）= 这族硬件在 homelab / 极客渠道有「可刷机」口碑；对 Saga 的工业/工程客户意义不大，但对欧美 e-tailer / 小众品牌是卖点，也意味着**固件安全/锁机问题会被公开讨论**。
4. TRENDnet TEG-S562 与该 PCB 族同板 → 该硬件族已供货美国品牌（TRENDnet 为台资美企，按 INH 规则不是客户，仅记事实）。

## 3. 与库内资料的交叉
- `data/pi_orders/采购合同明细.csv`：Saga 向 HRUI 采购的 14 个 ZX 码里，ZX-SWTG015AS / 018AS / 1216AS / 1224AS / 1C8F / W2216AS / W2224AS / W2C80N 全部属于这一族（见 `docs/reference/实际进价与毛利_校验_2026-10-22.md` §3 推断表）。
- `data/hrui_STC对照表.csv`「规格书2026-10(ZX型号)」列 51 个 ZX 码 = HRUI 规格书原码。
- `docs/suppliers/HRUI/00-画像与资料地图.md` §8 已追加本节摘要。
