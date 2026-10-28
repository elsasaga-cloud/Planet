#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 94 批（T29-U89，公司底数第十二轮 · B 档「筛=1」主战场五国 22 户 + 补项 3）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=94 行）。
结构同 batch93_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批定性：同行 4（SB-207 Contemporary Controls / SB-205 barox / SB-152 Pulsar / SB-762 Ground Control 非品类）→ 不动；并线 1（SB-273 Eretekne → SB-867 Erete）；推定并线 1（SB-906 Avizio → SB-445 AICOM，待一次直查）。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 94 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US ----------
    'SB-098': [{'kp_match': 'paguilera@nexxtsolutions.com', 'role': '研究档 KP（职务未取；Nexxt 产品 / 采购部在迈阿密）= 首收件人' + TAG},
               {'kp_match': 'lgarcia@nexxtsolutions.com', 'role': '研究档 KP（职务未取）= 抄送' + TAG},
               {'facts': {'legal_name': 'Nexxt Solutions（Intcomex, Inc.（Delaware）旗下自有品牌 / 事业部；FL 实体号未取）', 'founded': '2006（品牌；母公司 Intcomex 1988/89 Shalom 父子创立）' + TAG, 'staff': 'Nexxt 51–500 人；Intcomex 集团 ≈2,600 人（第三方）', 'hq': '3505 NW 107th Ave, Miami (Doral), FL 33178',
                          'other': '第 94 批：Intcomex 自有品牌 = 典型贴牌商用 PoE 买家 → OEM 30%，但集团采购比价、量大 → B BIG；市场在拉美，买家在美国' + TAG}}],
    'SB-1114': [{'kp_match': 'cfikes@fikesmedia.com', 'role': 'Owner（2007–；同时任 Evadale ISD 信息技术主任 2018– + 兼职教授）= 一人副业老板' + TAG},
                {'facts': {'legal_name': 'FikesMedia LLC（德州；TX 登记号未取；镜像显示旧登记 inactive）', 'founded': '2007' + TAG, 'staff': '1 人（副业）', 'hq': '105 George St, Silsbee, TX 77656',
                           'other': '第 94 批：MikroTik 转售副业、老板全职在学区 → 分销 20% 一页纸，不投第 2 封；若回信问的是学区项目' + TAG}}],
    'SB-951': {'add_kp': {'name': 'Cody Gordon', 'role': 'President / Founder / Member（Montana SoS C1022717 登记代理人；BBB Member）= 老板 = 拍板人（邮箱未公开 → 官网表单 / sales@ 点名）' + TAG, 'email': '', 'phone': '', 'source': 'https://opencorporates.com/companies/us_mt/C1022717'},
               'facts': {'legal_name': 'Montavue LLC（Montana Domestic LLC；SoS C1022717；Active Good Standing；商标 MONTAVUE 2017-05-17）', 'founded': '2016-09-19（BBB）/ 2017（品牌）' + TAG, 'staff': '9–16 人；$5M 级（第三方）', 'hq': '5707 W Harrier Dr, Missoula, MT 59808',
                         'other': '第 94 批：自有品牌相机 / NVR + 只有一款自标工业 PoE → OEM 30% 首选：商用 PoE 全系贴 Montavue 标；研究档曾记 Lacey WA 为误，实为 Missoula MT' + TAG}},
    'SB-959': {'add_kp': {'name': 'Ben（姓未取）', 'role': 'Google Play 开发者账户联系人 ben@silarius.com（职务未取；疑为老板）= 收件人' + TAG, 'email': 'ben@silarius.com', 'phone': '', 'source': 'https://play.google.com/store/apps/details?id=com.silarius.app'},
               'facts': {'legal_name': 'Silarius LLC（New York LLC；登记号未取；BBB 成立 2019-03-25）', 'founded': '2019-03-25（LLC）；业务自称 2008' + TAG, 'staff': '2–10 人', 'hq': '1033 US Highway 46, Suite 204, Clifton, NJ 07013（登记地 155 Water St, Brooklyn, NY 11201）',
                         'other': '第 94 批：23 万 SKU 代销网店 + 自有品牌 Silarius 打「NDAA 合规」旗号（我方禁词，不配合）→ 只做商用 PoE 贴标一条线 OEM 30%；微型' + TAG}},
    'SB-408': [{'kp_match': 'sales@xblue.com', 'name': 'Paul Falanga', 'role': 'VP Product Development（NENA 登记联系人）= 产品 / 选型人 = 首收件人' + TAG},
               {'kp_name': 'Larry Steinmetz', 'role': 'Founder & President（2005 创立；Crunchbase / contactout）= 老板 = 抄送' + TAG},
               {'add_kp': {'name': 'Paul Lynch', 'role': 'Vice President, Product Development（contactout / ZoomInfo）= 产品口（与 Paul Falanga 并列）' + TAG, 'email': '', 'phone': '', 'source': 'https://contactout.com/company/XBLUE-Networks-51822'},
                'facts': {'legal_name': 'XBLUE Networks, LLC（Crunchbase 法定名；AZ 登记号未取）', 'founded': '2005' + TAG, 'staff': '11–14 人；$2M 级（第三方）', 'hq': '20801 N. 19th Ave, Suite 2 & 3, Phoenix, AZ 85027（旧址 Lenexa KS）',
                          'other': '第 94 批：自有品牌小企业电话系统经零售 / 电商销售；研究档「PoE = ONV 去 logo」= 已贴标 → OEM 30%：8 口 PoE 电话机配套，注明中性包装 + FCC' + TAG}}],
    'SB-351': [{'kp_match': 'jason@enetusa.com', 'name': 'Jason Barrette', 'role': 'President（growjo；原 ENET Components VP Sales）= 拍板层（2023-12 后归 NSI 集团）' + TAG},
               {'kp_match': 'sales@enetusa.com', 'role': '销售公域（研究档）' + TAG},
               {'facts': {'legal_name': 'ENET Solutions, Inc.（加州；2023-12-12 起为 NSI Industries, LLC（Huntersville NC）子公司 / 品牌；曾名 ENET Components, Inc.）', 'founded': '2003（Chris Brock 创立）' + TAG, 'staff': '27–30+ 人；$10M 级', 'hq': '75 Argonaut, Suite B, Aliso Viejo, CA 92656',
                          'other': '第 94 批：主品类 SFP / DAC / 内存（Saga 不供）；研究档「MC 自己的 logo」→ 只剩 MC 贴标一条线 OEM 30%，且已并入 NSI 集团采购 → 低概率，一页纸即止' + TAG}}],
    'SB-150': {'facts': {'other': '第 94 批：nexxus.cc 一次直查 → 站活（2025-03 更新）、自有标「3-Port Gigabit PoE Switch」+ 交换 / Wi-Fi / UC / 防火墙 / 存储方案商；与 nexxusnetworks.com 不是同一家；站无 Impressum → 永久「底数不可查」，OEM 30% 一页纸照发' + TAG}},
    # ---------- TR ----------
    'SB-273': {'facts': {'legal_name': 'Erete Bilgi Sistemleri Dış Tic. ve San. Ltd. Şti.（eretekne.com = Erete 的 B2B 网店；VKN 3540201016 Mecidiyeköy V.D.）= **与 SB-867 Erete 同一法人 → 并线 SB-867**', 'founded': '2001-12（Erete）' + TAG, 'staff': '小型（同 SB-867）', 'hq': '19 Mayıs Mah. Güven Sk. No:4/2, Şişli, İstanbul',
                         'other': '第 94 批：Erete = Edge-Core（Accton）+ Etherwan + Fluke 土耳其分销商（卖竞品）；B2B 负责人 Pınar Kabil（创始合伙人）；只跟 SB-867 一线，不加厚' + TAG}},
    'SB-653': {'facts': {'legal_name': 'Coredata Telekom A.Ş.（MERSİS / 商会号未取）', 'founded': '未取' + TAG, 'staff': '微型–小型（未取）', 'hq': 'Hamidiye Mah. Alp Sk. C Blok Apt. No:4/C/2, Kağıthane, İstanbul',
                         'other': '第 94 批：原 Plesk 默认页已换正式站（2026）但无人名 / 产品页 → 身份只到「伊斯坦布尔小电信 / 集成商」；写 satis@coredata.com.tr 一封分销 20%，不加厚' + TAG}},
    'SB-575': {'facts': {'other': '第 94 批：底数 1 次检索未命中（名片户、仅 WhatsApp）→ 标「底数不可查（名片户）」，不再查' + TAG}},
    'SB-323': {'facts': {'other': '第 94 批：底数 1 次检索未命中（gmail 名片户；同名陷阱：美国 D&N Electric、安卡拉 Doğan Mühendislik）→ 标「底数不可查（名片户）」，不再查' + TAG}},
    # ---------- GB ----------
    'SB-342': {'add_kp': {'name': 'Stephanie Lorraine Kirton', 'role': 'Director / Finance Director（2023-11-23 任；Companies House 04863038）= 现任董事中任期最长者；另两位董事 Louis Max Fitzsimmons / Edwyn Owen Thomas 2025-06-29 新任 = 换手期（邮箱未公开 → sales@ 点名）' + TAG, 'email': '', 'phone': '', 'source': CH + '04863038/officers'},
               'facts': {'legal_name': 'SURE24 LIMITED（Companies House 04863038；曾名 BATTANCO LIMITED → 2003-11-11；SIC 32990）', 'founded': '2003-08-11（SURE Group 1992 起）' + TAG, 'staff': '29 人；总资产 £2.11M / 负债 £1.33M（Endole；Small）', 'hq': 'Sure House, 2 Moorbridge Court, Moorbridge Road East, Bingham, Nottinghamshire, NG13 8GG',
                         'other': '第 94 批：隐蔽 / 警用 CCTV 设计制造分销；2023–2025 董事会整体换血 = 进门时机；只推商用 PoE + 工业小口数，先款后货' + TAG}},
    'SB-762': [{'kp_match': 'scotty.thibodeaux@groundcontrol.com', 'role': 'IoT Solution Architect（美国路易斯安那 Scott；RocketReach）= 美方技术，不管采购' + TAG},
               {'facts': {'legal_name': 'Ground Control Technologies UK Ltd（formerly Wireless Innovation Ltd；控股 Ground Control Technologies Holdings Ltd 10888253；美国 Ground Control Systems, Las Vegas NV）— 2025-10 起为法国 CLS Group（CNES 子公司）全资', 'founded': '2002（三家合并：美国 Ground Control 2000 + Wireless Innovation + Rock Seven）' + TAG, 'staff': '中型（集团 ≈100+；母公司 CLS 1,100 人）', 'hq': 'Unit D2, Churcham Business Park, Churcham, Gloucestershire, GL2 8AX',
                          'other': '第 94 批：卫星 IoT 设备商，PoE 只是配套（注入器 / 小交换机）→ 非品类 + 2025-10 集团化 → 不再补查、不再发（B 不动）' + TAG}}],
    'SB-856': [{'kp_match': 'martin@o-tc.co.uk', 'name': 'Martin Omond-Tong', 'role': '创办人（2012；Eplan 电气设计咨询；董事身份推定）= 老板；Pamela Omond-Tong Director 2015-05-15 任（Companies House 08154404）' + TAG},
               {'facts': {'legal_name': 'OMOND-TONG CONSULTANCY LTD（Companies House 08154404；t/a O-TC Ltd）', 'founded': '2012-07-24' + TAG, 'staff': '微型（夫妻公司）', 'hq': '4 Wentworth Way, Woodhall Spa, Lincolnshire, LN10 6PG',
                          'other': '第 94 批：两人电气设计咨询、买工业 MC 配自动化项目；自述已有中国 / 台湾 IoT 伙伴 → 小项目集成商 25%，量极小，不投第 2 封' + TAG}}],
    'SB-724': [{'kp_match': 'justin@comms-express.com', 'name': 'Justin Ellis', 'role': 'Director / Managing Director（2019-03-01 任；1972-03 生；Companies House 04359914；兼 Comms Capital Holdings Ltd 董事 = 控股方）= **老板 = 拍板人 = 研究档 KP 本人**' + TAG},
               {'facts': {'legal_name': 'COMMS EXPRESS LIMITED（Companies House 04359914；SIC 46510；VAT 787 391279；Comms Capital Holdings Ltd 100% 控股（2020-07 MBO 结构））', 'founded': '2002-01-24' + TAG, 'staff': '22–40 人；turnover £20.7m（Pomanda）', 'hq': '7 Grafton Place, Dukes Park Industrial Estate, Chelmsford, Essex, CM2 6TG',
                          'other': '第 94 批：£20M IT / 网络电商平台、MD 本人即 KP → 分销 20%：上架 SmartByte 品牌（不谈贴标），价格先行；发信 Thu 12–14 GMT' + TAG}}],
    # ---------- DE ----------
    'SB-207': {'facts': {'legal_name': 'Contemporary Controls GmbH（Amtsgericht Leipzig HRB 24731；曾 Stendal HRB 214009；USt DE220664517；美国 Contemporary Controls Systems, Inc.（Downers Grove IL）100% 子公司）', 'founded': '2006-10（Eisleben 登记；2009-02 迁 Leipzig）' + TAG, 'staff': '德国分部 ≤20 人（母公司 ≈100）', 'hq': 'Fuggerstraße 1 B, 04158 Leipzig',
                         'other': '第 94 批：GF George M. Thomas = 美国母公司创始人；自有品牌工业交换机 / MC（CTRLink）+ BACnet 路由器制造商 = **同行** → 守界：不发价格表、不加厚、B 不动' + TAG}},
    'SB-208': {'add_kp': {'name': 'Ahmad Ebrahimi', 'role': 'Dipl.-Ing.；Geschäftsführer / 创始人（1992）/ 所有者（HRB 45788 B Charlottenburg；GF 登记 2004-10-14–）= 老板；Azar Bayegi Geschäftsführerin 2020-02-06–（采购在台北分公司，邮箱未取 → info@delock.de）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.delock.de/impressum/index.html'},
               'facts': {'legal_name': 'TRAGANT Handels- und Beteiligungsgesellschaft mbH（Delock / Navilock 品牌；AG Charlottenburg HRB 45788 B；LEI 391200S2D0IEA0LPEV63；USt DE156330245）', 'founded': '1992（创立）/ 2004-10-14（现登记）' + TAG, 'staff': '67–84 人；营收 €26M（2017）/ €10–50M；资产负债表 €28.4M（2023）', 'hq': 'Beeskowdamm 13/15, 14167 Berlin（台北分公司 2005 起）',
                         'other': '第 94 批：自有品牌 Delock IT 配件 / MC / SFP 进口分销 25 国、台北采购 → B BIG、OEM 30% 低概率；一页纸 MC + 小口数 PoE 即止' + TAG}},
    'SB-846': {'add_kp': {'name': 'Karin Scheer', 'role': 'Geschäftsführerin（einzelvertretungsberechtigt；*1984 Braunsbedra；AG Leipzig HRB 37030）= 老板 = 唯一联系人（qcone@ueberwachung.tv，Impressum 公域）' + TAG, 'email': 'qcone@ueberwachung.tv', 'phone': '', 'source': 'https://firmeneintrag.creditreform.de/04357/8190890687/QUALICAM_GMBH'},
               'facts': {'legal_name': 'Qualicam GmbH Sicherheitstechnik + Reizgasanlagen（AG Leipzig HRB 37030；USt DE298501143；WEEE DE 27008620；前身 Qualicom）', 'founded': '2015-01-15（GmbH；业务 2000 起、2012 起自产刺激气体报警装置）' + TAG, 'staff': '微型（1 GF；≤5 人）', 'hq': 'Volbedingstraße 2, 04357 Leipzig（经营地 Braunsbedra）',
                         'other': '第 94 批：一人 GmbH 安防网店 + 自产防盗气体装置，PoE 只是相机套装配件 → 分销 20% 小量，一封即止' + TAG}},
    'SB-205': [{'kp_match': 'mail@barox.de', 'name': 'Jeneeben Jesujeevagan', 'role': 'Head of Engineering（barox.ch 团队页；+41 56 511 10 41）= 产品 / 工程口 —— 研究档「revive 只有找到产品 / 采购负责人」对应的人；但 barox 为同行（自有品牌视频交换机制造商），默认不动' + TAG},
               {'kp_match': 'rohr.rudolf@barox.ch', 'name': 'Rudolf Rohr', 'role': 'Geschäftsführer / 创始人（1998-09-01 与 Angelo Banfi 共同创立；barox Kommunikation AG CEO；GmbH HRB 413457 Freiburg / 3457 Lörrach）= 老板' + TAG},
               {'facts': {'founded': '1998-09-01（AG）；GmbH 登记日未取' + TAG, 'staff': '≈15 人（barox.ch 团队页 2026-07；两地 Baden-Dättwil / Lörrach）', 'hq': 'Weiler Strasse 7, 79540 Lörrach（母公司 Im Grund 15, CH-5405 Baden-Dättwil）',
                          'other': '第 94 批：GF Angelo Banfi + Rudolf Rohr；LEI 549300UCXE39G2ZNV027；自有品牌视频 / 安防交换机 + MC 制造商 = **同行** → 守界：不发价格表、不加厚（2024 问价后拒样 + 退信已证）' + TAG}}],
    'SB-090': {'facts': {'legal_name': 'Adler Elreha GmbH（Amtsgericht Mannheim **HRB 724419**；EUID DEB8535.HRB724419；资本 €25,000；股东 EL RE HA Elektronische Regelungen GmbH（HRB 420487，Hamadeh 家族）等；GF Sachir Kamel Ajlouni（Clearwater FL）；Zhongjian Wei（深圳）曾任 GF / 持股）', 'founded': '2016-03-15（登记；合同 2015-12-02）' + TAG,
                         'other': '第 94 批：Northdata 直页补齐 HRB；股东含深圳人士 = 已有华南直采 / 合资渠道 → OEM 30% 判断降为低概率，一页纸即止；2025-11-28 新股东名单 = 股权在动' + TAG}},
    # ---------- PL ----------
    'SB-585': {'facts': {'legal_name': 'VIDOS Sp. z o.o.（KRS 0000857683 · NIP 5342626018 · REGON 386943260；资本 5,000 zł；前身 Reguły 主体 NIP 7281209711）', 'founded': '2020-09-03（KRS；品牌业务更早）' + TAG, 'staff': '小型（未取）', 'hq': 'ul. Sokołowska 44, 05-806 Sokołów k/Warszawy',
                         'other': '第 94 批：自有品牌视频对讲 / 门禁「Producent」+ 已有自标 PoE → OEM 30%：4 / 8 口 PoE 贴 Vidos 标；zarząd 未取；同名陷阱 vidos-domofony.pl（KRS 0000857651）/ vidos-sklep.pl（PPHU HERZ）为经销商' + TAG}},
    'SB-906': {'facts': {'other': '第 94 批：底数 1 次检索未命中；侧证 lan-cctv.pl（AICOM 网店）页脚「AICOM · KRS 0000654397 · NIP 6782913975」→ Avizio 疑为 SB-445 AICOM（Kraków）自有品牌（推定）→ 下轮一次直查 avizio.pl Impressum 即可定并线' + TAG}},
    'SB-1046': {'facts': {'legal_name': 'VOLTA Sp. z o.o.（ivolta.pl 为其网店品牌；KRS 0000023698 · NIP 5211367444 · REGON 010829096；资本 1,020,000 PLN；BDO 000051577）', 'founded': '2001-06-28（KRS；业务 1986 起）' + TAG, 'staff': '70+ 人、华沙总部 + 10 分部；营收 2025 90.85 mln zł（2024 83.30 / 2023 83.19）；资产 30.4 mln', 'hq': 'ul. Jutrzenki 94, 02-230 Warszawa',
                          'other': '第 94 批：Satel / Hikvision / Dahua 授权分销 = 波兰安防分销 Top 级 → B BIG，分销 20% 上架 SmartByte，不谈贴标；已有 PoE 供应（Utepo 等）→ 只谈第二供应 + 现货期；zarząd 未取' + TAG}},
    'SB-152': {'facts': {'legal_name': 'Pulsar（pulsar.pl；Siechnice；法定主体名 / KRS 未取 —— 同名陷阱：PULSAR Sp. z o.o. KRS 0000262594（卡托维兹，营收 76 万 zł）是另一家）', 'staff': '中型（8,000 m² 厂区）', 'hq': 'Siechnice（Wrocław 附近）',
                         'other': '第 94 批：自产安防电源 + PoE 交换机（S64 / S108 / SG32 / ISFG108）= **同行** → 守界：不发价格表、不加厚、B 不动' + TAG}},
}


def apply(d, u):
    kps = d.get('kp') or []
    if u.get('kp_match'):
        for k in kps:
            if u['kp_match'] in (k.get('email') or ''):
                if u.get('name') and not k.get('name'):
                    k['name'] = u['name']
                if u.get('name') and k.get('name') and k.get('name') != u['name'] and TAG not in (k.get('role') or ''):
                    k['name'] = u['name']
                if u.get('role') and TAG not in (k.get('role') or ''):
                    k['role'] = u['role']
    if u.get('kp_name'):
        for k in kps:
            if (k.get('name') or '') == u['kp_name'] and TAG not in (k.get('role') or ''):
                k['role'] = u['role']
    if u.get('add_kp') and not any(u['add_kp']['name'] == (k.get('name') or '') for k in kps):
        kps.append(u['add_kp'])
    seen, dedup = set(), []
    for k in kps:
        key = (k.get('name'), k.get('email'), k.get('role') or k.get('title'))
        if key in seen:
            continue
        seen.add(key); dedup.append(k)
    d['kp'] = dedup
    cf = d.get('company_facts') or {}
    for fk, fv in (u.get('facts') or {}).items():
        if TAG not in str(cf.get(fk, '')) and fv:
            cf[fk] = fv if fk != 'other' or not cf.get('other') else (cf['other'] + '；' + fv)
    d['company_facts'] = cf
    if u.get('country_fix'):
        d['country_fix'] = u['country_fix']


if __name__ == '__main__':
    for code, u in UPD.items():
        p = os.path.join(RESEARCH_DIR, f'{code}.json')
        d = json.load(open(p, encoding='utf-8'))
        for one in (u if isinstance(u, list) else [u]):
            apply(d, one)
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(code, 'ok')
