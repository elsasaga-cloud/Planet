#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 93 批（T29-U88 同轮续做，公司底数第十一轮 · B 档「筛=1」主战场五国 20 户）：把官方 / 准官方登记核出来的「老板 / 采购 / 法定名 / 成立日」写回研究档。
只改角色与登记字段，不动 mail_review。可重复运行（幂等，以 TAG 判重）。来源明细见 data/saga_clients/registry/*.json（batch=93 行）。
结构同 batch92_kp.py：UPD[code] 可为 dict 或 list；键 kp_match（邮箱子串）/ kp_name（姓名全等）/ name / role / add_kp / facts / country_fix。
本批附带 1 处 KP 误归属更正：SB-112 Opax 的 damian@opax.pl 是波兰同名纸箱厂董事，标「误归属」不再发。"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import RESEARCH_DIR

TAG = '（第 93 批 官方登记核实 2026-10-28）'
CH = 'https://find-and-update.company-information.service.gov.uk/company/'
UPD = {
    # ---------- US ----------
    'SB-150': {'facts': {'other': '第 93 批：底数 1 次检索未命中（同名陷阱极多；疑似 nexxusnetworks.com「智能 PoE 制造商 17 年」但域名不同，未证同一）→ 下轮一次直查后不再追' + TAG}},
    'SB-353': [{'kp_match': 'mark@fibermailbox.com', 'role': '研究档 KP（职务未取；8–15 人老店，回信即拍板层）' + TAG},
               {'facts': {'legal_name': 'Fiber Optic Cable Shop（dba；Sales@FiberMailbox.com；加州法定名 / 登记号未取）', 'founded': '1976（自述；三次 INC 500）' + TAG, 'staff': '8–15 人（ZoomInfo 8 / photonics 15；15,000 sq ft）', 'hq': '136 South Second Street, Richmond, CA 94804',
                          'other': '第 93 批：50 年老店、自产光纤组件 + 自有标 MC / 机架 / 交换机 → OEM 30% 只做 MC + 机架 MC 机箱 + 光口小交换机；主品类 SFP / 光缆不供' + TAG}}],
    'SB-730': [{'kp_match': 'jalasad@it2ss.com', 'role': 'CEO / President（兼 VastMed LLC CEO；Alasad 家族多元集团老板）= 拍板人' + TAG},
               {'facts': {'legal_name': 'ITSS Inc.（it2ss.com；Grand Prairie, TX；德州登记号未取）—— 同名陷阱：ITSS Inc. Goldsboro NC（itss.us）/ 瑞士 ITSS（银行软件）', 'founded': '2003（自述）' + TAG, 'staff': '微型（安防 / IT 线 ≤10 人）', 'hq': '807 S. Great Southwest Pkwy, Grand Prairie, TX 75051',
                          'other': '第 93 批：医疗 / 电商 / 建筑 / 安防 IT / 中美跨境多元集团 → 有进口经验、老板直联；安防只是一条线，量小 → 分销 20% 工业 PoE 一页纸' + TAG}}],
    'SB-756': {'add_kp': {'name': 'Anthony (Tony) Farinholt', 'role': 'Owner & President / CEO & Director（BBB；家族公司：Denise Farinholt CFO、Dominic Farinholt VP；Mark Mulvaney Dir. Ops）= 老板 = 联系人（邮箱未公开，走官网表单 / sales@）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.bbb.org/us/tx/irving/profile/fiber-optics/fluxlight-inc-0875-90796041'},
               'facts': {'legal_name': 'FluxLight, Inc.（德州 Corporation；BBB：Incorporated 2007-08-17）', 'founded': '2003 / 2004-12-15（业务）；2007-08-17（公司）' + TAG, 'staff': '6 人（家族）', 'hq': '2035 Royal Ln Suite 280, Dallas, TX 75229（Irving）',
                         'other': '第 93 批：自有品牌 FluxLight 光收发器 / MC → OEM 30% 只剩 MC / 机架 MC 机箱 + 光口小交换机一条线；微型' + TAG}},
    'SB-761': [{'kp_match': 'ben.larue@getscw.com', 'role': '研究档 KP（职务未取；31–50 人公司有采购岗）' + TAG},
               {'add_kp': {'name': 'Matthew Nederlanden', 'role': 'CEO / President / 创始人（2009 接手；INC 5000；BBB / SAM 登记负责人）= 拍板人，抄送' + TAG, 'email': '', 'phone': '', 'source': 'https://www.bbb.org/us/nc/asheville/profile/security-cameras/security-camera-warehouse-inc-0473-92005262'},
                'facts': {'legal_name': 'Security Camera Warehouse, Inc.（SCW；北卡 S Corporation；SAM UEI RR46YDVKTNJ1 / CAGE 6ELB6）', 'founded': '2009-09-01（业务）/ 2010-10-05（SAM）/ 2016-07-26（公司）' + TAG, 'staff': '31–50 人（BBB 33）', 'hq': '11 Richland St, Asheville, NC 28806',
                          'other': '第 93 批：自有品牌 SCW + 联邦（海军）供应商 = NDAA 敏感 → 政府线不碰、只走商用线 OEM 30%（SCW 标 PoE 配自家相机）；卖点写保修 + 固件长期供应' + TAG}}],
    # ---------- TR ----------
    'SB-112': [{'kp_match': 'damian@opax.pl', 'role': '**误归属**：opax.pl = 波兰 Przytkowice 纸箱印刷厂 OPAX Sp. z o.o. Sp.k.（KRS 0000593709）的董事 Damian Brózda，与土耳其 Opax 无关 → 不发' + TAG},
               {'kp_match': 'satis@opax.com', 'role': 'Satış（销售；研究档）= 本户唯一有效收件人' + TAG},
               {'facts': {'legal_name': 'Opax Güvenlik Sistemleri Dış Tic. Ltd. Şti.（全名「Opax Mühendislik Kamera Alarm ve Güvenlik Sistemleri … Dış Ticaret Pazarlama Limited Şirketi」；页脚 Opax İthalat Dış Ticaret Ltd. Şti.）', 'founded': '2004（自述；页脚 2007 起）' + TAG, 'staff': '小型（估 10–30 人）', 'hq': 'İstanbul（街道地址未取）',
                          'other': '第 93 批：自有品牌报警（OPAX-W 系列 GSM / WiFi）+ 相机进出口 → OEM 30%：PoE 交换机贴 OPAX 标配报警 + 相机套装；研究档首 KP damian@opax.pl 误归属已标' + TAG}}],
    'SB-276': {'add_kp': {'name': 'Fadime Maden', 'role': 'Purchasing Manager（采购经理；RocketReach）= **对口收件人**（邮箱未公开 → info@ 点名；GM Hakan Kasap 抄送；董事会成员 Kerim Yeşilyurt）' + TAG, 'email': '', 'phone': '', 'source': 'https://rocketreach.co/han-elektronik-profile_b40780acfc251b05'},
               'facts': {'legal_name': 'Han Elektronik Bilgisayar ve Güvenlik Sistemleri San. Tic. A.Ş.（EMIS）', 'founded': '2003-06-25（EMIS；LinkedIn 2000）' + TAG, 'staff': '20–52 人（集团自述 Han Grup 40 人）', 'hq': 'Mehmet Akif Mah. Bahariye Cad. 1904 Sk. No:15/A, Küçükçekmece / İstanbul 34307',
                         'other': '第 93 批：A.Ş.、自有品牌含交换机、专职采购经理 → OEM 30% 首选：Han 标 PoE 一对一替代现深圳货（研究档「hisource」）；bayi 网络 = 他们自己是分销（Q-33 其 bayi 不碰）；回信即 A 候选' + TAG}},
    'SB-285': {'add_kp': {'name': 'Raif Gündüz', 'role': 'Genel Müdür（Perpa 名录）= 老板 = 拍板人（邮箱未公开 → info@rfteknoloji.com.tr 点名）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.perpaonline.com/tr/firma.aspx?fid=2654'},
               'facts': {'legal_name': 'RF Teknoloji Makine ve Otomasyon San. Tic. Ltd. Şti.', 'founded': '2012' + TAG, 'staff': '微型（估 3–10 人）', 'hq': 'Tevfik Bey Mah. Şehit Adem Tamrak Sk. No:2/5, Sefaköy / Küçükçekmece / İstanbul',
                         'other': '第 93 批：工业无线（CalAmp 代理）+ 3onedata 工业交换机分销 → 已有深圳工业货源 → 分销 20%：STI DIN 轨 PoE 作第二货源一页纸' + TAG}},
    'SB-875': {'add_kp': {'name': 'Semih Sengir', 'role': '电商店铺登记人（n11 / PttAVM：个体 Proses Bilgisayar）= 老板' + TAG, 'email': '', 'phone': '', 'source': 'https://www.n11.com/magaza/lemaxguvenlik'},
               'facts': {'legal_name': 'Lemax Güvenlik ve Bilişim Sistemleri Toptan Satış Paz. İç ve Dış Tic. Ltd. Şti.（+ 个体 Semih Sengir 双主体）', 'founded': '2007–2012（自述四个版本）' + TAG, 'staff': '微型（1–5 人）', 'hq': 'Üsküdar Cad. 127C, Kartal / İstanbul',
                         'other': '第 93 批：微型网店、相机套装贴 Lemax 标、价格敏感 → 分销 20% 一页纸后不再投入' + TAG}},
    # ---------- GB ----------
    'SB-017': [{'kp_match': 'graham@securitytec.co.uk', 'name': 'Graham David Smith', 'role': 'Director（2005-10-06 起；1959-09 生；Companies House 05585047；身份已核验）= **老板 = 采购 = 联系人**（Secretary Katie Ann Smith = 家族）' + TAG},
               {'facts': {'legal_name': 'SECURITYTEC LIMITED（Companies House 05585047；同名陷阱 SECURITYTEC LTD 10186386 Manchester 已注销）', 'founded': '2005-10-06' + TAG, 'staff': '微型（0–9 人）', 'hq': 'Units 2 & 3 Redlands Centre, Redlands, Ullswater Industrial Estate, Coulsdon CR5 2HT',
                          'other': '第 93 批：夫妻店 20 年、Hikvision 授权批发、网店已有自有标 PoE 交换机 → OEM 30%：8/16 口 PoE 贴 Securitytec 标替换现款；有 charges 记录' + TAG}}],
    'SB-041': {'add_kp': {'name': 'John Dhunay', 'role': 'Director（2020-01-02 起；1969-05 生；Companies House 12383574；唯一在任 —— Rajinder Singh Dhunay 2026-02-23 辞任）= 老板' + TAG, 'email': '', 'phone': '', 'source': CH + '12383574/officers'},
               'facts': {'legal_name': 'TELCAM FIRE & SECURITY LTD（Companies House 12383574；曾名 Telcam Security Services Ltd）', 'founded': '2020-01-02' + TAG, 'staff': '微型（1–5 人）', 'hq': '5 Broadway Buildings, Boston Road, London W7 3TT',
                         'other': '第 93 批：Dhunay 家族安装商，2026-02 一董事退出 → 一人公司；火灾报警守界不碰，只谈 CCTV 配套 PoE；小项目集成商序列末位' + TAG}},
    'SB-063': {'add_kp': {'name': 'Javid Aria', 'role': 'Director（2013-11-11 起；1982-09 生；英国籍；Companies House 07964960；唯一在任）= 老板 = 联系人' + TAG, 'email': '', 'phone': '', 'source': CH + '07964960/officers'},
               'facts': {'legal_name': 'AVESTA (MANCHESTER) LTD（Companies House 07964960）', 'founded': '2012-02-24' + TAG, 'staff': '微型（1–9 人）', 'hq': '64 Waterloo Road, Manchester',
                         'other': '第 93 批：一人公司、HiLook（海康子品牌）授权分销、有 charges（抵押）→ 分销 20% 8/16 口 PoE 一页纸；T/T 50/50 坚持' + TAG}},
    'SB-076': {'add_kp': {'name': 'Senay Huseyin Bozaci', 'role': 'Director（2018-02-27 起；1980-01 生；Companies House 11228236；唯一董事）= 拍板人（17 次推送 0 回复 → 不动）' + TAG, 'email': '', 'phone': '', 'source': CH + '11228236/officers'},
               'facts': {'legal_name': 'IST SURVEILLANCE LTD（Companies House 11228236）', 'founded': '2018-02-27' + TAG, 'staff': '微型（1 人）', 'hq': 'Office 408, Screenworks, 22 Highbury Grove, London N5 2ER',
                         'other': '第 93 批：一人公司、17 次推送 0 回复 → 底数已清，不再投入' + TAG}},
    # ---------- DE ----------
    'SB-027': [{'kp_match': 'communication@voipdistri.com', 'role': 'Inhaber / CEO（个体工商 Gewerbebetrieb；Creditreform：1 Inhaber、Außenhandel / Import）= 老板 = 联系人' + TAG},
               {'facts': {'legal_name': 'Mathias Gottensträter VoIPDistri.com（Einzelunternehmen；无 HRB；USt-IdNr. DE814065254）', 'founded': '≈2003–2010（VoIPphones.de 编辑后创业）' + TAG, 'staff': '微型（1 人 + 兼职）', 'hq': 'Im Hagen 3, 33790 Halle (Westfalen)',
                          'other': '第 93 批：一人 VoIP 增值分销、自营进口 → 分销 20%：工业 M12 / DIN 轨 PoE 作第二货源；T/T 预付坚持' + TAG}}],
    'SB-077': [{'kp_name': 'Markus Diederichs', 'role': 'Geschäftsführer（**2025-09 起**，与 Carsten Simons 共同；前 BDO Cyber Security；主推「自研 / 德国制造 / 主权」；HRB 44506 Wittlich）= 新拍板人' + TAG},
               {'kp_match': 'info@liveye.com', 'name': 'Carsten Simons', 'role': 'Geschäftsführer（2021-03 登记单独代表权；创始人型）= 老板' + TAG},
               {'facts': {'legal_name': 'LivEye GmbH（AG Wittlich HRB 44506；USt DE321392908；D-U-N-S 315185493；控股 LivEye Beteiligungs GmbH HRB 46290）', 'founded': '2018（Indeed）' + TAG, 'staff': '≈95 人、5 地点（DACH + 波兰）；营收 €4–21M 区间', 'hq': 'Europa-Allee 56b, 54343 Föhren',
                          'other': '第 93 批：移动监控塔制造商 → PoE 交换机是塔内部件 → OEM / 部件 30%：工业小口数宽温 PoE（付费样机验证）；新 GF 主打「摆脱全球供应链」→ 卖点写长期供货 + 固件 + 3 年保修，不提产地' + TAG}}],
    'SB-090': [{'kp_match': 'zain@adlerss.com', 'name': 'Zain (Sana) Ullah', 'role': 'Operations Engineer（signalhire）= 技术口（非采购）→ 技术切入：宽温 / PoE 预算 / SFP 兼容' + TAG},
               {'facts': {'legal_name': 'Adler ELREHA GmbH t/a Adler Security Systems（Hockenheim；HRB 1 次未取 → 下轮 Northdata 直链；约旦 Elreha 集团子公司 + 美国 Adler Systems LLC, St Petersburg FL）', 'founded': '2012 / 2013' + TAG, 'staff': '小型（11–50 人）', 'hq': 'Schwetzinger Str. 103, 68766 Hockenheim',
                          'other': '第 93 批：自有品牌 IP / 热成像相机制造商 → 交换机是系统部件 → OEM 30%：工业 PoE / 光口交换机贴 Adler 标配太阳能独立站；边境 / 政府项目制 → 量不稳；军用整机不碰' + TAG}}],
    'SB-242': [{'kp_match': 'arosen@grothe.de', 'name': 'Andreas Rosen', 'role': 'Geschäftsführer（AG Siegburg HRB 6442；wer-zu-wem / DDW / protector）= **研究档 KP 就是 GF 本人 = 拍板人**' + TAG},
               {'facts': {'legal_name': 'Grothe GmbH（AG Siegburg HRB 6442；LEI 529900VY9SISWY0OKP81；USt DE813326876；资本 €1.5M；意大利 Urmet S.p.A. 集团 100%）', 'founded': '2001-08-27（GmbH；品牌 1892 Köln，1998 迁 Hennef，2001 入 Urmet）' + TAG, 'staff': '70 人（2023）；营收 €13–21M；资产 €9.38M（2023）', 'hq': 'Löhestr. 22, 53773 Hennef (Sieg)',
                          'other': '第 93 批：Urmet 集团德国子公司 → CCTV / 网络件可能集团统采 → 只试 OEM 30%：Grothe 标 PoE 配其 IP 对讲 / CCTV；一封信直达 GF；130 年品牌付款稳' + TAG}}],
    # ---------- PL ----------
    'SB-664': {'add_kp': {'name': 'Sławomir Jarosław Pieszczek', 'role': 'Prezes Zarządu（KRS 0000416117；Wiceprezes Teresa Jadwiga Suchoń）= 拍板人（元器件广线分销，写 jm@jm.pl 点名采购 / 产品经理）' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/416117/jm-elektronik'},
               'facts': {'legal_name': 'JM elektronik Sp. z o.o.（KRS 0000416117 · NIP 6312645365 · REGON 242895943；资本 1,000,000 zł；D-U-N-S 422187464）', 'founded': '2012-04-03（Sp. z o.o.）' + TAG, 'staff': '中型；营收 2025 58.5 mln zł（2024 58.2 / 2023 64.1）、利润 0.24 mln、资产 32.4 mln', 'hq': 'ul. Karolinki 58, 44-100 Gliwice',
                         'other': '第 93 批：元器件广线分销 + ICP DAS（台湾）工业自动化 2009 起授权 → B BIG：分销 20%、STI 工业 DIN 轨作第二货源；利润率 0.4% → 价格 / 账期极敏感' + TAG}},
    'SB-1098': {'add_kp': {'name': 'Marek Ziniewicz', 'role': 'Prezes Zarządu / 80% 股东（KRS 0000690689；Dominika Talarczyk 20%）= 老板 = 联系人（biuro@zintronic.pl 点名）' + TAG, 'email': '', 'phone': '', 'source': 'https://rejestr.io/krs/690689/zintronic'},
                'facts': {'legal_name': 'Zintronic Sp. z o.o.（KRS 0000690689 · NIP 9662114233 · REGON 368007675；资本 5,000 zł；PKD 26.40.Z 消费电子生产）', 'founded': '2017-08-11' + TAG, 'staff': '微型–小型（估 5–15 人）', 'hq': 'ul. Karola Modzelewskiego 2, 15-535 Białystok',
                          'other': '第 93 批：自有品牌 Zintronic（PKD 生产类）+ 现供 Hasivo（深圳）→ OEM 30%：Zintronic 标 PoE 一对一替代 Hasivo；PL 第二 OEM 候选（Spacetronik 之后）；MOQ 1 箱、T/T 预付' + TAG}},
    'SB-270': {'add_kp': {'name': 'Damian Marciniak', 'role': '业主（FHU DAMIX，CEIDG 个体）' + TAG, 'email': '', 'phone': '', 'source': 'https://www.damixsat.pl/webpage/o-firmie.html'},
               'facts': {'legal_name': 'FHU DAMIX Damian Marciniak（CEIDG 个体；NIP 6981620419 · REGON 386854875；旧登记 NIP 6981560781）', 'founded': '2006' + TAG, 'staff': '微型（1–3 人）', 'hq': 'ul. Balcera 40, 64-000 Kościan',
                         'other': '第 93 批：个体 SAT / RTV 网店、交换机只是配件、经销 Spacetronik（SB-092）配件 → 不再投入（不动）；Spacetronik 做成 OEM 后此类店自动跟着卖' + TAG}},
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
