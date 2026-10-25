# fibotelecom.ru
**官方名称（调研核实）**：FIBO-TELECOM（fibotelecom.ru，Russia；光通信产品分销商，自有品牌 FIBO / FT-）

> **评级 B**　|　俄罗斯　|　档案编号 `SB-028`　|　优先级 ★★　|　状态：成交过·维护
>
> **类型**：运营商/光传输采购（待补证）（推断）　|　**历史关系**：成交/下单过　|　**所在清单**：DWDM线索、在用同行产品　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）

```yaml structured_profile
code: SB-028
rating: B
rating_auto: A
rating_research: B  # DWDM 品类非 Saga 主线（三供应商中仅 Hohunet 有 10G+/DC 线，无 DWDM 整机），俄罗斯非主攻区，且 0 互动 → 不具备 A 的'
name_official: "FIBO-TELECOM（fibotelecom.ru，Russia；光通信产品分销商，自有品牌 FIBO / FT-）"
score: 71
country: 俄罗斯
region: 俄语区
website: fibotelecom.ru
type: 运营商/光传输采购（待补证）
tier_tags: ["DWDM线索", "在用同行产品"]
deal: yes
replies: 0
followups: 0
first_contact: unknown
last_contact: unknown
s_mail: 6 msgs (out 6 / in 0), 2024-07-11 -> 2025-01-21
p1: STC-28DGGPM
price_tier: 30%
research: done
site_snapshot: ok  # 2026-10-21
sources: 2
updated: 2026-10-25
```

## SALES BRIEF（压缩模型）

- **是谁**：俄罗斯光通信产品分销商 FIBO-TELECOM（8 (800) 550-22-45；自有品牌 FIBO 兼容 SFP（FT-S1-C…CWDM 等）、PoE 交换机 FT-S118FP-2T1S（8 FE PoE + 2 GE + 1 SFP）4,841 ₽、FT-S1116FP-2T1S 11,133 ₽；DK 系列管理交换机：DK2110M-8T2S（Marvell，L2 8 GE + 2 SFP）21,424 ₽、DK2110R-8T2S（Realtek）16,664 ₽、DK2110M-24T4S（Marvell）27,614 ₽、DK2310R-24T4X（L3 Realtek 24 GE + 4 SFP+）42,850 ₽（含 VAT）；媒体转换器、DWDM）。用户表（MIPS 2024；DWDM CENTEC 线索）：采购 Anastasia Roshchupkina；买过飞宇的产品；兴趣光模块 PON、SFP、MC；备注链接其交换机目录。自有品牌 + Marvell/Realtek 双线与 Saga 完全同构 → OEM 30%（贴 FIBO 牌）。（调研 2026-10-21；表内兴趣：光模块 PON；SFP MC(光路的)  DPtek客户   后边链接）
- **为什么是 B 级**：**调研后定级 B**（DWDM 品类非 Saga 主线（三供应商中仅 Hohunet 有 10G+/DC 线，无 DWDM 整机），俄罗斯非主攻区，且 0 互动 → 不具备 A 的'可追溯需求+可赢'条件，降 B 待机。）；自动分级 A：+50 有成单/下单/买过记录（用户备注或跟进表）；+10 用户二筛：在用 Utepo/ONV/Ewind 等同行产品（贴牌切入口）；-8 DWDM/光传输线索：Saga 不做 DWDM（Hohunet 线为交换机）；+2 兴趣仅 MC/SFP/配件（边缘品类）；+10 有企业邮箱；+5 有可核实的公司网站/域名；+0 区域 俄语区/俄罗斯；+2 最近活动 2024
- **历史互动**：成交/下单过
- **P1（下一步唯一主推 · 来自针对性复盘 2026-10-24）**：STC-28DGGPM — OEM 30% 档：STC-28DGGPM（Marvell 2 SFP + 8 GE PoE+ L2+，$87.4）对位 DK2110M-8T2S 的 PoE 版；Realtek 线 STC-28GPM（$62.2）对位 DK2110R；L3 STC-424XGGM(L3)（$291.5）对位 DK2310R-24T4X；Realtek 线按 HRUI 2026-09-30 进价 +30% 现算（Q-47 默认，不用 Drive 旧表价）：STC-28GPM $62.2→$77.0；按主表（研究档 saga_fit）；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-08-09 $220（48 port managed switch）；群发里他已看到的价（续，第 66 批全量复核）：2025-01-21 $240（24 Port Fiber Switch）
- **第一问（只问一个）**：Анастасия, по вашей линейке DK: мы делаем те же платформы — Marvell L2+ 2 SFP + 8 GbE PoE+ под маркой FIBO 87,4 USD EXW, Realtek L2 версия 77,0 USD, L3 24 GbE + 4×10G 291,5 USD, прошивка с вашим логотипом. Какую модель DK вы сейчас закупаете в наибольшем объёме?
- **最大未知**：年走量与现供应商
- **下一步**：群发节奏 A 邮箱 观察打开

## 针对性复盘（邮件 / PI / Drive 证据 · 2026-10-24）

> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py SB-028` 可复现）+ PI 包 + Drive 资料；复盘日期 2026-10-24。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**

- **绑定等级：未触达（S 邮箱 6 封 2024→2025，无记录打开，0 回；收件 info@fibotelecom.ru；主题多为「PoE Switch、48 port managed switch」；Elsa 箱：`to:fibotelecom.ru` 逐户查 0（2026-10-25，complete，To/Bcc 同查） → Elsa 箱从未发过本户，往来只在 S/A 箱（去 6 / 来 0）（第 74 批(l)））** ｜ 类型：运营商/光传输采购（待补证） ｜ 筛子：1（只收到群发） ｜ 停点：只打通用邮箱，无记录打开 ｜ 复活：保持季度群发到 2027-Q1；无打开即停 ｜ 通路：RU 次级（Simon 2026-08 点名） ｜ 节奏：季度 ｜ 证据：gmail_digest：out 6；用户表：「光模块 PON / SFP MC(光路的) DPtek客户 / Anastasia Roshchupkina Purchasing / 买了飞宇的 / http」；研究档 risks：俄罗斯结算/物流；已有稳定中国供应商（飞宇等）；无互动记录
- **现状一句话**：俄罗斯光通信产品分销商 FIBO-TELECOM（8 (800) 550-22-45；自有品牌 FIBO 兼容 SFP（FT-S1-C…CWDM 等）、PoE 交换机 FT-S118FP-2T1S（8 FE PoE + 2 GE + 1 SFP）4,841 ₽、FT-S1116FP-2T1S 11,133 ₽；DK 系列管理交换机：DK2110M-8T2S（Marvell，L2 8 GE + 2 SFP）21,424 ₽、DK2110R-8T2S（Realtek）16,664 ₽、DK2110M-24T4S（Marvell）27,614 ₽、DK2310R-24T4X（L3 Realtek 24 GE + 4 SFP+）42,850 ₽（含 VAT）；媒体转换器、DWDM）。用户表（MIPS 2024；DWDM CENTEC 线索）：采购 Anastasia Roshchupkina；买过
- **对方真实需求（有据）**：OEM 30% 档：STC-28DGGPM（Marvell 2 SFP + 8 GE PoE+ L2+，$87.4）对位 DK2110M-8T2S 的 PoE 版；Realtek 线 STC-28GPM（$62.2）对位 DK2110R；L3 STC-424XGGM(L3)（$291.5）对位 DK2310R-24T4X
- **断点 / 为什么停在这里**：俄罗斯结算/物流；已有稳定中国供应商（飞宇等）；无互动记录
- **Saga 现在该推什么**：P1 **STC-28DGGPM**（30% 档，Realtek 线按 HRUI 2026-09-30 进价 +30% 现算（Q-47 默认，不用 Drive 旧表价）：STC-28GPM $62.2→$77.0；按主表（研究档 saga_fit）；群发里他已看到的价（= Simon 实际在用的老表量级；信稿同款不得高于它，要高就先点明原因；2026-06 PDF 的 +10% 从未发出，别提）：2024-08-09 $220（48 port managed switch）；群发里他已看到的价（续，第 66 批全量复核）：2025-01-21 $240（24 Port Fiber Switch））——OEM 30% 档：STC-28DGGPM（Marvell 2 SFP + 8 GE PoE+ L2+，$87.4）对位 DK2110M-8T2S 的 PoE 版；Realtek 线 STC-28GPM（$62.2）对位 DK2110R；L3 STC-424XGGM(L3)（$291.5）对位 DK2310R-24T4X
- **下一步（具体）**：群发节奏　A 邮箱　观察打开
  - 第一问（只问一个）：Анастасия, по вашей линейке DK: мы делаем те же платформы — Marvell L2+ 2 SFP + 8 GbE PoE+ под маркой FIBO 87,4 USD EXW, Realtek L2 версия 77,0 USD, L3 24 GbE + 4×10G 291,5 USD, прошивка с вашим логотипом. Какую модель DK вы сейчас закупаете в наибольшем объёме?

| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |
|---|---|---|---|---|---|
| 2025-01-21 | 去 | S 群发 | PoE Switch、48 port managed switch | 6 封 / 0 次打开 / 0 回｜首封 2024-07-11 → 末封 2025-01-21（6 去 / 0 来） | `gmail_digest` |
| 2026-10-21 | 用户表 | Simon | 光模块 PON / SFP MC(光路的) DPtek客户 / Anastasia Roshchupkina Purchasing / 买了飞宇的 / https://fibotelecom.ru/catalog/kommutatory/k | 表内备注 | `用户表` |

## 基本事实（事实/推断/假设分层）

| 项 | 内容 | 层级 |
|---|---|---|
| 名称 | fibotelecom.ru（取自域名，公司全名待核） | 推断 |
| 国家 | 俄罗斯 | 事实（用户表）|
| 网站/域名 | fibotelecom.ru | 事实（用户表 URL/邮箱域名） |
| 类型 | 运营商/光传输采购（待补证） | 推断（据兴趣/备注关键词） |
| 联系人 | Anastasia Roshchupkina / Purchasing / 买了飞宇的 | 事实（用户表） |
| 来源（From） | MIPS2024 / 富通天下 | 事实（用户表） |
| 兴趣（Interested in） | 光模块 PON / SFP MC(光路的) <br>DPtek客户   后边链接 | 事实（用户表） |
| 用户备注（Remark） | https://fibotelecom.ru/catalog/kommutatory/kommutatory_ethernet | 事实（用户表） |
| 所在清单 | DWDM线索、在用同行产品 | 事实（文件路径） |
| 在卖/在用品牌（备注所见） | — | 事实（用户备注）/ 推断 |

## 客户调研（网页核实 · 引文 + URL + 日期）

- **状态：已调研（2026-10-21）**　网站状态：在线（电商）
- **是谁**：俄罗斯光通信产品分销商 FIBO-TELECOM（8 (800) 550-22-45；自有品牌 FIBO 兼容 SFP（FT-S1-C…CWDM 等）、PoE 交换机 FT-S118FP-2T1S（8 FE PoE + 2 GE + 1 SFP）4,841 ₽、FT-S1116FP-2T1S 11,133 ₽；DK 系列管理交换机：DK2110M-8T2S（Marvell，L2 8 GE + 2 SFP）21,424 ₽、DK2110R-8T2S（Realtek）16,664 ₽、DK2110M-24T4S（Marvell）27,614 ₽、DK2310R-24T4X（L3 Realtek 24 GE + 4 SFP+）42,850 ₽（含 VAT）；媒体转换器、DWDM）。用户表（MIPS 2024；DWDM CENTEC 线索）：采购 Anastasia Roshchupkina；买过飞宇的产品；兴趣光模块 PON、SFP、MC；备注链接其交换机目录。自有品牌 + Marvell/Realtek 双线与 Saga 完全同构 → OEM 30%（贴 FIBO 牌）。
- **类型**：运营商/光传输采购（待补证）
- **规模**：待补证
- **在卖/在用品牌**：飞宇（用户记录）, DPtek（用户记录）, FIBO / FT-（自有品牌）, DK（自有系列）
- **【用户记录】DWDM 线索；0 次跟进；采购联系人具名**
  > DWDM lead, 0 fu, DPtek customer；买了飞宇的；Anastasia Roshchupkina / Purchasing（用户 Clients 表摘录）
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **【网店】DK 系列型号与价格**
  > Коммутатор DK2310R-24T4X L3, 24*10/100/1000Base-T, 4*1G/2.5G/10G SFP+ Realtek 42 849,70 ₽ … DK2110R-8T2S L2, 8*10/100/1000Base-T, 2*1G SFP, Realtek 16 663,62 ₽ … DK2110M-8T2S L2, 8*10/100/1000 Base-T, 2*1000 Base-X SFP, Marvell 21 424,40 ₽ … DK2110M-24T4S L2, 24*10/100/1000Base-T, 4*1G SFP, Marvell 27 614,49 ₽
  > 来源：https://fibotelecom.ru/catalog/kommutatory/kommutatory_ethernet（抓取 2026-10-21）
- **【网店】自有品牌 PoE 交换机**
  > Коммутатор неуправляемый POE FT-S118FP-2T1S 8*10/100M RJ45 POE, 2*10/100M/1000 RJ45 1*SFP, корпус металл … 4 840,92 ₽
  > 来源：https://fibotelecom.ru/catalog/kommutatory/kommutatory_poe（抓取 2026-10-21）
- **【网店】自有品牌 SFP 与电话**
  > FIBO FT-S1-C3940LD совместимый 1G CWDM SFP модуль 1390нм 40км … Звоните 8 (800) 550-22-45!
  > 来源：https://fibotelecom.ru/catalog/sovmestimye_transivery/sfp_transivery/1g_cwdm_sfp_modul_1390nm_40km_ft_s1_c3940ld-compatible-fibo-ft_s1_c3940ld（抓取 2026-10-21）
- **【用户表】MIPS 2024；采购 KP；买过飞宇；目录链接**
  > 光模块 PON / SFP MC(光路的) DPtek客户 / Anastasia Roshchupkina Purchasing / 买了飞宇的 / https://fibotelecom.ru/catalog/kommutatory/kommutatory_ethernet
  > 来源：（本地 Clients/ 表格，无公开 URL）（抓取 2026-10-21）
- **KP**：Anastasia Roshchupkina（Purchasing）roshchupkina@fibotelecom.ru 〔用户 Clients 表〕
- **调研后定级**：B（原自动 A）——DWDM 品类非 Saga 主线（三供应商中仅 Hohunet 有 10G+/DC 线，无 DWDM 整机），俄罗斯非主攻区，且 0 互动 → 不具备 A 的'可追溯需求+可赢'条件，降 B 待机。
- 备注：若 Hohunet CENTEC 10G/25G 汇聚机型对其有用可一次触达；否则不主动跟。

### 加厚挖掘（2026-10-21 · B 级加厚 v1（网店核对））

| 公司事实 | 内容 |
|---|---|
| 法定名称 | FIBO-TELECOM（ООО，全称待核） |
| 总部/地址 | Россия（Москва/СПб 配送；8 800 550-22-45） |
| 其他 | 自有品牌 FIBO / FT-；DK 系列（Marvell 与 Realtek 两条线） |

- **业务线**：兼容 SFP / CWDM-DWDM 模块；交换机（PoE 非管理、L2/L2+/L3 管理）；媒体转换器、PON

| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |
|---|---|---|---|---|
| FIBO DK | DK2110M-8T2S | L2 管理，8 GE + 2 SFP，Marvell；21,424 ₽ 含 VAT | STC-28DGGM/STC-28DGGPM 同平台（PoE 版 $87.4@30） | https://fibotelecom.ru/catalog/kommutatory/kommutatory_ethernet（2026-10-21） |
| FIBO DK | DK2110R-8T2S | L2 管理，8 GE + 2 SFP，Realtek；16,664 ₽ | STC-28GM（列表 $50.6）/ STC-28GPM（$62.2） | https://fibotelecom.ru/catalog/kommutatory/kommutatory_ethernet（2026-10-21） |
| FIBO DK | DK2310R-24T4X | L3，24 GE + 4×10G SFP+，Realtek；42,850 ₽ | STC-424XGGM(L3)（$291.5@30） | https://fibotelecom.ru/catalog/kommutatory/kommutatory_ethernet（2026-10-21） |
| FIBO FT | FT-S118FP-2T1S | 8 FE PoE + 2 GE + 1 SFP 非管理；4,841 ₽ | STC-028GP 千兆升级（$24.2） | https://fibotelecom.ru/catalog/kommutatory/kommutatory_poe（2026-10-21） |

- **触达通道（公开）**：网店: https://fibotelecom.ru/catalog/kommutatory/kommutatory_ethernet；电话: 8 (800) 550-22-45（公开）；邮箱: roshchupkina@fibotelecom.ru / info@fibotelecom.ru（用户表）
- **近况信号**：
  - 自有品牌 DK 系列同时有 Marvell 与 Realtek 版本——与 Saga STI/STC 双线一一对应 → 贴牌第二来源（OEM 30%）
  - 采购 KP 具名（Anastasia Roshchupkina）
- **风险/边界**：俄罗斯结算/物流；已有稳定中国供应商（飞宇等）；无互动记录
- **Saga 对位结论**：P1 STC-28DGGPM（30% 档）——OEM 30% 档：STC-28DGGPM（Marvell 2 SFP + 8 GE PoE+ L2+，$87.4）对位 DK2110M-8T2S 的 PoE 版；Realtek 线 STC-28GPM（$62.2）对位 DK2110R；L3 STC-424XGGM(L3)（$291.5）对位 DK2310R-24T4X
- **邮件切入句（英文）**：Анастасия, по вашей линейке DK: мы делаем те же платформы — Marvell L2+ 2 SFP + 8 GbE PoE+ под маркой FIBO 87,4 USD EXW, Realtek L2 версия 77,0 USD, L3 24 GbE + 4×10G 291,5 USD, прошивка с вашим логотипом. Какую модель DK вы сейчас закупаете в наибольшем объёме?

### 官网快照（自动摘要 · 抓取 2026-10-21 · 状态：在线）

- **首页**：https://fibotelecom.ru/　语言：ru　站点地图 URL 数：4706
- **标题**：Купить телекоммуникационное и сетевое оборудование и кабель по выгодной цене в интернет-магазине с доставкой по РФ
- **描述**：Купить телекоммуникационное и сетевое оборудование и кабель по выгодной цене с доставкой по России. Компания FIBO предлагает заказать информационно-телекоммуникационное оборудование, сетевое периферийное, кабель, серверное, поставки с производства патч-кордов по низкой стоимости от интернет-магазина
- **首页栏目**：Экспертная помощь перед покупкой / Полезная информация / Поддержка всегда рядом / Это интересно
- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：sfp 79、10g 39、industrial 6、telecom 6、ethernet 3、poe 2、2.5g 1、cisco 1
- **站内出现的品牌**：Cisco, Juniper　（「（！）」= Saga 自家/供应商品牌已在其站内出现）
- **站内型号串**（正则抽取，含非交换机）：SFP28, QSFP28, QSFP56, BX20-D-I, FT-DA-17B-LU-A, FT-ODCM-40, FT-S10-D3480LD, FT-S10-D5780LD, MN-AT-MF05LU, MN-PC-LU-LU-SMD3L, MN-PC-LU-LU-SMS3L
- **站内公开邮箱**：info@fibotelecom.ru
- **产品类页面**：https://fibotelecom.ru/catalog/kommutatory/kommutatory_poe；https://fibotelecom.ru/catalog/kommutatory/kommutatory_industrial；https://fibotelecom.ru/catalog/sovmestimye_transivery/industrial_transivery；https://fibotelecom.ru/catalog；https://fibotelecom.ru/catalog/kommutatory；https://fibotelecom.ru/catalog/oborudovanie_pon
- **已抓子页**：[Купить SFP модуль 10G и трансивер SFP 10G по выгодной цене с](https://fibotelecom.ru/catalog/sovmestimye_transivery/industrial_transivery)；[Контакты](https://fibotelecom.ru/for-clients/contacts)；[О нас](https://fibotelecom.ru/company/about)；[Передача 10G на 120 км по одному волокну - FIBO](https://fibotelecom.ru/solutions/dwdm-120-10g-1-fiber)；[Каталоги PDF](https://fibotelecom.ru/fibo-catalog)；[Коммутаторы](https://fibotelecom.ru/catalog/kommutatory)
- 首页正文摘录：Каталог $ ₽ 8 (812) 509-67-89 Покупателям Оплата Статьи Сервис Гарантия Доставка О компании О нас Вакансии Новости Решения Контакты Отгрузка заказа в день оплаты Склады в крупных городах России позволяют выстраивать эффективную логистику доставки товаров Подробнее DWDM проекты любой сложности и под любой бюджет Реализовали 560км со скоростью 200G Подробнее Совместимые трансиверы Активное оборудование Оборудование PON
- **自动对位建议**：STI-288GP（官网快照对位：工业/自动化词频 6、PoE 2 → DIN 8 PoE+ 2 SFP 起手；仅在无人工对位时作为 P1）
- 数据文件：`data/saga_clients/site_snapshots/SB-028.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。

## 在卖/在用品牌 → Saga 对位

（备注未提及具体品牌）

## 历史跟进记录（原表照录）

（无跟进表记录）

## 邮箱往来（S 邮箱 · 自动汇总）

- **账号**：s.sagatelecom　|　**邮件**：6 封（去 6 / 来 0）　|　**期间**：2024-07-11 → 2025-01-21　|　**最后去信**：2025-01-21
- **对方邮箱**：info@fibotelecom.ru
- 对方从未回信（全部为我方去信）
- **邮件里报过的价**：2025-01-21 $240；2024-08-09 $220

| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |
|---|---|---|---|---|---|
| 24 Port Fiber Switch | 2025-01-21 | 2025-01-21 | 0 | 1 | 1 |
| 2.5G Web Managed Switch | 2024-12-25 | 2024-12-25 | 0 | 1 | 1 |
| 24 Port Passive PoE Switch | 2024-10-14 | 2024-10-14 | 0 | 1 | 1 |
| Web managed switch | 2024-09-05 | 2024-09-05 | 0 | 1 | 1 |
| 48 port managed switch | 2024-08-09 | 2024-08-09 | 0 | 1 | 1 |
| PoE Switch | 2024-07-11 | 2024-07-11 | 0 | 1 | 1 |

## 动态监控（自动 · 网站 / 社媒 / 代码库）

- **监控层**：B 级面层　|　**自动源**：4 个　|　**数据截至**：2026-10-25T07:41:18Z　|　**最近变化**：2026-10-24T04:35:40Z
- **最近变化摘要**：2026-10-24 news_2：内容变化：+0 −2 行
- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/SB-028/`；本节随档案重渲染刷新，实时看日志。

| 源 | 类型 | 状态 | 最近变化 | 摘要 |
|---|---|---|---|---|
| [home](https://fibotelecom.ru/) | html | HTTP 200 | 2026-10-24T04:35:40Z | 4009 字符；首行：FIBO — телекоммуникационное оборудование |
| [sitemap](https://fibotelecom.ru/sitemap.xml) | sitemap | HTTP 200 | 2026-10-23T04:20:51Z | 0 个 URL；最新 lastmod - |
| [news_1](https://fibotelecom.ru/company/news) | html | HTTP 200 | 2026-10-24T04:35:40Z | 920 字符；首行：Новости \| FIBO |
| [news_2](https://fibotelecom.ru/for-clients/articles) | html | HTTP 200 | 2026-10-24T04:35:40Z | 1482 字符；首行：Статьи \| FIBO |

## 联系方式（已有 · 原值照录）

- 邮箱：`roshchupkina@fibotelecom.ru`〔企业邮箱；来源：用户表原值〕
- 邮箱：`info@fibotelecom.ru`〔企业邮箱；来源：用户表原值〕
- 联系人（原值）：Anastasia Roshchupkina / Purchasing
- 联系人（原值）：买了飞宇的
- 网站/域名：fibotelecom.ru
- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。

## 关键人（KP）与触达通道

| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |
|---|---|---|---|---|
| Anastasia Roshchupkina | Purchasing | roshchupkina@fibotelecom.ru | 调研核实（公开页） | 用户 Clients 表 |

- **通道建议**：企业邮箱可直发

## 来源与归并（不漏 · 原始行定位）

本客户由 **2 行**原始记录归并而成；归并键：`d:fibotelecom.ru`, `e:info@fibotelecom.ru`。

| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |
|---|---|---|---|---|---|---|---|---|---|
| DWDM CENTEC_ALAN 08.13.xlsx#总表:73 | 72 | https://fibotelecom.ru/ | 俄罗斯 | Anastasia Roshchupkina<br>Purchasing | MIPS2024 | 光模块 PON | roshchupkina@fibotelecom.ru<br>info@fibotelecom.ru |  | — |
| 客户再筛选_在用同行的产品.xlsx#总表:69 | 68 | https://fibotelecom.ru/catalog/aktivnoe_oborudovanie/mediakonovertery | 俄罗斯 | 买了飞宇的 | 富通天下 | SFP MC(光路的) <br>DPtek客户   后边链接 | info@fibotelecom.ru | https://fibotelecom.ru/catalog/kommutatory/kommutatory_ethernet | — |

## 产品决策（Saga · 单一决策口径）

| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |
|---|---|---|---|---|
| **P1** | STC-28DGGPM | 深挖对位：OEM 30% 档：STC-28DGGPM（Marvell 2 SFP + 8 GE PoE+ L2+，$87.4）对位 DK2110M-8T2S 的 PoE 版；Realtek 线 STC-28GPM（$62.2）对位 DK2110R；L3 STC-424XGGM(L3)（$291.5）对位 DK2310R-24T4X | $87.4 USD EXW（30% 档，SmartByte LT-S8310GP-2GX8GT 450 CNY × 1.30 ÷ 6.69，汇率快照 2026-10-17，15 天有效，报价前核价） | 深挖对位；档位 30%（运营商/光传输采购（待补证）） |
| 备选2 | STI-288DGGPM | 工业 L2+ 8 PoE + 2×2.5G SFP | $137.5 USD EXW（㉕ 封顶：30% 档 $151.6 高于 2026-06 Saga 列表价 $137.5，按列表价；SmartByte LT-IS6310GP-2GX8GT 780 CNY，汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |
| 备选3 | STC-424XGGPM-280W | 24 PoE + 4×10G 上联 | $180 USD EXW（㉕ ② 群发现价（群发价台账），30% 档公式为 $196.3——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；汇率快照 2026-10-17，15 天有效，报价前核价） | P1 之后的台阶，不进首触 |

- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。

## 跟进建议

> 每次只推进一个台阶、只问一个问题；全程只推 P1（STC-28DGGPM），备选型不进首触。

- **第 1 次**：老客户回访——问上次所购型号的使用情况 + 告知 Marvell 新款（STC-28DGGPM）；只问一个问题：当前在采购的主力型号与月量。
- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。
- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；30% 档报价。
- 节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。
- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。

## SWOT

- **S**：有成交史，信任与开户成本已付
- **W**：俄语区：物流/收款/汇率摩擦高于主攻区
- **O**：P1 STC-28DGGPM 按 30% 档报价，做现供应商的第二货源；规模（调研）：待补证
- **T**：深圳同行（ONV / Utepo / 迈威等）价格战；汇率与海运波动吃掉 20–30% 的价差

## 触达与风险红线

1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。
2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。
3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。
4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。
5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。

## Qualification 清单

| 门槛 | 状态 |
|---|---|
| 需求面成立（在卖/在用交换机或 PoE） | ✅ |
| 决策人识别 | ✅ |
| 触达通道 | ✅ 企业邮箱 |
| 现用/在卖交换品牌 | ❓ 未知 |
| 采购量/预算 | ✅ 有成交史（量待确认） |
| 商业资格结论 | **技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟** |

## Unknowns（待问清单 · 跟进后逐项消除）

- [ ] 年走量与现供应商

## 英文跟进邮件（样板 · 可直接发送）

**主题**：STC-28DGGPM - 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks (Marvell-based, neutral label)

```text
Hi Anastasia,

Thank you again for your earlier order with us - this is a short update rather than a cold mail.

We supply a Marvell-based 8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks - model STC-28DGGPM - that fits the same slot as your FIBO DK DK2110M-8T2S at a lower landed cost, and we can ship it with neutral packaging. Current price: $87.4 USD EXW (price snapshot 2026-10-17, valid 15 days).

One question: Are PoE / industrial switches something you still source today, or has that line been dropped?

If useful, one unit at the unit price for a 30-day side-by-side test. If not a fit, one line and I close the loop.

Best regards,
Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)
https://sagatele.com/
```

> 研究档备注（未并入正文）：客户语言一句话（研究档 email_hook；要用就整段单发，不混进英文信）：Анастасия, по вашей линейке DK: мы делаем те же платформы — Marvell L2+ 2 SFP + 8 GbE PoE+ под маркой FIBO 87,4 USD EXW, Realtek L2 версия 77,0 USD, L3 24 GbE + 4×10G 291,5 USD, прошивка с вашим логотипом. Какую модель DK вы сейчас закупаете в наибольшем объёме?

> 发送前检查：① 不出现「Made in China」或原产地；② 不承诺未实测指标（PoE 功率/温宽）；③ 落款换成发件人姓名；④ 一次只问一个问题；⑤ 价格为 USD EXW 快照，过窗先核价；⑥ 只用表内/公开原值邮箱，不猜地址；⑦ 发出后在「新跟进记录」补一行并告知日期。

## 新跟进记录（仓库外发出后补）

| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。

## 下次复核

- **2026-11-24**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。

## 变更日志

- 2026-10-25：建档（PR-02-19 · 从 `Clients/` 2 行原始记录归并；自动评级 A，分数 71）；人工/调研定级 → B

---

*建档日期：2026-10-25　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*
