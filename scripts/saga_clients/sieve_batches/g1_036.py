#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 1 · 第 36 批（2026-10-29）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 56–110 户（按综合分序，SC-556 … SC-1205）。

构成：阿里巴巴 RFQ / Shopify / 自建站免费邮箱个人 28、展会 / 微信 / WA 接触 9（马来西亚 3、土耳其 2、印度 2、尼泊尔、菲律宾）、仅网址 6（德国 2、印度 3）、俄语区 4、守界 3（RAK 警察、伊朗、乌克兰）。
  · 口径同第 35 批（桶 ⑦）。候选 4 = EFB-Elektronik DE（德国大型网络基础设施分销，无邮箱 → 闸 2 查 HRB + 官网找采购；疑自有品牌待核）/ IT Group KZ（找 ONV 管理交换机 RFQ + 「有回复正在沟通」；哈萨克先例）/
    Projexon IN（Director 具名 + WA 问 L2 / L3 + 公司域名在）/ Bilimsa Teknoloji TR（8 光 8 电 PoE 网管已报价 $110，「最近在找这种产品」）。永久 pass 0。
  · 留意：quicklert.com PH（微信在，4 光 8 已报 $150，但 60W PoE++ Saga 无 + 菲律宾无先例）、atronicsys / iview-tech / unicamsystems IN（已买 ONV / hisource，无邮箱 → 找到邮箱即转候选）、addsecure.de（德国，巨头服务商，无邮箱）。

用法：python3 sieve_batches/g1_036.py   （幂等；写 sieve.json + docs/requirements/C池闸1_批36_2026-10-29.md）
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

BATCH = 'G1-36'
DATE = '2026-10-29'
CODES = ["SC-556", "SC-557", "SC-560", "SC-568", "SC-574", "SC-579", "SC-581", "SC-583", "SC-584", "SC-590", "SC-599", "SC-601", "SC-606", "SC-612", "SC-613", "SC-615", "SC-626", "SC-641", "SC-649", "SC-651", "SC-652", "SC-672", "SC-676", "SC-679", "SC-680", "SC-689", "SC-712", "SC-742", "SC-800", "SC-830", "SC-838", "SC-974", "SC-1003", "SC-1007", "SC-1008", "SC-1012", "SC-1019", "SC-1028", "SC-1034", "SC-1036", "SC-1039", "SC-1087", "SC-1143", "SC-1146", "SC-1167", "SC-3318", "SC-1170", "SC-1175", "SC-1177", "SC-1178", "SC-1185", "SC-1187", "SC-1190", "SC-1197", "SC-1205"]

OVERRIDE = {
    'SC-568': ('candidate', '德国 EFB-Elektronik（efb-elektronik.de；德国大型网络 / 布线基础设施分销商，Simon「比较专业 / 质量高」；无邮箱、官网正常）：德国主区 ✔ 大分销 ✔ 对位 ✔（疑有自有品牌线待闸 2 核）→ 闸 2 查底数（Impressum HRB）+ 官网找采购 / 供应商邮箱', []),
    'SC-574': ('candidate', '哈萨克斯坦 IT Group（itgroup.kz 域正常；2022 年 RFQ「找 ONV 的商业管理交换机」= 中国同类 ✔；备注「有回复，正在沟通」= 真回 ✔；Zhangozha Zamadion；gmail）：哈萨克先例 ✔ 对位 ✔ → 闸 2 查底数（statsnet / adata）；收款路径待 Simon', []),
    'SC-1177': ('candidate', '印度 Projexon（projexon.com 域正常；主要 CCTV，WhatsApp 问了 L2 / L3 交换机 ✔；R. Vignesh Director 具名 ✔；两手机）：印度点名国 ✔ 对位 ✔ 决策人 ✔ WA 可达 ✔（§5 ≥4 条）→ 闸 2 查底数（MCA 镜像）后 WA 一页纸（STC-2224GP $86 / STC-4424GCPM $165）', []),
    'SC-1190': ('candidate', '土耳其 Bilimsa Teknoloji（bilimsateknoloji@gmail.com；Muharrem Kılıç；8 光 8 电 PoE 网管已报 $110，「最近在找这种产品」= 真需求 ✔；两电话）：土耳其主区 ✔ 对位 ✔ 决策人 ✔ 可达 ✔ → 闸 2 查底数（vergi / 目录）后 WA 跟报价', []),
    'SC-672': ('keep_C', '阿联酋 Ministry of Interior RAK Police（Haja Mohideen Rizmy；gmail；工业交换机问网管）：警务 / 政府 = 守界（不做不 pass）→ 留 C', []),
    'SC-1146': ('keep_C', '伊朗 Arioonet（arioonet.com；主动询价光端机；仅电话）：伊朗守界 + 光端机本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1197': ('keep_C', '乌克兰 Etechnika（etechnika.com.ua；ukr.net；洪瑞的很多产品；7 推 0 回）：乌克兰守界 + 洪瑞 Q-33 → 留 C', []),
    'SC-676': ('keep_C', '马来西亚 Puncak Niaga Holdings（水务集团；只用 Cisco 想找其他牌子，AP 多，问 PoE + 网管；Muhammad Azhari；gmail；手机）：巨头终端用户 → 不 pass → 留 C（来询被动报价）', []),
    'SC-557': ('keep_C', '德国 AddSecure（addsecure.de；Simon「比较专业 / 质量高」；无邮箱、无电话）：欧洲 IoT / 安防通信服务巨头（运营商型）+ 无路径 → 留 C 待巡检', []),
    'SC-590': ('keep_C', '菲律宾 Quicklert（quicklert.com 域正常；Howie Cia；微信 HowieDay29；8 / 16 / 24 口工业 PoE 60W，问 4 光 8 报了 $150，用思科较多）：真需求 ✔ 微信可达 ✔ 但 60W PoE++ Saga 无（STI-488DGGPM 为 PoE+）+ 菲律宾无先例 → 留 C 储备（来询被动报价，如实说口径）', []),
    'SC-679': ('keep_C', '马来西亚 SPECTRUM（security 公司；展会谈了 CCTV 应用图 + 商业 PoE 1+2+8；Datuk Dr William Stevenson；icloud；手机）：展会接触 ✔ 对位 ✔ 但免费邮箱 + 马来西亚无先例 → 留 C 储备（一页纸一次后看）', []),
    'SC-680': ('keep_C', '马来西亚 SUREN Smart Electrical（旁边展位谈了很久；IP networking / CCTV；问 MC + 千兆 1+2+16 PoE 价格；Sathees Manager；gmail；手机）：展会接触 ✔ 具体需求 ✔ 决策人 ✔ 但免费邮箱 + 马来西亚无先例 → 留 C 储备（一页纸一次后看，有回应即转候选）', []),
    'SC-1039': ('keep_C', '尼泊尔 UDAAN Electronics Pvt Ltd（Ravi Gupta MD；对 SFP + 工业 FS 有兴趣让发资料；Simon 加了另一人微信 Bicky Patel；名片 home appliance / CATV / ISP equipment；域名 nxdomain；gmail）：微信可达 ✔ 决策人 ✔ 但尼泊尔无先例 + 兼营杂 → 留 C 储备 + dayjob_fit（SFP）', ['dayjob_fit']),
    'SC-1003': ('keep_C', '奥地利 Bojan Skoric（仅电话 +43 664 655 1876；需要 PoE 8 口价格）：欧洲 ✔ 需求 ✔ 但个人名 / 仅电话 → 留 C 储备（WA 一页纸后看，问到公司名即转候选）', []),
    'SC-3318': ('keep_C', '土耳其（未具名；Evelyn 加了 WhatsApp +90 532 638 1462；要收发器，不会英语）：收发器 = 本职线 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1167': ('keep_C', '印度 VMO Broadband Pvt Ltd（ISP；Vipin Jangra；gmail；手机「可加」；1 推）：ISP 终端 → 留 C（来询被动报价）', []),
    'SC-712': ('keep_C', '印度 Atronic Systems（atronicsys.com 域正常；switch，从 ONV 买 = 中国同类 ✔；无邮箱）：印度点名国 ✔ 对位 ✔ 但无路径 → 留 C 待巡检（官网找到邮箱即转候选）', []),
    'SC-830': ('keep_C', '印度 iView Tech（iview-tech.com 域正常；买的 hisource 的 PoE = 中国同类 ✔；无邮箱）：印度 ✔ 对位 ✔ 无路径 → 留 C 待巡检（找到邮箱即转候选）', []),
    'SC-974': ('keep_C', '印度 Unicam Systems（unicamsystems.com 域正常；PoE switch，hisource 的 ✔；无邮箱）：印度 ✔ 对位 ✔ 无路径 → 留 C 待巡检（找到邮箱即转候选）', []),
    'SC-579': ('keep_C', '俄罗斯 Matrixcam（matrixcam.ru 域正常；联系用 mail.ru；CCTV + 商业 PoE，在用帧田的 = 中国同类 ✔；16 推 0 回）：俄罗斯 ✔ 对位 ✔ 但 16 推 0 回 + 免费邮箱 → 留 C 储备（换稿一次后看）', []),
    'SC-742': ('keep_C', '俄罗斯 CMD Video（cmdvideo.ru nxdomain；mail.ru；Utepo 的很多产品 ✔；WA +7 950 741 0925 在表；17 推 0 回）：俄罗斯 ✔ 对位 ✔ 但域死 + 17 推 0 回 → 留 C 储备（WA 试一次后看）', []),
    'SC-1187': ('keep_C', '俄罗斯 Amursat（amursat.ru 域正常；ya.ru；无需求记录）：冷户无信息 → 留 C', []),
    'SC-689': ('keep_C', '韩国 A Digital Media（adigitalmedia.co.kr；naver；大口 FS 没啥工业；23 推 0 回）：零回应冷户 → 留 C', []),
    'SC-800': ('keep_C', '韩国 Hanaend（hanaend.com；naver；工业 FS + bypass 方案；23 推 0 回）：bypass 本职线 + 零回应 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1036': ('keep_C', '韩国 Multicom System Co., Ltd（imulticom.co.kr；naver；Mr. Jang；11 推 0 回；无需求记录）：零回应冷户 → 留 C', []),
    'SC-599': ('keep_C', '阿尔及利亚 ZN Technology（询盘「2 光 8 管理 bypass」；gmail）：bypass 本职线 + 区域外 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-601': ('keep_C', '土耳其 Aksu Co 采购办事处（2014 年 RFQ「400G DAC」；Osman Aksu；gmail；手机）：DAC / 光模块本职线 + 陈旧 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-649': ('keep_C', '瑞典 sumitr87@gmail.com（RFQ「400G 交换机」）：数据中心 400G 非 Saga 线 → 留 C', []),
    'SC-838': ('keep_C', '美国 Koscom Cable（koscomcable.com / cdc.ua；Sergii Kushnarov Founder；gmail；问 2 光 4 管理 bypass 怎么用；8 推 0 回）：bypass 本职线 + 乌克兰关联 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1175': ('keep_C', '埃塞俄比亚 Miko（自建站询盘「百兆收发器」；gmail）：收发器本职线 + 区域外 → 留 C + dayjob_fit', ['dayjob_fit']),
    'SC-1012': ('keep_C', '土耳其 eren.yazici92@gmail.com（2015 年 RFQ「无人机」）：品类不符 → 留 C', []),
    'SC-1028': ('keep_C', '加拿大 tyrone.cousins@gmail.com（2010 年询盘「升压 5 口」；Brampton 地址）：升压 PoE Saga 不供 + 陈旧 → 留 C', []),
    'SC-612': ('keep_C', '意大利 cyrilpseter@hotmail.com（RFQ「16 槽管理机架」）：机架 Saga 不供 → 留 C', []),
    'SC-556': ('keep_C', '津巴布韦 Prime Traders（RFQ「26 口全电千兆商业 PoE」；gmail）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-560': ('keep_C', '以色列 avnerroman@gmail.com（RFQ「12 个 10G 光 L3 管理」）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-581': ('keep_C', '以色列 monifhadad@gmail.com（2020 年 RFQ「1+2+16FE 商业 PoE」）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-583': ('keep_C', '肯尼亚 muken automation（RFQ「5 电口带管理」；gmail）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-584': ('keep_C', '巴西 Namba Software（nambasoftware.com.br 域正常但联系用 gmail；用 Cisco 较多做项目）：软件 / 项目商 + 免费邮箱 → 留 C', []),
    'SC-606': ('keep_C', '西班牙 alexangelovmartinov@gmail.com（RFQ「商业 PoE 交换机」）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-613': ('keep_C', '美国 djj2148@gmail.com（Shopify 询盘「8 个 10G 光交换机」）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-615': ('keep_C', '意大利 francesco.castaldo@gmail.com（询盘「4 / 8 口 PoE 交换机」）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-626': ('keep_C', '美国 jpinformation@gmail.com（Shopify 询盘「8 个 10G 网交换机」）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-641': ('keep_C', '美国 rogwabbit@yahoo.com（Shopify 询盘「12 个 10G 光 L3 管理」；电话 334111114 疑假）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-651': ('keep_C', '美国 ucbced@gmail.com（Shopify 询盘「8 个 10G 网交换机」）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-652': ('keep_C', '加拿大 vano.argie@gmail.com（RFQ「商业 PoE 管理 16 口」）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1007': ('keep_C', '多哥 TESTIMONY（询盘「导轨非管理 PoE」；yahoo.fr）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1008': ('keep_C', '加纳 Vikipat Media Solutions（阿里巴巴广告「2 个 2+4 百兆商业 PoE」；gmail）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1019': ('keep_C', '印度 meet computer and cctv camera（自建站询盘「IM-FS140FE」型号指定；gmail）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1034': ('keep_C', '巴西 Ecopoxi Distributor Wholesale（2011 年 RFQ「PoE system」；Belo Horizonte；gmail）：陈旧 + 免费邮箱 → 留 C', []),
    'SC-1087': ('keep_C', '保加利亚 Kabeli.eu / XCom（kabeli.eu / xcombg.com 域正常，联系用 gmail；AHD / PoE / FS「东西比较杂」）：杂货网店 + 免费邮箱 → 留 C', []),
    'SC-1143': ('keep_C', '蒙古国 Simon（自建站询盘「12 光 12 电管理 PoE」；仅电话；WA 加不上）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1170': ('keep_C', '坦桑尼亚 Alpsa Company Limited（询盘「千兆 1 光 4 工业小壳」；gmail；WA 加不上）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1178': ('keep_C', '莫桑比克 Serviços de Telecomunicações（自建站询盘「2 光 8 PoE 商业级」；gmail；WA 加不上）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1185': ('keep_C', '阿曼 alexabir10567@gmail.com（RFQ「8+2+1 百兆商业 PoE」）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
    'SC-1205': ('keep_C', '新西兰 m.batmunkh@yahoo.com（RFQ「24 / 48 PoE + 10G 上联」）：阿里巴巴 / Shopify / 自建站零散询盘，免费邮箱、无公司域名 = 个人 / 非渠道买家 → 不入池、不 pass → 留 C（来询被动报价）', []),
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
    L = [f'# C 池 · 闸 1 · 第 36 批（{DATE}）—— 桶 ⑦「其余（免费邮箱 / 仅电话 / 仅网址）」第 56–110 户（{len(V)} 户）', '',
         f'> 口径 `docs/C池三闸筛选_方案_2026-10-29.md` §3 / §5 + 桶 ⑦ 口径（第 35 批报告）；写入 `data/saga_clients/sieve.json`（gate=1, batch={BATCH}）。'
         f' 结果：永久 pass **{c["pass_final"]}** / 留 C **{c["keep_C"]}** / 候选（进闸 2）**{c["candidate"]}**；标签 dayjob_fit {tg["dayjob_fit"]} / oem_target {tg["oem_target"]}。', '',
         '> 构成：阿里巴巴 RFQ / Shopify / 自建站免费邮箱个人 28、展会 / 微信 / WA 接触 9、仅网址 6、俄语区 4、守界 3。候选 4 = EFB-Elektronik（DE，大分销，无邮箱 → 闸 2 + 找采购）/ IT Group（KZ，ONV 同类 RFQ + 有回复）/ Projexon（IN，Director + WA + L2/L3 需求）/ Bilimsa Teknoloji（TR，8 光 8 电已报价 + 真需求）。', '',
         '> 值得留意的留 C：quicklert PH（微信 + 已报价，60W 口径 / 无先例）、atronicsys / iview-tech / unicamsystems IN（已买中国 PoE，无邮箱 → 找到即转候选）、addsecure.de / efb 之外的德国仅网址户、SUREN / SPECTRUM / Puncak Niaga MY（展会接触，免费邮箱）、UDAAN NP（Simon 加了微信）。**Simon 可按编号否决**。', '']
    for verdict, title in (('pass_final', '永久 pass（告别）'), ('candidate', '候选 → 闸 2'), ('keep_C', '留 C（储备）')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 理由 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(tags)} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸1_批36_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), dict(tg), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
