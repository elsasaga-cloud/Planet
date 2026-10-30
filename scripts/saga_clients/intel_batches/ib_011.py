#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-11（T29-U141 2026-10-30）· Switchtec（UK）/ BitBook（RU，PI）/ RFCOM（GR）。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-11'
ITEMS = [
    ('SB-255', '登记', 'companycheck（Companies House）：SWITCHTEC LIMITED · 01613368 · Incorporated 12 February 1982 · Active - Accounts Filed · SIC 46520 Wholesale of electronic and telecommunications equipment and parts · Brooms Road, Stone, Staffordshire ST15 0SH · Directors 8；2020-07 Switchtec Components Limited 名下一项 charge 未清', 'https://companycheck.co.uk/company/01613368/SWITCHTEC-LIMITED/companies-house-data', '1982 年起的英国工业元器件专业分销（UK franchisee for world-wide manufacturers）；研究档「11–50 人」核实为 13–15 人'),
    ('SB-255', 'KP', 'LinkedIn / contactout：Switchtec Ltd · Stone, Staffordshire · 2,353 followers · 11–50（13 on LinkedIn）· Founded 1982 · Owner Bob Lyons · National Wholesale Manager Nick Morgan · Area Sales Managers Mark Burton（North，兼技术）、Chris Hibbert（North & Scotland）、Sean Campbell（South, Wholesale）、Mark Stevens · Warehouse Manager Graham Donohoe；contactout 估营收 $7.3M', 'https://contactout.com/company/Switchtec-Ltd-66643', 'Simon 备注其「分销爱尔兰和英国，主要处理 Ethernet switch、Kyland」；老板 Bob Lyons 是决策人，区域销售网络现成'),
    ('SA-016', '登记', 'rusprofile / saby / gz-spb：ООО «Битбук» · ИНН 6623126845 · ОГРН 1186658033220（2018-04-24）· Свердловская обл., г. Нижний Тагил（ул. Юности 47А，1）· Директор Татарников Андрей Александрович · 2025 年收入 64 млн руб. · Субъект малого предпринимательства · 2020-07 起在圣彼得堡政府采购平台注册为供应商 · www.bitbuk.ru · +7(343)537-87-87', 'https://www.gz-spb.ru/gzSuppliers/ViewSupplier/15399', 'PI 成单户：下塔吉尔小型分销商（条码为主 + 网络 PoE），年收入约 64M RUB、做政府采购；主 OKVED 登记为不动产出租（经营多元）'),
    ('SB-057', '供应商/品牌关系', 'rfcom.gr：「Η RFCOM αποτελεί μία αμιγώς ελληνική και ταχέως αναπτυσσόμενη εισαγωγική εταιρεία, εξειδικευμένη στα συστήματα ασφαλείας」；代理以色列 Risco Group 报警系统；xo.gr：RFCOM.GR · 301 Lagkada Street, 561 23 Ampelokipi Thessaloniki · +30 2310 257337', 'https://rfcom.gr/el/etaireia', '塞萨洛尼基安防进口商（Risco 希腊代理）→ PoE 交换机作为安防配套的分销对位'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
