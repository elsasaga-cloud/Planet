#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-R10（Planet 3 户）· 官网快照打回候选复核（T29-U134「搞吧」2026-10-29 16:2xZ）。
来源 data/长期客户群_快照打回候选_2026-10-29.csv：PB-068 marcomweb.it（http_error ×2）、PB-084 voip.world（http_error ×2，
SafeLine WAF 拦截早已知）、PB-086 technicalreality.co.uk（unreachable ×2，首页 fetch 早已「Failed to fetch」）。
dnspython 2026-10-29 16:2xZ 复查：三域 MX / NS 均正常（见 NOTE）→ 快照失败 = 反爬 / WAF，非死域 → 留 B。
写：Planet CSV 备注追加 + data/长期客户群_复核记录.csv 追加 3 行；幂等。
"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PCSV = os.path.join(ROOT, 'data', '客户名单_Planet渠道_2026-10.csv')
LOG = os.path.join(ROOT, 'data', '长期客户群_复核记录.csv')
BATCH = 'LT-R10'
DATE = '2026-10-29'
MARK = '快照失败复核（LT-R10 2026-10-29）'
DNS = {
    'PB-068': 'marcomweb.it MX alt2/alt3/alt4.aspmx.l.google.com；A 104.21.43.15 / 172.67.215.215（Cloudflare）；NS kia/kip.ns.cloudflare.com',
    'PB-084': 'voip.world MX mx01/mx02.mxgate.org；A 185.226.241.97；NS ns.udag.org/net/de',
    'PB-086': 'technicalreality.co.uk MX technicalreality-co-uk.mail.protection.outlook.com；A 无（仅 www）；NS ns59/ns60.domaincontrol.com',
}
WHY = {
    'PB-068': '快照 http_error ×2（10-21 / 10-29）= Cloudflare 反爬',
    'PB-084': '快照 http_error ×2 = SafeLine WAF「Client Verifying」（表内早已记录）',
    'PB-086': '快照 unreachable ×2 = 站点屏蔽机器抓取（表内早已「Failed to fetch」）',
}


def main():
    rows = list(csv.DictReader(open(PCSV, encoding='utf-8-sig')))
    n = 0
    for r in rows:
        c = r['档案编号']
        if c in DNS and MARK not in (r['备注'] or ''):
            r['备注'] = ((r['备注'] or '') + '｜' + MARK + '：' + WHY[c] + '；DNS 16:2xZ ' + DNS[c] + ' → 非死域、邮箱路径在 → 留 B，不作打回依据').strip('｜')
            n += 1
    with open(PCSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print('Planet 备注', n)
    byc = {r['档案编号']: r for r in rows}
    done = {(x['编号'], x['批次']) for x in csv.DictReader(open(LOG, encoding='utf-8-sig'))}
    m = 0
    with open(LOG, 'a', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        for c in DNS:
            if (c, BATCH) in done:
                continue
            r = byc[c]
            w.writerow([c, r['公司名'], r['国家'], r['评级'], r['评级'], BATCH, DATE,
                        f'官网快照两次失败（{WHY[c]}），DNS 2026-10-29 16:2xZ 复查 {DNS[c]} → 非死域、邮箱路径未断 → 留 B 不动；快照失败只记「官网不可抓」，不作打回依据'])
            m += 1
    print('log rows', m)


if __name__ == '__main__':
    main()
