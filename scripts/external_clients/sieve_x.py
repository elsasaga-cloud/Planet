#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T29-U119 · External XC 池三闸筛选（与 Saga C 同法）· 闸 0 刚性机筛 + 状态落盘。

方案：docs/C池三闸筛选_方案_2026-10-29.md（§2 闸 0 三条刚性规则；§10 闸 3）—— External 4,351 户与 Saga 同池，origin=External。
对象：External Clients 现判 XC（人工改级 > 研究卡 > 导入初判）= CCTV-PoE 1,671 + mikrotik-info 353 + Edgecore 109 = 2,133。
数据：data/external_clients/sieve_x.json  {code: {verdict, gate, rule, reason, date, repo, origin, dup_of?}}
      verdict ∈ pass_final | keep_C | candidate | pool_candidate | pool | pool_watch
      data/external_clients/mx_check_x_<日期>.json（DNS MX / A，复用 scripts/saga_clients/mx_check.py 的 lookup / classify）

用法：
  python3 sieve_x.py --mx                 # 查 XC 全部域名 MX / A（dnspython；--only-missing 只补新域）
  python3 sieve_x.py --gate0              # 闸 0 机筛 → sieve_x.json + docs/requirements/XC池闸0_机筛报告_<日期>.md
  python3 sieve_x.py --stats

闸 0 只认三条刚性规则（Simon U117）：G0-1 无任何联系路径 / G0-2 退信（全部邮箱停用）且域名全死 / G0-3 明确拒绝。
例外（一律不进闸 0，留闸 1 人判）：与 Saga 重叠（随 Saga 档结论）/ S 箱已群发或有回信 / 乌克兰 / 展会档 / OEM 品牌商。
"""
import argparse
import collections
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import DATA, ROOT, GENERIC, domain_of  # noqa: E402  （external_clients/common.py；saga 侧同名模块不进 sys.path）
from research_store import all_cards  # noqa: E402

TODAY = dt.date.today().isoformat()
REQ = os.path.join(ROOT, 'docs', 'requirements')
SIEVE_PATH = os.path.join(DATA, 'sieve_x.json')
MX_PATH = os.path.join(DATA, f'mx_check_x_{TODAY}.json')
SAGA_SIEVE = os.path.join(ROOT, 'data', 'saga_clients', 'sieve.json')
REPOS = [('cctv.json', 'CCTV-PoE'), ('edgecore.json', 'Edgecore'), ('mikrotik.json', 'mikrotik-info')]
DEAD = {'nxdomain', 'dead'}
EMAIL_RE = re.compile(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}')
URL_RE = re.compile(r'https?://|www\.|\b[a-z0-9-]+\.(?:com|net|org|io|co|biz|info|eu|de|uk|fr|it|es|pl|tr|nl|se|ae|sa|in|vn|cz|ru|kz|ua|br|mx|ca|au|za|tw|jp|kr|ch|at|be|pt|gr|ro|hu|sk|bg|lt|lv|ee|fi|no|dk|ie|il|qa|om|kw|bh|eg|ma|ng|ke|th|my|sg|id|ph|pk|bd|lk|ar|cl|co\.uk|com\.tr|com\.au|co\.za|com\.br|com\.mx|co\.in|com\.vn|com\.sa|com\.pl|com\.ua)\b')
PHONE_RE = re.compile(r'\+?\(?\d[\d\s\-().]{5,}\d')
PLATFORM_RE = re.compile(r'whatsapp|wa\.me|linkedin|telegram|skype|wechat|微信|viber|facebook\.com|instagram\.com', re.I)
REFUSE_RE = re.compile(r'拉黑|要求停发|不要再发|unsubscribe|remove (me|us) from|do not contact|stop (e-?mailing|sending)', re.I)
UA_RE = re.compile(r'乌克兰|Ukrain', re.I)


def now_z():
    return subprocess.check_output(['date', '-u', '+%H:%MZ']).decode().strip()


def load_overrides():
    p = os.path.join(DATA, 'overrides.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


def final_grade(r, ov, cards):
    o = ov.get(r['code'])
    if o:
        return o['grade']
    c = cards.get(r['code'])
    if c:
        return c['grade_final']
    return r['grade']


def load_xc():
    ov, cards = load_overrides(), all_cards()
    out = []
    for fn, repo in REPOS:
        d = json.load(open(os.path.join(DATA, fn), encoding='utf-8'))
        for r in d['records']:
            if r.get('grade') == 'DELETE':
                continue
            if final_grade(r, ov, cards) == 'C':
                out.append((r, repo))
    return out


def load_sieve():
    return json.load(open(SIEVE_PATH, encoding='utf-8')) if os.path.exists(SIEVE_PATH) else {}


def save_sieve(s):
    rows = {k: v for k, v in s.items() if k != '_meta'}
    cnt = collections.Counter(v.get('verdict') for v in rows.values())
    s['_meta'] = {'updated': TODAY, 'time': now_z(), 'n': len(rows), 'counts': dict(cnt), 'origin': 'External',
                  'scheme': 'docs/C池三闸筛选_方案_2026-10-29.md（External XC 同法）'}
    with open(SIEVE_PATH, 'w', encoding='utf-8') as f:
        json.dump(dict(sorted(s.items(), key=lambda kv: (kv[0] != '_meta', kv[0]))), f, ensure_ascii=False, indent=0)
    return cnt


def load_mx():
    if os.path.exists(MX_PATH):
        return json.load(open(MX_PATH, encoding='utf-8'))
    import glob
    fs = sorted(glob.glob(os.path.join(DATA, 'mx_check_x_*.json')))
    return json.load(open(fs[-1], encoding='utf-8')) if fs else {'domains': {}, 'households': {}}


CARDS = {}


def text_of(r):
    card = CARDS.get(r['code'])
    parts = [json.dumps(card, ensure_ascii=False) if card else '', r.get('raw') or '', r.get('contact_text') or '', r.get('kp_text') or '', r.get('evidence_text') or '',
             r.get('entry_contact') or '', r.get('entry_point') or '', ' '.join(r.get('evidence_urls') or []),
             json.dumps(r.get('kv') or {}, ensure_ascii=False), json.dumps(r.get('notes') or '', ensure_ascii=False),
             json.dumps(r.get('r_notes') or '', ensure_ascii=False), json.dumps(r.get('facts') or '', ensure_ascii=False)]
    for a in r.get('also') or []:
        parts.append(a.get('raw') or '')
    return '\n'.join(p for p in parts if p)


def domains_of(r):
    ds = []
    for d in (r.get('domain'), domain_of(r.get('website'))):
        if d and '.' in d:
            ds.append(d.lower())
    for e in (r.get('emails') or []):
        a = (e.get('addr') if isinstance(e, dict) else e) or ''
        a = a.split('@')[-1].lower().strip() if '@' in a else ''
        if a and a not in GENERIC:
            ds.append(a)
    return list(dict.fromkeys(ds))


def hist_signals(r, text):
    sig = []
    if r.get('touch'):
        t = r['touch']
        sig.append(f"S箱触达(去{t.get('去信', '?')}/来{t.get('来信', '?')})")
    st = str(r.get('stage') or '')
    if st.startswith('02') or 'replied' in st:
        sig.append('有回信')
    fl = r.get('flags') or []
    for k in ('S箱已群发', '展会档', 'OEM品牌商', 'PlanetUSA', 'smartbyte子库'):
        if k in fl:
            sig.append(k)
    if any(str(k).startswith('展会:') for k in fl):
        sig.append('展会参展')
    fu = r.get('followups') or []
    if len(fu) > 2 or any('回' in str(x) and '未联系' not in str(x) for x in fu[1:]):
        sig.append('跟进记录')
    if r.get('phones'):
        sig.append('有电话')
    if PLATFORM_RE.search(text):
        sig.append('平台/WA线索')
    return sig


def run_mx(only_missing, workers):
    import dns.resolver  # noqa
    import importlib.util
    import types
    # 复用 saga_clients/mx_check.py 的 lookup / classify / PUBLIC_SUFFIX：它 `from common import DATA` 会撞本目录 common → 先塞一个假 common 再加载
    spec = importlib.util.spec_from_file_location('saga_mx_check', os.path.join(HERE, '..', 'saga_clients', 'mx_check.py'))
    mx_check = importlib.util.module_from_spec(spec)
    saved = sys.modules.get('common')
    fake = types.ModuleType('common')
    fake.DATA = os.path.join(ROOT, 'data', 'saga_clients')
    sys.modules['common'] = fake
    try:
        spec.loader.exec_module(mx_check)
    finally:
        if saved is not None:
            sys.modules['common'] = saved
    hh, doms = {}, set()
    for r, _ in load_xc():
        ds = [d for d in domains_of(r) if d not in mx_check.PUBLIC_SUFFIX]
        if ds:
            hh[r['code']] = ds
            doms.update(ds)
    old = load_mx()
    res = dict(old.get('domains') or {})
    todo = sorted(d for d in doms if not (only_missing and d in res))
    resolver = dns.resolver.Resolver()
    resolver.timeout = 3
    resolver.lifetime = 6
    print(f'XC households {len(hh)} domains {len(doms)} todo {len(todo)}', flush=True)
    done = 0
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(mx_check.lookup, d, resolver): d for d in todo}
        for f in cf.as_completed(futs):
            d = futs[f]
            try:
                res[d] = f.result()
            except Exception as e:  # noqa
                res[d] = {'mx': [], 'a': [], 'status': 'error:' + type(e).__name__, 'cls': '', 'checked': TODAY}
            done += 1
            if done % 100 == 0:
                print(done, flush=True)
    st = collections.Counter(v['status'] for v in res.values())
    cl = collections.Counter(v.get('cls') for v in res.values() if v.get('cls'))
    meta = {'checked': TODAY, 'time': now_z(), 'source': 'DNS MX/A 查询（dnspython，沙箱解析器；复用 saga_clients/mx_check.py）', 'scope': 'External XC 2,133',
            'domains': len(res), 'households': len(hh), 'status_counts': dict(st), 'class_counts': dict(cl.most_common())}
    json.dump({'_meta': meta, 'domains': res, 'households': hh}, open(MX_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(json.dumps(meta, ensure_ascii=False, indent=1))


def gate0(recs, mx, saga_sieve):
    D, HH = mx.get('domains', {}), mx.get('households', {})
    hits, exceptions, suggest, dups = [], [], [], []
    for r, repo in recs:
        code = r['code']
        text = text_of(r)
        tn = text.lower()
        live_emails = [e for e in (r.get('emails') or []) if (e.get('status') if isinstance(e, dict) else '') != '停用']
        all_emails = r.get('emails') or []
        ds = HH.get(code) or domains_of(r)
        st = [D[d]['status'] for d in ds if d in D]
        all_dead = bool(st) and all(x in DEAD for x in st)
        has_email = bool(live_emails) or bool(EMAIL_RE.search(tn))
        has_phone = bool(r.get('phones')) or any(len(re.sub(r'\D', '', m.group(0))) >= 7 for m in PHONE_RE.finditer(text))
        has_web = bool(ds) or bool(URL_RE.search(tn))
        has_platform = bool(PLATFORM_RE.search(text))
        sig = hist_signals(r, text)
        ua = bool(UA_RE.search(r.get('country_zh') or '') or UA_RE.search(r.get('country_text') or ''))
        # 与 Saga 重叠：随 Saga 档，不单独判
        if r.get('saga_dup'):
            sd = r['saga_dup']
            sv = saga_sieve.get(sd.get('code')) or {}
            dups.append((r, repo, sd, sv))
            continue
        # 第 2 步研究卡判「与 X?-?### 同一公司 → 并线」：随主档，不单独判
        card = CARDS.get(code)
        gr = (card or {}).get('grade_reason_final') or ''
        m = re.search(r'与\s*(X[ABC]-[A-Z]\d{3,4})', gr) if ('并线' in gr or '同一公司' in gr) else None
        if m:
            dups.append((r, repo, {'code': m.group(1), 'grade': 'X', 'via': '研究卡并线'}, {}))
            continue
        rule = reason = None
        if not has_email and not has_phone and not has_web and not has_platform:
            rule = 'G0-1'
            fl = r.get('flags') or []
            if '终端触点' in fl:
                reason = '来源库「终端触点」= 文档里提到的终端 / 市场主体名称（商场、球场、连锁、项目），原文无邮箱、电话、网址、WA 等任何联系线索'
            else:
                reason = '仅有公司 / 组织名称，原文（含 kv / 备注 / 多处出现）无邮箱、电话、网址、WA 等任何联系线索'
        elif all_emails and not live_emails and all_dead and not has_phone and not has_platform:
            rule = 'G0-2'
            reason = '全部邮箱已标停用 / 退信；' + '、'.join(f'{d} {D[d]["status"].upper()}' for d in ds if d in D) + '；无电话、无 WA'
        elif REFUSE_RE.search(text):
            m = REFUSE_RE.search(text)
            ctx = text[max(0, m.start() - 30):m.end() + 20].replace('\n', ' ')
            rule, reason = 'G0-3', f'原文「…{ctx.strip()}…」—— 明确拒绝 / 要求停发'
        if rule:
            blockers = list(sig)
            if ua:
                blockers.append('乌克兰（守界，不进闸 0）')
            if blockers:
                exceptions.append((r, repo, rule, reason, blockers))
            else:
                hits.append((r, repo, rule, reason))
        elif all_dead and not live_emails and not has_phone and not has_platform and not sig and not ua:
            suggest.append((r, repo, '、'.join(f'{d} {D[d]["status"].upper()}' for d in ds if d in D)))
    return hits, exceptions, suggest, dups


def md(s):
    return str(s or '').replace('|', '\\|').replace('\n', ' ')


def write_report(hits, exceptions, suggest, dups, n_c, mx, path):
    ts = now_z()
    cnt = collections.Counter(rule for _, _, rule, _ in hits)
    by_repo = collections.Counter(repo for _, repo, _, _ in hits)
    by_cty = collections.Counter((r.get('country_zh') or '未填') for r, _, _, _ in hits)
    L = [f'# External XC 池 · 闸 0 刚性机筛报告（{TODAY}）', '',
         f'> 生成 {ts} · 输入 `data/external_clients/{{cctv,edgecore,mikrotik}}.json`（现判 XC {n_c:,} 户）+ `mx_check_x_{TODAY}.json`（DNS MX/A，{len(mx.get("domains", {}))} 域）'
         f' · 规则与 Saga C 完全相同（`docs/C池三闸筛选_方案_2026-10-29.md` §2）· 结果写入 `data/external_clients/sieve_x.json`（verdict=pass_final, gate=0, origin=External）。', '>',
         '> **Simon 看法**：每一户都可一句话否决（报编号即可，改回 keep_C 进闸 1）。没否决的按「永久 pass · 永不考虑」处理。T29-U119 起评估权在 Agent，这里照旧留否决口。', '',
         '## 结果', '',
         f'- 闸 0 永久 pass **{len(hits)}** 户：' + ' / '.join(f'{k} {v}' for k, v in sorted(cnt.items())) + '；按库：' + ' / '.join(f'{k} {v}' for k, v in by_repo.most_common()),
         f'- 例外（命中规则但有历史互动 / 乌克兰 → 转闸 1）：{len(exceptions)} 户',
         f'- 与 Saga Clients / 库内主档重叠（随主档结论，不单独判）：{len(dups)} 户',
         f'- 建议闸 1 优先（域名全死但未退信、无电话）：{len(suggest)} 户',
         f'- 其余 {n_c - len(hits) - len(dups):,} 户待闸 1 轻卡（含例外 {len(exceptions)}）', '',
         '### 永久 pass 按国家（前 25）', '', '| 国家 | 户数 |', '|---|---|']
    for k, v in by_cty.most_common(25):
        L.append(f'| {k} | {v} |')
    L += ['', '## 永久 pass 明细', '', '| 编号 | 库 | 公司 / 名称 | 国家 | 规则 | 理由 | 来源库标记 |', '|---|---|---|---|---|---|---|']
    for r, repo, rule, reason in sorted(hits, key=lambda x: x[0]['code']):
        L.append(f"| {r['code']} | {repo} | {md(r['name'])[:60]} | {r.get('country_zh') or '未填'} | {rule} | {md(reason)} | {md('、'.join(r.get('flags') or []))[:60]} |")
    L += ['', '## 例外（转闸 1）', '', '| 编号 | 库 | 公司 | 国家 | 命中规则 | 拦下原因 |', '|---|---|---|---|---|---|']
    for r, repo, rule, reason, bl in sorted(exceptions, key=lambda x: x[0]['code']):
        L.append(f"| {r['code']} | {repo} | {md(r['name'])[:60]} | {r.get('country_zh') or '未填'} | {rule} | {md('、'.join(bl))} |")
    L += ['', '## 与 Saga / 库内主档重叠（随主档）', '', '| 编号 | 库 | 公司 | 主档编号 | 主档评级 | 主档筛选结论 |', '|---|---|---|---|---|---|']
    for r, repo, sd, sv in sorted(dups, key=lambda x: x[0]['code']):
        L.append(f"| {r['code']} | {repo} | {md(r['name'])[:60]} | {sd.get('code')} | {sd.get('grade')} | {md(sv.get('verdict') or ('研究卡并线 → 随主档' if sd.get('via') == '研究卡并线' else ('A/B 档（不在 C 池筛选内）' if sd.get('grade') in ('A', 'B') else '—')))} |")
    L += ['', '## 建议闸 1 优先（域名全死）', '', '| 编号 | 库 | 公司 | 国家 | 域名状态 |', '|---|---|---|---|---|']
    for r, repo, dsx in sorted(suggest, key=lambda x: x[0]['code']):
        L.append(f"| {r['code']} | {repo} | {md(r['name'])[:60]} | {r.get('country_zh') or '未填'} | {md(dsx)} |")
    open(path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    return ts


def apply_gate0(hits, dups, sieve):
    added = kept = 0
    keep_codes = {r['code'] for r, *_ in hits} | {r['code'] for r, *_ in dups}
    dropped = [k for k, v in list(sieve.items()) if k != '_meta' and v.get('gate') == 0 and not v.get('manual') and k not in keep_codes]
    for k in dropped:
        sieve.pop(k)
    for r, repo, rule, reason in hits:
        cur = sieve.get(r['code'])
        if cur and cur.get('manual'):
            kept += 1
            continue
        sieve[r['code']] = {'verdict': 'pass_final', 'gate': 0, 'rule': rule, 'reason': reason, 'date': TODAY, 'repo': repo, 'origin': 'External'}
        added += 1
    for r, repo, sd, sv in dups:
        cur = sieve.get(r['code'])
        if cur and cur.get('manual'):
            kept += 1
            continue
        if sd.get('via') == '研究卡并线':
            verdict = 'keep_C'
            reason = f"第 2 步研究卡：与 {sd.get('code')} 同一公司 → 并线，随主档，不单独判"
        elif sv:
            verdict = sv.get('verdict')
            reason = f"与 Saga {sd.get('code')} 同一公司（经 {sd.get('via')}）→ 随 Saga 档：{verdict}（闸 {sv.get('gate')}，{str(sv.get('reason') or '')[:120]}）"
        else:
            verdict = 'keep_C'
            reason = f"与 Saga {sd.get('code')}（评级 {sd.get('grade')}）同一公司（经 {sd.get('via')}）→ Saga A/B 档在跟，本条只留来源库事实，不单独入池"
        sieve[r['code']] = {'verdict': verdict, 'gate': 0, 'rule': 'DUP', 'reason': reason, 'date': TODAY, 'repo': repo, 'origin': 'External', 'dup_of': sd.get('code')}
        added += 1
    return added, kept, len(dropped)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mx', action='store_true')
    ap.add_argument('--only-missing', action='store_true')
    ap.add_argument('--workers', type=int, default=16)
    ap.add_argument('--gate0', action='store_true')
    ap.add_argument('--stats', action='store_true')
    a = ap.parse_args()
    if a.mx:
        run_mx(a.only_missing, a.workers)
    if a.gate0:
        CARDS.update(all_cards())
        recs = load_xc()
        mx = load_mx()
        saga = json.load(open(SAGA_SIEVE, encoding='utf-8')) if os.path.exists(SAGA_SIEVE) else {}
        hits, exceptions, suggest, dups = gate0(recs, mx, saga)
        sieve = load_sieve()
        added, kept, dropped = apply_gate0(hits, dups, sieve)
        cnt = save_sieve(sieve)
        path = os.path.join(REQ, f'XC池闸0_机筛报告_{TODAY}.md')
        ts = write_report(hits, exceptions, suggest, dups, len(recs), mx, path)
        print(json.dumps({'time': ts, 'XC': len(recs), 'pass_final_gate0': len(hits), 'by_rule': dict(collections.Counter(r for _, _, r, _ in hits)),
                          'exceptions': len(exceptions), 'dups': len(dups), 'suggest_gate1': len(suggest), 'added': added, 'kept_manual': kept, 'dropped': dropped,
                          'sieve_counts': dict(cnt), 'report': os.path.relpath(path, ROOT)}, ensure_ascii=False))
    if a.stats:
        rows = {k: v for k, v in load_sieve().items() if k != '_meta'}
        print('n', len(rows), dict(collections.Counter((v.get('gate'), v.get('verdict')) for v in rows.values())))


if __name__ == '__main__':
    main()
