#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T29-U117 · C 池三闸筛选 · 状态落盘 + 闸 0 机筛 + 闸 1 排队。

方案：docs/C池三闸筛选_方案_2026-10-29.md
数据：data/saga_clients/sieve.json  {code: {verdict, gate, rule, reason, date, manual?, card?}}
      verdict ∈ pass_final | keep_C | candidate | pool_candidate | pool（P 池正式入池，闸 3）| pool_watch（P 池观察档，闸 3）

用法：
  python3 sieve.py --gate0            # 跑闸 0 刚性机筛，写 sieve.json + docs/requirements/C池闸0_机筛报告_<日期>.md
  python3 sieve.py --queue 60         # 按方案 §3 顺序打印下一批待闸 1 的户（不写文件）
  python3 sieve.py --set SC-xxxx keep_C 理由...   [--gate 1] [--rule G1]   # 人工落判（manual: true）
  python3 sieve.py --stats            # 当前状态统计

闸 0 只认三条刚性规则（Simon U117）：G0-1 无任何联系路径 / G0-2 退信且域名全死 / G0-3 明确拒绝（拉黑 / 信息造假）。
例外：成单 / 样品 / 实质回信 / 互动备注 / 加过 WA / 有电话 / 乌克兰 → 一律转闸 1。
"""
import argparse
import collections
import datetime as dt
import glob
import json
import os
import re
import subprocess
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
SIEVE = os.path.join(DATA, 'sieve.json')
REQ = os.path.join(ROOT, 'docs', 'requirements')
TODAY = dt.date.today().isoformat()

EMAIL_RE = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
CONTACT_RE = re.compile(r'微信|wechat|whatsapp|\bwa\b|已加|加了|linkedin|skype|telegram|viber|手机|电话|\btel\b|phone|'
                        r'www\.|http|\.[a-z]{2,4}(?:\b|/)|\d[\d\s\-()]{6,}\d')
UA_RE = re.compile(r'乌克兰')
PLATFORM_RE = re.compile(r'阿里巴巴|国际站|alibaba|RFQ|自建站|made-in-china|globalsources|富通天下|ETW', re.I)
DEAD = {'nxdomain', 'dead'}

# G0-3b：联系信息明显造假（逐户核过原始行，理由写死在这里，透明可查）
FAKE_INFO = {
    'SC-2858': '邮箱 asdsd@gmail.com 明显假 + 表记「邮件发不过去 垃圾询盘」',
    'SC-2928': '号码 966-55-12345678 明显假 + 加不上 + 表记「有点像垃圾询盘」',
}


def now_z():
    try:
        return subprocess.check_output(['date', '-u', '+%Y-%m-%d %H:%MZ']).decode().strip()
    except Exception:
        return dt.datetime.utcnow().strftime('%Y-%m-%d %H:%MZ')


def load_entities():
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    return ents if isinstance(ents, list) else list(ents.values())


def load_raw():
    raw = {}
    with open(os.path.join(DATA, 'rows_raw.jsonl'), encoding='utf-8') as f:
        for line in f:
            r = json.loads(line)
            raw[(r['file'], r.get('sheet'), str(r.get('row')))] = r
    return raw


def load_mx():
    fs = sorted(glob.glob(os.path.join(DATA, 'mx_check_*.json')))
    if not fs:
        return {'domains': {}, 'households': {}}, ''
    return json.load(open(fs[-1], encoding='utf-8')), os.path.basename(fs[-1])


def load_sieve():
    if os.path.exists(SIEVE):
        return json.load(open(SIEVE, encoding='utf-8'))
    return {'_meta': {}}


def save_sieve(s):
    rows = {k: v for k, v in s.items() if k != '_meta'}
    cnt = collections.Counter(v.get('verdict') for v in rows.values())
    cnt_c = collections.Counter(v.get('verdict') for k, v in rows.items() if k.startswith('SC-'))
    cnt_ab = collections.Counter(v.get('verdict') for k, v in rows.items() if not k.startswith('SC-'))   # A / B 并池行（AB-01 起，只加池位不改等级）
    s['_meta'] = {'updated': TODAY, 'rules': 'docs/C池三闸筛选_方案_2026-10-29.md §2 · A/B 并池 docs/AB并池方案_草案_2026-10-29.md §5', 'counts': dict(cnt), 'n': len(rows),
                  'counts_C': dict(cnt_c), 'n_C': sum(cnt_c.values()), 'counts_AB': dict(cnt_ab), 'n_AB': sum(cnt_ab.values())}
    out = {'_meta': s['_meta']}
    for k in sorted(rows):
        out[k] = rows[k]
    json.dump(out, open(SIEVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return cnt


def raw_text(ent, raw):
    parts = []
    for s in ent.get('sources') or []:
        r = raw.get((s['file'], s.get('sheet'), str(s.get('row'))))
        if not r:
            continue
        for k, v in r.items():
            if k in ('file', 'sheet', 'row', 'no'):
                continue
            if isinstance(v, (dict, list)):
                v = json.dumps(v, ensure_ascii=False)
            if v:
                parts.append(f'{k}={v}')
    return ' | '.join(parts)


def norm(s):
    return unicodedata.normalize('NFKD', s).replace('\u0307', '').lower()


def is_ua(ent):
    return bool(UA_RE.search(ent.get('country') or '') or UA_RE.search(ent.get('c_sub') or ''))


def hist_signals(ent):
    fl = ent.get('flags') or {}
    sig = []
    if fl.get('deal'):
        sig.append('成单')
    if fl.get('sample'):
        sig.append('样品')
    if (ent.get('reply_sub') or 0) > 0:
        sig.append(f"实质回信{ent['reply_sub']}")
    if fl.get('engaged_note'):
        sig.append('互动备注')
    if fl.get('wa_added'):
        sig.append('加过WA')
    if ent.get('phones'):
        sig.append('有电话')
    return sig


def gate0(ents, raw, mx):
    D, HH = mx.get('domains', {}), mx.get('households', {})
    hits, exceptions, suggest = [], [], []
    for e in ents:
        if e.get('grade') != 'C':
            continue
        code = e['code']
        fl = e.get('flags') or {}
        t = raw_text(e, raw)
        tn = norm(t)
        ua = is_ua(e)
        sig = hist_signals(e)
        ds = HH.get(code) or []
        st = [D[d]['status'] for d in ds if d in D]
        all_dead = bool(st) and all(x in DEAD for x in st)
        rule = reason = None
        # G0-1 无任何联系路径
        platform = bool(PLATFORM_RE.search(t))
        if (not e.get('emails') and not e.get('phones') and not e.get('domains') and not e.get('urls')
                and not e.get('platform_links') and not fl.get('wa_added')
                and not EMAIL_RE.search(tn) and not CONTACT_RE.search(tn)):
            nm = e.get('name') or ''
            if '未具名' in nm or re.search(r'下边|已经发过|发过CENTEC', nm):
                rule, reason = 'G0-1', '表内无名 / 注释行，原始行全文无邮箱、电话、网址、微信等任何联系线索'
            else:
                rule, reason = 'G0-1', '仅有公司 / 人名，原始行全文无邮箱、电话、网址、微信等任何联系线索'
            if platform:
                sig = sig + ['平台询盘（联系方式在阿里 / 自建站后台）']
        # G0-2 退信且域名全死
        elif fl.get('bounce') and all_dead and not e.get('phones') and not fl.get('wa_added'):
            rule = 'G0-2'
            reason = '表记发不过去 / 退信；' + '、'.join(f'{d} {D[d]["status"].upper()}' for d in ds if d in D) + '；无电话、无 WA'
        # G0-3 明确拒绝
        elif '拉黑' in t:
            m = re.search(r'.{0,24}拉黑.{0,6}', t)
            rule, reason = 'G0-3', '表记「' + (m.group(0).strip() if m else '拉黑') + '」—— 关系已断死'
            if re.search(r'(似乎|好像|可能|应该)\s*(是)?\s*(被)?拉黑', t):
                sig = sig + ['表记「似乎拉黑」不确定']
        elif code in FAKE_INFO:
            rule, reason = 'G0-3', FAKE_INFO[code]
        if rule:
            blockers = [x for x in sig if not (rule == 'G0-3' and x in ('加过WA', '有电话', '互动备注'))]
            if ua:
                blockers.append('乌克兰')
            if rule == 'G0-2' and any(x in ('成单', '样品') or x.startswith('实质回信') for x in sig):
                blockers = blockers or ['历史互动']
            if blockers:
                exceptions.append((e, rule, reason, blockers))
            else:
                hits.append((e, rule, reason))
        elif all_dead and not fl.get('bounce') and not e.get('phones') and not fl.get('wa_added') and not sig and not ua:
            suggest.append((e, '、'.join(f'{d} {D[d]["status"].upper()}' for d in ds if d in D)))
    return hits, exceptions, suggest


def write_report(hits, exceptions, suggest, mxname, n_c, path):
    ts = now_z()
    cnt = collections.Counter(r for _, r, _ in hits)
    L = []
    L.append(f'# C 池 · 闸 0 刚性机筛报告（{TODAY}）')
    L.append('')
    L.append(f'> 生成 {ts} · 输入 `entities.json`（C {n_c:,} 户）+ `rows_raw.jsonl`（原始表行全文）+ `{mxname}`（DNS MX/A）'
             f' · 规则见 `docs/C池三闸筛选_方案_2026-10-29.md` §2 · 结果写入 `data/saga_clients/sieve.json`（verdict=pass_final, gate=0）。')
    L.append('>')
    L.append('> **Simon 看法**：下面每一户都可以一句话否决（告诉我编号即可，改回 keep_C 进闸 1）。没否决的按「永久 pass · 永不考虑」处理。')
    L.append('')
    L.append('## 1. 计数')
    L.append('')
    L.append('| 规则 | 含义 | 自动 pass | 命中但例外（转闸 1） |')
    L.append('|---|---|---|---|')
    exc_cnt = collections.Counter(r for _, r, _, _ in exceptions)
    for r, m in (('G0-1', '无任何联系路径（原始行全文核对）'), ('G0-2', '退信且所有邮箱域名 NXDOMAIN / 无解析，无电话无 WA'),
                 ('G0-3', '明确拒绝：拉黑 / 联系信息明显造假')):
        L.append(f'| {r} | {m} | {cnt.get(r, 0)} | {exc_cnt.get(r, 0)} |')
    L.append(f'| **合计** | | **{len(hits)}** | {len(exceptions)} |')
    L.append('')
    L.append(f'C 总数 {n_c:,} → 闸 0 永久 pass **{len(hits)}** → 待闸 1 **{n_c - len(hits):,}**（其中「机筛建议 pass 优先项」{len(suggest)} 户：域名全死但表内无退信记录，闸 1 先看）。')
    L.append('')
    for r, title in (('G0-1', '无任何联系路径'), ('G0-2', '退信且域名全死'), ('G0-3', '明确拒绝')):
        rows = [(e, rs) for e, rr, rs in hits if rr == r]
        L.append(f'## 2.{r[-1]} {r} {title}（{len(rows)}）')
        L.append('')
        L.append('| 编号 | 公司 / 名 | 国家 | C 细分 | 依据 |')
        L.append('|---|---|---|---|---|')
        for e, rs in sorted(rows, key=lambda x: x[0]['code']):
            L.append(f"| `{e['code']}` | {md(e.get('name'))} | {e.get('country') or '未填'} | {md(e.get('c_sub'))} | {md(rs)} |")
        L.append('')
    L.append(f'## 3. 命中规则但触发例外 → 转闸 1（{len(exceptions)}）')
    L.append('')
    L.append('| 编号 | 公司 / 名 | 国家 | 命中 | 例外原因 |')
    L.append('|---|---|---|---|---|')
    for e, r, rs, bl in sorted(exceptions, key=lambda x: x[0]['code']):
        L.append(f"| `{e['code']}` | {md(e.get('name'))} | {e.get('country') or '未填'} | {r}：{md(rs)[:60]} | {'、'.join(bl)} |")
    L.append('')
    L.append(f'## 4. 闸 1 机筛建议 pass 优先项（{len(suggest)}，**未**自动 pass）')
    L.append('')
    L.append('域名全部 NXDOMAIN / 无解析，但表内没有退信记录、无电话无 WA、无任何互动 —— 闸 1 先核官网 / 社媒是否也死，死透再 pass。')
    L.append('')
    L.append('| 编号 | 公司 / 名 | 国家 | C 细分 | 域名状态 |')
    L.append('|---|---|---|---|---|')
    for e, ds in sorted(suggest, key=lambda x: x[0]['code']):
        L.append(f"| `{e['code']}` | {md(e.get('name'))} | {e.get('country') or '未填'} | {md(e.get('c_sub'))} | {md(ds)} |")
    L.append('')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    return ts


def md(s):
    return (str(s) if s is not None else '').replace('|', '／').replace('\n', ' ')


def apply_gate0(hits, sieve):
    added = kept = 0
    for e, rule, reason in hits:
        cur = sieve.get(e['code'])
        if cur and (cur.get('manual') or (cur.get('gate') or 0) >= 1):
            kept += 1
            continue
        sieve[e['code']] = {'verdict': 'pass_final', 'gate': 0, 'rule': rule, 'reason': reason, 'date': cur.get('date') if cur else TODAY}
        added += 1
    # 之前闸 0 自动判、这次不再命中的（规则收紧 / 数据更新）→ 撤回
    now = {e['code'] for e, _, _ in hits}
    dropped = 0
    for k in list(sieve):
        v = sieve[k]
        if k != '_meta' and v.get('gate') == 0 and not v.get('manual') and k not in now:
            del sieve[k]
            dropped += 1
    return added, kept, dropped


PRIORITY = [
    ('① 成单 / 样品', lambda e, fl: fl.get('deal') or fl.get('sample')),
    ('② 自有品牌', lambda e, fl: fl.get('own_brand')),
    ('③ 实质回信', lambda e, fl: (e.get('reply_sub') or 0) > 0),
    ('④ 加过 WhatsApp', lambda e, fl: fl.get('wa_added')),
    ('⑤ 企业邮箱 · 四主区+波兰', lambda e, fl: bool(e.get('corp_emails')) and (e.get('region') in ('北美', '欧洲', '土耳其') or e.get('country') == '波兰')),
    ('⑥ 企业邮箱 · 其他区', lambda e, fl: bool(e.get('corp_emails'))),
    ('⑦ 其余（免费邮箱 / 仅电话 / 仅网址）', lambda e, fl: True),
]


def bucket(e):
    fl = e.get('flags') or {}
    for name, fn in PRIORITY:
        if fn(e, fl):
            return name
    return PRIORITY[-1][0]


def queue(ents, sieve, n):
    rows = []
    for e in ents:
        if e.get('grade') != 'C' or e['code'] in sieve:
            continue
        rows.append(e)
    order = {name: i for i, (name, _) in enumerate(PRIORITY)}
    rows.sort(key=lambda e: (order[bucket(e)], -(e.get('score') or 0), e['code']))
    print(f'待闸 1 共 {len(rows)} 户；分桶：', dict(collections.Counter(bucket(e) for e in rows)))
    for e in rows[:n]:
        rs = '有调研' if os.path.exists(os.path.join(DATA, 'research', e['code'] + '.json')) else ''
        print(f"{e['code']} | {bucket(e)[:1]} | {(e.get('name') or '')[:28]} | {e.get('country')} | {(e.get('c_sub') or '')[:14]} | "
              f"{'/'.join(hist_signals(e))} | {(e.get('corp_emails') or e.get('emails') or [''])[0][:30]} | {rs}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gate0', action='store_true')
    ap.add_argument('--queue', type=int)
    ap.add_argument('--set', nargs='+', metavar=('CODE', 'VERDICT'))
    ap.add_argument('--gate', type=int, default=1)
    ap.add_argument('--rule', default='G1')
    ap.add_argument('--stats', action='store_true')
    a = ap.parse_args()
    ents = load_entities()
    sieve = load_sieve()
    if a.gate0:
        raw = load_raw()
        mx, mxname = load_mx()
        n_c = sum(1 for e in ents if e.get('grade') == 'C')
        hits, exceptions, suggest = gate0(ents, raw, mx)
        added, kept, dropped = apply_gate0(hits, sieve)
        cnt = save_sieve(sieve)
        path = os.path.join(REQ, f'C池闸0_机筛报告_{TODAY}.md')
        ts = write_report(hits, exceptions, suggest, mxname, n_c, path)
        print(json.dumps({'time': ts, 'C': n_c, 'pass_final_gate0': len(hits), 'by_rule': dict(collections.Counter(r for _, r, _ in hits)),
                          'exceptions': len(exceptions), 'suggest_gate1': len(suggest), 'added': added, 'kept_manual': kept,
                          'dropped': dropped, 'sieve_counts': dict(cnt), 'report': os.path.relpath(path, ROOT)}, ensure_ascii=False))
    if a.queue:
        queue(ents, sieve, a.queue)
    if a.set:
        code, verdict, reason = a.set[0], a.set[1], ' '.join(a.set[2:])
        assert verdict in ('pass_final', 'keep_C', 'candidate', 'pool_candidate', 'pool', 'pool_watch'), verdict
        assert any(e['code'] == code for e in ents), code
        assert reason, '必须给理由'
        sieve[code] = {'verdict': verdict, 'gate': a.gate, 'rule': a.rule, 'reason': reason, 'date': TODAY, 'manual': True}
        cnt = save_sieve(sieve)
        print(code, verdict, dict(cnt))
    if a.stats:
        rows = {k: v for k, v in sieve.items() if k != '_meta'}
        print('n', len(rows), dict(collections.Counter((v.get('gate'), v.get('verdict')) for v in rows.values())))


if __name__ == '__main__':
    main()
