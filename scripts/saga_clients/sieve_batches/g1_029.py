#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 29 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 936–990 户（按综合分序，SC-1974 … SC-2123）。

构成：「品类不符 VC / DWDM / CCTV」0 触达约 35 户（线缆 / 无源 / 跳线 / CWDM / 光猫 / CCTV 为主 = 本职线或周边）、退信 8（域名多正常或有备用域 → 待巡检）、乌克兰 2（守界）、伊朗 4、中国大陆 1、学校 / 研究机构 2（Unsika、CERN）、表内国别错位 2（cern.ch 写智利；technoma.com.py 写阿根廷）。
  · 口径同桶 ⑥ 首批（分销 / 集成 + 中国品牌证据 + 有先例地区 → 闸 2 低优先；自有品牌线索 → 候选；真意向 → 候选；周边 / 无源 / 线缆 → 留 C；本职线 → dayjob_fit；退信但域正常 / 有备用域 → 留 C 待巡检）。
  · 候选 3 = Acceron IN（主动要 company profile + catalogue = 真意向）/ Zebeye → Zebronics IN（洪瑞商业 PoE 贴自有牌 Zebronics；zebeye.com 退信但 zebronics.com 正常 = 换址；Q-33）/ AMI-COM RU（朱姐客户，很多 ONV 型号未改 + 「Just」牌疑自有）→ 闸 2 查底数。
  · 永久 pass 0。
  · 其余留 C：本职线 dayjob_fit（Smart Security 16ch VC · Ace-Plus WDM 线缆 · Fiberoptic.co.il 光猫 · SK Inc MC 光开关 · GGI Raisecom OTN · Resco MC 板卡 · CERN CWDM SFP（瑞士，国别待核）· MSP-ICT CWDM · Unitrek CWDM / DWDM · Al-Darwish 8ch VC 域 dead · dwdm.ru）；线缆 / 无源 / 跳线 / CCTV（Bennett · Cables.com.tw · Grove · Goldennews · Irix · Kalaam BH 运营商 · Kishspark · MP Solution · Techmod · Zialcita · Eurolan · HD Telecom · Hyperline · Bridgecom · Astra KZ · PACTON · Sima Fiber IR 无源）；退信待巡检（Maxxtek IN · IDMR ID · Switchpoe IR 备用域 nktechco.com · AusPCMarket AU 平台 · IndustrialEthernet.info PH）；乌克兰 Btron / RTS 守界；中国大陆 P-techno（4 台工业交换机 → 私账线）；马来西亚 VEMAX / iPlanet 名牌分销无中国品牌证据；印度 Cogent（Weidmüller）/ JNT（含糊）/ Fusionnet 空白；俄罗斯 Aktivsb（转售 OSNOVO 等，OSNOVO 已入池 → 储备）/ Eltex（本土大厂同行，Simon 判不再跟进）/ Svir 装修公司 / Rostelecin 域 dead；巴西 HGK 域 dead / Logos 自动化；Technoma .py 国别待核；卢旺达 Vision MC；巴林 / 伊拉克 Cyber-Tek（Simon 判不再跟进，无客户明确拒绝 → 留 C）；学校 Unsika 16 槽机架。
  · 「stop」flag 来自 STOP_WORDS 文本命中 / Simon 备注「不再跟进」，均非客户明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_029.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批29_2026-10-29.md）
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

BATCH = 'G1-29'
DATE = '2026-10-29'
CODES = ["SC-1974", "SC-1977", "SC-1981", "SC-1998", "SC-2007", "SC-2008", "SC-2009", "SC-2010", "SC-2012", "SC-2014", "SC-2016", "SC-2017", "SC-2018", "SC-2019", "SC-2021", "SC-2023", "SC-2024", "SC-2025", "SC-2026", "SC-2027", "SC-2028", "SC-2029", "SC-2030", "SC-2033", "SC-2036", "SC-2038", "SC-2039", "SC-2040", "SC-2048", "SC-2062", "SC-2064", "SC-2065", "SC-2067", "SC-2068", "SC-2078", "SC-2079", "SC-2001", "SC-2084", "SC-2085", "SC-2089", "SC-2090", "SC-2096", "SC-2097", "SC-2098", "SC-2100", "SC-2101", "SC-2110", "SC-2111", "SC-2112", "SC-2114", "SC-2118", "SC-2120", "SC-2121", "SC-2122", "SC-2123"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-2021': ('candidate', '印度 Acceron（acceron.net；表内名「distributor」；主动索要 1/ company profile 2/ catalogue；8 推 0 回）：真意向 ✔ 分销主体 ✔ Simon 点名印度；→ 闸 2 查底数（zaubacorp）后点名回「已发资料」稿；低优先', []),
    'SC-2078': ('candidate', '印度 Zebeye → Zebronics（zebeye.com 退信；zebronics.com 正常 = 换址；洪瑞的商业 PoE / FS 贴 Zebronics 牌在卖）：自有品牌 = OEM 对象 ✔ Simon 点名印度 ✔ 对位 ✔；洪瑞现供 → Q-33 口径待 Simon；→ 闸 2 查底数（zaubacorp）+ 换 zebronics.com 地址', ['oem_target']),
    'SC-2111': ('candidate', '俄罗斯 AMI-COM（ami-com.ru；朱姐客户的；很多 ONV 型号都没变 + 「Just」这个牌子可能是他们自己的；主要 CCTV 本土品牌）：进口中国同类 ✔ 疑自有牌 ✔ Simon 点名俄罗斯；未触达 → 闸 2 查底数（rusprofile）核自有牌；俄语区收款待定，低优先', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-2008': ('keep_C', '中国大陆 P-techno（p-techno.cn；自建站询 4 台工业交换机）：国内单子只走私账 → 留 C（不入出口池）', []),
    'SC-2062': ('keep_C', '俄罗斯 Aktivsb（aktivsb.ru；OSNOVO（hasivo 代工）/ MC / E-link VC，整体较杂）：转售 OSNOVO 等，OSNOVO 本身已入池（SC-302）→ 留 C（储备；避免渠道冲突）', []),
    'SC-2065': ('keep_C', '俄罗斯 Eltex（eltex-co.com / .ru；工业以太网 / PON / 核心交换机自产；Simon 备注「不再跟进」；5 推 0 回）：本土大厂同行 → 留 C（不作 pass，无客户明确拒绝）', []),
    'SC-2064': ('keep_C', '伊拉克 Cyber-Tek（cyber-tek.net；工业 FS / PoE / 周边 ONV 的；Simon 备注「不再跟进 / Spam」）：无客户明确拒绝记录 → 留 C（储备，不作 pass）', []),
    'SC-2001': ('keep_C', '俄罗斯 Svir（svir.ru；装修公司，对 IP camera 感兴趣；WA 加不上；9 推 0 回）：终端装修公司 + CCTV → 留 C', []),
    'SC-2090': ('keep_C', 'CERN（cern.ch；表内「智利」实为瑞士 → 国别待核；CWDM SFP）：研究机构招标采购 + 光模块非 Saga 线 → 留 C + dayjob_fit（不作 pass）', ['dayjob_fit']),
    'SC-1981': ('keep_C', '印尼 Unsika 大学（unsika.ac.id；16 槽机架）：学校终端 + 机架非 Saga 线 → 留 C', []),
    'SC-2029': ('keep_C', '巴林 KEMS / Kalaam Telecom（kems.net / kalaam-telecom.com；CCTV / Networking）：运营商 → 留 C（巨头 / 运营商不永久 pass）', []),
    'SC-2017': ('keep_C', '乌克兰 Btron（btron.com.ua；工业品）：乌克兰 = 守界（非永久 pass）→ 留 C', []),
    'SC-2036': ('keep_C', '乌克兰 RTS（rts.ua；工业 FS / PoE / MC）：乌克兰 = 守界（非永久 pass）→ 留 C', []),
    'SC-2039': ('keep_C', '伊朗 Switchpoe（switchpoe.ir 退信；nktechco.com 正常；工业 FS、洪瑞 bypass、ONV 大口 FS）：备用域在 → 留 C 待巡检（伊朗收款路径另议）', []),
    'SC-1998': ('keep_C', '印度 Maxxtek Global（maxxtekglobal.com 域正常；退信；商业交换机 / ONU / OLT）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2027': ('keep_C', '印尼 IDMR（idmr.co.id 域正常；退信；很多牌子的 switch；2 推）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2089': ('keep_C', '澳大利亚 AusPCMarket（auspcmarket.com.au 域正常；退信；TP-Link / MC / SFP 销售平台）：网店 + 退信 → 留 C 待巡检', []),
    'SC-2123': ('keep_C', '菲律宾 IndustrialEthernet.info（域正常；退信；MC / SFP / FS 无源，Etherwan / E-link）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-1974': ('keep_C', '俄罗斯 Rostelecin-CC（rostelecin-cc.ru 域 dead；仅手机）：域死但无退信记录 → 留 C 待巡检', []),
    'SC-2096': ('keep_C', '巴西 HGK Rep（hgkrep.com.br 域 dead；「下月去深圳，给 Melody 的名片」旧线索）：域死无退信记录 → 留 C 待巡检', []),
    'SC-2110': ('keep_C', '沙特 Al-Darwish（al-darwish.com 域 dead；8ch VC；WA 加不上）：光端机 = 本职线 + 域死 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-2100': ('keep_C', 'Technoma（technoma.com.py；表内「阿根廷」实为 .py 巴拉圭 → 国别待核；行业相关但网站不细）：无品牌证据 + 零互动 → 留 C（储备）', []),
    'SC-2012': ('keep_C', '马来西亚 VEMAX Technology Sdn Bhd（vemax.com.my；ICT 分销多品牌，展会说第二天带 boss 来）：名牌分销 + 无中国品牌证据 + 非点名国 → 留 C（储备）', []),
    'SC-2026': ('keep_C', '马来西亚 iPlanet Solution Sdn Bhd（iplanetsolution.net；EPON / GPON 项目，主要分销 Cisco / Aruba / Nokia）：名牌分销 + 无中国品牌证据 → 留 C（储备）', []),
    'SC-2019': ('keep_C', '印度 Cogent Tech Solutions（cogenttechsolutions.in；在卖 Weidmüller；9 推 0 回）：欧洲品牌代理 + 无中国品牌证据 → 留 C（储备）', []),
    'SC-2048': ('keep_C', '印度 JNT Networks（jntnetworks.com；要 cheap fiber optic transmission solution，无具体产品；Trichy 地址 + 手机）：需求含糊 → 留 C（储备）', []),
    'SC-1977': ('keep_C', '沙特 Smart Security（smartsecurityco.com；16ch VC；WA 加不上）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2014': ('keep_C', '台湾 Ace-Plus（ace-plus.com；WDM / 线缆）：本职线 + 同行 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2023': ('keep_C', '以色列 Fiberoptic.co.il（需要光猫；连接器 / 周边）：本职线 + 周边 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2038': ('keep_C', '韩国 SK Inc（skinc.co.kr；无源配件 + MC / 光开关）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2068': ('keep_C', '印尼 GGI（ggi-idn.com；OTN / PON，从 Raisecom 买；1 推）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2084': ('keep_C', '巴基斯坦 Resco Reliable Security Systems（resco.com.pk / reliable.com.pk；MC / card / chassis）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2098': ('keep_C', '伊朗 MSP-ICT（msp-ict.com；CWDM / 线缆配件）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2101': ('keep_C', '澳大利亚 Unitrek（unitrek.com.au；CWDM / DWDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2118': ('keep_C', '俄罗斯 dwdm.ru（DWDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 29 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 936–990 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：「品类不符」0 触达约 35 户（线缆 / 无源 / 跳线 / CWDM / 光猫 / CCTV）、退信 8、乌克兰 2、伊朗 4、中国大陆 1、学校 / 研究机构 2、国别错位 2（cern.ch / technoma.com.py）。口径同桶 ⑥ 首批。候选 3 = Acceron（IN，索要资料 = 真意向）/ Zebronics（IN，洪瑞贴自有牌，退信换址 zebronics.com，Q-33）/ AMI-COM（RU，朱姐客户 + 疑自有牌 Just）；永久 pass 0。留 C：本职线 dayjob_fit、线缆 / 无源 / CCTV 周边、退信待巡检、乌克兰守界、国内私账线、名牌分销无中国品牌证据、Eltex 同行、学校 / 研究机构、运营商。「stop」flag / Simon「不再跟进」备注均非客户明确拒绝，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批29_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
