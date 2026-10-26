# -*- coding: utf-8 -*-
"""Saga Clients 共用：路径、国家表、文件语义标签、文本解析。"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, 'data', 'saga_clients')
OUT_DIR = os.path.join(ROOT, 'Saga Clients')
RESEARCH_DIR = os.path.join(DATA, 'research')

# 目录分桶（T29-U60，2026-10-26）：GitHub 网页一个目录只显示前 1,000 个文件，B/C 超过 → 每 500 户一个子目录
# `Saga Clients/B/SB-0001-0500/`、`SB-0501-1000/`、`SB-1001-1500/` …（四位补零让目录按数字排序）；A 只有几十户，平铺。
BUCKET = 500
BUCKETED = ('B', 'C')


def sub_dir(code, grade):
    """某客户 MD 所在的子目录名（'' = 直接在等级目录下）。"""
    if grade not in BUCKETED:
        return ''
    n = int(code.split('-')[1])
    lo = (n - 1) // BUCKET * BUCKET + 1
    return f'S{grade}-{lo:04d}-{lo + BUCKET - 1:04d}'


def md_files(grade):
    """遍历等级目录（含子目录）下的全部客户 MD → [(文件名, 完整路径)]，不含 `_` 开头的索引/总览。"""
    out = []
    base = os.path.join(OUT_DIR, grade)
    if not os.path.isdir(base):
        return out
    for dp, dns, fns in os.walk(base):
        dns.sort()
        for fn in sorted(fns):
            if fn.endswith('.md') and not fn.startswith('_'):
                out.append((fn, os.path.join(dp, fn)))
    return out

FREEMAIL = {
    'poczta.fm', 'poczta.onet.pl', 'op.pl', 'vp.pl', 'tlen.pl', 'spoko.pl', 'autograf.pl', 'go2.pl', 'buziaczek.pl', 'neostrada.pl', 'gazeta.pl', 'interia.eu', 'onet.eu',
    'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'live.com', 'icloud.com', 'aol.com', 'msn.com', 'yandex.ru',
    'yandex.com', 'mail.ru', 'bk.ru', 'list.ru', 'inbox.ru', 'rambler.ru', 'ya.ru', 'naver.com', 'daum.net', 'hanmail.net',
    'qq.com', '163.com', '126.com', 'foxmail.com', 'protonmail.com', 'proton.me', 'gmx.de', 'gmx.net', 'web.de', 't-online.de',
    'yahoo.co.uk', 'yahoo.fr', 'yahoo.com.br', 'yahoo.co.in', 'yahoo.es', 'yahoo.it', 'yahoo.de', 'hotmail.co.uk', 'hotmail.fr',
    'hotmail.it', 'hotmail.es', 'hotmail.de', 'live.co.uk', 'live.fr', 'outlook.es', 'outlook.de', 'outlook.fr', 'rediffmail.com',
    'ymail.com', 'me.com', 'mac.com', 'yahoo.com.tw', 'yahoo.com.au', 'yahoo.ca', 'yahoo.com.mx', 'yahoo.com.ar', 'wp.pl', 'o2.pl',
    'onet.pl', 'interia.pl', 'seznam.cz', 'email.cz', 'centrum.cz', 'abv.bg', 'mail.bg', 'ukr.net', 'i.ua', 'bigpond.com',
    'optusnet.com.au', 'sbcglobal.net', 'comcast.net', 'verizon.net', 'att.net', 'bellsouth.net', 'cox.net', 'zoho.com',
    'hotmail.com.br', 'bol.com.br', 'uol.com.br', 'terra.com.br', 'ig.com.br', 'globo.com', 'yahoo.co.jp', 'nate.com',
    'libero.it', 'virgilio.it', 'tiscali.it', 'alice.it', 'tin.it', 'orange.fr', 'wanadoo.fr', 'free.fr', 'laposte.net', 'sfr.fr',
    'telenet.be', 'skynet.be', 'ziggo.nl', 'kpnmail.nl', 'planet.nl', 'hetnet.nl', 'xs4all.nl', 'bluewin.ch', 'eircom.net',
    'btinternet.com', 'sky.com', 'talktalk.net', 'virginmedia.com', 'ntlworld.com', 'rogers.com', 'shaw.ca', 'telus.net',
    'sympatico.ca', 'videotron.ca', 'mweb.co.za', 'telkomsa.net', 'vodamail.co.za', 'emirates.net.ae', 'eim.ae', 'live.com.au',
    'yahoo.com.sg', 'singnet.com.sg', 'yahoo.com.hk', 'netvigator.com', 'yahoo.com.vn', 'hotmail.co.th', 'yahoo.co.th',
    'yahoo.co.id', 'yahoo.com.ph', 'yahoo.com.my', 'hotmail.co.id', 'pm.me', 'tutanota.com', 'mail.com', 'email.com', 'usa.com',
    'post.com', 'inbox.lv', 'mail.ee', 'walla.co.il', 'walla.com', 'bezeqint.net', 'netvision.net.il', 'yahoo.gr', 'otenet.gr',
    'hotmail.gr', 'sapo.pt', 'netcabo.pt', 'telia.com', 'hotmail.se', 'online.no', 'live.se', 'live.dk', 'live.nl', 'live.it',
    'live.de', 'live.ca', 'live.in', 'hotmail.ca', 'yahoo.in', 'ymail.in', 'mail.ee', 'qq.cn', 'sina.com', 'sohu.com', 'yeah.net',
}
TWO_LEVEL_TLD = {
    'co.uk', 'org.uk', 'ac.uk', 'gov.uk', 'me.uk', 'com.br', 'com.tr', 'com.au', 'net.au', 'org.au', 'co.za', 'co.kr', 'or.kr', 'ne.kr',
    'co.jp', 'ne.jp', 'or.jp', 'co.in', 'net.in', 'org.in', 'co.th', 'or.th', 'com.sa', 'com.vn', 'net.vn', 'com.my', 'com.ar',
    'com.mx', 'com.co', 'com.pe', 'com.ec', 'com.bo', 'com.py', 'com.uy', 'com.ve', 'com.gt', 'com.sv', 'com.do', 'com.pa', 'com.ph',
    'com.sg', 'com.hk', 'com.tw', 'com.cn', 'net.cn', 'org.cn', 'com.pk', 'com.bd', 'com.np', 'com.lk', 'com.eg', 'com.ng', 'co.ke',
    'co.tz', 'co.ug', 'co.zw', 'co.zm', 'com.gh', 'co.il', 'org.il', 'com.lb', 'com.jo', 'com.kw', 'com.qa', 'com.om', 'com.bh',
    'com.ua', 'net.ua', 'org.ua', 'kiev.ua', 'kyiv.ua', 'kh.ua', 'dp.ua', 'od.ua', 'lviv.ua', 'zp.ua', 'dn.ua', 'in.ua', 'com.pl', 'com.ru', 'com.ge', 'com.kz', 'com.uz', 'com.by', 'com.mt', 'com.cy', 'com.gr', 'com.pt', 'com.es', 'com.ni',
    'com.hn', 'com.cu', 'com.jm', 'com.tt', 'co.nz', 'net.nz', 'org.nz', 'co.id', 'or.id', 'web.id', 'com.kh', 'com.mm', 'com.bn',
    'com.mv', 'com.af', 'com.iq', 'com.sy', 'com.ly', 'com.tn', 'com.dz', 'co.ma', 'com.et', 'com.sd', 'com.mz', 'co.ao', 'co.mz',
    'com.ba', 'com.mk', 'com.al', 'com.au', 'co.ir', 'com.az', 'com.am', 'com.md', 'com.ee', 'com.lv', 'com.lt', 'com.hr', 'com.rs',
    'co.rs', 'com.si', 'com.ro', 'com.bg', 'com.sk', 'com.cz', 'com.hu', 'com.de', 'com.fr', 'com.it', 'com.nl', 'com.be', 'com.ch',
    'com.at', 'com.se', 'com.no', 'com.dk', 'com.fi', 'com.ie', 'com.is', 'com.lu',
}

GENERIC_SLD = {'com', 'net', 'org', 'co', 'gov', 'edu', 'ac', 'or', 'ne', 'go', 'mil', 'biz', 'info', 'web', 'firm', 'gen', 'ind', 'nic',
               'res', 'ltd', 'plc', 'in', 'on', 'id', 'sch', 'asn', 'conf', 'art', 'nom', 'pro', 'tv'}

# 中文国家名 → (标准中文, ISO2, 区域桶)
COUNTRY_TABLE = {
    '美国': ('美国', 'US', '北美'), 'us': ('美国', 'US', '北美'), 'usa': ('美国', 'US', '北美'), 'united states': ('美国', 'US', '北美'),
    '加拿大': ('加拿大', 'CA', '北美'), 'canada': ('加拿大', 'CA', '北美'),
    '德国': ('德国', 'DE', '欧洲'), 'germany': ('德国', 'DE', '欧洲'), '英国': ('英国', 'GB', '欧洲'), 'uk': ('英国', 'GB', '欧洲'),
    '意大利': ('意大利', 'IT', '欧洲'), 'italy': ('意大利', 'IT', '欧洲'), '法国': ('法国', 'FR', '欧洲'), '西班牙': ('西班牙', 'ES', '欧洲'),
    '波兰': ('波兰', 'PL', '欧洲'), '捷克': ('捷克', 'CZ', '欧洲'), '荷兰': ('荷兰', 'NL', '欧洲'), '比利时': ('比利时', 'BE', '欧洲'),
    '瑞士': ('瑞士', 'CH', '欧洲'), '瑞典': ('瑞典', 'SE', '欧洲'), '挪威': ('挪威', 'NO', '欧洲'), '丹麦': ('丹麦', 'DK', '欧洲'),
    '芬兰': ('芬兰', 'FI', '欧洲'), '奥地利': ('奥地利', 'AT', '欧洲'), '爱尔兰': ('爱尔兰', 'IE', '欧洲'), '葡萄牙': ('葡萄牙', 'PT', '欧洲'),
    '希腊': ('希腊', 'GR', '欧洲'), 'greece': ('希腊', 'GR', '欧洲'), '匈牙利': ('匈牙利', 'HU', '欧洲'), '罗马尼亚': ('罗马尼亚', 'RO', '欧洲'),
    '保加利亚': ('保加利亚', 'BG', '欧洲'), '立陶宛': ('立陶宛', 'LT', '欧洲'), '拉脱维亚': ('拉脱维亚', 'LV', '欧洲'), '爱沙尼亚': ('爱沙尼亚', 'EE', '欧洲'),
    '斯洛文尼亚': ('斯洛文尼亚', 'SI', '欧洲'), '斯洛伐克': ('斯洛伐克', 'SK', '欧洲'), '克罗地亚': ('克罗地亚', 'HR', '欧洲'), '塞尔维亚': ('塞尔维亚', 'RS', '欧洲'),
    '塞浦路斯': ('塞浦路斯', 'CY', '欧洲'), '马耳他': ('马耳他', 'MT', '欧洲'), '冰岛': ('冰岛', 'IS', '欧洲'), '阿尔巴尼亚': ('阿尔巴尼亚', 'AL', '欧洲'),
    '马其顿': ('北马其顿', 'MK', '欧洲'), '科索沃': ('科索沃', 'XK', '欧洲'), 'kosovo': ('科索沃', 'XK', '欧洲'), '欧洲': ('欧洲（国别未填）', 'EU', '欧洲'),
    '土耳其': ('土耳其', 'TR', '土耳其'), 'turkey': ('土耳其', 'TR', '土耳其'),
    '俄罗斯': ('俄罗斯', 'RU', '俄语区'), '白俄罗斯': ('白俄罗斯', 'BY', '俄语区'), '哈萨克斯坦': ('哈萨克斯坦', 'KZ', '俄语区'),
    '乌兹别克斯坦': ('乌兹别克斯坦', 'UZ', '俄语区'), '吉尔吉斯': ('吉尔吉斯斯坦', 'KG', '俄语区'), '吉尔吉斯斯坦': ('吉尔吉斯斯坦', 'KG', '俄语区'),
    '亚美尼亚': ('亚美尼亚', 'AM', '俄语区'), '阿塞拜疆': ('阿塞拜疆', 'AZ', '俄语区'), '格鲁吉亚': ('格鲁吉亚', 'GE', '俄语区'),
    '摩尔多瓦': ('摩尔多瓦', 'MD', '俄语区'), '蒙古': ('蒙古国', 'MN', '亚太'), '蒙古国': ('蒙古国', 'MN', '亚太'),
    '乌克兰': ('乌克兰', 'UA', '乌克兰'), 'ukraine': ('乌克兰', 'UA', '乌克兰'),
    '沙特阿拉伯': ('沙特阿拉伯', 'SA', '中东'), '沙特': ('沙特阿拉伯', 'SA', '中东'), '阿联酋': ('阿联酋', 'AE', '中东'), '卡塔尔': ('卡塔尔', 'QA', '中东'),
    '科威特': ('科威特', 'KW', '中东'), '巴林': ('巴林', 'BH', '中东'), '阿曼': ('阿曼', 'OM', '中东'), '以色列': ('以色列', 'IL', '中东'),
    '约旦': ('约旦', 'JO', '中东'), '黎巴嫩': ('黎巴嫩', 'LB', '中东'), '伊拉克': ('伊拉克', 'IQ', '中东'), '伊朗': ('伊朗', 'IR', '中东'),
    '叙利亚': ('叙利亚', 'SY', '中东'), '伊斯兰': ('（国别不明：伊斯兰）', '??', '未知'),
    '韩国': ('韩国', 'KR', '亚太'), '日本': ('日本', 'JP', '亚太'), '台湾': ('台湾', 'TW', '亚太'), '香港': ('香港', 'HK', '亚太'), '澳门': ('澳门', 'MO', '亚太'),
    '新加坡': ('新加坡', 'SG', '亚太'), '马来西亚': ('马来西亚', 'MY', '亚太'), '泰国': ('泰国', 'TH', '亚太'), '越南': ('越南', 'VN', '亚太'),
    '印度尼西亚': ('印度尼西亚', 'ID', '亚太'), '印尼': ('印度尼西亚', 'ID', '亚太'), '菲律宾': ('菲律宾', 'PH', '亚太'), '澳大利亚': ('澳大利亚', 'AU', '亚太'),
    '新西兰': ('新西兰', 'NZ', '亚太'), '柬埔寨': ('柬埔寨', 'KH', '亚太'), '老挝': ('老挝', 'LA', '亚太'), '缅甸': ('缅甸', 'MM', '亚太'),
    '文莱': ('文莱', 'BN', '亚太'), '斐济': ('斐济', 'FJ', '亚太'), '图瓦卢': ('图瓦卢', 'TV', '亚太'), '基里巴斯': ('基里巴斯', 'KI', '亚太'),
    '印度': ('印度', 'IN', '南亚'), '巴基斯坦': ('巴基斯坦', 'PK', '南亚'), '孟加拉国': ('孟加拉国', 'BD', '南亚'), '斯里兰卡': ('斯里兰卡', 'LK', '南亚'),
    '尼泊尔': ('尼泊尔', 'NP', '南亚'), '不丹': ('不丹', 'BT', '南亚'), '马尔代夫': ('马尔代夫', 'MV', '南亚'), 'ariana': ('阿富汗（Ariana）', 'AF', '南亚'),
    '巴西': ('巴西', 'BR', '拉美'), '墨西哥': ('墨西哥', 'MX', '拉美'), '阿根廷': ('阿根廷', 'AR', '拉美'), '智利': ('智利', 'CL', '拉美'),
    '秘鲁': ('秘鲁', 'PE', '拉美'), '哥伦比亚': ('哥伦比亚', 'CO', '拉美'), '厄瓜多尔': ('厄瓜多尔', 'EC', '拉美'), '厄尔多瓜': ('厄瓜多尔', 'EC', '拉美'),
    '玻利维亚': ('玻利维亚', 'BO', '拉美'), '巴拉圭': ('巴拉圭', 'PY', '拉美'), '乌拉圭': ('乌拉圭', 'UY', '拉美'), '委内瑞拉': ('委内瑞拉', 'VE', '拉美'),
    '危地马拉': ('危地马拉', 'GT', '拉美'), '萨尔瓦多': ('萨尔瓦多', 'SV', '拉美'), '洪都拉斯': ('洪都拉斯', 'HN', '拉美'), '哥斯达黎加': ('哥斯达黎加', 'CR', '拉美'),
    '巴拿马': ('巴拿马', 'PA', '拉美'), '多米尼加': ('多米尼加', 'DO', '拉美'), '多米尼亚': ('多米尼加', 'DO', '拉美'), '多米尼克': ('多米尼克', 'DM', '拉美'),
    '牙买加': ('牙买加', 'JM', '拉美'), '特立尼达': ('特立尼达和多巴哥', 'TT', '拉美'), '特立尼达岛': ('特立尼达和多巴哥', 'TT', '拉美'),
    '瓜德罗普岛': ('瓜德罗普', 'GP', '拉美'),
    '南非': ('南非', 'ZA', '非洲'), '埃及': ('埃及', 'EG', '非洲'), '尼日利亚': ('尼日利亚', 'NG', '非洲'), '肯尼亚': ('肯尼亚', 'KE', '非洲'),
    '坦桑尼亚': ('坦桑尼亚', 'TZ', '非洲'), '乌干达': ('乌干达', 'UG', '非洲'), '津巴布韦': ('津巴布韦', 'ZW', '非洲'), '赞比亚': ('赞比亚', 'ZM', '非洲'),
    '加纳': ('加纳', 'GH', '非洲'), '阿尔及利亚': ('阿尔及利亚', 'DZ', '非洲'), '突尼斯': ('突尼斯', 'TN', '非洲'), '摩洛哥': ('摩洛哥', 'MA', '非洲'),
    '利比亚': ('利比亚', 'LY', '非洲'), 'libya': ('利比亚', 'LY', '非洲'), '埃塞俄比亚': ('埃塞俄比亚', 'ET', '非洲'), '喀麦隆': ('喀麦隆', 'CM', '非洲'),
    '科迈隆': ('喀麦隆', 'CM', '非洲'), '塞内加尔': ('塞内加尔', 'SN', '非洲'), '萨内加尔': ('塞内加尔', 'SN', '非洲'), '科特迪瓦': ('科特迪瓦', 'CI', '非洲'),
    '安哥拉': ('安哥拉', 'AO', '非洲'), '莫桑比克': ('莫桑比克', 'MZ', '非洲'), '刚果': ('刚果', 'CD', '非洲'), '南苏丹': ('南苏丹', 'SS', '非洲'),
    '苏丹': ('苏丹', 'SD', '非洲'), '博茨瓦纳': ('博茨瓦纳', 'BW', '非洲'), '布隆迪': ('布隆迪', 'BI', '非洲'), '毛里塔尼亚': ('毛里塔尼亚', 'MR', '非洲'),
    '马达加斯加': ('马达加斯加', 'MG', '非洲'), '几内亚': ('几内亚', 'GN', '非洲'), '赤道几内亚': ('赤道几内亚', 'GQ', '非洲'), '多哥': ('多哥', 'TG', '非洲'),
    '加蓬': ('加蓬', 'GA', '非洲'), '莱索托': ('莱索托', 'LS', '非洲'), '马拉维': ('马拉维', 'MW', '非洲'), '马拉维共和国': ('马拉维', 'MW', '非洲'),
    '斯威士兰': ('斯威士兰', 'SZ', '非洲'), '尼日尔': ('尼日尔', 'NE', '非洲'), '布基纳法索': ('布基纳法索', 'BF', '非洲'), '贝宁共和国': ('贝宁', 'BJ', '非洲'),
    '卢旺达': ('卢旺达', 'RW', '非洲'), '塞拉利昂': ('塞拉利昂', 'SL', '非洲'), '索马里': ('索马里', 'SO', '非洲'), '马里': ('马里', 'ML', '非洲'),
    '毛里求斯': ('毛里求斯', 'MU', '非洲'),
    '中国': ('中国大陆', 'CN', '中国大陆'), 'china': ('中国大陆', 'CN', '中国大陆'), '深圳': ('中国大陆', 'CN', '中国大陆'), '深圳龙华': ('中国大陆', 'CN', '中国大陆'),
    '深圳宝安': ('中国大陆', 'CN', '中国大陆'), '广州': ('中国大陆', 'CN', '中国大陆'), '湖南长沙': ('中国大陆', 'CN', '中国大陆'), '北京大兴': ('中国大陆', 'CN', '中国大陆'),
    '北京昌平': ('中国大陆', 'CN', '中国大陆'), '福建福州': ('中国大陆', 'CN', '中国大陆'),
}
FILE_COUNTRY = {  # 文件名 / 表名 → 国家（Country 列为空时兜底）
    'AU': '澳大利亚', 'CZ': '捷克', 'Canada': '加拿大', 'DE': '德国', 'FR': '法国', 'HK': '香港', 'Israel': '以色列', 'Italy': '意大利',
    'Japan': '日本', 'KR': '韩国', 'PL': '波兰', 'Singapore': '新加坡', 'South Africa': '南非', 'Spain': '西班牙', 'Thailand': '泰国',
    'UK': '英国', 'US': '美国', 'Ukraine': '乌克兰', '优质俄罗斯客户': '俄罗斯', '土耳其客户': '土耳其', 'TR': '土耳其', 'CA': '加拿大',
    'ES': '西班牙', 'IL': '以色列', 'IN': '印度', 'IT': '意大利', 'SG': '新加坡', 'TH': '泰国', 'UA': '乌克兰', 'ZA': '南非', 'JP': '日本',
    'RU': '俄罗斯', 'Russia': '俄罗斯', 'VN': '越南', 'Cisco': '', '印度': '印度', '沙特阿拉伯': '沙特阿拉伯', '阿联酋': '阿联酋', 'Taiwan': '台湾',
    '2025土耳其ISAF客户': '土耳其', 'ISAF 2025': '土耳其',
}

URL_RE = re.compile(r'(?:https?://|www\.)[^\s,;，；"\'<>()（）]+|\b[a-z0-9][a-z0-9\-]*(?:\.[a-z0-9\-]+)+\.(?:com|net|org|io|co|biz|info|eu|de|uk|it|fr|es|pl|cz|nl|be|ch|se|no|dk|fi|at|ie|pt|gr|hu|ro|bg|lt|lv|ee|si|sk|hr|rs|cy|tr|ru|by|kz|uz|ge|am|az|md|ua|sa|ae|qa|kw|bh|om|il|jo|lb|iq|ir|kr|jp|tw|hk|sg|my|th|vn|id|ph|au|nz|in|pk|bd|lk|np|br|mx|ar|cl|pe|co|ec|bo|py|uy|ve|gt|sv|hn|cr|pa|do|za|eg|ng|ke|tz|ug|zw|zm|gh|dz|tn|ma|ly|et|cm|sn|ci|ao|mz|cn|mn|kh|la|mm|bn|mv|af|al|mk|ba|xk|is|mt|lu|li|tech|shop|store|online|site|pro|me|tv|ltd|group|systems|solutions|network|global|digital|cloud|energy|security)\b(?:/[^\s,;，；"\'<>()（）]*)?', re.I)
EMAIL_RE = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}')
PHONE_RE = re.compile(r'(?:\+|\b)(?:\d[\d \-().]{6,}\d)')


def registrable_domain(host: str) -> str:
    host = host.lower().strip().strip('.')
    host = re.sub(r'^https?://', '', host)
    host = host.split('/')[0].split(':')[0]
    if host.startswith('www.'):
        host = host[4:]
    parts = host.split('.')
    if len(parts) >= 3 and ('.'.join(parts[-2:]) in TWO_LEVEL_TLD or (len(parts[-1]) == 2 and parts[-2] in GENERIC_SLD)):
        return '.'.join(parts[-3:])
    if len(parts) >= 2:
        return '.'.join(parts[-2:])
    return host


def norm_country(raw: str, fallback: str = '') -> tuple:
    r = (raw or '').strip()
    key = r.lower()
    if key in COUNTRY_TABLE:
        return COUNTRY_TABLE[key]
    if r in COUNTRY_TABLE:
        return COUNTRY_TABLE[r]
    if fallback and fallback in COUNTRY_TABLE:
        return COUNTRY_TABLE[fallback]
    if r:
        return (r, '??', '未知')
    return ('未填', '??', '未知')


LEGAL = r'\b(gmbh|ag|kg|co|ltd|limited|plc|srl|s\.r\.l|spa|s\.p\.a|sl|s\.l|sa|s\.a|sas|sarl|bv|b\.v|nv|aps|a/s|ab|as|oy|sp\.? z o\.?o|s\.r\.o|sro|inc|llc|corp|corporation|company|bvba|kft|d\.o\.o|doo|pty|pvt|private|lda|ltda|llp|lp|pte|sdn bhd|sdn|bhd|tic|ltd\.sti|sti|ltd\.şti|şti|a\.ş|as\.|ooo|оoo|ооо|зао|оао|тов|ип|ltd\.|co\.|inc\.|s\.a\.s)\b'


def norm_name(name: str) -> str:
    n = name.lower()
    n = re.sub(r'\(.*?\)', ' ', n)
    n = re.sub(LEGAL, ' ', n)
    n = re.sub(r'[^a-z0-9\u00c0-\u024f\u0400-\u04ff\u4e00-\u9fff]+', ' ', n)
    return re.sub(r'\s+', ' ', n).strip()


def slug(s: str, maxlen: int = 40) -> str:
    s = re.sub(r'[\\/:*?"<>|\n\r\t]+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[:maxlen].strip(' .')
