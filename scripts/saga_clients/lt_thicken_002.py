#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-T02 · A 级「邮件证据」档官网实查 3 户（SB-1114 FikesMedia / SB-1115 Milliseconds Evolution / SB-1117 Switchcom）· T29-U131 2026-10-29。

fetch_page 实查（2026-10-29 14:38Z），原文摘录 + URL 写进研究档 evidence / signals / brands_seen / website_status；不改等级。幂等（evidence kind 'LT-T02 官网实查'）。
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA  # noqa: E402

R = os.path.join(DATA, 'research')
DATE = '2026-10-29'
KIND = 'LT-T02 官网实查'
FACTS = {
    'SB-1117': {
        'website_status': '在线（Shopify 网店 www.switchcom.co.za；2026-10-29 实查）',
        'type': '网络设备分销商（ICT 分销：无线 / 网络 / VoIP / 监控 / 光纤；服务 reseller / installer / ISP / WISP / 终端；Shopify 网店）',
        'brands_seen': ['Cambium Networks', 'Hikvision', 'MikroTik', 'Ubiquiti', 'Siklu', 'ALGcom', 'Fanvil', 'TP-Link', 'Extralink', 'Mercusys', 'Tenda', 'Huawei eKit'],
        'evidence': [{'kind': KIND, 'claim': '2015 年创立的 ICT 分销商；无线 / 网络 / VoIP / 监控 / 光纤五条线；客户 = reseller / installer / ISP / WISP / 终端；bulk purchasing + price match',
                      'quote': 'Switchcom Distribution is a dynamic and innovative ICT distributor founded in 2015 … Wireless, Networking, VoIP, Surveillance and Fibre sectors … sales, distribution, technical support and financing for resellers, installers, ISPs, WISPs and end users. Our product portfolio consists of top international brands such as Cambium Networks, Hikvision, MikroTik, Ubiquiti and more.',
                      'url': 'https://www.switchcom.co.za/', 'date': DATE}],
        'signals': ['官网首页品牌墙：Huawei eKit / Siklu / ALGcom / MikroTik / Fanvil / Ubiquiti / TP-Link / Extralink / Hikvision / Mercusys / Tenda + 自有配件线「Switchcom Distribution」（2026-10-29）→ 走量分销 + 自有配件标 = 20% 档 + 贴牌话题可谈',
                    'Best sellers 全是 Ubiquiti airMAX CPE（WISP 客群）→ 对位 = WISP 汇聚 PoE（STC-228GP / STC-2224GP）而不是企业核心'],
    },
    'SB-1115': {
        'website_status': '域名在线但无站点内容（millievolution.com = Apache「Index of /」目录列表，仅 cgi-bin/ 2025-10-31；2026-10-29 实查）',
        'evidence': [{'kind': KIND, 'claim': '官网无内容：Apache 默认目录列表，只有 cgi-bin/（2025-10-31）', 'quote': 'Index of / … cgi-bin/ 2025-10-31 13:16',
                      'url': 'https://millievolution.com/', 'date': DATE}],
        'risks': ['新公司（Companies House 2025-10-24 注册）+ 官网空站（2026-10-29）→ 对外一切以邮件往来与 Companies House 为准；不要在信里引用其官网'],
    },
    'SB-1114': {
        'website_status': '在线（Google Sites www.fikesmedia.com；2026-10-29 实查）',
        'type': 'IT 集成 / 网络顾问（一人公司；客群 = 地方政府 / K-12 与高校 / SMB；方案 = 企业网络、数据中心网络、VoIP、MikroTik 咨询）',
        'evidence': [{'kind': KIND, 'claim': '客群三块：地方政府（图书馆 / 市政厅 / 警局）、K-12 与高校、SMB；方案四块：Enterprise Networking / Datacenter Networking（ToR、VXLAN）/ Open Voice（VoIP）/ Network Consulting（MikroTik consulting 页）',
                      'quote': "It's about function, not vendors. … Datacenter Networking: High speed throughput, top of rack connectivity, VXLAN, or a custom solution. … Network Consulting … /mikrotik-consulting",
                      'url': 'https://www.fikesmedia.com/', 'date': DATE}],
        'signals': ['「function, not vendors」+ 自建数据中心网络页（ToR / VXLAN）→ 对白牌 Marvell 管理型 + 10G 上联接受度高；MikroTik 顾问身份 = 懂 CLI / SNMP，回信时直说 SNMP + CLI 自动化可做、REST 云控不做（见 notes）'],
    },
}


def main():
    n = 0
    for code, f in FACTS.items():
        p = os.path.join(R, f'{code}.json')
        j = json.load(open(p, encoding='utf-8'))
        if any(e.get('kind') == KIND for e in j.get('evidence') or []):
            continue
        j['website_status'] = f['website_status']
        if f.get('type'):
            j['type'] = f['type']
        if f.get('brands_seen'):
            j['brands_seen'] = sorted(set((j.get('brands_seen') or []) + f['brands_seen']))
        j['evidence'] = (j.get('evidence') or []) + f['evidence']
        if f.get('signals'):
            j['signals'] = (j.get('signals') or []) + f['signals']
        if f.get('risks'):
            j['risks'] = (j.get('risks') or []) + f['risks']
        j['deep'] = {'done_at': DATE, 'level': '邮件证据 + 官网实查 v1（LT-T02）', 'batch': 'LT-T02'}
        j['notes'] = f'LT-T02 官网实查（{DATE}）：见 evidence「{KIND}」。\n' + (j.get('notes') or '')
        json.dump(j, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        n += 1
    print('LT-T02', n)


if __name__ == '__main__':
    main()
