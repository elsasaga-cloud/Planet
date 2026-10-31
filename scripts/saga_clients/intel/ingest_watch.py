#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把日跑 watch 的 intel_* 源新条目 + intel_docs 关键词命中，转成研究档 intel 条目（T29-U139 2026-10-30）。
每轮会话跑一次（本地、幂等）：
  data/customer_watch/state.json   <code>/intel_news_*（rss）→ 新闻/招标（标题 + 链接 + 日期；同一条只入一次）
                                   <code>/intel_edgar（rss）→ 年报/财务（申报类型 + 日期）；<code>/intel_ch_filings / intel_ir_* / intel_careers（html）→ 变化摘要
                                   <code>/intel_github_*（github）→ GitHub/技术足迹（新仓库 / 推送）
  data/saga_clients/intel_docs/<code>/*.hits.json → 年报/财务（采购线索：关键词窗口，去重后每文档最多 N 条）
游标 data/saga_clients/intel_ingest_state.json 记录每个源已入库的 item id / 文档 sha1。
"""
import glob
import json
import os
import re
import sys
import datetime as _dt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import intel_store as IS  # noqa: E402

ROOT = IS.ROOT
SD = os.path.join(ROOT, 'data', 'saga_clients')
STATE = os.path.join(ROOT, 'data', 'customer_watch', 'state.json')
CUR = os.path.join(SD, 'intel_ingest_state.json')
DATE = _dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%d')
MAX_NEWS = 8      # 每源每轮最多入库条数（标题含公司名优先）
MAX_HITS = 10     # 每份文档最多入库的关键词窗口


def norm_date(s):
    s = str(s or '')
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', s)
    if m:
        return m.group(0)
    try:
        from email.utils import parsedate_to_datetime
        return parsedate_to_datetime(s).strftime('%Y-%m-%d')
    except Exception:
        return s[:10]


def main():
    st = json.load(open(STATE, encoding='utf-8')) if os.path.exists(STATE) else {}
    cur = json.load(open(CUR, encoding='utf-8')) if os.path.exists(CUR) else {'sources': {}, 'docs': {}}
    ents = {e['code']: e for e in json.load(open(os.path.join(SD, 'entities.json'), encoding='utf-8'))}
    n = 0
    touched = set()
    digest = {}
    for key, v in st.items():
        if '/' not in key or not isinstance(v, dict):
            continue
        code, sid = key.split('/', 1)
        if not sid.startswith('intel_') or code not in ents:
            continue
        seen = set(cur['sources'].get(key) or [])
        rs = IS.load(code)
        if rs is None:
            continue
        name_toks = [t.lower() for t in re.findall(r'[A-Za-z\u00C0-\u024F]{4,}', str((rs.get('name_official') or ents[code].get('name') or '')))][:3]
        if v.get('kind') == 'rss':
            items = v.get('items') or {}
            new = [(iid, it) for iid, it in items.items() if iid not in seen]
            if sid.startswith('intel_news'):
                new.sort(key=lambda kv: (not any(t in (kv[1].get('title') or '').lower() for t in name_toks), kv[1].get('date') or ''), reverse=False)
                kind = '新闻/招标'
            elif sid.startswith('intel_edgar'):
                kind = '年报/财务'
            else:
                kind = '新闻/招标'
            for iid, it in new[:MAX_NEWS]:
                title = (it.get('title') or '')[:200]
                q = f"{'[SEC 申报] ' if kind == '年报/财务' else ''}{title}"
                if IS.add(code, kind, q, iid if iid.startswith('http') else (v.get('url') or ''), norm_date(it.get('date')) or DATE, f'watch 源 {sid}（日跑自动发现，标题级，未逐条核读）', 'WATCH', True, rs=rs, persist=False):
                    n += 1
                    touched.add(code)
                    digest.setdefault(code, []).append((kind, title[:120]))
                seen.add(iid)
            cur['sources'][key] = sorted(seen)[-400:]
        elif v.get('kind') == 'github':
            items = v.get('items') or {}
            new = [(iid, it) for iid, it in items.items() if iid not in seen]
            for iid, it in new[:MAX_NEWS]:
                if IS.add(code, 'GitHub/技术足迹', f"仓库 {iid}：{(it.get('title') or '')[:120]}", f'https://github.com/{iid}' if '/' in iid and not iid.startswith('http') else iid, norm_date(it.get('date')) or DATE, f'watch 源 {sid}', 'WATCH', True, rs=rs, persist=False):
                    n += 1
                    touched.add(code)
                    digest.setdefault(code, []).append(('GitHub/技术足迹', iid[:120]))
                seen.add(iid)
            cur['sources'][key] = sorted(seen)[-400:]
        else:  # html：只在有变化时记一条摘要
            lc = v.get('last_change_at') or ''
            if lc and lc != '-' and lc not in seen and (v.get('summary') or '').strip() and v.get('first_seen') != lc:
                kind = '年报/财务' if ('ch_filings' in sid or 'ir_' in sid) else ('人事变动' if 'careers' in sid else '官网变化')
                if IS.add(code, kind, f"[{sid}] 页面有更新：{(v.get('summary') or '')[:200]}", v.get('url') or '', lc[:10], 'watch 日跑检测到变化（看快照 diff 再细读）', 'WATCH', True, rs=rs, persist=False):
                    n += 1
                    touched.add(code)
                    digest.setdefault(code, []).append((kind, f"{sid} 页面更新：{(v.get('summary') or '')[:100]}"))
                seen.add(lc)
                cur['sources'][key] = sorted(seen)[-50:]
        IS.save(code, rs)
    # intel_docs 关键词命中
    for f in glob.glob(os.path.join(SD, 'intel_docs', '*', '*.hits.json')):
        h = json.load(open(f, encoding='utf-8'))
        code = h.get('code')
        if cur['docs'].get(f) == h.get('sha1'):
            continue
        if code == '*' and h.get('kw_map'):      # 展会名录：关键词 → 户
            seen_pair = set()
            for x in h.get('hits') or []:
                c2 = h['kw_map'].get(x.get('kw'))
                if not c2 or c2 not in ents or (c2, h.get('label')) in seen_pair:
                    continue
                rs2 = IS.load(c2)
                if rs2 is None:
                    continue
                ex = re.sub(r'\s+', ' ', x.get('excerpt') or '').strip()
                if IS.add(c2, '展会/活动', f"[疑似参展 · {h.get('fair') or h.get('label')}] 10times 参展商页出现「{x.get('kw')}」：…{ex[:240]}…", h.get('url') or '', (h.get('fetched_at') or DATE)[:10], '关键词命中（10times 页只渲染部分参展商；同名误报需人工看一眼再用）', 'WATCH-FAIR', True, rs=rs2, persist=False):
                    n += 1
                    touched.add(c2)
                    digest.setdefault(c2, []).append(('展会/活动', f"疑似参展 {h.get('fair')}：「{x.get('kw')}」"))
                IS.save(c2, rs2)
                seen_pair.add((c2, h.get('label')))
            cur['docs'][f] = h.get('sha1')
            continue
        if code not in ents:
            continue
        rs = IS.load(code)
        if rs is None:
            continue
        got = 0
        seen_ex = set()
        for x in h.get('hits') or []:
            ex = re.sub(r'\s+', ' ', x.get('excerpt') or '').strip()
            k = ex[:80]
            if not ex or k in seen_ex:
                continue
            seen_ex.add(k)
            if IS.add(code, '年报/财务', f"[{h.get('label')} · 关键词「{x.get('kw')}」] …{ex[:360]}…", h.get('url') or '', (h.get('fetched_at') or DATE)[:10], '采购线索（Simon 2026-10-30：年报里供应商政策 / 资本开支 / 网络设备投入也要）；运行器全文在 data/saga_clients/intel_docs/', 'WATCH-DOC', True, rs=rs, persist=False):
                n += 1
                got += 1
                touched.add(code)
                digest.setdefault(code, []).append(('年报/财务', f"{h.get('label')} 关键词「{x.get('kw')}」"))
            if got >= MAX_HITS:
                break
        IS.save(code, rs)
        cur['docs'][f] = h.get('sha1')
    json.dump(cur, open(CUR, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # 变动摘要（给 Simon 看「哪些户有新动静」）
    dp = os.path.join(ROOT, 'docs', f'A情报_变动摘要_{DATE}.md')
    L = [f'# A 类情报 · 变动摘要（{DATE}，ingest_watch 自动）\n', f'- 本次入库 {n} 条，涉及 {len(touched)} 户；来源 = 日跑 watch（新闻 RSS / 申报 / IR / 招聘页 / GitHub）+ 运行器文档（年报全文关键词、展会名录）。标题级信息未逐条核读，用前看一眼原文。\n']
    if digest:
        L.append('| 编号 | 公司 | 维度 | 新动静 |')
        L.append('|---|---|---|---|')
        for c in sorted(digest):
            for kind, t in digest[c][:12]:
                L.append(f"| {c} | {str(ents[c].get('name', ''))[:24].replace('|', '／')} | {kind} | {t.replace('|', '／')} |")
    else:
        L.append('（本次无新动静）')
    if os.path.exists(dp):
        old = open(dp, encoding='utf-8').read()
        if '## 追加' not in old:
            old += '\n'
        open(dp, 'a', encoding='utf-8').write('\n## 追加 ' + _dt.datetime.now(_dt.timezone.utc).strftime('%H:%MZ') + '\n\n' + '\n'.join(L[1:]) + '\n')
    else:
        open(dp, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('ingest_watch: items +', n, 'households', len(touched), '→', dp)


if __name__ == '__main__':
    main()
