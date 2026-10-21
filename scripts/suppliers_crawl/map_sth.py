#!/usr/bin/env python3
"""Saga STH-xxx（CENTEC 线）↔ Hohunet 官网 S 系列：按端口签名自动对照。

输入：
  data/hohunet_site/products.json          （build.py 生成；service_ports 字段）
  data/suppliers_drive_index.json + data/suppliers_drive/_listing_centec.tsv（Drive 里出现过的 STH 型号夹）
  也可用 --sth 追加型号。
输出：
  data/hohunet_STH对照表.csv
  stdout：对照摘要（供回填 docs/suppliers/Hohunet/00-画像与资料地图.md §6）

STH 命名解码（推断，来自 Drive 型号夹与 Hohunet 端口表的互证）：
  <n><code> 串接，code：C=100G QSFP28 · QC=400G · OC=800G · QX=40G QSFP+ · DX=25G SFP28 · XF=10G SFP+ · XE=10G Base-T ·
  XP=10G Base-T PoE · VE=5G Base-T · VP=5G PoE · DE=2.5G Base-T · DP=2.5G PoE · GF=1G SFP · GE=1G Base-T · GP=1G PoE
  后缀 HSI = 双电源热插拔（≈ Hohunet -EI），SFI = 单固定电源（≈ -SI）。
"""
import csv
import json
import os
import re
import sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
rp = lambda *a: os.path.join(ROOT, *a)  # noqa

CODE = OrderedDict([  # 长码在前，避免 'QC' 被 'C' 抢
    ('QC', (400, 'F', False)), ('OC', (800, 'F', False)), ('QX', (40, 'F', False)), ('DX', (25, 'F', False)),
    ('XF', (10, 'F', False)), ('XE', (10, 'E', False)), ('XP', (10, 'E', True)), ('VE', (5, 'E', False)), ('VP', (5, 'E', True)),
    ('DE', (2.5, 'E', False)), ('DP', (2.5, 'E', True)), ('GF', (1, 'F', False)), ('GE', (1, 'E', False)), ('GP', (1, 'E', True)),
    ('C', (100, 'F', False)),
])
TOKEN_RE = re.compile(r'(\d+)(' + '|'.join(CODE) + r')')


def decode_sth(name):
    body = name.replace('STH-', '')
    suffix = ''
    m = re.search(r'-(HSI|SFI)$', body)
    if m:
        suffix = m.group(1)
        body = body[:m.start()]
    sig = []
    pos = 0
    for m in TOKEN_RE.finditer(body):
        if m.start() != pos:
            return None, suffix  # 有解不出的片段
        pos = m.end()
        n, code = int(m.group(1)), m.group(2)
        sp, media, poe = CODE[code]
        sig.append((n, sp, media, poe))
    if pos != len(body) or not sig:
        return None, suffix
    return tuple(sorted(sig)), suffix


SPEED = {'100M': 0.1, '1000M': 1, '1000MB': 1, '1G': 1, '2.5G': 2.5, '5G': 5, '10G': 10, '25G': 25, '40G': 40, '50G': 50, '100G': 100, '200G': 200, '400G': 400, '800G': 800,
         '10/100/1000MB': 1, '10/100/1000M': 1, '10/100/1000MBPS': 1}
SEG_RE = re.compile(r'(\d+)\s*[x×\*]\s*([0-9./GMB]+(?:\s*/\s*[0-9.GMB]+)*)\s*([A-Za-z+ 0-9-]*?)(?=,|;|$|\d+\s*[x×\*])')


def decode_hohunet(service_ports):
    """'24 x 10G SFP+, 2 x 100G QSFP28' → 签名。速率多档取最高档；介质 SFP/QSFP/OSFP=F，Base-T/RJ45=E；含 PoE → poe。"""
    s = (service_ports or '').replace('，', ',').replace('BaseT', 'Base-T').replace('Base T', 'Base-T')
    s = re.sub(r'\(([^)]*)\)', lambda m: ' ' + m.group(1).replace(',', ' ') + ' ', s)  # 括号内逗号不作分隔
    s = s.replace(' + ', ', ')
    sig = []
    for m in SEG_RE.finditer(s):
        n = int(m.group(1))
        speeds = [x.strip().upper().replace('MBPS', 'M') for x in m.group(2).split('/')]
        sp = max((SPEED.get(x, SPEED.get(x + 'G', 0)) for x in speeds), default=0)
        if sp == 0:
            m2 = re.search(r'([\d.]+)\s*G', m.group(2).upper())
            sp = float(m2.group(1)) if m2 else 0
        rest = m.group(3).upper()
        media = 'E' if re.search(r'BASE-T|RJ45|BASET', rest) else 'F' if re.search(r'SFP|QSFP|OSFP|FIBER', rest) else '?'
        poe = 'POE' in rest
        if n and sp:
            sig.append((n, sp, media, poe))
    return tuple(sorted(sig)) if sig else None


# 端口文本机器解不出、或官网口数与 Saga 命名有差的人工近似（都标「近似」，待 Joey 确认）
MANUAL = {
    'STH-2C6QX-HSI': ('S7606X-2Z-EI', '官网端口写法为拆分说明（6×40G QSFP+ + 2×100G QSFP28，半宽热备机）'),
    'STH-2C6QX-SFI': ('S7606X-2Z-SI', '同上，SI 档'),
    'STH-2QX4DX8XP40DP-HSI': ('S5040P-8T2Q4N-EI', '官网页端口栏只写 40×2.5G PoE++ + 10×10G PoE++，型号里 2Q4N = 2×40G + 4×25G；Saga 名写 8×10G PoE，口数差异待核'),
    'STH-4C12DX32XF-HSI': ('S5732-16N4Z-EI', '官网 32×10G SFP+ + 16×10G/25G SFP28 + 4×100G；Saga 名写 12×25G，口数差异待核'),
}


def sth_from_drive():
    names = set()
    for f in [rp('data', 'suppliers_drive_index.json'), rp('data', 'suppliers_drive', '_listing_centec.tsv')]:
        if os.path.exists(f):
            names |= set(re.findall(r'STH-[0-9A-Z]+(?:-(?:HSI|SFI))?', open(f, encoding='utf-8', errors='ignore').read()))
    for dp, dn, fn in os.walk(rp('docs', 'drive')):
        for x in fn:
            names |= set(re.findall(r'STH-[0-9A-Z]+(?:-(?:HSI|SFI))?', open(os.path.join(dp, x), encoding='utf-8', errors='ignore').read()))
    return sorted(names)


def main():
    sth = sth_from_drive()
    extra = [a for a in sys.argv[1:] if a.startswith('STH-')]
    sth = sorted(set(sth) | set(extra))
    P = json.load(open(rp('data', 'hohunet_site', 'products.json'), encoding='utf-8'))
    H = []
    for p in P:
        sig = decode_hohunet(p.get('service_ports', ''))
        H.append((p['model'], sig, p))
    rows = []
    for name in sth:
        sig, suf = decode_sth(name)
        want = {'HSI': 'EI', 'SFI': 'SI'}.get(suf, '')
        exact, loose = [], []
        if sig:
            for m, hs, p in H:
                if hs == sig:
                    (exact if (not want or m.endswith('-' + want) or m.endswith('-' + want + '-PLUS')) else loose).append(m)
        concl = '对上' if exact else ('仅端口对上（电源档不同/官网无此档）' if loose else '官网无同端口机型（Saga 专属定制或官网未列）')
        note = ''
        if not exact and name in MANUAL:
            loose = [MANUAL[name][0]] if not loose else loose
            note = MANUAL[name][1]
            concl = '近似（人工）'
        rows.append(OrderedDict([
            ('Saga型号', name), ('端口解码', ' + '.join(f"{n}×{sp:g}G{'E' if me == 'E' else 'F'}{'(PoE)' if poe else ''}" for n, sp, me, poe in sig) if sig else '（解码失败）'),
            ('电源档', {'HSI': '双电源热插拔（≈-EI）', 'SFI': '单固定电源（≈-SI）'}.get(suf, '')),
            ('Hohunet官网同端口同档', ' / '.join(exact)), ('Hohunet官网同端口异档或近似', ' / '.join(loose)),
            ('结论', concl), ('备注', note),
        ]))
    out = rp('data', 'hohunet_STH对照表.csv')
    with open(out, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator='\r\n')
        w.writeheader()
        w.writerows(rows)
    n_exact = sum(1 for r in rows if r['结论'] == '对上')
    n_loose = sum(1 for r in rows if r['结论'].startswith('仅端口'))
    n_man = sum(1 for r in rows if r['结论'].startswith('近似'))
    print(f'STH 型号 {len(rows)}：对上 {n_exact}，仅端口对上 {n_loose}，人工近似 {n_man}，无 {len(rows) - n_exact - n_loose - n_man} → {os.path.relpath(out, ROOT)}')
    for r in rows:
        print(f"  {r['Saga型号']:<28} {r['端口解码']:<45} → {r['Hohunet官网同端口同档'] or r['Hohunet官网同端口异档或近似'] or '—'}  [{r['结论']}]")
    # Hohunet 端口签名解码失败的机型（供排查）
    bad = [m for m, hs, p in H if hs is None and p.get('service_ports')]
    if bad:
        print('Hohunet service_ports 解码失败：', bad)


if __name__ == '__main__':
    main()
