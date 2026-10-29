#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 27 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 826–880 户（按综合分序，SC-1709 … SC-1815）。

构成：印度 0 触达冷名单约 22 户（networks / telecom 泛注 + 几户台湾 / 中国品牌经销）、越南 4、肯尼亚 / 坦桑尼亚 / 埃及 / 苏丹 / 孟加拉 / 巴基斯坦 / 斯里兰卡 / 尼泊尔零星、拉美 6、表内国别明显错位 4（mpl.ch / omniray.ch 写「智利」实为 .ch 瑞士；oak-integrator.lv 写「玻利维亚」实为 .lv 拉脱维亚；opensky.com.uy 写「乌干达」实为 .uy 乌拉圭）、退信 1、WA 加不上 2。
  · 口径同桶 ⑥ 首批（分销 / 集成 + 中国 / 台湾品牌证据 + 有先例地区 / 欧洲 → 闸 2 低优先；具体型号 / 数量询问 = 真需求 → 候选；泛注 / 名牌 / 周边 → 留 C；本职线 → dayjob_fit；国别错位 → 候选时同步「国别待核」）。
  · 候选 8 = Omni Ray CH（Moxa 工业分销，.ch 瑞士 国别待核）/ OAK Integrator LV（Korenix，.lv 拉脱维亚 国别待核）/ BBCPL IN（主要是 Planet 的）/ Cohesive Global IN（Wi-Tek + Grandstream）/ Mootek IN（三旺 + 长飞）/ Indraheera IN（洪瑞 → Q-33）/ Joohitha Power Systems IN（问过工业 2 光 2 = 具体需求）/ Habari TZ（常规千兆小外电 20 个 = 数量询问，具名 KP 2）→ 闸 2 查底数。
  · 永久 pass 0。
  · 其余留 C：印度泛注 networks / telecom（aarjay · babbler · convergentwireless · futurenetwings · klovertel · saimaa · nibe 商业 FS · rscommunication 配件 · Crossmatrix 安防 no_mx）+ 本职线（netlinkict SFP · sirindhrananth bypass MC · texonic 模块 · bhumientech bypass · racomm 光纤）+ Pantherun（工业 FS，疑自有品牌未核证 → 储备）；越南 icomteck 台湾牌子 / n-tek / nme.vn 谈合作 / —；肯尼亚 Unilink 华为 SFP+ 50 对（光模块非 Saga 线）/ Victorock Ruijie / Network Options Planet（无先例地区储备）；孟加拉 DOT / networkingbd BDCOM；巴基斯坦 Onsite E-link / Global Connect GPON；斯里兰卡 Network Store 店铺；尼泊尔 Max TV 宽带；埃及 Sama-Link D-Link / Afro Group WDM / 开罗美国大学（学校 EOC 询问）；苏丹 Mustafa Sultan；南非 Redstar D-Link MC / Centurion Micro 杂货 / Fibreway 布线；格鲁吉亚 Telco.ge 大口 FS 16 推；拉美 Prodelcom PE 进口公司 / SSYCSA PA Utepo / Terton MX 配件 / ITB BR WA 加不上 / YPF AR 国企巨头 Bidi MC / Opensky UY 国别待核；MPL .ch（瑞士，industrial network，无品牌证据 → 储备 + 国别待核）；乌克兰 StereoTV 守界；VNSEC 迪拜 CCTV 24 推 0 回；台湾 Lightwavelink bypass；波兰 PRT Gdańsk WDM（国别未填）；俄罗斯 NS-T 退信（tinko.ru 可换址 → 待巡检）。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_027.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批27_2026-10-29.md）
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

BATCH = 'G1-27'
DATE = '2026-10-29'
CODES = ["SC-1709", "SC-1710", "SC-1713", "SC-1714", "SC-1715", "SC-1717", "SC-1718", "SC-1719", "SC-1721", "SC-1722", "SC-1723", "SC-1724", "SC-1725", "SC-1726", "SC-1727", "SC-1807", "SC-1731", "SC-1734", "SC-1752", "SC-1753", "SC-1757", "SC-1760", "SC-1762", "SC-1764", "SC-1766", "SC-1767", "SC-1769", "SC-1773", "SC-1774", "SC-1778", "SC-1779", "SC-1780", "SC-1781", "SC-1783", "SC-1789", "SC-1790", "SC-1792", "SC-1794", "SC-1795", "SC-1796", "SC-1797", "SC-1799", "SC-1801", "SC-1802", "SC-1803", "SC-1804", "SC-1805", "SC-1808", "SC-1809", "SC-1810", "SC-1811", "SC-1812", "SC-1813", "SC-1814", "SC-1815"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-1714': ('candidate', 'Omni Ray（omniray.ch；表内「智利」实为 .ch 瑞士 → 国别待核；Moxa）：欧洲主区 ✔ 台湾工业品牌分销 ✔ 对位（STI 工业线）✔；未触达 → 闸 2 查底数（zefix / 官网 Impressum）并核国别', []),
    'SC-1713': ('candidate', 'OAK Integrator（oak-integrator.lv；表内「玻利维亚」实为 .lv 拉脱维亚 → 国别待核；Korenix）：欧洲 ✔ 台湾工业品牌集成 ✔ 对位 ✔；未触达 → 闸 2 查底数（firmas.lv / lursoft）并核国别', []),
    'SC-1795': ('candidate', '印度 BBCPL（bbcpl.in；主要是 Planet 的）：台湾品牌分销 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-1797': ('candidate', '印度 Cohesive Global（cohesiveglobal.com；Wi-Tek / Grandstream）：中国品牌分销 ✔ 对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-1807': ('candidate', '印度 Mootek（mootek.in；三旺 / 长飞；只发过改邮箱通知，无实质需求）：中国工业品牌分销 ✔ 对位 ✔ Simon 点名印度；→ 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-1804': ('candidate', '印度 Indraheera（indraheera.com / .org；洪瑞）：中国品牌分销 ✔ 对位 ✔ Simon 点名印度；洪瑞现供 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）；→ 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-1734': ('candidate', '印度 Joohitha Power Systems Pvt Ltd（gridx.in；光猫 + 工业 2 光 2）：具体型号需求 ✔（STI-154GP / STI-244DGGPM 同口型）对位 ✔ Simon 点名印度；未触达 → 闸 2 查底数（zaubacorp）；低优先', []),
    'SC-1803': ('candidate', '坦桑尼亚 Habari（habari.co.tz；常规千兆小外电 20 个；具名 KP liliani.mboya@ / eliangiringa@）：数量询问 = 真需求 ✔ 对位（STC-028GP）✔ 决策人可点名 ✔；→ 闸 2 查底数（官网 / 目录；BRELA ✗）；非点名国 → 低优先', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-1709': ('keep_C', 'MPL（mpl.ch；表内「智利」实为 .ch 瑞士 → 国别待核；industrial network）：欧洲主区 ✔ 工业对位 ✔ 但无品牌 / 进口证据 + 零互动 → 留 C（储备；§5 条数不够，回信即候选）', []),
    'SC-1764': ('keep_C', '印度 Pantherun（pantherun.com；工业 FS / 工业通讯）：疑自有品牌但表内未证 + 零互动 → 留 C（储备；巡检见自有品牌页即转候选 oem_target）', []),
    'SC-1812': ('keep_C', '俄罗斯 NS-T / Tinko（ns-t.ru 退信「发不过去」，域正常；tinko.ru 正常；串口 / MC / SFP / 工业 FS / PoE 多牌）：进口中国同类 ✔ 但退信 → 留 C 待巡检（换 tinko.ru 地址再试）', []),
    'SC-1769': ('keep_C', '乌克兰 StereoTV（stereotv.com.ua；商业 PoE；16 推 0 回）：乌克兰 = 守界（非永久 pass）→ 留 C', []),
    'SC-1773': ('keep_C', 'VNSEC（vnsec.us；表内沙特，网站载迪拜硅谷绿洲总部；CCTV；24 推 0 回）：品类 CCTV + 24 推 0 回 + 国别待核 → 留 C（储备）', []),
    'SC-1774': ('keep_C', '阿根廷 YPF（ypf.com；Bidi 60 km MC；WA 加不上）：国企能源巨头终端 + MC 非 Saga 线 → 留 C（巨头不永久 pass）', []),
    'SC-1792': ('keep_C', '埃及 开罗美国大学（aucegypt.edu；同轴转网口 EOC 询问）：学校终端 + EOC 非 Saga 线 → 留 C', []),
    'SC-1813': ('keep_C', 'Opensky（opensky.com.uy；表内「乌干达」实为 .uy 乌拉圭 → 国别待核；通讯 / 网络）：无品牌证据 + 零互动 → 留 C（储备）', []),
    'SC-1752': ('keep_C', '越南 Icomteck（icomteck.vn；卖台湾牌子的；9 推 0 回）：台湾品牌分销 ✔ 但四主区外非点名国 + 9 推 0 回 → 留 C（储备）', []),
    'SC-1809': ('keep_C', '肯尼亚 Network Options（network-options.co.ke；planet）：台湾品牌分销 ✔ 但无先例地区 + 零互动 → 留 C（储备）', []),
    'SC-1722': ('keep_C', '巴拿马 SSYCSA（ssycsa.com；有 Utepo 的）：进口中国同类 ✔ 但无先例地区 + 零互动 → 留 C（储备）', []),
    'SC-1726': ('keep_C', '肯尼亚 Unilink Communication（unilinkcommunication.com；1270/1310 华为 SFP+ 单纤模块 50 对）：光模块非 Saga 线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1710': ('keep_C', '印度 Netlink ICT（netlinkict.com；SFP，从 Opway 买）：光模块 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1721': ('keep_C', '印度 Sirindhrananth（sirindhrananth.com；bypass MC 周边）：本职线 + 周边 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1725': ('keep_C', '印度 Texonic（texonic.com；从 AOA 买模块）：光模块 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1757': ('keep_C', '台湾 Lightwavelink（lightwavelink.com.tw；bypass 光开关；amy@）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1766': ('keep_C', 'PRT Gdańsk（prt-gdansk.com；表内国别未填 → 波兰；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1790': ('keep_C', '埃及 Afro Group（afro-group.com；WDM 比较懂；老板手机在表）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1796': ('keep_C', '印度 Bhumi Entech（bhumientech.com；方案商 bypass）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1814': ('keep_C', '印度 Racomm（racomm.in；Fiber optics）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1781': ('keep_C', '南非 Fibreway Telecoms（fibre-way.co.za；Data and Fibre Optic Cabling）：布线商 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1718': ('keep_C', '南非 Redstar Africa（redstarafrica.com；几乎都是 D-Link 的 MC）：名牌 MC 为主 + 零互动 → 留 C', []),
    'SC-1723': ('keep_C', '格鲁吉亚 Telco.ge（CTC Union + 深圳 MC；大口 FS 名牌；无工业品；16 推 0 回）：MC 为主 + 16 推 0 回 → 留 C（储备）', []),
    'SC-1778': ('keep_C', '南非 Centurion Micro Electronics（cme.co.za；网站像杂货店；damian@ / peet@ 具名）：主体不明 + 零互动 → 留 C（储备）', []),
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
    L = [f'# C 池 · 闸 1 · 第 27 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 826–880 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：印度 0 触达约 22 户、越南 4、非洲 / 南亚零星、拉美 6、表内国别错位 4（.ch 瑞士写智利 ×2 / .lv 拉脱维亚写玻利维亚 / .uy 乌拉圭写乌干达）、退信 1、WA 加不上 2。口径同桶 ⑥ 首批。候选 8 = Omni Ray（CH，Moxa）/ OAK Integrator（LV，Korenix）/ BBCPL（IN，Planet）/ Cohesive Global（IN，Wi-Tek）/ Mootek（IN，三旺）/ Indraheera（IN，洪瑞 Q-33）/ Joohitha（IN，问工业 2 光 2）/ Habari（TZ，千兆 20 个 + 具名 KP）；永久 pass 0。留 C：印度泛注 / 本职线、Pantherun 疑自有品牌未证、越南 / 肯尼亚 / 孟加拉 / 巴基斯坦储备、乌克兰守界、YPF 巨头、学校终端、退信待巡检、国别待核。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批27_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
