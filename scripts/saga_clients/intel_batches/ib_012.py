#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-12（T29-U142 2026-10-30）· HFCL（Simon 口述 KP，见 p81）+ 欧洲 6 户 + 俄区/高加索 PI 2 户。来源 web_search 结果页，引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-12'
ITEMS = [
    ('SA-070', '登记', '未得：网查「Top Italia / topsicurezza.com」命中多家同名 Top Security S.r.l.（Grugliasco 12 人 / Muggia 15 人 / Ospitaletto 清算中），均无法与 topsicurezza.com 对应', '', '1 查未得即停；下轮用官网 Partita IVA 再核'),
    ('SB-767', '领英公司页', 'Tracxn：iTM Systems · Peterborough · founded 2010 · 11–50 employees（2024-07）；ZoomInfo 描述：digital video surveillance solutions … IP cameras, access control, facial recognition, LPR；「also serves as an original equipment manufacturer and integrates systems in-house … network of installers」（ZoomInfo 的「201–500 / $63.5M」与另一条「51–200 / $19.8M」互相矛盾，不采）', 'https://tracxn.com/d/companies/itm-systems/__sQLG_1qEEY0x0aGUE_iGcikoWS5BdtXbehAI93w1oOU', '英国 OEM + 集成 + 安装商网络的监控方案商；规模按 11–50 采信'),
    ('SB-134', '登记', 'papagal.bg：КАССАБА СИСТЕМС ЕООД · ЕИК 131403477 · 2005 年注册 · ДДС BG131403477（2006-09-15）· 资本 2 556 € · 地址 София, ж.к. Разсадника, ул. Троян 4, ет. 5, ап. 8（住宅地址）· 经营：计算机网络设计与建设、软件、自动化、电气安装、网站、培训；econ.bg：+359 88 720 26 10', 'https://papagal.bg/eik/131403477/a657', '独资微型 IT 服务公司（住宅地址）→ A-DEEP-05 下放 B'),
    ('SA-082', '登记', 'goyellow / Kompass / wlw：ISIMKO GmbH · Guhrower Straße 5, 03044 Cottbus · Amtsgericht Cottbus HRB 472 · USt-IdNr. DE138775376 · Gründungsjahr 1990 · Geschäftsführer Wolfgang Noack, Ralph Hannemann, Diego Noack · Mitarbeiter 50–99（wlw）/ 100–249（Kompass）· Kapital 250.001 EUR · Zertifikate BHE, DIN 14675, ISO 9001 · 业务：Informationstechnik, Sicherheitstechnik, Medientechnik, Kommunikationstechnik（Fertigung, Lieferung und Montage）', 'https://www.goyellow.de/home/elektriker-isimko-gmbh-cottbus--grpbv9.html', '勃兰登堡 50–249 人的 IT/安防/通信系统集成商，三位 GF 可直接写信（Noack 家族 + Hannemann）'),
    ('SB-256', '登记', 'aleo / GoWork：TVPRZEMYSLOWA.PL KAROL NOWAK · ul. Kórnicka 30, 61-141 Poznań · NIP 7822376077 · REGON 300661519 · Indywidualna działalność gospodarcza（2007-09-24 起）· 「wyłączny dystrybutor marki Eneo w Polsce」；伙伴 Milestone, Axis, Axxon, Flir, Mobotix, Sony, BCS, Dahua, Hikvision, Evos, Neovo, Camsat, Videotec, Mobeye；另有 S.C. Karol Nowak Lidia Nowak（NIP 7822563253）', 'https://aleo.com/pl/firma/tvprzemyslowapl-poznan', '个体工商户形式的 CCTV 分销（Eneo 波兰独家）→ A-DEEP-05 下放 B（Eneo 独家这一点留给 B1 跟进）'),
    ('SB-003', '登记', 'rio-krsk.ru Реквизиты：ООО «РИО-ИМПОРТ» · ИНН 2460214069 · КПП 246001001 · ОГРН 1092468006047 · 660075 г. Красноярск, ул. Красной Гвардии, д. 21 · +7 (391) 291-14-24 · rio-import2003@mail.ru · 开户行 Филиал «Центральный» Банка ВТБ；「Группа компаний РИО — одна из крупнейших поставщиков в Красноярском регионе полного спектра оборудования для АСУТП, шкафного оборудования, электронных компонентов」', 'https://www.rio-krsk.ru/company/requisites/', 'PI 成单户：克拉斯诺亚尔斯克工业自动化（АСУТП）设备集团公司成员，法定信息齐'),
    ('SB-375', '领英公司页', 'dc.ge / RocketReach：Delta Consulting LLC（დელტა კონსალტინგი）· Tbilisi ·「one of the leading IT system integrator company in Georgia, cooperating with … IBM, Lenovo, Cisco, Dell, Stulz, Juniper Networks, Ruckus」· 面向企业与政府 · CEO George Jaliashvili · RocketReach 仅 4 人可见', 'https://www.dc.ge/about-us-eng', 'PI 成单户（gg）：第比利斯政企 IT 集成商，Cisco/Juniper 渠道；规模按公开信息偏小，CEO 直联'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, bool(url))
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
