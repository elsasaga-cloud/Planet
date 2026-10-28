#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 97 批 · DE 4 户 + GB 4 户 + PL 4 户（T29-U90 同轮续做，2026-10-28）：一户一查。可重复运行。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put
F = '2026-10-28'
B = 97
CH = 'https://find-and-update.company-information.service.gov.uk/company/'

# ---------------- DE 4 ----------------
put('SB-188', key='de', batch=B, name='Schaltanlagenbau Förderstedt GmbH（saf-slk.de；Seeland OT Hoym，Sachsen-Anhalt）— 低压开关柜 / 控制柜制造商，GF = 研究档 KP', iso='DE', fetched=F,
    source='DE · 1 次检索：saf-slk.de/impressum（Schaltanlagenbau Förderstedt GmbH；Ascherslebener Straße 18d, 06467 Hoym；Amtsgericht Stendal HRB 19446；USt DE289406638；GF Marco Bohne；ppa. Anika Duschka；Handlungsbevollmächtigter Christopher Roder-Rosenov）+ webvalid / implisense（2013-04-17 成立、2013-06-03 登记；资本 €25,000；经营范围：低压开关与控制设备的规划、制造、安装；原址 Güsten → Seeland）+ Northdata（Ralf Otto / Martin Dziersan 已退出 GF；Marco Bohne 由 ppa. 升 GF）+ Kompass（10–19 人）+ Creditreform（1 名股东）',
    url='https://saf-slk.de/impressum/',
    number='Amtsgericht Stendal HRB 19446', status='Active', incorporated='2013-04-17（登记 2013-06-03）', company_type='GmbH（资本 €25,000；单一股东）',
    sic=['27.12 低压 / 中压开关柜、控制柜定制制造 + 能源管理（培训企业）'],
    address='Ascherslebener Straße 18d, 06467 Seeland OT Hoym（研究档旧址 Neue Anlage 2, 39439 Güsten）', accounts='—（小型 GmbH）', accounts_due='—', size_band='小型（10–24 人；≤€10M）',
    officers=['Marco Bohne — Geschäftsführer（= 研究档 KP bohne@ 本人 = 拍板人）', 'Anika Duschka — ppa.（= 研究档 KP duschka@）', 'Christopher Roder-Rosenov — Handlungsbevollmächtigter'], psc='单一股东（姓名未取）', charges='', prev_names=[],
    lines=['**研究档 KP 就是 GF + 授权代表两人**；开关柜里要装 DIN 导轨工业交换机（外采配套）→ **工业 PoE 小口数一条线（STI-054GP / STI-144GP / STI-288DGGPM），集成商 25%**，一页纸直接写 GF',
           '地址更正：Güsten → Seeland OT Hoym（Impressum 2025）；发信窗口 Thu 12–14 CET'],
    notes='')
put('SB-683', key='de', batch=B, name='Spectra GmbH & Co. KG（spectra.de；Reutlingen）— 工业 PC 制造商 + ORing 工业交换机分销，三位股东 GF 之一 = 研究档 KP', iso='DE', fetched=F,
    source='DE · 1 次检索：Creditreform（Spectra GmbH & Co. KG；Amtsgericht Stuttgart HRA 726688；最近变更 2025-08-06）+ industrie-pc.de/Impressum（phG Spectra Verwaltungs-GmbH HRB 738432 Stuttgart；GF Jürgen Rauscher, Klaus Rottmayr）+ companyhouse.de（GF Harald Lang 2011-08-16 起 / Klaus Rottmayr；资本 €500,000；KG 2011-08-16 登记）+ Die Deutsche Wirtschaft（90 人；€23M 估；**Inhaber Lang / Rauscher / Rottmayr**；Mahdenstr. 3, 72768 Reutlingen）+ wer-zu-wem（100 人；€10–50M；1982 创立）+ IHK Reutlingen 2025-08（收购 ICP Deutschland GmbH）+ PresseControl 2025-05（收购 Compmall）+ 站点 Winterthur / Linz',
    url='https://firmeneintrag.creditreform.de/72768/7270311204/SPECTRA_GMBH_CO_KG',
    number='Amtsgericht Stuttgart HRA 726688（Komplementärin Spectra Verwaltungs-GmbH HRB 738432）', status='Active（2025 两起并购）', incorporated='1982（创立）/ 2011-08-16（KG 登记）', company_type='GmbH & Co. KG（股东 = 三位 GF）',
    sic=['26.20 工业 PC / 面板 PC / 机架系统自产 + 工业自动化组件分销（含 ORing 工业交换机）'],
    address='Mahdenstr. 3, 72768 Reutlingen（分部 Winterthur CH / Linz AT）', accounts='€10–50M 营收档（wer-zu-wem）', accounts_due='—', size_band='中型（90–100 人）',
    officers=['Jürgen Rauscher — Geschäftsführer / 股东（= 研究档 KP juergen.rauscher@ 本人 = 拍板人）', 'Harald Lang — Geschäftsführer / 股东', 'Klaus Rottmayr — Geschäftsführer / 股东', 'Harald Behnstedt + Albin Markwardt — Business Development（2025 并购而来）'], psc='Lang / Rauscher / Rottmayr', charges='', prev_names=[],
    lines=['**研究档 KP = 三位老板之一**；在售 ORing 工业交换机（台湾货）→ **工业 PoE 自有标 Spectra = OEM 30% 目标 / 分销 20% 为底**（STI 系列对标 ORing 价格差一截），B BIG',
           '2025 连并两家工业 PC 公司 = 扩品类期 → 一页纸写 Rauscher、抄 vertrieb@ 点名「Produktmanagement Netzwerk」；发信窗口 Thu 12–14 CET'],
    notes='B BIG。')
put('SB-171', key='de', batch=B, name='COMTEK NETWORK SYSTEMS GmbH（comtek-de.com；Mörfelden-Walldorf）— 英国 Comtek（Deeside）德国子公司：网络设备翻新 / 维修 / 二手 = 非品类', iso='DE', fetched=F,
    source='DE · 1 次检索：Northdata（COMTEK NETWORK SYSTEMS GmbH；Amtsgericht Darmstadt HRB 100142（原 Offenbach HRB 40700）；2003-11-11 登记于 Dreieich；2020-02-27 迁 Mörfelden-Walldorf；资本 €25,000；GF Askar Sheibani）+ fusionbase（经营范围：网络设备销售、维修、维护；Nordendstraße 2, 64546 Mörfelden-Walldorf）+ comtek-de.com（USt DE813812023）+ 母公司 Comtek Network Systems (UK) Ltd 05929974（Deeside；1989 Askar Sheibani 创立；PSC Askar + Christine Sheibani；Sales Director Philip Bartlett）',
    url='https://www.northdata.com/COMTEK+NETWORK+SYSTEMS+GmbH,+M%C3%B6rfelden-Walldorf/Amtsgericht+Darmstadt+HRB+100142',
    number='Amtsgericht Darmstadt HRB 100142（母公司 Companies House 05929974）', status='Active', incorporated='2003-11-11', company_type='GmbH（英国 Comtek 集团子公司）',
    sic=['95.12 / 46.52 电信 / 网络设备维修、翻新、二手采购与销售（Cisco 等原厂件）'],
    address='Nordendstraße 2, 64546 Mörfelden-Walldorf', accounts='—', accounts_due='—', size_band='小型（德国分部；集团 Deeside 为主）',
    officers=['Askar Sheibani — Geschäftsführer / 集团 CEO（1951 生；Deeside）', 'Philip John Bartlett — 集团 Sales Director（1977 生）', 'Christine Sheibani — 集团 HR Director / PSC'], psc='Askar + Christine Sheibani（经英国母公司）', charges='', prev_names=[],
    lines=['翻新 / 二手原厂件商 = **不买新品白牌 → 非品类，B 不动、不发**（研究档已写「翻新、维修与二手采购」，本批坐实法人）'],
    notes='不再查。')
put('SB-794', key='de', batch=B, name='Wiesemann & Theis GmbH（wut.de；Wuppertal）— 1979 起的 Web-IO / Com-Server 制造商（W&T），50 人，二代接班', iso='DE', fetched=F,
    source='DE · 1 次检索：wut.de Impressum（Wiesemann & Theis GmbH；Porschestr. 12, 42279 Wuppertal；GF Tobias Theis (M.Eng.)；Amtsgericht Wuppertal HRB 6377；USt DE121008340）+ wut.de 新闻（2024 年初 Rüdiger Theis 近 40 年后把 GF 交给儿子 Tobias Theis；1979 由 Reinhard Wiesemann + Rüdiger Theis 创立；50 人）+ Creditreform（HRB 6377；1 GF + 2 Prokurist；3 名股东；2024-01-05 公告 GF 变更）+ wer-zu-wem（53 人；€10–50M）+ Kompass（资本 €250,001）+ wut.de 联系人 PDF（产品经理 Frank Thiel / Marc Lüppken / Jan Gerdes）',
    url='https://www.wut.de/e-wwwww-im-inde-000.php',
    number='Amtsgericht Wuppertal HRB 6377', status='Active', incorporated='1979', company_type='GmbH（资本 €250,001；Theis 家族 3 名股东）',
    sic=['26.20 网络 I/O（Web-IO）/ Com-Server / USB-Server / 串口转换 / 光纤接口 / 网络技术自研自产（Wuppertal 本地生产）'],
    address='Porschestr. 12, 42279 Wuppertal', accounts='€10–50M 营收档', accounts_due='—', size_band='小型（50–53 人）',
    officers=['Tobias Theis — Geschäftsführer（2024-01 起；二代）', 'Rüdiger Theis — 创始人 / 品牌大使（已卸任 GF）', 'Frank Thiel / Marc Lüppken / Jan Gerdes — Produktmanager（公开邮箱 f.thiel@ / m.lueppken@ / j.gerdes@）'], psc='Theis 家族', charges='', prev_names=[],
    lines=['**准同行**：自研自产网络 I/O 与接口器件、「made in Wuppertal」为卖点，目录里的交换机是补位转售 → 对华南货接受度低 → **只给产品经理一页纸（工业 / 商用 PoE 补位，MC / 光口），不加厚、不投第 2 封**',
           '研究档无 KP → 收件人 Jan Gerdes（SPE / 网络方向产品经理）；发信窗口 Thu 12–14 CET'],
    notes='低概率。')

# ---------------- GB 4 ----------------
put('SB-1031', key='gb', batch=B, name='RALAKDE LTD（findcontrols.com / ralakde.co.uk；Stoke-on-Trent）— 工业自动化备件贸易与维修，一人 PSC', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 09757591（RALAKDE LTD；2015-09-02 注册；Unit 5a Victoria Road, Stoke-On-Trent ST4 2HS；Active；SIC 33120 / 33140 / 33200 / 47421；最近账目至 2025-07-31；下期 2026-07-31 应 2027-04-30 递交）+ officers（Deepak Gupta，1992-06 生，Director 2019-11-06 起，印度籍 / 英国居住；曾 2015–2018 任董事）+ PSC（Deepak Gupta 75%+）+ 关联：RALAKDE AUTOMATION LTD 11435782（2018-06-27；账目应 2026-03-31 → 是否逾期待核）、RALAKDE HOLDINGS LIMITED 16830812（2025-11-04 新设控股）、RALAKDE AUTOMOTIVE LTD 12121820（已注销）+ Endole（1 名股东）',
    url=CH + '09757591',
    number='Companies House 09757591（关联 11435782 / 16830812）', status='Active（2025-11 新设控股公司 = 重组中）', incorporated='2015-09-02', company_type='Private limited company（Deepak Gupta 一人 PSC）',
    sic=['33120 机械维修 / 33140 电气设备维修 / 33200 工业设备安装 / 47421 手机零售（工业自动化备件贸易 + 维修）'],
    address='Unit 5a Victoria Road, Stoke-On-Trent ST4 2HS', accounts='微型 / 小型（2025-07-31 期已递交）', accounts_due='2027-04-30（2026-07-31 期）', size_band='微型（1 名股东；人数未取）',
    officers=['Deepak Gupta — Director / PSC 75%+（= 研究档 KP dgupta@ 本人 = 老板）'], psc='Deepak Gupta', charges='', prev_names=[],
    lines=['备件贸易（停产 PLC / 驱动件）→ 交换机只是顺带 → **分销 20% 一页纸即止（工业 DIN 导轨 STI 系列），不加厚**；老板本人是 KP，直接写',
           '发信窗口 Thu 12–14 GMT'],
    notes='')
put('SB-975', key='gb', batch=B, name='CCTV GLOBAL LONDON LTD（cctv-global.co.uk / cctv-store.co.uk；Chobham, Surrey）— Hikvision / HiLook / Ajax 授权分销，两位创始董事', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 08411023（CCTV GLOBAL LONDON LTD；2013-02-20 注册；Alpha 319, Building K, Chobham Business Centre, Chertsey Road, Chobham, Woking GU24 8JB；Active；2 officers / 0 resignations）+ officers（Iain Robert McNeil，1972-04 生，Director 2013-02-20 起；Gonçalo Filipe Dos Santos Silva，1983-10 生，葡萄牙籍，Director 2013-02-20 起；两人均 PSC）+ LinkedIn（Iain McNeil = Co-founder，负责开发 / 管理 / 运营）+ cctv-global.co.uk（Hikvision / HiLook / AJAX 授权分销，供英国与爱尔兰）+ cctv-store.co.uk 隐私政策（数据控制人 Iain McNeil）',
    url=CH + '08411023',
    number='Companies House 08411023', status='Active', incorporated='2013-02-20', company_type='Private limited company（两位创始人 PSC）',
    sic=['46.52 CCTV / 报警 / 对讲 / 门禁分销（Hikvision / HiLook / Ajax / EZVIZ；站内 Ruijie 交换机）'],
    address='Alpha 319, Building K, Chobham Business Centre, Chertsey Road, Chobham, Woking, Surrey GU24 8JB', accounts='—（小型）', accounts_due='—', size_band='小型',
    officers=['Iain Robert McNeil — Co-founder / Director / PSC（= 研究档 KP imcneil@ 本人）', 'Gonçalo Filipe Dos Santos Silva — Co-founder / Director / PSC'], psc='McNeil + Santos Silva', charges='', prev_names=[],
    lines=['**研究档 KP = 联合创始人本人**；现卖 Ruijie 交换机配 Hikvision → **分销 20%：商用 PoE（STC-028GP / STC-228GP / STC-2224GP）对标 Ruijie 价格直接给到位**，一页纸',
           '发信窗口 Thu 12–14 GMT'],
    notes='')
put('SB-154', key='gb', batch=B, name='WIRE TECHNOLOGIES LIMITED（wire.tech；Cirencester）— 数据中心互连产品自有品牌（光模块 / DAC / 线缆），2026-01 并入 Granity Point Group', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 11576417（WIRE TECHNOLOGIES LIMITED；2018-09-19 注册；Unit 5 Cirencester Business Estate, Esland Place, Love Lane, Cirencester GL7 1YG；Active；2 officers）+ officers（Nathan Brian Barrowclough，1981-04 生，Director 2018-09-19 起；James Edward Brooks，1993-04 生，Director 2021-12-21 起）+ filing history（**2026-01-26 PSC 由 Barrowclough 变更为 Granity Point Group Ltd**）+ Endole（微型：营业额 <£1M、<10 人；2025-09 递交账目）+ Tracxn（2024-09-30 6 人）+ LinkedIn（11–50 人；「UK based manufacturer of data transmission products」；MD Nathan Barrowclough，前 RAF / 皇家海军陆战队）+ Nuvias 2022（英国独家分销）+ BASEC 客户页',
    url=CH + '11576417',
    number='Companies House 11576417（PSC Granity Point Group Ltd，2026-01-26 起）', status='Active', incorporated='2018-09-19', company_type='Private limited company（控股 Granity Point Group）',
    sic=['47910 网络互连产品自有品牌（光模块 / DAC / AOC / MPO / CAT 线 / MC / PDU）设计制造 + 渠道分销（Nuvias）'],
    address='Unit 5 Cirencester Business Estate, Esland Place, Love Lane, Cirencester, Gloucestershire GL7 1YG', accounts='微型（营业额 <£1M）', accounts_due='—', size_band='微型（6–11 人）',
    officers=['Nathan Brian Barrowclough — Managing Director / 创始人（= 研究档 KP nathan@ 本人）', 'James Edward Brooks — Director（= 研究档 KP「James」james@ 本人）'], psc='Granity Point Group Ltd（2026-01-26 起；此前 Barrowclough）', charges='', prev_names=[],
    lines=['**两位研究档 KP = 两位董事本人**；自有品牌 + 走 Nuvias 渠道 → **MC / 光口小交换机贴 Wire 标 = OEM 30% 一条线（STC-110XGE / 光口型号），不碰其光模块 / DAC 主业（Saga 不供）**',
           '2026-01 控股变更 = 刚被收编 / 重组 → 一页纸写 Nathan、抄 James，不加厚；发信窗口 Thu 12–14 GMT'],
    notes='')
put('SB-255', key='gb', batch=B, name='SWITCHTEC LIMITED（switchtec.com；Stone, Staffordshire）— 1982 起的工业电气 / 电子元器件分销，Lester 家族，7,000+ 现货 SKU', iso='GB', fetched=F,
    source='GB · 1 次检索：Companies House 01613368（SWITCHTEC LIMITED；1982-02-12 注册；Brooms Road, Stone Business Park, Stone ST15 0SH；Active；SIC 46520；最近账目至 2025-12-31；下期 2026-12-31 应 2027-09-30 递交；11 officers / 3 resignations）+ officers / companycheck（Jeremy Alan Lester 1977-03 生 Director 2003-11-07 起 = MD；Janet Lester 1947-09 生 Director + Secretary 1991 起；Julia Mary Johnson；Emma Jane Lester；Daniel Adam Kelsall（Technical Sales）；John Plows 1997 起；**Nick Neil Morgan = Sales Director，2024-06-14 起**；创始人 Alan Lester 2020-04-26 退任）+ 关联 SWITCHTEC COMPONENTS LIMITED 02612994 / SWITCHTEC ELECTRONICS LIMITED 05541783（同址）+ Business Live 2022（40 周年；家族经营）+ Stone Town Council 2026-05（J. Lester 申请厂房钢结构扩建）',
    url=CH + '01613368',
    number='Companies House 01613368（关联 02612994 / 05541783）', status='Active（2026-05 申请扩建）', incorporated='1982-02-12', company_type='Private limited company（Lester 家族）',
    sic=['46520 工业电气 / 电子元器件批发（7,000+ 现货；无最小订量）'],
    address='Brooms Road, Stone Business Park, Stone, Staffordshire ST15 0SH', accounts='小型（2025-12-31 期已递交）', accounts_due='2027-09-30（2026-12-31 期）', size_band='小型（11–50 人）',
    officers=['Jeremy Alan Lester — Managing Director / Director（= 研究档 KP；sales@ 公域）', 'Nick Neil Morgan — Sales Director（2024-06-14 起）', 'Daniel Adam Kelsall — Director / Technical Sales', 'Janet Lester — Director / Company Secretary（创始人之妻）', 'Julia Mary Johnson / Emma Jane Lester — Directors（家族）'], psc='Lester 家族', charges='', prev_names=[],
    lines=['工业元器件目录商（DIN 导轨 / 机柜配套）→ **工业 DIN 导轨 PoE 一条线（STI-054GP / STI-144GP / STI-288DGGPM），分销 20%**，一页纸写 MD Jeremy Lester、抄 Sales Director Nick Morgan',
           '2026 扩建 = 扩品类窗口；发信窗口 Thu 12–14 GMT'],
    notes='')

# ---------------- PL 4 ----------------
put('SB-1004', key='pl', batch=B, name='Arpeo Sp. z o.o.（arpeo.pl；Bielsko-Biała）— 电缆穿墙密封 / 线缆导向 / 电工配件网店，2020 新公司', iso='PL', fetched=F,
    source='PL · 1 次检索：arpeo.pl/polityka-prywatnosci（Arpeo Sp. z o.o.；ul. prof. dr. Mieczysława Michałowicza 12, 43-300 Bielsko-Biała；Sąd Rejonowy Bielsko-Biała VIII Wydz. KRS 0000854041；NIP 5472220160；REGON 386724612）+ imsig（2020-08-07 登记；PKD 46.90.Z；aktywna）+ gowork（资本 5,000 zł；Zarząd Artur Łykowski + Radosław Herman）+ infoveriti（股东 Artur Łykowski 1976 生 33 udziały / Paweł Mierzwa 1990 生 33 udziały）+ arpeo.pl（arpeo@arpeo.pl；站内工业以太网交换机 ESN 页）',
    url='https://www.imsig.pl/krs/0000854041',
    number='KRS 0000854041（NIP 5472220160；REGON 386724612）', status='Aktywna', incorporated='2020-08-07', company_type='Sp. z o.o.（资本 5,000 zł；三名小股东）',
    sic=['46.90.Z 电工配件批发网店（穿墙密封 / 金属软管 / 接地夹 / 工业信号灯 + 工业交换机页）'],
    address='ul. prof. dr. Mieczysława Michałowicza 12, 43-300 Bielsko-Biała', accounts='—（微型）', accounts_due='—', size_band='微型',
    officers=['Artur Łykowski — Członek Zarządu / 股东（1976 生）', 'Radosław Herman — Członek Zarządu', 'Paweł Mierzwa — 股东（1990 生）'], psc='Łykowski / Mierzwa / 第三人', charges='', prev_names=[],
    lines=['资本 5,000 zł 的微型配件网店、站内已有工业交换机页（表内「工业电源 5 8 16 电口」）→ **工业非管理 STI 小口数一条线，分销 20% 一页纸即止**，写 arpeo@ 点名 Artur Łykowski',
           '发信窗口 Thu 12–14 CET；不加厚'],
    notes='')
put('SB-441', key='pl', batch=B, name='„METAL UNION” Sp. z o.o.（metalunion.pl；Częstochowa）— 冷弯精密钢型材制造商 = 成单终端用户（€50 光模块）', iso='PL', fetched=F,
    source='PL · 1 次检索：metalunion.pl/kontakt（Metal Union sp. z o.o.；ul. Żyzna 11F, 42-200 Częstochowa；NIP 573-10-21-083；REGON 150090573；Sąd Rejonowy Częstochowa XVII Wydz. KRS 0000138529）+ krs-pobierz（2002-11-15 登记；最近变更 2026-06-30；主业 24.33.Z 冷弯成型制品）+ bizraport（1995-04-26 开业；资本 1,000,500 zł；净利 91 tys zł；「wartość firmy」50 mln 量级）+ aleo（PKD 24.33.Z / 25.12.Z / 25.61.Z 等）+ pkt.pl（1994 创立）+ 官网（1996 起轧辊成型精密型材：卷帘 / 窗帘轨 / 推拉门 / 中空玻璃间隔条）',
    url='https://www.metalunion.pl/kontakt',
    number='KRS 0000138529（NIP 5731021083；REGON 150090573）', status='Aktywna（2026-06-30 有变更）', incorporated='1995-04-26（KRS 2002-11-15）', company_type='Sp. z o.o.（资本 1,000,500 zł）',
    sic=['24.33.Z 冷弯精密钢型材制造（卷帘 / 窗帘 / 推拉门型材、中空玻璃间隔条）'],
    address='ul. Żyzna 11F, 42-200 Częstochowa', accounts='净利 91 tys zł（bizraport 最近期）', accounts_due='—', size_band='中型（制造业；人数未取）',
    officers=['管理层未取（rejestr.io 摘要未展开）；研究档：onet 企业邮箱、WhatsApp 加不上'], psc='未取', charges='', prev_names=[],
    lines=['**研究档谜底**：这是一家钢型材厂的 IT 部门买了 2 个光模块 + 1 个 MC（€50）= 终端用户、非渠道 → **B 保留但不加厚；若发只写一页纸「厂区监控 / 车间网络用商用 PoE + MC」给 IT**',
           '发信窗口 Thu 12–14 CET'],
    notes='终端用户；不追。')
put('SB-942', key='pl', batch=B, name='DMTrade Mikołaj Tomaszewski（dmtrade.pl；Kościan）— 电子 / CCTV / 智能家居网店 + 批发，Cudy 波兰官方分销（个体工商户）', iso='PL', fetched=F,
    source='PL · 1 次检索：dmtrade.pl/pl/contact（DMTrade Mikołaj Tomaszewski；NIP 6981681757；REGON 300138031；Wiśniowa 36, 64-000 Kościan；sklep@dmtrade.pl；BDO 000006055）+ targeo / krs-online（CEIDG 个体；PKD 47.91.Z；2005 起）+ dmtrade.pl 文章（「DMTrade jako oficjalny dystrybutor na Polskę produktów firmy Cudy」）+ b2b.dmtrade.pl（批发端：TV-SAT / DVB-T / 报警 / CCTV / LAN）+ aplikuj（jednostka fizyczna）',
    url='https://www.dmtrade.pl/pl/contact.html',
    number='CEIDG（NIP 6981681757；REGON 300138031）', status='Aktywna', incorporated='2005', company_type='Jednoosobowa działalność gospodarcza（Mikołaj Tomaszewski）',
    sic=['47.91.Z 电子 / RTV / CCTV / 智能家居网店 + B2B 批发（Cudy 官方分销；Spacetronik 等）'],
    address='ul. Wiśniowa 36, 64-000 Kościan', accounts='—', accounts_due='—', size_band='小型（网店 + 批发）',
    officers=['Mikołaj Tomaszewski — 业主（CEIDG）'], psc='Mikołaj Tomaszewski', charges='', prev_names=[],
    lines=['表内「宇航的工业 FS，买的 Cudy 的牌子」= 已经在买深圳品牌 → **分销 20%：商用 PoE + 工业小口数对标 Cudy 价格直接给到位**，一页纸写业主',
           '与 SB-092 Spacetronik（A 候选）有供货关系（站内卖 Spacetronik 电动桌）→ 若 Spacetronik 成线，DMTrade 可作其下游、不单独加厚；发信窗口 Thu 12–14 CET'],
    notes='')
put('SB-784', key='pl', batch=B, name='BCS Sp. z o.o.（原 NSS Sp. z o.o.，2024-10-14 更名；bcs.pl；Warszawa）— 波兰 CCTV 自有品牌 BCS（2008 起）的品牌所有人', iso='PL', fetched=F,
    source='PL · 1 次检索：bcs.pl/gb/content/24-change-of-company-name（2024-10-14 起「NSS Sp. z o.o.」更名「BCS Sp. z o.o.」，NIP / 地址 / 账户不变）+ imsig（NSS SP. Z O.O.；KRS 0000092488；REGON 017161046；NIP 5213124674；2002-02-21 登记；PKD 46.52.Z；ul. Modularna 11, 02-238 Warszawa）+ rejestr.io（Prezes Zarządu Artur Stępowski；资本 50 tys zł）+ nsssecurity.com.pl/o-nas（1998 起进口分销美国报警设备；2008 推出自有 CCTV 品牌 BCS）+ Northdata（LEI 259400J1GBGK8VAOD039；2003 年曾名 N.S.S. Trebor sp. z o.o.）+ 研究档（KP Maciej Sobecki = Project Manager @bcs.pl、Michał Skalecki @bcs.pl；站内 poe 106 / switch 85）',
    url='https://rejestr.io/krs/92488/bcs',
    number='KRS 0000092488（NIP 5213124674；REGON 017161046；LEI 259400J1GBGK8VAOD039）', status='Aktywna（2024-10-14 更名）', incorporated='2002-02-21（业务 1998）', company_type='Sp. z o.o.（资本 50 tys zł）',
    sic=['46.52.Z 安防 / CCTV 进口分销 + 自有品牌 BCS（BCS ECO / LINE / PRO / 含 PoE 交换机）'],
    address='ul. Modularna 11, 02-238 Warszawa', accounts='—（KRS 财报未展开）', accounts_due='—', size_band='中型（波兰 CCTV 知名品牌；人数未取）',
    officers=['Artur Stępowski — Prezes Zarządu（拍板人）', 'Maciej Sobecki — Project Manager（= 研究档 KP m.sobecki@bcs.pl = 产品口）', 'Michał Skalecki — 研究档 KP m.skalecki@bcs.pl'], psc='未取', charges='', prev_names=['NSS Sp. z o.o.（2002–2024）', 'N.S.S. Trebor sp. z o.o.（2003 前）'],
    lines=['**研究档 KP 邮箱是 @bcs.pl = 品牌所有人本尊（非 sklep-bcs.pl 经销店）**；BCS 自有标 PoE 交换机 106 处 = 华南贴牌 → **OEM 30% 首选（PL）、B BIG**：商用 PoE 全系贴 BCS 标，写 Project Manager Maciej Sobecki、点名 Prezes',
           '一个问题：BCS 标 PoE 现供应商交期 / 年量？发信窗口 Thu 12–14 CET；**升 A 候选（回信即 A）**'],
    notes='OEM 首选；A 候选。')

print('b97_de_gb_pl ok')
