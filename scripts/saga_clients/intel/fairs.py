#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""展会名录 watch（第二遍 · 展会/活动 维度）：把行业展会的 10times 参展商页排进运行器文档队列，关键词 = 全部 A 户的辨识词，
命中 → ingest_watch.py 记「疑似参展」（10times 页只渲染前 ~50 家，是部分信号；人工看到命中再去官方名录核）。离线、幂等。"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
QUEUE = os.path.join(SD, 'intel_fetch_queue.json')

# (slug, 展会, 地点/月份)
FAIRS = [
    ('isaf-smart-houses', 'ISAF International / Smart Life（Istanbul，10 月）', 'TR'),
    ('intersec', 'Intersec Dubai（1 月）', 'AE'),
    ('intersec-saudi-arabia', 'Intersec Saudi Arabia（Riyadh，10 月）', 'SA'),
    ('isc-west', 'ISC West（Las Vegas，3–4 月）', 'US'),
    ('security-essen', 'Security Essen（9 月，双年）', 'DE'),
    ('ifsec-international', 'IFSEC International（London，5 月）', 'GB'),
    ('win-eurasia', 'WIN Eurasia（Istanbul，6 月）', 'TR'),
    ('sps-ipc-drives', 'SPS Nuremberg（11 月）', 'DE'),
    ('hannover-messe', 'Hannover Messe（4 月）', 'DE'),
    ('securika-moscow', 'Securika Moscow（4 月）', 'RU'),
    ('secutech', 'Secutech Taipei（5 月）', 'TW'),
    ('expo-seguridad-mexico', 'Expo Seguridad México（4 月）', 'MX'),
    ('gitex', 'GITEX Global（Dubai，10 月）', 'AE'),
    ('convergence-india', 'Convergence India（New Delhi，1 月）', 'IN'),
    ('secutech-india', 'Secutech India（Mumbai，5 月）', 'IN'),
]
GENERIC = {'security', 'systems', 'system', 'technology', 'technologies', 'solutions', 'solution', 'networks', 'network', 'group', 'international', 'limited', 'company', 'services', 'service', 'sistemleri', 'teknoloji', 'elektronik', 'güvenlik', 'guvenlik', 'bilişim', 'bilisim', 'communications', 'engineering', 'electronics', 'computer', 'wireless', 'industries', 'trading', 'global', 'digital', 'telecom', 'infotech', 'enterprises', 'private', 'corporation', 'informatics', 'vision', 'control', 'controls', 'power', 'smart', 'media', 'fiber', 'fibre'}


def tokens_for(ents):
    kw_map = {}
    for c, e in ents.items():
        if e.get('grade') != 'A':
            continue
        rs = e.get('research') or {}
        names = [str(rs.get('name_official') or ''), str(e.get('name') or '')]
        for nm in names:
            nm = re.split(r'[（(｜|/／;；,，]', nm)[0]
            for t in re.findall(r'[A-Za-zÀ-ÿĞğİıŞşÖöÜüÇç][A-Za-zÀ-ÿĞğİıŞşÖöÜüÇç\-]{5,}', nm):
                tl = t.lower()
                if tl in GENERIC or tl.endswith('.com') or len(tl) < 6:
                    continue
                kw_map.setdefault(t, c)
            # 两词组合更稳（如 "Angora Networks"）
            words = [w for w in re.findall(r'[A-Za-zÀ-ÿĞğİıŞşÖöÜüÇç][A-Za-zÀ-ÿĞğİıŞşÖöÜüÇç\-]{2,}', nm)]
            if len(words) >= 2:
                kw_map.setdefault(' '.join(words[:2]), c)
    return kw_map


def main():
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    kw_map = tokens_for(ents)
    q = json.load(open(QUEUE, encoding='utf-8')) if os.path.exists(QUEUE) else []
    have = {x['url'] for x in q}
    added = 0
    for slug, label, iso in FAIRS:
        url = f'https://10times.com/{slug}/exhibitors'
        if url in have:
            for x in q:
                if x['url'] == url:
                    x['keywords'] = sorted(kw_map)
                    x['kw_map'] = kw_map
            continue
        q.append({'code': '*', 'url': url, 'label': f'fair_{slug}', 'kind': 'html', 'fair': label, 'iso': iso, 'keywords': sorted(kw_map), 'kw_map': kw_map, 'refresh_days': 30})
        added += 1
    json.dump(q, open(QUEUE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('fairs queued +', added, 'tokens', len(kw_map), 'queue total', len(q))


if __name__ == '__main__':
    main()
