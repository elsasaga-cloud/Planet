# XC-M115 · Phoebe IDF · 法国

> **现判 XB 慢慢跟进** ｜ 人工改级 2026-10-29：B（Q-76 LT-01 2026-10-29：XC 三闸捞出 → B（Simon U128「直接定为 B」；长期客户群 · 普通跟）；闸 2：○ 电信 / 光传输工程 + 产品分销 25%：PHOEBE Ile de France（Les Ulis；SIRET 412 080 814 00095；1996 起；75 人；子公司 PHOEBE Fibres 供光缆跳线）坐实；ORing 授权分销 → STI / FS 对位（光传输亦合日职线）；contact@phoebe.fr） ｜ 来源 mikrotik-info `C-050`（原评级 C，阶段 未触达） ｜ 导入 2026-10-27 ｜ 研究状态：已研究（LT-T03 2026-10-29）→ 下一动作 不动
>
> **C 池三闸筛选（External 同法，`data/external_clients/sieve_x.json`）：○ P 池 · 正式入池**（闸 3 · G3 · 2026-10-29）：○ 电信 / 光传输工程 + 产品分销 25%：PHOEBE Ile de France（Les Ulis；SIRET 412 080 814 00095；1996 起；75 人；子公司 PHOEBE Fibres 供光缆跳线）坐实；ORing 授权分销 → STI / FS 对位（光传输亦合日职线）；contact@phoebe.fr

## 1. 初判与理由
- 初判：**XC** — 来源库（mikrotik-info）已判 C（细分：B下放·无邮箱（群发触达不到）；依据：【2026-09-23 复核下放】无邮箱（群发触达不到），按「B 只做群发」原则沉 C 待命；全量信息保留，出现以下任一）；Simon 口径「mik 的 C 不碰」→ 关仓前仅存档，不跟
- 人工改级：XB（2026-10-29，Q-76 LT-01 2026-10-29：XC 三闸捞出 → B（Simon U128「直接定为 B」；长期客户群 · 普通跟）；闸 2：○ 电信 / 光传输工程 + 产品分销 25%：PHOEBE Ile de France（Les Ulis；SIRET 412 080 814 00095；1996 起；75 人；子公司 PHOEBE Fibres 供光缆跳线）坐实；ORing 授权分销 → STI / FS 对位（光传输亦合日职线）；contact@phoebe.fr）；编号不变
- 标记：来源C、邮箱已补（X1-02 2026-10-29）
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Phoebe IDF |
| 国家 / 城市 | 法国 |
| ISO | FR |
| 网站 | distribution.phoebe.fr |
| 类型 / 角色 | 分销（ORing 授权） |
| 在卖品牌（反向信号） | ORing |
| 自有品牌 | 否 |
| 切入点（来源库） | 法国分销（distribution 部门） |
| 他们首推（仅参考，不照搬） | STI-488XGGPM（Saga） |
| 来源库优先级 / 状态 | ★★★ / 未触达 |
| 来源库之来源 | ORing经销商名录/2026-09 |
| 来源库备注 | 【待补】本行由分销商名录批量导入，三星依据仅为渠道等级（分销（ORing 授权））与「ORing」，尚无人工核实。建议先查证其是否已有工业交换机 / PoE++ 产品线，再定切入型号 【2026-09-28 R49 复核】域名已无站点（OVH 占位）：distribution.phoebe.fr 返回 OVH「站点未安装」占位页（无内容）；原入口 +33 1 30 67 69 15 保留 证据：[1](https://distribution.phoebe.fr/)；批次：batch/contact_research_2026-09-28_R49_邮箱补录与复筛.json#C-212 |
| 来源库评级依据 | 【2026-09-23 复核下放】无邮箱（群发触达不到），按「B 只做群发」原则沉 C 待命；全量信息保留，出现以下任一情形可重评：①补到邮箱 ②对方主动询价 ③出现 EOL 替换需求 ④冒出内部联系人。原判：三星依据仅为渠道等级，需求未核实，需先查证其是否已有工业/PoE 产品线 |
| 来源文件 | `profile/C/C-050-Phoebe IDF-法国.md` @ elsasaga-cloud/mikrotik-info@a60f11f8 (arena/01a0c3ef-mikrotik-info) |

## 3. 联系方式
- 邮箱：contact@phoebe.fr（公开·X1-02 补）
- 邮箱：phoebe-fibres@phoebe.fr（公开·X1-02 补）
- 来源库入口字段：+33 1 30 67 69 15

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 7. 我方产品线提示
- SmartByte 商用管理型（Marvell）为主 + Saga STI 工业系列补位（MikroTik/Allied/工业品牌渠道，缺的是性价比管理型与工业 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究卡（第 2 步，LT-T03，2026-10-29）

- **结论：XC** — X1-02 补路径：○ 电信 / 光传输工程 + 产品分销 25%：PHOEBE Ile de France（Les Ulis；SIRET 412 080 814 00095；1996 起；75 人；子公司 PHOEBE Fibres 供光（等级不动，池位见 sieve_x）
- 活着吗：快照失败（distribution.phoebe.fr：HTTP 错误，2026-10-29，第 1 次）
- 一句话：PHOEBE Ile de France（SIRET 41208081400095）：电信 / 光传输工程 + 子公司 PHOEBE Fibres 供应光缆跳线（ORing 授权分销 distribution.phoebe.fr）；1996 起；75 人（Verif）/ 51–200（LinkedIn）
- 是什么人：分销（ORing 授权）；PHOEBE Ile de France（SIRET 41208081400095）
- 对口哪条线：Saga STI 工业 / SmartByte 商用 PoE — ○ 电信 / 光传输工程 + 产品分销 25%：PHOEBE Ile de France（Les Ulis；SIRET 
- 找得到人吗：contact@phoebe.fr（官网 / 名录公开（X1-02 补路径））；KP：无具名
- 已触达：未触达（路径 2026-10-29 新补）
- 与 Saga Clients：无
- **下一动作：不动** — 已入 P 池 → 按巡检节奏首触

证据：
| 类型 | 说明 | 摘录 | 来源 | 日期 |
|---|---|---|---|---|
| 官网 / 名录 | Verif：PHOEBE ILE DE FRANCE · SIRET 41208081400095 · 4 Av du Parana Les Ulis · 75 人 |  | https://www.verif.com/en/company/PHOEBE-ILE-DE-FRANCE-68d9cecd12992303385b6963/ | 2026-10-29 |
| 官网 / 名录 | 官网新闻：PHOEBE Fibres 子公司 · phoebe-fibres@phoebe.fr · 总部 Les Ulis 01 85 41 03 00 |  | http://phoebe-telecoms.com/news-detail/phoebe-fibers.html | 2026-10-29 |
| 官网 / 名录 | LinkedIn：51–200 人 · 1996 · contact@phoebe.fr |  | https://tt.linkedin.com/company/phoebe-ile-de-france?trk=similar-pages_result-card_full-click | 2026-10-29 |

- 备注：LT-T03 官网快照加厚（2026-10-29）：alive/fail#1。
PHOEBE Ile de France（SIRET 41208081400095）；4 avenue du Paraná, 91940 Les Ulis（+ Aquitaine / PACA 分部）；SIRET 412 080 814 00095；+33 1 85 41 03 00
