# -*- coding: utf-8 -*-
"""第 134 批（T29-U118g，2026-10-29）—— **C 池三闸 · 闸 2 第十一批**：闸 1 第 36–46 批（桶 ⑦ 第 56–660 户）候选 25 户中的 **欧洲 / 土耳其 / 俄语区 10 户** 先查底数（DE 1 / TR 3 / PT 1 / LV 1 / RU 2 / KZ 2）；其余 15 户（印度 6 / 越南 9）留第 135 批。
路径：DE → 官网 UKCA 声明页 + firmendatenbanken（HRB / USt-ID / GF）；TR → taysad / ostimsavunma / alo118 目录（地址 / 规模）、vknsorgula（未命中）；PT → racius + iberinform（NIF / CAE / 资本 / 成立日）；LV → Lursoft（未命中）；RU → rusprofile（同名壳 ≠ 品牌）；KZ → niac.kz / ba.prg.kz（БИН / 负责人 / ОКЭД）。
每户 1 查、depth 1；1 查未中即停 = 未坐实（url=''），下轮再查 1 次。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 134
F = '2026-10-29'
DE = '— 德国主区常规：英文 / 德语稿、20 / 25 / 30 + T/T 50/50 + DAP 买方清关（CE / RoHS / REACH）；周二 / 周四 10–12 CET'
TR = '— 土耳其常规：英文 / 土耳其语稿、20 / 25 / 30 + T/T 50/50（首单可预付 100%）+ FOB 深圳 / DAP 买方清关（CE / RoHS）；周二 / 周四 10–12 TRT'
PT = '— 葡萄牙常规：英文稿、20 / 25 / 30 + 预付 100%（微型）+ DAP 买方清关（CE / RoHS / REACH）；周二 / 周四 10–12 WET'
RU = '— 俄语区常规：英 / 俄稿、20 / 25 / 30；收款 / 物流路径待 Simon（RU / KZ 「收款待定」）；FOB 深圳'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 德国 ----------------
row('SC-568', 'de', 'EFB-Elektronik GmbH（efb-elektronik.de；**HRB 33008 AG Bielefeld；USt-IdNr. DE 126943218；Striegauer Straße 1, 33719 Bielefeld；+49 521 40418-0；info@efb-elektronik.de；Geschäftsführer Robin Ohle（目录另列 Nana Heinemann / Alexander van der Lof）；结构化布线 / 光纤 / 网络机柜 / 网络技术，身份「Hersteller + Großhändler」= 自有品牌 EFB 产品线（含网络交换机）；UKCA 声明 2026-10-06 自署 = 在营**）；表内：Simon「比较专业 / 质量」', 'DE',
    'DE · 1 次检索：efb-elektronik.de UKCA 声明页（HRB / USt-ID / GF / 地址 / 电话）+ firmendatenbanken（HRB 33008 / GF / 业务）；2026-10-29', 'https://www.firmendatenbanken.de/unternehmen/detail/463966/efb-elektronik-gmbh.htm',
    'HRB 33008（AG Bielefeld）', '营业中（2026-10 自署 UKCA 声明）', '未取', 'GmbH', '网络 / 布线基础设施制造 + 批发（比勒费尔德）', 'Striegauer Straße 1, 33719 Bielefeld', '大型（德国全国性分销 + 自有品牌）',
    ['Robin Ohle — Geschäftsführer', 'Nana Heinemann / Alexander van der Lof — 目录列 GF（待核）'],
    '**德国主区 · 自有品牌分销商 OEM 30%（长线）：info@ + 官网找 Einkauf / Produktmanagement 后一页纸一次（STC-2224GP $86 / STC-4424GCPM $165 / STC-424XGGPM-280W $198 中性包装 + 贴 EFB 牌 + MOQ 1 + 付费样机）' + DE + '**',
    'OEM 30%；P 池候选 ★ 长线（德国主区 ✔ 自有品牌 ✔ 对位 ✔ Simon「专业」✔；决策人未具名 → 先找 Einkauf）；坐实（HRB 33008）。')

# ---------------- 土耳其 ----------------
row('SC-2776', 'tr', 'Karel Elektronik Sanayi ve Ticaret A.Ş.（karel.com.tr；**1986 年成立；总部 Ankara Teknoloji Geliştirme Bölgesi (Cyberpark) Üniversiteler Mah. 1606. Cad. B Blok Kat:3, Bilkent 06800 Ankara；工厂 Sincan OSB Gazneliler Cad. No:10, 06935 Ankara（室内 20,500 m²）；约 2,500 人；100% 土耳其资本；IT 500「土耳其本土 IT 制造商」第一；研发投入 ≈ 营收 8.5%；出口 30+ 国**）；ticaret sicil / MERSİS 未取；表内：Simon 二筛「用的丰润达的」= 已采购中国 OEM 商业 PoE 交换机；无邮箱', 'TR',
    'TR · 1 次检索：taysad.org.tr 会员页（法人名 / Cyberpark 地址）+ ostimsavunma.org（1986 / 2,500 人 / Sincan 工厂 / 出口 30+ 国）+ alo118（工厂地址）；ticaret sicil 未取；2026-10-29', 'https://www.ostimsavunma.org/companies/karel-elektronik-as-2',
    '未取（ticaret sicil / MERSİS 未查；法人名 + 地址坐实）', '营业中（目录 2025–2026）', '1986', 'Anonim Şirketi（A.Ş.）', '通信电子制造（PBX / 网络 / 安防）自有品牌（安卡拉）', 'Cyberpark Üniversiteler Mah. 1606. Cad. B Blok Kat:3, Bilkent 06800 Ankara', '大型（≈ 2,500 人）',
    ['（具名采购 KP 未取；官网 İletişim / Satın Alma 待找）'],
    '**土耳其主区 · 巨头品牌商 OEM 30%（长线）：官网找 Satın Alma / Ürün Yönetimi 邮箱后一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 / STC-4424GCPM $165 中性包装 + 贴 Karel 牌 + MOQ 1；丰润达现供 → 只推 SmartByte / Marvell 管理线差异）' + TR + '**',
    'OEM 30%；P 池候选 ★ 长线（土耳其主区 ✔ 巨头自有品牌 ✔ 已用中国 OEM ✔ 对位 ✔；无邮箱 → 先找路径；Simon 原「判定不行」→ 可按编号否决）；部分坐实（sicil 未取）。')
row('SC-1190', 'tr', 'Bilimsa Teknoloji（表内；bilimsateknoloji@gmail.com；Muharrem Kılıç；8 光 8 电工业交换机已报 $110；**1 次检索未中（vknsorgula 返回同名壳 Bilimtek / 学术同名人）**）', 'TR',
    'TR · 1 次检索：vknsorgula「Bilimsa Teknoloji」未命中（返回 BİLİMTEK MAKİNA 等非同一主体）；2026-10-29', '',
    '未取（未坐实）', '未知', '未取', '未取', '工业交换机询价（土耳其）', '未取', '未取',
    ['Muharrem Kılıç — 表内联系人'],
    '**土耳其主区 · 待坐实：先回 gmail 问法人名 / 网址（引用已报 $110 的 8 光 8 电），坐实后再 WA 一页纸' + TR + '**',
    '未坐实（1 查未中即停）→ 回 C 待下轮 1 查；土耳其主区 ✔ 已报价 ✔ 具名 ✔。')
row('SC-2271', 'tr', 'NAZEMCO（表内；Osama；Ady 展会加了微信；要商业级 PoE 交换机；**1 次检索未中（返回 Una-IoT / 贸易数据同名个人等非同一主体）**）', 'TR',
    'TR · 1 次检索：「Nazemco Turkey network switch Osama」未命中；2026-10-29', '',
    '未取（未坐实）', '未知', '未取', '未取', '商业 PoE 交换机询价（土耳其）', '未取', '未取',
    ['Osama — 表内微信联系人'],
    '**土耳其主区 · 待坐实：微信先问公司全名 / 网址 / 所在市，坐实后一页纸（STC-028GP $28 / STC-228GP $33 / STC-2224GP $86）' + TR + '**',
    '未坐实（1 查未中即停）→ 回 C 待下轮 1 查；土耳其主区 ✔ 微信可达 ✔；并入「土耳其微信追问公司名」清单。')

# ---------------- 葡萄牙 ----------------
row('SC-2969', 'pt', 'Metrikingdom Unipessoal Lda（metrikingdom.com；**NIF / NIPC 515518425；Rua Santa Marta N.º 43Ef, 3 D, 1150-293 Lisboa；2019-06-04 成立；Sociedade Unipessoal por Quotas；资本 € 6.000；CAE 62100 = 计算机编程活动（iberinform 2026-08 更新）**）；表内：Saleha Kanwal，+351 920 236 978，问 2 SFP + 2 RJ45 交换机', 'PT',
    'PT · 1 次检索：racius（NIF / 地址 / 成立日 / 资本）+ iberinform（CAE 62100 / 形式）；2026-10-29', 'https://www.racius.com/metrikingdom-unipessoal-lda/',
    '515518425（NIF / NIPC）', '营业中（iberinform 2026-08）', '2019-06-04', 'Sociedade Unipessoal por Quotas', 'IT 编程 / 服务（里斯本）—— 非网络设备分销', 'Rua Santa Marta N.º 43Ef, 3 D, 1150-293 Lisboa', '微型（独资有限，资本 € 6k）',
    ['Saleha Kanwal — 表内联系人（职务未取）'],
    '**葡萄牙（欧洲）· 微型 IT 服务商 25%：先回邮确认用途 / 数量（2 SFP + 2 RJ45 → STI-154GP 样机 $36 或 STC-228GP $33），预付 100% + DAP' + PT + '**',
    '集成 25%；P 池候选 △ 预付 100%（欧洲 ✔ 具体需求 ✔ 坐实 ✔；但 CAE 软件 + € 6k 资本 + 独资 = 微型、复购存疑）；坐实（NIF）。')

# ---------------- 拉脱维亚 ----------------
row('SC-1976', 'lv', 'Signalizācija（signalizacija.lv no_mx；tiger.cctv@inbox.lv；主要 CCTV，Utepo；**1 次检索未中（Lursoft 返回 SIA Signal 等非同一主体；signalizācija = 「报警系统」通名，难以指认法人）**）', 'LV',
    'LV · 1 次检索：Lursoft「SIA Signalizācija」未命中；2026-10-29', '',
    '未取（未坐实）', '未知', '未取', '未取', 'CCTV / 报警（拉脱维亚）', '未取', '未取',
    [],
    '**欧洲 · 待坐实：官网页脚 / 域名 whois 找法人名（Reģ. nr.）后再一页纸（STC-028GP $28 / STC-228GP $33）**',
    '未坐实（1 查未中即停）→ 回 C 待下轮 1 查；欧洲 ✔ 中国品牌 Utepo ✔ 但仅 inbox.lv 免费邮箱 + 一次询价。')

# ---------------- 俄罗斯 ----------------
row('SC-1613', 'ru', 'ORIGO Networks（origo-networks.ru；Simon「自己的白色外壳，有人在卖他们的」「比较重要」= 自有品牌；**1 次检索未中：rusprofile 两家 ООО «Ориго»（ИНН 7743272134 金融服务 2018 / ИНН 7727565486 咨询 2006）均非网络设备主体 = 同名壳 ≠ 品牌法人**）', 'RU',
    'RU · 1 次检索：rusprofile「ООО Ориго」仅同名壳，未指向 origo-networks.ru；2026-10-29', '',
    '未取（未坐实）', '未知', '未取', '未取', '网络设备自有品牌（俄罗斯）', '未取', '未取',
    [],
    '**俄罗斯 · 自有品牌 OEM 30% 待坐实：官网「Реквизиты / О компании」取 ИНН 后再一页纸（STC-028GP $28 / STC-2224GP $86 中性包装 + 贴牌）' + RU + '**',
    '未坐实（1 查未中即停）→ 回 C 待下轮 1 查（官网页脚 ИНН）；oem_target ✔ Simon「比较重要」✔；收款待定。')
row('SC-2957', 'ru', 'ConexPro（conexpro.com；Simon 二筛「基本是全线帧田的」= 自有品牌、全线中国 OEM；**1 次检索未中：rusprofile 返回 ООО «Коннект-Про»（ИНН 9702037865，2021，1 人，执行董事 Смольянинова К.М.）= 同名壳 ≠ 品牌法人**；无邮箱', 'RU',
    'RU · 1 次检索：rusprofile「Конекспро」仅同名壳 Коннект-Про，未指向 conexpro.com；2026-10-29', '',
    '未取（未坐实）', '未知', '未取', '未取', '网络 / 安防设备自有品牌（俄罗斯）', '未取', '未取',
    [],
    '**俄罗斯 · 自有品牌 OEM 30% 待坐实：官网「Контакты / Реквизиты」取 ИНН + 采购邮箱后再一页纸（帧田现供 → 推 SmartByte / Marvell 管理线差异）' + RU + '**',
    '未坐实（1 查未中即停）→ 回 C 待下轮 1 查；oem_target ✔（Simon 原「判定不行」→ 可按编号否决）；无邮箱；收款待定。')

# ---------------- 哈萨克斯坦 ----------------
row('SC-574', 'kz', 'IT Group（itgroup.kz；**1 次检索出两家同名：ТОО «IT GROUP KAZAKHSTAN» БИН 151040005191（2015-10-07；乌拉尔斯克 ул. Гумара Караша 33/2 оф. 8；负责人 Дудниченков М.М.；ОКЭД 62.01.1 软件；≤5 人）/ ТОО «KAZ - IT GROUP» БИН 210640025476（2021-06-17；奇姆肯特 ул. Еримбетова 304Г；视频监控 / 电信 / PON / GPON 供应商）—— 哪一家 = itgroup.kz 待官网页脚确认**）；表内：2022 年 RFQ「找 ONV 的商业管理交换机」，有回', 'KZ',
    'KZ · 1 次检索：niac.kz（两家同名 БИН / 地址 / 负责人 / ОКЭД）+ mp.kz（KAZ-IT Group 业务）；主体未唯一 → 部分坐实；2026-10-29', 'https://niac.kz/151040005191',
    '151040005191 或 210640025476（待指认）', '均在营（niac.kz）', '2015-10-07 / 2021-06-17', 'ТОО', 'IT / 视频监控 / 电信设备供应（哈萨克斯坦）', '乌拉尔斯克 ул. Гумара Караша 33/2 оф. 8 / 奇姆肯特 ул. Еримбетова 304Г', '小型（≤5 人 / 小企业）',
    ['Дудниченков Михаил Михайлович — IT GROUP KAZAKHSTAN 负责人（待指认）'],
    '**哈萨克斯坦（点名区外，先例 ✔）· 分销 20%：回邮引用 2022 RFQ 问法人名 + 收货城市，坐实后一页纸（STC-2224GP $86 / STC-4424GCPM $165 vs ONV）' + RU + '**',
    '分销 20%；部分坐实（两家同名待指认）→ 回 C 待下轮 1 查（itgroup.kz 页脚 БИН）；有回 ✔ 对位 ✔；收款待定。')
row('SC-1602', 'kz', 'LS Service（lsservice.kz；表内「俄罗斯」→ 哈萨克斯坦 国别待核；ls-servicom@yandex；**ТОО «LS SERVICE» БИН 210740005950；2021-07-06 注册；010000 Астана, р-н Сарыарка, ул. Бердібек Соқпақбаев 4, н.п. 6；负责人 / 创始人 Ерсабиров Салауат Жанбатырович；+7 778 336-62-77；ОКЭД 43220 = 水暖 / 空调安装（与网络设备不符 → 待核是否同一主体）**）', 'KZ',
    'KZ · 1 次检索：ba.prg.kz（БИН / 地址 / 负责人 / 电话 / ОКЭД，电子政务 2025-07-30 校验）；名称完全一致但 ОКЭД 不符 → 部分坐实；2026-10-29', 'https://ba.prg.kz/710000000-astana/210740005950-too-ls-service/',
    '210740005950（БИН）', '在营（电子政务 2025-07-30）', '2021-07-06', 'ТОО', '工程安装（ОКЭД 43220）—— 网络设备业务待核（阿斯塔纳）', '010000 Астана, ул. Бердібек Соқпақбаев 4, н.п. 6', '小型',
    ['Ерсабиров Салауат Жанбатырович — 负责人 / 创始人'],
    '**哈萨克斯坦 · 集成 25%：回 yandex 邮箱确认法人 = ТОО LS SERVICE（阿斯塔纳）及用途后一页纸（STI-054GP / STC-028GP $28 / STC-228GP $33），预付 100%' + RU + '**',
    '集成 25%；P 池候选 △ 预付 100%（先例 ✔ 对位 ✔ 坐实 ✔ 但 ОКЭД 水暖 + 2021 新 + 国别待核）；部分坐实（主体同名、业务不符）。')

print('b134_c done')
