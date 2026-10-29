#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 44 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 496–550 户（按综合分序，SC-2621 … SC-2772；综合分 −29 → −39，桶尾）。

构成：陈旧 / 群发免费邮箱个人 38（本职线 VC / AHD / MC / HDMI / DWDM / DAC / 光猫 / 串口 22；WA 加不上 14）、仅电话 6、阿里询盘「无联系方式」（后台可回）3、守界乌克兰 3、公司域名但无邮箱 2（cctvsupply.us、smartxzone.com）、退信但域名存活 1、Simon 备注「不跟」2（SC-2729 stop 标记、SC-3419 DIGIDIS）。
  · 口径同第 36–43 批。本批无一户满足四条 → 候选 0；退信户 SC-2646 域名存活 = 非刚性 → 永久 pass 0。Simon 备注「不再跟进 / 只入库不跟」不是闸 0 依据 → 留 C 不主动。
  · 留意：DIGIDIS（Abdellah，2024-03 真回要目录，gmail 无域名，Simon「只入库记录，不跟」）、cngs@bk.ru（俄罗斯进口代理，「帮其他公司进口，有从中国进口经验」）、Systemplus Consulting FR（400G 光模块 RFQ = 本职线）、cctvsupply.us（美国 CCTV 网店有商业 PoE，无邮箱）。

用法：python3 sieve_batches/g1_044.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批44_2026-10-29.md）
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

BATCH = 'G1-44'
DATE = '2026-10-29'
CODES = ["SC-2621", "SC-2627", "SC-2629", "SC-2632", "SC-2635", "SC-2636", "SC-2638", "SC-2640", "SC-2641", "SC-2643", "SC-2644", "SC-2645", "SC-2646", "SC-2648", "SC-2649", "SC-2654", "SC-2655", "SC-2656", "SC-2660", "SC-2664", "SC-2666", "SC-2623", "SC-2670", "SC-2674", "SC-2675", "SC-2676", "SC-2678", "SC-2679", "SC-2685", "SC-2688", "SC-2689", "SC-2653", "SC-2690", "SC-2692", "SC-2703", "SC-2708", "SC-2715", "SC-2716", "SC-2727", "SC-2729", "SC-2731", "SC-2732", "SC-2748", "SC-2750", "SC-2752", "SC-2755", "SC-2761", "SC-2763", "SC-2764", "SC-2765", "SC-3419", "SC-2769", "SC-2770", "SC-2771", "SC-2772"]

OVERRIDE = {
    'SC-3419': ('keep_C', 'DIGIDIS（Abdellah；a.digidis@gmail.com；国别未填；2024-03-15 真回要 8 口千兆 PoE 管理型目录；全程 3 封；Simon「非重点区域、无公司域名、单次问目录——只入库记录，不跟」）：真实回复 ✔ 但无域名 / 国别不明 + Simon 不跟 → 留 C 储备（来询再报；Simon 备注非 pass 依据）', []),
    'SC-2729': ('keep_C', '孟加拉 Jannatul Nayeem（gdnayeem1996@gmail.com；阿里询盘「48 port RJ45 不带 PoE」；Simon 标记不再跟进 / Spam）：Simon 备注非闸 0 依据 → 留 C 不主动', []),
    'SC-2623': ('keep_C', '俄罗斯 Mamontov Vladimir（cngs@bk.ru；「帮其他公司进口各类产品，有从中国进口经验」；WA 加不上；8 推 0 回）：进口代理 / 中间商 + 零回应 → 留 C 储备', []),
    'SC-2772': ('keep_C', '美国 CCTV Supply（cctvsupply.us 正常；主要 CCTV 类，有商业 PoE；无邮箱；Simon 判定不相关）：美国 CCTV 网店 + 无路径 → 留 C 待巡检（找到邮箱再看）', []),
    'SC-2646': ('keep_C', '哥伦比亚 Telestar del Norte（telestardelnorte.com 正常；telestarhd@gmail.com 退信；用的 HDV 的，周边产品为主）：退信但域名存活 = 非刚性 → 留 C 待巡检（官网找邮箱）', []),
    'SC-2648': ('keep_C', '法国 Systemplus Consulting（Audrey Lahrach；阿里 RFQ「400G 光模块」；无邮箱 / 电话）：阿里巴巴询盘 / 对话，表内无邮箱电话但阿里后台可回 = 路径存在（非闸 0）→ 留 C 待巡检；400G 模块本职线', ['dayjob_fit']),
    'SC-2670': ('keep_C', '肯尼亚 Hand Therapy-Kenya（阿里即时对话「问产品线」；无邮箱 / 电话）：阿里巴巴询盘 / 对话，表内无邮箱电话但阿里后台可回 = 路径存在（非闸 0）→ 留 C 待巡检', []),
    'SC-2761': ('keep_C', '印度尼西亚 Chaepur Rahman（阿里询盘「DWDM」；无邮箱 / 电话）：阿里巴巴询盘 / 对话，表内无邮箱电话但阿里后台可回 = 路径存在（非闸 0）→ 留 C 待巡检；DWDM 本职线', ['dayjob_fit']),
    'SC-2649': ('keep_C', '乌克兰 Alexander Khokhanovskyi（gmail；2020 年 RFQ「60W PoE 规格的工业交换机」）：守界乌克兰（不 pass，不主动发）→ 留 C', []),
    'SC-2685': ('keep_C', '乌克兰 Ivan Lazukin（gmail；阿里询盘「DWDM」）：守界乌克兰（不 pass，不主动发）→ 留 C；DWDM 本职线', ['dayjob_fit']),
    'SC-2689': ('keep_C', '乌克兰 Dmytro Rozhevskyi（gmail；2014 年「2 光 8 管理反向 PoE 工业级」）：守界乌克兰（不 pass，不主动发）→ 留 C；反向 PoE Saga 不供', []),
    'SC-2641': ('keep_C', '哥伦比亚 Centro de Servicio Andino（centrodeservicioandino.com 正常；Fernando Güiza Gamboa，yahoo.es；CCTV 类产品；8 推 0 回）：CCTV 服务商 + 零回应 → 留 C', []),
    'SC-2675': ('keep_C', '印度 Security Systems（security-systems.co.in no_mx；Kodan.R，gmail；VC）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2703': ('keep_C', '印度 Vizor Electronics Pvt. Ltd（vizor.in no_mx；gmail；cameras / DVRs；WA 加不上）：CCTV 品类 → 留 C', []),
    'SC-2731': ('keep_C', '印度 Smartxzone（smartxzone.com nxdomain；仅电话；VC，FB 上摄像头多；16 推 0 回）：域死但电话在 + VC 本职线 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-2635': ('keep_C', '沙特 A. Alaidaroos Trading Est.（Abubakr Ali Alaidaroos；仅电话；HDMI extender；16 推 0 回）：HDMI 延长本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2636': ('keep_C', '津巴布韦 ARODHAR Professional Electronics（Aron Sibanda，gmail；2020 年 RFQ CCTV 相关；WA 加不上）：CCTV 品类 → 留 C', []),
    'SC-2679': ('keep_C', '特立尼达 RB TRADERS（Raju Babani，hotmail；HDMI extender 30m）：HDMI 延长本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2690': ('keep_C', '越南 Centre for Applications of …（Trinh Dinh Hai，gmail；VC；WA 加不上）：研究机构 + VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2763': ('keep_C', '多米尼加 Tele-Costa Digital（Jonathan Martinez，hotmail；VC；WA 加不上）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2765': ('keep_C', '秘鲁 LP Ingenieros S.A.（gmail；VC；WA 加不上）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2769': ('keep_C', '肯尼亚 INFORMED SYSTEMS LTD（仅电话；买 MC；网站门禁 / 安防 / CCTV；15 推 0 回）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2771': ('keep_C', '俄罗斯 Skycam（WhatsApp / Viber 7 909 184-09-57；摄像头公司）：CCTV 品类 + 仅电话 → 留 C', []),
    'SC-2655': ('keep_C', '俄罗斯 Industriya-T（industriya-t@yandex.ru；Николаев；装修公司）：装修公司 + 零需求 → 留 C', []),
    'SC-2732': ('keep_C', '越南 Viễn Thông Vinanet（Pham Quoc Oai Director，gmail；跳线）：跳线非 Saga 线 → 留 C', []),
    'SC-2621': ('keep_C', '哈萨克斯坦 Baurt Telibekov（gmail；千兆 MC / SFP；2020 年注册没啥信息）：MC / SFP 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2638': ('keep_C', '印度 Rohali Kirana Store（gmail；HDMI / DVI 转光；WA 加不上）：HDMI 光传本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2643': ('keep_C', '印度 dineshkumargoutham6@gmail.com（Bidi 千兆小外电 60 公里；WA 加不上）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2644': ('keep_C', '刚果 Gloire Mutombo（gmail；之前问过 HDMI 级联）：HDMI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2645': ('keep_C', '印度 Muthu（gmail；1Fx4UTP；WA 加不上）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2664': ('keep_C', '美国 Blake Jasper（vermarhemi@hotmail.com；2022 年串口服务器「问是厂家嘛」；WA 加不上）：串口服务器本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2666': ('keep_C', '美国 Adelaide Yeates（wirthettelr@hotmail.com；2022 年询盘光猫，问能否再低；WA 加不上）：光猫本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2678': ('keep_C', '巴西 Geizi Monteiro（仅电话；无源产品；13 推 0 回）：无源非 Saga 线 → 留 C', []),
    'SC-2688': ('keep_C', '泰国 Pipat Trakulchang（pt24631@gmail.com；1080P 16ch HD-AHD）：AHD 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2653': ('keep_C', '俄罗斯 Evgeniy Dedyaev（yandex；IP camera；7 推 0 回）：摄像机品类 → 留 C', []),
    'SC-2692': ('keep_C', '文莱 Alan Saikawa（gmail；2017 年 RFQ「40G DAC 跳线」，看了很多 WDM）：DAC / WDM 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2708': ('keep_C', '玻利维亚 David Guzman Fernandez（gmail；「TA510-GE 30 对」；Santa Cruz）：MC 本职线有量 + 个人 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2715': ('keep_C', '津巴布韦 Hatisari Zizhou（gmail；2014 年「百兆单纤 MC 150 对」）：MC 本职线 + 陈旧 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2716': ('keep_C', '秘鲁 islavend@gmail.com（OM4301 视频光端机）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2727': ('keep_C', '哥伦比亚 Yofrey Beltran（wifititansj@gmail.com；2021 年「千兆单纤小外电 10 对」）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2748': ('keep_C', '喀麦隆 Simon Onana（gmail；2016 年「百兆双小外电 1 个」）：MC 本职线 + 陈旧 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2750': ('keep_C', '赤道几内亚 Filéas Momo（gmail；2020 年「20 对单模单纤 20km / 40km」）：MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2764': ('keep_C', '巴西 Audemarms Martins（hotmail；interested in VC）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2770': ('keep_C', '秘鲁 Jesusmanuel Tolentino（仅电话；HDMI 转网 KVM；16 推 0 回）：HDMI / KVM 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2627': ('keep_C', '刚果 juniorkitenge972@gmail.com（2 光 4 长壳商业级；9 推 0 回）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2629': ('keep_C', '孟加拉 Kajal Telecom（gmail；大壳 2 光 4 PoE 非管理；陈旧）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2632': ('keep_C', '南非 Rolin（rolinc@gmail.com；6 光 8 管理；陈旧）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）（南非先例在，坐实公司后看）', []),
    'SC-2640': ('keep_C', '埃及 Ashraf Waheed（hotmail；General information；WA 加不上）：群发冷名单 / 陈旧免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2654': ('keep_C', '菲律宾 Hero Rodriguez（gmail；TA510-FE；19 年注册没别的信息）：群发冷名单 / 陈旧免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2656': ('keep_C', '印度尼西亚 Jamaluddin（gmail；TA510-GE 没公司，新注册）：群发冷名单 / 陈旧免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2660': ('keep_C', 'rlnatmmm@bk.ru（表内俄罗斯，+998 乌兹别克号 → 国别待核；无需求记录）：群发冷名单 / 陈旧免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2674': ('keep_C', '孟加拉 Hasibur Rahman Hasib（gmail；千兆 5 口交换机；WA 加不上）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2676': ('keep_C', '斯里兰卡 tashinavimukthi123@gmail.com（4 光 8 电工业；WA 加不上）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-2752': ('keep_C', '坦桑尼亚 Idd Mussa（gmail；14 年国际站，其他没信息）：群发冷名单 / 陈旧免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
    'SC-2755': ('keep_C', '孟加拉 Tawkir Khan（gmail；TA330-GE；陈旧）：群发冷名单 / 陈旧免费邮箱个人，无公司域名 + 零回应 → 不 pass、不入池 → 留 C', []),
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
    L = [f'# C 池 · 闸 1 · 第 44 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 496–550 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：免费邮箱个人 38、仅电话 6、阿里后台可回 3、守界乌克兰 3、公司域名无邮箱 2、退信域存活 1、Simon 备注「不跟」2。候选 0、永久 pass 0 —— 桶尾全部留 C。', '',
         '> 值得留意的留 C：DIGIDIS Abdellah（真回要目录，无域名）、cngs@bk.ru（俄进口代理）、Systemplus Consulting FR（400G 模块 → 本职线）、cctvsupply.us（找到邮箱再看）、Telestar del Norte CO（退信但域名活，待巡检）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批44_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
