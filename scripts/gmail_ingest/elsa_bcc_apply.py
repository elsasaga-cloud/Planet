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
    if h['subject'] == '10G Enterprise SFP Switch' and h['date'].startswith('2026-05'):
        return '10G Enterprise SFP Switch — 24×1G SFP + 8 combo + 4×10G SFP+ managed, dual AC（价格不在摘要里）'
    pt = (h.get('price_text') or '').strip()
    if pt.startswith('Hi,'):
        pt = pt.split('?', 1)[-1].strip() if '?' in pt[:20] else pt
    return f"{h['subject']} — {pt[:150]}" if pt else f"{h['subject']}（价格未读）"


def anchor_summary(meta, hits, all_batches):
    """按群发批次（anchor To）给一句「时间线」：首尾轮次、总轮数、是否中途加入/剔除。"""
    anchors = meta.get('anchors') or {}
    alias = {}
    for to, a in anchors.items():
        alias[to.lower()] = to
        for x in a.get('aliases') or []:
            alias[x.lower()] = to
    by = {}
    for h in hits:
        key = alias.get(h['to'].lower())
        if key:
            by.setdefault(key, []).append(h)
    out = []
    for to, hs in by.items():
        a = anchors[to]
        camps = sorted(a['campaigns'], key=lambda c: c['date'])
        mine = sorted({h['date'] for h in hs})
        first, last = mine[0], mine[-1]
        n_between = sum(1 for c in camps if first <= c['date'] <= last)
        subj = []
        for c in camps:
            if first <= c['date'] <= last and c['subject'] not in subj:
                subj.append(c['subject'])
        read_ids = {b['msg_id'] for b in all_batches}
        oldest, newest = camps[0], camps[-1]
        parts = []
        if len(mine) >= 2:
            parts.append(f"同批次（To {to}）{first}→{last} 共 {n_between} 轮群发（{'、'.join(subj)}），本户在首尾两轮 Bcc 名单内，名单稳定、中间轮次按同名单推断")
        else:
            parts.append(f"同批次（To {to}）本户见于 {first} 名单")
        if oldest['msg_id'] in read_ids and oldest['date'] < first:
            parts.append(f"{oldest['date']} 首轮名单无此地址 → 中途加入")
        if newest['msg_id'] in read_ids and newest['date'] > last:
            parts.append(f"{newest['date']} 最新一轮名单已不含此地址 → 中途被剔除（退信 / 退订 / 手工）")
        if oldest['msg_id'] not in read_ids and oldest['date'] < first:
            parts.append(f"该批次最早 {oldest['date']} 起共 {len(camps)} 轮，更早轮次 Bcc 未读")
        out.append('；'.join(parts))
    return '；'.join(out)


def apply(res, meta):
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
        first = f"，首见 {hits[0]['date']}" if len(hits) >= 2 and hits[0]['date'] != h['date'] else ''
        tag = (f"Elsa 群发 BCC 已触达 {h['date']}「{h['subject']}」{ptxt}，{h['batch']} 批次 To {h['to']}{first}，0 回"
               f"（第 74 批 Bcc 头核对 msg {h['msg_id']}）")
        changed = False
        b = mr.get('binding')
        if isinstance(b, dict):
            lvl = str(b.get('level') or '')
            if 'Bcc 头核对' not in lvl:
                b['level'] = (tag + '；S/A 箱：' + lvl[4:]) if lvl.startswith('未发信（') else (lvl + '；' + tag)
                ev = str(b.get('evidence') or '')
                if 'bcc_batches_2026.json' not in ev:
                    b['evidence'] = (ev + '；data/gmail_e/bcc_batches_2026.json').strip('；')
                changed = True
        else:
            s = str(b or '')
            if 'Bcc 头核对' not in s:
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
        summ = anchor_summary(meta, hits, meta['batches'])
        if summ and isinstance(b, dict):
            ev0 = str(b.get('evidence') or '')
            ev = ev0
            if '批次时间线：' in ev:
                import re as _re
                ev = _re.sub(r'；?批次时间线：.*$', '', ev)
            ev = (ev + '；批次时间线：' + summ).strip('；')
            if ev != ev0:
                b['evidence'] = ev
                changed = True
        nm = mr.get('next_move') or {}
        w = str(nm.get('when') or '')
        if any(k in w for k in ['待 Simon 排期', '2026-11', '2026-12', '现在']):
            a = str(nm.get('action') or '')
            if '首封前知悉' not in a:
                price = '，$170' if h['subject'] == '24 Port PoE Managed Switch' else ''
                saw170 = any(x['subject'] == '24 Port PoE Managed Switch' for x in hits)
                fx = "；同款 24-PoE 要报 $180 就先说 8–9 月那封是 $170、汇率 7.2→6.7。" if saw170 else "。"
                nm['action'] = (f"首封前知悉：Elsa 已 BCC 群发触达（最近 {h['date']}「{h['subject']}」{price}），"
                                f"开头按 ㉝ 写「我们发过几封 X 主题的信、你没有理由回」，别当完全陌生" + fx + (' ' + a if a else ''))
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
    n, fa = apply(res, meta)
    print(f"{'DRY ' if DRY else ''}patched {n} research JSONs, facts added {fa}")
    out = os.path.join(ROOT, 'data/gmail_e/bcc_match_latest.json')
    if not DRY:
        json.dump(res, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('match table →', os.path.relpath(out, ROOT))


if __name__ == '__main__':
    main()
