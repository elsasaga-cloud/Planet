#!/usr/bin/env python3
"""Elsa 邮箱群发 BCC 触达 → 研究档（第 73 批(o)，2026-10-24）。

输入：data/gmail_e/bcc_batches_2026.json（连接器 get_message(metadata) 读到的 To + Bcc 头，逐封追加）。
动作：按域名 / 完整地址与 entities.json 比对；对有 research JSON 且有 mail_review 的 A/B 户：
  1) binding.level 前缀「未发信（…」→「Elsa 群发 BCC 已触达 …；S/A 箱：…」，其它绑定则追加一句；
  2) facts 追加 k=elsa_bcc 的「去」事实（按 (date, quote[:25]) 去重）；
  3) 近期首封（待 Simon 排期 / 2026-11 / 2026-12 / 现在）的 next_move.action 前加「首封前知悉」提示；
  4) as_of = 今天。
C 户只统计不改（C JSON 多无 mail_review）。幂等：已带「第 73 批(o)」/同事实的不重复写。
用法：python3 scripts/gmail_ingest/elsa_bcc_apply.py [--dry]
之后照例：cd scripts/saga_clients && python3 build.py && python3 render.py && python3 audit.py
"""
import json, os, sys, datetime, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BATCHES = os.path.join(ROOT, 'data/gmail_e/bcc_batches_2026.json')
ENT = os.path.join(ROOT, 'data/saga_clients/entities.json')
RES = os.path.join(ROOT, 'data/saga_clients/research')
TODAY = datetime.date.today().isoformat()
DRY = '--dry' in sys.argv


def load_entities():
    E = json.load(open(ENT, encoding='utf-8'))
    ents = E if isinstance(E, list) else E.get('entities', E)
    return ents if isinstance(ents, list) else list(ents.values())


def match(batches, ents):
    res = {}
    for b in batches:
        addrs = [a.lower() for a in b['bcc']] + [b['to'].lower()]
        doms = {a.split('@')[1] for a in addrs if '@' in a}
        for e in ents:
            ed = {x.lower() for x in (e.get('domains') or [])}
            em = {x.lower() for x in (e.get('emails') or [])}
            hit = em & set(addrs)
            for d in doms:
                for x in ed:
                    if d == x or d.endswith('.' + x):
                        hit.add(d)
            if hit:
                res.setdefault(e['code'], {'grade': e.get('grade'), 'name': e.get('name', ''), 'hits': []})['hits'].append(
                    {'msg_id': b['msg_id'], 'date': b['date'], 'subject': b['subject'], 'batch': b['batch'],
                     'to': b['to'], 'price_text': b.get('price_text', ''), 'matched': sorted(hit)})
    return res


def quote_for(h):
    if h['subject'] == '24 Port PoE Managed Switch':
        return '24 Port PoE Managed Switch — Marvell AC5 L2+ 24 PoE af/at + 10G uplinks, OEM/Web GUI; Price: 170USD/PC'
    if h['subject'] == '10G Enterprise SFP Switch':
        return '10G Enterprise SFP Switch — 24×1G SFP + 8 combo + 4×10G SFP+ managed, dual AC（价格不在摘要里）'
    return f"{h['subject']}（{h.get('price_text') or '价格未读'}）"


def apply(res):
    n = fa = 0
    for c, v in sorted(res.items()):
        if v['grade'] not in ('A', 'B'):
            continue
        p = os.path.join(RES, f'{c}.json')
        if not os.path.exists(p):
            continue
        d = json.load(open(p, encoding='utf-8'))
        mr = d.get('mail_review')
        if not mr:
            continue
        hits = sorted(v['hits'], key=lambda x: x['date'])
        h = hits[-1]
        ptxt = '，正文「Price: 170USD/PC」' if h['subject'] == '24 Port PoE Managed Switch' else '（价格未读）'
        tag = (f"Elsa 群发 BCC 已触达 {h['date']}「{h['subject']}」{ptxt}，{h['batch']} 批次 To {h['to']}，0 回"
               f"（第 73 批(o) Bcc 头核对 msg {h['msg_id']}）")
        changed = False
        b = mr.get('binding')
        if isinstance(b, dict):
            lvl = str(b.get('level') or '')
            if '第 73 批(o)' not in lvl:
                b['level'] = (tag + '；S/A 箱：' + lvl[4:]) if lvl.startswith('未发信（') else (lvl + '；' + tag)
                ev = str(b.get('evidence') or '')
                if 'bcc_batches_2026.json' not in ev:
                    b['evidence'] = (ev + '；data/gmail_e/bcc_batches_2026.json').strip('；')
                changed = True
        else:
            s = str(b or '')
            if '第 73 批(o)' not in s:
                mr['binding'] = (tag + '；S/A 箱：' + s[4:]) if s.startswith('未发信（') else (s + '；' + tag)
                changed = True
        facts = mr.setdefault('facts', [])
        for hh in hits:
            q = quote_for(hh)
            key = (hh['date'], q[:25])
            if any((f.get('date'), str(f.get('quote', ''))[:25]) == key for f in facts):
                continue
            facts.append({'date': hh['date'], 'dir': '去',
                          'who': f"Elsa 群发（BCC；To {hh['to']}，{hh['batch']} 批次）", 'quote': q,
                          'why': f"Elsa 箱群发 BCC 触达证据（命中地址 {', '.join(hh['matched'])}）；S/A digest 看不到 Elsa 的 BCC，之前据此写的「未发信/未触达」不成立",
                          'k': 'elsa_bcc'})
            fa += 1
            changed = True
        facts.sort(key=lambda f: str(f.get('date', '')))
        nm = mr.get('next_move') or {}
        w = str(nm.get('when') or '')
        if any(k in w for k in ['待 Simon 排期', '2026-11', '2026-12', '现在']):
            a = str(nm.get('action') or '')
            if '首封前知悉' not in a:
                price = '，$170' if h['subject'] == '24 Port PoE Managed Switch' else ''
                nm['action'] = (f"首封前知悉：Elsa 已 BCC 群发触达（最近 {h['date']}「{h['subject']}」{price}），"
                                f"开头按 ㉝ 写「我们发过几封 X 主题的信、你没有理由回」，别当完全陌生；"
                                f"同款 24-PoE 要报 $180 就先说 8–9 月那封是 $170、汇率 7.2→6.7。" + (' ' + a if a else ''))
                mr['next_move'] = nm
                changed = True
        if changed:
            mr['as_of'] = TODAY
            n += 1
            if not DRY:
                json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return n, fa


def main():
    meta = json.load(open(BATCHES, encoding='utf-8'))
    ents = load_entities()
    res = match(meta['batches'], ents)
    by = collections.Counter(v['grade'] for v in res.values())
    print(f"batches {len(meta['batches'])}  matched entities {len(res)}  by grade {dict(by)}")
    n, fa = apply(res)
    print(f"{'DRY ' if DRY else ''}patched {n} research JSONs, facts added {fa}")
    out = os.path.join(ROOT, 'data/gmail_e/bcc_match_latest.json')
    if not DRY:
        json.dump(res, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('match table →', os.path.relpath(out, ROOT))


if __name__ == '__main__':
    main()
