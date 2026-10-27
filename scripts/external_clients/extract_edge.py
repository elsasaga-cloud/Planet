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
from common import (DATA, EXT, GENERIC, domain_of, emails_in, iso_of, name_known, norm_key, phones_in, pregrade, saga_domains,
                    section, table_rows, touch_of, urls_in)

REPO = os.path.join(EXT, 'edge')
KEY = re.compile(r'(退信|停用|bounce|MX|DNS|改用|改为|实名|LinkedIn|电话|邮箱|回复|已回|无效|失效|表单|WhatsApp|Telegram)')


def git_head():
    try:
        return subprocess.check_output(['git', '-C', REPO, 'rev-parse', '--short', 'HEAD'], stderr=subprocess.DEVNULL).decode().strip()
    except Exception:                      # 仓库已私有/只剩 data/external_repos/archive 解包的文本树
        return '729187d(archive)'


def git_branch():
    try:
        return subprocess.check_output(['git', '-C', REPO, 'rev-parse', '--abbrev-ref', 'HEAD'], stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return 'arena/6214ebb8-edgecore(archive)'


def deleted_ledger():
    """来源库 2026-10-19 R16/R17 终局删除的档案：名字 → (旧编号, 理由)。
    名单取 profile/00-编号对照表.md 的「已删除」段，理由取 docs/audit/R16-B类待删记录.md / R17-C类待删记录.md。"""
    out = {}
    fn = os.path.join(REPO, 'profile', '00-编号对照表.md')
    if not os.path.exists(fn):
        return out
    txt = open(fn, encoding='utf-8').read()
    for m in re.finditer(r'### 已删除.*?(?=\n## |\Z)', txt, flags=re.S):
        for code, nm in re.findall(r'([BC]-\d{3}) ([^（）、\n]+?)（', m.group(0)):
            out[norm_key(nm)] = (code, nm.strip(), '')
    for led in ('R16-B类待删记录.md', 'R17-C类待删记录.md'):
        f2 = os.path.join(REPO, 'docs', 'audit', led)
        if not os.path.exists(f2):
            continue
        for line in open(f2, encoding='utf-8'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) >= 3 and re.match(r'[BC]-\d{3}$', cells[0]):
                nm = re.sub(r'（.*?）', '', cells[1]).strip()
                why = cells[-1]
                for k, v in list(out.items()):
                    if v[0] == cells[0]:
                        out[k] = (v[0], v[1], why)
                out.setdefault(norm_key(nm), (cells[0], nm, why))
    # 宪法 #28 里只写了编号没写名字 / 名字缩写的几家，手工对上（依据：宪法-对话记录.md #27–#28、R15 批 5 审计）
    for nm, code, why in (('Xentech B.V.', 'A-018→B-135', 'KvK 登记 2020-08-04 已注销（Opgeheven），官网仍在线'),
                          ('Active Solution', 'A-013→B-134', '工商登记 in Liquidazione 清算中'),
                          ('Ravi and Singh Communication', 'A-062', '登记 LLP 已除名、签约主体混乱'),
                          ('Algorithmic Digital Solutions Inc.', 'A-034', '官网为软件开发代理商、无硬件货架证据')):
        out.setdefault(norm_key(nm), (code, nm, why))
    # A 类删档只记在宪法对话记录 / R15 审计里（「删档执行」「直接删档」行）
    f3 = os.path.join(REPO, '宪法-对话记录.md')
    if os.path.exists(f3):
        for line in open(f3, encoding='utf-8'):
            if not re.search(r'删档|删除执行|直接删', line):
                continue
            for code, nm, why in re.findall(r'([ABC]-\d{3}) ([^（）、\n]+?)（([^（）]*)）', line):
                out.setdefault(norm_key(nm), (code, nm.strip(), why.strip()))
    return out


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


# ---- 只在《Edgecore客户数据库.xlsx》里、没建 profile 的名字（2026-10-27 关仓前清点补入） ----
# xlsx 已原样复制到 docs/reference/external/Edgecore/，各 sheet 转 CSV 存 data/external_repos/edgecore_xlsx/（提取只读 CSV，不依赖 openpyxl）
XLSX_DIR = os.path.join(os.path.dirname(DATA), 'external_repos', 'edgecore_xlsx')
# 域名为 Agent 依常识补写（xlsx 本身无网站列），一律标「待核」
XLSX_DOMAIN = {'ASI': 'asipartner.com', 'Avnet': 'avnet.com', 'Tech Data': 'techdata.com', 'AMAX': 'amax.com', 'ePLUS': 'eplus.com',
               'GDT': 'gdt.com', 'KGPCo': 'kgpco.com', 'SHI': 'shi.com', 'WWT': 'wwt.com', 'CDW': 'cdw.com', 'LINX（伦敦互联网交换中心）': 'linx.net',
               'UTSA（德州大学圣安东尼奥）': 'utsa.edu', 'NETAS': 'netas.com.tr', 'Indio Networks': 'indionetworks.com',
               'Dojo Networks': 'dojonetworks.com', 'ASBIS（塞浦路斯/波兰/中东）': 'asbis.com', 'NCTU（台湾交通大学）': 'nycu.edu.tw'}
# 美国超大 VAR / 分销（xlsx 渠道伙伴库里有、BIG_GROUP 正则没覆盖的）：按 Saga 守界直接 C
XLSX_BIG = re.compile(r'^(ASI|AMAX|ePLUS|GDT|KGPCo|SHI|WWT)$', re.I)
END_USER = re.compile(r'教育|科研|IXP|大学|运营商|ISP/MDU|政府|城市|互联网企业|实验室|AI |测试|IDC|电信|基础设施')


def xlsx_extras(known_keys):
    out = []
    if not os.path.isdir(XLSX_DIR):
        return out
    import csv
    sheets = [('渠道伙伴库', 3, 2, [('渠道类型', 4), ('地址', 5), ('电话', 6), ('来源页', 7), ('采集时间', 8)]),
              ('案例客户库', 1, 2, [('行业/类型', 3), ('项目/用途', 4), ('涉及产品/方案', 5), ('来源', 6), ('采集时间', 7)]),
              ('目标客户评估', 1, 2, [('我方目标类型', 3), ('匹配理由', 4), ('切入点建议', 5), ('优先级(1最高)', 6), ('跟进状态', 7)])]
    for sheet, ci, cc, cols in sheets:
        fn = os.path.join(XLSX_DIR, sheet + '.csv')
        if not os.path.exists(fn):
            continue
        rows = list(csv.reader(open(fn, encoding='utf-8-sig')))
        for r in rows[1:]:
            if len(r) <= ci or not r[ci].strip():
                continue
            name = r[ci].strip()
            if not norm_key(name) or name.startswith(('（', '(')):      # 占位行，如「（官网拉丁美洲名录当前无收录条目）」
                continue
            if name_known(name, known_keys):
                continue
            known_keys.add(norm_key(name))
            country = r[cc].strip()
            facts = [(c, r[i].strip()) for c, i in cols if len(r) > i and r[i].strip()]
            typ = next((v for c, v in facts if c in ('渠道类型', '行业/类型', '我方目标类型')), '')
            phones = phones_in(next((v for c, v in facts if c == '电话'), ''))
            dom = XLSX_DOMAIN.get(name, '')
            rec = {
                'repo': 'Edgecore', 'src_code': f'XLSX-{sheet}#{r[0].strip()}', 'src_grade': '-', 'src_path': 'Edgecore客户数据库.xlsx',
                'src_stage': '', 'src_updated': next((v for c, v in facts if c == '采集时间'), ''), 'src_p1': '', 'src_role': typ,
                'src_segment': sheet, 'src_needs': [], 'src_risk': [], 'src_volume': '',
                'name': re.sub(r'[（(].*?[)）]', '', name).strip() or name, 'country_zh': country, 'iso': iso_of(country.split('/')[0]), 'city': '',
                'website': dom, 'domain': dom, 'type': typ or sheet, 'src_status': '',
                'facts': facts + ([('域名', dom + '（Agent 常识补写，待核）')] if dom else []), 'contact_text': '', 'kp_text': '', 'evidence_text': '',
                'evidence_urls': [], 'followups': [], 'r_notes': [], 'emails': [], 'emails_live': [], 'phones': phones, 'kp_named': False,
                'stage': '', 'flags': ['来源库未建档（仅在 xlsx）', '无可用邮箱'],
            }
            if dom:
                rec['flags'].append('域名待核')
            out.append(rec)
    return out


def main():
    head, branch = git_head(), git_branch()
    recs = []
    for g in 'ABC':
        d = os.path.join(REPO, 'profile', g)
        for fn in sorted(os.listdir(d)):
            if fn.endswith('.md') and re.match(r'[ABC]-\d{3}-', fn):
                recs.append(parse(os.path.join(d, fn), g))
    known = {norm_key(r['name']) for r in recs if norm_key(r['name'])}
    extras = xlsx_extras(known)
    deleted = deleted_ledger()
    for r in extras:
        k = norm_key(r['name'])
        hit = deleted.get(k) or next((v for kk, v in deleted.items() if len(k) > 5 and (k in kk or kk in k)), None)
        if hit:
            r['src_deleted'] = {'old_code': hit[0], 'name': hit[1], 'why': hit[2]}
            r['flags'].append('来源库终局已删')
    recs.extend(extras)                      # 追加在末尾：原有编号不动
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
        if r['src_grade'] == '-' and g in ('A', 'B'):
            if r.get('src_deleted'):
                d = r['src_deleted']
                g, why, fl = 'C', (f"来源库 2026-10-19 R16/R17 终局已删（旧 {d['old_code']}）：{d['why'] or '理由见其待删台账'}；"
                                   '按方案 §7 已删档案不复活，仅存档备查'), fl + ['来源库已删']
            elif XLSX_BIG.match(r['name']):
                g, why, fl = 'C', '美国超大 VAR / 分销（Saga 守界：大集团搞不定）；只在来源库 xlsx 里出现，未建档', fl + ['大集团']
            elif END_USER.search(r['type']):
                g, why, fl = 'C', '终端用户 / 运营商案例（Edgecore 官方案例页），不是渠道买家；仅存档', fl + ['终端触点']
            else:
                why = why + '；只在来源库 xlsx 里出现（未建档），资料极少，待研究'
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
          'touch', sum(1 for r in recs if r['touch']), 'noemail', sum(1 for r in recs if not r['emails_live']),
          'xlsx_extras', len(extras), [(r['code'], r['name']) for r in extras])


if __name__ == '__main__':
    main()
