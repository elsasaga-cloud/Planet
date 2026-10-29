#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Planet 仓 129 户（profile/A|B|C，主表 data/客户名单_Planet渠道_2026-10.csv + batch/*.json）三闸筛选 → data/sieve_planet.json。

口径：docs/C池三闸筛选_方案_2026-10-29.md（Saga / External 同法，origin=Planet）。
  闸 0 刚性：① 无邮箱 / 电话 / WA 任何路径 → pass_final；② 域名 nxdomain 且无其他路径 → pass_final；③ 明确拒收 / 停发 → pass_final。
  并档：同域名 / 同 Mikrotik 旧编号命中 Saga（entities.json）或 External（cctv / edgecore / mikrotik.json）→ 随主档：
        主档已有三闸结论（sieve.json / sieve_x.json）→ 抄；主档是 A / B（未筛）→ keep（随 A/B 主档，升级讨论时一并）。
  闸 1 人工（sieve_batches_p/p1_001.py）→ 闸 2 底数（batch facts 已有注册号者直接坐实，否则 1 次检索）→ 闸 3 入池（p2_001.py）。

用法：
  python3 scripts/sieve_p.py --mx            # 129 域 MX（复用 scripts/saga_clients/mx_check.lookup）
  python3 scripts/sieve_p.py --gate0         # 闸 0 + 并档，写 data/sieve_planet.json，打印统计
  python3 scripts/sieve_p.py --queue         # 打印待闸 1 清单（供人工批）
  python3 scripts/sieve_p.py --stats
"""
import argparse
import collections
import csv
import glob
import importlib.util
import json
import os
import re
import subprocess
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'data')
CSV_PATH = os.path.join(DATA, '客户名单_Planet渠道_2026-10.csv')
BATCH_DIR = os.path.join(ROOT, 'batch')
SIEVE_P = os.path.join(DATA, 'sieve_planet.json')
MX_P = os.path.join(DATA, 'mx_check_planet_2026-10-29.json')
SAGA_ENT = os.path.join(DATA, 'saga_clients', 'entities.json')
SAGA_SIEVE = os.path.join(DATA, 'saga_clients', 'sieve.json')
EXT_DIR = os.path.join(DATA, 'external_clients')
EXT_SIEVE = os.path.join(EXT_DIR, 'sieve_x.json')
DATE = '2026-10-29'

GENERIC = {'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'live.com', 'icloud.com', 'yandex.ru', 'mail.ru', 'wp.pl', 'o2.pl', 'seznam.cz'}
GIANT_RE = re.compile(r'巨头|规模过大|决策链长|上市|集团|泛欧|大型|Group|plc|S\.A\.|Exertis|Ingram|TD Synnex|Also|Senetic|Morele|Alcadon', re.I)
REFUSE_RE = re.compile(r'拉黑|明确拒|要求停发|停止发送|unsubscribe|do not contact|不要再发|退订', re.I)


def now_z():
    return subprocess.check_output(['date', '-u', '+%H:%MZ']).decode().strip()


def domain_of(s):
    s = (s or '').strip().lower()
    s = re.sub(r'^https?://', '', s).split('/')[0].split('?')[0]
    s = s[4:] if s.startswith('www.') else s
    return s


def domains_of_row(r):
    out = []
    for part in re.split(r'[\s/;,，；]+', r.get('网站') or ''):
        d = domain_of(part)
        if d and '.' in d and d not in out:
            out.append(d)
    return out


def load_planet():
    rows = list(csv.DictReader(open(CSV_PATH, encoding='utf-8-sig', newline='')))
    bat = {}
    for p in sorted(glob.glob(os.path.join(BATCH_DIR, '*.json'))):
        b = json.load(open(p, encoding='utf-8'))
        for c in b.get('customers', []):
            bat.setdefault(c['_code'], []).append(c)
    out = []
    for r in rows:
        code = r['档案编号']
        cs = bat.get(code, [])
        contacts, facts, evidence, notes = [], {}, [], []
        mref = (r.get('Mikrotik仓库对照编号') or '').strip()
        for c in cs:
            for ct in (c.get('contacts') or []):
                if ct not in contacts:
                    contacts.append(ct)
            if isinstance(c.get('facts'), dict):
                facts.update(c['facts'])
            for ev in (c.get('evidence') or []):
                if ev not in evidence:
                    evidence.append(ev)
            if c.get('notes'):
                notes.append(str(c['notes']))
            if not mref and c.get('mikrotik_ref'):
                mref = str(c['mikrotik_ref']).strip()
        emails = []
        for ct in contacts:
            e = (ct.get('email') or '').strip().lower()
            if e and '@' in e and e not in emails:
                emails.append(e)
        for m in re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', r.get('入口/联系方式') or ''):
            if m.lower() not in emails:
                emails.append(m.lower())
        phones = [ct.get('phone') for ct in contacts if ct.get('phone')]
        phones += re.findall(r'\+?\d[\d\s()-]{6,}\d', r.get('入口/联系方式') or '')
        out.append({'code': code, 'name': r['公司名'], 'country': r['国家'], 'city': r.get('城市', ''), 'grade': r['评级'],
                    'manual_grade': (r.get('人工定级') or '').strip(), 'type': r['类型'], 'signal': r.get('信号（在卖什么品牌）', ''),
                    'status': r.get('状态', ''), 'remark': r.get('备注', ''), 'basis': r.get('评级依据', ''), 'c_sub': r.get('C级细分', ''),
                    'domains': domains_of_row(r), 'emails': emails, 'phones': phones, 'contacts': contacts, 'facts': facts,
                    'evidence': evidence, 'notes': notes, 'mik_ref': re.sub(r'[（(].*', '', mref).strip(), 'own_brand': r.get('是否自有品牌', ''),
                    'priority': r.get('优先级', ''), 'planet_url': r.get('PLANET关联证据URL', '')})
    return out


def load_json(p):
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


def load_sieve():
    d = load_json(SIEVE_P)
    d.pop('_meta', None)
    return d


def save_sieve(s):
    cnt = collections.Counter(v['verdict'] for v in s.values())
    out = {'_meta': {'updated': DATE, 'time': now_z(), 'n': len(s), 'counts': dict(cnt), 'origin': 'Planet',
                     'scheme': 'docs/C池三闸筛选_方案_2026-10-29.md（Planet 仓同法）'}}
    out.update({k: s[k] for k in sorted(s)})
    json.dump(out, open(SIEVE_P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return cnt


# ---------- 并档索引 ----------
def saga_index():
    ents = json.load(open(SAGA_ENT, encoding='utf-8'))
    by_dom = {}
    for e in ents:
        ds = e.get('domains')
        if isinstance(ds, str):
            try:
                ds = json.loads(ds.replace("'", '"'))
            except Exception:
                ds = re.findall(r"[\w.-]+\.[a-z]{2,}", ds)
        for d in ds or []:
            d = domain_of(d)
            if d and d not in GENERIC:
                by_dom.setdefault(d, e['code'])
    return by_dom


def ext_index():
    by_dom, by_src = {}, {}
    for repo in ('cctv', 'edgecore', 'mikrotik'):
        recs = load_json(os.path.join(EXT_DIR, f'{repo}.json')).get('records', [])
        for r in recs:
            if r.get('src_code'):
                by_src.setdefault((repo, r['src_code']), r['code'])
            ds = [r.get('domain')] + [domain_of(x) for x in (r.get('also') or []) if isinstance(x, str)]
            for d in ds:
                d = domain_of(d)
                if d and d not in GENERIC:
                    by_dom.setdefault(d, r['code'])
    return by_dom, by_src


def dup_lookup(r, sidx, eidx, esrc):
    """返回 (主档编号, 途径) 或 None。优先 Saga，再 External。"""
    for d in r['domains']:
        if d in sidx:
            return sidx[d], f'同域名 {d}'
    for e in r['emails']:
        d = e.split('@')[-1]
        if d not in GENERIC and d in sidx:
            return sidx[d], f'同邮箱域 {d}'
    if r['mik_ref']:
        k = ('mikrotik', r['mik_ref'])
        if k in esrc:
            return esrc[k], f'Mikrotik 旧编号 {r["mik_ref"]}'
    for d in r['domains']:
        if d in eidx:
            return eidx[d], f'同域名 {d}（External）'
    return None


def master_verdict(code):
    """主档的三闸结论：Saga C → sieve.json；External XC → sieve_x.json；A / B → ('AB', grade)。"""
    if code.startswith('SC-'):
        v = load_json(SAGA_SIEVE).get(code)
        return ('sieve', v) if v else ('none', None)
    if code.startswith(('SA-', 'SB-')):
        return ('AB', code[1])
    if code.startswith('XC-'):
        v = load_json(EXT_SIEVE).get(code)
        return ('sieve', v) if v else ('none', None)
    if code.startswith(('XA-', 'XB-')):
        return ('AB', code[1])
    return ('none', None)


# ---------- MX ----------
def run_mx():
    fake = types.ModuleType('common')
    fake.DATA = os.path.join(DATA, 'saga_clients')
    old = sys.modules.get('common')
    sys.modules['common'] = fake
    spec = importlib.util.spec_from_file_location('mx_check_saga', os.path.join(HERE, 'saga_clients', 'mx_check.py'))
    mx = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mx)
    if old is not None:
        sys.modules['common'] = old
    else:
        sys.modules.pop('common', None)
    import dns.resolver
    res = dns.resolver.Resolver()
    res.timeout = 4
    res.lifetime = 8
    doms = sorted({d for r in load_planet() for d in r['domains']} | {e.split('@')[-1] for r in load_planet() for e in r['emails'] if e.split('@')[-1] not in GENERIC})
    out = {}
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=16) as ex:
        for d, v in zip(doms, ex.map(lambda d: mx.lookup(d, res), doms)):
            out[d] = v
    json.dump({'_meta': {'date': DATE, 'time': now_z(), 'n': len(out)}, 'domains': out}, open(MX_P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('mx', len(out), collections.Counter((v or {}).get('status') for v in out.values()))


def mx_status(d, mxd):
    return ((mxd.get(d) or {}).get('status')) if d else None


# ---------- 闸 0 ----------
def gate0():
    recs = load_planet()
    mxd = load_json(MX_P).get('domains', {})
    sidx, (eidx, esrc) = saga_index(), ext_index()
    sieve = load_sieve()
    # 清掉旧的非人工闸 0 行
    for k in [k for k, v in sieve.items() if v.get('gate') == 0 and not v.get('manual')]:
        sieve.pop(k)
    rows = []
    for r in recs:
        code = r['code']
        if code in sieve and sieve[code].get('manual'):
            continue
        dup = dup_lookup(r, sidx, eidx, esrc)
        has_path = bool(r['emails'] or r['phones'])
        dead = bool(r['domains']) and all(mx_status(d, mxd) in ('nxdomain', 'dead') for d in r['domains'])
        text = ' '.join([r['remark'], r['basis'], r['status']] + r['notes'])
        row = None
        if dup:
            mcode, via = dup
            kind, mv = master_verdict(mcode)
            if kind == 'sieve':
                row = {'verdict': mv['verdict'], 'gate': 0, 'rule': 'DUP', 'dup_of': mcode,
                       'reason': f'与 {mcode} 同一公司（{via}）→ 随主档：{mv["verdict"]}（闸 {mv.get("gate")}，{str(mv.get("reason"))[:120]}）'}
            elif kind == 'AB':
                row = {'verdict': 'keep', 'gate': 0, 'rule': 'DUP-AB', 'dup_of': mcode,
                       'reason': f'与 {mcode}（{ "Saga" if mcode.startswith("S") else "External"} {mv} 级，本轮不筛 A/B）同一公司（{via}）→ 随主档，不单独判；A/B 升级讨论时一并'}
            else:
                row = {'verdict': 'keep', 'gate': 0, 'rule': 'DUP', 'dup_of': mcode, 'reason': f'与 {mcode} 同一公司（{via}），主档尚无结论 → 随主档'}
        elif REFUSE_RE.search(text):
            row = {'verdict': 'pass_final', 'gate': 0, 'rule': 'G0-3', 'reason': f'明确拒收 / 停发：{REFUSE_RE.search(text).group(0)}'}
        elif not has_path and GIANT_RE.search(' '.join([r['type'], r['basis'], r['c_sub'], r['name']])):
            row = {'verdict': 'keep_C', 'gate': 0, 'rule': 'G0-giant', 'reason': f'无邮箱 / 电话路径，但为巨头 / 大集团 / 大电商（{r["type"][:40]}）—— Simon 口径「巨头硬但不永久 pass」→ 留 C 长线不 pass（官网 {"、".join(r["domains"])}）'}
        elif not has_path:
            row = {'verdict': 'pass_final', 'gate': 0, 'rule': 'G0-1', 'reason': f'无邮箱 / 电话 / WA 任何路径（主表「入口」+ batch contacts 均空；官网 {"、".join(r["domains"]) or "无"}）'}
        elif dead and not r['phones']:
            row = {'verdict': 'pass_final', 'gate': 0, 'rule': 'G0-2', 'reason': f'域名 {"、".join(d + ":" + str(mx_status(d, mxd)) for d in r["domains"])} 全死且无电话'}
        if row:
            row.update({'date': DATE, 'origin': 'Planet', 'grade': r['grade']})
            sieve[code] = row
        rows.append((code, row))
    cnt = save_sieve(sieve)
    n_pending = sum(1 for c, row in rows if row is None and c not in sieve)
    print('gate0', len(recs), dict(cnt), '待闸 1', n_pending)
    return sieve


def queue():
    recs = load_planet()
    sieve = load_sieve()
    mxd = load_json(MX_P).get('domains', {})
    n = 0
    for r in recs:
        if r['code'] in sieve:
            continue
        n += 1
        kp = '；'.join(f'{c.get("name") or "—"}（{(c.get("role") or "")[:18]}）{c.get("email") or ""}' for c in r['contacts'][:3])
        facts = '，'.join(f'{k}:{str(v)[:30]}' for k, v in list(r['facts'].items())[:4])
        print(f"{r['code']} | {r['grade']}{('→' + r['manual_grade']) if r['manual_grade'] else ''} | {r['name'][:40]} | {r['country']} | {r['type'][:60]} | 自牌:{r['own_brand'][:12]} | {r['status'][:20]} | mx:{'/'.join(str(mx_status(d, mxd)) for d in r['domains'])} | KP:{kp[:150]} | facts:{facts[:120]} | 据:{r['basis'][:160]}")
    print('待闸 1', n)


def stats():
    s = load_sieve()
    c = collections.Counter((v.get('gate'), v['verdict']) for v in s.values())
    print('n', len(s), dict(sorted(c.items(), key=lambda x: (str(x[0][0]), x[0][1]))))
    print('dups →', collections.Counter(v.get('dup_of', '')[:2] for v in s.values() if v.get('dup_of')))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--mx', action='store_true')
    ap.add_argument('--gate0', action='store_true')
    ap.add_argument('--queue', action='store_true')
    ap.add_argument('--stats', action='store_true')
    a = ap.parse_args()
    if a.mx:
        run_mx()
    if a.gate0:
        gate0()
    if a.queue:
        queue()
    if a.stats:
        stats()
