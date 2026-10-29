#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长期客户群复核 · LT-R07（External 优先级 3 全部 669 户）+ LT-R08（Planet 仓 优先级 3 全部 23 户）· T29-U129 2026-10-29。

Simon U129：「只要没深入挖过 / 不确定是否为行业客户 / 不确定有较大可能成单 → 统统挖掘 → 评一下 → 不行就进 C；剩下的就是 OK 的」。
依据 = 来源库 9 月官网 / 名录核对（type / signals / kv）+ 第 2 步研究卡（type_final / size / grade_reason_final / evidence）+ Planet 表「信号 / 评级依据」。
留 B = 行业内 ✔（分销 / 集成 / 系统之家 / 安装 / ISP·WISP / 自有品牌）+ 对位 ✔（在卖或在装交换机）+ 有路径；非主区 → 预付 100%。
打回 C 储备（可逆）五类：CONS 个人顾问 / 讲师 / 培训机构（MikroTik 认证名录，服务型非采购主体）；SHOP 微型零售 / 平台卖家 / 未核实小店；
NOFIT 业务线不对位；NOPATH 无路径或主体状态不明；EVENT 展会主办方。
落点：External `overrides.json`（grade / review）；Planet CSV「人工定级 / C级细分 / 长期群复核」；P 池巡检表剔除打回户；日志 data/长期客户群_复核记录.csv。幂等。
"""
import csv
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XD = os.path.join(ROOT, 'data', 'external_clients')
PCSV = os.path.join(ROOT, 'data', '客户名单_Planet渠道_2026-10.csv')
LOG = os.path.join(ROOT, 'data', '长期客户群_复核记录.csv')
WATCH = os.path.join(ROOT, 'data', 'saga_clients', 'P池_巡检表_2026-10-29.csv')
DATE = '2026-10-29'
BX, BP = 'LT-R07', 'LT-R08'

CONS = set("""XA-M002 XA-M003 XA-M005 XA-M007 XA-M008 XA-M010 XA-M012 XA-M013 XA-M015 XA-M019 XA-M020 XA-M023 XA-M024 XA-M025 XA-M026 XA-M027
XA-M029 XA-M030 XA-M033 XA-M034 XA-M035 XA-M036 XA-M037 XA-M039 XA-M040 XA-M041 XA-M042 XA-M044 XA-M047 XA-M048 XA-M053 XA-M056 XA-M057
XA-M058 XA-M059 XA-M062 XA-M063 XA-M067 XA-M071 XA-M075 XA-M078 XA-M082 XA-M083 XA-M087 XA-M102 XA-M115 XA-M116 XA-M118 XA-M126 XA-M133
XA-M135 XA-M138 XA-M151 XA-M160 XA-M187 XA-M189 XA-M196 XA-M203 XA-M210 XA-M232 XA-M239 XA-M240 XA-M249 XA-M258 XA-M259 XA-M263 XA-M264
XA-M265 XA-M268 XA-M271 XA-M274 XA-M277 XA-M282 XA-M283 XA-M284 XA-M287 XA-M288 XA-M291 XA-M298 XA-M334 XA-M336 XA-M046 XA-M223 XA-M224
XA-M295 XA-M297 XA-M331 XA-M257""".split())
SHOP = set("XA-M065 XA-M069 XA-M072 XA-M073 XA-M108 XA-M144 XA-M156 XA-M180 XA-M206 XA-M214 XA-M290 XA-M225 XA-M246 XA-M305 XB-C0224 XB-C0167 XB-C0531".split())
NOFIT = set("XA-M204 XA-M251 XA-M508 XA-M329 XA-E027 XA-M320 XA-M408 XA-M418 XA-M379 XA-M392 XA-M368 XA-M387 XA-M486".split())
NOPATH = set("XA-M092 XA-M292 XA-M215 XA-M509 XA-E016 XA-M467 XA-M349 XA-M353 XB-E085 XB-E090".split())
EVENT = {'XB-C0060'}
CAT = {
    'CONS': '个人顾问 / 讲师 / 培训机构（MikroTik 认证名录）：服务型非采购主体、一人或无采购量 → C 储备（来信询价即回 B）',
    'SHOP': '微型零售 / 平台卖家 / 未核实小店：无进口证据、难复购 → C 储备（询价或坐实即回 B）',
    'NOFIT': '业务线不对位（电气承包 / 特种电缆 / 船用电子 / 报警消防 / IT 咨询 / 远程访问软件 / 元器件 design-in / 翻新二手 / POF 厂商 / LoRaWAN 厂商附带小店）→ C 储备',
    'NOPATH': '无可用路径或主体状态不明（无邮箱 / 仅社媒 / 仅 gmail / 邮箱域不一致 / 重组中 / 信息不足）→ C 储备（补到路径或明朗即回 B）',
    'EVENT': '展会主办方，非客户主体 → C',
}
PLANET_C = {
    'PC-006': '100MEGA Distribution（捷克大型 IT 分销集团）：Mikrotik 仓已两次建档且退信、无其他路径 → C 储备（补到路径即回 B；大集团决策链长）',
    'PB-060': 'DATA GROUP SK：主业翻新大牌经纪，PLANET 为询价表单制边线、无库存证据 → C 储备',
    'PB-085': 'ESUS IT：内存 / SSD 电商，PLANET 类目为 FEN feed、样本款缺货 → 需求弱 → C 储备',
    'PB-091': 'DIGIRAM.PL（个体经营网店）：PLANET 全线为分销 feed 转售、个体微型、无进口 → C 储备',
}
MAIN = {'US', 'CA', 'TR', 'PL', 'GB', 'DE', 'FR', 'IT', 'ES', 'NL', 'BE', 'AT', 'CH', 'SE', 'NO', 'DK', 'FI', 'IE', 'PT', 'CZ', 'SK', 'HU', 'RO', 'BG', 'GR', 'HR', 'SI',
        'LT', 'LV', 'EE', 'LU', 'MT', 'CY', 'IS', 'RS', 'BA', 'ME', 'MK', 'AL', 'XK', 'MD', 'UA'}


def cat_of(code):
    for name, s in (('CONS', CONS), ('SHOP', SHOP), ('NOFIT', NOFIT), ('NOPATH', NOPATH), ('EVENT', EVENT)):
        if code in s:
            return name
    return None


def load_log():
    if not os.path.exists(LOG):
        return [], set()
    rows = list(csv.DictReader(open(LOG, encoding='utf-8-sig')))
    return rows, {(r['编号'], r['批次']) for r in rows}


def save_log(rows):
    f = ['编号', '公司', '国家', '复核前等级', '复核后等级', '批次', '日期', '结论与理由']
    with open(LOG, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=f)
        w.writeheader()
        w.writerows(rows)


def kv_text(r):
    kv = r.get('kv') or {}
    if not isinstance(kv, dict):
        return ''
    keep = []
    for k in ('类型', '产品', '品牌', '业务', '主营', '成立', '规模'):
        if kv.get(k):
            keep.append(f'{k}={str(kv[k])[:50]}')
    return '；'.join(keep)[:160]


def external(log, seen):
    recs = {}
    for repo in ('cctv', 'edgecore', 'mikrotik'):
        for r in json.load(open(os.path.join(XD, f'{repo}.json'), encoding='utf-8'))['records']:
            recs[r['code']] = r
    p = os.path.join(XD, 'overrides.json')
    ov = json.load(open(p, encoding='utf-8'))
    n = {'留B': 0, '打回C': 0}
    drop = set()
    for code, o in ov.items():
        rv = o.get('review') or {}
        if rv.get('status') != '待过' or rv.get('prio') != 3:
            continue
        r = recs.get(code, {})
        card = os.path.join(XD, 'research', f'{code}.json')
        j = json.load(open(card, encoding='utf-8')) if os.path.exists(card) else {}
        tf = re.sub(r'\s+', ' ', str(j.get('type_final') or r.get('type') or ''))[:70]
        gr = re.sub(r'\s+', ' ', str(j.get('grade_reason_final') or ''))[:60]
        c = cat_of(code)
        if c:
            reason = f'{CAT[c]}｜档：{tf}' + (f'；研究卡：{gr}' if gr else '')
            o['prev_reason'] = o.get('reason', '')
            o['grade'] = 'C'
            o['reason'] = f'Q-76 {BX} {DATE}：复核打回 C 储备（{c}）— {reason}'
            o['date'] = DATE
            o['batch'] = BX
            o['from'] = 'B'
            o['review'] = {'status': '打回C', 'prio': 3, 'date': DATE, 'batch': BX, 'note': reason, 'cat': c}
            after = 'C'
            drop.add(code)
            n['打回C'] += 1
        else:
            iso = (r.get('iso') or '')[:2].upper()
            region = '主区 / 欧洲' if iso in MAIN else '非主区（预付 100%）'
            kv = kv_text(r)
            reason = (f'桌面复核（来源库核对 + 研究卡）：{tf}' + (f'；研究卡：{gr}' if gr else '') + (f'；{kv}' if kv else '')
                      + f'；行业内 ✔ 对位 ✔ 有路径 ✔ → 留 B 普通跟·群发（{region}）')
            o['review'] = {'status': '留B', 'prio': 3, 'date': DATE, 'batch': BX, 'note': reason}
            after = 'B'
            n['留B'] += 1
        if (code, BX) not in seen:
            log.append({'编号': code, '公司': r.get('name', ''), '国家': r.get('country_zh', ''), '复核前等级': 'B', '复核后等级': after,
                        '批次': BX, '日期': DATE, '结论与理由': reason})
            seen.add((code, BX))
    json.dump(ov, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return n, drop


def planet(log, seen):
    rows = list(csv.DictReader(open(PCSV, encoding='utf-8-sig')))
    fields = list(rows[0].keys())
    n = {'留B': 0, '打回C': 0}
    drop = set()
    for r in rows:
        note = r.get('长期群复核') or ''
        if '待过·优先级 3' not in note:
            continue
        code = r['档案编号']
        if code in PLANET_C:
            reason = PLANET_C[code]
            r['人工定级'] = 'C'
            r['C级细分'] = '储备·复核打回'
            r['长期群复核'] = note.replace('待过·优先级 3', f'打回C·{BP} {DATE}（{reason}）')
            after = 'C'
            drop.add(code)
            n['打回C'] += 1
        else:
            ev = re.sub(r'\s+', ' ', r.get('信号（在卖什么品牌）') or '')[:90]
            reason = f'桌面复核（PLANET 关联证据 URL 已在表）：{ev}；在售 PLANET 交换机 = 行业内 ✔ 对位 ✔ 进口分销 ✔ → 留 B 普通跟·群发'
            r['长期群复核'] = note.replace('待过·优先级 3', f'留B·{BP} {DATE}（{reason}）')
            after = 'B'
            n['留B'] += 1
        if (code, BP) not in seen:
            log.append({'编号': code, '公司': r['公司名'], '国家': r['国家'], '复核前等级': 'B', '复核后等级': after,
                        '批次': BP, '日期': DATE, '结论与理由': reason})
            seen.add((code, BP))
    with open(PCSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    return n, drop


def prune_watch(drop):
    if not drop or not os.path.exists(WATCH):
        return 0
    rows = list(csv.DictReader(open(WATCH, encoding='utf-8-sig')))
    keep = [r for r in rows if r['编号'] not in drop]
    if len(keep) != len(rows):
        with open(WATCH, 'w', encoding='utf-8-sig', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(keep)
    return len(rows) - len(keep)


def main():
    for s in (CONS, SHOP, NOFIT, NOPATH, EVENT):
        for t in (CONS, SHOP, NOFIT, NOPATH, EVENT):
            assert s is t or not (s & t), s & t
    log, seen = load_log()
    before = len(log)
    nx, dx = external(log, seen)
    np_, dp = planet(log, seen)
    save_log(log)
    pruned = prune_watch(dx | dp)
    print(f'{BX} external {nx} | {BP} planet {np_} | log + {len(log) - before} = {len(log)} | 巡检表剔除 {pruned}')


if __name__ == '__main__':
    main()
