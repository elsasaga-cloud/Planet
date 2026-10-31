#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B-PASS-01 · B 池分层（T29-U146 2026-10-31，Simon：「那就开始搞B吧」）。

口径（沿 A 的逻辑降一档）：B = 长期慢慢跟的群，必须「OK」——身份能核、角色对位、路径活、无否决项；不 OK 的下放 C 储备（只巡检，不发）。
  C（储备）：否决项（守界国 / 巨头 / 中国大陆 / 同行卖家 / 品类不对位 / 轨交军工主业）· 路径断（无邮箱无 WA，或 MX 死且无 WA）· 最后一句硬婉拒（R-）·
            个人免费邮箱 + 0 回复 + 非主攻区 · 身份未坐实 + 0 回复 + 官网死
  B1（重点普通跟，目标 ≈300）：出 A 的户（AB-FINAL / A-DEEP 下放，非守界/同行原因）· 有实质回信（R+ / Rw / R±）· 对位角色（OEM 品牌 / 分销 / ISP / 工业集成）+ 身份坐实 + 主攻区（美加欧土）或次主攻（俄印韩）
  B2（普通跟）：其余 OK 的
输出：data/saga_clients/B类分层_<date>.json/.csv；报告 docs/requirements/B类分层_<date>.md/.html；跟进分组 data/saga_clients/B跟进分组_<date>.csv。不改等级（p82 应用）。
"""
import csv
import glob
import json
import os
import re
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
DATE = '2026-10-31'
FOCUS = {'US', 'CA', 'TR', 'GB', 'DE', 'FR', 'IT', 'ES', 'PL', 'NL', 'BE', 'AT', 'CH', 'SE', 'NO', 'DK', 'FI', 'IE', 'PT', 'CZ', 'SK', 'HU', 'RO', 'BG', 'GR', 'HR', 'SI', 'RS', 'LT', 'LV', 'EE', 'CY', 'MT', 'LU', 'BA', 'MK', 'AL', 'ME', 'MD', 'IS'}
SECOND = {'RU', 'IN', 'KR', 'KZ', 'BY', 'UZ'}
GUARD = {'UA', 'IR', 'SY', 'KP', 'CU'}
FREE = re.compile(r'@(gmail|hotmail|yahoo|outlook|live|icloud|mail|yandex|protonmail|aol|gmx|web|list|bk|inbox|rambler|163|qq|126|telus|ymail|msn)\.', re.I)
ROLE_FIT = re.compile(r'分销|经销|distribut|wholesale|批发|reseller|dealer|集成|integrat|install|安装|弱电|OEM|ODM|自有品牌|自牌|own brand|品牌商|brand|ISP|运营商|operator|wisp|broadband|宽带|工业自动化|automation|网店|e-?commerce|电商|trading|贸易|进口', re.I)
OFF = re.compile(r'^(二手|翻新|refurbish)|^(HDMI|AV |音视频|投影|消费电子|游戏|家电)|软件公司|SaaS|数字营销|广告代理|保安服务|guard company|^(学校|school|university|hospital|医院|政府|ministry|military|军工|tactical|轨交|铁路|railway)|^(食品|农业|房地产|物流|律师|会计|纺织|textile)', re.I)
PEER = re.compile(r'同行|竞品|competitor|switch manufacturer|交换机厂|我们的供应商|卖家反推销|把 Saga 当买家|白牌厂|深圳.*厂|OEM 工厂（同行）', re.I)


def load(p, d=None):
    try:
        return json.load(open(p, encoding='utf-8'))
    except Exception:
        return d


def main():
    ents = {e['code']: e for e in load(os.path.join(SD, 'entities.json'))}
    dossier = load(os.path.join(SD, '回信档案_2026-10-30.json'), {})
    digest = load(os.path.join(SD, 'site_digest.json'), {})
    mx = (load(os.path.join(SD, 'mx_check_2026-10-29.json'), {}) or {}).get('domains', {})
    registry = {}
    for f in glob.glob(os.path.join(SD, 'registry', '*.json')):
        for c, v in (load(f, {}) or {}).get('rows', {}).items():
            registry.setdefault(c, v)
    manual = set()
    pm = os.path.join(SD, '人工定级.csv')
    if os.path.exists(pm):
        for r in csv.DictReader(open(pm, encoding='utf-8-sig')):
            manual.add((r.get('键或编号') or '').strip())
    out = {}
    for c, e in ents.items():
        if e.get('grade') != 'B':
            continue
        rs = e.get('research') or {}
        mr = rs.get('mail_review') or {}
        d = dossier.get(c) or {}
        rc = d.get('reply_class') or ('R+' if e.get('reply_sub') else 'none')
        iso = e.get('iso') or ''
        txt = ' '.join([str(rs.get('type', '')), str(rs.get('summary', ''))[:600], ' '.join(rs.get('business_lines') or []), str((mr.get('binding') or {}).get('type', '') if isinstance(mr.get('binding'), dict) else mr.get('binding', ''))[:200], str(e.get('name', ''))])
        dg = digest.get(c) or {}
        site_txt = ' '.join([str(dg.get('title', '')), str(dg.get('desc', ''))])
        # 身份
        reg = registry.get(c) or {}
        reg_ok = bool(reg) and bool(reg.get('number')) and not re.search(r'0 查|未查|未取|未得', str(reg.get('number', '')) + str(reg.get('source', '')))
        legal = str((rs.get('company_facts') or {}).get('legal_name') or rs.get('name_official') or '')
        legal_ok = bool(legal) and '待补' not in legal and not re.match(r'^[\w.-]+\.[a-z]{2,}$', legal.strip(), re.I) and '@' not in legal and not re.search(r'建档|0 查|个人|未具名|没查到', legal)
        site_ok = dg.get('status') == 'ok'
        ident = '登记坐实' if reg_ok else ('法定名' if legal_ok else ('官网' if site_ok else '未坐实'))
        # 路径
        emails = list(e.get('emails') or [])
        site_emails = [m for m in ((rs.get('site_contacts') or {}).get('emails') or []) if '@' in str(m)]
        emails_all = emails + [m for m in site_emails if m not in emails]
        corp = [m for m in emails_all if not FREE.search(m)]
        def mxs(m):
            return (mx.get(m.split('@')[-1].lower()) or {}).get('status')
        known = [mxs(m) for m in emails_all if mxs(m)]
        mx_ok = 'ok' in known
        mx_dead = bool(known) and all(k in ('dead', 'nxdomain') for k in known)
        wa = bool((e.get('flags') or {}).get('wa_added') or e.get('wa_in_fu'))
        bounce = bool((e.get('flags') or {}).get('bounce'))
        phones = [x for x in (e.get('phones') or []) if re.search(r'\d{6,}', str(x))]
        if not emails_all and not wa and not phones and not site_ok:
            path = '断'
        elif not emails_all and not wa:
            path = '弱'      # 只有电话（可 WhatsApp）或只有官网表单
        elif mx_dead and not wa and not site_ok and not phones:
            path = '断'
        elif mx_ok or wa or (site_ok and emails_all and not mx_dead):
            path = '活' if not bounce or len(emails_all) > 1 or wa else '弱'
        else:
            path = '弱'
        # 角色 / 对位
        role_fit = bool(ROLE_FIT.search(txt)) or bool((e.get('fit') or {}).get('switch')) or bool((e.get('fit') or {}).get('mc_sfp')) or bool(re.search(r'switch|poe|network|fiber|industrial|security|cctv|telecom|ethernet', site_txt, re.I))
        bl = rs.get('business_lines') or []
        short = (str(rs.get('type', '')).strip() or (str(bl[0]).strip() if bl else '')) + ' ' + str(e.get('name', ''))
        m_role = re.search(r'OEM|品牌商|自有品牌|自牌|分销|经销|distribut|ISP|运营商|工业集成|系统集成|集成商', str(rs.get('type', '')))
        strong_role = m_role.group(0) if m_role else ''
        off = bool(OFF.search(short)) and not strong_role and not re.search(r'switch|交换机|PoE|工业|industrial|distribut|分销|集成|integrat|安防|security', short, re.I)
        peer = bool(re.search(r'同行|竞品|自研交换机|switch manufacturer|交换机厂|白牌厂|OEM 工厂（同行）|中资', str(rs.get('type', '')) + str(e.get('name', ''))))
        q33 = bool(rs.get('q33_hold')) or '代理商客户' in ' '.join(e.get('tags') or [])
        # 否决
        veto = []
        if iso in GUARD or e.get('region') == '乌克兰':
            veto.append('守界国')
        giant = bool((e.get('flags') or {}).get('giant'))
        if iso == 'CN' or e.get('region') == '中国大陆' or (e.get('domains') and all(str(x).endswith('.cn') for x in e.get('domains'))):
            veto.append('中国大陆')
        if peer:
            veto.append('同行')
        if off:
            veto.append('品类不对位')
        if re.match(r'^(军工|轨交|铁路|railway|defen[cs]e|military)', str(rs.get('type', '')).strip(), re.I):
            veto.append('守界行业')
        # 出 A 记录
        exa = [h for h in (rs.get('override_history') or []) if str(h.get('batch', '')).startswith(('AB-FINAL', 'A-DEEP')) and h.get('to') == 'B']
        exa_reason = (exa[-1].get('reason') or '') if exa else ''
        exa_bad = bool(re.search(r'守界|同行|不对位|不可核|个人|微型|婉拒|无路径|自动回复', exa_reason))
        focus = 'focus' if iso in FOCUS else ('second' if iso in SECOND else 'other')
        free_only = bool(emails) and not corp
        # 结论
        why = []
        if veto:
            tier, why = 'C', ['否决：' + '、'.join(veto)]
        elif path == '断':
            tier, why = 'C', ['路径断（无邮箱无 WA / MX 死 / 退信）']
        elif rc == 'R-':
            tier, why = 'C', ['最后一句硬婉拒（R-）']
        elif free_only and ident == '未坐实' and rc in ('none', 'auto', 'R0') and focus == 'other' and not exa:
            tier, why = 'C', ['个人免费邮箱 + 身份未坐实 + 0 实质回复 + 非主攻区']
        elif q33:
            tier, why = 'B2', ['Q-33 代理商客户：不碰，标记']
        elif giant:
            tier, why = 'B2', ['巨头：不追，标记']
        elif ident == '未坐实' and rc in ('none', 'auto', 'R0') and not site_ok and not exa:
            tier, why = 'C', ['身份未坐实 + 0 回复 + 官网不可用']
        elif exa and not exa_bad:
            tier, why = 'B1', ['出 A 户（' + exa_reason[-80:] + '）']
        elif rc in ('R+', 'Rw', 'R±'):
            tier, why = 'B1', [f'有回信（{rc}）']
        elif strong_role and ident == '登记坐实' and focus == 'focus' and path == '活' and site_ok:
            tier, why = 'B1', [f'强对位（{strong_role}）+ 登记坐实 + 主攻区 + 路径活']
        else:
            tier, why = 'B2', ['OK 但无回信/非主攻' if focus == 'other' else 'OK，待首触反馈']
        if c in manual:
            tier, why = 'B2', ['人工定级 B（不动）']
        out[c] = {'code': c, 'name': e.get('name'), 'country': e.get('country'), 'iso': iso, 'region': e.get('region'), 'tier': tier, 'why': '；'.join(why), 'ident': ident, 'path': path, 'rc': rc, 'role_fit': role_fit, 'focus': focus, 'exA': bool(exa), 'veto': veto,
                  'type': str(rs.get('type', ''))[:40], 'emails': len(emails), 'corp': len(corp), 'wa': wa, 'last_in': d.get('last') or '', 'site': dg.get('status', '')}
    json.dump(out, open(os.path.join(SD, f'B类分层_{DATE}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    with open(os.path.join(SD, f'B类分层_{DATE}.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['编号', '公司', '国家', '区域', '分层', '原因', '身份', '路径', '回信', '对位', '区域档', '出A', '否决', '类型', '邮箱数', '企业邮箱', 'WA', '最近来信', '官网'])
        for c, o in sorted(out.items(), key=lambda kv: (kv[1]['tier'], kv[1]['region'], kv[0])):
            w.writerow([c, o['name'], o['country'], o['region'], o['tier'], o['why'], o['ident'], o['path'], o['rc'], o['role_fit'], o['focus'], o['exA'], '、'.join(o['veto']), o['type'], o['emails'], o['corp'], o['wa'], o['last_in'], o['site']])
    cnt = Counter(o['tier'] for o in out.values())
    print('B', len(out), dict(cnt))
    print('C reasons', Counter(o['why'].split('；')[0][:14] for o in out.values() if o['tier'] == 'C').most_common(8))
    print('B1 by region', Counter(o['region'] for o in out.values() if o['tier'] == 'B1').most_common())
    print('B1 reasons', Counter(o['why'][:6] for o in out.values() if o['tier'] == 'B1').most_common())


if __name__ == '__main__':
    main()
