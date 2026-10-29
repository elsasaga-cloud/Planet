#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""External XC · 闸 1 人工批 X1-01（2026-10-29，T29-U119 评估权下放）—— 规则辅助（`sieve_x.py --gate1 apply`，724 户）之后交人工的 46 户。

口径同 Saga 闸 1（方案 §3–§5）：候选 = 渠道型买家 + 有邮箱 / 具名 KP + 对位 + （主区 或 体量大）；仅电话 / 仅 info@ 且非主区 / 网店 / 巨头 → 留 C。
候选 → 闸 2 查底数（x2_001.py）。

用法：python3 sieve_batches_x/x1_001.py   （幂等）
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve_x  # noqa: E402

BATCH = 'X1-01'
DATE = '2026-10-29'
# code: (verdict, reason, tags)
V = {
    # ---- Edgecore 来源库「终局已删」仅电话（无邮箱）：路径弱 → 留 C 待巡检；巨头另标 ----
    'XC-E087': ('keep_C', 'TESSCO（美国，无线 / 通信分销巨头，2023 年被 Alliance 收购）：来源库终局已删、仅电话 → 巨头守界 + 路径弱，留 C', ['giant']),
    'XC-E066': ('keep_C', 'M2M Enterprise（英国 SI / VAR）：来源库终局已删、仅电话无邮箱 → 路径未建，留 C 待巡检', []),
    'XC-E067': ('keep_C', 'Telent Technology Services（英国，大型基建 / 公共部门 SI，数千人）：巨头守界「大的搞不定」+ 仅电话 → 留 C', ['giant']),
    'XC-E068': ('keep_C', 'Vesper Technologies（英国 SI / VAR）：来源库终局已删、仅电话 → 路径未建，留 C 待巡检', []),
    'XC-E060': ('keep_C', 'DELTA Computer Products GmbH（德国 SI / VAR）：来源库终局已删、仅电话 → 路径未建，留 C 待巡检', []),
    'XC-E059': ('keep_C', 'Alyseo（法国 SI / VAR）：仅电话无邮箱 → 路径未建，留 C 待巡检', []),
    'XC-E063': ('keep_C', 'Xentech B.V.（荷兰 SI / VAR）：仅电话无邮箱 → 路径未建，留 C 待巡检', []),
    'XC-E064': ('keep_C', 'TELCARIA（葡萄牙 SI / VAR）：仅电话无邮箱 → 路径未建，留 C 待巡检', []),
    'XC-E039': ('keep_C', 'Mekong Link（柬埔寨分销商）：非主区 + 仅电话 → 留 C', []),
    'XC-E040': ('keep_C', 'PT Converion Solution Informatica（印尼分销商）：非主区 + 仅电话 → 留 C', []),
    'XC-E041': ('keep_C', 'PT. Sysware Indonesia（印尼分销商）：非主区 + 仅电话 → 留 C', []),
    'XC-E043': ('keep_C', 'MACNICA, Inc.（日本，半导体 / 网络大分销，上市集团）：巨头守界 + 仅电话 → 留 C', ['giant']),
    'XC-E045': ('keep_C', 'SWS Group（泰国分销商）：非主区 + 仅电话 → 留 C', []),
    'XC-E047': ('keep_C', 'Algorithmic Digital Solutions（菲律宾 SI）：非主区 + 仅电话 → 留 C', []),
    'XC-E048': ('keep_C', 'AsiaPac Distribution（新加坡 SI / VAR）：非主区 + 仅电话 → 留 C', []),
    'XC-E049': ('keep_C', 'ComWorth Solutions（新加坡 SI / VAR）：非主区 + 仅电话 → 留 C', []),
    'XC-E050': ('keep_C', 'TRENTO SYSTEMS（韩国 SI / VAR）：非主区 + 仅电话 + KC 认证门槛 → 留 C', []),
    'XC-E054': ('keep_C', 'KRUPAM SOLUTIONS LLP（印度 SI / VAR）：非主区 + 仅电话 → 留 C', []),
    'XC-E055': ('keep_C', 'Ravi and Singh Communication（印度 SI / VAR）：非主区 + 仅电话 → 留 C', []),
    'XC-E090': ('keep_C', 'META LLC（亚美尼亚分销商）：非主区 + 仅电话 → 留 C', []),
    # ---- mikrotik-info 来源 C 的工业 / 网络分销商（有邮箱）：欧洲对位 → 具名 KP + 主区 / 波兰 / 德奥 者候选；仅 info@ 或微型市场者留 C ----
    'XC-M079': ('keep_C', 'EB Horsman & Son（加拿大电气批发，HMS / N-Tron 渠道）：主区 ✔ 对位（工业）✔ 但仅 info@、电气批发为主 → 冷户不足 4 条，留 C 待巡检', []),
    'XC-M090': ('candidate', 'PRIMATION Systemtechnik GmbH & Co. KG（德国，HMS / Red Lion / N-Tron 工业网络分销；具名 matthias.henning@）：主区 ✔ 对位 ✔ 具名 KP ✔ 分销主体 ✔ → 候选，闸 2 查 HRB', []),
    'XC-M092': ('candidate', 'Videor（德国 Rödermark，安防视频大分销，ComNet 授权；具名 m.schwamborn@ / m.niehus@）：主区 ✔ 对位（安防 PoE / 工业）✔ 具名 KP ✔ 体量 ✔ → 候选，闸 2 查 HRB', []),
    'XC-M118': ('candidate', 'Eptimo（波兰，MikroTik 官方分销 / VAD；具名 maciej.wiszniewski@）：波兰 ✔ 对位（ISP / 无线渠道 = SmartByte 管理型 + STI）✔ 具名 KP ✔ 分销主体 ✔ → 候选，闸 2 查 KRS', []),
    'XC-M119': ('candidate', 'Maritex Leszek Łosin Sp.j.（波兰 Gdynia，ORing 授权工业网络分销；具名 g.kondratowicz@）：波兰 ✔ 对位（工业 FS）✔ 具名 KP ✔ 分销主体 ✔ → 候选，闸 2 查 KRS / NIP', []),
    'XC-M120': ('candidate', 'Tekniska Polska（波兰，Westermo Gold 伙伴；具名 piotr.grychtol@）：波兰 ✔ 对位（工业）✔ 具名 KP ✔ 分销主体 ✔ → 候选，闸 2 查 KRS', []),
    'XC-M066': ('keep_C', 'Bross Engineering ApS（丹麦，HMS 渠道）：欧洲 ✔ 对位 ✔ 但仅 info@、北欧微型 → 留 C 待巡检', []),
    'XC-M074': ('candidate', 'Pondi d.o.o.（克罗地亚，MikroTik 官方分销 mikrotik-hrvatska.com；prodaja@）：欧洲 ✔ 对位（ISP 渠道）✔ 分销主体 ✔ 官方分销身份 ✔ → 候选（库内重复合并判断），闸 2 查 OIB', []),
    'XC-M082': ('candidate', 'ATYS Co Controll Engineering（匈牙利，Westermo Reseller；sales@ + kissa@；S 箱已群发）：欧洲 ✔ 对位 ✔ 已触达 ✔ 分销主体 ✔ → 候选，闸 2 查登记', []),
    'XC-M085': ('keep_C', 'NovaTel（塞尔维亚，Westermo Reseller；office@）：非 EU、仅公共邮箱 → 留 C 待巡检', []),
    'XC-M086': ('candidate', 'AIONA Automation GmbH（奥地利，HMS / Red Lion / N-Tron 分销；具名 gz@ + office@）：欧洲 ✔ 对位 ✔ 具名 KP ✔ 分销主体 ✔ → 候选，闸 2 查 FN', []),
    'XC-M111': ('keep_C', 'Audin（法国 Reims，HMS 渠道电气 / 自动化分销；reims@ 分部邮箱）：欧洲 ✔ 对位 ✔ 但分部公共邮箱、电气为主 → 留 C 待巡检', []),
    'XC-M114': ('keep_C', 'Inmac Wstore（法国，B2B IT 电商大分销 Bechtle 系）：巨头 / 电商守界 → 留 C', ['giant']),
    'XC-M349': ('candidate', 'EURO DK SIA（拉脱维亚，MikroTik 官方分销 / 波罗的海 ISP 渠道；eurodk@）：欧洲 ✔ 对位（ISP 渠道）✔ 官方分销身份 ✔ 分销主体 ✔ → 候选，闸 2 查 Reģ. Nr.', []),
    'XC-M069': ('keep_C', 'El-Gev Electronics（以色列，Westermo Reseller；sales@）：非主区 + 公共邮箱 → 留 C', []),
    'XC-M070': ('keep_C', 'Galoz Electronics（以色列，HMS 渠道；具名 alex@）：非主区，对位 ✔ 具名 ✔ 但以色列物流 / 认证门槛 → 留 C 待巡检', []),
    'XC-M071': ('keep_C', 'IPNet Solutions（以色列，ORing 授权；info@）：非主区 + 公共邮箱 → 留 C', []),
    'XC-M075': ('keep_C', 'Microstar（克罗地亚 / 斯洛文尼亚，Westermo Bronze；info@）：欧洲 ✔ 对位 ✔ 但仅 info@、微型 → 留 C 待巡检', []),
    'XC-M076': ('keep_C', 'Fálkinn Ísmar ehf.（冰岛，HMS 渠道；具名 kjartan@ / gisli@）：市场极小 → 留 C', []),
    'XC-M077': ('keep_C', 'Mælibúnaður（冰岛，Westermo Reseller；sala@）：市场极小 → 留 C', []),
    # ---- CCTV-PoE 库「终端触点」但实为分销 / 贸易商（有邮箱） ----
    'XC-C0155': ('candidate', 'Sapphire Trading and Marketing Ltd（肯尼亚 1996，Hikvision 国家分销商 / 电子进口商；info@sapphire.co.ke + 电话）：非主区但国家级分销体量 ✔ 对位 ✔ 进口经验 ✔ 邮箱 ✔ → 候选，闸 2 查登记', []),
    'XC-C0157': ('candidate', 'LEHOANG Trading Technology（越南 HCMC 2002，Hikvision 国家分销 / CCTV 进口商；info@lehoangcctv.com + 电话）：越南 CCTV 分销先例（Saga P 池已有 VN 多户）✔ 对位 ✔ 体量 ✔ 邮箱 ✔ → 候选，闸 2 查 MST', []),
    'XC-C0490': ('candidate', 'Smartplus Co. LLC（沙特 Riyadh，Hikvision 战略级全国分销；hello@smartplus.com.sa）：非主区但战略级分销体量 ✔ 对位 ✔ 邮箱 ✔ → 候选，闸 2 查 CR', []),
    'XC-C1023': ('candidate', 'IT Warehouse（菲律宾 Quezon City，ISP 设备分销商；business@itwarehouse.ph；SmartByte 子库条目）：ISP 渠道对位 SmartByte 管理型 ✔ 分销主体 ✔ 邮箱 ✔ 子库来源 ✔ → 候选，闸 2 查 SEC', []),
    'XC-C1531': ('keep_C', 'Server Basket / Alaitisal Computers（阿联酋，网络交换机在线零售）：网店 / 零售 → 留 C 待巡检', []),
    'XC-C1602': ('keep_C', 'Morgan Arabia Trading（沙特 Riyadh + Khobar，IT 设备贸易商；info@ + 2 电话）：贸易商、无具名 KP、非主区 → 留 C 待巡检', []),
}


def main():
    sieve = sieve_x.load_sieve()
    recs = {r['code']: (r, repo) for r, repo in sieve_x.load_xc()}
    n = 0
    for code, (verdict, reason, tags) in V.items():
        assert code in recs, code
        cur = sieve.get(code)
        assert cur is None or cur.get('batch') == BATCH, (code, cur)
        row = {'verdict': verdict, 'gate': 1, 'rule': 'G1', 'reason': reason, 'date': DATE, 'manual': True,
               'repo': recs[code][1], 'origin': 'External', 'batch': BATCH}
        if tags:
            row['tags'] = tags
        sieve[code] = row
        n += 1
    cnt = sieve_x.save_sieve(sieve)
    import collections
    print(BATCH, n, dict(collections.Counter(v[0] for v in V.values())), dict(cnt))


if __name__ == '__main__':
    main()
