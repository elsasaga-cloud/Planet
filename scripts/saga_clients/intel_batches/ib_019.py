#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-19（T29-U143 2026-10-30）· 俄语区 7 户 + 非洲 2 户 + 拉美 1 户 + 北美 1 户。来源 web_search 结果页（俄方 ЕГРЮЛ 聚合站），引文原样。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-19'
ITEMS = [
    ('SA-035', '年报/财务', 'saby / СПАРК：ООО «ТД «Фарадей Электроникс» · ИНН 7820046904 · ОГРН 1167847053934（2016-01-14）· Санкт-Петербург（Пушкинский）· Генеральный директор Твердохлеб Татьяна Владимировна（с 10.11.2023）· Выручка 98 млн руб. · 6 сотрудников · Уставный капитал 10 000 руб. · ОКВЭД 46.69 торговля оптовая прочими машинами и оборудованием', 'https://saby.ru/profile/7820046904-782001001', '电源贸易公司（自牌），6 人、年销 ≈$1.1M；2023-11 换总经理 → A-DEEP-10 下放 B（俄区 B1）'),
    ('SA-064', '年报/财务', 'saby / РБК：ООО «ОПТА» · ИНН 7708768402 · ОГРН 1127746631814（2012-08-15）· Москва, 1-й Красносельский пер., д. 3 · Генеральный директор / учредитель Елизаров Николай Николаевич（с 28.05.2014）· Выручка 21.8 млн руб.（2021：16.1 млн）· Среднесписочная численность 1 сотрудник · Торги：участник 444 / заказчик 11 · ОКВЭД 46.90', 'https://saby.ru/profile/7708768402-770801001', '一人招投标贸易公司（年销 ≈$250K、投标 444 次）：回信最勤（18/20）但体量极小 → A-DEEP-10 下放 B（B1 重点，Simon 标「比较重要」保留在备注）'),
    ('SB-1122', '年报/财务', 'checko / saby：ООО «КОМТИНЮ» · ИНН 7725777573 · ОГРН 1127747244514（2012-12-13）· Москва · Генеральный директор Авидон Елена Александровна · Выручка 29,4 млн руб.（−85%）· Чистая прибыль −1,1 млн · Капитал 27,5 млн（−41%）· ССЧ 2025：3 человека · участие в торгах 49', 'https://checko.ru/company/komtinyu-1127747244514', '3 人、收入暴跌 85% 的贸易公司却谈 25G/100G DC 项目 → 体量不支撑，A-DEEP-10 下放 B'),
    ('SB-487', '年报/财务', 'rusprofile / checko / Бухонлайн：ЗАО «НПО «Телеком» · ИНН 1833018276 · ОГРН 1021801507694 · 426039 Ижевск, Воткинское ш., 31 · регистрация 1997-10-22 · Директор Афонин Михаил Владимирович（我方 KP）· Выручка 2025 670,1 млн руб. · Чистая прибыль 280,2 млн · ССЧ 62 · 358 госконтрактов на 892,9 млн руб. · Основной вид деятельности：「Производство оборудования средств связи, в том числе программное обеспечение, обеспечивающее выполнение установленных действий при проведении оперативно-розыскных мероприятий」', 'https://checko.ru/company/npo-telekom-1021801507694', '62 人、年销 ≈$7.5M、高利润，但主业 = 俄执法部门合法监听（СОРМ/ОРМ）通信设备 → 守界 + 制裁风险，A-DEEP-10 下放 B'),
    ('SA-067', '登记', 'orginfo.uz / yellowpages.uz / afisha.uz：\"LATMEDIA GROUP\" MChJ · ИНН 304474713 · 2016-12-14 · Toshkent, Mirzo Ulug‘bek tumani, Muminova ko‘chasi 1/3-8 · Руководитель / 100% учредитель Pak Maksim Anatolevich · 业务：Digital 广告代理（SEO / SMM / 网站推广）', 'https://orginfo.uz/organization/79a3a199eafc/', '实为数字营销代理（GitHub 招聘测试仓亦印证），非网络设备渠道 → A-DEEP-10 下放 B（品类不对位）'),
    ('SB-1135', '登记', 'СПАРК / rusprofile：圣彼得堡有两家「ООО ДИЛЕР」——ИНН 7842169106（保险代理，清算人 Косолапова Е.А.）与 ИНН 7840448665（2011 年，非专业批发，6 起仲裁 / 3 起执行）；均无法与 raisecom.su 对应', 'https://spark-interfax.ru/sankt-peterburg-tsentralny/ooo-diler-inn-7840448665-ogrn-1117847101844-bbe7c6edc505415f876646fac17d3275', '主体不可核 + Simon 此前已判「不行」→ A-DEEP-10 下放 B'),
    ('SB-163', '年报/财务', 'companium / sbis / rusprofile：ООО «СКЕО» · ИНН 7810990736 · ОГРН 1147847171185（2014-05-14）· Санкт-Петербург · Генеральный директор Деркач Алексей Александрович（учредители Афакова Э.К., Деркач А.А., Гатина Я.Г.）· Выручка 2025 100,7 млн руб.（+34%）· Чистая прибыль 3,8 млн（+48%）· участие в торгах 22 · ОКВЭД 46.90', 'https://www.companium.ru/id/1147847171185-skeo', '圣彼得堡批发商，年销 ≈$1.1M 且 +34% 增长 → 俄区小而活'),
    ('SA-079', '登记', 'ng-check：BIZ-ETHICS LIMITED · RC 401375 · registered 2001-01-23, Ikeja · 30/31 Otigba Street, Computer Village, Ikeja, Lagos · Directors Okafor Chidi Ogonna, Mbata Valentine, Mbata Livinus, Odiachi Evelyn, Mbata Evelyn, Mbata Uchechukwu Samuel；ngcontacts：「Sales of Computers, Networking (Wired/Wireless) Equipments, Surveillance & Access Control Systems and Power-Conditioning Equipment」', 'https://ng-check.com/biz-ethics-limited/938121.html', 'PI 成单户（BEL Networks 自牌 BNSC-）：拉各斯电脑城（Computer Village）网络设备经销，Mbata 家族企业'),
    ('SB-122', '领英公司页', 'contactout / aihitdata / arounddeal：Tera Technologies and Engineering Limited · Plot 2283, Block H, Tarangire Street, Africana Drive, P.O. Box 31257, Dar es Salaam · Founded 2011 · 11–50（32 可见）· est. revenue $3.8M · 「Service Provider in Telecommunications, ICT, Power and Security Systems solutions」', 'https://contactout.com/company/Tera-Technologies-and-Engineering-Limited-82148', '达累斯萨拉姆 ICT/电信/安防集成商（≈32 人）'),
    ('SA-045', '登记', 'energyplusystems.cl：Energy Plus Systems · RUT 76762149-3 · 6 ½ Oriente #270, Viña del Mar · +56 9 9218 8218 · Ventas Ling Fuentes · ventas@energyplusystems.cl · 产品线：Cables mineros, Variadores de frecuencia, Partidores suaves, **Switch Industriales**, IoT, Telcom Networking, Transformadores · 「experiencia por más de 15 años」', 'https://energyplusystems.cl/', '智利矿业/工业技术供应商，目录里已有工业交换机品类；销售对口 Ling Fuentes'),
    ('SA-060', '领英公司页', 'RocketReach / ZoomInfo：FiberX（FiberX LLC）· Puerto Rico · Founded 2016 · 34 employees · Revenue $5.6M · CEO Iván Rivera（我方 KP）· Director Network Engineering Edwuar Morillo（我方 KP）· CTO Jean Melendez · Operations Manager Yeraldine Acevedo · Senior Sales Engineer Hector Boschetti · OSP Design Supervisor Jesus Teran', 'https://www.zoominfo.com/c/fiberx/556679757', '波多黎各 FTTH 运营商（34 人、$5.6M）；两位 KP 均核实在职'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
