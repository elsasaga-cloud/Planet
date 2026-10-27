#!/usr/bin/env python3
"""
MikroTik L2+ Access Layer Switch Scraper - Enhanced Version
抓取 MikroTik 所有 L2+ 接入层交换机的详细信息并导出 Excel
包含: 价格、芯片、端口配置、PoE、SFP、市场分类、工业温度、环网协议等
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter
import json
from urllib.parse import urljoin
import sys

# ============================================================
# 配置
# ============================================================
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://mikrotik.com/',
}

BASE_URL = 'https://mikrotik.com'
REQUEST_DELAY = 2.0   # 请求间隔秒数，礼貌爬虫


# ============================================================
# 网络层
# ============================================================
def get_session():
    session = requests.Session()
    session.headers.update(HEADERS)
    return session


def fetch_page(session, url, retries=4):
    """抓取页面，带指数退避重试"""
    for attempt in range(retries):
        try:
            print(f"    → GET {url}  (尝试 {attempt + 1}/{retries})")
            resp = session.get(url, timeout=30)
            if resp.status_code == 404:
                print(f"    ⚠️  404 Not Found: {url}")
                return None
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as e:
            print(f"    请求异常: {e}")
            if attempt < retries - 1:
                wait = 4 * (2 ** attempt)
                print(f"    等待 {wait}s 后重试...")
                time.sleep(wait)
    print(f"    ❌ 放弃: {url}")
    return None


# ============================================================
# 产品列表抓取
# ============================================================
def get_switch_product_links(session):
    """从官网产品列表页抓取所有交换机链接"""
    products = []
    seen_urls = set()

    list_pages = [
        'https://mikrotik.com/products/group/switches',
        'https://mikrotik.com/products/group/smart-switches',
    ]

    for page_url in list_pages:
        print(f"\n  📄 列表页: {page_url}")
        html = fetch_page(session, page_url)
        if not html:
            continue
        soup = BeautifulSoup(html, 'html.parser')

        for a in soup.find_all('a', href=True):
            href = a['href']
            if '/product/' not in href:
                continue
            full_url = urljoin(BASE_URL, href).split('?')[0].split('#')[0]
            if full_url in seen_urls:
                continue
            seen_urls.add(full_url)
            slug = href.split('/product/')[-1].strip('/')
            if slug:
                products.append({'name': slug, 'url': full_url})

    # ---- 已知型号补充清单（确保不遗漏）----
    known_models = [
        # CRS1xx
        'CRS106-1C-5S',
        'CRS112-8G-4S-IN',
        'CRS112-8P-4S-IN',
        # CRS2xx
        'CRS210-8G-2SplusIN',
        'CRS212-1G-10S-1SplusIN',
        # CRS3xx
        'CRS305-1G-4SplusIN',
        'CRS309-1G-8SplusIN',
        'CRS310-1G-5S-4SplusIN',
        'CRS310-8Gplus2SplusIN',
        'CRS312-4Cplus8XG',
        'CRS312-4Cplus8XGRM',
        'CRS317-1G-16SplusRM',
        'CRS318-1Fi-15Fr-2S',
        'CRS318-16P-2SplusRM',
        'CRS320-8P-8B-4SplusRM',
        'CRS326-4Cplus20Gplus2SplusRM',
        'CRS326-24G-2SplusIN',
        'CRS326-24G-2SplusRM',
        'CRS326-24S-2QplusRM',
        'CRS328-4C-20S-4SplusRM',
        'CRS328-24P-4SplusRM',
        'CRS332-32S-6CplusRM',
        # CRS5xx
        'CRS504-4XQ-IN',
        'CRS504-4XQ-OUT',
        'CRS510-8XS-2XQ-IN',
        'CRS518-16XS-2XQ-RM',
        # CSS
        'CSS106-5G-1S',
        'CSS106-1G-4P-1S',
        'CSS610-8G-2SplusIN',
        'CSS610-8P-2SplusIN',
        'CSS326-24G-2SplusRM',
        # netPower
        'netPower-15FR',
        'netPower-16P',
        'netPower-Lite-7R',
    ]
    for model in known_models:
        url = f'{BASE_URL}/product/{model}'
        if url not in seen_urls:
            seen_urls.add(url)
            products.append({'name': model, 'url': url})

    print(f"\n  ✅ 共 {len(products)} 个候选产品")
    return products


# ============================================================
# 价格抓取 - 专用函数
# ============================================================
def fetch_price(session, product_slug):
    """
    尝试多种方式获取价格:
    1. 产品页面直接抓取
    2. MikroTik Store API / JSON
    3. 页面内嵌 JSON-LD / microdata
    """
    price = 'N/A'

    # --- 方式1: 直接从产品页 HTML 抓取 ---
    urls_to_try = [
        f'{BASE_URL}/product/{product_slug}',
        f'{BASE_URL}/store/product/{product_slug}',
    ]

    for url in urls_to_try:
        html = fetch_page(session, url)
        if not html:
            continue
        soup = BeautifulSoup(html, 'html.parser')

        # 1a. JSON-LD Product schema
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                data = json.loads(script.string or '{}')
                # 可能是列表
                items = data if isinstance(data, list) else [data]
                for item in items:
                    if item.get('@type') in ('Product', 'Offer'):
                        offers = item.get('offers', item)
                        if isinstance(offers, dict):
                            p = offers.get('price') or offers.get('lowPrice')
                            currency = offers.get('priceCurrency', 'USD')
                            if p:
                                price = f"{currency} {p}"
                                return price
                        elif isinstance(offers, list) and offers:
                            p = offers[0].get('price')
                            currency = offers[0].get('priceCurrency', 'USD')
                            if p:
                                price = f"{currency} {p}"
                                return price
            except Exception:
                pass

        # 1b. meta itemprop=price
        meta_price = soup.find('meta', itemprop='price')
        if meta_price and meta_price.get('content'):
            currency_meta = soup.find('meta', itemprop='priceCurrency')
            currency = currency_meta.get('content', 'USD') if currency_meta else 'USD'
            price = f"{currency} {meta_price['content']}"
            return price

        # 1c. span/div itemprop=price
        price_elem = soup.find(itemprop='price')
        if price_elem:
            raw = price_elem.get('content') or price_elem.get_text(strip=True)
            if raw:
                price = f"USD {raw}"
                return price

        # 1d. 常见 CSS class 匹配
        price_selectors = [
            {'class': re.compile(r'price', re.I)},
            {'class': re.compile(r'cost', re.I)},
            {'id': re.compile(r'price', re.I)},
        ]
        for sel in price_selectors:
            elems = soup.find_all(['span', 'div', 'p', 'strong', 'b'], attrs=sel)
            for elem in elems:
                text = elem.get_text(strip=True)
                # 匹配 $xx.xx 或 xx.xx USD 格式
                m = re.search(r'[\$€£]?\s*(\d[\d,]*\.?\d*)\s*(USD|EUR|GBP)?', text)
                if m:
                    amount = m.group(1).replace(',', '')
                    try:
                        if 1.0 < float(amount) < 100000:
                            currency = m.group(2) or 'USD'
                            price = f"{currency} {amount}"
                            return price
                    except ValueError:
                        pass

        # 1e. 全页正则扫描价格模式
        page_text = soup.get_text()
        price_patterns = [
            r'\$\s*(\d[\d,]*\.?\d*)',
            r'USD\s*(\d[\d,]*\.?\d*)',
            r'Price[:\s]+\$?\s*(\d[\d,]*\.?\d*)',
            r'(\d[\d,]*\.?\d*)\s*USD',
        ]
        for pat in price_patterns:
            m = re.search(pat, page_text, re.I)
            if m:
                amount = m.group(1).replace(',', '')
                try:
                    val = float(amount)
                    if 1.0 < val < 100000:
                        price = f"USD {val:.2f}"
                        return price
                except ValueError:
                    pass

    # --- 方式2: MikroTik API (部分型号有 JSON API) ---
    api_urls = [
        f'https://mikrotik.com/api/products/{product_slug}',
        f'https://mikrotik.com/product/{product_slug}?format=json',
    ]
    for api_url in api_urls:
        try:
            resp = session.get(api_url, timeout=15)
            if resp.status_code == 200:
                try:
                    data = resp.json()
                    p = (data.get('price') or data.get('Price') or
                         data.get('msrp') or data.get('retail_price'))
                    if p:
                        price = f"USD {p}"
                        return price
                except Exception:
                    pass
        except Exception:
            pass

    return price


# ============================================================
# 单产品页面解析
# ============================================================
def parse_product_page(session, product_info):
    """
    解析产品详情页，提取所有规格字段
    返回: dict 或 None (非交换机/页面不存在)
    """
    url = product_info['url']
    html = fetch_page(session, url)
    if not html:
        return None

    soup = BeautifulSoup(html, 'html.parser')
    page_text = soup.get_text(separator='\n')

    # ---------- 初始化结果 ----------
    R = {
        # 基础标识
        'product_name':           'N/A',
        'product_code':           'N/A',
        'product_url':            url,
        'price':                  'N/A',
        'description':            'N/A',

        # 市场/分类
        'market_category':        'N/A',   # Enterprise / SMB / ISP / Carrier / SOHO
        'product_series':         'N/A',   # CRS / CSS / netPower

        # 芯片
        'switch_chip_model':      'N/A',
        'switch_chip_ports':      'N/A',
        'cpu':                    'N/A',
        'cpu_core_count':         'N/A',
        'cpu_frequency':          'N/A',

        # 内存/存储
        'ram':                    'N/A',
        'storage':                'N/A',

        # 端口配置
        'port_configuration':     'N/A',   # 详细端口描述
        'total_ports':            'N/A',
        'ethernet_ports':         'N/A',   # RJ45 GbE 数量
        'eth_2_5g_ports':         'N/A',   # 2.5G 端口
        'eth_10g_ports':          'N/A',   # 10G RJ45
        'sfp_ports':              'N/A',   # 1G SFP 数量
        'sfp_plus_ports':         'N/A',   # 10G SFP+ 数量
        'sfp28_ports':            'N/A',   # 25G SFP28 数量
        'qsfp_ports':             'N/A',   # 40G QSFP+ 数量
        'qsfp28_ports':           'N/A',   # 100G QSFP28 数量
        'combo_ports':            'N/A',   # Combo 端口
        'fiber_ports':            'N/A',   # 光纤 Fast Ethernet

        # PoE
        'poe_in':                 'N/A',   # PoE 供电输入
        'poe_out':                'N/A',   # PoE 输出类型
        'poe_budget':             'N/A',   # PoE 功率预算 (W)

        # 上联
        'uplink':                 'N/A',   # 上联端口描述

        # 操作系统 / 协议
        'operating_system':       'N/A',
        'ring_protocol':          'N/A',   # STP/RSTP/MSTP/ERPS/Ring
        'switch_chip_features':   'N/A',

        # 工业级
        'industrial_temp':        'N/A',   # Yes / No
        'operating_temperature':  'N/A',

        # 电源
        'max_power_consumption':  'N/A',
        'psu':                    'N/A',

        # 物理
        'dimensions':             'N/A',
        'weight':                 'N/A',
        'form_factor':            'N/A',   # Desktop / 1U Rack / Outdoor

        # 内部标记
        'is_switch':              False,
        'is_l2_plus':             False,
    }

    # ---------- 产品名 ----------
    h1 = soup.find('h1')
    R['product_name'] = h1.get_text(strip=True) if h1 else product_info['name']

    # 检查 404
    if ('404' in R['product_name'] or
            'not found' in page_text.lower()[:300] or
            'page not found' in page_text.lower()[:300]):
        print(f"    ⚠️  404: {url}")
        return None

    # ---------- 判断是否是交换机 ----------
    sw_keywords = ['switch chip', 'CRS', 'CSS', 'netPower',
                   'Cloud Router Switch', 'Cloud Smart Switch',
                   'SwOS', 'switching capacity']
    R['is_switch'] = any(kw.lower() in page_text.lower() for kw in sw_keywords)
    if not R['is_switch']:
        # 从 URL / 名称判断
        if re.search(r'\bCRS|CSS|netPower', url, re.I):
            R['is_switch'] = True
    if not R['is_switch']:
        return None

    # ---------- 收集所有键值对规格 ----------
    specs = {}  # key(lower) -> value

    # 方法A: <table>
    for table in soup.find_all('table'):
        for row in table.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            if len(cells) >= 2:
                k = cells[0].get_text(separator=' ', strip=True)
                v = cells[-1].get_text(separator=' ', strip=True)
                if k and v:
                    specs[k.lower()] = v

    # 方法B: <dl><dt><dd>
    for dl in soup.find_all('dl'):
        dts = dl.find_all('dt')
        dds = dl.find_all('dd')
        for dt, dd in zip(dts, dds):
            k = dt.get_text(strip=True)
            v = dd.get_text(strip=True)
            if k and v:
                specs[k.lower()] = v

    # 方法C: div 配对 (label + value)
    for container in soup.find_all('div', class_=re.compile(
            r'spec|param|detail|property|row|field', re.I)):
        parts = container.find_all(['div', 'span'],
                                   class_=re.compile(r'label|name|key|title|left', re.I))
        vals  = container.find_all(['div', 'span'],
                                   class_=re.compile(r'value|data|right|content', re.I))
        for lbl, val in zip(parts, vals):
            k = lbl.get_text(strip=True)
            v = val.get_text(strip=True)
            if k and v:
                specs[k.lower()] = v

    # ---------- 从 specs 字典填充字段 ----------
    FIELD_MAP = {
        # (目标字段, [关键词列表])
        'switch_chip_model':     ['switch chip model', 'switch chip'],
        'switch_chip_ports':     ['switch chip ports'],
        'cpu':                   ['cpu', 'processor'],
        'cpu_core_count':        ['cpu core count', 'core count'],
        'cpu_frequency':         ['cpu nominal frequency', 'cpu frequency'],
        'ram':                   ['size of ram', 'ram'],
        'storage':               ['storage size', 'flash', 'storage'],
        'operating_system':      ['operating system'],
        'max_power_consumption': ['max power consumption', 'maximum power consumption'],
        'poe_budget':            ['poe out budget', 'poe-out budget', 'total poe'],
        'dimensions':            ['dimensions'],
        'weight':                ['weight'],
        'operating_temperature': ['operating temperature', 'tested ambient temperature'],
        'product_code':          ['product code'],
        'psu':                   ['power supply', 'psu', 'power input'],
    }

    for field, keywords in FIELD_MAP.items():
        if R[field] != 'N/A':
            continue
        for kw in keywords:
            for sk, sv in specs.items():
                if kw in sk:
                    R[field] = sv
                    break
            if R[field] != 'N/A':
                break

    # PoE 特殊处理
    for sk, sv in specs.items():
        if 'poe' in sk:
            if 'budget' in sk or 'output' in sk:
                R['poe_budget'] = sv
            elif 'in' in sk and R['poe_in'] == 'N/A':
                R['poe_in'] = sv
            elif 'out' in sk and R['poe_out'] == 'N/A':
                R['poe_out'] = sv
            elif R['poe_out'] == 'N/A':
                R['poe_out'] = sv

    # ---------- 正则兜底从全文提取 ----------
    regex_map = {
        'switch_chip_model':     [
            r'Switch [Cc]hip [Mm]odel[:\s]+([^\n]+)',
            r'Switch [Cc]hip[:\s]+([^\n]+)',
            r'\b(98DX\w+)\b',
            r'\b(QCA8\w+)\b',
            r'\b(RTL83\w+|RTL93\w+)\b',
            r'\b(BCM5\w+|BCM6\w+)\b',
            r'\b(MT7\w{3,})\b',
        ],
        'cpu':                   [r'CPU[:\s]+([^\n]+)', r'Processor[:\s]+([^\n]+)'],
        'cpu_core_count':        [r'CPU [Cc]ore [Cc]ount[:\s]+(\d+)', r'[Cc]ore [Cc]ount[:\s]+(\d+)'],
        'cpu_frequency':         [r'CPU (?:[Nn]ominal )?[Ff]requency[:\s]+([^\n]+)'],
        'ram':                   [r'(?:Size of )?RAM[:\s]+([^\n]+)'],
        'storage':               [r'(?:Storage|Flash)[:\s]+([^\n]+)'],
        'operating_system':      [r'Operating [Ss]ystem[:\s]+([^\n]+)'],
        'max_power_consumption': [r'Max(?:imum)? [Pp]ower [Cc]onsumption[:\s]+([^\n]+)'],
        'poe_budget':            [r'PoE[- ]?[Oo]ut [Bb]udget[:\s]+([^\n]+)',
                                  r'Total PoE[:\s]+([^\n]+)'],
        'dimensions':            [r'Dimensions?[:\s]+([^\n]+)'],
        'weight':                [r'Weight[:\s]+([^\n]+)'],
        'operating_temperature': [r'(?:Operating|Tested [Aa]mbient) [Tt]emperature[:\s]+([^\n]+)'],
        'product_code':          [r'Product [Cc]ode[:\s]+([A-Z0-9\-\+]+)'],
    }

    for field, patterns in regex_map.items():
        if R[field] != 'N/A':
            continue
        for pat in patterns:
            m = re.search(pat, page_text, re.MULTILINE)
            if m:
                val = m.group(1).strip().rstrip('.')
                if val and len(val) < 200:
                    R[field] = val
                    break

    # ---------- 端口解析 ----------
    _parse_ports(R, soup, page_text)

    # ---------- 价格 ----------
    R['price'] = _extract_price(soup, page_text)

    # ---------- 上联端口 ----------
    R['uplink'] = _detect_uplink(R)

    # ---------- PoE 总结 ----------
    _parse_poe(R, page_text, soup)

    # ---------- 环网协议 ----------
    ring_protos = []
    for kw in ['STP', 'RSTP', 'MSTP', 'ERPS', 'G.8032', 'Ring protocol',
               'Rapid Ring', 'ITU-T G.8032']:
        if kw.lower() in page_text.lower():
            ring_protos.append(kw)
    R['ring_protocol'] = ', '.join(ring_protos) if ring_protos else 'STP/RSTP'

    # ---------- 工业温度 ----------
    temp_str = R['operating_temperature']
    R['industrial_temp'] = _check_industrial_temp(temp_str, page_text)

    # ---------- 外形 ----------
    R['form_factor'] = _detect_form_factor(R['product_name'], page_text)

    # ---------- 市场分类 ----------
    R['market_category'] = _detect_market_category(R)

    # ---------- 产品系列 ----------
    name_upper = R['product_name'].upper()
    if 'CRS' in name_upper:
        R['product_series'] = 'CRS (Cloud Router Switch)'
    elif 'CSS' in name_upper:
        R['product_series'] = 'CSS (Cloud Smart Switch)'
    elif 'NETPOWER' in name_upper:
        R['product_series'] = 'netPower'
    else:
        R['product_series'] = 'Other'

    # ---------- 芯片特性 ----------
    feature_kws = ['VLAN', 'QoS', 'ACL', 'STP', 'RSTP', 'MSTP', 'LACP',
                   'IGMP snooping', 'port mirroring', 'rate limiting',
                   'jumbo frame', 'link aggregation', '802.1Q', '802.1p',
                   '802.1w', 'spanning tree', 'bonding', 'HW offload',
                   'hardware offload', 'CRC']
    found = [kw for kw in feature_kws if kw.lower() in page_text.lower()]
    R['switch_chip_features'] = ', '.join(found) if found else 'N/A'

    # ---------- L2+ 判断 ----------
    l2_kws = ['VLAN', 'QoS', 'ACL', 'IGMP', 'STP', 'RSTP', 'MSTP', 'LACP',
              '802.1Q', 'switch chip', 'SwOS', 'switching']
    R['is_l2_plus'] = any(kw.lower() in page_text.lower() for kw in l2_kws)
    if re.search(r'\b(CRS|CSS|netPower)\b', R['product_name'], re.I):
        R['is_l2_plus'] = True

    # ---------- 描述 ----------
    meta = soup.find('meta', attrs={'name': 'description'})
    if meta and meta.get('content'):
        R['description'] = meta['content'][:400]
    else:
        p_tag = soup.find('p')
        if p_tag:
            R['description'] = p_tag.get_text(strip=True)[:400]

    # ---------- 端口配置字符串 ----------
    R['port_configuration'] = _build_port_config_string(R)

    return R


# ============================================================
# 辅助解析函数
# ============================================================
def _extract_price(soup, page_text):
    """从已加载页面提取价格"""
    # 1. JSON-LD
    for script in soup.find_all('script', type='application/ld+json'):
        try:
            data = json.loads(script.string or '{}')
            items = data if isinstance(data, list) else [data]
            for item in items:
                offers = item.get('offers', {})
                if isinstance(offers, list):
                    offers = offers[0] if offers else {}
                p = offers.get('price') or offers.get('lowPrice')
                currency = offers.get('priceCurrency', 'USD')
                if p:
                    return f"{currency} {p}"
        except Exception:
            pass

    # 2. meta itemprop
    meta_p = soup.find('meta', itemprop='price')
    if meta_p and meta_p.get('content'):
        meta_c = soup.find('meta', itemprop='priceCurrency')
        cur = meta_c.get('content', 'USD') if meta_c else 'USD'
        return f"{cur} {meta_p['content']}"

    # 3. itemprop=price 元素
    pe = soup.find(attrs={'itemprop': 'price'})
    if pe:
        raw = pe.get('content') or pe.get_text(strip=True)
        if raw:
            return f"USD {raw}"

    # 4. class 含 price 的元素
    for tag in soup.find_all(['span', 'div', 'p', 'strong'],
                              class_=re.compile(r'\bprice\b|\bcost\b|\bmsrp\b', re.I)):
        txt = tag.get_text(strip=True)
        m = re.search(r'[\$€£]?\s*(\d[\d,]*\.?\d*)\s*(USD|EUR|GBP)?', txt)
        if m:
            try:
                val = float(m.group(1).replace(',', ''))
                if 1.0 < val < 99999:
                    cur = m.group(2) or 'USD'
                    return f"{cur} {val:.2f}"
            except ValueError:
                pass

    # 5. 全文正则
    patterns = [
        r'\$\s*(\d[\d,]*\.?\d*)',
        r'USD\s+(\d[\d,]*\.?\d*)',
        r'Price[:\s]+\$?\s*(\d[\d,]*\.?\d*)',
        r'(\d[\d,]*\.?\d*)\s*USD',
        r'Retail[:\s]+\$?\s*(\d[\d,]*\.?\d*)',
        r'MSRP[:\s]+\$?\s*(\d[\d,]*\.?\d*)',
    ]
    for pat in patterns:
        m = re.search(pat, page_text, re.I)
        if m:
            try:
                val = float(m.group(1).replace(',', ''))
                if 1.0 < val < 99999:
                    return f"USD {val:.2f}"
            except ValueError:
                pass

    return 'N/A'


def _parse_ports(R, soup, page_text):
    """解析各类端口数量"""

    # 模式字典: (字段, 正则列表)
    port_patterns = {
        'ethernet_ports': [
            r'(\d+)\s*[xX×]\s*(?:10/100/1000|Gigabit Ethernet|1000BASE|1GbE|GbE)\b',
            r'(\d+)\s*(?:Gigabit|GbE)\s*(?:Ethernet\s*)?[Pp]ort',
        ],
        'eth_2_5g_ports': [
            r'(\d+)\s*[xX×]\s*(?:2\.5G|2500BASE|2\.5GbE|2\.5\s*Gbps)',
        ],
        'eth_10g_ports': [
            r'(\d+)\s*[xX×]\s*(?:10G\s*RJ45|10GBASE-T|10GbE\s*RJ45)',
        ],
        'sfp_ports': [
            r'(\d+)\s*[xX×]\s*SFP(?!\+|28)',
            r'(\d+)\s*SFP(?!\+|28)\s*(?:port|cage|slot)',
        ],
        'sfp_plus_ports': [
            r'(\d+)\s*[xX×]\s*SFP\+',
            r'(\d+)\s*SFP\+\s*(?:port|cage|slot)',
        ],
        'sfp28_ports': [
            r'(\d+)\s*[xX×]\s*SFP28',
        ],
        'qsfp_ports': [
            r'(\d+)\s*[xX×]\s*QSFP\+',
            r'(\d+)\s*QSFP\+\s*(?:port)',
        ],
        'qsfp28_ports': [
            r'(\d+)\s*[xX×]\s*(?:QSFP28|100G)',
        ],
        'combo_ports': [
            r'(\d+)\s*[xX×]?\s*[Cc]ombo',
            r'(\d+)\s*[Cc]ombo\s*(?:port)',
        ],
        'fiber_ports': [
            r'(\d+)\s*[xX×]\s*(?:100M\s*[Ff]iber|Fast\s*Ethernet\s*[Ff]iber|Fr\b)',
        ],
    }

    for field, pats in port_patterns.items():
        if R[field] != 'N/A':
            continue
        for pat in pats:
            m = re.search(pat, page_text, re.I)
            if m:
                R[field] = m.group(1)
                break

    # 从产品名解析 (eg: CRS326-24G-2S+IN -> 24G, 2S+)
    name = R['product_name']
    name_parts = re.findall(r'(\d+)(G\+?|S\+?|S28|XS|XQ|XG|P|B|C\+?|Fi|Fr)', name, re.I)
    for count, suffix in name_parts:
        s = suffix.upper()
        if s in ('G',) and R['ethernet_ports'] == 'N/A':
            R['ethernet_ports'] = count
        elif s in ('G+',) and R['eth_2_5g_ports'] == 'N/A':
            R['eth_2_5g_ports'] = count
        elif s == 'XG' and R['eth_10g_ports'] == 'N/A':
            R['eth_10g_ports'] = count
        elif s == 'S' and R['sfp_ports'] == 'N/A':
            R['sfp_ports'] = count
        elif s in ('S+', 'XS') and R['sfp_plus_ports'] == 'N/A':
            R['sfp_plus_ports'] = count
        elif s == 'S28' and R['sfp28_ports'] == 'N/A':
            R['sfp28_ports'] = count
        elif s == 'XQ' and R['qsfp28_ports'] == 'N/A':
            R['qsfp28_ports'] = count
        elif s == 'Q' and R['qsfp_ports'] == 'N/A':
            R['qsfp_ports'] = count
        elif s in ('C', 'C+') and R['combo_ports'] == 'N/A':
            R['combo_ports'] = count
        elif s == 'FI' and R['fiber_ports'] == 'N/A':
            pass
        elif s == 'FR' and R['fiber_ports'] == 'N/A':
            R['fiber_ports'] = count


def _build_port_config_string(R):
    """构建端口配置描述字符串"""
    parts = []
    port_fields = [
        (R['ethernet_ports'],  'x GbE RJ45'),
        (R['eth_2_5g_ports'],  'x 2.5GbE'),
        (R['eth_10g_ports'],   'x 10GbE RJ45'),
        (R['fiber_ports'],     'x 100M Fiber'),
        (R['combo_ports'],     'x Combo'),
        (R['sfp_ports'],       'x SFP'),
        (R['sfp_plus_ports'],  'x SFP+'),
        (R['sfp28_ports'],     'x SFP28'),
        (R['qsfp_ports'],      'x QSFP+'),
        (R['qsfp28_ports'],    'x QSFP28'),
    ]
    for count, label in port_fields:
        if count != 'N/A' and count != '0':
            parts.append(f"{count}{label}")

    # 计算总端口数
    total = 0
    for count, _ in port_fields:
        try:
            total += int(count)
        except (ValueError, TypeError):
            pass
    if total > 0:
        R['total_ports'] = str(total)

    return ', '.join(parts) if parts else 'N/A'


def _parse_poe(R, page_text, soup):
    """解析 PoE 信息"""
    text_lower = page_text.lower()

    if 'poe' not in text_lower:
        return

    # PoE-in
    if R['poe_in'] == 'N/A':
        if 'poe-in' in text_lower or 'powered from poe' in text_lower:
            R['poe_in'] = 'PoE-in supported'
        elif 'passive poe' in text_lower and 'in' in text_lower:
            R['poe_in'] = 'Passive PoE-in'

    # PoE-out
    if R['poe_out'] == 'N/A':
        if '802.3bt' in page_text:
            R['poe_out'] = 'PoE+ (802.3bt)'
        elif '802.3at' in page_text:
            R['poe_out'] = 'PoE+ (802.3at)'
        elif '802.3af' in page_text:
            R['poe_out'] = 'PoE (802.3af)'
        elif 'passive poe' in text_lower:
            R['poe_out'] = 'Passive PoE'
        elif 'reverse poe' in text_lower:
            R['poe_out'] = 'Reverse PoE (input)'
        elif 'poe out' in text_lower or 'poe-out' in text_lower:
            R['poe_out'] = 'PoE-out'


def _detect_uplink(R):
    """根据端口信息推断上联端口"""
    parts = []
    if R['sfp28_ports'] != 'N/A':
        parts.append(f"{R['sfp28_ports']}x SFP28 (25G)")
    if R['sfp_plus_ports'] != 'N/A':
        parts.append(f"{R['sfp_plus_ports']}x SFP+ (10G)")
    if R['qsfp28_ports'] != 'N/A':
        parts.append(f"{R['qsfp28_ports']}x QSFP28 (100G)")
    if R['qsfp_ports'] != 'N/A':
        parts.append(f"{R['qsfp_ports']}x QSFP+ (40G)")
    if R['sfp_ports'] != 'N/A':
        parts.append(f"{R['sfp_ports']}x SFP (1G)")
    return ', '.join(parts) if parts else 'N/A'


def _check_industrial_temp(temp_str, page_text):
    """判断是否工业级温度 (-40°C 及以下视为工业级)"""
    if temp_str != 'N/A':
        m = re.search(r'(-\d+)', temp_str)
        if m:
            try:
                low = int(m.group(1))
                if low <= -40:
                    return 'Yes (-40°C)'
                elif low <= -20:
                    return 'No (-20°C)'
            except ValueError:
                pass
    if '-40' in page_text:
        return 'Yes (-40°C)'
    if '-20' in page_text:
        return 'No (-20°C)'
    return 'N/A'


def _detect_form_factor(product_name, page_text):
    """判断外形规格"""
    name_lower = product_name.lower()
    text_lower = page_text.lower()
    if 'rm' in name_lower or '1u' in text_lower or 'rack' in text_lower or 'rackmount' in text_lower:
        return '1U Rack'
    if 'out' in name_lower or 'outdoor' in text_lower:
        return 'Outdoor'
    if 'din' in text_lower:
        return 'DIN Rail'
    return 'Desktop'


def _detect_market_category(R):
    """推断市场定位"""
    name = R['product_name'].upper()
    # 100G 以上 -> Carrier/Data Center
    if R['qsfp28_ports'] != 'N/A' or R['sfp28_ports'] != 'N/A':
        return 'Data Center / Carrier'
    # 10G 上联
    if R['sfp_plus_ports'] != 'N/A':
        try:
            if int(R['sfp_plus_ports']) >= 16:
                return 'Enterprise / ISP'
            elif int(R['sfp_plus_ports']) >= 8:
                return 'Enterprise'
            else:
                return 'SMB / Enterprise'
        except ValueError:
            pass
    # PoE
    if R['poe_out'] != 'N/A':
        return 'SMB / Access'
    # CSS 系列
    if 'CSS' in name:
        return 'SMB / SOHO'
    return 'SMB'


# ============================================================
# 导出 Excel
# ============================================================
def export_to_excel(products, filename='MikroTik_L2Plus_Switches.xlsx'):
    """导出到 Excel，多 Sheet"""

    wb = openpyxl.Workbook()

    # ===== Sheet 1: 完整数据 =====
    ws = wb.active
    ws.title = 'All Switches'

    # 列定义: (标题, 字段key, 宽度)
    COLUMNS = [
        ('序号',               None,                    6),
        ('产品名称',            'product_name',          32),
        ('产品系列',            'product_series',        22),
        ('市场定位',            'market_category',       20),
        ('产品代码',            'product_code',          22),
        ('价格 (USD)',          'price',                 14),
        ('产品页面',            'product_url',           50),
        ('Switch Chip 型号',   'switch_chip_model',     20),
        ('Switch Chip 端口数', 'switch_chip_ports',     14),
        ('CPU / 处理器',        'cpu',                   22),
        ('CPU 核心数',          'cpu_core_count',        10),
        ('CPU 频率',            'cpu_frequency',         13),
        ('RAM',                'ram',                   10),
        ('存储',               'storage',               10),
        ('端口配置',            'port_configuration',    38),
        ('总端口数',            'total_ports',            9),
        ('GbE RJ45',           'ethernet_ports',         9),
        ('2.5GbE',             'eth_2_5g_ports',         9),
        ('10GbE RJ45',         'eth_10g_ports',          9),
        ('SFP (1G)',            'sfp_ports',              9),
        ('SFP+ (10G)',          'sfp_plus_ports',         9),
        ('SFP28 (25G)',         'sfp28_ports',            9),
        ('QSFP+ (40G)',         'qsfp_ports',             9),
        ('QSFP28 (100G)',       'qsfp28_ports',           9),
        ('Combo 端口',          'combo_ports',            9),
        ('光纤端口',             'fiber_ports',            9),
        ('上联端口',             'uplink',                24),
        ('PoE 输入',            'poe_in',                18),
        ('PoE 输出',            'poe_out',               20),
        ('PoE 功率预算',         'poe_budget',            14),
        ('操作系统',             'operating_system',      18),
        ('环网协议',             'ring_protocol',         20),
        ('工业级温度',           'industrial_temp',       13),
        ('工作温度范围',          'operating_temperature', 20),
        ('最大功耗',             'max_power_consumption', 12),
        ('外形规格',             'form_factor',           12),
        ('尺寸',                'dimensions',            28),
        ('重量',                'weight',                10),
        ('芯片支持特性',          'switch_chip_features',  45),
        ('产品描述',             'description',           55),
    ]

    # 样式
    HDR_FONT   = Font(name='Calibri', bold=True, color='FFFFFF', size=10)
    HDR_FILL   = PatternFill('solid', fgColor='1F4E79')
    HDR_ALIGN  = Alignment(horizontal='center', vertical='center', wrap_text=True)
    DATA_FONT  = Font(name='Calibri', size=9)
    DATA_ALIGN = Alignment(horizontal='left', vertical='center', wrap_text=True)
    URL_FONT   = Font(name='Calibri', size=9, color='0563C1', underline='single')
    CHIP_FONT  = Font(name='Calibri', size=9, bold=True, color='843C0C')
    PRICE_FONT = Font(name='Calibri', size=9, bold=True, color='375623')
    THIN       = Border(left=Side(style='thin'),   right=Side(style='thin'),
                        top=Side(style='thin'),    bottom=Side(style='thin'))
    ALT_FILL   = PatternFill('solid', fgColor='EBF3FB')
    CHIP_FILL  = PatternFill('solid', fgColor='FFF2CC')
    PRICE_FILL = PatternFill('solid', fgColor='E2EFDA')

    # 写表头
    for ci, (title, _, width) in enumerate(COLUMNS, 1):
        c = ws.cell(row=1, column=ci, value=title)
        c.font      = HDR_FONT
        c.fill      = HDR_FILL
        c.alignment = HDR_ALIGN
        c.border    = THIN
        ws.column_dimensions[get_column_letter(ci)].width = width

    ws.row_dimensions[1].height = 32
    ws.freeze_panes = 'A2'
    ws.auto_filter.ref = f'A1:{get_column_letter(len(COLUMNS))}1'

    # 写数据
    for ri, prod in enumerate(products, 2):
        for ci, (_, field, _) in enumerate(COLUMNS, 1):
            if field is None:
                val = str(ri - 1)
            else:
                val = str(prod.get(field, 'N/A'))

            c = ws.cell(row=ri, column=ci, value=val)
            c.border = THIN

            # 默认样式
            c.font      = DATA_FONT
            c.alignment = DATA_ALIGN

            # 交替行底色
            if ri % 2 == 0:
                c.fill = ALT_FILL

            # 特殊列样式
            col_title = COLUMNS[ci - 1][0]
            if col_title == '产品页面':
                c.font      = URL_FONT
                c.hyperlink = val
                c.fill      = ALT_FILL if ri % 2 == 0 else PatternFill()
            elif col_title == 'Switch Chip 型号' and val not in ('N/A', ''):
                c.fill = CHIP_FILL
                c.font = CHIP_FONT
            elif col_title == '价格 (USD)' and val not in ('N/A', ''):
                c.fill = PRICE_FILL
                c.font = PRICE_FONT

        ws.row_dimensions[ri].height = 22

    # ===== Sheet 2: 芯片汇总 =====
    ws2 = wb.create_sheet('芯片型号汇总')
    chip_map = {}
    for p in products:
        chip = p.get('switch_chip_model', 'N/A')
        if chip != 'N/A':
            chip_map.setdefault(chip, []).append(p['product_name'])

    s2_cols = [('芯片型号', 22), ('产品数量', 10), ('对应产品列表', 90)]
    for ci, (title, width) in enumerate(s2_cols, 1):
        c = ws2.cell(row=1, column=ci, value=title)
        c.font = HDR_FONT; c.fill = HDR_FILL
        c.alignment = HDR_ALIGN; c.border = THIN
        ws2.column_dimensions[get_column_letter(ci)].width = width

    ws2.row_dimensions[1].height = 28
    ws2.freeze_panes = 'A2'

    for ri, (chip, pnames) in enumerate(
            sorted(chip_map.items(), key=lambda x: -len(x[1])), 2):
        ws2.cell(row=ri, column=1, value=chip).border = THIN
        ws2.cell(row=ri, column=1).font = Font(name='Calibri', size=9, bold=True)
        ws2.cell(row=ri, column=2, value=len(pnames)).border = THIN
        ws2.cell(row=ri, column=2).alignment = Alignment(horizontal='center')
        ws2.cell(row=ri, column=3, value=', '.join(pnames)).border = THIN
        ws2.cell(row=ri, column=3).alignment = Alignment(wrap_text=True)
        ws2.row_dimensions[ri].height = 18

    # ===== Sheet 3: 价格清单 =====
    ws3 = wb.create_sheet('价格清单')
    priced = [(p['product_name'], p.get('price', 'N/A'),
               p.get('port_configuration', 'N/A'),
               p.get('switch_chip_model', 'N/A'),
               p.get('product_url', ''))
              for p in products]
    priced_sort = sorted(priced, key=lambda x: (
        0 if x[1] == 'N/A' else 1,
        _price_sort_key(x[1])
    ))

    p3_cols = [('产品名称', 32), ('价格', 14), ('端口配置', 38),
               ('Switch Chip', 20), ('产品链接', 50)]
    for ci, (title, width) in enumerate(p3_cols, 1):
        c = ws3.cell(row=1, column=ci, value=title)
        c.font = HDR_FONT; c.fill = HDR_FILL
        c.alignment = HDR_ALIGN; c.border = THIN
        ws3.column_dimensions[get_column_letter(ci)].width = width

    ws3.freeze_panes = 'A2'
    ws3.row_dimensions[1].height = 28

    for ri, (name, price, ports, chip, url_p) in enumerate(priced_sort, 2):
        row_data = [name, price, ports, chip, url_p]
        for ci, val in enumerate(row_data, 1):
            c = ws3.cell(row=ri, column=ci, value=str(val))
            c.border = THIN
            c.font = DATA_FONT
            c.alignment = DATA_ALIGN
            if ri % 2 == 0:
                c.fill = ALT_FILL
            if ci == 2 and val not in ('N/A', ''):
                c.fill = PRICE_FILL
                c.font = PRICE_FONT
            if ci == 5:
                c.font = URL_FONT
                c.hyperlink = str(val)
        ws3.row_dimensions[ri].height = 18

    wb.save(filename)
    print(f"\n  💾 已保存: {filename}")
    return filename


def _price_sort_key(price_str):
    """将价格字符串转为可排序数字"""
    if price_str in ('N/A', ''):
        return 999999
    m = re.search(r'(\d[\d,]*\.?\d*)', price_str)
    if m:
        try:
            return float(m.group(1).replace(',', ''))
        except ValueError:
            pass
    return 999999


# ============================================================
# 已知数据库（备用 / 补充）
# ============================================================
def get_known_mikrotik_switches():
    """
    MikroTik L2+ 交换机已知数据
    价格来自 MikroTik 官网 MSRP（2024年参考价，实际以官网为准）
    """
    data = [
        # ----------------------------------------------------------------
        # CRS3xx 系列 - Marvell 98DX 芯片
        # ----------------------------------------------------------------
        {
            'product_name':          'CRS305-1G-4S+IN',
            'product_code':          'CRS305-1G-4S+IN',
            'product_url':           'https://mikrotik.com/product/CRS305-1G-4SplusIN',
            'price':                 'USD 149.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB / Enterprise',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '5',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '1x GbE RJ45, 4x SFP+ (10G)',
            'total_ports':           '5',
            'ethernet_ports':        '1',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '4',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '4x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'Yes (-40°C)',
            'operating_temperature': '-40°C to +60°C',
            'max_power_consumption': '11 W',
            'form_factor':           'Desktop',
            'dimensions':            '142 x 115 x 28 mm',
            'weight':                'N/A',
            'psu':                   'DC jack 8-28V / 802.3af PoE-in',
            'description':           'Compact desktop switch with 1G management port and 4x 10G SFP+. Ideal for small office uplink aggregation.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS309-1G-8S+IN',
            'product_code':          'CRS309-1G-8S+IN',
            'product_url':           'https://mikrotik.com/product/CRS309-1G-8SplusIN',
            'price':                 'USD 229.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'Enterprise',
            'switch_chip_model':     '98DX8208',
            'switch_chip_ports':     '9',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '1x GbE RJ45, 8x SFP+ (10G)',
            'total_ports':           '9',
            'ethernet_ports':        '1',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '8',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '8x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'Yes (-40°C)',
            'operating_temperature': '-40°C to +60°C',
            'max_power_consumption': '27 W',
            'form_factor':           'Desktop',
            'dimensions':            '228 x 120 x 28 mm',
            'weight':                '475 g',
            'psu':                   'DC 12V / 802.3af PoE-in',
            'description':           'Desktop 10G switch with 8x SFP+ and 1x GbE management. Suitable for 10G aggregation.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS310-1G-5S-4S+IN',
            'product_code':          'CRS310-1G-5S-4S+IN',
            'product_url':           'https://mikrotik.com/product/CRS310-1G-5S-4SplusIN',
            'price':                 'USD 195.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB / Enterprise',
            'switch_chip_model':     '98DX226S',
            'switch_chip_ports':     '10',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '256 MB',
            'storage':               '16 MB',
            'port_configuration':    '1x GbE RJ45, 5x SFP (1G), 4x SFP+ (10G)',
            'total_ports':           '10',
            'ethernet_ports':        '1',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             '5',
            'sfp_plus_ports':        '4',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '5x SFP (1G), 4x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'Yes (-40°C)',
            'operating_temperature': '-40°C to +60°C',
            'max_power_consumption': '17 W',
            'form_factor':           'Desktop',
            'dimensions':            '285 x 145 x 28 mm',
            'weight':                'N/A',
            'psu':                   'DC 12V',
            'description':           'Hybrid SFP/SFP+ switch for fiber-rich environments.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS310-8G+2S+IN',
            'product_code':          'CRS310-8G+2S+IN',
            'product_url':           'https://mikrotik.com/product/CRS310-8Gplus2SplusIN',
            'price':                 'USD 149.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB / Enterprise',
            'switch_chip_model':     '98DX226S',
            'switch_chip_ports':     '10',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '256 MB',
            'storage':               '16 MB',
            'port_configuration':    '8x 2.5GbE RJ45, 2x SFP+ (10G)',
            'total_ports':           '10',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        '8',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '2',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '2x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'Yes (-40°C)',
            'operating_temperature': '-40°C to +60°C',
            'max_power_consumption': '18 W',
            'form_factor':           'Desktop',
            'dimensions':            '220 x 125 x 30 mm',
            'weight':                'N/A',
            'psu':                   'DC 12-57V',
            'description':           '8-port 2.5G switch with 2x SFP+ uplinks. Ideal for WiFi 6 AP aggregation.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS312-4C+8XG-RM',
            'product_code':          'CRS312-4C+8XG-RM',
            'product_url':           'https://mikrotik.com/product/CRS312-4Cplus8XGRM',
            'price':                 'USD 399.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'Enterprise',
            'switch_chip_model':     '98DX8212',
            'switch_chip_ports':     '12',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '650 MHz',
            'ram':                   '64 MB',
            'storage':               '16 MB',
            'port_configuration':    '4x Combo (10G SFP+/RJ45), 8x 10GbE RJ45',
            'total_ports':           '12',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         '8',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '4',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           '4',
            'fiber_ports':           'N/A',
            'uplink':                '4x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '76 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 199 x 44 mm',
            'weight':                '2.05 kg',
            'psu':                   'Internal AC',
            'description':           '12-port all-10G rackmount switch with copper and fiber options.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS312-4C+8XG',
            'product_code':          'CRS312-4C+8XG',
            'product_url':           'https://mikrotik.com/product/CRS312-4Cplus8XG',
            'price':                 'USD 349.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'Enterprise',
            'switch_chip_model':     '98DX8212',
            'switch_chip_ports':     '12',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '650 MHz',
            'ram':                   '64 MB',
            'storage':               '16 MB',
            'port_configuration':    '4x Combo (10G SFP+/RJ45), 8x 10GbE RJ45',
            'total_ports':           '12',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         '8',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '4',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           '4',
            'fiber_ports':           'N/A',
            'uplink':                '4x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '76 W',
            'form_factor':           'Desktop',
            'dimensions':            '330 x 199 x 44 mm',
            'weight':                '1.85 kg',
            'psu':                   'Internal AC',
            'description':           'Desktop 12-port all-10G switch.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS317-1G-16S+RM',
            'product_code':          'CRS317-1G-16S+RM',
            'product_url':           'https://mikrotik.com/product/CRS317-1G-16SplusRM',
            'price':                 'USD 499.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'Enterprise / ISP',
            'switch_chip_model':     '98DX8216',
            'switch_chip_ports':     '17',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '1 GB',
            'storage':               '16 MB',
            'port_configuration':    '1x GbE RJ45, 16x SFP+ (10G)',
            'total_ports':           '17',
            'ethernet_ports':        '1',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '16',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '16x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '36 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 199 x 44 mm',
            'weight':                '2.3 kg',
            'psu':                   'Dual Internal AC (redundant)',
            'description':           '1U 16-port SFP+ rackmount switch for ISP and enterprise core.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS318-1Fi-15Fr-2S',
            'product_code':          'CRS318-1Fi-15Fr-2S',
            'product_url':           'https://mikrotik.com/product/CRS318-1Fi-15Fr-2S',
            'price':                 'USD 225.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'ISP / FTTB',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '18',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '15x 100M Fiber, 1x 1G Fiber (SFP), 2x SFP',
            'total_ports':           '18',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             '2',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           '16',
            'uplink':                '2x SFP (1G)',
            'poe_in':                'Reverse PoE (from fiber)',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +70°C',
            'max_power_consumption': '11 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 144 x 44 mm',
            'weight':                '1.5 kg',
            'psu':                   'Internal AC / Reverse PoE from fiber',
            'description':           'FTTB fiber aggregation switch with 15x 100M + 1x 1G fiber ports.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS318-16P-2S+RM',
            'product_code':          'CRS318-16P-2S+RM',
            'product_url':           'https://mikrotik.com/product/CRS318-16P-2SplusRM',
            'price':                 'USD 329.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB / Access',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '18',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '16x GbE RJ45 (PoE-out), 2x SFP+ (10G)',
            'total_ports':           '18',
            'ethernet_ports':        '16',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '2',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '2x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'PoE+ (802.3af/at/bt)',
            'poe_budget':            '300 W',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '340 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 199 x 44 mm',
            'weight':                '2.2 kg',
            'psu':                   'Internal AC 350W',
            'description':           '16-port PoE+ rackmount switch with 300W budget and 2x SFP+ uplinks.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS320-8P-8B-4S+RM',
            'product_code':          'CRS320-8P-8B-4S+RM',
            'product_url':           'https://mikrotik.com/product/CRS320-8P-8B-4SplusRM',
            'price':                 'USD 299.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB / Access',
            'switch_chip_model':     '98DX226S',
            'switch_chip_ports':     '20',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '256 MB',
            'storage':               '16 MB',
            'port_configuration':    '8x GbE PoE-out, 8x GbE, 4x SFP+ (10G)',
            'total_ports':           '20',
            'ethernet_ports':        '16',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '4',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '4x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'PoE+ (802.3af/at)',
            'poe_budget':            '150 W',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '187 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 199 x 44 mm',
            'weight':                '2.3 kg',
            'psu':                   'Internal AC',
            'description':           '20-port switch with 8x PoE + 8x regular GbE + 4x SFP+ uplinks.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS326-24G-2S+IN',
            'product_code':          'CRS326-24G-2S+IN',
            'product_url':           'https://mikrotik.com/product/CRS326-24G-2SplusIN',
            'price':                 'USD 199.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '26',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '24x GbE RJ45, 2x SFP+ (10G)',
            'total_ports':           '26',
            'ethernet_ports':        '24',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '2',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '2x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'Yes (-40°C)',
            'operating_temperature': '-40°C to +60°C',
            'max_power_consumption': '19 W',
            'form_factor':           'Desktop',
            'dimensions':            '337 x 144 x 28 mm',
            'weight':                'N/A',
            'psu':                   'DC 24V / 802.3af PoE-in',
            'description':           '24-port Gigabit desktop switch with 2x SFP+ uplinks.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS326-24G-2S+RM',
            'product_code':          'CRS326-24G-2S+RM',
            'product_url':           'https://mikrotik.com/product/CRS326-24G-2SplusRM',
            'price':                 'USD 219.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '26',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '24x GbE RJ45, 2x SFP+ (10G)',
            'total_ports':           '26',
            'ethernet_ports':        '24',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '2',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '2x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '19 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 144 x 44 mm',
            'weight':                '1.5 kg',
            'psu':                   'Internal AC',
            'description':           '24-port Gigabit rackmount switch with 2x SFP+ uplinks.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS326-24S+2Q+RM',
            'product_code':          'CRS326-24S+2Q+RM',
            'product_url':           'https://mikrotik.com/product/CRS326-24S-2QplusRM',
            'price':                 'USD 599.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'Enterprise / ISP',
            'switch_chip_model':     '98DX8332',
            'switch_chip_ports':     '26',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '650 MHz',
            'ram':                   '1 GB',
            'storage':               '16 MB',
            'port_configuration':    '24x SFP+ (10G), 2x QSFP+ (40G)',
            'total_ports':           '26',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '24',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            '2',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '2x QSFP+ (40G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '67 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 199 x 44 mm',
            'weight':                '2.5 kg',
            'psu':                   'Dual Internal AC (redundant)',
            'description':           '24x SFP+ all-fiber switch with 40G QSFP+ uplinks for ISP/DC.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS326-4C+20G+2S+RM',
            'product_code':          'CRS326-4C+20G+2S+RM',
            'product_url':           'https://mikrotik.com/product/CRS326-4Cplus20Gplus2SplusRM',
            'price':                 'USD 239.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '26',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '4x Combo (GbE/SFP), 20x GbE RJ45, 2x SFP+ (10G)',
            'total_ports':           '26',
            'ethernet_ports':        '20',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '2',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           '4',
            'fiber_ports':           'N/A',
            'uplink':                '2x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '23 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 144 x 44 mm',
            'weight':                '1.7 kg',
            'psu':                   'Internal AC',
            'description':           '26-port switch with 4x combo, 20x GbE, 2x SFP+.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS328-4C-20S-4S+RM',
            'product_code':          'CRS328-4C-20S-4S+RM',
            'product_url':           'https://mikrotik.com/product/CRS328-4C-20S-4SplusRM',
            'price':                 'USD 299.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'ISP / SMB',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '28',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '4x Combo (GbE/SFP), 20x SFP (1G), 4x SFP+ (10G)',
            'total_ports':           '28',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             '20',
            'sfp_plus_ports':        '4',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           '4',
            'fiber_ports':           'N/A',
            'uplink':                '4x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '37 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 199 x 44 mm',
            'weight':                '2.1 kg',
            'psu':                   'Internal AC',
            'description':           'SFP aggregation switch with 20x SFP + 4x SFP+ + 4x Combo.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS328-24P-4S+RM',
            'product_code':          'CRS328-24P-4S+RM',
            'product_url':           'https://mikrotik.com/product/CRS328-24P-4SplusRM',
            'price':                 'USD 499.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB / Access',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '28',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '24x GbE RJ45 (PoE-out), 4x SFP+ (10G)',
            'total_ports':           '28',
            'ethernet_ports':        '24',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '4',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '4x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'PoE+ (802.3af/at)',
            'poe_budget':            '500 W',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '555 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 280 x 44 mm',
            'weight':                '3.5 kg',
            'psu':                   'Internal AC 600W',
            'description':           '24-port PoE+ switch with 500W budget and 4x SFP+ uplinks.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS332-32S+RM',
            'product_code':          'CRS332-32S+RM',
            'product_url':           'https://mikrotik.com/product/CRS332-32S-6CplusRM',
            'price':                 'USD 749.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'Enterprise / ISP',
            'switch_chip_model':     '98DX8332',
            'switch_chip_ports':     '38',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '650 MHz',
            'ram':                   '1 GB',
            'storage':               '16 MB',
            'port_configuration':    '32x SFP+ (10G), 6x Combo (SFP+/RJ45)',
            'total_ports':           '38',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '32',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           '6',
            'fiber_ports':           'N/A',
            'uplink':                '32x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '73 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 290 x 44 mm',
            'weight':                '3.2 kg',
            'psu':                   'Dual Internal AC (redundant)',
            'description':           '32x SFP+ switch with 6x Combo for ISP and enterprise aggregation.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        # ----------------------------------------------------------------
        # CRS5xx 系列 - 高端 25G/100G
        # ----------------------------------------------------------------
        {
            'product_name':          'CRS504-4XQ-IN',
            'product_code':          'CRS504-4XQ-IN',
            'product_url':           'https://mikrotik.com/product/CRS504-4XQ-IN',
            'price':                 'USD 499.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'Data Center / Carrier',
            'switch_chip_model':     '98DX4310',
            'switch_chip_ports':     '4',
            'cpu':                   'Marvell 88F7040',
            'cpu_core_count':        '4',
            'cpu_frequency':         '1.6 GHz',
            'ram':                   '1 GB',
            'storage':               '512 MB',
            'port_configuration':    '4x QSFP28 (100G)',
            'total_ports':           '4',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          '4',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '4x QSFP28 (100G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'Yes (-40°C)',
            'operating_temperature': '-40°C to +60°C',
            'max_power_consumption': '38 W',
            'form_factor':           'Desktop',
            'dimensions':            '220 x 125 x 30 mm',
            'weight':                'N/A',
            'psu':                   'DC 12-57V / 802.3at PoE-in',
            'description':           'Compact 4x100G QSFP28 switch for data center spine.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS504-4XQ-OUT',
            'product_code':          'CRS504-4XQ-OUT',
            'product_url':           'https://mikrotik.com/product/CRS504-4XQ-OUT',
            'price':                 'USD 549.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'Data Center / Carrier',
            'switch_chip_model':     '98DX4310',
            'switch_chip_ports':     '4',
            'cpu':                   'Marvell 88F7040',
            'cpu_core_count':        '4',
            'cpu_frequency':         '1.6 GHz',
            'ram':                   '1 GB',
            'storage':               '512 MB',
            'port_configuration':    '4x QSFP28 (100G)',
            'total_ports':           '4',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          '4',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '4x QSFP28 (100G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'Yes (-40°C)',
            'operating_temperature': '-40°C to +75°C',
            'max_power_consumption': '38 W',
            'form_factor':           'Outdoor',
            'dimensions':            '220 x 125 x 30 mm',
            'weight':                'N/A',
            'psu':                   'DC 12-57V',
            'description':           'Outdoor 4x100G switch with IP55 enclosure.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS510-8XS-2XQ-IN',
            'product_code':          'CRS510-8XS-2XQ-IN',
            'product_url':           'https://mikrotik.com/product/CRS510-8XS-2XQ-IN',
            'price':                 'USD 599.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'Data Center / Carrier',
            'switch_chip_model':     '98DX8525 (Aldrin3S)',
            'switch_chip_ports':     '10',
            'cpu':                   'Marvell 88F7040',
            'cpu_core_count':        '4',
            'cpu_frequency':         '1.6 GHz',
            'ram':                   '1 GB',
            'storage':               '512 MB',
            'port_configuration':    '8x SFP28 (25G), 2x QSFP28 (100G)',
            'total_ports':           '10',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           '8',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          '2',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '8x SFP28 (25G), 2x QSFP28 (100G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'Yes (-40°C)',
            'operating_temperature': '-40°C to +60°C',
            'max_power_consumption': '55 W',
            'form_factor':           'Desktop',
            'dimensions':            '228 x 120 x 28 mm',
            'weight':                'N/A',
            'psu':                   'DC 12-57V / 802.3at PoE-in',
            'description':           '25G/100G compact switch for spine-leaf architectures.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS518-16XS-2XQ-RM',
            'product_code':          'CRS518-16XS-2XQ-RM',
            'product_url':           'https://mikrotik.com/product/CRS518-16XS-2XQ-RM',
            'price':                 'USD 999.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'Data Center / Carrier',
            'switch_chip_model':     '98DX8525 (Aldrin3S)',
            'switch_chip_ports':     '18',
            'cpu':                   'Marvell 88F7040',
            'cpu_core_count':        '4',
            'cpu_frequency':         '1.6 GHz',
            'ram':                   '1 GB',
            'storage':               '512 MB',
            'port_configuration':    '16x SFP28 (25G), 2x QSFP28 (100G)',
            'total_ports':           '18',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           '16',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          '2',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '16x SFP28 (25G), 2x QSFP28 (100G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping, HW offload',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '76 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 199 x 44 mm',
            'weight':                '2.6 kg',
            'psu':                   'Dual Internal AC (redundant)',
            'description':           '1U 25G/100G rackmount switch for data center.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        # ----------------------------------------------------------------
        # CSS 系列 - SwOS Only
        # ----------------------------------------------------------------
        {
            'product_name':          'CSS106-5G-1S (RB260GS)',
            'product_code':          'CSS106-5G-1S',
            'product_url':           'https://mikrotik.com/product/CSS106-5G-1S',
            'price':                 'USD 29.00',
            'product_series':        'CSS (Cloud Smart Switch)',
            'market_category':       'SMB / SOHO',
            'switch_chip_model':     'Atheros AR8327N',
            'switch_chip_ports':     '6',
            'cpu':                   'Atheros AR8327N (standalone)',
            'cpu_core_count':        '1',
            'cpu_frequency':         '200 MHz',
            'ram':                   'N/A',
            'storage':               'N/A',
            'port_configuration':    '5x GbE RJ45, 1x SFP (1G)',
            'total_ports':           '6',
            'ethernet_ports':        '5',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             '1',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '1x SFP (1G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'SwOS',
            'ring_protocol':         'STP, RSTP',
            'switch_chip_features':  'VLAN, QoS, port mirroring, IGMP snooping',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +50°C',
            'max_power_consumption': '3 W',
            'form_factor':           'Desktop',
            'dimensions':            '113 x 83 x 28 mm',
            'weight':                '116 g',
            'psu':                   'DC 9-28V',
            'description':           'Entry-level 5-port Gigabit smart switch with SwOS.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CSS106-1G-4P-1S (RB260GSP)',
            'product_code':          'CSS106-1G-4P-1S',
            'product_url':           'https://mikrotik.com/product/CSS106-1G-4P-1S',
            'price':                 'USD 59.00',
            'product_series':        'CSS (Cloud Smart Switch)',
            'market_category':       'SMB / SOHO',
            'switch_chip_model':     'Atheros AR8327N',
            'switch_chip_ports':     '6',
            'cpu':                   'Atheros AR8327N (standalone)',
            'cpu_core_count':        '1',
            'cpu_frequency':         '200 MHz',
            'ram':                   'N/A',
            'storage':               'N/A',
            'port_configuration':    '4x GbE PoE-out, 1x GbE, 1x SFP (1G)',
            'total_ports':           '6',
            'ethernet_ports':        '5',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             '1',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '1x SFP (1G)',
            'poe_in':                'N/A',
            'poe_out':               'Passive PoE (24V)',
            'poe_budget':            'N/A',
            'operating_system':      'SwOS',
            'ring_protocol':         'STP, RSTP',
            'switch_chip_features':  'VLAN, QoS, port mirroring, IGMP snooping',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +50°C',
            'max_power_consumption': 'N/A',
            'form_factor':           'Desktop',
            'dimensions':            '113 x 83 x 28 mm',
            'weight':                '120 g',
            'psu':                   'DC 9-28V',
            'description':           '5-port PoE smart switch with passive PoE and SwOS.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CSS326-24G-2S+RM',
            'product_code':          'CSS326-24G-2S+RM',
            'product_url':           'https://mikrotik.com/product/CSS326-24G-2SplusRM',
            'price':                 'USD 199.00',
            'product_series':        'CSS (Cloud Smart Switch)',
            'market_category':       'SMB',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '26',
            'cpu':                   'Marvell 98DX3236',
            'cpu_core_count':        '1',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '24x GbE RJ45, 2x SFP+ (10G)',
            'total_ports':           '26',
            'ethernet_ports':        '24',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '2',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '2x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'SwOS',
            'ring_protocol':         'STP, RSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, port mirroring, IGMP snooping',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '19 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 144 x 44 mm',
            'weight':                '1.5 kg',
            'psu':                   'Internal AC',
            'description':           '24-port Gigabit managed switch with SwOS only (same HW as CRS326).',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CSS610-8G-2S+IN',
            'product_code':          'CSS610-8G-2S+IN',
            'product_url':           'https://mikrotik.com/product/CSS610-8G-2SplusIN',
            'price':                 'USD 89.00',
            'product_series':        'CSS (Cloud Smart Switch)',
            'market_category':       'SMB / SOHO',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '10',
            'cpu':                   'Marvell 98DX3236',
            'cpu_core_count':        '1',
            'cpu_frequency':         '800 MHz',
            'ram':                   '128 MB',
            'storage':               '16 MB',
            'port_configuration':    '8x GbE RJ45, 2x SFP+ (10G)',
            'total_ports':           '10',
            'ethernet_ports':        '8',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '2',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '2x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'SwOS',
            'ring_protocol':         'STP, RSTP',
            'switch_chip_features':  'VLAN, QoS, port mirroring, IGMP snooping',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +50°C',
            'max_power_consumption': '11 W',
            'form_factor':           'Desktop',
            'dimensions':            '220 x 125 x 30 mm',
            'weight':                '300 g',
            'psu':                   'DC 12-28V / 802.3af PoE-in',
            'description':           '8-port Gigabit SwOS switch with 2x SFP+ for 10G uplink.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CSS610-8P-2S+IN',
            'product_code':          'CSS610-8P-2S+IN',
            'product_url':           'https://mikrotik.com/product/CSS610-8P-2SplusIN',
            'price':                 'USD 139.00',
            'product_series':        'CSS (Cloud Smart Switch)',
            'market_category':       'SMB / SOHO',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '10',
            'cpu':                   'Marvell 98DX3236',
            'cpu_core_count':        '1',
            'cpu_frequency':         '800 MHz',
            'ram':                   '128 MB',
            'storage':               '16 MB',
            'port_configuration':    '8x GbE RJ45 (PoE-out), 2x SFP+ (10G)',
            'total_ports':           '10',
            'ethernet_ports':        '8',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '2',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '2x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'PoE+ (802.3af/at)',
            'poe_budget':            '140 W',
            'operating_system':      'SwOS',
            'ring_protocol':         'STP, RSTP',
            'switch_chip_features':  'VLAN, QoS, port mirroring, IGMP snooping',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +50°C',
            'max_power_consumption': '162 W',
            'form_factor':           'Desktop',
            'dimensions':            '220 x 125 x 30 mm',
            'weight':                '320 g',
            'psu':                   'DC 48-57V / 802.3at PoE-in',
            'description':           '8-port PoE+ SwOS switch with 140W budget and 2x SFP+.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        # ----------------------------------------------------------------
        # CRS1xx / CRS2xx 旧系列
        # ----------------------------------------------------------------
        {
            'product_name':          'CRS106-1C-5S',
            'product_code':          'CRS106-1C-5S',
            'product_url':           'https://mikrotik.com/product/CRS106-1C-5S',
            'price':                 'USD 89.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB',
            'switch_chip_model':     'QCA8511',
            'switch_chip_ports':     '6',
            'cpu':                   'Atheros AR9344',
            'cpu_core_count':        '1',
            'cpu_frequency':         '400 MHz',
            'ram':                   '128 MB',
            'storage':               '128 MB',
            'port_configuration':    '1x Combo (GbE/SFP), 5x SFP (1G)',
            'total_ports':           '6',
            'ethernet_ports':        '1',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             '5',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           '1',
            'fiber_ports':           'N/A',
            'uplink':                '5x SFP (1G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP',
            'switch_chip_features':  'VLAN, QoS, port mirroring',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '7 W',
            'form_factor':           'Desktop',
            'dimensions':            '150 x 93 x 28 mm',
            'weight':                '190 g',
            'psu':                   'DC 12V / 802.3af PoE-in',
            'description':           'Small SFP desktop switch with 5x SFP and 1x Combo port.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS112-8G-4S-IN',
            'product_code':          'CRS112-8G-4S-IN',
            'product_url':           'https://mikrotik.com/product/CRS112-8G-4S-IN',
            'price':                 'USD 119.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB',
            'switch_chip_model':     'QCA8513',
            'switch_chip_ports':     '12',
            'cpu':                   'Atheros AR9344',
            'cpu_core_count':        '1',
            'cpu_frequency':         '400 MHz',
            'ram':                   '128 MB',
            'storage':               '128 MB',
            'port_configuration':    '8x GbE RJ45, 4x SFP (1G)',
            'total_ports':           '12',
            'ethernet_ports':        '8',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             '4',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '4x SFP (1G)',
            'poe_in':                'N/A',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP',
            'switch_chip_features':  'VLAN, QoS, port mirroring',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '8 W',
            'form_factor':           'Desktop',
            'dimensions':            '210 x 113 x 28 mm',
            'weight':                '290 g',
            'psu':                   'DC 12V / 802.3af PoE-in',
            'description':           '12-port desktop switch with 8x GbE and 4x SFP.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'CRS112-8P-4S-IN',
            'product_code':          'CRS112-8P-4S-IN',
            'product_url':           'https://mikrotik.com/product/CRS112-8P-4S-IN',
            'price':                 'USD 199.00',
            'product_series':        'CRS (Cloud Router Switch)',
            'market_category':       'SMB / Access',
            'switch_chip_model':     'QCA8511',
            'switch_chip_ports':     '12',
            'cpu':                   'Atheros AR9344',
            'cpu_core_count':        '1',
            'cpu_frequency':         '400 MHz',
            'ram':                   '128 MB',
            'storage':               '128 MB',
            'port_configuration':    '8x GbE RJ45 (PoE-out), 4x SFP (1G)',
            'total_ports':           '12',
            'ethernet_ports':        '8',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             '4',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '4x SFP (1G)',
            'poe_in':                'N/A',
            'poe_out':               'PoE+ (802.3af/at)',
            'poe_budget':            '150 W',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP',
            'switch_chip_features':  'VLAN, QoS, port mirroring',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '170 W',
            'form_factor':           'Desktop',
            'dimensions':            '210 x 113 x 28 mm',
            'weight':                '310 g',
            'psu':                   'Internal AC 170W',
            'description':           '12-port PoE switch with 8x GbE PoE-out and 4x SFP.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        # ----------------------------------------------------------------
        # netPower 系列
        # ----------------------------------------------------------------
        {
            'product_name':          'netPower 15FR',
            'product_code':          'CRS318-1Fi-15Fr-2S',
            'product_url':           'https://mikrotik.com/product/netPower-15FR',
            'price':                 'USD 225.00',
            'product_series':        'netPower',
            'market_category':       'ISP / FTTB',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '18',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '15x 100M Fiber, 1x 1G Fiber, 2x SFP',
            'total_ports':           '18',
            'ethernet_ports':        'N/A',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             '2',
            'sfp_plus_ports':        'N/A',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           '16',
            'uplink':                '2x SFP (1G)',
            'poe_in':                'Reverse PoE (power from fiber)',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +70°C',
            'max_power_consumption': '11 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 144 x 44 mm',
            'weight':                '1.4 kg',
            'psu':                   'Internal AC / Reverse PoE',
            'description':           'FTTB fiber access switch for apartment buildings (15x100M + 2x SFP uplink).',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'netPower 16P',
            'product_code':          'CRS318-16P-2S+RM',
            'product_url':           'https://mikrotik.com/product/netPower-16P',
            'price':                 'USD 329.00',
            'product_series':        'netPower',
            'market_category':       'SMB / Access',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '18',
            'cpu':                   'Marvell 88F6820',
            'cpu_core_count':        '2',
            'cpu_frequency':         '800 MHz',
            'ram':                   '512 MB',
            'storage':               '16 MB',
            'port_configuration':    '16x GbE RJ45 (PoE-out), 2x SFP+ (10G)',
            'total_ports':           '18',
            'ethernet_ports':        '16',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '2',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           'N/A',
            'uplink':                '2x SFP+ (10G)',
            'poe_in':                'N/A',
            'poe_out':               'PoE+ (802.3af/at/bt)',
            'poe_budget':            '300 W',
            'operating_system':      'RouterOS v7 / SwOS',
            'ring_protocol':         'STP, RSTP, MSTP',
            'switch_chip_features':  'VLAN, QoS, ACL, STP, RSTP, MSTP, LACP, IGMP snooping',
            'industrial_temp':       'No (-20°C)',
            'operating_temperature': '-20°C to +60°C',
            'max_power_consumption': '340 W',
            'form_factor':           '1U Rack',
            'dimensions':            '443 x 199 x 44 mm',
            'weight':                '2.2 kg',
            'psu':                   'Internal AC 350W',
            'description':           'Outdoor-rated 16-port PoE switch variant of CRS318.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
        {
            'product_name':          'netPower Lite 7R',
            'product_code':          'CSS610-1Gi-7R-2S+OUT',
            'product_url':           'https://mikrotik.com/product/netPower-Lite-7R',
            'price':                 'USD 99.00',
            'product_series':        'netPower',
            'market_category':       'ISP / Outdoor',
            'switch_chip_model':     '98DX3236',
            'switch_chip_ports':     '10',
            'cpu':                   'Marvell 98DX3236',
            'cpu_core_count':        '1',
            'cpu_frequency':         '800 MHz',
            'ram':                   '128 MB',
            'storage':               '16 MB',
            'port_configuration':    '1x GbE RJ45, 7x 100M Fiber (Reverse PoE), 2x SFP+ (10G)',
            'total_ports':           '10',
            'ethernet_ports':        '1',
            'eth_2_5g_ports':        'N/A',
            'eth_10g_ports':         'N/A',
            'sfp_ports':             'N/A',
            'sfp_plus_ports':        '2',
            'sfp28_ports':           'N/A',
            'qsfp_ports':            'N/A',
            'qsfp28_ports':          'N/A',
            'combo_ports':           'N/A',
            'fiber_ports':           '7',
            'uplink':                '2x SFP+ (10G)',
            'poe_in':                'Reverse PoE-in (from fiber)',
            'poe_out':               'N/A',
            'poe_budget':            'N/A',
            'operating_system':      'SwOS',
            'ring_protocol':         'STP, RSTP',
            'switch_chip_features':  'VLAN, QoS, port mirroring, IGMP snooping',
            'industrial_temp':       'Yes (-40°C)',
            'operating_temperature': '-40°C to +70°C',
            'max_power_consumption': '9 W',
            'form_factor':           'Outdoor',
            'dimensions':            '220 x 125 x 30 mm',
            'weight':                'N/A',
            'psu':                   'Reverse PoE / DC',
            'description':           'Outdoor reverse-PoE switch for fiber CPE power via copper uplink.',
            'is_switch':             True,
            'is_l2_plus':            True,
        },
    ]
    return data


# ============================================================
# 主流程
# ============================================================
def main_with_fallback():
    print("=" * 72)
    print("  MikroTik L2+ 接入层交换机信息抓取 & 导出工具  v2.0")
    print("  字段: Model / Chipset / Ports / PoE / SFP / Price / ...")
    print("=" * 72)

    print("\n选择运行模式:")
    print("  1. 在线抓取 (需要能访问 mikrotik.com)")
    print("  2. 离线数据库 (直接使用内置已知数据)")
    print("  3. 混合模式 (内置数据 + 在线补充, 推荐)")
    mode = input("\n请输入 (1/2/3, 直接回车 = 3): ").strip() or '3'

    session = get_session()

    if mode == '1':
        # ---- 纯在线 ----
        products_meta = get_switch_product_links(session)
        all_products  = _online_scrape(session, products_meta)

    elif mode == '2':
        # ---- 纯离线 ----
        print("\n📦 加载内置数据库...")
        all_products = get_known_mikrotik_switches()
        print(f"   共 {len(all_products)} 条记录")

    else:
        # ---- 混合 ----
        print("\n📦 Step 1: 加载内置数据库...")
        known = get_known_mikrotik_switches()
        known_urls = {p['product_url'] for p in known}
        print(f"   内置 {len(known)} 条记录")

        print("\n🌐 Step 2: 在线补充...")
        try:
            products_meta   = get_switch_product_links(session)
            new_meta        = [p for p in products_meta if p['url'] not in known_urls]
            online_products = _online_scrape(session, new_meta)
            all_products    = known + online_products
            print(f"\n   在线补充了 {len(online_products)} 个新产品")
        except Exception as e:
            print(f"\n   ⚠️ 在线抓取出错: {e}，使用纯内置数据")
            all_products = known

    # ---- 显示汇总 ----
    _print_summary(all_products)

    # ---- 导出 ----
    print("\n📝 正在导出 Excel...")
    fname = export_to_excel(all_products)
    print(f"\n🎉 完成! 共 {len(all_products)} 个产品 → {fname}")


def _online_scrape(session, products_meta):
    """在线逐个抓取"""
    result = []
    total  = len(products_meta)
    for idx, meta in enumerate(products_meta, 1):
        print(f"\n[{idx}/{total}] {meta['name']}")
        prod = parse_product_page(session, meta)
        if prod and prod.get('is_switch'):
            result.append(prod)
            print(f"    ✅ chip={prod['switch_chip_model']}  price={prod['price']}")
        else:
            print(f"    ⏭️  跳过")
        time.sleep(REQUEST_DELAY)
    return result


def _print_summary(products):
    """控制台打印汇总表"""
    print(f"\n{'=' * 100}")
    print(f"  共 {len(products)} 个 L2+ 交换机")
    print(f"{'=' * 100}")
    fmt = "{:<4} {:<30} {:<22} {:<18} {:<16} {:<14} {:<14}"
    print(fmt.format('No.', '产品名称', 'Switch Chip', '端口配置概要',
                     '操作系统', '价格', '工业温度'))
    print("-" * 100)
    for i, p in enumerate(products, 1):
        ports = p.get('port_configuration', 'N/A')
        if len(ports) > 30:
            ports = ports[:28] + '..'
        print(fmt.format(
            i,
            p.get('product_name', '')[:29],
            p.get('switch_chip_model', 'N/A')[:21],
            ports,
            p.get('operating_system', 'N/A')[:15],
            p.get('price', 'N/A')[:13],
            p.get('industrial_temp', 'N/A')[:13],
        ))


# ============================================================
if __name__ == '__main__':
    missing = []
    for pkg, imp in [('requests', 'requests'),
                     ('beautifulsoup4', 'bs4'),
                     ('openpyxl', 'openpyxl')]:
        try:
            __import__(imp)
        except ImportError:
            missing.append(pkg)

    if missing:
        print("⚠️  缺少依赖:")
        for m in missing:
            print(f"   pip install {m}")
        sys.exit(1)

    main_with_fallback()