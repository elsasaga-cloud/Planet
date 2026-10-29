# -*- coding: utf-8 -*-
"""第 128 批（T29-U118d，2026-10-29）—— **C 池三闸 · 闸 2 第五批**：闸 1 第 09–11 批（桶 ⑤ 收尾）产出的候选 18 户查底数（GB 4 / DE 3 / CZ 4 / US 2 / PL / TR / BG / IT / BE 各 1）。
路径：BG papagal / yox（КСТ ООД ЕИК 831850563）；TR 官网 + elektrikport（GSL Mühendislik A.Ş. 1988 Ankara；MERSIS 未取）；DE Impressum 1 查即得（AMC HRB 995 Chemnitz；systerra HRB 32770 Wiesbaden；itjan.de = 个体 Dittmar Janetzky）；
IT registroaziende / 官网 privacy（SARC Italia P.IVA 03184880361 REA MO-365943）；CZ kurzy / finmag / firmy.cz / 官网 kontakt（100MEGA IČO 60707968；Express Alarm Czech IČ 26446863；Bluecom IČ 25955993；HTV Hodina = 个体 Michal Hodina IČ 48424986）；
BE 官网 Over ons（MegaMobile = M&C Technology BTW BE 0479.101.014）；PL krs-online / owg / 官网 regulamin（Elmark Automatyka S.A. KRS 0000803828 NIP 5252072585）；US rocketreach / leadiq / cbinsights（Baltic Networks Lisle IL 2005）+ crunchbase / 官网产品页（New Tech Industries, Inc. Davie FL，自有品牌工业 PoE 交换机 NT408-2P）；
GB companycheck（LEADER OPTEC LIMITED 03936485，董事 Paul Anthony Desmond = 表内邮箱）+ zoominfo / globaldatabase（Annicom Limited Bordon 24 人）+ 官网 About / LinkedIn（Mast Digital (UK) Ltd Epworth，Dahua Tier 1 + Wi-Tek 授权）+ 官网 About（Semaphore Systems Ltd London NW6，Advantech 1988 起）。
每户 1 查、depth 1；无 1 查未得；无国别纠偏。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 128
F = '2026-10-29'
EU = '— 欧洲常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 预付 100%）+ DAP（买方清关）或 FOB 深圳；周四 12–14 当地'
US = '— 北美常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 预付 100%）+ FOB 深圳 / DAP（买方清关）；周三 08–10 当地'
TR = '— 土耳其常规：英文稿、20 / 25 / 30 + T/T 50/50 + FOB 深圳 / DAP（买方清关）；周四 10–12 当地'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 保加利亚 ----------------
row('SC-575', 'bg', 'КСТ ООД — KST Ltd（kst-bg.com；**papagal / yox：ЕИК 831850563；1995 年登记（LinkedIn 称 1991/93 创立）；ООД；VAT BG831850563；бул. Сливница 357, 1336 София（Люлин）；17–18 人；2020 营业额 €3.26M；管理人 Светлин Димитров Капитанов（= 表内 skapitanov@）；CATV / SMATV / 通信布线分销，Motorola 保加利亚代表；ISO 9002**）；表内：国内的交换机；13 推 0 回', 'BG',
    'BG · 1 次检索：papagal.bg（ЕИК / 状态 / 营业额 / 管理人）+ yox.bg（18 人；地址）+ linkedin（定位 / 11–50）；2026-10-29', 'https://papagal.bg/eik/831850563/93d8',
    '831850563（ЕИК）', '营业中（Активен）', '1995', 'ООД', 'CATV / 通信布线 / 网络分销（索非亚）', 'бул. Сливница 357, 1336 София', '小型（17–18；€3.26M）',
    ['Светлин Димитров Капитанов — 管理人（skapitanov@kst-bg.com 表内 = 决策人直达）'],
    '**CATV 分销补网络线 → 分销 20%：点名 Svetlin 一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP + MOQ 1 + 付费样机）' + EU + '**',
    '分销 20%；P 池候选 ○（决策人邮箱在表 + 进口中国交换机 ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔）；坐实（ЕИК）。')
# ---------------- 土耳其 ----------------
row('SC-571', 'tr', 'GSL Mühendislik Sanayi ve Ticaret A.Ş.（gsl.com.tr；**官网 + elektrikport：1988 年安卡拉创立；Moxa / Robustel / Kyland / Digi / TXOne / RuggON / Transcend / Pro Optix 土耳其增值分销商；安卡拉 + 伊斯坦布尔两办公室（+90 312 473 3540 / +90 216 469 4191）；土耳其 IT 500 强；2016 TOBB 增长最快 100 强；store.gsl.com.tr 在线商店**）；表内：国内 Kyland + Moxa 工业 FS；umit@ 具名；11 推 0 回', 'TR',
    'TR · 1 次检索：gsl.com.tr 首页（法人 A.Ş. / 品牌 / 两地电话）+ store.gsl.com.tr + elektrikport 名录（1988 / 500 强）；MERSIS 未取；2026-10-29', 'https://gsl.com.tr/',
    '未取（MERSIS 未查；法人名坐实）', '营业中（官网 2026）', '1988', 'A.Ş.', '工业网络 / 自动化增值分销（安卡拉 + 伊斯坦布尔）', 'Ankara（总部）/ İstanbul', '中型（IT 500 强）',
    ['Ümit（umit@gsl.com.tr 表内具名；职务未取）', '（info@gsl.com.tr 表内）'],
    '**Kyland 现供分销 → 分销 20%：点名 Ümit 一页纸一次（STI-154GP / STI-288GPM / STI-0240GE 对标 Kyland 入门线 + MOQ 1 + 付费样机；Kyland / Moxa 不点名）' + TR + '**',
    '分销 20%；P 池候选 ★（四主区中型工业分销 + 已进口中国工业品牌 + 具名 KP）；部分坐实（MERSIS 未取）。')
# ---------------- 德国 ----------------
row('SC-700', 'de', 'AMC – Analytik & Messtechnik GmbH Chemnitz（amc-systeme.de；**Impressum：Heinrich-Lorenz-Str. 55, 09120 Chemnitz；Amtsgericht Chemnitz HRB 995；USt-ID DE 140847488；GF Dipl.-Ing. Bernd Göbel；Prokura Iris Winkler；1990 起测控 / 自动化系统集成，Advantech / Gantner / Meilhaus / NI 授权销售伙伴（allaboutautomation 展商档）**）；表内：主要是研华的；名单内未触达', 'DE',
    'DE · 1 次检索：amc-systeme.de/impressum.html（HRB / GF / USt）+ allaboutautomation 展商档 + pressebox；2026-10-29', 'https://www.amc-systeme.de/impressum.html',
    'HRB 995（Amtsgericht Chemnitz）', '营业中（官网在线）', '1990', 'GmbH', '测控 / 自动化系统集成 + 工业 IT 分销（萨克森）', 'Heinrich-Lorenz-Str. 55, 09120 Chemnitz', '小型',
    ['Bernd Göbel — Geschäftsführer', 'Iris Winkler — Prokuristin', '（info@amc-systeme.de 表内总邮箱）'],
    '**研华系统集成 → 集成 25% / 分销 20%：一页纸一次（STI-154GP / STI-288GPM / STI-0240GE 柜内工业以太网 + MOQ 1 + 付费样机；Advantech 不点名）' + EU + '**',
    '集成 25%；P 池候选 ○（四主区 + 进口台湾工业品牌 ✔ 对位 ✔ 坐实 ✔ = 冷户四条）；坐实（HRB）。')
row('SC-827', 'de', 'Dipl.-Ing. Dittmar Janetzky（itjan.de / janetzky.net；**Impressum：个体，Humboldtstr. 1, 90513 Zirndorf-Weiherhof；+49 911 9608926；janetzky@janetzky.net（= 表内）；网站「im Aufbau」**）；表内：「100 个 用于 Amazon 销售」= 数量信号', 'DE',
    'DE · 1 次检索：itjan.de 首页 Impressum（个体 / 地址 / 电话 / 邮箱）；2026-10-29', 'https://itjan.de/',
    '无（个体，§ 5 TMG Impressum）', '营业中（站点建设中）', '未取', '个体（Einzelunternehmer）', '亚马逊卖家 / IT 个体（纽伦堡近郊）', 'Humboldtstr. 1, 90513 Zirndorf-Weiherhof', '个体微型',
    ['Dittmar Janetzky — 业主（janetzky@janetzky.net 表内 = 决策人直达）'],
    '**个体亚马逊卖家 100 台意向 → 分销 20% + 预付 100%：点名 Dittmar 一页纸一次（STC-028GP $28 × 100 阶梯 + 中性包装 + 付费样机）' + EU + '**',
    '分销 20%；P 池候选 △（数量信号 ✔ 决策人直达 ✔ 四主区 ✔；个体 + 空站 → 观察档 + 预付）；坐实（Impressum 个体）。')
row('SC-956', 'de', 'systerra computer GmbH（systerra.de；**Impressum：Kreuzberger Ring 22, 65205 Wiesbaden；Amtsgericht Wiesbaden HRB 32770；USt DE345659756；GF Harald Borger；LinkedIn 11–50 人；坚固 / MIL 级计算与网络平台 20+ 年，Moxa / MPL / Mercury / RTD / Acromag 伙伴；AFCEA 展商联系人 Stephan Hering**）；表内：Moxa 分销；名单内未触达', 'DE',
    'DE · 1 次检索：systerra.de/Impressum.htm（HRB / GF / USt）+ linkedin（11–50；Moxa 伙伴）+ afcea 展商档（定位 / 联系人）；2026-10-29', 'https://www.systerra.de/Impressum.htm',
    'HRB 32770（Amtsgericht Wiesbaden）', '营业中（LinkedIn 近期更新）', '未取（20+ 年）', 'GmbH', '坚固计算 / 工业网络方案（威斯巴登；国防 / 工业）', 'Kreuzberger Ring 22, 65205 Wiesbaden', '小型（11–50）',
    ['Harald Borger — Geschäftsführer', 'Stephan Hering — 销售（AFCEA 展商档公开）', '（info@systerra.de 表内总邮箱）'],
    '**Moxa 伙伴 → 分销 20%（仅工业 / 商用场景，不承诺 MIL）：一页纸一次（STI-288DGGPM / STI-488DGGPM 管理型工业 + MOQ 1 + 付费样机；Moxa 不点名）' + EU + '**',
    '分销 20%；P 池候选 ○（四主区工业网络方案商 + 对位 + 坐实 = 冷户四条）；坐实（HRB）；守界：MIL 不承诺。')
# ---------------- 意大利 ----------------
row('SC-925', 'it', 'SARC ITALIA SRL（sarcitalia.it；**官网 privacy + registroaziende / reportaziende：P.IVA / C.F. 03184880361；REA MO-365943；Strada Albareto 503, 41122 Modena；+39 059 8751076；Ateco 46.69.2 工业电气材料批发；2024 营收 €1.31M（-10%，小亏 €13K）；2025 约 €1.3M；工业自动化技术分销商**）；表内：Atop + USR IoT；名单内未触达', 'IT',
    'IT · 1 次检索：sarcitalia.it/sarc-italia-privacy-policy.php（法人 / P.IVA / REA / 地址）+ registroaziende（营收 / Ateco）+ reportaziende；2026-10-29', 'https://www.sarcitalia.it/sarc-italia-privacy-policy.php',
    '03184880361（P.IVA；REA MO-365943）', '营业中（Attiva）', '未取', 'S.r.l.', '工业自动化分销（摩德纳）', 'Strada Albareto 503, 41122 Modena', '小型（€1.3M）',
    ['（info@sarcitalia.it 表内总邮箱；具名 KP 未取）'],
    '**Atop / USR 现供分销 → 分销 20%：一页纸一次（STI-154GP / STI-288GPM 对标 Atop 入门 + MOQ 1 + 付费样机；Atop 不点名）' + EU + '**',
    '分销 20%；P 池候选 ○（已进口台湾 / 中国工业品牌 ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔）；坐实（P.IVA）。')
# ---------------- 捷克 ----------------
row('SC-656', 'cz', '100MEGA Distribution s.r.o.（100mega.cz；**kurzy / finmag：IČO 60707968；DIČ CZ60707968；1994-05-24 成立；Železná 681/7, Horní Heršpice, 619 00 Brno；数据箱 8xtdkfn；捷克大型 IT 分销商**）；表内：主要是 Planet 的；名单内未触达', 'CZ',
    'CZ · 1 次检索：rejstrik-firem.kurzy.cz（IČO / 地址 / 成立）+ finmag 商事 + 营业执照登记；2026-10-29', 'https://www.finmag.cz/obchodni-rejstrik/60707968-100mega-distribution-s-r-o',
    '60707968（IČO）', '营业中（商事登记 2026-01）', '1994-05-24', 's.r.o.', 'IT / 网络产品大分销（布尔诺）', 'Železná 681/7, Horní Heršpice, 619 00 Brno', '中型 / 大型（捷克主要 IT 分销）',
    ['（info@100mega.cz 表内总邮箱；网络线产品经理 KP 待 LinkedIn）'],
    '**Planet 渠道大分销 → 分销 20%（长线）：一页纸一次（STC-228GP / STC-2224GP / STC-424XGGM 对标 Planet 同口型 + MOQ 1 + 付费样机）' + EU + '**',
    '分销 20%；P 池候选 ★（大分销 + Planet 渠道 + 欧洲 + 坐实）；坐实（IČO）。')
row('SC-783', 'cz', 'Express Alarm Czech s.r.o.（expressalarm.cz；**官网 kontakt + kurzy：IČ 26446863；DIČ CZ26446863；Městský soud v Praze C 82812；2001-04-18 成立；股本 CZK 200,000；20–24 人；Plkovská 2934/1, 193 00 Praha 9 – Horní Počernice；+420 281 925 363；斯洛伐克姊妹公司 Express Alarm Slovakia s.r.o.（IČO 31630146）；销售代表 Štefan Stein（stein@expressalarm.cz 官网公开）；EZS / EPS / CCTV 批发**）；表内：有名牌子 + Wi-Tek 很多产品；名单内未触达', 'CZ',
    'CZ · 1 次检索：expressalarm.cz/dokument/kontakt/（法人 / IČ / 登记 / 联系人）+ kurzy 统计（2001；20–24 人；股本）+ estav 名录；2026-10-29', 'https://www.expressalarm.cz/dokument/kontakt/',
    '26446863（IČ；Praha C 82812）', '营业中', '2001-04-18', 's.r.o.', '安防系统批发（布拉格 + 斯洛伐克）', 'Plkovská 2934/1, 193 00 Praha 9 – Horní Počernice', '小型（20–24）',
    ['Štefan Stein — Obchodní zástupce（stein@expressalarm.cz 官网公开）', '（obchod@expressalarm.cz 表内）'],
    '**Wi-Tek 现供安防批发 → 分销 20%：一页纸一次（STC-028GP $28 / STC-228GP $33 对标 Wi-Tek + STI-154GP + MOQ 1 + 付费样机；Wi-Tek 不点名）' + EU + '**',
    '分销 20%；P 池候选 ○（已进口中国同类品牌 ✔ 欧洲 ✔ 对位 ✔ 坐实 ✔；双国渠道）；坐实（IČ）。')
row('SC-809', 'cz', 'HTV Hodina — Michal Hodina（htv-hodina.cz；**firmy.cz / ziveobce：个体经营（Fyzická osoba）IČ 48424986；DIČ CZ6804201646；U Kapličky 63/8, 712 00 Ostrava – Muglinov；+420 602 719 145；Jablotron 安防 / CCTV 门店 + 批零；业主 Michal Hodina、店长 Matěj Hodina（matej@）**）；表内：Wi-Tek；名单内未触达', 'CZ',
    'CZ · 1 次检索：firmy.cz（IČ / 地址 / 邮箱）+ ziveobce（个体法律形式 / DIČ / 联系人）+ jahho 名录；2026-10-29', 'https://ziveobce.cz/htv-hodina_f1081862?loc=50114944&cz=21',
    '48424986（IČ；个体）', '营业中（名录在线）', '未取', '个体（živnostník）', '安防 / CCTV 门店（俄斯特拉发）', 'U Kapličky 63/8, 712 00 Ostrava – Muglinov', '个体微型',
    ['Michal Hodina — 业主', 'Matěj Hodina — 店长（matej@htv-hodina.cz 名录公开）'],
    '**个体门店 + 冷户 → 不动（来信再起则预付 100%）**',
    '回 C 储备（个体微型 + 非主区 + 冷户 0 互动）；坐实（IČ）。')
row('SC-908', 'cz', 'BLUECOM s.r.o. — prumysloveswitche.cz（bluecom.cz；**官网 Advantech 页 / networkmanagement.cz：IČ 25955993；DIČ CZ25955993；Krajský soud v Hradci Králové C 17530；Nerudova 1034, 537 01 Chrudim；+420 469 688 054；Advantech B+B 工业交换机 / Axis / Bosch / Fluke / Milestone / HiPoE 经销商价目**）；表内：「工业交换机」专卖，基本都是研华的；名单内未触达', 'CZ',
    'CZ · 1 次检索：bluecom.cz/advantech（法人 / IČ / 登记 / 地址）+ bluecom.cz/dealer（经销品牌）+ networkmanagement.cz/kontakt.php；2026-10-29', 'https://www.bluecom.cz/advantech',
    '25955993（IČ；Hradec Králové C 17530）', '营业中（官网在线）', '未取', 's.r.o.', '工业交换机 / 安防 / 网络诊断分销（赫鲁迪姆）', 'Nerudova 1034, 537 01 Chrudim', '小型',
    ['（sales@bluecom.cz 表内总邮箱；具名 KP 未取）'],
    '**工业交换机专卖 → 分销 20%：一页纸一次（STI-154GP / STI-288GPM / STI-288DGGPM / STI-0240GE 对标 Advantech B+B 入门 + MOQ 1 + 付费样机；Advantech 不点名）' + EU + '**',
    '分销 20%；P 池候选 ○（对位极强 + 进口台湾工业品牌 ✔ 欧洲 ✔ 坐实 ✔）；坐实（IČ）。')
# ---------------- 比利时 ----------------
row('SC-856', 'other', 'MegaMobile.be — M&C Technology（megamobile.be；**官网 Over ons：Onze-Lieve-Vrouwestraat 135, 2800 Mechelen；BTW BE 0479.101.014；手机 / 电子配件网店**）；表内：Wi-Tek；名单内未触达', 'BE',
    'BE · 1 次检索：megamobile.be/nl/info/over-ons（法人商号 / BTW / 地址）；2026-10-29', 'https://www.megamobile.be/nl/info/over-ons',
    '0479.101.014（BTW / KBO）', '营业中（网店在线）', '未取', '未取（商号 M&C Technology）', '手机 / 电子配件网店（梅赫伦）', 'Onze-Lieve-Vrouwestraat 135, 2800 Mechelen', '微型',
    ['（info@megamobile.be 表内总邮箱）'],
    '**主业手机配件网店，PoE 为边角 → 不动**',
    '回 C 储备（坐实但主业不对位 + 冷户）；坐实（BTW）。')
# ---------------- 波兰 ----------------
row('SC-770', 'pl', 'ELMARK AUTOMATYKA S.A.（elmark.com.pl；**krs-online / owg / 官网 regulamin：KRS 0000803828（S.A. 2019-10-01 转制）；NIP 5252072585；REGON 013144306；股本 PLN 650,000；ul. Bukowińska 22 lok. 1B, 02-703 Warszawa；1997 起工业自动化分销（Moxa / Advantech 等多牌）**）；表内：很多牌子；名单内未触达', 'PL',
    'PL · 1 次检索：krs-online.com.pl（NIP / REGON / 1997）+ owg.pl（KRS / 状态 AKTYWNY / VAT 在册）+ elmark.com.pl/regulamin（登记法院 / 股本）；2026-10-29', 'https://www.owg.pl/krs-rp/elmark_automatyka_spolka_akcyjna_9,88,000080382,0000803828',
    '0000803828（KRS；NIP 5252072585）', '营业中（AKTYWNY；VAT czynny）', '1997（S.A. 2019）', 'S.A.', '工业自动化 / 工业网络分销（华沙）', 'ul. Bukowińska 22 lok. 1B, 02-703 Warszawa', '中型（股本 PLN 650k）',
    ['（elmark@elmark.com.pl 表内总邮箱；工业网络产品经理 KP 待 LinkedIn）'],
    '**波兰工业分销主体 → 分销 20%：一页纸一次（STI-154GP / STI-288GPM / STI-0240GE / STI-488DGGPM + MOQ 1 + 付费样机；Moxa 不点名）' + EU + '**',
    '分销 20%；P 池候选 ★（波兰中型工业分销 + 对位 + 坐实）；坐实（KRS / NIP）。')
# ---------------- 美国 ----------------
row('SC-562', 'us', 'Baltic Networks（balticnetworks.com；**rocketreach / leadiq / cbinsights：2200 Ogden Ave Suite 100, Lisle, IL 60532；2005 年创立；约 9 人；营收估 $6M；面向 WISP / 集成商的增值分销 + 工程服务，50+ 厂牌 5,000 SKU（路由 / 交换 / 天线 / 回传 / 光纤）；(630) 929-3610**）；表内：很多牌子、工业 FS / SFP；9 推 0 回', 'US',
    'US · 1 次检索：rocketreach（地址 / 2005 / 9 人 / $6M）+ leadiq（定位 / 50+ 厂牌）+ cbinsights；IL SoS 未取；2026-10-29', 'https://leadiq.com/c/baltic-networks/5a1d9dd82300005a008dbfdb',
    '未取（IL SoS 未查）', '营业中（名录 2024 更新）', '2005', 'Inc. / LLC（推定）', 'WISP 无线 / 网络增值分销（芝加哥西郊）', '2200 Ogden Ave Suite 100, Lisle, IL 60532', '微型 / 小型（约 9；$6M）',
    ['Laura Tomasello — Customer Service Manager & Sales Support（RocketReach）', '（hello@ / support@balticnetworks.com 表内）'],
    '**WISP 分销 → 分销 20%：一页纸一次（STI-154GP 工业 PoE 塔上 + STC-228GP + STC-110XGE MC + MOQ 1 + 付费样机）' + US + '**',
    '分销 20%；P 池候选 ○（主区分销主体 + 对位 + 坐实（名录）= 冷户四条）；部分坐实（IL SoS 未取）。')
row('SC-634', 'us', 'New Tech Industries, Inc.（newtechindustries.com / newtechind.com；**Crunchbase：Davie, Florida；11–50 人；制造 + 分销电信 / 网络 / 光纤 / 视频 / 散装线缆；官网产品页：自有品牌「New Tech Industries」工业 PoE DIN 导轨交换机 NT408-2P（8 口千兆 240W 2 SFP -40～75 ℃）、NT404-1 等 = 自有型号贴牌；同时在售 TRENDnet TI-PG80 / TI-G50 / TI-G80**）；表内：Wi-Tek 的也有、比较多外壳；harry@ / jim@ / subhanshu@ 三具名；18 推全退信但两域 MX 正常', 'US',
    'US · 1 次检索：newtechindustries.com 产品页 ×2（自有品牌型号 NT408-2P / NT404-1）+ crunchbase（法人名 / Davie FL / 11–50）；FL sunbiz 未取；2026-10-29', 'https://www.newtechindustries.com/8-port-gigabit-industrial-fiber-poe-din-rail-mount-switch-240w-2-sfp-40-to-75-celsius/',
    '未取（FL sunbiz 未查；法人名坐实）', '营业中（官网在售）', '未取', 'Inc.', '线缆 / 网络产品制造 + 分销，自有品牌工业 PoE 交换机（南佛罗里达）', 'Davie, Florida', '小型（11–50）',
    ['harry@ / jim@newtechindustries.com、subhanshu@newtechind.com（表内三具名 = 均退信；职务未取）'],
    '**自有型号工业 PoE 交换机（NT408-2P 等）现由中国厂供 → OEM 30%：找到新地址后一页纸一次（STI-288GPM 对标 NT408-2P 丝印 + STI-154GP + MOQ + 付费样机）' + US + '**；退信 → 官网表单 / LinkedIn 换址',
    'OEM 30%；P 池候选 ★（自有品牌工业 PoE 线 + 主区 + 对位极强；退信待换址）；部分坐实（sunbiz 未取）。')
# ---------------- 英国 ----------------
row('SC-671', 'gb', 'LEADER OPTEC LIMITED（leaderoptec.com；**companycheck：Company No 03936485；2000-02-29 注册；Active – Accounts Filed；SIC 28990；Unit 15 Lite Linke Buildings, St. Asaph Business Park, St Asaph LL17 0LJ；董事 Paul Anthony Desmond（2000 起 = 表内 pauldesmond@）、Laurie Sara Summers；秘书 Lisa Desmond；ZoomInfo 11–50 人 / $5.1M；Crunchbase：光纤 + 铜缆制造商，MD Paul Desmond**）；表内：passive / FTTH 为主的 trader，30–40% 业务在中国，表内邮箱 = 负责采购 active 产品的负责人；未触达', 'GB',
    'GB · 1 次检索：companycheck.co.uk（公司号 / 董事 / 状态）+ zoominfo（11–50；$5.1M）+ crunchbase（MD Paul Desmond）；2026-10-29', 'https://companycheck.co.uk/company/03936485/LEADER-OPTEC-LIMITED/companies-house-data',
    '03936485', 'Active（账目已报）', '2000-02-29', 'Private limited', '光纤 / 铜缆产品制造 + 贸易（北威尔士）', 'Unit 15 Lite Linke Buildings, St. Asaph Business Park, St Asaph LL17 0LJ', '小型（11–50；$5.1M）',
    ['Paul Anthony Desmond — Director / MD（pauldesmond@leaderoptec.com 表内 = 决策人直达）', 'Laurie Sara Summers — Director', 'Lisa Desmond — Company Secretary'],
    '**自有品牌布线商补 active 线 → OEM 30%：点名 Paul 一页纸一次（STC-028GP / STC-228GP / STC-110XGE MC 丝印 + MOQ + 付费样机；可提中国采购直供）' + EU + '**',
    'OEM 30%；P 池候选 ★（MD 邮箱在表 + 自有品牌 + 中国采购经验 + 四主区）；坐实（Companies House）。')
row('SC-704', 'gb', 'ANNICOM LIMITED（annicom.com；**globaldatabase / zoominfo：Unit 21 Highview, High Street, Bordon, Hampshire GU35 0AX；+44 1420 487788；24 人（账目）；营收 <$5M；董事 Dennis Gates；Crunchbase：工业控制 / HVAC / 楼宇自动化电子设计制造 + 电气分销**；Companies House 号未取）；表内：Kyland；名单内未触达', 'GB',
    'GB · 1 次检索：uk.globaldatabase.com（地址 / 24 人 / 董事）+ zoominfo（51–200 估）+ crunchbase（业务）；CH 号未取；2026-10-29', 'https://uk.globaldatabase.com/company/annicom-limited',
    '未取（Companies House 号未查；法人名坐实）', '营业中（名录在线）', '未取', 'Limited', '工业控制电子设计制造 + Kyland 等分销（汉普郡）', 'Unit 21 Highview, High Street, Bordon GU35 0AX', '小型（24）',
    ['Dennis Gates — Director', 'Hannah Psaila — Inside Sales（globaldatabase）', '（sales@annicom.com 表内）'],
    '**Kyland 现供 → 分销 20%：一页纸一次（STI-154GP / STI-288GPM / STI-0240GE 对标 Kyland 入门 + MOQ 1 + 付费样机；Kyland 不点名）' + EU + '**',
    '分销 20%；P 池候选 ○（四主区 + 已进口中国工业品牌 ✔ 对位 ✔ 坐实 部分 ✔）；部分坐实（CH 号未取）。')
row('SC-855', 'gb', 'Mast Digital (UK) Ltd（mastdigital.co.uk；**官网 About + LinkedIn：Unit A Station Road Industrial Estate, Epworth, Doncaster DN9 1JZ；01427 874455；2014 年成为 Ltd；2016 迁现址；2021-01 起 Dahua Tier 1 英国分销商；20+ 人；Wi-Tek / Ajax / TP-Link / Netvio / Videx / GJD 授权分销；MD Stuart Smedley、Director Mick Smedley；家族 trade-only B2B**；Companies House 号未取）；表内：Dahua + Wi-Tek；名单内未触达', 'GB',
    'GB · 1 次检索：mastdigital.co.uk/support/about-us（沿革 / 规模）+ linkedin（授权品牌 / MD）+ 官网页脚（地址）；CH 号未取；2026-10-29', 'https://www.mastdigital.co.uk/support/about-us',
    '未取（Companies House 号未查；法人名坐实）', '营业中（官网 2026）', '2014（Ltd）', 'Ltd', 'CCTV / 网络 / AV trade-only 分销（南约克郡）', 'Unit A Station Road Industrial Estate, Epworth, Doncaster DN9 1JZ', '小型 / 中型（20+）',
    ['Stuart Smedley — Managing Director', 'Mick Smedley — Director', '（enquiries@mastdigital.co.uk 表内）'],
    '**Wi-Tek 现供 Dahua 分销 → 分销 20%：点名 Stuart 一页纸一次（STC-028GP $28 / STC-228GP $33 / STC-2224GP 对标 Wi-Tek + STI-154GP + MOQ 1 + 付费样机；Wi-Tek 不点名）' + EU + '**',
    '分销 20%；P 池候选 ★（四主区快速增长 CCTV 分销 + 已进口中国同类品牌 + MD 具名）；部分坐实（CH 号未取）。')
row('SC-935', 'gb', 'Semaphore Systems Ltd（semaphore-systems.co.uk；**官网 About：Unit 4, The Quadrant, 135 Salusbury Road, London NW6 6RJ；020 7625 7744；1988 起 Advantech 主要英国分销 + 伦敦组装 IPC（DAB 广播 / 国防 / 科研）；ZoomInfo：1979 创立；1–10 人；<$5M**；Companies House 号未取）；表内：Advantech；名单内未触达', 'GB',
    'GB · 1 次检索：semaphore-systems.co.uk/about-us/（地址 / 定位）+ 产品页（Advantech 1988 起）+ zoominfo（1979；1–10）；CH 号未取；2026-10-29', 'https://www.semaphore-systems.co.uk/about-us/',
    '未取（Companies House 号未查；法人名坐实）', '营业中（官网在线）', '1979', 'Limited', 'Advantech 工业计算分销 + IPC 组装（伦敦）', 'Unit 4, The Quadrant, 135 Salusbury Road, London NW6 6RJ', '微型（1–10）',
    ['（sales@semaphore-systems.co.uk 表内总邮箱）'],
    '**研华分销补工业交换机 → 分销 20%：一页纸一次（STI-154GP / STI-288GPM + MOQ 1 + 付费样机；Advantech 不点名）' + EU + '**',
    '分销 20%；P 池候选 ○（四主区 + 进口台湾工业品牌 ✔ 对位 ✔ 坐实 部分 ✔；微型）；部分坐实（CH 号未取）。')

print('b128_c rows written: 18')
