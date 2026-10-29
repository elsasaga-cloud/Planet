#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""External XC · 「路径未建」补邮箱 第二批 X1-03（2026-10-29，T29-U122 Simon「继续」）。

对象：X1-02 之后仍是「渠道型主体但路径未建 → 补到邮箱再闸 2」的 74 户 keep_C（US 33 / AE 12 / GB 5 / CA 4 / IN 3 …）里，
按对位 + 区域挑出 29 户各做一次 depth-1 检索（未中即止）；结果（邮箱 / 法人 / 地址 / 事实 + URL）落在
data/external_clients/xc_path_fill_2026-10-29_b2.json['rows']（本脚本只读它，不再外查）。

另有 17 户「巨头 / 上市 / 零售集团」按规则直接定（不检索）：采购走招标 / 供应商门户，补路径无意义 → 留 C 标 giant / retail，
不入池、不群发；其余 28 户（阿联酋无名小户 4、电商 3、美国电气批发余户、非主区小户等）本批未查，原判不动。

落三处（全部幂等）：
  1. data/external_clients/{cctv,edgecore,mikrotik}.json['records'] —— emails 追加 {addr, status:'公开·X1-03 补'}、emails_live 同步、
     flags「无可用邮箱 / 缺联系」→「邮箱已补（X1-03 …）」。
  2. data/external_clients/research/<code>.json —— 轻研究卡（round X1-03；证据带 URL + 日期；等级不动 = C，池位在 sieve_x）。
  3. data/external_clients/sieve_x.json —— 按闸 2 / 闸 3 口径定：pool ○（对位 ✔ 渠道主体 ✔ 邮箱 ✔ + 官网 / 名录法人部分坐实 → reg_pending）、
     pool_watch ☆（微型 / 对位一般 / 体量未知，试单后转正）、keep_C（对位弱 / 微型 / 非主区店铺型 / 仍无邮箱；有邮箱者标 email_found）。
     入池户追加到 data/saga_clients/P池_巡检表_2026-10-29.csv + docs/P池_资产池名册_2026-10-29.md「External 并池 · 批 X1-03」。

用法：python3 sieve_batches_x/x1_003_email.py
"""
import collections
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve_x  # noqa: E402
import research_store  # noqa: E402

BATCH = 'X1-03'
DATE = '2026-10-29'
NEXT_CHECK = '2026-12-28'
ROOT = sieve_x.ROOT
DATA = os.path.join(ROOT, 'data', 'external_clients')
FILL = os.path.join(DATA, f'xc_path_fill_{DATE}_b2.json')
WATCH = os.path.join(ROOT, 'data', 'saga_clients', f'P池_巡检表_{DATE}.csv')
ROSTER = os.path.join(ROOT, 'docs', f'P池_资产池名册_{DATE}.md')
CHECK_ITEMS = '官网改版 / 新品 / 招聘 / 社媒（LinkedIn / FB / IG）/ GitHub / 展会出席 / 新闻稿 / 域名 MX 存活'
REPO_FILE = {'cctv-info': 'cctv.json', 'edgecore-info': 'edgecore.json', 'mikrotik-info': 'mikrotik.json'}
MAIN = '四主区 + 波兰'
EU = '欧洲其他'
ME = '中东 / 非洲'

# code: dict(verdict, star, group, company, country, links, tags, reason)
# 口径同 X1-02：○ 对位 + 渠道主体 + 邮箱 + 法人部分坐实（reg_pending）；☆ 观察（微型 / 对位一般 / 体量未知，试单后转正）；keep_C 留储备。
D = {
    # ---- 入池 ○（美国主区工业自动化分销 / 数据中心 / 欧洲工业分销）----
    'XC-E085': dict(verdict='pool', star='○', group=MAIN, company='Racklive（ASA Computers, Inc. 数据中心事业部）', country='美国', links='racklive.com', tags=['dc', 'reg_pending'],
                    reason='○ 机架集成 / 数据中心服务器与存储 25%：Racklive = ASA Computers, Inc. 数据中心事业部（Fremont CA 48761 Kato Rd；2011 起；ISO 9001:2015；全球部署）官网部分坐实（法人 ASA Computers 州注册号待补）；数据中心交换机对位（CENTEC 敲门砖 + SmartByte 万兆）；主区 US；sales@racklive.com'),
    'XC-M151': dict(verdict='pool', star='○', group=MAIN, company='Power/mation', country='美国', links='powermation.com', tags=['industrial', 'reg_pending'],
                    reason='○ 工业自动化分销 20%：Power/mation（St. Paul MN 1310 Energy Lane + Waukesha WI；1961 起；≈159 人；CEO Jim Landes）名录部分坐实（MN SOS 号待补）；HMS / Red Lion / N-Tron 渠道 → STI 工业对位；主区 US；info@powermation.com'),
    'XC-M140': dict(verdict='pool', star='○', group=MAIN, company='CBT Company', country='美国', links='cbtcompany.com', tags=['industrial', 'reg_pending'],
                    reason='○ 工业自动化分销 20%：CBT Company（Cincinnati OH；百年企业；5 处分支 OH / KY；自述区域最大工业自动化分销）官网部分坐实（法人全名 / OH SOS 号待补）；HMS / Red Lion / N-Tron 渠道 → STI 对位；主区 US；hello@cbtcompany.com（官网联系箱，待挖采购 KP）'),
    'XC-M164': dict(verdict='pool', star='○', group=MAIN, company='TMMI, LLC（TMMI powered by GrayMatter）', country='美国', links='tmmi.com', tags=['industrial', 'reg_pending'],
                    reason='○ 工业自动化 / 电气控制设备分销 20%：TMMI, LLC（Wheat Ridge CO 5000 Robb St；1977 起；落基山 8 州；GrayMatter 旗下）item 官方伙伴页部分坐实（CO SOS 号待补）；HMS / Red Lion / N-Tron 渠道 → STI 对位；主区 US；具名 VP Bryan Young byoung@tmmi.com'),
    'XC-M149': dict(verdict='pool', star='○', group=MAIN, company='Logic, Inc.', country='美国', links='logic-control.com', tags=['industrial', 'reg_pending'],
                    reason='○ 工业自动化高科技分销 20%：Logic, Inc.（Olathe KS 890 N Martway Ct；设 OEM 销售经理 John Wilmes）官方 FB + ZoomInfo 部分坐实（KS SOS 号待补）；HMS / Red Lion / N-Tron 渠道 → STI 对位；主区 US；sales@logic-control.com'),
    'XC-M153': dict(verdict='pool', star='○', group=MAIN, company='Process Technology, Inc.（PTI）', country='美国', links='process-tech.com', tags=['industrial', 'reg_pending'],
                    reason='○ 过程仪表 + 工厂自动化分销 20%：Process Technology, Inc.（Salt Lake City UT；1986 起；AZ / CO 分部；11–50 人）官网 FAQ + 名录部分坐实（UT 注册号待补）；HMS / Red Lion / N-Tron 渠道 → STI 对位；主区 US；quotes@ / process@process-tech.com'),
    'XC-C1449': dict(verdict='pool', star='○', group=MAIN, company='EFCO Electronics GmbH', country='德国', links='efcotec.de | shop.efcotec.de', tags=['industrial', 'reg_pending'],
                    reason='○ 工业 PC / Panel PC + Teltonika 分销 20%：EFCO Electronics GmbH（Deggendorf Ulrichsberger Str. 17/G1；来源库称 2014 起 100–199 人；官方网店）名录 + 网店部分坐实（HRB 待补）；工业网关 / 路由渠道 → STI 对位；主区 DE；sales@efcotec.de'),
    'XC-M096': dict(verdict='pool', star='○', group=EU, company='JAMPEL S.r.l.', country='意大利', links='jampel.it', tags=['industrial', 'reg_pending'],
                    reason='○ 嵌入式 PC / 工业通信分销 20%：JAMPEL S.r.l.（Bologna Via degli Stradelli Guelfi 86/A；ICP DAS 官方分销 + Moxa 授权）官方名录部分坐实（P.IVA 待补）；STI 工业对位；info@jampel.it'),
    'XC-C1431': dict(verdict='pool', star='○', group=EU, company='HOTEL CARE（Groupe TB6）', country='法国', links='hotel-care.fr', tags=['hospitality', 'reg_pending'],
                    reason='○ 酒店 / 医疗机构 TV / WiFi / IPTV 网络集成 25%：HOTEL CARE（Mauguio 34 总部 + Meyreuil 13；Groupe TB6 子公司，集团 2007 起；Nice / Lyon / Paris）官网部分坐实（SIREN 待补）；酒店 PoE 接入 → SmartByte 商用 PoE 对位；contact@hotel-care.fr'),
    'XC-M126': dict(verdict='pool', star='○', group=EU, company='evolvit Solutions AB（原 Dialect Skövde）', country='瑞典', links='evolvit.se | shop.evolvit.se', tags=['isp_channel', 'reg_pending'],
                    reason='○ IT 服务 / 系统集成 + 电信 25%：evolvit Solutions AB（Skövde Gesällgatan 1；51–100 人；MikroTik 官方分销名录）RIPE 会员页 + Crunchbase 部分坐实（org.nr 待补）；MikroTik 渠道 → SmartByte 管理型 + STI 对位；info@ / kontakt@evolvit.se'),
    # ---- 观察档 ☆（微型 / 对位一般 / 体量未知，试单后转正）----
    'XC-M184': dict(verdict='pool_watch', star='☆', group=EU, company='Computer Products Professional Benelux B.V.', country='荷兰', links='cppb.nl', tags=['industrial', 'micro', 'reg_pending'],
                    reason='☆ ATEX Zone II 工业以太网交换机等专业分销 20%：Computer Products Professional Benelux B.V.（Puttershoek Biezenvijver 4，与 RTP Europe 同址）官网部分坐实（KvK 待补）；小型 + 防爆细分 → 观察档；info@compprof-rtp.com'),
    'XC-M176': dict(verdict='pool_watch', star='☆', group=MAIN, company='Digital Controls', country='英国', links='digitalcontrols.biz', tags=['industrial', 'micro'],
                    reason='☆ Red Lion / Horner 等自动化产品分销 20%：Digital Controls（Peterborough PE2 7DR；联系人 Tim Sommerville）官网 + 行业名录部分坐实（法人形式 / Companies House 号未明）；主区 GB 但微型 → 观察档；sales@digitalcontrols.biz'),
    'XC-M133': dict(verdict='pool_watch', star='☆', group=MAIN, company='Adcon Engineering Co., Inc.', country='美国', links='adconengineering.com', tags=['industrial', 'reg_pending'],
                    reason='☆ 工业元件 / 传感 / 视觉 / 机柜分销 20%：Adcon Engineering Co., Inc.（Strongsville OH 20102 Progress Dr；线卡含 EtherDevice DIN 导轨非管理交换机）官网 + NDT 名录部分坐实（OH SOS 号待补）；主区 US 但体量未知、官网陈旧 → 观察档；sales@adconengineering.com'),
    'XC-M163': dict(verdict='pool_watch', star='☆', group=MAIN, company='TCIC Inc.', country='美国', links='tcicinc.com', tags=['industrial', 'reg_pending'],
                    reason='☆ 工业自动化 + 工业通信 / 无线分销 20%：TCIC Inc.（Golden Valley MN 628 Mendelssohn Ave N；President & CEO Christine Frank）官网部分坐实（MN SOS 号待补）；主区 US 但小型 → 观察档；info@tcicinc.com'),
    'XC-M152': dict(verdict='pool_watch', star='☆', group=MAIN, company='Power Motion Sales Inc.', country='美国', links='powermotionsales.com', tags=['industrial', 'reg_pending'],
                    reason='☆ 自动化元件与系统分销 20%：Power Motion Sales Inc.（Fenton MO 652 Axminister Dr；St. Louis / KC / Little Rock；Owner Christopher Tremblay）官方 FB 部分坐实（MO SOS 号待补）；主区 US 但体量未知、视觉 / 运动为主 → 观察档；slsales@powermotionsales.com'),
    'XC-M148': dict(verdict='pool_watch', star='☆', group=MAIN, company='Lakeland Engineering Equipment Company', country='美国', links='lakelandengineering.com', tags=['industrial', 'reg_pending'],
                    reason='☆ 电气电机控制与元件分销 20%：Lakeland Engineering Equipment Company（Minneapolis MN + KC / Omaha / Fargo / Denver；101–250 人）官网部分坐实（MN SOS 号待补）；主区 US、体量够但电气元件为主 → 观察档；sales@lakelandengineering.com'),
    'XC-M141': dict(verdict='pool_watch', star='☆', group=MAIN, company='Clayton Engineering Company', country='美国', links='claytonengineering.com', tags=['industrial', 'reg_pending'],
                    reason='☆ 电气分销 + 培训 / 咨询 20%：Clayton Engineering Company（Cuddy / Bridgeville PA；1947 起；AHTD 会员；11–50 人；Owner Don Bohn）官网线卡部分坐实（PA 注册号待补）；主区 US 但电气分销为主 → 观察档；sales@clayeng.net'),
    # ---- 留 C（有邮箱 → 群发可用，但对位 / 体量 / 形态 / 区域不够入池）----
    'XC-M178': dict(verdict='keep_C', reason='留 C：Future Focus Energy Limited（Blackpool；4 人；能源管理 / 监测公司）→ 不是渠道分销，对位弱；邮箱已补 Info@futurefocusenergy.co.uk', tags=['email_found', 'micro']),
    'XC-M171': dict(verdict='keep_C', reason='留 C：Clanrye Electrical Supplies Ltd（Newry BT35；电气批发 35 年 + KNX 分销伙伴）→ 电气 / 楼宇自动化为主，交换机对位弱；邮箱已补 info@clanryeelectrical.com，随群发节奏', tags=['email_found']),
    'XC-M146': dict(verdict='keep_C', reason='留 C：ErieTec, Inc.（Erie PA；1958 起；51–100 人；电气控制 + 机械传动分销）→ 机电为主，交换机对位弱；邮箱已补 solutions@ / erie@erietecinc.com', tags=['email_found']),
    'XC-M169': dict(verdict='keep_C', reason='留 C：Zesco Inc.（Broadview Hts OH；营收 $0.5–1M；Owner Ed Sustersic）微型自动化分销；邮箱已补 sales@zescoinc.com', tags=['email_found', 'micro']),
    'XC-M137': dict(verdict='keep_C', reason='留 C：Branom Instrument Company（Seattle WA；1947 起；过程仪表分销）→ 仪表为主，交换机对位弱；邮箱已补 sales@branom.com', tags=['email_found']),
    'XC-C1478': dict(verdict='keep_C', reason='留 C：ITWorld Trading LLC（Bur Dubai；电脑硬件 / CCTV / 网络批发小户）→ 非主区店铺型贸易商，宁缺毋滥；邮箱已补 info@itworlduae.com，预付 100% 随群发', tags=['email_found', 'prepay']),
    'XC-C1490': dict(verdict='keep_C', reason='留 C：Switch Link Computers Trading LLC（Bur Dubai Unit 103；Cisco 合作伙伴小户；官网 WA +971 50 804 6102）→ 非主区小型 Cisco 转售；邮箱已补 info@switchlinkdubai.com，预付 100% 随群发', tags=['email_found', 'prepay']),
    'XC-C1540': dict(verdict='keep_C', reason='留 C：Al Dhahab Computer Trading L.L.C.（Deira Al Sabkha Rd Shop 4；B2B IT 硬件转口 GCC / 非洲 / CIS）→ 非主区店铺型转口商；邮箱已补 info@aldhahab.ae，预付 100% 随群发', tags=['email_found', 'prepay']),
    'XC-C1472': dict(verdict='keep_C', reason='留 C：Colion International Trading LLC（Deira；IT 硬件库存 / 批发 / 出口；DCG 会员，具名 Muhammed Anas anas@colioninternational.com）→ 非主区店铺型；邮箱已补 info@colioninternational.com，预付 100% 随群发', tags=['email_found', 'prepay']),
    # ---- 留 C（一次检索仍无直接邮箱 → 止）----
    'XC-E075': dict(verdict='keep_C', reason='留 C：Tuangru（Vancouver；已转型 Hyperview DCIM 软件；CTO Rami Jebara）公开页无直接邮箱 → 路径仍未建，且软件转型对位弱，一次检索即止', tags=[]),
    'XC-C0599': dict(verdict='keep_C', reason='留 C：Abboud Trading Corp.（Medley / Miami FL；1996 起；消费电子全渠道分销拉美；Director William Abboud）官网无公开邮箱（聚合页个人邮箱不采）→ 路径仍未建；消费电子口径对位弱，一次检索即止', tags=[]),
    'XC-M165': dict(verdict='keep_C', reason='留 C：Thorp Controls（Merriam KS / Denver CO；100–200 人；President Todd Thorp）公开页只有遮蔽邮箱 → 路径仍未建（官网表单），一次检索即止；体量够，补到邮箱即可闸 3', tags=[]),
}

# 规则判（不检索）：巨头 / 上市 / 零售集团 —— 采购走招标 / 供应商门户，补路径无意义；留 C 不入池、不群发。
GIANT = {
    'XC-C1534': ('retail', 'Carrefour UAE（Majid Al Futtaim）零售集团'),
    'XC-C1594': ('retail', 'Lulu Group 零售集团'),
    'XC-C0789': ('retail', 'Tesco 零售集团'),
    'XC-M107': ('retail', 'T.S.Bohemia a.s. 捷克 IT 零售连锁'),
    'XC-E086': ('giant', 'SHI International 美国 IT 大分销 / 方案商'),
    'XC-E081': ('giant', 'ePlus inc. 美国上市 IT 方案商'),
    'XC-E082': ('giant', 'GDT（General Datatech）美国大型集成商'),
    'XC-M136': ('giant', 'Black Box（AGC Networks）跨国 IT 服务'),
    'XC-M157': ('giant', 'Radwell International 大型工业备件平台'),
    'XC-C0603': ('giant', 'Datto / Kaseya 软件巨头'),
    'XC-E042': ('giant', 'ITOCHU 综合商社'),
    'XC-M191': ('giant', 'Omron Iberia 自动化巨头子公司'),
    'XC-C0604': ('giant', 'Wipro Lighting 集团子公司'),
    'XC-M180': ('giant', 'Netceed UK（原 Comtec）跨国电信分销集团'),
    'XC-M166': ('giant', 'Van Meter Inc. 美国大型电气分销（员工持股）'),
    'XC-M081': ('giant', 'Proax Technologies 加拿大大型自动化分销'),
    'XC-E070': ('giant', 'ASI Corp.（asipartner.com）美国大型 IT 元件 / 系统分销'),
}


def main():
    fill = json.load(open(FILL, encoding='utf-8'))['rows']
    assert set(fill) == set(D), set(fill) ^ set(D)
    sieve = sieve_x.load_sieve()
    recs = {r['code']: (r, repo) for r, repo in sieve_x.load_xc()}

    # 1) 来源记录：邮箱
    touched = collections.Counter()
    for repo, fn in REPO_FILE.items():
        p = os.path.join(DATA, fn)
        d = json.load(open(p, encoding='utf-8'))
        changed = False
        for r in d['records']:
            code = r.get('code')
            if code not in fill:
                continue
            emails = fill[code]['emails']
            have = {e['addr'].lower() for e in (r.get('emails') or [])}
            for e in emails:
                if e.lower() not in have:
                    r.setdefault('emails', []).append({'addr': e, 'status': f'公开·{BATCH} 补'})
                    r.setdefault('emails_live', []).append(e)
                    have.add(e.lower())
                    changed = True
                    touched['emails+'] += 1
            if emails:
                tag = f'邮箱已补（{BATCH} {DATE}）'
                fl = [x for x in (r.get('flags') or []) if x not in ('无可用邮箱', '缺联系')]
                if tag not in fl:
                    fl.append(tag)
                if fl != r.get('flags'):
                    r['flags'] = fl
                    changed = True
        if changed:
            json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # 2) 轻研究卡（只给有邮箱的；已有卡不覆盖）
    for code, f in fill.items():
        if not f['emails'] or research_store.get(code):
            continue
        r, repo = recs[code]
        v = D[code]
        research_store.put({
            'code': code, 'name': r['name'], 'round': BATCH, 'researched_at': DATE,
            'alive': f'{DATE} 检索命中官网 / 名录（在线）', 'summary': (f['legal'] or r['name']) + '：' + f['note'][:120],
            'type_final': (r.get('type') or '渠道') + ('；' + f['legal'] if f['legal'] else ''), 'size': '',
            'saga_line': 'Saga STI 工业 / SmartByte 商用 PoE' if 'dc' not in (v.get('tags') or []) else 'CENTEC 数据中心（敲门砖）+ SmartByte',
            'fit': v.get('reason', '')[:60], 'brands_seen': [],
            'contacts': {'email': f['emails'][0], 'email_status': f'官网 / 名录公开（{BATCH} 补路径）', 'kp': []},
            'evidence': [{'kind': '官网 / 名录', 'claim': w, 'quote': '', 'url': u, 'date': DATE} for w, u in f['facts']],
            'touch_status': f'未触达（路径 {DATE} 新补）', 'saga_overlap': '无', 'grade_final': 'C',
            'grade_reason_final': f'{BATCH} 补路径：{v["reason"][:110]}（等级不动，池位见 sieve_x）',
            'next_move': {'action': '不动', 'angle': {'pool': '已入 P 池 → 按巡检节奏首触', 'pool_watch': '观察档 → 试单后转正', 'keep_C': '留 C 储备，随群发节奏'}[v['verdict']]},
            'deep': False, 'notes': '；'.join(x for x in (f['legal'], f['addr'], f['reg'], f['phone']) if x),
        })
        touched['cards+'] += 1

    # 3) sieve_x：检索户
    for code, v in D.items():
        assert code in recs, code
        cur = sieve.get(code) or {}
        assert cur.get('batch') in ('X1-auto', 'X1-01', BATCH), (code, cur.get('batch'))
        gate = 3 if v['verdict'] in ('pool', 'pool_watch') else 1
        row = {'verdict': v['verdict'], 'gate': gate, 'rule': 'G3' if gate == 3 else 'G1', 'reason': v['reason'], 'date': DATE, 'manual': True,
               'repo': recs[code][1], 'origin': 'External', 'batch': BATCH,
               'facts': [{'what': w, 'url': u, 'date': DATE} for w, u in fill[code]['facts']]}
        if cur.get('batch') in ('X1-auto', 'X1-01') and cur.get('reason'):
            row['g1_reason'] = cur['reason']
            row['g1_batch'] = cur['batch']
        elif cur.get('g1_reason'):
            row['g1_reason'], row['g1_batch'] = cur['g1_reason'], cur['g1_batch']
        if v.get('star'):
            row['star'] = v['star']
        tags = list(v.get('tags') or [])
        if fill[code]['emails'] and 'email_found' not in tags:
            tags.append('email_found')
        if tags:
            row['tags'] = tags
        if fill[code]['emails']:
            row['emails'] = fill[code]['emails']
        sieve[code] = row
    # 3b) sieve_x：规则判巨头 / 零售（不检索；保留闸 1 原判为 g1_reason）
    n_giant = 0
    for code, (tag, label) in GIANT.items():
        assert code in recs, code
        cur = sieve.get(code) or {}
        if cur.get('batch') == BATCH:
            continue
        assert cur.get('verdict') == 'keep_C' and cur.get('batch') in ('X1-auto', 'X1-01'), (code, cur.get('verdict'), cur.get('batch'))
        sieve[code] = {'verdict': 'keep_C', 'gate': 1, 'rule': 'G1-giant', 'date': DATE, 'manual': True, 'repo': recs[code][1], 'origin': 'External',
                       'batch': BATCH, 'tags': [tag], 'g1_reason': cur.get('reason'), 'g1_batch': cur.get('batch'),
                       'reason': f'留 C（规则判 {BATCH}，不检索）：{label} —— 巨头 / 上市 / 零售集团采购走招标 / 供应商门户，补路径无意义；不入池、不群发，只在客户主动找上门时再议'}
        n_giant += 1
    cnt = sieve_x.save_sieve(sieve)

    # 4) 巡检表（幂等：按编号）
    with open(WATCH, encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))
    header, body = rows[0], rows[1:]
    have = {r[0] for r in body}
    added = 0
    for code, v in D.items():
        if v['verdict'] not in ('pool', 'pool_watch') or code in have:
            continue
        body.append([code, v['star'], '正式' if v['verdict'] == 'pool' else '观察', v['company'], v['country'], v['group'], v['links'],
                     '、'.join(x for x in (v.get('tags') or []) if x != 'email_found'), DATE, NEXT_CHECK, CHECK_ITEMS,
                     f'来源：External/{recs[code][1]}；{v["reason"][:160]}'])
        added += 1
    with open(WATCH, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(body)

    # 5) 名册小节（幂等：按标记）
    marker = f'## External 并池 · 批 {BATCH}'
    md = open(ROSTER, encoding='utf-8').read()
    if marker not in md:
        pools = [(c, v) for c, v in D.items() if v['verdict'] == 'pool']
        watch = [(c, v) for c, v in D.items() if v['verdict'] == 'pool_watch']
        keep = [(c, v) for c, v in D.items() if v['verdict'] == 'keep_C']
        n_mail = sum(1 for f in fill.values() if f['emails'])
        lines = ['', marker + f'（{DATE}，正式 {len(pools)} / 观察 {len(watch)}）', '',
                 f'> 来源：External Clients「渠道型主体但路径未建」keep_C 第二批补邮箱（`data/external_clients/xc_path_fill_{DATE}_b2.json`，每户一次检索）。'
                 f'{len(D)} 户查到邮箱 {n_mail}；按闸 2 / 闸 3 口径定：入池 ○ {len(pools)}、观察 ☆ {len(watch)}、留 C {len(keep)}（其中有邮箱 {sum(1 for c, _ in keep if fill[c]["emails"])} 户随群发节奏）。'
                 f'另 {len(GIANT)} 户巨头 / 上市 / 零售集团按规则直接留 C（`giant` / `retail`，不检索、不群发）。'
                 f'美国自动化分销多为 HMS / Red Lion / N-Tron 既有渠道 → 一律 `reg_pending`，州注册号补到即转 ★ / ○ 复核。巡检同表 `data/saga_clients/P池_巡检表_{DATE}.csv`，下次 {NEXT_CHECK}。',
                 '', '| 编号 | 档 | 公司 | 国家 | 区域组 | 来源库 | 标签 | 判语（摘） |', '|---|---|---|---|---|---|---|---|']
        for c, v in pools + watch:
            lines.append(f'| {c} | {v["star"]} | {v["company"]} | {v["country"]} | {v["group"]} | External/{recs[c][1]} | {"、".join(x for x in (v.get("tags") or []) if x != "email_found")} | {v["reason"][:140].replace("|", "｜")}… |')
        lines += ['', '留 C：' + '；'.join(f'{c} {(fill[c]["legal"] or recs[c][0]["name"])[:36]}（{v["reason"].split("：", 1)[-1][:46]}…）' for c, v in keep),
                  '', '规则判巨头 / 零售（不检索）：' + '；'.join(f'{c} {label}' for c, (_, label) in GIANT.items()), '']
        open(ROSTER, 'a', encoding='utf-8').write('\n'.join(lines))

    print(BATCH, dict(collections.Counter(v['verdict'] + (v.get('star') or '') for v in D.values())), 'giant', n_giant, dict(touched), 'watch+', added, dict(cnt))


if __name__ == '__main__':
    main()
