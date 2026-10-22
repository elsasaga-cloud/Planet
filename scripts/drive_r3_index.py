#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T29-U12 / PR-02-33：Google Drive 第三轮（Elsa 账号里剩余的全部文件夹）入库索引
  输入  data/_drive_r3_folders.tsv   id \t 文件夹名 \t 父文件夹 id   （根 = 0AJ8a22_hYShqUk9PVA）
        data/_drive_r3_files.tsv     id \t 文件名 \t mime \t 字节 \t 父文件夹 id
  输出  data/drive_r3_index.json     与 data/suppliers_drive_index.json 同 schema
        {meta, 文件夹清单, files[文件名/文件类型/文件大小/所在子文件夹路径/内容摘要/_drive_id/_bytes/_摘要来源]}
路径前缀统一为 Drive第三轮/<根文件夹名>/…，scripts/drive_ingest/ingest.py 的 load_index() 取第 2 段为 top，
因此每个根文件夹各自打包成 ≤1.8 GB 的 Release 分卷。
完整性：文件 TSV 已与 Drive 全局计数对账（'me' in owners 非文件夹 1,910 = 本表 1,456 + 供应商两夹 453 + Extra Info.zip 1；
另加 5 份 Anda Telecom 共享文件的副本），见 docs/入库完整性总审计_2026-10-22.md。
用法：python3 scripts/drive_r3_index.py
"""
import csv, datetime, json, os
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDERS = os.path.join(ROOT, 'data', '_drive_r3_folders.tsv')
FILES = os.path.join(ROOT, 'data', '_drive_r3_files.tsv')
OUT = os.path.join(ROOT, 'data', 'drive_r3_index.json')
DRIVE_ROOT = '0AJ8a22_hYShqUk9PVA'
PREFIX = 'Drive第三轮'

EXT_TYPE = {
    '.png': '图片', '.jpg': '图片', '.jpeg': '图片', '.gif': '图片', '.bmp': '图片', '.webp': '图片',
    '.docx': 'Word', '.doc': 'Word', '.pdf': 'PDF', '.pptx': 'PPT', '.ppt': 'PPT',
    '.xlsx': 'Excel', '.xls': 'Excel', '.mp4': '视频', '.mov': '视频', '.zip': '压缩包', '.rar': '压缩包',
    '.txt': '文本', '.cfg': '配置',
}
ROOT_NOTE = {
    'Saga Telecom Resource Library': 'Saga 资料库（Roadmap、软件功能清单）',
    'MUST KNOW': '必读资料（认证/测试报告/价格表/手册）',
    'Marvell Based Commercial Managed Switch': 'SmartByte 商用管理型（Saga STC-）',
    'Marvell Based Industrial Managed Switch': 'SmartByte 工业管理型（Saga STI-）',
    'Marvell Based Industrial Unmanaged Switch': 'SmartByte 工业非管理型（Saga STI-）',
    'Anda Telecom 共享（副本，供入库）': 'andatelecom1@gmail.com 共享给 Elsa 的测试报告/PA 资料/视频（副本）',
}


def human(n):
    n = int(n or 0)
    for u in ('B', 'KB', 'MB', 'GB'):
        if n < 1024 or u == 'GB':
            return f'{n:.1f} {u}' if u != 'B' else f'{n} B'
        n /= 1024.0


def ftype(name):
    ext = os.path.splitext(name)[1].lower()
    return EXT_TYPE.get(ext, ext.lstrip('.').upper() or '未知')


def clip(s, n=50):
    return s if len(s) <= n else s[:n - 1] + '…'


def main():
    name_of, parent_of = {}, {}
    with open(FOLDERS, encoding='utf-8') as f:
        for r in csv.reader(f, delimiter='\t'):
            if len(r) < 3 or not r[0]:
                continue
            name_of[r[0]] = r[1]
            parent_of[r[0]] = r[2]

    def path_of(fid):
        parts, guard = [], 0
        while fid in name_of and guard < 30:
            parts.append(name_of[fid])
            fid = parent_of.get(fid)
            guard += 1
        return '/'.join([PREFIX] + list(reversed(parts)))

    rows = []
    with open(FILES, encoding='utf-8') as f:
        for r in csv.reader(f, delimiter='\t'):
            if len(r) < 5 or not r[0]:
                continue
            rows.append(dict(id=r[0], name=r[1], mime=r[2], size=int(r[3] or 0), parent=r[4]))
    ids = [r['id'] for r in rows]
    assert len(ids) == len(set(ids)), 'duplicate ids in files tsv'
    missing_parent = [r for r in rows if r['parent'] not in name_of]
    assert not missing_parent, f'{len(missing_parent)} files with unknown parent, e.g. {missing_parent[:2]}'

    img_count = Counter(r['parent'] for r in rows if ftype(r['name']) == '图片')
    img_rank, rank_counter = {}, Counter()
    for r in sorted(rows, key=lambda x: (x['parent'], x['name'])):
        if ftype(r['name']) == '图片':
            rank_counter[r['parent']] += 1
            img_rank[r['id']] = rank_counter[r['parent']]

    files = []
    for r in rows:
        name, t = r['name'], ftype(r['name'])
        folder_path = path_of(r['parent'])
        model = name_of.get(r['parent'], '')
        stem = os.path.splitext(name)[0]
        if t == '图片':
            summ = f'{model} 产品图 {img_rank.get(r["id"])}/{img_count.get(r["parent"], 0)}（入库时提取文字/缩略图）'
        elif t == 'Word' and stem.startswith(('STI-', 'STC-', 'STH-')):
            summ = f'{stem} 数据表（Word，入库时全文提取）'
        elif t == '视频':
            summ = f'{stem}（视频，入库时留元数据+备份原件）'
        else:
            summ = f'{stem}（{t}，入库时全文提取）'
        files.append(OrderedDict([
            ('文件名', name), ('文件类型', t), ('文件大小', human(r['size'])),
            ('所在子文件夹路径', folder_path), ('内容摘要', clip(summ)),
            ('_drive_id', r['id']), ('_bytes', r['size']), ('_摘要来源', '文件名推断'),
            ('_mime', r['mime']),
        ]))
    files.sort(key=lambda x: (x['所在子文件夹路径'], x['文件名']))
    folders = sorted({path_of(fid) for fid in name_of})
    total = sum(x['_bytes'] for x in files)
    by_type = Counter(x['文件类型'] for x in files)
    by_top = Counter(x['所在子文件夹路径'].split('/')[1] for x in files)
    bytes_top = Counter()
    for x in files:
        bytes_top[x['所在子文件夹路径'].split('/')[1]] += x['_bytes']
    roots = [fid for fid, p in parent_of.items() if p == DRIVE_ROOT]
    meta = OrderedDict([
        ('来源', 'Google Drive（Elsa 账号）第三轮：SmartByte/CENTEC/Realtek 之外剩余的全部根文件夹 '
                + '；'.join(f'《{name_of[r]}》(id {r})' for r in roots)),
        ('生成时间UTC', datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')),
        ('生成方式', 'google_drive.list_files 逐文件夹抄录 → data/_drive_r3_folders.tsv + _drive_r3_files.tsv；'
                 '2026-10-22 与 Drive 全局计数对账（\'me\' in owners 非文件夹 1,910）补齐漏抄的 95 个文件（2.5G L2+ with PoE 9 份 docx、'
                 'L3 BT 4 份 docx、12 个型号夹 82 张 PNG）；andatelecom1 共享的 5 个文件复制到《Anda Telecom 共享（副本，供入库）》；'
                 '→ scripts/drive_r3_index.py 汇总；原件由 scripts/drive_ingest/ingest.py 在 GitHub Actions 下载、提取全文并打包到私有 Release'),
        ('文件总数', len(files)),
        ('文件夹总数', len(folders)),
        ('总大小', human(total)),
        ('总字节', total),
        ('按根文件夹', OrderedDict((k, {'文件数': by_top[k], '字节': bytes_top[k], '说明': ROOT_NOTE.get(k, '')}) for k in sorted(by_top))),
        ('按类型', dict(by_type.most_common())),
        ('字段说明', OrderedDict([
            ('文件名', 'Drive 中的文件名'),
            ('文件类型', '按扩展名归类：图片/Word/PDF/PPT/Excel/视频/配置'),
            ('文件大小', '人类可读（源字节数见 _bytes）'),
            ('所在子文件夹路径', f'{PREFIX}/<根文件夹名>/…（第 2 段为打包单位）'),
            ('内容摘要', '索引阶段仅按文件名推断；真正的全文/缩略图在 data/drive_r3/ 由 ingest.py 生成'),
        ])),
    ])
    out = OrderedDict([('meta', meta), ('文件夹清单', folders), ('files', files)])
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f'files={len(files)} folders={len(folders)} total={human(total)} by_top={dict(by_top)} by_type={dict(by_type)}')


if __name__ == '__main__':
    main()
