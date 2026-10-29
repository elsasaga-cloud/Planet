#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""External Clients · 长期客户群 批 LT-01（T29-U128，2026-10-29）：三库同一把尺子（Q-76；Simon U128 ③「OK」）。

尺子（与 Saga 同）：A = 核心（真人往来 / 成单 / 样品 / PI + 对位）；B = 普通跟（对位 + 活着 + 有路径）；C = 储备（活着但无路径 / 不对位 / 个人顾问 / 守界）；pass = 走。
外部库没有一户有往来记录（仅 W44 发送包 20 + S 箱来信 10 条信号）→ 没有 A；原 XA 优先级以 `x_prio` 留痕，发送包排序照旧。
规则：
  · XC（三闸已过）：sieve_x verdict pool / pool_watch → B（Simon「C 捞上来的直接定为 B」）+ 复核 待过 优先级 1；其余 XC 不动（储备 / 永久 pass）。
  · XA / XB：与 Saga 重叠（saga_dup）→ 随 Saga 主档等级；乌克兰 / 伊朗 / 叙利亚 → C 守界；无可用邮箱（emails_live 空）→ C 储备·无路径；
            标记「个人顾问」→ C 储备·个人；其余 → B（原 A 带 x_prio）。研究卡 deep=True 视为已过，否则 待过 优先级 3。
落点：data/external_clients/overrides.json {code: {grade, reason, date, batch, review, x_prio}}（render.py / sieve_x.py 的 final_grade 最高优先层）
      data/external_clients/长期客户群_LT-01_变更_2026-10-29.csv
之后：python3 scripts/external_clients/render.py。幂等：同 code 同 batch 覆写。
"""
import csv
import importlib.util
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data', 'external_clients')
SAGA = os.path.join(ROOT, 'data', 'saga_clients')
BATCH = 'LT-01'
DATE = '2026-10-29'
TAG = f'Q-76 {BATCH} {DATE}'
REPOS = [('cctv.json', 'CCTV-PoE'), ('edgecore.json', 'Edgecore'), ('mikrotik.json', 'mikrotik-info')]
GUARD = {'UA', 'IR', 'SY'}


def _mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    now = subprocess.check_output(['date', '-u', '+%H:%MZ']).decode().strip()
    rs = _mod('x_research_store', os.path.join(HERE, 'research_store.py'))
    cards = rs.all_cards()
    ovp = os.path.join(DATA, 'overrides.json')
    ov = json.load(open(ovp, encoding='utf-8')) if os.path.exists(ovp) else {}
    sx = json.load(open(os.path.join(DATA, 'sieve_x.json'), encoding='utf-8'))
    saga = {e['code']: e for e in json.load(open(os.path.join(SAGA, 'entities.json'), encoding='utf-8'))}
    rows, cnt = [], {}

    def tick(k):
        cnt[k] = cnt.get(k, 0) + 1

    def final(r):
        o = ov.get(r['code'])
        if o and o.get('batch') != BATCH:
            return o['grade']          # Simon 人工改级（非本批）优先
        c = cards.get(r['code'])
        return c['grade_final'] if c else r['grade']

    for fn, repo in REPOS:
        d = json.load(open(os.path.join(DATA, fn), encoding='utf-8'))
        for r in d['records']:
            if r.get('grade') == 'DELETE':
                continue
            code = r['code']
            o = ov.get(code)
            if o and o.get('batch') != BATCH:
                tick('skip_manual')
                continue
            cur = final(r)
            card = cards.get(code)
            deep = str((card or {}).get('deep', '')).lower() == 'true'
            flags = set(r.get('flags') or [])
            dup = r.get('saga_dup') or {}
            sv = (sx.get(code) or {}).get('verdict')
            new, reason, review, prio = None, '', '', 0
            if cur == 'C':
                if sv in ('pool', 'pool_watch') and dup.get('code') and dup['code'] in saga:
                    new, reason = saga[dup['code']]['grade'], f'{TAG}：与 Saga {dup["code"]} 同一公司 → 随主档等级 {saga[dup["code"]]["grade"]}（复核随主档，不单列）'
                elif sv in ('pool', 'pool_watch'):
                    new = 'B'
                    g2 = (sx[code].get('g2_reason') or sx[code].get('reason') or '')[:200]
                    reason = f'{TAG}：XC 三闸捞出 → B（Simon U128「直接定为 B」；长期客户群 · 普通跟）；闸 2：{g2}'
                    review, prio = '待过', 1
                else:
                    tick('XC 不动')
                    continue
            else:
                if dup.get('code') and dup['code'] in saga:
                    sg = saga[dup['code']]['grade']
                    if sg != cur:
                        new, reason = sg, f'{TAG}：与 Saga {dup["code"]} 同一公司 → 随主档等级 {sg}'
                    else:
                        tick('dup 同级不动')
                        continue
                elif r.get('iso') in GUARD:
                    new, reason = 'C', f'{TAG}：守界（{r.get("country_zh")}）→ C 储备，不发不跟'
                elif not r.get('emails_live'):
                    new, reason = 'C', f'{TAG}：无可用邮箱（无路径）→ C 储备；补到邮箱即回 B'
                elif '个人顾问' in flags:
                    new, reason = 'C', f'{TAG}：个人顾问 / 自由职业（非公司采购主体）→ C 储备'
                else:
                    new = 'B'
                    if cur == 'A':
                        reason = f'{TAG}：XA → B 普通跟（长期群 A = 真人往来 / 成单证据；外部库无往来）；原 XA 优先级留痕 x_prio'
                    else:
                        reason = f'{TAG}：XB 留 B（对位 + 活着 + 有路径）'
                    review, prio = ('已过·研究卡 deep', 0) if deep else ('待过', 3)
            if new == cur and not review:
                tick(f'{cur} 不动')
                continue
            ent = {'grade': new, 'reason': reason, 'date': DATE, 'batch': BATCH, 'from': cur}
            if review:
                ent['review'] = {'status': review, 'prio': prio, 'date': DATE}
            if cur == 'A' and new == 'B':
                ent['x_prio'] = 'XA'
            if ent['grade'] == cur and review:
                # 等级不变只记复核状态：仍写入 overrides（final_grade 结果一致），便于名册统一读取
                pass
            ov[code] = ent
            tick(f'{cur}->{new}' + ('' if not review else f' {review}'))
            rows.append([code, repo, r.get('name'), r.get('country_zh'), cur, new, reason, review, prio])
    json.dump(ov, open(ovp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    out = os.path.join(DATA, '长期客户群_LT-01_变更_2026-10-29.csv')
    with open(out, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['编号', '来源库', '公司', '国家', '原等级', '新等级', '理由', '复核', '优先级'])
        w.writerows(rows)
    print(BATCH, now, cnt, 'overrides', len(ov), 'rows', len(rows))


if __name__ == '__main__':
    main()
