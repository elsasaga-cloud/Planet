# -*- coding: utf-8 -*-
"""Edgecore 仓库（elsasaga-cloud/Edgecore, profile/A|B|C/*.md）→ data/external_clients/edgecore.json
只抽事实（基本事实 / 联系方式 / KP / 证据 URL / 跟进记录 / 核验摘录）；不搬信稿、SWOT、三步计划。"""
import json
import os
import re
import subprocess
import sys

import yaml

sys.path.insert(0, os.path.dirname(__file__))
from common import (DATA, EXT, GENERIC, domain_of, emails_in, iso_of, phones_in, pregrade, saga_domains, section, table_rows,
                    touch_of, urls_in)

REPO = os.path.join(EXT, 'edge')
KEY = re.compile(r'(退信|停用|bounce|MX|DNS|改用|改为|实名|LinkedIn|电话|邮箱|回复|已回|无效|失效|表单|WhatsApp|Telegram)')


def git_head():
    return subprocess.check_output(['git', '-C', REPO, 'rev-parse', '--short', 'HEAD']).decode().strip()


def git_branch():
    return subprocess.check_output(['git', '-C', REPO, 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()


def parse(path, grade_dir):
    text = open(path, encoding='utf-8').read()
    fn = os.path.basename(path)[:-3]
    m = re.match(r'([ABC]-\d{3})-(.*)-([^-]+)$', fn)
    code, fn_name, fn_country = (m.group(1), m.group(2), m.group(3)) if m else (fn[:5], fn[6:], '')
    sp = {}
    fm = re.match(r'^---\n(.*?)\n---\n', text, flags=re.S)
    if fm:
        try:
            y = yaml.safe_load(fm.group(1)) or {}
            sp = y.get('structured_profile') or y
        except Exception:
            sp = {}
    body = text[fm.end():] if fm else text
    h1 = re.search(r'^# (.+)$', body, flags=re.M)
    h1name = ''
    if h1:
        t = h1.group(1)
        if ' · ' in t:            # 「# A-001 · 公司 · 国家」
            parts = [x.strip() for x in t.split(' · ')]
            h1name = parts[1] if len(parts) >= 2 else parts[0]
        else:
            h1name = t.strip()
    name = str(sp.get('company') or sp.get('name') or h1name or fn_name).strip()
    country = str(sp.get('country') or fn_country).strip()
    quote = re.search(r'^> \*\*评级.*$', body, flags=re.M)
    city = ''
    if quote:
        mm = re.search(r'\| ([^|·]+) · ([^|]+) \|', quote.group(0))
        if mm:
            city = mm.group(2).strip()
    role_q = ''
    if quote:
        mm = re.search(r'角色：([^|]+)', quote.group(0))
        if mm:
            role_q = mm.group(1).strip()
    status_q = ''
    if quote:
        mm = re.search(r'状态：([^|]+)', quote.group(0))
        if mm:
            status_q = mm.group(1).strip()
    facts = table_rows(section(body, r'基本事实'))
    contact = section(body, r'联系方式')
    kp = section(body, r'关键人|KP')
    evid = section(body, r'调研要点|证据|来源')
    follow = table_rows(section(body, r'^##+ ?(\d+\. )?跟进记录'))
    rsec = []
    for mm in re.finditer(r'^## (R\d+[^\n]*)$', body, flags=re.M):
        start = mm.end()
        n = re.search(r'^## ', body[start:], flags=re.M)
        chunk = body[start:start + n.start() if n else len(body)]
        lines = [l.strip() for l in chunk.split('\n') if KEY.search(l) and len(l.strip()) > 6]
        if lines:
            rsec.append({'title': mm.group(1).strip(), 'lines': lines[:12]})
    # 邮箱：联系方式 + KP + 全文；停用判定
    dead = set()
    pref = set()
    for l in contact.split('\n') + [h1.group(1) if h1 else '']:
        if re.search(r'停用|退信|无效|失效|不可用|bounce', l, flags=re.I):
            dead.update(emails_in(l))
        if re.search(r'首选|\*\*邮箱\*\*', l):
            pref.update(emails_in(l))
    pref -= dead
    all_em = emails_in(contact + '\n' + kp + '\n' + '\n'.join(' | '.join(r) for r in facts) + '\n' + body)
    emails = []
    for e in all_em:
        st = '停用' if e in dead else ('首选' if e in pref else '公开')
        emails.append({'addr': e, 'status': st})
    live = [e['addr'] for e in emails if e['status'] != '停用']
    website = ''
    for l in contact.split('\n'):
        if '网站' in l or '官网' in l:
            mm = re.search(r'[（(]?((?:https?://)?(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)+(?:/[^\s）)]*)?)', l.split('：', 1)[-1], flags=re.I)
            if mm:
                website = mm.group(1)
                break
    if not website:
        for r in facts:
            mm = re.search(r'\b((?:www\.)?[a-z0-9-]+\.(?:com|net|org|io|co|eu|de|uk|fr|it|es|nl|be|ch|at|pl|cz|tr|us|ca|uz|kz|za|ae|sa|in|kr|jp|tw|hk|sg|my|th|vn|id|ph|au|nz|br|mx|ar|cl|co|pe|ru|ua|by|kg|tj|tm|ge|am|az|il|eg|ma|tn|ng|ke|tz|ug|gh|et|rw|zm|zw|mz|ao|na|bw|mu|pk|bd|lk|np|mn|ir|iq|jo|lb|om|qa|kw|bh|cy|gr|mt|ro|bg|hu|sk|si|hr|rs|ba|me|mk|al|ee|lv|lt|md|fi|se|no|dk|is|ie|pt|lu|li|biz|info|tech|digital|network|solutions|global|group|asia|africa|lat|cloud|online|shop)(?:\.[a-z]{2})?)\b', ' '.join(r), flags=re.I)
            if mm:
                website = mm.group(1)
                break
    domain = domain_of(website) or (live[0].split('@')[1] if live and live[0].split('@')[1] not in GENERIC else '')
    kp_named = bool(re.search(r'\*\*[A-ZÀ-Ž][^*]{2,60}—', kp)) or bool(re.search(r'linkedin\.com/in/', kp))
    stage = str(sp.get('stage') or '')
    rec = {
        'repo': 'Edgecore', 'src_code': code, 'src_grade': grade_dir, 'src_path': os.path.relpath(path, REPO),
        'src_stage': stage, 'src_updated': str(sp.get('updated') or ''), 'src_p1': str(sp.get('p1') or ''),
        'src_role': str(sp.get('role') or sp.get('biz_model') or ''), 'src_segment': str(sp.get('segment') or ''),
        'src_needs': sp.get('needs') if isinstance(sp.get('needs'), list) else ([str(sp['needs'])] if sp.get('needs') else []),
        'src_risk': sp.get('risk_flags') if isinstance(sp.get('risk_flags'), list) else [],
        'src_volume': str(sp.get('volume_potential') or ''),
        'name': name, 'country_zh': country, 'iso': iso_of(country), 'city': city, 'website': website, 'domain': domain,
        'type': role_q or str(sp.get('role') or sp.get('biz_model') or 'SI/VAR（Edgecore where-to-buy）'),
        'src_status': status_q,
        'facts': facts, 'contact_text': contact, 'kp_text': kp, 'evidence_text': evid, 'evidence_urls': urls_in(evid + '\n' + '\n'.join(' | '.join(r) for r in facts)),
        'followups': follow, 'r_notes': rsec,
        'emails': emails, 'emails_live': live, 'phones': phones_in(contact), 'kp_named': kp_named,
        'stage': stage, 'flags': [],
    }
    if dead:
        rec['flags'].append('有停用地址')
    if not live:
        rec['flags'].append('无可用邮箱')
    return rec


def main():
    head, branch = git_head(), git_branch()
    recs = []
    for g in 'ABC':
        d = os.path.join(REPO, 'profile', g)
        for fn in sorted(os.listdir(d)):
            if fn.endswith('.md') and re.match(r'[ABC]-\d{3}-', fn):
                recs.append(parse(os.path.join(d, fn), g))
    sd = saga_domains()
    seen_dom = {}
    for r in recs:
        r['src_repo_ref'] = f'elsasaga-cloud/Edgecore@{head} ({branch})'
        doms = {r['domain']} | {e['addr'].split('@')[1] for e in r['emails']}
        doms = {d for d in doms if d and d not in GENERIC}
        r['saga_dup'] = None
        for d in sorted(doms):
            if d in sd:
                r['saga_dup'] = {'code': sd[d][0], 'grade': sd[d][1], 'via': d}
                break
        r['repo_dup'] = None
        for d in sorted(doms):
            if d in seen_dom and seen_dom[d] != r['src_code']:
                r['repo_dup'] = seen_dom[d]
                r['flags'].append('库内重复')
                break
        for d in doms:
            seen_dom.setdefault(d, r['src_code'])
        r['touch'] = touch_of([e['addr'] for e in r['emails']])
        if r['touch']:
            r['flags'].append('S箱已群发')
        g, why, fl = pregrade(r)
        if r['src_grade'] == 'C' and g in ('A', 'B'):
            g, why, fl = 'C', '来源库（Edgecore）已判 C：' + (r['type'] or '见原档') + '；沿用，待研究再定', fl + ['来源C']
        r['grade'], r['grade_reason'], r['flags'] = g, why, sorted(set(fl))
    # 编号：按初判等级分别从 001 起，顺序 = 原编号顺序
    cnt = {'A': 0, 'B': 0, 'C': 0}
    for r in recs:
        if r['grade'] == 'DELETE':
            r['code'] = ''
            continue
        cnt[r['grade']] += 1
        r['code'] = f"X{r['grade']}-E{cnt[r['grade']]:03d}"
    os.makedirs(DATA, exist_ok=True)
    out = {'repo': 'Edgecore', 'src': f'elsasaga-cloud/Edgecore@{head}', 'branch': branch, 'count': len(recs), 'records': recs}
    json.dump(out, open(os.path.join(DATA, 'edgecore.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    from collections import Counter
    print('edge', len(recs), Counter(r['grade'] for r in recs), 'dupSaga', sum(1 for r in recs if r['saga_dup']),
          'touch', sum(1 for r in recs if r['touch']), 'noemail', sum(1 for r in recs if not r['emails_live']))


if __name__ == '__main__':
    main()
