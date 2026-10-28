#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 92 批 · 补项 3 处（T29-U88，2026-10-28）：SB-231 PSC 页（fetch_page）/ SB-574 Impakt zarząd（web_search rejestr.io）/ SB-537 rusprofile ИНН 7204152580（web_search 一次未命中 → 停）。put 为增量合并（只更新给出的字段）。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from registry_store import put, load_all
F = '2026-10-28'
put('SB-231', key='gb',
    psc='Nathan James Parys（1982-01 生，威尔士）— 股份 / 表决权 ≥75% + 任免董事权，2025-04-02 起（身份已核验）；**前控制人 Mrs Jie Kennett（中国籍，1981 生，Wigan）≥75% 2017-09-08 → 2025-04-02 终止**；Rebecca Mary Parkinson 25–50% 2017-09 → 2018-01 终止（PSC 页 2026-10-28 取）',
    notes='第 92 批补项：PSC 页已取 → 2025-04-02 换手坐实（股权 + 董事同日由中国籍创始人 Jie Kennett 转给 Nathan Parys）= 新东家 100% 控股、一人决策；「中国供应链熟人」时代结束，供应商正在重建。')
put('SB-574', key='pl',
    officers=['Marcin Chojnacki — Prezes Zarządu（2025-07-01 起）', 'Tadeusz Piotr Alankiewicz — Wiceprezes Zarządu（2015-11-13 起；Prezes / Wiceprezes 可单独代表）', 'Łukasz Wardak — Członek Zarządu（2025-07-01 起）', 'Maciej Grygiel / Hubert Kaczmarek — Prokurenci', 'Robert Żurek（前 Prezes / 创始人）+ Celina Żurek — Rada Nadzorcza（监事会）= 控股家族', '（gowork 旧记录：Robert Władysław Żurek Prezes、Dariusz Andrzej Żurkowski Wiceprezes —— 已换届）'],
    psc='国内自然人所有（bizraport「WŁASNOŚĆ KRAJOWYCH OSÓB FIZYCZNYCH」）；推定 Żurek 家族控股（夫妇坐监事会）',
    accounts='RDF 已报 2023 / 2024 / 2025 年财报（imsig）；主 PKD 46.51.Z 电脑 / 外设 / 软件批发；KRZ 无记录',
    notes='第 92 批补项：zarząd 已取 —— **2025-07-01 换届**（创始人 Robert Żurek 退居监事会，新总裁 Marcin Chojnacki）→ 新管理层一年内重审品类 / 供应商 = Lanberg 交换机 OEM 的进门窗口；写 Lanberg 产品经理抄 Prezes 办公室；两人联署制（Prezes 或 Wiceprezes 可单独签）→ 合同走 Alankiewicz / Chojnacki。')
put('SB-537', key='ru',
    notes=(load_all().get('SB-537', {}).get('notes', '') + '；第 92 批补项：web_search「ИНН 7204152580 rusprofile」一次未命中（结果全为无关 Rusprofile 自身条目）→ 按规程停，下轮如需改用 checko.ru / list-org 直链').strip('；'))
print('fix 3 ok')
