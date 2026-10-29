#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 09 批（2026-10-29）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 496–550 户（按编号序，SC-561 … SC-755）。

构成：几乎全是「群发冷名单无回应 · 名单内未触达」+ 少量「综合分低 · 已推送 9–29 次未回复」的欧美 / 土耳其 / 波兰光通信 · 安防 · 工业网络经销商。
  · 候选 8 = 已进口中国 / 台湾工业品牌（gsl.com.tr Kyland / annicom Kyland / amc-systeme 研华 / kst-bg 国内交换机 / newtechindustries Wi-Tek 退信待换址）或 主区分销主体（balticnetworks 工业 FS 多牌 / 100mega.cz Planet 渠道 / Leader Optec 中国采购负责人在表）→ 闸 2 查底数。
  · 永久 pass 0：本批无刚性 pass 证据（企业邮箱域全部正常、无婉拒 / 停发要求）。
  · 其余留 C：巨头 / 同行（R. STAHL · Sealevel · Comtrol · Artel · Cabur · Alarm.com）/ 本职线（VC · WDM · SDI 光端机 · CWDM SFP → dayjob_fit）/ 网店 · 平台 · 顾问中介 / 仅卖欧美日名牌。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_009.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批09_2026-10-29.md）
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

BATCH = 'G1-09'
DATE = '2026-10-29'
CODES = ["SC-561", "SC-562", "SC-563", "SC-565", "SC-567", "SC-571", "SC-575", "SC-586", "SC-587", "SC-589", "SC-591", "SC-598", "SC-603", "SC-614", "SC-617", "SC-624", "SC-628", "SC-629", "SC-634", "SC-639", "SC-645", "SC-656", "SC-658", "SC-659", "SC-662", "SC-665", "SC-671", "SC-685", "SC-686", "SC-687", "SC-691", "SC-693", "SC-694", "SC-695", "SC-696", "SC-700", "SC-704", "SC-709", "SC-710", "SC-716", "SC-728", "SC-732", "SC-733", "SC-734", "SC-735", "SC-736", "SC-737", "SC-741", "SC-744", "SC-745", "SC-748", "SC-752", "SC-753", "SC-754", "SC-755"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2 ----
    'SC-562': ('candidate', '美国 Baltic Networks（balticnetworks.com；很多牌子、工业 FS / SFP = 北美无线 / 网络分销主体）：主区 + 分销主体 + 对位 ✔；9 推 0 回 → 闸 2 查底数（冷户四条待坐实）', []),
    'SC-571': ('candidate', '土耳其 GSL（gsl.com.tr；国内 Kyland + Moxa 工业 FS / 工业控制）：四主区 + 已进口中国工业品牌 + 对位 ✔；11 推 0 回 → 闸 2 查底数', []),
    'SC-575': ('candidate', '保加利亚 KST（kst-bg.com；国内的交换机）：欧洲 + 已进口中国同类品牌 + 对位 ✔；13 推 0 回 → 闸 2 查底数，低优先', []),
    'SC-634': ('candidate', '美国 NewTech Industries（newtechindustries.com / newtechind.com；一部分工业 FS、Wi-Tek 的也有、比较多外壳）：主区 + 已进口中国同类品牌 + 对位 ✔；18 推全退信但两域名 MX 正常 → 闸 2 查底数 + 找新地址', []),
    'SC-656': ('candidate', '捷克 100MEGA（100mega.cz；主要是 Planet 的 = 捷克 IT 分销主体）：欧洲 + Planet 渠道 + 对位 ✔；名单内未触达 → 闸 2 查底数', []),
    'SC-671': ('candidate', '英国 Leader Optec（leaderoptec.com；passive / FTTH 为主的 trader，30–40% 业务在中国，表内邮箱 = 其国内负责人、负责采购 active 产品）：四主区 + 进口经验 + 中国采购 KP 在表 + 对位 ✔；未触达 → 闸 2 查底数', []),
    'SC-700': ('candidate', '德国 AMC Systeme（amc-systeme.de；主要是研华的 = 工业电脑 / 网络分销）：四主区 + 已进口台湾工业品牌 + 对位 ✔；名单内未触达 → 闸 2 查底数', []),
    'SC-704': ('candidate', '英国 Annicom（annicom.com；Kyland）：四主区 + 已进口中国工业品牌 + 对位 ✔；名单内未触达 → 闸 2 查底数', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-563': ('keep_C', '比利时 Belram（belram.be；MC / VC 14 槽机架，几个牌子含 Optronics）：光传输为主 = 本职线；冷名单未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-587': ('keep_C', '波兰 Proexe（proexe.pl；45 对 3G-SDI 光端机，2016 国际站）：本职线产品；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-589': ('keep_C', '美国 Proline Options（prolineoptions.com；MC「有人卖他们的」= 自有 MC 品牌）：仅 MC 单品对位弱（Saga 仅 STC-110XGE）；未触达 → 留 C，oem 备注', []),
    'SC-591': ('keep_C', '德国 R. STAHL（r-stahl.com；防爆电气巨头，自有网络产品线）：巨头采购体系 + 同行属性；未触达 → 留 C', []),
    'SC-598': ('keep_C', '美国 ZeroConnect（zeroconnect.com；从 Volktek 买 MC）：仅 MC 对位弱；未触达 → 留 C（若问交换机再起）', []),
    'SC-603': ('keep_C', '英国 Northern Blue Ltd（顾问 / 中介，名片似为介绍客户市场者，会一点中文）：非买家中介；17 推 0 回 → 留 C（非刚性 pass）', []),
    'SC-624': ('keep_C', '德国 reichelt elektronik（info@reichelt.de；大型电子元器件电商，TRENDnet 等）：大型电商采购体系；未触达 → 留 C', []),
    'SC-629': ('keep_C', '美国 Mimotik（mimotik.com；CCTV 为主 + 商业 PoE，似洪瑞换壳）：19 推全退信但域名 MX 正常 → 留 C 待巡检 / 换址' + Q33, []),
    'SC-645': ('keep_C', '美国 Sealevel Systems（sealevel.com；工业 I/O / IoT 自有品牌制造商）：同行属性；9 推 0 回 → 留 C', []),
    'SC-665': ('keep_C', '罗马尼亚 Civitas Systems Srl（civitasgroup.ro；问过 WDM、拿了 catalog、感觉不太懂）：WDM = 本职线；15 推 0 回 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-694': ('keep_C', '美国 Alarm.com（安防云平台巨头）：非经销买家 + 巨头体系；未触达 → 留 C', []),
    'SC-709': ('keep_C', '美国 Artel Video Systems（artel.com；MC / 多功能 VC / 广电传输自有品牌）：本职线 + 同行；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-734': ('keep_C', '意大利 Cabur（cabur.it；DIN 电源 / 接线端子制造商）：非经销买家；未触达 → 留 C', []),
    'SC-736': ('keep_C', '加拿大 CA Optronics Group（caoptronicsgroup.com；SFP / WDM）：本职线 / 光模块同行；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-737': ('keep_C', '加拿大 Caretek（caretek.ca；CWDM SFP / Network）：本职线为主；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-744': ('keep_C', '美国 Comtrol（comtrol.com；工业通信制造商，与 Moxa 合作；Skype / 电话加不上）：同行自有品牌；29 推 0 回 → 留 C', []),
    'SC-755': ('keep_C', '芬兰 Dasys（dasys.fi；多功能 VC 为主、在卖 OTS 产品）：本职线；未触达 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 09 批（{DATE}）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 496–550 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：几乎全是群发冷名单未触达 + 少量已推送 9–29 次未回复。候选 8 = 已进口中国 / 台湾工业品牌（GSL Kyland / Annicom Kyland / AMC 研华 / KST / NewTech Wi-Tek 退信待换址）或主区分销主体（Baltic Networks / 100MEGA Planet 渠道 / Leader Optec 中国采购 KP 在表）；'
         '永久 pass 0（无刚性证据）。留 C：巨头 / 同行（R. STAHL · Sealevel · Comtrol · Artel · Cabur · Alarm.com）、本职线（VC · WDM · SDI · CWDM SFP → dayjob_fit）、网店 / 平台 / 中介、仅卖欧美日名牌。「stop」flag = 文本命中，不作 pass 依据。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批09_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
