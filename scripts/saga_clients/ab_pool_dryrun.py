#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A / B 档并入 P 池 · 预演（只读，不改任何等级 / 池位）—— T29-U123（2026-10-29，Simon「继续」）。

背景：三库 C 筛完（P 池正式 243 / 观察 59），按 U115–U117 的顺序该「讨论 A/B 升级 / 调整」了。A 90 + B 1,139 的底数
（登记簿 1,229 行）、邮件层绑定（research.mail_review.binding.sieve）、表内成单 / 样品 / WA、对位（fit）都已在库 —— 不需要外查，
直接按 P 池准入六条（成单 / 样品；决策人真回；产品对位；四主区 + 波兰优先；登记坐实；复购体量；≥2 条）算一遍，给出每户的
「预演结论」，供 Simon 看一眼后再执行（执行脚本另写，本脚本不落任何状态）。

结论档：
  P 核心        —— A 档成单 / 真回户（A = 长期跟进，默认全部入池；邮件层 0 回复的 A 标「A 复核」供新标准讨论）
  P 核心候选    —— B 档有成单 / 样品 / PI（J5：看证据不看地区）
  P 正式候选    —— B 档决策人真回（有回复·跟进中 / 回复暂无需求 / 绑定 ≥3）+ 对位 + （登记坐实 或 体量 ≥ 中小）
  P 观察候选    —— B 档真回但微型 / 未坐实；或冷户四条全中（对位 + 四主区 + 坐实 + 体量 ≥ 中小）
  留 B          —— 其余（继续慢慢跟进；不是 pass）
  留 B·复核     —— 注销 / 退信无备用 / 明确拒绝 → 下一轮人工看

输出：data/saga_clients/AB并池_预演_2026-10-29.csv（utf-8-sig）+ 终端汇总（写进 docs/AB并池方案_草案_2026-10-29.md）。
用法：python3 scripts/saga_clients/ab_pool_dryrun.py
"""
import collections
import csv
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
ENTS = os.path.join(DATA, 'entities.json')
MANUAL = os.path.join(DATA, '人工定级.csv')
OUT = os.path.join(DATA, 'AB并池_预演_2026-10-29.csv')
MAIN = {'美国', '加拿大', '英国', '德国', '土耳其', '波兰'}
GROUP_ORDER = ['四主区 + 波兰', '欧洲其他', '俄语区', '印度 / 南亚', '东亚 / 东南亚 / 大洋洲', '中东 / 非洲', '拉美', '其他']
CONC_ORDER = ['P 核心', 'P 核心候选', 'P 正式候选', 'P 观察候选', '留 B', '留 B·复核', '留 B·守界']
GUARD = {'乌克兰', '伊朗', '叙利亚'}   # 守界：不 pass、不入池（U117 ⑧ + 闸 1 教训）


def group_of(e):
    c = e.get('country') or ''
    r = e.get('region') or ''
    if c in MAIN:
        return '四主区 + 波兰'
    if r in ('欧洲',) or c in ('瑞士', '捷克', '西班牙', '意大利', '法国', '葡萄牙', '挪威', '丹麦', '芬兰', '瑞典', '荷兰', '比利时', '奥地利', '匈牙利', '斯洛伐克', '立陶宛', '拉脱维亚', '爱沙尼亚', '保加利亚', '希腊', '罗马尼亚', '塞尔维亚', '克罗地亚', '斯洛文尼亚', '爱尔兰', '欧洲（国别未填）'):
        return '欧洲其他'
    if r in ('俄语区',) or c in ('俄罗斯', '白俄罗斯', '哈萨克斯坦', '乌兹别克斯坦', '格鲁吉亚', '亚美尼亚', '阿塞拜疆', '吉尔吉斯斯坦', '摩尔多瓦'):
        return '俄语区'
    if r in ('南亚',) or c in ('印度', '巴基斯坦', '孟加拉国', '尼泊尔', '斯里兰卡'):
        return '印度 / 南亚'
    if r in ('亚太', '东亚', '东南亚', '大洋洲') or c in ('越南', '台湾', '韩国', '日本', '香港', '泰国', '马来西亚', '新加坡', '印度尼西亚', '菲律宾', '澳大利亚', '新西兰'):
        return '东亚 / 东南亚 / 大洋洲'
    if r in ('中东', '非洲') or c in ('南非', '阿联酋', '沙特阿拉伯', '坦桑尼亚', '埃及', '以色列', '肯尼亚', '尼日利亚', '摩洛哥'):
        return '中东 / 非洲'
    if r in ('拉美',) or c in ('巴西', '墨西哥', '智利', '玻利维亚', '厄瓜多尔', '巴拉圭', '危地马拉', '哥伦比亚', '阿根廷', '秘鲁'):
        return '拉美'
    return '其他'


def load_registry():
    rows = {}
    for p in glob.glob(os.path.join(DATA, 'registry', '*.json')):
        for code, r in json.load(open(p, encoding='utf-8'))['rows'].items():
            rows[code] = r
    return rows


def load_manual():
    m = {}
    if os.path.exists(MANUAL):
        with open(MANUAL, encoding='utf-8-sig', newline='') as f:
            for r in csv.DictReader(f):
                m[r['键或编号']] = r
    return m


RE_ACTIVE = re.compile(r'Active|Aktiv|Attiva|Действ|Live|营业中|Activa|Actif|Faal|有效|存续|在业|正常|ยัง|Activo|Ativa|Aktywn|Registered|Actief|Aktif|營業|Активен|Activă|Aktiivinen|Aktívna|在册|互动中|站点在线', re.I)
RE_DEAD = re.compile(r'Dissolved|注销|Liquid|清算|吊销|Inactive|Ceased|Gelöscht|Opgeheven|closed|停业|撤销|Ликвид|站点失效|主体不明', re.I)


def judge(e, reg, manual):
    r = e.get('research') or {}
    mr = (r.get('mail_review') or {}).get('binding') or {}
    sieve = (mr.get('sieve') or '').strip()
    lvl = int(sieve[0]) if sieve[:1].isdigit() else None
    flags = e.get('flags') or {}
    status = e.get('status') or ''
    fit = e.get('fit') or {}
    grp = group_of(e)
    # 六条
    deal = bool(flags.get('deal') or flags.get('sample') or e.get('pi') or e.get('deal_in_fu') or status.startswith('成交过') or (lvl is not None and lvl >= 4) or (sieve.startswith('3') and '付样' in sieve))
    engaged = bool(e.get('reply_sub') or status.startswith('有回复') or status.startswith('回复') or (lvl is not None and lvl >= 3))
    wa = bool(flags.get('wa_added') or e.get('wa_in_fu'))
    fit_sw = (fit.get('switch') or 0) >= 1
    fit_only_off = (not fit_sw) and (fit.get('off') or 0) >= 1 and not fit.get('mc_sfp')
    fit_txt = '✔ 交换机' if fit_sw else ('MC/SFP' if fit.get('mc_sfp') else ('✘ 光端机等（日职线）' if fit_only_off else '未知'))
    main = grp == '四主区 + 波兰'
    eu = grp == '欧洲其他'
    number = (reg or {}).get('number') or ''
    rstatus = (reg or {}).get('status') or ''
    registered = bool(re.search(r'\d{4,}', number)) and not RE_DEAD.search(rstatus)
    dead = bool(RE_DEAD.search(rstatus)) and not RE_ACTIVE.search(rstatus)
    sb = (reg or {}).get('size_band') or ''
    big = bool(re.match(r'(中型|大型|中小|51–200|11–50|中等)', sb))
    micro = bool(re.match(r'(微型|个人|个体|小微|一人|2–10|1 人)', sb))
    giant = sb.startswith('大型') and bool(re.search(r'上市|集团|跨国|运营商|巨头', sb + ' ' + (r.get('type') or '')))
    own_brand = bool(flags.get('own_brand'))
    bounce = bool(flags.get('bounce') or flags.get('wa_failed'))
    no_path = not (e.get('emails') or e.get('phones') or wa)
    neg = bool(e.get('reply_neg'))
    man = manual.get(e['code']) or {}
    simon_gg = ('gg' in (man.get('理由') or '')) or any('gg' in t for t in (e.get('tags') or [])) or ('已凉' in status)
    hits = sum([deal, engaged, fit_sw, main, registered, big])
    red = []
    if dead:
        red.append('登记注销 / 主体不明')
    if bounce and no_path:
        red.append('退信且无备用路径')
    if neg and status.startswith('回复暂无需求'):
        red.append('回复暂无需求')
    if giant:
        red.append('巨头 / 集团（长线）')
    if simon_gg:
        red.append('Simon: gg / 已凉')
    tags = []
    if own_brand:
        tags.append('oem_target')
    if grp == '俄语区':
        tags += ['ru_payment', 'prepay']
    elif not (main or eu) and not registered:
        tags.append('prepay')
    if (e.get('country') or '') == '韩国':
        tags.append('kc_needed')
    if fit_only_off:
        tags.append('dayjob_fit')
    if giant:
        tags.append('giant')
    # 结论
    if (e.get('country') or '') in GUARD and e['grade'] != 'A':
        conc = '留 B·守界'
        why = f"{e.get('country')} 守界：不 pass、不入池（U117 ⑧）" + ('；成单 / 样品 ✔' if deal else '') + ('；真回 ✔' if engaged else '')
    elif e['grade'] == 'A':
        conc = 'P 核心'
        why = 'A 档默认入池（长期跟进）' + ('；成单 / 样品 ✔' if deal else '') + ('；真回 ✔' if engaged else '') + ('' if (deal or engaged) else '；**A 复核**：邮件层 0 回复 / 无成单记录 → 等新 A 标准')
    elif dead or (bounce and no_path):
        conc = '留 B·复核'
        why = '；'.join(red) + ' → 人工看一眼再定'
    elif deal:
        conc = 'P 核心候选'
        why = '成单 / 样品 / PI ✔（J5 看证据不看地区）' + ('；真回 ✔' if engaged else '') + ('；对位 ' + fit_txt)
    elif engaged and fit_sw and (registered or big):
        conc = 'P 正式候选'
        why = '真回 ✔ + 对位 ✔ + ' + ('坐实 ✔' if registered else '') + ('体量 ✔' if big else '') + ('；WA ✔' if wa else '')
    elif engaged:
        conc = 'P 观察候选'
        why = '真回 ✔ 但 ' + ('微型' if micro else '') + ('未坐实' if not registered else '') + ('对位 ' + fit_txt if not fit_sw else '') + ' → 观察'
    elif fit_sw and main and registered and big:
        conc = 'P 观察候选'
        why = '冷户四条全中（对位 + 四主区 + 坐实 + 体量）→ 观察，首触看反应'
    else:
        conc = '留 B'
        why = f'命中 {hits}/6（' + '、'.join(x for x, ok in [('对位', fit_sw), ('四主区', main), ('欧洲其他', eu), ('坐实', registered), ('体量', big), ('WA', wa)] if ok) + '）；' + ('微型' if micro else '') + ('；读而不回' if (lvl == 2) else '') + ('；只收到群发' if lvl == 1 else '') + ('；未触达' if lvl in (0, None) else '')
    if red and conc not in ('留 B·复核',):
        why += '；⚠ ' + '；'.join(red)
    return dict(code=e['code'], grade=e['grade'], name=(r.get('name_official') or e.get('name') or '')[:60], country=e.get('country') or '', group=grp,
                deal='✔' if deal else '', engaged='✔' if engaged else '', wa='✔' if wa else '', fit=fit_txt, registered='✔' if registered else ('✘ 注销' if dead else '未坐实'),
                size=sb[:14], hits=hits, sieve=sieve[:28], status=status, red='；'.join(red), tags='、'.join(tags), conc=conc, why=why)


def main():
    ents = json.load(open(ENTS, encoding='utf-8'))
    reg = load_registry()
    manual = load_manual()
    rows = [judge(e, reg.get(e['code']), manual) for e in ents if e.get('grade') in ('A', 'B')]
    rows.sort(key=lambda x: (CONC_ORDER.index(x['conc']), GROUP_ORDER.index(x['group']), x['code']))
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['编号', '等级', '公司（登记名优先）', '国家', '区域组', '成单/样品', '真回', 'WA', '对位', '登记', '体量', '命中/6', '邮件绑定档', '表内状态', '红旗', '标签', '预演结论', '理由'])
        for x in rows:
            w.writerow([x['code'], x['grade'], x['name'], x['country'], x['group'], x['deal'], x['engaged'], x['wa'], x['fit'], x['registered'], x['size'], x['hits'], x['sieve'], x['status'], x['red'], x['tags'], x['conc'], x['why']])
    by = collections.Counter(x['conc'] for x in rows)
    byg = collections.defaultdict(collections.Counter)
    for x in rows:
        byg[x['conc']][x['group']] += 1
    print('rows', len(rows), dict(by))
    for c in CONC_ORDER:
        print(' ', c, {g: byg[c][g] for g in GROUP_ORDER if byg[c][g]})
    a_review = [x['code'] for x in rows if x['grade'] == 'A' and 'A 复核' in x['why']]
    print('A 复核', len(a_review), a_review[:40])
    red = collections.Counter()
    for x in rows:
        for t in x['red'].split('；'):
            if t:
                red[t] += 1
    print('red flags', dict(red))
    cand = [x for x in rows if x['conc'] in ('P 核心候选', 'P 正式候选')]
    print('B 核心+正式候选', len(cand), collections.Counter(x['group'] for x in cand))
    watch = [x for x in rows if x['conc'] == 'P 观察候选']
    print('B 观察候选', len(watch), collections.Counter(x['group'] for x in watch))
    print('fit 分布（B 候选）', collections.Counter(x['fit'] for x in cand + watch))
    print('→', OUT)


if __name__ == '__main__':
    main()
