#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 39 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 221–275 户（按综合分序，SC-1891 … SC-2042；综合分 1 → −4，已到桶尾低分段）。

构成：群发冷名单（免费邮箱 + 公司网址）30（越南 11、俄语区 5、印度 4、其他 10）、仅网址 2、阿里巴巴 / 自建站个人 15（无人机 2、光模块 / CWDM / 收发器 / VC 8）、WA 加不上的可疑线索 4、守界乌克兰 1。
  · 口径同第 36–38 批；本批越南专业店密集，凡点名中国品牌（中科德能 / 三旺 / ONV / G-net-hasivo / hisource / Utepo）+ 先例国或欧洲 → 候选。
  · 候选 5 = 印度 Vigil（PoE switch，hisource 的）/ 越南 Viễn Thông Hà Nội（工业 FS 主要中科德能）/ 越南 Switch Quang（ONV、三旺；VC / 工业 FS / SFP / PoE / 串口 / MC 全线）/ 越南 Việt Long Telecom（商业 PoE 用 G-net = hasivo）/ 拉脱维亚 Signalizācija（CCTV 报警安装商，有 Utepo 的；欧洲）。永久 pass 0。
  · 留意：Talad Security VN（ONV 全线引进，域 nxdomain 无邮箱 → 待巡检）、Staphone VN（疑本土品牌）、Thiết Bị Quang VN（傲通达 / OPTONE 模块大买家 = 本职线）、WA 加不上的 4 条美英可疑线索（Router Hansome 同类）。

用法：python3 sieve_batches/g1_039.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批39_2026-10-29.md）
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

BATCH = 'G1-39'
DATE = '2026-10-29'
CODES = ["SC-1891", "SC-1894", "SC-1898", "SC-1899", "SC-1903", "SC-1907", "SC-1908", "SC-1910", "SC-1911", "SC-1913", "SC-1915", "SC-1916", "SC-1918", "SC-1919", "SC-1923", "SC-1925", "SC-1930", "SC-1937", "SC-1941", "SC-1943", "SC-1945", "SC-1867", "SC-1948", "SC-1952", "SC-1954", "SC-1955", "SC-1958", "SC-1959", "SC-1967", "SC-1969", "SC-1976", "SC-1978", "SC-1979", "SC-1980", "SC-1982", "SC-1983", "SC-1984", "SC-1985", "SC-1879", "SC-1986", "SC-1987", "SC-1990", "SC-1992", "SC-1993", "SC-1995", "SC-1996", "SC-1999", "SC-2002", "SC-2003", "SC-2005", "SC-2013", "SC-2022", "SC-2032", "SC-2037", "SC-2042"]

OVERRIDE = {
    'SC-1916': ('candidate', '印度 Vigil（vigilworld.com no_mx；vigil_usv@yahoo.co.in；PoE switch，hisource 的 ✔）：点名中国品牌 ✔ 印度先例 ✔ 对位 ✔ 可达 ✔ → 闸 2 查底数（MCA 镜像）后一页纸', []),
    'SC-1867': ('candidate', '越南 Viễn Thông Hà Nội（vienthonghanoi.vn 正常；gmail；工业 FS 主要是中科德能的 ✔；8 推 0 回）：点名中国工业品牌 ✔ 越南先例 ✔ 工业对位 ✔ 可达 ✔ → 闸 2 查底数（MST）后换稿一页纸（零回应 → 坐实后仅一次）', []),
    'SC-1979': ('candidate', '越南 Switch Quang / Thanh Bình Technology（switchquang.com.vn 正常；gmail；ONV、三旺 ✔；VC / 工业 FS / SFP / PoE / 串口 / MC 全线；8 推 0 回）：点名中国品牌 ✔ 越南先例 ✔ 全线对位 ✔ 可达 ✔ → 闸 2 查底数（MST）后换稿一页纸；VC 本职线并行', ['dayjob_fit']),
    'SC-1983': ('candidate', '越南 Việt Long Telecom（vietlongtelecom.com 正常；gmail；商业 PoE 用 G-net 的 = hasivo ✔；8 推 0 回）：点名中国品牌 ✔ 越南先例 ✔ 对位 ✔ 可达 ✔ → 闸 2 查底数（MST）后换稿一页纸', []),
    'SC-1976': ('candidate', '拉脱维亚 Signalizācija（signalizacija.lv no_mx；tiger.cctv@inbox.lv；主要是 CCTV，有 Utepo 的 ✔；15 推 0 回）：点名中国品牌 ✔ 欧洲 ✔ 安装商对位 ✔ 可达 ✔ → 闸 2 查底数（Lursoft / firmas.lv）后换稿一页纸（15 推零回应 → 坐实后仅一次，不行回 C）', []),
    'SC-2022': ('keep_C', '乌克兰 Faraon2000（faraon2000.com no_mx；gmail；ONV / 洪瑞等很多牌子的杂货铺；16 推 0 回）：守界乌克兰 + 洪瑞渠道 Q-33 → 留 C', []),
    'SC-1980': ('keep_C', '越南 Talad Security（taladsecurity.com nxdomain；无邮箱；「ONV 产品的全线引进」）：ONV 全线 ✔ 但域死 + 无路径 → 留 C 待巡检（找到新域 / 邮箱即转候选；下次仍死即 pass）', []),
    'SC-1978': ('keep_C', '越南 Staphone（staphone.com.vn no_mx；gmail；主要是有名牌子，「似乎是一个本土牌子」）：疑本土自有品牌（oem_target 备查）+ 零互动 → 留 C 储备', ['oem_target']),
    'SC-1913': ('keep_C', '越南 Thiết Bị Quang / VFV Telecom（thietbiquangvn.com 正常；gmail；从 OPTONE / 傲通达买很多模块，网站可见）：光模块大买家 = 本职线 → 留 C + dayjob_fit（越南先例在，问到交换机即转候选）', ['dayjob_fit']),
    'SC-1891': ('keep_C', '俄罗斯 Fibercon（fibercon.ru 正常；yandex；SFP / MC 一些有名牌子）：光模块 / MC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1898': ('keep_C', '俄罗斯 ISP Ruza（isp-ruza.ru nxdomain；list.ru；从 o-netcom 买模块）：小 ISP + 模块本职线 + 域死 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-1982': ('keep_C', '俄罗斯 vga-hdmi.ru（域正常；yandex；无需求记录）：HDMI 周边 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1879': ('keep_C', '俄罗斯 Sentinel（Alex director；gmail / yandex；装修类工程商，熟悉光纤，想要光纤产品目录；8 推）：装修工程商 + 光纤本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1894': ('keep_C', '印度 Gentop（gentop.in 正常；gmail；主要是 CCTV 商业 PoE）：CCTV 店 + 无品牌证据 → 留 C 储备', []),
    'SC-1903': ('keep_C', '印度 Matchdigi（matchdigi.com 正常；gmail；商业 PoE / MC 周边；网站有 WA 按钮）：零互动 + 无品牌证据 → 留 C 储备（一页纸一次后看）', []),
    'SC-1987': ('keep_C', 'Balaji Electronics（Chennai，表内国别未填 → 印度；bajajelectronics.com 疑非其域；gmail；收发器 / SFP 要好价；「杂货铺」）：杂货铺 + 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1911': ('keep_C', '孟加拉 Techlink（techlink.com.bd 正常；gmail；FS 主要是 CCTV，杂）：CCTV 杂货 → 留 C', []),
    'SC-1918': ('keep_C', '摩洛哥 Wahda Technique（wahdatechnique.com 正常；gmail；大口 FS，BDCOM）：点名中国品牌 ✔ 但摩洛哥无先例 + 零互动 → 留 C 储备', []),
    'SC-1910': ('keep_C', '突尼斯 Tac-Tic（tac-tic.net 正常；Bouali Mohamed Amine，gmail；转发过我方帖子 ✔；2 光 8 傻瓜 + 2 网口模块；5 推）：社媒互动 ✔ 但突尼斯无先例 + 免费邮箱 → 留 C 储备（一页纸一次后看）', []),
    'SC-1937': ('keep_C', '肯尼亚 Micronet Power Systems（micronetpowersystems.com 正常；David Vundi，gmail；4 光 8 工业大壳，需要 edgecore 型号；WA 加不上；1 推）：品牌指定 + 无先例 → 留 C', []),
    'SC-1941': ('keep_C', '阿联酋 SAP Telecom（saptelecom.com 正常；Omar Elrefaey，outlook；工业 FS / MC 方案解决商，Opengear logo；13 推 0 回）：方案商对位 ✔ 但 13 推零回应 + 免费邮箱 → 留 C 储备', []),
    'SC-1945': ('keep_C', '泰国 Taisin Netcam（taisinnetcam.com 正常；gmail ×2；FS 卖国内很多品牌，销售平台 / CCTV 类）：平台型 → 留 C', []),
    'SC-1925': ('keep_C', '澳大利亚 AFW Technologies（afwtechnologies.com.au 正常；gmail；CWDM）：CWDM 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1943': ('keep_C', '澳大利亚 Soligen（soligen.com.au 正常；Fiber optics；无邮箱）：光纤本职线 + 无路径 → 留 C 待巡检 + dayjob_fit', ['dayjob_fit']),
    'SC-1967': ('keep_C', '越南 Hàn Cáp Quang（hancapquang.net 正常；gmail；光纤熔接 / 无需求记录）：熔接服务商 → 留 C', []),
    'SC-1984': ('keep_C', '越南 VTT Miền Nam（vttmiennam.com nxdomain；gmail；主要卖海康威视的）：海康 CCTV 店 + 域死 → 留 C 待巡检', []),
    'SC-2032': ('keep_C', '越南 Máy Văn Phòng Hưng Anh（域 nxdomain；gmail；办公设备店，有 ONV 的 switch）：办公设备店 + 域死 → 留 C 待巡检', []),
    'SC-1923': ('keep_C', '墨西哥 NúcleoNet Comunications（Jesus Zepeda Director；hotmail；2009 年「1 光 4 小壳」）：陈旧 + 免费邮箱 → 留 C', []),
    'SC-1992': ('keep_C', '阿塞拜疆 Maral-Gel LLC（Chingiz Avishov，gmail；2010 年 RFQ CWDM；有回复「价格太贵」）：CWDM 本职线 + 陈旧 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1993': ('keep_C', '秘鲁 Plabee（Diego Olmedo，gmail；2012 年 Wi-tek PoE 配件）：陈旧 + 品牌指定 → 留 C', []),
    'SC-1958': ('keep_C', '韩国 Young Telecom, Ltd（daum；2017 年「D2*2B Bypass」）：Bypass 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2013': ('keep_C', '韩国 Wisung（Yangsook Lee，gmail；最近没登录，RFQ 报过）：零互动 → 留 C', []),
    'SC-1955': ('keep_C', '卡塔尔 Provision Production LLC（Albert Bou Farhat，hotmail；3G-SDI 多功能；1 推）：SDI 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2005': ('keep_C', '沙特 Amr WJ company（hotmail；「OM610-4V↑1D↓WT/R」视频光端机型号）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2042': ('keep_C', '埃及 ELNILE JET（Eid Hammad Supervisor；gmail；收发器 / FS 1 光 4 电；「非常久不上线」）：零互动 + 无先例 → 留 C', []),
    'SC-1990': ('keep_C', '埃塞俄比亚 Furdaa Health center（gmail；插卡式 PoE MC）：终端用户 + 本职线 → 留 C', []),
    'SC-1986': ('keep_C', '加纳 Alfred Kwame（仅电话；「ST 千兆 MC 6 个」；13 推 1 条负面）：个人 + MC 本职线 → 留 C（reply_neg 非闸 0 依据）', ['dayjob_fit']),
    'SC-1919': ('keep_C', 'An Electrical（Asghar Nabi Electrician；hotmail；+44 7843 英国手机 → 国别待核；工业 PoE / HDMI switch；15 推 0 回）：个体电工 → 留 C', []),
    'SC-1899': ('keep_C', 'Kolal（kolal.br@gmail.com，国别未填 → 疑巴西；「1U 机架交换机需要 AC input」；6 推 0 回）：个人 → 留 C', []),
    'SC-1959': ('keep_C', '美国 Salman Ahmad（gmail ×2；「千兆单纤小外电」后来不回复；阿里上也看）：个人 → 留 C', []),
    'SC-1985': ('keep_C', '（未填；+880 1787 孟加拉号）easin8256@gmail.com（「商业级 1 光 4 电」；5 推；没办法加 WhatsApp）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1948': ('keep_C', '英国 Alleviance cycle stores（「Cisco items」；美国 303 号码加不上；gmail）：WA 加不上 + 免费邮箱 + 泛泛需求 = 疑可疑 / 钓鱼线索 → 留 C（不主动发）', []),
    'SC-1952': ('keep_C', '美国 KWILLIAMS TRADE COMAPY（「General information」；加不上；gmail）：WA 加不上 + 免费邮箱 + 泛泛需求 = 疑可疑 / 钓鱼线索 → 留 C（不主动发）', []),
    'SC-1954': ('keep_C', '美国 New Business Line（「Transmitter」；wallacehoustonceo@gmail.com；加不上）：WA 加不上 + 免费邮箱 + 泛泛需求 = 疑可疑 / 钓鱼线索 → 留 C（不主动发）', []),
    'SC-1969': ('keep_C', '法国 kairos musique（「MM-SM」；加不上；gmail）：乐器店 + 品类不符：WA 加不上 + 免费邮箱 + 泛泛需求 = 疑可疑 / 钓鱼线索 → 留 C（不主动发）', []),
    'SC-1907': ('keep_C', '尼泊尔 saileshshrm@gmail.com（自建站「4 & 8 port PoE with cloud management」）：云管理 Saga 不供 → 留 C', []),
    'SC-1908': ('keep_C', '加纳 Gideon Simpini（自建站「5 电口」；gmail）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1915': ('keep_C', '尼日利亚 Trushift Solutions（自建站「2 光 4 管理小壳」；gmail）：阿里巴巴 / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1930': ('keep_C', '墨西哥 giacintoconti@outlook.com（RFQ「8 路 CWDM 模块」）：CWDM 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1995': ('keep_C', '尼日利亚 adekunleadekoya@gmail.com（RFQ「收发器 / 光模块」）：光模块本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1996': ('keep_C', '南苏丹 charityossa@gmail.com（自建站「SFP Modules」）：光模块本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1999': ('keep_C', 'mohamedghet1.ly@gmail.com（表内印度，.ly 疑利比亚；询盘「无人机模块」）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-2037': ('keep_C', '秘鲁 salvador.nepo94@gmail.com（RFQ「无人机模块」；WA 加不上）：无人机 / 无人机模块 = 品类不符 → 留 C', []),
    'SC-2002': ('keep_C', '喀麦隆 wadebe2016@gmail.com（RFQ「16 槽收发器机架」）：机架 Saga 不供 + 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-2003': ('keep_C', '巴西 willdenim@gmail.com（自建站「4V1D 1080P」视频光端机）：VC 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
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
    L = [f'# C 池 · 闸 1 · 第 39 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 221–275 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：群发冷名单（免费邮箱 + 公司网址）30、仅网址 2、阿里巴巴 / 自建站个人 15、可疑线索 4、守界乌克兰 1。候选 5 = 印度 Vigil（hisource）+ 越南 Viễn Thông Hà Nội / Switch Quang / Việt Long（点名中国品牌 + 越南先例）+ 拉脱维亚 Signalizācija（Utepo + 欧洲）。', '',
         '> 值得留意的留 C：Talad Security VN（ONV 全线，无路径待巡检）、Staphone VN（疑本土品牌 oem_target 备查）、Thiết Bị Quang VN（傲通达大买家 = 本职线）、SAP Telecom AE（工业方案商，13 推 0 回）、Matchdigi IN（有 WA 按钮）、Micronet KE（要 edgecore 型号）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批39_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
