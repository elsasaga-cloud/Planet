#!/usr/bin/env python3
"""把 S 邮箱入库数据（data/gmail_s/）按客户编号压成档案可用的摘要 → data/saga_clients/gmail_digest.json。

每个客户：线程表（主题 / 首末日期 / 来 / 去 / 附件数）、最后一封来信（日期 / 发件人 / 摘要）、最后一封去信日期、
邮件里报过的价（来自 data/gmail_s/报价史.csv）、往来附件名。只做机械汇总，不做判断；render.py 对 A/B 档案加「邮箱往来」节。
多账号：将来 A 邮箱入库后在 ACCOUNTS 里加 'a' 即可。
"""
import csv, glob, json, os, re
from collections import defaultdict
from common import DATA, ROOT

ACCOUNTS = ['s', 'a']   # 2026-10-24 T29-U40：A 邮箱入库后并入（2025-03~08 分片待 Release 重跑补齐）
AUTO = re.compile(r'(out of (the )?office|automatic reply|auto-?reply|autoreply|delivery status|undeliver|mailer-daemon|postmaster|unsubscribe|no-?reply|noreply|newsletter|zendesk|ticket|thank you for contacting|we have received your (message|email|inquiry)|vacation|abwesen|poza biurem|отпуск|автоответ|réponse automatique|ferie|on leave|promo|%|sale!)', re.I)
OUT = os.path.join(DATA, 'gmail_digest.json')


def main():
    digest = {}
    for acct in ACCOUNTS:
        base = os.path.join(ROOT, 'data', f'gmail_{acct}')
        link_p = os.path.join(base, 'clients_link.json')
        if not os.path.exists(link_p):
            continue
        threads = json.load(open(os.path.join(base, 'threads.json'), encoding='utf-8'))['threads']
        # 当前 entities.json 的域名 → 编号（比入库时的 clients_link 新：补录客户也能对上）
        ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
        dom2, em2 = {}, {}
        for e in ents:
            for d in e.get('domains') or []:
                dom2[d.lower()] = e['code']
            for x in (e.get('emails') or []) + (e.get('corp_emails') or []):
                em2[x.lower()] = e['code']        # 邮箱级匹配：免费邮箱（gmail 等）客户靠这个对上
        # 人工确认的邮箱/域名别名（data/saga_clients/邮箱别名.csv：编号,邮箱或域名,依据,日期）——同一客户换邮箱 / 用私人邮箱 / 第二域名
        alias_p = os.path.join(DATA, '邮箱别名.csv')
        if os.path.exists(alias_p):
            for r in csv.DictReader(open(alias_p, encoding='utf-8-sig')):
                k = (r.get('邮箱或域名') or '').strip().lower()
                code = (r.get('编号') or '').strip()
                if not k or not code:
                    continue
                (em2 if '@' in k else dom2)[k] = code
        own = {'gmail.com', 'googlemail.com', 'sagatelecom.com', 'sagatelecom.com.cn', 'sagatele.com'}
        stat = defaultdict(lambda: {'messages': 0, 'out': 0, 'in': 0, 'first': '9999', 'last': '0000', 'emails': set(), 'threads': set()})
        last_in, last_out, atts = {}, {}, defaultdict(set)
        for f in sorted(glob.glob(os.path.join(base, 'messages', '*', '*.jsonl'))):
            for line in open(f, encoding='utf-8'):
                m = json.loads(line)
                people = [m['from']] + (m.get('to') or []) + (m.get('cc') or [])
                codes = set(m.get('client') or [])
                for x in people:
                    em = x['e'].lower()
                    dmn = em.split('@')[-1]
                    if em in em2:
                        codes.add(em2[em])
                    elif dmn in dom2 and dmn not in own:
                        codes.add(dom2[dmn])
                if not codes:
                    continue
                d = m['date'][:10]
                for code in codes:
                    st = stat[code]
                    st['messages'] += 1
                    st['out' if m.get('dir') == 'out' else 'in'] += 1
                    st['first'] = min(st['first'], d)
                    st['last'] = max(st['last'], d)
                    st['threads'].add(m['thr'])
                    for x in people:
                        em = x['e'].lower()
                        dmn = em.split('@')[-1]
                        if em2.get(em) == code or (dom2.get(dmn) == code and dmn not in own):
                            st['emails'].add(em)
                    if m.get('dir') == 'in':
                        t = (m.get('text') or '')
                        qa = m.get('quote_at')
                        t = t[:qa] if qa else t
                        t = re.sub(r'\s+', ' ', t).strip()
                        if code not in last_in or d >= last_in[code]['date']:
                            last_in[code] = {'date': d, 'from': m['from']['e'], 'subject': m['subj'][:80], 'snippet': t[:260], 'thr': m['thr'],
                                             'auto': bool(AUTO.search(m['subj']) or AUTO.search(t[:300]) or AUTO.search(m['from']['e']))}
                    else:
                        if d > last_out.get(code, ''):
                            last_out[code] = d
                    for a in m.get('att') or []:
                        n = a.get('name') or ''
                        if n and not re.search(r'\.(png|jpe?g|gif)$', n, re.I):
                            atts[code].add(n[:60])
        links = {code: {'messages': st['messages'], 'out': st['out'], 'in': st['in'], 'first': st['first'], 'last': st['last'],
                        'emails': sorted(st['emails']), 'threads': sorted(st['threads'])} for code, st in stat.items()}
        quotes = defaultdict(list)
        qp = os.path.join(base, '报价史.csv')
        if os.path.exists(qp):
            for r in csv.DictReader(open(qp, encoding='utf-8-sig')):
                if r['客户编号'] and r['类型'] == '单价' and r['群发?'] != 'Y':
                    quotes[r['客户编号']].append({'date': r['日期'], 'usd': r['价格USD'], 'model': r['型号(正文出现)'], 'ctx': r['价格所在句'][:110]})
        for code, v in links.items():
            th = []
            for tid in v.get('threads', []):
                t = threads.get(tid)
                if t:
                    th.append({'id': tid, 'subject': t['subject'][:80], 'first': t['first'][:10], 'last': t['last'][:10], 'in': t['in'], 'out': t['out'], 'atts': t['atts']})
            th.sort(key=lambda x: x['last'], reverse=True)
            q = sorted(quotes.get(code, []), key=lambda x: x['date'], reverse=True)
            # 同日同价去重
            seen, qq = set(), []
            for x in q:
                k = (x['date'], x['usd'])
                if k in seen:
                    continue
                seen.add(k)
                qq.append(x)
            li = last_in.get(code)
            pending = False
            if li and not li.get('auto') and li['date'] > (last_out.get(code, '') or ''):
                t = threads.get(li.get('thr') or '')
                pending = bool(t and t.get('out', 0) > 0)
            for x in th:
                x['acct'] = acct
            rec = {'pending_reply': pending, 'account': f'{acct}.sagatelecom', 'messages': v['messages'], 'out': v['out'], 'in': v['in'], 'first': v['first'][:10], 'last': v['last'][:10],
                   'emails': v.get('emails', []), 'threads': th[:30], 'last_in': last_in.get(code), 'last_out': last_out.get(code, ''),
                   'quotes': qq[:12], 'attachments': sorted(atts.get(code, []))[:12]}
            old = digest.get(code)
            if not old:
                digest[code] = rec
                continue
            # 多账号合并（2026-10-24）：计数相加、线程并集按最后日期排序、最后来/去信取最新、报价/附件并集；pending 以最新一封来信为准
            li_old, li_new = old.get('last_in'), rec.get('last_in')
            li = li_new if (li_new and (not li_old or li_new['date'] >= li_old['date'])) else li_old
            lo = max(old.get('last_out') or '', rec.get('last_out') or '')
            pend = bool(li and not li.get('auto') and li['date'] > lo and (old['pending_reply'] if li is li_old else rec['pending_reply']))
            thr = {x['id']: x for x in old['threads'] + rec['threads']}
            seen_q, qm = set(), []
            for x in sorted(old['quotes'] + rec['quotes'], key=lambda x: x['date'], reverse=True):
                if (x['date'], x['usd']) in seen_q:
                    continue
                seen_q.add((x['date'], x['usd']))
                qm.append(x)
            digest[code] = {'pending_reply': pend, 'account': old['account'] + '+' + f'{acct}.sagatelecom', 'messages': old['messages'] + rec['messages'],
                            'out': old['out'] + rec['out'], 'in': old['in'] + rec['in'], 'first': min(old['first'], rec['first']), 'last': max(old['last'], rec['last']),
                            'emails': sorted(set(old['emails']) | set(rec['emails'])), 'threads': sorted(thr.values(), key=lambda x: x['last'], reverse=True)[:30],
                            'last_in': li, 'last_out': lo, 'quotes': qm[:12], 'attachments': sorted(set(old['attachments']) | set(rec['attachments']))[:12]}
    json.dump(digest, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('clients', len(digest), '→', os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
