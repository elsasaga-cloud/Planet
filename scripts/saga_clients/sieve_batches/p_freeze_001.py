#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 3「入池冻结」第 01 批（2026-10-29，T29-U119）—— Simon：「那些需要评估的你自己搞吧 我没办法挨个看 就是按照你搜索 以及 对于 saga 产品线 idea 的理解」。

把闸 2 的 P 池候选 204 户按闸 2 档位一次性定档入池（不再等逐户否决）：
  · ★★ / ★ / ○ → verdict = pool（P 池正式入池：终身跟进 + 每 2 个月巡检）
  · △           → verdict = pool_watch（P 池观察档：试单 / 回访一次后转正或退回 C；不计入「极精华」口径）
  · 个别例外：SC-2730 RVi（ГК «Рубеж» 制裁名单待核）→ pool_watch 守界，核查清楚前不主动发
  · 标签：Q-33（洪瑞 / 经销体系现供）→ q33_hold（只巡检不主动发，直到 Simon 另说）；国别存疑 → country_pending

产出：
  · data/saga_clients/sieve.json（gate=3, rule=P1, batch=P-01；保留 g2_batch / g2_reason / g1_batch / g1_reason）
  · docs/P池_资产池名册_2026-10-29.md（按区域 × 档位的名册：线路 / 下一步 / 巡检点）
  · data/saga_clients/P池_巡检表_2026-10-29.csv（每 2 个月巡检用：域名 / 平台链接 / 下次巡检日）

用法：python3 sieve_batches/p_freeze_001.py   （幂等）
"""
import csv
import os
import re
import sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402
import registry_store  # noqa: E402

BATCH = 'P-01'
DATE = '2026-10-29'
NEXT_CHECK = '2026-12-28'
ROSTER = os.path.join(sieve.ROOT, 'docs', f'P池_资产池名册_{DATE}.md')
WATCH = os.path.join(sieve.DATA, f'P池_巡检表_{DATE}.csv')

MAIN = {'美国', '加拿大', '英国', '德国', '土耳其', '波兰'}
GROUP_ORDER = ['四主区 + 波兰', '欧洲其他', '俄语区', '印度 / 南亚', '东亚 / 东南亚 / 大洋洲', '中东 / 非洲', '拉美', '其他']
WATCH_OVERRIDE = {
    'SC-2730': 'ГК «Рубеж» 制裁名单待核 —— 守界：核查清楚前不主动发，只巡检',
}


def grade(reason):
    m = re.match(r'^\W{0,3}?(★★|★|○|△)', reason.strip())
    return m.group(1) if m else '○'


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


def line_of(reason):
    m = re.search(r'(OEM 30%|分销 20%|集成 25%|渠道 25%|贸易 20%|零售 20%|回访|dayjob|成单)', reason)
    return m.group(1) if m else '—'


def strip_grade(s):
    return re.sub(r'^(★★|★|○|△)\s*', '', s or '')


def short(s, n):
    s = re.sub(r'\s+', ' ', s or '')
    return s if len(s) <= n else s[:n - 1] + '…'


def main():
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    reg = registry_store.load_all()
    todo = {k: v for k, v in sv.items() if isinstance(v, dict) and v.get('verdict') in ('pool_candidate', 'pool', 'pool_watch')}
    assert len(todo) == 204, len(todo)
    rows = []
    for code, cur in sorted(todo.items()):
        base = cur.get('g2_reason') or (cur['reason'] if cur.get('gate') == 2 else None) or cur['reason']
        base = re.sub(r'^(★ P 池正式入池|☆ P 池观察档)[^：]*：', '', base)
        g = grade(base)
        tags = set(cur.get('tags') or [])
        if 'Q-33' in base or '洪瑞现供' in base:
            tags.add('q33_hold')
        if re.search(r'国别(待核|存疑|纠偏)', base):
            tags.add('country_pending')
        if code in WATCH_OVERRIDE:
            verdict = 'pool_watch'
            why = f'☆ P 池观察档（{WATCH_OVERRIDE[code]}）：{base}'
        elif g in ('★★', '★', '○'):
            verdict = 'pool'
            why = f'★ P 池正式入池（档位 {g}）：{base}'
        else:
            verdict = 'pool_watch'
            why = f'☆ P 池观察档（档位 △ = 微型 / 自用 / 个体 / 存疑，试单或回访一次后定）：{base}'
        row = {'verdict': verdict, 'gate': 3, 'rule': 'P1', 'reason': why, 'date': DATE, 'manual': True, 'batch': BATCH,
               'g2_batch': cur.get('g2_batch') or (cur.get('batch') if cur.get('gate') == 2 else None), 'g2_reason': base,
               'g1_batch': cur.get('g1_batch'), 'g1_reason': cur.get('g1_reason'), 'grade': g, 'next_check': NEXT_CHECK}
        if tags:
            row['tags'] = sorted(tags)
        sv[code] = row
        e = ents[code]
        r = reg.get(code) or {}
        action = (r.get('lines') or [''])[0]
        action = re.sub(r'\*\*', '', action)
        action = re.sub(r'— .*?常规：.*$', '', action)
        links = list(OrderedDict.fromkeys((e.get('domains') or []) + [u for u in (e.get('platform_links') or []) if 'google.com/search' not in u and 'yandex.com/search' not in u]))
        rows.append((group_of(e), verdict, g, code, e, base, action, links, sorted(tags), r))
    cnt = sieve.save_sieve(sv)

    c_v = Counter(v for _, v, *_ in rows)
    c_g = Counter(g for _, _, g, *_ in rows)
    c_grp = Counter((grp, v) for grp, v, *_ in rows)
    L = [f'# P 池 · 资产池名册（第 01 批冻结，{DATE}）', '',
         f'> 来源：C 池三闸筛选（`docs/C池三闸筛选_方案_2026-10-29.md`）闸 2 P 池候选 204 户，按 Simon 2026-10-29「需要评估的你自己搞」口令一次性定档（`scripts/saga_clients/sieve_batches/p_freeze_001.py`，`data/saga_clients/sieve.json` gate=3）。'
         f' **正式入池 {c_v["pool"]}（★★ {c_g["★★"]} / ★ {c_g["★"]} / ○ {c_g["○"] - sum(1 for _, v, g, *_ in rows if v == "pool_watch" and g == "○")}）/ 观察档 {c_v["pool_watch"]}**。'
         f' origin：本批全部 = Saga C（External 4,351 + Planet 仓 129 后续同法并入，名册加 origin 列）。', '',
         '> 规则：正式入池 = 终身跟进 + 每 2 个月巡检（官网 / 社媒 / GitHub / 展会 / 新品，见 `data/saga_clients/P池_巡检表_' + DATE + '.csv`，下次 ' + NEXT_CHECK + '）；观察档 = 试单 / 回访一次后转正或退回 C。'
         ' 标签：`q33_hold` = 洪瑞 / 经销体系现供（Q-33）只巡检不主动发；`country_pending` = 国别待核（纠偏见 research JSON `country_fix`）；`oem_target` = 贴牌 / 自有品牌 → OEM 30% 线；`dayjob_fit` = 光端机 / DWDM / 光模块需求（Simon 本职线并行）。'
         ' 价格口径：分销 20% / 集成 25% / OEM 30%；T/T 50/50，微型预付 100%；MOQ 1；英文稿；一页纸一次，不追发。', '',
         '## 总览', '', '| 区域 | 正式入池 | 观察档 |', '|---|---|---|']
    for grp in GROUP_ORDER:
        if c_grp[(grp, 'pool')] + c_grp[(grp, 'pool_watch')]:
            L.append(f'| {grp} | {c_grp[(grp, "pool")]} | {c_grp[(grp, "pool_watch")]} |')
    L.append(f'| **合计** | **{c_v["pool"]}** | **{c_v["pool_watch"]}** |')
    L.append('')
    order = {'★★': 0, '★': 1, '○': 2, '△': 3}
    for grp in GROUP_ORDER:
        sub = [x for x in rows if x[0] == grp]
        if not sub:
            continue
        L += [f'## {grp}（正式 {c_grp[(grp, "pool")]} / 观察 {c_grp[(grp, "pool_watch")]}）', '']
        for verdict, title in (('pool', '正式入池'), ('pool_watch', '观察档')):
            ss = [x for x in sub if x[1] == verdict]
            if not ss:
                continue
            L += [f'### {title}（{len(ss)}）', '', '| 档 | 编号 | 公司 | 国家 | 线路 | 标签 | 闸 2 结论 | 下一步 | 巡检点 |', '|---|---|---|---|---|---|---|---|---|']
            for _, v, g, code, e, base, action, links, tags, r in sorted(ss, key=lambda x: (order[x[2]], x[3])):
                concl = sieve.md(short(strip_grade(base), 150))
                L.append(f"| {g} | `{code}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {line_of(base)} | {'、'.join(tags)} | {concl} | {sieve.md(short(action, 120))} | {sieve.md(short(' / '.join(links), 90))} |")
            L.append('')
    L += ['## 本批评估口径（Agent 代判，Simon 可随时按编号改）', '',
          '- Karel（SC-2776）/ Conexpro（SC-2957）/ Urban Security Group（SC-2597）等 Simon 早年「判定不行」的户：表内证据（在卖中国贴牌 / 自有品牌）满足 U117 新口径 → 入池；Conexpro 实为捷克 Plzeň 品牌（国别纠偏 RU→CZ 已落 research JSON）。',
          '- 永久 pass 不救回：SC-3276 PT Integra（印尼，仅公司名）/ SC-3281 Rasyonel（土耳其，2011 仅公司名）维持 pass —— 刚性①成立，且非四主区 / 无任何路径，与「一旦入选永不考虑」一致。',
          '- Q-33（洪瑞 / 经销体系现供）默认 = 入池但 `q33_hold` 只巡检不主动发；RVi（SC-2730）= 观察档守界，制裁核查清楚前不发。',
          '- △ 观察档 36 户不计入「300–500 极精华」口径；成单 / 复购的微型终端（JEVASO、EasyWind、Continental Towers、Radio ZP30）各回访一次，有复购即转正。',
          '- 本批之后 P 池只增不减：External XC 2,133 同法闸 0 → 闸 1 → 闸 2 → 闸 3；Planet 仓 129 并池；A / B 的升降另议（A 90 新标准待 Simon）。']
    open(ROSTER, 'w', encoding='utf-8').write('\n'.join(L) + '\n')

    with open(WATCH, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['编号', '档位', '入池', '公司', '国家', '区域组', '域名 / 平台链接', '标签', '上次巡检', '下次巡检', '巡检项', '备注'])
        for grp, v, g, code, e, base, action, links, tags, r in sorted(rows, key=lambda x: (GROUP_ORDER.index(x[0]), x[1] != 'pool', order[x[2]], x[3])):
            w.writerow([code, g, '正式' if v == 'pool' else '观察', e.get('name'), e.get('country') or '未填', grp, ' | '.join(links), '、'.join(tags), DATE, NEXT_CHECK,
                        '官网改版 / 新品 / 招聘 / 社媒（LinkedIn / FB / IG）/ GitHub / 展会出席 / 新闻稿 / 域名 MX 存活', short(strip_grade(base), 160)])
    print(BATCH, len(rows), dict(c_v), dict(c_g), 'sieve', dict(cnt), os.path.relpath(ROSTER, sieve.ROOT), os.path.relpath(WATCH, sieve.ROOT))


if __name__ == '__main__':
    main()
