# XA-M319 · Security 101 - Rochester NY · 美国

> **现判 XC 暂不管** ｜ 来源 mikrotik-info `A-126`（原评级 A，阶段 01-contacted） ｜ 导入 2026-10-27 ｜ 研究状态：已研究（W1-R02 2026-10-27）→ 下一动作 并线
>
> **C 池三闸筛选（External 同法，`data/external_clients/sieve_x.json`）：留 XC 储备**（随 Saga `XA-M318`）（闸 0 · DUP · 2026-10-29）：第 2 步研究卡：与 XA-M318 同一公司 → 并线，随主档，不单独判

## 1. 初判与理由
- 初判：**XA** — 主攻区（美加/欧/土）+ 渠道型买家 + 有可用商务邮箱
- 研究后改级：XA → **XC**（W1-R02，同品牌连锁，并入 XA-M318 → C）；编号不变
- 标记：S箱已群发、库内重复
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 库内重复：与来源库 `A-125` 同域名，研究时合并判断
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Security 101 - Rochester NY |
| 国家 / 城市 | 美国 / Rochester, NY |
| ISO | US |
| 网站 | https://www.security101.com/rochester |
| 类型 / 角色 | 集成商/代理（Allied Telesis） |
| 在卖品牌（反向信号） | Allied Telesis（Marvell Prestera 接入层） |
| 自有品牌 | 否 |
| 切入点（来源库） | Marvell 接入层生态切入 |
| 组织 / 模式（来源库推断） | 公司/工作室（有官网） / 工程/集成项目制 |
| 他们首推（仅参考，不照搬） | STC-424XGGPM-280W |
| 来源库优先级 / 状态 | ★★★ / 01-已跟进一轮（用户报告；具体日期/收件人未逐户记录） |
| 来源库之来源 | 厂商官方渠道名录 |
| 来源库备注 | 与 Security 101 - CT 同品牌不同实体，**注意别重复触达**。 【2026-09-27 联系方式核验】公开邮箱·一方/伙伴来源。官网 2023 年 PGA 项目新闻公开 Owner/CEO Victor Wainwright 邮箱；另有当前地方服务邮箱 rochester-service@security101.com。具名职位属历史披露，未验证任职延续。 来源：[3](https://www.security101.com/blog/security-101-helps-secure-the-pga-championship-with-mobile-surveillance) [1](https://www.security101.com/rochester) |
| 来源库评级依据 | 【人工定级】A —— 自动规则已跳过；人工指定 |
| 来源库人工定级 | A |
| 来源文件 | `profile/A/A-126-Security 101 - Rochester NY-美国.md` @ elsasaga-cloud/mikrotik-info@a60f11f8 (arena/01a0c3ef-mikrotik-info)（更新 2026-10-12） |

来源库「基本事实」表（原样）：

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | Security 101 - Rochester NY（CSV 原样；登记名以调研为准） | 事实 |
| 国家/城市 | 美国 / Rochester, NY | 事实 |
| 网站 | https://www.security101.com/rochester | 事实 |
| 类型 | 集成商/代理（Allied Telesis） | 事实（CSV 名录口径） |
| 反向信号（资质/品牌） | Allied Telesis（Marvell Prestera 接入层） | 事实（名录/自报口径） |
| 组织性质 | 公司/工作室（有官网） | 【推断】 |
| 商业模式 | 工程/集成项目制 | 【推断】 |
| 团队规模 | 有官网组织，规模未量化 | 【推断】 |
| 决策链 | 中（联系人+业主/采购两层以内） | 【推断】 |

## 3. 联系方式
- 邮箱：victor.wainwright@security101.com（首选）
- 邮箱：rochester-service@security101.com（公开）
- 来源库入口字段：victor.wainwright@security101.com [Publicly listed; delivery not tested]; https://www.security101.com/rochester

来源库「联系方式」段原文：

> - **邮箱**：victor.wainwright@security101.com
>   - 状态：既有/公开
> - **电话**：—
> - 来源等级：official（R41–R48 联系方式台账口径）
> - **原始联系字段**：victor.wainwright@security101.com [Publicly listed; delivery not tested]; https://www.security101.com/rochester

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- https://www.security101.com/rochester

## 6. 已知触达
- Saga S 箱群发：「24 Port PoE Managed Switch」→ rochester-service@security101.com，首次 2026-09-29，最后 2026-09-29，去信 1，来信 0（对账源 `data/gmail_s/2026-09_10群发名单_未入库.csv`；来信含自动回复，需人工看）

## 7. 我方产品线提示
- SmartByte 商用管理型（Marvell）为主 + Saga STI 工业系列补位（MikroTik/Allied/工业品牌渠道，缺的是性价比管理型与工业 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究卡（第 2 步，W1-R02，2026-10-27）

- **结论：XC** — 同品牌连锁，并入 XA-M318 → C
- 活着吗：来源库 2026-09-27 核对在线；本轮未复查
- 一句话：= XA-M318 Security 101（同品牌 Rochester 分部）；Marvell 接入层生态切入
- 是什么人：= XA-M318 Security 101（同品牌 Rochester 分部）；规模：未量化
- 在卖/在用：Allied Telesis（Marvell Prestera 接入层）
- 对口哪条线：—
- 找得到人吗：victor.wainwright@security101.com（来源库公开邮箱）；KP：无具名
- 已触达：S 箱 2026-09-29 群发「24 Port PoE Managed Switch」→ 已发未回
- 与 Saga Clients：无
- **下一动作：并线** — 分销首触：24 口 PoE + STI 工业线；型号 STC-424XGGPM-280W / STI-288DGGPM；价 USD 170 EXW Shenzhen (snapshot 2026-10-27, valid 15 days) / USD 137 EXW Shenzhen (snapshot 2026-10-27, valid 15 days)

证据：
| 类型 | 说明 | 摘录 | 来源 | 日期 |
|---|---|---|---|---|
| 来源库官网/名录核对 | 与 Security 101 - CT 同品牌不同实体，注意别重复触达。 【2026-09-27 联系方式核验】公开邮箱·一方/伙伴来源。官网 2023 年 PGA 项目新闻公开 Owner/CEO Victor Wainwright 邮箱；另有当前地方服务邮箱 rochester-service@security101.com。具名职位属历史披露，未验证任职延续。 来源：[3](https://www.security101.com/ |  | https://security101.com/ | 2026-09-27 |
| S 箱群发记录 | S 箱 2026-09-29 发 connecticut-service@security101.com「24 Port PoE Managed Switch」，去 1 来 0 |  | data/gmail_s/2026-09_10群发名单_未入库.csv | 2026-09-29 |

- 备注：轻卡：本轮未外查，沿用来源库官网/名录核对。
