#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T29-U64 · 第 82 批 · 当地假日避让：A/B 出现的每个国家，列 2026-10-27 → 2027-03-31 的法定假日（holidays 包）
+ 手工叠加的「惯例停摆」（圣诞-新年停摆、斋月、春节供应侧停摆、俄罗斯新年长假、黑五周、澳洲夏休、巴西狂欢节…）。

输出：
  data/saga_clients/holidays_2026-11_2027-03.json   {iso: {"legal": [[date, name]], "practice": [[start, end, label, kind]]}}
  docs/各国假日避让_2026-11_2027-03.md               按 A/B 户数排序的国家表 + 近 30 天「别发信的日子」
calendar.py / render.py 读 JSON；本脚本只在假日表要刷新时重跑。
用法：python3 holidays_cal.py
"""
import datetime as dt
import json
import os
import sys
from collections import Counter

# 本目录有 calendar.py（跟进日历），会遮住标准库 calendar → 先把脚本目录移出 sys.path 再导 holidays
_here = os.path.dirname(os.path.abspath(__file__))
sys.path = [p for p in sys.path if os.path.abspath(p or '.') != _here]
import calendar  # noqa: E402  标准库
import holidays  # noqa: E402  pip install holidays
sys.path.insert(0, _here)

from common import DATA, ROOT  # noqa: E402

START, END = dt.date(2026, 10, 27), dt.date(2027, 3, 31)
OUT = os.path.join(DATA, 'holidays_2026-11_2027-03.json')
DOC = os.path.join(ROOT, 'docs', '各国假日避让_2026-11_2027-03.md')

WEST = set('US CA GB IE DE AT CH FR IT ES PT NL BE LU DK SE NO FI IS PL CZ SK HU RO BG HR SI LT LV EE GR CY MT MX CL AR CO PE BR ZA PH'.split())
ORTHODOX = set('RU UA BY RS GE MK ME MD KZ'.split())
RAMADAN = set('TR AE SA PK ID MY EG IQ JO KW QA BH OM LB MA DZ TN BD IR LY'.split())
CNY = set('CN TW HK SG MY VN KR MO'.split())

# (iso 集合或单个 iso, start, end, 标签, 类型)  类型：惯例 / 宗教 / 供应侧 / 商业季
PRACTICE = [
    (WEST, '2026-12-21', '2027-01-03', '圣诞-新年停摆：多数公司 12-21 起只剩值班，决策人 1-04 以后才回', '惯例'),
    ({'JP'}, '2026-12-29', '2027-01-03', '年末年始：日本公司 12-29→1-03 关门', '惯例'),
    ({'RU', 'BY'}, '2026-12-31', '2027-01-10', '俄罗斯新年长假：法定 1-01→1-08，叠加周末实际到 1-10；12 月最后一周已在收尾', '惯例'),
    ({'KZ', 'UZ'}, '2026-12-31', '2027-01-04', '新年假：1-01/1-02 法定，叠加周末', '惯例'),
    (ORTHODOX, '2027-01-07', '2027-01-07', '东正教圣诞', '宗教'),
    (RAMADAN, '2027-02-08', '2027-03-09', '斋月（按天文估算 2027-02-08 起，以当地公告为准）：白天效率低、午后早走，海湾国家法定工时缩到 6 小时；开斋节前一周基本不做决策', '宗教'),
    (RAMADAN, '2027-03-09', '2027-03-12', '开斋节（Eid al-Fitr / Ramazan Bayramı，估算）：3–4 天全停', '宗教'),
    (CNY, '2027-02-04', '2027-02-14', '春节：客户侧（台 / 港 / 新 / 马华人企业 / 越南 Tết / 韩国 Seollal 2-06→2-08）放假 3–9 天', '惯例'),
    ('*', '2027-01-25', '2027-02-21', '我方供应侧春节停摆：SmartByte / HRUI 工厂约 2-01→2-17 放假，1-25 前不锁单的 2 月出不了货，节后出货排队到 2 月底；任何「现在要货」的客户 1 月中就得催 PI', '供应侧'),
    ({'US', 'CA'}, '2026-11-23', '2026-11-30', '感恩节周 + 黑五 / 网一：11-26 法定、11-27 实际放假；零售 / 电商类客户整周最忙，别推销', '商业季'),
    ({'IN'}, '2026-11-08', '2026-11-10', '排灯节 Diwali（11-08 周日）：11-09/11-10 多数公司放假，整周慢', '宗教'),
    ({'AU', 'NZ'}, '2026-12-18', '2027-01-25', '澳新夏休：12-18 起到 1 月下旬，很多公司直接关到澳大利亚日（1-26）后', '惯例'),
    ({'ZA'}, '2026-12-11', '2027-01-11', '南非 builders\' holiday：工程 / 安装类客户 12 月中到 1 月中停工', '惯例'),
    ({'BR'}, '2027-02-08', '2027-02-10', '狂欢节（2-08/2-09 + 2-10 上午）', '惯例'),
    ({'TR'}, '2026-10-28', '2026-10-29', '共和国日：10-28 下午半天 + 10-29 全天', '法定补充'),
    ({'IL'}, '2027-03-23', '2027-03-23', '普珥节 Purim（非法定，但很多公司放半天）', '宗教'),
    ({'TH'}, '2026-12-31', '2027-01-03', '泰国新年假（12-31 + 1-01 法定，叠加周末）', '惯例'),
    ({'PH'}, '2026-12-24', '2027-01-01', '菲律宾圣诞-新年：12-24 / 12-31 特别非工作日，12-25 / 12-30 / 1-01 法定', '惯例'),
]


def load_ab_isos():
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    ents = ents if isinstance(ents, list) else list(ents.values())
    c = Counter()
    names = {}
    for e in ents:
        if e.get('grade') in ('A', 'B'):
            iso = (e.get('iso') or '').upper()
            if len(iso) == 2 and iso != 'EU':
                c[iso] += 1
                names.setdefault(iso, e.get('country') or iso)
    return c, names


def legal(iso):
    try:
        hs = holidays.country_holidays(iso, years=[2026, 2027], language='en_US')
    except Exception:
        try:
            hs = holidays.country_holidays(iso, years=[2026, 2027])
        except Exception:
            return []
    rows = []
    for d, n in sorted(hs.items()):
        if START <= d <= END:
            rows.append([d.isoformat(), n])
    return rows


def practice(iso):
    rows = []
    for who, s, e, label, kind in PRACTICE:
        if who == '*' or iso in who:
            rows.append([s, e, label, kind])
    return rows


def main():
    counts, names = load_ab_isos()
    data = {}
    for iso in counts:
        data[iso] = {'country': names[iso], 'ab': counts[iso], 'legal': legal(iso), 'practice': practice(iso)}
    meta = {'generated': dt.datetime.utcnow().strftime('%Y-%m-%d %H:%MZ'), 'range': [START.isoformat(), END.isoformat()],
            'source': f'holidays {holidays.__version__}（法定）+ 手工惯例表（PRACTICE，{len(PRACTICE)} 条）', 'countries': len(data)}
    json.dump({'_meta': meta, 'countries': data}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

    # ---- doc ----
    L = [f'# 各国假日避让 2026-11 → 2027-03（第 82 批，自动生成，勿手改）', '',
         f"生成：{meta['generated']}。来源：{meta['source']}。覆盖 A/B 出现的 {len(data)} 个国家，按 A/B 户数排序。"
         '法定假日 = `holidays` 包（伊斯兰 / 农历节日为天文估算，±1 天）；「惯例」= 行业常识，不是法律，用来避开发信 / 催单的死时段。',
         '', '## 用法', '',
         '- 跟进日历（`docs/跟进日历_YYYY-MM.md`）每行已带「该月假日」列；各户档案「第 82 批 · 邮箱域体检 + 假日避让」一节按该户 `next_move.when` 算出撞上的日子。',
         '- 原则：法定假日前 1 个工作日下午、假日当天、长假后第 1 个工作日上午都别发——发了也沉底。斋月期间只在上午 10 点前（对方时间）发。',
         '- 我方春节停摆是**所有国家共用**的硬约束：1-25 前锁单，2-01→2-17 工厂放假。',
         '', '## 近 30 天别发信的日子（2026-10-27 → 2026-11-26）', '']
    soon_end = START + dt.timedelta(days=30)
    rows = []
    for iso, v in data.items():
        for d, n in v['legal']:
            dd = dt.date.fromisoformat(d)
            if START <= dd <= soon_end:
                rows.append((d, iso, v['country'], v['ab'], n))
    rows.sort(key=lambda r: (r[0], -r[3]))
    L.append('| 日期 | 国家 | A/B 户 | 假日 |')
    L.append('|---|---|---|---|')
    for d, iso, cn, ab, n in rows:
        L.append(f'| {d} | {cn}（{iso}） | {ab} | {n} |')
    L += ['', '## 分国家', '']
    for iso, v in sorted(data.items(), key=lambda kv: -kv[1]['ab']):
        L.append(f"### {v['country']}（{iso}）· A/B {v['ab']} 户")
        L.append('')
        if v['legal']:
            L.append('法定：' + '；'.join(f'{d} {n}' for d, n in v['legal']))
        else:
            L.append('法定：（holidays 包无该国数据）')
        for s, e, label, kind in v['practice']:
            L.append(f'- 【{kind}】{s}→{e}：{label}' if s != e else f'- 【{kind}】{s}：{label}')
        L.append('')
    open(DOC, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(json.dumps(meta, ensure_ascii=False), '→', OUT, DOC)


if __name__ == '__main__':
    main()
