#!/usr/bin/env python3
"""Saga C · 闸 2 复查批 G2R-01（2026-10-29，T29-U121「OK 继续」）—— 闸 2 回 C「未坐实」28 户里有域名的 21 户，各做第 2 次检索（站内 / 域名 + 登记关键词）。

无域名 / 仅免费邮箱 / 仅微信的 7 户（SC-1025 / SC-1190 / SC-2271 / SC-2386 / SC-2504 / SC-296 + 守界 SC-859）不查：要 Simon 回信 / 微信问法人名才有抓手。
结果：入池 ○ 6（SC-729 / SC-623 / SC-509 / SC-1203 / SC-1883 / SC-1855）+ 观察 △ 1（SC-969）+ 留 C 14（其中 7 户补到法人名 / 地址但不够入池；SC-2143 国别疑为阿根廷）。
口径同 docs/C池三闸筛选_方案_2026-10-29.md §2 + 名册「本批评估口径」：坐实 + 对位 + 路径 → ○；部分坐实（官方页有法人名无注册号）+ 对位 → ○ prepay / reg_pending；个体 / 微型 / 红旗 → 留 C。
副作用（幂等，按 batch 标记）：data/saga_clients/sieve.json；P池_巡检表 追加 7 行；名册追加「Saga C 复查 · 批 G2R-01」小节。
用法：python3 scripts/saga_clients/sieve_batches/g2r_001.py
"""
import collections
import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
SIEVE = os.path.join(ROOT, 'data', 'saga_clients', 'sieve.json')
WATCH = os.path.join(ROOT, 'data', 'saga_clients', 'P池_巡检表_2026-10-29.csv')
ROSTER = os.path.join(ROOT, 'docs', 'P池_资产池名册_2026-10-29.md')
BATCH = 'G2R-01'
DATE = '2026-10-29'
NEXT_CHECK = '2026-12-28'
CHECK_ITEMS = '官网改版 / 新品 / 招聘 / 社媒（LinkedIn / FB / IG）/ GitHub / 展会出席 / 新闻稿 / 域名 MX 存活'

# code → dict(verdict, star, group, company, country, links, reason, facts[(what,url)], tags)
V = {
    # ---------- 入池 ○ ----------
    'SC-623': dict(verdict='pool', star='○', group='俄语区', company='ООО «АКОМ»（Industrial Nets / i-nets.ru）', country='俄罗斯', links='industrialnets.ru | i-nets.ru | anybus.ru',
                   reason='○ 俄罗斯 · 工业网络设备分销 20%：ООО «АКОМ»（Автоматизация и КОМмуникации；ИНН 7448060703，ОГРН 1047422004475（2004 起）；Челябинск ул. Сахарова 1；8 800 222 32 80；sales@i-nets.ru；тех. директор Молчанов Алексей Юрьевич acom@industrialnets.ru；站点 industrialnets.ru + anybus.ru = HMS/Anybus 渠道）官网联系页坐实；进口中国同类 ✔ 对位（网关 / 转换器 / 交换机）✔ 具名 KP ✔；收款待定（RU）→ 预付 100% 起步',
                   facts=[('官网联系页：ООО "АКОМ" ИНН 7448060703 ОГРН 1047422004475 · Челябинск · sales@i-nets.ru · Молчанов А.Ю. acom@industrialnets.ru', 'https://www.industrialnets.ru/contact/')],
                   tags=['ru_payment', 'prepay', 'industrial']),
    'SC-729': dict(verdict='pool', star='○', group='俄语区', company='Brown Bear（brownbear.ru）', country='俄罗斯', links='brownbear.ru',
                   reason='○ 俄罗斯 · 安防 / 网络设备批发 20%：brownbear.ru 对应法人 ИНН 9728025085 / ОГРН 1217700015807（Москва，2021 登记；类目：安防系统、网络设备、电缆、电信设备）第三方聚合页部分坐实（官网页脚未直取 → reg_pending 复核）；Planet 渠道 ✔ 对位 ✔ order@ 路径 ✔；年轻公司 + 收款待定 → 预付 100%',
                   facts=[('tapki.com 聚合：brownbear.ru · TIN 9728025085 · OGRN 1217700015807 · 安防 / 网络设备 / 电缆 / 电信设备', 'https://tapki.com/en/email/753520044')],
                   tags=['ru_payment', 'prepay', 'reg_pending']),
    'SC-509': dict(verdict='pool', star='○', group='印度 / 南亚', company='NexTik Bharat Private Limited', country='印度', links='nextik.co.in',
                   reason='○ 印度 · 自有品牌 FTTH / 交换机制造商 OEM 30%：NEXTIK BHARAT PRIVATE LIMITED（CIN U72900DL2021PTC377914，2021-03-03 成立；805 Devika Tower Nehru Place New Delhi 110019 + Noida Sec 57 制造基地；+91 8130608406；info@nextik.co.in；自述「leading switch provider in India」core switch / FTTH / WDM / 数据中心方案）Tracxn + 官网坐实；品牌商 ✔ 对位 ✔ → OEM 目标，预付 100% 起步',
                   facts=[('官网联系页：Corporate Office 805 Devika Tower Nehru Place · 制造 A-29 Sec 57 Noida · +91 8130608406 · info@nextik.co.in', 'https://nextik.co.in/contact'),
                          ('Tracxn：NEXTIK BHARAT PRIVATE LIMITED · CIN U72900DL2021PTC377914 · 2021-03-03 · 同址', 'https://tracxn.com/d/legal-entities/india/nextik-bharat-private-limited/__zlEjgHjbrKjywYO5rm8g6JO-O1brfcN1Z7OuD5hZQG0'),
                          ('About：FTTH 10 年 · 交换机 / 光缆方案 · 电信 / 园区 / 监控 / 数据中心', 'https://nextik.co.in/about-us.php')],
                   tags=['oem_target', 'prepay']),
    'SC-1203': dict(verdict='pool', star='○', group='印度 / 南亚', company='Lapis Technologies（Hyderabad）', country='印度', links='lapistechnologies.in',
                    reason='○ 印度 · 网络集成商 25%：Lapis Technologies（Secunderabad / Hyderabad 500084；+91 40 6690 4704；11–50 人；设计 / 部署 / 托管信息网络；Pre-Sales Head Sk Gopi 2009 至今）ZoomInfo + Crunchbase 名录部分坐实（CIN 未取；此前 Shimoga 同名壳不是它）；对位 ✔（园区网交换机）；非主区 → 预付 100%，reg_pending',
                    facts=[('ZoomInfo：Lapis technologies · Hyderabad Telangana 500084 · +91 4066904704 · lapistechnologies.in', 'https://www.zoominfo.com/c/lapis-technologies/429866407'),
                           ('Crunchbase：Lapis Technologies · Secunderabad · 11–50 · 信息网络设计 / 部署 / 托管', 'https://www.crunchbase.com/organization/lapis-technologies')],
                    tags=['prepay', 'reg_pending', 'integrator']),
    'SC-1883': dict(verdict='pool', star='○', group='东亚 / 东南亚 / 大洋洲', company='Công ty TNHH A.N.F.A Việt Nam（ANFA Vietnam Co., Ltd.）', country='越南', links='anfatech.com.vn',
                    reason='○ 越南 · NAS / 网络设备分销 20%：Công ty TNHH A.N.F.A Việt Nam（129E Nguyễn Đình Chính P8 Phú Nhuận TP.HCM + Hà Nội 办公室；QNAP NAS 越南渠道；info@ / sales@anfatech.com.vn；Mr. Thắng 0909 560 555 thang.nv@、Mr. Quý quy.nv@ 具名）官网 + FB 法人名坐实（MST 未取）；NAS 渠道买交换机对位 ✔；非主区 → 预付 100%',
                    facts=[('官网文章页脚：Công ty TNHH A.N.F.A Việt Nam · 129E Nguyễn Đình Chính · info@ / sales@ / quy.nv@anfatech.com.vn', 'https://anfatech.com.vn/uncategorized/optimize-nas-performance/'),
                           ('Facebook：ANFA Vietnam Co., Ltd. · HCMC · +84 90 956 05 55 · Thang.nv@anfatech.com.vn', 'https://www.facebook.com/anfatech.com.vn/')],
                    tags=['prepay', 'reg_pending']),
    'SC-1855': dict(verdict='pool', star='○', group='四主区 + 波兰', company='Kıraç Bilgi ve İletişim Teknolojileri San. ve Tic. A.Ş.', country='土耳其', links='kiracbilisim.com.tr | zkr.com.tr',
                    reason='○ 土耳其主区 · 医疗通信系统制造商（品牌 ZKR）OEM 30%：Kıraç Bilgi ve İletişim Teknolojileri San. ve Tic. A.Ş.（Eskişehir 75. Yıl OSB Şehitler Bulvarı No:21 Odunpazarı 26250；2005-01-06 成立；Kıraç Group 1982 起；Ankara Ümitköy 办公室；护士呼叫 / IP 通信方案自产）EMIS + D&B 坐实；主区 ✔ 自有品牌 ✔ 具名 KP shaalan@ ✔；此前 9 推 0 回 → 入池只巡检 + 换 KP 再触',
                    facts=[('EMIS：Kirac Bilgi Ve Iletisim Teknolojileri Sanayi Ve Ticaret A.S. · Eskişehir · 成立 2005-01-06', 'https://www.emis.com/php/company-profile/TR/Kirac_Bilgi_Ve_Iletisim_Teknolojileri_AS_en_3316187.html'),
                           ('D&B：同名 A.Ş. · NO:21 75. Yıl OSB Şehitler Bulvarı Odunpazarı 26250 · 网站 zkr.com.tr', 'https://www.dnb.com/business-directory/company-profiles.kirac_bilgi_ve_iletisim_teknolojileri_sanayi_ve_ticaret_anonim_sirketi.9deee9e9a1e2f55c85e3f1fcfda65cd6.html'),
                           ('Turkish Medical Index：ZKR = Kıraç Bilişim 商标（2011）· 护士呼叫 / 代码警示 / 语音通信 · Ankara +90 312 446 0344', 'https://www.turkishmedicalindex.com/tmi?slug=kirac-bilgi-ve-iletisim-teknolojileri-san-ve-tic-a-s')],
                    tags=['oem_target', 'cold']),
    # ---------- 观察 △ ----------
    'SC-969': dict(verdict='pool_watch', star='△', group='印度 / 南亚', company='Trueview（trueview.co.in）', country='印度', links='trueview.co.in',
                   reason='△ 印度 · 自有品牌 CCTV / IFPD / 数字标牌 OEM 30%（观察）：Trueview（2011 起；Plot A-114/6 Five Star Shendra MIDC + Plot 56 AURIC，Chhatrapati Sambhajinagar/Aurangabad；+91 92255 50000；自称 India\'s No 1 CCTV & display brand）官网地址坐实、法人名 / CIN 未取（Delhi / Mumbai 同名两户都不是）；具名 KP manish@ / rupesh.bagde@ ✔ 对位 ✔ → 观察档：法人坐实即转 ○',
                   facts=[('官网联系页：Plot No. A-114/6 Five Star Shendra MIDC 431007 · +91 92255 50000', 'https://trueview.co.in/contact-us/'),
                          ('官网首页：AURIC Plot 56 Sector 13 办公室', 'https://trueview.co.in/'),
                          ('About：2011 年成立', 'https://trueview.co.in/about-us/')],
                   tags=['oem_target', 'reg_pending']),
}

# 留 C：复查补记（不入池）
KEEP = {
    'SC-912': '复查 1 查仍无（qpoptom.ru 法人未取）→ 留 C',
    'SC-2841': '复查：piir.ru 商品页脚「Поставщик PIIR.RU：ИП Илларионов，ИНН 501712304861，ОГРНИП 316502400063255，Москва」= 个体经营者 → 坐实但个体 → 留 C（来信再起预付 100%）',
    'SC-2972': '复查：仅 ООО «Актел»（Москва，ИНН 9722065388，2023-12 登记，已清算）同名，域名归属仍未证 → 留 C',
    'SC-860': '复查：mistercom.ru/about.html 页脚 = ООО «Мистерком»（ИНН 5005054785，ОГРН 1115005002386，Воскресенск ул. Титова 13 + Москва Б. Косинская 27；ОКВЭД 47.43；ГД Корзенникова Н.Ю.）坐实，但即此前「执行程序 34 件」主体 → 红旗保留，留 C',
    'SC-324': '复查：官网联系页 ENERCORE SYSTEMS，204 Luxmi Building Sector 10A Gurugram 122001，+91 124 46082947，hello@ → 地址坐实、无法人形式 / 注册号，微型 → 留 C',
    'SC-1322': '复查：Active System Integration（Chennai Anna Nagar East，New No.18 N Block 21st St；admin@ / sales@asi.ind.in；044 4556 6999）安防集成商，官网地址坐实、无注册号、体量不明 → 留 C',
    'SC-1366': '复查 1 查仍只返回 Mazenet（Coimbatore 培训公司）→ Mayenet 法人未取 → 留 C（样品例外保留）',
    'SC-1020': '复查：moon.kz 「реквизиты」页为模板占位（虚构银行），页脚仅 Алматы ул. Муканова 245 + im@moon.kz（电脑配件 + Tiandy/Cantonk 监控电商）→ 法人未取 → 留 C',
    'SC-1976': '复查：官网联系页 = "TIGER & CCTV" LTD（SIA TIGER & CCTV，Katlakalna iela 11/1 Rīga；+371 28323820；tiger.cctv@inbox.lv；安防 / 太阳能安装 + 门店）法人名坐实、注册号未取、免费邮箱 + 门店型微型 → 留 C',
    'SC-2143': '复查：ZoomInfo 把 cygnus.la 归为 Cygnus Electronics（Buenos Aires，+54 11 3221 8153）→ 国别疑为阿根廷而非塞浦路斯（待 Simon 确认后 country_fix）；法人 / CUIT 未取 + Simon 判不行 → 留 C',
    'SC-2437': '复查：官网联系页 = Nana Corporation Co., Ltd.（Samut Prakan 10290 + Bangkok Bang Khun Thian；+66 2 101 2055；sales@nana-tech.net）法人名坐实、注册号未取；冷户 + Simon 判不行 → 留 C',
    'SC-2622': '复查：ZoomInfo cctvvideo.com = 387 Canal St New York 10013，1–10 人安防批发网店，(212) 431-2622 → 微型 → 留 C',
    'SC-3057': '复查：检索只返回 kamery-hikvision-sk.sk（Bratislava，另一家）→ kamery-hikvision.sk 法人仍未取 → 留 C',
    'SC-1755': '复查 1 查仍无（jjenka.com 无公司信息）→ 留 C',
}
KEEP_FACTS = {
    'SC-2841': [('piir.ru 商品页脚：ИП Илларионов · ИНН 501712304861 · ОГРНИП 316502400063255', 'https://piir.ru/product/ip-videoregistrator-16-potokovyj-hiwatch-ds-n316-2-b/')],
    'SC-2972': [('rusprofile：ООО «Актел» ИНН 9722065388 · 2023-12-26 · ликвидирована', 'https://www.rusprofile.ru/id/1237700938573')],
    'SC-860': [('mistercom.ru/about：ООО «Мистерком» ИНН 5005054785 ОГРН 1115005002386', 'https://mistercom.ru/about.html'), ('saby.ru：ОКВЭД 47.43 · ГД Корзенникова Наталья Юрьевна · 招标 20 / 中标 10', 'https://saby.ru/profile/5005054785-500501001')],
    'SC-324': [('enercore.co.in/contact：ENERCORE SYSTEMS · 204 Luxmi Building Sector 10A Gurugram · hello@', 'https://enercore.co.in/contact.html')],
    'SC-1322': [('activesystemintegration.in 联系页：New No.18 N Block 21st St Anna Nagar East Chennai · admin@asi.ind.in', 'http://www.activesystemintegration.in/contact-us'), ('cctv.org.in About：ASI 团队 · admin@ / sales@asi.ind.in · 044 4556 6999', 'https://cctv.org.in/about-us.php')],
    'SC-1020': [('moon.kz 页脚：Алматы ул. Муканова 245 · im@moon.kz（реквизиты 页为模板）', 'https://moon.kz/contacts/requisites.php')],
    'SC-1976': [('signalizacija.lv 联系页："TIGER & CCTV" LTD · Katlakalna iela 11/1 Rīga · tiger.cctv@inbox.lv', 'https://www.signalizacija.lv/ru/contacts-50789')],
    'SC-2143': [('ZoomInfo：Cygnus Electronics (cygnus.la) · Buenos Aires · +54 1132218153', 'https://www.zoominfo.com/c/cygnus-electronics/547313862')],
    'SC-2437': [('nana-tech.net/contactus：Nana Corporation Co.,Ltd. · Samut Prakan 10290 / Bangkok · +66 2 101 2055 · sales@', 'https://www.nana-tech.net/contactus')],
    'SC-2622': [('ZoomInfo：Cctvvideo.com · 387 Canal St NYC 10013 · 1–10 人', 'https://www.zoominfo.com/c/cctvvideocom/1123301377')],
}


def main():
    s = json.load(open(SIEVE, encoding='utf-8'))
    n_pool = n_keep = 0
    for code, v in V.items():
        cur = s[code]
        if cur.get('batch') == BATCH:
            continue
        assert cur['verdict'] == 'keep_C' and cur.get('gate') == 2, (code, cur['verdict'], cur.get('gate'))
        row = {'verdict': v['verdict'], 'gate': 3, 'rule': 'P1', 'reason': f'{v["star"]} P 池{"正式入池" if v["verdict"] == "pool" else "观察档"}（档位 {v["star"]}，复查批 {BATCH}）：{v["reason"]}',
               'date': DATE, 'manual': True, 'batch': BATCH, 'g2_batch': cur.get('batch'), 'g2_reason': cur.get('reason'),
               'g1_batch': cur.get('g1_batch'), 'g1_reason': cur.get('g1_reason'), 'grade': v['star'], 'next_check': NEXT_CHECK,
               'tags': v.get('tags') or [], 'facts': [{'what': w, 'url': u, 'date': DATE} for w, u in v['facts']]}
        s[code] = {k: val for k, val in row.items() if val is not None}
        n_pool += 1
    for code, note in KEEP.items():
        cur = s[code]
        if f'｜{BATCH}：' in cur['reason']:
            continue
        assert cur['verdict'] == 'keep_C', code
        cur['reason'] = cur['reason'] + f'｜{BATCH}：{note}'
        cur.setdefault('facts', []).extend({'what': w, 'url': u, 'date': DATE} for w, u in KEEP_FACTS.get(code, []))
        cur['recheck'] = BATCH
        n_keep += 1
    rows = {k: v for k, v in s.items() if k != '_meta'}
    cnt = collections.Counter(v['verdict'] for v in rows.values())
    s['_meta'] = {'updated': DATE, 'rules': 'docs/C池三闸筛选_方案_2026-10-29.md §2', 'counts': dict(cnt), 'n': len(rows)}
    out = {'_meta': s['_meta']}
    out.update(sorted(rows.items()))
    json.dump(out, open(SIEVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)   # 与 sieve.py save_sieve 同格式

    with open(WATCH, encoding='utf-8-sig', newline='') as f:
        rws = list(csv.reader(f))
    header, body = rws[0], rws[1:]
    have = {r[0] for r in body}
    added = 0
    for code, v in V.items():
        if code in have:
            continue
        body.append([code, v['star'], '正式' if v['verdict'] == 'pool' else '观察', v['company'], v['country'], v['group'], v['links'],
                     '、'.join(v.get('tags') or []), DATE, NEXT_CHECK, CHECK_ITEMS, f'来源：Saga C（复查批 {BATCH}）；{v["reason"][:160]}'])
        added += 1
    with open(WATCH, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(body)

    marker = f'## Saga C 复查 · 批 {BATCH}'
    md = open(ROSTER, encoding='utf-8').read()
    if marker not in md:
        pools = [(c, v) for c, v in V.items() if v['verdict'] == 'pool']
        watch = [(c, v) for c, v in V.items() if v['verdict'] == 'pool_watch']
        lines = ['', marker + f'（{DATE}，正式 {len(pools)} / 观察 {len(watch)}）', '',
                 f'> 闸 2 回 C「未坐实」28 户里有域名的 21 户第 2 次检索（站内 / 域名 + 登记关键词）：入池 ○ {len(pools)} / 观察 △ {len(watch)} / 留 C {len(KEEP)}（其中 7 户补到法人名或地址但个体 / 微型 / 红旗 / 冷户不够入池）；无域名、仅免费邮箱或微信的 7 户要 Simon 回信时问法人名。巡检同表，下次 {NEXT_CHECK}。',
                 '', '| 编号 | 档 | 公司 | 国家 | 区域组 | 判语（摘） |', '|---|---|---|---|---|---|']
        for c, v in pools + watch:
            lines.append(f'| {c} | {v["star"]} | {v["company"]} | {v["country"]} | {v["group"]} | {v["reason"][:150].replace("|", "｜")}… |')
        lines.append('')
        open(ROSTER, 'a', encoding='utf-8').write('\n'.join(lines))
    print(BATCH, 'pool+', n_pool, 'keep_noted', n_keep, 'csv+', added, dict(cnt))


if __name__ == '__main__':
    main()
