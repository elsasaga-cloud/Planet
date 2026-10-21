#!/usr/bin/env python3
"""Saga Realtek 线价格表（STC-xxx，`data/hrui_realtek_价格表_Drive2026Q3.csv`）↔ HRUI 官网产品：按端口签名 + PoE + 管理级自动对照。

输入：data/hrui_site/products.json（build.py hrui 生成；interface / brief / overview / category_slug）
输出：data/hrui_STC对照表.csv；stdout 摘要（回填 docs/suppliers/HRUI/00-画像与资料地图.md §6）

签名 = 多重集 {(口数, 速率 Gbps, 介质 F/E/C, PoE)}；USB / Console / 电源口不计。管理级：U 非网管 / W Web 网管 / M 带 Console 的 L2 网管。
"""
import csv
import json
import os
import re
import sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
rp = lambda *a: os.path.join(ROOT, *a)  # noqa

SPEED_WORD = {'GIGABIT': 1, 'FAST ETHERNET': 0.1}
SEG_RE = re.compile(r'(\d+)\s*[x×\*]\s*((?:\d+(?:\.\d+)?\s*(?:G|M)?(?:BPS)?\s*/?\s*)+|GIGABIT|10 GIGABIT)\s*([A-Z0-9+/()\- ]*?)(?=,|;|/\s*\d+\s*[x×\*]|\+\s*\d+\s*[x×\*]|$)', re.I)


def speed_of(txt):
    t = txt.upper().replace('BPS', '').replace(' ', '')
    if t.startswith('10GIGABIT'):
        return 10
    if t == 'GIGABIT':
        return 1
    best = 0
    for part in re.split(r'/', t):
        m = re.match(r'(\d+(?:\.\d+)?)(G|M)?', part)
        if not m:
            continue
        v = float(m.group(1))
        unit = m.group(2)
        if unit == 'M' or (unit is None and v >= 10 and v in (10, 100, 1000)):
            v = v / 1000
        best = max(best, v)
    return best


def decode(text):
    s = (text or '')
    s = re.sub(r'\(([^)]*)\)', lambda m: ' ' + m.group(1).replace(',', ' ').replace('+', ' ') + ' ', s)
    s = s.replace('Port+', 'Port + ').replace('ports+', 'ports + ')
    s = re.sub(r'\b(10/100/1000M)\b(?!\s*(RJ45|BASE|PoE|Ethernet|ports?))', r'\1 RJ45', s, flags=re.I)
    sig = []
    for m in SEG_RE.finditer(s):
        n = int(m.group(1))
        sp = speed_of(m.group(2))
        rest = m.group(3).upper()
        if re.search(r'USB|CONSOLE|POWER|DC\b|RESET', rest):
            continue
        if 'COMBO' in rest:
            media = 'C'
        elif re.search(r'SFP|FIBER|OPTIC', rest):
            media = 'F'
        else:
            media = 'E'
        poe = 'POE' in rest and 'BUDGET' not in rest
        if n and sp:
            sig.append((n, sp, media, poe))
    # 同速率/介质/PoE 的口合并（"4*10G RJ45 + 2*10G RJ45 uplink" ≡ "6*10G RJ45"）
    merged = OrderedDict()
    for n, sp, me, poe in sig:
        merged[(sp, me, poe)] = merged.get((sp, me, poe), 0) + n
    return tuple(sorted((n, sp, me, poe) for (sp, me, poe), n in merged.items())) if merged else None


def apply_poe_category(sig, category):
    """Saga 价格表里 PoE 网管款的规格串不写 PoE（如 STC-28GPM），按类别把最大的一组电口标成 PoE。"""
    if not sig or not re.search(r'(?<!non-)poe', category.lower()) or any(p for *_, p in sig):
        return sig
    cands = [i for i, (n, sp, me, p) in enumerate(sig) if me == 'E']
    if not cands:
        return sig
    i = max(cands, key=lambda k: sig[k][0])
    n, sp, me, _ = sig[i]
    out = list(sig)
    out[i] = (n, sp, me, True)
    return tuple(sorted(out))


def mgmt_saga(category):
    c = category.lower()
    if 'web managed' in c:
        return 'W'
    if 'managed' in c and 'unmanaged' not in c:
        return 'M'
    return 'U'


def mgmt_hrui(pr):
    text = ' '.join([pr.get('brief', ''), pr.get('overview', '')[:600], pr.get('title', '')]).lower()
    iface = (pr.get('interface') or '').lower()
    if 'console' in iface or re.search(r'\bl3 managed|\bl2\+? managed|cli', text):
        return 'M'
    if 'web' in text and 'managed' in text or 'web smart' in text or 'web-managed' in text or pr.get('category_slug') == 'managed-switch':
        return 'W'
    return 'U'


def sig_str(sig):
    return ' + '.join(f"{n}×{sp:g}G{me}{'(PoE)' if poe else ''}" for n, sp, me, poe in sig) if sig else '（解码失败）'


def main():
    P = json.load(open(rp('data', 'hrui_site', 'products.json'), encoding='utf-8'))
    H = []
    for pr in P:
        if pr.get('category_slug', '').startswith('industrial') or pr.get('category_slug') in ('poe-accessory', 'wireless-bridge', 'optical-fiber-converter'):
            continue
        src = pr.get('interface') or pr.get('brief') or ''
        sig = decode(src)
        if not sig:
            sig = decode(pr.get('ports', ''))
        H.append((pr['model'], sig, mgmt_hrui(pr), pr))
    rows = []
    with open(rp('data', 'hrui_realtek_价格表_Drive2026Q3.csv'), encoding='utf-8-sig') as f:
        saga = list(csv.DictReader(f))
    for r in saga:
        sig = apply_poe_category(decode(r['规格']), r['类别'])
        mg = mgmt_saga(r['类别'])
        poe_saga = any(p for _, _, _, p in (sig or ()))
        exact, loose = [], []
        for m, hs, hm, pr in H:
            if hs and sig and hs == sig:
                (exact if hm == mg else loose).append(f'{m}({hm})')
            elif hs and sig and tuple((n, sp, me) for n, sp, me, _ in hs) == tuple((n, sp, me) for n, sp, me, _ in sig):
                loose.append(f'{m}({hm},PoE{"✓" if any(p for *_, p in hs) else "✗"})')
        rows.append(OrderedDict([
            ('Saga型号', r['Saga型号']), ('类别', r['类别']), ('规格', r['规格']), ('Saga对外价USD_EXW', r['Saga对外价USD_EXW']),
            ('端口解码', sig_str(sig)), ('管理级', mg),
            ('HRUI官网同配置', ' / '.join(exact)), ('HRUI官网同端口异级或PoE异', ' / '.join(loose)),
            ('结论', '对上' if exact else ('近似' if loose else '官网无同配置机型')),
        ]))
    out = rp('data', 'hrui_STC对照表.csv')
    with open(out, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator='\r\n')
        w.writeheader()
        w.writerows(rows)
    n1 = sum(1 for r in rows if r['结论'] == '对上')
    n2 = sum(1 for r in rows if r['结论'] == '近似')
    print(f'Saga Realtek 价格表 {len(rows)} 行 ↔ HRUI 官网商用交换机 {len(H)} 款：对上 {n1}，近似 {n2}，无 {len(rows) - n1 - n2} → {os.path.relpath(out, ROOT)}')
    for r in rows:
        print(f"  {r['Saga型号']:<16} {r['管理级']} {r['端口解码']:<42} → {r['HRUI官网同配置'] or r['HRUI官网同端口异级或PoE异'] or '—'}")
    if '-v' in sys.argv:
        print('\nHRUI 侧签名：')
        for m, hs, hm, pr in H:
            print(f"  {m:<26} {hm} {sig_str(hs):<45} | {pr.get('interface') or pr.get('brief') or ''}"[:160])


if __name__ == '__main__':
    main()
