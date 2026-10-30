#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-02（T29-U138 2026-10-30）· 土耳其第二批 5 户（Bilge / Zeytek / Onsis / Fiberix / Hiperonline）。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-02'
ITEMS = [
    ('SB-074', '领英公司页', 'LinkedIn：Bilge Güvenlik Sistemleri ve Teknoloji A.Ş · 135 followers · Security Systems Services · 11–50 employees · İstanbul · Founded 2004；业务 CCTV、Zayıf Akım、Yapısal Kablolama、Trafik Yönetim', 'https://www.linkedin.com/company/bilge-g%C3%BCvenlik-sistemleri-teknoloji-a-%C5%9F/', ''),
    ('SB-074', '登记', '官网 Kurumsal：Bilge Güvenlik ve Teknoloji A.Ş.，2003 年成立，İstanbul / Ankara / İzmir 三地分支，电子安防系统集成商', 'https://www.bilgeguvenlik.com/tr/kurumsal', ''),
    ('SB-074', '新闻/招标', 'LinkedIn 1 个月前帖：「Güneydoğu Avrupa yılın en iyi partneri Bilge Teknoloji. #milestone #MDXistanbul #BestChannelPartneroftheYear」——获某厂商东南欧年度最佳渠道伙伴', 'https://www.linkedin.com/company/bilge-g%C3%BCvenlik-sistemleri-teknoloji-a-%C5%9F/', '厂商未在摘要中标出（标签 MDXistanbul）；说明其在某主流品牌渠道体系内'),
    ('SB-185', '领英公司页', 'LinkedIn：Zeytek Bilişim ve Teknoloji Ürünleri San. Tic. Ltd. Şti. · BT Hizmetleri ve BT Danışmanlığı · 2–10 çalışan · İstanbul Sancaktepe', 'https://tr.linkedin.com/company/zeytek-bi%CC%87li%CC%87%C5%9Fi%CC%87m-ve-teknoloji%CC%87-%C3%BCr%C3%BCnleri%CC%87-san-ti%CC%87c-ltd-%C5%9Fti%CC%87', ''),
    ('SB-185', 'KP', 'ZoomInfo：Mehmet Zeytinli — Genel Koordinatör（+90 216 755 72 33）；此前 Gunko Endüstriyel Sistemler Türkiye Satış Müdürü，亦曾任职 Asimetrik Metal / Asrack Kabinet、Dat Telekom、Legrand Group；RocketReach：Kamuran İpek（Sales Assistant）、Sinem Doğan（Bookkeeping），共 5 人', 'https://www.zoominfo.com/p/Mehmet-Zeytinli/-1518915670', '老板出身工业系统/机柜/Legrand 渠道，懂机柜与布线 → 工业交换机 + 机架 PoE 都能谈'),
    ('SB-167', '登记', 'D&B：ONSIS ELEKTRIK ELEKTRONIK GUVENLIK SISTEMLERI INSAAT SANAYI VE TICARET LIMITED SIRKETI · Ankara · Building Equipment Contractors · Key Principal Esef Taskiran', 'https://www.dnb.com/business-directory/company-profiles/onsis-elektrik-elektronik-guvenlik-sistemleri-insaat-sanayi-ve-ticaret-limited-sirketi.0fc7751a528ed7eb618cb09f47a7e656', ''),
    ('SB-167', 'KP', 'RocketReach：Esef Taşkıran — Genel Müdür；Filiz Gündoğan — Muhasebe；Esra Çal — Accountant；公司约 6 人（Datanyze 页写 359 人 / $28.2M 明显失真，不采）', 'https://rocketreach.co/onsis-elektrik-elektronik-guvenlik-sitemleri-management_b73b6c95c7ea033f', '安卡拉小型安防/弱电承包商'),
    ('SB-274', '登记', 'Google Play 开发者信息：FIBERIX ILETISIM HIZMETLERI LIMITED SIRKETI · Gazi Mahallesi Zübeyde Hanım Bulvarı No:74-A, Şehitkamil 27001 Gaziantep · +90 850 333 27 00 · destek@fiberix.com.tr；自有客户 App（合同/账单/故障）', 'https://play.google.com/store/apps/details?id=co.fiberix_oim_app.android&hl=en_US', ''),
    ('SB-274', '论坛/社区', 'Şikayetvar：Fiberix internet müşteri hizmetleri 31 şikayet——Şahinbey / Şehitkamil 用户投诉频繁断网、100 Mbps 12 月合约 410 TL/月、2025-05 安装费争议', 'https://www.sikayetvar.com/fiberix/internet/musteri-hizmetleri', '居民 FTTH 运营商，网络稳定性被投诉 → 汇聚/接入交换机升级是切口'),
    ('SB-274', '人事变动', 'elemanonline：Fiberix İletişim Hizmetleri Ltd. Şti.（Gaziantep，İnternet Servis Sağlayıcısı）在招聘平台有雇主档案', 'https://www.elemanonline.com.tr/firma/fiberix-iletisim-hizmetleri-ltd-sti/519b526100000a4600000a46', ''),
    ('SB-389', '登记', '官网：HİPERONLİNE İLETİŞİM HİZMETLERİ SANAYİ TİCARET LİMİTED ŞİRKETİ，BTK 授权 ISP；地址 Binbaşı Reşatbey Mah. 351 Sok. Şükrü Ölçer İş Merkezi No:2 Gaziemir / İzmir；客服 0850 840 98 83', 'https://hiperonline.com.tr/eskisehir-metro-ethernet-internet', '总部在伊兹密尔 Gaziemir，Eskişehir 是自建光纤 + Airfiber 无线的重点城市'),
    ('SB-389', '供应商/品牌关系', '官网：Eskişehir 自建 fiber + kablosuz（Airfiber 100 Mbps）；81 il 通过批发线路提供 fiber / VDSL；企业 Metro Ethernet 最高 10.000 Mbps；GigaHiper 1000 Mbps 套餐', 'https://hiperonline.com.tr/eskisehir-internet', 'ISP 自建网 → 接入/汇聚交换机、SFP 需求真实'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
