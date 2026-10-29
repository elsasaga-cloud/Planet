#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 28 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 881–935 户（按综合分序，SC-1816 … SC-1973）。

构成：退信户 13（多数域名仍正常或有备用域 / WA → 待巡检；仅伊朗 Zaviyehdid 双域全死）、俄罗斯陈旧线索约 12 户（多数备注空白 / 电话）、台湾 / 马来西亚「品类不符」VC / MC / 无源 约 8 户（同行 / 本职线）、印度 / 孟加拉泛注、非洲 / 拉美 WA 加不上 6、巨头终端 2（MAN Middle East、Apar）、政府研究机构 1（C-DOT）。
  · 口径同桶 ⑥ 首批（分销 / 集成 + 中国 / 台湾品牌证据 + 有先例地区 → 闸 2 低优先；具体型号 / 数量询问 = 真需求 → 候选；退信但域名正常 / 有备用域 / 有 WA → 留 C 待巡检；退信 + 全部域名死 = 闸 0 刚性 → 永久 pass；本职线 → dayjob_fit）。
  · 候选 5 = Jjenka RU（MM GE converter 约 20 pcs 询价 = 数量询问，STC-110XGE 对位）/ Bay Datacom NP（问网管工业级 4 光 24 电 PoE = 具体型号）/ Anfatech VN（ONV 全线产品引进 = 整线进口商）/ Konect Soluciones EC（洪瑞 + 海硕 PON，厄瓜多尔有先例 SC-2402；Q-33）/ VoIPdevice RU（CCTV + Witek 很多 = 中国品牌分销，17 推 0 回 → 换稿）→ 闸 2 查底数。
  · 永久 pass 1 = Zaviyehdid IR（退信 + zaviyehdid.com / i30cctv.com 双域 no_mx = 退信且域名全死，闸 0 刚性 G0-2）。
  · 其余留 C：退信待巡检（Babayama SN 有 WA · Daboconnect SN · Ellipse BD 洪瑞 · MM Infotech IN · Optel AE · Alfaro Subsea ID 光端机 · Hitron KR（CCTV 厂 + Utepo，疑自有交换机 HAP-SW24F → 巡检换址后可转候选 oem_target）· Tron-Opto TW · Chuyenpoe VN 备用域 antinco.vn · LD Africa ZA · iTeam RU 备用域 leta.ru）；本职线 dayjob_fit（Sifens 光端机 · Silica WDM · CNCA 100G/200G DWDM 真互动 · SOL Global VC · AC Union · Bridge EG · C-DOT · Inteltec .lb · Redtag · Smartnet · Hoatech · AREEJ 2V1D · Ramat · Baycom · Catacomm）；巨头 / 政府（MAN Middle East 工业 8 电口导轨询问 — 斯洛文尼亚客户的客户 · Apar · C-DOT）；印度 / 孟加拉泛注（Sigma-Byte · Team Engineers · TN Instruments · Stel · Techland · GeoIPL）；俄罗斯陈旧（Beward 疑 CCTV 自有品牌未证 · DMTY · Legit Telecom · mall.ru 域 dead · MIP-SB 安保 · Mircod 主体未明 · Goldenage KZ Cisco · IT NET .kg 国别待核）；WA 加不上（Chipcom GT · Barmedas TZ · Sumtec PE）；Optimal PH（Simon 备注「不再跟进 / Spam」但无客户明确拒绝 → 留 C）；Fortune ET MC 投标；KVC / Belco MY；Legit / Mircod 等。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_028.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批28_2026-10-29.md）
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

BATCH = 'G1-28'
DATE = '2026-10-29'
CODES = ["SC-1816", "SC-1817", "SC-1818", "SC-1819", "SC-1820", "SC-1821", "SC-1822", "SC-1823", "SC-1840", "SC-1841", "SC-1845", "SC-1846", "SC-1858", "SC-1860", "SC-1755", "SC-1870", "SC-1871", "SC-1872", "SC-1876", "SC-1882", "SC-1883", "SC-1884", "SC-1887", "SC-1888", "SC-1896", "SC-1897", "SC-1900", "SC-1902", "SC-1904", "SC-1906", "SC-1909", "SC-1914", "SC-1917", "SC-1920", "SC-1922", "SC-1926", "SC-1929", "SC-1932", "SC-1944", "SC-1947", "SC-1950", "SC-1951", "SC-1953", "SC-1957", "SC-1960", "SC-1961", "SC-1962", "SC-1963", "SC-1964", "SC-1966", "SC-1968", "SC-1970", "SC-1971", "SC-1972", "SC-1973"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-1755': ('candidate', '俄罗斯 Jjenka（jjenka.com；「need MM GE converter about 20pcs, price information」；8 推 0 回）：数量询问 = 真需求 ✔ 对位（STC-110XGE 千兆 MC）✔ Simon 点名俄罗斯；→ 闸 2 查底数（rusprofile）；俄语区收款待定，低优先', []),
    'SC-1871': ('candidate', '尼泊尔 Bay Datacom Solutions Pvt Ltd（baydatacom.com；问网管工业级 4 光 24 电 PoE 交换机）：具体型号需求 ✔ 对位（STC-4424GCPM 商规 / STI 工业线近似，如实说明）✔；未触达 → 闸 2 查底数（官网 / 目录）；非点名国 → 低优先', []),
    'SC-1883': ('candidate', '越南 Anfatech（anfatech.com.vn；ONV 的全线产品引进 + QNAP；8 推 0 回）：中国品牌整线进口商 ✔ 对位 ✔（同批 Metsuki 先例）；→ 闸 2 查底数（masothue）；非点名国 → 低优先，换稿点名', []),
    'SC-1900': ('candidate', '厄瓜多尔 Konect Soluciones（konectsoluciones.com；洪瑞 + 买的海硕的 PON；1 推 0 回）：中国品牌进口 ✔ 对位 ✔ 厄瓜多尔有先例（SC-2402）；洪瑞现供 → Q-33 口径待 Simon；→ 闸 2 查底数（supercias 镜像 / 官网 RUC）；低优先', []),
    'SC-1917': ('candidate', '俄罗斯 VoIPdevice（voipdevice.ru；主要是 CCTV，Witek 的很多；17 推 0 回）：中国品牌分销 ✔ 对位 ✔ Simon 点名俄罗斯；17 推 0 回 → 闸 2 查底数后换稿点名；俄语区收款待定，低优先', []),
    # ---- 永久 pass（闸 0 刚性补判）----
    'SC-1823': ('pass_final', '伊朗 Zaviyehdid（zaviyehdid.com / i30cctv.com 双域均 no_mx；退信「发不过去」；卖很多洪瑞的产品）：退信 + 全部域名死 = 闸 0 刚性 G0-2 → 永久 pass（无任何可达路径）', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-1840': ('keep_C', '塞内加尔 Babayama（babayama.com 无 MX；退信；很多光路 + 大口 FS；官网有 WA 按钮 +221 77 379 61 76）：退信但 WA 路径在 → 非刚性 → 留 C 待巡检', []),
    'SC-1845': ('keep_C', '塞内加尔 Daboconnect（daboconnect.com 域正常；退信；销售平台 丰润达 / Comfast 商业 PoE）：退信但域正常 + 无换址线索 → 留 C 待巡检', []),
    'SC-1846': ('keep_C', '孟加拉 Ellipse Tech Ltd（ellipsetechltd.com 域正常；退信；交换机方案商，似乎是洪瑞的商业 FS）：退信待巡检 + 洪瑞 Q-33 → 留 C', []),
    'SC-1858': ('keep_C', '印度 MM Infotech（mm-infotech.in 域正常；退信；switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-1860': ('keep_C', '阿联酋 Optel TSS（opteltss.ae 域正常；退信；17 推）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-1870': ('keep_C', '印尼 Alfaro Subsea（alfarosubsea.com 域正常；退信；1V1D 阿里巴巴询盘；万隆地址 + 手机在表）：光端机 = 本职线 + 退信 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-1896': ('keep_C', '韩国 Hitron（hitron.co.kr 域正常；退信；CCTV 厂 + Utepo 工业 FS；官网 PDF HAP-SW24F 疑自有交换机型号）：韩国自有品牌 = OEM 对象线索 ✔ 但退信 + 无换址 → 留 C 待巡检（巡检取到新地址即转候选 oem_target）', ['oem_target']),
    'SC-1914': ('keep_C', '台湾 Tron-Opto（tron-opto.com.tw 域正常；退信；MC / 工业 FS；8 推）：台湾同行 / 制造商 + 退信 → 留 C 待巡检', []),
    'SC-1926': ('keep_C', '越南 Chuyenpoe（chuyenpoe.com 域 dead；antinco.vn 正常；退信；有 Utepo 的）：备用域在 → 留 C 待巡检（换 antinco.vn 再试）', []),
    'SC-1953': ('keep_C', '南非 LD Africa Pty Ltd（ldafrica.com 域正常；退信；工业 FS + Milesight IPC + Hored 商业 PoE；8 推）：进口中国同类 ✔ 但退信 + 无换址 → 留 C 待巡检', []),
    'SC-1968': ('keep_C', '俄罗斯 iTeam / Leta（iteam.guru 退信；leta.ru 正常；PoE switch；17 推）：备用域在 → 留 C 待巡检（换 leta.ru 再试）', []),
    'SC-1841': ('keep_C', '阿根廷 CNCA（cnca.com.ar；谈过 100G / 200G 点对点 100 km 2 芯非相干低价方案 + 1.6T 一体式 + 上下波，6COM 客户用信泰）：DWDM 真互动 = 本职线 → 留 C + dayjob_fit（交换机线零需求）', ['dayjob_fit']),
    'SC-1902': ('keep_C', '阿联酋 MAN Middle East（man-middleeast.com 无 MX；man.eu 正常；问工业 8 电口导轨安装；珊姐转，大概率是斯洛文尼亚客户的客户）：巨头终端（卡车集团）+ 已有渠道客户在供 → 留 C（巨头不永久 pass；不越过渠道）', []),
    'SC-1888': ('keep_C', '印度 C-DOT（cdot.in；WDM）：政府电信研发中心 = 守界 + 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1884': ('keep_C', '印度 Apar Industries（apar.com；Networking）：大型集团终端 + 无互动 → 留 C（巨头不永久 pass）', []),
    'SC-1904': ('keep_C', '菲律宾 Optimal（optimal.com.ph；主要从 FS / Etherwan / Planet 买，分销商；回复里有详细联系方式；Simon 备注「不再跟进 / Spam」）：台湾品牌分销 ✔ 但 Simon 判不再跟进且无客户明确拒绝记录 → 留 C（储备；不作 pass）', []),
    'SC-1962': ('keep_C', '俄罗斯 Beward（beward.ru；「视频监控莫斯科负责人」）：疑俄本土 CCTV 自有品牌但表内未证 + 零互动 → 留 C（储备；巡检见自有品牌页即转候选 oem_target）', []),
    'SC-1950': ('keep_C', 'IT NET（itnet.kg；表内俄罗斯，.kg 吉尔吉斯 → 国别待核；仅手机 / Skype）：无品牌证据 + 国别待核 → 留 C', []),
    'SC-1897': ('keep_C', 'Inteltec（inteltec.com.lb；表内「利比亚」实为 .lb 黎巴嫩 → 国别待核；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1971': ('keep_C', '俄罗斯 mall.ru（域 dead；贸易公司）：域死但无退信记录 → 留 C 待巡检', []),
    'SC-1973': ('keep_C', '俄罗斯 Mircod（mircod.com；「本土优化设计师」备注含糊，主体未明）：不确定是否买家 → 留 C（不作 pass）', []),
    'SC-1816': ('keep_C', '刚果 Sifens（sifens.com；3 对 analog 1V1D；网站不相关）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1818': ('keep_C', '阿根廷 Silica Networks（silicanetworks.com；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1876': ('keep_C', '墨西哥 SOL Global（solglobal.com.mx；very interested in VC；WA 加不上）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1882': ('keep_C', '台湾 AC Union（ac-union.com；无源配件 / 光模块）：本职线 + 同行 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1887': ('keep_C', '埃及 Bridge Technologies（bridgetechnologies.com；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1906': ('keep_C', '巴基斯坦 Redtag（redtag.com.pk；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1909': ('keep_C', '赞比亚 Smartnet（smartnet.co.zm；Fiber optic）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1932': ('keep_C', '台湾 Hoatech（hoatech.com.tw；VC / MC；9 推 0 回）：本职线 + 同行 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1947': ('keep_C', '阿联酋 AREEJ（areej-group.net / .com；买 2V1D，会中文 / 法语，伊拉克裔迪拜；WA 加不上）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1957': ('keep_C', '沙特 Ramat（ramat.biz；need price list for V.C. / projector；WA 加不上）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1960': ('keep_C', '台湾 Baycom（baycom.com.tw；MC / SFP / 无源 / 线缆）：本职线 + 同行 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1963': ('keep_C', '马来西亚 Catacomm（catacomm-corp.com；VC / SFP / MC / 机架；官网 WA 未加）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 28 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 881–935 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：退信户 13（多数域名正常 / 有备用域 / 有 WA → 待巡检）、俄罗斯陈旧线索约 12、台湾 / 马来西亚 VC / MC / 无源 同行约 8、印度 / 孟加拉泛注、WA 加不上 6、巨头终端 2、政府研发 1。口径同桶 ⑥ 首批。候选 5 = Jjenka（RU，MM GE converter 20 pcs）/ Bay Datacom（NP，问 4 光 24 电 PoE）/ Anfatech（VN，ONV 全线）/ Konect Soluciones（EC，洪瑞 + 海硕 Q-33）/ VoIPdevice（RU，Witek 很多）；永久 pass 1 = Zaviyehdid（IR，退信 + 双域全死）。留 C：退信待巡检（含 Hitron KR 疑自有交换机 → 换址后可转 oem_target）、本职线 dayjob_fit、巨头 / 政府、印度泛注、俄罗斯陈旧、WA 加不上、国别待核。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批28_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
