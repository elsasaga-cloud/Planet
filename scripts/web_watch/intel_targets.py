#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A 类「挖个底掉」长期 watch 源生成（T29-U139 2026-10-30，Simon：要建 workflow 定期爬、看是否更新，长期 watch——这是长期资产）。

离线、幂等。输出 scripts/web_watch/targets_intel.json，由 watch.py 在 Actions 日跑里与 targets.json / targets_auto.json 合并：
  intel_news_en / intel_news_<lang>   Google News RSS（公司名精确短语；本地语种版按国家）        → 新闻/招标、人事变动（任免新闻）
  intel_edgar                          SEC EDGAR 全部申报 Atom（美国上市：10-K / 10-Q / 8-K）         → 年报/财务、人事变动
  intel_ch_filings                     英国 Companies House filing history（有公司号的英国户）       → 年报/财务（账目 / 任免 / 地址变更）
  intel_ir_<n>                         上市公司 IR / 年报列表页（html）                              → 年报/财务
  intel_github_<org>                   intel 里已确认的 GitHub 组织（kind github）                    → GitHub/技术足迹
  intel_careers                        官网快照里发现的招聘页（html）                                 → 人事变动
新条目由 scripts/saga_clients/intel/ingest_watch.py 在每轮会话里转成研究档 intel 条目（人工看一眼再入库）。
"""
import glob
import json
import os
import re
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SD = os.path.join(ROOT, 'data', 'saga_clients')
OUT = os.path.join(HERE, 'targets_intel.json')

LANG = {'TR': ('tr', 'TR', 'TR:tr'), 'DE': ('de', 'DE', 'DE:de'), 'AT': ('de', 'AT', 'AT:de'), 'CH': ('de', 'CH', 'CH:de'), 'IT': ('it', 'IT', 'IT:it'), 'ES': ('es', 'ES', 'ES:es'),
        'FR': ('fr', 'FR', 'FR:fr'), 'PL': ('pl', 'PL', 'PL:pl'), 'RU': ('ru', 'RU', 'RU:ru'), 'KZ': ('ru', 'RU', 'RU:ru'), 'BY': ('ru', 'RU', 'RU:ru'), 'UZ': ('ru', 'RU', 'RU:ru'), 'PT': ('pt-PT', 'PT', 'PT:pt-150'),
        'BR': ('pt-BR', 'BR', 'BR:pt-419'), 'NL': ('nl', 'NL', 'NL:nl'), 'BE': ('nl', 'BE', 'BE:nl'), 'RO': ('ro', 'RO', 'RO:ro'), 'HU': ('hu', 'HU', 'HU:hu'), 'CZ': ('cs', 'CZ', 'CZ:cs'), 'GR': ('el', 'GR', 'GR:el'),
        'MX': ('es-419', 'MX', 'MX:es-419'), 'AR': ('es-419', 'AR', 'AR:es-419'), 'CO': ('es-419', 'CO', 'CO:es-419'), 'EC': ('es-419', 'EC', 'EC:es-419'), 'KR': ('ko', 'KR', 'KR:ko'), 'JP': ('ja', 'JP', 'JP:ja'),
        'VN': ('vi', 'VN', 'VN:vi'), 'ID': ('id', 'ID', 'ID:id'), 'TH': ('th', 'TH', 'TH:th'), 'UA': ('uk', 'UA', 'UA:uk'), 'BG': ('bg', 'BG', 'BG:bg'), 'RS': ('sr', 'RS', 'RS:sr'), 'LV': ('lv', 'LV', 'LV:lv'), 'SK': ('sk', 'SK', 'SK:sk'), 'HR': ('hr', 'HR', 'HR:hr'), 'SE': ('sv', 'SE', 'SE:sv'), 'FI': ('fi', 'FI', 'FI:fi'), 'DK': ('da', 'DK', 'DK:da'), 'NO': ('no', 'NO', 'NO:no')}
GENERIC = {'security', 'systems', 'system', 'technology', 'technologies', 'solutions', 'solution', 'networks', 'network', 'group', 'international', 'limited', 'ltd', 'llc', 'inc', 'company', 'co', 'services', 'service', 'sistemleri', 'teknoloji', 'elektronik', 'güvenlik', 'guvenlik', 'bilişim', 'bilisim', 'communications', 'engineering', 'electronics', 'computer', 'wireless', 'industries', 'trading', 'srl', 'gmbh', 'sas', 'bv', 'spa', 'sa', 'as', 'ltda', 'pvt', 'private', 'corporation', 'corp', 'media', 'global', 'digital', 'tech'}
FREE = re.compile(r'^(gmail|hotmail|yahoo|outlook|live|icloud|mail|yandex|protonmail|aol|gmx|web|list|bk|inbox|rambler|163|qq|126|telus)\.', re.I)
# 人工补：上市 / 申报源（code → sources）
MANUAL = {
    'SB-831': [  # Actelis Networks (NASDAQ: ASNS) CIK 0001141284
        {'id': 'intel_edgar', 'kind': 'rss', 'url': 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001141284&type=&dateb=&owner=include&count=40&output=atom', 'note': 'SEC EDGAR 全部申报 Atom（10-K / 10-Q / 8-K；8-K = 任免 / 大单 / 融资）'},
        {'id': 'intel_ir_filings', 'kind': 'html', 'url': 'https://ir.actelis.com/sec-filings/all-sec-filings', 'note': 'IR 申报列表页'},
    ],
    'SA-086': [  # Netaş (BIST: NETAS)
        {'id': 'intel_ir_reports', 'kind': 'html', 'url': 'https://netas.com.tr/tr/yatirimci-iliskileri/faaliyet-raporlari', 'note': '年报列表页（新年报 PDF 出现在此；URL 以快照为准，失败则改 IR 首页）'},
        {'id': 'intel_ir_home', 'kind': 'html', 'url': 'https://netas.com.tr/tr/yatirimci-iliskileri', 'note': '投资者关系首页（KAP 公告摘要 / 财报日历）'},
    ],
}


def load_json(p, d=None):
    try:
        return json.load(open(p, encoding='utf-8'))
    except Exception:
        return d


def news_name(e, rs):
    """给 Google News 用的公司短语：优先研究档法定名的主干，再退回实体名；个人 / 免费邮箱 / 太泛的名字不生成。"""
    cands = []
    for x in (rs.get('name_official') or '', (rs.get('company_facts') or {}).get('legal_name') or '', e.get('name') or ''):
        x = re.split(r'[（(｜|/／;；]', str(x))[0].strip()
        x = re.sub(r'\b(S\.?A\.?S?|S\.?r\.?l\.?|GmbH|Ltd\.?|LLC|Inc\.?|A\.?Ş\.?|Ltd\.? ?Şti\.?|San\.? ve Tic\.?|Pvt\.? Ltd\.?|Limited|Corporation|Corp\.?|B\.?V\.?|S\.?p\.?A\.?|d\.o\.o\.|Kft\.?|Sp\. z o\.o\.|OÜ|Oy|AB|AS|SIA|UAB)\b\.?', '', x, flags=re.I).strip(' ,.-')
        if x and not re.search(r'@|未具名|公司名|没查到|客户|联系人', x) and not re.match(r'^[\w.-]+\.[a-z]{2,}$', x, re.I):
            cands.append(x)
    for x in cands:
        toks = [t for t in re.findall(r'[\w\u00C0-\u024F\u0400-\u04FF]+', x) if t.lower() not in GENERIC]
        if len(x) >= 5 and toks and (len(toks) >= 2 or len(toks[0]) >= 6):
            return x[:60]
    return ''


def main():
    ents = {e['code']: e for e in load_json(os.path.join(SD, 'entities.json'), [])}
    digest = load_json(os.path.join(SD, 'site_digest.json'), {}) or {}
    registry = {}
    for f in glob.glob(os.path.join(SD, 'registry', '*.json')):
        for c, v in (load_json(f, {}) or {}).get('rows', {}).items():
            registry.setdefault(c, v)
    customers = []
    st = {'news_en': 0, 'news_local': 0, 'edgar': 0, 'ch': 0, 'ir': 0, 'github': 0, 'careers': 0, 'skipped_news': 0}
    for c, e in sorted(ents.items()):
        rs = e.get('research') or {}
        dug = any(str(x.get('batch', '')).startswith('INTEL') and x.get('found') for x in ((rs.get('intel') or {}).get('items') or []))
        if e.get('grade') != 'A' and not (e.get('grade') == 'B' and dug):
            continue  # A 户全部 + 挖过情报后下放 B 的户（如 Actelis EDGAR）继续 watch
        srcs = []
        nm = news_name(e, rs)
        if nm:
            q = urllib.parse.quote(f'"{nm}"')
            srcs.append({'id': 'intel_news_en', 'kind': 'rss', 'url': f'https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en', 'note': f'Google News 英文：「{nm}」（精确短语；同名误报看标题再用）'})
            st['news_en'] += 1
            iso = e.get('iso') or ''
            if iso in LANG:
                hl, gl, ceid = LANG[iso]
                srcs.append({'id': f'intel_news_{hl.split("-")[0]}', 'kind': 'rss', 'url': f'https://news.google.com/rss/search?q={q}&hl={hl}&gl={gl}&ceid={ceid}', 'note': f'Google News 本地语种（{iso}）：「{nm}」'})
                st['news_local'] += 1
        else:
            st['skipped_news'] += 1
        reg = registry.get(c) or {}
        if (reg.get('source') or '').startswith('UK Companies House') and re.match(r'^[0-9A-Z]{8}$', str(reg.get('number') or '')):
            srcs.append({'id': 'intel_ch_filings', 'kind': 'html', 'url': f"https://find-and-update.company-information.service.gov.uk/company/{reg['number']}/filing-history", 'note': f"Companies House 申报历史（{reg.get('name', '')} {reg['number']}）：新账目 / 任免 / 地址变更"})
            st['ch'] += 1
        for s in MANUAL.get(c, []):
            if any(x['id'] == s['id'] for x in srcs):
                continue
            srcs.append(dict(s))
            st['edgar' if 'edgar' in s['id'] else 'ir'] += 1
        for x in ((rs.get('intel') or {}).get('items') or []):
            if x.get('kind') == 'GitHub/技术足迹' and x.get('found') and x.get('url', '').startswith('https://github.com/') and '组织' in x.get('quote', ''):
                login = x['url'].rstrip('/').split('/')[-1]
                srcs.append({'id': f'intel_github_{login}', 'kind': 'github', 'login': login, 'note': 'intel 已确认的 GitHub 组织（新仓库 / 推送）'})
                st['github'] += 1
        dg = digest.get(c) or {}
        for sp in (dg.get('subpages') or [])[:40]:
            u = sp.get('url') if isinstance(sp, dict) else str(sp)
            if u and re.search(r'career|kariyer|jobs?\b|join-us|vacanc|insan-kaynaklari|stellen|lavora-con-noi|empleo|recrut', u, re.I):
                srcs.append({'id': 'intel_careers', 'kind': 'html', 'url': u, 'note': '官网招聘页（人事变动 / 扩张信号）'})
                st['careers'] += 1
                break
        if srcs:
            customers.append({'code': c, 'name': e.get('name'), 'grade': e.get('grade'), 'country': e.get('country'), 'layer': 'A' if e.get('grade') == 'A' else 'B', 'sources': srcs})
    cfg = {'_comment': 'A 类挖底 watch 源（intel_targets.py 离线生成，幂等；与 targets.json / targets_auto.json 合并，源 id 以 intel_ 开头）', 'generated': '2026-10-30', 'stats': st, 'customers': customers}
    json.dump(cfg, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('targets_intel: customers', len(customers), st)


if __name__ == '__main__':
    main()
