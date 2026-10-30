#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-01（T29-U138 2026-10-30）· A 类「挖个底掉」第一批：土耳其 11 户网查（年报 / 领英公司页 / KP / 人事变动 / 展会 / 论坛 / 供应商关系）+ A-DEEP-01 网查事实镜像进 intel。
来源 = web_search 结果页（引文原样，URL 可复核）。幂等。
"""
import os
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-01'
ITEMS = [
    # SA-086 Netaş（PI 成单）
    ('SA-086', '年报/财务', '2025 Faaliyet Raporu：2025 yıl sonu itibarıyla çalışan sayısı 1.264；800’e yakın uzman kadro，81 ili kapsayan dağıtım ve servis ağı', 'https://netas.com.tr/docs/tr/faaliyet_raporlari/2025/Netas%20Faaliyet%20Raporu%202025.pdf', '上市公司年报 PDF（2026-03 发布）；可逐年追'),
    ('SA-086', '年报/财务', 'PitchBook：As of 31-Dec-2025 trailing 12-month revenue $304M · Employees 1,264 · founded 1967 · Public（BIST: NETAS，1993-03-03 上市）', 'https://pitchbook.com/profiles/company/58001-86', ''),
    ('SA-086', '年报/财务', 'cnbce 财报摘要：Hasılat 1.719.059.796 TL · Brüt Kar 125.156.133 TL · Sürdürülen Faaliyetler Dönem Zararı -83.668.798 TL · Çalışan 1403 · Kuruluş 31/03/1967', 'https://www.cnbce.com/borsa/hisseler/netas-netas-telekomunikasyon-as', '期间未标，按页面最新季报理解；亏损中'),
    ('SA-086', '人事变动', '2026-07-31 KAP 特别公告：Yönetim Kurulu Başkanı Aiguang Peng görevinden ayrıldı；yerine ZTE Avrupa Başkanı Zhi Ling atandı（首个股东大会追认）', 'https://www.yatirimx.com.tr/sirket-haberleri/netasta-yonetim-degisikligi-baskanlik-koltugu-el-degistirdi/22749', '母公司 ZTE 派任；Saga 在 Netaş 的采购关系不受影响但要知道板子上是 ZTE 的人'),
    ('SA-086', '新闻/招标', '2026-08-07 Dijital Haber：Zhi Ling 被任命为 Yönetim Kurulu Üyesi、Başkanı 和 Kurumsal Yönetim Komitesi Üyesi', 'https://www.dijitalhaber.com.tr/yonetim-kurulu-ceo-genel-mudur-atamalari/netas-yonetim-kurulu-baskanligi-gorevine-zhi-ling-getirildi-38870', ''),
    # SA-077 Angora Networks（PI 成单）
    ('SA-077', '领英公司页', 'LinkedIn：Angora Networks · 2.110 takipçi · Bilgi Teknolojisi ve Hizmetleri · 11–50 çalışan · Genel Merkez Ankara · Kuruluş 2016 · Uzmanlık IT Network, Network Switch, Network Management', 'https://tr.linkedin.com/company/angora-networks', '总部是安卡拉（研究档原写 İstanbul 商号，以 LinkedIn 为准核对）'),
    ('SA-077', 'KP', 'LinkedIn 员工：Mehmet Yasin Koru — Hardware Design Lead；Ufuk Gökçe — Sales manager & Business Development Manager；Levent KILIÇ — Technology Evangelist and Consultant / Business Advisor（ICT Media 2023 称其 Genel Müdür）', 'https://tr.linkedin.com/company/angora-networks', '硬件设计负责人 = OEM/贴牌谈规格的人'),
    ('SA-077', '新闻/招标', 'ICT Media 2023-06：Levent KILIÇ：「Biz kendi satışlarımızı kendi markamız ile yapıyoruz ama yeterli sayıda, büyüklükte projeler olduğu zaman OEM ürünlerde üretebiliyoruz」；Teknokent’e geçtik，yazılım tarafı büyüyor', 'https://ictmedia.com.tr/haber/yerli-bir-ureticiye-verilebilecek-en-buyuk-destek-onun-urunlerini-kullanmaktir', '自牌为主、也接 OEM；SD-WAN / 软件方向'),
    ('SA-077', '供应商/品牌关系', '官网：Turkey’s network equipment manufacturer；2023-12 Data Diode 支持 ModBUS/OPC；2021-06 PacketFence NAC 集成；Turkish Cyber Security Cluster 成员', 'https://www.angoranetworks.com/?lang=en', '本地化制造叙事（yerli）→ Saga 只做零部件级/白牌供货，不抢其品牌'),
    # SA-030 Snexus
    ('SA-030', '领英公司页', 'Lusha：SNEXUS NETWORKS · Istanbul · Computer Networking Products · 11–50 employees；产品线 Switches / Industrial Switches / PtP bridges for CCTV / Access Points', 'https://www.lusha.com/business/5c6520780ede2087/', ''),
    ('SA-030', 'KP', 'LinkedIn：Erdem Timur Koca — SNEXUS NETWORKS，15+ 年 IT 销售/BD；ZyXEL Certified Network Professional（Switch/Security/Wireless）、EnGenius Network Associate；帖子：「ISN-GS2300-10FP Industrial is one of our top-selling industrial switches」', 'https://www.linkedin.com/in/erdem-timur-koca-01565b63/', '前 ZyXEL/EnGenius 渠道背景；工业 10 口 PoE 是其畅销款 → STI-288DGGPM 对位'),
    ('SA-030', '供应商/品牌关系', '官网产品线：Plug & Play Megabit/Gigabit PoE Series · Managed Gigabit · Managed 10G · Fiber Backbone Switches · Industrial Switches · Modules（自有品牌 Snexus）', 'https://www.snexus.com.tr/en', '自牌全系交换机 → OEM 30% 档，白牌来源可替换'),
    # SA-009 Koptek
    ('SA-009', '供应商/品牌关系', '官网 Hakkımızda：2010 年起 DCN（Digital China Network）土耳其分销商，2020 年在土运行设备超 10,000 台；2020 年起 ONV Technologies 分销商（工业与室内交换机）', 'http://www.coptek.com.tr/hakkimizda.html', 'ONV = 深圳白牌工业交换机厂 → 同源竞争；Saga 卖点只能是 Marvell/CENTEC 方案与交期'),
    ('SA-009', '展会/活动', '2018 DCN Distribütörler Toplantısı, Bali — 公司代表作行业分享（官网照片说明）', 'http://www.coptek.com.tr/hakkimizda.html', ''),
    ('SA-009', '登记', 'firmatlas：Koptek Bilgisayar ve İletişim Sistemleri San. ve Tic. Ltd. Şti. · Gayrettepe Mah. Fuatsarp Sok. Mutlu Apt. No:4/3 Balmumcu / İstanbul · 212 275 79 53', 'https://www.firmatlas.com/koptek-bilgisayar-ve-iletisim-sistemleri-san-ve-tic-ltd-sti/', ''),
    # SA-055 Nova Grup
    ('SA-055', '领英公司页', '官网/FB：Nova Grup Mühendislik 2002 年成立，Zayıf Akım（弱电）进口 + 批发：Kamera, Alarm, Data, Fiber, Uydu, Yangın, İnterkom；自有品牌 NOVACOM；办公点 İzmir / İstanbul / Ankara / Şanlıurfa / London UK；LinkedIn company/novagrup', 'https://www.facebook.com/esmakdd/', ''),
    ('SA-055', 'KP', 'LinkedIn：Erdal Özcan — Satış Müdürü, Nova Grup Mühendislik（Ankara，2023-08 至今；电气电子工程师）', 'https://www.linkedin.com/in/erdal-%C3%B6zcan-7904a862/', '安卡拉销售经理，2023 新入职'),
    ('SA-055', '供应商/品牌关系', '官网 Hakkımızda：NOVACOM markası altında sunduğu ürünler；Uydu ve CCTV 为主的弱电全品类', 'https://www.novacom.com.tr/hakkimizda', '自牌弱电 → PoE 交换机贴 NOVACOM 的 OEM 口子'),
    # SA-047 SGE
    ('SA-047', '领英公司页', 'LinkedIn：SGE Muhendislik · 1.042 takipçi · Endüstriyel Otomasyon · 11–50 çalışan · Istanbul · Kuruluş 2007 · Scada Automation SAS, Relays and RTU’s, Test and Measurement, Energy Meters', 'https://tr.linkedin.com/company/sge-muhendislik', ''),
    ('SA-047', '供应商/品牌关系', '网店在售工业以太网交换机 MIGE2205G（5×1G DIN 导轨非管理，DC9-60V / AC85-264V 版，交期 5 周）', 'https://shop.sge.com.tr/urundetay-mige2205g-5x1gbit-layer2-switch-295-2883.html', '在转售他家工业交换机且交期 5 周 → Saga STI-144GP/288 系列可比交期'),
    ('SA-047', '展会/活动', 'Facebook：2024-06-05～08 WIN Otomasyon Fuarı 参展（zenon SCADA + CET 电能分析仪）', 'https://www.facebook.com/SgeMuhendislik', '每年 6 月 WIN Eurasia（Istanbul）'),
    ('SA-047', '人事变动', 'LinkedIn 近 3 月招聘：TEST VE ÖLÇÜ ALETLERİ SATIŞ MÜHENDİSİ（İstanbul Anadolu yakası）', 'https://tr.linkedin.com/company/sge-muhendislik', '在扩销售团队'),
    # SA-076 TBI Telemobil
    ('SA-076', '领英公司页', 'LinkedIn：TBI - Telemobil · 1.402 takipçi · BT Hizmetleri ve BT Danışmanlığı · 51–200 çalışan（97 çalışan LinkedIn 可见）· ISTANBUL Üsküdar · Kuruluş 2005；业务：BT Sistem Entegrasyonu / Elektrik Taahhüt / Bina Yönetim, Otomasyon ve Zayıf Akım', 'https://tr.linkedin.com/company/tbitelemobil', ''),
    ('SA-076', '人事变动', 'kariyer.net 2025-11-12：招聘 İnşaat Teknikeri（Hatay：Antakya / İskenderun / Arsuz）；公司档：Bilişim, Elektrik & Elektronik Proje Taahhüt, Elektronik Güvenlik Sistemleri, İnşaat · 50–74 Çalışan', 'https://www.kariyer.net/is-ilani/telemobil-bilgi-iletisim-hizmetleri-san-ve-tic-insaat-teknikeri-4299443', '哈塔伊（震后重建）有项目'),
    ('SA-076', '新闻/招标', 'ZoomInfo：data center construction, electrical and mechanical contracting, automation solutions；clientele education / healthcare / construction', 'https://www.zoominfo.com/c/tbi---telemobil/372637611', ''),
    # SA-085 HCS
    ('SA-085', '领英公司页', 'LinkedIn：HCS Kablolama Sistemleri · 867 takipçi · Bilgisayar Ağları Ürünleri · 51–200 çalışan · İstanbul Başakşehir · Kuruluş 2000；土耳其 + 海外经销商网络；近期帖：HCS DataLight SLT 室外单模光缆', 'https://tr.linkedin.com/company/hcskablolamasistemleri', ''),
    ('SA-085', '供应商/品牌关系', 'GelecekBT 经销页：HCS 为土耳其本土全球品牌，铜缆 CAT6/6A/7 + 光纤 + MTP/MPO + 数据中心布线方案；Phy-FiXX 物理层管理平台', 'https://gelecekbt.com/hcs', '自牌布线品牌、无有源设备线 → 「HCS 牌 PoE 交换机」OEM 切口'),
    # SB-132 F.A.S.T.
    ('SB-132', '领英公司页', 'Crunchbase：FAST（Fabrika Aygıtları Sistem Teknolojisi A.Ş.）· Istanbul · 11–50 · distributor of AC speed control devices, CNC control units, and power sources；LinkedIn company/fasttr', 'https://www.crunchbase.com/organization/fabrika-ayg%C4%B1tlar%C4%B1-sistem-teknolojisi', ''),
    ('SB-132', '供应商/品牌关系', 'LinkedIn 活动标签：#meanwell #shihlin #renu #texcomputer #suncarve #inverter #hcfa — 代理 Mean Well 电源、Shihlin 变频、RENU PLC/HMI、Texcomputer CNC', 'https://www.linkedin.com/in/%C3%B6mer-aydin-2a465b62/', '工业自动化分销，Mean Well 电源 + 工业交换机是自然搭配'),
    ('SB-132', '论坛/社区', '自营论坛 www.fasttr.com/forum（Şener Üstbaş 在 LinkedIn 反复引流）', 'https://www.linkedin.com/in/g%C3%B6knur-mekatronik-352077186/', '可在其论坛看客户问什么'),
    ('SB-132', 'KP', 'LinkedIn：Şener Üstbaş — F.A.S.T.（活跃发帖人，RENU PLC/HMI 推广）', 'https://www.linkedin.com/in/g%C3%B6knur-mekatronik-352077186/', ''),
    # SB-137 Oral
    ('SB-137', '领英公司页', '官网：Oral Companies 1982 年起在 Kuzey Kıbrıs（北塞浦路斯）经营：Oral Güvenlik Sistemleri / Oral Alüminyum / Oral Çelik Yapı / Oral Fotoğrafçılık …；RocketReach：Oral Güvenlik Sistemleri 6 名员工', 'https://www.oralcompanies.com/', '实际在北塞浦路斯，不是土耳其本土；家族集团下的小安防公司'),
    ('SB-137', 'KP', 'AeroLeads：Metin Oral — Business Owner, Oral Companies；Muhammad Azeem — Manager, Oral Güvenlik Sistemleri；RocketReach：Mevlüt Önal — Computer Technician', 'https://aeroleads.com/c/oralguvenliksistemleri', ''),
    # SB-392 Makro Sistem
    ('SB-392', '供应商/品牌关系', '官网：Makro Sistem Dış Tic. A.Ş. — i-PRO（原 Panasonic Security Systems）Türkiye Premium Distribütörü；Edge AI 摄像机 250+ 型号、NVR、CCTV、火灾探测', 'https://makrosisas.com.tr/', '高端摄像机分销 → 配套 PoE 交换机（STC 系列）'),
    ('SB-392', '登记', '官网联系：Kuştepe Mah. Leylak 1 Sok. Nursanlar İş Merkezi No:1 Kat:7 Daire:26 Şişli / İSTANBUL · +90 212 272 47 92 · info@makrosisas.com.tr', 'https://makrosisas.com.tr/contact.html', ''),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    # A-DEEP-01 网查事实 → intel 镜像
    m = 0
    import glob
    for p in glob.glob(os.path.join(IS.RESEARCH, '*.json')):
        rs = json.load(open(p, encoding='utf-8'))
        wf = (rs.get('a_deep') or {}).get('web_facts') or []
        if not wf:
            continue
        code = rs['code']
        ch = False
        for f in wf:
            u = f.get('url', '')
            kind = '领英公司页' if 'linkedin.com' in u else ('登记' if any(k in u for k in ('zauba', 'tracxn', 'companies', 'dnb.com', 'romanian-companies', 'atoka', 'zoominfo', 'crunchbase', 'firmatlas')) else '新闻/招标')
            if IS.add(code, kind, f.get('quote', ''), u, f.get('date', D), 'A-DEEP-01 网查镜像', 'A-DEEP-01', True, rs=rs, persist=False):
                ch = True
                m += 1
        if ch:
            IS.save(code, rs)
    print(B, 'items +', n, 'mirror +', m)


if __name__ == '__main__':
    main()
