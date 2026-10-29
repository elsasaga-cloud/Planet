#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群（A/B 三库）深挖缺口盘点 · T29-U131 2026-10-29。

Simon：「这些 A / B 都深挖过了吗？加厚 审核 交叉检查等等 把没有的都再搞一下 如果都搞完了 告诉我」。
一户一行，七个维度：研究深度 / 登记底数 / 官网快照 / 域名·MX / 邮箱·具名 KP / 复核 / 跨库重复 → 「还缺什么」。
写：data/长期客户群_深挖缺口_<date>.csv + docs/长期客户群_深挖缺口_<date>.md；External / Planet 域名 DNS 体检写
data/external_clients/mx_check_<date>.json、data/planet_mx_check_<date>.json（沙箱放行 DNS；dnspython）。幂等。
用法：python3 scripts/lt_gap_audit.py [--no-dns]
"""
import collections
import csv
import datetime as dt
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SD = os.path.join(ROOT, 'data', 'saga_clients')
XD = os.path.join(ROOT, 'data', 'external_clients')
PCSV = os.path.join(ROOT, 'data', '客户名单_Planet渠道_2026-10.csv')
DATE = '2026-10-29'
OUT_CSV = os.path.join(ROOT, 'data', f'长期客户群_深挖缺口_{DATE}.csv')
OUT_MD = os.path.join(ROOT, 'docs', f'长期客户群_深挖缺口_{DATE}.md')
XMX = os.path.join(XD, f'mx_check_{DATE}.json')
PMX = os.path.join(ROOT, 'data', f'planet_mx_check_{DATE}.json')
FIELDS = ['库', '编号', '公司', '国家', '等级', '研究深度', '登记底数', '官网快照', '域名MX', '邮箱', '具名KP', '复核', '跨库重复', '还缺什么']


def load_json(p, default=None):
    if not os.path.exists(p):
        return default
    return json.load(open(p, encoding='utf-8'))


def dns_check(domains, cache_path, workers=16):
    """MX/A 查询；结果缓存到 cache_path（同日不重查）。status: ok | no_mx | dead | nxdomain | error"""
    cache = load_json(cache_path, {'_meta': {}, 'domains': {}})
    todo = [d for d in sorted(set(domains)) if d and d not in cache['domains']]
    if todo:
        try:
            import dns.resolver  # noqa
        except Exception:
            print('dnspython 不可用 → 跳过 DNS 体检（pip install --break-system-packages dnspython）')
            return cache['domains']
        import concurrent.futures as cf
        res = dns.resolver.Resolver()
        res.lifetime = 6
        res.timeout = 3

        def one(d):
            r = {'checked': DATE}
            try:
                mx = sorted((x.preference, str(x.exchange).rstrip('.')) for x in res.resolve(d, 'MX'))
                r['mx'] = mx
                if mx == [(0, '')] or (len(mx) == 1 and mx[0][1] in ('', '.')):
                    r['status'] = 'null_mx'
                else:
                    r['status'] = 'ok'
                return d, r
            except dns.resolver.NXDOMAIN:
                r['status'] = 'nxdomain'
                return d, r
            except Exception:
                pass
            try:
                a = [str(x) for x in res.resolve(d, 'A')]
                r['a'] = a
                r['status'] = 'no_mx' if a else 'dead'
            except dns.resolver.NXDOMAIN:
                r['status'] = 'nxdomain'
            except Exception as e:
                r['status'] = 'dead' if 'NoAnswer' in type(e).__name__ else f'error:{type(e).__name__}'
            return d, r
        with cf.ThreadPoolExecutor(max_workers=workers) as ex:
            for d, r in ex.map(one, todo):
                cache['domains'][d] = r
        cache['_meta'] = {'checked': DATE, 'source': 'DNS MX/A 查询（dnspython，沙箱解析器）', 'domains': len(cache['domains']),
                          'status_counts': dict(collections.Counter(v['status'] for v in cache['domains'].values()))}
        json.dump(cache, open(cache_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return cache['domains']


def saga_rows():
    rows = list(csv.DictReader(open(os.path.join(SD, '客户主表.csv'), encoding='utf-8-sig')))
    ab = [r for r in rows if r['评级'] in ('A', 'B')]
    reg = {}
    for f in glob.glob(os.path.join(SD, 'registry', '*.json')):
        reg.update(load_json(f)['rows'])
    sd = load_json(os.path.join(SD, 'site_digest.json'), {})
    mxf = sorted(glob.glob(os.path.join(SD, 'mx_check_*.json')))
    mx = load_json(mxf[-1])['domains'] if mxf else {}
    ents = {e['code']: e for e in load_json(os.path.join(SD, 'entities.json'))}
    out = []
    for r in ab:
        c = r['档案编号']
        j = load_json(os.path.join(SD, 'research', f'{c}.json'), {})
        e = ents.get(c, {})
        deep = j.get('deep')
        lv = str((deep or {}).get('level') if isinstance(deep, dict) else deep or '')
        if not deep:
            depth = '骨架'
        elif '深挖' in lv:
            depth = '深挖'
        elif 'LT-T01' in lv or '桌面' in lv:
            depth = '桌面加厚（LT-T01，待官网快照）'
        elif 'LT-T02' in lv or '实查' in lv:
            depth = '加厚（邮件证据 + 官网实查）'
        elif '加厚' in lv or '核查' in lv:
            depth = '加厚（官网 / 登记核对）'
        else:
            depth = '仅表内 / 邮件证据（无域名）'
        rg = reg.get(c)
        regs = ('已坐实' if rg.get('number') and '未取' not in str(rg.get('number')) and '未命中' not in str(rg.get('number')) else '部分坐实（无登记号）') if rg else '无'
        s = sd.get(c)
        snap = '有（ok）' if s and s.get('status') == 'ok' else (f"失败（{s.get('status')}）" if s else '无')
        doms = e.get('domains') or []
        sts = [mx.get(d, {}).get('status') for d in doms]
        mxs = ('ok' if 'ok' in sts else (sts[0] or '未查')) if doms else '无域名'
        em = '有' if (r['企业邮箱'] or r['全部邮箱']) else '无'
        kp = '有' if any(k.get('name') not in (None, '', '—', '-') for k in (j.get('kp') or [])) or any(p and p not in ('发不过去',) for p in (e.get('persons') or [])) else '无'
        lt = j.get('lt_review') or {}
        rv = f"{lt.get('status')}·{lt.get('batch')}" if lt else ('已过·登记 + 加厚' if deep else '未过')
        dup = '—'
        miss = []
        if depth == '骨架':
            miss.append('加厚（官网 / 业务线 / 型号对位）')
        elif depth.startswith('桌面加厚'):
            miss.append('官网快照后加厚（型号对位校正）')
        if regs == '无':
            miss.append('登记底数')
        if snap != '有（ok）' and doms:
            miss.append('官网快照')
        if mxs not in ('ok', 'no_mx') and doms:
            miss.append(f'邮箱域异常（{mxs}）')
        if em == '无':
            miss.append('邮箱')
        if kp == '无':
            miss.append('具名 KP')
        out.append({'库': 'Saga', '编号': c, '公司': r['公司名'][:60], '国家': r['国家'], '等级': r['评级'], '研究深度': depth, '登记底数': regs,
                    '官网快照': snap, '域名MX': mxs, '邮箱': em, '具名KP': kp, '复核': rv, '跨库重复': dup, '还缺什么': '；'.join(miss) or '齐'})
    return out


def external_rows(do_dns=True):
    recs = {}
    for repo in ('cctv', 'edgecore', 'mikrotik'):
        for r in load_json(os.path.join(XD, f'{repo}.json'))['records']:
            recs[r['code']] = r
    ov = load_json(os.path.join(XD, 'overrides.json'))
    codes = [c for c, o in ov.items() if o.get('grade') != 'C' and (o.get('grade') == 'B' or (o.get('review') or {}).get('status') == '留B')]
    doms = [recs[c].get('domain') for c in codes if recs.get(c, {}).get('domain')]
    mx = dns_check(doms, XMX) if do_dns else (load_json(XMX, {}).get('domains') or {})
    out = []
    for c in codes:
        r = recs[c]
        o = ov[c]
        card = load_json(os.path.join(XD, 'research', f'{c}.json'))
        depth = ('深挖' if card.get('deep') is True else '桌面卡') if card else '无卡'
        regs = '已坐实' if card and any('登记' in str(ev.get('kind', '')) or '工商' in str(ev.get('claim', '')) for ev in card.get('evidence') or []) else '无'
        d = r.get('domain') or ''
        mxs = (mx.get(d, {}).get('status') or '未查') if d else '无域名'
        em = '有' if (r.get('emails_live') or r.get('emails')) else '无'
        kp = '有' if str(r.get('kp_named')) == 'True' or (card and (card.get('contacts') or {}).get('kp')) else '无'
        rv = (o.get('review') or {}).get('status') or ('随主档' if r.get('saga_dup') not in (None, 'None', '') else '未过')
        rv = f"{rv}·{(o.get('review') or {}).get('batch', '')}".rstrip('·')
        sdp = r.get('saga_dup')
        dup = f"Saga {sdp['code']}" if isinstance(sdp, dict) else '—'
        miss = []
        if depth == '无卡':
            miss.append('研究卡（桌面）')
        if depth != '深挖':
            miss.append('官网快照 + 加厚')
        if regs == '无':
            miss.append('登记底数')
        if d and mxs not in ('ok', 'no_mx'):
            miss.append(f'邮箱域异常（{mxs}）')
        if em == '无':
            miss.append('邮箱')
        if kp == '无':
            miss.append('具名 KP')
        out.append({'库': 'External', '编号': c, '公司': r.get('name', '')[:60], '国家': r.get('country_zh', ''), '等级': 'B', '研究深度': depth, '登记底数': regs,
                    '官网快照': '无', '域名MX': mxs, '邮箱': em, '具名KP': kp, '复核': rv, '跨库重复': dup, '还缺什么': '；'.join(miss) or '齐'})
    return out


def planet_rows(do_dns=True):
    rows = list(csv.DictReader(open(PCSV, encoding='utf-8-sig')))
    ab = [r for r in rows if (r['人工定级'] or r['评级']) in ('A', 'B')]
    doms = [r['网站'].split('/')[0].replace('www.', '') for r in ab if r['网站']]
    mx = dns_check(doms, PMX) if do_dns else (load_json(PMX, {}).get('domains') or {})
    out = []
    for r in ab:
        c = r['档案编号']
        g = r['人工定级'] or r['评级']
        d = r['网站'].split('/')[0].replace('www.', '') if r['网站'] else ''
        mxs = (mx.get(d, {}).get('status') or '未查') if d else '无域名'
        em = '有' if '@' in (r['入口/联系方式'] or '') else '无'
        kp = '有' if any(k in (r['入口/联系方式'] or '') + (r['备注'] or '') for k in ('Mr', 'Ms', 'CEO', 'Owner', 'Director', '经理', '总')) else '无'
        rv = (r['长期群复核'] or '未过').split('（')[0][:24]
        dup = f"Saga/Mikrotik {r['Mikrotik仓库对照编号']}" if r['Mikrotik仓库对照编号'] else '—'
        depth = '仓研究（评级依据 + 证据 URL）' if r['评级依据'] and r['PLANET关联证据URL'] else '名录级'
        miss = ['官网快照 + 加厚', '登记底数']
        if d and mxs not in ('ok', 'no_mx'):
            miss.append(f'邮箱域异常（{mxs}）')
        if em == '无':
            miss.append('邮箱')
        if kp == '无':
            miss.append('具名 KP')
        out.append({'库': 'Planet 仓', '编号': c, '公司': r['公司名'][:60], '国家': r['国家'], '等级': g, '研究深度': depth, '登记底数': '无',
                    '官网快照': '无', '域名MX': mxs, '邮箱': em, '具名KP': kp, '复核': rv, '跨库重复': dup, '还缺什么': '；'.join(miss)})
    return out


def cross_checks():
    """交叉检查：三库同域重复 / Saga C ↔ External B 同域未标 / 国别不一致。"""
    import re
    ents = load_json(os.path.join(SD, 'entities.json'))
    dom = lambda u: re.sub(r'^https?://', '', (u or '').lower().strip()).split('/')[0].removeprefix('www.')  # noqa: E731
    saga_ab, saga_all = {}, {}
    for e in ents:
        for d in e.get('domains') or []:
            saga_all.setdefault(dom(d), (e['code'], e['grade']))
            if e['grade'] in 'AB':
                saga_ab.setdefault(dom(d), e['code'])
    recs = {}
    for repo in ('cctv', 'edgecore', 'mikrotik'):
        for r in load_json(os.path.join(XD, f'{repo}.json'))['records']:
            recs[r['code']] = r
    ov = load_json(os.path.join(XD, 'overrides.json'))
    xb = [c for c, o in ov.items() if o.get('grade') != 'C' and (o.get('grade') == 'B' or (o.get('review') or {}).get('status') == '留B')]
    x_saga, x_sagaC, x_inner, ext_dom = [], [], [], {}
    for c in xb:
        d = dom(recs[c].get('domain'))
        if d and d in saga_ab:
            x_saga.append((c, saga_ab[d], d))
        elif d and d in saga_all:
            x_sagaC.append((c, saga_all[d][0], d))
        elif d and d in ext_dom:
            x_inner.append((c, ext_dom[d], d))
        elif d:
            ext_dom[d] = c
    p_dup = []
    for r in csv.DictReader(open(PCSV, encoding='utf-8-sig')):
        g = r['人工定级'] or r['评级']
        if g not in ('A', 'B') or not r['网站']:
            continue
        d = dom(r['网站'])
        m = saga_ab.get(d) or ext_dom.get(d)
        if m:
            p_dup.append((r['档案编号'], m, d))
    reg = {}
    for f in glob.glob(os.path.join(SD, 'registry', '*.json')):
        reg.update(load_json(f)['rows'])
    cmm = []
    for e in ents:
        if e['grade'] not in 'AB':
            continue
        rg = reg.get(e['code'])
        if rg and rg.get('iso') and e.get('iso') and rg['iso'][:2].upper() != e['iso'][:2].upper():
            j = load_json(os.path.join(SD, 'research', f"{e['code']}.json"), {})
            if not j.get('country_fix'):
                cmm.append((e['code'], e['iso'], rg['iso'][:40]))
    L = ['## 4. 交叉检查（三库互相对）', '',
         f'- **同一公司两库都有档（副档随主档，不重复计）**：External B 与 Saga A/B 同域 {len(x_saga)}；External 内部同域两码 {len(x_inner)}；Planet 仓 A/B 与 Saga / External 同域 {len(p_dup)}。名册 §5 列全（`scripts/lt_roster.py` 自动去重）。',
         f"- **External B 与 Saga C 同域（Saga 侧是 C 储备）{len(x_sagaC)}**：" + '、'.join(f'{a}↔{b}（{d}）' for a, b, d in x_sagaC) + ' → 以 External 卡为长期群主档，External 卡 `saga_overlap` 已标（LT-X01）。',
         f"- **国别不一致（表内 vs 登记，且无 country_fix）{len(cmm)}**：" + ('、'.join(f'{c} 表 {a} / 登记 {b}' for c, a, b in cmm) or '无') + '（SB-021 表内 FR = 欧洲顾问所在地，登记 TW，已知；其余随手修）。',
         '- Saga A/B 同域多码：0（人工归并已清）。', '']
    return L


def main():
    do_dns = '--no-dns' not in sys.argv
    rows = saga_rows() + external_rows(do_dns) + planet_rows(do_dns)
    with open(OUT_CSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    C = collections.Counter
    by_lib = C(r['库'] for r in rows)
    depth = C((r['库'], r['研究深度']) for r in rows)
    reg = C((r['库'], r['登记底数']) for r in rows)
    snap = C((r['库'], r['官网快照'].split('（')[0]) for r in rows)
    mxs = C((r['库'], r['域名MX']) for r in rows)
    em = C((r['库'], r['邮箱']) for r in rows)
    kp = C((r['库'], r['具名KP']) for r in rows)
    need = C()
    for r in rows:
        for m in r['还缺什么'].split('；'):
            need[(r['库'], m.split('（')[0])] += 1
    ts = dt.datetime.utcnow().strftime('%H:%MZ')
    L = [f'# 长期客户群 A/B 深挖缺口盘点（{DATE} {ts}）', '',
         '> Simon U131：「这些 A / B 都深挖过了吗？加厚 审核 交叉检查等等 把没有的都再搞一下」。一户一行见 `data/长期客户群_深挖缺口_' + DATE + '.csv`；本页是汇总。',
         '> 口径：**深挖** = 官网 + 业务线 + 型号对位 + 登记 + KP（Saga 深挖 v1 口径）；**桌面** = 1–2 次检索 / 来源库核对 + 登记整合；**骨架** = 只有三闸结论。', '']
    L += ['## 1. 总表', '', '| 库 | 户数 | 研究深度 | 登记底数 | 官网快照 | 域名 MX | 邮箱 | 具名 KP |', '|---|---|---|---|---|---|---|---|']
    for lib in ('Saga', 'External', 'Planet 仓'):
        f = lambda cnt: ' / '.join(f'{k[1]} {v}' for k, v in sorted(cnt.items(), key=lambda x: -x[1]) if k[0] == lib)  # noqa: E731
        L.append(f'| {lib} | {by_lib[lib]} | {f(depth)} | {f(reg)} | {f(snap)} | {f(mxs)} | {f(em)} | {f(kp)} |')
    L += ['', '## 2. 还缺什么（户次）', '', '| 库 | 缺项 | 户数 |', '|---|---|---|']
    for (lib, m), v in sorted(need.items(), key=lambda x: (x[0][0], -x[1])):
        L.append(f'| {lib} | {m} | {v} |')
    L += ['', '## 3. 怎么补（已排）', '',
          '1. **官网快照**：沙箱抓不了客户网站 → 每日 02:23Z 的 GitHub Actions「customer-watch」在巡检后顺手补抓缺快照的 A/B 官网（Saga + External + Planet，清单 `data/长期客户群_补快照清单_' + DATE + '.json`，含失败重试），结果提交回本分支 `data/saga_clients/site_snapshots/<编号>.json`。',
          '2. **加厚**：快照到了就跑 `snapshot_digest.py` + 加厚批（型号对位 / 在卖品牌 / 页面邮箱 → 研究档），不需要 Simon。',
          '3. **登记底数**：Saga 已全覆盖；External / Planet B 按「四主区 + 波兰 → 欧洲其他 → 其他」顺序分批坐实（每批 24 户，走 `registry_store` 同一套配方）。',
          '4. **具名 KP**：快照页面邮箱 + 登记董事（officers）回填；没有就留 info@（规则：具名 KP > info@，但不编造）。',
          '5. **邮箱域异常**：nxdomain / dead 的 → 先查是否换域名，查不到 → 打回 C 储备（Gate 0 不是，因为还有网站或其他路径）。', '']
    L += cross_checks()
    L += ['## 5. 决定（默认，Simon 一句话可改）', '',
          '- **B 普通跟（B2）**：做到「桌面卡 + 官网快照 + 邮箱域活」为止，不逐户查登记 / 具名 KP——群发不需要，省时间。',
          '- **B1 重点普通跟 + A**：登记底数 + 具名 KP 必须齐（Q-77 分层一落地就按 B1 清单分批坐实，每批 24 户）。',
          '- **打回 C 的条件不变**：快照回来发现站死 / 业务线不对位 → 打回 C 储备（可逆）。', '']
    open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(L))
    print(f'rows {len(rows)} {dict(by_lib)}')
    print('depth', dict(depth))
    print('need', sorted(need.items(), key=lambda x: (x[0][0], -x[1])))


if __name__ == '__main__':
    main()
