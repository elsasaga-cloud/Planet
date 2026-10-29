#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""External XC · 闸 2 查底数 + 闸 3 入池 批 X2-01（2026-10-29，T29-U119 评估权下放）—— x1_001.py 的 13 户候选。

口径同 Saga 闸 2 / 闸 3（方案 §6–§8）：官方注册号 / 官方分销名录 = 坐实；官网页脚 + 目录页 = 部分坐实；只查到同名 = 未坐实（留 C(2) 等追问，不强判）。
入池档位：★ = 体量 + 对位 + 登记齐；○ = 对位 + 登记齐但体量一般；△ = 有疑点（预付 100%）。
副作用（幂等）：
  · data/external_clients/sieve_x.json（verdict pool / keep_C，gate 2，facts 带 URL + 日期）
  · data/saga_clients/P池_巡检表_2026-10-29.csv 追加 External 行（备注列标「来源：External/<库>」）
  · docs/P池_资产池名册_2026-10-29.md 追加「External 并池」小节（标记来源）

用法：python3 sieve_batches_x/x2_001.py
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve_x  # noqa: E402

BATCH = 'X2-01'
DATE = '2026-10-29'
NEXT_CHECK = '2026-12-28'
ROOT = sieve_x.ROOT
WATCH = os.path.join(ROOT, 'data', 'saga_clients', f'P池_巡检表_{DATE}.csv')
ROSTER = os.path.join(ROOT, 'docs', f'P池_资产池名册_{DATE}.md')
CHECK_ITEMS = '官网改版 / 新品 / 招聘 / 社媒（LinkedIn / FB / IG）/ GitHub / 展会出席 / 新闻稿 / 域名 MX 存活'

# code: dict(verdict, star, group, reason, facts=[(what, url)], links, tags)
V = {
    'XC-M092': dict(verdict='pool', star='★', group='四主区 + 波兰', company='VIDEOR E. Hartig GmbH', country='德国', links='videor.com',
                    reason='★ 安防视频分销 20%：VIDEOR E. Hartig GmbH（Rödermark Carl-Zeiss-Str. 8；HRB 32047 Offenbach；1987 年登记 / 1975 年创立；注册资本 €870,000；营收级别 €50–100M；家族企业，GF Dominik Mizdrak；经营范围含视频技术 / 门禁 / 周界的进出口贸易）坐实；ComNet 授权分销 → PoE / 工业交换机对位；具名 KP m.schwamborn@ / m.niehus@；主区 DE',
                    facts=[('HRB 32047 Offenbach am Main · 1987-08-23 · €870,000 · VAT DE113592980 · LEI 529900I9XJZT6A9R6M34', 'https://app.implisense.com/en/companies/videor-e-hartig-gmbh-roedermark--DEYGXG2HXY63'),
                           ('Carl-Zeiss-Str. 8, 63322 Rödermark · 经营范围：视频技术 / 门禁 / 周界进出口贸易', 'https://www.northdata.com/VIDEOR+E.+Hartig+GmbH,+R%C3%B6dermark/Amtsgericht+Offenbach+am+Main+HRB+32047'),
                           ('Umsatzklasse 50–100 Mio. € · 家族企业（Hartig）· GF Dominik Mizdrak', 'https://www.wer-zu-wem.de/firma/videor.html')],
                    tags=['security_dist']),
    'XC-M118': dict(verdict='pool', star='★', group='四主区 + 波兰', company='EPTIMO S.A.', country='波兰', links='eptimo.com',
                    reason='★ ISP / 无线渠道分销 20%：EPTIMO Spółka Akcyjna（Warszawa Plac Bankowy 2；KRS 0000640183；NIP 5472148020；REGON 243394597；2016-10-03 登记；股本 802,990 zł；IT 硬件）坐实；MikroTik 官方分销 / VAD → SmartByte 管理型 + STI 对位；具名 KP maciej.wiszniewski@；波兰',
                    facts=[('KRS 0000640183 · NIP 5472148020 · REGON 243394597 · S.A. · 2016-10-03', 'https://www.wyszukiwarkakrs.pl/profile/0000640183'),
                           ('Plac Bankowy 2, 00-095 Warszawa · 股本 802 990 zł', 'https://www.gowork.pl/eptimo-s.a.,21473428/dane-kontaktowe-firmy')],
                    tags=['isp_channel']),
    'XC-M082': dict(verdict='pool', star='★', group='欧洲其他', company='ATYS-CO Kft', country='匈牙利', links='atysco.hu',
                    reason='★ 工业自动化分销 20%：ATYS-CO Korlátolt Felelősségű Társaság（Budapest Fertő u. 14；Cégjegyzékszám 01-09-462105；Adószám 12060991-2-42；1997-02-06 登记，前身 1991；净营收 4.5–6.5 bn HUF ≈ €12–16M；A+ 信用）坐实；Westermo Reseller → STI 工业对位；S 箱已群发（已触达）；sales@ + kissa@',
                    facts=[('Cégjegyzékszám 01-09-462105 · Adószám 12060991-2-42 · 1997-02-06 · 营收 6,533,503,000 HUF', 'https://www.companywall.hu/v%C3%A1llalat/atys-co-kft/MM9yv8a0'),
                           ('1107 Budapest, Fertő u. 14 · 注册资本 19,330,000 Ft · 净营收 4,520,774,100 Ft', 'https://icegtar.com/ceg/atys-co-kft/')],
                    tags=['industrial']),
    'XC-M349': dict(verdict='pool', star='★', group='欧洲其他', company='SIA "EURO DK"（LSEZ；现以 Getic 品牌运营）', country='拉脱维亚', links='eurodk.com | eurodk.lv | getic.com',
                    reason='★ ISP / 无线渠道分销 20%：SIA "EURO DK"（Liepāja Satiksmes iela 6；Reģ. Nr. 42103042138；PVN LV42103042138；2007-05-23 成立；2011 年起 MikroTik 官方分销、2013 年起 Ubiquiti 官方分销；发货 150+ 国）坐实；现以 getic.com 品牌运营 —— XC-C0175「Getic（欧洲）」同一公司，随本档；eurodk@ / sales@eurodk.lv',
                    facts=[('Reģistrācijas Nr. 42103042138 · 法定地址 Liepāja, Satiksmes iela 6 · 2007-05-23 · eurodk.com', 'https://infolapa.zl.lv/euro-dk-sia/'),
                           ('Getic 公司史：2007 EURO DK 成立 → 2011 MikroTik 官方分销 → 2013 Ubiquiti 官方分销', 'https://www.getic.com/company'),
                           ('LSEZ "EURO DK" SIA 仓库 Satiksmes iela 6 Liepāja · sales@eurodk.lv', 'https://www.eurodk.lv/lv/products/accessories')],
                    tags=['isp_channel'], merge=['XC-C0175']),
    'XC-C0490': dict(verdict='pool', star='★', group='中东 / 非洲', company='Smartplus Co. LLC', country='沙特', links='smartplus.com.sa',
                    reason='★ 安防分销 20%：Smartplus Co. LLC（Riyadh Al Laban, Al Murabba 12612；Hikvision 官方「Strategic National Distributor for Saudi Arabia」名录在册；多仓 + RMA 中心；产品目录含非管理 / 管理 / L3 / PoE 交换机）官方名录坐实（CR 号未查到 → 补证）；hello@smartplus.com.sa + +966 11 412 9 412；非主区但战略级国家分销体量',
                    facts=[('Hikvision 官方分销名录：Strategic National Distributor KSA · hello@smartplus.com.sa · +966 11 412 9 412 · Al Laban, Al Murabba, Riyadh 12612', 'https://www.hikvision.com/en/Partners/channel-partners/find-a-distributor/'),
                           ('产品目录含 Unmanaged / Managed / L3 / PoE 交换机（Hikvision 品牌）', 'https://projectsuppliers.net/en/supplier/smart-plus-co')],
                    tags=['security_dist', 'cr_pending']),
    'XC-M090': dict(verdict='pool', star='○', group='四主区 + 波兰', company='Primation Systemtechnik GmbH & Co. KG', country='德国', links='primation.de',
                    reason='○ 工业 / IT 分销 20%：Primation Systemtechnik GmbH & Co. KG（Grasbrunn Bretonischer Ring 11；HRA 78735 München；2001-09-13 登记（Kompass 称 1994 创立）；资本 €250,001；USt DE813373627；WZ 4651 IT 设备批发；0–9 人）坐实；HMS / Red Lion / N-Tron 渠道 → STI 对位；具名 KP matthias.henning@；主区 DE；体量微型 → ○',
                    facts=[('HRA 78735 Amtsgericht München · 2001-09-13 · Bretonischer Ring 11, 85630 Grasbrunn · 活跃', 'https://openregister.de/company/DE-HRA-D2601-78735'),
                           ('WZ 4651 Großhandel mit Datenverarbeitungsgeräten · 资本 250,001 EUR · USt DE813373627 · 0–9 人', 'https://de.kompass.com/c/primation-systemtechnik-gmbh-co-kg/de664373/')],
                    tags=['industrial', 'micro']),
    'XC-M119': dict(verdict='pool', star='○', group='四主区 + 波兰', company='"MARITEX" Leszek Łosin Sp.j.', country='波兰', links='maritex.com.pl | maritex.eu',
                    reason='○ 工业 / 电子元件分销 20%：„MARITEX" Leszek Łosin Spółka Jawna（Gdynia ul. Rdestowa 53D；KRS 0000880720；NIP 9581659572；REGON 221578676；经营自 2012-01-02，KRS 2021-02-02）坐实；ORing 授权工业网络分销 → STI 对位；具名 KP g.kondratowicz@ + orders@；波兰',
                    facts=[('KRS 0000880720 · NIP 9581659572 · REGON 221578676 · Gdynia Rdestowa 53D · 经营自 2012-01-02', 'https://www.bizraport.pl/krs/0000880720/maritex-leszek-losin-spolka-jawna'),
                           ('tel 58 622 89 00 · maritex.com.pl', 'https://www.krs-online.com.pl/firma/8248693-maritex-leszek-losin-sp-j')],
                    tags=['industrial']),
    'XC-M120': dict(verdict='pool', star='○', group='四主区 + 波兰', company='Tekniska Polska Przemysłowe Systemy Transmisji Danych Sp. z o.o.', country='波兰', links='tekniska.pl | westermo.pl',
                    reason='○ 工业数据传输专业分销 20%：Tekniska Polska – Przemysłowe Systemy Transmisji Danych Sp. z o.o.（Gliwice ul. Łabędzka 9/9G；KRS 0000383694；NIP 6312631825；REGON 241922862；股本 50,000 zł；代理 Westermo（Gold）/ Advantech B+B / Radiflow / Teldat 等）坐实 → STI 工业对位；具名 KP piotr.grychtol@ + handlowy@；波兰',
                    facts=[('KRS 0000383694 · NIP 6312631825 · REGON 241922862 · Łabędzka 9, 44-121 Gliwice', 'https://www.krs-online.com.pl/firma/4807000-tekniska-polska-przemyslowe-systemy-transmisji-danych-sp-z-o-o'),
                           ('品牌：Westermo / Advantech B+B SmartWorx / Radiflow / Teldat / OTN Systems · 持有 westermo.pl', 'https://www.automatyka.pl/firmy/tekniska-polska-przemyslowe-systemy-transmisji-danych-sp-z-o-o--598-1')],
                    tags=['industrial']),
    'XC-M086': dict(verdict='pool', star='○', group='欧洲其他', company='AIONA Automation GmbH', country='奥地利', links='aiona.at',
                    reason='○ 工业自动化 / IT 分销 20%：AIONA Automation GmbH（Wien；FN 408418 s；UID ATU68435749；2014-01-15 成立；经营 IT 产品贸易：可视化 / 通信 / 远程维护）坐实；HMS / Red Lion / N-Tron 分销 → STI 对位；具名 KP gz@ + office@；体量小 → ○',
                    facts=[('FN 408418 s · UID ATU68435749 · Petritschgasse 20, 1210 Wien', 'https://www.firmenabc.at/aiona-automation-gmbh_Jtfs'),
                           ('成立 2014 · Handel mit IT-Produkten im Bereich Visualisierung, Kommunikation und Fernwartung', 'https://www.herold.at/gelbe-seiten/wien/LcRxd/aiona-automation-gmbh/')],
                    tags=['industrial']),
    'XC-C0155': dict(verdict='pool', star='○', group='中东 / 非洲', company='Sapphire Trading & Marketing Ltd', country='肯尼亚', links='sapphire.co.ke',
                    reason='○ 安防分销 20%：Sapphire Trading & Marketing Ltd（Nairobi 17 Kijabe Street；官网联系页 Info@sapphire.co.ke / +254 795 705 335；ZoomInfo 11–50 人，设 Hikvision 销售经理岗；目录页另载 nishit@sapphire.co.ke）部分坐实（肯尼亚公司注册号未查到 → 补证）；Hikvision 国家分销（来源库称 1996 年起）→ PoE 对位；非主区 → 预付 100% 起步',
                    facts=[('官网联系页：Info@sapphire.co.ke · +254 795 705 335 · 17 Street, Kijabe, Nairobi', 'https://sapphire.co.ke/index.php/contact-us/'),
                           ('11–50 人 · 17 Kijabe St Nairobi · Sales Manager (Hik Vision) Robert Thuo 等', 'https://www.zoominfo.com/pic/sapphire-trading-marketing-ltd/540673424'),
                           ('Yellow Pages Kenya：nishit@sapphire.co.ke · +254722513444', 'https://www.yellowpageskenya.com/business-category/food-products/business-details/1295445-sapphire-trading-marketing-ltd')],
                    tags=['security_dist', 'prepay']),
    'XC-C1023': dict(verdict='pool', star='○', group='东亚 / 东南亚 / 大洋洲', company='IT Warehouse Distribution Inc.', country='菲律宾', links='itwarehouse.ph',
                    reason='○ ISP / WISP 渠道分销 20%：IT Warehouse Distribution Inc.（Quezon City Cubao, RedGold Building 1840 E. Rodriguez Sr. Ave；官网自述 MikroTik / Ubiquiti / RF elements / Ruijie / VSOL 分销，服务 ISP / WISP / SI / 经销商；business@itwarehouse.ph；(02) 7905-6052）官网 + 目录页部分坐实（SEC 号未查到 → 补证）→ SmartByte 管理型 + 光纤对位；SmartByte 子库来源；非主区 → 预付 100% 起步',
                    facts=[('官网：Distributor of Network and Fiber Equipment · business@itwarehouse.ph · (02) 7905-6052 · RedGold Building 1840 E. Rodriguez Sr. Ave Cubao', 'https://itwarehouse.ph/'),
                           ('IT Warehouse Distribution Inc. · Quezon City · LinkedIn / YouTube / FB / IG 链接', 'https://bpoai.ai/directory/it-warehouse-distribution-inc')],
                    tags=['isp_channel', 'prepay']),
    # ---- 留 C(2) ----
    'XC-M074': dict(verdict='keep_C', star='', group='欧洲其他', company='Pondi d.o.o.', country='克罗地亚', links='mikrotik-hrvatska.com | pondi.hr',
                    reason='坐实但微型：Pondi d.o.o.（Split Ostravska 8；OIB 62781739468；MBS 060121488；2025 营收 €418,353；主业 web hosting，MikroTik 批发为副线 mikrotik-hrvatska.com）→ 体量不够「极精华」，留 C(2) 巡检；回信或下单即转观察档',
                    facts=[('OIB 62781739468 · MBS 060121488 · 营收 418,353.21 € · 资本 2,946.45 €', 'https://provjera.hr/tvrtka/pondi-doo'),
                           ('mikrotik-hrvatska.com 经营主体 Pondi d.o.o. · prodaja@ · 021/494-000', 'https://www.mikrotik-hrvatska.com/conditions.html')],
                    tags=['micro']),
    'XC-C0157': dict(verdict='keep_C', star='', group='东亚 / 东南亚 / 大洋洲', company='LEHOANG Trading Technology Co., Ltd', country='越南', links='lehoangcctv.com',
                    reason='未坐实：一次检索只见同名（河内 LE HOANG TECHNOLOGY MST 0103242353、平定 / 头顿两家 Lê Hoàng）—— 与 HCMC lehoangcctv.com 主体对不上，不强判 → 留 C(2)，等 Simon 追问 MST 后再入池',
                    facts=[('同名户：CÔNG TY TNHH CÔNG NGHỆ LÊ HOÀNG · MST 0103242353 · Hà Nội（非 HCMC，待排除）', 'https://thuvienphapluat.vn/ma-so-thue/cong-ty-tnhh-cong-nghe-le-hoang-mst-0103242353.html')],
                    tags=['unverified']),
}


def main():
    sieve = sieve_x.load_sieve()
    recs = {r['code']: (r, repo) for r, repo in sieve_x.load_xc()}
    for code, v in V.items():
        assert code in recs, code
        cur = sieve.get(code) or {}
        assert cur.get('batch') in ('X1-01', BATCH), (code, cur.get('batch'))
        row = {'verdict': v['verdict'], 'gate': 3 if v['verdict'] == 'pool' else 2, 'rule': 'G3' if v['verdict'] == 'pool' else 'G2',
               'reason': v['reason'], 'date': DATE, 'manual': True, 'repo': recs[code][1], 'origin': 'External', 'batch': BATCH,
               'facts': [{'what': w, 'url': u, 'date': DATE} for w, u in v['facts']]}
        if v['star']:
            row['star'] = v['star']
        if v.get('tags'):
            row['tags'] = v['tags']
        sieve[code] = row
        for m in v.get('merge', []):
            assert m in recs, m
            sieve[m] = {'verdict': 'keep_C', 'gate': 2, 'rule': 'DUP', 'reason': f'与 {code} 同一公司（{v["company"]}）→ 随主档，不单独判', 'date': DATE,
                        'manual': True, 'repo': recs[m][1], 'origin': 'External', 'batch': BATCH, 'dup_of': code}
    cnt = sieve_x.save_sieve(sieve)

    # 巡检表追加（幂等：按编号去重）
    with open(WATCH, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f))
    header, body = rows[0], rows[1:]
    have = {r[0] for r in body}
    added = 0
    for code, v in V.items():
        if v['verdict'] != 'pool' or code in have:
            continue
        repo = recs[code][1]
        body.append([code, v['star'], '正式', v['company'], v['country'], v['group'], v['links'], '、'.join(v.get('tags') or []), DATE, NEXT_CHECK, CHECK_ITEMS,
                     f'来源：External/{repo}；{v["reason"][:160]}'])
        added += 1
    with open(WATCH, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(body)

    # 名册追加小节（幂等：按标记）
    marker = f'## External 并池 · 批 {BATCH}'
    md = open(ROSTER, encoding='utf-8').read()
    if marker not in md:
        pools = [(c, v) for c, v in V.items() if v['verdict'] == 'pool']
        lines = ['', marker + f'（{DATE}，正式 {len(pools)} / 观察 0）', '',
                 f'> 来源：External Clients（`External Clients/<库>/C/`，`data/external_clients/sieve_x.json`）。XC 2,254 户三闸走完：永久 pass 1,211 / 随主档 274 / 留 C 757+33+2 / 本批入池 {len(pools)}（★ {sum(1 for _, v in pools if v["star"] == "★")} / ○ {sum(1 for _, v in pools if v["star"] == "○")}）。巡检同表 `data/saga_clients/P池_巡检表_{DATE}.csv`，下次 {NEXT_CHECK}。',
                 '', '| 编号 | 档 | 公司 | 国家 | 区域组 | 来源库 | 判语（摘） |', '|---|---|---|---|---|---|---|']
        for c, v in pools:
            lines.append(f'| {c} | {v["star"]} | {v["company"]} | {v["country"]} | {v["group"]} | External/{recs[c][1]} | {v["reason"][:140].replace("|", "｜")}… |')
        lines += ['', '留 C(2)：' + '；'.join(f'{c} {v["company"]}（{v["reason"][:40]}…）' for c, v in V.items() if v['verdict'] != 'pool'), '']
        open(ROSTER, 'a', encoding='utf-8').write('\n'.join(lines))
    import collections
    print(BATCH, dict(collections.Counter(v['verdict'] + v['star'] for v in V.values())), 'watch+', added, dict(cnt))


if __name__ == '__main__':
    main()
