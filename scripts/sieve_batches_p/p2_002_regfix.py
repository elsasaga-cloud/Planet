#!/usr/bin/env python3
"""P 池 · 注册号补证 批 P2-02（2026-10-29，T29-U120 续）。幂等：按标记「补证 P2-02」判断是否已写。

对象 = 入池时标 reg_pending / cr_pending / prepay 的 6 户（Planet 3 + External 3），各做 1 次检索（2026-10-29，never re-search）：
  PB-020 Jlinks        → BC 公司注册公报 2005-10-27 INCORPORATIONS「0738462 JLINKS TECHNOLOGY CORP.」→ 坐实，去 reg_pending
  PB-052 STS Lab       → SAM.gov 联邦供应商登记 UEI KXVVK8PBDD75 / CAGE 7ERG8（S-Corp，2015-07-14 起，有效至 2027-03-13；51–250 人；$10–50M 估）→ 坐实，去 reg_pending
  PC-011 Akçaba        → 法人名「Akçaba Ltd.」（kimibilin.com 名录）；TRNC 登记号仍无公开库 → 保留 reg_pending，补法人名
  XC-C0490 Smartplus   → D&B「SMART PLUS CO」Riyadh King Faisal Rd Al Murabba, PO Box 54210, 50 人, $3.26M, CEO Mohammed Alsultan → CR 号仍无 → 保留 cr_pending
  XC-C0155 Sapphire    → TradeAtlas「SAPPHIRE TRADING & MARKETING LTD.」P.O. Box 31177-00100 Nairobi；businesslist.co.ke 2011 起在册 → 法人名坐实，登记号仍无 → 保留 prepay
  XC-C1023 IT Warehouse→ bpoai.ai 名录：REDGOLD Building 1840 E Rodriguez Sr. Ave, Cubao, QC 1102，+63 2 8277 7898 → SEC 号仍无 → 保留 prepay
结论 / 档位不改（评估权下放 PR-02-64，入池判语不回炉）；只补事实、改标签、追加巡检表备注与名册备注。
"""
import csv
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'data', 'sieve_planet.json')
SX = os.path.join(ROOT, 'data', 'external_clients', 'sieve_x.json')
CSV = os.path.join(ROOT, 'data', 'saga_clients', 'P池_巡检表_2026-10-29.csv')
MD = os.path.join(ROOT, 'docs', 'P池_资产池名册_2026-10-29.md')
MARK = '补证 P2-02'
D = '2026-10-29'

FIX = {
    'PB-020': dict(file='planet', drop=['reg_pending'], add=['small'],
                   note='BC 公司注册公报 2005-10-27 INCORPORATIONS 列「0738462 JLINKS TECHNOLOGY CORP.」→ 登记坐实；ContactOut 列 1–10 人（弱证）→ 标 small，试单起步',
                   facts=[('BC Corporate Registry Notices 2005-10-27 · INCORPORATIONS · 0738462 JLINKS TECHNOLOGY CORP.', 'https://www.bclaws.gov.bc.ca/civix/document/id/corpreg/corpreg/crpn1027fin0905'),
                          ('ContactOut：328-13988 Cambie Rd Richmond BC · 1–10 人 · 门店 Richmond + St-Laurent QC', 'https://contactout.com/company/JLINKS-Technology-Corp-23388'),
                          ('ImportGenius：进口商记录 JLINKS TECHNOLOGY CORP 328-13988 Cambie Road Richmond BC', 'https://www.importgenius.com/importers/jlinks-technology-corp')]),
    'PB-052': dict(file='planet', drop=['reg_pending'], add=['fed_vendor'],
                   note='SAM.gov 联邦供应商登记：STS Lab, Inc. dba CCTV.Net，UEI KXVVK8PBDD75 / CAGE 7ERG8，S-Corp，2015-07-14 登记、有效至 2027-03-13，NAICS 423440，自报 51–250 人 / $10–50M → 登记坐实（体量口径以 SAM 自报为准，D&B $2.61M 为模型值）',
                   facts=[('GovTribe（SAM.gov）：STS Lab, Inc. DBA Cctv.net · UEI KXVVK8PBDD75 · CAGE 7ERG8 · 16037 Arminta St Van Nuys · S-Corp · 2001 创 · 51–250 人', 'https://govtribe.com/vendors/sts-lab-inc-dot-cctv-dot-net-7erg8'),
                          ('VIVOTEK Where to Buy：STS Lab, Inc. (CCTV.Net) 16037 Arminta St · +1 888 369 2288', 'https://www.vivotek.com/en-US/where-to-buy?area_eq=North+America'),
                          ('Bloomberg 私企档：STS Lab Inc · security dealers · 服务加州客户', 'https://www.bloomberg.com/profile/company/0443977D:US')]),
    'PC-011': dict(file='planet', drop=[], add=[],
                   note='法人名「Akçaba Ltd.」（Akcaba Communications；kimibilin.com 名录：Tuna Sk No 4 Lefkoşa 99010，info@akcaba.com，+90 392 229 15 15）；TRNC 公司登记无公开检索库 → reg_pending 保留，首单仍预付',
                   facts=[('kimibilin.com：Akçaba Ltd. (Akcaba Communications) · Tuna Sk No 4 Lefkoşa 99010 · info@akcaba.com · +90 392 229 15 15', 'https://kimibilin.com/f/akcaba-ltd/')]),
    'XC-C0490': dict(file='external', drop=[], add=[],
                     note='D&B：SMART PLUS CO，King Faisal Road Al Murabba, PO Box 54210 Riyadh 11514，50 人，$3.26M，CEO Mohammed Alsultan；Hikvision 官方名录在册 → 实体坐实、CR 号仍未公开 → cr_pending 保留',
                     facts=[('D&B：SMART PLUS CO · Riyadh · 50 人 · $3.26M · Key Principal Mohammed Alsultan (CEO)', 'https://www.dnb.com/business-directory/company-profiles.smart_plus_co.36049126c688f99c8936bce033f0d6ca.html'),
                            ('Hikvision Find a Distributor：Smartplus Co. LCC · Strategic National Distributor KSA · hello@smartplus.com.sa · +966 11 412 9 412', 'https://www.hikvision.com/en/Partners/channel-partners/find-a-distributor/')]),
    'XC-C0155': dict(file='external', drop=[], add=[],
                     note='TradeAtlas 贸易数据登记名「SAPPHIRE TRADING & MARKETING LTD.」P.O. Box 31177-00100 Nairobi；businesslist.co.ke 2011 起在册（Opp Text Book Centre Kijabe St，+254-20-2224566）→ 法人名坐实、肯尼亚登记号仍无 → prepay 保留',
                     facts=[('TradeAtlas：SAPPHIRE TRADING & MARKETING LTD. · 31177 00100 Nairobi', 'https://app.tradeatlas.com/en/firms/sapphire-trading-and-marketing-limited/f2e20e7ee3c268ec'),
                            ('BusinessList.co.ke：Sapphire Trading & Marketing Ltd · Opp Text Book Centre Kijabe St · +254-20-2224566 · 2011-08-30 登录', 'https://www.businesslist.co.ke/company/3971/sapphire-tradingmarketing-ltd')]),
    'XC-C1023': dict(file='external', drop=[], add=[],
                     note='bpoai.ai 名录：IT Warehouse Distribution Inc.，REDGOLD Building 1840 E Rodriguez Sr. Ave, Cubao, Quezon City 1102，+63 2 8277 7898（Google 评分 4.5 / 100）→ 地址二次印证、SEC 号仍无 → prepay 保留',
                     facts=[('bpoai.ai：IT Warehouse Distribution Inc. · REDGOLD Building 1840 E Rodriguez Sr. Ave Cubao QC 1102 · +63 2 8277 7898', 'https://bpoai.ai/directory/it-warehouse-distribution-inc')]),
}


def main():
    sp = json.load(open(SP, encoding='utf-8'))
    sx = json.load(open(SX, encoding='utf-8'))
    n = 0
    for code, fx in FIX.items():
        row = (sp if fx['file'] == 'planet' else sx)[code]
        if MARK in row['reason']:
            continue
        tags = [t for t in (row.get('tags') or []) if t not in fx['drop']] + [t for t in fx['add'] if t not in (row.get('tags') or [])]
        row['tags'] = tags
        row['reason'] = row['reason'] + f'｜{MARK}（{D}）：{fx["note"]}'
        row.setdefault('facts', []).extend({'what': w, 'url': u, 'date': D} for w, u in fx['facts'])
        n += 1
    json.dump(sp, open(SP, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(dict(sorted(sx.items(), key=lambda kv: (kv[0] != '_meta', kv[0]))), open(SX, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)   # 与 sieve_x.py save 同格式
    # 巡检表：标签列 + 备注列
    rows = list(csv.DictReader(open(CSV, encoding='utf-8-sig')))
    cols = list(rows[0].keys())
    m = 0
    for r in rows:
        fx = FIX.get(r['编号'])
        if not fx or MARK in r['备注']:
            continue
        tags = [t for t in re.split(r'[、,]', r['标签']) if t and t not in fx['drop']] + [t for t in fx['add'] if t not in r['标签']]
        r['标签'] = '、'.join(tags)
        r['备注'] = r['备注'] + f'｜{MARK}：{fx["note"]}'
        m += 1
    with open(CSV, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    # 名册：对应行末尾追加
    md = open(MD, encoding='utf-8').read()
    lines = md.split('\n')
    k = 0
    for i, ln in enumerate(lines):
        mm = re.match(r'^\| (P[ABC]-\d{3}|X[ABC]-[A-Z]\d{4}) \|', ln)
        if mm and mm.group(1) in FIX and MARK not in ln:
            cells = ln.rstrip().rstrip('|').rstrip()
            lines[i] = cells + f'｜{MARK}：{FIX[mm.group(1)]["note"].replace("|", "／")} |'
            k += 1
    open(MD, 'w', encoding='utf-8').write('\n'.join(lines))
    print(f'P2-02 regfix sieve {n} / csv {m} / md {k}')


if __name__ == '__main__':
    main()
