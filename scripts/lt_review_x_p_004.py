#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-X02 · Planet 仓 A 级 PB-046 Data Connect Enterprise, Inc. 登记底数（T29-U131 2026-10-29，web_search 1 次）。
BBB：Data Connect Enterprise Inc，3405 Olandwood Ct, Olney, MD 20832-1447；Type of Entity: Corporation；Business Started 1/13/1989；
Business Management: Mr. Barry G Patton, Resident Agent（https://www.bbb.org/us/md/olney/profile/data-communication-equipment/data-connect-enterprise-inc-0241-236050504）。
Crunchbase / Lusha：Olney, Maryland；11–50 人；1988 年创；自产网络边缘 / 延伸 / 接入产品（ADSL2+/VDSL2、以太网交换机、延伸器、PoE、T1/E1）
（https://www.crunchbase.com/organization/data-connect-enterprise ；https://www.lusha.com/business/e32fade3f08b79f9/）。
MD SDAT 部门 ID 1 查未取 → 部分坐实。幂等。
"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PCSV = os.path.join(ROOT, 'data', '客户名单_Planet渠道_2026-10.csv')
MARK = '登记底数（LT-X02 2026-10-29）'
NOTE = (MARK + '：Maryland Corporation「Data Connect Enterprise Inc」，3405 Olandwood Ct, Olney, MD 20832-1447；Business Started 1989-01-13；'
        'Resident Agent Mr. Barry G Patton（疑东主 / 具名 KP 候选）；11–50 人；自产网络边缘 / 延伸 / 接入产品（含以太网交换机、PoE、T1/E1）→ 对位：'
        '自牌 OEM 话题 + 工业 / 商用 PoE 补线；MD SDAT 部门 ID 未取 → 部分坐实。证据 https://www.bbb.org/us/md/olney/profile/data-communication-equipment/'
        'data-connect-enterprise-inc-0241-236050504 ; https://www.crunchbase.com/organization/data-connect-enterprise ; https://www.lusha.com/business/e32fade3f08b79f9/')


def main():
    rows = list(csv.DictReader(open(PCSV, encoding='utf-8-sig')))
    n = 0
    for r in rows:
        if r['档案编号'] == 'PB-046' and MARK not in (r['备注'] or ''):
            r['备注'] = ((r['备注'] or '') + '｜' + NOTE).strip('｜')
            if 'Barry' not in (r['入口/联系方式'] or ''):
                r['入口/联系方式'] = (r['入口/联系方式'] or '') + '｜Mr. Barry G Patton（Resident Agent，BBB 2020；疑东主）'
            n += 1
    with open(PCSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print('LT-X02 PB-046', n)


if __name__ == '__main__':
    main()
