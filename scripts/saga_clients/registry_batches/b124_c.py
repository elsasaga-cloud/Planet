# -*- coding: utf-8 -*-
"""第 124 批（T29-U118，2026-10-29）—— **C 池三闸 · 闸 2 首批**：闸 1 候选 55 户中的四主区 19 + 波兰 2 = 21 户查底数。
路径：GB Companies House 1 查即得（Crony 05732999 / Eurosat SC204360 / Qvis 08877091）；DE 名录（Leunig HRB 1531 Siegburg；2direct / Voygar / Gemaxx 官网 Impressum + 名录，HRB 未取）；
US 名录 + SAM.gov（FIS UEI H7LXDNB9UAY8；Winncom Ohio corp 1999）；TR 官网 + Crunchbase / RocketReach（MERSIS ✗）；PL KRS 官网自列（Eltrox 0000175807 / AAT 0000838329）；CA 官网 + Crunchbase（Ontario corp 号 ✗）。
1 查未得：Kıraç Bilişim（TR）→ 未坐实；Sami Çeuik 无公司名 → 0 查。每户 1 查、depth 1。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from registry_store import put
B = 124
F = '2026-10-29'
EU = '— 欧洲常规：英文稿、20 / 25 / 30 + T/T 50/50（未坐实 预付 100%）+ DAP（买方清关）或 FOB 深圳；周四 12–14 当地'
US = '— 北美常规：英文稿、20 / 25 / 30 + T/T 50/50 + FOB 深圳 / DAP（买方清关）；周三 08–10 当地'
TR = '— 土耳其常规：英文稿（可附土语备注）、20 / 25 / 30 + T/T 50/50（未坐实 预付 100%）+ FOB 深圳 / DAP（买方清关）；周四 10–12 当地'


def row(code, key, name, iso, source, url, number, status, inc, ctype, sic, addr, size, officers, line, notes):
    put(code, key=key, batch=B, name=name, iso=iso, fetched=F, source=source, url=url, number=number, status=status,
        incorporated=inc, company_type=ctype, sic=[sic], address=addr, accounts='未取', accounts_due='—', size_band=size,
        officers=officers, psc='未取', charges='', prev_names=[], lines=[line], notes=notes)


# ---------------- 土耳其 ----------------
row('SC-1009', 'tr', 'Varel Alarm Sistemleri Ticaret A.Ş.（varelalarm.com；**官网：1990 年创立、İstanbul Acıbadem 总部、消防 / CCTV / 门禁 / 紧急广播系统集成商、Siemens Solution Partner、2012 年并入荷兰 ARAS B.V.（ARAS Security 集团）；RocketReach 14 人；ZoomInfo 营收 <$5M**）；MERSIS 号 1 查未得 → 部分坐实；表内：工商业 FS、在卖 Utepo；arasvarel.com 无 MX（退信域）', 'TR',
    'TR · 1 次检索：varelalarm.com 首页（1990 yılında kurulan Varel Alarm Sistemleri Tic. A.Ş.；E5 Karayolu Üstü Etap İş Merkezi A Blok Lavanta Sokak No:16 Acıbadem；+90 216 327 62 80；vag@varelalarm.com；2012 ARAS B.V.）+ rocketreach（Employees 14；Founded 1990）+ zoominfo（<$5M）；2026-10-29', 'https://varelalarm.com/',
    '未取（MERSIS 1 查未得）', '营业中（官网 2026）', '1990', 'A.Ş.（ARAS B.V. 子公司）', '弱电 / 安防系统集成（消防、CCTV、门禁；伊斯坦布尔）', 'E5 Karayolu Üstü Etap İş Merkezi A Blok Lavanta Sok. No:16, Acıbadem – İstanbul', '小型（约 14）',
    ['（无具名决策人；vag@varelalarm.com 官网总邮箱 = 收件人；info@varelalarm.com 表内）', 'Burak Akgöz — Senior Technical Services Engineer（RocketReach；非决策人）'],
    '**集成商 25%：换 varelalarm.com 地址重发一页纸一次（STC-228GP $33 / STI-154GP 工业 + MOQ 1 + 付费样机；Utepo 不点名）' + TR + '**；再无回声 → 观察档',
    '集成商 25%；P 池候选 △（观察档：小型集成商、ARAS 集团采购或集中）；部分坐实。')
row('SC-1855', 'tr', 'Kıraç Bilişim（kiracbilisim.com.tr；shaalan@；**1 查「Kıraç Bilişim kiracbilisim.com.tr」仅返回 ARC / Kayra / Kargılı 等同业，无本体 → 未坐实**）；表内：跟澳视买、知道天地伟业、要求先发 email；9 次跟进无回复', 'TR',
    'TR · 1 次检索无命中（返回同业 arcbilisim / kayrabilisim / kargilibilisim）；2026-10-29', '',
    '未取（1 查无命中）', '存续待核（域名 MX 正常）', '未取', '未取', '安防 / IT（土耳其，推定）', '未取', '微型（推定）',
    ['（shaalan@kiracbilisim.com.tr 表内联系人，职务未取）'],
    '**未坐实 + 9 推 0 回 → 不动，回 C 储备**' + TR, '不动；回 C；未坐实。')
row('SC-1965', 'tr', 'Entegron Network（entegronnetwork.com；**官网产品页自有品牌「Entegron Switch」：ENTDPS1300P-8G-1TS-BT-90W（8 口 PoE++ BT）、ENTDS100-7PD（24V 反向 PoE，ISP / WISP）、ENTDPS8210PM（8 PoE 管理 + 2 SFP）= 贴牌中国 PoE 交换机（表内 E-wind / GXCOM）**）；公司登记 1 查未得（产品页占用）→ 部分坐实；Simon 曾判不行；2 次跟进无回复', 'TR',
    'TR · 1 次检索：entegronnetwork.com/urun/…（Brand: Entegron Switch；MODEL ENTDPS1300P-8G-1TS-BT-90W / ENTDS100-7PD / ENTDPS8210PM）；2026-10-29', 'https://www.entegronnetwork.com/urun/8-port-10-100-1000mbps-managed-poe-switch-with-2-gigabit-sfp-slots/',
    '未取（MERSIS 1 查未得）', '营业中（官网产品页在线）', '未取', '未取（Ltd. Şti. 推定）', '网络设备自有品牌（PoE / PON / 反向 PoE；土耳其）', '未取（土耳其）', '小型（推定）',
    ['（info@entegronnetwork.com 表内；具名 KP 未取）'],
    '**自有品牌贴牌 → OEM 30%：一页纸一次（STC-228GP 8 PoE + 2 SFP 管理 $33 / STC-028GP $28 同口型对标 + 丝印 / 彩盒 MOQ + 付费样机；反向 PoE / BT 90W 不供明说）' + TR + '**；Simon 可否决',
    'OEM 30%；P 池候选 ★（自有品牌）；部分坐实；Simon 曾判不行。')
row('SC-2481', 'tr', 'Okisan Güvenlik Teknolojileri San. ve Tic. A.Ş.（okisan.com；**Crunchbase：1986 年创立、Şişli İstanbul、11–50 人、安防技术进口 + 分销、Tiandy / Dahua 土耳其授权分销；Tiandy 官网合作方页：OKİSAN PLAZA, Mahmut Şevket Paşa Mah. Odesa Bulvarı Ersan Sok. No:24 Okmeydanı – Şişli**）；MERSIS 号 1 查未得 → 部分坐实；表内：已从深圳 HSGQ 进口 1V1D $30、用丰润达商业 PoE、要 catalog；KP Gökhan（gokhan@okisan.com，WA 已加）；Simon 曾判不行', 'TR',
    'TR · 1 次检索：crunchbase（Okisan Güvenlik Teknolojileri；Founded 1986；Sisli, Istanbul；11-50；import and distribution of security technologies；authorized distributor Tiandy and Dahua）+ en.tiandy.com/projects（Okisan Güvenlik Teknolojileri San. ve Tic. A.Ş.；OKİSAN PLAZA 地址）；2026-10-29', 'https://en.tiandy.com/projects/okisan-g-venlik-teknolojileri-san-ve-tic-a/3161.html',
    '未取（MERSIS 1 查未得）', '营业中（官网产品页 2026-05）', '1986', 'A.Ş.', '安防技术进口 + 分销（Tiandy / Dahua 授权；伊斯坦布尔）', 'Okisan Plaza, Mahmut Şevket Paşa Mah. Odesa Bulvarı Ersan Sok. No:24, Okmeydanı – Şişli / İstanbul', '小型（11–50）',
    ['Gökhan — 表内联系人（gokhan@okisan.com；WA 已加）= 收件人', 'Okan — okan@okisan.com（表内）'],
    '**现成进口商 + 分销 → 分销 20%：一页纸一次（STC-228GP $33 / STC-2224GP $86 / STC-110XGE $65 一口价 + MOQ 1 + 付费样机 + 工业线价目；HSGQ / 丰润达 不点名）' + TR + '**；Simon 可否决',
    '分销 20%；P 池候选 ★（进口经验 + 授权分销）；部分坐实；Simon 曾判不行。')
row('SC-259', 'tr', 'Sami Çeuik（ISAF 展；**无公司名 / 无邮箱 → 0 查**）— 表内：用光网视交换机、政府项目、问 500 台 2 光 8 PoE 网管价、展会最后一天买 1 台 2 光 10 电 PoE 样机 $100、Evelyn 加了微信', 'TR',
    '0 查（无公司名 / 无域名）；2026-10-29', '', '0 查', '互动中（展会成样品单）', '—', '未取', '安防 / 政府项目集成（土耳其，推定）', '未取', '未取',
    ['Sami Çeuik — 本人（微信 via Evelyn；无邮箱）= 收件人'],
    '**样品已成单 + 500 台口型 → 回访（集成商 25%）：微信一页纸（2 光 8 PoE 网管 STC-228GP $33 阶梯 100 / 500 台 + 付费样机已有）；先向 Simon / Evelyn 要公司名再补登记**' + TR,
    '回访（集成商 25%）；P 池候选 ★（成单 + 主区，§5 有关系户 ≥2 条）；0 查（待公司名）。')

# ---------------- 英国 ----------------
row('SC-1010', 'gb', 'CRONY TRADING LTD（**Companies House 05732999：Active；成立 2006-03-07；曾用名 CRONY ENTERTAINMENT LTD（至 2007-12-05）；注册地址 Flat 2, 218 Portland Road, South Norwood, London SE25 4QB（住宅）；SIC 46160 纺织 / 服装 / 鞋类销售代理；微型账目、1 名员工、股本 £1；唯一董事 Anthony Mwangi Waweru（2008-04 起，前任 7 人已辞）**）；表内：商业 PoE 用洪瑞的、网站品类杂；booking@ 退信', 'GB',
    'GB · 1 次检索：find-and-update.company-information.service.gov.uk/company/05732999 + companiesintheuk（Employees 1；Capital 1 GBP；Micro）+ companycheck（SIC 46160）；2026-10-29', 'https://find-and-update.company-information.service.gov.uk/company/05732999',
    '05732999', 'Active（账目至 2026-03-31 已交）', '2006-03-07', 'Private limited Company', '46160 纺织 / 服装销售代理（登记）≠ 网站网络产品', 'Flat 2, 218 Portland Road, South Norwood, London, SE25 4QB', '微型（1 人，股本 £1）',
    ['Anthony Mwangi Waweru — Director（Companies House；1982-07）'],
    '**一人贸易公司 + 住宅注册地 + 登记主业纺织 + 退信 → 不动，回 C 储备**' + EU, '不动；回 C；坐实（微型 / 红旗：£1 股本 + 住宅地址 + 主业不符）。')
row('SC-2372', 'gb', 'EUROSAT (SCOTLAND) LIMITED（eurosatscotland.co.uk / 关联 oprema.co.uk；**Companies House SC204360：Active；成立 2000-02-28；30 Couper Street, Glasgow G4 0DL；SIC 46439 电视 / 电器批发；董事 Graeme Colin Miller（2017-04）、Martin Brian Mulhern（2017-04）、Colin Thomas Miller（2000-02）；0141 552 2111**）；表内：大型安防分销、在卖 Dahua PoE；KP graeme@ = 董事；19 次跟进无回复；Simon 曾判不行', 'GB',
    'GB · 1 次检索：find-and-update.company-information.service.gov.uk/company/SC204360 + companycheck（3 directors）+ mirror directory（0141 552 2111）；2026-10-29', 'https://find-and-update.company-information.service.gov.uk/company/SC204360',
    'SC204360', 'Active（Accounts Filed）', '2000-02-28', 'Private limited Company', '46439 电视 / 卫星 / 电器批发（安防分销，Oprema 渠道）', '30 Couper Street, Glasgow, G4 0DL', '中型（25 年；3 董事）',
    ['Graeme Colin Miller — Director（Companies House 2017-04；graeme@eurosatscotland.co.uk 表内）= 收件人', 'Martin Brian Mulhern — Director（2017-04）', 'Colin Thomas Miller — Director（创始 2000）'],
    '**分销 20%：对董事一页纸一次（Dahua PoE 同口型对标 STC-028GP $28 / STC-228GP $33 / STC-2224GP $86 + MOQ 1 + 付费样机；UKCA）' + EU + '**；Simon 可否决',
    '分销 20%；P 池候选 ○（英国分销 + 董事直达）；坐实；Simon 曾判不行。')
row('SC-678', 'gb', 'Qvis（qvis.co.uk；**运营主体推定 QVIS LIGHTING & SECURITY LIMITED 08877091：Live；成立 2014-02；4 Merlin Park, Airport Service Road, Portsmouth PO3 5FU；SIC 27400；100% 股东 ENERGY & SAFETY GROUP LTD 15078583；Pomanda「established, mid sized」；另有壳公司 QVIS LIMITED 07568582（2011）/ QVIS CCTV LIMITED 08170128（2012；净资产 £100；董事 Joanna Elizabeth Brown）**）；表内：安防品牌、在华有摄像机工厂、问过 fiber optics 想买样品、「有需要会直接联系」；从未邮件触达', 'GB',
    'GB · 1 次检索：pomanda.com/company/08877091（Qvis Lighting & Security Limited；PO3 5FU；SIC 27400；Energy & Safety Group Ltd 100%）+ onlinefilings（Qvis Limited 07568582）+ companydatashop（Qvis CCTV Limited 08170128）；2026-10-29', 'https://pomanda.com/company/08877091/qvis-lighting-&-security-limited',
    '08877091（运营主体推定；壳 07568582 / 08170128）', 'Live / Active', '2014-02（品牌 2011 起）', 'Private limited（集团子公司）', '27400 照明 + 安防设备制造 / 自有品牌 CCTV + PoE 交换机', '4 Merlin Park, Airport Service Road, Portsmouth, Hampshire, PO3 5FU', '中型（集团子公司）',
    ['（sales@qvis.co.uk 表内；具名 KP 未取 — 一页纸请转产品经理）', 'Joanna Elizabeth Brown — 壳公司董事（Companies House；非运营 KP）'],
    '**自有品牌 → OEM 30%：一页纸一次（Qvis 牌 PoE 同口型 STC-028GP / STC-228GP / STC-2224GP 贴牌 + 丝印 MOQ + 付费样机；UKCA；光纤 / SFP 不供明说）' + EU + '**；回信即升',
    'OEM 30%；P 池候选 ★（英国品牌商）；坐实（主体映射推定）。')

# ---------------- 德国 ----------------
row('SC-1013', 'de', 'Gemaxx Network / geMaxx 品牌（gemaxxnetwork.com；**官网 about：「geMaxx brand established by an experienced team… network projects」= 自有品牌网络产品（表内 ONV 贴牌）；关联 GEMAXX Communications GmbH（Duisburg；Crunchbase 11–50；+49 211 176 08 02；info@gemaxx.net）；gemaxx24.de 页脚「GEMAXX Communications GmbH (2001 - 2023)」**）；HRB 1 查未得；sales@ 退信 + about 页 2022 → 存续待核', 'DE',
    'DE · 1 次检索：gemaxxnetwork.com/about-us（geMaxx brand；2022-12）+ gemaxx24.de（GEMAXX Communications GmbH 2001-2023；Hotline +49 211 176 08 02；info@gemaxx.net）+ crunchbase（Duisburg；11-50；Legal Name GEMAXX Communications GmbH）；2026-10-29', 'https://gemaxxnetwork.com/about-us/',
    '未取（HRB 1 查未得）', '存续待核（about 2022；sales@ 退信；集团站 2023）', '2001（GEMAXX Communications）', 'GmbH（关联主体）', '电信（电话卡 / IVR / 呼叫中心）+ 自有品牌网络设备', 'Duisburg, Nordrhein-Westfalen（街道未取）', '小型（11–50）',
    ['（info@gemaxx.net 集团站公开邮箱 = 试探收件人；sales@gemaxxnetwork.com 退信）'],
    '**自有品牌 → OEM 30%，但先确认存续：info@gemaxx.net 一封试探（一页纸：工业 / 商业 PoE 贴牌 + MOQ + 付费样机）' + EU + '**；无回声或退信 → 回 C（巡检 2 个月后复核官网）',
    'OEM 30%；P 池候选 △（观察档：存续待核）；部分坐实。')
row('SC-1230', 'us', 'wantec, inc（wantec.com；**官网 about：1999 年德国创立、CEO Stefan Rupp、7,000 sqft 研发生产；美国分销运营 524 S Main Street, Simpsonville, SC 29681（2019 新 5,000 sqft）；门禁对讲 / 2wIP 网络适配器 / wantecWire 跳线；自有品牌工业交换机 Wantec 3405（4 口 + 1 SFP DIN 导轨，EAN 4250367734056，Lieske 售 €158）= 宇航贴牌**）；LinkedIn 51–200（偏高）；表内：周边产品 + 宇航的工业 FS；18 次跟进无回复', 'US',
    'US · 1 次检索：wantec.com/about.html（Founded in Germany in 1999 by CEO Stefan Rupp；Simpsonville, SC）+ linkedin（wantec, inc；524 S Main Street Simpsonville SC 29681；Founded 1999）+ industry-electronics.com（Wantec 3405 Industrial Fiber Ethernet Switch 4 port + 1 SFP；EAN 4250367734056）；2026-10-29', 'http://www.wantec.com/about.html',
    '未取（SC SoS / 德国 HRB 未查）', '营业中（官网 + 经销在售）', '1999（德国）', 'Inc.（美国分销）+ 德国母体', '门禁对讲 / 网络配件制造 + 自有品牌工业交换机', '524 S Main Street, Simpsonville, SC 29681, US（德国研发生产地未取）', '小型 / 中型（LinkedIn 51–200 偏高）',
    ['Stefan Rupp — CEO / 创始人（官网 about；无公开邮箱）', 'Andre Costa — 表内联系人（andre.costa@wantec.com）= 收件人', '（service@wantec.com 表内）'],
    '**自有品牌工业交换机（已贴牌中国货）→ OEM 30%：一页纸一次（STI-154GP 4 PoE + 1 SFP 工业 / STI-054GP 同口型对标 Wantec 3405 + 丝印 MOQ + 付费样机；DE + US 两地口径）' + US + '**；回信即升',
    'OEM 30%；P 池候选 ★（德美双地自有品牌）；部分坐实。')
row('SC-161', 'de', '2direct GmbH（LogiLink 品牌；logilink.eu / 2direct.de；**lieferanten.de：Schalksmühle；2001 年 Lüdenscheid 创立；Geschäftsführer Wilfried Grohnert、Jan Alberts；5,000+ 产品、12 个欧洲核心市场、约 14,000 经销商客户；自有品牌 LogiLink / 2direct；「个性化 OEM 产品方案」为副业；RocketReach：Langenstück 5, 58579 Schalksmühle；$3M / 11 人（偏低）；LinkedIn 11–50**）；HRB 1 查未得 → 部分坐实；表内：在卖宇航的工业 FS / optical switch；KP grohnert@2direct.de = Geschäftsführer；Simon 曾判不行；15 次跟进无回复', 'DE',
    'DE · 1 次检索：lieferanten.de/lieferant-822-2direct-gmbh（Geschäftsführer Wilfried Grohnert, Jan Alberts；2001；über 50 Mitarbeiter；Eigenmarken LogiLink und 2direct；OEM-Produktlösungen）+ linkedin（Schalksmühle；11–50；2001）+ rocketreach（5 Langenstück 58579；Jan Alberts Geschäftsführer）；2026-10-29', 'https://www.lieferanten.de/lieferant-822-2direct-gmbh.html',
    '未取（HRB 1 查未得）', '营业中（官网 + 名录 2026）', '2001', 'GmbH', '计算机配件 / 网络技术批发 + 自有品牌制造（LogiLink）', 'Langenstück 5, 58579 Schalksmühle, Nordrhein-Westfalen', '中型（名录 50+；RocketReach 11 偏低）',
    ['Wilfried Grohnert — Geschäftsführer（lieferanten.de；grohnert@2direct.de 表内）= 收件人', 'Jan Alberts — Geschäftsführer（lieferanten.de / RocketReach；无公开邮箱）'],
    '**品牌商 + 14,000 经销网 → OEM 30%：对 GF 一页纸一次（LogiLink 牌工业 / 商业 PoE 贴牌：STI-054GP / STI-154GP / STC-028GP + 丝印彩盒 MOQ + 付费样机；在售宇航款不点名）' + EU + '**；Simon 可否决；回信即升',
    'OEM 30%；P 池候选 ★★（德国品牌商 + GF 直达）；部分坐实；Simon 曾判不行。')
row('SC-1935', 'de', 'LEUNIG GmbH（leunig.de；**firmendatenbanken.de：Sanddornweg 8b, D-53773 Hennef；HRB 1531 Siegburg；USt-ID DE123112391；Geschäftsführung Josef Hermann Vester（Hermann-J. Vester）；elektro-einkaufsfuehrer：1980 年创立；KVM / 延长器 / 远程电源 / 时间服务器 / 数据线缆；「欧洲、北美、远东战略伙伴」；Hersteller + Großhändler**）；表内：工业 FS / MC / 串口，主要卖 Moxa；sales@ 曾退信但域名正常', 'DE',
    'DE · 1 次检索：firmendatenbanken.de/unternehmen/detail/336211/leunig-gmbh（HRB 1531 Siegburg；DE123112391；GF Josef Hermann Vester）+ elektro-einkaufsfuehrer.de（Gründungsjahr 1980；sales@leunig.de；+49 2242 93389-0）；2026-10-29', 'https://www.firmendatenbanken.de/unternehmen/detail/336211/leunig-gmbh.htm',
    'HRB 1531（Siegburg）；USt DE123112391', '营业中（名录 + 官网）', '1980', 'GmbH', 'KVM / 接口 / 数据线缆 + 工业网络（Moxa 分销）批发', 'Sanddornweg 8b, 53773 Hennef, Nordrhein-Westfalen', '小型 / 中型',
    ['Hermann-J. (Josef Hermann) Vester — Geschäftsführer（名录；无公开邮箱）', '（sales@leunig.de 官网公开邮箱 = 收件人）'],
    '**工业网络分销（Moxa 线）→ 分销 20%：一页纸一次（STI-154GP / STI-288GPM 工业管理 + STI-0240GE 一口价 + MOQ 1 + 付费样机；Moxa 不点名）' + EU + '**；回信即升',
    '分销 20%；P 池候选 ○（德国工业分销 + HRB 坐实）；坐实。')
row('SC-683', 'de', 'VOYGAR SYSTEMS GmbH（voygar.de；**官网 Imprint：Stresemannstr 23, 10963 Berlin；030 65774162；info@voygar.de；自有品牌 VOYGAR 结构化布线系统（SCS）25 年系统质保 + Certified VOYGAR Installer 认证体系（2017-10 起）；ZoomInfo 营收 <$5M、电信设备制造**）；HRB 1 查未得 → 部分坐实；表内：Josef Klaus 工业 1 光 4 电 **54 台**询盘；WA 发不过去', 'DE',
    'DE · 1 次检索：voygar.de/en/support-downloads/imprint（VOYGAR SYSTEMS GmbH, Stresemannstr 23, 10963 Berlin；030 65774162；info@voygar.de）+ warranty 页（25-year SCS warranty；Certified Installer）+ zoominfo（<$5M；+49 3065774162）；2026-10-29', 'http://www.voygar.de/en/support-downloads/imprint',
    '未取（HRB 1 查未得）', '营业中（官网 2026）', '未取（CVI 2017 起）', 'GmbH', '自有品牌结构化布线（铜缆 / 光纤 / 数据中心）+ 有源设备扩展', 'Stresemannstr. 23, 10963 Berlin', '小型（<$5M）',
    ['Josef Klaus — 表内联系人（josef.klaus@voygar.de；54 台询盘）= 收件人', '（info@voygar.de 官网公开邮箱）'],
    '**布线品牌 + 54 台工业机口型 → OEM 30%：一页纸一次（STI-154GP 1 SFP + 4 PoE 工业 / STI-144GP 54 台阶梯价 + VOYGAR 丝印 MOQ + 付费样机）' + EU + '**；回信即升 A 候选',
    'OEM 30%；P 池候选 ★（数量询盘 + 自有品牌）；部分坐实。')

# ---------------- 美国 / 加拿大 ----------------
row('SC-1297', 'us', 'Winncom Technologies Corp（winncom.com；**Tracxn 法人：WINNCOM TECHNOLOGIES CORP（Ohio，1999-12-31 注册，Active）；prospeo：28900 Fountain Parkway, Unit B, Solon, OH 44139；+1 888 946 6266；1996 年创立；101–200 人（Tracxn 160 / 2024 年报 69）；无线 / 宽带 / LTE / CBRS 分销 + 工程**）；表内「实力不错的分销商」；10 次跟进无回复', 'US',
    'US · 1 次检索：prospeo.io/c/winncom-technologies（Solon OH；101-200；Founded 1996）+ tracxn（WINNCOM TECHNOLOGIES CORP；Dec 31, 1999；Active；160 employees）+ signalhire（$1-10M 估；Alex Cernik Head of Strategic Programs & BD）；2026-10-29', 'https://tracxn.com/d/companies/winncomtechnologies/__p_BJX1mRIETKDrtejaZ620uy7lAtkDlCWGp--RK8fIw',
    'Ohio corp（1999-12-31；号未取）', 'Active', '1996（公司注册 1999）', 'Corporation', '无线 / 宽带网络设备分销 + 工程（WISP / ISP 渠道）', '28900 Fountain Parkway, Unit B, Solon, OH 44139, US', '中型（100–160）',
    ['Alex Cernik — Head of Strategic Programs & Business Development（SignalHire；无公开邮箱）', '（sales@winncom.com 表内 = 收件人，请转产品线经理）'],
    '**WISP 渠道分销 → 分销 20%：一页纸一次（STI-280GE / STI-288GPM 工业 PoE + STC-424XGGPM-280W 10G 上联 一口价 + MOQ 1 + 付费样机；FCC）' + US + '**；再无回声 → 观察档',
    '分销 20%；P 池候选 ○（美国分销，体量中等）；坐实（州登记年份 + 地址）。')
row('SC-1443', 'ca', 'Infinique（infinique.com；**官网 about：2002 年安大略创立（Crunchbase 2001-01-01，Mississauga，11–50）；自有品牌视频监控 + 铜缆 / 光纤布线 + 网络交换机 / MC；2008 迪拜区域办公室、2019 印度技术中心；官网 2026-09 在线**）；Ontario 公司号 1 查未得 → 部分坐实；表内：几乎都是 ONV 的、刷了他们的 logo；sales@ 曾退信但域名正常；16 次跟进无回复', 'CA',
    'CA · 1 次检索：infinique.com/about-us（Since 2002；Founded in Ontario；switches and media converters；2026-09）+ crunchbase（Infinique Canada；Mississauga；11-50；Founded 2001）+ multinetfze（Dubai 2008 / India 2019）；2026-10-29', 'https://infinique.com/about-us',
    '未取（Ontario 登记 1 查未得）', '营业中（官网 2026-09）', '2002（Crunchbase 2001）', 'Inc.（推定）', '自有品牌安防 + 布线 + 网络交换机（ONV 贴牌）', 'Mississauga, Ontario（街道未取）', '小型（11–50）',
    ['（sales@ / info@infinique.com 表内；具名 KP 未取 — 一页纸请转采购 / 产品经理）'],
    '**已贴牌 ONV → OEM 30%：换地址一页纸一次（STC-028GP / STC-228GP / STI-154GP 贴牌 + 丝印 MOQ + 付费样机；FCC / IC 口径）' + US + '**；回信即升',
    'OEM 30%；P 池候选 ★（北美现成 OEM 买家）；部分坐实。')
row('SC-1450', 'us', 'MICROLINK NETWORKS LLC / NODEXON 品牌（microlinknet.com / nodexon.com；**公司简介 PDF：独立私营、总部 Houston；品牌 NODEXON（数据网络）、MICROAXS（自动化 2016）、iPARKPRO（智慧停车 2021）；「20+ distributors all over the globe」；nodexon.com 页脚「NODEXON is a brand of MICROLINK NETWORKS LLC, headquarter New York, offices Texas / Virginia」；ZoomInfo：70 E Sunrise Hwy, Valley Stream NY；(646) 851-2555；1994；51–200；$10M；CEO Yaseen Khalid**）；州登记号 1 查未得 → 部分坐实；表内：长飞 / 中科的工业 FS、商业 L3 核心、光配件多；info@ 曾退信但两域名正常', 'US',
    'US · 1 次检索：microlinknet.com/wp-content/uploads/2024/01/Microlink-Company-Profile.pdf（HQ Houston；NODEXON / MICROAXS / iPARKPRO；20+ distributors）+ nodexon.com（brand of MICROLINK NETWORKS LLC；HQ New York）+ zoominfo（70 E Sunrise Hwy Valley Stream NY；1994；51-200；$10M；Yaseen Khalid CEO）；2026-10-29', 'https://nodexon.com/',
    '未取（TX / NY 登记 1 查未得）', '营业中（官网 2026）', '1994', 'LLC', '自有品牌数据网络 / 布线 / 安防 / 自动化（NODEXON 交换机 = 贴牌）', '70 E Sunrise Hwy, Valley Stream, NY（ZoomInfo）/ Houston, TX（简介）', '中型（51–200；$10M）',
    ['Yaseen Khalid — CEO（ZoomInfo；无公开邮箱）', '（info@nodexon.com / info@microlinknet.com 表内 = 收件人，请转产品负责人）'],
    '**自有品牌 NODEXON（已贴牌中国货）→ OEM 30%：换地址一页纸一次（STC-4424GCPM L2+ / STC-424XGGPM-280W 10G 上联 + STI 工业线 贴牌 + 丝印 MOQ + 付费样机；L3 核心不供明说，CENTEC 仅提一句）' + US + '**；回信即升',
    'OEM 30%；P 池候选 ★（美国品牌商 + 20 家分销网）；部分坐实。')
row('SC-2066', 'us', 'EthoSwitch LLC（ethoswitch.com；**官网：New Jersey 总部 2400 Belmar Blvd Unit B20, Wall Township, NJ 07719 + 加州 10401 Venice Blvd #502, Los Angeles；1-800-657-1902；2012 年起自有品牌加固工业交换机 / SFP / 串口服务器 / MC，5 年换新质保；「两个事业部：美国 / 台湾制造 + 中国制造」；BBB of New Jersey**）；NJ 登记号 1 查未得 → 部分坐实；表内：买过台湾 KONTEN 工业 FS「质量不错」（成单）；sales@ 曾退信但域名 MX 正常', 'US',
    'US · 1 次检索：ethoswitch.com（EthoSwitch LLC；NJ + CA 地址；since 2012；products manufactured in China 事业部）+ 产品页（Industrial Unmanaged / PoE+ switches, 5-year warranty）；2026-10-29', 'https://www.ethoswitch.com/',
    '未取（NJ 登记 1 查未得）', '营业中（官网 2026）', '2012', 'LLC', '自有品牌工业以太网交换机 / 光纤产品（部分中国制造）', '2400 Belmar Blvd, Unit B20, Wall Township, NJ 07719, US（加州办事处 Los Angeles）', '小型',
    ['（sales@ethoswitch.com 表内；具名 KP 未取 — 一页纸请转采购 / 产品负责人）'],
    '**品牌商 + 中国制造事业部 + 成单史 → OEM 30%：一页纸一次（STI-054GP / STI-154GP / STI-288GPM 加固工业线 贴牌 + 丝印 MOQ + 付费样机；KONTEN 不点名）' + US + '**；回信即升 A 候选',
    'OEM 30%；P 池候选 ★（美国品牌商 + 成单）；部分坐实。')
row('SC-2598', 'us', 'Digital Watchdog（digital-watchdog.com；**Datanyze：5436 W Crenshaw St, Tampa, FL 33634；1987 年创立；80 人 / $38.9M（Zippia 125 人 / $11M；Adapt 100–250）；CEO HK Lee；President / COO Wade Thomas**）；FL 登记号 1 查未得 → 部分坐实；表内：大型安防品牌、商业 PoE 自有 logo；KP wade@ = President/COO、patrick@；20 次跟进无回复；Simon 曾判不行', 'US',
    'US · 1 次检索：datanyze（5436 W Crenshaw St Tampa FL 33634；$38.9M；80；1987）+ adapt.io（Wade Thomas President / COO；HK Lee CEO；100-250）+ zippia（125；$11M）；2026-10-29', 'https://www.datanyze.com/companies/digital-watchdog/346701354',
    '未取（FL Sunbiz 1 查未得）', '营业中', '1987', 'Inc.（私营）', '自有品牌视频监控（IP / HD over Coax）+ DW 牌 PoE 交换机', '5436 W Crenshaw St, Tampa, FL 33634, US', '中型（80–125；$11–39M）',
    ['Wade Thomas — President / COO（Adapt；wade@digital-watchdog.com 表内）= 收件人', 'HK Lee — CEO（Adapt）', 'Patrick — patrick@digital-watchdog.com（表内）'],
    '**品牌商 → OEM 30%：对 COO 一页纸一次（DW 牌商业 PoE 同口型 STC-028GP / STC-228GP / STC-2224GP / STC-4424GCPM 贴牌 + 丝印彩盒 MOQ + 付费样机；FCC）' + US + '**；Simon 可否决；回信即升',
    'OEM 30%；P 池候选 ★（美国品牌商，体量偏大）；部分坐实；Simon 曾判不行。')
row('SC-292', 'us', 'Fiber Instrument Sales, Inc.（FIS；fiberinstrumentsales.com；**GovTribe / SAM.gov：UEI H7LXDNB9UAY8、CAGE 0CKD9、注册 2001-07-12、有效至 2026-12-30；161 Clear Rd, Oriskany, NY 13424；1985 年创立；51–250 人；$10M–$50M；NAICS 334220 / 335929；prospeo：$53M、101–200；Owner Frank Giotto / Kim Dipierro；Director Strategic Accounts James Fasano**）；表内：大型光纤工具 / 无源分销商、在卖 Signamax 交换机、自有 logo 无源 / MC / CWDM；19 次跟进无回复', 'US',
    'US · 1 次检索：govtribe.com/vendors/fiber-instrument-sales-inc-dot-0ckd9（UEI H7LXDNB9UAY8；CAGE 0CKD9；SAM Active through Dec 30, 2026；161 Clear Rd Oriskany NY；1985）+ prospeo（$53M；101-200；Frank Giotto Owner；James Fasano Director Strategic Accounts）；2026-10-29', 'https://govtribe.com/vendors/fiber-instrument-sales-inc-dot-0ckd9',
    'UEI H7LXDNB9UAY8 / CAGE 0CKD9（NY 公司号未取）', 'Active（SAM.gov 至 2026-12-30）', '1985', 'Inc.（私营）', '光纤工具 / 无源 / 有源分销 + 自有标制造（FIS 品牌）', '161 Clear Road, Oriskany, NY 13424, US', '中型（100–250；$10–53M）',
    ['Frank Giotto — Owner（prospeo；无公开邮箱）', 'James Fasano — Director, Strategic Accounts（prospeo；无公开邮箱）', '（info@fiberinstrumentsales.com 表内 = 收件人，请转有源产品采购）'],
    '**自有标分销 → 分销 20% / 贴标 30% 二选一：一页纸一次（FIS 牌 MC 对标 STC-110XGE $65 + STC-228GP / STI-154GP 贴牌 + MOQ + 付费样机；Signamax 不点名）' + US + '**；再无回声 → 观察档',
    '分销 20%（可升贴标 30%）；P 池候选 ○（美国大型光纤分销）；坐实（SAM.gov）。')

# ---------------- 波兰 ----------------
row('SC-2510', 'pl', 'ELTROX Sp. z o.o.（eltrox.pl / getfort.com；**官网页脚：ul. Warszawska 74, 42-208 Częstochowa；NIP 646 24 90 527；KRS 0000175807；GIOŚ E0008934WZ；aleo（KRS 数据）：REGON 276916481；PZP Ochrona：2003 年起波兰领先安防分销 + 进口商、零售品牌 Eltrox + 批发品牌 Hurton、36 家自营门店 + 52 家合作门店、自有品牌 KENIK / GetFort（摄像机、对讲、网络设备、IT）**）；表内：全国性安防分销、MikroTik Master；Planet 仓 PB-051 评 B（并线）；Simon 曾判不行', 'PL',
    'PL · 1 次检索：eltrox.pl/i/eltrox-strona-korporacyjna-324（ELTROX SP. Z O.O.；NIP 646 24 90 527；KRS 0000175807）+ aleo.com（REGON 276916481；Warszawska 74）+ pzpochrona.pl（2003；36 salonów + 52 partnerskie；marki własne KENIK, GetFort）；2026-10-29', 'https://www.eltrox.pl/i/eltrox-strona-korporacyjna-324',
    'KRS 0000175807；NIP 6462490527；REGON 276916481', '营业中（KRS 存续；官网 2026）', '2003', 'Sp. z o.o.', '安防系统进口 + 分销（零售 Eltrox / 批发 Hurton）+ 自有品牌 KENIK / GetFort 制造', 'ul. Warszawska 74, 42-202 Częstochowa', '大型（36 直营 + 52 合作门店）',
    ['（rodo@eltrox.pl 表内 = GDPR 信箱，不作收件人；总机 +48 34 387 29 92 官网；具名采购 KP 未取 → 先查 Hurton 批发采购）', 'Robert Kosiorek — PZP 联系人（pzpochrona；职务未取）'],
    '**自有品牌 GetFort（网络设备）+ 进口商 → OEM 30%：找到采购 KP 后一页纸一次（GetFort 牌 PoE 同口型 STC-028GP / STC-228GP / STC-2224GP 贴牌 + 丝印彩盒 MOQ + 付费样机；MikroTik 不点名）' + EU + '**；Simon 可否决；与 Planet 仓 PB-051 并线',
    'OEM 30%；P 池候选 ★★（波兰品牌商 + 进口商 + 门店网）；坐实（KRS）；Simon 曾判不行；并线 PB-051。')
row('SC-2516', 'pl', 'AAT SYSTEMY BEZPIECZEŃSTWA sp. z o.o.（aat.pl / novuscctv.com；**aplikuj：KRS 0000838329（注册 2020-04-23 新主体；业务 1993 年起）；Warszawa；201–500 人；安防系统批发领先者、自有品牌 NOVUS / KADE / ZEUS / EVIX；LinkedIn：Handel hurtowy、201–500、1993**）；表内：波兰最大安防分销之一、Novus 工业 FS / PoE 延长器 / SFP；KP Stiepan Sedrakian、Dariusz Rośniak、export@；Simon 曾判不行', 'PL',
    'PL · 1 次检索：aplikuj.pl/pracodawca/19089（KRS 0000838329；sp. z o.o.；wpis 23.04.2020；201–500；marki własne NOVUS, KADE, ZEUS, EVIX）+ linkedin（AAT SYSTEMY BEZPIECZEŃSTWA sp. z o.o.；Warszawa；201-500；1993；Dariusz Mieszkowski Dyrektor Działu Sprzedaży Krajowej）；2026-10-29', 'https://www.aplikuj.pl/pracodawca/19089/aat-systemy-bezpieczenstwa-sp-z-o-o/opinie',
    'KRS 0000838329', '营业中（KRS 2020 新主体存续）', '1993（现主体 2020-04-23）', 'sp. z o.o.', '安防系统批发 + 自有品牌制造（NOVUS CCTV 等 4 品牌）', 'Warszawa, Mazowieckie（街道未取）', '大型（201–500）',
    ['Stiepan Sedrakian — 表内 KP（stiepan.sedrakian@aat.pl）= 收件人', 'Dariusz Rośniak — 表内（dariusz.rosniak@aat.pl）', 'Dariusz Mieszkowski — Dyrektor Działu Sprzedaży Krajowej（LinkedIn；无公开邮箱）', '（export@aat.pl 表内）'],
    '**4 个自有品牌 + 波兰最大批发 → OEM 30%：对 KP 一页纸一次（NOVUS 牌工业 FS / PoE 同口型 STI-154GP / STI-288GPM / STC-228GP 贴牌 + 丝印 MOQ + 付费样机；波兰语备注）' + EU + '**；Simon 可否决；回信即升',
    'OEM 30%；P 池候选 ★（波兰品牌商，体量偏大）；坐实（KRS）；Simon 曾判不行。')

print('b124_c rows written: 21')
