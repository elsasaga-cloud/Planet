"""T29-U63：非美国客户的公开 / 半公开海关数据逐户查询结果（第 81 批）。
一个 JSON、一户一条；来源混合：
  - HMRC Find UK Traders（英国官方：进口商名 + 8 位商品编码 + 交易月份；无供应商 / 无数量 / 无金额）
  - Volza 公司页摘要（土耳其 / 俄罗斯 / 巴基斯坦等海关镜像；票数 / 供应商数 / 来源国占比 / HS / 前三供应商 / 一张样例提单）
  - NBD Trade Data 公司页摘要（印度海关：记录数 / 供应商数 / HS / 关联伙伴 / 分年票数 / 最近 5 条）
  - Tendata / MarketInsideData 搜索摘要（土耳其：票数 / 供应商数 / 金额区间）
Usage (python):  from imports_other import put;  put('SA-015', name=..., iso='GB', source=..., found=True, lines=[...])
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
P = os.path.join(ROOT, 'data', 'saga_clients', 'imports', 'other_countries_2026-10-27.json')

META = {
    'source': '其他国家公开 / 半公开海关数据（HMRC Find UK Traders；Volza / NBD / Tendata / MarketInsideData 公司页免费摘要）',
    'kind': 'other',
    'fetched': '2026-10-27',
    'note': '一户一条；found=false 表示该来源按公司名 / IEC 查不到。英国官方数据只有「商品编码 × 月份」，没有供应商、数量、金额；'
            '聚合站摘要只给票数 / 供应商数 / 来源国 / HS / 前几名供应商，明细要付费，我们不买。',
}


def load():
    if os.path.exists(P):
        return json.load(open(P, encoding='utf-8'))
    return {'_meta': dict(META), 'rows': {}}


def save(D):
    os.makedirs(os.path.dirname(P), exist_ok=True)
    json.dump(D, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def put(code, **kw):
    D = load()
    kw.setdefault('fetched', '2026-10-27')
    D['rows'][code] = kw
    save(D)
    return len(D['rows'])


if __name__ == '__main__':
    D = load()
    rows = D['rows']
    print(len(rows), 'rows;', sum(1 for r in rows.values() if r.get('found')), 'found')
    for c, r in sorted(rows.items()):
        print(c, r.get('iso'), '✓' if r.get('found') else '✗', r.get('source'), '|', (r.get('lines') or [''])[0][:90])
