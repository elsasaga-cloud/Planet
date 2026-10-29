#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 26 批（2026-10-29）—— 桶 ⑥「企业邮箱 · 其他区」第 771–825 户（按综合分序，SC-1570 … SC-1705）。

构成：俄罗斯「WDM」0 触达冷名单（约 20 户 = 本职线 → dayjob_fit）、巴西 Utepo / 三旺 / 迈威 经销商约 12 户、德国「未填国别」名牌经销 / 销售平台 7 户、印尼 / 厄瓜多尔 / 中东零星、WhatsApp 加不上 2、域名死 2。
  · 口径同桶 ⑥ 首批（分销 / 集成 + 中国 / 台湾品牌证据 + 有先例地区 → 闸 2 低优先；具体型号 / 数量询问 = 真需求 → 候选；备注空白 / 名牌 / 周边 → 留 C；本职线 → dayjob_fit；四主区但无中国品牌证据 → 留 C）。
  · 候选 5 = Tekmodul DE（Atop 专业经销 = 德国主区 + 台湾品牌证据）/ Cartago Comex BR（HTB MC 100 对 = 数量询问）/ Metsuki VN（ONV 工业 PoE + 问到 4-8-16-24 口 = 具体需求，21 推 0 回）/ Abovenet BR（三旺专营）/ Alfacomp BR（全线迈威 + 官网 WA）→ 闸 2 查底数。
  · 永久 pass 0（iksmedia.ru 疑电信行业媒体但未核证 → 留 C 不作 pass）。
  · 其余留 C：俄罗斯 WDM / 光开关 / 光纤（cheredin · cirex · monosystems · nateks-ural · neosnetworks · optic-ring 域 dead · rotec · specint · sphotonics · supertel · telecomparts · ukrservice · wdmpro · zettaline ADVA · iksmedia）+ 阿塞拜疆 Delta Telecom + 印尼 Global Solusi / Primatel + 哈萨克 Stroymig / Bplus（光端机偶有订单 = 本职线）→ dayjob_fit；icsgroup DC 接线、idisglobal.ru（IDIS 俄分部 → 并入 SC-493 韩国总部）、spb.ru no_mx；中国大陆迈普（国内 / 同行，Evelyn 微信）；巴西 CCTV 店「有 Utepo 的」3 户（Eagle Vision · Fontec · Helper）储备、centraisvoip VoIP、aceplus / fibrastore 光模块；德国名牌经销 Bressner / Piospartslap / Trius（无中国品牌证据）、销售平台 all4fiber / gt-netstore、安防站 vtis；中东 Allied Resources（只回回执）/ Metco 光网络 / Movantech / GST Egypt Advantech；厄瓜多尔 Inredtel / FIS（WA 加不上）、巴拉圭 Netvision MC、蒙古 Microciti、特立尼达 Bellcom 接头、毛里塔尼亚 CSS、台湾 Aibao SFP、印度 Infofiber MC 周边 / cpplusworld（= CP PLUS 品牌站 → 并入 SC-1042）、墨西哥 Intelimax 域 dead。
  · 「stop」flag 来自 STOP_WORDS 文本命中，不是明确要求停发 → 不作 pass 依据。

用法：python3 sieve_batches/g1_026.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批26_2026-10-29.md）
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

BATCH = 'G1-26'
DATE = '2026-10-29'
CODES = ["SC-1570", "SC-1575", "SC-1576", "SC-1583", "SC-1584", "SC-1585", "SC-1587", "SC-1588", "SC-1595", "SC-1598", "SC-1599", "SC-1600", "SC-1601", "SC-1607", "SC-1608", "SC-1609", "SC-1612", "SC-1618", "SC-1619", "SC-1630", "SC-1631", "SC-1632", "SC-1633", "SC-1635", "SC-1637", "SC-1641", "SC-1646", "SC-1649", "SC-1651", "SC-1654", "SC-1659", "SC-1660", "SC-1661", "SC-1663", "SC-1666", "SC-1669", "SC-1670", "SC-1671", "SC-1672", "SC-1675", "SC-1676", "SC-1677", "SC-1680", "SC-1689", "SC-1690", "SC-1691", "SC-1692", "SC-1693", "SC-1694", "SC-1697", "SC-1698", "SC-1700", "SC-1701", "SC-1704", "SC-1705"]

Q33 = '；洪瑞现供客户 → Q-33 口径待 Simon（默认只推 SmartByte / Marvell 管理 + 工业线）'
VETO = '；Simon 曾判不行 → 可按编号否决'

OVERRIDE = {
    # ---- 候选 → 闸 2（桶 ⑥ 低优先）----
    'SC-1675': ('candidate', '德国 Tekmodul（tekmodul.de；表内国别未填 → .de；「Atop 的，感觉比较专业」= 台湾工业品牌专业经销）：德国主区 ✔ 台湾品牌证据 ✔ 分销主体 ✔ 对位（STI 工业线）✔；未触达 → 闸 2 查底数（handelsregister 镜像 / 官网 Impressum）', []),
    'SC-1583': ('candidate', '巴西 Cartago Comex（cartagocomex.com；HTB MC 100 对，拿 BYXGD 牌子来问）：数量询问 = 真需求 ✔ 进口中国同类 ✔ 巴西有先例（Teltex / Parks）；→ 闸 2 查 CNPJ；MC 仅 STC-110XGE 对位 → 低优先', []),
    'SC-1670': ('candidate', '越南 Metsuki（metsuki.com.vn；CCTV 为主 + 商业 / 工业 PoE ONV，问到百千兆 4-8-16-24 口；21 推 0 回）：具体需求 ✔ 进口中国同类 ✔ 对位 ✔；→ 闸 2 查底数（masothue）；四主区外非点名国 → 低优先，换稿点名', []),
    'SC-1689': ('candidate', '巴西 Abovenet（abovenet.com.br；三旺的）：中国工业品牌专营 ✔ 对位 ✔ 巴西有先例；未触达 → 闸 2 查 CNPJ；低优先', []),
    'SC-1691': ('candidate', '巴西 Alfacomp（alfacomp.net / alfacomp.ind.br；全线迈威产品 + 官网 WA 按钮）：中国工业品牌全线 ✔ 对位 ✔ WA 路径 ✔ 巴西有先例；未触达 → 闸 2 查 CNPJ；低优先', []),
    # ---- 留 C（带标签 / 具体理由）----
    'SC-1570': ('keep_C', '哈萨克斯坦 Bplus（bplus.kz；品类不符 VC / DWDM / CCTV；偶尔有反应，订一两对光端机；8 推）：光端机 = 本职线 → 留 C + dayjob_fit（交换机线零需求）', ['dayjob_fit']),
    'SC-1575': ('keep_C', '中国大陆 迈普 Maipu（maipu.com；Evelyn 微信加的参展商，有客户要工业级交换机，用过 ONV，问流量整形，推 VSC 报 100 多美金）：国内单子只走私账 + 大厂同行 → 留 C（不入出口池）', []),
    'SC-1599': ('keep_C', '俄罗斯 IDIS Global RU（idisglobal.ru；CCTV + 商业 PoE）：= 韩国 IDIS（SC-493，闸 2 第 130 批 P 池候选）俄分部 → 并入总部跟进，留 C 避免双发', []),
    'SC-1600': ('keep_C', '俄罗斯 iksmedia.ru（WDM）：疑 ИКС-Медиа 电信行业媒体（未核证）→ 留 C + dayjob_fit，不作 pass', ['dayjob_fit']),
    'SC-1612': ('keep_C', '俄罗斯 Optic-Ring / Mosline（optic-ring.moscow 域 dead；mosline.ru 正常；WDM）：本职线 + 主域死 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-1630': ('keep_C', '俄罗斯 spb.ru（无 MX；商业 PoE / PoE 配件）：通用域主体不明 + 无 MX → 留 C 待巡检', []),
    'SC-1660': ('keep_C', 'all4fiber（all4fiber.de 无 MX / all4fiber.com 正常；表内国别未填；光纤销售平台）：专业网店 = 转售主体（非综合商城）+ 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1663': ('keep_C', '德国 Bressner（bressner.de；表内国别未填；卖几个有名牌子的）：德国主区 ✔ 但无中国品牌证据 + 零互动 → 留 C（储备；§5 条数不够）', []),
    'SC-1661': ('keep_C', '沙特 Allied Resources（alliedresources.sa；12 推只回自动回执）：回执 ≠ 回信 + 无品牌证据 → 留 C', []),
    'SC-1671': ('keep_C', '阿联酋 Movantech（movantech.com；安防 + 网络「和公司业务很近」；14 推 0 回）：对位 ✔ 但无中国品牌证据 + 非点名国 → 留 C（储备）', []),
    'SC-1693': ('keep_C', '印度 cpplusworld.com（CP PLUS 品牌站；商业 PoE / 工业 FS）：= Aditya Infotech / CP PLUS（SC-1042，闸 2 第 130 批 P 池候选）同主体 → 并入，留 C 避免双发', []),
    'SC-1694': ('keep_C', '巴西 Eagle Vision（eaglevision.com.br；有 Utepo 的）：CCTV 店多牌之一 + 零互动 + 非点名国 → 留 C（储备；巴西已有专营候选）', []),
    'SC-1698': ('keep_C', '巴西 Fontec CFTV（fontecftv.com.br；有 Utepo 的）：同上 → 留 C（储备）', []),
    'SC-1701': ('keep_C', '巴西 Helper Tecnologia（helpertecnologia.com.br；有 Utepo 的）：同上 → 留 C（储备）', []),
    'SC-1705': ('keep_C', '墨西哥 Intelimax（intelimax.mx 域 dead；19 年国际站）：域死但无退信记录 → 留 C 待巡检', []),
    'SC-1585': ('keep_C', '俄罗斯 cheredin.ru（WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1587': ('keep_C', '俄罗斯 cirex.ru（WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1588': ('keep_C', '阿塞拜疆 Delta Telecom（delta-telecom.net；WDM）：本职线 + 运营商 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1595': ('keep_C', '印尼 Global Solusi（global-solusi.co.id；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1607': ('keep_C', '俄罗斯 Monosystems（monosystems.ru；WDM 卖几个牌子的）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1608': ('keep_C', '俄罗斯 Nateks-Ural（nateks-ural.ru；WDM；本土设备商分部）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1609': ('keep_C', '俄罗斯 Neos Networks（neosnetworks.com；Fiber optics）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1618': ('keep_C', '印尼 Primatel（primatel.co.id；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1619': ('keep_C', '俄罗斯 Rotec（rotec.ru；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1631': ('keep_C', '俄罗斯 Specint（specint.ru；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1632': ('keep_C', '俄罗斯 Sphotonics（sphotonics.ru；光开关）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1633': ('keep_C', '哈萨克斯坦 Stroymig（stroymig.com / .kz；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1635': ('keep_C', '俄罗斯 Supertel（supertel.ru；supertel.tel 无 MX；WDM；本土电信设备商）：本职线 + 同行 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1637': ('keep_C', '俄罗斯 Telecomparts（telecomparts.ru；WDM 卖几个牌子的）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1641': ('keep_C', 'ukrservice.net（表内俄罗斯，域名含 ukr → 国别存疑；WDM）：本职线 + 国别待核 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1646': ('keep_C', '俄罗斯 WDMpro（wdmpro.ru；WDM）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1649': ('keep_C', '俄罗斯 Zettaline（zettaline.ru；WDM，ADVA 的）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1659': ('keep_C', '台湾 Aibao Tech（aibaotech.com；基本都是 SFP / 光模块）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1669': ('keep_C', '科威特 Metco Networks（metconetworks.com；optical networking；9 推 0 回）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1690': ('keep_C', '巴西 Aceplus（aceplusbrasil.com.br；光模块为主）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1697': ('keep_C', '巴西 Fibrastore（fibrastore.com.br；基本都是 SFP）：本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1704': ('keep_C', '印度 Infofiber（infofiber.in；MC / SFP / 周边）：本职线 + 周边 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 26 批（{DATE}）—— 桶 ⑥「企业邮箱 · 其他区」第 771–825 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：俄罗斯「WDM」0 触达约 20 户（本职线 → dayjob_fit）、巴西 Utepo / 三旺 / 迈威 经销商约 12 户、德国未填国别名牌经销 / 销售平台 7 户、印尼 / 厄瓜多尔 / 中东零星、WA 加不上 2、域名死 2。口径同桶 ⑥ 首批。候选 5 = Tekmodul（DE，Atop 专业经销）/ Cartago Comex（BR，MC 100 对）/ Metsuki（VN，ONV + 问 4-8-16-24 口）/ Abovenet（BR，三旺专营）/ Alfacomp（BR，全线迈威）；永久 pass 0。留 C：俄罗斯 WDM 本职线、IDIS 俄分部并入 SC-493、cpplusworld 并入 SC-1042、巴西 CCTV 店储备、德国名牌经销无中国品牌证据、销售平台 / 周边 / 光模块、WA 加不上、域死待巡检。「stop」flag = 文本命中，不作 pass 依据。**Simon 可按编号否决候选**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批26_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
