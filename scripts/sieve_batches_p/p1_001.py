#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Planet 仓 · 闸 1 人工批 P1-01（2026-10-29，T29-U120「继续弄planet仓的」；评估权下放 PR-02-64）—— 闸 0 / 并档之后独立待判的 47 户。

口径同 Saga / External 闸 1（方案 §3–§5）：候选 = 渠道型买家 + 邮箱 / 具名 KP + 对位（PLANET 在售 = 交换机进货事实）+ 主区 / 欧洲 + 体量不微不巨；
PLANET 自家实体 / 代表处、目录 feed 型综合电商、微型安装商 / 个体网店、巨头 → keep（留 Planet 仓原档，只巡检不入池）。
候选 → 闸 2 查底数（p2_001.py）。verdict 'keep' = 留在 Planet 仓原 A/B/C 档（不是 pass）。

用法：python3 scripts/sieve_batches_p/p1_001.py   （幂等）
"""
import collections
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve_p  # noqa: E402

BATCH = 'P1-01'
DATE = '2026-10-29'
V = {
    # ---- 候选（→ 闸 2） ----
    'PA-002': ('candidate', 'Cartronic Group（西班牙 Madrid，PLANET 西班牙官方分销 + Teltonika / Hanwha VAD；具名 Director jmcobo@）：欧洲 ✔ 对位 ✔ 具名 KP ✔ 官方分销体量 ✔ → 候选，闸 2 查 CIF', []),
    'PB-002': ('candidate', 'W3CAM SAS（法国 Lorient，安防分销 + PLANET 本地库存；SIREN 483019345 已在 batch facts；contact@）：主区 FR ✔ 对位 ✔ 登记 ✔ → 候选（体量 3–5 人待闸 2 定档）', []),
    'PB-003': ('candidate', 'Konsorcjum FEN（波兰 Poznań，PLANET 波兰官方分销 planet.fen.pl；KRS 0000196881；具名 AM bartosz.banaszak@）：波兰 ✔ 对位 ✔ 具名 ✔ 登记 ✔ 官方分销 ✔ → 候选', []),
    'PA-007': ('candidate', 'ALARM ABSOLON（捷克 Praha，1989 年起安防批发；具名 tikovsky@ / kacenova@）：欧洲 ✔ 对位 ✔ 具名 KP ✔ 分销主体 ✔ → 候选，闸 2 查 IČO', []),
    'PA-008': ('candidate', 'Aspectis Kft.（匈牙利 Budapest，IP 安防 VAD + PLANET 分销；总经理直邮 gabor.laczko@）：欧洲 ✔ 对位 ✔ 决策人直邮 ✔ 分销主体 ✔ → 候选，闸 2 查 cégjegyzék', []),
    'PA-010': ('candidate', 'iOC Tech Inc.（加拿大 Markham，工业以太网分销 + 定制线缆，自述 PLANET 加拿大授权分销；sales@，Director 具名）：主区 CA ✔ 对位 ✔ 分销主体 ✔ → 候选（2–10 人，闸 2 定档）', []),
    'PB-009': ('candidate', 'BTS NETWORK GmbH / lwl-shop24.de（德国 Erftstadt，光纤网络制造 + 批发，自有品牌，另运营 planet-technology.de；anfrage@，两位 GF 具名）：主区 DE ✔ 对位 ✔ 自牌 OEM 线索 ✔ 体量 ✔ → 候选，闸 2 查 HRB', ['oem_target']),
    'PB-011': ('candidate', 'ProVu Communications（英国 Huddersfield，VoIP 分销 1999 年起，刚引入 PLANET 交换机；contact@，Sales Manager 具名）：主区 GB ✔ 对位 ✔ 分销主体 ✔ 新品类窗口 ✔ → 候选，闸 2 查 Companies House', []),
    'PB-018': ('candidate', 'Power Biztonságtechnikai Kft.（匈牙利 Budapest，仅面向安装商 / 经销商的安防批发；info@ / sales@，MD 具名）：欧洲 ✔ 对位（48 口 PoE + 工业 PoE 在售）✔ 分销主体 ✔ → 候选，闸 2 查 cégjegyzék', []),
    'PB-020': ('candidate', 'Jlinks Technology（加拿大 Richmond BC + Montreal，低压线缆制造 + 安防 / 网络分销 2002 年起；sales@，Director 具名）：主区 CA ✔ 对位 ✔ 分销主体 ✔ 两地 ✔ → 候选，闸 2 查登记', []),
    'PA-012': ('candidate', 'SIR.tel. S.r.l.（意大利 Verona，1991 年起监控 / 门禁 / 电信分销，PLANET 授权分销价目季更；P.IVA 02565900236；采购经理具名）：欧洲 ✔ 对位 ✔ 登记 ✔ 体量 €6.67M ✔ 采购 KP ✔ → 候选', []),
    'PA-013': ('candidate', 'Leteng AS（挪威，AV / IT 增值分销 1984 年起，Org nr 952 002 872，21 人，Lagercrantz 集团成员；总经理直邮 oyvind@）：欧洲 ✔ 对位 ✔ 登记 ✔ 决策人直邮 ✔ → 候选', []),
    'PB-025': ('candidate', 'Microdata Finland Oy（芬兰 Vantaa，电信 / 网络批发，面向经销商；myynti@ + 具名 aki.jarvinen@）：欧洲 ✔ 对位 ✔ 具名 ✔ 分销主体 ✔ → 候选，闸 2 查 Y-tunnus（体量待定档）', []),
    'PB-033': ('candidate', 'Ergen Elektronik（土耳其 Antalya，Dahua / Zanuo 分销口径 + PLANET 品牌页；info@，Serhat Ergen 具名）：主区 TR ✔ 对位 ✔ 分销主体 ✔ → 候选，闸 2 查登记', []),
    'PB-040': ('candidate', 'Alarmsysteemexpert（荷兰 Gorinchem，20+ 年安防电商 / 安装 + 展厅，自有白牌 PoE 交换机系列；info@ + WhatsApp）：欧洲 ✔ 对位 ✔ 自牌 OEM 线索 ✔ 渠道 ✔ → 候选，闸 2 查 KvK', ['oem_target']),
    'PC-011': ('candidate', 'Akçaba Communications（北塞浦路斯 Lefkoşa，T06 裁决随土耳其；交钥匙通信集成 + PLANET 美元标价有库存；18 人 / $5.2M；info@）：随 TR ✔ 对位 ✔ 体量 ✔ 自装消耗 ✔ → 候选，闸 2 查登记（TRNC 公开登记少 → 部分坐实即可）', []),
    'PB-049': ('candidate', 'Intermédia – Informática, Lda（葡萄牙 Coimbra，PLANET 全系带价在售含 L3 PoE / 工业线；NIF 503329827；compras@ 采购信箱）：欧洲 ✔ 对位 ✔ 登记 ✔ 采购入口 ✔ → 候选（体量小，闸 2 定档）', []),
    'PB-052': ('candidate', 'STS Lab, Inc. / CCTV.Net（美国 Van Nuys CA，2001 年起独立安防分销 82 品牌、dealer-only，PLANET 为在售交换机主线 1,028 件；sales@ / info@）：主区 US ✔ 对位 ✔ 分销主体 ✔ 体量 ✔ → 候选，闸 2 补底数', []),
    'PB-058': ('candidate', 'JPF Industries SAS（法国 Quévert，Groupe Fauché 子公司：电气 + 网络安装 + 网店，88–100 人 €11.1M；SIREN 404954125；jpfid@）：主区 FR ✔ 对位 ✔ 登记 ✔ 项目消耗体量 ✔ → 候选', []),
    'PB-059': ('candidate', 'Europ Computer Performance SARL（法国 Stains，1995 年起 IT 进口 / 批发 5,000+ SKU / 5,000+ 经销商，自称 PLANET 批发分销；SIREN 402225098；sales@）：主区 FR ✔ 对位 ✔ 进口经验 ✔ 登记 ✔ → 候选', []),
    'PB-061': ('candidate', 'Elctron E-commerce Partners / CTR（波兰 Warszawa，CCTV 批发 2008 年起、64 个合作点、PLANET 35 款现货；KRS 0001031273；info@，Prezes 具名）：波兰 ✔ 对位 ✔ 登记 ✔ 现货 ✔ → 候选', []),
    'PA-016': ('candidate', 'VOIP24SKLEP.PL Sp. z o.o.（波兰 Bydgoszcz，VoIP / 网络电商，PLANET 为交换机主品牌；KRS 0000666618；董事直邮 k.maroszczyk@）：波兰 ✔ 对位 ✔ 登记 ✔ 决策人直邮 ✔ → 候选（体量小，闸 2 定档）', []),
    'PB-082': ('candidate', 'Snugfort Limited / ScreenMoove（英国 London，商用 AV / 数字标牌集成 + 网店，PLANET Official Partner、实时库存 168 件；Companies House 12278368；info@）：主区 GB ✔ 对位 ✔ 登记 ✔ 真实库存 ✔ → 候选', []),
    'PB-088': ('candidate', 'Mills Ltd（英国 Uxbridge，1918 年起布线 / 电信工具器材分销 ~60 人，PLANET 为唯一交换机线；Companies House 00282704；sales@）：主区 GB ✔ 对位 ✔ 登记 ✔ 体量 ✔ → 候选', []),
    # ---- keep（留 Planet 仓原档，只巡检不入池） ----
    'PB-006': ('keep', 'Network Camera Store（美国，drop-ship 无库存网店，2–10 人；sales@）：无自有库存 = 无进货决策 → 留原档巡检', ['micro']),
    'PB-007': ('keep', 'Paragon Networks Ltd（英国，小型网络产品网店，PLANET 工业专区；enquiries@，无具名）：体量小、无 KP → 冷户不足 4 条，留原档巡检', []),
    'PB-008': ('keep', 'PLANET Germany GmbH（德国，名称绑定 PLANET 的微型分销 GmbH，资本 €25k）：PLANET 体系内实体，第二货源意愿存疑 → 视同原厂 / 同行，留原档不入池', ['peer']),
    'PB-010': ('keep', 'Ballicom Ltd（英国，综合 IT 网店 26 人，GS-4210-24P4C 库存 30 台；sales@）：目录型 IT 电商、无具名 KP → 长期复利弱，留原档巡检', []),
    'PB-012': ('keep', 'Visual Control Systems（英国，4 人智能家居安装商）：微型安装商 → 留原档', ['micro']),
    'PB-014': ('keep', 'NetWalker EURL（法国，微型监控软件分销 + 网店；contact@）：微型、无具名 → 留原档', ['micro']),
    'PB-016': ('keep', 'LK enterprise / Kamerový Svět（捷克，2022 年成立安防网店 + 安装；obchod@）：新设微型 → 留原档巡检', ['micro']),
    'PB-019': ('keep', 'Sound People AS（挪威，5 人 AV 商店）：微型零售 → 留原档', ['micro']),
    'PB-021': ('keep', 'Nassau National Cable（美国，1950 年起线缆分销 Inc 5000；PLANET 仅 1 款）：线缆为主、交换机边线 → 对位弱，留原档巡检', []),
    'PC-006': ('keep', '100MEGA Distribution / ASM（捷克大型 IT 分销集团，planet-tech.cz no_mx；Mikrotik 仓两次建档均退信）：巨头守界 + 路径不稳 → 留原档不 pass', ['giant']),
    'PB-023': ('keep', 'Anatronic S.A.（西班牙 1982，PLANET 西 / 葡厂商代表；comercial@）：代表制与 PLANET 绑定、第二货源冲突 → 视同同行，留原档', ['peer']),
    'PB-026': ('keep', 'CMS plc（英国 15 人，Norbain SD 旗下）：集团采购可能上收 → 留原档巡检', []),
    'PB-027': ('keep', 'VERSIM S.A.（波兰上市 VAD，Extreme Networks 分销；PLANET 现状待核）：VAD 偏大 + PLANET 在售待核 → 留原档巡检', []),
    'PB-029': ('keep', 'Microsam（加拿大 CCTV 系统供应 <25 人；microsam.ca 域名 nxdomain，仅电话）：路径半死 → 留原档巡检，域名恢复再闸 2', []),
    'PB-056': ('keep', 'ViSe S.r.l.（意大利 1–5 人 IP 监控分销，P.IVA 01817610353）：坐实但微型 → 留原档巡检', ['micro']),
    'PB-060': ('keep', 'DATA GROUP SK（斯洛伐克 2 人翻新大牌经纪，2022 年设）：PLANET 为边线、经纪型 → 留原档', ['micro']),
    'PB-062': ('keep', 'Gateway Comunicaciones（西班牙 4 人安防物料网店，CIF B35679638）：微型 → 留原档巡检', ['micro']),
    'PB-075': ('keep', 'SOFTCOM GROUP（捷克 30,000 SKU 综合 IT 电商，PLANET 来自分销 feed）：目录 feed 型 → 留原档', []),
    'PB-080': ('keep', 'Telecom Creations（美国 50,000 SKU 通信电商，PLANET 页 2018 年建、多停产款）：目录 feed 型 → 留原档', []),
    'PB-084': ('keep', 'VoIPDistri.com（德国个体企业 VoIP 网店，交换机 1 款在库）：个体 + 边线 → 留原档', ['micro']),
    'PB-085': ('keep', 'ESUS IT（波兰内存 / SSD 电商，交换机类目为 FEN feed）：feed 型 → 留原档（主档随 PB-003 FEN 渠道）', []),
    'PB-086': ('keep', 'Technical Reality（英国 100,000 SKU 通用 IT 供应商）：目录型 → 留原档巡检', []),
    'PB-091': ('keep', 'DIGIRAM.PL Adam Tytoń（波兰个体网店，PLANET 全线在售、店主直邮 adam@）：个体微型 → 留原档巡检；复购体量出现再闸 2', ['micro']),
}


def main():
    sieve = sieve_p.load_sieve()
    recs = {r['code']: r for r in sieve_p.load_planet()}
    for code, (verdict, reason, tags) in V.items():
        assert code in recs, code
        cur = sieve.get(code)
        assert cur is None or cur.get('batch') in (BATCH, 'P2-01'), (code, cur)
        if cur and cur.get('batch') == 'P2-01':
            continue  # 闸 2 已覆盖
        row = {'verdict': verdict, 'gate': 1, 'rule': 'G1', 'reason': reason, 'date': DATE, 'manual': True,
               'origin': 'Planet', 'grade': recs[code]['grade'], 'batch': BATCH}
        if tags:
            row['tags'] = tags
        sieve[code] = row
    cnt = sieve_p.save_sieve(sieve)
    print(BATCH, len(V), dict(collections.Counter(v[0] for v in V.values())), dict(cnt))


if __name__ == '__main__':
    main()
