#!/usr/bin/env python3
"""成交 PI 包（data/pi_2026-10/text/*.json，files_job 抽取结果）→ 结构化订单数据。

输出（data/pi_orders/）：
  销售单据明细.csv   每张 PI / CI / Quotation / 报关发票 的每一行货物（型号、数量、单价 USD、金额）
  采购合同明细.csv   每份 采购合同 的每一行（卖方 SmartByte/HRUI…、卖方型号、买方型号、数量、单价 RMB、小计）
  成单客户汇总.csv   按客户文件夹汇总：Simon 自己的标签、订单号数、首末单、累计销售 USD、累计采购 RMB、型号集合
  单号对照.csv       同一单号下 销售 USD vs 采购 RMB（能对上的才算毛利）
只做机械解析，不做判断；解析不到的文件在 _parse_report.md 里列出。
"""
import csv, glob, json, os, re
from collections import defaultdict, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'data', 'pi_2026-10', 'text')
OUT = os.path.join(ROOT, 'data', 'pi_orders')
os.makedirs(OUT, exist_ok=True)

MONTHS = {m: i + 1 for i, m in enumerate(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])}
MODEL_RE = re.compile(r'(?:^|^Seller:?[ \t]*\n?[ \t]*)((?:ST[ICH]|LT|ANW|TT|TRX|BNSC|HR|ZX|SW|DTM|SDI|HDR|NDR|LRS|MDR|AST)[A-Z]*-[A-Z0-9][A-Za-z0-9+()\-/._]{1,40}?)(?=[\t\n])', re.M)
INVNO_RE = r'([A-Z]{2,6}-?\d{6,}(?:-\d+)?[A-Z0-9_\-]*)'
NUMROW_RE = re.compile(r'\t(\d+)\t(\d+(?:\.\d+)?)\t(\d+(?:\.\d+)?)(?:\t|\n|$)')
SKIP_MODEL = re.compile(r'^(HS Code|Packing|TOTAL|SAY|PayPal|Freight|Bank|Misc|Shipping|Discount|Sample)', re.I)


def norm_date(s):
    if not s:
        return ''
    s = s.strip()
    m = re.search(r'(\d{4})[.\-/年](\d{1,2})[.\-/月](\d{1,2})', s)
    if m:
        return f'{int(m.group(1)):04d}-{int(m.group(2)):02d}-{int(m.group(3)):02d}'
    m = re.search(r'(\d{1,2})(?:st|nd|rd|th)?[,.\s]+([A-Za-z]{3,9})[,.\s]+(\d{4})', s)
    if m and m.group(2)[:3].lower() in MONTHS:
        return f'{int(m.group(3)):04d}-{MONTHS[m.group(2)[:3].lower()]:02d}-{int(m.group(1)):02d}'
    m = re.search(r'([A-Za-z]{3,9})[,.\s]+(\d{1,2})(?:st|nd|rd|th)?[,.\s]+(\d{4})', s)
    if m and m.group(1)[:3].lower() in MONTHS:
        return f'{int(m.group(3)):04d}-{MONTHS[m.group(1)[:3].lower()]:02d}-{int(m.group(2)):02d}'
    return s[:20]


def field(t, label):
    m = re.search(label + r'\s*[:：]?\s*\t+\s*([^\t\n]+)', t)
    return m.group(1).strip() if m else ''


def parse_sales(t):
    """Saga PI/CI/Quotation 模板（Invoice No. / Buyer / Model 行）。"""
    doc = OrderedDict()
    if re.search(r'Commercial\s+Invoice', t, re.I):
        doc['type'] = 'CI'
    elif re.search(r'Proforma\s+Invoice', t, re.I):
        doc['type'] = 'PI'
    elif re.search(r'^Quotation\s*$', t, re.M) or 'Quoted By' in t:
        doc['type'] = 'Quotation'
    elif re.search(r'Packing\s+List', t, re.I):
        doc['type'] = 'PL'
    else:
        return None
    m = None
    for lab in (r'Invoice No\.?', r'Order ID', r'P/I No\.?', r'Quotation No\.?', r'Invoice Number'):
        m = re.search(lab + r'\s*[:：]?\s*\t*\s*' + INVNO_RE, t)
        if m:
            break
    if not m:
        m = re.search(r'\b(ST[A-Z]{2}-?\d{8,}(?:-\d+)?[A-Z0-9_\-]*)', t)
    doc['currency'] = 'RMB' if re.search(r'Unit Price\s*\n?\s*\(RMB\)', t) else 'USD'
    doc['no'] = m.group(1) if m else ''
    doc['buyer'] = field(t, r'Buyer') or field(t, r'Company Name:\t[^\n]*?Company Name')
    if not doc['buyer']:
        m = re.search(r'Consignee/Importer[\s\S]{0,200}?Company Name:\t([^\t\n]+)', t)
        doc['buyer'] = m.group(1).strip() if m else ''
    doc['contact'] = field(t, r'Contact Person')
    doc['email'] = field(t, r'Email')
    doc['tel'] = field(t, r'Tel')
    doc['date'] = norm_date(field(t, r'Invoice Date') or field(t, r'(?<![A-Za-z] )Date(?! of)') or (re.search(r'Date of Exportation[^\n]*\n[^\n]*?(\d{4}\.\d{1,2}\.\d{1,2})', t) or [None, ''])[1])
    doc['payment'] = field(t, r'Payment Term') or field(t, r'Price Term')
    doc['destination'] = field(t, r'Destination')
    items = []
    # 模板 A：Model 行
    starts = [(m.start(1), m.group(1).strip()) for m in MODEL_RE.finditer(t) if not SKIP_MODEL.match(m.group(1)) and not re.search(r'SWIFT|IBAN|BIC', m.group(1))]
    tot = re.search(r'^TOTAL\t+(\d+)?\t*(\d+(?:\.\d+)?)?[^\n]*$', t, re.M | re.I)
    end_all = tot.start() if tot else len(t)
    for i, (pos, model) in enumerate(starts):
        nxt = starts[i + 1][0] if i + 1 < len(starts) else end_all
        chunk = t[pos:max(nxt, pos + 1)]
        if nxt < pos:
            chunk = t[pos:pos + 600]
        nm = None
        for mm in NUMROW_RE.finditer(chunk):
            q, u, a = int(mm.group(1)), float(mm.group(2)), float(mm.group(3))
            if q > 0 and abs(q * u - a) <= max(1.0, 0.02 * a):
                nm = (q, u, a)
                break
        spec = re.sub(r'\s+', ' ', chunk.split('\t', 1)[1] if '\t' in chunk else chunk)[:120]
        saga = re.search(r'\b(ST[ICH]-[A-Z0-9][A-Za-z0-9()+\-/]*)', chunk)
        items.append({'model': model, 'saga_model': saga.group(1) if saga else (model if model.startswith('ST') else ''), 'spec': spec,
                      'qty': nm[0] if nm else '', 'unit': nm[1] if nm else '', 'amount': nm[2] if nm else ''})
    # 模板 B：报关发票（Description of Goods … Q'ty Unit Value Total Value）
    if not items and 'Description of Goods' in t:
        for mm in re.finditer(r'^([A-Za-z][^\t\n]{2,60})\t+\d{8,10}\t[^\n]*?\t(\d+)\t(\d+(?:\.\d+)?)\t(\d+(?:\.\d+)?)\s*$', t, re.M):
            items.append({'model': mm.group(1).strip(), 'saga_model': '', 'spec': '报关品名', 'qty': int(mm.group(2)), 'unit': float(mm.group(3)), 'amount': float(mm.group(4))})
        tot = re.search(r'^Total\t+(\d+(?:\.\d+)?)', t, re.M)
        if tot:
            doc['total_qty'] = sum(x['qty'] for x in items if x['qty'] != '')
            doc['total'] = float(tot.group(1))
    if 'total' not in doc:
        if tot and tot.lastindex and tot.group(tot.lastindex):
            doc['total_qty'] = int(tot.group(1)) if tot.group(1) else ''
            doc['total'] = float(tot.group(2)) if tot.group(2) else ''
        else:
            doc['total_qty'] = sum(x['qty'] for x in items if x['qty'] != '') or ''
            doc['total'] = round(sum(x['amount'] for x in items if x['amount'] != ''), 2) or ''
    doc['items'] = items
    return doc


def parse_purchase(t):
    if '采购合同' not in t and '采购订单编号' not in t:
        return None
    doc = OrderedDict(type='采购合同')
    m = re.search(r'采购订单编号\s*[:：]?\s*\t*\s*([A-Z]{2,6}\d{6,}[A-Z0-9_\-]*)', t)
    doc['no'] = m.group(1) if m else ''
    m = re.search(r'卖方\s*[:：]?\s*\t*\s*([^\n\t]+)', t)
    seller = m.group(1).strip() if m else ''
    low = (seller + t[:1500]).lower()
    doc['seller'] = 'SmartByte' if 'smartbyte' in low or '凌特华盛' in low else ('HRUI' if 'hrui' in low or '洪瑞' in low else ('Hohunet' if 'hohunet' in low or '浩互' in low else seller[:30]))
    doc['date'] = norm_date(field(t, r'订单日期'))
    items = []
    tot = re.search(r'^TOTAL\t+(\d+)?\t*(\d+(?:\.\d+)?)?', t, re.M)
    end_all = tot.start() if tot else len(t)
    starts = [(m.start(1), m.group(1).strip()) for m in MODEL_RE.finditer(t[:end_all]) if not re.search(r'SWIFT|IBAN|BIC', m.group(1))]
    for i, (pos, model) in enumerate(starts):
        nxt = starts[i + 1][0] if i + 1 < len(starts) else end_all
        chunk = t[pos:nxt]
        cells = chunk.split('\t')
        buyer_model = cells[1].strip().split('\n')[0] if len(cells) > 1 else ''
        nm = None
        for mm in NUMROW_RE.finditer(chunk):
            q, u, a = int(mm.group(1)), float(mm.group(2)), float(mm.group(3))
            if q > 0 and abs(q * u - a) <= max(1.0, 0.02 * a):
                nm = (q, u, a)
                break
        if nm is None:
            mm = re.search(r'\t(\d+)\t(\d+(?:\.\d+)?)\t(\d+(?:\.\d+)?)', chunk)
            if mm:
                nm = (int(mm.group(1)), float(mm.group(2)), float(mm.group(3)))
        items.append({'seller_model': model, 'buyer_model': buyer_model, 'spec': re.sub(r'\s+', ' ', chunk)[:120],
                      'qty': nm[0] if nm else '', 'unit_rmb': nm[1] if nm else '', 'sub_rmb': nm[2] if nm else ''})
    doc['total_qty'] = int(tot.group(1)) if tot and tot.group(1) else (sum(x['qty'] for x in items if x['qty'] != '') or '')
    doc['total_rmb'] = float(tot.group(2)) if tot and tot.group(2) else (round(sum(x['sub_rmb'] for x in items if x['sub_rmb'] != ''), 2) or '')
    doc['items'] = items
    return doc


def main():
    sales, purch, report, costs = [], [], [], []
    for p in sorted(glob.glob(os.path.join(SRC, '*.json'))):
        j = json.load(open(p, encoding='utf-8'))
        t = j.get('text') or ''
        if not t or j['ext'].lower() not in ('.xls', '.xlsx', '.pdf', '.docx'):
            continue
        parts = j['path'].split('/')
        cust = parts[2] if len(parts) > 3 else ''
        sub = parts[3] if len(parts) > 4 else ''
        fn = parts[-1]
        if fn.startswith('成本统计'):
            for sh in re.split(r'^--- Sheet: ', t, flags=re.M)[1:]:
                name, body = sh.split(' ---', 1)
                rows = []
                for mm in re.finditer(r'^([^\t\n]+)\t(\d+)\t(\d+(?:\.\d+)?)\t(\d+(?:\.\d+)?)\s*$', body, re.M):
                    rows.append((mm.group(1).strip(), int(mm.group(2)), float(mm.group(3)), float(mm.group(4))))
                g = lambda k: (re.search(r'^' + k + r'\t+(\d+(?:\.\d+)?)', body, re.M) or [None, ''])[1]
                costs.append({'cust': cust, 'no': name.strip(), 'rows': rows, 'cost': g('总计'), 'received': g('总收款'), 'profit': g('利润'), 'file': j['path']})
            continue
        if '采购' in fn or '采购订单编号' in t:
            d = parse_purchase(t)
            if d:
                d.update(cust=cust, sub=sub, file=j['path'], ext=j['ext'])
                purch.append(d)
                if not d['items']:
                    report.append(('采购合同无明细', j['path']))
            continue
        if 'Zhengzhou Saga' not in t and 'Saga Telecom' not in t:
            continue
        d = parse_sales(t)
        if not d:
            continue
        d.update(cust=cust, sub=sub, file=j['path'], ext=j['ext'])
        sales.append(d)
        if not d['items'] and d['type'] != 'PL':
            report.append(('销售单据无明细', j['path']))
    # 写明细
    with open(os.path.join(OUT, '销售单据明细.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n')
        w.writerow(['客户文件夹', '订单子目录', '文件', '格式', '单据类型', '单号', '日期', '买方', '联系人', '邮箱', '付款/价格条款', '币种', '型号(单据)', 'Saga型号', '规格摘要', '数量', '单价', '金额', '单据合计数量', '单据合计'])
        for d in sales:
            rows = d['items'] or [{'model': '', 'saga_model': '', 'spec': '', 'qty': '', 'unit': '', 'amount': ''}]
            for it in rows:
                w.writerow([d['cust'], d['sub'], d['file'].split('/', 2)[-1], d['ext'], d['type'], d['no'], d['date'], d['buyer'], d['contact'], d['email'], d['payment'], d.get('currency', ''), it['model'], it['saga_model'], it['spec'], it['qty'], it['unit'], it['amount'], d['total_qty'], d['total']])
    with open(os.path.join(OUT, '采购合同明细.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n')
        w.writerow(['客户文件夹', '订单子目录', '文件', '格式', '采购订单编号', '卖方', '订单日期', '卖方型号', '买方型号', '规格摘要', '数量', '单价RMB', '小计RMB', '合同合计数量', '合同合计RMB'])
        for d in purch:
            rows = d['items'] or [{'seller_model': '', 'buyer_model': '', 'spec': '', 'qty': '', 'unit_rmb': '', 'sub_rmb': ''}]
            for it in rows:
                w.writerow([d['cust'], d['sub'], d['file'].split('/', 2)[-1], d['ext'], d['no'], d['seller'], d['date'], it['seller_model'], it['buyer_model'], it['spec'], it['qty'], it['unit_rmb'], it['sub_rmb'], d['total_qty'], d['total_rmb']])
    with open(os.path.join(OUT, '成本统计_Simon.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n')
        w.writerow(['客户文件夹', '单号(sheet)', '型号', '数量', '单价RMB', '小计RMB', '总计成本RMB', '总收款RMB', '利润RMB', '文件'])
        for c in costs:
            for r in c['rows'] or [('', '', '', '')]:
                w.writerow([c['cust'], c['no'], r[0], r[1], r[2], r[3], c['cost'], c['received'], c['profit'], c['file'].split('/', 2)[-1]])
    cost_by_no = {(c['cust'], c['no']): c for c in costs}
    # 单号归一：同一单号多份文件 → 取 CI 优先，其次 PI 最新修订（文件名含 R\d 取最大），再次 Quotation
    def rank(d):
        pri = {'CI': 0, 'PI': 1, 'Quotation': 2, 'PL': 3}[d['type']]
        rev = re.search(r'[_\- ]R(\d+)', d['file'])
        return (pri, 0 if d['items'] else 1, -(int(rev.group(1)) if rev else 0), 0 if d['ext'] != '.pdf' else 1)
    by_no = defaultdict(list)
    for d in sales:
        if d['no'] and d['type'] in ('CI', 'PI', 'Quotation'):
            by_no[(d['cust'], d['no'])].append(d)
    pur_by_no = defaultdict(list)
    for d in purch:
        pur_by_no[(d['cust'], d['no'])].append(d)
    best = {k: sorted(v, key=rank)[0] for k, v in by_no.items()}
    with open(os.path.join(OUT, '单号对照.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n')
        w.writerow(['客户文件夹', '单号', '取用单据', '日期', '买方', '币种', '销售合计', '销售数量', '型号', '采购卖方', '采购合计RMB', '采购数量', '采购型号', '毛利估算USD(按6.9/未税RMB)', '毛利率', 'Simon成本统计:成本RMB', '总收款RMB', '利润RMB'])
        for (cust, no), d in sorted(best.items()):
            pu = pur_by_no.get((cust, no), [])
            prmb = sum(float(x['total_rmb']) for x in pu if x['total_rmb'] != '') if pu else ''
            pqty = sum(int(x['total_qty']) for x in pu if x['total_qty'] != '') if pu else ''
            pm = '、'.join(sorted({it['seller_model'] + ('→' + it['buyer_model'] if it['buyer_model'] else '') for x in pu for it in x['items']}))
            sellers = '、'.join(sorted({x['seller'] for x in pu}))
            models = '、'.join(sorted({it['saga_model'] or it['model'] for it in d['items'] if (it['saga_model'] or it['model'])}))
            gp = gpr = ''
            if prmb != '' and d['total'] not in ('', None) and d.get('currency') == 'USD':
                try:
                    gp = round(float(d['total']) - prmb / 6.9, 1)
                    gpr = f'{gp / float(d["total"]) * 100:.0f}%' if float(d['total']) else ''
                except Exception:
                    pass
            cs = cost_by_no.get((cust, no), {})
            w.writerow([cust, no, d['type'] + ' ' + os.path.basename(d['file']), d['date'], d['buyer'], d.get('currency', ''), d['total'], d['total_qty'], models, sellers, prmb, pqty, pm, gp, gpr, cs.get('cost', ''), cs.get('received', ''), cs.get('profit', '')])
    # 客户汇总
    with open(os.path.join(OUT, '成单客户汇总.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n')
        w.writerow(['客户文件夹', 'Simon标签', '买方名称', '邮箱', '客户名单编号', '单号数(CI/PI)', '首单', '末单', '累计销售USD(单号去重)', '累计销售RMB(货代走账单)', '累计数量', '采购合同数', '累计采购RMB', 'Simon成本统计:利润RMB合计', 'Saga型号集合'])
        ents = json.load(open(os.path.join(ROOT, 'data', 'saga_clients', 'entities.json'), encoding='utf-8'))
        dom2 = {d.lower(): e['code'] for e in ents for d in (e.get('domains') or [])}
        name2 = {re.sub(r'[^a-z0-9]', '', (e.get('name') or '').lower())[:12]: e['code'] for e in ents if e.get('name')}
        custs = sorted({d['cust'] for d in sales} | {d['cust'] for d in purch})
        for cust in custs:
            ds = [d for (c, n), d in best.items() if c == cust]
            tags = re.sub(r'^\d+\s*', '', cust)
            buyers = [d['buyer'] for d in sorted(ds, key=lambda x: x['date'] or '') if d['buyer']]
            emails = sorted({d['email'] for d in ds if d['email']})
            dates = sorted(d['date'] for d in ds if re.match(r'\d{4}-\d{2}-\d{2}', d['date'] or ''))
            tot = round(sum(float(d['total']) for d in ds if d['total'] not in ('', None) and d['type'] != 'Quotation' and d.get('currency') == 'USD'), 2)
            tot_rmb = round(sum(float(d['total']) for d in ds if d['total'] not in ('', None) and d['type'] != 'Quotation' and d.get('currency') == 'RMB'), 2)
            codes = set()
            for em in emails:
                for one in re.split(r'[,;\s]+', em):
                    dmn = one.split('@')[-1].lower()
                    if dmn in dom2:
                        codes.add(dom2[dmn])
            if not codes:
                for b in buyers:
                    k = re.sub(r'[^a-z0-9]', '', b.lower())[:12]
                    if k and k in name2:
                        codes.add(name2[k])
            profit = round(sum(float(c['profit']) for c in costs if c['cust'] == cust and c['profit'] not in ('', None)), 2)
            qty = sum(int(d['total_qty']) for d in ds if d['total_qty'] not in ('', None) and d['type'] != 'Quotation')
            pu = [d for d in purch if d['cust'] == cust]
            prmb = round(sum(float(d['total_rmb']) for d in pu if d['total_rmb'] != ''), 2)
            models = sorted({it['saga_model'] or it['model'] for d in ds for it in d['items'] if (it['saga_model'] or it['model'])})
            w.writerow([cust, tags, buyers[-1] if buyers else '', '; '.join(emails), '、'.join(sorted(codes)), len(ds), dates[0] if dates else '', dates[-1] if dates else '', tot, tot_rmb, qty, len(pu), prmb, profit, '、'.join(models)])
    with open(os.path.join(OUT, '_parse_report.md'), 'w', encoding='utf-8') as f:
        f.write(f'# PI 包解析报告\n\n- 销售单据 {len(sales)} 份（PI/CI/Quotation/PL），单号去重 {len(best)}；采购合同 {len(purch)} 份；成本统计 sheet {len(costs)} 个\n- 未解析出明细的文件 {len(report)}：\n\n' + '\n'.join(f'- {a}：`{b}`' for a, b in report) + '\n')
    print('sales', len(sales), 'best', len(best), 'purchase', len(purch), 'issues', len(report))


if __name__ == '__main__':
    main()
