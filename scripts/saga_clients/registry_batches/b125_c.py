# -*- coding: utf-8 -*-
"""第 125 批（T29-U118b，2026-10-29）—— **C 池三闸 · 闸 2 第二批**：闸 1 候选中的欧洲（非四主区）20 户查底数。
路径：ES einforma / empresia / iberinform / infoempresa（CIF 1 查即得：Casmar A08551061 / Bunker B62851712 / Visiotech B80645518 官网页脚 / JEVASO B15299548）；BE staatsbladmonitor / kompass（Bausch 0437.286.193）；
HU cegadatok（Agenda-Age）；NO gulesider（Eldi 924312963）；LV 官网自列（SPX SIA 40003637852）；FI 官网 Y-tunnus（Starelec 0549989-1）；CZ rejstrik.penize / finance.cz（Discomp 25236792）；
PT 官网条款页 NIF（Neurónio Digital 517867990）；LT spec.lt / okredo（Somi 300528292）；DK 官网 CVR（ITV-Security 38937456）；SK foaf.sk / ifirmy（TSS Group 36323551）；IT aziende.it / reportaziende（Comelit 01546400167）；HR Fina infobiz（H1 Telekom OIB 88551335012，**已注销**）。
1 查未得：Cygnus（CY，仅返回同名无关公司）→ 未坐实；A-SECUR（Leistung S.L.U.，CIF 未取）/ TBK Vision（西班牙法人未取，域名关联法国 TBK SOLUTION）→ 部分坐实。红旗：Bunker Seguridad **Concursal（破产程序）**。每户 1 查、depth 1。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 125
F = '2026-10-29'
EU = '— 欧洲常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 预付 100%）+ DAP（买方清关）或 FOB 深圳；周四 12–14 当地'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 西班牙 ----------------
row('SC-1014', 'es', 'GOTE, S.A.（品牌 GTLAN；gtlan.com；**matmax 品牌页：1984 年创立、Parque Tecnológico Ronda Narciso Monturiol 13, 46980 Paterna (Valencia)；自有品牌 GTLAN 制造 + 分销数据网络 / 电信产品（线缆、配线、LAN/WAN 网络电子、无线、工业电话、仪表）；ContactOut +34 961 366 571**）；表内：工业 FS，GXcom + 宇航，有工业 10G 5 口产品页；曾退信但域名正常', 'ES',
    'ES · 1 次检索：matmax.es/marcas/gtlan（Razón social GOTE, S.A.；Paterna；1984；marca propia Gtlan）+ contactout（+34 961 366 571；linkedin.com/company/gtlan）；2026-10-29', 'https://www.matmax.es/marcas/gtlan',
    '未取（CIF 1 查未得；法人名已坐实）', '营业中（品牌页 2024 / 官网在线）', '1984', 'S.A.', '网络 / 电信产品自有品牌制造 + 分销（瓦伦西亚）', 'Pque. Tecn. Rda. Narciso Monturiol 13, 46980 Paterna (Valencia)', '中小型（推定）',
    ['（comercial@gtlan.com 表内 = 收件人；具名 KP 未取，LinkedIn 公司页可挖）'],
    '**自有品牌 GTLAN 已在卖宇航 / GXcom 工业交换机 → OEM 30%：一页纸一次（STI-154GP 工业 4 PoE+1 GE+1 SFP / STI-288GPM 对标 + 丝印 / 彩盒 MOQ + 付费样机；10G 工业款不供明说）' + EU + '**',
    'OEM 30%；P 池候选 ★（自有品牌 + 已进口中国工业线）；坐实（法人名 + 地址）。')
row('SC-1053', 'es', 'CASMAR ELECTRONICA SA（casmarglobal.com；**einforma / empresia：CIF A08551061；Calle Maresme 71-79, 08019 Barcelona；1979-02-02 成立；社会资本 300,010 €；2024 年 82 名员工；CNAE 8020 安防系统服务；对象「安防报警系统的商业化与制造」；审计 AOB Global；casmar@casmar.es 公开**）；表内：国际化安防分销集团、无邮箱、从未触达', 'ES',
    'ES · 1 次检索：iberinform（A08551061；Maresme 71-79；1979）+ empresia（82 empleados 2024；capital 300.010 €；casmar@casmar.es；933406408）+ einforma；2026-10-29', 'https://www.empresia.es/empresa/casmar-electronica/',
    'A08551061', 'ACTIVA（Registro Mercantil de Barcelona）', '1979-02-02', 'S.A.', '安防系统分销 / 制造（巴塞罗那；国际化）', 'Calle Maresme 71-79, 08019 Barcelona', '中型（82）',
    ['（casmar@casmar.es 官网 / 名录公开总邮箱 = 首发收件人；Administrador único 姓名未取；具名采购 KP 待 LinkedIn）'],
    '**分销 20%：首次触达一页纸（安防 PoE 线 STC-028GP $28 / STC-228GP $33 + 工业 STI-154GP；MOQ 1 + 付费样机）' + EU + '**；冷户 → 回声后再深挖',
    '分销 20%；P 池候选 ○（冷户：对位 ✔ 欧洲 ✔ 坐实 ✔ 体量 ✔ = §5 四条）；坐实。')
row('SC-1173', 'es', 'JEVASO S.L.（表内「DPTO. ELECTRONICA」；alberto@abbolli.com；**einforma：NIF B15299548；Pg. Ind. Sabón, Av. del Embalse Pa 87-B, 15142 Arteixo (A Coruña)；1991-01-11 成立；CNAE 1421 外衣成衣制造 / 纺织包装物流 / 电商**→ 纺织企业的电子部门；abbolli.com 为另一域名，关系未取）；表内：成单户（「是个技术」）', 'ES',
    'ES · 1 次检索：einforma（JEVASO SL B15299548；Arteixo；1991；CNAE 1421）+ ardan（jevaso.com；jevaso@jevaso.com）+ poligonosabon（981 676 717）；abbolli.com 未查；2026-10-29', 'https://www.einforma.com/informacion-empresa/jevaso',
    'B15299548', '营业中', '1991-01-11', 'S.L.', '纺织成衣 / 物流（电子部门为内部自用）', 'Pg. Ind. Sabón, Av. del Embalse Pa 87-B, 15142 Arteixo (A Coruña)', '中型（推定）',
    ['Alberto（alberto@abbolli.com；表内「是个技术」= 成单对接人；职务未取）'],
    '**成单回访（终端自用 25%）：按原单回访一次（复购 + 同款升级 STI 工业线；MOQ 1）' + EU + '**；体量小不主动加码',
    '终端自用 25%；P 池候选 △（成单 ✔ 欧洲 ✔ 对位 ✔ 但复购体量低 → Simon 定）；坐实（法人）；abbolli.com 关系待核。')
row('SC-1556', 'es', 'BUNKER SEGURIDAD ELECTRONICA SL（bunkerseguridad.es；**infoempresa：CIF B62851712；C/ Franklin 10, Pol. Ind. Gitesa, 28814 Daganzo de Arriba (Madrid)；2002-04-11 成立；CNAE 4652 电子 / 电信设备批发；10–49 人、营收 <2M €；最近 BORME 2024-11-20；法律状态 Concursal（破产程序）；Iberinform 标 Inactiva**）；表内：安防分销 / 项目型，官网 Data transmission 栏有工业交换机；曾退信', 'ES',
    'ES · 1 次检索：infoempresa（B62851712；Concursal；BORME 2024-11-20）+ iberinform（Inactiva）+ 官网隐私页（am2@bunkerseguridad.es；913316313）；2026-10-29', 'https://www.infoempresa.com/es-es/es/empresa/bunker-seguridad-electronica-sl',
    'B62851712', '**Concursal（破产程序）/ Iberinform 标 Inactiva**', '2002-04-11', 'S.L.', '周界安防 / 安防设备批发（马德里）', 'C/ Franklin 10, Pol. Ind. Gitesa, 28814 Daganzo de Arriba (Madrid)', '小型（10–49）',
    ['（am2@bunkerseguridad.es 官网隐私页公开邮箱；info@ 表内曾退信）'],
    '**红旗：破产程序中 → 不动；回 C 储备（每 2 月巡检 BORME，若重整完成再议）**',
    '不动；回 C；坐实（红旗 Concursal）。')
row('SC-2452', 'es', 'Leistung S.L.U.（分销品牌 A-SECUR；a-secur.com；**Crunchbase：A-SECUR 为 Leistung S.L.U. 的分销品牌，面向专业安装商的电子安防批发（CCTV / 入侵 / 门禁 / 布线；Dahua 兼容 + 自有线 Movok AI 视频产品）；11–50 人；paxinasgalegas：Anel da Lagoa 18, Pol. Ind. Veigadaña, 36415 Mos (Pontevedra)；986 169 242；info@a-secur.es；join.com：15 年以上、由安装商转型分销**）；CIF 1 查未得 → 部分坐实；表内：ONV / Utepo 页面；15 推 0 回；Simon 曾判不行', 'ES',
    'ES · 1 次检索：crunchbase（Leistung S.L.U.；Movok；11-50）+ paxinasgalegas（Mos 地址 / 电话）+ join.com；2026-10-29', 'https://www.crunchbase.com/organization/a-secur',
    '未取（CIF 1 查未得；法人名 Leistung S.L.U.）', '营业中（招聘 / 官网在线）', '未取（>15 年）', 'S.L.U.', '电子安防批发（加利西亚 Mos；自有线 Movok）', 'Anel da Lagoa 18, Pol. Ind. Veigadaña, 36415 Mos (Pontevedra)', '小型（11–50）',
    ['javperez@a-secur.es（表内具名；职务未取）', '（info@a-secur.es 官网公开总邮箱）'],
    '**贴牌渠道（自有线 Movok）→ OEM 30% / 分销 20% 双轨：一页纸一次（STC-028GP $28 / STC-228GP $33 + 丝印 MOQ；Utepo / ONV 不点名）' + EU + '**；Simon 可否决',
    '分销 20% / OEM 30%；P 池候选 ○（进口经验 ✔ 自有线 ✔ 欧洲 ✔ 对位 ✔）；部分坐实；Simon 曾判不行。')
row('SC-371', 'es', 'VISIOTECH SECURITY S.L.（visiotechsecurity.com；**官网页脚：CIF B80645518；Calle Alberto Sánchez 31, 28052 Madrid；+ 葡萄牙分部；自称「leading supplier of technological equipment in Europe」；自有品牌 Safire / X-Security / Nivian（+ 分销 Ajax / Uniview / Ruijie-Reyee / ZKTeco / IMOU / Akuvox）**）；表内：成单记录 + OEM 交换机合作邮件、31 次跟进；产品中见中科德能', 'ES',
    'ES · 1 次检索：visiotechsecurity.com/en/（CIF B80645518；Calle Alberto Sánchez 31, 28052 Madrid；品牌 Safire / X-Security / Nivian；Portugal 分部）；2026-10-29', 'https://www.visiotechsecurity.com/en/',
    'B80645518', '营业中（官网 2026）', '未取', 'S.L.', '安防 / 网络技术设备大型分销 + 自有品牌（马德里；欧洲多国）', 'Calle Alberto Sánchez 31, 28052 Madrid', '大型（欧洲多国分销）',
    ['emussons@visiotechsecurity.com（表内具名 = OEM 合作对接；职务未取）', '（comercial@visiotechsecurity.com 表内总邮箱）'],
    '**成单 + 曾谈 OEM 交换机 → OEM 30% 主线：按 Safire / X-Security 口型复盘（STC-028GP / STC-228GP / STC-2224GP 24 PoE + 2 SFP 丝印彩盒 MOQ + STI 工业线；付费样机）一页纸 + 旧线索点名回访' + EU + '**',
    'OEM 30%；P 池候选 ★★（成单 + 自有品牌 + 大分销 + 具名 KP）；坐实。')
row('SC-427', 'es', 'TBK Vision（tbkvision.com；**1 查：品牌真实（manualslib TBK NEO 4/8/16 DVR 手册 → tbkvision.com）；verif.com 显示法国 TBK SOLUTION（SIREN 750660060；23 Che du Chanay, 69720 Saint-Bonnet-de-Mure；2012；资本 5,000 €；15 人）以 tbkvision.com 为官网；西班牙法人 1 查未得 → 部分坐实（法人国别待核）**）；表内：安防品牌商，Utepo 工业交换机 + 自有型号；退信但域名正常；14 次跟进', 'ES',
    'ES · 1 次检索：verif.com（TBK SOLUTION FR 750660060；site tbkvision.com）+ manualslib（TBK NEO DVR）；西班牙登记无命中；2026-10-29', 'https://www.verif.com/en/company/TBK-SOLUTION-68d9c05a1299230338d95049/',
    '未取（法国 TBK SOLUTION SIREN 750660060 关联；西班牙法人未得）', '营网中（品牌页在线）', '未取（法国关联公司 2012）', '未取', '安防自有品牌（DVR / 摄像机 / 交换机贴牌）', '未取（西班牙；法国关联 Saint-Bonnet-de-Mure）', '小型（关联公司 15 人）',
    ['（info@tbkvision.com 表内曾退信；具名 KP 未取）'],
    '**自有品牌 → OEM 30%：先核法人国别 + 找新 KP（LinkedIn「TBK Vision」），再一页纸（STI-154GP 工业 / STC-228GP + 丝印 MOQ；Utepo 不点名）' + EU + '**',
    'OEM 30%；P 池候选 △（自有品牌 ✔ 进口 Utepo ✔ 欧洲 ✔，但法人未坐实 → 预付 100%）；部分坐实。')
# ---------------- 比利时 / 匈牙利 / 挪威 / 拉脱维亚 / 芬兰 / 丹麦 / 克罗地亚（other）----------------
row('SC-1033', 'other', 'BAUSCH DATACOM NV（bausch.be；**staatsbladmonitor：ondernemingsnummer 0437.286.193；Tiensesteenweg 56, 3360 Bierbeek（Korbeek-Lo）；1997-01-17 成立（Kompass 1989）；NV；状态 Actief / Normale toestand；最近年报 2024 年度（2025-07-14 递交）；NACE 46520 电子 / 电信设备批发**）；表内：网络产品分销（二层光纤交换机、SFP）、冷户（未推送过）；dominiek@bausch.be 具名', 'BE',
    'BE · 1 次检索：staatsbladmonitor（BE0437286193；Actief；jaarrekening 2024）+ kompass（Tiensesteenweg 56；1989；46520）+ trendstop（旧 0436.762.393 Leuven 分支）；2026-10-29', 'https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0437286193',
    '0437.286.193', 'Actief（年报 2024 已递）', '1997-01-17', 'NV', '电子 / 电信设备批发（46520）', 'Tiensesteenweg 56, 3360 Bierbeek', '中小型（推定）',
    ['Dominiek（dominiek@bausch.be 表内具名；职务未取）'],
    '**分销 20%：首次触达一页纸（STC-228GP $33 / STC-2224GP $86 二层光口 + MOQ 1 + 付费样机）' + EU + '**；冷户 → 回声后再深挖',
    '分销 20%；P 池候选 ○（冷户：对位 ✔ 欧洲 ✔ 坐实 ✔ 体量 ✔ = §5 四条）；坐实。')
row('SC-1181', 'other', 'AGENDA-AGE Kft.（agendaage.hu；**cegadatok：2002-05-09 成立；1095 Budapest, Soroksári út 48. 8.ép.fsz；主业 IT / 通信产品批发；最近年营收 >514M HUF；状态 aktív；ugyvezeto@agendaage.hu（总经理邮箱）公开；ZoomInfo 20–49 人、营收 1–5M；官网自述「网络 IT 批发，仅服务法人 / 签约经销商 / 安装商」**）；表内：SFP / MC / 工业 FS，在用深圳 credfiber；15 次跟进无回复', 'HU',
    'HU · 1 次检索：cegadatok.hu/agenda-age-kft（2002；514M HUF；ugyvezeto@）+ agendaage.hu 首页（B2B only；+36 1 313 1073）+ zoominfo（20–49）；2026-10-29', 'https://cegadatok.hu/agenda-age-kft/',
    '未取（cegjegyzékszám 页内未列）', 'aktív', '2002-05-09', 'Kft.', 'IT / 通信产品批发（布达佩斯；B2B 光纤 + 铜缆方案）', '1095 Budapest, Soroksári út 48. 8. ép. fsz.', '小型（20–49；>514M HUF）',
    ['（ugyvezeto@agendaage.hu = 总经理邮箱，名录公开 → 首发收件人）', '（info@agendaage.hu 表内）'],
    '**进口商 / 分销 20%：换 ugyvezeto@ 一页纸一次（STI-154GP / STC-228GP 对标 credfiber 同类 + MOQ 1 + 付费样机）' + EU + '**',
    '分销 20%；P 池候选 ○（进口经验 ✔ 欧洲 ✔ 坐实 ✔ 对位 ✔）；坐实。')
row('SC-1194', 'other', 'ELDI AS（eldi.no；**gulesider：org.nr 924312963；2019-12-24 登记；股本 NOK 30,300；NACE 46.640 机械设备批发；Daglig leder Tony Volden Uthuslien（= 表内 tony@eldi.no）；董事长 Dag Petter Evensen；derdubor：Täby vei 15, 1474 Lørenskog；「楼宇自动化材料批发（HDL 系统）」**）；表内：宇航的工业 FS / SFP，产品较少；15 次跟进无回复', 'NO',
    'NO · 1 次检索：gulesider.no（924312963；2019；30 300；Tony Volden Uthuslien）+ derdubor.no（Täby vei 15 Lørenskog；grossist byggautomasjon）；2026-10-29', 'https://www.gulesider.no/eldi+as+oslo/155035623/bedrift',
    '924312963', '营业中（MVA 登记）', '2019-12-24', 'AS', '楼宇自动化材料批发（HDL；网络为副线）', 'Täby vei 15, 1474 Lørenskog', '微型 / 小型（2019 新司，股本 NOK 30,300）',
    ['Tony Volden Uthuslien — Daglig leder（tony@eldi.no 表内 = 决策人直达）'],
    '**分销 20%：点名 Tony 一页纸一次（STI-154GP / STI-280GE 工业线对标宇航 + MOQ 1 + 付费样机）' + EU + '**；新司小股本 → 预付 100%',
    '分销 20%；P 池候选 ○（决策人邮箱在表 + 进口经验 + 坐实；体量小 → 预付）；坐实。')
row('SC-1215', 'other', 'SPX SIA（router.lv；**官网 About us：MikroTik 官方分销（里加 + 维尔纽斯仓）；Reg. No. 40003637852 / VAT LV40003637852；15 Krustpils street, Riga LV-1073；+371 67724000；sales@router.lv**）；表内：switch 等，有少量 Utepo；15 次跟进无回复', 'LV',
    'LV · 1 次检索：router.lv/eng/15/（SPX SIA；40003637852；Krustpils 15；MikroTik Distributor）+ facebook（官方 MikroTik 分销）；2026-10-29', 'https://www.router.lv/eng/15/',
    '40003637852', '营业中（官网 / 网店在线）', '未取', 'SIA', 'MikroTik 官方分销 + 网络设备网店（拉脱维亚 / 立陶宛）', '15 Krustpils street, Riga LV-1073', '小型（推定）',
    ['（sales@router.lv 官网公开 / router@router.lv 表内；具名 KP 未取）'],
    '**MikroTik 分销 → 分销 20%：一页纸一次（MikroTik 无 PoE 工业款补位：STI-154GP / STC-228GP + MOQ 1 + 付费样机）' + EU + '**',
    '分销 20%；P 池候选 ○（MikroTik 分销 = 对位渠道；进口 Utepo ✔；坐实）；坐实。')
row('SC-1220', 'other', 'Starelec Oy（starelec.fi；**官网 Yritys 页：Y-tunnus 0549989-1；Kiillekuja 3, FI-65300 Vaasa；1984-06-14 成立；家族企业，电子元件 / 仪表 / 焊接工具分销 + 全国网店；状态 Aktiivinen**）；表内：Networking 类有 ONV 的 switch；sampo.aallos@ 具名；15 次跟进无回复', 'FI',
    'FI · 1 次检索：starelec.fi/sivu/yritys（0549989-1；1984；Vaasa）+ yritystele（Aktiivinen）；2026-10-29', 'https://starelec.fi/sivu/yritys',
    '0549989-1', 'Aktiivinen', '1984-06-14', 'Oy', '电子元件 / 仪表分销（网络设备为副线）', 'Kiillekuja 3, FI-65300 Vaasa', '小型（推定）',
    ['Sampo Aallos（sampo.aallos@starelec.fi 表内具名；职务未取）', '（myynti@ / shop@starelec.fi 公开销售邮箱）'],
    '**分销 20%：点名 Sampo 一页纸一次（STC-028GP $28 / STC-228GP $33 对标 ONV + MOQ 1）' + EU + '**；网络为副线不加码',
    '分销 20%；P 池候选 △（进口 ONV ✔ 欧洲 ✔ 坐实 ✔ 对位 ✔，但网络为副线、体量小 → Simon 定）；坐实。')
row('SC-1706', 'other', 'ITV-Security ApS（itvsecurity.dk / .com；**官网页脚：CVR 38937456；Æblehaven 7, 8930 Randers NØ；电话 35115000；kontakt@itvsecurity.dk；品牌页 Vivotek / Avico / Milestone**）；表内：产品线 Vivotek + 深圳 acorid 牌；15 次跟进无回复', 'DK',
    'DK · 1 次检索：itvsecurity.dk 商品 / 品牌页页脚（ITV-Security ApS；CVR 38937456；Randers NØ）；2026-10-29', 'https://itvsecurity.dk/shop/8-vms-software-amp-apps/',
    'CVR 38937456', '营业中（网店在线）', '未取（CVR 389… ≈ 2017）', 'ApS', '安防 / 视频监控网店 + 分销（丹麦）', 'Æblehaven 7, 8930 Randers NØ', '微型 / 小型（推定）',
    ['（kontakt@itvsecurity.dk 表内 = 公开总邮箱；具名 KP 未取）'],
    '**分销 20%：一页纸一次（安防 PoE：STC-028GP / STC-228GP + MOQ 1 + 付费样机；acorid 不点名）' + EU + '**',
    '分销 20%；P 池候选 △（进口中国品牌 ✔ 欧洲 ✔ 坐实 ✔ 对位 ✔；体量小）；坐实。')
row('SC-667', 'other', 'H1 TELEKOM d.d.（h1telekom.hr；**Fina infobiz：OIB 88551335012；MB 01834649；Dračevac 2/d, 21000 Split；2004 年成立；曾为克罗地亚领先替代固网运营商（13 万线）；状态 Neaktivan / izbrisan（已注销 / 删除，推定并购吸收）**）；表内：成样品单（SFP / 收发器）、「常回复」、17 次跟进；silvana.pavic@ / branka.trogrlic@ 具名', 'HR',
    'HR · 1 次检索：infobiz.fina.hr（OIB 88551335012；Status Neaktivan/izbrisan）+ fininfo（Brisan；2004）+ novac.net（旧简介：13 万线、MBS 060145425、股本 23.76M kn）；2026-10-29', 'https://infobiz.fina.hr/tvrtka/h1-telekom-d-d/OIB-88551335012',
    'OIB 88551335012 / MB 01834649', '**已注销（Neaktivan / izbrisan）**', '2004', 'd.d.（已注销）', '固网运营商（已并入他方，推定）', 'Dračevac 2/d, 21000 Split（原）', '—（法人已注销）',
    ['Silvana Pavić（silvana.pavic@h1telekom.hr 表内「常回复」；去向待核）', 'Branka Trogrlić（branka.trogrlic@h1telekom.hr 表内）'],
    '**法人已注销 → 不动；回 C（KP 去向 LinkedIn 待核，若在承继运营商任职再议；品类偏光模块 = 本职线）**',
    '不动；回 C；坐实（已注销）。')
# ---------------- 捷克 / 葡萄牙 / 立陶宛 / 斯洛伐克 / 塞浦路斯 / 意大利 ----------------
row('SC-1335', 'cz', 'DISCOMP s.r.o.（discomp.cz；**rejstrik.penize / finance.cz：IČO 25236792；Cvokařská 1216/8, Lobzy, 312 00 Plzeň；1999-09-21 登记（Krajský soud v Plzni C 11558）；RES 50–99 名员工；2014 吸收合并 DISCOMP HOLDING；LinkedIn 公司页**）；表内：光纤设备 / CWDM / SFP，有部分 Planet 的；dan.pacanda@ / milan.harmacek@ 具名；冷户', 'CZ',
    'CZ · 1 次检索：rejstrik.penize.cz/25236792（Cvokařská 1216/8；1999；fúze 2014）+ finance.cz（50–99 zaměstnanců）+ firmy.euro.cz（C 11558）；2026-10-29', 'https://rejstrik.penize.cz/25236792-discomp-s-r-o',
    'IČO 25236792', '营业中（年检 2026-10）', '1999-09-21', 's.r.o.', '网络 / 光纤设备分销（Planet 渠道；皮尔森）', 'Cvokařská 1216/8, Lobzy, 312 00 Plzeň', '中型（50–99）',
    ['Dan Pacanda（dan.pacanda@discomp.cz 表内具名；职务未取）', 'Milan Harmáček（milan.harmacek@discomp.cz 表内具名；职务未取）'],
    '**Planet 渠道分销 → 分销 20%：点名 Dan 一页纸一次（STC-2224GP $86 / STI-288GPM $78.9 对标 Planet 同口型 + MOQ 1 + 付费样机）' + EU + '**；与 Planet 仓并线核对',
    '分销 20%；P 池候选 ★（中型分销 + Planet 渠道 + 具名 KP；冷户 §5 四条齐）；坐实；dayjob 线索 CWDM。')
row('SC-1446', 'pt', 'Neurónio Digital, Unipessoal Lda.（lojaCCTV；lojacctv.com；**官网条款页：NIF PT517867990；Av. Augusto Hilário Nr.5 Loja C, 2620-528 Ramada；geral@lojacctv.com；ensun：1–10 人、CCTV 批发（Hikvision / Uniview 套装）**）；表内：卖多种外壳 PoE 的安防网店 / 分销，回过 1 次、16 次跟进；fabio@ 具名', 'PT',
    'PT · 1 次检索：lojacctv.com/page/termos-e-condicoes（Neurónio Digital, Unipessoal Lda.；NIF 517867990；Ramada）+ ensun（1–10）；2026-10-29', 'https://www.lojacctv.com/page/termos-e-condicoes',
    'NIF 517867990', '营业中（网店在线）', '未取', 'Unipessoal Lda.（一人公司）', '安防 / CCTV 网店 + 批发（里斯本北郊）', 'Av. Augusto Hilário Nr.5 Loja C, 2620-528 Ramada', '微型（1–10）',
    ['Fábio（fabio@lojacctv.com 表内具名 = 回信人推定）'],
    '**分销 20%：点名 Fábio 续上回信一页纸（STC-028GP $28 / STC-228GP $33 + MOQ 1；一人公司 → 预付 100%）' + EU + '**',
    '分销 20%；P 池候选 △（回信 ✔ 欧洲 ✔ 坐实 ✔ 对位 ✔；微型一人公司 → 预付）；坐实。')
row('SC-1629', 'lt', 'UAB SOMI NETWORKS（sominetworks.com；**官网 Contacts + spec.lt / okredo：Company Code 300528292；VAT LT100002144113；Ukmergės g. 283A, LT-06313 Vilnius（仓 Raciu str. 6A）；2006-01-19 成立；8 名员工（2024-12）；Sodra 欠费 0；拉脱维亚子公司 SIA SOMI NETWORKS 40003830305**）；表内：MC / SFP / 工业 FS / VC / 机架，宇航的设备，「中性、来自不同国内供应商、价格 OK」；vytas.norkus@ 具名；15 次跟进无回复；SC-2767 SOMI RT 疑似同源', 'LT',
    'LT · 1 次检索：sominetworks.com/contacts（300528292；LT100002144113；Ukmergės 283A）+ spec.lt（2006；8 darbuotojai）+ okredo（Active）；2026-10-29', 'https://sominetworks.com/contacts/',
    '300528292', 'Active', '2006-01-19', 'UAB（+ SIA 拉脱维亚）', '网络 / 光纤中性产品进口分销（波罗的海）', 'Ukmergės g. 283A, LT-06313 Vilnius', '小型（8）',
    ['Vytas Norkus（vytas.norkus@sominetworks.lt 表内具名；职务未取）', '（info@sominetworks.com 官网公开）'],
    '**中性进口商 → 分销 20%：点名 Vytas 一页纸一次（STI-154GP / STI-288GPM 工业 + STC-228GP 对标宇航 + MOQ 1 + 付费样机）' + EU + '**；并线核对 SC-2767',
    '分销 20%；P 池候选 ○（进口中国中性产品 ✔ 欧洲 ✔ 坐实 ✔ 对位 ✔）；坐实；dayjob 线索 MC / SFP。')
row('SC-1881', 'sk', 'TSS Group a. s.（tssgroup.sk；**foaf.sk / ifirmy / pracuj：IČO 36323551；DIČ 2020116505；Továrenská 4201/50, 018 41 Dubnica nad Váhom；2002-04-24 成立（Okresný súd Trenčín Sa/10609/R）；102–150 名员工；分销 + 开发 + 制造，进口销售安防系统（Dahua / Avigilon / Sony 摄像机、车辆 GPS 监控），覆盖斯洛伐克 / 捷克 / 欧洲**）；表内：自称斯洛伐克第二大 CCTV 批发商，对 IP / analog over fiber 感兴趣；电话加不上，sokol@ / roxer@ 具名', 'SK',
    'SK · 1 次检索：foaf.sk/36323551（Sa/10609/R；2002；Továrenská 4201/50）+ ifirmy（102 人；Distribútor / Dovozca）+ pracuj.sk（≈150 人；Dahua / Avigilon / SONY 分销）；2026-10-29', 'https://www.foaf.sk/36323551',
    'IČO 36323551', '营业中（登记更新 2026-10-07）', '2002-04-24', 'a.s.', '安防系统进口分销 + 制造（Dahua / Avigilon；斯洛伐克 / 捷克）', 'Továrenská 4201/50, 018 41 Dubnica nad Váhom', '中型（102–150）',
    ['Sokol（sokol@tssgroup.sk 表内具名；职务未取）', 'Roxer（roxer@tssgroup.sk 表内具名；职务未取）'],
    '**大型安防分销 → 分销 20%：点名 sokol@ 一页纸一次（安防 PoE 线 STC-028GP / STC-228GP / STC-2224GP + 工业 STI-154GP；光纤回传：STI-154GP SFP 口 + MC STC-110XGE 不供百兆明说）' + EU + '**',
    '分销 20%；P 池候选 ★（中型进口分销 + 具名 KP + 对位）；坐实；dayjob 线索 analog over fiber。')
row('SC-2143', 'cy', 'Cygnus（cygnus.la；info@；**1 查「Cygnus cygnus.la Cyprus Limassol」仅返回 Cypronetwork / CyprusNet 等无关同名 → 未坐实**）；表内：SFP / 工商业 FS，主要是 Utepo 的；Simon 曾判不行、4 次无回复', 'CY',
    'CY · 1 次检索无命中（返回 Cypronetwork Consultancy / CyprusNet）；2026-10-29', '',
    '未取（1 查无命中）', '存续待核（域名 MX 正常）', '未取', '未取', '网络设备经销（塞浦路斯，推定）', '未取', '微型（推定）',
    ['（info@cygnus.la 表内；具名 KP 未取）'],
    '**未坐实 + Simon 判不行 + 4 推 0 回 → 不动，回 C 储备**' + EU, '不动；回 C；未坐实。')
row('SC-2219', 'it', 'COMELIT GROUP S.p.A.（comelitgroup.com；**aziende.it / reportaziende：P.IVA 01546400167；Via Don Basilide Arrigoni 5, 24020 Rovetta (BG)；1985-02-01 登记（CCIAA Bergamo）；2024 营收 €111.6M、净利 €10.3M；2025 营收 €112.5M；250–499 名员工；ATECO 27.9 其他电气设备制造；PEC amministrazione@pec.comelit.it**）；表内：对讲 / 安防集团，UniPoE 工业 FS + 商业 PoE 自有 logo；之前跟过西班牙分公司；Simon 曾判不行', 'IT',
    'IT · 1 次检索：aziende.it/comelit-group-s-p-a（01546400167；€111.6M 2024；250–499）+ reportaziende（€112.5M 2025）+ impresaitalia；2026-10-29', 'https://www.aziende.it/comelit-group-s-p-a',
    'P.IVA 01546400167', '营业中（2025 年报）', '1985-02-01', 'S.p.A.', '楼宇对讲 / 安防系统品牌制造商（自有品牌 PoE 交换机贴牌；贝加莫）', 'Via Don Basilide Arrigoni 5, 24020 Rovetta (BG)', '大型（250–499；€112M）',
    ['（info@comelit.it / info@comelit.es 表内总邮箱；采购 / 产品经理 KP 待 LinkedIn 挖掘）'],
    '**自有品牌 PoE 交换机（UniPoE）→ OEM 30%：找总部产品 / 采购 KP 后一页纸（STC-028GP / STC-228GP / STI-154GP 对标 UniPoE 口型 + 丝印彩盒 MOQ + 付费样机）' + EU + '**；Simon 可否决；巨头式采购流程 → 长线',
    'OEM 30%；P 池候选 ★（品牌商自有 PoE 线 = 目标顺位 1；体量大但非巨头）；坐实；Simon 曾判不行。')

print('b125_c rows written: 20')
