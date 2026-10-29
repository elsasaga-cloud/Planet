#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saga Clients · 第 3 步：把 entities.json 渲染成 `Saga Clients/A|B|C/<编号>-<公司>-<国家>.md`（结构同 profile/）+ 索引。

绝不手改 MD：改规则 → 改 build.py / research JSON / 人工定级.csv → 重跑 build.py + render.py。
"""
import csv
import datetime as dt
import glob
import json
import os
import re
import shutil
from collections import Counter, defaultdict

from common import DATA, OUT_DIR, ROOT, slug, sub_dir, BUCKET, BUCKETED

TODAY = dt.date.today().isoformat()
PRICE_CSV = os.path.join(ROOT, 'data', '价格主表.csv')
DIGEST_JSON = os.path.join(DATA, 'site_digest.json')   # snapshot_digest.py 产物（官网快照摘要），缺失则跳过
GMAIL_DIGEST = os.path.join(DATA, 'gmail_digest.json')  # gmail_digest.py 产物（S 邮箱按客户汇总），缺失则跳过
GMAIL = json.load(open(GMAIL_DIGEST, encoding='utf-8')) if os.path.exists(GMAIL_DIGEST) else {}
DIMS_JSON = os.path.join(DATA, 'dims.json')             # dims.py 产物（第 79 批多维画像），缺失则跳过
DIMS = json.load(open(DIMS_JSON, encoding='utf-8')) if os.path.exists(DIMS_JSON) else {}
from batch82 import fmt_batch82  # T29-U64 第 82 批：邮箱域体检 + 假日避让 + 公司底数 + 官网标价
IMPORTS_DIR = os.path.join(DATA, 'imports')               # T29-U62：公开海关提单（ImportYeti 美国海运）逐户查询结果，缺失则跳过


def _load_imports():
    """T29-U63：一个客户可能同时有美国提单（ImportYeti）和其他国家来源（HMRC / Volza / NBD …）→ 每码一个列表。
    文件 _meta.kind 缺省为 'importyeti'（第 80 批美国海运提单），'other' = 第 81 批其他国家来源。"""
    out = {}
    if not os.path.isdir(IMPORTS_DIR):
        return out
    for fn in sorted(os.listdir(IMPORTS_DIR)):
        if not fn.endswith('.json'):
            continue
        d = json.load(open(os.path.join(IMPORTS_DIR, fn), encoding='utf-8'))
        meta = d.get('_meta', {})
        for code, row in (d.get('rows') or {}).items():
            row = dict(row)
            row['_src'] = meta.get('source', fn)
            row['_kind'] = meta.get('kind', 'importyeti')
            out.setdefault(code, []).append(row)
    return out


IMPORTS = _load_imports()
WEEKDAY_CN = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
MONTH_CN = {1: '1 月', 2: '2 月', 3: '3 月', 4: '4 月', 5: '5 月', 6: '6 月', 7: '7 月', 8: '8 月', 9: '9 月', 10: '10 月', 11: '11 月', 12: '12 月'}


def _hm(h):
    return f'{int(h):02d}:{int(round((h - int(h)) * 60)):02d}'


def fmt_dims(ent):
    """多维画像（第 79 批 · T29-U61）：dims.py 的机械推导，按维度一行；没有信号的维度不写。"""
    d = DIMS.get(ent['code'])
    if not d:
        return ''
    L = []
    t = d.get('timing')
    if t and t.get('n'):
        seg = [f"真人来信 {t['n']} 封（{t['first']} → {t['last']}）"]
        if t.get('months_top'):
            seg.append('多在 ' + ' / '.join(f'{MONTH_CN[m]}（{n}）' for m, n in t['months_top']))
        if t.get('local_hour_median') is not None and t['n'] >= 2:
            iq = f"，四分位 {_hm(t['local_hour_iqr'][0])}–{_hm(t['local_hour_iqr'][1])}" if t.get('local_hour_iqr') else ''
            tz = (d.get('calendar') or {}).get('tz')
            bj = f"（= 北京时间 {_hm((t['local_hour_median'] - tz + 8) % 24)}）" if isinstance(tz, (int, float)) else ''
            seg.append(f"对方本地时间中位 {_hm(t['local_hour_median'])}{iq}{bj}")
        if t.get('weekdays') and t['n'] >= 3:
            seg.append(f"{t['weekdays'][0][0]}最多（{t['weekdays'][0][1]}）" + (f"、周末 {t['weekend_share']}%" if t.get('weekend_share') else ''))
        if t.get('their_reply_n'):
            seg.append(f"**他们回信中位 {t['their_reply_h_median']} 小时**（{t['their_reply_n']} 次，{t['their_reply_fast_share']}% 在 24 小时内）")
        if t.get('our_reply_n'):
            slow = f"，>72 小时 {t['our_reply_slow']} 次" if t.get('our_reply_slow') else ''
            seg.append(f"我方回信中位 {t['our_reply_h_median']} 小时（{t['our_reply_n']} 次{slow}）")
        if t.get('unanswered_in'):
            seg.append(f"**我方未回 {t['unanswered_in']} 封**")
        L.append('- **时机与节律**：' + '；'.join(seg) + '。')
    cw = d.get('country_window')
    if cw and cw.get('best'):
        best = '、'.join(f"{WEEKDAY_CN[b['wd']]} {b['h']:02d}–{b['h'] + 2:02d} 点 {b['rate']}%（{b['n']} 封）" for b in cw['best'])
        L.append(f"- **发信窗口（{cw['iso']} 全库 {cw['sent']} 封群发的打开标签，对方本地时间；均值 {cw['avg']}%）**：{best}。像素统计，只看相对高低；排发信日时落在这两个时段。")
    cs = d.get('country_season')
    if cs:
        L.append(f"- **本国来询季节（{cs['iso']} 全库 {cs['n']} 个「户·月」真人来信{'，样本小' if cs['n'] < 30 else ''}）**：" + ' / '.join(f"{MONTH_CN[x['m']]} {x['pct']}%" for x in cs['top']) + '——本户来信太少，按本国节奏排下一步。')
    o = d.get('opens')
    if o and o.get('sent'):
        seg = [f"群发 {o['sent']} 封（{o['first_sent']} → {o['last_sent']}），打开标签 {o['opened']} 次" + (f"（近 12 个月 {o['opened_12m']}，最后 {o['last_opened']}）" if o['opened'] else '')]
        if o.get('bounce_days'):
            seg.append(f"退信日 {o['bounce_days']} 个（前后一天的打开已剔除）")
        if o.get('opened_subjects'):
            seg.append('打开过：' + '、'.join(f'「{s}」×{n}（{dt}）' for s, n, dt in o['opened_subjects']))
        if o.get('never_opened') and o['opened']:
            seg.append('从未打开：' + '、'.join(f'「{s}」' for s in o['never_opened'][:3]))
        if o.get('streak_unopened', 0) >= 6 and not o.get('opened_180d'):
            seg.append(f"**最近连续 {o['streak_unopened']} 封没打开**（近 180 天发 {o['sent_180d']} 封 0 打开）→ 群发对这户已失效，停两个月，改一句 1:1 或换收件人")
        elif o.get('opened_180d'):
            seg.append(f"近 180 天发 {o['sent_180d']} 封、打开 {o['opened_180d']} 次 → 还在读，主题沿着打开过的那类走")
        L.append('- **打开偏好**（Opened = 像素，代理网关会误触发，只作参考）：' + '；'.join(seg) + '。')
    q = d.get('quotes')
    if q and q.get('rows'):
        tier_note = f"{q['rows'][0]['tier_used']}% 档" + ('' if q.get('tier_known') else '（未定档，暂按 25%）')
        mix = f"1:1 {q.get('n_1to1', q['n'])} 条" + (f" + 个性化群发价 {q['n_mass']} 条" if q.get('n_mass') else '')
        L.append(f"- **报价轨迹**（S/A 去信里「价 + 型号/描述同句」：{mix}，{q['first']} → {q['last']}；「今天」= 价格主表 2026-10-17 汇率、{tier_note}、不高于 2026-06 列表价；只列每个型号/描述最近一次，最多 8 行）：")
        L.append('')
        L.append('  | 日期 | 型号 / 原句 | 当时 | 今天应报 | 变化 | 性质 | 主题 | 消息 key |')
        L.append('  |---|---|---|---|---|---|---|---|')
        for r in q['rows']:
            what = r['model'] or ('「' + re.sub(r'[*_`]+', '', (r.get('desc') or '')).replace('|', '/').replace('1*', '1×') + '」')
            if r['model']:
                today = f"${r['today']}" if r.get('today') else '主表无此型号'
            else:
                today = '—（原句无型号）'
            delta = (f"{'+' if r['delta_pct'] > 0 else ''}{r['delta_pct']}%" if r.get('delta_pct') is not None else '—')
            L.append(f"  | {r['date']} | {what} | ${r['price']:g} | {today} | {delta} | {r.get('kind', '1:1')} | {r['subj'].replace('|', '/')} | `{r['k']}` |")
        L.append('')
        ups = [r for r in q['rows'] if (r.get('delta_pct') or 0) >= 5]
        downs = [r for r in q['rows'] if (r.get('delta_pct') or 0) <= -5]
        note = []
        if ups:
            note.append('涨的部分只有一个口径：汇率 7.2 → 6.7（成本按人民币不变）；对方若拿旧价压，先认旧价有效期已过，再谈量')
        if downs:
            note.append('今天比当时低：直接报今天的价，顺手说一句「比上次低」是现成的开场')
        if q.get('n_mass'):
            note.append('「个性化群发价」= 同一句价发给 ≥5 家的信（Simon 的手工群发），对方未必读过，但它就是对方邮箱里躺着的「上次报价」')
        if note:
            L.append('  ' + '；'.join(note) + '。')
    cv = d.get('coverage')
    if cv:
        seg = ['官网兴趣：' + ' / '.join(f'{c}（{ev}）' for c, ev in cv['interest'])]
        shown = cv.get('shown') or {}
        if shown or cv.get('bought'):
            parts = [f'{k} ×{v}' for k, v in shown.items()]
            seg.append('我们报过 / 卖过：' + '、'.join(parts) + (f"（买过 {'、'.join(cv['bought'])}）" if cv.get('bought') else ''))
        else:
            seg.append('我们 1:1 从未报过价、也没成交')
        if cv.get('opened_cats'):
            seg.append('打开过的群发主题落在：' + ' / '.join(cv['opened_cats']))
        if cv.get('gaps'):
            g = cv['gaps'][0]
            price = f"${g['price']}" if g.get('price') else '价见主表'
            seg.append(f"**还没碰过的一类：{g['cat']}** → 下封信可加一句 {g['model']}（{g['desc']}，{price} EXW）")
        else:
            seg.append('兴趣品类都已碰过——缺口不在品类，在上面的断点')
        L.append('- **品类覆盖与缺口**：' + '；'.join(seg) + '。')
    sc = d.get('scale')
    if sc:
        seg = []
        if sc.get('sitemap'):
            seg.append(f"站点地图 {sc['sitemap']} 条 URL" + ('（≥500 = 大目录 / 网店体量）' if sc['sitemap'] >= 500 else ''))
        if sc.get('brands_n'):
            seg.append(f"站内可见品牌 {sc['brands_n']} 个（{'、'.join(sc['brands'])}）" + ('——多品牌分销位，Saga 作「同口数 Marvell 方案低一档」的补位货源' if sc['brands_n'] >= 4 else ''))
        if sc.get('own_label'):
            seg.append(f"**自有型号串 {len(sc['own_label'])} 个**（{'、'.join(sc['own_label'][:3])}）→ 已在贴自己的牌：按 OEM 档说话（logo 免费、彩盒 $2.5/套 200 起）")
        if sc.get('lang') and not str(sc['lang']).lower().startswith('en'):
            seg.append(f"官网语言 {sc['lang']}（信照样英文，首句可用对方语言问候）")
        if sc.get('social'):
            seg.append('社媒：' + '、'.join(sc['social'][:3]))
        if seg:
            L.append(f"- **规模与贴牌线索（官网快照 {sc.get('fetched', '')}）**：" + '；'.join(seg) + '。')
    rel = d.get('related')
    if rel:
        L.append('- **关联户**：' + '；'.join(f"{r['code']} {r['name'][:30]}（{r['grade']}；{'、'.join(r['why'])}）" for r in rel) + '——写信前看一眼对方档案，别两边说两套价。')
    pp = d.get('people')
    if pp:
        seg = []
        for p in pp:
            nm = p.get('name') or p['email'].split('@')[0]
            tt = f" — {p['title']}" if p.get('title') else ''
            seg.append(f"{nm}{tt}（{p['email']}，{p['n']} 封，{p['first']} → {p['last']}）")
        L.append('- **写信的人（来信签名机械抽取）**：' + '；'.join(seg) + '。')
    w = d.get('words')
    if w:
        seg = []
        if w.get('topics'):
            seg.append('话题（次数，最近一次）：' + '、'.join(f'{k} ×{n}（{dt}）' for k, n, dt in w['topics']))
        if w.get('competitors'):
            seg.append('**提到的同行品牌**：' + '、'.join(f'{k} ×{n}（{dt}）' for k, n, dt in w['competitors']))
        if w.get('chips'):
            seg.append('芯片 / 供应商词：' + '、'.join(f'{k} ×{n}' for k, n, _ in w['chips']))
        if w.get('qty'):
            seg.append('**提过的数量**：' + '；'.join(f"{q['q']:,}（{q['date']}，「…{q['ctx']}…」，`{q['k']}`）" for q in w['qty']))
        L.append(f"- **他们嘴里的词（{w['n_mails']} 封来信、去引用后 {w['chars']:,} 字符的词频）**：" + '；'.join(seg) + '。')
    ch = d.get('channels')
    if ch:
        seg = []
        for mb, v in ch.items():
            who = {'S': 'S 箱（Simon）', 'A': 'A 箱（Alan）'}[mb]
            seg.append(f"{who} 去 {v['out']}（1:1 {v['one']} / 群发 {v['mass']}）回 {v['in']}" + (f"，最近回 {v['last_in']}" if v['last_in'] else '，从未回'))
        ins = {mb: v['in'] for mb, v in ch.items()}
        verdict = ''
        if sum(1 for v in ins.values() if v) == 1:
            only = [mb for mb, v in ins.items() if v][0]
            verdict = f" → 只对 {'S 箱 Simon' if only == 'S' else 'A 箱 Alan'} 有反应，下一封别换箱"
        elif all(ins.values()):
            verdict = ' → 两箱都回过，按绑定行的渠道走即可'
        L.append('- **渠道反应**：' + '；'.join(seg) + verdict + '。')
    b = d.get('ball')
    if b:
        seg = [f"1:1 对话 {b['threads']} 段，最长一段 {b['longest_n']} 封 / 跨 {b['longest_days']} 天（{b['longest_first']} → {b['longest_last']}，「{b['longest_subj']}」）"]
        if b['last_dir'] == 'in':
            seg.append(f"**最后一句是他们说的**（{b['last_date']}，{b['days_since']} 天前，「{b['last_subj']}」，`{b['last_k']}`）" + (f"：「{b['last_snippet']}…」" if b.get('last_snippet') else ''))
            if b.get('last_questions'):
                seg.append('**他们没得到答复的问题**：' + ' / '.join(f'「{q}」' for q in b['last_questions']))
        else:
            seg.append(f"最后一句是我们说的（{b['last_date']}，{b['days_since']} 天前，「{b['last_subj']}」，`{b['last_k']}`）→ 球在对方手里")
            med = (d.get('timing') or {}).get('their_reply_h_median')
            n_rep = (d.get('timing') or {}).get('their_reply_n') or 0
            if med and n_rep >= 3:
                ratio = b['days_since'] * 24 / med
                if ratio >= 10 and b['days_since'] <= 120:
                    seg.append(f"按他们过去中位 {med} 小时回信（{n_rep} 次），这次 {b['days_since']} 天没回 ≈ 常态的 {ratio:.0f} 倍 → **值得追一句**（不是催，是换个问法）")
                elif ratio < 3:
                    seg.append(f"他们过去中位 {med} 小时回信，这次才 {b['days_since']} 天 → 还在常态内，别催")
        L.append('- **最后一球**：' + '；'.join(seg) + '。')
    lk = d.get('lookalike')
    if lk:
        tier_s = f"{lk['tier']}% 档" if lk.get('tier') else '同线'
        line_s = f"、主推线「{lk['line']}」" if lk.get('line') else ''
        seg = '；'.join(f"{r['code']} {r['name']}（{r['grade']}，{r['why']}：{'，'.join(r['did'])}）" for r in lk['refs'])
        L.append(f"- **同国同档参照（{lk['iso']}，{tier_s}{line_s}，共 {lk['n']} 户有动静，列前 3）**：{seg}。用法：他们回过 / 买过的型号与价位就是这个国家这一档的「已验证组合」，写信时按同一组合起手；**信里不点名其他客户**。")
    gh = d.get('github')
    if gh:
        seg = []
        for a in gh.get('accounts') or []:
            how = {'strong': '官网/邮箱域名一致', 'name': '仅名称一致，未核实是否同一家', 'company': 'company 字段一致'}.get(a.get('match'), '')
            repos = [r['name'] for r in (a.get('repos') or []) if not r.get('fork')][:3]
            last = max((r.get('pushed_at') or '' for r in (a.get('repos') or [])), default='')[:10]
            seg.append(f"{'组织' if a.get('type') == 'Organization' else '用户'} [{a['login']}]({a['url']})（{how}；公开仓库 {a.get('public_repos')}" + (f"，最近 push {last}：{'、'.join(repos)}" if repos else '') + '）')
        if seg:
            L.append(f"- **GitHub 足迹（公开资料，{(gh.get('checked_at') or '')[:10]} 查）**：" + '；'.join(seg) + '——有工程师在写代码的客户，SNMP / CLI / LibreNMS 适配是现成话题（NYNEX 先例）。')
    cal = d.get('calendar')
    if cal:
        seg = []
        if cal.get('holidays'):
            seg.append('对方：' + '；'.join(f'{dd} {nm}' for dd, nm in cal['holidays']))
        seg.append(cal['cny'])
        L.append('- **日历窗口**：' + ' ｜ '.join(seg))
    if not L:
        return ''
    head = [f"## 多维画像（数据推导 · 第 79 批 · {d.get('generated_at', TODAY)}）", '',
            '> 只用仓库里已有的证据机械推导（S/A 邮箱索引、报价史、PI 包、官网快照摘要、GitHub 公开资料），每条带数字 / 日期 / 消息 key；没有信号的维度不写。'
            '**不替代上面的「针对性复盘」**，只是多几把尺子：什么时候发、发什么、找谁、还有哪一类没碰。重算：`python3 scripts/saga_clients/dims.py` 后重渲染。', '']
    return '\n'.join(head + L) + '\n'


def fmt_imports_other(r):
    """第 81 批 · T29-U63：非美国来源（HMRC 英国官方 / Volza / NBD / ImportGenius / Tendata / MarketInsideData 免费摘要）。"""
    L = [f"## 进口记录（公开海关数据 · 第 81 批 · {r.get('fetched', TODAY)}）", '',
         f"> 来源：**{r.get('source', r.get('_src', ''))}**。{r.get('coverage', '')} 查询日 {r.get('fetched', TODAY)}。", '']
    if not r.get('found'):
        tried = '；'.join(r.get('tried') or [])
        L.append(f"- **查无**：{tried or '按公司名查不到'}。")
        for x in r.get('lines') or []:
            L.append(f"- {x}")
        if r.get('notes'):
            L.append(f"- **对 Saga 的含义**：{r['notes']}")
        L.append('- 查无 ≠ 不进口：可能用别的报关主体名、走快递 / 空运、或该国海关数据根本不对外公开。')
        return '\n'.join(L) + '\n'
    head = []
    if r.get('name'):
        head.append(f"报关主体 **{r['name']}**")
    if r.get('latest'):
        head.append(f"最近记录 **{r['latest']}**")
    if r.get('url'):
        head.append(f"[来源页]({r['url']})")
    if head:
        L.append('- ' + '；'.join(head))
    for x in r.get('lines') or []:
        L.append(f"- {x}")
    if r.get('hs'):
        L.append('- **涉及商品编码**：' + '、'.join(str(h) for h in r['hs']))
    if r.get('partners'):
        L.append('- **已披露的贸易伙伴**：' + '；'.join(r['partners']))
    if r.get('notes'):
        L.append(f"- **对 Saga 的含义**：{r['notes']}")
    return '\n'.join(L) + '\n'


def fmt_imports(ent):
    """进口记录：第 80 批 ImportYeti（美国海运提单）+ 第 81 批其他国家来源；一个客户可能两段都有。查无也写，省得下次再查。"""
    rows = IMPORTS.get(ent['code']) or []
    out = []
    for r in rows:
        if r.get('_kind') == 'other':
            out.append(fmt_imports_other(r))
        else:
            out.append(fmt_imports_us(r))
    return '\n'.join(out)


def fmt_imports_us(r):
    """第 80 批 · T29-U62：ImportYeti（美国海关海运提单）逐户查询。"""
    L = [f"## 进口记录（公开海关数据 · 第 80 批 · {r.get('fetched', TODAY)}）", '',
         '> 来源：ImportYeti 整理的 **美国海关（CBP）海运提单**，2015-01 起；只覆盖海运到美国港口的货，**空运 / 快递 / 陆运看不见，欧洲 / 土耳其 / 加拿大按公司查不到**。'
         '美国提单**没有货值**，只有到港日 / 发货人 / 重量 / 件数 / 品名 / 估算海运费——所以「金额」一栏给不出，量只能用重量与箱数估。查询日 ' + str(r.get('fetched', TODAY)) + '。', '']
    if not r.get('found'):
        tried = '；'.join(r.get('tried') or [])
        L.append(f"- **查无**：ImportYeti 公司页没有此户（{tried or '按公司名 slug 查 404'}）。{r.get('notes', '')}".rstrip())
        L.append('- 查无 ≠ 不进口：可能用别的报关主体名、走空运 / 快递、或申请了舱单保密（ImportYeti FAQ）。')
        return '\n'.join(L) + '\n'
    seg = []
    if r.get('total_shipments') is not None:
        seg.append(f"海运提单 **{r['total_shipments']} 票**（{r.get('range', '')}）")
    if r.get('last_shipment'):
        seg.append(f"最近一票 **{r['last_shipment']}**")
    if r.get('avg_teu_month'):
        seg.append(f"月均 {r['avg_teu_month']} TEU")
    if r.get('est_freight'):
        seg.append(f"ImportYeti 估算海运费累计 {r['est_freight']}（不是货值）")
    if r.get('lcl_fcl'):
        seg.append(str(r['lcl_fcl']))
    if r.get('ports'):
        seg.append('到港 ' + str(r['ports']))
    L.append(f"- **总量**：{'；'.join(seg)}。[公司页]({r['url']})（synced {r.get('synced', '')}）")
    if r.get('china_share'):
        L.append(f"- **中国占比**：{r['china_share']}")
    sup = r.get('suppliers') or []
    if sup:
        L.append('- **主要发货人**（票数 · 品名）：')
        for x in sup[:9]:
            L.append(f"  - {x.get('n', '')}（{x.get('c', '')}）· {x.get('s', '?')} 票 · {x.get('p', '')}")
    rec = r.get('recent') or []
    if rec:
        L.append('- **近期提单**（到港日 · 发货人 · 重量/件数 · 品名）：')
        for x in rec[:10]:
            L.append('  - ' + ' · '.join(str(v) for v in x))
    for k, lab in (('hrui_shipments', 'HRUI 直采票数'), ('onv_shipments', 'ONV 票数'), ('centro_shipments', 'Shenzhen Centro 票数')):
        if r.get(k) is not None:
            L.append(f"- **{lab}**：{r[k]}")
    if r.get('notes'):
        L.append(f"- **对 Saga 的含义**：{r['notes']}")
    if r.get('related'):
        L.append(f"- 关联户：{r['related']}")
    return '\n'.join(L) + '\n'
PI_DIR = os.path.join(ROOT, 'data', 'pi_orders')  # parse_pi.py 产物（PI 包成交记录），缺失则跳过


def _load_pi():
    out = {}
    p = os.path.join(PI_DIR, '单号对照.csv')
    if not os.path.exists(p):
        return out
    for r in csv.DictReader(open(p, encoding='utf-8-sig')):
        out.setdefault(r['客户文件夹'], []).append(r)
    return out


PI_ORDERS = _load_pi()

WATCH_DIR = os.path.join(ROOT, 'data', 'customer_watch')      # web_watch 产物（运行器上跑，state.json 每轮覆盖）
WATCH_CFG = os.path.join(ROOT, 'scripts', 'web_watch')


def _load_watch():
    """T29-U19：把监控清单（targets.json 精选层 + targets_auto.json 面层）和最近状态（state.json）按客户码合并。"""
    out = {}
    def _j(p):
        return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None
    cur = _j(os.path.join(WATCH_CFG, 'targets.json')) or {'customers': []}
    auto = _j(os.path.join(WATCH_CFG, 'targets_auto.json')) or {'customers': []}
    state = _j(os.path.join(WATCH_DIR, 'state.json')) or {}
    for c in cur['customers']:
        o = out.setdefault(c['code'], {'layer': '成单精选层', 'sources': [], 'manual': []})
        o['sources'] += [dict(x) for x in c['sources']]
        o['manual'] += [m if isinstance(m, str) else f"{m.get('label')}: {m.get('url')}" for m in c.get('manual', [])]
    for c in auto['customers']:
        o = out.setdefault(c['code'], {'layer': f"{c.get('grade', 'B')} 级面层", 'sources': [], 'manual': []})
        have = {x.get('url') or x.get('login') for x in o['sources']}
        for x in c['sources']:
            if (x.get('url') or x.get('login')) in have:
                continue
            x = dict(x)
            if o['layer'] == '成单精选层':
                x['id'] = 'auto_' + x['id']
            o['sources'].append(x)
        for m in c.get('manual', []):
            t = m if isinstance(m, str) else f"{m.get('label')}: {m.get('url')}"
            if t not in o['manual']:
                o['manual'].append(t)
    meta = state.get('_meta') or {}
    for code, o in out.items():
        if meta.get(code, {}).get('feed_auto'):
            o['sources'].append({'id': 'feed_auto', 'kind': 'rss', 'url': meta[code]['feed_auto'], 'note': '首页自动发现的 feed'})
        o['meta'] = meta.get(code) or {}
        for x in o['sources']:
            x['state'] = state.get(f"{code}/{x['id']}") or {}
    return out


WATCH = _load_watch()


def fmt_watch(ent):
    """动态监控（自动）：列出该客户被监控的源、最近状态、最近变化；只读事实，不做判断。"""
    w = WATCH.get(ent['code'])
    if not w:
        return ''
    L = []
    fetched = [x['state'].get('fetched_at') for x in w['sources'] if x['state'].get('fetched_at')]
    last_change = max([x['state'].get('last_change_at') or '' for x in w['sources']] + [''])
    note = w['meta'].get('last_change_note') or ''
    L.append(f"- **监控层**：{w['layer']}　|　**自动源**：{len(w['sources'])} 个　|　**数据截至**：{max(fetched) if fetched else '尚未跑过首轮（清单已就位，等运行器基线）'}"
             + (f"　|　**最近变化**：{last_change}" if last_change and last_change != '-' else ''))
    if note:
        L.append(f"- **最近变化摘要**：{md_escape(note)}")
    L.append('- 规则：运行器每轮抓取 → 与上轮比对 → 变化 append-only 记入 `data/customer_watch/变化日志.md`（成单层）/ `变化日志_AB.md`（A/B 层），最新文本在 `data/customer_watch/snapshots/' + ent['code'] + '/`；本节随档案重渲染刷新，实时看日志。')
    L.append('')
    L.append('| 源 | 类型 | 状态 | 最近变化 | 摘要 |')
    L.append('|---|---|---|---|---|')
    for x in w['sources'][:10]:
        st = x['state']
        status = st.get('error') or (f"HTTP {st.get('status')}" if st.get('status') else '待首轮')
        url = x.get('url') or ('https://github.com/' + x.get('login', ''))
        L.append(f"| [{x['id']}]({url}) | {x['kind']} | {md_escape(str(status))[:60]} | {st.get('last_change_at', '—')} | {md_escape(st.get('summary') or x.get('note') or '')[:90]} |")
    if len(w['sources']) > 10:
        L.append(f"| …共 {len(w['sources'])} 个源（全表见 `data/customer_watch/当前状态*.md`） | | | | |")
    if w['manual']:
        L.append('')
        L.append('- **人工定期看（登录墙，不自动抓）**：' + '；'.join(md_escape(m) for m in w['manual'][:8]))
    return '\n'.join(L)


def load_digest():
    if not os.path.exists(DIGEST_JSON):
        return {}
    try:
        return json.load(open(DIGEST_JSON, encoding='utf-8'))
    except Exception:
        return {}


SITE = load_digest()


def load_sieve():
    """T29-U117：C 池三闸筛选状态（data/saga_clients/sieve.json）。pass_final = 永久 pass，MD 顶部挂横幅。"""
    p = os.path.join(DATA, 'sieve.json')
    if not os.path.exists(p):
        return {}
    d = json.load(open(p, encoding='utf-8'))
    return {k: v for k, v in d.items() if k != '_meta'}


SIEVE = load_sieve()
SIEVE_TAG_NOTE = {'dayjob_fit': '（光端机 / DWDM / 光模块 —— Simon 本职公司可用，不 pass）', 'oem_target': '（贴牌卖交换机的渠道商 —— OEM 专项对象，留 C）'}
SIEVE_LABEL = {'pass_final': '⛔ 已过筛 · 永久 pass', 'keep_C': '留 C 储备', 'candidate': '闸 2 候选', 'pool_candidate': 'P 池候选', 'pool': '★ P 池 · 正式入池（资产池，终身跟进 + 每 2 个月巡检）', 'pool_watch': '☆ P 池 · 观察档（试单 / 回访后转正或退回 C）'}

# 兴趣 → Saga 主推（型号, 场景说明）
P1_RULES = [
    (r'48', 'STC-448DGGPM', '48 口 PoE 走量款'),
    (r'24.{0,3}(poe|PoE|POE)|4光24|2光24|24口|24电|24 ?PoE', 'STC-424DGGPM-280W', '24 口 PoE L2+ 走量款'),
    (r'10G|10g|万兆|2\.5G|2\.5g', 'STC-424XGGPM-280W', '24 口 PoE + 4×10G 上联'),
    (r'L3|三层|3层|核心|core|汇聚|数据中心|DC|堆叠|stack', 'STC-448XGGM(L3)', 'L3 48 口 + 4×10G（Hohunet/CENTEC 线）'),
    (r'16.{0,3}(poe|PoE|POE)|16电|16口|2光16|16 ?PoE', 'STI-21616GP', '工业 16 PoE + 2 SFP'),
    (r'工业.{0,6}(PoE|POE|poe)|导轨|DIN|din', 'STI-288DGGPM', '工业 L2+ 8 PoE + 2×2.5G SFP'),
    (r'1光4|4电|5电口|5口|4口|4 ?PoE|4PoE', 'STI-144GP', '工业 4 PoE + 1 SFP 小壳'),
    (r'2光8|1光8|8.{0,3}(poe|PoE|POE)|8电|8口|8 ?PoE|商业PoE|商业POE|商业poe', 'STC-28DGGPM', '8 口 PoE + 2 SFP L2+'),
    (r'工业FS|工业交换机|工业|industrial|Industrial', 'STI-288DGGPM', '工业 L2+ 8 PoE + 2×2.5G SFP'),
    (r'MC|media converter|光纤收发器|收发器', 'STI-110GE', '工业迷你 1 光 1 电（MC 位）'),
    (r'SFP|光模块|DAC|AOC|模块', None, 'SFP/DAC：Saga 三份价格表无光模块 → 按需询 SmartByte/HRUI'),
    (r'VC|光端机|AHD|HDMI|视频|video', None, 'VC/光端机：Saga 不做（可只推交换机）'),
    (r'DWDM|OTDR|相干|QSFP|200G|400G', None, 'DWDM/OTDR：Saga 不做'),
    (r'PoE|POE|poe|switch|Switch|交换机|FS', 'STC-424DGGPM-280W', '24 口 PoE L2+ 走量款'),
]
BRANDS = ['ONV', 'Utepo', 'Upeto', 'Ewind', '洪瑞', 'HRUI', '中科德能', 'E-link', 'Elink', 'E-Link', 'BDCOM', 'PLANET', 'Planet', 'planet', 'Cisco',
          'Redlion', 'redlion', 'Red Lion', 'Moxa', 'MOXA', 'Antaira', 'Hikvision', 'Dahua', 'TP-Link', 'Mikrotik', 'MikroTik', 'Ubiquiti', 'Netgear',
          'Trendnet', 'Kontron', '迈威', 'Maiwe', '丰润达', '磊通', 'GXCOM', 'Gxcom', 'Witek', 'Diva', 'Longse', 'N-net', 'OTS', 'UniPoE', '优力普',
          'Oring', 'ORing', 'Korenix', 'Westermo', 'Hirschmann', 'Phoenix', 'Advantech', 'Lantech', 'Comnet', 'ComNet', 'Perle', 'Transition',
          'Allied Telesis', 'D-Link', 'Zyxel', 'Tenda', 'Ruijie', 'H3C', 'Huawei', 'Uotek', 'Mlis', 'CTCU', 'Aruba', 'HPE', 'Dell', 'Juniper',
          'Extreme', 'Ubiquiti', 'Cambium', 'G-net', 'Gnet', 'Hioso', 'Fiberhome', 'ZTE', 'Raisecom', 'Televes', 'Dptek', 'DPTEK', 'Smartbyte',
          'SmartByte', 'Realtek', 'Marvell', '海思', 'Hisilicon', '华为', '海康', '大华', 'Axis', 'Bosch', 'Hanwha', 'Uniview', 'UNV', 'Milesight',
          'Teltonika', 'Robustel', 'InHand', 'Siemens', 'Weidmuller', 'Weidmüller', 'Belden', 'EtherWAN', 'Black Box', 'StarTech', 'TRENDnet',
          'Zebra', 'Supermicro', 'FS.com', 'FS', 'Ubiquiti', '武汉迈威', 'Kyland', '东土', 'Ruggedcom', 'Scalance']
TYPE_RULES = [
    (r'自己的logo|自己的品牌|自己的标|自己的牌子|自己的型号|自有品牌|OEM|ODM|贴牌|own brand|private label|刷了自己', '品牌商/贴牌需求（OEM/ODM）'),
    (r'分销|distributor|Distributor|销售平台|有人卖他们|有人在卖|经销|reseller|wholesale|批发|trader|trading|贸易|Trading', '分销商/经销商'),
    (r'集成|integrator|工程|项目|project|Project|solution|Solution|engineering|Engineering|安装|installer|方案', '系统集成/工程商'),
    (r'CCTV|安防|security|Security|监控|camera|摄像头|guvenlik|güvenlik|seguridad|segurança|sicurezza', '安防集成/经销'),
    (r'电信|telecom|Telecom|ISP|运营商|wisp|WISP|network operator', '电信/ISP/网络运营'),
    (r'自动化|automation|Automation|控制|PLC|IoT|物联网|工业控制', '工业自动化/IoT 方案商'),
    (r'电商|shop|Shop|store|Store|e-?commerce|online', '电商/网店'),
    (r'制造|manufactur|Manufactur|厂商|工厂|factory', '制造商（可能是同行或 OEM 客户）'),
]


def load_prices():
    by = {}
    if not os.path.exists(PRICE_CSV):
        return by
    for r in csv.DictReader(open(PRICE_CSV, encoding='utf-8-sig')):
        k = r['Saga对应型号'].strip()
        if k and not k.startswith('（') and k not in by:
            by[k] = r
    # 回退：Saga 暂无对应名的 SmartByte 型号（如 bypass 系列）按 SmartByte 型号索引，MD 中须注明「SmartByte 型号」
    for r in csv.DictReader(open(PRICE_CSV, encoding='utf-8-sig')):
        k2 = (r.get('SmartByte型号') or '').strip()
        if k2 and k2 not in by:
            by[k2] = r
    return by


PRICES = load_prices()


def load_alt_prices():
    """Saga 对外价（HRUI Realtek 线 / Hohunet CENTEC 线对照表）——SmartByte 价格主表无此型号时的回退。"""
    alt = {}
    for fn, src in (('hrui_STC对照表.csv', 'HRUI Realtek 线'), ('hohunet_STH对照表.csv', 'Hohunet CENTEC 线')):
        fp = os.path.join(ROOT, 'data', fn)
        if not os.path.exists(fp):
            continue
        for r in csv.DictReader(open(fp, encoding='utf-8-sig')):
            k = (r.get('Saga型号') or '').strip()
            price = (r.get('Saga对外价USD_EXW') or r.get('Saga对外价USD') or '').strip()
            if k and price and k not in alt:
                alt[k] = (price, src, fn)
    return alt


ALT_PRICES = load_alt_prices()


def load_hrui_tiers():
    """HRUI Realtek 线三档价：data/价格主表_HRUI.csv（洪瑞 2026-09-30 报价单 CNY 不含税含运 → USD × 1.20/1.25/1.30）。
    第 73 批口径：Saga 列表价隐含加价已低于 20% 底线的型号（028GP $24.2 → $25.1、228GP $30.8 → $33.2 …）按成本 + 档位报；
    列表价高于档位价的沿用列表价（不低于自家公开价）。同一 Saga 型号对到多个 ZX 码时取 CSV 首行（对照表所对的 902 系列）。"""
    fp = os.path.join(ROOT, 'data', '价格主表_HRUI.csv')
    out = {}
    if not os.path.exists(fp):
        return out
    for r in csv.DictReader(open(fp, encoding='utf-8-sig')):
        for sm in [x.strip() for x in (r.get('Saga对应型号') or '').split('/') if x.strip()]:
            if sm in out:
                continue
            try:
                out[sm] = {20: float(r['USD@+20%']), 25: float(r['USD@+25%']), 30: float(r['USD@+30%']),
                           'list': float(r['Saga列表价USD']) if r.get('Saga列表价USD') else None, 'zx': r['ZX型号'], 'rate_date': r.get('汇率日期', '')}
            except (ValueError, KeyError):
                continue
    return out


HRUI_TIERS = load_hrui_tiers()


def hrui_price(model, tier):
    """→ (price_float, basis_str) 或 None。max(成本+档位, Saga 列表价)。"""
    t = HRUI_TIERS.get(model)
    if not t:
        return None
    v = t.get(tier) or t[25]
    if t.get('list') and t['list'] > v:
        return t['list'], f'Saga 对外列表价 ${t["list"]}（高于洪瑞 2026-09-30 成本 + {tier}% = ${v}）'
    return v, f'洪瑞 2026-09-30 成本 + {tier}%（列表价 ${t.get("list")} 隐含加价低于底线，第 73 批口径）'


def tier_price(r, tier):
    """SmartByte 档位价 → (价, 是否封顶)。规则 ㉕：任何数不得高于 2026-06 Saga 列表价（2.5G-SFP 工业 DGG 家族等
    档位价已高于列表价的型号按列表价封顶）。"""
    col = {20: 'USD@+20%', 25: 'USD@+25%', 30: 'USD@+30%'}[tier]
    v = float(r[col])
    try:
        lst = float(r.get('Saga列表价USD') or 0)
    except ValueError:
        lst = 0
    if lst and v > lst:
        return f'{lst:g}' if lst != int(lst) else f'{lst:.1f}', True
    return r[col], False


def price_line(model, tier):
    r = PRICES.get(model)
    if not r:
        h = hrui_price(model, tier)
        if h:
            return f"${h[0]} USD EXW（HRUI Realtek 线：{h[1]}；见 data/价格主表_HRUI.csv；汇率 {HRUI_TIERS[model]['rate_date']}，15 天有效，报价前核价）"
        a = ALT_PRICES.get(model)
        if a:
            return f"${a[0]} USD EXW（Saga 对外列表价，{a[1]}，见 data/{a[2]}；非 SmartByte 加价公式，报价前核价）"
        return '价格待核（价格主表无此型号）'
    col = {20: 'USD@+20%', 25: 'USD@+25%', 30: 'USD@+30%'}[tier]
    if model in ELSA_LIVE_NOW:
        return (f"${ELSA_LIVE_NOW[model]} USD EXW（㉕ ② 群发现价（群发价台账），{tier}% 档公式为 ${r[col]}——同一客户随时可能收到 Alan 的群发，信稿不高于群发价；"
                f"汇率快照 {r['汇率日期']}，15 天有效，报价前核价）")
    v, capped = tier_price(r, tier)
    if capped:
        return (f"${v} USD EXW（㉕ 封顶：{tier}% 档 ${r[col]} 高于 2026-06 Saga 列表价 ${v}，按列表价；"
                f"SmartByte {r['SmartByte型号']} {r['CNY未税']} CNY，汇率快照 {r['汇率日期']}，15 天有效，报价前核价）")
    return (f"${r[col]} USD EXW（{tier}% 档，SmartByte {r['SmartByte型号']} {r['CNY未税']} CNY × {1 + tier / 100:.2f} ÷ {r['汇率']}，"
            f"汇率快照 {r['汇率日期']}，15 天有效，报价前核价）")


def infer_type(ent):
    txt = ' '.join(ent['interests'] + ent['remarks'] + ent['names'] + ent['froms'] + ent.get('positions', []))
    if ent.get('research', {}).get('type'):
        return ent['research']['type']
    for pat, t in TYPE_RULES:
        if re.search(pat, txt):
            return t
    return '经销/集成（类型待核）'


def infer_tier(ent, typ):
    if '品牌' in typ or 'OEM' in typ:
        return 30
    if '分销' in typ or '经销' in typ or '电商' in typ:
        return 20
    return 25


def infer_p1(ent):
    txt = ' '.join(ent['interests'] + ent['remarks'])
    for pat, model, why in P1_RULES:
        if re.search(pat, txt):
            return model, why
    return 'STC-424DGGPM-280W', '无明确兴趣记录：按 Saga 走量款起手'


def brands_seen(ent):
    txt = ' '.join(ent['interests'] + ent['remarks'])
    out = []
    for b in BRANDS:
        if b in txt and b not in out:
            out.append(b)
    # 去同义
    norm = []
    seen = set()
    for b in out:
        k = b.lower().replace('-', '').replace(' ', '')
        k = {'upeto': 'utepo', 'elink': 'elink', 'redlion': 'redlion', 'hrui': '洪瑞', 'dptek': 'dptek', 'smartbyte': 'smartbyte', 'mikrotik': 'mikrotik',
             'oring': 'oring', 'comnet': 'comnet', 'weidmüller': 'weidmuller', 'trendnet': 'trendnet', 'gxcom': 'gxcom', 'gnet': 'gnet', 'planet': 'planet'}.get(k, k)
        if k not in seen:
            seen.add(k)
            norm.append(b)
    return norm


def stars(grade):
    return {'A': '★★★', 'B': '★★', 'C': '—'}[grade]


def md_escape(s):
    return (s or '').replace('|', '\\|').replace('\n', '<br>')


def fmt_sources(ent):
    lines = ['| 文件#表:行 | No. | Company（原值） | Country | Person | From | Interested in | Contact | Remark | 跟进表 |', '|---|---|---|---|---|---|---|---|---|---|']
    for s in ent['sources']:
        lines.append('| ' + ' | '.join(md_escape(x) for x in [
            f"{s['file'].replace('Clients/', '')}#{s['sheet']}:{s['row']}", s['no'], s['company'], s['country'] or s.get('category', ''), s['person'],
            s['from'], s['interest'], ' '.join(x for x in [s['contact'], s['mobile'], s['website']] if x), ' '.join(x for x in [s['remark'], s['extra'], s['position']] if x),
            str(s['followups']) + ' 条' if s['followups'] else '—']) + ' |')
    return '\n'.join(lines)


def fmt_followups(ent, limit=400):
    fus = ent['followups']
    if not fus:
        return '（无跟进表记录）'
    lines = [f'合并自 {len({(f["file"], f["no"]) for f in fus})} 张跟进表，共 {len(fus)} 条（原值照录，日期已按年份递推补全）：', '',
             '| 日期 | 原始时间 | 我方推送内容 | 客户回复 | 平台 | 备注 | 来源表 |', '|---|---|---|---|---|---|---|']
    for f in fus[:limit]:
        lines.append('| ' + ' | '.join(md_escape(x) for x in [f['date_iso'] or '?', f['date'], f['content'], f['reply'], f['platform'], f['note'],
                                                            f"{os.path.basename(f['file'])}#{f['no']}"]) + ' |')
    if len(fus) > limit:
        lines.append(f'| … | | 其余 {len(fus) - limit} 条见 data/saga_clients/entities.json | | | | |')
    return '\n'.join(lines)


def fmt_contacts(ent):
    out = []
    bounce = ent['flags'].get('bounce')
    for e in ent['emails']:
        corp = e.split('@')[1] in {d for d in ent['domains']} or e in ent['corp_emails']
        st = '企业邮箱' if e in ent['corp_emails'] else '免费邮箱'
        if bounce:
            st += '；用户备注含「发不过去」——发送前核对是哪一个地址'
        out.append(f'- 邮箱：`{e}`〔{st}；来源：用户表原值〕')
    for ph in ent['phones']:
        wa = 'WhatsApp 已加' if ent['flags'].get('wa_added') or ent['wa_in_fu'] else ('WhatsApp 加不上' if ent['flags'].get('wa_failed') else '电话/WhatsApp 状态未记')
        out.append(f'- 电话：`+{ph}`〔{wa}；原值见来源表〕')
    for p in ent['persons']:
        out.append(f'- 联系人（原值）：{p}')
    for p in ent.get('positions', []):
        out.append(f'- 职位（原值）：{p}')
    for d in ent['domains']:
        out.append(f'- 网站/域名：{d}')
    for u in ent['platform_links'][:5]:
        out.append(f'- 平台链接：{u}')
    if not out:
        out.append('- （无任何联系方式：仅公司名/备注）')
    out.append('- **邮箱纪律**：只用表内原值，不猜测、不拼接；发不过去的地址标注后保留不删。')
    return '\n'.join(out)


def fmt_research(ent):
    rs = ent.get('research')
    if not rs:
        return ('- **状态：待调研**。分级目前基于用户表内信号 + 规则；A/B 候选将按批次做网页核实（公司是否仍在运营、业务类型、规模、在卖品牌），'
                '写入 `data/saga_clients/research/' + ent['code'] + '.json` 后由渲染器并入本节。')
    lines = [f"- **状态：已调研（{rs.get('researched_at', '')}）**　网站状态：{rs.get('website_status', '未记')}",
             f"- **是谁**：{rs.get('summary', '')}"]
    if rs.get('type'):
        lines.append(f"- **类型**：{rs['type']}")
    if rs.get('size'):
        lines.append(f"- **规模**：{rs['size']}")
    if rs.get('brands_seen'):
        lines.append(f"- **在卖/在用品牌**：{', '.join(rs['brands_seen'])}")
    for ev in rs.get('evidence', []):
        lines.append(f"- **【{ev.get('kind', '网页')}】{ev.get('claim', '')}**")
        if ev.get('quote'):
            lines.append(f"  > {ev['quote']}")
        lines.append(f"  > 来源：{ev.get('url', '')}（抓取 {ev.get('date', '')}）")
    for kp in rs.get('kp', []):
        lines.append(f"- **KP**：{kp.get('name', '')}（{kp.get('role', '')}）{kp.get('email', '')} {kp.get('phone', '')}〔{kp.get('source', '')}〕")
    if rs.get('grade_override'):
        lines.append(f"- **调研后定级**：{rs['grade_override']}（原自动 {ent['grade_auto']}）——{rs.get('override_reason', '')}")
    if rs.get('notes'):
        lines.append(f"- 备注：{rs['notes']}")
    lines.append(fmt_deep(ent))
    return '\n'.join(lines)


def fmt_snapshot(ent):
    """官网快照（自动摘要）块：来自 GitHub Actions 批量抓取 → snapshot_digest.py。缺失即不渲染。
    只呈现站内可见事实（标题/描述/语言/关键词词频/站内型号/公开邮箱电话/产品页/站内出现的品牌），不做人工判断。"""
    sg = SITE.get(ent['code'])
    if not sg:
        return ''
    L = ['', f"### 官网快照（自动摘要 · 抓取 {sg.get('fetched_at', '')[:10]} · 状态：{sg.get('status_cn', sg.get('status', ''))}）", '']
    if sg.get('status') != 'ok':
        L.append(f"- 尝试域名：{', '.join(sg.get('domains') or [])}")
        for e in (sg.get('errors') or [])[:3]:
            L.append(f'  > {e}')
        if sg.get('status') == 'mismatch':
            L.append('- **提示**：人工核对后判定表内域名不属于本客户（见上方说明），本客户以邮箱/电话为准；快照内容不采用。')
        elif sg.get('status') == 'parked_or_empty':
            L.append('- **提示**：域名停放/空站 → 公司可能已停业或换域名；跟进前先用邮箱/电话核实，勿只凭网站判死。')
        elif sg.get('status') == 'unreachable':
            L.append('- **提示**：域名不可达 → 表内域名可能拼错/过期；跟进前核对邮箱域名。')
        else:
            L.append('- **提示**：抓取失败不代表公司不在；人工打开一次即可。')
        L.append(f"- 数据文件：`data/saga_clients/site_snapshots/{ent['code']}.json`")
        return '\n'.join(L)
    L.append(f"- **首页**：{sg.get('final_url', '')}　语言：{sg.get('lang') or '未标'}　站点地图 URL 数：{sg.get('sitemap_count', 0)}")
    if sg.get('title'):
        L.append(f"- **标题**：{sg['title'].replace('|', '/')}")
    if sg.get('desc'):
        L.append(f"- **描述**：{sg['desc'].replace('|', '/')}")
    if sg.get('headings'):
        L.append(f"- **首页栏目**：{' / '.join(h.replace('|', '/') for h in sg['headings'])}")
    if sg.get('kw'):
        kw = sorted(sg['kw'].items(), key=lambda x: -x[1])[:12]
        L.append('- **关键词词频**（首页 + 产品子页，子串计数，仅作画像）：' + '、'.join(f'{k} {v}' for k, v in kw))
    if sg.get('brands'):
        L.append(f"- **站内出现的品牌**：{', '.join(sg['brands'])}　（「（！）」= Saga 自家/供应商品牌已在其站内出现）")
    if sg.get('models'):
        L.append(f"- **站内型号串**（正则抽取，含非交换机）：{', '.join(sg['models'])}")
    if sg.get('emails'):
        L.append(f"- **站内公开邮箱**：{', '.join(sg['emails'])}")
    if sg.get('phones'):
        L.append(f"- **站内公开电话**：{', '.join(sg['phones'])}")
    if sg.get('social'):
        L.append(f"- **社媒**：{', '.join(sg['social'])}")
    if sg.get('product_pages'):
        L.append('- **产品类页面**：' + '；'.join(sg['product_pages'][:6]))
    if sg.get('subpages'):
        L.append('- **已抓子页**：' + '；'.join(f"[{(x.get('title') or '').replace('|', '/')[:60]}]({x.get('url', '')})" for x in sg['subpages'][:6]))
    if sg.get('excerpt'):
        L.append(f"- 首页正文摘录：{sg['excerpt'].replace('|', '/')}")
    if sg.get('auto_p1'):
        L.append(f"- **自动对位建议**：{sg['auto_p1']}（{sg.get('auto_p1_why', '')}；仅在无人工对位时作为 P1）")
    L.append(f"- 数据文件：`data/saga_clients/site_snapshots/{ent['code']}.json`（原始摘要）；来源 GitHub Actions `saga-clients-snapshot` 抓取，仅公开页面。")
    return '\n'.join(L)


def fmt_deep(ent):
    """加厚挖掘块（T27）：公司事实 / 业务线 / 在卖型号→Saga 对位 / 触达通道 / 近况信号 / 风险。字段缺失即不渲染。"""
    rs = ent.get('research') or {}
    dp = rs.get('deep')
    if not dp:
        return ''
    L = ['', f"### 加厚挖掘（{dp.get('done_at', '')} · {dp.get('level', '深挖')}）", '']
    cf = rs.get('company_facts') or {}
    if cf:
        L.append('| 公司事实 | 内容 |')
        L.append('|---|---|')
        for k, lbl in [('legal_name', '法定名称'), ('founded', '成立'), ('hq', '总部/地址'), ('staff', '人数'), ('revenue', '营收'), ('registry', '注册/税号'), ('ownership', '股权/集团'), ('other', '其他')]:
            if cf.get(k):
                L.append(f'| {lbl} | {md_escape(str(cf[k]))} |')
        L.append('')
    if rs.get('business_lines'):
        L.append('- **业务线**：' + '；'.join(rs['business_lines']))
    ps = rs.get('products_seen') or []
    if ps:
        L.append('')
        L.append('| 在卖/在用（深挖所见） | 型号 | 规格要点 | Saga 对位 | 出处 |')
        L.append('|---|---|---|---|---|')
        for x in ps:
            L.append(f"| {md_escape(x.get('brand', ''))} | {md_escape(x.get('model', ''))} | {md_escape(x.get('spec', ''))} | {md_escape(x.get('saga', '') or '—')} | {x.get('url', '')}{'（' + x['date'] + '）' if x.get('date') else ''} |")
        L.append('')
    ch = rs.get('channels') or {}
    if ch:
        L.append('- **触达通道（公开）**：' + '；'.join(f'{k}: {v}' for k, v in ch.items() if v))
    if rs.get('signals'):
        L.append('- **近况信号**：')
        for x in rs['signals']:
            L.append(f'  - {x}')
    if rs.get('risks'):
        L.append('- **风险/边界**：' + '；'.join(rs['risks']))
    sf = rs.get('saga_fit') or {}
    if sf:
        L.append(f"- **Saga 对位结论**：P1 {sf.get('p1') or '待核型（无标准对应）'}（{sf.get('tier', '')}% 档）——{sf.get('why', '')}")
    if rs.get('email_hook'):
        L.append(f"- **邮件切入句（英文）**：{rs['email_hook']}")
    return '\n'.join(L)


def fmt_mail_review(ent):
    """针对性复盘（T29-U11）：基于 S/A 邮箱 + PI + Drive 的真实往来写的现状判断，每条事实带日期/方向/原话/消息 key。
    数据来自 research JSON 的 mail_review 块；缺失即不渲染。字段：as_of, situation, facts[{date,dir,who,quote,k,why}],
    breakpoint, need, saga_now{p1,tier,price,why,repeat[],gaps[]}, next_move{when,channel,action,one_question}, proof_gaps[], draft_en{subject,body}."""
    mr = (ent.get('research') or {}).get('mail_review')
    if not mr:
        return ''
    L = [f"> 依据：S/A 邮箱全量往来（`scripts/saga_clients/mail_dump.py {ent['code']}` 可复现）+ PI 包 + Drive 资料；复盘日期 {mr.get('as_of', '')}。**这一节优先于下文自动生成的 P1 / 第一问 / 邮件样板。**", '']
    bd = mr.get('binding') or {}
    if bd:
        # T29-U40 判读框架 J1–J7（docs/Saga内在逻辑与概念_2026-10-24.md §4）：一行固定格式，脚本可读
        L.append(f"- **绑定等级：{bd.get('level', '未绑定')}** ｜ 类型：{bd.get('type', '—')} ｜ 筛子：{bd.get('sieve', '—')} ｜ 停点：{bd.get('stop', '—')} ｜ 复活：{bd.get('revive', '—')} ｜ 通路：{bd.get('lane', '—')} ｜ 节奏：{bd.get('cadence', '—')} ｜ 证据：{bd.get('evidence', '—')}")
    if mr.get('situation'):
        L.append(f"- **现状一句话**：{mr['situation']}")
    if mr.get('need'):
        L.append(f"- **对方真实需求（有据）**：{mr['need']}")
    if mr.get('breakpoint'):
        L.append(f"- **断点 / 为什么停在这里**：{mr['breakpoint']}")
    sn = mr.get('saga_now') or {}
    if sn:
        L.append(f"- **Saga 现在该推什么**：P1 **{sn.get('p1', '—')}**（{sn.get('tier', '')}% 档，{sn.get('price', '价见价格主表')}）——{sn.get('why', '')}")
        if sn.get('repeat'):
            L.append('  - 复购/在买项：' + '；'.join(sn['repeat']))
        if sn.get('gaps'):
            L.append('  - 做不了 / 要先核的：' + '；'.join(sn['gaps']))
    nm = mr.get('next_move') or {}
    if nm:
        L.append(f"- **下一步（具体）**：{nm.get('when', '')}　{nm.get('channel', '')}　{nm.get('action', '')}")
        if nm.get('one_question'):
            L.append(f"  - 第一问（只问一个）：{nm['one_question']}")
    facts = mr.get('facts') or []
    if facts:
        L.append('')
        L.append('| 日期 | 向 | 谁 | 原话 / 事实（节录） | 为什么重要 | 消息 key |')
        L.append('|---|---|---|---|---|---|')
        for f in facts:
            L.append(f"| {f.get('date', '')} | {f.get('dir', '')} | {md_escape(f.get('who', ''))} | {md_escape(f.get('quote', ''))} | {md_escape(f.get('why', ''))} | `{f.get('k', '')}` |")
    if mr.get('proof_gaps'):
        L.append('')
        L.append('- **还缺的证据（等 A 邮箱 / Extra Info）**：' + '；'.join(mr['proof_gaps']))
    return '\n'.join(L)


def fmt_pi(ent):
    """成交记录（PI 包 · 自动汇总）：来自 data/pi_orders/单号对照.csv + 客户编号映射.json（build 阶段挂到 ent['pi']）。"""
    pi = ent.get('pi') or {}
    rows = sorted(PI_ORDERS.get(pi.get('folder', ''), []), key=lambda r: r['日期'] or '')
    L = []
    lab = pi.get('simon') or '—'
    L.append(f"- **Simon 的标签**（PI 包文件夹名）：**{lab}**" + (f"　|　收款：{pi['pay']}" if pi.get('pay') else '') + (f"　|　{pi['bind']}" if pi.get('bind') else '') + f"　|　买方抬头：{pi.get('buyer') or '—'}")
    if rows:
        usd = sum(float(r['销售合计'] or 0) for r in rows if r['币种'] == 'USD' and not r['取用单据'].startswith('Quotation'))
        rmb = sum(float(r['销售合计'] or 0) for r in rows if r['币种'] == 'RMB' and not r['取用单据'].startswith('Quotation'))
        prof = sum(float(r['利润RMB'] or 0) for r in rows if r['利润RMB'])
        first = min(r['日期'] for r in rows if r['日期']) if any(r['日期'] for r in rows) else '?'
        last = max(r['日期'] for r in rows if r['日期']) if any(r['日期'] for r in rows) else '?'
        L.append(f"- **单号** {len(rows)} 个（{first} → {last}）　|　**销售** USD {usd:,.0f}" + (f" + RMB {rmb:,.0f}（货代走账）" if rmb else '') + (f"　|　**Simon 成本表利润** RMB {prof:,.0f}" if prof else ''))
        L.append('')
        L.append('| 单号 | 日期 | 单据 | 型号 | 数量 | 金额 | 采购（卖方 / RMB） | Simon 成本表（成本 / 收款 / 利润 RMB） |')
        L.append('|---|---|---|---|---|---|---|---|')
        for r in rows:
            pur = (f"{r['采购卖方']} / {r['采购合计RMB']}" if r['采购合计RMB'] else '—')
            cs = (f"{r['Simon成本统计:成本RMB']} / {r['总收款RMB']} / {r['利润RMB']}" if r['利润RMB'] else '—')
            L.append(f"| {r['单号']} | {r['日期'] or '?'} | {r['取用单据'].split(' ')[0]} | {(r['型号'] or '—')[:60]} | {r['销售数量'] or '?'} | {r['币种']} {r['销售合计']} | {pur} | {cs} |")
        L.append('')
        L.append('> 口径：同一单号多份文件取 CI > PI（最新修订）> Quotation；Quotation 行不计入销售合计；明细见 `data/pi_orders/销售单据明细.csv`、采购价见 `采购合同明细.csv`；原件在 Release `files-pi_2026-10`。')
    else:
        L.append('- （PI 包里有此客户文件夹，但未解析出带单号的单据，见 `data/pi_orders/_parse_report.md`）')
    return '\n'.join(L)


def fmt_gmail(ent):
    """S 邮箱往来（自动汇总，来自 data/saga_clients/gmail_digest.json）；只对 A/B 档案输出。"""
    g = GMAIL.get(ent['code'])
    if not g:
        return ''
    L = []
    L.append(f"- **账号**：{g['account']}　|　**邮件**：{g['messages']} 封（去 {g['out']} / 来 {g['in']}）　|　**期间**：{g['first']} → {g['last']}　|　**最后去信**：{g['last_out'] or '—'}")
    if g.get('emails'):
        L.append('- **对方邮箱**：' + '、'.join(g['emails'][:6]))
    li = g.get('last_in')
    if li:
        L.append(f"- **最后一封来信**：{li['date']} {li['from']}「{md_escape(li['subject'])}」：{md_escape(li['snippet'])}")
        if g.get('pending_reply'):
            L.append('- ⚠️ **对方来信在我们最后一封之后（同一线程我方发过）——待回**')
    elif g['in'] == 0:
        L.append('- 对方从未回信（全部为我方去信）')
    if g.get('quotes'):
        L.append('- **邮件里报过的价**：' + '；'.join(f"{q['date']} ${q['usd']}{('（' + q['model'] + '）') if q['model'] else ''}" for q in g['quotes'][:8]))
    if g.get('threads'):
        L.append('')
        L.append('| 线程主题 | 首封 | 末封 | 来 | 去 | 附件 |')
        L.append('|---|---|---|---|---|---|')
        for t in g['threads'][:12]:
            L.append(f"| {md_escape(t['subject'])} | {t['first']} | {t['last']} | {t['in']} | {t['out']} | {t['atts']} |")
        if len(g['threads']) > 12:
            L.append(f"| …共 {len(g['threads'])} 条线程（全文见 `data/gmail_s/threads.json` / `messages/`） | | | | | |")
    if g.get('attachments'):
        L.append('')
        L.append('- **往来附件**：' + '、'.join(md_escape(a) for a in g['attachments'][:10]))
    return '\n'.join(L)


def followup_plan(ent, grade, p1, tier):
    if grade == 'C':
        return ('> C 级不主动跟进。保留档案的意义：① 不重复开发；② 若对方主动来询再升级。\n'
                f'> 不跟进理由：{ent["c_sub"] or "综合分低"}。若用户不同意，在 `data/saga_clients/人工定级.csv` 写一行 `{ent["code"]},B,理由` 后重跑即可。')
    model = p1 or 'STC-424DGGPM-280W'
    deal = ent['flags'].get('deal') or ent['deal_in_fu']
    if deal:
        step1 = f'**第 1 次**：老客户回访——问上次所购型号的使用情况 + 告知 Marvell 新款（{model}）；只问一个问题：当前在采购的主力型号与月量。'
    elif ent['reply_sub']:
        step1 = f'**第 1 次**：接着上次对方的问题（见跟进记录最后一条客户回复）直接给答案 + {model} 一条规格链接；只问一个问题。'
    else:
        step1 = f'**第 1 次**：换角度首触（不要再发产品图）：一句话说清 Saga 是 Marvell 方案 OEM/ODM 货源，附 {model} 一条规格链接；只问一个问题。'
    if grade == 'A':
        cadence = '节奏：A 级 2–3 周一次，按对方时区工作日发；WhatsApp 已加的优先 WhatsApp 短消息，邮件做正式报价。'
    else:
        cadence = '节奏：B 级 4–6 周一次（慢慢跟）；只发有信息量的内容（新品/价格窗口/案例），不发纯问候。'
    return '\n'.join([
        f'> 每次只推进一个台阶、只问一个问题；全程只推 P1（{model}），备选型不进首触。',
        '',
        f'- {step1}',
        f'- **第 2 次**：样机/并行测试邀约（1 台，30 天）；说明 CE/RoHS/FCC/REACH/UKCA，明说无 UL、无 bt（商用线）、无云管理。',
        f'- **第 3 次**：贴牌/定制与批量：MOQ、交期（10–15 天）、付款（T/T 或 PayPal，50/50；定制 100% 预付）；{tier}% 档报价。',
        f'- {cadence}',
        '- **停止条件**：3 次定向触达无任何实质回复 → 降 B/C；对方书面拒绝 → C 并记原因。',
    ])



P1_EN = {
    # (英文描述, 芯片字样)——芯片字样只给网管 L2/L2+/L3 的 Marvell 线（规则 ㉛）；非网管/HRUI Realtek 线留空；CENTEC 只在 STH
    # 商用 Marvell 线（SmartByte 价格主表）
    'STC-28DGGPM': ('8-port Gigabit PoE+ L2+ managed switch with 2 SFP uplinks', 'Marvell-based'),
    'STC-424DGGPM-280W': ('24-port Gigabit PoE+ L2+ managed switch (280 W PoE budget, 4 uplinks)', 'Marvell-based'),
    'STC-424XGGPM-280W': ('24-port Gigabit PoE+ L2+ managed switch with 4x10G SFP+ uplinks', 'Marvell-based'),
    'STC-448DGGPM': ('48-port Gigabit PoE+ L2+ managed switch', 'Marvell-based'),
    'STC-448XGGPM': ('48-port Gigabit PoE+ L2+ managed switch with 4x10G SFP+ uplinks (440 W)', 'Marvell-based'),
    'STC-424XGGM': ('24-port Gigabit L2+ managed switch with 4x10G SFP+ uplinks', 'Marvell-based'),
    'STC-448XGGM': ('48-port Gigabit L2+ managed switch with 4x10G SFP+ uplinks', 'Marvell-based'),
    'STC-424XGGM(L3)': ('24-port Gigabit L3 switch with 4x10G SFP+ uplinks', 'Marvell-based'),
    'STC-448XGGM(L3)': ('48-port Gigabit L3 switch with 10G uplinks', 'Marvell-based'),  # 主表 L3 档 = Marvell 线（CENTEC 只在 STH）
    'STC-448XGGMO': ('48-port SFP L3 fibre switch with 4x10G SFP+ uplinks', 'Marvell-based'),
    'STC-4168XGGCM': ('16-SFP + 8-combo L3 fibre switch with 4x10G SFP+ uplinks', 'Marvell-based'),
    # 工业 Marvell 网管线
    'STI-240GM': ('industrial DIN-rail L2 managed switch, 4x Gigabit plus 2 SFP', 'Marvell-based'),
    'STI-244GPM': ('industrial DIN-rail L2 managed switch, 4x Gigabit PoE+ plus 2 SFP (120 W)', 'Marvell-based'),
    'STI-280GM': ('industrial DIN-rail L2 managed switch, 8x Gigabit plus 2 SFP', 'Marvell-based'),
    'STI-288GPM': ('industrial DIN-rail L2 managed switch, 8x Gigabit PoE+ plus 2 SFP (240 W)', 'Marvell-based'),
    'STI-280DGGM': ('industrial DIN-rail L2+ managed switch, 8x Gigabit plus 2x 2.5G SFP', 'Marvell-based'),
    'STI-288DGGPM': ('industrial DIN-rail L2+ managed switch, 8x Gigabit PoE+ plus 2x 2.5G SFP', 'Marvell-based'),
    'STI-288DGGPM-2BT': ('industrial DIN-rail L2+ managed switch, 8x Gigabit PoE+ (2x 90 W bt) plus 2x 2.5G SFP', 'Marvell-based'),
    'STI-488DGGPM': ('industrial DIN-rail L2+ managed switch, 8x Gigabit PoE+ plus 4x 2.5G SFP', 'Marvell-based'),
    'STI-488XGGPM': ('industrial DIN-rail L2+ managed switch, 8x Gigabit PoE+ plus 4x10G SFP+', 'Marvell-based'),
    'STI-488DGGGM': ('industrial L2+ managed switch, 8x Gigabit plus 8 SFP plus 4x 2.5G SFP uplinks', 'Marvell-based'),
    'STI-448DGGGM': ('industrial L2+ managed switch, 8x Gigabit plus 4 SFP plus 4x 2.5G SFP', 'Marvell-based'),
    'STI-448DGGGPM': ('industrial L2+ managed switch, 8x Gigabit PoE+ plus 4 SFP plus 4x 2.5G SFP', 'Marvell-based'),
    'STI-448XGGGPM(L3)': ('industrial L3 managed switch, 8x Gigabit PoE+ plus 4 SFP plus 4x10G SFP+', 'Marvell-based'),
    'STI-21616XGGPM': ('industrial L2+ managed switch, 16x Gigabit PoE+ plus 2x10G SFP+', 'Marvell-based'),
    'STI-41616XGGPM': ('industrial L3 managed switch, 16x Gigabit PoE+ plus 4x10G SFP+', 'Marvell-based'),
    'STI-41616XGGPM-4BT': ('industrial L3 managed switch, 16x Gigabit PoE+ (4x 90 W bt) plus 4x10G SFP+', 'Marvell-based'),
    'STI-42424XGGPM-4BT': ('industrial L2+ managed switch, 24x Gigabit PoE+ (4x 90 W bt) plus 4x10G SFP+', 'Marvell-based'),
    'STI-4168DGGCM-U': ('industrial L2+ managed fibre switch, 16 SFP plus 8 combo plus 4x 2.5G SFP', 'Marvell-based'),
    # 工业非网管线（SmartByte 非网管表；不写芯片）
    'STI-110GE': ('industrial mini Gigabit media converter (1 fiber + 1 copper)', ''),
    'STI-110FE': ('industrial mini Fast Ethernet media converter (1 fiber + 1 copper)', ''),
    'STI-111GP': ('industrial mini Gigabit PoE media converter (1 SFP + 1 PoE copper)', ''),
    'STI-220GE': ('industrial compact switch, 2x Gigabit plus 2 SFP (unmanaged)', ''),
    'STI-050GE': ('industrial DIN-rail 5-port Gigabit switch (unmanaged)', ''),
    'STI-080GE': ('industrial DIN-rail 8-port Gigabit switch (unmanaged)', ''),
    'STI-240GE': ('compact industrial DIN-rail switch, 4x Gigabit plus 2 SFP (unmanaged)', ''),
    'STI-280GE': ('industrial DIN-rail switch, 8x Gigabit plus 2 SFP (unmanaged)', ''),
    'STI-054FP': ('industrial DIN-rail switch, 4x Fast Ethernet PoE plus 1 uplink (unmanaged)', ''),
    'STI-054GP': ('industrial DIN-rail switch, 4x Gigabit PoE+ plus 1 Gigabit uplink (unmanaged)', ''),
    'STI-144GP': ('compact industrial switch, 4x Gigabit PoE+ plus 1 SFP (unmanaged)', ''),
    'STI-154GP': ('industrial DIN-rail switch, 4x Gigabit PoE+ plus 1 SFP and 1 copper uplink (unmanaged)', ''),
    'STI-244GP': ('industrial DIN-rail switch, 4x Gigabit PoE+ plus 2 SFP (unmanaged)', ''),
    'STI-288GP': ('industrial DIN-rail switch, 8x Gigabit PoE+ plus 2 SFP (unmanaged)', ''),
    'STI-488GP': ('industrial DIN-rail switch, 8x Gigabit PoE+ plus 4 SFP (unmanaged)', ''),
    'STI-21616GP': ('16-port Gigabit PoE+ industrial switch with 2 SFP uplinks (unmanaged)', ''),
    # LT-IS6312GP-4GX8GT-FBP（光纤 Bypass）：Saga 无自有型号，不进样板（供应商型号不外露）→ 走「核型中」样板
    # 商用 Realtek 线（HRUI 对照表；Saga 对外列表价）
    'STC-08GE': ('8-port Gigabit desktop switch (unmanaged)', ''),
    'STC-024FP': ('4-port Fast Ethernet PoE switch with 2 uplinks (unmanaged)', ''),
    'STC-028GFP': ('8-port Fast Ethernet PoE switch with 2 Gigabit uplinks (unmanaged)', ''),
    'STC-024GP': ('4-port Gigabit PoE switch with 2 Gigabit uplinks (unmanaged)', ''),
    'STC-028GP': ('8-port Gigabit PoE switch with 2 Gigabit uplinks (unmanaged, 120 W)', ''),
    'STC-114GP': ('4-port Gigabit PoE switch with 1 SFP and 1 copper uplink (unmanaged)', ''),
    'STC-204GP': ('4-port Gigabit PoE switch with 2 SFP uplinks (unmanaged)', ''),
    'STC-228GP': ('8-port Gigabit PoE switch with 2 SFP and 2 copper uplinks (unmanaged, 120 W, PoE watchdog)', ''),
    'STC-2016GP': ('16-port Gigabit PoE switch with 2 SFP uplinks (unmanaged, 300 W)', ''),
    'STC-2024GP': ('24-port Gigabit PoE switch with 2 SFP uplinks (unmanaged, 300 W)', ''),
    'STC-114XGDGP': ('4-port 2.5G PoE switch with 1x10G SFP+ and 1x 2.5G uplink (unmanaged)', ''),
    'STC-28GM': ('8-port Gigabit L2 managed switch with 2 SFP uplinks (commercial line)', ''),
    'STC-28GPM': ('8-port Gigabit PoE+ L2 managed switch with 2 SFP uplinks (commercial line, 120 W)', ''),
    'STC-2216GPM': ('16-port Gigabit PoE+ L2 managed switch with 2 SFP and 2 copper uplinks (commercial line)', ''),
    # 数据中心 CENTEC 线
    'STH-2C24XF-SFI': ('24x10G SFP+ plus 2x100G QSFP28 data-centre switch', 'CENTEC-based'),
}
SWITCH_BRANDS = {'ONV', 'Utepo', 'Upeto', 'Ewind', 'HRUI', 'E-link', 'Elink', 'E-Link', 'BDCOM', 'PLANET', 'Planet', 'planet', 'Cisco', 'Redlion', 'redlion',
                 'Red Lion', 'Moxa', 'MOXA', 'Antaira', 'TP-Link', 'Mikrotik', 'MikroTik', 'Ubiquiti', 'Netgear', 'Trendnet', 'TRENDnet', '迈威', 'Maiwe',
                 'Oring', 'ORing', 'Korenix', 'Westermo', 'Hirschmann', 'Phoenix', 'Advantech', 'Lantech', 'Comnet', 'ComNet', 'Perle', 'Transition',
                 'Allied Telesis', 'D-Link', 'Zyxel', 'Tenda', 'Ruijie', 'H3C', 'Huawei', 'Aruba', 'HPE', 'Dell', 'Juniper', 'Extreme', 'Cambium',
                 'EtherWAN', 'Black Box', 'StarTech', 'FS.com', 'Kyland', 'Ruggedcom', 'Scalance', 'Siemens', 'Weidmuller', 'Weidmüller', 'Belden',
                 'CTCU', 'N-net', 'UniPoE', '优力普', 'G-net', 'Gnet', 'Hioso', 'Raisecom', 'Dptek', 'DPTEK', 'Witek', 'GXCOM', 'Gxcom', '丰润达', '磊通', '洪瑞', '中科德能'}
_BRANDS_LOW = {b.lower() for b in BRANDS} | {'maiwe', 'bdcom', 'utepo', 'onv', 'planet', 'cisco', 'moxa', 'hikvision', 'dahua', 'tplink', 'tp-link', 'ubiquiti', 'mikrotik', 'netgear', 'trendnet', 'dlink', 'd-link', 'zyxel', 'huawei', 'h3c', 'ruijie'}
_LATIN_NAME = re.compile(r"^[A-Za-zÀ-ÿĀ-žİıŞşĞğÇçÖöÜü'.\-]{2,}$")


def kp_rows(ent):
    """关键人表：调研 KP（具名）+ 用户表原值联系人/邮箱/电话；每行带状态与来源。"""
    rows = []
    rs = ent.get('research') or {}
    for kp in rs.get('kp', []):
        nm = (kp.get('name') or '').strip()
        if not nm or nm.startswith('（'):
            continue
        rows.append((nm, kp.get('role') or '—', ' / '.join(x for x in [kp.get('email'), kp.get('phone')] if x) or '—', '调研核实（公开页）', kp.get('source') or '调研'))
    wa = 'WhatsApp 已加' if ent['flags'].get('wa_added') or ent['wa_in_fu'] else ''
    seen = {re.sub(r'[^a-z]', '', r[0].lower())[:12] for r in rows}
    for p in ent['persons'][:8]:
        nm = re.sub(r'[\u4e00-\u9fff].*$', '', re.split(r'[/|]', p)[0]).strip(' -–:：')
        if not nm or not re.search(r'[A-Za-zÀ-ÿĀ-ž]', nm):
            continue  # 纯中文备注（如「自建站是后边网站」）不是人名
        key = re.sub(r'[^a-z]', '', nm.lower())[:12]
        if key and key in seen:
            continue
        seen.add(key)
        rows.append((nm, (ent.get('positions') or ['—'])[0], ' / '.join(ent['emails'][:2] + [f'+{x}' for x in ent['phones'][:1]]) or '—', '用户表原值' + ('·' + wa if wa else ''), 'Clients/ 表'))
        if len(rows) >= 5:
            break
    if not rows:
        ch = ' / '.join(ent['emails'][:2] + [f'+{x}' for x in ent['phones'][:2]]) or '—'
        rows.append(('—（未具名）', '公司级', ch, '用户表原值' + ('·' + wa if wa else ''), 'Clients/ 表'))
    return rows


def channel_advice(ent, g):
    wa = ent['flags'].get('wa_added') or ent['wa_in_fu']
    deaf = ent['fu_count'] >= 8 and not ent['reply_sub']
    corp = bool(ent['corp_emails'])
    out = []
    if wa:
        out.append('首选 WhatsApp 短消息（已加），邮件只做正式报价')
    elif ent['phones']:
        out.append('有电话但 WhatsApp 状态未记：先试加 WhatsApp，再邮件')
    if deaf:
        out.append(f'邮件已推送 {ent["fu_count"]} 次无回复 → 换通道（电话 / LinkedIn / 官网表单），不要再发同模板')
    elif corp:
        out.append('企业邮箱可直发')
    elif ent['emails']:
        out.append('仅免费邮箱：可发，但优先找官网公开的企业邮箱（见调研 KP）')
    else:
        out.append('无邮箱：只能电话 / WhatsApp / 官网表单')
    if ent['flags'].get('bounce'):
        out.append('备注含「发不过去」：发送前核对是哪一个地址，退信地址保留不删')
    return '；'.join(out)


def swot(ent, g, typ, p1, tier, brands):
    rs = ent.get('research') or {}
    deal = ent['flags'].get('deal') or ent['deal_in_fu']
    S, W, O, T = [], [], [], []
    if deal:
        S.append('有成交史，信任与开户成本已付')
    if ent['reply_sub']:
        S.append(f'有 {ent["reply_sub"]} 次实质回复（对方认识我们）')
    if ent['flags'].get('wa_added') or ent['wa_in_fu']:
        S.append('WhatsApp 直达')
    if '品牌' in typ or 'OEM' in typ:
        S.append('自有品牌/贴牌需求 = 现成 OEM 客户')
    if ent['region'] in ('北美', '欧洲', '土耳其'):
        S.append(f'{ent["region"]}主攻区，复购与口碑可外溢')
    if 'ISAF2025展会' in ent['tags']:
        S.append('ISAF 2025 面对面建立过联系')
    if not S:
        S.append('名单内已有联系记录，不是零起点')
    if not ent['persons'] and not any(not (k.get('name') or '').startswith('（') for k in rs.get('kp', [])):
        W.append('无具名决策人，仍是公司级触达')
    if ent['fu_count'] >= 8 and not ent['reply_sub']:
        W.append(f'已推送 {ent["fu_count"]} 次无回复，邮件通道疲劳')
    if ent['region'] in ('南亚', '非洲', '拉美', '中东', '俄语区'):
        W.append(f'{ent["region"]}：物流/收款/汇率摩擦高于主攻区')
    if not ent['corp_emails'] and not ent['phones']:
        W.append('没有可靠直达通道')
    if not W:
        W.append('Saga 无 UL / bt（商用线）/ 云管理，若对方招标要求这些即出局')
    O.append(f'P1 {p1 or "—"} 按 {tier}% 档报价，做现供应商的第二货源')
    if '品牌' in typ or 'OEM' in typ:
        O.append('贴牌 + 定制 UI/型号 → 30% 档与长期绑定')
    sb = [b for b in brands if b in SWITCH_BRANDS]
    if sb:
        O.append(f'对位其在用/在卖的 {", ".join(sb[:3])}：涨价、断货或交期拉长时切入')
    if rs.get('size'):
        O.append(f'规模（调研）：{rs["size"]}')
    T.append('深圳同行（ONV / Utepo / 迈威等）价格战')
    if sb:
        T.append('现有品牌分销协议可能限制同品类采购')
    T.append('汇率与海运波动吃掉 20–30% 的价差')
    return '\n'.join([f'- **S**：{"；".join(S)}', f'- **W**：{"；".join(W)}', f'- **O**：{"；".join(O)}', f'- **T**：{"；".join(T)}'])


def qualification(ent, g, brands):
    rs = ent.get('research') or {}
    txt = ' '.join(ent['interests'] + ent['remarks'])
    need = '✅' if re.search(r'PoE|POE|poe|switch|Switch|交换机|工业|industrial|MC|收发器|FS', txt) else '❓ 表内兴趣不含交换机关键词'
    named = bool(ent['persons']) or any(not (k.get('name') or '').startswith('（') for k in rs.get('kp', []))
    kp = '✅' if named else '❌ 未识别（公司级）'
    if ent['corp_emails']:
        ch = '✅ 企业邮箱'
    elif ent['flags'].get('wa_added') or ent['wa_in_fu']:
        ch = '✅ WhatsApp 已加'
    elif ent['emails']:
        ch = '⚠️ 仅免费邮箱'
    elif ent['phones']:
        ch = '⚠️ 仅电话'
    else:
        ch = '❌ 无'
    br = ('✅ ' + ', '.join(brands[:4])) if brands else '❓ 未知'
    deal = ent['flags'].get('deal') or ent['deal_in_fu']
    vol = '✅ 有成交史（量待确认）' if deal else ('❓ 未确认（有回复但未报量）' if ent['reply_sub'] else '❓ 未确认')
    if g == 'A':
        concl = '**技术上合格 / 商业上有互动证据（成交或实质回复或面谈）→ 值得长期跟进**'
    elif g == 'B':
        concl = '**技术上合格 / 商业上未合格（待实质回复）→ 慢慢跟**'
    else:
        concl = '**不合格（见 C 级细分）→ 不主动跟进**'
    return '\n'.join(['| 门槛 | 状态 |', '|---|---|', f'| 需求面成立（在卖/在用交换机或 PoE） | {need} |', f'| 决策人识别 | {kp} |',
                      f'| 触达通道 | {ch} |', f'| 现用/在卖交换品牌 | {br} |', f'| 采购量/预算 | {vol} |', f'| 商业资格结论 | {concl} |'])


def greeting_name(ent):
    rs = ent.get('research') or {}
    cands = []
    for kp in rs.get('kp', []):
        nm = (kp.get('name') or '').strip()
        if nm and not nm.startswith('（'):
            cands.append(nm)
    cands += ent['persons']
    titles = {'sales', 'info', 'mr', 'mrs', 'ms', 'miss', 'dr', 'eng', 'ing', 'attn', 'sr', 'sra', 'herr', 'frau', 'mme', 'sig', 'bay', 'bayan', 'team', 'dear'}
    garbage = {'array', 'none', 'null', 'n/a', 'test', 'unknown', 'contact', 'purchase', 'purchasing', 'manager', 'director', 'owner', 'ceo', 'md'}
    company_first = re.sub(r'[^a-z]', '', (ent['name'].split() or [''])[0].lower())
    for nm in cands:
        for tok in re.split(r'[\s/|,;（(]+', nm.strip())[:3]:
            if not tok or not _LATIN_NAME.match(tok):
                break
            low = tok.lower().strip('.')
            if low in titles:
                continue
            if len(low) <= 2 or low in garbage or re.sub(r'[^a-z]', '', low) == company_first or low in _BRANDS_LOW:
                break  # 首字母缩写 / 垃圾值 / 公司名当人名 → 退回 Hello,
            return tok[0].upper() + tok[1:].rstrip('.')
    return ''


# 第 74 批(q) 2026-10-25：自动样板对 Elsa 箱触达史的感知（规则 ㉝ 开头句、㉟ 已见价）
ELSA_SEEN = {  # 群发主题 → (型号, 稿内价)
    '24 Port PoE Managed Switch': ('STC-424XGGPM-280W', 170),
    '48 Port PoE Managed Switch': ('STC-448XGGPM', 300),
    '10G Enterprise SFP Switch': ('STC-4168XGGCM', 280),
    '24 Port Fiber Switch': ('STC-4168XGGCM', 240),
}
ELSA_LIVE = {'STC-424XGGPM-280W': 180, 'STC-448XGGPM': 335, 'STC-4168XGGCM': 300}  # 同款见过群发价的户：4168 群发 $280（2025-09→2026-05，≈进价）已停，按 FX 7.2→6.7 写 $300（SB-865 口径）
ELSA_LIVE_NOW = {'STC-424XGGPM-280W': 180, 'STC-448XGGPM': 335}  # 仍在发 / 现行对外价：没见过群发的户也不高于它（㉕ ②）


def elsa_touch(ent):
    """从 research.mail_review.facts 取 Elsa 箱去信：(轮数, 最近日期, 最近主题, {型号: (已见价, 日期)}) 或 None。"""
    mr = ((ent.get('research') or {}).get('mail_review') or {})
    facts = [f for f in (mr.get('facts') or []) if isinstance(f, dict) and str(f.get('k') or '').startswith('elsa') and f.get('date')]
    if not facts:
        return None
    facts.sort(key=lambda f: f['date'])
    last = facts[-1]
    subj = re.split(r'（| — |：', str(last.get('quote') or ''))[0].strip() or 'our product mail'
    seen = {}
    for f in facts:
        q = str(f.get('quote') or '')
        for sub, (model, pr) in ELSA_SEEN.items():
            if q.startswith(sub):
                seen[model] = (pr, f['date'])
    return (len(facts), last['date'], subj, seen)



_FOREIGN_GREET = re.compile(r"^(?:(?:Hola|Bonjour|Buongiorno|Merhaba|Dzień dobry|Здравствуйте|Olá|Hallo|Guten Tag|Ciao|Hej|Hei|Sayın|Herr|Frau|Anh|Chị|Đinh)(?:\s+[A-ZÀ-Ý][\w'’.-]+){0,2}|Chào anh/chị [^,—–-]+|[A-ZÀ-Ý][\w'’.-]+(?: Bey| Hanım)?)\s*[,，—–:-]+\s*")
_ENG_WORDS = {'the', 'for', 'we', 'your', 'you', 'and', 'with', 'our', 'which', 'can', 'supply', 'switches', 'switch', 'next', 'beside',
              'alongside', 'under', 'from', 'that', 'this', 'would', 'not', 'but', 'price', 'unit', 'units', 'have', 'there', 'what', 'how', 'is', 'are',
              'any', 'where', 'still', 'could', 'should', 'need', 'it', 'same', 'also', 'only', 'worth', 'fit', 'fits', 'list', 'listing', 'range', 'sell',
              'site', 'sites', 'first', 'before', 'after', 'when', 'again', 'more', 'than', 'asked', 'about', 'into', 'class', 'quarter', 'airflow', 'to', 'relevant'}


def hook_lang(hk):
    """研究档 email_hook 语言判定：返回 (english_hook, native_hook)。
    英文钩子句（可能带外语称呼「Hola —」「Herr X,」「X Bey,」）→ 去称呼后返回英文；
    土/俄/法/西/德/意等客户语言整句 → 不混进英文样板，整段原样返回 native 供单发。"""
    hk = (hk or '').strip()
    if not hk:
        return '', ''
    t = _FOREIGN_GREET.sub('', hk, count=1).strip()
    words = re.findall(r"[^\W\d_]+", t.lower())
    eng = sum(1 for w in words if w in _ENG_WORDS)
    if re.search(r'[Ѐ-ӿ]', t) or eng < 3:
        return '', hk
    if t and t[0].islower():
        t = t[0].upper() + t[1:]
    return t, ''


def _dfmt(iso):
    """2026-09-04 → 4 September 2026（英文信里的日期写法）"""
    try:
        d = dt.date.fromisoformat(str(iso)[:10])
        return f'{d.day} {d.strftime("%B")} {d.year}'
    except Exception:
        return str(iso)

def email_draft(ent, g, typ, p1, tier, brands, first_q):
    if g == 'C':
        return '> C 级不出邮件样板（不主动跟进）。'
    hook_raw = ((ent.get('research') or {}).get('email_hook') or '').strip()
    if re.search(r'[\u4e00-\u9fff]', hook_raw) and re.search(r'不主动发送|不发送|不发：|不跟|不触达|守界：不', hook_raw[:40]):
        return f'> 研究档 email_hook 标注「{hook_raw}」：不出邮件样板（对方来询再按「产品决策」P1 手写）。'
    if not p1 or p1 not in P1_EN:
        hook = hook_raw
        if re.search(r'[\u4e00-\u9fff]', hook):
            m_en = re.search(r'[：:]\s*([A-Z][^）]{30,})', hook)
            hook = m_en.group(1).strip() if m_en else ''
        native0 = ''
        if hook:
            hook, native0 = hook_lang(hook)
        if native0:
            return (f'> 研究档 email_hook 为客户语言一句话（不混进英文样板；要用就整段单发 WhatsApp/邮件，或按「产品决策」P1 手写英文稿）：\n>\n> {native0}')
        if hook:
            name = greeting_name(ent)
            hi = f'Hi {name},' if name else 'Hello,'
            if name:
                hook = re.sub(r'^' + re.escape(name) + r'(?: Bey| Hanım)?,\s*', '', hook)
                if hook and hook[0].islower():
                    hook = hook[0].upper() + hook[1:]
            et0 = elsa_touch(ent)
            _f0 = (((ent.get('research') or {}).get('mail_review') or {}).get('facts') or [])
            if ent['reply_sub'] or ent['flags'].get('deal') or ent['deal_in_fu'] or any(isinstance(x, dict) and x.get('dir') == '来' for x in _f0):
                op0 = 'Picking up our earlier exchange about PoE / industrial switches.'
            elif et0:
                op0 = (f'{"Over the past months" if et0[1] >= "2026-04-01" else "Some time ago"} you had '
                       f'{"a few product mails" if et0[0] >= 2 else "a product mail"} from us - {"most recently " if et0[0] >= 2 else ""}"{et0[2]}" on {_dfmt(et0[1])} - '
                       f'and there was no reason to answer a mass mail. This one is specific.')
            else:
                op0 = 'We have been in touch before about PoE and industrial switches; this is a specific follow-up rather than a catalogue.'
            q0 = '' if '?' in hook else 'One question: is the port mix fixed by the design, or can we propose an equivalent layout?\n\n'
            body = (f"{hi}\n\n{op0} {hook}\n\n{q0}"
                    "Best regards,\nSaga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)\nhttps://sagatele.com/")
            note0 = ('> 该需求无 Saga 标准型号对应（见「产品决策」P1 待核型）：此样板只确认需求与核型进度，不报价；核型后再出带型号/价格的版本。' if not p1
                     else f'> P1 = {p1}：型号不在样板描述表（render.py P1_EN）内，样板未带型号/价格——报价前按价格表核 {p1}。')
            if re.search(r'[\u4e00-\u9fff]', hook_raw):
                note0 = f'> 研究档备注（未并入正文）：{hook_raw}\n\n' + note0
            return ('**主题**：Follow-up on your switch requirement (model confirmation in progress)\n\n```text\n' + body + '\n```\n\n' + note0)
        if hook_raw:
            return f'> 研究档 email_hook 为备注「{hook_raw}」，无英文钩子句：不出自动样板。'
        return '> 该客户的需求（VC/光端机、SFP/DWDM 等）不在 Saga 三家供应商产品线内：不出邮件样板；若要只推交换机，用 STC-28DGGPM 版本手改。'
    desc, chip = P1_EN[p1]
    r = PRICES.get(p1)
    col = {20: 'USD@+20%', 25: 'USD@+25%', 30: 'USD@+30%'}[tier]
    if r:
        _v, _capped = tier_price(r, tier)
        price = f"${_v} USD EXW (price snapshot {r['汇率日期']}, valid 15 days)"
    elif hrui_price(p1, tier):
        price = f"${hrui_price(p1, tier)[0]} USD EXW (valid 15 days)"
    elif ALT_PRICES.get(p1):
        price = f"${ALT_PRICES[p1][0]} USD EXW (valid 15 days)"
    else:
        price = 'price on request'
    # 规则 ㉕：档案 saga_now.price 里已定的锚价（own quote → 群发现价 → 最近实报 → 档位）优先于档位公式
    _snp = (((ent.get('research') or {}).get('mail_review') or {}).get('saga_now') or {})
    _snp = _snp.get('price') if isinstance(_snp, dict) else None
    if isinstance(_snp, str):
        _m = re.search(r'锚价[：:]?\s*' + re.escape(p1) + r'\s*\$\s*([0-9][0-9,]*(?:\.[0-9]+)?)', _snp)
        if _m:
            price = f"${_m.group(1)} USD EXW (valid 15 days)"
    deal = ent['flags'].get('deal') or ent['deal_in_fu']
    name = greeting_name(ent)
    hi = f'Hi {name},' if name else 'Hello,'
    if 'ISAF2025展会' in ent['tags']:
        opener = 'We met at ISAF 2025 in Istanbul last October - this picks up what we discussed at the booth, with one concrete option.'
    elif deal:
        opener = 'Thank you again for your earlier order with us - this is a short update rather than a cold mail.'
    elif ent['reply_sub']:
        opener = 'Picking up our earlier exchange about PoE / industrial switches.'
    else:
        opener = 'We have been in touch before about PoE and industrial switches; instead of a catalogue, here is one concrete option.'
    et = elsa_touch(ent)
    _facts = (((ent.get('research') or {}).get('mail_review') or {}).get('facts') or [])
    _inbound = any(isinstance(x, dict) and x.get('dir') == '来' for x in _facts)
    if et and _inbound and not deal and not ent['reply_sub'] and 'ISAF2025展会' not in ent['tags']:
        opener = 'Picking up our earlier exchange about PoE / industrial switches.'  # 对方来过信（含对 Elsa 的回复）：不说「没理由回群发」
    elif et and not deal and not ent['reply_sub'] and 'ISAF2025展会' not in ent['tags']:
        # 只替换「泛泛开头」；真实往来（回过信/成单/展会）保留原开头
        n, last_d, last_s, _seen = et
        many = 'a few product mails' if n >= 2 else 'a product mail'
        when = 'Over the past months' if last_d >= '2026-04-01' else 'Some time ago'
        recent = 'most recently ' if n >= 2 else ''
        opener = (f'{when} you had {many} from us - {recent}"{last_s}" on {_dfmt(last_d)} - '
                  f'and there was no reason to answer a mass mail. This one is specific.')
    if et and et[3].get(p1):
        seen_pr, seen_d = et[3][p1]
        live = ELSA_LIVE.get(p1)
        if live and live > seen_pr:
            why_fx = ' - the difference is the CNY/USD move from 7.2 to 6.7' if p1 in ('STC-424XGGPM-280W', 'STC-448XGGPM', 'STC-4168XGGCM') else ''
            price = (f'${live} USD EXW (MOQ 1, 15-day validity; our {seen_d[:7]} mail showed ${seen_pr}{why_fx})')
        elif live:
            price = f'${live} USD EXW (same as the ${seen_pr} you saw in our {seen_d[:7]} mail; MOQ 1, 15-day validity)'
    elif ELSA_LIVE_NOW.get(p1) and not (isinstance(_snp, str) and re.search(r'锚价[：:]?\s*' + re.escape(p1), _snp)):
        price = f'${ELSA_LIVE_NOW[p1]} USD EXW (MOQ 1, 15-day validity)'   # ㉕ ②：该型号的群发现价高于一切档位公式
    rs = ent.get('research') or {}
    _en_brand = {'迈威': 'Maiwe', '海康': 'Hikvision', '大华': 'Dahua', '华为': 'Huawei'}
    _never_name = {'洪瑞', 'HRUI', 'SmartByte', 'Smartbyte', 'Hohunet', '中科德能', '宇航'}  # 自家供应商名不进对外文案
    sb = [_en_brand.get(b, b) for b in brands if b in SWITCH_BRANDS and b not in _never_name]
    sb = [b for b in sb if not re.search(r'[\u4e00-\u9fff]', b) and b not in _never_name]
    slot = f'the {sb[0]} class you work with' if sb else 'the units you source today'
    def _ok_product(x):  # 只用能写进英文正文的对位产品：无中文/全角注记，且是交换机/MC 一类（不是注入器/摄像机/电源/线缆）
        t = f"{x.get('brand') or ''} {x.get('model') or ''}"
        if re.search(r'[\u4e00-\u9fff（）；：]', t):
            return False
        if re.search(r'injector|camera|nvr|power|psu|cable|hdmi|transceiver|module|antenna|router', t, re.I):
            return False
        return bool(x.get('model'))
    _all = [x for x in (rs.get('products_seen') or []) if isinstance(x, dict) and _ok_product(x)]
    ps = [x for x in _all if x.get('saga') == p1] or _all
    if ps:
        slot = f"your {(ps[0].get('brand') or '').strip()} {ps[0]['model']}".replace('  ', ' ')
    hook_note = None
    hk = (rs.get('email_hook') or '').strip()
    if re.search(r'[\u4e00-\u9fff]', hk):
        # 研究档 email_hook 是中文备注（「（不主动发送）」「（无邮箱；WhatsApp：…）」「（低优先…）」）而非钩子句
        hook_note = hk
        if re.search(r'不主动发送|不发送|不发：|不跟|不触达|守界：不', hk[:40]):
            return f'> 研究档 email_hook 标注「{hk}」：不出邮件样板（对方来询再按「产品决策」P1 手写）。'
        m_en = re.search(r'[：:]\s*([A-Z][^）]{30,})', hk)
        hk = m_en.group(1).strip() if m_en else ''
    native = ''
    if hk:
        if name:  # 称呼已在 Hi 行：钩子句开头的「Name,」/「Name Bey,」去重
            hk = re.sub(r'^' + re.escape(name) + r'(?: Bey| Hanım| Bey,)?,\s*', '', hk)
            if hk and hk[0].islower():
                hk = hk[0].upper() + hk[1:]
        hk, native = hook_lang(hk)
        if native:
            hook_note = f'客户语言一句话（研究档 email_hook；要用就整段单发，不混进英文信）：{native}'
            if 'ISAF2025展会' in ent['tags']:
                first_q = 'Is the requirement we talked about at ISAF still open - and which port count comes first?'
        if hk:
            opener = opener + ' ' + hk
    oem = ' under your own label with neutral packaging' if ('品牌' in typ or 'OEM' in typ or '分销' in typ or '经销' in typ) else ' with neutral packaging'
    short = re.split(r' \(|, ', desc)[0]
    subj = f'{p1} - {short} ({chip + ", " if chip else ""}neutral label)'
    hook_q = bool(hk) and '?' in hk  # 钩子句已带问题 → 不再叠加通用问句（一次只问一个问题）
    # 钩子句自带价：与 P1 档价不同（差 > $1）→ 不再叠加 P1 段落（一封信一个价，钩子句为准，P1 段留注）
    _hk_nums = [float(a or b) for a, b in re.findall(r'\$\s?(\d+(?:\.\d+)?)|(?<![\d.])(\d+(?:\.\d+)?)\s?USD', hk or '')]
    _cur = re.search(r'\$([\d.]+)', price or '')
    _cur = float(_cur.group(1)) if _cur else None
    _ranges = [(float(a), float(b)) for a, b in re.findall(r'\$\s?(\d+(?:\.\d+)?)\s?[–-]\s?(\d+(?:\.\d+)?)', hk or '')]
    _in_range = _cur is not None and any(lo - 1.0 <= _cur <= hi + 1.0 for lo, hi in _ranges)
    price_clash = (bool(_hk_nums) and _cur is not None and not _in_range
                   and all(abs(n - _cur) > 1.0 and abs(n - 2 * _cur) > 1.0 for n in _hk_nums))  # 区间含档价 / 「一对」= 2× 单价 不算冲突
    para = (f"We supply {'a ' + chip + ' ' if chip else ('an ' if (desc[0] in 'aeiou' or desc.startswith(('8', '18', '80'))) else 'a ')}{desc} - model {p1} - that fits the same slot as {slot} at a lower landed cost, and we can ship it{oem}. "
            f'Current price: {price}.')
    body = '\n'.join([
        hi, '',
        opener, ''] + ([] if price_clash else [para, '']) + ([] if hook_q else [f'One question: {first_q}', '']) + [
        'If useful, one unit at the unit price for a 30-day side-by-side test. If not a fit, one line and I close the loop.', '',
        'Best regards,',
        'Saga Telecom - PoE / industrial switch OEM-ODM supplier (neutral packing available)',
        'https://sagatele.com/',
    ])
    out = [f'**主题**：{subj}', '', '```text', body, '```', '']
    if hook_note:
        out += [f'> 研究档备注（未并入正文）：{hook_note}', '']
    if price_clash:
        out += [f'> 钩子句自带价（{" / ".join("$" + str(n) for n in _hk_nums)}）与 P1 {p1} 档价（${_cur}）不同：样板未并入 P1 段落，一封信一个价；发前按 ㉕ 核钩子句的价是否仍有效。', '']
    out.append('> 发送前检查：① 不出现「Made in China」或原产地；② 不承诺未实测指标（PoE 功率/温宽）；③ 落款换成发件人姓名；④ 一次只问一个问题；⑤ 价格为 USD EXW 快照，过窗先核价；⑥ 只用表内/公开原值邮箱，不猜地址；⑦ 发出后在「新跟进记录」补一行并告知日期。')
    return '\n'.join(out)


def next_review(g):
    d = dt.date.today()
    if g == 'A':
        return f'- **{(d + dt.timedelta(days=14)).isoformat()}**（14 天）：无回复 → 换通道再试一次；仍无 → 降 B。有任何回复 → 当即更新 research JSON 并重渲染。'
    if g == 'B':
        return f'- **{(d + dt.timedelta(days=30)).isoformat()}**（30 天）：只在有新品/价格窗口/案例时触达；实质回复 → 升 A。'
    return '- 不复核。对方主动来询 → 在 `data/saga_clients/人工定级.csv` 写一行升级后重跑。'


def render_one(ent):
    g = ent['grade']
    code = ent['code']
    typ = infer_type(ent)
    tier = infer_tier(ent, typ)
    p1, p1_why = infer_p1(ent)
    sf = (ent.get('research') or {}).get('saga_fit') or {}
    sg = SITE.get(code) or {}
    if 'p1' in sf and sf['p1'] is None:
        p1, p1_why = None, f"深挖对位：{sf.get('why', '')}"
    elif sf.get('p1'):
        p1, p1_why = sf['p1'], f"深挖对位：{sf.get('why', '')}"
    elif sg.get('auto_p1') and p1_why.startswith('无明确兴趣记录'):
        p1, p1_why = sg['auto_p1'], sg.get('auto_p1_why', '官网快照对位')
    if sf.get('tier') in (20, 25, 30):
        tier = sf['tier']
    brands = brands_seen(ent)
    deal = bool(ent['flags'].get('deal') or ent['deal_in_fu'])
    rel = []
    if deal:
        rel.append('成交/下单过')
    if ent['reply_sub']:
        rel.append(f'实质回复 {ent["reply_sub"]} 次')
    if ent['reply_neg']:
        rel.append(f'回复暂无需求 {ent["reply_neg"]} 次')
    if ent['flags'].get('wa_added') or ent['wa_in_fu']:
        rel.append('WhatsApp 已加')
    if ent['fu_count']:
        rel.append(f'推送 {ent["fu_count"]} 次（{ent["fu_first"] or "?"} → {ent["fu_last"] or "?"}）')
    if not rel:
        rel.append('名单内·无互动记录')
    tags_short = '、'.join(ent['tags'])
    ai_txt = ''
    for a in ent['ai_evals']:
        parts = []
        if a.get('claude') and a['claude'].get('grade'):
            parts.append(f"Claude {a['claude']['pct']}% {a['claude']['grade']}")
        if a.get('ai') and a['ai'].get('grade'):
            parts.append(f"AI {a['ai']['pct']}% {a['ai']['grade']}")
        if parts:
            ai_txt = '；'.join(parts)
            break
    website = ent['domains'][0] if ent['domains'] else ''
    p1_price = price_line(p1, tier) if p1 else '—'
    last_reply = ''
    for f in reversed(ent['followups']):
        if f['reply'] and f['reply_kind'] in ('substantive', 'negative', 'other'):
            last_reply = f"{f['date_iso'] or f['date']}：{f['reply']}"
            break
    first_q = {
        'A': 'Which switch model are you buying most often right now, and roughly how many units a month?',
        'B': 'Are PoE / industrial switches something you still source today, or has that line been dropped?',
        'C': '—（C 级不发首触）',
    }[g]
    unknown = []
    if not ent['persons']:
        unknown.append('采购/产品负责人姓名（表内只有公司级邮箱）')
    if not website:
        unknown.append('公司网站（表内无域名，无法核实是否仍在运营）')
    if not ent['interests']:
        unknown.append('具体需求型号（表内兴趣列为空）')
    if not ent.get('research'):
        if sg.get('status') == 'ok':
            unknown.append('人工网页调研未做（已有官网自动快照，见「客户调研 → 官网快照」；规模/决策人待人工补）')
        else:
            unknown.append('网页调研未做（公司规模/业务/在卖品牌待核）')
    if website and sg and sg.get('status') == 'mismatch':
        unknown.append('公司官网（表内域名经核实不属于本客户；真实官网未知）')
    elif website and sg and sg.get('status') not in ('ok', None, ''):
        unknown.append(f"官网当前状态异常（{sg.get('status_cn', sg.get('status'))}）——公司是否仍在运营待核")
    if not unknown:
        unknown.append('年走量与现供应商')
    yaml_tags = json.dumps(ent['tags'], ensure_ascii=False)
    lines = []
    rs = ent.get('research') or {}
    lines.append(f'# {ent["name"]}')
    if rs.get('name_official') and rs['name_official'].strip() != ent['name'].strip():
        lines.append(f'**官方名称（调研核实）**：{rs["name_official"]}')
    lines.append('')
    lines.append(f'> **评级 {g}**　|　{ent["country"]}　|　档案编号 `{code}`　|　优先级 {stars(g)}　|　状态：{ent["status"]}')
    lines.append('>')
    sv = SIEVE.get(code)
    if sv:
        lab = SIEVE_LABEL.get(sv.get('verdict'), sv.get('verdict'))
        if sv.get('verdict') == 'pass_final':
            lines.append(f"> **{lab}**（闸 {sv.get('gate')} · {sv.get('rule')} · {sv.get('date')}）：{sv.get('reason')} —— 不再加厚 / 不群发 / 不监控 / 不进日历；撤销只在客户主动找上门时由 Simon 拍板（`data/saga_clients/sieve.json`）。")
        else:
            tg = ('　|　标签：' + '、'.join(t + SIEVE_TAG_NOTE.get(t, '') for t in sv['tags'])) if sv.get('tags') else ''
            lines.append(f"> **C 池筛选：{lab}**（闸 {sv.get('gate')} · {sv.get('date')}）：{sv.get('reason')}{tg}")
        lines.append('>')
    lines.append(f'> **类型**：{typ}（推断）　|　**历史关系**：{"；".join(rel)}　|　**所在清单**：{tags_short}　|　结构版本：v1（Saga Clients · 继承 profile/ 骨架 · 2026-10-21 起）')
    lines.append('')
    lines.append('```yaml structured_profile')
    lines.append(f'code: {code}')
    lines.append(f'rating: {g}')
    lines.append(f'rating_auto: {ent["grade_auto"]}')
    if SIEVE.get(code):
        lines.append(f"sieve: {SIEVE[code].get('verdict')}  # 闸 {SIEVE[code].get('gate')} {SIEVE[code].get('rule')} {SIEVE[code].get('date')}")
    if rs.get('grade_override'):
        lines.append(f'rating_research: {rs["grade_override"]}  # {rs.get("override_reason", "")[:80]}')
    if rs.get('name_official'):
        lines.append(f'name_official: {json.dumps(rs["name_official"], ensure_ascii=False)}')
    if ent.get('manual'):
        lines.append(f'rating_manual: {ent["manual"].get("等级", "")}  # {ent["manual"].get("理由", "")}')
    lines.append(f'score: {ent["score"]}')
    lines.append(f'country: {ent["country"]}')
    if ent.get('country_table'):
        lines.append(f'country_table: {ent["country_table"]}  # 表内原填；调研纠正为 {ent["country"]}（research JSON country_fix）')
    lines.append(f'region: {ent["region"]}')
    lines.append(f'website: {website or "none"}')
    lines.append(f'type: {typ}')
    lines.append(f'tier_tags: {yaml_tags}')
    lines.append(f'deal: {"yes" if deal else "no"}')
    lines.append(f'replies: {ent["reply_sub"]}')
    lines.append(f'followups: {ent["fu_count"]}')
    lines.append(f'first_contact: {ent["fu_first"] or "unknown"}')
    lines.append(f'last_contact: {ent["fu_last"] or "unknown"}')
    gm = GMAIL.get(code)
    if gm:
        lines.append(f"s_mail: {gm['messages']} msgs (out {gm['out']} / in {gm['in']}), {gm['first']} -> {gm['last']}")
    lines.append(f'p1: {p1 or "none"}')
    lines.append(f'price_tier: {tier}%')
    lines.append(f'research: {"done" if ent.get("research") else "pending"}')
    lines.append(f'site_snapshot: {sg.get("status", "none")}' + (f'  # {sg.get("fetched_at", "")[:10]}' if sg else ''))
    lines.append(f'sources: {len(ent["sources"])}')
    lines.append(f'updated: {TODAY}')
    lines.append('```')
    lines.append('')
    lines.append('## SALES BRIEF（压缩模型）')
    lines.append('')
    who = f'{ent["country"]}的{typ}'
    if ent['interests']:
        who += '；兴趣/在卖：' + '；'.join(ent['interests'])[:160].replace('\n', ' ')
    if brands:
        who += f'；提到的品牌：{", ".join(brands)}'
    if rs.get('summary'):
        who = rs['summary'].strip() + f'（调研 {rs.get("researched_at", "")}；表内兴趣：' + ('；'.join(ent['interests'])[:120].replace('\n', ' ') if ent['interests'] else '—') + '）'
    lines.append(f'- **是谁**：{who}')
    why = '；'.join(ent['reasons']) + (f'；C 级细分：{ent["c_sub"]}' if g == 'C' and ent['c_sub'] else '')
    if ent.get('manual'):
        why = f'**人工定级 {ent["manual"].get("等级", "")}**（{ent["manual"].get("理由", "")}）；自动分级 {ent["grade_auto"]}：' + why
    elif rs.get('grade_override'):
        why = f'**调研后定级 {rs["grade_override"]}**（{rs.get("override_reason", "")}）；自动分级 {ent["grade_auto"]}：' + why
    lines.append(f'- **为什么是 {g} 级**：' + why)
    hist = '；'.join(rel)
    if last_reply:
        hist += f'；最近一次客户回复：{last_reply}'
    lines.append(f'- **历史互动**：{hist}')
    mr = rs.get('mail_review') or {}
    if g != 'C' and mr:
        sn = mr.get('saga_now') or {}
        nm = mr.get('next_move') or {}
        lines.append(f"- **P1（下一步唯一主推 · 来自针对性复盘 {mr.get('as_of', '')}）**：{sn.get('p1') or p1 or '—'} — {sn.get('why', '')}；{sn.get('price', '')}")
        lines.append(f"- **第一问（只问一个）**：{nm.get('one_question') or first_q}")
    elif g != 'C':
        lines.append(f'- **P1（下一步唯一主推）**：{p1 or "—"} — {p1_why}；{p1_price}')
        lines.append(f'- **第一问（只问一个）**：{first_q}')
    else:
        lines.append(f'- **P1**：不推（C 级）；若对方主动来询，起手 {p1 or "STC-424DGGPM-280W"}（{p1_why}）')
    lines.append(f'- **最大未知**：{"；".join(unknown)}')
    nxt = {'A': '按下文「跟进建议」第 1 次执行；回复后更新 research JSON 并重渲染', 'B': '放入慢跟队列（4–6 周一次）；有回复即重评', 'C': '不跟进；仅归档防重复开发'}[g]
    if mr and (mr.get('next_move') or {}).get('action'):
        nm = mr['next_move']
        nxt = f"{nm.get('when', '')} {nm.get('channel', '')} {nm.get('action', '')}".strip()
    lines.append(f'- **下一步**：{nxt}')
    lines.append('')
    if mr:
        lines.append(f"## 针对性复盘（邮件 / PI / Drive 证据 · {mr.get('as_of', '')}）")
        lines.append('')
        lines.append(fmt_mail_review(ent))
        lines.append('')
    if g in ('A', 'B'):
        dm = fmt_dims(ent)
        if dm:
            lines.append(dm)
        im = fmt_imports(ent)
        if im:
            lines.append(im)
        b82 = fmt_batch82(ent, rs)
        if b82:
            lines.append(b82)
    elif ent['code'] in SIEVE and SIEVE[ent['code']].get('gate', 0) >= 2:  # C 池闸 2 查过底数 → 渲染「公司底数」块（T29-U118）
        b82 = fmt_batch82(ent, rs)
        if b82:
            lines.append(b82)
    lines.append('## 基本事实（事实/推断/假设分层）')
    lines.append('')
    lines.append('| 项 | 内容 | 层级 |')
    lines.append('|---|---|---|')
    lines.append(f'| 名称 | {md_escape(ent["name"])}{"（取自域名，公司全名待核）" if ent["name_src"] == "domain" else ""} | {"事实（用户表）" if ent["name_src"] == "company" else "推断"} |')
    if len(ent['names']) > 1:
        lines.append(f'| 其他名称写法 | {md_escape(" / ".join(ent["names"][1:]))} | 事实（用户表） |')
    lines.append(f'| 国家 | {ent["country"]}{"（另见：" + "、".join(ent["other_countries"]) + "）" if ent["other_countries"] else ""} | 事实（用户表）|')
    lines.append(f'| 网站/域名 | {md_escape(" / ".join(ent["domains"]) or "—")} | 事实（用户表 URL/邮箱域名） |')
    lines.append(f'| 类型 | {typ} | 推断（据兴趣/备注关键词） |')
    lines.append(f'| 联系人 | {md_escape(" / ".join(ent["persons"]) or "—")} | 事实（用户表） |')
    lines.append(f'| 来源（From） | {md_escape(" / ".join(ent["froms"]) or "—")} | 事实（用户表） |')
    lines.append(f'| 兴趣（Interested in） | {md_escape(" / ".join(ent["interests"]) or "—")} | 事实（用户表） |')
    lines.append(f'| 用户备注（Remark） | {md_escape(" / ".join(ent["remarks"]) or "—")} | 事实（用户表） |')
    if ent['categories']:
        lines.append(f'| 用户分档（Category） | {md_escape(" / ".join(sorted(set(ent["categories"]))))} | 事实（用户表） |')
    if ai_txt:
        lines.append(f'| 用户 AI 评估 | {ai_txt} | 事实（用户表 AI评估结果/CALUDE评估结果列） |')
    lines.append(f'| 所在清单 | {md_escape(tags_short)} | 事实（文件路径） |')
    lines.append(f'| 在卖/在用品牌（备注所见） | {", ".join(brands) or "—"} | 事实（用户备注）/ 推断 |')
    lines.append('')
    if ent['ai_evals']:
        lines.append('### 用户 AI / Claude 评估原文')
        lines.append('')
        for a in ent['ai_evals']:
            for k in ('claude', 'ai'):
                if a.get(k) and a[k].get('text'):
                    lines.append(f'- **{"Claude" if k == "claude" else "AI"}**（{os.path.basename(a["file"])}）：')
                    for ln in a[k]['text'].split('\n'):
                        lines.append(f'  > {ln}')
        lines.append('')
    lines.append('## 客户调研（网页核实 · 引文 + URL + 日期）')
    lines.append('')
    lines.append(fmt_research(ent))
    snap_block = fmt_snapshot(ent)
    if snap_block:
        lines.append(snap_block)
    lines.append('')
    lines.append('## 在卖/在用品牌 → Saga 对位')
    lines.append('')
    if brands:
        lines.append('| 备注所见品牌 | 含义 | Saga 切入 |')
        lines.append('|---|---|---|')
        for b in brands:
            bl = b.lower()
            if bl in ('洪瑞', 'hrui'):
                meaning, cut = '洪瑞 = HRUI（Saga 的 Realtek 辅线供应商）', '同源货：Saga STC Realtek 线（见 data/hrui_STC对照表.csv）可直接对型号报价'
            elif bl in ('smartbyte', 'dptek'):
                meaning, cut = 'Saga 主供应商 / 深圳同行品牌', '对方已接受深圳 Marvell 方案：直接谈贴牌与价格'
            elif bl in ('onv', 'utepo', 'upeto', 'ewind', '中科德能', 'e-link', 'elink', '丰润达', '磊通', 'gxcom', 'witek', 'g-net', 'gnet', 'uotek', 'n-net', 'ots', 'unipoe', '优力普', '迈威', 'maiwe', '武汉迈威', 'kyland', '东土', 'ctcu', 'hioso', 'raisecom', 'bdcom', 'mlis', 'diva', 'longse'):
                meaning, cut = '深圳/国内白牌或品牌供应商', '对方已在买中国货：以 Marvell 芯片 + L2+ 功能 + 交期为差异点做第二货源'
            elif bl in ('planet', 'moxa', 'oring', 'korenix', 'lantech', 'etherwan', 'advantech', 'antaira', 'comnet', 'perle', 'transition', 'westermo', 'hirschmann', 'phoenix', 'redlion', 'red lion', 'siemens', 'weidmuller', 'weidmüller', 'belden', 'ruggedcom', 'scalance', 'black box', 'startech', 'trendnet', 'allied telesis', 'd-link', 'zyxel', 'netgear', 'tp-link', 'tenda', 'mikrotik', 'ubiquiti', 'cambium', 'teltonika', 'robustel', 'inhand', 'milesight', 'fs.com', 'fs', 'televes'):
                meaning, cut = '台系/欧美/品牌工业或商用网络品牌', '按「同口数同功能的 Marvell 方案、价低一档、中性包装」做对位（不贬低原品牌）'
            elif bl in ('cisco', 'aruba', 'hpe', 'dell', 'juniper', 'extreme', 'huawei', 'h3c', 'ruijie', 'zte', 'fiberhome', '华为'):
                meaning, cut = '企业级大牌（Cisco/HPE/华为类）', 'Saga 只能接接入层/工业层，不对标核心；问清是否有白牌接入层需求'
            elif bl in ('hikvision', 'dahua', 'uniview', 'unv', 'axis', 'bosch', 'hanwha', '海康', '大华'):
                meaning, cut = '安防摄像头品牌', '对方是安防集成/经销：主推 PoE 交换机配套（看门狗、长距、bt 口）'
            else:
                meaning, cut = '品牌/芯片提及', '按场景对位'
            lines.append(f'| {b} | {meaning} | {cut} |')
    else:
        lines.append('（备注未提及具体品牌）')
    lines.append('')
    lines.append('## 历史跟进记录（原表照录）')
    lines.append('')
    lines.append(fmt_followups(ent))
    lines.append('')
    if ent.get('pi'):
        lines.append('## 成交记录（PI 包 · 自动汇总）')
        lines.append('')
        lines.append(fmt_pi(ent))
        lines.append('')
    if g in ('A', 'B') and GMAIL.get(code):
        lines.append('## 邮箱往来（S 邮箱 · 自动汇总）')
        lines.append('')
        lines.append(fmt_gmail(ent))
        lines.append('')
    if WATCH.get(code):
        lines.append('## 动态监控（自动 · 网站 / 社媒 / 代码库）')
        lines.append('')
        lines.append(fmt_watch(ent))
        lines.append('')
    lines.append('## 联系方式（已有 · 原值照录）')
    lines.append('')
    lines.append(fmt_contacts(ent))
    lines.append('')
    lines.append('## 关键人（KP）与触达通道')
    lines.append('')
    lines.append('| 姓名 | 角色 | 联系方式 | 状态/核实度 | 来源 |')
    lines.append('|---|---|---|---|---|')
    for r in kp_rows(ent):
        lines.append('| ' + ' | '.join(md_escape(str(x)) for x in r) + ' |')
    lines.append('')
    lines.append(f'- **通道建议**：{channel_advice(ent, g)}')
    lines.append('')
    lines.append('## 来源与归并（不漏 · 原始行定位）')
    lines.append('')
    if len(ent['sources']) > 1:
        lines.append(f'本客户由 **{len(ent["sources"])} 行**原始记录归并而成；归并键：{", ".join("`" + k + "`" for k in ent.get("merge_keys", [])) or "（同一文件内同 No.）"}。')
    else:
        lines.append('本客户只有 1 行原始记录。')
    if ent.get('code_aliases'):
        lines.append(f'曾用编号：{", ".join(ent["code_aliases"])}')
    lines.append('')
    lines.append(fmt_sources(ent))
    lines.append('')
    if g != 'C':
        lines.append('## 产品决策（Saga · 单一决策口径）')
        lines.append('')
        lines.append('| 优先级 | 型号 | 场景 | 价格（USD EXW 快照） | 选它的原因 |')
        lines.append('|---|---|---|---|---|')
        lines.append(f'| **P1** | {p1 or "待核型（无标准对应，向 SmartByte 核）"} | {p1_why} | {p1_price} | {"深挖对位" if p1_why.startswith("深挖对位") else "据用户表兴趣/备注推断"}；档位 {tier}%（{typ}） |')
        alts = [('STC-28DGGPM', '8 口 PoE + 2 SFP L2+ 小接入'), ('STI-288DGGPM', '工业 L2+ 8 PoE + 2×2.5G SFP'), ('STC-424XGGPM-280W', '24 PoE + 4×10G 上联')]
        n = 2
        for m, sc in alts:
            if m != p1:
                lines.append(f'| 备选{n} | {m} | {sc} | {price_line(m, tier)} | P1 之后的台阶，不进首触 |')
                n += 1
        lines.append('')
        lines.append('- **口径纪律**：价格 = SmartByte CNY × (1+档位) ÷ 汇率；档位：分销/电商 20%、集成/项目 25%、OEM/ODM 30%；商用线无 802.3bt、无云管理；证书只有 CE/RoHS/FCC/REACH/UKCA（无 UL）。')
        lines.append('')
    lines.append('## 跟进建议')
    lines.append('')
    lines.append(followup_plan(ent, g, p1, tier))
    lines.append('')
    if g != 'C':
        lines.append('## SWOT')
        lines.append('')
        lines.append(swot(ent, g, typ, p1, tier, brands))
        lines.append('')
    lines.append('## 触达与风险红线')
    lines.append('')
    lines.append('1. 包装、外观、说明书全部中性，不出现「Made in China」，贴客户自己的型号。')
    lines.append('2. 邮件只用表内原值地址；「发不过去」的地址保留并标注，不猜新地址。')
    lines.append('3. 不承诺 UL、EN50155、IP67、云管理；PoE 功率与工业温宽以实测为准。')
    lines.append('4. 乌克兰/军工/公共部门/轨道/生命安全场景守界；巨头分销与品牌厂商不投入。')
    lines.append('5. 同一客户在多张表出现时以本档为唯一入口，避免多人重复触达。')
    lines.append('')
    lines.append('## Qualification 清单')
    lines.append('')
    lines.append(qualification(ent, g, brands))
    lines.append('')
    lines.append('## Unknowns（待问清单 · 跟进后逐项消除）')
    lines.append('')
    for u in unknown:
        lines.append(f'- [ ] {u}')
    if unknown and '年走量与现供应商' not in unknown:
        lines.append('- [ ] 年走量与现供应商')
    lines.append('')
    lines.append('## 英文跟进邮件（样板 · 可直接发送）')
    lines.append('')
    dr = (rs.get('mail_review') or {}).get('draft_en') or {}
    if dr.get('body'):
        lines.append(f"**主题**：{dr.get('subject', '')}\n\n```text\n{dr['body'].strip()}\n```\n\n> 本稿来自「针对性复盘」（有据可查的现状），替代下方自动样板；发送前只核价格快照日期。")
        _hk = (rs.get('email_hook') or '').strip()
        if _hk and not re.search(r'[\u4e00-\u9fff]', _hk):
            _en, _nat = hook_lang(_hk)
            if _nat and _nat.strip() not in dr['body']:
                lines.append(f"\n> 客户语言一句话（研究档 email_hook；对方若不读英文，整段单发 WhatsApp/邮件）：{_nat}")
    else:
        lines.append(email_draft(ent, g, typ, p1, tier, brands, first_q))
    lines.append('')
    lines.append('## 新跟进记录（仓库外发出后补）')
    lines.append('')
    lines.append('| 日期 | 渠道 | 对象 | 我方动作 | 对方回应 | 下一步 | 下次动作日期 |')
    lines.append('|---|---|---|---|---|---|---|')
    lines.append('|  |  |  |  |  |  |  |')
    lines.append('')
    lines.append('> 历史跟进见上文「历史跟进记录（原表照录）」；新动作由用户在仓库外执行后告知日期与渠道，写入 research JSON 的 notes 后重渲染。')
    lines.append('')
    lines.append('## 下次复核')
    lines.append('')
    lines.append(next_review(g))
    lines.append('')
    lines.append('## 变更日志')
    lines.append('')
    lines.append(f'- {TODAY}：建档（PR-02-19 · 从 `Clients/` {len(ent["sources"])} 行原始记录归并；自动评级 {ent["grade_auto"]}，分数 {ent["score"]}）' + (f'；人工/调研定级 → {g}' if g != ent['grade_auto'] else ''))
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append(f'*建档日期：{TODAY}　|　数据来源：`Clients/`（Simon 上传，原件只读）　|　渲染：scripts/saga_clients/render.py　|　重复归并：data/saga_clients/重复客户归并记录.md*')
    return '\n'.join(lines) + '\n'


def main():
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    for g in 'ABC':
        d = os.path.join(OUT_DIR, g)
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d, exist_ok=True)
    index = defaultdict(list)
    for e in ents:
        fn = f"{e['code']}-{slug(e['name'])}-{slug(e['country'], 12)}.md"
        sub = sub_dir(e['code'], e['grade'])
        os.makedirs(os.path.join(OUT_DIR, e['grade'], sub), exist_ok=True)
        path = os.path.join(OUT_DIR, e['grade'], sub, fn)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(render_one(e))
        index[e['grade']].append((e, fn))
    write_readme(ents, index)
    write_deep_overview(index)
    print({g: len(v) for g, v in index.items()})


def write_deep_overview(index):
    """A 级加厚挖掘总览（生成文件，不手改）：编号 / 公司 / 国家 / 深挖等级 / P1 / 档位 / 对位理由 / 文件。"""
    rows = []
    for e, fn in sorted(index.get('A', []), key=lambda x: x[0]['code']):
        rs = e.get('research') or {}
        dp = rs.get('deep') or {}
        sf = rs.get('saga_fit') or {}
        seen = rs.get('products_seen') or []
        dm = DIMS.get(e['code']) or {}
        heat = (dm.get('heat') or {}).get('score', '')
        bl = dm.get('ball') or {}
        if bl:
            ball = ('**他们**' if bl.get('last_dir') == 'in' else '我们') + f" {bl.get('last_date', '')}（{bl.get('days_since', '')} 天）"
        else:
            ball = '—'
        rows.append('| {code} | {name} | {c} | {lvl} | {p1} | {tier} | {n} | {heat} | {ball} | {why} | `{fn}` |'.format(
            code=e['code'], name=(rs.get('name_official') or e['name'])[:40].replace('|', '/'), c=e['country'],
            lvl=(dp.get('level') or '未加厚').replace('|', '/'), p1=sf.get('p1') or ('待核型' if 'p1' in sf else '—'),
            tier=f"{sf.get('tier')}%" if sf.get('tier') else '—', n=len(seen), heat=heat, ball=ball,
            why=(sf.get('why') or '')[:90].replace('|', '/'), fn=fn))
    done = sum(1 for e, _ in index.get('A', []) if (e.get('research') or {}).get('deep'))
    L = ['# A 级客户 · 加厚挖掘总览', '',
         f'> 生成：{TODAY}　|　A 级 {len(index.get("A", []))} 家，已加厚 {done} 家（深挖块 = 公司事实 / 业务线 / 在卖在用型号→Saga 对位 / 公开通道 / 近况信号 / 风险 / 对位结论 / 英文切入句，均在各自 MD 的「客户调研 → 加厚挖掘」小节）。',
         '>', '> 改 `data/saga_clients/research/<编号>.json`（经 `scripts/saga_clients/deepen.py`）后重跑 `render.py` 生成；**不手改**。', '',
         '> 「热度」「最后一句」两列来自第 79 批多维画像（`dims.json`）：热度 0–100 = 最近来信 / 回过几次 / 近 12 个月打开 / 成交 / 1:1 报价；最后一句 = 1:1 对话里最后说话的是谁与日期（**他们** = 球在我们手里）。', '',
         '| 编号 | 公司 | 国家 | 深挖等级 | P1 | 档位 | 型号条数 | 热度 | 最后一句 | 对位理由（摘） | 文件 |', '|---|---|---|---|---|---|---|---|---|---|---|']
    L += rows
    with open(os.path.join(OUT_DIR, 'A', '_加厚总览.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')


def write_readme(ents, index):
    n = len(ents)
    byg = Counter(e['grade'] for e in ents)
    byreg = Counter((e['grade'], e['region']) for e in ents)
    regions = ['北美', '欧洲', '土耳其', '中东', '亚太', '俄语区', '南亚', '拉美', '非洲', '乌克兰', '中国大陆', '未知']
    L = []
    L.append('# Saga Clients — Saga 历史客户全量档案（A / B / C）')
    L.append('')
    L.append(f'> 生成：{TODAY}　|　来源：`Clients/`（Simon 上传到 main 的 137 个文件：6,246 行线索 + 20,819 条跟进记录）　|　归并后 **{n} 个客户**：A {byg["A"]} / B {byg["B"]} / C {byg["C"]}')
    L.append('>')
    L.append('> 流水线：`scripts/saga_clients/extract.py`（逐表逐行抽取）→ `build.py`（归并重复 + 规则分级 + 人工定级/调研覆盖）→ `render.py`（本目录）。**MD 不手改**：改 `data/saga_clients/人工定级.csv` 或 `research/<编号>.json` 后重跑。')
    L.append('')
    L.append('## 等级定义（用户口径 → 执行口径）')
    L.append('')
    L.append('| 等级 | 用户定义 | 执行口径（build.py） |')
    L.append('|---|---|---|')
    L.append('| **A** | 值得长期跟进 / OK 的 | 分数 ≥ 60 **且**有互动证据（成交 / 实质回复 / 询盘 / 展会面谈 / S 重点名单）；台系品牌商、巨头、守界区域、品类不符封顶 B 或 C |')
    L.append('| **B** | 一般的，慢慢跟进 | 分数 25–59；或有实质回复但分数低（托底 B）；或 A 候选但无互动证据（封顶 B） |')
    L.append('| **C** | 垃圾 / 基本或压根不值得跟进 | 分数 < 25；或硬规则：用户已归「不行及不太相关」、无联系方式、中国大陆、乌克兰（守界）、巨头/品牌厂商/运营商、备注「不再跟进/Spam」 |')
    L.append('')
    L.append('分数 = 用户信号（成单 +50、实质回复 +22/+30、S 名单 +25、已回复名单 +18、WhatsApp +15、询盘 +12、ISAF 面谈 +12、1类 +15、AI/Claude A +15…）'
             '− 负面（不行 −60、不再跟进 −40、发不过去 −25、巨头 −45、聋名单 −10/−16/−22…）+ 契合（自有品牌 +12、交换机主线 +8、品类不符 −15）'
             '+ 通道（企业邮箱 +10、有网站 +5、无联系方式 −40）+ 区域（北美/欧洲/土耳其 +8 … 南亚/非洲 −6、中国大陆 −40、乌克兰 −20）+ 时效。每个档案的「为什么是 X 级」逐项列出。')
    L.append('')
    L.append('## 分布')
    L.append('')
    L.append('| 区域 | A | B | C | 合计 |')
    L.append('|---|---|---|---|---|')
    for r in regions:
        a, b, c = byreg[('A', r)], byreg[('B', r)], byreg[('C', r)]
        if a + b + c:
            L.append(f'| {r} | {a} | {b} | {c} | {a + b + c} |')
    L.append(f'| **合计** | {byg["A"]} | {byg["B"]} | {byg["C"]} | {n} |')
    L.append('')
    st = Counter(e['status'].split('·')[0].split(' ')[0] for e in ents)
    L.append('状态分布：' + '；'.join(f'{k} {v}' for k, v in st.most_common()))
    L.append('')
    csub = Counter(e['c_sub'] for e in ents if e['grade'] == 'C')
    L.append('C 级细分：' + '；'.join(f'{k} {v}' for k, v in csub.most_common()))
    L.append('')
    rsn = sum(1 for e in ents if e.get('research'))
    ovr = Counter((e['research'].get('grade_override') or 'keep') for e in ents if e.get('research'))
    L.append('## 调研覆盖（A 候选逐家网页核实）')
    L.append('')
    L.append(f'- 自动评级曾为 A 的候选 **全部** 做了网页核实：{rsn} 家（`data/saga_clients/research/`，每家含引文 + URL + 日期）；'
             f'维持 A {ovr["keep"]} / 调研后降 B {ovr["B"]} / 调研后降 C {ovr["C"]}。')
    L.append('- 降级口径：≥14 次推送 0 回复（即便面谈/OEM 意向）→ B 并标「回复即升 A」；核心需求在 Saga 线外（IP67、M12、HDMI 延长器、仅 SFP/DWDM、400G）→ B；'
             '已停业 / 休眠壳公司 / 疑似同行 / 军工守界 / TKH 等集团子公司 → C；中国直采的纯比价客户 → B。')
    L.append('- B/C 级未逐家网页核实（量级 4,500+），分级依据为用户表信号 + 规则；任一 B 升 A 前先补一份 research JSON。')
    L.append('')
    L.append('## 档案结构（与 `profile/` 同骨架）')
    L.append('')
    L.append('头部引言（评级/编号/状态）→ `yaml structured_profile` → SALES BRIEF → 基本事实（分层）→ 用户 AI/Claude 评估原文 → 客户调研（引文+URL+日期）→ 在卖/在用品牌→Saga 对位 → '
             '历史跟进记录（原表照录）→ 联系方式（原值）→ 关键人（KP）与触达通道 → 来源与归并（原始行定位）→ 产品决策（P1 + 备选 + 价格快照）→ 跟进建议（3 步）→ SWOT → '
             '触达与风险红线 → Qualification 清单 → Unknowns → 英文跟进邮件（样板）→ 新跟进记录 → 下次复核 → 变更日志。C 级省略产品决策/SWOT/邮件样板。')
    L.append('')
    L.append('## 配套文件')
    L.append('')
    L.append('- `data/saga_clients/客户主表.csv` — 一行一个客户（编号 / 等级 / 分数 / 联系方式 / 来源定位 / 评级依据）')
    L.append('- `data/saga_clients/重复客户归并记录.md` — 多来源客户与归并键、正负名单冲突')
    L.append('- `data/saga_clients/rows_raw.jsonl` / `followups.jsonl` / `extract_report.json` — 原始逐行抽取与逐文件行数（不漏复核）')
    L.append('- `data/saga_clients/research/` — 调研 JSON（引文 + URL + 日期；含 grade_override）')
    L.append('- `data/saga_clients/人工定级.csv` — 人工覆盖（列：键或编号, 等级, 理由）')
    L.append('- `Clients/` — 原件（只读，不改名不改内容）')
    L.append('')
    L.append('## 索引')
    L.append('')
    L.append(f'目录结构：A 平铺；B / C 每 {BUCKET} 户一个子目录（`B/SB-0001-0500/`、`B/SB-0501-1000/`、`B/SB-1001-1500/` …，GitHub 网页一个目录只显示前 1,000 个文件），'
             '编号连号，看编号就知道在哪个子目录；各级 `_索引.md` 的链接直达文件。')
    L.append('')
    for g in 'ABC':
        subs = sorted({sub_dir(e['code'], g) for e, _ in index[g]} - {''}, key=lambda s: int(s.split('-')[1]))
        L.append(f'### {g} 级（{len(index[g])}）— `Saga Clients/{g}/`' + (f'（子目录 {" / ".join(f"`{s}/`" for s in subs)}）' if subs else ''))
        L.append('')
        if g == 'A':
            L.append('| 编号 | 公司 | 国家 | 类型 | 状态 | 分数 | 调研 | 档案 |')
            L.append('|---|---|---|---|---|---|---|---|')
            for e, fn in sorted(index[g], key=lambda x: x[0]['code']):
                L.append(f"| {e['code']} | {md_escape(e['name'])} | {e['country']} | {infer_type(e)} | {e['status']} | {e['score']} | {'已' if e.get('research') else '待'} | [{fn}]({g}/{fn.replace(' ', '%20')}) |")
        else:
            L.append(f'全部 {len(index[g])} 个档案见 `Saga Clients/{g}/_索引.md`（编号 / 公司 / 国家 / 状态 / 分数 / 文件名）。')
            with open(os.path.join(OUT_DIR, g, '_索引.md'), 'w', encoding='utf-8') as f:
                f.write(f'# {g} 级索引（{len(index[g])}）\n\n')
                n_pass = sum(1 for e, _ in index[g] if (SIEVE.get(e['code']) or {}).get('verdict') == 'pass_final')
                if g == 'C' and SIEVE:
                    f.write(f'> C 池三闸筛选（`docs/C池三闸筛选_方案_2026-10-29.md`）：⛔ 永久 pass {n_pass} 户（状态列前缀 ⛔）；★ = P 池正式入池、☆ = P 池观察档 / 候选（名册 `docs/P池_资产池名册_2026-10-29.md`）；其余留 C 见 `data/saga_clients/sieve.json`。\n\n')
                f.write('| 编号 | 公司 | 国家 | 状态 | 分数 | C级细分 | 档案 |\n|---|---|---|---|---|---|---|\n')
                for e, fn in sorted(index[g], key=lambda x: x[0]['code']):
                    rel = (sub_dir(e['code'], g) + '/' + fn) if sub_dir(e['code'], g) else fn
                    sv = SIEVE.get(e['code']) or {}
                    st = ('⛔ ' if sv.get('verdict') == 'pass_final' else ('★ ' if sv.get('verdict') == 'pool' else ('☆ ' if sv.get('verdict') in ('candidate', 'pool_candidate', 'pool_watch') else ''))) + e['status']
                    f.write(f"| {e['code']} | {md_escape(e['name'])} | {e['country']} | {st} | {e['score']} | {e['c_sub']} | [{fn}]({rel.replace(' ', '%20')}) |\n")
        L.append('')
    with open(os.path.join(OUT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')


if __name__ == '__main__':
    main()
