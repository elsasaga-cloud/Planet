#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 06 批（2026-10-29）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 166–275 户（按编号序，SC-1512 … SC-2241）。

口径与第 05 批完全相同（复用 g1_005 的组句规则 / 标签正则）：
  · 永久 pass 仅「纯无关行业 + 零互动」（科技孵化机构、云监控 SaaS）。
  · 候选 = 对位 ✔ + 主区 / 欧洲 + 硬信号（已在卖 Utepo / 宇航 / GXCOM / E-wind / acorid / Moxa 等 = 进口经验或工业分销主体；斯洛伐克第二大 CCTV 批发商）。
    Simon 曾「判不行」的 LogiLink / Entegron / Cygnus 仍进闸 2 —— 进口经验是硬信号，Simon 可按编号否决。
  · 其余留 C（守界 / 巨头 / 同行 / 板级 / 工程服务 / Q-33 ×3 / 光端机-WDM-CCTV 网店 → dayjob_fit）。

用法：python3 sieve_batches/g1_006.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批06_2026-10-29.md）
"""
import os
import sys
import json
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import sieve  # noqa: E402
from g1_005 import compose  # noqa: E402

BATCH = 'G1-06'
DATE = '2026-10-29'
CODES = ["SC-1512", "SC-153", "SC-1532", "SC-1533", "SC-154", "SC-155", "SC-1555", "SC-1556", "SC-1558", "SC-1568", "SC-157", "SC-1571", "SC-1574", "SC-1578", "SC-158", "SC-1581", "SC-159", "SC-1596", "SC-161", "SC-162", "SC-1626", "SC-1629", "SC-164", "SC-165", "SC-1650", "SC-1653", "SC-1655", "SC-166", "SC-1667", "SC-1685", "SC-1699", "SC-1702", "SC-1703", "SC-1706", "SC-1730", "SC-1733", "SC-1735", "SC-1737", "SC-1738", "SC-1739", "SC-1740", "SC-1741", "SC-1744", "SC-1745", "SC-1746", "SC-1748", "SC-1749", "SC-175", "SC-1754", "SC-1759", "SC-1761", "SC-1765", "SC-1768", "SC-1772", "SC-1787", "SC-181", "SC-182", "SC-183", "SC-1833", "SC-1837", "SC-1838", "SC-1839", "SC-1843", "SC-1844", "SC-1850", "SC-1851", "SC-1852", "SC-1854", "SC-1855", "SC-1857", "SC-1859", "SC-1861", "SC-1862", "SC-1864", "SC-1865", "SC-1868", "SC-187", "SC-1881", "SC-1924", "SC-1927", "SC-1933", "SC-1934", "SC-1935", "SC-1938", "SC-1939", "SC-194", "SC-1946", "SC-1965", "SC-198", "SC-2015", "SC-2020", "SC-2035", "SC-2070", "SC-2113", "SC-212", "SC-214", "SC-2143", "SC-215", "SC-216", "SC-2169", "SC-217", "SC-2178", "SC-218", "SC-220", "SC-221", "SC-2223", "SC-2228", "SC-223", "SC-2236", "SC-2241"]

OVERRIDE = {
    # ---- 永久 pass ----
    'SC-154': ('pass_final', '加拿大 Communitech（滑铁卢科技企业孵化 / 加速机构，非硬件渠道；Preseem 为另一家软件公司）8 次跟进零回复 → 纯无关行业，永久 pass', []),
    'SC-223': ('pass_final', '美国 3dEYE（云视频监控 SaaS 平台，不经销硬件）零互动 → 纯无关行业，永久 pass', []),
    # ---- 候选 → 闸 2 ----
    'SC-1556': ('candidate', '西班牙 Bunker Seguridad（安防分销 / 项目型，官网 Data transmission 栏有工业交换机）：欧洲 + 分销商主体 + 对位 ✔；曾退信但域名正常 → 闸 2 查底数 + 找新地址', []),
    'SC-1629': ('candidate', '立陶宛 Somi Networks（MC / SFP / 工业 FS / VC / 机架，宇航的设备，「中性、来自不同国内供应商、价格 OK」）：欧洲 + 已进口中国中性产品 + 对位 ✔；15 次跟进无回复（冷）→ 闸 2 查底数', ['dayjob_fit']),
    'SC-1706': ('candidate', '丹麦 ITV Security（产品线 Vivotek + 深圳 acorid 牌）：欧洲 + 已进口中国品牌 + 对位 ✔（安防网络）；15 次跟进无回复（冷）→ 闸 2 查底数', []),
    'SC-161': ('candidate', '德国 LogiLink（2direct GmbH 配件品牌，在卖宇航的工业 FS / optical switch = 自有品牌 OEM 买家）：德国主区 + 进口经验 + OEM（30% 口径）；Simon 曾判不行、15 次无回复 → 闸 2 查底数再定，Simon 可否决', ['oem_target', 'dayjob_fit']),
    'SC-1935': ('candidate', '德国 Leunig（工业 FS / MC / 串口，主要卖 Moxa）：德国主区 + 工业网络分销主体 + 对位 ✔；曾退信但域名正常 → 闸 2 查底数 + 找新地址', ['dayjob_fit']),
    'SC-1965': ('candidate', '土耳其 Entegron Network（PON / 商业 PoE，有 E-wind 和 GXCOM 的产品）：土耳其主区 + 已进口中国同类品牌 + 对位 ✔；Simon 曾判不行、2 次无回复 → 闸 2 查底数再定，Simon 可否决', []),
    'SC-2143': ('candidate', '塞浦路斯 Cygnus（SFP / 工商业 FS，主要是 Utepo 的）：欧洲 + 已进口中国同类品牌 + 对位 ✔；Simon 曾判不行、4 次无回复 → 闸 2 查底数，低优先', ['dayjob_fit']),
    'SC-1881': ('candidate', '斯洛伐克 TSS Group（CCTV 集成商，自称斯洛伐克第二大 CCTV 批发商；对 IP / analog over fiber 感兴趣）：欧洲 + 批发商体量 + PoE 对位；电话加不上、企业邮箱在 → 闸 2 查底数', ['dayjob_fit']),
    'SC-1855': ('candidate', '土耳其 Kıraç Bilişim（跟澳视买、知道天地伟业，要求先发 email）：土耳其主区 + 已进口中国安防品牌；9 次跟进无回复 → 闸 2 查底数，低优先', []),
    # ---- 需要专门说明的留 C ----
    'SC-181': ('keep_C', '立陶宛 Vikings Technology（SmartByte 经销名单内）→ Q-33 待裁，不主动碰；留 C', []),
    'SC-182': ('keep_C', '西班牙 WifiSafe（SmartByte 经销名单内）→ Q-33 待裁，不主动碰；留 C', []),
    'SC-175': ('keep_C', '英国 Heat & Combustion（终端，在用 SmartByte 产品）→ Q-33 + 终端；留 C', []),
    'SC-187': ('keep_C', '波兰 PLVision（SONiC / NOS 软件工程服务，Marvell 芯片；Simon 曾注「可以着重跟一下」）→ 不转售成品，最多样机；留 C（CENTEC / 白盒话题可借力，不群发）', []),
    'SC-1626': ('keep_C', '波兰 sklep.pl / iotsolution.pl（几个小有名气的牌子，外壳特别）：sklep.pl 域死、iotsolution.pl 正常；15 次无回复、无进口硬证据 → 留 C（波兰次优区，巡检再看）', []),
    'SC-1934': ('keep_C', '希腊 JMC Tech（商业 PoE 及周边）：曾退信但域名正常；无进口 / 分销硬证据 → 留 C', []),
    'SC-1737': ('keep_C', '比利时 Nexgen（主做模块，懂 DWDM，在为本地项目找供应商）→ 需求 DWDM / 模块（Saga 不供，Simon 本职强相关）；留 C', ['dayjob_fit']),
    'SC-1852': ('keep_C', '土耳其 İmteg（WDM / DWDM 10 个，2017 年起国际站）→ 需求 DWDM（本职可参考）；留 C', ['dayjob_fit']),
    'SC-1933': ('keep_C', '美国 Jabil（DWDM，用的瑞斯康达）→ 巨头 + DWDM（本职可参考）；留 C', ['dayjob_fit']),
    'SC-1735': ('keep_C', '斯洛伐克 Morez（要价目表，嫌北京某家光纤产品贵，$80/对）→ 需求为光端机类（本职可参考）；电话加不上；留 C', ['dayjob_fit']),
    'SC-212': ('keep_C', '英国 Essentia Technologies（软件外包公司自用 Cisco / Netgear，想找低价替代）17 次无回复 → 终端用户；留 C（来询被动报价）', []),
    'SC-1924': ('keep_C', 'adsensekorea.com（「公司介绍」来信，表记 Spam / 不再跟进 = 我方备注）→ 主体不明、不刚性；留 C', []),
    'SC-2241': ('keep_C', '法国 Faiveley Transport（轨道巨头，已并入 Wabtec；域名 dead）→ 守界轨道 + 巨头；留 C', ['dayjob_fit']),
    'SC-2020': ('keep_C', '大华荷兰分公司（需 M12 车载交换机 + 欧盟认证）→ 巨头 + 车载品类 Saga 无；留 C', []),
    'SC-1859': ('keep_C', '英国 Norbain（大型 IP CCTV 分销商；表记网站打不开）→ 体量大 + 冷；留 C（巡检官网）', ['dayjob_fit']),
}


def main():
    assert len(CODES) == 110 and len(set(CODES)) == 110
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
    L = [f'# C 池 · 闸 1 · 第 06 批（{DATE}）—— 桶 ⑤「企业邮箱 · 四主区+波兰」第 166–275 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5，与第 05 批相同；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 候选里 LogiLink（德国配件品牌，在卖宇航工业机 = OEM 买家）、Entegron（土耳其，E-wind / GXCOM）、Cygnus（塞浦路斯，Utepo）三户 Simon 曾判不行——进口经验是硬信号，先进闸 2 查底数，**Simon 可按编号否决**；pass 的 2 户同样可一句话恢复。'
         ' 本段大量「光端机 / WDM / CCTV 网店」（SC-1741…SC-1772、SC-1833…SC-1946）留 C + dayjob_fit；Q-33 渠道冲突 3 户（Vikings / WifiSafe / Heat & Combustion）留 C 不碰。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批06_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
