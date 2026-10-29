#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 03 批（2026-10-29）—— 「实质回信」桶 18 户（reply_sub ≥ 1 且尚未判定）。

判定口径：docs/C池三闸筛选_方案_2026-10-29.md §3 + §5 补充。
  回过信的户只有两种硬 pass：客户明确要求移出邮件列表（SC-003）、表记「拉黑了」（闸 0 因有回信转闸 1，人判同 G0-3）；
  其余按巨头 / 伊朗 / 中国大陆 / 我方决定不跟 → keep_C；欧洲主区 + 回信 + 对位 → candidate。
标签：dayjob_fit（光端机 / DWDM / 光模块）、oem_target（贴牌渠道商）。

用法：python3 sieve_batches/g1_003.py   （幂等）
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G1-03'
DATE = '2026-10-29'
DJ = ['dayjob_fit']
OEM = ['oem_target']
BOTH = ['oem_target', 'dayjob_fit']

V = {
    'SC-003': ('pass_final', '美国 Westward Sales（Antaira / TRENDnet 增值分销）2025-10-13 Dawn Gumtow 明确要求「Please take us off your email list」→ 客户要求停发（Simon 刚性第 ③ 条）', []),
    'SC-007': ('keep_C', '英国 Born Electronics（2019 注册，Companies House 休眠账目；白牌工业交换机目录站，疑同行壳）→ 休眠 ≠ 注销；1 次回复后无后续；留 C', []),
    'SC-024': ('keep_C', '伊朗 Rayvarz（与 Teltonika / Ewind 合作，WA 已加，2025-01 回 price）→ 制裁口径不主动；活着', []),
    'SC-041': ('keep_C', '伊朗 Pelpaco（VC / AHD 为主，WA 已加，2024-05 回 more specs）→ 制裁口径；光端机类本职可参考', DJ),
    'SC-1428': ('pass_final', '阿联酋 Climax Oilfield（2 光 8 长壳询价、2 次回信）表记「9715696 55955 拉黑了」→ 关系已断死（G0-3 口径，因有回信转闸 1 后人判）', []),
    'SC-1446': ('candidate', '葡萄牙 LojaCCTV（卖多种外壳 PoE 的安防网店 / 分销，回过 1 次、16 次跟进）→ 欧洲主区 + 回信 + 对位 ✔ → 闸 2 查底数', OEM),
    'SC-151': ('keep_C', '俄罗斯 JSC COTTAGE（mail.ru，2V1D，回过 1 次，WA 加不上）→ 俄区 + 光端机类；留 C', DJ),
    'SC-1623': ('keep_C', '南非 Shopfiber / Southern Elements（SmartByte 10G MC / SFP 配件，回过 1 次）→ 表记「Paulo 不跟进了」为我方决定；留 C；光模块本职可参考', DJ),
    'SC-1798': ('pass_final', '哥伦比亚 Colbits（百兆工业 MC，2 次回信、21 次跟进）表记「5730457 79427 拉黑了」→ 关系已断死（G0-3 口径）', DJ),
    'SC-2365': ('pass_final', '荷兰 MediaChoice Group（8 路 SDI 视频光端机，回过 1 次）表记「+316 18 110037 拉黑了」→ 关系已断死（G0-3 口径）', DJ),
    'SC-2401': ('keep_C', '伊朗 SAE-net（ONV 工业 FS / BTON VC，回过 1 次）→ 制裁口径 + 表记 Spam / 不再跟进（我方决定）；留 C', []),
    'SC-2423': ('keep_C', 'Viettel Burundi（运营商，gmail，WA 已加，3 次回信，问 2 光 8 PoE 没成）→ 巨头运营商不 pass；区域外；留 C', []),
    'SC-2446': ('pass_final', '秘鲁 Jotas Comunicaciones（20 台 8 口 PoE + 70 台 24 口询价，回过 1 次）表记「96222 0939 已加 拉黑了」→ 关系已断死（G0-3 口径）', []),
    'SC-2485': ('pass_final', '乌干达 Trust Security（2 光 2 工业小壳，回过 1 次）表记「25675608 6452 已加 拉黑了」→ 关系已断死（G0-3 口径）', []),
    'SC-258': ('keep_C', 'IC Intracom / Intellinet 中国办公室（archieliu@icintracom.com，2 次回信：MC / 工业 FS / SFP / PoE 商业品）→ 中国大陆规则（国内单只走私账）；品牌商采购口在国内 → oem_target 留档', OEM),
    'SC-262': ('keep_C', 'Supermicro（2025-09 两位工程师真回：户外 PoE 温度 / 合规）→ 巨头不 pass；SOHO 体量难进其供应链；留 C 待其再询', []),
    'SC-550': ('keep_C', 'BT（Derrick Lewis 懂 WDM / VC / SFP，问 PoE 功率 + IPC，回过 1 次，17 次跟进）→ 巨头运营商不 pass；留 C', []),
    'SC-566': ('keep_C', 'Convergint（全美最大安防集成商，Allen Thorpe 回过 1 次，20 次跟进）→ 巨头不 pass；留 C 待其再询', []),
}


def main():
    assert len(V) == 18, len(V)
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    for code, (verdict, reason, tags) in V.items():
        assert code in ents and ents[code].get('grade') == 'C', code
        assert verdict in ('pass_final', 'keep_C', 'candidate'), (code, verdict)
        assert len(reason) >= 12, code
        cur = sv.get(code) or {}
        if cur.get('gate', 0) >= 1 and cur.get('batch') != BATCH:
            continue
        row = {'verdict': verdict, 'gate': 1, 'rule': 'G1', 'reason': reason, 'date': cur.get('date') or DATE, 'manual': True, 'batch': BATCH}
        if tags:
            row['tags'] = tags
        sv[code] = row
    cnt = sieve.save_sieve(sv)
    from collections import Counter
    c = Counter(v[0] for v in V.values())
    tg = Counter(t for v in V.values() for t in v[2])
    L = [f'# C 池 · 闸 1 · 第 03 批（{DATE}）—— 「实质回信」桶 18 户', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 + §5 补充；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 oem_target {tg["oem_target"]} / dayjob_fit {tg["dayjob_fit"]}。', '',
         '> 回过信的户只有两种硬 pass：客户明确要求移出邮件列表、表记「拉黑了」；巨头 / 伊朗 / 中国大陆 / 我方决定不跟 → 留 C。', '']
    for verdict, title in (('pass_final', '永久 pass'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批03_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
