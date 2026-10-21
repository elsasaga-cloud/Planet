#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saga Clients · 第 1 步：把 `Clients/`（Simon 上传到 main 的历史客户表）逐文件、逐表、逐行原样抽出。

输入：Clients/**/*.xlsx|xls|xlt|docx
输出：
  data/saga_clients/rows_raw.jsonl      每行一个线索（原值照录 + 来源定位 file/sheet/row）
  data/saga_clients/followups.jsonl     每行一条跟进记录（原值照录 + 所属 file/No.）
  data/saga_clients/extract_report.json 每个文件/表抽到多少行，便于「不漏」复核

列名识别（不区分大小写）：
  No. | Company | Country / E或A | Person / Name | Position | From / Date | Interested in | Contact / E-mail / Mobile / Website | Remark
  AI评估结果 | CALUDE评估结果 | 询盘统计表：日期 国家 客户名称 客户来源 备注 联系人 邮箱 其他联系方式
跟进表（表名为数字 = 总表 No.）：跟进时间 | 跟进内容 | 客户回复 | 平台 | 备注（合并单元格 → 取非空格）
"""
import json
import os
import re
import sys
import warnings
import zipfile
from collections import OrderedDict

warnings.filterwarnings('ignore')
import openpyxl  # noqa: E402

try:
    import xlrd  # noqa: E402
except Exception:  # pragma: no cover
    xlrd = None

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'Clients')
OUT = os.path.join(ROOT, 'data', 'saga_clients')
os.makedirs(OUT, exist_ok=True)

HEADER_MAP = OrderedDict([
    ('no', ['no.', 'no', '序号']),
    ('company', ['company', '客户名称', '公司']),
    ('country', ['country', 'e或a', '国家']),
    ('person', ['person', 'name', '联系人', '姓名']),
    ('position', ['position', '职位']),
    ('from', ['from', 'date', '客户来源', '来源', '日期']),
    ('interest', ['interested in', 'interested', '兴趣', '需求']),
    ('contact', ['contact', 'e-mail', 'email', '邮箱', '联系方式']),
    ('mobile', ['mobile', '电话', '其他联系方式']),
    ('website', ['website', '网站']),
    ('remark', ['remark', '备注', 'remarks']),
    ('ai_eval', ['ai评估结果', 'ai评估']),
    ('claude_eval', ['calude评估结果', 'claude评估结果', 'claude评估']),
])
FOLLOW_MAP = OrderedDict([
    ('date', ['跟进时间', '时间', '日期']),
    ('content', ['跟进内容', '内容']),
    ('reply', ['客户回复', '回复']),
    ('platform', ['平台']),
    ('note', ['备注']),
])


def cell_str(v):
    if v is None:
        return ''
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    s = str(v).replace('\r\n', '\n').replace('\r', '\n').strip()
    return s


def map_header(cells, mapping):
    """返回 {字段: 列号}；同一字段多列时取第一列，其余列号放到 extra。"""
    idx = {}
    extra = []
    for i, c in enumerate(cells):
        key = cell_str(c).lower().replace(' ', '')
        if not key:
            continue
        hit = None
        for field, names in mapping.items():
            if key in [n.replace(' ', '') for n in names]:
                hit = field
                break
        if hit and hit not in idx:
            idx[hit] = i
        elif hit:
            extra.append((hit, i))
        else:
            extra.append((key, i))
    return idx, extra


def is_list_header(cells):
    keys = [cell_str(c).lower().replace(' ', '') for c in cells]
    return any(k in ('company', '客户名称') for k in keys)


def is_follow_header(cells):
    keys = [cell_str(c).lower().replace(' ', '') for c in cells]
    return any(k in ('跟进时间', '跟进内容') for k in keys)


def iter_sheets(path):
    """统一产出 (sheet_name, rows[list[list]])。"""
    ext = path.rsplit('.', 1)[-1].lower()
    if ext == 'xlsx':
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for ws in wb.worksheets:
            rows = []
            for row in ws.iter_rows(values_only=True):
                rows.append(list(row))
            yield ws.title, rows
        wb.close()
    elif ext in ('xls', 'xlt') and xlrd:
        wb = xlrd.open_workbook(path)
        for ws in wb.sheets():
            rows = [ws.row_values(r) for r in range(ws.nrows)]
            yield ws.name, rows


def parse_list_sheet(rows, file_rel, sheet):
    out = []
    hdr_i = None
    for i, r in enumerate(rows[:15]):
        if is_list_header(r):
            hdr_i = i
            break
    if hdr_i is None:
        return out, None
    idx, extra = map_header(rows[hdr_i], HEADER_MAP)
    for rn, r in enumerate(rows[hdr_i + 1:], start=hdr_i + 2):
        if not any(cell_str(c) for c in r):
            continue
        rec = OrderedDict()
        rec['file'] = file_rel
        rec['sheet'] = sheet
        rec['row'] = rn
        for field in HEADER_MAP:
            j = idx.get(field)
            rec[field] = cell_str(r[j]) if j is not None and j < len(r) else ''
        ex = []
        for name, j in extra:
            if j < len(r) and cell_str(r[j]):
                ex.append(f'{name}: {cell_str(r[j])}')
        rec['extra'] = ' | '.join(ex)
        # 一行里除了 No. 之外全空 → 模板空行，跳过
        if not any(rec[f] for f in HEADER_MAP if f != 'no') and not rec['extra']:
            continue
        out.append(rec)
    return out, idx


def parse_follow_sheet(rows, file_rel, sheet):
    out = []
    hdr_i = None
    for i, r in enumerate(rows[:5]):
        if is_follow_header(r):
            hdr_i = i
            break
    if hdr_i is None:
        # 无表头但有内容（极少数）：按前 5 个非空格落位
        body = [r for r in rows if any(cell_str(c) for c in r)]
        for rn, r in enumerate(body, start=1):
            vals = [cell_str(c) for c in r if cell_str(c)]
            if vals:
                out.append(OrderedDict(file=file_rel, no=sheet, row=rn, date=vals[0], content=vals[1] if len(vals) > 1 else '', reply=vals[2] if len(vals) > 2 else '', platform=vals[3] if len(vals) > 3 else '', note=' / '.join(vals[4:])))
        return out
    # 合并单元格：表头的列位置 = 字段起始列；某字段的值取 [起始列, 下一字段起始列) 内第一个非空
    hdr = rows[hdr_i]
    starts = []
    for i, c in enumerate(hdr):
        key = cell_str(c).replace(' ', '')
        for field, names in FOLLOW_MAP.items():
            if key in names:
                starts.append((i, field))
                break
    starts.sort()
    for rn, r in enumerate(rows[hdr_i + 1:], start=hdr_i + 2):
        if not any(cell_str(c) for c in r):
            continue
        rec = OrderedDict(file=file_rel, no=sheet, row=rn)
        for k, (i, field) in enumerate(starts):
            j_end = starts[k + 1][0] if k + 1 < len(starts) else len(r)
            vals = [cell_str(c) for c in r[i:j_end] if cell_str(c)]
            rec[field] = ' / '.join(vals)
        for field in FOLLOW_MAP:
            rec.setdefault(field, '')
        if any(rec[f] for f in FOLLOW_MAP):
            out.append(rec)
    return out


def docx_text(path):
    try:
        z = zipfile.ZipFile(path)
        xml = z.read('word/document.xml').decode('utf-8', 'ignore')
    except Exception as e:  # noqa
        return []
    paras = re.findall(r'<w:p[ >].*?</w:p>', xml, flags=re.S)
    out = []
    for p in paras:
        t = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p))
        t = t.strip()
        if t:
            out.append(t)
    return out


def main():
    rows_all, follows_all, report = [], [], []
    for dp, dn, fn in os.walk(SRC):
        for f in sorted(fn):
            path = os.path.join(dp, f)
            rel = os.path.relpath(path, ROOT)
            ext = f.rsplit('.', 1)[-1].lower()
            rep = OrderedDict(file=rel, kind=ext, sheets=[])
            if ext in ('xlsx', 'xls', 'xlt'):
                try:
                    for sheet, rows in iter_sheets(path):
                        nonempty = sum(1 for r in rows if any(cell_str(c) for c in r))
                        if nonempty == 0:
                            continue
                        if sheet.strip().isdigit():
                            fl = parse_follow_sheet(rows, rel, sheet.strip())
                            follows_all += fl
                            if fl:
                                rep['sheets'].append({'sheet': sheet, 'type': 'followup', 'rows': len(fl)})
                        else:
                            lst, idx = parse_list_sheet(rows, rel, sheet)
                            if idx is None:
                                # 不是客户清单表：也许是跟进表或说明
                                fl = parse_follow_sheet(rows, rel, sheet) if any(is_follow_header(r) for r in rows[:5]) else []
                                follows_all += fl
                                rep['sheets'].append({'sheet': sheet, 'type': 'followup' if fl else 'other', 'rows': len(fl) or nonempty})
                            else:
                                rows_all += lst
                                rep['sheets'].append({'sheet': sheet, 'type': 'list', 'rows': len(lst), 'columns': list(idx)})
                except Exception as e:  # noqa
                    rep['error'] = str(e)[:300]
            elif ext == 'docx':
                paras = docx_text(path)
                rep['sheets'].append({'sheet': '(docx)', 'type': 'docx', 'rows': len(paras)})
                rows_all.append(OrderedDict(file=rel, sheet='(docx)', row=0, no='', company='', country='', person='', position='', from_='', interest='', contact='', mobile='', website='', remark='', ai_eval='', claude_eval='', extra='', docx_paragraphs=paras))
            else:
                rep['sheets'].append({'sheet': '(binary)', 'type': ext, 'rows': 0})
            report.append(rep)
    # 字段名统一（from 是关键字，上面 docx 行用了 from_）
    for r in rows_all:
        if 'from_' in r:
            r['from'] = r.pop('from_')
    with open(os.path.join(OUT, 'rows_raw.jsonl'), 'w', encoding='utf-8') as f:
        for r in rows_all:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    with open(os.path.join(OUT, 'followups.jsonl'), 'w', encoding='utf-8') as f:
        for r in follows_all:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    with open(os.path.join(OUT, 'extract_report.json'), 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    n_list = sum(s['rows'] for rep in report for s in rep['sheets'] if s['type'] == 'list')
    n_fl = len(follows_all)
    print(f'files={len(report)} list_rows={n_list} followups={n_fl} docx={sum(1 for r in rows_all if "docx_paragraphs" in r)}')
    for rep in report:
        if rep.get('error'):
            print('ERROR', rep['file'], rep['error'])


if __name__ == '__main__':
    main()
