#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 131 批（2026-10-29）—— 闸 1 第 26–32 批（桶 ⑥「企业邮箱 · 其他区」第 771–1155 户）候选 **31 户**查底数
= RU 6 / IN 8（含表内「尼泊尔」实为印度 1）/ TW 3 / BR 3 / VN 2 / DE / CH / LV / HK / GE / BD / EC / TZ / ZA 各 1，底数见 registry_batches/b131_c.py。本批跑完 → 闸 1 第 01–32 批候选全部过闸 2（candidate 归零）。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-131）：
  · pool_candidate = 法人 / 官网坐实或部分坐实 + §5 条数够 → 「P 池候选」，等 Simon 定夺；微型 / 非点名国 → △ 观察档 + 预付 100%。
  · keep_C = 未坐实（Jjenka / Anfatech / PIIR / Akatel）/ 网店型（VoIP Telecom）/ 同行 ODM 制造商（Konten）/ 微型商场安装商（Protech）→ 回 C 储备。无新 pass_final。
  · 国别存疑（待 Simon，未写 research）：SC-1871 Bay Datacom 表内「尼泊尔」↔ CIN 泰伦加纳（印度）；SC-1714 Omni Ray「智利」↔ 瑞士 CHE；SC-1713 OAK「玻利维亚」↔ 拉脱维亚 Reģ. Nr.。
tier：★ 品牌商 · 中型分销 / ○ 分销 · 集成 · 区域 ISP / △ 观察档（微型 / 非点名国 → 预付 100%）。

用法：python3 sieve_batches/g2_131.py   （幂等；写 sieve.json + docs/requirements/C池闸2_批131_2026-10-29.md）
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-131'
DATE = '2026-10-29'

V = {
    # ---- 欧洲 ----
    'SC-1675': ('pool_candidate', '★ 德国主区 · 工业通信分销 20%：tekmodul GmbH（München；HRB 158866；2005；GF Tassilo Halt；electronica 2024 参展；Atop 经销）坐实；主区 ✔ 台湾工业品牌经销 ✔ 对位 ✔ 决策人具名 ✔ → P 池候选', []),
    'SC-1714': ('pool_candidate', '★ 欧洲 · 工业自动化分销 20%：Omni Ray AG（Dübendorf；CHE-105.959.689；1950；CHF 2.05M；20–49 人；MD Roger Müller；Moxa 分销）坐实；欧洲 ✔ 台湾工业品牌分销 ✔ 对位 ✔ → P 池候选；表内「智利」→ 瑞士 country_fix 待 Simon', []),
    'SC-1713': ('pool_candidate', '○ 欧洲 · 工业自动化小分销 20%：OAK INTEGRATOR Products SIA（Rīga；Reģ. 40003540103；2001；原 Beijer Electronics SIA；Mitsubishi Electric 独家 + Westermo / Korenix；$1.33M / 3 人）坐实；欧洲 ✔ 台湾工业品牌集成 ✔ 对位 ✔ → P 池候选；表内「玻利维亚」→ 拉脱维亚 country_fix 待 Simon', []),
    # ---- 巴西 ----
    'SC-1689': ('pool_candidate', '★ 巴西 · 工业网络分销 / 集成 20%：Above-Net Comercio de Informatica, Telecomunicacao e Servicos Ltda（Rio de Janeiro；CNPJ 05.920.155/0001-60；2003；800+ 客户 / 1,500 项目）坐实；已进口中国工业线（三旺）✔ 对位 ✔ 巴西先例 ✔ → P 池候选', []),
    'SC-1691': ('pool_candidate', '★ 巴西 · 工业分销 20%：Alfacomp Automação Industrial Ltda（Porto Alegre + Campinas；CNPJ 04.430.358/0001-05；2001；R$400K）坐实；中国工业品牌全线（迈威）✔ 对位 ✔ WA ✔ → P 池候选', []),
    'SC-1583': ('pool_candidate', '△ 观察档 · 巴西进口代理 贸易 20% + 预付 100%：Cartago Comex Ltda（Maringá；CNPJ 36.699.505/0001-33；2020；报关行 + 商业代理；R$1,000；1–10 人）坐实但微型；MC 100 对数量询问 ✔ 有进口经验 ✔ 对位（STC-110XGE）✔ → 入池观察档；可否决', []),
    # ---- 越南 / 厄瓜多尔 / 坦桑尼亚 / 南非 / 孟加拉 ----
    'SC-1670': ('pool_candidate', '○ 越南 · CCTV 进口商 分销 20%：Công Ty TNHH Phát Triển Công Nghệ Metsuki VietNam（TP.HCM Q12；MST 0304967173；2007；51–100 人；电子电信进出口 + CCTV）坐实；进口商 ✔ 4-8-16-24 口需求 ✔ 对位 ✔ → P 池候选（21 推 0 回 → 换稿点名口数）', []),
    'SC-1900': ('pool_candidate', '○ 厄瓜多尔 · 进口集成 25%：Soluciones Tecnológicas Konect Cía. Ltda.（Quito；2019；17 人；Tendata 进口商 36 供应商）部分坐实（RUC 未取）；中国品牌进口 ✔ 对位 ✔ WA ✔ 先例 SC-2402 ✔ → P 池候选（洪瑞现供 → Q-33 口径待 Simon）', []),
    'SC-1803': ('pool_candidate', '○ 坦桑尼亚 · 区域 ISP 自用 直客 25%：Habari Node Limited（Arusha AICC；Cert. 75466；2010；接续 1994 起 ISP；数据中心）坐实；千兆 20 台数量询问 ✔ 具名 KP ✔ 对位 ✔ → P 池候选', []),
    'SC-2885': ('pool_candidate', '○ 南非 · 安防集成 25%：Plug & Play Solutions = 表内 LS Networks (Pty) Ltd（Centurion；2012；35 人；$5M；Sales Exec Kelvin Jordaan）部分坐实（Reg No 未取）；工业 PoE + MC 真需求 ✔ 对位 ✔ 南非先例 ✔ Simon「单独跟进」✔ → P 池候选', []),
    'SC-2891': ('pool_candidate', '△ 观察档 · 孟加拉贴牌 CCTV 店 OEM 30% + 预付 100%：Trimatrik Multimedia（Dhaka Uttara + Mouchak 分店；进口商 / 安装）部分坐实（注册号未取）；ONV 带标卖 = 贴自有牌 ✔ 对位 ✔ WA 手机 ✔；小型 + 非点名国 → 入池观察档；可否决', ['oem_target']),
    # ---- 印度 ----
    'SC-1795': ('pool_candidate', '★ 印度 · 工业网络分销 20%：Bluboxx Communication Pvt Ltd — BBCPL（Pune；$5.1M；工业网络 + 自动化分销）部分坐实（CIN 未取）；台湾品牌（Planet）经销 ✔ 对位 ✔ Simon 点名印度 ✔ → P 池候选', []),
    'SC-1797': ('pool_candidate', '○ 印度 · 全国分销 20%（交换机副线）：Cohesive Technologies (P) Ltd（Grandstream 印度授权全国分销；服务 IN / LK / NP / MV）部分坐实（CIN / 地址未取）；中国品牌（Wi-Tek / Grandstream）✔ 对位（IP 电话配套 PoE）✔ → P 池候选', []),
    'SC-1804': ('pool_candidate', '★ 印度 · 自有品牌（政府渠道）OEM 30%：Indra Heera Group / IHT（Arrah Bihar；Make-in-India 制造商 + RDI；NSDTS Trusted Source / GeM）部分坐实（CIN 未取）；自有品牌 ✔ 政府渠道 ✔ 对位 ✔ → P 池候选（洪瑞现供 → Q-33 口径待 Simon）', ['oem_target']),
    'SC-1807': ('pool_candidate', '★ 印度 · 贴牌工业交换机 OEM 30%：Mootek Technologies（Chennai；GST 33AQSPM9347C1ZJ；2013；Founder / CEO Moorthy D；以 Mootek 品牌列三旺型号体系 IES215 / IES2005）坐实；自有品牌贴牌 ✔ 已进口中国工业线 ✔ 决策人具名 ✔ → P 池候选', ['oem_target']),
    'SC-1734': ('pool_candidate', '○ 印度 · 电力 EPC 集成 25%：Joohitha Power Systems Pvt Ltd — GridX（Hyderabad；CIN U74999TG2011PTC077260；2011；₹10 lakh；SCADA / OLTE / PLCC EPC；11–50 人）坐实；工业 2 光 2 电具体需求 ✔ 工业对位 ✔ → P 池候选', []),
    'SC-1871': ('pool_candidate', '○ 印度 · 大集成 25%：Bay Datacom Solutions Pvt Ltd（Hyderabad + Bengaluru；CIN U32100TG1998PTC028943；1998；200–500 人；₹24 Cr）坐实；4 光 24 电 PoE 具体需求 ✔ 中型集成 ✔ → P 池候选；表内「尼泊尔」→ 印度 country_fix 待 Simon', []),
    'SC-2021': ('pool_candidate', '★ 印度 · VAD 分销 20%：Acceron Infosol Pvt Ltd（Thane / Mumbai；2007；30 人；IT 安全 / 网络 / 无线增值分销）部分坐实（CIN 未取）；主动索要资料 = 真意向 ✔ 分销主体 ✔ 对位 ✔ → P 池候选（回「已发资料」稿）', []),
    'SC-2078': ('pool_candidate', '★ 印度 · 全国品牌商 OEM 30%（长线）：Zebronics India Pvt Ltd（Chennai；CIN U30000TN1997PTC038037；1997；实收 ₹3.28 Cr；31 GST 登记；MCA 邮箱 sandeep.doshi@）坐实；自有品牌 ✔ 已贴牌中国 PoE ✔ 大型 ✔ 对位 ✔ → P 池候选（换 zebronics.com 地址；洪瑞现供 → Q-33 口径待 Simon）', ['oem_target']),
    # ---- 俄罗斯 ----
    'SC-2111': ('pool_candidate', '★ 俄罗斯 · 自有品牌 + 大分销 OEM 30%：ООО «Амиком» / ТД «Амиком»（Москва；1992；25 万 SKU；自有商标 Just / Advert / PRIME；大客户 РЖД / Сбербанк）部分坐实（ИНН 未取）；自有品牌 ✔ 已进口中国同类 ✔ 朱姐渠道 ✔ 对位 ✔ → P 池候选；收款路径待 Simon', ['oem_target']),
    'SC-2730': ('pool_candidate', '★ 俄罗斯 · 品牌商 OEM 30%（长线）：RVi Group（ГК «Рубеж» 成员；2007；视频监控制造商；产品线含交换机 / 网络设备）部分坐实（ИНН 未取）；自有品牌 ✔ 已贴牌中国 PoE ✔ 对位 ✔ → P 池候选；守界：集团是否涉制裁待核 + 收款路径待 Simon', ['oem_target']),
    'SC-1917': ('keep_C', '闸 2 回 C（网店型）：ООО «Воип Телеком» VoIPdevice（Москва；ИНН 7733663234；2008）坐实但网店 + 实施型，17 推 0 回 → 回 C 储备', []),
    'SC-1755': ('keep_C', '闸 2 回 C：Jjenka（jjenka.com）2 查无公司信息 → 未坐实 → 回 C 储备（MC 20 pcs 需求保留，来信再起 STC-110XGE 报价 + 预付 100%）', []),
    'SC-2841': ('keep_C', '闸 2 回 C：PIIR（piir.ru）1 查仅同名 ООО «ПИИР» 设计院（СПб 2021）域名归属未证 → 未坐实 → 回 C 储备', []),
    'SC-2972': ('keep_C', '闸 2 回 C：Akatel（akatel.ru / alarmex.ru）2 查仅同名他户 → 未坐实 → 回 C 储备（想直购 = 真意向保留；座机在表，电话接通再起）', []),
    # ---- 台湾 / 香港 ----
    'SC-2695': ('pool_candidate', '★ 台湾 · 上市品牌商 OEM 30%（长线）：慧友電子 EverFocus Electronics Corp.（新北；統編 89639615；上市 5484；1995；實收 NT$11.85 億）坐实；自有品牌 ✔ 上市 ✔ 对位 ✔ → P 池候选（找硬件采购）', ['oem_target']),
    'SC-2839': ('pool_candidate', '★ 台湾 · 上櫃品牌商 OEM 30%（长线）：宸曜科技 Neousys Technology Inc.（新北中和；統編 29169532；上櫃 6922；2010；資本 NT$5 億；董事長 高明和）坐实；品牌商 ✔ 工业对位 ✔ → P 池候选（20 推 0 回 → 换 OEM 稿点名产品经理）', ['oem_target']),
    'SC-2971': ('keep_C', '闸 2 回 C（同行）：元生工業 Konten Networks Inc.（新北新店；統編 65489708；2016；自述工业交换机 OEM/ODM 设计制造；出口 13 买家）坐实但 = 竞品制造商 → 回 C 储备（不推销）', []),
    'SC-2587': ('pool_candidate', '★ 香港 · 品牌商 OEM 30%：tactio Corporation（Lai Chi Kok；2006；自有品牌 INEO 工业 PoE + 交换机 8–48 口 + MC + AP 全线）部分坐实（CR 未取）；自有品牌全线 ✔ 已贴牌中国同类 ✔ 对位 ✔ → P 池候选（换 OEM 稿）', ['oem_target']),
    # ---- 回 C：格鲁吉亚 / 越南 ----
    'SC-2687': ('keep_C', '闸 2 回 C（微型）：PROTECH（Tbilisi Karvasla 商场 A308/1；ID 438117477；安防 / 消防 / 网络安装）坐实但微型 + 非点名国 + 16 推 0 回 → 回 C 储备（贴牌线索保留）', []),
    'SC-1883': ('keep_C', '闸 2 回 C：Anfatech（anfatech.com.vn）1 查仅近名 ANPHATECH JSC（2022；税号 2024-12 已关闭）归属未证 → 未坐实 → 回 C 储备', []),
}


def main():
    assert len(V) == 31
    ents = {e['code']: e for e in sieve.load_entities()}
    sv = sieve.load_sieve()
    for code, (verdict, reason, tags) in V.items():
        assert verdict in ('pool_candidate', 'keep_C', 'pass_final') and len(reason) >= 12, code
        cur = sv.get(code) or {}
        assert cur.get('verdict') in ('candidate', verdict) or cur.get('batch') == BATCH, ('not a gate-1 candidate', code, cur)
        g1_batch = cur.get('g1_batch') or (cur.get('batch') if cur.get('gate') == 1 else None)
        g1_reason = cur.get('g1_reason') or (cur.get('reason') if cur.get('gate') == 1 else None)
        row = {'verdict': verdict, 'gate': 2, 'rule': 'G2', 'reason': reason, 'date': DATE, 'manual': True, 'batch': BATCH,
               'g1_batch': g1_batch, 'g1_reason': g1_reason}
        old_tags = set(cur.get('tags') or [])
        new_tags = sorted(old_tags | set(tags))
        if new_tags:
            row['tags'] = new_tags
        sv[code] = row
    cnt = sieve.save_sieve(sv)
    c = Counter(v[0] for v in V.values())
    L = [f'# C 池 · 闸 2 · 第 131 批（{DATE}）—— 闸 1 第 26–32 批（桶 ⑥ 第 771–1155 户）候选 31 户查底数（候选全部过闸 2）', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b131_c.py`，第 131 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]} / 回 C {c["keep_C"]}**（无新永久 pass）。坐实 15（tekmodul、Omni Ray、OAK、Above-Net、Alfacomp、Cartago、Metsuki、Habari、Mootek、Joohitha、Bay Datacom、Zebronics、EverFocus、Neousys、Konten）/ 部分坐实 11（Konect、Plug & Play、Trimatrik、BBCPL、Cohesive、Indra Heera、Acceron、Амиком、RVi、tactio、Protech）/ 未坐实 4（Jjenka、Anfatech、PIIR、Akatel）+ 网店型 1（VoIP Telecom）。'
         ' 国别存疑待 Simon：SC-1871 Bay Datacom 表内「尼泊尔」↔ 印度 CIN；SC-1714 Omni Ray「智利」↔ 瑞士；SC-1713 OAK「玻利维亚」↔ 拉脱维亚。本批跑完 → 闸 1 第 01–32 批候选全部过闸 2，candidate 归零；P 池候选累计 179。', '',
         '> 档位：★ 14 = 自有品牌 / 贴牌 OEM 对象 8（Indra Heera、Mootek、Zebronics、Амиком、RVi、EverFocus、Neousys、tactio）+ 中型 · 专业分销 6（tekmodul、Omni Ray、Above-Net、Alfacomp、BBCPL、Acceron）；'
         '○ 8 = OAK、Metsuki、Konect、Habari、Plug & Play、Cohesive、Joohitha、Bay Datacom；△ 观察档 2 = Cartago Comex（微型报关行）/ Trimatrik（小型贴牌店）；'
         '回 C 7 = 未坐实 4 + 网店 1（VoIP Telecom）+ 同行 1（Konten）+ 微型 1（Protech）。Q-33 洪瑞现供：Indra Heera / Zebronics / Konect 口径待 Simon；俄语区 3 户收款路径待 Simon。'
         '**Simon 可按编号否决**。', '']
    for verdict, title in (('pool_candidate', 'P 池候选'), ('keep_C', '回 C 储备'), ('pass_final', '永久 pass')):
        rows = [(k, v) for k, v in V.items() if v[0] == verdict]
        if not rows:
            continue
        L += [f'## {title}（{len(rows)}）', '', '| 编号 | 公司 / 名 | 国家 | 标签 | 闸 2 结论 |', '|---|---|---|---|---|']
        for k, (vd, rs, tags) in sorted(rows):
            e = ents[k]
            L.append(f"| `{k}` | {sieve.md(e.get('name'))} | {e.get('country') or '未填'} | {'、'.join(sorted(set(tags) | set((sv[k].get('tags') or []))))} | {sieve.md(rs)} |")
        L.append('')
    p = os.path.join(sieve.REQ, f'C池闸2_批131_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
