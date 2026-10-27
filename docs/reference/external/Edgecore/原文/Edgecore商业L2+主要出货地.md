# Edgecore 商业 L2+ 主要出货地

> **文档类型**：市场/出货地分析（按 mikrotik-info 同等范式处理）
> **撰写时间**：2026-10-18 17:40:00 (Asia/Shanghai)
> **数据来源**：Edgecore 官网 Where-to-Buy 全球渠道名录（2026-10-18 采集，见 `Edgecore客户数据库.xlsx` 渠道伙伴库 198 条）、Edgecore 案例/新闻稿、公开经销商报价（Baltic Networks / Streakwave / CDW / Getic 等）
> **用途**：判断 Edgecore 商业 L2+（ECS 系列）的真实出货重心，指导我方区域开发顺序

---

## 1. 渠道版图总览（Where-to-Buy 收录统计）

| 大区 | 分销商 | SI/VAR/经销商 | 电商 | 特征 |
|---|---|---|---|---|
| 北美 | 12 | 26 | 3 (CDW/Insight/Colfax) | 渠道最密：TD SYNNEX、Tech Data、Avnet、Anixter、WWT、TESSCO、SHI |
| EMEA | 23 | 43 | — | 欧洲最全：德/荷/英/法为轴，辐射中东、非洲、巴基斯坦 |
| 亚太 | 29 | 38 | — | 东南亚/南亚/东北亚全覆盖，越南/泰国/韩国/印度密度高 |
| 印度次大陆 | 5 | 10 | — | 印度为主，孟买/班加罗尔/德里 |
| 独联体 | 4 | 2 | — | 高加索+乌克兰+白俄/乌兹别克 |
| 拉美 | 0（当前名录空） | 0 | — | 弱区，多通过北美渠道辐射 |

## 2. 商业 L2+（ECS 系列）出货重心判断

### 🥇 第一梯队：北美（ISP/WISP + 企业接入）
- ECS4100/4125/4150/4155 系列公开报价主要出现在 **Baltic Networks、Streakwave、Newegg Business、CDW、Amazon** 等北美渠道。
- 案例侧：大量美国 ISP/WISP（Amplex、Haefele Connect、Nextlink、MetaLINK、Dojo Networks）用 Edgecore 做接入/聚合。
- **买家画像**：WISP/中小 ISP、园区集成商、MSP——要 ERPS、PoE、IGMP（IPTV/监控）、性价比。
- 对我方意义：这是 Edgecore L2+ 的**定价锚市场**，也是我方 CCTV/PoE/L2+ 线的目标市场（客户已在亚洲供应链里）。

### 🥈 第二梯队：欧洲（西欧技术渠道 + 东欧性价比市场）
- 德/荷/英/法：专业开放网络分销（STORDIS、Circle B、Xantaro、ADN、Infradata、Exclusive Networks）+ 区域 SI。
- 案例：LINX、AnschlussWerk（德）、Prosoluce（法）、ITandTEL（奥）、IPNexia/Deca（比）。
- **买家画像**：技术型 SI/ISP，认 CLI/MIB/开放网络，价格敏感度中等。
- 对我方意义：**技术型客户主场**——深度定制（UI/CLI/MIB）在这里最值钱；东欧（波兰/罗/匈/塞/保）打性价比。

### 🥉 第三梯队：东南亚 + 南亚（进口习惯强、价格敏感）
- 越南（NETMARK/PAVANA/SSS/FPT/NDC/NETCOM）、泰国、印尼、菲律宾、马来、新加坡、印度、孟加拉、尼泊尔、巴基斯坦。
- 案例：Lang Son City（越南）、ITM University（印度）、印度多家 SI。
- **买家画像**：分销/项目商，中国进口熟手（离供应链近），CCTV/PoE 需求大。
- 对我方意义：**首攻区域**——地理/供应链/价格三重契合，PoE/CCTV/L2+ 直接对位。

### 第四梯队：东北亚（韩/日/台）
- 韩国 SI 群体很大（约 10 家），日本是大商社（ITOCHU/MACNICA/APRESIA/三井/NEC NSI），台湾本地渠道。
- 对我方意义：**谨慎**——韩国要 KC 认证（我方没有），日本门槛高；仅接无强制认证的小项目或做长期池。

### 第五梯队：中东/非洲/独联体（新兴、价格驱动）
- 巴基斯坦三家、MBUZZ/迪拜自由区、东非 Mart Networks 四国、高加索/白俄/乌兹别克。
- **买家画像**：价格敏感、转口活跃、项目小而多。
- 对我方意义：性价比+交期+灵活付款，正中我方打法；弱化品牌、强化方案与价格让利。

## 3. 产品×市场速查

| 场景 | 主销区域 | 对应 Edgecore 产品 | 我方对位产品 |
|---|---|---|---|
| ISP/园区接入 PoE | 北美、东南亚、中东 | ECS4150-28P/54P、ECS4155-30P | Smartbyte Marvell PoE 系列 |
| CCTV 接入 | 全球（新兴市场尤甚） | ECS4100 PoE 型号 | CCTV 专用交换机（主力） |
| 10G 汇聚 | 北美/欧洲 ISP、企业 | ECS4150-54T(SFP28)、ECS5550 | CENTEC 10G SFP+ 汇聚（hohunet） |
| 工业 | 欧洲（匈/德/斯洛文尼亚） | ECS4150-x-I | 工业级全线 |
| 数据中心/白盒 | 北美/欧洲/运营商 | AS 系列+SONiC | **不做**（避开） |

## 4. 开发顺序建议（结合我方策略）

1. **首攻**：东南亚（越南→泰/印尼/菲/马）+ 巴基斯坦/孟加拉——进口习惯、价格敏感、CCTV/PoE 对口。
2. **次攻**：东非 Mart Networks 体系、独联体 FIBERGET/NAGTECH、中东迪拜自由区——转口/新兴市场。
3. **技术线跟进**：欧洲中小 SI/开放网络商（Deca、Pine、STORDIS、Circle B、Cell-Core、Kontron）——深度定制主场，长期培养。
4. **长期池**：北美 WISP/中小 SI（Blue Core、Myriad、Will Jaya 等）+ 韩国 SI 群体（注意 KC）。
5. **观察/情报**：TD SYNNEX/Avnet/ASBIS 等大分销、日系商社——只做情报与背书，不主攻。

---

*配套文件：`Edgecore客户数据库.xlsx`、`Edgecore-vs-交换机价值分析.md`、`宪法-对话记录.md`（变更须记录）*
