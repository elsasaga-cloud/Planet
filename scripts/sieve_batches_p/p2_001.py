#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Planet 仓 · 闸 2 查底数 + 闸 3 入池 批 P2-01（2026-10-29，T29-U120）—— p1_001.py 的 24 户候选。

证据来源：① batch/*.json 既有 facts / evidence（W01–W22 挖掘时已带 URL + 日期）；② 本轮每户最多 1 次 web_search（2026-10-29）。
坐实 = 官方注册号（HRB / KRS / SIREN / CIF / IČO / cégjegyzék / Companies House / Org nr / Y-tunnus / KvK / NIF / 加拿大 Corp No）；
部分坐实 = 官网页脚 + 第三方名录（无注册号）；档位：★ 体量 + 对位 + 登记齐 / ○ 对位 + 登记齐体量一般 / 观察档 = 坐实但微型（试单后转正）。

副作用（幂等）：data/sieve_planet.json；data/saga_clients/P池_巡检表_2026-10-29.csv 追加（备注标「来源：Planet 仓」）；
docs/P池_资产池名册_2026-10-29.md 追加「Planet 仓 并池 · 批 P2-01」小节。
用法：python3 scripts/sieve_batches_p/p2_001.py
"""
import collections
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve_p  # noqa: E402

BATCH = 'P2-01'
DATE = '2026-10-29'
NEXT_CHECK = '2026-12-28'
ROOT = sieve_p.ROOT
WATCH = os.path.join(ROOT, 'data', 'saga_clients', f'P池_巡检表_{DATE}.csv')
ROSTER = os.path.join(ROOT, 'docs', f'P池_资产池名册_{DATE}.md')
CHECK_ITEMS = '官网改版 / 新品 / 招聘 / 社媒（LinkedIn / FB / IG）/ GitHub / 展会出席 / 新闻稿 / 域名 MX 存活 / PLANET 在售款数变化'
G4 = '四主区 + 波兰'
GE = '欧洲其他'

V = {
    # ---------- ★ ----------
    'PA-002': dict(verdict='pool', star='★', group=GE, company='Cartronic Memory S.A.（Cartronic Group）', country='西班牙', links='cartronic.es',
                   reason='★ 官方分销 / VAD 20%：Cartronic Memory S.A.（San Sebastián de los Reyes, Madrid；CIF A81347239；S.A. 1996-01-22 登记（集团自述 1989）；资本 €650,000；10–49 人 / 营收 €10–50M；CNAE 4652 电信元件批发；Administrador único Mario Agreda Ballesteros）坐实；PLANET 西班牙官方分销 + Teltonika / Hanwha VAD；具名 KP Director de marketing y operaciones jmcobo@cartronic.es',
                   facts=[('CIF A81347239 · S.A. · 1996-01-22 · Avenida Fuentenueva 12 · CNAE 4652 · 10–49 人 · €10–50M', 'https://www.infoempresa.com/en-in/en/company/cartronic-memory-sa'),
                          ('资本 650,000 € · Administrador único Agreda Ballesteros Mario', 'https://www.datoscif.es/empresa/cartronic-memory-sa'),
                          ('PLANET Networking 西班牙官方分销页', 'https://cartronic.es/partners-planet-networking/')],
                   tags=['official_dist']),
    'PB-003': dict(verdict='pool', star='★', group=G4, company='Konsorcjum FEN Sp. z o.o.', country='波兰', links='fen.pl | planet.fen.pl',
                   reason='★ 官方分销 20%：Konsorcjum FEN Sp. z o.o.（Poznań ul. Czarnkowska 13；KRS 0000196881，官网页脚）坐实；「Oficjalny Polski Dystrybutor Planet」专站 planet.fen.pl，带测试设备与售前售后；具名 AM bartosz.banaszak@fen.pl + sales@；波兰',
                   facts=[('planet.fen.pl：FEN to Oficjalny Polski Dystrybutor Planet', 'https://planet.fen.pl/'),
                          ('法人登记 KRS 0000196881 + 具名 AM（官网 kontakt）', 'https://fen.pl/kontakt/')],
                   tags=['official_dist']),
    'PA-012': dict(verdict='pool', star='★', group=GE, company='SIR.tel. S.r.l.', country='意大利', links='sirtel.it',
                   reason='★ 授权分销 20%：SIR.tel. S.r.l.（Verona 省；P.IVA 02565900236；1991 年起；营收 €6.67M（2023））坐实；PLANET 授权分销自 2012、价目表 2026 Q1 季更；采购经理 Gioia Mantoan 具名（经 sales@sirtel.it「Attn:」）',
                   facts=[('PLANET 价目表 2026 Q1 更新（现役分销）', 'https://sirtel.it/notizie/aggiornamento-listino-planet-q1-gennaio-2026/'),
                          ('团队具名：CEO / 采购经理 / 技术产品经理 / 销售总监', 'http://sirtel.it/team/'),
                          ('营收 €6.67M（2023）· 1991 · P.IVA 02565900236', 'https://www.reportaziende.it/sirtel_srl_vr')],
                   tags=['official_dist']),
    'PB-018': dict(verdict='pool', star='★', group=GE, company='Power Biztonságtechnikai Kereskedelmi Kft.', country='匈牙利', links='powerbizt.hu | techson.hu',
                   reason='★ 安防批发 20% + 自牌 OEM 30%：Power Biztonságtechnikai Kft.（1031 Budapest Kazal u. 64–66；Cégjegyzékszám 01-09-974579；Adószám 13678144-2-41；LEI 5299001BBFG4OUCAVZ44；2005 年起；2025 净营收 10,401,159 千 Ft ≈ €26M；MD Galambosi Ákos / Banai Miklós）坐实；仅面向安装商 / 经销商的安防批发，自有品牌 Techson；PLANET 48 口 PoE + 工业 PoE 在售；info@ / sales@',
                   facts=[('Impresszum：Cégjegyzékszám 01-09-974579 · Adószám 13678144-2-41 · LEI · 两位 MD', 'https://powerbizt.hu/impresszum'),
                          ('OPTEN：2005 · 净营收 10 401 159 ezer Ft（2025）· 注册资本 5–10 M Ft', 'https://webshop.opten.hu/power-kft-c1309107053.html'),
                          ('Techson 自有品牌站（同一法人 / 税号）', 'https://techson.hu/en/cookie-policy')],
                   tags=['oem_target', 'security_dist']),
    'PA-013': dict(verdict='pool', star='★', group=GE, company='Leteng AS', country='挪威', links='leteng.no',
                   reason='★ AV / IT 增值分销 20%：Leteng AS（Org nr 952 002 872；1984 年起（注册 1995）；21 人（proff.no）；Lagercrantz Group 成员但独立运营、与 PA-009 Direktronik 同集团）坐实；PLANET 厂商页 + PoE 在售 + AV 安装渠道；总经理 Øyvind Jacobsen 直邮 oyvind@leteng.no、销售经理 borgar@',
                   facts=[('batch W-facts：Org nr 952 002 872 · 1984 / 1995 · 21 人 · Lagercrantz Group（proff.no 口径，已记 batch/*.json）', 'https://www.proff.no/')],
                   tags=['group_member']),
    'PB-009': dict(verdict='pool', star='★', group=G4, company='BTS NETWORK GmbH（lwl-shop24.de）', country='德国', links='lwl-shop24.de | planet-technology.de',
                   reason='★ 制造 + 批发 20% / 自牌 OEM 30%：BTS NETWORK GmbH（Erftstadt Albert-Einstein-Ring 2；HRB 45186 Köln；GmbH 2002-06-27（品牌 1999 起）；20+ 人；50,000 产品；光纤产品开发 / 生产 / 贸易，自有品牌；另运营 planet-technology.de 自称 PLANET 分销）坐实；主区 DE；anfrage@，GF 具名',
                   facts=[('HRB 45186 Amtsgericht Köln · Albert-Einstein-Ring 2, 50374 Erftstadt · 电信 / 电子元件批发', 'https://firmeneintrag.creditreform.de/50374/5190612148/BTS_NETWORK_GMBH'),
                          ('1999 成立 · 20+ 员工 · 50,000 产品 · Hersteller + Großhändler（光纤）', 'https://www.lieferanten.de/lieferant-25724-bts-network-gmbh-und-co-kg.html'),
                          ('planet-technology.de：「Ihr PLANET Distributor」（W03 补证）', 'http://planet-technology.de/')],
                   tags=['oem_target']),
    'PB-088': dict(verdict='pool', star='★', group=G4, company='Mills Limited', country='英国', links='millsltd.com',
                   reason='★ 布线 / 电信器材分销 20%：Mills Limited（Companies House 00282704；VAT 227 0825 74；1918 年起家族企业；~60 人；7,000+ 产品；Uxbridge + Amble 两柜台；CityFibre 等 altnet 供应商）坐实；Active Equipment 类目 6 款 PLANET 带价现货 = 唯一交换机线；sales@ + 020 8833 2626，Sales Manager Dil Bhachu 具名',
                   facts=[('batch W-facts：Companies House 00282704 · VAT 227 0825 74 · ~60 人 · 7,000+ 产品（已记 batch/*.json）', 'https://www.millsltd.com/pages/about')],
                   tags=[]),
    # ---------- ○ ----------
    'PA-007': dict(verdict='pool', star='○', group=GE, company='ALARM ABSOLON, spol. s r.o.', country='捷克', links='absolon.cz',
                   reason='○ 安防批发 20%：ALARM ABSOLON, spol. s r.o.（Praha 8 Karlín Březinova 487/9；IČO 44796391；DIČ CZ44796391；1991-12-18 登记 C 6075；25–49 人）坐实；1989 年起捷克安防批发，目录有 PLANET 厂商页 + 多款 PoE；具名 tikovsky@ / kacenova@',
                   facts=[('IČO 44796391 · Březinova 487/9 Praha-Karlín · 25–49 人（RES）', 'https://rejstrik.penize.cz/ares/44796391-alarm-absolon-spol-s-r-o'),
                          ('Městský soud v Praze C 6075 · 1991-12-18 · 活跃', 'https://firmy.euro.cz/subjekt-alarm-absolon-spol-s-r-o-44796391')],
                   tags=['security_dist']),
    'PA-008': dict(verdict='pool', star='○', group=GE, company='Aspectis Informatikai és Biztonságtechnikai Kft.', country='匈牙利', links='aspectis.hu',
                   reason='○ IP 安防 VAD 20%：Aspectis Kft.（H-1158 Budapest Késmárk u. 11–13；Cégjegyzékszám 01-09-722853；Adószám 13106261-2-42；2003 年 Bata Miklós / Laczkó Gábor 创立，IP 视频系统分销先驱）坐实；Axis / Milestone / Hanwha + PLANET 匈牙利分销；总经理 Laczkó Gábor 直邮 gabor.laczko@aspectis.hu',
                   facts=[('官网页脚：Cégjegyzékszám 01-09-722853 · Adószám 13106261-2-42 · 2003 年创立', 'https://aspectis.hu/'),
                          ('Kapcsolat：ügyvezető Laczkó Gábor gabor.laczko@ · 财务 / 物流主管具名', 'https://aspectis.hu/kapcsolat')],
                   tags=['security_dist']),
    'PB-011': dict(verdict='pool', star='○', group=G4, company='ProVu Communications Ltd', country='英国', links='provu.co.uk',
                   reason='○ VoIP / IP 电话分销 20%：ProVu Communications Ltd（Savile Mill, Huddersfield HD3 4PG；Companies House 03748320；1999-04-08 注册；5 董事；2025 现金 £1.04M）坐实；刚引入 PLANET 交换机专页（新品类窗口）；contact@，Sales Manager Joe Walberg 具名；主区 GB',
                   facts=[('Company number 03748320 · 1999-04-08 · Active · 2025 cash £1,040,902', 'https://www.companiesintheuk.co.uk/ltd/provu-communications'),
                          ('PLANET 交换机专页', 'https://www.provu.co.uk/planet-switches.html')],
                   tags=[]),
    'PB-020': dict(verdict='pool', star='○', group=G4, company='Jlinks Technology Corp.', country='加拿大', links='jlinks.com',
                   reason='○ 线缆制造 + 安防 / 网络分销 20%：Jlinks Technology Corp.（Richmond BC 328-13988 Cambie Road 总部 2002 起 + Montreal 分部 2010 起；S.A.E. Cable 独家分销；UL / cUL / CSA 线缆）官网 + 名录部分坐实（BC 公司号未查到 → 补证）；PLANET 多型号在售；sales@，Director Jack Chou 具名；主区 CA',
                   facts=[('About：2002 年起 Greater Vancouver · 2010 Montreal 分部 · S.A.E. Cable 独家分销 · 制造 + 分销', 'https://jlinks.com/about/'),
                          ('Yelp：安防 / 线缆批发 · (604) 207-1662', 'https://www.yelp.ca/biz/jlinks-technology-corp-richmond')],
                   tags=['reg_pending']),
    'PB-033': dict(verdict='pool', star='○', group=G4, company='Hasan Ergen – Ergen Elektronik', country='土耳其', links='ergenelektronik.com',
                   reason='○ 安防 / IT 区域分销 20%：Hasan Ergen – Ergen Elektronik（Antalya Muratpaşa；个体商号；EMIS 记 1994-07-18 设立，名录记 2002-08-13；Zanuo Türkiye 官方分销 + Dahua 在售有库存）部分坐实（个体商号无公司注册号；find.com.tr 页为占位数字不采信）；主区 TR；info@，负责人 Serhat Ergen 具名 → 预付 100% 起步',
                   facts=[('EMIS：Hasan Ergen Ergen Elektronik · Antalya · 1994-07-18', 'https://www.emis.com/php/company-profile/TR/Hasan_Ergen_Ergen_Elektronik_en_4259975.html'),
                          ('官网：zanuo Türkiye – Resmi Distribütörü · Dahua 库存', 'https://www.ergenelektronik.com/urun/32778/DAHUA//sitekural//sitekural/garanti')],
                   tags=['prepay', 'sole_trader']),
    'PB-040': dict(verdict='pool', star='○', group=GE, company='H&V Security B.V.（Alarmsysteemexpert）', country='荷兰', links='alarmsysteemexpert.nl',
                   reason='○ 安防电商 / 安装 20% + 白牌 OEM 30%：H&V Security B.V.（Gorinchem Edisonweg 12；KvK 69433550；bol.com 另记 KvK 57221073 / BTW NL852488282B01 —— 两实体同商号，待统一）坐实；20+ 年安防系统 + 展厅 + 自有支持工程师；自有白牌 PoE 交换机系列（Movok / VK）→ OEM 线索；info@ + WhatsApp 06-83823011',
                   facts=[('About us：H&V Security B.V. · Edisonweg 12 4207 HG Gorinchem · KvK 69433550 · WhatsApp', 'https://alarmsysteemexpert.nl/en/pages/about-us'),
                          ('bol.com 商家信息：KvK 57221073 · BTW NL852488282B01', 'https://www.bol.com/nl/v/alarmsysteemexpert-nl/952936/')],
                   tags=['oem_target']),
    'PC-011': dict(verdict='pool', star='○', group=G4, company='Akçaba Communications（Akçaba Ltd.）', country='北塞浦路斯（随土耳其）', links='akcaba.com',
                   reason='○ 通信集成 + 经销 25%：Akçaba Communications（Lefkoşa Tuna Sok. 4；+90 392 229 15 15；ZoomInfo 11–50 人 / $5.2M；20+ 年光纤 / 布线 / 通信交钥匙，客户含政府 / 酒店 / 学校 / 医院）部分坐实（TRNC 无公开登记）；PLANET 商用 + 工业 PoE 美元标价有库存；info@，联合创始人 Faize Akçaba 具名；T06 随土耳其 → 预付 100% 起步',
                   facts=[('ZoomInfo：11–50 人 · $5.2M · 4 Tuna Sok. Lefkoşa · 光纤 / 布线 / 交钥匙', 'https://www.zoominfo.com/c/akc%CC%A7aba-communications/456053781'),
                          ('官网联系页（北塞浦路斯）', 'https://akcaba.com/en/iletisim/')],
                   tags=['prepay', 'reg_pending']),
    'PB-052': dict(verdict='pool', star='○', group=G4, company='STS Lab, Inc.（dba CCTV.Net）', country='美国', links='cctv.net',
                   reason='○ 独立安防分销 20%：STS Lab, Inc. dba CCTV.Net（16037 Arminta St, Van Nuys CA 91406；2001 年起；82 品牌 dealer-only；D&B 模型营收 $2.61M、principal Boris Bronstein；Cience 估 $10–25M → 体量口径不一）官网 + D&B 部分坐实（CA SoS 实体号未查到 → 补证）；PLANET 为在售交换机主线（1,028 件 + dealer 价目）；sales@ / info@；主区 US；注意 UL / ETL 问法',
                   facts=[('Privacy Policy：STS Lab, Inc. · 16037 Arminta St Van Nuys CA 91406 · info@cctv.net', 'https://cctv.net/privacy-policy'),
                          ('D&B：dba CCTV.net · 营收 $2.61M（modelled）· principal BORIS BRONSTEIN', 'https://www.dnb.com/business-directory/company-profiles.sts_lab_inc.4a1716e0df1ff52b48f6572be02066c4.html')],
                   tags=['reg_pending', 'security_dist']),
    'PB-058': dict(verdict='pool', star='○', group=G4, company='JPF Industries SAS', country='法国', links='jpfidistribution.com',
                   reason='○ 安装商 + 网络配件分销 25%：JPF Industries SAS（22100 Quévert 8 Bd de Préval；SIREN 404 954 125；资本 €380k；1996 起（Groupe Fauché 收购 Ballant 更名）；88–100 人；营收 €11.1M）坐实（pappers）；电气 + 网络安装自有项目消耗 + 网店 PLANET 3 款在售；jpfid@fauche.com；主区 FR；集团子公司但网店自主运营',
                   facts=[('pappers：SIREN 404954125 · SAS · 88–100 人 · 行业代码（已记 batch/*.json）', 'https://www.pappers.fr/entreprise/jpf-industries-404954125')],
                   tags=['group_member']),
    'PB-059': dict(verdict='pool', star='○', group=G4, company='Europ Computer Performance SARL（ECP）', country='法国', links='europ-computer.com',
                   reason='○ IT 进口 / 批发 20%：Europ Computer Performance SARL（93240 Stains ZA La Cerisaie 29 av. Jean Moulin；SIREN 402 225 098 RCS Bobigny；1995-09-10）坐实；自述「importation et distribution」5,000+ SKU / 5,000+ 经销商，官网 PLANET 品牌页自称批发分销；sales@ + +33 1 49 98 98 98；主区 FR；人数 / 营收待补',
                   facts=[('官网 À propos：进口 / 分销定位 · 1995 · 地址与公开邮箱', 'https://www.europ-computer.com/content/1-a-propos'),
                          ('PagesJaunes：SARL · 注册号 402 225 098', 'https://www.pagesjaunes.fr/pros/51310079')],
                   tags=[]),
    'PB-061': dict(verdict='pool', star='○', group=G4, company='Elctron E-commerce Partners Sp. z o.o.（CTR / ctr.pl）', country='波兰', links='ctr.pl',
                   reason='○ CCTV 批发 + 安装 20%：Elctron E-commerce Partners Sp. z o.o.（Warszawa Górczewska 129；KRS 0001031273；NIP 5273052174；2023-04-14 注册，品牌 CTR 自 2008；资本 5,000 zł；64 个合作点；Prezes Marek Andrzej Sołtys）坐实；PLANET 35 款现货 24 h 发货；info@ctr.pl + +48 504 500 007；波兰',
                   facts=[('krs-pobierz：KRS 0001031273 · 注册日 / 资本 / 主营', 'https://krs-pobierz.pl/elctron-e-commerce-partners-spolka-z-ograniczona-odpowiedzialnoscia-i0001031273'),
                          ('官网 kontakt：法人 + CCTV 批发 + 安装 + 64 代表点', 'https://ctr.pl/kontakt')],
                   tags=['security_dist']),
    'PA-016': dict(verdict='pool', star='○', group=G4, company='VOIP24SKLEP.PL Sp. z o.o.', country='波兰', links='voip24sklep.pl',
                   reason='○ VoIP / 网络电商 20%：VOIP24SKLEP.PL Sp. z o.o.（Bydgoszcz；KRS 0000666618；NIP 9671387462；REGON 366697204；2017-03-02；资本 5,000 zł）坐实；PLANET 为交换机主品牌（生产商页 + 自写博客 + 库存）；董事兼大股东 Kryspin Maroszczyk 直邮 k.maroszczyk@ → 决策链最短；波兰；体量小但复购真实',
                   facts=[('官网 Contact-us：KRS 0000666618 · REGON 366697204 · 注册地址', 'https://www.voip24sklep.pl/Contact-us'),
                          ('Nasza firma：董事具名直邮', 'https://www.voip24sklep.pl/nasza-firma')],
                   tags=[]),
    'PB-082': dict(verdict='pool', star='○', group=G4, company='Snugfort Limited（ScreenMoove）', country='英国', links='screenmoove.com',
                   reason='○ 商用 AV / 数字标牌集成 + 网店 25%：Snugfort Limited（England & Wales 12278368；VAT GB 396 2351 74；London EC2A 4NE；2019 起；500+ 企业客户）坐实；PLANET Official Partner，交换机类目 220/270 为 PLANET、IPOE-260 实时库存 168 件 → 真实周转；info@ + support@；主区 GB',
                   facts=[('About us：2019 起 · 500+ 企业客户 · Samsung / LG / iiyama 授权（Companies House 12278368 已记 batch/*.json）', 'https://screenmoove.com/pages/about-us')],
                   tags=[]),
    # ---------- 观察档（坐实但微型） ----------
    'PB-002': dict(verdict='pool_watch', star='☆', group=G4, company='W3CAM SAS', country='法国', links='w3cam.fr',
                   reason='☆ 观察：W3CAM SAS（Lorient；SIREN 483 019 345；NAF 46.43Z 批发；2005 起 SAS 资本 €25k；3–5 人）坐实但微型；PLANET 分销 + 本地库存 + 官方保修（brand/22-planet）；仅 contact@，Président Bertrand Ripoll 具名无直邮 → 试单 / 回访一次后转正或退回',
                   facts=[('data.gouv 年鉴：SIREN 483019345 · NAF 46.43Z · Lorient 在营', 'https://annuaire-entreprises.data.gouv.fr/entreprise/w3cam-483019345'),
                          ('pappers：3–5 人 · 2005 · SAS', 'https://www.pappers.fr/entreprise/w3cam-483019345'),
                          ('PLANET 品牌页：本地库存 + 官方保修', 'https://www.w3cam.fr/brand/22-planet')],
                   tags=['micro']),
    'PA-010': dict(verdict='pool_watch', star='☆', group=G4, company='iOC Tech Inc.', country='加拿大', links='ioctech.ca | store.ioctech.ca',
                   reason='☆ 观察：iOC Tech Inc.（Markham ON；CBCA 公司号 8441189，BN 827795733RC0001，2013-02-20 注册，4 董事，Active；1–10 人）坐实但微型；工业以太网分销 + 定制线缆，自述 PLANET 加拿大授权分销（旧页 404，现 store.ioctech.ca）；sales@，Director Lloyd Raskina 具名；主区 CA → 试单后转正',
                   facts=[('Canada company registry：Corp No 8441189 · BN 827795733RC0001 · 2013-02-20 · Active · 4 directors', 'https://www.canadacompanyregistry.com/companies/ioc-tech-inc/'),
                          ('Crunchbase：Markham · 1–10 人 · sales@ioctech.ca', 'https://www.crunchbase.com/organization/ioc-tech')],
                   tags=['micro']),
    'PB-025': dict(verdict='pool_watch', star='☆', group=GE, company='Microdata Finland Oy', country='芬兰', links='microdata.fi',
                   reason='☆ 观察：Microdata Finland Oy（Vantaa Robert Huberin tie 2；Y-tunnus 2049377-0；2006-07-27；NACE 46510；2025 营收 €1.5M、5 人、营业利润率 15.7%；TJ Juha-Matti Joutkoski）坐实但微型；电信 / 网络批发面向经销商，PLANET PoE 在售；myynti@ + 具名 aki.jarvinen@ → 试单后转正',
                   facts=[('proff.fi：Y-tunnus 2049377-0 · 营收 1,5 MEUR（2025）· 5 人 · TJ Joutkoski Juha-Matti', 'https://www.proff.fi/yrityksen/microdata-finland-oy/vantaa/tietokoneet-tietokonelaitteet-ja-ohjelmistot-%E2%80%93-tukkukauppa/2049377-0I10ML'),
                          ('finder.fi：2006-07-27 · Osakeyhtiö · Vantaa', 'https://www.finder.fi/Verkkoj%C3%A4rjestelm%C3%A4t+tietoliikennej%C3%A4rjestelm%C3%A4t/Microdata+Finland+Oy/Vantaa/yhteystiedot/962136')],
                   tags=['micro']),
    'PB-049': dict(verdict='pool_watch', star='☆', group=GE, company='Intermédia – Informática, Lda', country='葡萄牙', links='intermedia.pt',
                   reason='☆ 观察：Intermédia – Informática, Lda（Coimbra Rua Dom Ernesto Sena de Oliveira Lote 1；NIF 503329827；主营电信设备）坐实但微型（Lda，人数未公开）；官网 PLANET 专页全系带价（含 L3 PoE 与 IGS-6325 工业线）= 真实备货经销；info@ / compras@（采购信箱）→ 试单后转正',
                   facts=[('iberinform：法人 / 地址 / 官网一致', 'https://www.iberinform.pt/empresa/22087434/intermedia-informatica-lda'),
                          ('racius：主营电信设备', 'https://www.racius.com/intermedia-informatica-lda/')],
                   tags=['micro']),
}


def main():
    sieve = sieve_p.load_sieve()
    recs = {r['code']: r for r in sieve_p.load_planet()}
    for code, v in V.items():
        assert code in recs, code
        cur = sieve.get(code) or {}
        assert cur.get('batch') in ('P1-01', BATCH), (code, cur.get('batch'))
        row = {'verdict': v['verdict'], 'gate': 3 if v['verdict'] in ('pool', 'pool_watch') else 2,
               'rule': 'G3' if v['verdict'] in ('pool', 'pool_watch') else 'G2', 'reason': v['reason'], 'date': DATE, 'manual': True,
               'origin': 'Planet', 'grade': recs[code]['grade'], 'batch': BATCH, 'star': v['star'],
               'facts': [{'what': w, 'url': u, 'date': DATE} for w, u in v['facts']]}
        if v.get('tags'):
            row['tags'] = v['tags']
        sieve[code] = row
    cnt = sieve_p.save_sieve(sieve)

    with open(WATCH, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f))
    header, body = rows[0], rows[1:]
    have = {r[0] for r in body}
    added = 0
    for code, v in V.items():
        if v['verdict'] not in ('pool', 'pool_watch') or code in have:
            continue
        body.append([code, v['star'], '正式' if v['verdict'] == 'pool' else '观察', v['company'], v['country'], v['group'], v['links'],
                     '、'.join(v.get('tags') or []), DATE, NEXT_CHECK, CHECK_ITEMS, f'来源：Planet 仓（profile/{code[1]}/，原档 {recs[code]["grade"]}）；{v["reason"][:160]}'])
        added += 1
    with open(WATCH, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(body)

    marker = f'## Planet 仓 并池 · 批 {BATCH}'
    md = open(ROSTER, encoding='utf-8').read()
    if marker not in md:
        pools = [(c, v) for c, v in V.items() if v['verdict'] == 'pool']
        watch = [(c, v) for c, v in V.items() if v['verdict'] == 'pool_watch']
        lines = ['', marker + f'（{DATE}，正式 {len(pools)} / 观察 {len(watch)}）', '',
                 f'> 来源：Planet 仓（`profile/A|B|C/`，主表 `data/客户名单_Planet渠道_2026-10.csv`，`data/sieve_planet.json`）。129 户三闸走完：并档随 Saga / External 主档 79（其中随 Saga P 池 6）/ 永久 pass 1 / 巨头留 C 2 / 闸 1 留原档 23 / **本批入池 {len(pools)}（★ {sum(1 for _, v in pools if v["star"] == "★")} / ○ {sum(1 for _, v in pools if v["star"] == "○")}）+ 观察 {len(watch)}**。巡检同表 `data/saga_clients/P池_巡检表_{DATE}.csv`，下次 {NEXT_CHECK}。',
                 '', '| 编号 | 档 | 公司 | 国家 | 区域组 | 原档 | 判语（摘） |', '|---|---|---|---|---|---|---|']
        for c, v in pools + watch:
            lines.append(f'| {c} | {v["star"]} | {v["company"]} | {v["country"]} | {v["group"]} | Planet {recs[c]["grade"]} | {v["reason"][:140].replace("|", "｜")}… |')
        lines.append('')
        open(ROSTER, 'a', encoding='utf-8').write('\n'.join(lines))
    print(BATCH, dict(collections.Counter(v['verdict'] + v['star'] for v in V.values())), 'watch+', added, dict(cnt))


if __name__ == '__main__':
    main()
