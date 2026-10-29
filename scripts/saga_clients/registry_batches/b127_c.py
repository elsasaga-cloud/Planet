# -*- coding: utf-8 -*-
"""第 127 批（T29-U118c，2026-10-29）—— **C 池三闸 · 闸 2 第四批（闸 1 候选收尾）**：闸 1 第 07 / 08 批候选余 34 户 = 欧洲其他 + 加拿大 20（IT 4 / NO 2 / ES 5 / FR 2 / PT / NL / DK / EE / SK / CZ / CA）+ 其他区 14（IN 4 / TH 2 / UZ / RU / ZA / GT / PY / SA / AU / KR）查底数。
路径：IT 官网页脚（Redfox CF 01870630447 REA AP-180065；DEMA s.a.s. P.I. 13338240156；Lastella Trade P.I. 03695681209 REA BO-539359）+ Crunchbase / Confapi（Townet）；NO proff / gulesider（Alcadon AS org 952 334 891）+ 官网 About（Hatteland = EMBRON 子公司）；
CZ 官网 Terms（PARTIZAN SECURITY s.r.o. IČ 28909437；Praha C 152541）；FR societe.com / annuaire-entreprises（Sphinx Connect France SIREN 439 398 462）+ 官网（Pine Networks Garches）；EE inforegister / e-krediidiinfo（BK Eesti OÜ 10022238）；NL LinkedIn / ZoomInfo（Niveo = BNS Netstar bv / Niveo International bv，Hilversum）；
PT rigorbiz / nif.pt（PT Refurb NIF 510298370）；ES empresite / iberinform / einforma（Mercasat B92538883）+ datoscif + 官网 aviso legal（Todo Telecom B53673364；Calytel 个体 NIF 11857123W；SiSeCam Solutions S.L.U. 官网页脚）+ indisa / interempresas（Tempel, S.A. 1978）；CA 官网 + Facebook（Smart Access Mississauga）；
UZ yellowpages.uz / pc.uz / top.uz（SETKO ООО）；RU 官网（Satvision 萨马拉 12 分部）；ZA 官网 privacy（Duxbury Transmission Equipment (Pty) Ltd 2018/441897/07）；IN bharatibiz / zoominfo（Optilink Networks Pvt. Ltd. 孟买 20 人）+ zaubacorp（Prama Hikvision India CIN U36100MH2009PTC190094 = 海康 JV 体系）；
GT rocketreach / linkedin / pitchbook（Continental Towers Corp LATAM；mip.com.gt 未直接命中）；PY 官网 + radiosdeparaguay（Asociación Civil Radio ZP-30）；SA linkedin / prospeo（Al Rajhi Telecom = Al Rajhi Building & Construction 子公司）；TH 官网（บริษัท อัลฟา เบส มาร์เก็ตติ้ง จำกัด 1995）；AU crunchbase / bluebusinessguide / zoominfo（Optimal Cable Services Pty Ltd → AFL）。
1 查未得：kamery-hikvision.sk（仅返回同名他站）、nana-tech.net（仅 Nana Engineering 水泵 + thai.finance 同名合伙企业，域名未对上）→ 未坐实；gmail / hanmail 户 0 查：Pixelcube、KHUSHI ENTERPRISES、lsipro。国别纠偏：Partizan Store 「欧洲（国别未填）」→ 捷克；kamery-hikvision.sk 「斯洛文尼亚」→ 斯洛伐克（.sk）。每户 1 查、depth 1。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 127
F = '2026-10-29'
EU = '— 欧洲常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 预付 100%）+ DAP（买方清关）或 FOB 深圳；周四 12–14 当地'
US = '— 北美常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 预付 100%）+ FOB 深圳 / DAP（买方清关）；周三 08–10 当地'
OT = '— 区域外常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 预付 100%）+ FOB 深圳；低频一页纸'
Q33 = '；洪瑞现供 → Q-33 口径（默认只推 SmartByte / Marvell 管理 + 工业线）'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 意大利 ----------------
row('SC-2256', 'it', 'REDFOX S.R.L.（redfox-tech.com；**官网页脚：Via Pasubio 57/A, 63074 San Benedetto del Tronto (AP)；CF / Registro Imprese 01870630447；REA AP-180065；资本 €10,050；PEC redfox@pec-mail.it；防盗 / 视频监控 / 智能家居安装 15+ 年；Contatti 页：Marco Di Pietro — CEO & Sales Manager（m.dipietro@fifanetwork.it）、Gianluca Faraotti — 技术主管**）；表内：工商业 PoE 用 Utepo；14 推 0 回；Simon 曾判不行', 'IT',
    'IT · 1 次检索：redfox-tech.com 首页页脚（CF / REA / 资本）+ /contatti/（CEO 具名 + 邮箱公开）；2026-10-29', 'https://www.redfox-tech.com/contatti/',
    '01870630447（CF / Registro Imprese AP）', '营业中（官网 2024-12）', '未取（15+ 年）', 'S.r.l.', '安防集成 / 安装（马尔凯）', 'Via Pasubio 57/A, 63074 San Benedetto del Tronto (AP)', '微型（资本 €10,050）',
    ['Marco Di Pietro — CEO & Sales Manager（m.dipietro@fifanetwork.it，官网 contatti 页公开）', 'Gianluca Faraotti — Capotecnico（tecnicorf@fifanetwork.it 官网公开）'],
    '**小集成商 → 集成 25%：点名 Marco 一页纸一次（STC-028GP $28 / STI-154GP 工业 PoE + MOQ 1 + 付费样机；Utepo 不点名）' + EU + '**；微型 → 预付；Simon 可否决',
    '集成 25%；P 池候选 △（进口 Utepo ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔ + CEO 公开邮箱；微型集成商 → 观察档 + 预付）；坐实（CF / REA）；Simon 曾判不行。')
row('SC-2258', 'it', 'TOWNET S.R.L.（townet.it；**Crunchbase：Cagli, Marche；1–10 人；电信设备 / 能源系统 / 传感器制造；Confapi Pesaro 名录 + Sicurezza Milano 展商档：Via dei Finale 20, 61043 Cagli (PU)；0721-797396；2003 年创立，2018 起 SmartBox 供电 / 控制电柜 BU + 自有 IoT 云平台**）；表内：用 hasivo 的（安防 + 工业 FS）；enrico@ 具名；9 推 0 回；Simon 曾判不行', 'IT',
    'IT · 1 次检索：crunchbase（法人名 Townet Srl；Cagli；1–10）+ confapipesaro 名录（地址 / 电话）+ expoplaza-sicurezza 展商档（2003；SmartBox）；P.IVA 未取；2026-10-29', 'https://expoplaza-sicurezza.fieramilano.it/en/exhibitors/townet-s-r-l-1',
    '未取（P.IVA 未查）', '营业中（Crunchbase Active；2024 展商）', '2003', 'S.r.l.', '电信设备 + 智能供电柜（SmartBox）制造（马尔凯）', 'Via dei Finale 20, 61043 Cagli (PU)', '微型（1–10）',
    ['enrico@townet.it（表内具名；职务未取）'],
    '**自产 SmartBox 柜内配套交换机 → OEM 30% / 集成 25% 双轨：点名 Enrico 一页纸一次（STI-154GP / STI-288GPM 工业 PoE 柜内配套 + 丝印 MOQ + 付费样机；hasivo 不点名）' + EU + '**；Simon 可否决',
    'OEM 30%；P 池候选 ○（制造商 + 柜内配套 = 贴牌对象；欧洲 ✔ 对位 ✔）；部分坐实（P.IVA 未取）；Simon 曾判不行。')
row('SC-2260', 'it', 'DEMA s.a.s. — videosorveglianza.it（**官网页脚：Via Cavour 63, 20871 Vimercate (MB)；CF / P.I. 13338240156；CCIAA MI-1640818；视频监控套件网店（Safire Smart 等）**）；表内：商业 PoE 进口 ONV / 洪瑞 / Witek 多牌；14 推 0 回；Simon 曾判不行', 'IT',
    'IT · 1 次检索：videosorveglianza.it 首页页脚（DEMA s.a.s.；P.I.；CCIAA）；2026-10-29', 'https://www.videosorveglianza.it/',
    '13338240156（P.I.；CCIAA MI-1640818）', '营业中（官网 2024-09）', '未取', 's.a.s.（合伙）', 'CCTV 网店 / 安装（伦巴第）', 'Via Cavour 63, 20871 Vimercate (MB)', '微型',
    ['（info@videosorveglianza.it 表内总邮箱；具名 KP 未取）'],
    '**多牌进口微型网店 → 分销 20%：一页纸一次（STC-028GP $28 / STC-228GP $33 + MOQ 1 + 付费样机）' + EU + Q33 + '**；微型 → 预付；Simon 可否决',
    '分销 20%；P 池候选 △（多牌直进 ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔；微型 s.a.s. → 观察档 + 预付）；坐实（P.I.）；Q-33；Simon 曾判不行。')
row('SC-2941', 'it', 'Lastella Trade S.r.l. Società unipersonale — digitX.it（**官网 Chi siamo / Assistenza：CCIAA Bologna，CF / P.I. 03695681209，REA 539359；Via Galliera 62, 40050 Funo di Argelato (BO)；051 6604005；门户 2007 起（prodotti-moxa.it）、2012 被 Lastella 收购、2014 更名 digitX、2018 digitx 注册商标（自有光纤产品线）；在售 Moxa / Teltonika / Takachi / Patlite / Planet / Mean Well**）；表内：3onedata / Planet 工业 FS 买家（研究档）；退信；Simon 曾判不行', 'IT',
    'IT · 1 次检索：digitx.it/chi_siamo.asp（法人 / P.I. / REA / 沿革 / 商标）+ /assistenza.asp（地址 / 电话）；2026-10-29', 'https://www.digitx.it/chi_siamo.asp',
    '03695681209（P.I.；REA BO-539359）', '营业中（官网 2026）', '2012（Lastella 接手；门户 2007）', 'S.r.l. unipersonale', '工业电子 B2B 电商（自动化 / 工业网络 / 光纤；自有商标 digitx）', 'Via Galliera 62, 40050 Funo di Argelato (BO)', '小型',
    ['（info@digitx.it 表内 = 退信；官网仅表单 + 电话 051 6604005；采购 KP 待 LinkedIn）'],
    '**工业 B2B 电商 + 自有商标 digitx → 分销 20% / OEM 30%：一页纸一次（STI-154GP / STI-288GPM / STI-0240GE 对标 Moxa 入门 + 丝印 MOQ + 付费样机）' + EU + '**；退信 → 官网表单 / 电话换地址；Simon 可否决',
    'OEM 30%；P 池候选 ○（进口 3onedata / Planet ✔ 自有商标 ✔ 欧洲 ✔ 对位 ✔）；坐实（P.I. / REA）；Simon 曾判不行。')
# ---------------- 挪威 ----------------
row('SC-274', 'no', 'ALCADON AS（alcadon.no；**proff / gulesider：Org.nr 952 334 891；成立 1989-07-11 / 注册 1995-02-19；Aksjeselskap；股本 NOK 600,000；16 人；营业额 NOK 85,842 千；Alfaset 1. industrivei 4, 0668 Oslo；23 17 78 80；最大股东 Alcadon Mrv AB（瑞典 Alcadon 集团）；行业：电子 / 电信设备批发**）；表内：北欧布线 / 网络分销，很多 Planet 产品、CWDM；10 推 0 回', 'NO',
    'NO · 1 次检索：proff.no（org / 成立 / 股东 / 16 人）+ gulesider（营业额 85,842 tkr；3.1% 利润率）；2026-10-29', 'https://www.proff.no/selskap/alcadon-as/oslo/elektronikk-og-telekommunikasjonsutstyr-engros/IFQZUAZ10MZ-1',
    '952 334 891', '营业中（Foretaksregisteret）', '1989-07-11', 'AS（Alcadon 集团子公司）', '网络 / 布线分销（挪威；集团瑞典）', 'Alfaset 1. industrivei 4, 0668 Oslo', '小型（16；NOK 85.8M）',
    ['（salg@alcadon.no 表内总邮箱；产品经理 KP 待 LinkedIn；集团采购在瑞典）'],
    '**集团分销 → 分销 20%（长线）：一页纸一次（STC-228GP / STC-2224GP 对标 Planet 同口型 + MOQ 1 + 付费样机）' + EU + '**；体量偏大 → 同步找集团产品管理',
    '分销 20%；P 池候选 ○（集团分销 + Planet 渠道 + 欧洲 + 对位 = 冷户四条）；坐实（org.nr）。')
row('SC-490', 'no', 'Hatteland Technology AS（hattelandtechnology.com；**官网 About / Product Portfolio：总部 Aksdal（挪威）+ Lysaker（Strandveien 35）；EMBRON Group 全资子公司；约 200 人（挪威 / 瑞典 / 芬兰 + 德法意美）；自产船用 / 国防显示器、面板 PC；安防监控 / 工业网络 / 工业计算授权分销 + 北欧网店；mail@hattelandtechnology.com；NSI 分销页：Gøran Labrå**）；表内：工业 FS 用 ONV + Moxa，「分销有名牌子的」；15 推 0 回', 'NO',
    'NO · 1 次检索：hattelandtechnology.com/about（EMBRON；200 人；Aksdal / Lysaker）+ /product-portfolio（分销线 + 网店）+ nsi-be.com/distributors/norway（Lysaker 地址 + 联系人）；org.nr 未取；2026-10-29', 'https://www.hattelandtechnology.com/about',
    '未取（Brønnøysund 未查；法人名坐实）', '营业中（官网 2023–26）', '未取', 'AS（EMBRON 子公司）', '工业 IT 制造 + 工业网络 / 安防分销（北欧）', 'Aksdal, Norway（总部）/ Strandveien 35, 1366 Lysaker', '中型（约 200）',
    ['Gøran Labrå — 销售（goran.labra@hattelandtechnology.com；NSI 分销页公开）', '（mail@ / sales.sweden@ 表内）'],
    '**工业分销 + 自产 → 分销 20%：一页纸一次（STI-154GP / STI-288DGGPM 工业 + STC-424XGGM + MOQ 1 + 付费样机；船用型式认证不承诺）' + EU + '**；长线',
    '分销 20%；P 池候选 ○（中型工业分销 + 进口 ONV ✔ 欧洲 ✔ 对位 ✔）；部分坐实（org.nr 未取）。')
# ---------------- 斯洛伐克 / 捷克 ----------------
row('SC-3057', 'sk', 'kamery-hikvision.sk（**1 查仅返回同名他站：hik-kamery.sk = Insomnium s.r.o. IČO 46590129；kamery-hikvision-sk.sk（Svornosti 50, Bratislava）；maxalarm.sk = EUROIN a.s. —— 均非本域名 → 经营主体未坐实**）；国别纠偏：表内「斯洛文尼亚」→ 斯洛伐克（.sk）；表内：Wi-Tek 的；退信；Simon 曾判不行', 'SK',
    'SK · 1 次检索：hik-kamery.sk 隐私页 + kamery-hikvision-sk.sk 联系页 + maxalarm.sk（均为同名他站）；ORSR 未查；2026-10-29', 'https://www.kamery-hikvision-sk.sk/kontaktujte-nas',
    '未取（经营主体未命中）', '未坐实', '未取', '未取', 'CCTV 网店（斯洛伐克；推定）', '未取', '微型（推定）',
    ['（predaj@kamery-hikvision.sk 表内 = 退信）'],
    '**未坐实 + 退信 → 不动**；国别改斯洛伐克（待 Simon 确认）',
    '回 C 储备（1 查未命中经营主体 + 退信 + Simon 判不行）；国别纠偏 SK。')
row('SC-2609', 'cz', 'PARTIZAN SECURITY s.r.o. — partizanstore.eu（**官网 Terms / Privacy：IČ 28909437；DIČ CZ28909437；Kresomyslova 384/17, Nusle, 140 00 Praha；布拉格市法院商事登记 C 152541；+420 776 345 933；About：Partizan = 2008 年创立的欧洲安防品牌，自产硬件 + 自研软件（IP / AHD CCTV、门禁、Partizan 软件 26 语种），总部布拉格，项目遍及 60+ 国**）→ 国别纠偏：表内「欧洲（国别未填）」→ 捷克；表内：商业 PoE 主要是洪瑞的；17 推 0 回；Simon 曾判不行', 'CZ',
    'CZ · 1 次检索：partizanstore.eu/en/commercial-terms-and-conditions/（IČ / 地址 / 登记）+ /about-us/（品牌沿革）；2026-10-29', 'https://www.partizanstore.eu/en/commercial-terms-and-conditions/',
    '28909437（IČ；Praha C 152541）', '营业中（官网 2026）', '未取（品牌 2008）', 's.r.o.', '自有品牌 CCTV / 门禁（硬件 + 软件）+ 欧洲网店', 'Kresomyslova 384/17, Nusle, 140 00 Praha 4', '小型（推定）',
    ['（sales@partizanstore.eu 表内总邮箱；产品经理 KP 待 LinkedIn）'],
    '**自有品牌 CCTV 配套 PoE 现由洪瑞供 → OEM 30%：一页纸一次（STC-028GP / STC-228GP / STC-2224GP 丝印 + MOQ + 付费样机）' + EU + Q33 + '**；Simon 可否决',
    'OEM 30%；P 池候选 ★（自有品牌 + 现成贴牌需求 + 欧洲 + 坐实）；坐实（IČ）；国别纠偏 CZ；Q-33；Simon 曾判不行。')
# ---------------- 法国 ----------------
row('SC-3135', 'fr', 'SPHINX CONNECT FRANCE（sphinxconnect.fr / sphinxcomputer.fr；**societe.com / annuaire-entreprises：SIREN 439 398 462；SIRET 总部 439 398 462 00044；TVA FR27439398462；创立 2001-10-10；SAS（原 SARL）；20–49 人；NAF 46.51Z 计算机 / 外设批发；Parc de la Bretonnière, 85600 Montaigu-Vendée（Boufféré）；4 个机构 1 个在营**）；表内：工业 FS 好几个牌子 = 工业网络分销商；Simon 曾判不行', 'FR',
    'FR · 1 次检索：societe.com（SIREN / 人数 / NAF）+ annuaire-entreprises.data.gouv.fr（RNE 2001-10-10；机构）+ lefigaro entreprises（SAS）；2026-10-29', 'https://annuaire-entreprises.data.gouv.fr/entreprise/439398462',
    '439 398 462（SIREN）', '营业中（RNE 在册）', '2001-10-10', 'SAS', '工业网络 / IT 设备批发（旺代）', 'Parc de la Bretonnière, 85600 Montaigu-Vendée', '小型（20–49）',
    ['（sales@sphinxconnect.fr 表内总邮箱；产品经理 KP 待 LinkedIn）'],
    '**工业分销 → 分销 20%：一页纸一次（STI-154GP / STI-288GPM / STI-0240GE + MOQ 1 + 付费样机）' + EU + '**；Simon 可否决',
    '分销 20%；P 池候选 ○（工业分销 + 欧洲 + 对位 + 坐实 = 冷户四条）；坐实（SIREN）；Simon 曾判不行。')
row('SC-345', 'fr', 'Pine Networks（pine-networks.com；**官网：219 Grande Rue, 92380 Garches；+33 1 88 94 77 04；contact@pine-networks.com；开放网络交钥匙集成（Edgecore / Adtran / UfiSpace 等，数据中心 1G–800G）+ 自研监控 PMO；客户云服务商 / ISP / 企业**）；表内：Edgecore 的；christophe@ 具名；名单内未触达', 'FR',
    'FR · 1 次检索：pine-networks.com 首页（地址 / 电话 / 合作品牌）+ /data-center/ + /portfolios/sonic/；SIREN 未取；2026-10-29', 'https://pine-networks.com/',
    '未取（SIREN 未查）', '营业中（官网 2026-01）', '未取', 'SAS（推定）', '开放网络 / 数据中心集成（巴黎西郊）', '219 Grande Rue, 92380 Garches', '微型 / 小型（推定）',
    ['christophe@pine-networks.com（表内具名；职务未取）'],
    '**DC 白盒集成 → 集成 25%（CENTEC 敲门砖）：点名 Christophe 一页纸一次（STH-2C24XF-HSI $1,500 / STH-8C48DX-HSI 接入层 + 付费样机）' + EU + '**；客户稿内不提 SONiC / ONIE',
    '集成 25%；P 池候选 ○（DC 对位 + 具名 KP + 欧洲 + 坐实（官网）= 冷户四条）；部分坐实（SIREN 未取）。')
# ---------------- 爱沙尼亚 ----------------
row('SC-468', 'other', 'BK EESTI OÜ（bkeesti.ee；**inforegister / e-krediidiinfo / infopank：注册码 10022238；1996-03-29 注册（前身 Balti Kontaktide AS 1994）；VAT EE100265240；Järveotsa tee 50c, 13520 Tallinn；+372 6506901；2020 转为 OÜ，与 SIA BK Latvia、UAB BK grupė（立陶宛）同属 BK 集团（控制权转换公告）；登记邮箱 andrius@bkgrupe.lt**）；表内：CCTV 为主，有 Utepo 的；martin.kirk@ / oskar.ojaste@ 具名；15 推 0 回', 'EE',
    'EE · 1 次检索：inforegister.ee（注册码 / 日期 / VAT / 集团公告）+ e-krediidiinfo（地址 / 曾用名）+ infopank（电话）；2026-10-29', 'https://www.inforegister.ee/en/10022238-BK-EESTI-OU/',
    '10022238', '营业中（Registered）', '1996-03-29', 'OÜ（BK 集团）', '安防 / 弱电分销（波罗的海三国集团）', 'Järveotsa tee 50c, 13520 Tallinn', '小型（推定）',
    ['Martin Kirk（martin.kirk@bkeesti.ee 表内具名；职务未取）', 'Oskar Ojaste（oskar.ojaste@bkeesti.ee 表内具名）', '（集团采购 andrius@bkgrupe.lt 登记邮箱 — 仅备查）'],
    '**波罗的海集团分销 → 分销 20%：点名 Martin 一页纸一次（STC-028GP / STC-228GP + STI-154GP + MOQ 1 + 付费样机；Utepo 不点名）' + EU + '**',
    '分销 20%；P 池候选 ○（集团分销 + 进口 Utepo ✔ 欧洲 ✔ 对位 ✔ 具名 KP ✔）；坐实（注册码）。')
# ---------------- 荷兰 ----------------
row('SC-3302', 'nl', 'Niveo Professional — BNS Netstar bv / Niveo International bv（niveoprofessional.com；**LinkedIn：Hilversum；2009 年创立；2–10 人；面向专业 A/V 安装商的自有网络品牌；Arthur de Jager = BNS Netstar bv 共同所有人 / Niveo International bv 董事总经理（= 表内 arthur@）；北美销售总监 David Stephens；ZoomInfo：Olympia 2D, Hilversum；营收估 $6.9M；制造业 / 电信设备**）；表内：自有品牌 Niveo 全线（商业 PoE / 10G / MC / 机架 / SFP / 大口 FS）；15 推 0 回 + 退信；Simon 曾判不行', 'NL',
    'NL · 1 次检索：linkedin.com/company/netstar-products-bv（2009；2–10；Arthur de Jager 职务）+ zoominfo（Olympia 2D；$6.9M）；KvK 未取；2026-10-29', 'https://www.linkedin.com/company/netstar-products-bv',
    '未取（KvK 未查）', '营业中（LinkedIn 2024 更新）', '2009', 'B.V.（BNS Netstar bv / Niveo International bv）', '自有品牌网络产品（A/V 安装渠道；欧美）', 'Olympia 2D, Hilversum', '微型（2–10；$6.9M）',
    ['Arthur de Jager — Co-owner BNS Netstar bv / MD Niveo International bv（arthur@niveoprofessional.com 表内 = 决策人直达）', 'jaap@niveoprofessional.com（表内具名）', 'David Stephens — Director of Sales North America'],
    '**全线自有品牌 → OEM 30%：点名 Arthur 一页纸一次（STC-228GP / STC-2224GP / STC-4424GCPM L2+ 丝印 + 10G 口型 STC-424XGGM + MOQ + 付费样机）' + EU + '**；退信 → 改发 arthur@ / jaap@；Simon 可否决',
    'OEM 30%；P 池候选 ★（全线自有品牌 + 决策人邮箱在表 + 欧洲 + 对位）；部分坐实（KvK 未取）；Simon 曾判不行。')
# ---------------- 葡萄牙 ----------------
row('SC-2870', 'pt', 'PT REFURB, UNIPESSOAL LDA（ptrefurb.pt；**rigorbiz / nif.pt / 官网 Terms：NIF 510298370；成立 2012-06-01；资本 €15,000；CAE 47401 计算机 / 外设零售；Rua do Pinheiro 363, 4410-037 Serzedo, Vila Nova de Gaia；自称「全国最大翻新电脑进口分销商、伊比利亚最大之一」**）；表内：洪瑞的商业 PoE；17 推 0 回；Simon 曾判不行', 'PT',
    'PT · 1 次检索：rigorbiz.pt（NIF / 资本 / CAE / 地址）+ nif.pt + ptrefurb.pt/en/termos-e-condicoes/（法人 + 定位）；2026-10-29', 'https://www.rigorbiz.pt/pt-refurb-unipessoal-lda',
    '510298370（NIF）', '营业中（Ativa）', '2012-06-01', 'Unipessoal Lda', '翻新电脑进口 / 零售（CAE 47401）', 'Rua do Pinheiro 363, 4410-037 Serzedo, Vila Nova de Gaia', '小型（资本 €15k）',
    ['（geral@ptrefurb.pt 表内总邮箱）'],
    '**主业翻新电脑零售，PoE 为边角 → 不动**' + Q33,
    '回 C 储备（坐实但主业不对位 CAE 47401 + 冷户 0 回 + Simon 判不行）；Q-33。')
# ---------------- 西班牙 ----------------
row('SC-2633', 'es', 'SiSeCam Solutions S.L.U.（sisecam.es / sisecamtiendaonline.es；**官网页脚：Oficina Central Avenida Condes de San Isidro 47, Planta 1ª Of. 2, Edificio Madrid, 29640 Fuengirola (Málaga)；+34 952 637 131；axis@sisecam.es；Axis 全线网店（对讲 / 音频 / 门禁，备货 + 10 天交付）**）；表内：工业 FS；Axis 及其他牌子分销；邮件 fail；Simon 曾判不行', 'ES',
    'ES · 1 次检索：sisecamtiendaonline.es（Axis 网店 3 页，页脚法人 S.L.U. + 地址 + 电话）；CIF 未取；2026-10-29', 'https://sisecamtiendaonline.es/Control-de-acceso-fisico-Axis/Axis-Network-Intercoms-Series',
    '未取（CIF 未查）', '营业中（网店 2024 版权）', '未取', 'S.L.U.', 'Axis 安防网店 / 分销（马拉加）', 'Av. Condes de San Isidro 47, 1ª Of. 2, 29640 Fuengirola (Málaga)', '微型 / 小型',
    ['（axis@sisecam.es 表内 = 曾 fail；官网仍公示同址；具名 KP 未取）'],
    '**Axis 体系网店 → 分销 20%：一页纸一次（STC-028GP / STC-228GP 配套 Axis 摄像机 + STI-154GP + MOQ 1 + 付费样机）' + EU + '**；邮件 fail → 官网表单 / 电话；Simon 可否决',
    '分销 20%；P 池候选 △（分销 ✔ 欧洲 ✔ 对位 ✔ 坐实 部分 ✔；Axis 体系微型 → 观察档）；部分坐实（CIF 未取）；Simon 曾判不行。')
row('SC-2718', 'es', 'MERCASAT SL（mercasat.es；**empresite / iberinform / einforma：CIF B92538883；Sociedad limitada unipersonal；资本 €3,120；CNAE 4652 电子 / 电信设备批发；Calle La Boheme 22 esq. Sal Marina, Pol. Ind., 29006 Málaga；952 105 737；22 年；BORME 2006 章程修改**）；表内：商业 PoE 好几种外壳、好多家国内牌子；Simon 曾判不行', 'ES',
    'ES · 1 次检索：empresite.eleconomista.es（CIF / 形式）+ iberinform（地址 / CNAE / Activa）+ einforma（资本 €3,120；BORME）；2026-10-29', 'https://www.iberinform.es/empresa/1329911/mercasat',
    'B92538883（CIF）', '营业中（Activa）', '约 2004（22 年）', 'S.L. unipersonal', '卫星 / 电信 / 电子设备批发（马拉加）', 'Calle La Boheme 22, Pol. Ind., 29006 Málaga', '微型（资本 €3,120）',
    ['（info@mercasat.es 表内总邮箱；具名 KP 未取）'],
    '**多牌进口批发 → 分销 20%：一页纸一次（STC-028GP $28 / STC-228GP $33 + MOQ 1 + 付费样机）' + EU + '**；资本微型 → 预付；Simon 可否决',
    '分销 20%；P 池候选 △（多牌直进 ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔；资本 €3,120 微型 → 观察档 + 预付）；坐实（CIF）；Simon 曾判不行。')
row('SC-2725', 'es', 'TODO TELECOM, S.L.（todotelecom.com；**datoscif + 官网 aviso legal：CIF B53673364；Registro Mercantil de Alicante T 2552 F 86 H A-71082；资本 €26,800；Pol. Ind. Juyarco 40-A, Partida Madrigueres Sud, 03700 Dénia (Alicante)；96 578 44 63；BORME 2023-08 委任代理人 Francisco Manuel Valero Tello；webinfo@todotelecom.com**）；表内：商业 PoE 为主、多种外壳、销售平台、网站有 WA 按钮；Simon 曾判不行', 'ES',
    'ES · 1 次检索：datoscif.es（CIF / 资本 / BORME）+ todotelecom.com/content/3-condiciones-genrales-de-uso（登记）+ /content/2-aviso-legal-politica-privacidad（地址 / 电话）；2026-10-29', 'https://www.datoscif.es/empresa/todo-telecom-sl',
    'B53673364（CIF；RM Alicante H A-71082）', '营业中（BORME 2023）', '未取（2014 前）', 'S.L.', '电信 / 网络设备网店 + 批发（阿利坎特）', 'Pol. Ind. Juyarco 40-A, 03700 Dénia (Alicante)', '小型（资本 €26.8k）',
    ['Francisco Manuel Valero Tello — Apoderado（BORME 2023-08-31）', '（webinfo@todotelecom.com 表内总邮箱）'],
    '**多牌网店 → 分销 20%：一页纸一次（STC-028GP / STC-228GP / STC-2216GP + MOQ 1 + 付费样机）' + EU + '**；Simon 可否决',
    '分销 20%；P 池候选 △（多牌直进 ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔；网店小型 → 观察档）；坐实（CIF）；Simon 曾判不行。')
row('SC-2760', 'es', 'TEMPEL, S.A. — Tempel Group（tempelgroup.com；**indisa 名录：C/ Cobalto 4, 08907 L\'Hospitalet de Llobregat (Barcelona)；品牌 Panasonic / Transcend / Advantech / Moxa / Robustel / Getac / IEI / AAEON 等；interempresas / automaticaeinstrumentacion：1978 年巴塞罗那创立，电子品牌分销（西 + 葡）+ 拉美分部（阿根廷 / 智利 / 哥伦比亚 / 巴西 / 秘鲁 / 墨西哥），工业 + 消费双线，客户含大型工程公司**）；表内：Moxa 分销 = 工业电子分销集团；Simon 曾判不行', 'ES',
    'ES · 1 次检索：indisa.es（法人 TEMPEL, S.A.；地址；品牌）+ interempresas（35 周年 2013；拉美分部）+ automaticaeinstrumentacion；CIF 未取；2026-10-29', 'https://www.indisa.es/empresas/tempel-sa-barcelona',
    '未取（CIF 未查；法人名 S.A. 坐实）', '营业中（名录 + 官网）', '1978', 'S.A.', '工业 / 消费电子分销集团（伊比利亚 + 拉美 6 国）', 'C/ Cobalto 4, 08907 L\'Hospitalet de Llobregat (Barcelona)', '中型（集团；多国分部）',
    ['（info@tempelgroup.com 表内总邮箱；工业线产品经理 KP 待 LinkedIn）'],
    '**工业分销集团（Moxa 在售）→ 分销 20%：一页纸一次（STI-154GP / STI-288GPM / STI-0240GE 入门工业线对标 + MOQ 1 + 付费样机；Moxa 不点名）' + EU + '**；拉美分部可带出口；Simon 可否决',
    '分销 20%；P 池候选 ★（中型集团分销 + 工业对位 + 欧洲 + 坐实）；部分坐实（CIF 未取）；Simon 曾判不行。')
row('SC-3266', 'es', 'Calytel Distribución de Sistemas de Seguridad — Francisco Santos González（calytel.com / calytel.es / calytel.info；**官网 Aviso Legal：个体 NIF 11857123W；Espada 6, Bajo C, 28923 Alcorcón (Madrid)；门店 C/ Los Mesejo 25, 28007 Madrid；910 82 12 50；安防电子产品分销网店**）；表内：很多国内产品、CCTV 为主、「卖下边公司的」；Simon 曾判不行', 'ES',
    'ES · 1 次检索：calytel.com/PBCPPlayer.asp?ID=1688672（aviso legal：个体 NIF / 地址）+ calytel.info/aviso-legal/；2026-10-29', 'https://www.calytel.info/aviso-legal/',
    '11857123W（个体 NIF）', '营业中（官网在线）', '未取', '个体经营（autónomo）', '安防产品分销网店（马德里）', 'Espada 6, Bajo C, 28923 Alcorcón (Madrid)', '个体微型',
    ['Francisco Santos González — 业主（info@calytel.com 表内 = 官网公示）'],
    '**个体微型网店 + 冷户 0 回 → 不动**',
    '回 C 储备（个体 NIF 坐实但微型 + 冷户 + Simon 判不行）。')
# ---------------- 加拿大 ----------------
row('SC-2832', 'ca', 'Smart Access — SASTORE.ca（smartaccess.ca；**官网 n.smartaccess.ca + Facebook：25 Helene St N, Mississauga, ON L5G 3B6；1-844-244-2299；info@smartaccess.ca；IP / AHD / TVI 监控 + PoE 网络设备网店**；注意：Google Play 的 Smart Access Inc.（1904038 Alberta Ltd，Edmonton，零售软件）为同名他司）；法人名未取 → 部分坐实；表内：商业 PoE 国内外壳、CCTV；退信；Simon 曾判不行', 'CA',
    'CA · 1 次检索：n.smartaccess.ca（地址 / 电话 / 邮箱 / 品类）+ facebook.com/SmartAccessCanada（Mississauga）；法人名 / 注册号未取；2026-10-29', 'https://n.smartaccess.ca/',
    '未取（法人名未取）', '营业中（官网 2021 存档；Facebook 在线）', '未取', '未取', 'CCTV / PoE 网店（安大略）', '25 Helene St N, Mississauga, ON L5G 3B6', '微型',
    ['（info@smartaccess.ca 表内 = 退信）'],
    '**微型网店 + 退信 + 法人未取 → 不动**',
    '回 C 储备（微型 CCTV 网店 + 退信 + 法人未取 + Simon 判不行）。')
# ---------------- 丹麦 ----------------
row('SC-2872', 'other', 'SEVECU Security（sevecu.com / sevecu.dk；**官网：丹麦语 + 英语安防网店，品类 Dahua / AirSpace / 「Branded」/「MARCA BLANCA」白标 PoE（= Visiotech 西班牙目录体系）**；CVR 未取 → 法人未坐实）；表内：商业 PoE 大华 / ONV / 洪瑞；17 推 0 回；Simon 曾判不行', 'DK',
    'DK · 1 次检索：sevecu.dk（Dahua / 白标 PoE 产品页 ×2）+ sevecu.com（AirSpace SEV-0004139）；CVR 未取；2026-10-29', 'https://www.sevecu.com/sev-0004139-detail',
    '未取（CVR 未查）', '营业中（网店在线）', '未取', '未取（ApS 推定）', '安防网店（丹麦；Visiotech 目录下游）', '未取', '微型（推定）',
    ['（sales@sevecu.com 表内总邮箱）'],
    '**Visiotech 渠道下游 + 法人未取 → 不动（Visiotech SC-371 已在池）**' + Q33,
    '回 C 储备（Visiotech 下游 + CVR 未取 + 冷户 + Simon 判不行）；Q-33。')
# ---------------- 乌兹别克斯坦 ----------------
row('SC-1393', 'other', 'SETKO ООО — 「Умный Дом」（setko.uz；**yellowpages.uz / pc.uz / top.uz：塔什干 Mirzo-Ulugbek 区（просп. Мустакиллик 2 / м-в Ирригатор 2）；+998 71 237-29-77；Panasonic / Siemens / Samsung 企业通信系统官方供应商 + 安防 / 网络 / 智能家居；top.uz 公开邮箱 info@ / nikolay@setko.uz；信息更新 2025-07**）；表内：2018/19 买过洪瑞 PoE 交换机；退信但 MX 正常', 'UZ',
    'UZ · 1 次检索：yellowpages.uz（法人 SETKO ООО）+ pc.uz（品类 / 电话 / 2025 更新）+ top.uz（nikolay@ 公开）；ИНН 未取；2026-10-29', 'https://pc.uz/company/10212-setko',
    '未取（ИНН 未查；法人名坐实）', '营业中（名录 2025-07 更新）', '未取', 'ООО', '企业通信 / 安防 / 网络集成 + 门店（塔什干）', 'Мирзо-Улугбекский район, Ташкент 100000', '小型（推定）',
    ['Nikolay（nikolay@setko.uz；top.uz 公开 — 职务未取）', '（info@ / sales@setko.uz 表内；曾退信）'],
    '**成单户回访 → 分销 20% / 集成 25%：改发 nikolay@ 一页纸一次（STC-028GP / STC-228GP + STI-154GP + MOQ 1）' + OT + Q33 + '**',
    '成单回访；P 池候选 ○（成单 ✔ 对位 ✔ 坐实 ✔ 区域次优）；部分坐实（ИНН 未取）；Q-33。')
# ---------------- 俄罗斯 ----------------
row('SC-1942', 'ru', 'Satvision（satvision-cctv.ru / satvision.pro；**官网：视频监控设备自有商标 20+ 年；中央办公室 Самара, ул. Санфировой 95 к.1；8 800 550-12-51；satvision@satv.ru；全俄 12 个分部；自研软件；客户含 Сбербанк / Ростелеком / РЖД / Почта России**；法人 ООО 名 / ИНН 未取）；表内：自有 logo，Mike Yakushev（m.yakushev@satv.ru）回过 1 次，15 次跟进', 'RU',
    'RU · 1 次检索：satvision-cctv.ru 首页（地址 / 分部 / 客户）+ /company/（品牌定位）+ satvision.pro；ИНН 未取（rusprofile 下轮）；2026-10-29', 'https://satvision-cctv.ru/company/',
    '未取（ИНН 未查）', '营业中（官网在线）', '未取（20+ 年）', 'ООО（推定）', '自有品牌 CCTV（萨马拉；12 分部）', 'ул. Санфировой 95 к.1, Самара', '中型（12 分部）',
    ['Mike Yakushev（m.yakushev@satv.ru 表内 = 真回 KP；职务未取）'],
    '**自有品牌 CCTV 配套 PoE → OEM 30%：点名 Mike 一页纸一次（STC-028GP / STC-228GP / STC-2224GP 丝印 + MOQ + 付费样机）；预付款 + 待 Simon 定收款 / 物流路径**',
    'OEM 30%；P 池候选 ★（真回 + 自有品牌 + 体量）；部分坐实（ИНН 未取）；RU 收款路径待 Simon。')
# ---------------- 南非 ----------------
row('SC-1493', 'other', 'DUXBURY TRANSMISSION EQUIPMENT (PTY) LIMITED t/a Duxbury Networking（duxbury.co.za；**官网 Privacy Policy：注册号 2018/441897/07；Block 1, Riviera Office Park, 66 Oxford Rd, Parktown, Johannesburg 2193；telecoms-channel 档：1984 年创立，JHB / CT / DBN 三分部，8,000+ 经销伙伴，增值分销（Netgear / HPE Aruba / Extreme / Cambium / Proxim / Axis / Sophos / Milesight 独家）**）；表内：要过 8 光 8 管理 PoE 样品、「也卖很多商业 PoE」；3 具名邮箱；16 推 0 回', 'ZA',
    'ZA · 1 次检索：duxbury.co.za/privacy-policy/（法人 + 注册号 + 地址）+ telecoms-channel.co.za（沿革 / 品牌 / 规模）；2026-10-29', 'https://www.duxbury.co.za/privacy-policy/',
    '2018/441897/07', '营业中（官网 2026）', '1984（现法人 2018）', '(Pty) Ltd', '网络 / 无线 / 安防增值分销（南非三分部）', 'Block 1, Riviera Office Park, 66 Oxford Rd, Parktown, Johannesburg 2193', '中型（8,000+ 经销商）',
    ['T. van Schalkwyk（tvanschalkwyk@duxnet.co.za 表内具名）', 'P. Stuttard（pstuttard@duxnet.co.za 表内具名）', 'J. Pillay（jpillay@duxnet.co.za 表内具名）'],
    '**大分销 → 分销 20%：点名曾索样者一页纸一次（STC-4424GCPM L2+ Marvell $165 对标其索样口型 + STC-228GP + MOQ 1 + 付费样机）' + OT + '**；次优区长线',
    '分销 20%；P 池候选 ★（中型分销 + 索样互动 + 具名 KP + 坐实）；坐实（注册号）。')
# ---------------- 印度 ----------------
row('SC-343', 'in', 'Optilink Networks Pvt. Ltd.（optilinknetwork.com；**ZoomInfo：501/502 Sanjona Complex, Plot 11-A, Hemu Kalani Chembur Rd, Mumbai 400071；20 人；自有品牌 Optilink 网络 / 无线 / VoIP / IPTV / 数字前端全线分销，全球渠道伙伴；bharatibiz：Shashank Shah — Manager（shashank@optilinknetwork.com）；RocketReach：Vinit Savla = 高级网络工程师（表内 KP 实为工程岗）**）；表内：MC / SFP / FS / 周边自有品牌；未触达', 'IN',
    'IN · 1 次检索：zoominfo（地址 / 20 人 / 定位）+ bharatibiz（Manager 具名 + 邮箱）+ rocketreach（Vinit Savla 职务）；CIN 未取（zaubacorp 下轮）；2026-10-29', 'https://www.zoominfo.com/pic/optilink-networks-pvt-ltd/347261750',
    '未取（CIN 未查；法人名坐实）', '营业中（名录在线）', '未取', 'Pvt. Ltd.', '自有品牌网络 / 光通信产品（孟买）', '501/502 Sanjona Complex, Hemu Kalani Chembur Rd, Mumbai 400071', '小型（20）',
    ['Shashank Shah — Manager（shashank@optilinknetwork.com；bharatibiz 公开）', 'Vinit Savla — Senior Network Engineer（表内 KP；非采购）'],
    '**自有品牌全线 → OEM 30%：点名 Shashank 一页纸一次（STC-028GP / STC-228GP / STC-2224GP 丝印 + STC-110XGE MC + MOQ + 付费样机）' + OT + '**；印度次优区',
    'OEM 30%；P 池候选 ○（自有品牌 + 次优区 + 坐实；冷）；部分坐实（CIN 未取）。')
row('SC-347', 'in', 'Prama India（pramaindia.in；**1 查命中 PRAMA HIKVISION INDIA PRIVATE LIMITED（zaubacorp：CIN U36100MH2009PTC190094；2009-02-03；ROC Mumbai；海康威视合资子公司，37 分部 / 26 RMA 中心，Goregaon East 总部；industrialautomationindia：10K+ 人，营收 ₹500–1K Cr）—— pramaindia.in 为 Prama 方域名，法人未直接命中 → 部分坐实**）；表内：CCTV 为主 + 商业 PoE 自有 logo；未触达', 'IN',
    'IN · 1 次检索：zaubacorp（Prama Hikvision CIN）+ exportersindia + industrialautomationindia（JV 沿革 / 规模）；pramaindia.in 自身法人未命中；2026-10-29', 'https://www.zaubacorp.com/PRAMA-HIKVISION-INDIA-PRIVATE-LIMITED-U36100MH2009PTC190094',
    'U36100MH2009PTC190094（JV 公司；pramaindia.in 法人另待）', '营业中（Active）', '2009-02-03（JV）', 'Pvt. Ltd.（海康 JV）', 'CCTV 制造 / 分销（海康印度体系）', 'Oberoi Commerz II, Goregaon (East), Mumbai 400063（JV 总部）', '巨型（10K+；₹500–1K Cr）',
    ['（sales@pramaindia.in 表内总邮箱）'],
    '**海康 JV 体系，PoE 自配 → 不动（oem 备注留档）**',
    '回 C 储备（巨头 / 中资 JV 体系 + 域名法人未直接命中 + 未触达）；oem 备注。')
row('SC-1025', 'in', 'Pixelcube（**gmail 户 pixelcube.siran@gmail.com；无域名 / 法人 → 0 查**）；表内：Siran（WeChat siran-pixel）问 SKD、要全系列价目、想来公司看', 'IN',
    'IN · 0 查（gmail 个体，无可查主体）；2026-10-29', '',
    '未取（无主体）', '未坐实', '未取', '未取', '未取（SKD / 贴牌意向）', '未取', '未取',
    ['Siran（pixelcube.siran@gmail.com 表内；WeChat siran-pixel）'],
    '**无法人 → 不动；若其来信 / 微信再起则按 OEM 30% + 预付 100% 走**',
    '回 C 储备（gmail 个体 0 查未坐实；SKD 意向留档）。')
row('SC-2386', 'in', 'KHUSHI ENTERPRISES（**gmail 户 panaji@gmail.com；无域名 → 0 查**）；表内：「import from ONV, need price list, LG distributor」', 'IN',
    'IN · 0 查（gmail，无可查主体）；2026-10-29', '',
    '未取（无主体）', '未坐实', '未取', '未取（商号）', '进口分销（推定；果阿？）', '未取', '未取',
    ['（panaji@gmail.com 表内）'],
    '**无法人 → 不动；来信再起则预付 100%**',
    '回 C 储备（gmail 商号 0 查未坐实）。')
# ---------------- 危地马拉 ----------------
row('SC-2955', 'other', 'Continental Towers Guatemala, S.A.（mip.com.gt；**1 查命中 Continental Towers Corp LATAM（LinkedIn：拉美最大私营通信铁塔商，18+ 年，中美洲 / 秘鲁 / 哥伦比亚；11–50 人；2da calle 7-93 zona 14, Plaza Las Conchas 701, Guatemala 01014；PitchBook：2008 成立，母公司 Terra Towers；RocketReach：$3M / 18 人）—— mip.com.gt 域名未直接命中 → 部分坐实**）；表内：「下过两次单买 2 光 3 电和收发器」= 复购户；英语不好；Simon 曾判不行', 'GT',
    'GT · 1 次检索：rocketreach（规模 / 地址）+ linkedin（定位 / 分部）+ pitchbook（2008；Terra Towers）；mip.com.gt 法人未直接命中；2026-10-29', 'https://www.linkedin.com/company/continental-towers',
    '未取（登记未查）', '营业中（LinkedIn 2026 更新）', '2008', 'S.A.', '通信铁塔基础设施（中美洲）', '2da calle 7-93 zona 14, Plaza Las Conchas 701, Guatemala 01014', '小型（11–50）',
    ['（info@ / sistemas@mip.com.gt 表内总邮箱；IT 系统部）'],
    '**复购终端回访 → 直客价（分销 20% 口径）：一页纸一次（STC-228GP 2 光 / STI-154GP 站点用 + STC-110XGE MC + MOQ 1；西语一句问候可加）' + OT + '**；区域外低频',
    '成单复购；P 池候选 △（成单 ✔ 复购 ✔；区域外 + 终端自用 → 观察档）；部分坐实（域名法人未直接命中）；Simon 曾判不行。')
# ---------------- 巴拉圭 ----------------
row('SC-2368', 'other', 'Asociación Civil Radio ZP-30 「La Voz del Chaco Paraguayo」（zp30.com.py；**官网 + radiosdeparaguay + Facebook：Calle Trébol 137E, Filadelfia 160401, Fernheim, Boquerón；+595 491 432 330；avisos@zp30.com.py；基督教广播电台（AM 610），分台 Loma Plata / Yalve Sanga**）；表内：HDMI + USB over SM fiber 光端机「多次下单」；wernerh@ 具名', 'PY',
    'PY · 1 次检索：zp30.com.py 页脚 + radiosdeparaguay.com.py（法人形式 Asociación Civil）+ facebook；RUC 未取；2026-10-29', 'https://radiosdeparaguay.com.py/la-voz-del-chaco/',
    '未取（RUC 未查）', '营业中（官网 2025）', '未取', 'Asociación Civil（非营利）', '广播电台（终端自用）', 'Calle Trébol 137E, Filadelfia, Boquerón', '微型',
    ['Werner H.（wernerh@zp30.com.py 表内具名 = 复购下单人）'],
    '**复购终端（光端机 = 本职线）→ Q-70 dayjob 子池；Saga 线只在其问交换机时报 STC-028GP / STC-110XGE**',
    '成单复购；P 池候选 △ + dayjob_fit（复购 ✔ 具名 ✔；终端 + 区域外 + 本职线产品 → 观察档，待 Q-70）；部分坐实（RUC 未取）。')
# ---------------- 沙特 ----------------
row('SC-257', 'other', 'Al Rajhi Telecom（alrajhitel.com；**LinkedIn：Al Rajhi Building & Construction 子公司；利雅得；2013 年创立；系统集成（弱电 / CCTV / 门禁 / 数据中心 / Cisco Premium Partner / 网络安全）；LinkedIn 规模 501–1,000 vs prospeo 51–100 + 营收估 $7.96M；7687 King Fahad Branch Rd, Al Murabba, Riyadh 12612；+966 11 422 1089；2025 Intersec Saudi 参展**；CR 号未取）；表内：2024-10-22 DC Division Manager（inam@）回群发索样 STI-154GP（答 $36 非免费）', 'SA',
    'SA · 1 次检索：linkedin.com/company/alrajhitel（母公司 / 2013 / 专长）+ x.com/alrajhitel + prospeo（地址 / 电话 / 规模）；CR 未取；2026-10-29', 'https://www.linkedin.com/company/alrajhitel/',
    '未取（CR 未查）', '营业中（LinkedIn 2025 更新）', '2013', 'LLC（集团子公司）', '系统集成 / 弱电 / 数据中心（利雅得）', '7687 King Fahad Branch Rd, Al Murabba, Riyadh 12612', '中型（51–100 ～ 501–1,000）',
    ['Inam（inam@alrajhitel.com 表内 = DC Division Manager，真回索样）'],
    '**DC 集成商回访 → 集成 25%：点名 Inam 一页纸一次（STI-154GP 样机 $36 + STC-4424GCPM / STH-2C24XF-HSI DC 接入 + 付费样机 + T/T 50/50）' + OT + '**；次优区',
    '集成 25%；P 池候选 ○（具名 KP 真回 ✔ 样品意向 ✔ 对位 ✔ 体量 ✔）；部分坐实（CR 未取）。')
# ---------------- 泰国 ----------------
row('SC-1045', 'other', 'บริษัท อัลฟา เบส มาร์เก็ตติ้ง จำกัด — Alfa Base Marketing Co., Ltd.（alfabase.co.th；**官网：582/5 ถนนลาดกระบัง, Lat Krabang, Bangkok 10520；1995（พ.ศ. 2538）注册；进口 + 制造 + 咨询；自有品牌 ALFA BASE（UTP / 光纤跳线 / 配线架 / ODF / MC / SFP / MPO / 机架 / 电源 / 蓄电池），面向政府与电信**）；表内：自有品牌 + 同时卖 ONV / Elink；16 推 0 回', 'TH',
    'TH · 1 次检索：alfabase.co.th 首页 + /shop/ + /product-category/products/alfa-base/（法人泰文名 / 地址 / 1995 / 自有品牌型号）；DBD 注册号未取；2026-10-29', 'https://alfabase.co.th/product-category/products/alfa-base/',
    '未取（DBD 未查；法人泰文名坐实）', '营业中（官网 2026 版权）', '1995', 'Co., Ltd.', '自有品牌布线 / 光通信产品 + 进口分销（曼谷）', '582/5 Lat Krabang Rd, Lat Krabang, Bangkok 10520', '小型 / 中型（20+ 年）',
    ['（info@alfabase.co.th 表内总邮箱；产品经理 KP 待 LinkedIn）'],
    '**自有品牌布线商补网络线 → OEM 30%：一页纸一次（STC-028GP / STC-228GP 丝印 + STC-110XGE MC 对标其 MC 线 + MOQ + 付费样机）' + OT + '**；次优区',
    'OEM 30%；P 池候选 ○（自有品牌 ✔ 进口 ✔ 对位 ✔ 坐实 ✔；冷）；部分坐实（DBD 未取）。')
row('SC-2437', 'other', 'Nana-tech（nana-tech.net；**1 查仅返回 Nana Engineering Technology Co., Ltd.（水泵；nanaengineering.com）与 thai.finance 同名合伙企业 NANA TECH LIMITED PARTNERSHIP 0133547002680（Pathum Thani）—— 域名均未对上 → 未坐实**）；表内：工业网络分销，大量 Utepo；pimpisa@ 具名；8 推 0 回；Simon 判不行', 'TH',
    'TH · 1 次检索：nanaengineering.com/about（他司）+ thai.finance/az-companies/nana-t（同名合伙，未证明为本域名）；2026-10-29', 'http://thai.finance/az-companies/nana-t',
    '未取（0133547002680 为同名合伙，未证实）', '未坐实', '未取', '未取', '工业网络分销（推定）', '未取', '未取',
    ['Pimpisa（pimpisa@nana-tech.net 表内具名；职务未取）'],
    '**未坐实 → 不动；来信再起则预付 100%**',
    '回 C 储备（1 查未命中 + 冷户 + Simon 判不行）。')
# ---------------- 澳大利亚 ----------------
row('SC-2106', 'au', 'Optimal Cable Services Pty Ltd → AFL（optimal.com.au；**Crunchbase：澳大利亚光缆 / 连接产品制造商，11–50 人，已被 AFL（藤仓集团）收购；bluebusinessguide：100 Olympia St, Tottenham VIC；03 9316 8300；ZoomInfo：Peter Dicka = Manager, Connectivity AFL (Australia)（= 表内 peter_dicka@optimal.com.au）**）；表内：2007 年起合作、买过 MC / CWDM、「偶尔有反应」、23 次跟进；marketing@aflglobal.com 亦在表', 'AU',
    'AU · 1 次检索：crunchbase（被 AFL 收购；11–50）+ bluebusinessguide（地址 / 电话）+ zoominfo（Peter Dicka 现职）；ABN 未取；2026-10-29', 'https://www.crunchbase.com/organization/optimal-cable-services',
    '未取（ABN 未查）', '营业中（AFL 旗下）', '未取', 'Pty Ltd（AFL 子公司）', '光缆 / 连接产品制造（墨尔本）', '100 Olympia St, Tottenham VIC 3012', '小型（11–50；集团 AFL）',
    ['Peter Dicka — Manager, Connectivity AFL (Australia)（peter_dicka@optimal.com.au 表内 = 老 KP 仍在职）'],
    '**长期成单户（MC / CWDM = 本职线为主）→ Q-70 dayjob 子池；Saga 线只提 STC-110XGE MC + STI 工业 PoE；AFL 集团采购体系 → 长线**',
    '成单回访；P 池候选 △ + dayjob_fit（长期成单 ✔ KP 在职 ✔；产品偏光传输 + 巨头体系 → 观察档）；部分坐实（ABN 未取）。')
# ---------------- 韩国 ----------------
row('SC-296', 'kr', 'lsipro（**hanmail 户 lsipro@hanmail.net；无域名 / 法人 → 0 查**）；表内：3G / HD-SDI 光端机「多次下单」= 复购户（本职线产品）', 'KR',
    'KR · 0 查（hanmail 个体，无可查主体）；2026-10-29', '',
    '未取（无主体）', '未坐实', '未取', '未取', '未取（光端机复购）', '未取', '未取',
    ['（lsipro@hanmail.net 表内）'],
    '**无法人 + 本职线产品 → 不动；Q-70 定 dayjob 子池后复议**',
    '回 C 储备 + dayjob_fit（复购但 hanmail 0 查未坐实；待 Q-70）。')

print('b127_c rows written: 34')
