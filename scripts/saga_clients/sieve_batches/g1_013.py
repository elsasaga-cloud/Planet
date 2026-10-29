#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 13 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 56–110 户（按综合分序，SC-300 … SC-415）。

构成：俄罗斯 CCTV / 工业分销群发 8–18 次 0 回户、印度冷名单（0 触达）、韩国展会名片户（群发 16–45 次 0 回）、台湾 / 香港 / 韩国同行、澳新平台商。
  · 口径同桶 ⑥ 首批：四主区外默认留 C；「已进口中国 / 台湾同类品牌或自有品牌」且属俄罗斯 / 印度 / 韩国（或同区先例 ZA）→ 闸 2（低优先，俄语区收款待定）。
  · 候选 10 = OSNOVO RU（自有品牌 PoE / MC）/ ProSoft RU（大工业分销，三旺 · 迈威 · BDCOM）/ TD Tel RU（卖朱姐牌 PoE / MC）/ Videoglaz RU（CCTV 分销 + hasivo PoE）/ CompTek RU（大分销，有 DCN）/ Enercore IN（工业 FS 有海思的）/ Security Warehouse ZA（hasivo + CCTV）/ DGTAS KR（摄像头厂，Evelyn 微信在，要远程 PoE 配套）/ Alloy AU（自有品牌 MC / SFP / 工业 FS，多家在卖）/ HiFocus IN（自有品牌 CCTV，买丰润达商业 PoE）→ 闸 2 查底数。
  · 永久 pass 0。
  · 其余留 C：台 / 韩 / 港同行（Atop · CAMEO · CERIO · Eten · Dinkle · AddPac · Sollae · Altai · Allwin）/ 大平台（PB Tech · CTC）/ 巨头体系（Hyundai HDS · SAGE）/ 韩国名片户 16–45 推 0 回（CoreEdge · ELPKNEW · FST Korea（问 KC，Saga 无）· NST · GTS · Hiprotech）/ 印度 · 中亚 · 高加索 · 拉美 0 触达无进口证据 / 俄罗斯无品牌证据（rus-networks · inzer · iq-tools · c-sb）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_013.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批13_2026-10-29.md）
"""
import os
import sys
import json
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import sieve  # noqa: E402
from g1_005 import compose, SUB_WHY  # noqa: E402

SUB_WHY.insert(0, (r'用户判定不行', 'Simon 曾判不行 / 不相关；无刚性 pass 证据、企业邮箱域正常 → 留 C（不主动碰，除非出现新信号）'))

BATCH = 'G1-13'
DATE = '2026-10-29'
CODES = ["SC-300", "SC-302", "SC-304", "SC-305", "SC-306", "SC-307", "SC-309", "SC-311", "SC-190", "SC-314", "SC-323", "SC-324", "SC-326", "SC-332", "SC-333", "SC-335", "SC-336", "SC-337", "SC-341", "SC-346", "SC-350", "SC-353", "SC-354", "SC-356", "SC-359", "SC-360", "SC-373", "SC-374", "SC-375", "SC-376", "SC-377", "SC-381", "SC-382", "SC-386", "SC-387", "SC-389", "SC-390", "SC-392", "SC-395", "SC-396", "SC-397", "SC-398", "SC-399", "SC-400", "SC-401", "SC-403", "SC-404", "SC-405", "SC-408", "SC-409", "SC-411", "SC-412", "SC-413", "SC-414", "SC-415"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-302': ('candidate', '俄罗斯 OSNOVO（osnovo.ru；俄区自有品牌 PoE 交换机 / MC / 工业 FS，中国代工）：自有品牌 ✔ 对位 ✔ Simon 点名俄罗斯；群发 18 次 0 回 → 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', ['oem_target']),
    'SC-305': ('candidate', '俄罗斯 ProSoft（prosoft.ru；大型工业自动化分销，表内「三旺 · 迈威 · BDCOM」）：进口中国工业同类 ✔ 对位 ✔ 俄罗斯；群发 8 次 0 回 → 闸 2 查底数；俄语区收款待定，低优先', []),
    'SC-309': ('candidate', '俄罗斯 TD Tel（tdtel.ru；表内「卖朱姐牌子设备 PoE / MC / switch / 周边」= 在售中国同口型产品）：进口中国同类 ✔ 对位 ✔ 俄罗斯；群发 18 次 0 回 → 闸 2 查底数；俄语区收款待定，低优先', []),
    'SC-311': ('candidate', '俄罗斯 Videoglaz（videoglaz.ru；CCTV 为主 + hasivo 商业 PoE）：进口中国同类 ✔ 对位 ✔ 俄罗斯；群发 17 次 0 回 → 闸 2 查底数；俄语区收款待定，低优先', []),
    'SC-323': ('candidate', '俄罗斯 CompTek（comptek.ru；大型网络分销，表内「有 DCN 的，switch 等很多产品」）：进口中国同类 ✔ 对位 ✔ 俄罗斯；未触达 → 闸 2 查底数；俄语区收款待定，低优先', []),
    'SC-324': ('candidate', '印度 Enercore（enercore.co.in；表内「工业 FS 有海思的」= 在售中国方案工业机）：进口中国同类 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-382': ('candidate', '南非 Security Warehouse（securitywarehouse.co.za；Hasivo + CCTV 分销）：进口中国同类 ✔ 对位 ✔ + 同区先例 Duxbury / MiRO；群发 5 次 0 回 → 闸 2 查底数；低优先', []),
    'SC-387': ('candidate', '韩国 DGTAS（dgtas.co.kr；摄像头厂商，有客户项目，要「可远程控制的 PoE switch」配套；Evelyn 加了微信，KP Lily）：自有品牌摄像头 ✔ 微信在 ✔ Simon 点名韩国；邮件 37 次 0 回 → 闸 2 查底数（bizno）+ 改走微信；低优先', ['oem_target']),
    'SC-397': ('candidate', '澳大利亚 Alloy（alloy.com.au；自有品牌 MC / SFP / 光猫 / 工业 FS / 商业 PoE，「很多公司在卖他家的」）：自有品牌 = OEM 对象 ✔ 对位 ✔；群发 22 次 0 回 → 闸 2 查底数（ABN）；四主区外，低优先', ['oem_target']),
    'SC-413': ('candidate', '印度 HiFocus（hifocuscctv.com；自有品牌 CCTV，表内「买丰润达的商业 PoE」）：自有品牌 ✔ 进口中国同类 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', ['oem_target']),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-304': ('keep_C', '新西兰 PB Tech（pbtech.com / pbtech.co.nz；大型 IT 零售电商，很多牌子）：大平台；未触达 → 留 C', []),
    'SC-307': ('keep_C', '澳大利亚 SAGE Automation（sageautomation.com；大型自动化集成集团）：巨头体系 + 四主区外；未触达 → 留 C', []),
    'SC-346': ('keep_C', '亚美尼亚 Planet Fibers（planetfibers.com；BDCOM 高速交换机）：进口中国同类 ✔ 但非点名国别、未触达 → 留 C（储备）', []),
    'SC-354': ('keep_C', '利比亚 SmarTV（smartv.ly；问 HPE Aruba 设备，珊姐转）：品牌指定 + 区域外 → 留 C', []),
    'SC-375': ('keep_C', '俄罗斯 c-sb.ru（销售平台 / 集成商，出现朱姐客户产品 + NSGate）：身份不明（「似乎」）；群发 8 次 0 回 → 留 C（储备，闸 2 轮空）', []),
    'SC-377': ('keep_C', '台湾 Dinkle（dinkle.com；端子台制造商，工业 FS 为边角）：台湾厂商 → 留 C', []),
    'SC-386': ('keep_C', '韩国 CoreEdge Networks（coreedge.co.kr；要 2 光 10 电 PoE 网管 BT 90W / 4 光 8 电 10G，会英文；KP Moo Seok Choi）：规格询盘 ✔ 但群发 35 次 0 回、BT 90W Saga 不供 → 留 C（回信即候选）', []),
    'SC-389': ('keep_C', '韩国 ELPKNEW（elpknew.com；PoE switch；KP Kim Jinkook）：群发 45 次 0 回、无进口证据 → 留 C', []),
    'SC-390': ('keep_C', '韩国 FST Korea（fstkorea.com；PoE switch，问 KC 认证 = Saga 无 KC）：群发 45 次 0 回 → 留 C', []),
    'SC-392': ('keep_C', '韩国 NST（nstco.co.kr；工业 FS / PoE / MC / 机架 FS；KP Suksung Lee）：群发 31 次 0 回、无进口证据 → 留 C', []),
    'SC-396': ('keep_C', '韩国 AddPac（addpac.com；VoIP / 网络设备制造商）：同行；群发 23 次 0 回 → 留 C', []),
    'SC-399': ('keep_C', '台湾 Aristar（aristar.com.tw；官网打不开）：死站无退信；群发 9 次 0 回 → 留 C 待巡检', []),
    'SC-401': ('keep_C', '台湾 Atop Technologies（atoponline.com 域 no_mx / atop.com.tw；工业 MC / 光猫厂商，多办事处）：台湾同行 → 留 C', []),
    'SC-403': ('keep_C', '台湾 CAMEO（cameo.com.tw；网络 ODM）：台湾同行；群发 9 次 0 回 → 留 C', []),
    'SC-404': ('keep_C', '台湾 CERIO（cerio.com.tw；自有品牌 PoE / injector）：台湾同行；群发 9 次 0 回 → 留 C', []),
    'SC-405': ('keep_C', '澳大利亚 CTC Communications（ctccommunications.com.au；销售平台，很多牌子有 Wi-Tek，injector 较多）：平台商 + 四主区外；群发 15 次 0 回 → 留 C（储备）', []),
    'SC-408': ('keep_C', '台湾 Eten Technologies（etentech.com；工业 FS / MC / SFP 厂商）：台湾同行；群发 9 次 0 回 → 留 C', []),
    'SC-409': ('keep_C', '韩国 Sollae Systems（eztcp.com；串口服务器 / 网络模块厂商）：同行；群发 16 次 0 回 → 留 C', []),
    'SC-414': ('keep_C', '韩国 Hiprotech（hiprotech.co.kr；基本都是 Profibus，少量工业 FS）：对位弱；群发 23 次 0 回 → 留 C', []),
    'SC-415': ('keep_C', '韩国 Hyundai HDS（hyundaihds.co.kr；大口高速交换机）：集团体系；群发 23 次 0 回 → 留 C', []),
}


def main():
    assert len(CODES) == 55 and len(set(CODES)) == 55
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    rd = os.path.join(sieve.ROOT, 'data', 'saga_clients', 'research')
    V = {}
    for code in CODES:
        e = ents[code]
        assert e.get('grade') == 'C', code
        cur = sv.get(code) or {}
        assert not cur or cur.get('batch') == BATCH, ('already judged elsewhere', code, cur)
        if code in OVERRIDE:
            V[code] = OVERRIDE[code]
        else:
            p = os.path.join(rd, code + '.json')
            research = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None
            reason, tags = compose(e, research)
            V[code] = ('keep_C', reason, tags)
    for code in OVERRIDE:
        assert code in V, ('override not in batch', code)
    for code, (verdict, reason, tags) in V.items():
        assert verdict in ('pass_final', 'keep_C', 'candidate') and len(reason) >= 12, code
        cur = sv.get(code) or {}
        row = {'verdict': verdict, 'gate': 1, 'rule': 'G1', 'reason': reason, 'date': cur.get('date') or DATE, 'manual': True, 'batch': BATCH}
        if tags:
            row['tags'] = tags
        sv[code] = row
    cnt = sieve.save_sieve(sv)
    c = Counter(v[0] for v in V.values())
    tg = Counter(t for v in V.values() for t in v[2])
    L = [f'# C 池 · 闸 1 · 第 13 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 56–110 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：俄罗斯 CCTV / 工业分销群发 8–18 次 0 回户、印度冷名单 0 触达、韩国展会名片户群发 16–45 次 0 回、台 / 港 / 韩同行、澳新平台商。口径同桶 ⑥ 首批（四主区外默认留 C；进口中国 / 台湾同类或自有品牌 + 俄 / 印 / 韩或同区先例 → 闸 2 低优先）。候选 10 = OSNOVO / ProSoft / TD Tel / Videoglaz / CompTek（RU，收款待定）、Enercore / HiFocus（IN）、Security Warehouse（ZA）、DGTAS（KR，微信在）、Alloy（AU 自有品牌）；永久 pass 0。留 C：台 / 韩 / 港同行、大平台、巨头体系、韩国名片户 16–45 推 0 回、0 触达无进口证据、俄罗斯无品牌证据。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批13_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
