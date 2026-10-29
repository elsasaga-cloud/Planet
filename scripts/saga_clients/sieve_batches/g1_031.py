#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 31 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 1046–1100 户（按综合分序，SC-2337 … SC-2800）。

构成：「用户判定不行 / 不相关」22 户（本批首次大量进入 — 按 U115 全部过筛：真不行才 pass，自有品牌 / 贴牌者反而是 OEM 对象）、退信 19（域名多正常 / 有备用域 / 有微信 → 待巡检；3 户单域全死 → 永久 pass）、巨头 6（Omron · Samsung/S1 · Bosch · Alltron · WAGO · NTT-AT）、乌克兰 3（守界）、WA 加不上 6、国别错位 4（alltron.ch / fabrimex-systems.ch 写智利 = 瑞士；dtcgroup.com.ua 写俄罗斯；polinnov.ch 写摩洛哥）。
  · 口径同桶 ⑥ 首批 + 本批新增「贴牌 / 自有品牌 = OEM 对象」线：Simon 备注里的「带标卖」「有人卖他们的」「主要是 hasivo 的商业 PoE」即自有品牌证据 → 候选 oem_target（目标顺序 OEM 品牌商 > 有进口经验者 > 分销商）。
  · 候选 4 = Tactio HK（工业 FS 国内外壳贴自有牌，「有人卖他们的」）/ Protech GE（「主要是 ONV 的 带标卖」）/ EverFocus TW（台湾安防品牌商，商业 PoE 自有牌）/ RVi Group RU（俄罗斯 CCTV 品牌，「主要是 hasivo 的商业 PoE」贴牌；19 推 0 回 → 换稿）→ 闸 2 查底数。
  · 永久 pass 3 = CCTVapp VN（cctvapp.net no_mx + wificamera.vn nxdomain + 退信）/ KVMswitches IN（唯一域 no_mx + 退信）/ Optimaunit RU（唯一域 no_mx + 退信）—— 均为域名即户名、无公司名 / 电话 / WA 的死户，闸 0 刚性 G0-2。
  · 其余留 C：退信但有公司名 / 备用域 / 微信（Al Keyam Electronics LLC AE 海康分销 → 公司名可查 · Fibcom IN null MX 疑并入他司 · Discomp CL 备用域 discomp.cl · NQC VN · Padtec BR 备用域 · SLT 运营商 · Unified Africa TZ · Arsitec BR 已加微信 · AM-Trading RU 手机 / Skype · Addhia OM 光猫 · GVision / ViewVision / Mehta / Mazenet IN · Crystal BD · Bicomsi MX 备用域）；巨头（Omron · Samsung/S1 问 PoE 代理 44 推 0 回 · Bosch · Alltron CH · WAGO · NTT-AT）；乌克兰守界（STC Kiev · Yavir · DTC Group .com.ua）；本职线 dayjob_fit（Stilsoft VC · Ciel CM 16ch VC · Aquatronics KE VC · Polinnov 120 km 摄像机传输 · Versia-IT WDM · iSunjoin MC · Huatenmax 国内 DWDM → 私账线）；「用户判定不行」留 C（Powertec AU ONV / 锐捷进口商 22 推 0 回 → 储备换稿 · Microtech PK 把 Saga 当买家 · Camerahainam VN 域 dead · Fabrimex CH 工业 FS 无中国品牌证据 · Beyondtech TW Mlis 同行 · Conetec RU 名牌 · hk.ge / Innocom GE 平台 · Quick Steps SA 问 L3 工业 = Saga 无 · Computech BR 网店 · Videomarin 高 IP 延长器 · Skyline IN ISP · CNI ID）。
  · 「stop」flag / Simon「不再跟进」「不行」备注均非客户明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_031.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批31_2026-10-29.md）
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

BATCH = 'G1-31'
DATE = '2026-10-29'
CODES = ["SC-2337", "SC-2338", "SC-2342", "SC-2346", "SC-2352", "SC-2366", "SC-2367", "SC-2370", "SC-2373", "SC-2374", "SC-2376", "SC-2335", "SC-2409", "SC-2454", "SC-2476", "SC-2493", "SC-2494", "SC-2495", "SC-2496", "SC-2497", "SC-2499", "SC-2501", "SC-2503", "SC-2513", "SC-2524", "SC-3321", "SC-2532", "SC-2533", "SC-2539", "SC-2547", "SC-2556", "SC-2564", "SC-2569", "SC-2587", "SC-2651", "SC-2659", "SC-2665", "SC-2672", "SC-2681", "SC-2682", "SC-2687", "SC-2693", "SC-2694", "SC-2695", "SC-2698", "SC-2705", "SC-2730", "SC-2749", "SC-2751", "SC-2753", "SC-2783", "SC-2791", "SC-2792", "SC-2793", "SC-2800"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（OEM 对象线）----
    'SC-2587': ('candidate', '香港 Tactio（tactio.net；工业 FS / PoE / MC 周边；「工业 FS 看着像国内外壳，有人卖他们的」= 贴自有牌；8 推 0 回）：自有品牌 = OEM 对象 ✔ 对位 ✔；→ 闸 2 查底数（HK 公司注册 / 官网）后换 OEM 稿；低优先', ['oem_target']),
    'SC-2687': ('candidate', '格鲁吉亚 Protech（protech.com.ge；「主要是 ONV 的，带标卖」；16 推 0 回）：贴自有牌 = OEM 对象 ✔ 对位 ✔；非点名国 → 闸 2 查底数（官网 / 目录）后换 OEM 稿；低优先', ['oem_target']),
    'SC-2695': ('candidate', '台湾 EverFocus（everfocus.com；台湾安防品牌商，安防 / 通讯较杂，商业 PoE 自有牌）：品牌商 = OEM 对象 ✔ 对位 ✔（台湾 OEM 先例：DGTAS / HiSharp / AVTECH 已入池）；→ 闸 2 查底数（twincn）；低优先', ['oem_target']),
    'SC-2730': ('candidate', '俄罗斯 RVi Group（rvigroup.ru；俄罗斯 CCTV 品牌，「主要是 hasivo 的商业 PoE」= 贴牌；19 推 0 回）：自有品牌 = OEM 对象 ✔ Simon 点名俄罗斯 ✔；→ 闸 2 查底数（rusprofile）后换 OEM 稿；俄语区收款待定', ['oem_target']),
    # ---- 永久 pass（闸 0 刚性补判：域名即户名 + 全部域名死 + 退信）----
    'SC-2370': ('pass_final', '越南 CCTVapp（cctvapp.net no_mx；wificamera.vn nxdomain；退信「发不过去」；智能监控 / smart home）：退信 + 全部域名死 + 无公司名 / 电话 → 闸 0 刚性 G0-2 → 永久 pass', []),
    'SC-2493': ('pass_final', '印度 KVMswitches（kvmswitches.co.in 唯一域 no_mx；退信；Bypass）：退信 + 域名死 + 无公司名 / 电话 → 闸 0 刚性 G0-2 → 永久 pass', []),
    'SC-2659': ('pass_final', '俄罗斯 Optimaunit（optimaunit.ru 唯一域 no_mx；退信；CCTV 类）：退信 + 域名死 + 无公司名 / 电话 → 闸 0 刚性 G0-2 → 永久 pass', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-2501': ('keep_C', '阿联酋 Al Keyam Electronics LLC（hikvision-uae.com no_mx + 退信；海康分销商，take catalog）：品牌经销域名死但公司名可查 → 非刚性 → 留 C 待巡检（找官网换址）', []),
    'SC-2524': ('keep_C', '印度 Fibcom（fibcom.com null MX + 退信；WDM 厂商）：null MX = 疑并入他司 / 换域 → 留 C 待巡检 + dayjob_fit（本职线同行）', ['dayjob_fit']),
    'SC-2454': ('keep_C', '智利 Discomp Industrial（discompindustrial.com nxdomain；discomp.cl 正常；退信；一直在用 Trendnet）：备用域在 → 留 C 待巡检（换 discomp.cl）', []),
    'SC-2374': ('keep_C', '越南 NQC Telecom（nqctelecom.vn 正常；ngctelecom.vn nxdomain；退信；WDM 用 PacketLight + 工业交换机）：退信待巡检 + 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2494': ('keep_C', '巴西 Padtec（padtec.com.br 退信；padtec.com 正常；WDM 制造商）：本职线同行 + 备用域 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-2497': ('keep_C', '斯里兰卡 SLT（slt.lk 域正常；退信；光派产品）：运营商 = 巨头线（不永久 pass）→ 留 C', []),
    'SC-2499': ('keep_C', '坦桑尼亚 Unified Africa（unifiedafrica.co.tz 正常；退信；telecom networking）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2705': ('keep_C', '巴西 Arsitec（arsitec.com.br 域正常；退信；用瑞斯康达的 DWDM；Simon 领英邀请看展并已加微信；手机在表）：微信路径在 + 本职线 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-2547': ('keep_C', '俄罗斯 AM-Trading（am-trading.ru 域正常；退信；手机 / Skype 在表）：退信但有电话路径 → 留 C 待巡检', []),
    'SC-2681': ('keep_C', '阿曼 Addhia（addhia.com 域正常；退信；光猫；8 推）：退信待巡检 + 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2337': ('keep_C', '印度 GVision CCTV（gvisioncctv.com 域正常；退信；PoE switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2338': ('keep_C', '印度 Mehta Group（mehtagroup.net 域正常；退信；跳线 / EDFA / 华为 switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2342': ('keep_C', '印度 ViewVision India（viewvisionindia.com 域正常；退信；PoE switch）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2373': ('keep_C', '印度 Mazenet Deck（mazenetdeck.com 域正常；退信；bypass switch / IoT）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2346': ('keep_C', '孟加拉 Crystal Vision Solutions（crystalcomputers.com.bd 域正常；退信；DAC 线缆阿里巴巴询盘）：退信 + 无换址线索 → 留 C 待巡检', []),
    'SC-2682': ('keep_C', '墨西哥 Bicomsi（bicomsi.com.mx nxdomain；pagina.mx 正常；有名牌子工业 FS 分销商；1 推）：备用域在 + 无中国品牌证据 → 留 C 待巡检', []),
    'SC-2376': ('keep_C', '日本 Omron（omron.com；SMB Data；2 推）：巨头终端 → 留 C（巨头不永久 pass）', []),
    'SC-2409': ('keep_C', '韩国 Samsung / S1 Corp（xo.kr nxdomain；samsung.com 正常；MIKI CHOI 会中文，问 PoE switch 在韩有无代理 / 客户；44 推 0 回）：巨头集团安防子公司 → 留 C（巨头不永久 pass；44 推 0 回 → 停推，仅观察）', []),
    'SC-2539': ('keep_C', '新加坡 Bosch Security（boschsecurity.com no_mx；bosch.com 正常；工业 FS）：巨头品牌商 → 留 C（巨头不永久 pass）', []),
    'SC-2672': ('keep_C', 'Alltron（alltron.ch；表内「智利」实为瑞士 → 国别待核；多品牌 PoE injector / switch 大分销）：巨头分销（Competec 集团）→ 留 C（巨头不永久 pass；瑞士 = 欧洲，日后可作长线）', []),
    'SC-2793': ('keep_C', 'WAGO（wago.com；表内「俄罗斯」实为德国总部 → 国别待核；工业交换机 / SFP 自产）：巨头同行 → 留 C（巨头不永久 pass）', []),
    'SC-2698': ('keep_C', '日本 NTT-AT（ntt-at.com 域 dead；optical switch）：巨头集团 + 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-3321': ('keep_C', '乌克兰 STC（stc.kiev.ua；take catalog, knows fiber optic, send prices；WA 加不上）：乌克兰 = 守界（非永久 pass）→ 留 C', []),
    'SC-2556': ('keep_C', '乌克兰 Yavir 2000（yavir2000.com；CCTV 类）：乌克兰 = 守界 → 留 C', []),
    'SC-2749': ('keep_C', 'DTC Group（dtcgroup.com.ua；表内「俄罗斯」实为 .com.ua 乌克兰 → 国别待核；SFP / MC / 工业 FS / 10G，卖朱姐客户的牌子 CTC Union）：乌克兰 = 守界 → 留 C（局势变化后优先复看）', []),
    'SC-2335': ('keep_C', '俄罗斯 Stilsoft（stilsoft.ru；VC，看上去不熟产品；WA 加不上；8 推）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2476': ('keep_C', '喀麦隆 Ciel Solutions Technologies（cielsofts.com；1080P 16ch HD-AHD 视频光端机；Skype）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2532': ('keep_C', '肯尼亚 Aquatronics（aquakenya.com；VC，take catalog；WA 加不上）：光端机 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2533': ('keep_C', '摩洛哥 Polinnov（polinnov.ch nxdomain → 国别待核；问 120 km IP camera 信号传输；WA 加不上）：本职线 + 域 dead → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-2665': ('keep_C', '俄罗斯 Versia-IT（versia-it.ru；WDM / 测试设备；Simon 备注「不再跟进」）：本职线 → 留 C + dayjob_fit（无客户明确拒绝）', ['dayjob_fit']),
    'SC-2791': ('keep_C', '台湾 iSunjoin（isunjoin.com；sunjoin.com no_mx；MC 周边）：本职线 + 同行 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2503': ('keep_C', '中国大陆 Shenzhen Huatenmax（huatenmax.com；阿里巴巴询盘 DWDM）：国内 + 本职线同行 → 留 C（国内单子只走私账）', []),
    'SC-2495': ('keep_C', '澳大利亚 Powertec（powertec.com.au；在用 ONV / 锐捷等的工业 FS / 商业 FS；22 推 0 回；Simon 判不行）：进口中国同类 ✔ 但 22 推 0 回 → 留 C（储备；换稿 / 换人后再看，不作 pass）', []),
    'SC-2513': ('keep_C', '巴基斯坦 Microtech（microtech.net.pk；工业 FS / PoE，洪瑞商业 PoE / V-SOL；Elsa 线程 5 封：把 Saga 当买家回「Not Available」并发来自家 MikroTik 报价单）：互动错位 + 非点名国 → 留 C（储备；Q-33 洪瑞）', []),
    'SC-2564': ('keep_C', '越南 Camerahainam（camerahainam.net 域 dead；商业 PoE 主要洪瑞 / 光网视；Simon 判不行）：域死但无退信记录 → 留 C 待巡检（不作 pass）', []),
    'SC-2569': ('keep_C', 'Fabrimex Systems（fabrimex-systems.ch；表内「智利」实为瑞士 → 国别待核；工业 FS 较多周边；Simon 备注「不再跟进」）：欧洲工业分销但无中国品牌证据 → 留 C（储备；国别核实后可复看）', []),
    'SC-2693': ('keep_C', '台湾 Beyondtech（beyondtech.com.tw；工业 FS 基本是 Mlis 牌；发送失败）：台湾同行代理 → 留 C', []),
    'SC-2694': ('keep_C', '俄罗斯 Conetec（conetec.ru；有名牌子商业品；7 推 0 回）：名牌分销无中国品牌证据 → 留 C（储备）', []),
    'SC-2751': ('keep_C', '格鲁吉亚 hk.ge（商业 PoE 好几种外壳，销售平台）：平台型 → 留 C', []),
    'SC-2753': ('keep_C', '格鲁吉亚 Innocom（innocom.ge；商业 PoE 好几种外壳）：转售多外壳 + 零互动 → 留 C（储备）', []),
    'SC-2783': ('keep_C', '沙特 Quick Steps Contracting Est.（quickstepsco.com；要 L3 管理 4 光 16 电导轨式）：Saga 无 L3 工业线 → 留 C（储备，如实不对位）', []),
    'SC-2792': ('keep_C', 'Videomarin（videomarin.com；国别未填；工业 PoE 延长器，高 IP 等级，像 Centro 的）：高防护 / 延长器非 Saga 线 → 留 C', []),
    'SC-2800': ('keep_C', '巴西 Computech Loja（computechloja.com.br；PON / switch / PoE 网店）：网店 → 留 C', []),
    'SC-2496': ('keep_C', '印度 Skyline Network（skylinenetwork.in；ISP + CCTV networking；8 推 0 回）：小 ISP 终端 → 留 C', []),
    'SC-2651': ('keep_C', '印尼 CNI（cni.net.id；Networking；Simon 备注「不再跟进」）：无客户明确拒绝 → 留 C（储备）', []),
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
    L = [f'# C 池 · 闸 1 · 第 31 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 1046–1100 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：「用户判定不行」22（本批首次大量进入，按 U115 全部过筛）、退信 19、巨头 6、乌克兰 3、WA 加不上 6、国别错位 4（alltron.ch / fabrimex-systems.ch / dtcgroup.com.ua / polinnov.ch）。口径同桶 ⑥ 首批 + 新增「贴牌 / 自有品牌 = OEM 对象」线。候选 4 = Tactio（HK，贴自有牌）/ Protech（GE，ONV 带标卖）/ EverFocus（TW，品牌商）/ RVi Group（RU，hasivo 贴牌）；永久 pass 3 = CCTVapp VN / KVMswitches IN / Optimaunit RU（域名即户名 + 全域死 + 退信）。留 C：退信但有公司名 / 备用域 / 微信 → 待巡检、巨头（Omron · Samsung/S1 · Bosch · Alltron · WAGO · NTT-AT）、乌克兰守界、本职线 dayjob_fit、「用户判定不行」储备（Powertec AU 22 推 0 回 等）。「stop」flag / Simon 备注均非客户明确拒绝，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批31_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
