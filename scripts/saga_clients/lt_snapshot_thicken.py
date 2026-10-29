#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-T03 · 官网快照 → 加厚校正（三库通用消费端）· T29-U131 2026-10-29。

输入：data/saga_clients/site_snapshots/<编号>.json（GitHub Actions「customer-watch」每晚 02:23Z 顺手补抓；Saga S*-、External X*-、Planet 仓 P*- 同目录）
处理（只动长期客户群 A/B；每份快照按 fetched_at 只消费一次，幂等）：
  Saga   research/<code>.json：
         在线 → website_status（仅替换「待 Actions 补抓 / 快照失败 / 不可达 / 域名 xxx」类占位）、brands_seen 并集、
                site_contacts（页面公开邮箱 / 电话 / 社媒，只记证据，不改 entities 邮箱）、saga_fit 默认对位 → 快照自动对位（原值留 p1_prev）、
                deep.level 加「+ 官网快照」、mail_review.facts 追加一条 dir=查 证据（标题 + 描述 + URL + 日期）
         死 / 空 → website_status 记失败态 + snap_fails 累计（不同 fetched_at 计一次）；连续两次失败且无真回 / 无 WA 的进「打回候选」表
  External research/<code>.json（research_store）：alive / brands_seen / contacts.page_emails / evidence 追加 / round=LT-T03
  Planet  data/客户名单_Planet渠道_2026-10.csv：备注追加「快照 <状态> <日期>」
输出：data/长期客户群_快照加厚_<日期>.csv（逐户动作）+ data/长期客户群_快照打回候选_<日期>.csv（两次失败户，人工批复核，不自动打回）
用法：python3 scripts/saga_clients/lt_snapshot_thicken.py [--dry] [--snap-dir DIR] [--only CODE,CODE] [--since YYYY-MM-DD]
之后：cd scripts/saga_clients && renumber.py --snapshot-md; build.py; render.py; renumber.py --restore-dates; audit_full.py；
      python3 scripts/external_clients/render.py；cd scripts && python3 render.py；python3 scripts/lt_roster.py；python3 scripts/lt_gap_audit.py --no-dns
"""
import argparse
import ast
import csv
import glob
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
XDATA = os.path.join(ROOT, 'data', 'external_clients')
PCSV = os.path.join(ROOT, 'data', '客户名单_Planet渠道_2026-10.csv')
SNAP_DEFAULT = os.path.join(DATA, 'site_snapshots')
BATCH = 'LT-T03'
FAIL = ('unreachable', 'timeout', 'http_error', 'parked_or_empty', 'nxdomain', 'dead', 'error')
PLACEHOLDER = ('待 Actions 补抓', '快照失败', '不可达', 'unreachable', '待快照', '未知')
# 摘要器旧名 → 当前默认起手型号（都在价格主表 / HRUI 线里）
P1_MAP = {'STC-424DGGPM-280W': 'STC-424XGGPM-280W', 'STI-288GP': 'STI-288GPM'}


def _mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def valid_models():
    s = set()
    for r in csv.DictReader(open(os.path.join(ROOT, 'data', '价格主表.csv'), encoding='utf-8-sig')):
        v = (r.get('Saga对应型号') or '').strip()
        if v.startswith('ST'):
            s.add(v)
    src = open(os.path.join(HERE, 'audit_ab.py'), encoding='utf-8').read()
    m = re.search(r'HRUI_MODELS = (\{.*?\})', src, re.S)
    if m:
        s |= set(ast.literal_eval(m.group(1)))
    return s


def load_json(p):
    return json.load(open(p, encoding='utf-8'))


def dump_json(p, j):
    json.dump(j, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def ab_codes():
    """长期客户群 A/B 编号集合（三库），按当前等级。"""
    codes = {}
    for e in load_json(os.path.join(DATA, 'entities.json')):
        if e.get('grade') in ('A', 'B'):
            codes[e['code']] = ('Saga', e)
    ov = load_json(os.path.join(XDATA, 'overrides.json'))
    for repo in ('cctv', 'edgecore', 'mikrotik'):
        for r in load_json(os.path.join(XDATA, repo + '.json'))['records']:
            g = (ov.get(r.get('code')) or {}).get('grade') or r.get('grade')
            if g in ('A', 'B') and r.get('code'):
                codes[r['code']] = ('External', r)
    for r in csv.DictReader(open(PCSV, encoding='utf-8-sig')):
        g = r.get('人工定级') or r.get('评级')
        if g in ('A', 'B') and r.get('档案编号'):
            codes[r['档案编号']] = ('Planet', r)
    return codes


def thicken_saga(code, dg, ent, date, dry, valid):
    p = os.path.join(DATA, 'research', code + '.json')
    if not os.path.exists(p):
        return 'no_research'
    j = load_json(p)
    seen = j.setdefault('snap_thicken', {'consumed': []})
    if dg['fetched_at'] in seen.get('consumed', []):
        return 'already'
    acts = []
    dom = (dg.get('domains') or [''])[0]
    if dg['status'] == 'ok':
        ws = j.get('website_status') or ''
        if not ws or any(k in ws for k in PLACEHOLDER) or ws.startswith('域名 '):
            j['website_status'] = f"在线（{dom}，快照 {date}）：{dg.get('title') or dg.get('final_url') or ''}"[:200]
            acts.append('website_status')
        bs = list(j.get('brands_seen') or [])
        for b in dg.get('brands') or []:
            if b not in bs:
                bs.append(b)
        if bs != (j.get('brands_seen') or []):
            j['brands_seen'] = bs
            acts.append('brands_seen')
        sc = {'emails': (dg.get('emails') or [])[:5], 'phones': (dg.get('phones') or [])[:3], 'social': (dg.get('social') or [])[:4],
              'models_on_site': (dg.get('models') or [])[:8], 'url': dg.get('final_url') or '', 'date': date,
              'note': '官网公开页抓取（全量见 site_digest.json）；只作证据 / 路径备选，未写入群发邮箱'}
        if sc['emails'] or sc['phones'] or sc['social'] or sc['models_on_site']:
            j['site_contacts'] = sc
            acts.append('site_contacts')
        sf = j.get('saga_fit') or {}
        ap = P1_MAP.get(dg.get('auto_p1') or '', dg.get('auto_p1'))
        if sf and str(sf.get('basis', '')).startswith('默认') and ap and ap in valid:
            if ap != sf.get('p1'):
                sf['p1_prev'] = sf.get('p1')
                sf['p1'] = ap
            sf['why'] = f"{dg.get('auto_p1_why')}（{BATCH} 快照自动对位 {date}；原默认 {sf.get('p1_prev') or sf.get('p1')}）"
            sf['basis'] = f'官网快照自动对位（{BATCH}）· 人工点名时再校'
            j['saga_fit'] = sf
            mr = j.setdefault('mail_review', {})
            mr['saga_now'] = {'p1': sf['p1'], 'why': sf['why']}
            acts.append('saga_fit')
        elif sf and str(sf.get('basis', '')).startswith('默认'):
            sf['basis'] = f'默认 · 官网快照已到（{date}）无型号线索，沿用'
            j['saga_fit'] = sf
            acts.append('saga_fit.basis')
        d = j.get('deep') if isinstance(j.get('deep'), dict) else {}
        if d and not d.get('snapshot_at'):
            d['level'] = (d.get('level') or '') + f' + 官网快照（{BATCH} {date}）'
            d['snapshot_at'] = date
            j['deep'] = d
            acts.append('deep')
        facts = j.setdefault('mail_review', {}).setdefault('facts', [])
        quote = f"{dg.get('title') or ''} — {dg.get('desc') or ''}".strip(' —')[:300]
        if quote and not any(f.get('url') == dg.get('final_url') and f.get('date') == date for f in facts):
            facts.append({'date': date, 'dir': '查', 'who': f'Agent 官网快照 {BATCH}', 'quote': quote,
                          'why': '官网快照（Actions 抓取）：在线 / 业务线 / 在卖品牌证据（非邮件事实，不计真回）', 'url': dg.get('final_url') or f'https://{dom}/'})
            acts.append('facts')
        seen['last_ok'] = date
    else:
        fails = seen.setdefault('fails', [])
        if date not in fails:
            fails.append(date)
        ws = j.get('website_status') or ''
        if not ws or any(k in ws for k in PLACEHOLDER) or ws.startswith('域名 '):
            j['website_status'] = f"快照失败（{dom}：{dg.get('status_cn') or dg['status']}，{date}，第 {len(fails)} 次）"
            acts.append('website_status')
        acts.append(f"fail#{len(fails)}")
    seen['consumed'] = (seen.get('consumed') or []) + [dg['fetched_at']]
    seen['batch'] = BATCH
    if acts and not acts == ['already']:
        j['notes'] = f"{BATCH} 官网快照加厚（{date}）：{'/'.join(acts)}。\n" + (j.get('notes') or '')
    if not dry:
        dump_json(p, j)
    return '/'.join(acts) or 'nochange'


def thicken_external(code, dg, rec, date, dry, store):
    card = store.get(code)
    if not card:
        return 'no_card'
    seen = card.setdefault('snap_thicken', {'consumed': []})
    if dg['fetched_at'] in seen.get('consumed', []):
        return 'already'
    acts = []
    dom = (dg.get('domains') or [''])[0]
    if dg['status'] == 'ok':
        card['alive'] = f"在线（{dom}，快照 {date}）：{dg.get('title') or ''}"[:200]
        acts.append('alive')
        bs = list(card.get('brands_seen') or [])
        for b in dg.get('brands') or []:
            if b not in bs:
                bs.append(b)
        if bs != (card.get('brands_seen') or []):
            card['brands_seen'] = bs
            acts.append('brands_seen')
        ct = card.setdefault('contacts', {})
        if dg.get('emails') or dg.get('phones'):
            ct['page_emails'] = dg.get('emails') or []
            ct['page_phones'] = dg.get('phones') or []
            ct['page_note'] = f'官网公开页抓取 {date}；只作证据 / 路径备选'
            acts.append('contacts.page')
        ev = card.get('evidence')
        if isinstance(ev, str):
            try:
                ev = ast.literal_eval(ev)
            except Exception:
                ev = []
        ev = list(ev or [])
        if not any(e.get('kind') == '官网快照' and e.get('date') == date for e in ev):
            ev.append({'kind': '官网快照', 'claim': f"官网在线；{dg.get('title') or ''}", 'quote': (dg.get('desc') or dg.get('title') or '')[:300],
                       'url': dg.get('final_url') or f'https://{dom}/', 'date': date})
            card['evidence'] = ev
            acts.append('evidence')
        if dg.get('auto_p1'):
            card['site_p1_hint'] = {'p1': P1_MAP.get(dg['auto_p1'], dg['auto_p1']), 'why': dg.get('auto_p1_why'), 'date': date}
            acts.append('site_p1_hint')
        seen['last_ok'] = date
    else:
        fails = seen.setdefault('fails', [])
        if date not in fails:
            fails.append(date)
        card['alive'] = f"快照失败（{dom}：{dg.get('status_cn') or dg['status']}，{date}，第 {len(fails)} 次）"
        acts += ['alive', f'fail#{len(fails)}']
    seen['consumed'] = (seen.get('consumed') or []) + [dg['fetched_at']]
    card['round'] = BATCH
    card['researched_at'] = date
    card['notes'] = f"{BATCH} 官网快照加厚（{date}）：{'/'.join(acts)}。\n" + (card.get('notes') or '')
    if not dry:
        store.put(card)
    return '/'.join(acts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry', action='store_true')
    ap.add_argument('--snap-dir', default=SNAP_DEFAULT)
    ap.add_argument('--only', default='')
    ap.add_argument('--since', default='')
    a = ap.parse_args()
    now = subprocess.check_output(['date', '-u', '+%Y-%m-%d %H:%MZ']).decode().strip()
    today = now[:10]
    dg_mod = _mod('snapshot_digest', os.path.join(HERE, 'snapshot_digest.py'))
    store = _mod('research_store', os.path.join(ROOT, 'scripts', 'external_clients', 'research_store.py'))
    valid = valid_models()
    codes = ab_codes()
    only = set(x for x in a.only.split(',') if x)
    rows, cands = [], []
    pl_rows = list(csv.DictReader(open(PCSV, encoding='utf-8-sig')))
    pl_by = {r['档案编号']: r for r in pl_rows}
    pl_changed = False
    cnt = {}
    for f in sorted(glob.glob(os.path.join(a.snap_dir, '*.json'))):
        code = os.path.basename(f)[:-5]
        if code.startswith('_') or code not in codes or (only and code not in only):
            continue
        lib, rec = codes[code]
        try:
            snap = load_json(f)
        except Exception as e:
            print('skip', f, e)
            continue
        dg = dg_mod.digest_one(snap)
        date = (dg.get('fetched_at') or today)[:10]
        if a.since and date < a.since:
            continue
        if lib == 'Saga':
            act = thicken_saga(code, dg, rec, date, a.dry, valid)
            if act.startswith('fail') or '/fail#' in act:
                j = load_json(os.path.join(DATA, 'research', code + '.json'))
                st = j.get('snap_thicken') or {}
                if len(st.get('fails') or []) >= 2 and not st.get('last_ok') and not (rec.get('reply_sub') or 0) and 'WA' not in json.dumps(j.get('mail_review') or {}, ensure_ascii=False):
                    cands.append([lib, code, rec.get('name'), rec.get('country'), rec.get('grade'), dg['status'], ';'.join(st.get('fails') or []), '两次快照失败 + 无真回 / 无 WA → 复核是否打回 C 储备（可逆）'])
        elif lib == 'External':
            act = thicken_external(code, dg, rec, date, a.dry, store)
            if '/fail#' in act:
                card = store.get(code) or {}
                st = card.get('snap_thicken') or {}
                if len(st.get('fails') or []) >= 2 and not st.get('last_ok'):
                    cands.append([lib, code, rec.get('name'), rec.get('country_zh'), rec.get('grade'), dg['status'], ';'.join(st.get('fails') or []), '两次快照失败 → 复核是否打回 C 储备（可逆）'])
        else:
            r = pl_by.get(code)
            act = 'no_row'
            if r is not None:
                mark = f'快照{dg["status"]} {date}'
                if mark in (r.get('备注') or ''):
                    act = 'already'
                else:
                    r['备注'] = ((r.get('备注') or '') + f'｜{mark}' + (f'：{dg.get("title")}' if dg.get('title') else '')).strip('｜')
                    pl_changed = True
                    act = '备注'
                    if dg['status'] != 'ok' and (r.get('备注') or '').count('快照') >= 2 and 'ok' not in (r.get('备注') or ''):
                        cands.append([lib, code, r.get('公司名'), r.get('国家'), r.get('评级'), dg['status'], date, '两次快照失败 → 复核是否打回 C 储备（可逆）'])
        cnt[act.split('/')[0] if act in ('already', 'no_research', 'no_card', 'no_row', 'nochange') else ('ok' if dg['status'] == 'ok' else 'fail')] = cnt.get(act.split('/')[0] if act in ('already', 'no_research', 'no_card', 'no_row', 'nochange') else ('ok' if dg['status'] == 'ok' else 'fail'), 0) + 1
        if act not in ('already',):
            rows.append([lib, code, (rec.get('name') or rec.get('公司名') or ''), dg['status'], date, (dg.get('title') or '')[:80], dg.get('auto_p1') or '', ';'.join(dg.get('brands') or []), len(dg.get('emails') or []), act])
    if pl_changed and not a.dry:
        with open(PCSV, 'w', encoding='utf-8-sig', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=list(pl_rows[0].keys()))
            w.writeheader()
            w.writerows(pl_rows)
    if rows and not a.dry:
        out = os.path.join(ROOT, 'data', f'长期客户群_快照加厚_{today}.csv')
        new = not os.path.exists(out)
        with open(out, 'a', encoding='utf-8-sig', newline='') as fh:
            w = csv.writer(fh)
            if new:
                w.writerow(['库', '编号', '公司', '快照状态', '快照日期', '标题', '自动对位', '在卖品牌', '页面邮箱数', '动作'])
            w.writerows(rows)
    if cands and not a.dry:
        out = os.path.join(ROOT, 'data', f'长期客户群_快照打回候选_{today}.csv')
        old = list(csv.reader(open(out, encoding='utf-8-sig')))[1:] if os.path.exists(out) else []
        keys = {r[1] for r in old}
        with open(out, 'w', encoding='utf-8-sig', newline='') as fh:
            w = csv.writer(fh)
            w.writerow(['库', '编号', '公司', '国家', '等级', '最近状态', '失败日期', '建议'])
            w.writerows(old + [c for c in cands if c[1] not in keys])
    print(BATCH, now, 'dry' if a.dry else 'write', dict(cnt), 'rows', len(rows), 'cands', len(cands))
    for r in rows[:12]:
        print('  ', r[:5], r[-1])


if __name__ == '__main__':
    main()
