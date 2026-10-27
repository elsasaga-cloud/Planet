# -*- coding: utf-8 -*-
"""mikrotik-info 仓库（elsasaga-cloud/mikrotik-info：客户名单_反向信号_2026-09.csv + profile/A|B|C/*.md）→ data/external_clients/mikrotik.json
A/B 正常初判；C 285 家（Simon：mik 的 C 不碰）2026-10-27 关仓前一并进库但一律 XC 存档（追加在 A/B 之后，原编号不动）。
另：根目录策略文档（重点客户深度分析 / 12 家作战卡 / 三家首发邮件）里点名、却从未写进 CSV 的自有品牌 OEM 目标，作 DOC-xx 追加。
只抽事实：CSV 22 列 + 基本事实 / 联系方式 / KP 表 / 跟进记录 / 退信与核验摘录。"""
import csv
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import (DATA, EXT, GENERIC, domain_of, emails_in, iso_of, name_known, norm_key, phones_in, pregrade, saga_domains,
                    section, table_rows, touch_of, urls_in)

REPO = os.path.join(EXT, 'mik')
CSV = os.path.join(REPO, '客户名单_反向信号_2026-09.csv')
KEY = re.compile(r'(退信|停用|bounce|无效|失效|已回|回复|样品|sample|冻结|frozen|改用|改为)', re.I)


def git(args):
    try:
        return subprocess.check_output(['git', '-C', REPO] + args, stderr=subprocess.DEVNULL).decode().strip()
    except Exception:                      # 仓库已私有/只剩 data/external_repos/archive 解包的文本树
        return {'HEAD': 'a60f11f8(archive)'}.get(args[-1], 'arena/01a0c3ef-mikrotik-info(archive)')


# ---- 根目录策略文档点名、CSV 里没有的自有品牌 / OEM 目标（2026-10-27 关仓前清点补入；事实均摘自所列文件）----
DOC1 = '重点客户深度分析与中性货打法_2026-09.md'
DOC2 = 'A类客户12家作战卡与开发信_2026-09.md'
DOC_EXTRAS = [
    # name, country_zh, city, website, type, emails, kp(list of (name,title)), facts(list of (k,v)), src files/sections
    ('Digital Data Communications GmbH', '德国', 'Dortmund', 'level1.com', '自有品牌商（LevelOne / equip / Conceptronic）· OEM 目标', [],
     [('Amanda Chen', 'Group CEO（LinkedIn 活跃）')],
     [('成立', '1991（批发起家 → 全球网络方案供应商）'), ('总部', 'Dortmund，德国；物流中心 Soest'), ('品牌', 'LevelOne / equip / Conceptronic / ABBRAZZIO'),
      ('来源库判断', 'PoE 线最强但停在 web-smart；已在中国生产，采购逻辑现成；决策链最短（Group CEO 在社交媒体）'),
      ('来源库风险', '他们自己有 ODM 服务，可能对我方是竞争'), ('来源库提醒', 'Amanda Chen 是 Group CEO，不要直接推销；先在帖子下做技术评论再转产品负责人')],
     f'{DOC1} §1②；{DOC2} #1'),
    ('2direct GmbH', '德国', 'Schalksmühle', '2direct.de', '自有品牌商（LogiLink / LogiLight）· OEM 目标', [],
     [('Wilfried Grohnert', 'Geschäftsführer'), ('Jan Alberts', 'Geschäftsführer')],
     [('地址', 'Langenstück 5, D-58579 Schalksmühle'), ('成立', '2001（Lüdenscheid）'), ('品牌', 'LogiLink / LogiLight'),
      ('来源库判断', '官网公开说做 OEM 项目；两位 Geschäftsführer 是中小企业老板，小公司里老板就是采购，可直接写但要短（5 行以内）'),
      ('来源库风险', '价格敏感，需给阶梯')],
     f'{DOC1} §1③；{DOC2} #2；三家首发邮件与反向信号客户名单_2026-09.md A2（德文首发邮件已写好）'),
    ('Intos Electronic AG', '德国', 'Gießen', 'inline-info.com', '自有品牌商（InLine）· OEM 目标', [],
     [('Wolfgang Isenberg', 'Vorstandsvorsitzender（董事长）')],
     [('地址', 'Siemensstraße 11, 35394 Gießen'), ('成立', '1991'), ('规模', '80+ 员工；自有品牌 InLine 约 5,000 SKU（总 8,000+）；95% 现货率；6 个德国销售办公室 + 1 个意大利'),
      ('来源库判断', '第二梯队代表：名声没那么大、决策快；24 口 PoE 440W 直接对标')],
     f'{DOC1} §1⑥、§2；三家首发邮件与反向信号客户名单_2026-09.md A3（德文首发邮件已写好）'),
    ('Deltaco AB', '瑞典', 'Ludvika', 'deltaco.se', '自有品牌商（北欧 IT 配件与网络产品）· OEM 目标', [], [],
     [('定位', '北欧自有品牌 IT 配件与网络产品；1991 年创立于 Ludvika，早期从台湾进口线缆'),
      ('现状', '自有产品占比持续提升；产品线含 switches、转换器、光纤、网络产品；隶属 DistIT AB（纳斯达克斯德哥尔摩），2022 年与 Aurora Group 合并为 Aurdel'),
      ('缺口', '北欧零售端以消费/SOHO 为主；可管理 PoE 与工业线薄弱'), ('来源库风险', '集团合并期，决策链变化')],
     f'{DOC2} #7'),
    ('StarTech.com', '加拿大', 'Toronto', 'startech.com', '自有品牌商（北美配件/连接）· OEM 目标', [], [],
     [('定位', '北美配件/连接自有品牌巨头'),
      ('现有工业交换机', 'IES61002POE（6 口，4×PoE+，DIN，-40~75°C，US$347）、IES81000PoE（8 口工业 PoE，TAA）、IESC1G50UP、IES1G52UPDIN、IES5102 —— 全部是非管理型'),
      ('售后', '2 年质保 + 终身免费技术支持'), ('缺口', '没有可管理型工业交换机，没有 PoE++，没有环网'),
      ('来源库提醒', 'TAA 合规型号中国原产拿不到 → 只做商用渠道；加拿大 CASL 严格 → 不要发冷邮件，走 LinkedIn + 电话 + 官网供应商入口')],
     f'{DOC2} #8'),
    ('Intelbras S.A.', '巴西', 'São José (SC)', 'intelbras.com', '安防/网络品牌商 · 接入层 + SKD/CKD 目标', [],
     [('Amilcar Scheffer', 'diretor de soluções e produtos de redes'), ('Elton Thiesen', 'gerente de segmento enterprise')],
     [('定位', '巴西安防/网络巨头，近年强势切入企业级'), ('关键事实', '与 H3C 战略合作，做本地化生产（tropicalização）'),
      ('现有交换机', 'SG 5204 MR L2+（48G+4×SFP）、S3028G-PB Max（L3，24G PoE + 4×SFP+，380W）、SG 2404 PoE L2+、SF800Q+'),
      ('缺口', 'H3C 覆盖企业核心/汇聚；接入层低价位、PoE++、工业宽温仍有空间；本地化生产需 SKD/CKD 方案'),
      ('来源库提醒', '葡萄牙语沟通；巴西认证（ANATEL / INMETRO）需提前确认')],
     f'{DOC2} #9'),
    ('Wentronic GmbH', '德国', 'Braunschweig', 'wentronic.com', '自有品牌商（goobay）· 配件/线材/电源', ['cs@wentronic.com'], [],
     [('地址', 'Pillmannstraße 12, 38112 Braunschweig'), ('成立', '1999'), ('来源库切入', '从 PoE 交换机/注入器补线')],
     f'{DOC1} §2'),
    ('Tragant Handels- und Beteiligungs GmbH', '德国', 'Berlin', 'delock.de', '自有品牌商（Delock）· 网络/接口', [], [],
     [('来源库切入', '小批量试单'), ('品牌', 'Delock')],
     f'{DOC1} §2'),
    ('Hama GmbH & Co KG', '德国', 'Monheim', 'hama.com', '消费电子自有品牌（体量大但品类浅）', [], [],
     [('来源库切入', '8/16 口 PoE 入门款')],
     f'{DOC1} §2（与 Vivanco / Schwaiger 并列）'),
    ('Vivanco GmbH', '德国', 'Ahrensburg', 'vivanco.de', '消费电子自有品牌（体量大但品类浅）', [], [],
     [('来源库切入', '8/16 口 PoE 入门款')],
     f'{DOC1} §2（与 Hama / Schwaiger 并列）'),
]


def doc_extras(known_keys):
    out = []
    for name, country, city, website, typ, mails, kp, facts, src in DOC_EXTRAS:
        if name_known(name, known_keys):
            continue
        known_keys.add(norm_key(name))
        emails = [{'addr': e, 'status': '公开'} for e in mails]
        out.append({
            'repo': 'mikrotik-info', 'src_code': f'DOC-{len(out) + 1:02d}', 'src_grade': '-', 'src_path': src.split('；')[0].split(' §')[0].split(' #')[0],
            'src_csv': '', 'src_stage': '', 'src_updated': '2026-09', 'src_p1': '', 'src_status': '', 'src_priority': '', 'src_source': src,
            'src_note': '仅见于根目录策略文档，来源库从未写进 CSV / 建档', 'src_rating_basis': '', 'src_manual': '', 'src_biz_org': '', 'src_business_model': '',
            'name': name, 'country_zh': country, 'iso': iso_of(country), 'city': city, 'website': website, 'domain': domain_of(website),
            'type': typ, 'signals': '', 'own_brand': '是', 'entry_point': next((v for k, v in facts if k == '来源库切入'), ''), 'entry_contact': '',
            'facts': [list(f) for f in facts] + [['网站', website + '（Agent 常识补写，待核）']],
            'contact_text': '', 'kp': [{'name': n, 'role': t, 'contact': '', 'status': '待核', 'source': src, 'guess': False} for n, t in kp], 'followups': [], 'r_notes': [], 'evidence_urls': [],
            'emails': emails, 'emails_live': [e['addr'] for e in emails], 'phones': [], 'kp_named': bool(kp), 'stage': '',
            'flags': ['来源库未入 CSV（策略文档点名）', 'OEM品牌商', '域名待核'] + ([] if mails else ['无可用邮箱']),
        })
    return out


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
    for g in 'ABC':
        d = os.path.join(REPO, 'profile', g)
        for fn in sorted(os.listdir(d)):
            m = re.match(r'([ABC]-\d{3})-', fn)
            if m and fn.endswith('.md'):
                prof[m.group(1)] = (g, os.path.join(d, fn))
    rows = list(csv.DictReader(open(CSV, encoding='utf-8-sig')))
    # A/B 先（顺序 = CSV 顺序，原编号不动），C 285 追加在后
    rows = [r for r in rows if (r.get('档案编号') or '')[:1] in 'AB'] + [r for r in rows if (r.get('档案编号') or '')[:1] == 'C']
    recs = []
    for r in rows:
        code = (r.get('档案编号') or '').strip()
        if not code or code[0] not in 'ABC':
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
            'c_sub': (r.get('C级细分') or '').strip(),
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
    known = {norm_key(x['name']) for x in recs if norm_key(x['name'])}
    extras = doc_extras(known)
    recs.extend(extras)
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
        if r['src_grade'] == 'C' and g in ('A', 'B'):
            g, why, fl = 'C', (f"来源库（mikrotik-info）已判 C（细分：{r.get('c_sub') or '—'}；依据：{(r.get('src_rating_basis') or '')[:60]}）；"
                               'Simon 口径「mik 的 C 不碰」→ 关仓前仅存档，不跟'), fl + ['来源C']
        if r['src_grade'] == '-' and g in ('A', 'B'):
            why = why + '；来源库策略文档点名的自有品牌 / OEM 目标（Saga 目标顺位第一类），未建档，资料待核'
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
    print('srcC', sum(1 for r in recs if r['src_grade'] == 'C'), 'doc_extras', [(r['code'], r['name']) for r in extras])


if __name__ == '__main__':
    main()
