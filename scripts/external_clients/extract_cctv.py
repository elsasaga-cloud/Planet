# -*- coding: utf-8 -*-
"""CCTV-PoE 仓库（elsasaga-cloud/CCTV-PoE）→ data/external_clients/cctv.json
来源：03-海外客户开发清单.md（表格 / 编号标题+维度表 / 粗体字段条目 / 编号粗体条目）、profile/*.md、smartbyte/03 清单 + smartbyte/profile/、exhibition/。
三种格式混杂、同一家多处出现：先抽全部出现（occurrence），再按域名/规范名合并为一户；非客户条目（情报/估算/展会说明）另存 side CSV。
不导入它们的产品主张（STC-028FP 等臆造型号、FOB 价、250 m PoE、2 年保、CCC），只留事实 + 原文块。"""
import csv
import json
import os
import re
import subprocess
import sys
from collections import Counter, OrderedDict

sys.path.insert(0, os.path.dirname(__file__))
from common import (BIG_GROUP, COMPANY_TOKEN, COUNTRY, DATA, EXT, GENERIC, MAIN, RISK, SECOND, VENDOR, domain_of, emails_in, phones_in,
                    saga_domains, touch_of, urls_in)

COMPANY_TOKEN_RE = COMPANY_TOKEN

REPO = os.path.join(EXT, 'cctv')
EN_COUNTRY = {
    'usa': 'US', 'united states': 'US', 'u.s.': 'US', 'america': 'US', 'canada': 'CA', 'turkey': 'TR', 'türkiye': 'TR', 'turkiye': 'TR',
    'uk': 'GB', 'united kingdom': 'GB', 'england': 'GB', 'scotland': 'GB', 'wales': 'GB', 'britain': 'GB', 'ireland': 'IE', 'france': 'FR',
    'germany': 'DE', 'deutschland': 'DE', 'netherlands': 'NL', 'holland': 'NL', 'belgium': 'BE', 'luxembourg': 'LU', 'austria': 'AT',
    'switzerland': 'CH', 'italy': 'IT', 'italia': 'IT', 'spain': 'ES', 'españa': 'ES', 'portugal': 'PT', 'denmark': 'DK', 'sweden': 'SE',
    'norway': 'NO', 'finland': 'FI', 'iceland': 'IS', 'poland': 'PL', 'polska': 'PL', 'czech': 'CZ', 'czechia': 'CZ', 'slovakia': 'SK',
    'hungary': 'HU', 'slovenia': 'SI', 'croatia': 'HR', 'serbia': 'RS', 'bosnia': 'BA', 'montenegro': 'ME', 'macedonia': 'MK',
    'albania': 'AL', 'greece': 'GR', 'cyprus': 'CY', 'malta': 'MT', 'romania': 'RO', 'bulgaria': 'BG', 'estonia': 'EE', 'latvia': 'LV',
    'lithuania': 'LT', 'moldova': 'MD', 'ukraine': 'UA', 'belarus': 'BY', 'russia': 'RU', 'georgia': 'GE', 'armenia': 'AM',
    'azerbaijan': 'AZ', 'kazakhstan': 'KZ', 'uzbekistan': 'UZ', 'kyrgyzstan': 'KG', 'tajikistan': 'TJ', 'turkmenistan': 'TM',
    'mongolia': 'MN', 'israel': 'IL', 'uae': 'AE', 'dubai': 'AE', 'abu dhabi': 'AE', 'emirates': 'AE', 'saudi': 'SA', 'ksa': 'SA',
    'riyadh': 'SA', 'jeddah': 'SA', 'qatar': 'QA', 'doha': 'QA', 'kuwait': 'KW', 'bahrain': 'BH', 'oman': 'OM', 'jordan': 'JO',
    'lebanon': 'LB', 'iraq': 'IQ', 'iran': 'IR', 'egypt': 'EG', 'morocco': 'MA', 'tunisia': 'TN', 'algeria': 'DZ', 'libya': 'LY',
    'south africa': 'ZA', 'nigeria': 'NG', 'kenya': 'KE', 'tanzania': 'TZ', 'uganda': 'UG', 'rwanda': 'RW', 'ethiopia': 'ET', 'ghana': 'GH',
    'senegal': 'SN', 'cameroon': 'CM', 'zambia': 'ZM', 'zimbabwe': 'ZW', 'mozambique': 'MZ', 'angola': 'AO', 'namibia': 'NA',
    'botswana': 'BW', 'mauritius': 'MU', 'india': 'IN', 'pakistan': 'PK', 'bangladesh': 'BD', 'sri lanka': 'LK', 'nepal': 'NP',
    'korea': 'KR', 'japan': 'JP', 'taiwan': 'TW', 'hong kong': 'HK', 'macau': 'MO', 'vietnam': 'VN', 'thailand': 'TH', 'malaysia': 'MY',
    'singapore': 'SG', 'indonesia': 'ID', 'philippines': 'PH', 'cambodia': 'KH', 'myanmar': 'MM', 'laos': 'LA', 'brunei': 'BN',
    'australia': 'AU', 'new zealand': 'NZ', 'mexico': 'MX', 'brazil': 'BR', 'brasil': 'BR', 'argentina': 'AR', 'chile': 'CL',
    'colombia': 'CO', 'peru': 'PE', 'ecuador': 'EC', 'venezuela': 'VE', 'bolivia': 'BO', 'paraguay': 'PY', 'uruguay': 'UY',
    'costa rica': 'CR', 'panama': 'PA', 'guatemala': 'GT', 'honduras': 'HN', 'el salvador': 'SV', 'nicaragua': 'NI',
    'dominican': 'DO', 'jamaica': 'JM', 'trinidad': 'TT', 'puerto rico': 'PR', 'china': 'CN', 'shenzhen': 'CN', 'prc': 'CN',
}
ZH_EXTRA = {'深圳': 'CN', '广州': 'CN', '东莞': 'CN', '上海': 'CN', '北京': 'CN', '杭州': 'CN', '厦门': 'CN', '大陆': 'CN', '迪拜': 'AE', '利雅得': 'SA',
            '吉达': 'SA', '多哈': 'QA', '伦敦': 'GB', '巴黎': 'FR', '柏林': 'DE', '米兰': 'IT', '华沙': 'PL', '马德里': 'ES', '伊斯坦布尔': 'TR',
            '安卡拉': 'TR', '开罗': 'EG', '内罗毕': 'KE', '拉各斯': 'NG', '约翰内斯堡': 'ZA', '孟买': 'IN', '新德里': 'IN', '班加罗尔': 'IN',
            '雅加达': 'ID', '曼谷': 'TH', '吉隆坡': 'MY', '马尼拉': 'PH', '胡志明': 'VN', '河内': 'VN', '首尔': 'KR', '东京': 'JP', '台北': 'TW',
            '悉尼': 'AU', '墨尔本': 'AU', '多伦多': 'CA', '温哥华': 'CA', '纽约': 'US', '洛杉矶': 'US', '加州': 'US', '德州': 'US', '佛州': 'US',
            '墨西哥城': 'MX', '圣保罗': 'BR', '布宜诺斯艾利斯': 'AR', '波哥大': 'CO', '利马': 'PE', '圣地亚哥': 'CL', '欧盟': '', '欧洲': '', '全球': '',
            '中东': '', '非洲': '', '亚太': '', '拉美': '', '北美': '', '东南亚': '', '南亚': '', '国际': ''}
ZH_KEYS = sorted([k for k in list(COUNTRY) + list(ZH_EXTRA) if k], key=len, reverse=True)
EN_KEYS = sorted(EN_COUNTRY, key=len, reverse=True)
NONCLIENT = re.compile(r'(汇总|总结|统计|估算|策略|情报|洞察|排名|Top ?\d|梯队|附录|渠道[A-Z0-9]*[:：]|Part ?\d|Batch|Round|展会|Expo|总计|累计|速查|竞争|说明|目录|'
                       r'README|FINAL|Summary|Index|Overview|方法论|清单|市场|机会|标准|趋势|结论|行动|时间表|KPI|对比|矩阵|搜索|关键词|分析|报告|计划|'
                       r'预算|需求量|端口|采购平台|平台概览|背景|总览|分类|小结|提示|注意|建议|下一步|数据|指标|模板|FAQ|术语|名词|阶段|里程碑|复盘|\d+\s*家|€|£|\$|%|需求|潜力|'
                       r'其他[^A-Za-z]*客户|其他[^A-Za-z]*$)', re.I)
LABELS = {'国家', '城市', '公司名', '公司', '网站', '规模', '业务', 'poe需求', 'saga匹配', '优先级', '开发策略', '客户等级', '产品线', '联系', '联系方式',
          '邮箱', '电话', '地址', '品牌', '类型', '级别', '年营收', '员工', '成立', '总部', '备注', '搜索轮次', '统计', '核心业务', '项目', '网络', '需求',
          '特点', '卖点', '推荐产品', '推荐', '对标', '策略', '定位', '覆盖', '状态', '来源', '渠道', '行业', '角色', '母公司', '营收', '产品', '服务',
          '切入点', '痛点', '机会', '风险', '下一步', '行动', '话术', '目标', '预算', '采购', '数量', '金额', '时间', '阶段', '匹配度', '匹配', '原因',
          '理由', '说明', '注', '注意', '提示', '结论', '总结', '汇总', '分析', '背景', '简介', '概况', '描述', '细节', '亮点', '关键', '核心', '主营',
          '主打', '代理', '代理品牌', '合作品牌', '在售品牌', '现有品牌', '竞品', '替代', '价格', '报价', '利润', '毛利', '成本', '交期', '物流', '付款',
          '认证', '质保', '保修', '标准', '规格', '参数', '功率', '端口', '覆盖区域', '区域', '地区', '位置', '所在地', '办公室', '分部', '门店', '店',
          'phase', 'website', 'email', 'phone', 'contact', 'address', 'notes', 'priority', 'strategy', 'poe', 'saga', 'wifi', 'wi-fi'}
LABEL_WORDS = re.compile(r'^(Europages|Batch|Round|Saga|HRUI|PoE|Wi-?Fi|Top|Part|FOB|OEM|ODM|NDAA|TAA|IP\d\d|LinkedIn|Amazon|Google|Alibaba|'
                         r'Volza|ImportYeti|Panjiva|Phase|Step|Tier|Total|Summary|Key|Note|Why|How|What|Action|Next|LSBU|LBU|UPS|CCTV|VMS|NVR|'
                         r'DVR|IP|AP|L2|L3|SFP|GbE|PoE\+|BT|AI|IoT|KPI|ROI|MOQ|RFQ|RFP|TCO|SLA|B2B|B2C|D2C|EU|UK|US|USA|UAE|KSA|GCC|MENA|APAC|'
                         r'EMEA|LATAM|ASEAN|CIS|NATO|ISO|CE|FCC|UL|RoHS|REACH|UKCA|EAC|ATEX|IEC|IEEE|ISC|Intersec|IFSEC|ISAF|Secutech|SIA|'
                         r'ASIS|GSX|Expo|Fair|Show)\b', re.I)
JUNK = re.compile(r'(情报|潜力|市场|数据|需求|机会|投资|开发$|朝圣|内部|系统$|PoE|Wi-?Fi|EV充电|太阳能|社区|展会|Expo\b|Fair\b|Summit|统计|总计|汇总|'
                  r'£|\$|€|%|Top ?\d|Batch|Round|Part ?\d|^[A-Z]{1,2}[:：]|LinkedIn|Volza|Europages|Yellow ?Pages|Google|Amazon|Alibaba|Kompass|'
                  r'ImportYeti|Panjiva|Noon\.com|\d+\s*家|端口|交换机$|品牌$|渠道$|分销$|集成$|客户$|竞品|对比|案例|项目$|标准|认证$|方案$|平台$|'
                  r'产业|行业|市场|趋势|总览|概览|清单|列表|名单|目录|索引|Overview|Summary|Index|List|排名|分析|^主要|详细|估算|合作方案|总结)', re.I)
MODEL = re.compile(r'\b[A-Z]{1,6}[- ]?\d{2,}[A-Z0-9-]*\b|\b\d{3,}[A-Z]{1,3}\b|\bv\d+(\.\d+)?\b')
ACRONYM_ONLY = re.compile(r'^(PoE|CCTV|IT|IP|AI|OEM|ODM|VMS|NVR|DVR|Wi-?Fi|B2B|B2C|D2C|OK|ERP|BMS|MEP|ELV|FM|ICT|IoT|LED|UPS|USB|HD|4K|5G|LTE|'
                          r'GPON|FTTH|SFP|L2|L3|AP|VPN|SD-WAN|KNX|DALI|BIM|ESG|GMP|NDAA|TAA|ATEX|UL|CE|FCC|RoHS|ISO|IEC|IEEE|EN|DIN|VdS|SIRA|'
                          r'DEWA|TOKİ|TOKI|NHS|NATO|EU|UK|US|USA|UAE|KSA|GCC|MENA|APAC|EMEA|LATAM|CIS|DACH|Benelux|Nordic|Baltic|Iberia)$', re.I)
CHANNEL_CTX = re.compile(r'(分销|经销|集成|安装|渠道|批发|零售|OEM|供应商|电商|网店|进口商|代理|Distributor|Integrator|Installer|Reseller|Wholesale|'
                         r'VAR|SI\b|Dealer|Partner|Shop|Store)', re.I)
DOMAIN_NAME = re.compile(r'^[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.(com|net|org|de|fr|it|es|pl|nl|be|uk|co\.uk|ae|sa|tr|ca|us|eu|io|shop|info|biz|ch|at|se|dk|no|fi|cz|hu|ro|gr|pt|ie)$', re.I)


def latin_core(name):
    t = re.sub(r'[^A-Za-zÀ-ž0-9&.\- ]+', ' ', name or '')
    toks = [x for x in t.split() if not ACRONYM_ONLY.match(x) and not re.match(r'^\d+$', x)]
    return ' '.join(toks).strip()


def looks_like_org(name, line='', ctx=''):
    """粗体/表格条目是否像一个组织名（而不是产品型号、地区、情报标题）"""
    if not name or len(name) < 3 or len(name) > 90:
        return False, '太短或太长'
    core = latin_core(name)
    if len(core) < 3:
        return False, '无拉丁名'
    if JUNK.search(name):
        return False, '情报/统计/产品类标题'
    if MODEL.search(core) and not re.search(r'\.(com|net|de|fr|it|es|pl|nl|uk|ae|sa|tr|ca|us|eu)\b', core):
        return False, '产品型号'
    if LABEL_WORDS.match(core):
        return False, '字段标签'
    return True, ''


def org_evidence(name, line, ctx):
    if re.search(r'@|https?://|www\.|\.(com|net|org|de|fr|it|es|pl|nl|be|co\.uk|uk|ae|sa|tr|ca|us|eu|io)\b', line):
        return True
    if COMPANY_TOKEN_RE.search(name):
        return True
    if CHANNEL_CTX.search(line) or CHANNEL_CTX.search(ctx):
        return True
    if find_countries(re.sub(r'^[^（(]*', '', name)):
        return True
    return False


FLAG = re.compile('[\U0001F1E6-\U0001F1FF]{2}')
STARS = re.compile('[★⭐🟢🟡🔴]+')
ENDUSER = re.compile(r'(大学|University|College|学校|School|学院|教育局|医院|Hospital|Clinic|医疗集团|机场|Airport|酒店|Hotel|Resort|超市|连锁|零售连锁|'
                     r'银行|Bank|政府|Government|Ministry|部委|市政|Municipal|Council|监狱|Prison|港口|Port Authority|铁路|Railway|Rail\b|Metro|地铁|'
                     r'公交|Transit|军|Defen[cs]e|Army|Navy|Air Force|石油|Oil|Gas|Aramco|博物馆|Museum|体育场|Stadium|Arena|球场|俱乐部|F\.?C\.?|'
                     r'物流中心|Logistics Cent|仓储|Warehouse\b(?!\s*(Ltd|LLC|BV|GmbH))|制造商\(终端|工厂|Factory|Plant|矿|Mine|电力公司|Utility|'
                     r'水务|Water|机关|Agency|Authority|Corporation of|市议会|County|State of|Province|Department|Dept|Police|警察|消防|Fire|'
                     r'Church|教堂|清真寺|Mosque|公园|Park|动物园|Zoo|赌场|Casino|购物中心|Mall|商场|Shopping|写字楼|Office Tower|地产|Real Estate|'
                     r'开发商|Developer|建筑公司|Construction|Contractor\b(?!.*(安防|Security|低压|ELV))|Telecom Operator|运营商|Operator|ISP\b|'
                     r'Airlines?|航空|Shipping|船公司|Cruise|邮轮|Hospitality|餐饮|Restaurant|快餐|Cafe|咖啡|Gym|健身|Cinema|影院|Theatre|剧院|Library|'
                     r'图书馆|Pharmacy|药店|Supermarket|Grocery|Hypermarket|Retailer\b(?!.*(安防|Security|CCTV|网络|IT)))', re.I)
ENDUSER2 = re.compile(r'(NHS|\bTrust\b|Universit|Politecnico|Ospedale|Hôpital|Krankenhaus|Klinik|Szpital|Uniwersytet|Universidad|Université|Universität|'
                      r'Hochschule|Scuola|Liceo|Lycée|Gymnasium|Comune di|Ayuntamiento|Mairie|Stadt\b|Gmina|Miasto|Provincia|Regione|Région|Ministero|Ministerio|'
                      r'Ministère|Ministerium|Aeroporto|Aeropuerto|Aéroport|Flughafen|Lotnisko|Porto di|Puerto de|Port of|Autostrade|Ferrovie|Trenitalia|Renfe|'
                      r'SNCF|Deutsche Bahn|\bPKP\b|Tramway|Banca|Banco|Banque|Sparkasse|Volksbank|Caja\b|Assicurazioni|Seguros|Assurance|Versicherung|'
                      r'\bEnel\b|Iberdrola|Endesa|\bEDF\b|Engie|E\.ON|\bRWE\b|Orlen|\bPGE\b|Tauron|\bEnea\b|\bEni\b|Repsol|Cepsa|TotalEnergies|Shell\b|\bBP\b|'
                      r'Acciaierie|Steel|Cement|Chimica|Pharma|Farmac|Laboratorios|Menarini|Stadio|Estadio|Stade\b|Stadion|Calcio|Fútbol|Football|Basket|'
                      r'Museo|Musée|Teatro|Opera|Biblioteca|Fiera|Feria|Messe\b|Salone|Supermercat|Supermarch|Supermarkt|Ipermercati|Hipermercados|Conad|'
                      r'\bCoop\b|Esselunga|Carrefour|Auchan|Lidl|Aldi|Tesco|Sainsbury|Asda|Morrisons|Mercadona|Eroski|Biedronka|Żabka|Kaufland|Rewe|Edeka|'
                      r'Leclerc|Intermarch|Monoprix|Decathlon|IKEA|Zara|Inditex|Mango|H&M|Primark|Luxottica|Safilo|Gucci|Prada|Armani|Ferrari|Lamborghini|'
                      r'Maserati|Fiat|Stellantis|Volkswagen|\bBMW\b|Mercedes|\bAudi\b|Porsche|Renault|Peugeot|Citroën|\bSEAT\b|Airbus|Leonardo|Thales|Dassault|'
                      r'Rheinmetall|Navantia|Fincantieri|Indra\b|Hensoldt|Diehl|KNDS|\bBAE\b|Rolls-Royce|Jaguar|Nissan|Toyota|Honda|Ford\b|\bDHL\b|FedEx|'
                      r'\bGLS\b|\bDPD\b|Poczta|Poste\b|Correos|La Poste|Royal Mail|Deutsche Post|Aramco|SABIC|Ma.aden|NEOM|Red Sea|Qiddiya|Diriyah|'
                      r'Expo 2030|Vision 2030|Saudi Electricity|\bSEC\b|\bSWCC\b|ACWA|Emaar|Nakheel|Aldar|Majid Al Futtaim|Al Futtaim|Etisalat|\bdu\b|'
                      r'\bSTC\b|Mobily|Zain|Ooredoo|Emirates\b|Etihad|Saudia|flydubai|Qatar Airways|Turkish Airlines|THY\b|Pegasus|Türk Telekom|Turkcell|'
                      r'Vodafone|Telefónica|Movistar|Orange\b|Bouygues|\bSFR\b|Free\b|Telecom Italia|\bTIM\b|WindTre|Iliad|Fastweb|Telekom|O2\b|\bEE\b|'
                      r'\bBT\b|Virgin Media|Sky\b|Plus\b|Play\b|T-Mobile|Netia|Orange Polska|Hilton|Marriott|Accor|Hyatt|IHG|Radisson|Meliá|NH Hotels|'
                      r'Barceló|Iberostar|RIU|Best Western|Premier Inn|Travelodge|Holiday Inn|Novotel|Ibis\b|Mercure|Sofitel|Kempinski|Four Seasons|Ritz|'
                      r'Jumeirah|Rotana|Address Hotels|Atlantis|Burj|TOKİ|TOKI|Belediye|Büyükşehir|Üniversite|Hastane|Havalimanı|Havaalanı|Liman|Metro|'
                      r'İETT|TCDD|BOTAŞ|TPAO|TÜPRAŞ|Petkim|Erdemir|Tofaş|Oyak|Koç|Sabancı|Eczacıbaşı|Zorlu|Doğuş|Anadolu|Ülker|Migros|BİM|A101|ŞOK|'
                      r'CarrefourSA|Teknosa|MediaMarkt|Vatan|Boyner|LC Waikiki|DeFacto|Mavi|Beko|Arçelik|Vestel|Ziraat|İş Bankası|Garanti|Akbank|Yapı Kredi|'
                      r'Halkbank|VakıfBank|QNB|Denizbank|TEB\b|ING\b|HSBC|Santander|BBVA|CaixaBank|Sabadell|Bankia|Unicredit|Intesa|BNP|Société Générale|'
                      r'Crédit Agricole|Commerzbank|Deutsche Bank|Barclays|Lloyds|NatWest|RBS\b|Nationwide|PKO|Pekao|mBank|Santander Bank|Alior|Millennium|'
                      r'Al Rajhi|SNB\b|Riyad Bank|SAB\b|Alinma|Emirates NBD|FAB\b|ADCB|Mashreq|DIB\b|RAKBANK)', re.I)
BUYER = re.compile(r'(分销|批发|经销|代理|集成|安装|工程|弱电|零售|电商|网店|进口|贸易|供应|方案商|服务商|系统商|安防公司|品牌商|自有品牌|OEM|ODM|'
                   r'VAR|\bSI\b|授权|经销|Authori[sz]ed|Dealer|Partner|Distribut|Wholesal|Install|Integrat|Reseller|Retail|Import|Trading|Supply|Supplier|Solutions?|Systems?|'
                   r'Technolog|Network|Telecom|Electronic|Security|Securit|Elektronik|Sistem|Güvenlik|Seguridad|Sécurité|Sicherheit|Sicurezza|'
                   r'Zabezpiecz|Webshop|Online|Store|Shop|E-commerce|Marketplace|Private Label|Brand)', re.I)


def git(args):
    return subprocess.check_output(['git', '-C', REPO] + args).decode().strip()


def flags_iso(text):
    out = []
    for m in FLAG.findall(text or ''):
        iso = ''.join(chr(ord(c) - 0x1F1E6 + 65) for c in m)
        if iso not in out:
            out.append(iso)
    return out


def find_countries(text):
    """返回文本里出现的 ISO 列表（去重，按出现顺序）；中国台湾/香港先于中国。"""
    t = text or ''
    out = []
    for iso in flags_iso(t):
        if iso not in out and iso not in ('EU',):
            out.append(iso)
    tt = t
    for k in ZH_KEYS:
        if k in tt:
            iso = COUNTRY.get(k, ZH_EXTRA.get(k, ''))
            tt = tt.replace(k, ' ')
            if iso and iso not in out:
                out.append(iso)
    low = ' ' + re.sub(r'[^a-zA-Zäöüéèáíóúñçğşİı.]+', ' ', tt.lower()) + ' '
    for k in EN_KEYS:
        if ' ' + k + ' ' in low or ' ' + k + '.' in low:
            iso = EN_COUNTRY[k]
            if iso not in out:
                out.append(iso)
    return out


def iso_label(iso):
    for k, v in COUNTRY.items():
        if v == iso:
            return k
    return iso


def clean_name(s):
    s = STARS.sub('', s or '')
    s = FLAG.sub('', s)
    s = s.replace('**', '').strip()
    s = re.sub(r'^\d+(\.\d+)*\.?\s*', '', s)
    s = re.sub(r'\s+', ' ', s).strip(' -—–|:：,，;；')
    return s


def norm_key(name):
    s = (name or '').lower()
    s = re.sub(r'[（(].*?[)）]', '', s)
    s = re.sub(r'\b(ltd|limited|llc|inc|corp|corporation|co|company|gmbh|ag|bv|b\.v|nv|sa|s\.a|srl|s\.r\.l|spa|s\.p\.a|sl|s\.l|sas|sarl|pty|sdn|bhd|'
               r'fze|fzco|fzc|dmcc|plc|oy|ab|as|aps|kft|zrt|doo|d\.o\.o|sro|s\.r\.o|sp\. ?z ?o\.? ?o\.?|lda|pvt|private|public|group|holding|holdings|'
               r'international|intl|trading|technologies|technology|tech|systems|system|solutions|solution|networks|network|distribution|'
               r'distributors|distributor|security|securities|the)\b', ' ', s)
    s = re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', s)
    return s


def split_heading(text):
    """'96.1 EuroDK | 丹麦 | B类 | Mikrotik欧洲分销' → name, segs"""
    t = clean_name(text)
    segs = [x.strip() for x in re.split(r'\s\|\s', t)] if ' | ' in t else [t]
    name = segs[0]
    desc = ''
    for sep in (' — ', ' – ', ' - ', '——', '：', ': '):
        if sep in name:
            name, desc = name.split(sep, 1)
            break
    return name.strip(), segs[1:], desc.strip()


def table_blocks(lines):
    """返回 [(header_cells, [rows])] 以及被表格占用的行号集合"""
    out, used = [], set()
    i = 0
    while i < len(lines):
        if lines[i].startswith('|') and i + 1 < len(lines) and re.match(r'^\|\s*:?-', lines[i + 1]):
            hdr = [c.strip() for c in lines[i].strip().strip('|').split('|')]
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].startswith('|'):
                rows.append([c.strip() for c in lines[j].strip().strip('|').split('|')])
                j += 1
            out.append((hdr, rows))
            used.update(range(i, j))
            i = j
        else:
            i += 1
    return out, used


def kv_from_block(lines, tbls):
    kv = OrderedDict()
    for hdr, rows in tbls:
        if len(hdr) == 2 and (hdr[0] in ('维度', '项目', '渠道', '字段', '属性', '条目') or hdr[1] in ('详情', '内容', '信息', '评估')):
            for r in rows:
                if len(r) >= 2:
                    k = r[0].replace('**', '').strip()
                    if k and k not in kv:
                        kv[k] = r[1].replace('**', '').strip()
    for l in lines:
        if l.startswith('|'):
            continue
        for m in re.finditer(r'\*\*([^*]{1,20})\*\*\s*[:：]\s*([^|]*)', l):
            k, v = m.group(1).strip(), m.group(2).strip()
            if k and k not in kv and v:
                kv[k] = v
    return kv


def kv_get(kv, *keys):
    for k in keys:
        for kk, v in kv.items():
            if kk == k or kk.startswith(k):
                return v
    return ''


DROPPED = []


class Occ:
    """一次出现"""

    def __init__(self, name, src_file, line, path, kind):
        self.name = name
        self.src_file = src_file
        self.line = line
        self.path = path          # heading path list
        self.kind = kind          # heading/table/bold/profile/exhibition
        self.country_text = ''
        self.iso = ''
        self.type = ''
        self.their_class = ''
        self.stars = 0
        self.website = ''
        self.emails = []
        self.phones = []
        self.kv = OrderedDict()
        self.raw = ''
        self.notes = ''
        self.flags = []
        self.iso_src = ''


def resolve_iso(o, ctx_iso):
    cands = []
    src = 'field'
    for key in ('国家', '国家/地区', '所在国', '所在地', '地区', '总部', '地址', '城市', '位置', '覆盖区域'):
        v = kv_get(o.kv, key)
        if v:
            cs = find_countries(v)
            if cs:
                cands = cs
                break
    if not cands and o.country_text:
        cands = find_countries(o.country_text)
        src = 'field'
    if not cands:
        cands = find_countries(re.sub(r'^[^（(]*', '', o.name))      # 名字里的 (中国)
        src = 'name'
    if not cands and ctx_iso:
        cands = [ctx_iso]
        src = 'ctx'
    o.iso_src = src if cands else ''
    if 'CN' in cands and len(cands) > 1 and not re.search(r'中国|China|深圳|Shenzhen', o.country_text + ' ' + kv_get(o.kv, '国家')):
        cands = [c for c in cands if c != 'CN']
    return cands[0] if cands else '', '/'.join(cands)


def block_entries(lines, start_line, path, src_file, ctx_iso):
    """非条目标题块：抽列表表格行 + 粗体条目"""
    occs = []
    tbls, used = table_blocks(lines)
    for hdr, rows in tbls:
        hl = [h.replace('**', '') for h in hdr]
        ci = None
        for i, h in enumerate(hl):
            if re.search(r'公司|客户|渠道|名称|Company|企业|机构|经销商|分销商|集成商|品牌|展商|参展', h):
                ci = i
                break
        if ci is None:
            continue
        for r in rows:
            if len(r) <= ci:
                continue
            nm = clean_name(r[ci])
            ok, why = looks_like_org(nm, ' '.join(r), ' '.join(path))
            if not ok:
                if nm:
                    DROPPED.append({'file': src_file, 'line': start_line, 'kind': 'table', 'name': nm, 'why': why, 'text': (' | '.join(r))[:200]})
                continue
            o = Occ(nm, src_file, start_line, path, 'table')
            for i, h in enumerate(hl):
                if i < len(r) and r[i] and i != ci:
                    o.kv[h] = r[i].replace('**', '').strip()
            o.country_text = kv_get(o.kv, '国家', '国家/地区', '地区', '所在地')
            o.type = kv_get(o.kv, '类型', '公司类型', '业务', '角色', '定位', '客户类型')
            o.their_class = re.sub(r'[^ABCD]', '', kv_get(o.kv, '级别', '客户级别', '等级', '评级', '分级', '客户等级', '类别'))[:1]
            o.stars = len(STARS.findall(' '.join(r)))
            o.raw = '| ' + ' | '.join(hl) + ' |\n| ' + ' | '.join(r) + ' |'
            occs.append(o)
    for idx, l in enumerate(lines):
        if idx in used or l.startswith('|'):
            continue
        m = re.match(r'^\s*(?:\d+\.|[-*•])\s+\*\*([^*]{3,90})\*\*\s*(.*)$', l) or re.match(r'^\*\*([^*]{3,90})\*\*\s*[-—–:：|]\s*(.*)$', l)
        if not m:
            continue
        nm_raw, rest = m.group(1), m.group(2)
        if re.match(r'^[^A-Za-z]*$', nm_raw) or LABEL_WORDS.match(nm_raw.strip()) or nm_raw.strip().lower().rstrip('：:') in LABELS:
            continue
        if re.match(r'^(.{1,12})[:：]', nm_raw) and nm_raw.split('：')[0].split(':')[0].strip().lower() in LABELS:
            continue
        nm = clean_name(nm_raw)
        if not nm or len(nm) < 3 or re.search(r'[:：]$', nm_raw.strip()):
            continue
        ok, why = looks_like_org(nm, l, ' '.join(path))
        if ok and not org_evidence(nm, l, ' '.join(path[-2:])):
            ok, why = False, '粗体条目无公司证据（无域名/公司后缀/渠道语境/国别）'
        if not ok:
            DROPPED.append({'file': src_file, 'line': start_line + idx, 'kind': 'bold', 'name': nm, 'why': why, 'text': l.strip()[:200]})
            continue
        o = Occ(nm, src_file, start_line + idx, path, 'bold')
        o.notes = rest.strip()[:300]
        o.country_text = ''
        o.stars = len(STARS.findall(l))
        o.raw = l.strip()[:600]
        occs.append(o)
    return occs


def heading_is_entry(level, htext, lines, tbls, bold_count):
    t = clean_name(htext)
    if len(latin_core(t.split(' | ')[0])) < 3:
        return False
    if re.search(r'€|£|\$|%|需求|市场|潜力|数据|情报|端口|\d+\s*家', t.split(' | ')[0]) and not COMPANY_TOKEN_RE.search(t):
        return False
    if NONCLIENT.search(t) and not re.search(r'\b(Ltd|LLC|GmbH|Inc|BV|SA|Srl|SpA|Sdn|Pty|FZE|DMCC|Limited|Corp|Co\.|AG|AS|AB|ApS|Kft|d\.o\.o|s\.r\.o|Sp\.)\b', t):
        return False
    latin = re.sub(r'[^A-Za-z ]', ' ', t).strip()
    if latin.lower() in EN_COUNTRY or len(latin) < 3:
        return False
    if any(len(h) >= 3 and re.search(r'公司|客户|渠道|名称|Company', ' '.join(h)) for h, _ in tbls):
        return False            # 下面是客户列表表，标题是分节
    if level <= 2 and not re.match(r'^#?\s*\d+\.\s', htext.strip('# ')) and not any(len(h) == 2 for h, _ in tbls):
        return False
    if re.match(r'^\d+(\.\d+)?\s', htext.strip('# ').strip()) or re.match(r'^\d+\.\s', htext.strip('# ').strip()):
        return True
    if any(len(h) == 2 and h[0] in ('维度', '项目') for h, _ in tbls):
        return True
    if re.search(r'^- \*\*(国家|公司名|公司全称|网站)\*\*', '\n'.join(lines), flags=re.M):
        return True
    if level == 1:
        return True
    return False


def parse_doc(path, src_file, base_ctx=None, kind='heading'):
    text = open(path, encoding='utf-8').read()
    L = text.split('\n')
    heads = [(i, len(re.match(r'^(#+)', l).group(1)), l[len(re.match(r'^(#+)', l).group(1)):].strip()) for i, l in enumerate(L) if re.match(r'^#{1,4} ', l)]
    heads.append((len(L), 0, ''))
    stack = {}
    occs, side = [], []
    ctx_iso = base_ctx or ''
    for n in range(len(heads) - 1):
        i, lvl, ht = heads[n]
        j = heads[n + 1][0]
        for k in list(stack):
            if k >= lvl:
                del stack[k]
        stack[lvl] = ht
        path = [stack[k] for k in sorted(stack)]
        # 上下文国家：从最近的父标题里找唯一国家
        ctx = base_ctx or ''
        for k in sorted(stack, reverse=True):
            cs = find_countries(stack[k])
            if len(cs) == 1 and cs[0] != 'CN':
                ctx = cs[0]
                break
        lines = L[i + 1:j]
        tbls, used = table_blocks(lines)
        bold_count = len([l for l in lines if re.match(r'^\s*(?:\d+\.|[-*])\s+\*\*', l) or l.startswith('**')])
        if heading_is_entry(lvl, ht, lines, tbls, bold_count):
            name, segs, desc = split_heading(ht)
            o = Occ(name, src_file, i + 1, path[:-1], kind)
            o.kv = kv_from_block(lines, tbls)
            o.country_text = segs[0] if segs else ''
            cls = ''
            for s in segs:
                m = re.search(r'\b([ABCD])\s*[类级]', s)
                if m:
                    cls = m.group(1)
            if not cls:
                m = re.search(r'([ABCD])\s*[类级]', kv_get(o.kv, '客户等级', '客户级别', '级别', '评级', '分级', '等级'))
                cls = m.group(1) if m else ''
            o.their_class = cls
            o.type = kv_get(o.kv, '类型', '公司类型', '业务', '角色', '定位', '客户类型') or (segs[2] if len(segs) > 2 else (segs[1] if len(segs) > 1 and not re.search(r'[ABCD][类级]', segs[1]) else desc))
            o.stars = len(STARS.findall(ht)) or len(STARS.findall(kv_get(o.kv, '优先级', '匹配度')))
            o.website = kv_get(o.kv, '网站', '官网', 'Website', '网址')
            body = '\n'.join(lines)
            o.raw = (ht + '\n' + body).strip()[:2500]
            o.emails = emails_in(body)
            o.phones = phones_in(body)
            o.notes = desc
            exh = re.search(r'来源展会[:：]\*?\*?\s*([^\n]+)', body)
            if exh:
                o.flags.append('展会:' + exh.group(1).strip()[:60])
            o.iso, o.country_text2 = resolve_iso(o, ctx)
            occs.append(o)
            # 条目块内若还有子公司列表表（如 Europages 聚合），一并抽
            for so in block_entries(lines, i + 1, path, src_file, ctx):
                if so.kind == 'table':
                    so.iso, _ = resolve_iso(so, o.iso or ctx)
                    occs.append(so)
            if len(lines) > 3 and not o.emails and not o.website and re.search(r'分销$|渠道$|平台$|市场$', name):
                o.flags.append('聚合条目')
        else:
            if NONCLIENT.search(clean_name(ht)) and lvl >= 2 and not tbls and bold_count == 0:
                side.append({'file': src_file, 'line': i + 1, 'heading': ht, 'why': '非客户段落（无表无条目）'})
            for so in block_entries(lines, i + 1, path, src_file, ctx):
                so.iso, _ = resolve_iso(so, ctx)
                occs.append(so)
    return occs, side


def parse_profile(path, src_file):
    text = open(path, encoding='utf-8').read()
    L = text.split('\n')
    h1 = re.search(r'^# (.+)$', text, flags=re.M)
    title = clean_name(h1.group(1)) if h1 else os.path.basename(path)[:-3]
    title = re.sub(r'^客户档案[:：]\s*', '', title)
    name = title.split(' — ')[0].split(' - ')[0].split('—')[0].strip()
    tbls, used = table_blocks(L)
    kv = kv_from_block(L, tbls)
    o = Occ(kv_get(kv, '公司全称', '公司名称', '公司') or name, src_file, 1, [title], 'profile')
    o.kv = kv
    o.country_text = kv_get(kv, '国家', '国家/地区', '地区') or (title.split(' — ')[1] if ' — ' in title else '')
    o.type = kv_get(kv, '类型', '公司类型', '业务', '定位')
    m = re.search(r'([ABCD])\s*[类级]', kv_get(kv, '客户级别', '客户等级', '级别', '评级', '分级', '等级'))
    o.their_class = m.group(1) if m else ''
    o.stars = len(STARS.findall(kv_get(kv, '优先级', '匹配度'))) or len(STARS.findall(text[:600]))
    o.website = kv_get(kv, '网站', '官网', 'Website', '网址')
    o.emails = emails_in(text)
    o.phones = phones_in(kv_get(kv, '电话', '总部', '中央销售办公室', 'WhatsApp', '联系电话') + '\n' + '\n'.join(' '.join(r) for h, rows in tbls for r in rows if h and h[0] in ('渠道', '项目')))
    o.raw = text[:3000]
    exh = re.search(r'来源展会[:：]\*?\*?\s*([^\n]+)', text)
    if exh:
        o.flags.append('展会:' + exh.group(1).strip()[:60])
    o.iso, _ = resolve_iso(o, '')
    return o


def classify(rec):
    """CCTV 专用初判。"""
    name, iso, typ = rec['name'], rec['iso'], rec.get('type') or ''
    flags = list(rec['flags'])
    blob = name + ' ' + typ + ' ' + ' '.join(rec.get('heading_path') or [])
    if iso == 'CN':
        return 'DELETE', '大陆公司（Simon：一律删除）', flags + ['大陆']
    if rec.get('saga_dup'):
        d = rec['saga_dup']
        return 'C', f"与 Saga Clients 重叠（{d['code']}，经 {d['via']}）→ 以 Saga 档为准", flags + ['重复=Saga']
    if BIG_GROUP.search(name):
        return 'C', '超大集团 / 决策链太长', flags + ['大集团']
    if VENDOR.search(name) or re.search(r'芯片|Chip|Semiconductor|VMS 厂商|VMS厂商|原厂', typ):
        return 'C', '品牌原厂 / 芯片商 / VMS 厂商 / 同行，不是买家', flags + ['原厂或同行']
    buyer_sig = bool(BUYER.search(name + ' ' + typ)) or rec.get('their_class') in ('A', 'B', 'C', 'D') or bool(DOMAIN_NAME.match(name.strip()))
    is_enduser = bool(ENDUSER.search(name)) or bool(ENDUSER2.search(name)) or (bool(ENDUSER.search(typ)) and not BUYER.search(typ)) or \
        (not buyer_sig and bool(ENDUSER.search(' '.join(rec.get('heading_path') or []))))
    if is_enduser:
        return 'C', '终端用户 / 渠道触点（机场、大学、超市、政府、军队…走集成商与框架采购，不是 Saga 的直接买家）', flags + ['终端触点']
    if '聚合条目' in flags:
        return 'B', '聚合条目（一条里列了多家），研究时拆开再定', flags
    live = rec.get('emails_live') or []
    if iso in RISK:
        return 'B', f'{iso}：战争 / 结算风险，先 XB', flags + ['风险国']
    if not iso:
        return 'B', '国别未识别，待核后再定', flags + ['国别待核']
    buyer = bool(BUYER.search(name + ' ' + typ)) or rec.get('their_class') in ('A', 'B', 'C', 'D') or bool(DOMAIN_NAME.match(name.strip()))
    if iso in MAIN:
        if buyer and live:
            return 'A', '主攻区（美加/欧/土）+ 渠道型买家（分销/集成/安装/零售/OEM 品牌）+ 有邮箱', flags
        if buyer:
            return 'B', '主攻区渠道型买家，但来源库只给了官网/—，没有邮箱 → 先 XB，补到邮箱再升', flags + ['缺联系']
        return 'B', '主攻区，类型待核（来源库没写清是渠道还是终端）', flags + ['类型待核']
    if iso in SECOND:
        return 'B', f'{iso}：Simon 口径「一些俄/印/韩」→ XB 慢慢跟', flags
    return 'B', '对口但不在主攻区（美加/欧/土以外）→ XB', flags


def main():
    head, branch = git(['rev-parse', '--short', 'HEAD']), git(['rev-parse', '--abbrev-ref', 'HEAD'])
    occs, side = [], []
    # 1) profile/ 与 smartbyte/profile/（最厚，先进，作为主档）
    for d, tag in (('profile', 'profile'), ('smartbyte/profile', 'smartbyte/profile')):
        dd = os.path.join(REPO, d)
        for fn in sorted(os.listdir(dd)):
            if not fn.endswith('.md') or fn.startswith(('README', 'FINAL-REPORT')):
                continue
            fp = os.path.join(dd, fn)
            txt = open(fp, encoding='utf-8').read()
            multi = len(re.findall(r'^#{2,4} \d+\.', txt, flags=re.M)) >= 3 or fn.startswith(('new-customers', 'other-customers')) or re.search(r'-part\d|deep-mining|-parts', fn)
            if multi:
                oc, sd = parse_doc(fp, f'{d}/{fn}')
                for o in oc:
                    o.flags.append('profile批次文件')
                    if tag.startswith('smartbyte'):
                        o.flags.append('smartbyte子库')
                occs += oc
                side += sd
                continue
            o = parse_profile(fp, f'{d}/{fn}')
            if tag.startswith('smartbyte'):
                o.flags.append('smartbyte子库')
            occs.append(o)
    # 2) exhibition/
    ed = os.path.join(REPO, 'exhibition')
    for fn in sorted(os.listdir(ed)):
        if not fn.endswith('.md') or fn == 'README.md':
            continue
        p = os.path.join(ed, fn)
        if fn == 'other-exhibitors-batch.md':
            text = open(p, encoding='utf-8').read()
            parts = re.split(r'^(?=# )', text, flags=re.M)
            for k, part in enumerate(parts):
                if not part.startswith('# '):
                    continue
                tmp = os.path.join('/tmp', f'exh_{k}.md')
                open(tmp, 'w', encoding='utf-8').write(part)
                o = parse_profile(tmp, f'exhibition/{fn}')
                o.line = text[:text.find(part)].count('\n') + 1
                o.flags.append('展会档')
                occs.append(o)
        else:
            o = parse_profile(p, f'exhibition/{fn}')
            o.flags.append('展会档')
            occs.append(o)
    # 3) smartbyte/03 清单
    oc, sd = parse_doc(os.path.join(REPO, 'smartbyte/03-SmartByte海外客户开发清单.md'), 'smartbyte/03-SmartByte海外客户开发清单.md')
    for o in oc:
        o.flags.append('smartbyte子库')
    occs += oc
    side += sd
    # 4) 03 清单主文件
    oc, sd = parse_doc(os.path.join(REPO, '03-海外客户开发清单.md'), '03-海外客户开发清单.md')
    occs += oc
    side += sd
    # ---- 合并 ----
    recs, by_key = [], {}
    sdm = saga_domains()
    for o in occs:
        if not o.website:
            for u in urls_in(o.raw):
                dm = domain_of(u)
                if dm and dm not in GENERIC and not re.search(r'linkedin|facebook|google|amazon|alibaba|youtube|wikipedia|volza|importyeti|panjiva|europages|kompass|yellowpages|crunchbase|zoominfo|dnb|opencorporates|gov\.|\.gov|github|bing|baidu|hikvision|dahua|ubnt|mikrotik|tp-link|cisco|edge-core|smartbyte|hruitech|sagatele', dm):
                    o.website = dm
                    break
        dom = domain_of(o.website)
        if not dom:
            for e in o.emails:
                if e.split('@')[1] not in GENERIC:
                    dom = e.split('@')[1]
                    break
        key = ('d:' + dom) if dom else ('n:' + norm_key(o.name))
        if key in ('n:', 'd:'):
            continue
        alt = 'n:' + norm_key(o.name)
        tgt = by_key.get(key) or by_key.get(alt)
        if tgt is None:
            r = {'repo': 'CCTV-PoE', 'name': o.name, 'iso': o.iso, 'country_zh': iso_label(o.iso) if o.iso else (o.country_text or ''),
                 'country_text': o.country_text, 'city': kv_get(o.kv, '城市'), 'website': o.website, 'domain': dom, 'type': o.type,
                 'their_class': o.their_class, 'stars': o.stars, 'emails': [{'addr': e, 'status': '公开'} for e in o.emails],
                 'phones': o.phones, 'kv': dict(o.kv), 'raw': o.raw, 'notes': o.notes, 'flags': list(o.flags),
                 'src_path': o.src_file, 'src_line': o.line, 'heading_path': o.path, 'src_kind': o.kind, 'also': []}
            r['_votes'] = {}
            if o.iso:
                r['_votes'][o.iso] = {'field': 3, 'name': 2, 'ctx': 1}.get(o.iso_src, 1)
                r['_ctext'] = {o.iso: o.country_text}
            by_key[key] = r
            by_key.setdefault(alt, r)
            recs.append(r)
        else:
            r = tgt
            r['also'].append({'src_path': o.src_file, 'src_line': o.line, 'heading': ' > '.join(o.path[-2:]), 'kind': o.kind,
                              'raw': o.raw[:800], 'country_text': o.country_text, 'type': o.type, 'their_class': o.their_class})
            if o.iso:
                r['_votes'][o.iso] = r['_votes'].get(o.iso, 0) + {'field': 3, 'name': 2, 'ctx': 1}.get(o.iso_src, 1)
                r.setdefault('_ctext', {}).setdefault(o.iso, o.country_text)
            if not r['website'] and o.website:
                r['website'], r['domain'] = o.website, dom
            if not r['type'] and o.type:
                r['type'] = o.type
            if not r['their_class'] and o.their_class:
                r['their_class'] = o.their_class
            for e in o.emails:
                if e not in [x['addr'] for x in r['emails']]:
                    r['emails'].append({'addr': e, 'status': '公开'})
            for p in o.phones:
                if p not in r['phones']:
                    r['phones'].append(p)
            for k, v in o.kv.items():
                r['kv'].setdefault(k, v)
            for f in o.flags:
                if f not in r['flags']:
                    r['flags'].append(f)
            if dom and 'd:' + dom not in by_key:
                by_key['d:' + dom] = r
    for r in recs:
        votes = r.pop('_votes', {})
        ctext = r.pop('_ctext', {})
        if votes:
            best = sorted(votes.items(), key=lambda x: -x[1])[0][0]
            if best != r['iso']:
                r['flags'].append(f"国别多说法:{'/'.join(votes)}")
            r['iso'], r['country_zh'] = best, iso_label(best)
            if ctext.get(best):
                r['country_text'] = ctext[best]
            if len(votes) > 1 and f"国别多说法:{'/'.join(votes)}" not in r['flags']:
                r['flags'].append(f"国别多说法:{'/'.join(votes)}")
        r['src_repo_ref'] = f'elsasaga-cloud/CCTV-PoE@{head} ({branch})'
        r['emails_live'] = [e['addr'] for e in r['emails']]
        r['kp_named'] = False
        r['stage'] = ''
        doms = {r['domain']} | {e['addr'].split('@')[1] for e in r['emails']}
        doms = {d for d in doms if d and d not in GENERIC}
        r['saga_dup'] = None
        for d in sorted(doms):
            if d in sdm:
                r['saga_dup'] = {'code': sdm[d][0], 'grade': sdm[d][1], 'via': d}
                break
        r['touch'] = touch_of([e['addr'] for e in r['emails']])
        if r['touch']:
            r['flags'].append('S箱已群发')
        if len(r['also']) > 0:
            r['flags'].append(f"多处出现×{len(r['also']) + 1}")
        g, why, fl = classify(r)
        r['grade'], r['grade_reason'], r['flags'] = g, why, sorted(set(fl))
    kept = [r for r in recs if r['grade'] != 'DELETE']
    width = 4 if any(sum(1 for r in kept if r['grade'] == g) > 999 for g in 'ABC') else 3
    cnt = Counter()
    for r in recs:
        if r['grade'] == 'DELETE':
            r['code'] = ''
            continue
        cnt[r['grade']] += 1
        r['code'] = f"X{r['grade']}-C{cnt[r['grade']]:0{width}d}"
    os.makedirs(DATA, exist_ok=True)
    json.dump({'repo': 'CCTV-PoE', 'src': f'elsasaga-cloud/CCTV-PoE@{head}', 'branch': branch, 'count': len(recs), 'occurrences': len(occs),
               'records': recs}, open(os.path.join(DATA, 'cctv.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(DATA, 'cctv_非客户段落.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['file', 'line', 'heading', 'why'])
        for s in side:
            w.writerow([s['file'], s['line'], s['heading'], s['why']])
    with open(os.path.join(DATA, 'cctv_剔除大陆.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['name', 'country_text', 'type', 'src_path', 'src_line'])
        for r in recs:
            if r['grade'] == 'DELETE':
                w.writerow([r['name'], r['country_text'], r['type'], r['src_path'], r['src_line']])
    with open(os.path.join(DATA, 'cctv_未导入条目.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['file', 'line', 'kind', 'name', 'why', 'text'])
        for d in DROPPED:
            w.writerow([d['file'], d['line'], d['kind'], d['name'], d['why'], d['text']])
    print('cctv occurrences', len(occs), 'records', len(recs), dict(Counter(r['grade'] for r in recs)), 'side', len(side), 'dropped', len(DROPPED))
    print(Counter(d['why'] for d in DROPPED).most_common(8))
    print(Counter(r['grade_reason'][:30] for r in recs).most_common(12))
    print('kinds', Counter(r['src_kind'] for r in recs))
    print('iso top', Counter(r['iso'] for r in recs).most_common(25))


if __name__ == '__main__':
    main()
