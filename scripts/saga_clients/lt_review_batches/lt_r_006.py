#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LT-R09 · 邮箱域体检异常户复核（Saga 12 户）· T29-U131 2026-10-29（缺口盘点 `lt_gap_audit.py` 「邮箱域异常」项）。

DNS 复查（dnspython，2026-10-29 14:48Z）：mreit.co.kr / hightrade-international.com / arcanlibya.com 其实正常（早上那轮超时误报）→ 留 B 不动；
真失效 9 户：有备用路径（WA / gmail / yahoo / FB 公开 gmail）或有真回的留 B 并记路径；无路径 + 无往来 + 非对位的打回 C 储备（可逆）。
web_search 3 次（itkati / microsam / fybera），引文 + URL 在 V 里。Planet PB-029 Microsam 在 lt_review_x_p_003.py 处理。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lt_review_lib import run  # noqa: E402

BATCH = 'LT-R09'
V = {
    'SB-082': ('留B', '域名 voltechelektronik.com 已失效（NXDOMAIN 2026-10-29），但 ISAF 2025 现场接触 + WA 已加 = 路径在 WA；土耳其主区小型安防服务商、找工业 PoE 网管交换机 → 留 B（路径 = WhatsApp；邮箱不再发）',
               [('DNS 2026-10-29：voltechelektronik.com MX/A/NS = NXDOMAIN', '')]),
    'SB-110': ('留B', '域名 itkati.com 已失效（NXDOMAIN 2026-10-29），但有 3 次实质回复；黄页 / Facebook 仍列 www.itkati.com，FB 公开邮箱 itkaticorp@gmail.com、电话 +256 704 575328 → 留 B，路径换 FB 公开 gmail（公开页取得，非编造）',
               [('yellow.ug：iTKATI UG LTD … established in 2009 … plot 4646 muwaire rd, Kampala … +256785284579 +256704575328 … www.itkati.com', 'https://www.yellow.ug/company/40803/itkati-ug-ltd'),
                ('Facebook：ITKati Corp. … Makindye, Kampala … +256 704 575328 itkaticorp@gmail.com itkati.com', 'https://www.facebook.com/itkati/')]),
    'SB-1103': ('留B', '域名 ara.com.bd 失效（NXDOMAIN 2026-10-29；support@ 早已退信），备用 gmail smchan91@gmail.com 在表 + 1 次真回 + 海关显示买过磊通 → 留 B（路径 = 备用 gmail；非主区预付 100%）',
                [('DNS 2026-10-29：ara.com.bd NXDOMAIN', '')]),
    'SB-194': ('留B', '域名 sabaindia.com 失效（NXDOMAIN 2026-10-29），备用 sriannaiassociates@yahoo.com 在表 + 2024-04 对 L2 管理 2 光 8 PoE 报过 $75、1 次真回 → 留 B（路径 = yahoo；印度常规预付 100%）',
               [('DNS 2026-10-29：sabaindia.com NXDOMAIN', '')]),
    'SB-944': ('留B', '域名 fybera.com DNS 委派坏（NoNameservers 2026-10-29，疑临时）；搜索可见官网在营：自有品牌 Fybera 光纤无源 + 媒体转换器 + 熔接机，联系电话 +359 2 4214270 = 保加利亚索非亚（表内写比利时有误 → country_fix BG）→ 自牌进口商留 B（OEM 话题；MC 对位弱、交换机待问）',
               [('fybera.com：FYBERA - Your optical fibre equipment provider … Ethernet Media Converter 1100/2 Brand: Fybera … Email: sales@fybera.com · Call now: +359 2 4214270', 'https://fybera.com/')]),
    'SB-1081': ('打回C', '域名 sswmcctvshop.com 失效（NXDOMAIN 2026-10-29）+ 只有 gmail + 16 次跟进 0 实质回复 + 泰国网店微型 → 无主体无路径 → C 储备（来信即回 B）',
                [('DNS 2026-10-29：sswmcctvshop.com NXDOMAIN', '')]),
    'SB-671': ('打回C', '两域 my-tec.co / mytec-iq.com 均失效（NXDOMAIN 2026-10-29）+ 只剩 yahoo + WA 19 次 0 实质回复 + 伊拉克非主区 → 无路径 → C 储备（来信即回 B）',
               [('DNS 2026-10-29：my-tec.co / mytec-iq.com NXDOMAIN', '')]),
    'SB-720': ('打回C', '域名 unitech-shop.ru 失效（NXDOMAIN 2026-10-29）+ 官网早已 unreachable + 表内未跟进 + Q-33（在卖 HRUI 外壳）+ RU 收款待定 → 无路径 → C 储备（来信即回 B）',
               [('DNS 2026-10-29：unitech-shop.ru NXDOMAIN', '')]),
    'SB-892': ('打回C', '域名 telcofusion.com.mx 失效（NXDOMAIN 2026-10-29）+ 只有 gmail + 需求 reverse PoE 板（Saga 无）+ 墨西哥非主区 → 不对位 + 无主体路径 → C 储备（来信即回 B）',
               [('DNS 2026-10-29：telcofusion.com.mx NXDOMAIN', '')]),
    'SB-545': ('留B', 'DNS 复查正常（mreit.co.kr MX mail.mreit.co.kr / A 210.206.162.16，2026-10-29 14:48Z；早上那轮超时误报）→ 不动；韩国自有 MR- 系列 PoE 品牌商，KC 待核',
               [('DNS 2026-10-29 14:48Z：mreit.co.kr MX 10 mail.mreit.co.kr；A 210.206.162.16', '')]),
    'SB-1037': ('留B', 'DNS 复查正常（hightrade-international.com MX mail.pro / A 109.234.165.213 / NS o2switch，2026-10-29 14:48Z；早上那轮误报）→ 不动',
                [('DNS 2026-10-29 14:48Z：hightrade-international.com MX 0 hightradeinternational-com02c.mail.pro；A 109.234.165.213', '')]),
    'SB-310': ('留B', 'DNS 复查正常（arcanlibya.com MX mx1–4.secure.ly / A 102.213.180.5，2026-10-29 14:48Z；早上那轮误报）→ 不动；ISAF 2025 接触 + WA 在',
               [('DNS 2026-10-29 14:48Z：arcanlibya.com MX 10 mx1.secure.ly…；A 102.213.180.5', '')]),
}


if __name__ == '__main__':
    run(BATCH, V)
