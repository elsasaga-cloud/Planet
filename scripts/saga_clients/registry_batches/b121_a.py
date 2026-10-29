# -*- coding: utf-8 -*-
"""第 121 批（T29-U114，2026-10-29）第 1 段 22 户（BR 池余 4 + IL 池 8 + KE 池 5 + JP 池 5）—— 官方登记核实写入 registry。
BR 路径沿用（CNPJ 3/3 有域名户命中：官网页脚自列 / 法院公报 / 支持站页脚）；
IL 路径首测：公司号（ח.פ.）= kycisrael.com/companies/<号>（含成立日、状态、年报年份）/ new-techguide 供应商页「Company ID」→ 2/8；D&B / tradeindia / 官网补地址；
KE 路径首测：BRS 不可 1 查 → hotfrog / africa2trust / RocketReach 补地址 → 部分坐实常态；gmail 3 户 0 查；
JP 路径沿用：法人番号 = houjin.jp / gbiz-info / helloboss / alarmbox 1 查即得（3/5），官网会社概要 + PR 稿补地址与代表者。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 121
F = '2026-10-29'
BR = '— 巴西常规：英文稿（可附葡语备注）、20 / 25 / 30 + T/T 预付 100% + FOB 深圳（进口税自理；Anatel 不声称）'
IL = '— 以色列常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP（买方清关；SII 不声称）'
KE = '— 肯尼亚常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP 内罗毕（买方清关；KEBS / CA 不声称）'
JP = '— 日本常规：英文稿、20 / 25 / 30 + T/T 预付 100% + FOB 深圳 或 DAP（买方清关；技適 / PSE 不声称）'

def row(code, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key='other', batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)

# ---------------- BR 池余 4 ----------------
row('SB-695', 'LRI Automação Industrial = Leandro Roisenberg Firma Individual（lri.com.br；**官网 contato 自列 CNPJ 94.574.647/0005-02；Rua Maria Lopes Borba 474, Navegantes - SC 88370-340；「LRI Store」商标 INPI 910048894；工业自动化产品分销（电源、DC/DC、工业交换机、嵌入式、数采）、巴西库存开 NF-e**）→ 坐实；个体企业（Firma Individual）；表内电话 +55 11 / +972 为业主个人；KP Leandro Roisenberg（Director / 业主）；WA 无实质回复', 'BR',
    'BR · 1 次检索：lri.com.br/contato（LRI Automação Industrial；Rua Maria Lopes Borba, 474 Navegantes - SC CEP 88370-340；Leandro Roisenberg Firma Individual CNPJ: 94.574.647/0005-02）+ /como-comprar（LRI Store é uma Marca Registrada de Leandro Roisenberg FI sob INPI 910048894）；2026-10-29', 'https://www.lri.com.br/contato',
    'CNPJ 94.574.647/0005-02（个体企业分支号 0005）', '营业中（官网 + 电商在）', '未取', 'Firma Individual（个体企业）', '工业自动化产品分销（纳韦甘特斯，SC）', 'Rua Maria Lopes Borba 474, Navegantes - SC 88370-340, Brazil', '微型（个体）',
    ['Leandro Roisenberg — Director / 业主（研究档 KP；leandro@lri.com.br）= 收件人'],
    '**同行工业交换机分销（在售进口工业品牌）→ 分销 20% B，一页纸一次（STI-154GP / STI-288DGGPM $137 / STI-280GE $46.6 中性包装一口价 + MOQ 1 + 付费样机；在售品牌不点名；葡语备注）' + BR + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；坐实（官网自列 CNPJ + 地址）。')
row('SB-798', 'GETECSEG Segurança Eletrônica Ltda ME（getecseg.com.br；**圣卡塔琳娜州法院公报 2019-04-01 税务名单：GETECSEG SEGURANÇA ELETRÔNICA LTDA ME，CNPJ 11.641.497/0001-43，Rua João Pessoa 1839, Velha, Blumenau - SC 89036-（欠税 R$4,924.98 公示）→ 坐实；表内 +55 47 = 布卢梅瑙 ✓**）；同名 Gettec（巴西利亚 61）为另一公司，不采信；KP Leonardo Sezerino（技术负责人）；WA 6 次无实质回复', 'BR',
    'BR · 1 次检索：escavador.com DJSC 2019-04-01 p.2781（GETECSEG SEGURANÇA ELETRÔNICA LTDA ME；11.641.497/0001-43；Rua João Pessoa, 1839, Velha Blumenau SC）；casadosdados Gettec 15.443.387（巴西利亚）≠ 本户；2026-10-29', 'https://www.escavador.com/diarios/845061/DJSC/jurisdicional-das-comarcas/2019-04-01?page=2781',
    'CNPJ 11.641.497/0001-43', '存续（2019 公报；状态未取）', '未取', 'Ltda - ME', '电子安防 / 监控（布卢梅瑙，SC）', 'Rua João Pessoa 1839, Velha, Blumenau - SC 89036, Brazil', '微型（ME）',
    ['Leonardo Sezerino — 技术负责人（研究档 KP；leonardo@getecseg.com.br）= 收件人'],
    '**安防公司 + 监控项目兴趣 → 集成商 25% B，一页纸一次（STC-028GP $28 / STC-2216GP + STC-228GP $33 一口价 + 付费样机；葡语备注）' + BR + '**；2019 欠税公示 → 预付 100% 不让步；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；坐实（法院公报 CNPJ + 地址；欠税红旗）。')
row('SB-900', '巴西南里奥格兰德 WhatsApp 联系人 Eleandro（+55 54；**无邮箱 / 公司 → 0 查**）— 主动问过千兆 MC 与商用 PoE 价格；WA 6 次无实质回复', 'BR',
    '0 查（无邮箱 / 公司）；2026-10-29', '', '0 查', '互动中（曾主动问价）', '—', '个人', '未知（RS）', '未取', '个人',
    ['Eleandro（WA；研究档无邮箱）'],
    '**曾主动问价 → 集成商 25% B，WA 一页纸一次（STC-028GP $28 / STC-228GP $33 + STC-110XGE $65 一口价；千兆 MC 不供明说；葡语备注）' + BR + '**；再无回声 → 不动',
    '集成商 25%；WA 一页纸一次（预付 100%）；0 查。')
row('SB-990', 'Precision Solutions（precisionsolutions.com.br；**支持站页脚自列 CNPJ 05.573.595/0001-98，I.E. 149.927.916.115；Avenida Nova Independência 87, conj. 32, Brooklin Paulista, São Paulo - SP 04570-000；+55 11 5103-3260；info@；EXFO 分销 / Fujikura 代表；20+ 年；光纤测试 / 校准**）→ 坐实；Director Eduardo Ken；需求 DWDM / DCI 高端（不供）', 'BR',
    'BR · 1 次检索：supportprecision.com.br（Precision Solutions；CNPJ 05.573.595/0001-98；I.E. 149.927.916.115；Avenida Nova Independência, 87 — conjunto 32 Brooklin Paulista；+55 (11) 5103-3260）+ nic.br 讲义（Distribuidor EXFO - Representante Fujikura）；同名 Precision Solutions Informática 10.730.077（BAIXADA）≠ 本户；2026-10-29', 'https://supportprecision.com.br/',
    'CNPJ 05.573.595/0001-98', '营业中（官网 + 支持站在）', '未取（自述 20+ 年）', 'Ltda（推定）', '光纤测试仪表分销 / 校准（圣保罗）', 'Avenida Nova Independência 87, conj. 32, Brooklin Paulista, São Paulo - SP 04570-000, Brazil', '小型',
    ['Eduardo Ken — Director（研究档 KP；eduardo.ken@precisionsolutions.com.br）'],
    '**需求 DWDM / DCI / 1.6T 高端（不供）+ 测试仪表商 → 不动（B 保留；来询按分销 20% 报 STH 数据中心机 / STC-110XGE）**' + BR,
    '不动（产品不对位）；坐实（页脚 CNPJ + 地址 + 电话）。')

# ---------------- IL 池 8 ----------------
row('SB-148', 'I.S.R. Technologies (Israel) Ltd / ISR Tech（isrcorp.co.il；**官网 + Google Play 开发者信息：5 Eliav Yaacov (Yaakov Eliav 5), Jerusalem 9546205；P.O. Box 34556；02-6520570；1986 年起（Integrated Systems Research Corp.）；智慧出行 / 车队管理 / 公交 ITS；Crunchbase 1–10 人**）；公司号 1 查未得 → 部分坐实；需求工业 8 电口 E-mark（不供）；KP Yukie Novick；WA 5 次无实质回复', 'IL',
    'IL · 1 次检索：isrcorp.co.il（ISR Tech；Tel 02-6520570；P.O. Box 34556；Yaakov elvav 5, Jerusalem；since 1986）+ play.google.com 开发者（I.S.R. TECHNOLOGIES ( ISRAEL) LTD；5 Eliav Yaacov JERUSALEM, 9546205）+ crunchbase（Founded 1986；1-10；Jerusalem）；公司号未得；2026-10-29', 'https://www.isrcorp.co.il/',
    '未取（公司号 1 查未得）', '营业中（官网 + 应用商店 2026）', '1986', 'Ltd', '智慧出行 / 车队管理 ITS（耶路撒冷）', '5 Eliav Yaacov St., Jerusalem 9546205, Israel', '微型（1–10）',
    ['Yukie Novick — 联系人（研究档 KP；novick@isrcorp.co.il）'],
    '**车载 E-mark 需求（不供）+ 5×0 → 不动（B 保留；来询按集成商 25% 报 STI-280GE 机柜 / 站房用途，不声称车载认证）**' + IL,
    '不动（产品不对位：车载认证）；部分坐实（官网地址 + 成立年；公司号未取）。')
row('SB-228', 'Negoh-Op Ltd（negoh-op.com；**TradeAtlas / tendata：Shabazi St. 10, Yahud 5623028, Israel；进口光延迟线 / RF-光转换器（RF 光子学测试测量）；ZoomInfo 11–50，+972 3 528 5972**）；公司号 1 查未得 → 部分坐实；CEO Dov Abraham；需求 10G 光模块（不供）；WA 无实质回复', 'IL',
    'IL · 1 次检索：app.tradeatlas.com（NEGOH-OP LTD；SHABAZI ST. 10 YAHUD, ISRAEL, 5623028）+ tendata（5 shipments；OPTICAL DELAY LINE / RF TO OPTICAL SIGNAL CONVERTER）+ zoominfo（+972 35285972；11-50；Test & Measurement）；公司号未得；2026-10-29', 'https://app.tradeatlas.com/en/firms/negoh-op-ltd/5ef774402f314ab6',
    '未取（公司号 1 查未得）', '营业中（企业库 + 进口记录）', '未取', 'Ltd', 'RF 光子学 / 测试测量（耶胡德）', 'Shabazi St. 10, Yahud 5623028, Israel', '小型（11–50）',
    ['Dov Abraham — CEO（研究档 KP；dov@negoh-op.com）'],
    '**需求 10G 光模块（不供）+ 非目标行业（RF 光子学）→ 不动（B 保留）**' + IL,
    '不动（产品不对位 + 非目标行业）；部分坐实（贸易库地址；公司号未取）。')
row('SB-328', 'Advice Electronics Ltd（advice.co.il；**new-techguide 供应商页：Company ID 511393159；16 Atir Yeda St., Kfar Saba；1988 / 1989 年成立；51–200 人；+972 3 900 0900；sales@advice.co.il；电源 / UPS / 储能 / 通信方案，代理 MeanWell / Eltek / Fronius 等，ISO9001；站内 PLANET 工业交换机 IGS-4215-4T2S / ISW-501T / ISW-511T、UIS16G-E；表内「自己的 logo，PLANET 的较多产品」**）→ 坐实；无具名 KP；群发 8 次无回复', 'IL',
    'IL · 1 次检索：new-techguide.com/supplier/advice-electronics-ltd（ADVICE ELECTRONICS LTD；established on 1988；Company ID: 511393159；16 Atir Yeda st. Kfar Saba）+ il.linkedin.com/company/advice-electronics（Founded 1989；51-200；972-3-9000900；sales@advice.co.il）；2026-10-29', 'https://www.new-techguide.com/supplier/advice-electronics-ltd/',
    '公司号 511393159', '营业中（官网 + 领英 2025）', '1988（领英口径 1989）', 'Ltd（私人有限）', '电源 / UPS / 通信方案分销与制造（卡法萨巴）', '16 Atir Yeda St., Kfar Saba, Israel', '中小型（51–200）',
    ['（无具名 KP：sales@advice.co.il；Attn: Communication Products Manager）'],
    '**自有 logo + 在售 PLANET 工业机 → 贴标 OEM 30%（STI-154GP 对 IGS-4215-4T2S / STI-054GP 对 ISW-501T 贴标）↔ 分销 20% 双轨 B，一页纸一次（PLANET 不点名；MOQ + 付费样机）' + IL + '**；回信 → 加厚',
    '贴标 OEM 30% ↔ 分销 20% 双轨；一页纸一次（预付 100%）；坐实（公司号 + 地址 + 成立年）。')
row('SB-378', 'Pal Wintec Systems Ltd（palwintec.com；**D&B：20 Hamagshimim St., Petah Tikva 4934829；inter-fair / tradeindia：2000 年成立、约 35 人、P.O. Box 7184、+972 3 922 2051；对讲 / 门禁 / 电话系统自研制造 + 出口；tradeindia 联系人 Mr. Ophir Reuveni**）；公司号 1 查未得 → 部分坐实；KP Efi Yosefian（VP）；表内「常规 af/at PoE、不用 90W、无需云管理」；6 次跟进无回复', 'IL',
    'IL · 1 次检索：dnb.com（PAL WINTEC SYSTEMS LTD；20 Hamagshimim PETAH TIKVA 4934829）+ inter-fair.com（established in 2000；+972 3 922 2051）+ tradeindia（Mr. Ophir Reuveni；Employee Count 35；Exporter, Importer, Manufacturer）；公司号未得；2026-10-29', 'https://www.dnb.com/business-directory/company-profiles.pal_wintec_systems_ltd.41d48ad1a0335f9455abaa962c86bea9.html',
    '未取（公司号 1 查未得）', '营业中（官网 + 企业库）', '2000', 'Ltd', '对讲 / 门禁 / 电话系统制造与出口（佩塔提克瓦）', '20 Hamagshimim St., P.O. Box 7184, Petah Tikva 4934829, Israel', '小型（约 35 人）',
    ['Efi Yosefian — VP（研究档 KP；efi@palwintec.com）= 收件人', 'Ophir Reuveni — 联系人（tradeindia 2026-10-29；无公开邮箱）'],
    '**自研对讲 / IP 监视器厂商、需求明确（af/at 常规 PoE）→ 集成商 25% B（随机配套 PoE：STC-028GP $28 / STC-2216GP 一口价）+ 贴标 30% 选项一句，一页纸一次（MOQ 1 + 付费样机）' + IL + '**；再无回声 → 不动',
    '集成商 25%（贴标选项）；一页纸一次（预付 100%）；部分坐实（D&B 地址 + 成立年 + 人数；公司号未取）。')
row('SB-704', 'Ethical Ltd（ethical-ltd.com；**kycisrael：Registration Number 512146788；Private Limited；Active；成立 1995-05-10；最近年报 2025；33 Shmuel Tamir St., Tel Aviv 6963717（D&B 同址）；采购服务与通信产品供应（元件、电光设备、连接器、终端服务器、MC、延长器、工业交换机）；cellpex 联系人 Ran Broudo；表内「Switch 主要用 Perle」**）→ 坐实；无具名 KP（ethical@）；群发 8 次无回复', 'IL',
    'IL · 1 次检索：kycisrael.com/companies/512146788/ethical-ltd（Registration Number 512146788；Private Limited Company；Active；Incorporation Date 10/05/1995；Last Annual Report Year 2025；33 תמיר שמואל 6963717）+ dnb（33/1 Tamir Shmuel TEL AVIV-JAFFA）+ cellpex（Ethical ltd；Ran Broudo）；2026-10-29', 'https://www.kycisrael.com/companies/512146788/ethical-ltd/',
    '公司号 512146788', 'Active（年报 2025）', '1995-05-10', 'Ltd（私人有限）', '采购服务 / 通信与电子产品供应（特拉维夫）', '33 Shmuel Tamir St., Tel Aviv 6963717, Israel', '小型',
    ['Ran Broudo — 联系人 / 负责人（cellpex 供应商档 2026-10-29；无公开邮箱）→ 收件 ethical@ethical-ltd.com Attn: Ran Broudo'],
    '**采购服务商（在供 Perle 类 MC / 工业机）→ 分销 20% B，一页纸一次（STC-110XGE $65 / STI-154GP / STI-288DGGPM $137 一口价 + MOQ 1 + 付费样机；在供品牌不点名）' + IL + '**；再无回声 → 不动',
    '分销 20%；一页纸一次（预付 100%）；坐实（公司号 + 成立日 + 年报 + 地址）。')
row('SB-911', 'itmarket.co.il（**1 查无命中 → 未坐实**；仅电话 +972 52 647 7172，无邮箱）— CCTV 与网络设备供应商（表内：ONV 工业 FS / MC，评估「质量高，50% A」）；WA 16 次无实质回复', 'IL',
    'IL · 1 次检索：「itmarket.co.il Israel CCTV network equipment company address」→ 无相关结果；2026-10-29', '', '未取（1 查无命中）', '未知', '未取', '未取', 'CCTV / 网络设备供应（以色列）', '未取', '小型（推定）',
    ['（未具名；仅 WA +972 52 647 7172）'],
    '**16×0 + 无 KP + 未坐实 → 不动（B 保留）**' + IL, '不动（16×0 + 无 KP）；未坐实。')
row('SB-915', 'RADWIN Ltd（radwin.com；**D&B / datanyze / cbinsights：27 Habarzel St., Tel Aviv 6971039；+972 3 766 2900；1997 年成立；约 270 人；营收约 $68M；CEO Sharon Sher（= 研究档 KP ✓）；运营商级固定无线 PtP / PtMP / 回传厂商**）；公司号 1 查未得 → 部分坐实（大型）；KP Dave Azria（Director of Product Management）；表内「Ethernet Switch」；未跟进', 'IL',
    'IL · 1 次检索：dnb.com/business-directory/company-profiles/radwin-ltd（27 Habarzel TEL AVIV-JAFFA 6971039；+972-37662900；CEO Sharon Shar）+ datanyze（Employees 270；Revenue $67.9M；Founded 1997）+ cbinsights（27 Habarzel Street, Tel Aviv, 6971039；1997）；公司号未得；2026-10-29', 'https://www.dnb.com/business-directory/company-profiles/radwin-ltd.540b3e48d35e64f615a68029699055c6',
    '未取（公司号 1 查未得）', '营业中（官网 + 企业库）', '1997', 'Ltd（私人有限）', '固定无线接入 / 回传设备制造（特拉维夫）', '27 Habarzel St., Tel Aviv 6971039, Israel', '大型（约 270 人）',
    ['Dave Azria — Director of Product Management（研究档 KP；dave_a@radwin.com）= 收件人', 'Sharon Sher — CEO（研究档 KP；D&B 吻合）'],
    '**无线原厂（CPE / IDU 配套 PoE 交换机 = 配件贴标入口）+ 产品管理总监为 KP → 贴标 OEM 30% B，一页纸一次（STC-028GP $28 / STC-228GP $33 贴标 + 工业 STI-154GP 户外机柜；MOQ + 付费样机）' + IL + '**；大厂成单概率低 → 一次即止',
    '贴标 OEM 30%；一页纸一次（预付 100%）；部分坐实（企业库地址 + 成立年 + 人数 + CEO；公司号未取）。')
row('SB-934', 'Alibi Security（alibisecurity.com；**美国：15505 Long Vista Drive, Suite 250, Austin, TX 78728；母公司 Observint Technologies（同址）；30+ 年经销商网络；100–200 人；CEO Brian Wood；888-858-1442；自有品牌摄像机 / 门禁 / VMS + 转售 D-Link / TP-Link PoE 交换机、Vigitron 注入器 → 表内国别「以色列」误 → country_fix 美国**）；州登记号未取 → 部分坐实；KP Billy Grumbles；未跟进', 'US',
    'US · 1 次检索：observint.com/News（Alibi Security … owned by parent company Observint Technologies, both headquartered in Austin, TX；15505 Long Vista Drive Suite 250 Austin, TX 78728）+ een.com（Brian Wood, CEO of Alibi Security；30 years）+ signalhire（15505 Long Vista Drive, Austin, Texas, 78728；100-200）；2026-10-29', 'https://observint.com/News/',
    '未取（Texas SoS 付费；品牌隶属 Observint Technologies）', '营业中（官网 + 新闻）', '约 1990（自述 30+ 年）', 'LLC / Inc.（Observint 旗下品牌）', '安防产品自有品牌 + 经销商渠道（奥斯汀，德州）', '15505 Long Vista Drive, Suite 250, Austin, TX 78728, USA', '中型（100–200）',
    ['Billy Grumbles — 联系人（研究档 KP；billy.grumbles@alibisecurity.com）= 收件人', 'Brian Wood — CEO（een.com 新闻 2026-10-29；无公开邮箱）'],
    '**自有品牌安防 + 转售 D-Link / TP-Link PoE → 贴标 OEM 30% B，一页纸一次（STC-028GP $28 / STC-2216GP / STC-2224GP $86 Alibi 贴标 + MOQ + 付费样机；NDAA / TAA 不声称、D-Link / TP-Link / Vigitron 不点名）— 美国常规：英文稿、20 / 25 / 30 + T/T 预付 + FOB 深圳 或 DAP（买方清关）；周三 08–10 当地**；回信 → 加厚',
    '贴标 OEM 30%；一页纸一次（预付 100%）；部分坐实（新闻 + 名录地址 + 母公司；州登记号未取）；country_fix 美国。')

# ---------------- KE 池 5 ----------------
row('SB-1076', 'Simplifi Networks Ltd（simplifinetworks.com；**hotfrog / africa2trust / RocketReach：Unit 28, Fortis Industrial Park, off Mombasa Road, Nairobi 80100；+254 727 401 262；2014 年成立；约 12 人；东非 Ubiquiti 直接分销 + MikroTik 主分销（内罗毕 / 坎帕拉 / 达累斯萨拉姆有库存）**）；注册号 1 查未得 → 部分坐实；表内「PoE 配件 / 工业 FS 有自己的 logo」；无具名 KP；1 次跟进无回复', 'KE',
    'KE · 1 次检索：hotfrog.co.ke（Simplifi Networks；Unit 28, Fortis Industrial park, Mombasa Road Nairobi 80100；0727 401262）+ africa2trust（Simplifi Networks Ltd；Distributor for Mikrotik, Ubiquiti UniFi, RF-Elements）+ rocketreach（Founded 2014；Employees 12；only Direct Distributor for Ubiquiti … MikroTik Master Distributor）；注册号未得；2026-10-29', 'https://rocketreach.co/simplifi-networks-profile_b45386d6fc871866',
    '未取（BRS 注册号 1 查未得）', '营业中（官网 + 名录）', '2014', 'Ltd', '网络设备分销（内罗毕；东非三国）', 'Unit 28, Fortis Industrial Park, off Mombasa Road, Nairobi 80100, Kenya', '小型（约 12 人）',
    ['（无具名 KP：kenya@simplifinetworks.com；Attn: Product Manager）'],
    '**原厂总分销（Ubiquiti / MikroTik）+ 自有 logo PoE 配件 → 贴标 OEM 30%（自标 PoE / 工业 FS：STC-028GP / STC-2216GP / STI-154GP）↔ 分销 20% 双轨 B，一页纸一次（原厂不点名；MOQ + 付费样机）' + KE + '**；再无回声 → 不动',
    '贴标 OEM 30% ↔ 分销 20% 双轨；一页纸一次（预付 100%）；部分坐实（名录地址 + 成立年 + 人数；注册号未取）。')
row('SB-337', 'Kimberley Telecommunications（**gmail + 无域名 → 0 查**）— 肯尼亚电信工程商，在用 PLANET 设备；需求 2 光 16 电管理型 passive PoE（非标，不供）；2024-07 回「price」', 'KE',
    '0 查（gmail + 无域名）；2026-10-29', '', '0 查', '互动中（2024-07 问价）', '—', '未取', '电信工程（肯尼亚）', '未取', '微型（推定）',
    ['（未具名；gadsatoh@gmail.com）'],
    '**曾问价 + 在用 PLANET → 集成商 25% B，一页纸一次（passive PoE 不供明说 → STC-2216GP 标准 af/at 一口价 + STC-228GP；PLANET 不点名）' + KE + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；0 查（gmail）。')
row('SB-586', 'Matrix Vision Systems / Matrix Systems（matrixsystems.co.ke；**1 查仅美国 / 中东同名，肯尼亚本体未命中 → 未坐实**；研究档：内罗毕电气工程 + 安防 + 软件集成商，11–50 人，Hikvision 战略伙伴，NCA / CA 认证 ICT 承包商）；技术总监 Mogeni Enock 2024-03 回「有用，需与团队沟通是否拿样」；需求光纤上行 IP 摄像机接入', 'KE',
    'KE · 1 次检索：「"Matrix Systems" matrixsystems.co.ke Nairobi」→ crunchbase（美国 Matrix Systems）/ facebook 同名（中东）→ 均非本户；2026-10-29', '', '未取（1 查未命中本体）', '营业中（研究档官网）', '未取（自述 10 年以上）', 'Ltd（推定）', '电气 / 安防 / ICT 集成（内罗毕）', '未取（Nairobi, Kenya）', '小型（11–50）',
    ['Mogeni Enock — 技术总监（研究档 KP；mogeni@matrixsystems.co.ke）= 收件人'],
    '**技术总监曾回复「需沟通拿样」→ 集成商 25% B，一页纸一次（光纤上行摄像机接入：STI-154GP / STC-228GP $33 付费样机一口价 + 运费；Hikvision 配套中性包装）' + KE + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（付费样机 + 预付 100%）；未坐实（同名未对齐）。')
row('SB-896', '肯尼亚联系人 Musine（wafulamusine@gmail.com；**无公司名 → 0 查**）— 需求千兆 PoE 媒体转换器（不供）；2025-04 回「interested」', 'KE',
    '0 查（gmail + 无公司名）；2026-10-29', '', '0 查', '互动中（2025-04）', '—', '个人', '未知（肯尼亚）', '未取', '个人',
    ['Musine（研究档 KP；wafulamusine@gmail.com）'],
    '**需求 PoE MC（不供）+ 无公司 → 不动（B 保留；来询按集成商 25% 报 STC-028GP + 预付 100%）**' + KE, '不动（产品不对位 + 个人）；0 查。')
row('SB-897', 'Peter Weru（wellspeter8@gmail.com；**gmail + 无公司名 → 0 查**）— 肯尼亚小型安装 / 转售商（2016 年起用国际站，WA 已加）；需求「百兆单纤小外电 50 对」（不供）；2024-06 要「price list」；19 次推送 2 次实质回复', 'KE',
    '0 查（gmail + 无公司名）；2026-10-29', '', '0 查', '互动中（2 次）', '—', '个体 / 微型', '安装 / 转售（肯尼亚）', '未取', '微型',
    ['Peter Weru — 业主（研究档 KP；wellspeter8@gmail.com；WA 已加）= 收件人'],
    '**两次实质回复 + 要价表 → 集成商 25% B，一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2216GP 一口价 + MOQ 1；百兆 MC 不供明说）' + KE + '**；再无回声 → 不动',
    '集成商 25%；一页纸一次（预付 100%）；0 查（gmail）。')

# ---------------- JP 池 5 ----------------
row('SB-157', 'データコントロルズ株式会社 Data Controls Inc.（dci.jp；**会社案内 PDF：1983 年設立；〒111-0052 東京都台東区柳橋 1-20-4 深代ビル 8F；TEL 03-5829-5805；事業 = ネットワーク機器の開発 / 製造 / 輸入販売 + 修理；日経 COMPASS 登記住所同址（電気機械器具卸売業）**）；法人番号 1 查未得 → 部分坐实；表内「光路 MC 系列、ORing 工业 FS」；无具名 KP（info@）；2 次跟进无回复', 'JP',
    'JP · 1 次检索：dci.jp/media/2024/08/DCIprofile2019.pdf（データコントロルズ株式会社；1983年設立；〒111-0052 東京都台東区柳橋1-20-4 深代ビル8F；ネットワーク機器の開発/製造/輸入販売）+ nikkei.com/compass（登記住所 東京都台東区柳橋１丁目２０番４号；電気機械器具卸売業）；法人番号未得；2026-10-29', 'https://dci.jp/media/2024/08/DCIprofile2019.pdf',
    '未取（法人番号 1 查未得）', '营业中（官网 + 日经）', '1983', '株式会社', '网络设备（MC / 工业交换机）开发・进口销售（东京台东区）', '〒111-0052 東京都台東区柳橋 1-20-4 深代ビル 8F, Japan', '小型',
    ['（无具名 KP：info@dci.jp；Attn: 購買担当 / Purchasing）'],
    '**MC / 工业交换机进口商兼自研 → 分销 20%（STC-110XGE $65 / STI-154GP / STI-288DGGPM $137）↔ 贴标 OEM 30% 双轨 B，一页纸一次（在供品牌不点名；MOQ 1 + 付费样机）' + JP + '**；再无回声 → 不动',
    '分销 20% ↔ 贴标 30% 双轨；一页纸一次（预付 100%）；部分坐实（会社案内 + 登記住所；法人番号未取）。')
row('SB-158', 'ダイヤトレンド株式会社 Diatrend Corporation（diatrend.com / diatrend.co.jp；**法人番号 5120001026515；1971-08 設立；代表 宮下清哉 = 研究档 KP Kiyomasa Miyashita ✓；〒530-0011 大阪府大阪市北区大深町 3-1（2017-01 起；旧址 中央区南船場 2-2-14）；子会社 DT エンジニアリング；電子応用製品の企画開発・製造・販売（接口电缆、光缆、PoE 注入 / 延长产品）**）→ 坐实；表内「工业 FS / MC / SFP 自己的 label」；2 次跟进无回复', 'JP',
    'JP · 1 次检索：houjin.jp/c/5120001026515（ダイヤトレンド株式会社；法人番号 5120001026515；設立 1971年08月；代表 宮下清哉；大阪市北区大深町3番1号；吸収合併 2022-06）+ catr.jp（DTエンジニアリング株式会社 子会社；本店移転履歴）；2026-10-29', 'https://houjin.jp/c/5120001026515',
    '法人番号 5120001026515', '营业中（登記更新 2022-06；官网在）', '1971-08', '株式会社', '电子应用产品企划开发・制造・销售（大阪北区）', '〒530-0011 大阪府大阪市北区大深町 3-1, Japan', '中小型',
    ['Kiyomasa Miyashita（宮下清哉）— 代表取締役 / Managing Director（法人登記 2026-10-29 吻合；研究档 KP info@diatrend.co.jp）= 收件人'],
    '**自有 label 的 MC / 工业 FS 厂商、代表取締役为 KP → 贴标 OEM 30% B，一页纸一次（STI-154GP / STI-288DGGPM $137 + STC-110XGE $65 贴标 + MOQ + 付费样机；SFP 不供明说）' + JP + '**；回信 → 加厚',
    '贴标 OEM 30%；一页纸一次（预付 100%）；坐实（法人番号 + 設立 + 代表 + 本店）。')
row('SB-161', 'マハネット株式会社 Mahanet Co., Ltd.（mahanet-jp.com；**gBizINFO：法人番号 7390001009301；設立 2005-02-25；本店 山形県東根市大字蟹沢 1646-33；被保険者数 4 人；全省庁統一資格；官网：資本金 1,000 万円、CEO Akira Ohe（大江）、TEL 0237-42-5833；防犯カメラ販売施工 + 自有 MH- 系列 IP 摄像机 / NVR / PoE 交换 HUB（MH-7204E / 7208E / 7216E-L2 / 7224E-L2）**）→ 坐实；表内「安防为主 有 Utepo 的交换机」；无具名 KP；7 次跟进无回复', 'JP',
    'JP · 1 次检索：info.gbiz.go.jp/hojin/ichiran?hojinBango=7390001009301（マハネット株式会社；法人番号 7390001009301；山形県東根市大字蟹沢１６４６番地３３；設立 2005年02月25日；被保険者数 4人）+ mahanet-jp.com/en（Incorporated 2005/02/25；Capital 10,000,000 Yen；CEO Akira Ohe；0237-42-5833）；2026-10-29', 'https://info.gbiz.go.jp/hojin/ichiran?hojinBango=7390001009301',
    '法人番号 7390001009301', '营业中（gBiz 在册 + 官网）', '2005-02-25', '株式会社（資本金 1,000 万円）', '防犯カメラ・安防系统销售施工，自有 MH 系列（山形东根）', '〒999-3716 山形県東根市大字蟹沢 1646-33, Japan', '微型（4 人）',
    ['Akira Ohe（大江）— CEO / 代表取締役（官网 2026-10-29；收件 info@mahanet-jp.com Attn: Mr. Ohe）'],
    '**自有 MH 系列 PoE 交换 HUB → 贴标 OEM 30% B，一页纸一次（MH-7204E / 7208E / 7216E-L2 / 7224E-L2 对位 STC-028GP $28 / STC-2216GP / STC-4424GCPM $165 贴标 + MOQ + 付费样机；UTEPO 不点名）' + JP + '**；7×0 → 最后一次，再无回声 → 不动',
    '贴标 OEM 30%；最后一次一页纸（预付 100%）；坐实（法人番号 + 設立 + 本店 + 代表）。')
row('SB-164', 'UNEAX 株式会社（unea-x.com；**法人番号 6021001077094；設立 2022-10-04；本店 〒242-0007 神奈川県大和市中央林間 5-5-23-6；従業員 1 人（eigyo-mfg）；事業 = SSD 販売、産業用イーサネットスイッチの開発・販売、IoT センサー、金型部品加工 → 微型同行（自标工业交换机）**）→ 坐实；研究档 KP Ryosuke Osako（2026-04-22 首位联系）/ Mari Inoue（2026-05 技术 / 合规对接）；表内「工业 switch 国内的外壳」', 'JP',
    'JP · 1 次检索：helloboss.com/corp/6021001077094（UNEAX株式会社；法人番号 6021001077094；神奈川県大和市中央林間5丁目5番23-6号；設立 2022-10-04）+ eigyo-mfg.com（従業員数 1人；SSDの販売, 産業用イーサネットスイッチの開発と販売, センサーシステム, 金型部品加工）+ alarmbox.jp（同法人番号）；2026-10-29', 'https://helloboss.com/corp/6021001077094',
    '法人番号 6021001077094', '营业中（登記 2022-10；官网在）', '2022-10-04（新壳）', '株式会社', '工业交换机自标开发销售 + SSD / IoT / 金型加工（神奈川大和）', '〒242-0007 神奈川県大和市中央林間 5-5-23-6, Japan', '微型（1 人）',
    ['Ryosuke Osako（大迫）— 首位联系人（研究档 KP；ryosuke.osako@unea-x.com）= 收件人', 'Mari Inoue（井上）— 技术 / 合规对接（研究档 KP；inoue.mari@unea-x.com）'],
    '**微型同行、明确要「国内外壳」工业交换机自标 + 2026 年在谈 → 贴标 OEM 30% B，一页纸一次（STI-054GP / STI-154GP / STI-288DGGPM $137 贴标 + MOQ + 付费样机；合规文件只给 CE / RoHS / FCC 现有件）' + JP + '**；1 人新壳 → 预付 100% 不让步',
    '贴标 OEM 30%；一页纸一次（预付 100%；新壳 1 人）；坐实（法人番号 + 設立 + 本店）。')
row('SB-822', 'ソリッド株式会社 Solid Corp.（品牌「ソリッドケーブル」solidcable.com；**PR 稿会社概要：〒541-0042 大阪府大阪市中央区今橋 2-3-16 5F；代表取締役 徳岡達人；TEL 06-6228-0577；商社；従業員 500 名未満；2004 年起製造直販 EC（TV / ネットワーク線缆、当日発送）；企业站 solid-corp.com**）；法人番号 1 查未得 → 部分坐实；表内「ONV 的 MC 一些周边通讯设备」；无具名 KP（support@）；2 次跟进无回复', 'JP',
    'JP · 1 次检索：dreamnews.jp/press/0000337263（ソリッド株式会社；代表取締役社長 徳岡達人；大阪府大阪市中央区今橋2-3-16-5F；06-6228-0577；商社；2004年 ソリッドケーブル）+ dreamnews 0000328525（会社HP solid-corp.com）；法人番号未得；2026-10-29', 'https://www.dreamnews.jp/press/0000337263',
    '未取（法人番号 1 查未得）', '营业中（PR 2025-12；EC 在）', '未取（EC 2004 起）', '株式会社', '线缆・通信周边製造直販 EC（大阪中央区）', '〒541-0042 大阪府大阪市中央区今橋 2-3-16 5F, Japan', '小型（<500 自报）',
    ['Tatsuto Tokuoka（徳岡達人）— 代表取締役（PR 稿 2026-10-29；收件 support@solidcable.com Attn: 仕入担当 / Purchasing）'],
    '**自有品牌线缆 EC（MC / 周边在售）→ 贴标 OEM 30%（STC-110XGE $65 / STC-028GP $28 自标）↔ 分销 20% 双轨 B，一页纸一次（在供品牌不点名；MOQ + 付费样机）' + JP + '**；再无回声 → 不动',
    '贴标 30% ↔ 分销 20% 双轨；一页纸一次（预付 100%）；部分坐实（PR 会社概要 + 代表；法人番号未取）。')
