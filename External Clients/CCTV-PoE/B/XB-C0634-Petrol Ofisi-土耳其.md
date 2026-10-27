# XB-C0634 · Petrol Ofisi · 土耳其

> **初判 XB 慢慢跟进** ｜ 来源 CCTV-PoE `profile/new-customers-batch-59-part7-turkey.md`:7 ｜ 导入 2026-10-27 ｜ 研究状态：未研究（第 2 步待做）

## 1. 初判与理由
- 初判：**XB** — 主攻区，类型待核（来源库没写清是渠道还是终端）
- 标记：profile批次文件、多处出现×3、类型待核
- 与 Saga Clients 重叠：按域名未发现（公共邮箱域不参与匹配）
- 规则：编号一次分配、永不重排；深度研究后升降只改「等级」字段并移动文件夹（见 00-总索引）

## 2. 基本事实（来源库口径，未经本库复核）
| 项 | 内容 |
|---|---|
| 公司 | Petrol Ofisi |
| 国家 / 城市 | 土耳其 |
| ISO | TR |
| 网站 | petrolofisi.com.tr |
| 类型 / 角色 | 土耳其最大加油站网络 (Fortinet SD-WAN验证!) |
| 他们首推（仅参考，不照搬） | — |
| 来源章节 | Batch 59 Part 7: 土耳其加油站+EV充电+Baykar+核电+钢铁 > 5渠道: 13K加油站Fortinet验证+38861充电桩+Baykar $2B 30国+Akkuyu 560栋+36.9Mt钢铁 > 渠道AI: 加油站 (4条 = 78,000+ PoE) |
| 来源库字段·城市 | Istanbul |
| 来源库字段·网站 | petrolofisi.com.tr |
| 来源库字段·规模 | **2,700加油站**(收购BP 770站后), 81省700区 |
| 来源库字段·基础设施 | 9燃油码头 + 18机场供油 + 1 LPG码头 + **1.5M m³储罐** |
| 来源库字段·营收 | $14B目标(2025), 土耳其500强#2 |
| 来源库字段·PoE需求 | 2,700站 × PoE(IP摄像头2-4+POS+WiFi AP+EV充电桩+燃油管理) |
| 来源库字段·Saga匹配 | Fortinet已在每站部署交换机=Saga PoE交换机可直接替换/补充 |
| 来源库字段·优先级 | ⭐⭐⭐⭐⭐ |
| 来源文件 | `profile/new-customers-batch-59-part7-turkey.md` 第 7 行 @ elsasaga-cloud/CCTV-PoE@9be1416 (arena/01a0c908-cctv-poe) |
| 同一家在来源库其他位置 | `profile/new-customers-batch-59-part7-turkey.md`:34（关键发现 > 超级PoE切入点）；`03-海外客户开发清单.md`:6194（🇹🇷 Batch 59 Part 7: 土耳其加油站+电动车充电+Baykar无） |

## 3. 联系方式
- 邮箱：无（表单或待挖）

## 4. 关键人（KP）
- 无（待挖）

## 5. 证据与来源 URL（来源库）
- 无

## 6. 已知触达
- Saga S 箱 2026-09/10 群发名单：未匹配到本户邮箱

## 6b. 来源库原文块（原样，含其产品主张——不采信型号与价格）

> - **101.56 Petrol Ofisi** 🇹🇷 A类 | **2,700站**, Fortinet SD-WAN 1800+站已部署, $14B
>
> ——另见 `profile/new-customers-batch-59-part7-turkey.md`:34：
> 1. **Petrol Ofisi**: Fortinet已在1,800+站部署交换机 = Saga PoE可直接替换/补充
>
> ——另见 `03-海外客户开发清单.md`:6194：
> 101.56 Petrol Ofisi — 土耳其最大加油站网络 (Fortinet SD-WAN验证!)
> - **国家**: 🇹🇷 Turkey | **城市**: Istanbul
> - **公司名**: Petrol Ofisi A.Ş. (Vitol集团)
> - **网站**: petrolofisi.com.tr
> - **规模**: **2,700加油站**(收购BP 770站后), 81省700区
> - **基础设施**: 9燃油码头 + 18机场供油 + 1 LPG码头 + **1.5M m³储罐**
> - **营收**: $14B目标(2025), 土耳其500强#2
> - **网络架构(已验证PoE!)**:
>   - **Fortinet SD-WAN** 覆盖**1,800+站**
>   - Türk Telekom扩展至**2,700站SD-WAN**(2024, 全球最大SD-WAN之一)
>   - Fortinet防火墙+**交换机+FortiAP WiFi** 每站部署
>   - 中央管理, 近100%可达性
>   - "Fortinet enables us to differentiate between all types of traffic"
> - **PoE需求**: 2,700站 × PoE(IP摄像头2-4+POS+WiFi AP+EV充电桩+燃油管理)
>   - **16,200+ PoE端口**

## 7. 我方产品线提示
- HRUI PoE 非管理型为主 + SmartByte PoE 管理型（安防/CCTV 渠道：价格 + 交期 + 长距 PoE）
- 报价规则：SmartByte CNY 成本 +20/25/30%（分销 20 / 集成 25 / OEM 30）→ USD；报价前查 `data/价格主表.csv` / `_HRUI.csv`；格式 `$xx USD EXW（快照日期，15 天有效）`
- 对外材料：英文；不写电话；不提供应商/客户/同行名；证书按国别（CE/RoHS/FCC/UKCA/EAC…）

## 8. 研究与跟进（第 2 步起填）
- 研究状态：未研究
- 研究结论 / 升降建议：—
- 下一步：—
