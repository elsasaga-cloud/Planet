#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTEL-04（T29-U139 2026-10-30）· 年报「采购线索」首批：Actelis 10-K FY2025（SEC 原文，fetch 第 4/10/13 段）+ Netaş 2025 年报（PDF 前 30 页）。
Simon：年报里供应商政策 / 资本开支 / 网络设备投入——EVERYTHING。引文原样（英/土），注释给中文要点。幂等。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'intel'))
import intel_store as IS  # noqa: E402

D = '2026-10-30'
B = 'INTEL-04'
K10 = 'https://ir.actelis.com/sec-filings/all-sec-filings/content/0001213900-26-030942/ea0280379-10k_actelis.htm'
NAR = 'https://netas.com.tr/docs/tr/faaliyet_raporlari/2025/Netas%20Faaliyet%20Raporu%202025.pdf'
ITEMS = [
    # ---- Actelis 10-K FY2025 · 采购线索
    ('SB-831', '供应商/品牌关系', '10-K Item 1：「Recent increase and creation of new tariffs by the Trump Administration is not likely to affect the Company significantly, since the Company manufactures its products in Israel and Taiwan, and the procurement of raw material is done directly to these countries.」', K10, '采购线索①：制造在以色列 + 台湾，原料直采这两地——不在中国制造；换中国货源 = 动其「cyber-hardened / FIPS / DoW」叙事，阻力大。Casey Hurley 回「Maybe…」符合此结构'),
    ('SB-831', '年报/财务', '10-K Item 1：「Over the past years, we entered into several large multi-year contracts with ITS, military, airports, and more … the worldwide airport technology provider, a provider of energy services to a major European city …, the city of San Jose, California and Northern Ireland railways.」', K10, '采购线索②：多年期合同（ITS / 军方 / 机场 / 北爱铁路 / 圣何塞市）——其采购是项目制、长周期'),
    ('SB-831', '供应商/品牌关系', '10-K Item 1：「We also have many non-exclusive third-party distributors, resellers and system integrators and partners around the world, located in the U.S., Canada, Philippines, Germany, Italy, Spain, Scandinavian countries, Greece, Netherlands, Japan and India.」；竞品自述「Cisco, Rad, Nokia, Siemens, Belden and others」', K10, '渠道结构 + 自认竞品；Saga 不是其竞品也不是其供应商类型（铜缆/混合光纤接入）——只能做其项目里的配套 PoE/工业交换机'),
    ('SB-831', '人事变动', '10-K Item 1：「During 2025, we upgraded our capabilities in Federal and Military sales and marketing by hiring a Chief Revenue Officer, Americas and a Director of Federal sales, both veterans of those markets … new strategy through the US Department of War Programs of Record (PoR)」', K10, '2025 新聘 CRO Americas + Director of Federal Sales；方向 = 美国国防「Programs of Record」——守界：Saga 不碰军方线，只谈 ITS / MDU / 市政'),
    ('SB-831', '年报/财务', '10-K Item 1：市场与资金面：「In 2024, we launched our MDU program, which was further expanded in 2025 …」「BEAD Program provides $42.45 billion … approximately $28 billion were ear-marked」；证书：FIPS 140-2 → 2026-02 部署 140-3；JITC 互操作认证；产品 UL / EN / VCCI / CISPR / ICES 认证', K10, '采购线索③：增长押注 MDU（多住户楼宇）+ BEAD 补贴项目；认证门槛高（UL/FIPS）——Saga 产品无 UL，不对位其核心产品，只可能配套'),
    ('SB-831', '年报/财务', '10-K 融资事件（Recent Developments）：2025-07 私募 ~$1M（$6.15/股 + 认股权证）；2025-09-27 White Lion 股权购买协议 + PIPE ~$850K（$2.125/股）；2025-12-17 公开发行 ~$5M（$0.80/股）；2025-11-18 1:10 反向拆股', K10, '一年三轮融资 + 反向拆股 → 现金紧、付款能力要盯；小额样品单可做，账期不放'),
    # ---- Netaş 2025 年报（前 30 页）
    ('SA-086', 'KP', '2025 Faaliyet Raporu · Üst Yönetim Ekibi：Sinan Dumlu — CEO, İcra Kurulu Başkanı；Börgehan Köksal — Kurumsal İşler；Burhan Metin / Levent Mutlu — Kamu ve Savunma；Selda Parın — Kurumsal İş Birimi GM；Gülden Erşan — İK；Zeynep Boz — Mali İşler；Ersin Öztürk — Ar-Ge GM；Koray Otyam — BDH GM；Mei Bowen — Operasyon（YK üyesi）；Dr. Xi Guang Qing — Teknoloji', NAR, '高管名单（2025 年报）；运营与技术两席是 ZTE 派驻；我方 PI 对接人 Ender Bulut / Burak Ozdemir 在采购/项目层，不在此名单'),
    ('SA-086', '供应商/品牌关系', '年报 Şirket Profili：三大业务线——Bilgi Teknolojileri（sistem entegrasyonu：veri merkezleri, ağ ve iletişim altyapıları, sunucu ve depolama …「Geniş iş ortağı ve teknoloji üreticisi ekosistemiyle, çoklu üretici ortamlarında」）、İletişim Teknolojileri（Orhanlı tesislerinde yerli üretim：baz istasyonları, mikrodalga, rectifier, lityum iyon akü, DC güç, sunucu）、Mobil（nubia）；BDH 子公司做运维', NAR, '采购线索①：SI 业务线是多厂商生态，网络设备按项目外采 → Saga 的口子在「项目配套交换机」；制造线是 ZTE 技术 + 本土组装，不是我们的位置'),
    ('SA-086', '年报/财务', 'CEO 致辞：「Netaş olarak ana hissedarımız ZTE ile olan ortaklığımızın gücü …」；2017-07 起 ZTE Cooperatief U.A. 子公司；重点：Savunma ve Havacılık（AS9100 认证）、Yerli Üretim ve Ar-Ge（yerli bulut sunucu、DC güç、lityum batarya、mikrodalga）、Kazakistan 集成项目出口、2026 年 5G 普及预期', NAR, '采购线索②：「yerli üretim（本土制造）」是其叙事主线——对我们意味着：白牌/部件级供货更贴合，而非品牌成品；哈萨克斯坦项目 = 俄语区二级市场线索'),
    ('SA-086', '年报/财务', '年报 Sayılarla Netaş：2025 yıl sonu çalışan sayısı 1.264（yaş ortalaması 36，%29 kadın）；dağıtım ve servis ağı 81 il；cinsiyete dayalı ücret oranı %94,4（全文 PDF 已排进运行器文档队列，tedarik / satın alma / yatırım 关键词窗口下一轮入库）', NAR, '全文抽取由日跑 intel_docs 完成（data/saga_clients/intel_fetch_queue.json）'),
]


def main():
    n = 0
    for code, kind, quote, url, note in ITEMS:
        n += IS.add(code, kind, quote, url, D, note, B, True)
    print(B, 'items +', n)


if __name__ == '__main__':
    main()
