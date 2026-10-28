# XB-C0586 · DIPOL sp. z o.o. · 波兰

> **现判 XA 长期跟进** ｜ 来源 CCTV-PoE `profile/poland-part1-deep-mining.md`:17 ｜ 导入 2026-10-27 ｜ 研究状态：已研究（W3-R06 2026-10-28）→ 下一动作 首触

## 1. 初判与理由
- 初判：**XB** — 主攻区，类型待核（来源库没写清是渠道还是终端）
- 研究后改级：XB → **XA**（W3-R06，PL 老牌分销、邮箱已补 → 升 A 首触（排 2027-W03））；编号不变
- 标记：profile批次文件、多处出现×2、类型待核
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | DIPOL sp. z o.o. |
| 国家 / 城市 | 波兰 |
| ISO | PL |
| 网站 | — |
| 类型 / 角色 | — |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | 波兰深度挖掘 Part 1 - 10个渠道 (104-113) > 104. 安防分销商 (Hikvision/Dahua/Uniview授权) > Hikvision Poland |
| 来源文件 | `profile/poland-part1-deep-mining.md` 第 17 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |
| 同一家在来源库其他位置 | `03-海外客户开发清单.md`:9930（104. 波兰安防分销商 (Hikvision/Dahua/Uniview授权分） |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> - **DIPOL sp. z o.o.** - Kraków
>
> ——另见 `03-海外客户开发清单.md`:9930：
> 6. **DIPOL sp. z o.o.** - Kraków

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究卡（第 2 步，W3-R06，2026-10-28）

- **结论：XA** — PL 老牌分销、邮箱已补 → 升 A 首触（排 2027-W03）
- 活着吗：本轮 web_search 复核在线（2026-10-28）
- 一句话：弱电设备欧洲分销 + 天线制造（DIPOL Sp.J.，Kraków；1990 起；CCTV/WLAN/TV-SAT；2,000+ 品类；批发 + 零售 + 安装商；英文站 dipolnet.com）
- 是什么人：弱电设备欧洲分销 + 天线制造（DIPOL Sp.J.，Kraków；1990 起；CCTV/WLAN/TV-SAT；2,000+ 品类；批发 + 零售 + 安装商；英文站 dipolnet.com）；规模：未量化
- 对口哪条线：SmartByte 商用 L2+ + HRUI 入门 PoE + Saga STI 工业 L2+ PoE — 欧洲级分销 + 自产天线 → 对 OEM/自有标签熟悉
- 找得到人吗：dipol@dipol.com.pl（来源库公开邮箱）；KP：无具名
- 已触达：S 箱 9–10 月群发名单未见本域 → 未触达
- 与 Saga Clients：无
- **下一动作：首触** — 分销三件套：HRUI 24 口 + SmartByte 24 口 L2+ + STI；型号 STC-2224GP / STC-424XGGPM-280W / STI-288DGGPM；价 USD 86 / USD 170 / USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)；窗口 PL 周四 12–14；建议 2027-01-21

证据：
| 类型 | 说明 | 摘录 | 来源 | 日期 |
|---|---|---|---|---|
| 来源库官网/名录核对 |  |  |  | 2026-09-28 |
| 本轮网查 | 官网：Założona w 1990 roku firma DIPOL jest europejskim dystrybutorem…oraz producentem anten；dipol@dipol.com.pl | Dipol - europejski dystrybutor CCTV, WLAN, TV-SAT oraz producent anten. Oferujemy ponad 2000 towarów | https://www.dipol.com.pl/firma_dipol_m110.htm | 2026-10-28 |

草稿（英文，首触；Simon 发，Agent 不发）：

```text
Subject: PoE switch line for your reseller channel - distributor pricing

Hi,

Saga Telecom supplies network and security distributors in Europe and North America with PoE and industrial switches; we are an engineering and supply-chain-first telecom partner, so you deal directly with the people who specify the product.

Three PoE switches our distributor partners move most, all EXW Shenzhen (snapshot 2026-10-27, valid 15 days), CE, under our label or yours:

- STC-2224GP: 24 x GE PoE+ (300 W) + 2 x GE + 2 x SFP, USD 86.
- STC-424XGGPM-280W: 24 x GE PoE+ (280 W) + 4 x 10G SFP+, Marvell-based L2+ managed, USD 170.
- STI-288DGGPM: DIN-rail industrial L2+, 8 x GE PoE+ (240 W) + 2 x SFP, -40 to +75 C, USD 137, 3-year warranty (12 months on the commercial units).

Who on your product team looks after new networking vendors, and would a sample or a price sheet be the better first step?

Simon
Saga Telecom - sagatele.com
```

- 备注：本轮网查复核（2026-10-28，证据见 §8「本轮网查」条）。
