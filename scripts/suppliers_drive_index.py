#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T25 / PR-02-18：把 Google Drive 两个供应商文件夹的逐页抄录
  data/suppliers_drive/_listing_realtek.tsv  + _imgs_realtek.txt   (Realtek Based Commercial Switch = HRUI 线)
  data/suppliers_drive/_listing_centec.tsv   + _imgs_centec.txt    (CENTEC Based High-Speed Network = Hohunet 线)
汇总成与 data/smartbyte_drive_index.json 同一 schema 的全量索引：
  data/suppliers_drive_index.json   {meta, 文件夹清单, files[文件名/文件类型/文件大小/所在子文件夹路径/内容摘要/_drive_id/_bytes/_摘要来源]}
规则沿用 T23：一个不漏、不复制原始文件、摘要 ≤50 字；
  _摘要来源 = 读取内容（代理用 read_file_text 读过正文/节选）/ 型号解码（按价格表规格或型号命名解码）/ 文件名推断（图片、视频、PPT 等未打开）。
用法：python3 scripts/suppliers_drive_index.py
"""
import json, os, re, sys, datetime
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'data', 'suppliers_drive')
OUT = os.path.join(ROOT, 'data', 'suppliers_drive_index.json')

REALTEK_ROOT = '17hEtGThaxugf-ngPfyNYYcuIzeEoT5p0'
CENTEC_ROOT = '1nKIZPptuYQhoUs0FbjyXYStrn2sl4iRU'

# ---------- 读取抄录 ----------
def read_listing(path):
    rows = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line or line.startswith('#'):
                continue
            p = line.split('\t')
            if len(p) < 6:
                p += [''] * (6 - len(p))
            rows.append(dict(id=p[0], name=p[1], mime=p[2], size=p[3], modified=p[4], parent=p[5]))
    return rows

def read_imgs(path):
    rows = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            p = line.split()
            rows.append(dict(id=p[0], name=p[1], mime='image', size=p[2], modified='', parent=p[3]))
    return rows

# ---------- 类型 / 大小 ----------
EXT_TYPE = {
    '.png': '图片', '.jpg': '图片', '.jpeg': '图片', '.gif': '图片', '.bmp': '图片', '.webp': '图片',
    '.docx': 'Word', '.doc': 'Word', '.pdf': 'PDF', '.pptx': 'PPT', '.ppt': 'PPT',
    '.xlsx': 'Excel', '.xls': 'Excel', '.mp4': '视频', '.mov': '视频', '.zip': '压缩包', '.rar': '压缩包',
}
def ftype(name):
    ext = os.path.splitext(name)[1].lower()
    return EXT_TYPE.get(ext, ext.lstrip('.').upper() or '未知')

def human(n):
    n = int(n or 0)
    for unit in ('B', 'KB', 'MB', 'GB'):
        if n < 1024 or unit == 'GB':
            return (f'{n} B' if unit == 'B' else f'{n:.1f} {unit}')
        n /= 1024.0

# ---------- 价格表（Drive PDF 已用 read_file_text 抄录到 text/） ----------
def load_price_specs():
    """返回 {型号: (规格短句, 价格USD)}，来自两份价格表抄录文本。"""
    specs = {}
    for fn in ('Price_List_Realtek_Based_Commercial_Switch.txt', 'Price_List_Commercial_Web_Managed_Switch.txt'):
        p = os.path.join(SRC, 'text', fn)
        if not os.path.exists(p):
            continue
        for line in open(p, encoding='utf-8'):
            m = re.match(r'^(STC-[0-9A-Z\-]+)\s+(.*?)\s+\$([0-9.]+)\s*$', line.strip())
            if m:
                specs[m.group(1)] = (m.group(2), m.group(3))
    return specs

def short_spec(spec):
    """把价格表的规格句压成 ≤30 字的端口描述。"""
    s = spec.split(' Remark:')[0]
    s = s.replace('10/100/1000M', 'GE').replace('Gigabit SFP', 'SFP').replace('10 Gigabit SFP', '10G SFP')
    s = s.replace(' Uplink', '↑').replace(' Downlink', '↓').replace('downward compatible', '向下兼容')
    s = s.replace('Rack compatible', '机架').replace('Desktop Type', '桌面').replace('AC input', 'AC')
    s = s.replace('Ethernet ports', '电口').replace('fiber ports', '光口').replace('fiber port', '光口')
    s = s.replace('PoE ports', 'PoE 口').replace('fan-less', '无风扇').replace('With fan', '带风扇')
    s = s.replace('Support ', '').replace('Without Ethernet port', '无电口').replace('Without optical port', '无光口')
    s = re.sub(r'\s+', ' ', s).strip(' ,')
    return s

def clip(s, n=50):
    s = re.sub(r'\s+', ' ', s).strip()
    return s if len(s) <= n else s[:n - 1] + '…'

# ---------- 摘要：已读文件（read_file_text，2026-10-21） ----------
READ_SUMMARY = {
    # Realtek 线
    '1fr-8I3Fycd1f1YG95aUy1Lk2TkvXthOp': 'Saga 版 Realtek 商用交换机价格表：46 款 STC 非管理/PoE/L2L3 管理型 USD EXW 价，15 天有效，保 1 年',
    '1MilMCyQFjGEdjJI_rv9V3UDJcdMk9o3C': 'Saga 版 Web 管理交换机价格表：15 款 STC-…W 2.5G/10G 光电及 PoE 型号 USD EXW 价，附光口速率备注',
    '1AR6-9NdSU_IcU33QqokLSKYfMqSaAvEB': 'STC-28GPM 数据表：8GE PoE+2SFP+Console，L2 管理，af/at，含特性/规格/包装/箱规',
    '1fb5GUURd89CKKAmEXND_LMJWxsp7Txht': 'Realtek 管理型交换机用户手册：装箱单、Console 115200、默认 IP 192.168.2.1 admin/admin、安装',
    '1UVusVTqOjuWO1-syRFFcOCDpY7fQvzez': 'Realtek 平台 CLI 手册：AAA/ACL/802.1X/DHCP Snooping/DAI/GVRP/IGMP 等命令参考（目录起）',
    # CENTEC 线
    '1t80mEw9GeKbNzGP8lSbqPnSh096xViAj': 'CENTEC 平台配置指南：系统/接口/VLAN/MLAG/RIP/OSPF/BGP/ISIS/PIM/ACL 等章节（目录起）',
}
# 仅凭文件名/目录推断（未打开）
NAME_SUMMARY = {
    '1iod829FajP6QxvYLgLoYJuc5euLQI-ht': 'Realtek 平台 Web 管理界面手册（图文，未逐页读取）',
    '1X59kS9cX6MfX1wW_NIdiH5YJZEbaCXIt': 'Realtek 非管理商用以太网交换机用户手册（与管理型手册同模板）',
    '1PMCpK-tavrlSnYXhSn0I5IYSttFmI-pV': 'Realtek 非管理商用 PoE 交换机用户手册（与管理型手册同模板）',
    '1Z2Eop1nL3mk4o-9GoCr5O3wBZrRS5j54': 'Web 管理交换机界面演示视频（MP4）',
    '1yYzY_xddsO6W8FiNYSYCR-NrBC5Vnf86': 'CENTEC 平台 CLI 命令手册（Word，未打开）',
    '1kT2CvZa4Sp_zDZ2z_bGpHuGvoX3-xuEj': 'CENTEC 平台 Web 管理界面手册（Word，未打开）',
    '1x1rW4v4_VG9lT5pkLpNFm7G5lS1Ih-4r': 'BigFlow 平台性能参数 PPT V2.1（表项/缓存/转发容量，未打开）',
    '1GGJ6OfSnXks0xDT0nLcaH4omz4Nnpgqm': 'PeakNetX 平台性能参数 PPT V3.1（未打开）',
    '1Det3utGaWwrSwDdplSiMU9K00HwRSl4e': 'SerdesX 平台性能参数 PPT V3.1（未打开）',
    '1QEzrYZIikoGBvlLyjmmFYfwlP-bnRfiy': 'VastLakes 平台性能参数 PPT V3.1（未打开）',
    '142eXf8XF4v-OwNU9bvMGsP3JunaA5UUx': 'STOS 软件功能清单 V2.4 PPT 版；PDF 同名件已节选入 docs/drive/Resource-Library',
    '1iCtxr_YsyAtC5XUpqSqM61gV70GlqOAD': 'XLite 系列安装/挂装方式说明 PPT（未打开）',
    '1eHfmY1khz85LvD2gF_wzms7ouA7E6FMr': 'STH 100G 系列产品介绍 PPT（未打开）',
    '1cb4fbt3dWQMXrMvF8e3B_y_3yJO0pSm7': 'STH 10G 系列产品介绍 PPT（read_file_text 不支持 pptx）',
    '131F1IJYCVo2MByJiufPP0xy2d90hruma': 'STH 2.5G 系列产品介绍 PPT（未打开）',
    '1iE4HUyl3tLAj7bSOOMTrQnrz22DzSVjt': 'STH 25G 系列产品介绍 PPT（未打开）',
    '1QqujI1BkJhsGXpzTOh41CZO7oKNdtfKw': 'STH 400G 系列产品介绍 PPT（未打开）',
    '1yfeAlyY_uRr-RWtai7gqxNSHAcqy0QSo': 'STH 5G 系列产品介绍 PPT（未打开）',
    '14cXs4W9nA2VbOI2vjHvdW7KBaGhjCvak': 'STH 800G 系列产品介绍 PPT（未打开）',
    '1CNlIf1ocrNNqh0W7jETRBC_ydSYgtQJr': 'XLite 轻量系列产品介绍 PPT（未打开）',
}

def main():
    specs = load_price_specs()
    groups = [
        ('Realtek', REALTEK_ROOT, 'Realtek Based Commercial Switch',
         read_listing(os.path.join(SRC, '_listing_realtek.tsv')), read_imgs(os.path.join(SRC, '_imgs_realtek.txt'))),
        ('CENTEC', CENTEC_ROOT, 'CENTEC Based High-Speed Network',
         read_listing(os.path.join(SRC, '_listing_centec.tsv')), read_imgs(os.path.join(SRC, '_imgs_centec.txt'))),
    ]
    files, folders = [], []
    seen = set()
    for key, root_id, root_name, listing, imgs in groups:
        name_of = {root_id: root_name}
        parent_of = {root_id: None}
        for r in listing:
            if r['id'] == root_id:
                continue
            name_of[r['id']] = r['name']
            parent_of[r['id']] = r['parent']
        def path_of(fid):
            parts = []
            cur = fid
            guard = 0
            while cur and cur in name_of and guard < 20:
                parts.append(name_of[cur]); cur = parent_of.get(cur); guard += 1
            return '/'.join(reversed(parts))
        folder_ids = [root_id] + [r['id'] for r in listing if r['mime'] == 'folder' and r['id'] != root_id]
        for fid in folder_ids:
            folders.append(path_of(fid))
        # 文件夹内图片计数（用于「产品图 n/N」）
        img_count = Counter(r['parent'] for r in imgs)
        img_rank = {}
        rank_counter = Counter()
        for r in sorted(imgs, key=lambda x: (x['parent'], x['name'])):
            rank_counter[r['parent']] += 1
            img_rank[r['id']] = rank_counter[r['parent']]
        for r in listing + imgs:
            if r['mime'] == 'folder' or r['id'] == root_id:
                continue
            if r['id'] in seen:
                continue
            seen.add(r['id'])
            name = r['name']
            t = ftype(name)
            folder_path = path_of(r['parent'])
            model = name_of.get(r['parent'], '')
            if r['id'] in READ_SUMMARY:
                summ, src = READ_SUMMARY[r['id']], '读取内容'
            elif r['id'] in NAME_SUMMARY:
                summ, src = NAME_SUMMARY[r['id']], '文件名推断'
            elif t == '图片':
                n = img_count.get(r['parent'], 0)
                summ, src = f'{model} 产品图 {img_rank.get(r["id"])}/{n}（外观/端口/细节，未逐张查看）', '文件名推断'
            elif t == 'Word' and name.startswith('STC-'):
                m = os.path.splitext(name)[0]
                if m in specs:
                    summ, src = f'{m} 数据表：{clip(short_spec(specs[m][0]), 42 - len(m) - len(specs[m][1]))}；${specs[m][1]}', '型号解码'
                else:
                    summ, src = f'{m} 数据表（同模板：简介/特性/规格/包装）', '型号解码'
            else:
                summ, src = f'{name}（{t}，未打开）', '文件名推断'
            files.append(OrderedDict([
                ('文件名', name), ('文件类型', t), ('文件大小', human(r['size'])),
                ('所在子文件夹路径', folder_path), ('内容摘要', clip(summ)),
                ('_drive_id', r['id']), ('_bytes', int(r['size'] or 0)), ('_摘要来源', src),
                ('_供应商线', 'HRUI（Realtek 芯片）' if key == 'Realtek' else 'Hohunet（CENTEC 芯片）'),
            ]))
    files.sort(key=lambda f: (f['所在子文件夹路径'], f['文件名']))
    folders = sorted(set(folders))
    total = sum(f['_bytes'] for f in files)
    by_type = Counter(f['文件类型'] for f in files)
    by_src = Counter(f['_摘要来源'] for f in files)
    by_line = Counter(f['_供应商线'] for f in files)
    meta = OrderedDict([
        ('来源', 'Google Drive 文件夹《Realtek Based Commercial Switch》(id %s) 与《CENTEC Based High-Speed Network》(id %s)，Simon 于 2026-10-20 上传；对应供应商 HRUI（hruitech.com，Realtek 芯片）与 Hohunet（hohunet.com，CENTEC 芯片）' % (REALTEK_ROOT, CENTEC_ROOT)),
        ('生成时间UTC', datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')),
        ('生成方式', 'google_drive.list_files 按父文件夹逐页抄录（Realtek：根+4 类目+46 型号夹；CENTEC：根+8 系列夹+42 型号夹）→ scripts/suppliers_drive_index.py 汇总；价格表 PDF/手册/数据表样本用 read_file_text 读取；未复制任何原始文件'),
        ('文件总数', len(files)),
        ('文件夹总数', len(folders)),
        ('总大小', human(total)),
        ('总字节', total),
        ('按供应商线', dict(by_line)),
        ('按类型', dict(by_type.most_common())),
        ('摘要来源统计', dict(by_src)),
        ('字段说明', OrderedDict([
            ('文件名', 'Drive 中的文件名'),
            ('文件类型', '按扩展名归类：图片/Word/PDF/PPT/视频'),
            ('文件大小', '人类可读（源字节数见 _bytes）'),
            ('所在子文件夹路径', '从 Drive 共享根文件夹名起的完整路径'),
            ('内容摘要', '≤50 字；_摘要来源 = 读取内容 / 型号解码（STC 数据表按价格表规格解码）/ 文件名推断（图片、PPT、视频未打开）'),
            ('_供应商线', 'HRUI（Realtek 芯片）= STC 商用系列；Hohunet（CENTEC 芯片）= STH 高速系列'),
        ])),
        ('注意', 'read_file_text 不支持 pptx，9 份 STH 系列 PPT、4 份平台性能 PPT、功能清单 PPT 均只按文件名推断；STC 数据表 docx 规格表为图片，摘要取自同名价格表行；图片未逐张打开。'),
    ])
    out = OrderedDict([('meta', meta), ('文件夹清单', folders), ('files', files)])
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f'files={len(files)} folders={len(folders)} total={human(total)} by_line={dict(by_line)} by_type={dict(by_type)} by_src={dict(by_src)}')
    bad = [f for f in files if len(f['内容摘要']) > 50]
    print('摘要>50字:', len(bad))
    write_price_csv()


def write_price_csv():
    """把两份 Drive 价格表抄录文本整理成 data/hrui_realtek_价格表_Drive2026Q3.csv（Saga 对外 USD EXW 价）。"""
    import csv
    rows = []
    for fn, src in (('Price_List_Realtek_Based_Commercial_Switch.txt', 'Price List_Realtek Based Commercial Switch.pdf'),
                    ('Price_List_Commercial_Web_Managed_Switch.txt', 'Price List_Commercial Web Managed Switch.pdf')):
        p = os.path.join(SRC, 'text', fn)
        if not os.path.exists(p):
            continue
        cat = ''
        for line in open(p, encoding='utf-8'):
            t = line.strip()
            if t.startswith('Commercial ') and '$' not in t:
                cat = t
                continue
            m = re.match(r'^(STC-[0-9A-Z\-]+)\s+(.*?)\s+\$([0-9.]+)\s*$', t)
            if m:
                spec = m.group(2)
                remark = ''
                if ' Remark:' in spec:
                    spec, remark = spec.split(' Remark:', 1)
                rows.append(OrderedDict([
                    ('Saga型号', m.group(1)), ('类别', cat), ('规格', spec.strip()), ('备注', remark.strip()),
                    ('Saga对外价USD_EXW', m.group(3)), ('价格表来源', src), ('供应商线', 'HRUI（Realtek 芯片）'),
                    ('价格条款', '15 天有效 / EXW / 保修 1 年 / <50 台交期 5~7 工作日 / 可定制'),
                ]))
    outp = os.path.join(ROOT, 'data', 'hrui_realtek_价格表_Drive2026Q3.csv')
    with open(outp, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator='\r\n')
        w.writeheader(); w.writerows(rows)
    print(f'price csv rows={len(rows)} -> {os.path.relpath(outp, ROOT)}')

if __name__ == '__main__':
    main()
