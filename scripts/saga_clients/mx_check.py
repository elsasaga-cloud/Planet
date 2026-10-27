#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T29-U64 · 第 82 批 · 邮箱域体检：A/B 全部域名查 MX / A 记录 → 邮件托管在谁那、域名死没死。

只做 DNS 查询（沙箱放行），不做 SMTP 探测。结果写 data/saga_clients/mx_check_<date>.json：
  {"_meta": {...}, "domains": {domain: {"mx": [[pref, host], ...], "a": [...], "status": "ok|no_mx|dead|nxdomain",
                                        "cls": "Microsoft 365|Google Workspace|...", "checked": iso-date}},
   "households": {code: [domain, ...]}}
用法：python3 mx_check.py [--grades AB] [--workers 16] [--only-missing]
再跑只补新域名（--only-missing），全量重跑把 --only-missing 去掉。
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import sys

import dns.resolver  # pip install dnspython
import dns.reversename

from common import DATA

TODAY = dt.date.today().isoformat()
PUBLIC_SUFFIX = set('uk.com us.com eu.com de.com cn.com br.com ru.com sa.com se.com uy.com za.com gb.com gb.net hu.com jpn.com kr.com no.com qc.com ae.org co.uk org.uk me.uk ltd.uk com.tr net.tr org.tr com.au net.au co.in net.in org.in com.br co.za com.pl com.vn co.kr or.kr com.my com.sg co.id com.ph com.pk co.th com.ua in.ua co.il com.sa com.mx com.ar com.co com.pe co.nz com.hk com.tw com.cn com.eg com.ng co.ke com.gh com.bd com.np com.kz com.uz com.ge com.lb com.jo com.kw com.qa com.bh com.om'.split())
OUT = os.path.join(DATA, f'mx_check_{TODAY}.json')

# MX 主机 → 服务商分类（顺序即优先级；企业网关排前面，因为网关后面才是 M365/Google）
CLS = [
    (r'pphosted\.com|ppe-hosted\.com|proofpoint', 'Proofpoint 企业网关'),
    (r'mailchannels\.net', 'MailChannels 过滤（主机商附带）'),
    (r'messagingengine\.com|fastmail', 'Fastmail'),
    (r'beget\.com|timeweb\.ru|masterhost\.ru|reg\.ru|hoster\.ru|nic\.ru|sprinthost|majordomo\.ru|ihc\.ru|spaceweb|rusonyx|jino\.ru', '俄罗斯主机商邮箱'),
    (r'uzmanposta|kurumsaleposta|alastyr|turkticaret|natro|turhost|isimtescil|radore|veridyen|guzel\.net|hosting\.com\.tr|isimkayit|dgn\.net\.tr|markum|vargonen|sadecehosting|hostixo|turkiyehost|yandex\.com\.tr', '土耳其主机商邮箱'),
    (r'daum\.net|kakao', 'Kakao / Daum 企业邮箱'),
    (r'dooray\.com|nhn', 'NHN Dooray 企业邮箱（韩国）'),
    (r'bizmail|hanmail|hiworks|gabia|cafe24', '韩国主机商 / 企业邮箱'),
    (r'ecounterp\.com', 'ecount ERP 邮箱（韩国）'),
    (r'stackmail\.com|20i\.com|krystal|fasthosts|names\.co\.uk|123-reg|heartinternet|tsohost|lcn\.com|ukfast|names\.co', '英国主机商邮箱'),
    (r'mailcluster\.com\.au|ventraip|crazydomains|netregistry|digitalpacific|zuver|synergywholesale', '澳洲主机商邮箱'),
    (r'emirates\.net\.ae|etisalat|eim\.ae|du\.ae', 'Etisalat / du 邮箱（阿联酋）'),
    (r'emailme\.com|mailhostbox|webhostbox', '印度 / 亚洲主机商邮箱'),
    (r'mimecast', 'Mimecast 企业网关'),
    (r'barracudanetworks|barracuda', 'Barracuda 网关'),
    (r'messagelabs|symanteccloud|broadcom', 'Broadcom/MessageLabs 网关'),
    (r'trendmicro|tmes\.', 'Trend Micro 网关'),
    (r'sophos', 'Sophos 网关'),
    (r'cisco\.com|iphmx\.com|ironport', 'Cisco Secure Email 网关'),
    (r'fortimail|fortinet', 'FortiMail 网关'),
    (r'hornetsecurity|antispameurope', 'Hornetsecurity 网关'),
    (r'spamexperts|antispamcloud|mailprotect', 'SpamExperts 网关（主机商附带）'),
    (r'mail\.protection\.outlook\.com|outlook\.com|hotmail', 'Microsoft 365'),
    (r'aspmx\.l\.google\.com|googlemail\.com|google\.com', 'Google Workspace'),
    (r'zoho', 'Zoho Mail'),
    (r'yandex', 'Yandex 360'),
    (r'mail\.ru|mailru|vk\.com', 'Mail.ru（VK WorkMail）'),
    (r'secureserver\.net', 'GoDaddy 邮箱'),
    (r'ionos|1and1|kundenserver|perfora', 'IONOS 主机邮箱'),
    (r'ovh\.net|ovh\.com|mail\.ovh', 'OVH 主机邮箱'),
    (r'titan\.email|hostinger', 'Hostinger / Titan'),
    (r'yahoodns|yahoo', 'Yahoo 小企业邮箱'),
    (r'icloud\.com|apple\.com', 'iCloud+ 自定义域'),
    (r'proton', 'Proton Mail'),
    (r'emailsrvr\.com|rackspace', 'Rackspace 邮箱'),
    (r'hostgator|websitewelcome|bluehost|hostmonster|justhost', 'HostGator / Bluehost 主机邮箱'),
    (r'mailgun|sendgrid|amazonses|awsapps|inbound-smtp.*amazonaws', 'AWS / Mailgun 类'),
    (r'register\.it|aruba\.it|arubabusiness|serverplan|keliweb', '意大利主机商邮箱（Aruba/Register.it）'),
    (r'strato\.de|rzone\.de|hosteurope|all-inkl|kasserver|df\.eu|domainfactory|hetzner|netcup|goneo|mailbox\.org|posteo|united-domains|udag', '德国主机商邮箱'),
    (r'home\.pl|nazwa\.pl|cyberfolks|ogicom|az\.pl|kei\.pl|hostinger\.pl|smarthost\.pl|linuxpl|dhosting', '波兰主机商邮箱'),
    (r'wedos|forpsi|active24|savana|websupport', '捷克 / 斯洛伐克主机商邮箱'),
    (r'natro|turhost|isimtescil|radore|veridyen|guzel\.net|hosting\.com\.tr|turkticaret|isimkayit|dgn\.net\.tr|markum|vargonen|sadecehosting|hostixo|turkiyehost', '土耳其主机商邮箱'),
    (r'bigrock|hostgator\.in|net4\.in|godaddy|bluehost\.in|milesweb|hostingraja|znetlive|ewebguru', '印度主机商邮箱'),
    (r'one\.com|simply\.com|loopia|binero|surftown|dandomain', '北欧主机商邮箱'),
    (r'xserver|sakura|lolipop|onamae', '日本主机商邮箱'),
    (r'gabia|cafe24|whois\.co\.kr|hiworks|daouoffice|naver|worksmobile', '韩国主机商 / Naver Works'),
    (r'hinet\.net|seed\.net|pchome|gandi', '台湾 / Gandi 主机邮箱'),
    (r'qq\.com|exmail\.qq|aliyun|mxhichina|163\.com|netease|feishu|larksuite|coremail|21cn|sina', '中国邮箱（腾讯企业 / 阿里 / 网易）'),
    (r'kundenserver|webhostbox|cpanel|mailspamprotection|hostedemail|mail\d*\.[a-z0-9-]+\.(?:net|com|org)$', '主机商 cPanel 类邮箱'),
]


def classify(domain, mx):
    if not mx:
        return ''
    hosts = [h.lower() for _, h in mx]
    joined = ' '.join(hosts)
    for pat, name in CLS:
        if re.search(pat, joined):
            return name
    base = '.'.join(domain.lower().split('.')[-2:])
    if all(h.endswith(base) for h in hosts):
        return '自建 / 同域名邮件服务器'
    return '其他主机商邮箱（' + hosts[0] + '）'


def ptr_of(host, resolver):
    """MX 主机 → IP → PTR（反解），用来区分「真自建」与「同域名别名指向主机商」。"""
    try:
        ip = str(resolver.resolve(host, 'A')[0])
        rev = dns.reversename.from_address(ip)
        ptr = str(resolver.resolve(rev, 'PTR')[0]).rstrip('.')
        return ip, ptr
    except Exception:
        return '', ''


def lookup(domain, resolver):
    rec = {'mx': [], 'a': [], 'status': 'ok', 'cls': '', 'checked': TODAY}
    try:
        ans = resolver.resolve(domain, 'MX')
        rec['mx'] = sorted([[int(x.preference), str(x.exchange).rstrip('.')] for x in ans])[:4]
    except dns.resolver.NXDOMAIN:
        rec['status'] = 'nxdomain'
        return rec
    except (dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        rec['status'] = 'no_mx'
    except Exception as e:  # timeout etc.
        rec['status'] = 'error:' + type(e).__name__
    try:
        rec['a'] = [str(x) for x in resolver.resolve(domain, 'A')][:3]
    except Exception:
        pass
    if rec['status'] == 'no_mx' and not rec['a']:
        rec['status'] = 'dead'
    # 「.」空 MX（RFC 7505）= 明确不收信
    if rec['mx'] and rec['mx'][0][1] in ('', '.'):
        rec['status'] = 'null_mx'
        rec['mx'] = []
    rec['cls'] = classify(domain, rec['mx'])
    if rec['cls'].startswith('自建'):
        ip, ptr = ptr_of(rec['mx'][0][1], resolver)
        rec['mx_ip'], rec['mx_ptr'] = ip, ptr
        base = '.'.join(domain.lower().split('.')[-2:])
        if ptr and not ptr.endswith(base):
            rec['cls'] = '同域名 MX → 托管在 ' + '.'.join(ptr.split('.')[-2:])
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--grades', default='AB')
    ap.add_argument('--workers', type=int, default=16)
    ap.add_argument('--only-missing', action='store_true')
    a = ap.parse_args()
    ents = json.load(open(os.path.join(DATA, 'entities.json'), encoding='utf-8'))
    ents = ents if isinstance(ents, list) else list(ents.values())
    hh, doms = {}, set()
    for e in ents:
        if e.get('grade') not in set(a.grades):
            continue
        ds = [d.lower().strip() for d in (e.get('domains') or []) if d and '.' in d]
        # 邮箱地址所在的域才是真正要发信的域（如 andys@case.uk.com 的 case.uk.com），一并查；
        # 纯公共后缀（uk.com / com.tr / co.uk …）是解析残片，跳过
        for em in (e.get('emails') or []):
            if '@' in em:
                ds.append(em.split('@')[-1].lower().strip())
        ds = [d for d in dict.fromkeys(ds) if d not in PUBLIC_SUFFIX]
        if ds:
            hh[e['code']] = ds
            doms.update(ds)
    old = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {'domains': {}}
    todo = sorted(d for d in doms if not (a.only_missing and d in old['domains']))
    res = dict(old.get('domains') or {})
    resolver = dns.resolver.Resolver()
    resolver.timeout = 3
    resolver.lifetime = 6
    print(f'households {len(hh)} domains {len(doms)} todo {len(todo)}', flush=True)
    done = 0
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(lookup, d, resolver): d for d in todo}
        for f in cf.as_completed(futs):
            d = futs[f]
            try:
                res[d] = f.result()
            except Exception as e:
                res[d] = {'mx': [], 'a': [], 'status': 'error:' + type(e).__name__, 'cls': '', 'checked': TODAY}
            done += 1
            if done % 100 == 0:
                print(done, flush=True)
                json.dump({'_meta': {'checked': TODAY, 'note': 'partial'}, 'domains': res, 'households': hh},
                          open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    from collections import Counter
    st = Counter(v['status'] for v in res.values())
    cl = Counter(v['cls'] for v in res.values() if v['cls'])
    meta = {'checked': TODAY, 'source': 'DNS MX/A 查询（dnspython，沙箱解析器）', 'grades': a.grades,
            'domains': len(res), 'households': len(hh), 'status_counts': dict(st), 'class_counts': dict(cl.most_common())}
    json.dump({'_meta': meta, 'domains': res, 'households': hh}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(json.dumps(meta, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
