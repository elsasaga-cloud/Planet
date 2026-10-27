# -*- coding: utf-8 -*-
"""mikrotik-info 仓库（elsasaga-cloud/mikrotik-info：客户名单_反向信号_2026-09.csv + profile/A|B/*.md）→ data/external_clients/mikrotik.json
只取 A/B（Simon：C 不要）。只抽事实：CSV 22 列 + 基本事实 / 联系方式 / KP 表 / 跟进记录 / 退信与核验摘录。"""
import csv
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import (DATA, EXT, GENERIC, domain_of, emails_in, iso_of, phones_in, pregrade, saga_domains, section, table_rows,
                    touch_of, urls_in)

REPO = os.path.join(EXT, 'mik')
CSV = os.path.join(REPO, '客户名单_反向信号_2026-09.csv')
KEY = re.compile(r'(退信|停用|bounce|无效|失效|已回|回复|样品|sample|冻结|frozen|改用|改为)', re.I)


def git(args):
    return subprocess.check_output(['git', '-C', REPO] + args).decode().strip()


def parse_profile(path):
    text = open(path, encoding='utf-8').read()
    sp = {}
    m = re.search(r'```yaml structured_profile\n(.*?)```', text, flags=re.S)
    if m:
        for l in m.group(1).split('\n'):
            mm = re.match(r'^(\w+):\s*(.*?)\s*(#.*)?$', l)
            if mm:
                sp[mm.group(1)] = mm.group(2).strip()
    quote = re.search(r'^> \*\*评级.*$', text, flags=re.M)
    status_q = ''
    if quote:
        mm = re.search(r'状态：(.+)$', quote.group(0))
        if mm:
            status_q = mm.group(1).strip()
    facts = table_rows(section(text, r'基本事实'))
    contact = section(text, r'^##+ 联系方式')
    kp_block = section(text, r'关键人（KP）')
    kp_rows = [r for r in table_rows(kp_block) if r and r[0] not in ('姓名',)]
    kp = []
    for r in kp_rows:
        if len(r) >= 3:
            nm = r[0].strip()
            guess = nm.startswith(('—', '（', '(')) or '猜测' in nm or '待查' in nm
            kp.append({'name': nm, 'role': r[1], 'contact': r[2], 'status': r[3] if len(r) > 3 else '', 'source': r[4] if len(r) > 4 else '', 'guess': guess})
    follow = table_rows(section(text, r'^##+ 跟进记录'))
    notes = []
    for mm in re.finditer(r'^## (R(?:6[0-9]|7[0-9])[^\n]*)$', text, flags=re.M):
        start = mm.end()
        n = re.search(r'^## ', text[start:], flags=re.M)
        chunk = text[start:start + n.start() if n else len(text)]
        lines = [l.strip() for l in chunk.split('\n') if KEY.search(l) and len(l.strip()) > 6 and '不补造' not in l and '未逐户' not in l]
        lines = [l for l in lines if not l.startswith('- **地址级范围**') and '未为本户' not in l and '可继续跟进不等于' not in l and '未将用户报告' not in l]
        if lines:
            notes.append({'title': mm.group(1).strip(), 'lines': lines[:10]})
    dead = set()
    for l in (contact + '\n' + '\n'.join(' | '.join(r) for r in follow) + '\n' + '\n'.join(x for n in notes for x in n['lines'])).split('\n'):
        if re.search(r'退信|停用|无效|失效|不可用|bounce|hard', l, flags=re.I) and not re.search(r'未为本户|无退信|未见退信', l):
            dead.update(emails_in(l))
    pref = set()
    for l in contact.split('\n'):
        if l.startswith('- **邮箱**'):
            pref.update(emails_in(l))
    # 具名 KP 通道里的邮箱也算（排除模式猜测）
    all_em = emails_in(contact + '\n' + kp_block + '\n' + '\n'.join(' | '.join(r) for r in facts))
    all_em = [e for e in all_em if not e.startswith(('firstname', 'first.last', 'name@'))]
    emails = [{'addr': e, 'status': ('停用' if e in dead else ('首选' if e in pref else '公开'))} for e in all_em]
    website = ''
    for r in facts:
        if r and r[0].startswith('网站') and len(r) > 1:
            website = r[1]
            break
    return {
        'sp': sp, 'src_status': status_q, 'facts': facts, 'contact_text': contact, 'kp': kp, 'kp_text': kp_block,
        'followups': follow, 'r_notes': notes, 'emails': emails, 'phones': phones_in(contact), 'website_profile': website,
        'evidence_urls': urls_in(kp_block + '\n' + '\n'.join(' | '.join(r) for r in facts)),
    }


def main():
    head, branch = git(['rev-parse', '--short', 'HEAD']), git(['rev-parse', '--abbrev-ref', 'HEAD'])
    prof = {}
    for g in 'AB':
        d = os.path.join(REPO, 'profile', g)
        for fn in sorted(os.listdir(d)):
            m = re.match(r'([AB]-\d{3})-', fn)
            if m and fn.endswith('.md'):
                prof[m.group(1)] = (g, os.path.join(d, fn))
    rows = list(csv.DictReader(open(CSV, encoding='utf-8-sig')))
    recs = []
    for r in rows:
        code = (r.get('档案编号') or '').strip()
        if not code or code[0] not in 'AB':
            continue
        g, path = prof.get(code, (code[0], None))
        p = parse_profile(path) if path else None
        name = r['公司名'].strip()
        website = (r.get('网站') or '').strip() or (p['website_profile'] if p else '')
        emails = p['emails'] if p else []
        for e in emails_in((r.get('入口/联系方式') or '') + '\n' + (r.get('备注') or '') + '\n' + (r.get('评级依据') or '')):
            if e not in [x['addr'] for x in emails] and not e.startswith(('firstname', 'first.last', 'name@')):
                emails.append({'addr': e, 'status': '公开'})
        live = [e['addr'] for e in emails if e['status'] != '停用']
        domain = domain_of(website) or (live[0].split('@')[1] if live and live[0].split('@')[1] not in GENERIC else '')
        kp_named = any(not k['guess'] for k in (p['kp'] if p else []))
        stage = (p['sp'].get('stage') if p else '') or (r.get('状态') or '')
        rec = {
            'repo': 'mikrotik-info', 'src_code': code, 'src_grade': g, 'src_path': os.path.relpath(path, REPO) if path else '',
            'src_csv': '客户名单_反向信号_2026-09.csv', 'src_stage': stage, 'src_updated': (p['sp'].get('updated') if p else ''),
            'src_p1': (p['sp'].get('p1') if p else '') or (r.get('首推Saga型号') or ''), 'src_status': p['src_status'] if p else '',
            'src_priority': r.get('优先级', ''), 'src_source': r.get('来源', ''), 'src_note': r.get('备注', ''),
            'src_rating_basis': r.get('评级依据', ''), 'src_manual': r.get('人工定级', ''), 'src_biz_org': (p['sp'].get('biz_org') if p else ''),
            'src_business_model': (p['sp'].get('business_model') if p else ''),
            'name': name, 'country_zh': r['国家'].strip(), 'iso': iso_of(r['国家']), 'city': (r.get('城市') or '').strip(),
            'website': website, 'domain': domain, 'type': (r.get('类型') or '').strip(), 'signals': (r.get('信号（在卖什么品牌）') or '').strip(),
            'own_brand': (r.get('是否自有品牌') or '').strip(), 'entry_point': (r.get('切入点') or '').strip(),
            'entry_contact': (r.get('入口/联系方式') or '').strip(),
            'facts': p['facts'] if p else [], 'contact_text': p['contact_text'] if p else '', 'kp': p['kp'] if p else [],
            'followups': p['followups'] if p else [], 'r_notes': p['r_notes'] if p else [], 'evidence_urls': p['evidence_urls'] if p else [],
            'emails': emails, 'emails_live': live, 'phones': p['phones'] if p else phones_in(r.get('入口/联系方式') or ''),
            'kp_named': kp_named, 'stage': stage, 'flags': [],
        }
        if any(e['status'] == '停用' for e in emails):
            rec['flags'].append('有停用地址')
        if not live:
            rec['flags'].append('无可用邮箱')
        if not path:
            rec['flags'].append('无档案文件')
        recs.append(rec)
    sd = saga_domains()
    seen = {}
    for r in recs:
        r['src_repo_ref'] = f'elsasaga-cloud/mikrotik-info@{head} ({branch})'
        doms = {r['domain']} | {e['addr'].split('@')[1] for e in r['emails']}
        doms = {d for d in doms if d and d not in GENERIC}
        r['saga_dup'] = None
        for d in sorted(doms):
            if d in sd:
                r['saga_dup'] = {'code': sd[d][0], 'grade': sd[d][1], 'via': d}
                break
        r['repo_dup'] = None
        for d in sorted(doms):
            if d in seen and seen[d] != r['src_code']:
                r['repo_dup'] = seen[d]
                r['flags'].append('库内重复')
                break
        for d in doms:
            seen.setdefault(d, r['src_code'])
        r['touch'] = touch_of([e['addr'] for e in r['emails']])
        if r['touch']:
            r['flags'].append('S箱已群发')
            if r['touch']['来信'] not in ('', '0'):
                r['flags'].append('S箱有来信')
        g, why, fl = pregrade(r)
        r['grade'], r['grade_reason'], r['flags'] = g, why, sorted(set(fl))
    cnt = {'A': 0, 'B': 0, 'C': 0}
    for r in recs:
        if r['grade'] == 'DELETE':
            r['code'] = ''
            continue
        cnt[r['grade']] += 1
        r['code'] = f"X{r['grade']}-M{cnt[r['grade']]:03d}"
    os.makedirs(DATA, exist_ok=True)
    out = {'repo': 'mikrotik-info', 'src': f'elsasaga-cloud/mikrotik-info@{head}', 'branch': branch, 'count': len(recs), 'records': recs}
    json.dump(out, open(os.path.join(DATA, 'mikrotik.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    from collections import Counter
    print('mik', len(recs), Counter(r['grade'] for r in recs), 'dupSaga', sum(1 for r in recs if r['saga_dup']),
          'touch', sum(1 for r in recs if r['touch']), 'noemail', sum(1 for r in recs if not r['emails_live']),
          'noprofile', sum(1 for r in recs if '无档案文件' in r['flags']))
    print(Counter(r['grade_reason'][:28] for r in recs).most_common(14))


if __name__ == '__main__':
    main()
