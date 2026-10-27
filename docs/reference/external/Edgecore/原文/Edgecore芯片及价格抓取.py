#!/usr/bin/env python3
"""
Edgecore Networks L2+/L3 Lite Access Layer Switch Scraper
抓取 Edgecore 接入层交换机规格信息，并从多渠道经销商获取参考价格
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter
import json
from urllib.parse import urljoin, quote_plus
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
}

HEADERS_JSON = {
    **HEADERS,
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
}

BASE_URL        = 'https://www.edge-core.com'
REQUEST_DELAY   = 2.5

# ============================================================
# 已知 Edgecore L2+/L3 Lite 交换机完整数据库
# 价格来自: Streakwave, Baltic Networks, Black Box,
#           Getic, Secomea, Amazon, CDW, Newegg 等经销商
# ============================================================
EDGECORE_SWITCHES = [

    # ===========================================================
    # ECS4150 系列 — Marvell Prestera 芯片，企业接入层主力
    # ===========================================================
    {
        'product_name':          'ECS4150-28T',
        'product_code':          'ECS4150-28T',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=59&id=790',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4150-28T_DS.pdf',
        'price_usd':             '~$350',
        'price_sources':         'Baltic Networks ~$349; Streakwave ~$359',
        'product_series':        'ECS4150',
        'market_category':       'Enterprise / SMB',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3255',
        'switch_chip_ports':     '28',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '2',
        'cpu_frequency':         '1.0 GHz',
        'ram':                   '1 GB DDR4',
        'storage':               '4 GB eMMC',
        'port_configuration':    '24x GbE RJ45, 4x SFP+ (10G)',
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
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'N/A',
        'poe_ports':             '0',
        'poe_standard':          'N/A',
        'poe_budget_w':          'N/A',
        'switching_capacity':    '128 Gbps',
        'forwarding_rate':       '95.24 Mpps',
        'mac_table':             '32K',
        'jumbo_frame':           '10240 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes (802.1D/w/s)',
        'lacp':                  'Yes (802.3ad)',
        'igmp_snooping':         'Yes (v1/v2/v3)',
        'qos':                   'Yes (8 queues, 802.1p, DSCP)',
        'acl':                   'Yes (L2/L3/L4)',
        'ipv6':                  'Yes (IPv6 management, MLD)',
        'routing':               'Static routing, RIP',
        'ring_protocol':         'STP, RSTP, MSTP, ERPS (G.8032)',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, RMON, ecCLOUD',
        'max_power_consumption': '25 W',
        'psu':                   'Internal AC 100-240V',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 210 x 44 mm',
        'weight':                '3.5 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           '28-port L2+ managed switch, 24x GbE + 4x 10G SFP+, no PoE. Enterprise campus access.',
    },
    {
        'product_name':          'ECS4150-28P',
        'product_code':          'ECS4150-28P',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=59&id=791',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4150-28P_DS.pdf',
        'price_usd':             '~$620',
        'price_sources':         'Streakwave $621; Baltic Networks ~$609; Amazon ~$650',
        'product_series':        'ECS4150',
        'market_category':       'Enterprise / SMB',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3255',
        'switch_chip_ports':     '28',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '2',
        'cpu_frequency':         '1.0 GHz',
        'ram':                   '1 GB DDR4',
        'storage':               '4 GB eMMC',
        'port_configuration':    '24x GbE RJ45 (PoE+), 4x SFP+ (10G)',
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
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE+ (802.3af/at)',
        'poe_ports':             '24',
        'poe_standard':          '802.3af / 802.3at (PoE+)',
        'poe_budget_w':          '370 W',
        'switching_capacity':    '128 Gbps',
        'forwarding_rate':       '95.24 Mpps',
        'mac_table':             '32K',
        'jumbo_frame':           '10240 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes (802.1D/w/s)',
        'lacp':                  'Yes (802.3ad)',
        'igmp_snooping':         'Yes (v1/v2/v3)',
        'qos':                   'Yes (8 queues, 802.1p, DSCP)',
        'acl':                   'Yes (L2/L3/L4)',
        'ipv6':                  'Yes (IPv6 management, MLD)',
        'routing':               'Static routing, RIP',
        'ring_protocol':         'STP, RSTP, MSTP, ERPS (G.8032)',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, RMON, ecCLOUD',
        'max_power_consumption': '420 W',
        'psu':                   'Internal AC 100-240V, 500W',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 300 x 44 mm',
        'weight':                '5.2 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           '28-port L2+ PoE+ managed switch, 24x GbE PoE+ + 4x 10G SFP+, 370W budget.',
    },
    {
        'product_name':          'ECS4150-28P-I',
        'product_code':          'ECS4150-28P-I',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=59&id=792',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4150-28P-I_DS.pdf',
        'price_usd':             '~$750',
        'price_sources':         'Baltic Networks ~$749; estimated industrial premium +20%',
        'product_series':        'ECS4150',
        'market_category':       'Industrial / Enterprise',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3255',
        'switch_chip_ports':     '28',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '2',
        'cpu_frequency':         '1.0 GHz',
        'ram':                   '1 GB DDR4',
        'storage':               '4 GB eMMC',
        'port_configuration':    '24x GbE RJ45 (PoE+), 4x SFP+ (10G)',
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
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE+ (802.3af/at)',
        'poe_ports':             '24',
        'poe_standard':          '802.3af / 802.3at (PoE+)',
        'poe_budget_w':          '370 W',
        'switching_capacity':    '128 Gbps',
        'forwarding_rate':       '95.24 Mpps',
        'mac_table':             '32K',
        'jumbo_frame':           '10240 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes (802.1D/w/s)',
        'lacp':                  'Yes (802.3ad)',
        'igmp_snooping':         'Yes (v1/v2/v3)',
        'qos':                   'Yes (8 queues, 802.1p, DSCP)',
        'acl':                   'Yes (L2/L3/L4)',
        'ipv6':                  'Yes',
        'routing':               'Static routing, RIP',
        'ring_protocol':         'STP, RSTP, MSTP, ERPS (G.8032)',
        'industrial_temp':       'Yes (-40°C)',
        'operating_temperature': '-40°C to +75°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, RMON, ecCLOUD',
        'max_power_consumption': '420 W',
        'psu':                   'Internal AC, 500W',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 300 x 44 mm',
        'weight':                '5.5 kg',
        'certifications':        'FCC, CE, RoHS, EN61000',
        'description':           'Industrial-grade PoE+ switch, -40~75°C, 24x GbE PoE+ + 4x 10G SFP+.',
    },
    {
        'product_name':          'ECS4150-54T',
        'product_code':          'ECS4150-54T',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=59&id=793',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4150-54T_DS.pdf',
        'price_usd':             '~$550',
        'price_sources':         'Baltic Networks ~$549; Streakwave ~$569',
        'product_series':        'ECS4150',
        'market_category':       'Enterprise / SMB',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3265',
        'switch_chip_ports':     '54',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '2',
        'cpu_frequency':         '1.0 GHz',
        'ram':                   '1 GB DDR4',
        'storage':               '4 GB eMMC',
        'port_configuration':    '48x GbE RJ45, 6x SFP28 (25G)',
        'total_ports':           '54',
        'ethernet_ports':        '48',
        'eth_2_5g_ports':        'N/A',
        'eth_10g_ports':         'N/A',
        'sfp_ports':             'N/A',
        'sfp_plus_ports':        'N/A',
        'sfp28_ports':           '6',
        'qsfp_ports':            'N/A',
        'qsfp28_ports':          'N/A',
        'combo_ports':           'N/A',
        'uplink':                '6x SFP28 (25G)',
        'poe_in':                'N/A',
        'poe_out':               'N/A',
        'poe_ports':             '0',
        'poe_standard':          'N/A',
        'poe_budget_w':          'N/A',
        'switching_capacity':    '300 Gbps',
        'forwarding_rate':       '190.48 Mpps',
        'mac_table':             '32K',
        'jumbo_frame':           '10240 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes (802.1D/w/s)',
        'lacp':                  'Yes (802.3ad)',
        'igmp_snooping':         'Yes (v1/v2/v3)',
        'qos':                   'Yes (8 queues, 802.1p, DSCP)',
        'acl':                   'Yes (L2/L3/L4)',
        'ipv6':                  'Yes',
        'routing':               'Static routing, RIP, OSPFv2',
        'ring_protocol':         'STP, RSTP, MSTP, ERPS (G.8032)',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, RMON, ecCLOUD',
        'max_power_consumption': '60 W',
        'psu':                   'Internal AC 100-240V',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 300 x 44 mm',
        'weight':                '5.0 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           '54-port switch, 48x GbE + 6x 25G SFP28 uplinks, no PoE. High-density access.',
    },
    {
        'product_name':          'ECS4150-54P',
        'product_code':          'ECS4150-54P',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=59&id=794',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4150-54P_DS.pdf',
        'price_usd':             '~$1,147',
        'price_sources':         'Streakwave $1,147; Baltic Networks $1,099; Black Box ~$1,200',
        'product_series':        'ECS4150',
        'market_category':       'Enterprise / Campus',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3265',
        'switch_chip_ports':     '54',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '2',
        'cpu_frequency':         '1.0 GHz',
        'ram':                   '1 GB DDR4',
        'storage':               '4 GB eMMC',
        'port_configuration':    '48x GbE RJ45 (PoE+/BT), 6x SFP28 (25G)',
        'total_ports':           '54',
        'ethernet_ports':        '48',
        'eth_2_5g_ports':        'N/A',
        'eth_10g_ports':         'N/A',
        'sfp_ports':             'N/A',
        'sfp_plus_ports':        'N/A',
        'sfp28_ports':           '6',
        'qsfp_ports':            'N/A',
        'qsfp28_ports':          'N/A',
        'combo_ports':           'N/A',
        'uplink':                '6x SFP28 (25G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE++ (802.3af/at/bt)',
        'poe_ports':             '48',
        'poe_standard':          '802.3af / 802.3at / 802.3bt (PoE++)',
        'poe_budget_w':          '740 W',
        'switching_capacity':    '300 Gbps',
        'forwarding_rate':       '190.48 Mpps',
        'mac_table':             '32K',
        'jumbo_frame':           '10240 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes (802.1D/w/s)',
        'lacp':                  'Yes (802.3ad)',
        'igmp_snooping':         'Yes (v1/v2/v3)',
        'qos':                   'Yes (8 queues, 802.1p, DSCP)',
        'acl':                   'Yes (L2/L3/L4)',
        'ipv6':                  'Yes (IPv6 security, MLD v1/v2)',
        'routing':               'Static routing, RIP, OSPFv2',
        'ring_protocol':         'STP, RSTP, MSTP, ERPS (G.8032)',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, RMON, ecCLOUD',
        'max_power_consumption': '830 W',
        'psu':                   'Internal AC, 900W (redundant optional)',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 380 x 44 mm',
        'weight':                '7.5 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           '48-port PoE++ switch, 740W budget, 6x 25G SFP28. Campus-class high-density.',
    },
    {
        'product_name':          'ECS4150-54P-I',
        'product_code':          'ECS4150-54P-I',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=59&id=795',
        'datasheet_url':         'N/A',
        'price_usd':             '~$1,350',
        'price_sources':         'Estimated industrial premium over ECS4150-54P (~+18%)',
        'product_series':        'ECS4150',
        'market_category':       'Industrial / Enterprise',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3265',
        'switch_chip_ports':     '54',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '2',
        'cpu_frequency':         '1.0 GHz',
        'ram':                   '1 GB DDR4',
        'storage':               '4 GB eMMC',
        'port_configuration':    '48x GbE RJ45 (PoE+/BT), 6x SFP28 (25G)',
        'total_ports':           '54',
        'ethernet_ports':        '48',
        'eth_2_5g_ports':        'N/A',
        'eth_10g_ports':         'N/A',
        'sfp_ports':             'N/A',
        'sfp_plus_ports':        'N/A',
        'sfp28_ports':           '6',
        'qsfp_ports':            'N/A',
        'qsfp28_ports':          'N/A',
        'combo_ports':           'N/A',
        'uplink':                '6x SFP28 (25G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE++ (802.3af/at/bt)',
        'poe_ports':             '48',
        'poe_standard':          '802.3af / 802.3at / 802.3bt',
        'poe_budget_w':          '740 W',
        'switching_capacity':    '300 Gbps',
        'forwarding_rate':       '190.48 Mpps',
        'mac_table':             '32K',
        'jumbo_frame':           '10240 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes (8 queues)',
        'acl':                   'Yes',
        'ipv6':                  'Yes',
        'routing':               'Static routing, RIP, OSPFv2',
        'ring_protocol':         'STP, RSTP, MSTP, ERPS (G.8032)',
        'industrial_temp':       'Yes (-40°C)',
        'operating_temperature': '-40°C to +75°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, RMON, ecCLOUD',
        'max_power_consumption': '830 W',
        'psu':                   'Internal AC, 900W',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 380 x 44 mm',
        'weight':                '7.8 kg',
        'certifications':        'FCC, CE, RoHS, EN61000',
        'description':           'Industrial PoE++ switch -40~75°C, 48x GbE PoE++ + 6x 25G SFP28.',
    },

    # ===========================================================
    # ECS4125 系列 — SMB/ISP 宽带接入
    # ===========================================================
    {
        'product_name':          'ECS4125-28T',
        'product_code':          'ECS4125-28T',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=143&id=880',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4125-28T_DS.pdf',
        'price_usd':             '~$250',
        'price_sources':         'Baltic Networks ~$249; estimated SMB tier pricing',
        'product_series':        'ECS4125',
        'market_category':       'SMB / ISP',
        'switch_chip_vendor':    'Broadcom',
        'switch_chip_model':     'Broadcom BCM53134',
        'switch_chip_ports':     '28',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '1',
        'cpu_frequency':         '500 MHz',
        'ram':                   '512 MB DDR3',
        'storage':               '128 MB Flash',
        'port_configuration':    '24x GbE RJ45, 4x SFP+ (10G)',
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
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'N/A',
        'poe_ports':             '0',
        'poe_standard':          'N/A',
        'poe_budget_w':          'N/A',
        'switching_capacity':    '128 Gbps',
        'forwarding_rate':       '95.24 Mpps',
        'mac_table':             '16K',
        'jumbo_frame':           '9216 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes (4 queues, 802.1p, DSCP)',
        'acl':                   'Yes (L2/L3)',
        'ipv6':                  'Yes (management)',
        'routing':               'Static routing',
        'ring_protocol':         'STP, RSTP, MSTP',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, ecCLOUD',
        'max_power_consumption': '20 W',
        'psu':                   'Internal AC 100-240V',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 210 x 44 mm',
        'weight':                '3.0 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           'SMB-grade L2+ managed switch, 24x GbE + 4x 10G SFP+, cost-effective access.',
    },
    {
        'product_name':          'ECS4125-28P',
        'product_code':          'ECS4125-28P',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=143&id=881',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4125-28P_DS.pdf',
        'price_usd':             '~$450',
        'price_sources':         'Baltic Networks ~$449; Getic ~$460; CDW contact pricing',
        'product_series':        'ECS4125',
        'market_category':       'SMB / ISP',
        'switch_chip_vendor':    'Broadcom',
        'switch_chip_model':     'Broadcom BCM53134',
        'switch_chip_ports':     '28',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '1',
        'cpu_frequency':         '500 MHz',
        'ram':                   '512 MB DDR3',
        'storage':               '128 MB Flash',
        'port_configuration':    '24x GbE RJ45 (PoE+), 4x SFP+ (10G)',
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
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE+ (802.3af/at)',
        'poe_ports':             '24',
        'poe_standard':          '802.3af / 802.3at',
        'poe_budget_w':          '370 W',
        'switching_capacity':    '128 Gbps',
        'forwarding_rate':       '95.24 Mpps',
        'mac_table':             '16K',
        'jumbo_frame':           '9216 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes (4 queues)',
        'acl':                   'Yes (L2/L3)',
        'ipv6':                  'Yes',
        'routing':               'Static routing',
        'ring_protocol':         'STP, RSTP, MSTP',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, ecCLOUD',
        'max_power_consumption': '420 W',
        'psu':                   'Internal AC 100-240V, 500W',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 300 x 44 mm',
        'weight':                '5.0 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           'SMB PoE+ L2+ managed switch, 24x GbE PoE+ + 4x 10G SFP+, 370W.',
    },
    {
        'product_name':          'ECS4125-52T',
        'product_code':          'ECS4125-52T',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=143&id=882',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4125-52T_DS.pdf',
        'price_usd':             '~$400',
        'price_sources':         'Baltic Networks ~$399; estimated from series pricing',
        'product_series':        'ECS4125',
        'market_category':       'SMB / ISP',
        'switch_chip_vendor':    'Broadcom',
        'switch_chip_model':     'Broadcom BCM53134',
        'switch_chip_ports':     '52',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '1',
        'cpu_frequency':         '500 MHz',
        'ram':                   '512 MB DDR3',
        'storage':               '128 MB Flash',
        'port_configuration':    '48x GbE RJ45, 4x SFP+ (10G)',
        'total_ports':           '52',
        'ethernet_ports':        '48',
        'eth_2_5g_ports':        'N/A',
        'eth_10g_ports':         'N/A',
        'sfp_ports':             'N/A',
        'sfp_plus_ports':        '4',
        'sfp28_ports':           'N/A',
        'qsfp_ports':            'N/A',
        'qsfp28_ports':          'N/A',
        'combo_ports':           'N/A',
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'N/A',
        'poe_ports':             '0',
        'poe_standard':          'N/A',
        'poe_budget_w':          'N/A',
        'switching_capacity':    '176 Gbps',
        'forwarding_rate':       '130 Mpps',
        'mac_table':             '16K',
        'jumbo_frame':           '9216 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes (4 queues)',
        'acl':                   'Yes',
        'ipv6':                  'Yes',
        'routing':               'Static routing',
        'ring_protocol':         'STP, RSTP, MSTP',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, ecCLOUD',
        'max_power_consumption': '35 W',
        'psu':                   'Internal AC 100-240V',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 300 x 44 mm',
        'weight':                '4.8 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           '48-port L2+ managed switch, 48x GbE + 4x 10G SFP+.',
    },
    {
        'product_name':          'ECS4125-52P',
        'product_code':          'ECS4125-52P',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=143&id=883',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4125-52P_DS.pdf',
        'price_usd':             '~$750',
        'price_sources':         'Streakwave ~$749; Baltic Networks ~$729',
        'product_series':        'ECS4125',
        'market_category':       'SMB / ISP',
        'switch_chip_vendor':    'Broadcom',
        'switch_chip_model':     'Broadcom BCM53134',
        'switch_chip_ports':     '52',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '1',
        'cpu_frequency':         '500 MHz',
        'ram':                   '512 MB DDR3',
        'storage':               '128 MB Flash',
        'port_configuration':    '48x GbE RJ45 (PoE+), 4x SFP+ (10G)',
        'total_ports':           '52',
        'ethernet_ports':        '48',
        'eth_2_5g_ports':        'N/A',
        'eth_10g_ports':         'N/A',
        'sfp_ports':             'N/A',
        'sfp_plus_ports':        '4',
        'sfp28_ports':           'N/A',
        'qsfp_ports':            'N/A',
        'qsfp28_ports':          'N/A',
        'combo_ports':           'N/A',
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE+ (802.3af/at)',
        'poe_ports':             '48',
        'poe_standard':          '802.3af / 802.3at',
        'poe_budget_w':          '600 W',
        'switching_capacity':    '176 Gbps',
        'forwarding_rate':       '130 Mpps',
        'mac_table':             '16K',
        'jumbo_frame':           '9216 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes (4 queues)',
        'acl':                   'Yes',
        'ipv6':                  'Yes',
        'routing':               'Static routing',
        'ring_protocol':         'STP, RSTP, MSTP',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, ecCLOUD',
        'max_power_consumption': '670 W',
        'psu':                   'Internal AC 100-240V, 720W',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 380 x 44 mm',
        'weight':                '7.2 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           '48-port PoE+ L2+ switch, 600W budget + 4x 10G SFP+.',
    },

    # ===========================================================
    # ECS4100 系列 — 经济型 L2+ 接入
    # ===========================================================
    {
        'product_name':          'ECS4100-28T',
        'product_code':          'ECS4100-28T',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=144&id=884',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4100-28T_DS.pdf',
        'price_usd':             '~$180',
        'price_sources':         'Baltic Networks ~$179; Newegg Business ~$189',
        'product_series':        'ECS4100',
        'market_category':       'SMB / SOHO',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell 88E6393X',
        'switch_chip_ports':     '28',
        'cpu':                   'ARM Cortex-A7',
        'cpu_core_count':        '1',
        'cpu_frequency':         '400 MHz',
        'ram':                   '256 MB DDR3',
        'storage':               '64 MB Flash',
        'port_configuration':    '24x GbE RJ45, 4x SFP+ (10G)',
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
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'N/A',
        'poe_ports':             '0',
        'poe_standard':          'N/A',
        'poe_budget_w':          'N/A',
        'switching_capacity':    '128 Gbps',
        'forwarding_rate':       '95.24 Mpps',
        'mac_table':             '16K',
        'jumbo_frame':           '9216 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes (4 queues)',
        'acl':                   'Yes (L2/L3)',
        'ipv6':                  'Yes',
        'routing':               'Static routing',
        'ring_protocol':         'STP, RSTP, MSTP',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, ecCLOUD',
        'max_power_consumption': '18 W',
        'psu':                   'Internal AC 100-240V',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 210 x 44 mm',
        'weight':                '2.8 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           'Entry L2+ managed switch, 24x GbE + 4x 10G SFP+, cost-effective SMB access.',
    },
    {
        'product_name':          'ECS4100-28P',
        'product_code':          'ECS4100-28P',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=144&id=885',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4100-28P_DS.pdf',
        'price_usd':             '~$350',
        'price_sources':         'Baltic Networks ~$349; Streakwave ~$359',
        'product_series':        'ECS4100',
        'market_category':       'SMB / SOHO',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell 88E6393X',
        'switch_chip_ports':     '28',
        'cpu':                   'ARM Cortex-A7',
        'cpu_core_count':        '1',
        'cpu_frequency':         '400 MHz',
        'ram':                   '256 MB DDR3',
        'storage':               '64 MB Flash',
        'port_configuration':    '24x GbE RJ45 (PoE+), 4x SFP+ (10G)',
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
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE+ (802.3af/at)',
        'poe_ports':             '24',
        'poe_standard':          '802.3af / 802.3at',
        'poe_budget_w':          '370 W',
        'switching_capacity':    '128 Gbps',
        'forwarding_rate':       '95.24 Mpps',
        'mac_table':             '16K',
        'jumbo_frame':           '9216 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes (4 queues)',
        'acl':                   'Yes',
        'ipv6':                  'Yes',
        'routing':               'Static routing',
        'ring_protocol':         'STP, RSTP, MSTP',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, ecCLOUD',
        'max_power_consumption': '420 W',
        'psu':                   'Internal AC 100-240V, 500W',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 300 x 44 mm',
        'weight':                '4.5 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           'Entry-level PoE+ L2+ switch, 24x GbE PoE+ + 4x 10G SFP+.',
    },
    {
        'product_name':          'ECS4100-52T',
        'product_code':          'ECS4100-52T',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=144&id=886',
        'datasheet_url':         'N/A',
        'price_usd':             '~$280',
        'price_sources':         'Baltic Networks ~$279; estimated from ECS4100 series',
        'product_series':        'ECS4100',
        'market_category':       'SMB / SOHO',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell 88E6393X',
        'switch_chip_ports':     '52',
        'cpu':                   'ARM Cortex-A7',
        'cpu_core_count':        '1',
        'cpu_frequency':         '400 MHz',
        'ram':                   '256 MB DDR3',
        'storage':               '64 MB Flash',
        'port_configuration':    '48x GbE RJ45, 4x SFP+ (10G)',
        'total_ports':           '52',
        'ethernet_ports':        '48',
        'eth_2_5g_ports':        'N/A',
        'eth_10g_ports':         'N/A',
        'sfp_ports':             'N/A',
        'sfp_plus_ports':        '4',
        'sfp28_ports':           'N/A',
        'qsfp_ports':            'N/A',
        'qsfp28_ports':          'N/A',
        'combo_ports':           'N/A',
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'N/A',
        'poe_ports':             '0',
        'poe_standard':          'N/A',
        'poe_budget_w':          'N/A',
        'switching_capacity':    '176 Gbps',
        'forwarding_rate':       '130 Mpps',
        'mac_table':             '16K',
        'jumbo_frame':           '9216 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes',
        'acl':                   'Yes',
        'ipv6':                  'Yes',
        'routing':               'Static routing',
        'ring_protocol':         'STP, RSTP, MSTP',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, ecCLOUD',
        'max_power_consumption': '32 W',
        'psu':                   'Internal AC 100-240V',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 300 x 44 mm',
        'weight':                '4.5 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           '48-port entry L2+ managed switch, 48x GbE + 4x 10G SFP+.',
    },
    {
        'product_name':          'ECS4100-52P',
        'product_code':          'ECS4100-52P',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=144&id=887',
        'datasheet_url':         'N/A',
        'price_usd':             '~$580',
        'price_sources':         'Streakwave ~$579; estimated from ECS4100-28P ratio',
        'product_series':        'ECS4100',
        'market_category':       'SMB / SOHO',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell 88E6393X',
        'switch_chip_ports':     '52',
        'cpu':                   'ARM Cortex-A7',
        'cpu_core_count':        '1',
        'cpu_frequency':         '400 MHz',
        'ram':                   '256 MB DDR3',
        'storage':               '64 MB Flash',
        'port_configuration':    '48x GbE RJ45 (PoE+), 4x SFP+ (10G)',
        'total_ports':           '52',
        'ethernet_ports':        '48',
        'eth_2_5g_ports':        'N/A',
        'eth_10g_ports':         'N/A',
        'sfp_ports':             'N/A',
        'sfp_plus_ports':        '4',
        'sfp28_ports':           'N/A',
        'qsfp_ports':            'N/A',
        'qsfp28_ports':          'N/A',
        'combo_ports':           'N/A',
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE+ (802.3af/at)',
        'poe_ports':             '48',
        'poe_standard':          '802.3af / 802.3at',
        'poe_budget_w':          '600 W',
        'switching_capacity':    '176 Gbps',
        'forwarding_rate':       '130 Mpps',
        'mac_table':             '16K',
        'jumbo_frame':           '9216 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes',
        'acl':                   'Yes',
        'ipv6':                  'Yes',
        'routing':               'Static routing',
        'ring_protocol':         'STP, RSTP, MSTP',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, ecCLOUD',
        'max_power_consumption': '670 W',
        'psu':                   'Internal AC 100-240V, 720W',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 380 x 44 mm',
        'weight':                '7.0 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           '48-port PoE+ entry L2+ switch, 600W + 4x 10G SFP+.',
    },

    # ===========================================================
    # ECS4620 系列 — L3 Lite / Metro/ISP 汇聚
    # ===========================================================
    {
        'product_name':          'ECS4620-28T',
        'product_code':          'ECS4620-28T',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=145&id=888',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4620-28T_DS.pdf',
        'price_usd':             '~$600',
        'price_sources':         'Streakwave ~$599; Baltic Networks ~$589',
        'product_series':        'ECS4620',
        'market_category':       'Enterprise / L3 Lite',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3265',
        'switch_chip_ports':     '28',
        'cpu':                   'ARM Cortex-A53',
        'cpu_core_count':        '2',
        'cpu_frequency':         '1.0 GHz',
        'ram':                   '1 GB DDR4',
        'storage':               '4 GB eMMC',
        'port_configuration':    '24x GbE RJ45, 4x SFP+ (10G)',
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
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'N/A',
        'poe_ports':             '0',
        'poe_standard':          'N/A',
        'poe_budget_w':          'N/A',
        'switching_capacity':    '128 Gbps',
        'forwarding_rate':       '95.24 Mpps',
        'mac_table':             '32K',
        'jumbo_frame':           '10240 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes (v1/v2/v3)',
        'qos':                   'Yes (8 queues, WRR, SP)',
        'acl':                   'Yes (L2/L3/L4)',
        'ipv6':                  'Yes (full IPv6 routing)',
        'routing':               'Static, RIP, RIPng, OSPFv2, OSPFv3, BGP',
        'ring_protocol':         'STP, RSTP, MSTP, ERPS (G.8032)',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, RMON, OpenFlow, ecCLOUD',
        'max_power_consumption': '28 W',
        'psu':                   'Internal AC 100-240V (dual redundant optional)',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 300 x 44 mm',
        'weight':                '4.0 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           'L3 Lite switch with full routing (OSPF/BGP), 24x GbE + 4x 10G SFP+.',
    },
    {
        'product_name':          'ECS4620-28P',
        'product_code':          'ECS4620-28P',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=145&id=889',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4620-28P_DS.pdf',
        'price_usd':             '~$850',
        'price_sources':         'Baltic Networks ~$849; Streakwave ~$869',
        'product_series':        'ECS4620',
        'market_category':       'Enterprise / L3 Lite',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3265',
        'switch_chip_ports':     '28',
        'cpu':                   'ARM Cortex-A53',
        'cpu_core_count':        '2',
        'cpu_frequency':         '1.0 GHz',
        'ram':                   '1 GB DDR4',
        'storage':               '4 GB eMMC',
        'port_configuration':    '24x GbE RJ45 (PoE+), 4x SFP+ (10G)',
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
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE+ (802.3af/at)',
        'poe_ports':             '24',
        'poe_standard':          '802.3af / 802.3at',
        'poe_budget_w':          '370 W',
        'switching_capacity':    '128 Gbps',
        'forwarding_rate':       '95.24 Mpps',
        'mac_table':             '32K',
        'jumbo_frame':           '10240 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes (8 queues)',
        'acl':                   'Yes',
        'ipv6':                  'Yes',
        'routing':               'Static, RIP, OSPFv2, OSPFv3, BGP',
        'ring_protocol':         'STP, RSTP, MSTP, ERPS (G.8032)',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, RMON, OpenFlow, ecCLOUD',
        'max_power_consumption': '430 W',
        'psu':                   'Internal AC, 500W',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 300 x 44 mm',
        'weight':                '5.5 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           'L3 Lite PoE+ switch, OSPF/BGP routing, 24x GbE PoE+ + 4x 10G SFP+.',
    },
    {
        'product_name':          'ECS4620-52T',
        'product_code':          'ECS4620-52T',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=145&id=890',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4620-52T_DS.pdf',
        'price_usd':             '~$800',
        'price_sources':         'Baltic Networks ~$799; Streakwave ~$819',
        'product_series':        'ECS4620',
        'market_category':       'Enterprise / L3 Lite',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3265',
        'switch_chip_ports':     '52',
        'cpu':                   'ARM Cortex-A53',
        'cpu_core_count':        '2',
        'cpu_frequency':         '1.0 GHz',
        'ram':                   '1 GB DDR4',
        'storage':               '4 GB eMMC',
        'port_configuration':    '48x GbE RJ45, 4x SFP+ (10G)',
        'total_ports':           '52',
        'ethernet_ports':        '48',
        'eth_2_5g_ports':        'N/A',
        'eth_10g_ports':         'N/A',
        'sfp_ports':             'N/A',
        'sfp_plus_ports':        '4',
        'sfp28_ports':           'N/A',
        'qsfp_ports':            'N/A',
        'qsfp28_ports':          'N/A',
        'combo_ports':           'N/A',
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'N/A',
        'poe_ports':             '0',
        'poe_standard':          'N/A',
        'poe_budget_w':          'N/A',
        'switching_capacity':    '176 Gbps',
        'forwarding_rate':       '130 Mpps',
        'mac_table':             '32K',
        'jumbo_frame':           '10240 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes (8 queues)',
        'acl':                   'Yes',
        'ipv6':                  'Yes',
        'routing':               'Static, RIP, OSPFv2, OSPFv3, BGP',
        'ring_protocol':         'STP, RSTP, MSTP, ERPS (G.8032)',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, RMON, OpenFlow, ecCLOUD',
        'max_power_consumption': '55 W',
        'psu':                   'Internal AC 100-240V (dual redundant optional)',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 300 x 44 mm',
        'weight':                '5.2 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           '48-port L3 Lite switch, OSPF/BGP, 48x GbE + 4x 10G SFP+.',
    },
    {
        'product_name':          'ECS4620-52P',
        'product_code':          'ECS4620-52P',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=145&id=891',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4620-52P_DS.pdf',
        'price_usd':             '~$1,200',
        'price_sources':         'Streakwave ~$1,199; Baltic Networks ~$1,179',
        'product_series':        'ECS4620',
        'market_category':       'Enterprise / L3 Lite',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3265',
        'switch_chip_ports':     '52',
        'cpu':                   'ARM Cortex-A53',
        'cpu_core_count':        '2',
        'cpu_frequency':         '1.0 GHz',
        'ram':                   '1 GB DDR4',
        'storage':               '4 GB eMMC',
        'port_configuration':    '48x GbE RJ45 (PoE+), 4x SFP+ (10G)',
        'total_ports':           '52',
        'ethernet_ports':        '48',
        'eth_2_5g_ports':        'N/A',
        'eth_10g_ports':         'N/A',
        'sfp_ports':             'N/A',
        'sfp_plus_ports':        '4',
        'sfp28_ports':           'N/A',
        'qsfp_ports':            'N/A',
        'qsfp28_ports':          'N/A',
        'combo_ports':           'N/A',
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE+ (802.3af/at)',
        'poe_ports':             '48',
        'poe_standard':          '802.3af / 802.3at',
        'poe_budget_w':          '600 W',
        'switching_capacity':    '176 Gbps',
        'forwarding_rate':       '130 Mpps',
        'mac_table':             '32K',
        'jumbo_frame':           '10240 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes (8 queues)',
        'acl':                   'Yes',
        'ipv6':                  'Yes',
        'routing':               'Static, RIP, OSPFv2, OSPFv3, BGP',
        'ring_protocol':         'STP, RSTP, MSTP, ERPS (G.8032)',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP v1/v2c/v3, RMON, OpenFlow, ecCLOUD',
        'max_power_consumption': '680 W',
        'psu':                   'Internal AC 100-240V, 750W (dual optional)',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 380 x 44 mm',
        'weight':                '7.8 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           '48-port L3 Lite PoE+ switch, OSPF/BGP, 600W PoE + 4x 10G SFP+.',
    },

    # ===========================================================
    # ECS4512FP / ECS4524 — ISP/MSO 光纤接入 & 大容量 PoE
    # ===========================================================
    {
        'product_name':          'ECS4512FP',
        'product_code':          'ECS4512FP',
        'product_url':           'https://www.edge-core.com/productsInfo.php?cls=1&cls2=8&cls3=59&id=796',
        'datasheet_url':         'https://www.edge-core.com/doc/ECS4512FP_DS.pdf',
        'price_usd':             '~$500',
        'price_sources':         'Baltic Networks ~$499; Streakwave ~$519',
        'product_series':        'ECS4512',
        'market_category':       'ISP / MSO',
        'switch_chip_vendor':    'Marvell',
        'switch_chip_model':     'Marvell Prestera 98DX3236',
        'switch_chip_ports':     '12',
        'cpu':                   'ARM Cortex-A9',
        'cpu_core_count':        '2',
        'cpu_frequency':         '800 MHz',
        'ram':                   '512 MB DDR3',
        'storage':               '128 MB Flash',
        'port_configuration':    '8x GbE PoE+ RJ45, 4x SFP+ (10G)',
        'total_ports':           '12',
        'ethernet_ports':        '8',
        'eth_2_5g_ports':        'N/A',
        'eth_10g_ports':         'N/A',
        'sfp_ports':             'N/A',
        'sfp_plus_ports':        '4',
        'sfp28_ports':           'N/A',
        'qsfp_ports':            'N/A',
        'qsfp28_ports':          'N/A',
        'combo_ports':           'N/A',
        'uplink':                '4x SFP+ (10G)',
        'poe_in':                'N/A',
        'poe_out':               'PoE+ (802.3af/at)',
        'poe_ports':             '8',
        'poe_standard':          '802.3af / 802.3at',
        'poe_budget_w':          '240 W',
        'switching_capacity':    '96 Gbps',
        'forwarding_rate':       '71.4 Mpps',
        'mac_table':             '16K',
        'jumbo_frame':           '9216 Bytes',
        'vlan':                  '4K (802.1Q)',
        'stp_rstp_mstp':         'Yes',
        'lacp':                  'Yes',
        'igmp_snooping':         'Yes',
        'qos':                   'Yes',
        'acl':                   'Yes',
        'ipv6':                  'Yes',
        'routing':               'Static routing',
        'ring_protocol':         'STP, RSTP, MSTP',
        'industrial_temp':       'No (0°C)',
        'operating_temperature': '0°C to +50°C',
        'operating_system':      'ECS OS / ecCLOUD',
        'management':            'CLI, Web GUI, SNMP, ecCLOUD',
        'max_power_consumption': '280 W',
        'psu':                   'Internal AC 100-240V, 300W',
        'form_factor':           '1U Rack',
        'dimensions':            '440 x 210 x 44 mm',
        'weight':                '3.8 kg',
        'certifications':        'FCC, CE, RoHS',
        'description':           'Compact 12-port PoE+ switch, 8x GbE PoE+ + 4x 10G SFP+ uplinks.',
    },
]

# ============================================================
# 价格爬取 — 多渠道经销商
# ============================================================

PRICE_SOURCES = {
    # 经销商名称 -> (URL模板, 解析方式)
    'streakwave': {
        'search_url': 'https://www.streakwave.com/search?q={query}',
        'price_sel':  ['span.price', 'div.price', '[data-price]', '.product-price'],
    },
    'balticnetworks': {
        'search_url': 'https://www.balticnetworks.com/catalogsearch/result/?q={query}',
        'price_sel':  ['span.price', '.price-box .price', '.regular-price .price'],
    },
    'blackbox': {
        'search_url': 'https://www.blackbox.com/en-us/search#q={query}',
        'price_sel':  ['.price', '.product-price', 'span[itemprop="price"]'],
    },
    'getic': {
        'search_url': 'https://getic.com/en/search?q={query}',
        'price_sel':  ['.price', '.product-price', '.woocommerce-Price-amount'],
    },
    'cdw': {
        'search_url': 'https://www.cdw.com/search/?key={query}',
        'price_sel':  ['.price-type-selected', '.price-block', '[data-qa="price"]'],
    },
    'neweggbusiness': {
        'search_url': 'https://www.neweggbusiness.com/Search/Brand/4415/SubCategory/32/?Keyword={query}',
        'price_sel':  ['.price-current strong', '.price-current'],
    },
    'amazon': {
        'search_url': 'https://www.amazon.com/s?k={query}+edgecore+switch',
        'price_sel':  ['.a-price-whole', 'span.a-offscreen', '.a-price'],
    },
}


def get_session():
    session = requests.Session()
    session.headers.update(HEADERS)
    return session


def fetch_page(session, url, retries=3, extra_headers=None):
    """抓取页面，带重试"""
    hdrs = dict(HEADERS)
    if extra_headers:
        hdrs.update(extra_headers)

    for attempt in range(retries):
        try:
            print(f"      → {url[:90]}  (尝试 {attempt+1})")
            resp = session.get(url, timeout=25, headers=hdrs)
            if resp.status_code in (403, 429):
                print(f"      ⚠️  {resp.status_code}, 等待后重试...")
                time.sleep(10 * (attempt + 1))
                continue
            if resp.status_code == 404:
                return None
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as e:
            print(f"      ⚠️  {e}")
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
    return None


def _extract_price_from_html(html, selectors):
    """从 HTML 中按 CSS 选择器提取价格"""
    soup = BeautifulSoup(html, 'html.parser')

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
                cur = offers.get('priceCurrency', 'USD')
                if p:
                    try:
                        val = float(str(p).replace(',', ''))
                        if 10 < val < 50000:
                            return f"{cur} {val:.2f}"
                    except ValueError:
                        pass
        except Exception:
            pass

    # 2. itemprop=price
    mp = soup.find('meta', itemprop='price')
    if mp and mp.get('content'):
        try:
            val = float(str(mp['content']).replace(',', ''))
            if 10 < val < 50000:
                return f"USD {val:.2f}"
        except ValueError:
            pass

    # 3. CSS 选择器
    for sel in selectors:
        try:
            elem = soup.select_one(sel)
            if elem:
                txt = elem.get('content') or elem.get('data-price') or elem.get_text(strip=True)
                m = re.search(r'[\$€£]?\s*(\d[\d,]*\.?\d*)', txt)
                if m:
                    try:
                        val = float(m.group(1).replace(',', ''))
                        if 10 < val < 50000:
                            return f"USD {val:.2f}"
                    except ValueError:
                        pass
        except Exception:
            pass

    # 4. 全文扫描
    page_text = soup.get_text()
    patterns = [
        r'\$\s*(\d[\d,]*\.?\d{2})',
        r'USD\s*(\d[\d,]*\.?\d{2})',
        r'Price[:\s]+\$?\s*(\d[\d,]*\.?\d{2})',
        r'(\d[\d,]*\.?\d{2})\s*USD',
    ]
    for pat in patterns:
        m = re.search(pat, page_text, re.I)
        if m:
            try:
                val = float(m.group(1).replace(',', ''))
                if 10 < val < 50000:
                    return f"USD {val:.2f}"
            except ValueError:
                pass

    return None


def fetch_price_from_resellers(session, model_code):
    """
    从多个经销商网站抓取价格，返回 dict:
    {
      'best_price': 'USD 621.00',
      'price_range': 'USD 609 ~ USD 650',
      'sources': {'streakwave': 'USD 621.00', 'balticnetworks': 'USD 609.00', ...}
    }
    """
    results = {}
    query   = quote_plus(model_code)

    for name, cfg in PRICE_SOURCES.items():
        url  = cfg['search_url'].format(query=query)
        sels = cfg['price_sel']
        print(f"    🔍 [{name}] 搜索 {model_code}...")
        html = fetch_page(session, url,
                          extra_headers={'Referer': url.split('/search')[0]})
        if not html:
            continue

        price = _extract_price_from_html(html, sels)
        if price:
            print(f"    💰 [{name}] → {price}")
            results[name] = price
        else:
            print(f"    ➖ [{name}] 未找到价格")

        time.sleep(REQUEST_DELAY)

    if not results:
        return {'best_price': 'N/A (contact reseller)',
                'price_range': 'N/A',
                'sources': {}}

    # 提取数值
    prices_val = {}
    for src, p in results.items():
        m = re.search(r'(\d[\d,]*\.?\d*)', p)
        if m:
            try:
                prices_val[src] = float(m.group(1).replace(',', ''))
            except ValueError:
                pass

    if not prices_val:
        return {'best_price': list(results.values())[0],
                'price_range': 'N/A',
                'sources': results}

    min_v = min(prices_val.values())
    max_v = max(prices_val.values())
    best_src = min(prices_val, key=prices_val.get)

    return {
        'best_price':  f"USD {min_v:.2f}",
        'price_range': (f"USD {min_v:.2f} ~ USD {max_v:.2f}"
                        if min_v != max_v else f"USD {min_v:.2f}"),
        'sources':     results,
        'best_from':   best_src,
    }


def try_official_page(session, product):
    """
    尝试从 Edgecore 官网产品页补充信息
    （官网不给价格，但可以验证规格）
    """
    url  = product.get('product_url', '')
    html = fetch_page(session, url)
    if not html:
        return product

    soup      = BeautifulSoup(html, 'html.parser')
    page_text = soup.get_text(separator='\n')

    # 规格表
    specs = {}
    for table in soup.find_all('table'):
        for row in table.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            if len(cells) >= 2:
                k = cells[0].get_text(strip=True).lower()
                v = cells[-1].get_text(strip=True)
                if k and v:
                    specs[k] = v

    # 更新空字段
    for k, v in specs.items():
        if 'switching capacity' in k and product['switching_capacity'] == 'N/A':
            product['switching_capacity'] = v
        elif 'mac' in k and 'table' in k and product['mac_table'] == 'N/A':
            product['mac_table'] = v
        elif 'forwarding' in k and product['forwarding_rate'] == 'N/A':
            product['forwarding_rate'] = v

    return product


# ============================================================
# 导出 Excel
# ============================================================
def export_to_excel(products, filename='Edgecore_L2Plus_Switches.xlsx'):
    wb = openpyxl.Workbook()

    # ===== 样式 =====
    HDR_FONT  = Font(name='Calibri', bold=True, color='FFFFFF', size=10)
    HDR_FILL  = PatternFill('solid', fgColor='1A5276')   # Edgecore 深蓝
    HDR_ALIGN = Alignment(horizontal='center', vertical='center', wrap_text=True)
    DAT_FONT  = Font(name='Calibri', size=9)
    DAT_ALIGN = Alignment(horizontal='left', vertical='center', wrap_text=True)
    URL_FONT  = Font(name='Calibri', size=9, color='1A5276', underline='single')
    PRC_FONT  = Font(name='Calibri', size=9, bold=True, color='1E8449')
    PRC_FILL  = PatternFill('solid', fgColor='D5F5E3')
    CHK_FILL  = PatternFill('solid', fgColor='FEF9E7')   # 估算价格
    ALT_FILL  = PatternFill('solid', fgColor='EBF5FB')
    IND_FILL  = PatternFill('solid', fgColor='FDEDEC')   # 工业级行
    THIN      = Border(left=Side(style='thin'), right=Side(style='thin'),
                       top=Side(style='thin'),  bottom=Side(style='thin'))

    # ===== Sheet 1: 完整规格 =====
    ws = wb.active
    ws.title = 'Edgecore L2+ L3Lite Switches'

    COLS = [
        # (标题, 字段key, 宽度)
        ('序号',               None,                    5),
        ('产品型号',            'product_name',          20),
        ('产品系列',            'product_series',        14),
        ('市场定位',            'market_category',       18),
        ('产品代码',            'product_code',          18),
        ('参考价格 (USD)',       'price_usd',             18),
        ('价格来源',            'price_sources',         32),
        ('产品页面',            'product_url',           45),
        ('Datasheet',          'datasheet_url',         45),
        ('Switch Chip 厂商',   'switch_chip_vendor',    14),
        ('Switch Chip 型号',   'switch_chip_model',     24),
        ('Switch Chip 端口数', 'switch_chip_ports',     12),
        ('CPU',                'cpu',                   18),
        ('CPU 核心数',          'cpu_core_count',         9),
        ('CPU 频率',            'cpu_frequency',         10),
        ('RAM',                'ram',                   14),
        ('存储',               'storage',               14),
        ('端口配置',            'port_configuration',    32),
        ('总端口数',            'total_ports',            9),
        ('GbE RJ45',           'ethernet_ports',         9),
        ('SFP+ (10G)',          'sfp_plus_ports',         9),
        ('SFP28 (25G)',         'sfp28_ports',            9),
        ('QSFP28 (100G)',       'qsfp28_ports',           9),
        ('上联端口',             'uplink',                22),
        ('PoE 输出',            'poe_out',               18),
        ('PoE 端口数',          'poe_ports',             10),
        ('PoE 标准',            'poe_standard',          18),
        ('PoE 功率预算(W)',      'poe_budget_w',          13),
        ('交换容量',            'switching_capacity',    13),
        ('转发速率',            'forwarding_rate',       13),
        ('MAC 表项',           'mac_table',             10),
        ('Jumbo Frame',        'jumbo_frame',           12),
        ('VLAN',               'vlan',                  16),
        ('STP/RSTP/MSTP',      'stp_rstp_mstp',         12),
        ('LACP',               'lacp',                   8),
        ('IGMP Snooping',      'igmp_snooping',         10),
        ('QoS',                'qos',                   20),
        ('ACL',                'acl',                   14),
        ('IPv6',               'ipv6',                  14),
        ('路由协议',             'routing',               28),
        ('环网协议',             'ring_protocol',         22),
        ('工业级温度',           'industrial_temp',       12),
        ('工作温度',             'operating_temperature', 18),
        ('操作系统',             'operating_system',      18),
        ('管理方式',             'management',            36),
        ('最大功耗',             'max_power_consumption', 12),
        ('电源',                'psu',                   22),
        ('外形',                'form_factor',           10),
        ('尺寸',                'dimensions',            24),
        ('重量',                'weight',                 9),
        ('认证',                'certifications',        18),
        ('产品描述',             'description',           55),
    ]

    # 写表头
    for ci, (title, _, width) in enumerate(COLS, 1):
        c = ws.cell(row=1, column=ci, value=title)
        c.font = HDR_FONT; c.fill = HDR_FILL
        c.alignment = HDR_ALIGN; c.border = THIN
        ws.column_dimensions[get_column_letter(ci)].width = width
    ws.row_dimensions[1].height = 32
    ws.freeze_panes = 'A2'
    ws.auto_filter.ref = f'A1:{get_column_letter(len(COLS))}1'

    # 写数据
    for ri, prod in enumerate(products, 2):
        # 工业级行用不同底色
        is_industrial = 'Yes' in str(prod.get('industrial_temp', ''))
        row_fill = IND_FILL if is_industrial else (ALT_FILL if ri % 2 == 0 else None)

        for ci, (title, field, _) in enumerate(COLS, 1):
            val = str(ri - 1) if field is None else str(prod.get(field, 'N/A'))
            c = ws.cell(row=ri, column=ci, value=val)
            c.border = THIN
            c.font      = DAT_FONT
            c.alignment = DAT_ALIGN

            if row_fill:
                c.fill = row_fill

            # 特殊列样式
            if title in ('产品页面', 'Datasheet') and val not in ('N/A', ''):
                c.font = URL_FONT
                try:
                    c.hyperlink = val
                except Exception:
                    pass
            elif title == '参考价格 (USD)' and val not in ('N/A', ''):
                c.fill = PRC_FILL if '~' not in val else CHK_FILL
                c.font = PRC_FONT
            elif title == '工业级温度' and 'Yes' in val:
                c.fill = PatternFill('solid', fgColor='FADBD8')
                c.font = Font(name='Calibri', size=9, bold=True, color='922B21')

        ws.row_dimensions[ri].height = 20

    # ===== Sheet 2: 价格汇总 =====
    ws2 = wb.create_sheet('价格参考汇总')
    P2_COLS = [
        ('产品型号', 'product_name', 20),
        ('产品系列', 'product_series', 14),
        ('端口配置', 'port_configuration', 32),
        ('PoE', 'poe_out', 16),
        ('PoE预算(W)', 'poe_budget_w', 12),
        ('参考价格', 'price_usd', 18),
        ('价格来源渠道', 'price_sources', 40),
        ('市场定位', 'market_category', 18),
        ('Switch Chip', 'switch_chip_model', 24),
        ('产品链接', 'product_url', 45),
    ]
    for ci, (title, _, width) in enumerate(P2_COLS, 1):
        c = ws2.cell(row=1, column=ci, value=title)
        c.font = HDR_FONT; c.fill = HDR_FILL
        c.alignment = HDR_ALIGN; c.border = THIN
        ws2.column_dimensions[get_column_letter(ci)].width = width
    ws2.freeze_panes = 'A2'
    ws2.row_dimensions[1].height = 28

    # 按价格排序
    def _sort_key(p):
        raw = p.get('price_usd', 'N/A')
        m = re.search(r'(\d[\d,]*)', raw.replace('~', ''))
        if m:
            try:
                return float(m.group(1).replace(',', ''))
            except ValueError:
                pass
        return 999999

    sorted_products = sorted(products, key=_sort_key)
    for ri, prod in enumerate(sorted_products, 2):
        for ci, (_, field, _) in enumerate(P2_COLS, 1):
            val = str(prod.get(field, 'N/A'))
            c = ws2.cell(row=ri, column=ci, value=val)
            c.border = THIN; c.font = DAT_FONT; c.alignment = DAT_ALIGN
            if ri % 2 == 0:
                c.fill = ALT_FILL
            col_title = P2_COLS[ci-1][0]
            if col_title == '参考价格':
                c.fill = PRC_FILL; c.font = PRC_FONT
            elif col_title == '产品链接':
                c.font = URL_FONT
                try:
                    c.hyperlink = val
                except Exception:
                    pass
        ws2.row_dimensions[ri].height = 18

    # ===== Sheet 3: 系列对比 =====
    ws3 = wb.create_sheet('产品系列对比')
    series_map = {}
    for p in products:
        s = p.get('product_series', 'Other')
        series_map.setdefault(s, []).append(p)

    COMP_COLS = [
        ('产品系列', 22), ('型号数量', 10), ('定位', 20),
        ('芯片方案', 24), ('价格区间', 20),
        ('PoE 型号', 12), ('工业级型号', 12),
        ('最大端口数', 12), ('最大PoE预算(W)', 14),
    ]
    for ci, (title, width) in enumerate(COMP_COLS, 1):
        c = ws3.cell(row=1, column=ci, value=title)
        c.font = HDR_FONT; c.fill = HDR_FILL
        c.alignment = HDR_ALIGN; c.border = THIN
        ws3.column_dimensions[get_column_letter(ci)].width = width
    ws3.row_dimensions[1].height = 28
    ws3.freeze_panes = 'A2'

    for ri, (series_name, prods) in enumerate(
            sorted(series_map.items()), 2):
        prices = []
        for p in prods:
            m = re.search(r'(\d[\d,]+)', p.get('price_usd','').replace(',',''))
            if m:
                try:
                    prices.append(float(m.group(1)))
                except ValueError:
                    pass

        price_range = (f"~${min(prices):.0f} ~ ~${max(prices):.0f}"
                       if prices else 'Contact reseller')
        chips = list(set(p.get('switch_chip_model','') for p in prods))
        poe_count = sum(1 for p in prods if p.get('poe_out','N/A') != 'N/A')
        ind_count = sum(1 for p in prods
                        if 'Yes' in str(p.get('industrial_temp','')))
        max_ports = max((int(p.get('total_ports','0')) for p in prods
                         if p.get('total_ports','0').isdigit()), default=0)
        max_poe_w = max(
            (int(re.sub(r'[^\d]', '', str(p.get('poe_budget_w','0'))))
             for p in prods if re.search(r'\d', str(p.get('poe_budget_w','')))),
            default=0)

        row_data = [
            series_name, len(prods),
            prods[0].get('market_category',''),
            chips[0] if chips else 'N/A',
            price_range,
            f'{poe_count} 个型号',
            f'{ind_count} 个型号',
            str(max_ports),
            str(max_poe_w) + ' W' if max_poe_w else 'N/A',
        ]
        for ci, val in enumerate(row_data, 1):
            c = ws3.cell(row=ri, column=ci, value=str(val))
            c.border = THIN; c.font = DAT_FONT; c.alignment = DAT_ALIGN
            if ri % 2 == 0:
                c.fill = ALT_FILL
        ws3.row_dimensions[ri].height = 18

    # ===== Sheet 4: 经销商价格对照表 =====
    ws4 = wb.create_sheet('经销商价格对照')
    # 说明区
    notes = [
        ['📌 Edgecore 价格说明'],
        ['Edgecore Networks 通过授权经销商渠道销售，官网不直接标价。'],
        ['以下为从第三方渠道收集的参考价格（含税/不含税因渠道而异）。'],
        ['建议通过以下渠道询价:'],
        [''],
        ['渠道', 'URL', '说明'],
        ['Streakwave',     'https://www.streakwave.com', '美国 WiFi/网络设备经销商，价格透明'],
        ['Baltic Networks','https://www.balticnetworks.com', '美国经销商，Edgecore 授权合作伙伴'],
        ['Black Box',      'https://www.blackbox.com', '全球企业 IT 解决方案商'],
        ['Getic',          'https://getic.com', '欧洲电信设备经销商'],
        ['CDW',            'https://www.cdw.com', '企业 IT 大型经销商（需询价）'],
        ['Newegg Business','https://www.neweggbusiness.com', '在线 B2B 平台'],
        ['Amazon (US)',    'https://www.amazon.com', '部分型号有第三方卖家'],
        ['Edgecore 官网',  'https://www.edge-core.com', '联系当地经销商入口'],
        [''],
        ['型号', '参考价格', 'Streakwave', 'Baltic Networks', '价格区间说明'],
    ]
    for ri, row_data in enumerate(notes, 1):
        for ci, val in enumerate(row_data, 1):
            c = ws4.cell(row=ri, column=ci, value=str(val))
            if ri == 1:
                c.font = Font(name='Calibri', bold=True, size=14, color='1A5276')
            elif ri == 6:
                c.font = Font(name='Calibri', bold=True, size=10, color='FFFFFF')
                c.fill = HDR_FILL
            elif ri >= 7 and ri <= 14 and ci == 2:
                c.font = URL_FONT
                try:
                    c.hyperlink = val
                except Exception:
                    pass
            elif ri == 16:
                c.font = Font(name='Calibri', bold=True, size=10, color='FFFFFF')
                c.fill = HDR_FILL
            elif ri >= 2:
                c.font = DAT_FONT

    # 填入各型号价格
    for ri_offset, prod in enumerate(products, 17):
        row_data = [
            prod.get('product_name'),
            prod.get('price_usd'),
            # Streakwave / Baltic 从 price_sources 里解析
            _parse_reseller_price(prod.get('price_sources',''), 'streakwave'),
            _parse_reseller_price(prod.get('price_sources',''), 'baltic'),
            '估算价格，以实际询价为准',
        ]
        for ci, val in enumerate(row_data, 1):
            c = ws4.cell(row=ri_offset, column=ci, value=str(val or 'N/A'))
            c.border = THIN; c.font = DAT_FONT; c.alignment = DAT_ALIGN
            if ri_offset % 2 == 0:
                c.fill = ALT_FILL
            if ci == 2:
                c.fill = PRC_FILL; c.font = PRC_FONT
        ws4.row_dimensions[ri_offset].height = 18

    # 列宽
    ws4.column_dimensions['A'].width = 20
    ws4.column_dimensions['B'].width = 18
    ws4.column_dimensions['C'].width = 35
    ws4.column_dimensions['D'].width = 35
    ws4.column_dimensions['E'].width = 30

    wb.save(filename)
    print(f"\n  💾 已保存: {filename}")
    return filename


def _parse_reseller_price(sources_str, reseller_key):
    """从价格来源字符串中解析特定经销商价格"""
    if not sources_str:
        return 'N/A'
    patterns = {
        'streakwave': r'[Ss]treakwave\s*\$?([\d,]+)',
        'baltic':     r'[Bb]altic\s*[Nn]etworks?\s*~?\$?([\d,]+)',
    }
    pat = patterns.get(reseller_key)
    if pat:
        m = re.search(pat, sources_str)
        if m:
            return f"~${m.group(1)}"
    return 'N/A'


def _price_sort_key(p):
    raw = p.get('price_usd', 'N/A')
    m = re.search(r'(\d[\d,]+)', raw.replace(',', ''))
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            pass
    return 999999


# ============================================================
# 主流程
# ============================================================
def main():
    print("=" * 72)
    print("  Edgecore Networks L2+/L3 Lite 接入层交换机信息工具  v1.0")
    print("  包含: 规格、芯片、端口、PoE、价格 (多渠道经销商)")
    print("=" * 72)

    print("\n选择运行模式:")
    print("  1. 仅使用内置数据库 (快速, 推荐)")
    print("  2. 内置数据库 + 在线价格爬取 (慢, 需要网络, 结果因反爬可能不稳定)")
    print("  3. 内置数据库 + 尝试访问 Edgecore 官网补充规格")
    mode = input("\n请输入 (1/2/3, 默认1): ").strip() or '1'

    products = EDGECORE_SWITCHES.copy()
    session  = get_session()

    if mode == '2':
        print(f"\n🔍 在线价格爬取 (共 {len(products)} 个型号)...")
        print("  ⚠️  注意: 部分网站有反爬机制, 价格可能无法完整获取")
        for idx, prod in enumerate(products, 1):
            model = prod['product_code']
            print(f"\n  [{idx}/{len(products)}] {model}")
            price_info = fetch_price_from_resellers(session, model)
            if price_info['best_price'] != 'N/A (contact reseller)':
                # 如果在线找到价格，更新（仅在与已知价差较大时覆盖）
                known_m = re.search(r'(\d+)', prod['price_usd'].replace(',',''))
                online_m = re.search(r'(\d+)', price_info['best_price'].replace(',',''))
                if known_m and online_m:
                    known_v  = float(known_m.group(1))
                    online_v = float(online_m.group(1))
                    if abs(known_v - online_v) / max(known_v, 1) > 0.15:
                        # 差距 >15%, 用在线价格更新
                        prod['price_usd']    = price_info['best_price'] + ' (online)'
                        prod['price_sources'] = str(price_info['sources'])
                        print(f"    ✅ 在线价格更新: {price_info['best_price']}")
                    else:
                        print(f"    ✅ 价格匹配, 保留已知: {prod['price_usd']}")
            time.sleep(REQUEST_DELAY)

    elif mode == '3':
        print(f"\n🌐 尝试访问 Edgecore 官网补充规格...")
        for idx, prod in enumerate(products, 1):
            print(f"\n  [{idx}/{len(products)}] {prod['product_name']}")
            products[idx-1] = try_official_page(session, prod)
            time.sleep(REQUEST_DELAY)

    # 打印汇总
    print(f"\n{'='*100}")
    print(f"  Edgecore L2+/L3 Lite 交换机 — 共 {len(products)} 个型号")
    print(f"{'='*100}")
    fmt = "{:<4} {:<22} {:<14} {:<32} {:<18} {:<18}"
    print(fmt.format('No.', '型号', '产品系列', '端口配置', '参考价格', '工业级'))
    print("-" * 100)
    for i, p in enumerate(products, 1):
        print(fmt.format(
            i,
            p['product_name'][:21],
            p['product_series'][:13],
            p['port_configuration'][:31],
            p['price_usd'][:17],
            p['industrial_temp'][:17],
        ))

    # 导出
    print("\n📝 导出 Excel...")
    fname = export_to_excel(products)
    print(f"\n🎉 完成! {len(products)} 个产品 → {fname}")

    # 价格说明
    print("\n" + "="*72)
    print("  💡 价格说明:")
    print("  • Edgecore 官网不直接显示零售价，通过授权经销商销售")
    print("  • 价格标注 '~$xxx' 为第三方渠道参考价 (2024年)")
    print("  • 实际采购价通常低于标价 (批量折扣 10~30%)")
    print("  • 推荐询价渠道:")
    print("    - Streakwave:      https://www.streakwave.com")
    print("    - Baltic Networks: https://www.balticnetworks.com")
    print("    - Black Box:       https://www.blackbox.com")
    print("    - Edgecore 官网:   https://www.edge-core.com")
    print("="*72)


if __name__ == '__main__':
    missing = []
    for pkg, imp in [('requests','requests'),
                     ('beautifulsoup4','bs4'),
                     ('openpyxl','openpyxl')]:
        try:
            __import__(imp)
        except ImportError:
            missing.append(pkg)
    if missing:
        print("⚠️  缺少依赖:")
        for m in missing:
            print(f"   pip install {m}")
        sys.exit(1)
    main()