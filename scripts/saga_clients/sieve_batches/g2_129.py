#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C 池三闸 · 闸 2 · 第 129 批（2026-10-29）—— 闸 1 第 12–25 批（桶 ⑥「企业邮箱 · 其他区」）候选 75 户中的**俄语区段 33 户** = RU 25 / BY 2 / KZ 4 / UZ 2（含表内「俄罗斯」实为 .by / .kz 的 4 户），底数见 registry_batches/b129_c.py。

闸 2 结论写回 sieve.json（gate=2, rule=G2, batch=G2-129）：
  · pool_candidate = 法人 / 官网坐实或部分坐实 + §5 条数够 → 「P 池候选」，等 Simon 定夺；俄语区全部「预付 100% + 收款 / 物流路径待 Simon 定」。
  · keep_C = 未坐实（1 查未得 / 同名多户）/ 红旗（法人清算 / 执行程序多 / 一人公司）/ 守界（军标 ГОСТ РВ / 克里米亚制裁风险）/ 电商网店 / 同主体并入 → 回 C 储备。无新 pass_final。
  · 国别纠偏（待 Simon 确认，未写 research）：SC-714 / SC-977 俄罗斯 → 白俄罗斯；SC-883 / SC-1513 俄罗斯 → 哈萨克斯坦。
tier：★★ 首选 / ★ 品牌商 · 中型分销 / ○ 分销 · 集成 / △ 观察档（法人存疑 / 诉讼红旗 → 预付 100%）。

用法：python3 sieve_batches/g2_129.py   （幂等；写 sieve.json + docs/requirements/C池闸2_批129_2026-10-29.md）
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import sieve  # noqa: E402

BATCH = 'G2-129'
DATE = '2026-10-29'

V = {
    # ---- 俄罗斯 · 自有品牌（OEM 对象）----
    'SC-283': ('pool_candidate', '★ 自有品牌 · OEM 30%：ООО «ОНИКС Системы Безопасности» / ComOnyx（Москва；ИНН 9715421349 / ОГРН 1227700346796；GD Азовцев П. К.；品牌 1993 起安防制造商）坐实；自有品牌 ✔ 进口中国 PoE ✔ 对位 ✔ 坐实 ✔ → P 池候选（预付 100%，收款路径待 Simon）', []),
    'SC-302': ('pool_candidate', '△ 观察档 · OEM 30% + 预付 100%：OSNOVO 俄区自有品牌 PoE / 工业交换机（品牌站 + 官方经销商 osnovo-shop.ru 在线；品牌运营法人 1 查未取）部分坐实；自有品牌 ✔ 对位 ✔ 中国代工 ✔ → 入池观察档（法人补查后升 ★）；可否决', []),
    'SC-782': ('pool_candidate', '★★ 制造商 · 真互动 · OEM 30%：ООО «ГК ЭКСАРА»（Москва；ИНН 9725000981 / ОГРН 5187746026331；2018；ОКВЭД 26.30 通信设备制造；营收 1.8 млрд ₽；GD Андросенко Т. В.）坐实；目录册已发、杭州中文联系人 +86 在表 ✔ 对位 ✔ 坐实 ✔ 体量 ✔ → P 池候选首选（微信 / 中文直跟；WDM / PTN 走本职线）', ['dayjob_fit']),
    'SC-884': ('pool_candidate', '△ 观察档 · OEM 30% + 预付 100%：Novicam = ООО «НОВЫЕ КАМЕРЫ»（Москва；ИНН 7725668550 / ОГРН 1097746256332；2009；GD Макиевский Г. В.）ИНН 对上但 2025 纳税 0 → 运营主体存疑；自有品牌 CCTV + PV-Link 配件 ✔ 对位 ✔ → 入池观察档；可否决', []),
    'SC-1251': ('pool_candidate', '★ 自有品牌大厂 · OEM 30%（长线）：АО НВП «БОЛИД»（Королёв；ИНН 5018000402 / ОГРН 1035003350766；1996；GD Бабанов И. А.；俄安防 / 消防自动化制造龙头）坐实；已进口 Elink MC ✔ 对位 ✔ 坐实 ✔ → P 池候选（找采购部；17 推 0 回 → 换稿）', []),
    'SC-1492': ('pool_candidate', '★ 自有品牌大厂 · OEM 30%（长线）：ООО «ДССЛ» / TRASSIR（Москва；ИНН 7709423841 / ОГРН 1037709044460；2003；GD Олейник И. В.；自产 + 19 物流中心 + 40 国）坐实；多牌进口中国 ✔ 对位 ✔ 坐实 ✔ → P 池候选（找硬件采购）', []),
    # ---- 俄罗斯 · 分销 / 集成 ----
    'SC-305': ('pool_candidate', '★ 中型工业分销 20%：ООО «ПРОСОФТ»（Москва；ИНН 7724020910 / ОГРН 1037739267488；1994；40 人在册；GD Минеев Е. М.）坐实；已进口三旺 / 迈威 / BDCOM ✔ 对位 ✔ 坐实 ✔ → P 池候选（找工业网络产品经理；8 推 0 回 → 换稿）', []),
    'SC-309': ('pool_candidate', '△ 观察档 · 分销 20% + 预付 100%：ООО «ТД ТЕЛЕКОР»（Москва；ИНН 9729079661 / ОГРН 1177746446778；2017；GD Трошин М. В.；trostyanskiy@tdtel.ru 在册）坐实但仲裁 33 + 执行程序 4 = 红旗；在售中国同口型 ✔ 对位 ✔ → 入池观察档；可否决', []),
    'SC-311': ('pool_candidate', '○ 连锁分销 20%：ООО «ВИДЕОГЛАЗ ЦЕНТР»（Москва；ИНН 7719840097 / ОГРН 1137746240279；品牌 2002；B2B 门户 + 加盟）坐实；已进口 hasivo PoE ✔ 对位 ✔ 坐实 ✔ 连锁体量 ✔ → P 池候选（17 推 0 回 → 点名 B2B 采购换稿）', []),
    'SC-323': ('pool_candidate', '★ 大分销 20%（长线）：ООО «КОМПТЕК»（Москва；ИНН 5003082667 / ОГРН 1085003004877；2008；2021 利润 628 млн ₽；GD Залётов А. Н.）坐实；已进口 DCN ✔ 对位 ✔ 坐实 ✔ → P 池候选（找网络线产品经理）', []),
    'SC-625': ('pool_candidate', '★ 中型分销 20%：ООО «АЙПИМАТИКА»（Красногорск；ИНН 7733678135 / ОГРН 5087746581621；2008；2025 利润 82.9 млн ₽；GD Усов М. Е.；经销合同在 Федресурс；.kz 分部）坐实；已进口 Wi-Tek / TG-NET ✔ 对位 ✔ 坐实 ✔ → P 池候选（17 推 0 回 → 换稿；哈萨克分部 = 备选收款路径）', []),
    'SC-670': ('pool_candidate', '○ 集成 25% + 预付 100%：ООО «ЛАНСЭЙЛ»（Москва；ИНН 9723019747 / ОГРН 1177746269634；2017；负责人 Петров П. В. = pvp@lansale.ru 决策人直达）坐实；150 台 1 光 2 PoE 询盘 ✔ 对位 ✔ 坐实 ✔ → P 池候选（点名 Павел 报阶梯价）', []),
    'SC-708': ('pool_candidate', '★ 大分销 20%（长线）：ООО «АРМО-Системы»（Москва；ИНН 7715284716 / ОГРН 1027739174352；2001；股本 10 млн ₽；2025 营收 3.2 млрд ₽；GD Кобытев А. В.）坐实；已进口 Utepo ✔ 对位 ✔ 坐实 ✔ → P 池候选（找产品经理）', []),
    'SC-722': ('pool_candidate', '○ 分销 20%：ООО «БИК-ВИДЕО»（СПб + Москва；ИНН 7826154575 / ОГРН 1027810264932；2002；22 人；Директор Залогин К. А.）坐实；多牌在售中国同口型 ✔ 对位 ✔ 坐实 ✔ → P 池候选（SDI / HDMI 走本职线）', []),
    'SC-817': ('pool_candidate', '★ 老牌进口分销 20%（长线）：ООО «ЭФО»（СПб；ИНН 7804050438 / ОГРН 1027802501000；1995；多家原厂独家代表；GD Федоров В. В.）坐实；很多中国合作商 ✔ 对位 ✔ 坐实 ✔ → P 池候选（infiber.ru 无 MX → 换 efo.ru 地址再发）', []),
    'SC-1280': ('pool_candidate', '○ 工业分销 20%：ООО «ПЛКСистемы»（Москва；ИНН 7708160477 / ОГРН 1027739102379；GD Прейс М. В.；Korenix + PLC / SCADA 分销）坐实；已进口台湾 Korenix ✔ 对位 ✔ 坐实 ✔ 分销主体 ✔ → P 池候选（18 推 0 回 → 换稿）', []),
    # ---- 俄罗斯 · 回 C ----
    'SC-623': ('keep_C', '闸 2 回 C：Industrial Nets（industrialnets.ru）1 查仅同名「Инженерные сети» 他户 → 未坐实；进口中国同类 ✔ 但法人未取 → 回 C 储备（来信再起则补查 + 预付 100%）', []),
    'SC-702': ('keep_C', '闸 2 回 C（守界）：АО «АНГСТРЕМ-ТЕЛЕКОМ»（Зеленоград；ИНН 7735102121；24 人；自有 Корунд / Топаз 系列）坐实但持 ГОСТ РВ 0015-002 军品体系证书 + Ангстрем 系制裁风险 → 军工不碰（INH）→ 回 C', []),
    'SC-729': ('keep_C', '闸 2 回 C：Brown Bear（brownbear.ru）1 查仅同名 ООО «Браун» 他户 → 未坐实；Planet 渠道 ✔ 但法人未取 → 回 C 储备', []),
    'SC-859': ('keep_C', '闸 2 回 C（守界 + 未坐实）：mirtelcom.ru 1 查命中 ООО «МИРТЕЛЕКОМ» Симферополь（Миранда-Медиа 子公司 = 克里米亚制裁风险）+ Краснодар 同名运营商，域名归属未证 → 不主动碰 → 回 C', []),
    'SC-860': ('keep_C', '闸 2 回 C：Mistercom 同名两户（Москва 已清算 / Воскресенск 执行程序 34 件）域名归属未证 → 未坐实 + 红旗 → 回 C 储备（WA 路径在，来信再核法人）', []),
    'SC-912': ('keep_C', '闸 2 回 C：QP Optom（qpoptom.ru）1 查仅同名「Видеонаблюдение» 他户 → 未坐实；批发主体 ✔ 但法人未取 → 回 C 储备', []),
    'SC-941': ('keep_C', '闸 2 回 C（红旗）：Smartec 对应法人 ООО «Смартек Секьюрити»（ИНН 7731421078）2026-10-02 状态不动 = 已清算，品牌站仍在线、新主体未取 → 回 C（新法人来信再起则 OEM 30% + 预付 100%）', []),
    'SC-946': ('keep_C', '闸 2 回 C（红旗 + 微型）：ООО «Спектр Видео»（Зеленоград；ИНН 7730667230；一人公司；执行程序 38 件）坐实但不入池 → 回 C 储备', []),
    'SC-1527': ('keep_C', '闸 2 回 C（微型）：ООО «ПЛКОНТРОЛЛЕР»（Омск；ИНН 5505062590；2019；在册 1 人；住宅地址）坐实但一人公司 → 回 C 储备（来信再起则预付 100%）', []),
    # ---- 白俄罗斯（国别纠偏待 Simon）----
    'SC-714': ('pool_candidate', '○ 自有 iFLOW 牌 + 多牌分销 · OEM 30% / 分销 20%：ООО «Торговый дом «АВАНТ-ТЕХНО»（Минск, ул. Короля 45；avant.by + utepo.by 同主体；BYN 计价；Hikvision / Utepo / 自有 iFLOW 工业 PoE）部分坐实（УНП 未取）；国别纠偏 俄罗斯 → 白俄罗斯 待 Simon；自有牌 ✔ 已进口中国同类 ✔ 对位 ✔ → P 池候选（预付 100%，白俄收款路径待 Simon）', ['oem_target']),
    'SC-977': ('keep_C', '闸 2 回 C（并入）：utepo.by 页脚 = ООО «Торговый дом «АВАНТ-ТЕХНО»（Минск, ул. Короля 45）与 SC-714 同一法人 → 并入 SC-714 统一跟进，避免双发；国别纠偏 俄罗斯 → 白俄罗斯 待 Simon', []),
    # ---- 哈萨克斯坦 ----
    'SC-299': ('pool_candidate', '★ 自有品牌 SNR · OEM 30%：ТОО «NAG KAZAKHSTAN»（Алматы, пр. Жибек Жолы 135；БИН 191040001403；2019；Евразийский банк USD / EUR 账户，代理行 Raiffeisen Vienna；NAG / SNR 集团哈萨克子公司）坐实；自有品牌 ✔ 中国直采 ✔ 对位 ✔ 坐实 ✔ → P 池候选（外币账户 = 俄语区收款路径线索，供 Simon 参考）', []),
    'SC-883': ('keep_C', '闸 2 回 C：Nout.kz = ТОО «Ноут кз»（Алматы；БИН 170940036145；2017；руководитель Унру А. С.）坐实但为笔记本 / 电子产品电商零售，非网络分销主体 → 回 C 储备；国别纠偏 俄罗斯 → 哈萨克斯坦 待 Simon', []),
    'SC-1020': ('keep_C', '闸 2 回 C：Moon.kz 1 查仅同名他户（topcam.kz 个体 / Monitoring Systems KZ / MOONSTAR.KZ）→ 未坐实 → 回 C 储备', []),
    'SC-1513': ('keep_C', '闸 2 回 C：ТОО «Manggis»（Алматы, пр. Гагарина 236Б；БИН 110940009256）坐实但为 CCTV 网店 + 安装商 → 回 C 储备（哈萨克有 NAG 更强主体）；国别纠偏 俄罗斯 → 哈萨克斯坦 待 Simon', []),
    # ---- 乌兹别克斯坦 ----
    'SC-295': ('pool_candidate', '○ 集成 25%：OOO «Inline System»（Ташкент, ул. Нукус 89；2011 起；СКС / ВОЛС / 安防 / IP 电话全线集成商；office@inline.uz）部分坐实（ИНН 未取）；在售同口型 2 光 8 ✔ 对位 ✔ 同区 SETKO 成单先例 ✔ → P 池候选（19 推 0 回 → 换稿；预付 100%）', []),
    'SC-897': ('pool_candidate', '★ 本土自有品牌 · OEM 30%：PixieTech（Ташкент, ул. Янгизамон 31/1；2020 创立「首家本土电信设备制造商」；交换机 / 路由 / GPON / IP 话机 / 机柜 / UPS 全线贴牌）部分坐实（ИНН 未取）；全线贴牌 = OEM 对象 ✔ 对位 ✔ 同区先例 ✔ → P 池候选（洪瑞现供 → Q-33 口径待 Simon：默认只推 SmartByte / Marvell 管理 + 工业线）', ['oem_target']),
}


def main():
    assert len(V) == 33
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
    L = [f'# C 池 · 闸 2 · 第 129 批（{DATE}）—— 闸 1 第 12–25 批（桶 ⑥）候选 · 俄语区段 33 户查底数', '',
         f'> 底数明细见 `data/saga_clients/registry/`（`registry_batches/b129_c.py`，第 129 批）并已渲染进各户 MD「公司底数」块；本表为闸 2 结论，写入 `data/saga_clients/sieve.json`（gate=2, batch={BATCH}）。'
         f' 结果：**P 池候选 {c["pool_candidate"]} / 回 C {c["keep_C"]}**（无新永久 pass）。坐实 24 / 部分坐实 5（OSNOVO 法人未取、Novicam 运营主体存疑、АВАНТ-ТЕХНО УНП 未取、Inline / PixieTech ИНН 未取）/ 未坐实 6（Industrial Nets、Brown Bear、Mirtelcom、Mistercom、QP Optom、Moon.kz）。'
         ' 国别纠偏待 Simon：SC-714 / SC-977 俄罗斯 → 白俄罗斯；SC-883 / SC-1513 俄罗斯 → 哈萨克斯坦。俄语区全部「预付 100% + 收款 / 物流路径待 Simon 定」（NAG KZ 有 USD / EUR 账户 + 维也纳代理行，可作路径线索）。', '',
         '> 档位：★★ 1 = Exara（制造商 + 真互动 + 中文直达）；★ 11 = ComOnyx / Bolid / DSSL（自有品牌）、ProSoft / CompTek / Ipmatika / ARMO / EFO（中型 · 大分销）、NAG KZ（SNR 自有品牌）、PixieTech UZ（本土贴牌）；'
         '○ 6 = Videoglaz / BIC Video / PLC Systems / Lansale（RU）、АВАНТ-ТЕХНО（BY）、Inline System（UZ）；△ 观察档 3 = OSNOVO（法人未取）/ Novicam（运营主体存疑）/ ТД Телекор（诉讼红旗）；'
         '回 C 13 = 未坐实 6 + 守界 2（Ангстрем-Телеком 军标 / Mirtelcom 克里米亚）+ 红旗 3（Smartec 清算 / Spektr Video 执行 38 / Mistercom）+ 微型 1（PLController）+ 网店 2（Nout.kz / Manggis）+ 并入 1（utepo.by → SC-714）。'
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
    p = os.path.join(sieve.REQ, f'C池闸2_批129_{DATE}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    print(BATCH, len(V), dict(c), 'sieve', dict(cnt), os.path.relpath(p, sieve.ROOT))


if __name__ == '__main__':
    main()
