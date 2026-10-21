#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saga Clients · 第 2 步：规范化 → 归并重复 → 规则分级（+人工定级覆盖）→ 编号。

输入：data/saga_clients/rows_raw.jsonl, followups.jsonl（extract.py 产出）
      data/saga_clients/人工定级.csv（可选：编号或键 → 等级，用户/代理人工覆盖）
      data/saga_clients/research/*.json（可选：调研结果，含 grade_override / notes）
      data/saga_clients/编号登记.json（编号登记簿：键 → 编号，追加不改）
输出：data/saga_clients/entities.json      每个客户实体的全部聚合信息（渲染用）
      data/saga_clients/客户主表.csv        一行一个客户（编号 / 等级 / 依据 / 来源 / 联系方式…）
      data/saga_clients/重复客户归并记录.md  谁和谁被并成一个、依据什么键、冲突说明
      data/saga_clients/build_stats.json
"""
import csv
import datetime as dt
import glob
import json
import os
import re
from collections import Counter, OrderedDict, defaultdict

from common import (DATA, ROOT, RESEARCH_DIR, FREEMAIL, FILE_COUNTRY, EMAIL_RE, URL_RE, PHONE_RE,
                    registrable_domain, norm_country, norm_name)

PLATFORM_DOMAINS = {
    'alibaba.com', 'aliexpress.com', 'made-in-china.com', 'globalsources.com', 'linkedin.com', 'facebook.com', 'instagram.com',
    'youtube.com', 'google.com', 'amazon.com', 'amazon.in', 'amazon.de', 'amazon.co.uk', 'amazon.ae', 'amazon.sa', 'ebay.com',
    'indiamart.com', 'tradekey.com', 'tradeindia.com', 'exportersindia.com', 'justdial.com', 'yellowpages.com', 'kompass.com',
    'europages.com', 'wikipedia.org', 'twitter.com', 'x.com', 'wa.me', 'whatsapp.com', 'tiktok.com', 'pinterest.com', 'bing.com',
    'yandex.ru', 'avito.ru', 'ozon.ru', 'wildberries.ru', 'tokopedia.com', 'shopee.co.id', 'shopee.com.my', 'lazada.com.my',
    'lazada.co.th', 'lazada.vn', 'shopee.vn', 'shopee.ph', 'lazada.com.ph', 'shopee.sg', 'lazada.sg', 'mercadolibre.com',
    'mercadolibre.com.mx', 'mercadolibre.com.ar', 'mercadolivre.com.br', 'olx.com', 'olx.in', 'dubizzle.com', 'noon.com', 'jumia.com',
    'konga.com', 'takealot.com', 'gumtree.co.za', 'bizrate.com', 'shopify.com', 'wix.com', 'wordpress.com', 'blogspot.com',
    'weebly.com', 'godaddysites.com', 'business.site', 'sites.google.com', 'uotek.com', 'lyvi.ru', 'cid.', 'sagatele.com',
    'xinhongrui.com', 'smartbyte.com', 'onvcom.com', 'utepo.com', 'utepo.com.cn', 'hohunet.com', 'hruitech.com',
    'taiwantrade.com', 'tradeford.com', 'ec21.com', 'ecplaza.net', 'go4worldbusiness.com', 'b2brazil.com', 'yell.com', 'cylex.com',
    'hotfrog.com', 'zoominfo.com', 'dnb.com', 'crunchbase.com', 'glassdoor.com', 'manta.com', 'bbb.org', 'opencorporates.com', '2gis.ru',
    'zoon.ru', 'yell.ru', 'rusprofile.ru', 'list-org.com', 'thomasnet.com', 'globalspec.com', 'directindustry.com', '1688.com',
    'dhgate.com', 'walmart.com', 'bestbuy.com', 'newegg.com', 'target.com', 'homedepot.com', 'lowes.com', 'kompass.com', 'yelp.com',
    'trustpilot.com', 'mouser.com', 'digikey.com', 'rs-online.com', 'farnell.com', 'bol.com', 'allegro.pl', 'ceneo.pl', 'heureka.cz',
    'idealo.de', 'geizhals.de', 'tiu.ru', 'prom.ua', 'satu.kz', 'deal.by', 'flagma.com', 'all.biz', 'pulscen.ru', 'blizko.ru',
    'market.yandex.ru', 'hepsiburada.com', 'trendyol.com', 'n11.com', 'sahibinden.com', 'gittigidiyor.com', 'cimri.com',
    'akakce.com', 'souq.com', 'desertcart.com', 'ubuy.com', 'daraz.pk', 'daraz.com.bd', 'flipkart.com', 'snapdeal.com', 'moglix.com',
    'industrybuying.com', 'bikroy.com', 'jiji.ng', 'jiji.co.ke', 'pricecheck.co.za', 'bidorbuy.co.za', 'loot.co.za', 'evetech.co.za',
    'wootware.co.za', 'coolblue.nl', 'fnac.com', 'cdiscount.com', 'ldlc.com', 'materiel.net', 'pccomponentes.com', 'mediamarkt.es',
    'mediamarkt.de', 'saturn.de', 'conrad.de', 'conrad.com', 'reichelt.de', 'alternate.de', 'cyberport.de', 'notebooksbilling.de',
    'otto.de', 'kabum.com.br', 'magazineluiza.com.br', 'americanas.com.br', 'submarino.com.br', 'shopee.com.br', 'linio.com',
    'falabella.com', 'ripley.com', 'exito.com', 'coppel.com', 'liverpool.com.mx', 'cyberpuerta.mx', 'gearbest.com', 'temu.com',
    'shein.com', 'wish.com', 'joom.com', 'rakuten.co.jp', 'kakaku.com', 'coupang.com', 'gmarket.co.kr', '11st.co.kr', 'auction.co.kr',
    'pchome.com.tw', 'momoshop.com.tw', 'shopee.tw', 'ruten.com.tw', 'jd.com', 'tmall.com', 'taobao.com', 'hktvmall.com', 'price.com.hk',
    'qoo10.sg', 'carousell.sg', 'carousell.com', 'mudah.my', 'priceprice.com', 'tokopedia.com', 'bukalapak.com', 'blibli.com',
    'jd.id', 'tiki.vn', 'sendo.vn', 'thegioididong.com', 'fptshop.com.vn', 'dienmayxanh.com', 'chotot.com', 'olx.ua', 'olx.pl',
    'olx.ro', 'olx.bg', 'olx.kz', 'olx.uz', 'bazos.cz', 'bazos.sk', 'sbazar.cz', 'aukro.cz', 'vatera.hu', 'jofogas.hu', 'emag.ro',
    'emag.bg', 'emag.hu', 'okazii.ro', 'kupujemprodajem.com', 'njuskala.hr', 'bolha.com', 'avtonet.si', 'ss.com', 'ss.lv', 'skelbiu.lt',
    'okidoki.ee', 'osta.ee', 'blocket.se', 'finn.no', 'dba.dk', 'tori.fi', 'marktplaats.nl', '2dehands.be', 'ricardo.ch', 'tutti.ch',
    'willhaben.at', 'kleinanzeigen.de', 'ebay-kleinanzeigen.de', 'gumtree.com', 'gumtree.com.au', 'trademe.co.nz', 'kijiji.ca',
    'craigslist.org', 'offerup.com', 'mercari.com', 'etsy.com', 'reverb.com', 'alibaba.co.jp', 'sourcingmap.com', 'tradewheel.com',
    'exporthub.com', 'eworldtrade.com', 'tradeindia.com', 'yellowpages.ae', 'yellowpages-uae.com', 'yello.ae', 'uaecontact.com',
    'atninfo.com', 'daleeel.com', 'saudiyp.com', 'yellowpages.com.sa', 'yellowpages.com.eg', 'egypt-business.com', 'businesslist.ph',
    'businesslist.pk', 'businesslist.my', 'yellowpages.my', 'yellowpages.co.th', 'thaiyellowpages.com', 'yellowpages.vn',
    'trangvang.vn', 'yellowpages.co.id', 'indonetwork.co.id', 'indotrading.com', 'yellowpages.com.sg', 'sgpbusiness.com',
    'yellowpages.com.hk', 'hkex.com.hk', 'yellowpages.com.tw', 'yellowpages.co.kr', 'yellowpages.jp', 'yellowpages.com.au',
    'truelocal.com.au', 'yellow.co.nz', 'yellowpages.ca', 'canada411.ca', 'paginasamarillas.es', 'paginegialle.it', 'pagesjaunes.fr',
    'gelbeseiten.de', 'goudengids.nl', 'pagesdor.be', 'local.ch', 'herold.at', 'pkt.pl', 'panoramafirm.pl', 'firmy.cz', 'zlatestranky.cz',
    'zlatestranky.sk', 'aranyoldalak.hu', 'paginiaurii.ro', 'zlatnistranici.bg', 'yellowpages.ua', 'ua-region.com.ua', 'youcontrol.com.ua',
    'yp.ru', 'spravker.ru', 'orgpage.ru', 'rusfirm.ru', 'b2b-center.ru', 'rosfirm.ru', 'yellowpages.kz', 'yellowpages.uz',
    'yellowpages.ge', 'yellowpages.am', 'yellowpages.az', 'eniro.se', 'hitta.se', 'gulesider.no', '1881.no', 'krak.dk', 'degulesider.dk',
    'fonecta.fi', 'ja.is', 'goldenpages.ie', 'yell.ie', 'yellowpages.co.za', 'brabys.com', 'yellowpages.co.ke', 'yellowpages.co.tz',
    'yellowpages.co.ug', 'yellowpages.com.ng', 'businesslist.com.ng', 'yellowpages.gh', 'paginasamarillas.com', 'paginasamarillas.com.mx',
    'seccionamarilla.com.mx', 'paginasamarillas.com.ar', 'paginasamarillas.cl', 'paginasamarillas.com.pe', 'paginasamarillas.com.co',
    'paginasamarillas.com.ec', 'paginasamarillas.com.bo', 'paginasamarillas.com.py', 'paginasamarillas.com.uy', 'paginasamarillas.com.ve',
    'paginasamarillas.com.gt', 'paginasamarillas.com.sv', 'paginasamarillas.com.hn', 'paginasamarillas.co.cr', 'paginasamarillas.com.pa',
    'paginasamarillas.com.do', 'telelistas.net', 'guiamais.com.br', 'apontador.com.br', 'yellowpages.com.tr', 'sarirehber.com',
    'firmasec.com', 'bulurum.com', 'isbul.net', 'kariyer.net', 'd4b.com.tr', 'turkishexporter.com.tr', 'turkishexporter.net',
    'tradeatlas.com', 'exportgenius.in', 'importgenius.com', 'panjiva.com', 'volza.com', 'seair.co.in', 'zauba.com', 'tradesparq.com',
    'importkey.com', '52wmb.com', 'tendata.cn', 'wmb.tendata.cn', 'wixsite.com', 'technodocbox.com', 'docplayer.net', 'issuu.com',
    'scribd.com', 'slideshare.net', 'yumpu.com', 'manualslib.com', 'redlion.net',
}
# 体量过大 / 巨头 / 知名品牌厂商（INH 规则：Ingram、TD SYNNEX、Arrow… 一律 C；品牌厂商非客户）
GIANT_DOMAINS = {
    'equinix.com', 'fiberhome.com', 'fhn-na.com', 'zte.com.cn', 'huawei.com', 'h3c.com', 'tp-link.com', 'tenda.com.cn', 'ruijie.com.cn', 'ruijienetworks.com',
    'supermicro.com', 'bt.com', 'btplc.com', 'convergint.com', 'adtran.com', 'adva.com', 'cisco.com', 'hpe.com', 'hp.com', 'dell.com',
    'ibm.com', 'intel.com', 'siemens.com', 'abb.com', 'se.com', 'schneider-electric.com', 'honeywell.com', 'bosch.com', 'jci.com',
    'johnsoncontrols.com', 'hikvision.com', 'dahuasecurity.com', 'axis.com', 'motorolasolutions.com', 'zebra.com', 'belden.com',
    'phoenixcontact.com', 'moxa.com', 'advantech.com', 'weidmueller.com', 'rockwellautomation.com', 'emerson.com', 'eaton.com',
    'legrand.com', 'panduit.com', 'commscope.com', 'corning.com', 'nokia.com', 'ericsson.com', 'huawei.com', 'zte.com.cn',
    'juniper.net', 'arista.com', 'extremenetworks.com', 'netgear.com', 'dlink.com', 'tp-link.com', 'ui.com', 'mikrotik.com',
    'zyxel.com', 'alliedtelesis.com', 'planet.com.tw', 'ingrammicro.com', 'tdsynnex.com', 'synnex.com', 'techdata.com', 'arrow.com',
    'avnet.com', 'wesco.com', 'anixter.com', 'graybar.com', 'adiglobal.com', 'adiglobaldistribution.us', 'bechtle.com',
    'computacenter.com', 'also.com', 'exertis.com', 'eetgroup.com', 'arena.com.tr', 'index.com.tr', 'despec.com.tr', 'penta.com.tr',
    'armada.com.tr', 'westcon.com', 'comstor.com', 'scansource.com', 'jenne.com', 'bluestarinc.com', 'alltron.ch', 'ethiotelecom.et',
    'klinikum-karlsruhe.de', 'televes.com', 'technetix.com', 'vodafone.com', 'orange.com', 'telefonica.com', 'turkcell.com.tr',
    'turktelekom.com.tr', 'stc.com.sa', 'etisalat.ae', 'du.ae', 'ooredoo.qa', 'mtn.com', 'safaricom.co.ke', 'airtel.com', 'jio.com',
    'tatacommunications.com', 'reliance.com', 'ntt.com', 'kddi.com', 'softbank.jp', 'kt.com', 'sktelecom.com', 'lguplus.co.kr',
    'singtel.com', 'telkom.co.id', 'pldt.com', 'globe.com.ph', 'viettel.com.vn', 'vnpt.vn', 'fpt.com.vn', 'ais.co.th', 'true.th',
    'tm.com.my', 'telstra.com.au', 'optus.com.au', 'spark.co.nz', 'bell.ca', 'rogers.com', 'telus.com', 'att.com', 'verizon.com',
    't-mobile.com', 'comcast.com', 'charter.com', 'lumen.com', 'rostelecom.ru', 'mts.ru', 'megafon.ru', 'beeline.ru', 'kyivstar.ua',
    'siemens-energy.com', 'ge.com', 'hitachi.com', 'toshiba.com', 'panasonic.com', 'sony.com', 'samsung.com', 'lg.com', 'hanwha.com',
    'hanwhavision.com', 'genetec.com', 'milestonesys.com', 'avigilon.com', 'pelco.com', 'flir.com', 'teledyne.com', 'thalesgroup.com',
    'leonardo.com', 'baesystems.com', 'raytheon.com', 'lockheedmartin.com', 'northropgrumman.com', 'boeing.com', 'airbus.com',
    'safran-group.com', 'aselsan.com.tr', 'havelsan.com.tr', 'roketsan.com.tr', 'tusas.com', 'baykartech.com', 'elbitsystems.com',
    'iai.co.il', 'rafael.co.il', 'kongsberg.com', 'saab.com', 'rheinmetall.com', 'hensoldt.net', 'diehl.com', 'indracompany.com',
    'navantia.es', 'fincantieri.com', 'naval-group.com', 'damen.com', 'hyundai.com', 'kia.com', 'toyota.com', 'vw.com', 'bmw.com',
    'daimler.com', 'mercedes-benz.com', 'ford.com', 'gm.com', 'tesla.com', 'byd.com', 'catl.com', 'foxconn.com', 'pegatron.com',
    'wistron.com', 'quantatw.com', 'compal.com', 'inventec.com', 'acer.com', 'asus.com', 'msi.com', 'gigabyte.com', 'lenovo.com',
    'xiaomi.com', 'oppo.com', 'vivo.com', 'honor.com', 'meta.com', 'facebook.com', 'google.com', 'amazon.com', 'microsoft.com',
    'apple.com', 'oracle.com', 'sap.com', 'salesforce.com', 'adobe.com', 'vmware.com', 'nvidia.com', 'amd.com', 'qualcomm.com',
    'broadcom.com', 'marvell.com', 'realtek.com', 'mediatek.com', 'tsmc.com', 'asml.com', 'micron.com', 'skhynix.com', 'kioxia.com',
    'westerndigital.com', 'seagate.com', 'schindler.com', 'kone.com', 'otis.com', 'thyssenkrupp.com', 'carrier.com', 'trane.com',
    'daikin.com', 'mitsubishielectric.com', 'fujielectric.com', 'yokogawa.com', 'omron.com', 'keyence.com', 'fanuc.com', 'kuka.com',
    'festo.com', 'sick.com', 'ifm.com', 'pepperl-fuchs.com', 'turck.com', 'balluff.com', 'wago.com', 'beckhoff.com', 'b-r-automation.com',
    'lenze.com', 'sew-eurodrive.com', 'danfoss.com', 'grundfos.com', 'ksb.com', 'wilo.com', 'xylem.com', 'pentair.com', 'flowserve.com',
    'parker.com', 'bosch-rexroth.com', 'hydac.com', 'smc.eu', 'norgren.com', 'camozzi.com', 'metso.com', 'sandvik.com', 'atlascopco.com',
    'ingersollrand.com', 'caterpillar.com', 'komatsu.com', 'volvo.com', 'scania.com', 'man.eu', 'iveco.com', 'daf.com', 'paccar.com',
    'cummins.com', 'deere.com', 'cnh.com', 'agco.com', 'claas.com', 'liebherr.com', 'terex.com', 'manitowoc.com', 'jcb.com', 'hitachicm.com',
    'doosan.com', 'hyundai-ce.com', 'sany.com', 'xcmg.com', 'zoomlion.com', 'liugong.com', 'weichai.com', 'yuchai.com', 'sinotruk.com',
    'faw.com', 'dongfeng.com', 'saic.com', 'geely.com', 'greatwall.com', 'chery.com', 'jac.com', 'baic.com', 'gac.com', 'changan.com',
}
GIANT_NAMES = ['Supermicro', 'British Telecom', 'Convergint', 'Adtran', 'ADVA', 'Cisco', 'Hewlett', 'HPE', 'Dell', 'Siemens', 'ABB',
               'Schneider', 'Honeywell', 'Bosch', 'Johnson Controls', 'Hikvision', 'Dahua', 'Axis Communications', 'Motorola', 'Zebra',
               'Belden', 'Phoenix Contact', 'Moxa', 'Advantech', 'Rockwell', 'Emerson', 'Eaton', 'Legrand', 'Panduit', 'CommScope',
               'Corning', 'Nokia', 'Ericsson', 'Huawei', 'ZTE', 'Juniper', 'Arista', 'Extreme Networks', 'Netgear', 'D-Link', 'TP-Link',
               'Ubiquiti', 'Zyxel', 'Allied Telesis', 'Ingram', 'SYNNEX', 'Tech Data', 'Arrow Electronics', 'Avnet', 'Wesco', 'Anixter',
               'Graybar', 'ADI Global', 'Bechtle', 'Computacenter', 'Exertis', 'Westcon', 'Comstor', 'ScanSource', 'Ethio Telecom',
               'Televes', 'Technetix', 'Vodafone', 'Orange ', 'Telefonica', 'Turkcell', 'Turk Telekom', 'Etisalat', 'Ooredoo', 'Safaricom',
               'Airtel', 'Reliance', 'Singtel', 'Telkom', 'Viettel', 'VNPT', 'Telstra', 'Optus', 'Rostelecom', 'Rosatom', 'Gazprom',
               'Lukoil', 'Rosneft', 'Saudi Aramco', 'Aramco', 'SABIC', 'ADNOC', 'Emirates', 'Etihad', 'Qatar Airways', 'Saudia']

OFF_WORDS = ['OTDR', 'DWDM', '相干', 'coherent', '200G', '400G', 'QSFP', '光端机', 'AHD', 'HDMI', 'KVM', 'PABX', '电话', 'IP Paging',
             'alarm', '报警', 'audio', '音频', 'PA系统', 'UPS', 'solar', '太阳能', 'OTN', 'EPON', 'GPON', 'OLT', 'ONU', '光猫', 'CPE',
             'router', '路由器', 'WiFi', 'wifi', 'camera', '摄像头', 'CCTV', 'NVR', 'DVR', '无源', 'patch', '线缆', 'cable', '跳线',
             '光缆', '熔接', 'splicer', 'ODF', '机柜', 'rack', 'server', '服务器', '存储', 'storage']
SWITCH_WORDS = ['交换机', 'switch', 'Switch', 'SWITCH', 'FS', 'PoE', 'POE', 'poe', '管理', 'L2', 'L3', '2.5G', '10G', '10g', '48口', '24口',
                '16口', '8口', '电口', '光口', '工业', '2光', '4光', '8光', '1光', 'bt', 'BT', '上联', 'uplink', 'managed', 'Managed', '汇聚',
                '核心', '接入', '堆叠', 'Stacking', 'stacking', 'DC', '数据中心', '迷你', 'mini', '壳', 'MC', 'media converter', '光纤收发器',
                'SFP', '光模块', 'DAC', 'AOC', 'injector', 'splitter', 'PoE配件', 'extender', '延长器']
MC_SFP_WORDS = ['MC', 'media converter', '光纤收发器', 'SFP', '光模块', 'DAC', 'AOC', 'injector', 'splitter', 'PoE配件', 'extender', '延长器',
                '模块', '收发器']
OWN_BRAND_WORDS = ['自己的logo', '自己的品牌', '自己的标', '自己的牌子', '自己的型号', '自有品牌', 'OEM', 'oem', 'ODM', '贴牌', 'own brand',
                   'private label', '自己开发', '自己的牌']
BIG_WORDS = ['大公司', '上市公司', '集团', '跨国', '世界500强', '运营商', 'telecom operator', '国企', '政府', '军']
STOP_WORDS = ['不再跟进', '不跟进', '不用跟', 'Spam', 'spam', 'SPAM', '骗子', '诈骗', '垃圾', '拉黑', '删除', '别发了', '不要再发', 'unsubscribe',
              'remove me', '不相关', '没用', '无效', '倒闭', '关门', '已离职', '离职']
DEAL_NEG_RE = re.compile(r'(想|没|没有|未|不|差点|差一点|准备|打算|可能|会|要|将|还没|尚未|否认|如果|若|不会|没能|没再|不再|之前想|说要|说想|考虑)\s*(下单|成单|成交|买|购买|返单|成样品单|样品单)|(下单|成单|成交|样品单)\s*(后|后续)?\s*(over|没|未|失败|取消|黄了|没成|无果|不了了之)')
DEAL_RE = re.compile(r'成单|成交|已成|下单|买过|买了|返单|信保|已付款|付过款|order placed|purchased|ordered|repeat order|已出货|发过货|合作过|老客户|已合作|成样品单|样品单')


def has_deal(text):
    """成交判定：先剔除否定/未遂表述（想下单 / 差点成样品单 / 下单后续over），再看是否仍有成交词。"""
    if not text:
        return False
    t = DEAL_NEG_RE.sub(' ', text)
    return bool(DEAL_RE.search(t))
ENGAGE_RE = re.compile(r'问了|问价|问过|询价|要了|拿了|已有回复|有回复|回复了|replied|回了|说了|聊了|交谈|见面|来了展位|来展位|去了他们展位|视频会|开了会|电话里|打电话|要资料|要报价|让发|让报|有意向|有兴趣|interested|感兴趣|想要|需要具体|报价80|quoted|报了价|报过价')
SAMPLE_RE = re.compile(r'样品|样机|sample|Sample|测样|试用')
AI_RE = re.compile(r'^\s*(\d{1,3})\s*%\s*([ABCD])', re.S)
YEAR_RE = re.compile(r'(20[012]\d)')
NAME_STOP = {'rfq', 'sales', 'info', 'spam', '阿里巴巴询盘', '自建站', '阿里巴巴rfq', '阿里巴巴', '珊姐转', '询盘', '谷歌', 'facebook', 'fb',
             'linkedin', '领英', 'whatsapp', 'wa', 'alibaba', 'rfq ', 'o', 'oem', 'odm', 'trade', 'company', 'test', 'n/a', 'na', '-', '—'}
NEG_REPLY = ['暂时没需求', '暂无需求', '没需求', '不需要', '已经有了', '有供应商', '有需求会说', '有需要会', 'no need', 'not interested',
             'not now', 'no thanks', 'no thank', 'unsubscribe', 'remove', 'stop', '别发', '不要发', '贵', 'expensive', 'too high']
READ_REPLY = ['read', '已读', 'seen', 'delivered', '已送达', '双勾', '蓝勾']
SUBSTANTIVE_HINT = ['price', 'Price', '价格', '报价', 'quote', 'quotation', 'interested', 'interest', '有兴趣', '有用', 'useful', 'sample',
                    '样', 'datasheet', 'DS', 'ds', 'spec', 'catalog', 'brochure', 'info', 'INFO', 'send', 'please', '问', 'ask', 'what',
                    'how', 'MOQ', 'moq', 'lead time', 'RMB', 'USD', '$', 'yes', 'ok', 'OK', 'noted', 'will check', 'let me check', 'check',
                    'thanks', 'thank', 'hi', 'Hi', 'hello', 'Hello', 'call', 'whatsapp', 'WhatsApp', 'wechat', '微信', '电话', 'meeting',
                    'test', 'PI', 'order', '订单', '下单', 'payment', '付款', 'ship', 'deliver', '要', '需要', '想', '可以', 'looking', 'need',
                    'model', '型号', 'pcs', 'units', 'qty', 'quantity', '数量']
GENERIC_LOCAL = {'info', 'sales', 'contact', 'office', 'mail', 'admin', 'support', 'hello', 'enquiries', 'enquiry', 'inquiry', 'export',
                 'import', 'purchase', 'purchasing', 'procurement', 'marketing', 'service', 'cs', 'hi', 'team', 'order', 'orders', 'ventas',
                 'vendas', 'satis', 'bilgi', 'kontakt', 'vertrieb', 'commerciale', 'comercial', 'biuro', 'sprzedaz', 'sale', 'sale1', 'sale2',
                 'sales1', 'sales2', 'info1', 'info2', 'general', 'business', 'trade', 'trading', 'buyer', 'buy', 'kinhdoanh', 'baogia'}


# ----------------------------------------------------------------- 文件语义 → 标签
def file_tags(path, sheet):
    p = path.replace('\\', '/')
    tags = []
    base = os.path.basename(p)
    if base.startswith('S 09.08'):
        tags.append('S重点')
    elif base.startswith('A Replied'):
        tags.append('A已回复')
    elif base.startswith('E Replied'):
        tags.append('E已回复')
    elif base.startswith('Whatsapp_S'):
        tags.append('WA跟进')
    elif base.startswith('Wa only'):
        tags.append('WA仅电话')
    elif base.startswith('不行及不太相关'):
        tags.append('用户判定不行')
    elif base.startswith('客户再筛选'):
        tags.append('在用同行产品')
    elif base.startswith('询盘统计表'):
        tags.append('询盘流水')
    elif base.startswith('DC Switches'):
        tags.append('DC线索')
    elif base.startswith('DWDM CENTEC'):
        tags.append('DWDM线索')
    elif base == '台湾.docx':
        tags.append('群发邮箱清单(台湾)')
    elif '/A/同行/' in p:
        tags.append('同行经销商(' + base.rsplit('.', 1)[0] + ')')
    elif '/A/DONE/' in p:
        tags.append('A优质名单(' + re.sub(r'\s*[\d.]+$', '', base.rsplit('.', 1)[0]).strip() + ')')
    elif '/A/' in p and 'ISAF' in base:
        tags.append('ISAF2025展会')
    elif '/A/Taiwan' in p:
        tags.append('A台湾名单')
    elif '/AI客户评估/' in p:
        cc = base.replace('AI客户评估_', '').rsplit('.', 1)[0]
        cc = re.sub(r'\s*[\d.]+$', '', cc).strip()
        tags.append('AI评估(' + (cc or '模板') + ')' + ('·DONE' if '/DONE/' in p else ''))
    elif re.search(r'/E/2026\.\d\d\.\d\d/', p):
        tags.append('E冷名单(' + base.rsplit('.', 1)[0] + ')')
    elif '/E/群发/' in p:
        if base == 'List.docx':
            tags.append('群发邮箱清单(' + os.path.basename(os.path.dirname(p)) + ')')
        else:
            sub = os.path.basename(os.path.dirname(p))
            nm = re.sub(r'\s*[\d. ]+$', '', base.rsplit('.', 1)[0]).strip()
            if sub != '群发':
                nm = re.sub(r'\s*[\d. ]+$', '', sub).strip() + '/' + nm
            tags.append('群发(' + nm + ')')
    else:
        tags.append('其他(' + base + ')')
    if sheet and sheet not in ('总表', 'Sheet1', '(docx)'):
        tags.append('表:' + sheet)
    return tags


def file_country_fallback(path, sheet):
    base = os.path.basename(path).rsplit('.', 1)[0]
    base2 = re.sub(r'\s*[\d. ]+$', '', base).strip()
    for k in (base, base2, base2.replace('AI客户评估_', ''), base.replace('AI客户评估_', '')):
        if k in FILE_COUNTRY and FILE_COUNTRY[k]:
            return FILE_COUNTRY[k]
    if re.search(r'/E/2026\.\d\d\.\d\d/', path.replace('\\', '/')):
        return base
    if sheet and sheet not in ('总表', 'Sheet1'):
        return sheet
    return ''


# ----------------------------------------------------------------- 字段解析
def clean_url(u):
    u = u.strip().rstrip('.,;，；)）')
    return u


def parse_row(r):
    fields = ['company', 'person', 'contact', 'mobile', 'website', 'remark', 'interest', 'from', 'extra', 'position', 'category']
    text_all = '\n'.join(r.get(f, '') or '' for f in fields)
    emails = []
    for e in EMAIL_RE.findall(text_all):
        e = e.lower().strip('.')
        if e not in emails:
            emails.append(e)
    urls = []
    utxt = EMAIL_RE.sub(' ', '\n'.join(r.get(f, '') or '' for f in ['company', 'website', 'remark', 'contact', 'extra']))
    utxt = re.sub(r'(^|\s)@([a-z0-9\-]+\.)', r'\1www.\2', utxt, flags=re.I)
    for m in URL_RE.finditer(utxt):
        u = clean_url(m.group(0))
        if '@' in u:
            continue
        if u not in urls:
            urls.append(u)
    domains, platform_links = [], []
    for u in urls:
        d = registrable_domain(u)
        if not d or '.' not in d:
            continue
        if d in PLATFORM_DOMAINS or any(d.endswith('.' + pd) for pd in PLATFORM_DOMAINS) or d in FREEMAIL:
            platform_links.append(u)
        elif d not in domains:
            domains.append(d)
    email_domains = []
    for e in emails:
        d = registrable_domain(e.split('@', 1)[1])
        if d in FREEMAIL:
            continue
        if d in PLATFORM_DOMAINS:
            continue
        if d not in email_domains:
            email_domains.append(d)
    phones = []
    ptxt = '\n'.join(r.get(f, '') or '' for f in ['contact', 'mobile', 'remark', 'person', 'extra'])
    ptxt = URL_RE.sub(' ', EMAIL_RE.sub(' ', ptxt))
    for m in PHONE_RE.finditer(ptxt):
        digits = re.sub(r'\D', '', m.group(0))
        if 8 <= len(digits) <= 16 and digits not in phones:
            # 排除日期串（如 20200306）、端口速率串（10/100/1000）、纯重复数字
            if re.fullmatch(r'20[012]\d[01]?\d[0-3]?\d', digits) or re.fullmatch(r'(?:10|100|1000|2|5|25|40)+', digits) or len(set(digits)) <= 2:
                continue
            phones.append(digits)
    # 公司名
    name_lines = []
    for line in (r.get('company') or '').replace('\n@', '\nwww.').split('\n'):
        if line.strip().startswith('@'):
            line = 'www.' + line.strip()[1:]
        if re.match(r'^\s*(https?://|www\.|[a-z0-9\-]+\.[a-z]{2,}(/|$))', line.strip(), re.I) and ' ' not in line.strip():
            continue  # 整行是网址：不当公司名
        line2 = URL_RE.sub(' ', line)
        line2 = EMAIL_RE.sub(' ', line2)
        line2 = re.sub(r'\s+', ' ', line2).strip(' -|,;:：，；')
        if len(line2) >= 2 and line2.lower() not in NAME_STOP:
            name_lines.append(line2)
    name = name_lines[0] if name_lines else ''
    # 公司名里常夹注释（成立年份 / 备注）：只有中文且含“成立/年”的行不当名字
    while name and re.search(r'[\u4e00-\u9fff]', name) and not re.search(r'[A-Za-z\u0400-\u04ff]', name):
        # 纯中文：多半是备注（如 "阿里巴巴询盘" / "看后边邮箱 新公司"），除非像正式公司名
        if not re.search(r'有限公司|股份|集团|公司$', name) or re.search(r'看|邮箱|备注|之前|后边|没有|不', name):
            name_lines.pop(0)
            name = name_lines[0] if name_lines else ''
        else:
            break
    flags = {
        'bounce': '发不过去' in text_all or 'bounce' in text_all.lower() or '退信' in text_all,
        'wa_added': '已加' in text_all,
        'wa_failed': '加不上' in text_all or '加不了' in text_all,
        'stop': any(w in text_all for w in STOP_WORDS),
        'deal': has_deal(text_all),
        'sample': bool(SAMPLE_RE.search(text_all)),
        'big': any(w in text_all for w in BIG_WORDS),
        'giant': any(d in GIANT_DOMAINS for d in domains + email_domains) or any(g.lower() in (name or '').lower() for g in GIANT_NAMES if len(g) > 3),
        'own_brand': any(w in text_all for w in OWN_BRAND_WORDS),
        'engaged_note': bool(ENGAGE_RE.search(text_all)),
    }
    it = (r.get('interest') or '') + '\n' + (r.get('remark') or '')
    fit = {
        'switch': any(w in it for w in SWITCH_WORDS if w not in MC_SFP_WORDS),
        'mc_sfp': any(w in it for w in MC_SFP_WORDS),
        'off': any(w in it for w in OFF_WORDS),
        'vc': bool(re.search(r'\bVC\b|光端机|AHD|video converter|视频', it)),
    }
    ai = None
    for key, src in (('claude', r.get('claude_eval') or ''), ('ai', r.get('ai_eval') or '')):
        m = AI_RE.match(src)
        if m:
            ai = ai or {}
            ai[key] = {'pct': int(m.group(1)), 'grade': m.group(2), 'text': src.strip()}
        elif src.strip():
            ai = ai or {}
            ai[key] = {'pct': None, 'grade': None, 'text': src.strip()}
    years = [int(y) for y in YEAR_RE.findall(text_all)]
    return dict(emails=emails, urls=urls, domains=domains, email_domains=email_domains, platform_links=platform_links, phones=phones,
                name=name, name_lines=name_lines, flags=flags, fit=fit, ai=ai, years=years)


# ----------------------------------------------------------------- 跟进记录
def _candidates(t):
    """返回 [(y|None, m, d)] 候选；3/4 位短写（125 = 1/25 或 12/5）给出全部合法解释。"""
    m = re.fullmatch(r'(20\d\d)\.(\d{1,2})\.(\d{1,2})', t)
    if m:
        return [(int(m.group(1)), int(m.group(2)), int(m.group(3)))]
    m = re.fullmatch(r'(20\d\d)(\d\d)(\d\d)', t)
    if m:
        return [(int(m.group(1)), int(m.group(2)), int(m.group(3)))]
    m = re.fullmatch(r'(20\d\d)\.(\d{1,2})', t)
    if m:
        return [(int(m.group(1)), int(m.group(2)), 1)]
    m = re.fullmatch(r'(\d{1,2})\.(\d{1,2})', t)
    if m:
        return [(None, int(m.group(1)), int(m.group(2)))]
    m = re.fullmatch(r'(\d{3,4})', t)
    if m:
        sdig = m.group(1)
        out = []
        for k in (1, 2):
            if k < len(sdig):
                mo, d = int(sdig[:k]), int(sdig[k:])
                if 1 <= mo <= 12 and 1 <= d <= 31:
                    out.append((None, mo, d))
        return out
    return []


def parse_follow_date(tok, ctx):
    """跟进时间：2024.5.2 / 916 / 1024 / 1.6 / 2025.2.20 / 325 / 125 … 年份沿用上一条，月份回退则 +1 年；
    短写有歧义时（125 = 1/25 或 12/5）取与上一条日期最接近且不早于上一条的解释。"""
    t = (tok or '').strip().replace('/', '.').replace('-', '.').replace('月', '.').replace('日', '').replace(' ', '')
    cands = [(y, mo, d) for (y, mo, d) in _candidates(t) if 1 <= mo <= 12 and 1 <= d <= 31]
    if not cands:
        return None
    prev = ctx.get('prev')  # (y, m, d) 上一条
    best = None
    for (y, mo, d) in cands:
        if y is None:
            if prev is None:
                continue
            y2 = prev[0] + (1 if (mo, d) < (prev[1], prev[2]) else 0)
        else:
            y2 = y
        try:
            cur = dt.date(y2, mo, min(d, 28) if d > 28 else d)
            prevd = dt.date(prev[0], prev[1], min(prev[2], 28)) if prev else None
        except Exception:
            continue
        gap = (cur - prevd).days if prevd else 0
        key = (gap < 0, abs(gap))
        if best is None or key < best[0]:
            best = (key, (y2, mo, d))
    if best is None:
        return None
    y2, mo, d = best[1]
    ctx['prev'] = (y2, mo, d)
    ctx['y'], ctx['m'] = y2, mo
    return f'{y2:04d}-{mo:02d}-{d:02d}'


def classify_reply(text):
    t = (text or '').strip()
    if not t:
        return ''
    tl = t.lower()
    if any(w in tl for w in READ_REPLY) and len(t) <= 12:
        return 'read'
    if any(w in tl for w in [x.lower() for x in NEG_REPLY]):
        return 'negative'
    if any(w in t for w in SUBSTANTIVE_HINT) or len(t) >= 6:
        return 'substantive'
    return 'other'


# ----------------------------------------------------------------- 并查集
class DSU:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


def main():
    rows = [json.loads(l) for l in open(os.path.join(DATA, 'rows_raw.jsonl'), encoding='utf-8')]
    fus = [json.loads(l) for l in open(os.path.join(DATA, 'followups.jsonl'), encoding='utf-8')]
    # 跟进记录按 (file, no) 归组并解析日期
    fu_by = defaultdict(list)
    for f in fus:
        fu_by[(f['file'], str(f['no']).strip())].append(f)
    for key, lst in fu_by.items():
        ctx = {}
        for f in lst:
            f['date_iso'] = parse_follow_date(f.get('date', ''), ctx)
            f['reply_kind'] = classify_reply(f.get('reply', ''))

    # docx 邮箱清单 → 行（只作补充：邮箱不在任何 xlsx 行里时才独立成行）
    docx_rows = [r for r in rows if 'docx_paragraphs' in r]
    rows = [r for r in rows if 'docx_paragraphs' not in r]
    all_emails_xlsx = set()
    parsed = []
    for i, r in enumerate(rows):
        p = parse_row(r)
        r['_p'] = p
        r['_id'] = i
        r['_tags'] = file_tags(r['file'], r.get('sheet', ''))
        fb = file_country_fallback(r['file'], r.get('sheet', ''))
        craw = r.get('country') or ''
        if not craw and r.get('category') and norm_country(r['category'])[1] != '??':
            craw = r['category']
        r['_country'] = norm_country(craw, fb)
        no = str(r.get('no') or '').strip()
        if no.endswith('.0'):
            no = no[:-2]
        r['_no'] = no
        r['_fu'] = fu_by.get((r['file'], no), []) if no else []
        all_emails_xlsx.update(p['emails'])
        parsed.append(r)
    docx_extra = []
    docx_total = 0
    for dr in docx_rows:
        grp = ''
        for para in dr['docx_paragraphs']:
            para = para.strip()
            if re.fullmatch(r'\d+(?:~\d+)?', para):
                grp = para
                continue
            for e in EMAIL_RE.findall(para):
                docx_total += 1
                e = e.lower()
                if e in all_emails_xlsx:
                    continue
                nr = OrderedDict(file=dr['file'], sheet='(docx)', row=0, no=grp, company='', country='', category='', person='',
                                 position='', **{'from': '群发邮箱清单'}, interest='', contact=e, mobile='', website='', remark='仅出现在 docx 群发清单，对应 xlsx 中无此邮箱', ai_eval='', claude_eval='', extra='')
                p = parse_row(nr)
                nr['_p'] = p
                nr['_id'] = len(parsed) + len(docx_extra)
                nr['_tags'] = file_tags(dr['file'], '(docx)')
                nr['_country'] = norm_country('', file_country_fallback(dr['file'], ''))
                nr['_no'] = grp
                nr['_fu'] = []
                docx_extra.append(nr)
                all_emails_xlsx.add(e)
    parsed += docx_extra

    # 归并键
    dsu = DSU()
    key_owner = {}
    merge_edges = defaultdict(list)

    def link(rid, key):
        if key in key_owner:
            a, b = key_owner[key], rid
            if dsu.find(a) != dsu.find(b):
                merge_edges[(min(a, b), max(a, b))].append(key)
            dsu.union(a, b)
        else:
            key_owner[key] = rid
        dsu.find(rid)

    for r in parsed:
        p = r['_p']
        rid = r['_id']
        dsu.find(rid)
        for d in p['domains'] + p['email_domains']:
            link(rid, 'd:' + d)
        for e in p['emails']:
            link(rid, 'e:' + e)
        for ph in p['phones']:
            if len(ph) >= 9:
                link(rid, 'p:' + ph[-9:])
        nn = norm_name(p['name']) if p['name'] else ''
        if nn and len(nn) >= 4 and nn not in NAME_STOP and r['_country'][1] != '??':
            link(rid, 'n:' + r['_country'][1] + '|' + nn)
        elif nn and len(nn) >= 6 and nn not in NAME_STOP:
            link(rid, 'n:??|' + nn)

    groups = defaultdict(list)
    for r in parsed:
        groups[dsu.find(r['_id'])].append(r)
    # 每个实体：哪些键把 ≥2 行连在一起（审计用）
    key_members = defaultdict(set)
    for r in parsed:
        p = r['_p']
        for d in p['domains'] + p['email_domains']:
            key_members['d:' + d].add(r['_id'])
        for e in p['emails']:
            key_members['e:' + e].add(r['_id'])
        for ph in p['phones']:
            if len(ph) >= 9:
                key_members['p:' + ph[-9:]].add(r['_id'])
        nn = norm_name(p['name']) if p['name'] else ''
        if nn and len(nn) >= 4 and nn not in NAME_STOP and r['_country'][1] != '??':
            key_members['n:' + r['_country'][1] + '|' + nn].add(r['_id'])
        elif nn and len(nn) >= 6 and nn not in NAME_STOP:
            key_members['n:??|' + nn].add(r['_id'])
    shared_keys = {k: v for k, v in key_members.items() if len(v) >= 2}

    # 编号登记簿
    reg_path = os.path.join(DATA, '编号登记.json')
    registry = json.load(open(reg_path, encoding='utf-8')) if os.path.exists(reg_path) else {'next': {'A': 1, 'B': 1, 'C': 1}, 'keys': {}}
    manual = {}
    mpath = os.path.join(DATA, '人工定级.csv')
    if os.path.exists(mpath):
        for m in csv.DictReader(open(mpath, encoding='utf-8-sig')):
            manual[m['键或编号'].strip()] = m
    research = {}
    for rp in glob.glob(os.path.join(RESEARCH_DIR, '*.json')):
        try:
            j = json.load(open(rp, encoding='utf-8'))
            research[j['code']] = j
        except Exception:
            pass

    entities = []
    for gid, members in groups.items():
        members.sort(key=lambda r: (r['file'], r.get('sheet', ''), r.get('row', 0)))
        ent = aggregate(members)
        ids = {m['_id'] for m in members}
        ent['merge_keys'] = sorted(k for k, v in shared_keys.items() if v & ids)
        entities.append(ent)

    # 分级
    for ent in entities:
        grade, score, reasons, c_sub, status = classify(ent)
        ent['grade_auto'] = grade
        ent['score'] = score
        ent['reasons'] = reasons
        ent['c_sub'] = c_sub
        ent['status'] = status

    # 编号：先按稳定键查登记簿；新实体按 (自动等级, 分数降序, 名称) 发号
    def stable_keys(ent):
        ks = []
        for d in ent['domains']:
            ks.append('d:' + d)
        for e in ent['emails']:
            ks.append('e:' + e)
        for ph in ent['phones']:
            ks.append('p:' + ph[-9:])
        if ent['name'] and ent['name'] != '（未具名）' and len(norm_name(ent['name'])) >= 3:
            ks.append('n:' + ent['iso'] + '|' + norm_name(ent['name']))
        return ks

    entities.sort(key=lambda e: ({'A': 0, 'B': 1, 'C': 2}[e['grade_auto']], -e['score'], e['name'] or 'zzz'))
    used_codes = set()
    for ent in entities:
        ks = stable_keys(ent)
        found = sorted({registry['keys'][k] for k in ks if k in registry['keys']})
        found_free = [c for c in found if c not in used_codes]
        if found_free:
            code = found_free[0]
            others = [c for c in found if c != code]
            if others:
                ent['code_aliases'] = others
        else:
            g = ent['grade_auto']
            code = f'S{g}-{registry["next"][g]:03d}'
            registry['next'][g] += 1
            if found:
                # 原实体被拆分（键归并规则修正）：本实体另发新号，并记录来源编号
                ent['split_from'] = found
                for k in ks:
                    if registry['keys'].get(k) in found:
                        registry['keys'][k] = code
        used_codes.add(code)
        for k in ks:
            registry['keys'].setdefault(k, code)
        ent['code'] = code
        ent['grade'] = ent['grade_auto']
        # 人工定级 / 调研覆盖
        ov = None
        for k in [code] + ks:
            if k in manual:
                ov = manual[k]
                break
        if ov and ov.get('等级') in ('A', 'B', 'C'):
            ent['grade'] = ov['等级']
            ent['manual'] = ov
        rs = research.get(code)
        if rs:
            ent['research'] = rs
            if rs.get('grade_override') in ('A', 'B', 'C') and not ov:
                ent['grade'] = rs['grade_override']
        # 覆盖后的 C 级细分：从理由里取 c_sub=…，否则统一标「调研/人工定级 C」；覆盖为非 C 则清空细分
        if ent['grade'] == 'C' and ent['grade_auto'] != 'C' and not ent.get('c_sub'):
            reason = (ov or {}).get('理由', '') if ov else (rs or {}).get('override_reason', '')
            m = re.search(r'c_sub\s*=\s*([^。；;\s]+)', reason or '')
            ent['c_sub'] = m.group(1) if m else ('人工定级 C' if ov else '调研后定级 C')
        elif ent['grade'] != 'C':
            ent['c_sub'] = ''
    with open(reg_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, ensure_ascii=False, indent=0)

    # 输出
    entities.sort(key=lambda e: e['code'])
    with open(os.path.join(DATA, 'entities.json'), 'w', encoding='utf-8') as f:
        json.dump(entities, f, ensure_ascii=False, indent=0)
    write_master(entities)
    write_merge_log(entities, merge_edges)
    stats = {
        'rows_xlsx': len(rows), 'rows_docx_extra': len(docx_extra), 'docx_emails_total': docx_total, 'followups': len(fus),
        'followups_attached': sum(len(e['followups']) for e in entities),
        'entities': len(entities), 'grades': dict(Counter(e['grade'] for e in entities)),
        'grades_auto': dict(Counter(e['grade_auto'] for e in entities)),
        'multi_source': sum(1 for e in entities if len(e['sources']) > 1),
        'c_sub': dict(Counter(e['c_sub'] for e in entities if e['grade'] == 'C')),
        'status': dict(Counter(e['status'] for e in entities)),
    }
    with open(os.path.join(DATA, 'build_stats.json'), 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False, indent=1))


# ----------------------------------------------------------------- 聚合
def aggregate(members):
    ent = OrderedDict()
    names, domains, emails, phones, urls, platform_links, persons, froms, interests, remarks, tags, positions = ([] for _ in range(12))
    countries = Counter()
    flags = Counter()
    fit = Counter()
    ai_evals = []
    years = []
    sources = []
    cats = []
    for r in members:
        p = r['_p']
        for n in p['name_lines']:
            if n not in names:
                names.append(n)
        for d in p['domains'] + p['email_domains']:
            if d not in domains:
                domains.append(d)
        for e in p['emails']:
            if e not in emails:
                emails.append(e)
        for ph in p['phones']:
            if ph not in phones:
                phones.append(ph)
        for u in p['urls']:
            if u not in urls:
                urls.append(u)
        for u in p['platform_links']:
            if u not in platform_links:
                platform_links.append(u)
        if r.get('person'):
            per = re.sub(r'\s*\n\s*', ' / ', r['person'].strip())
            if per not in persons:
                persons.append(per)
        if r.get('position') and r['position'] not in positions:
            positions.append(r['position'])
        if r.get('from') and r['from'].strip() not in froms:
            froms.append(r['from'].strip())
        if r.get('interest') and r['interest'].strip() not in interests:
            interests.append(r['interest'].strip())
        rm = ' / '.join(x for x in [r.get('remark', ''), r.get('extra', '')] if x)
        if rm and rm not in remarks:
            remarks.append(rm)
        if r.get('category'):
            cats.append(r['category'])
        for t in r['_tags']:
            if t not in tags:
                tags.append(t)
        if r['_country'][1] != '??':
            countries[r['_country']] += 1
        for k, v in p['flags'].items():
            if v:
                flags[k] += 1
        for k, v in p['fit'].items():
            if v:
                fit[k] += 1
        if p['ai']:
            ai_evals.append({'file': r['file'], **p['ai']})
        years += p['years']
        sources.append({'file': r['file'], 'sheet': r.get('sheet', ''), 'row': r.get('row', 0), 'no': r['_no'], 'tags': r['_tags'],
                        'company': r.get('company', ''), 'country': r.get('country', ''), 'person': r.get('person', ''),
                        'from': r.get('from', ''), 'interest': r.get('interest', ''), 'contact': r.get('contact', ''),
                        'mobile': r.get('mobile', ''), 'website': r.get('website', ''), 'remark': r.get('remark', ''),
                        'extra': r.get('extra', ''), 'category': r.get('category', ''), 'position': r.get('position', ''),
                        'ai_eval': r.get('ai_eval', ''), 'claude_eval': r.get('claude_eval', ''), 'followups': len(r['_fu'])})
    # 跟进记录合并（同文件同 No. 只算一次）
    seen = set()
    followups = []
    for r in members:
        k = (r['file'], r['_no'])
        if k in seen:
            continue
        seen.add(k)
        for f in r['_fu']:
            followups.append({'file': r['file'], 'no': r['_no'], 'date': f.get('date', ''), 'date_iso': f.get('date_iso'),
                              'content': f.get('content', ''), 'reply': f.get('reply', ''), 'platform': f.get('platform', ''),
                              'note': f.get('note', ''), 'reply_kind': f.get('reply_kind', '')})
    followups.sort(key=lambda f: (f['date_iso'] or '9999', f['file']))
    # 名称：优先带拉丁字母的公司名；否则域名；否则联系人；否则占位
    name = ''
    for n in names:
        if re.search(r'[A-Za-z\u0400-\u04ff]', n) and not re.fullmatch(r'[\d\s.\-+()]+', n):
            name = n
            break
    if not name and names:
        name = names[0]
    name_src = 'company'
    if not name and domains:
        name, name_src = domains[0], 'domain'
    if not name and emails:
        name, name_src = emails[0], 'email'
    if not name and persons:
        name, name_src = persons[0].split(' / ')[0], 'person'
    if not name:
        name, name_src = '（未具名）', 'none'
    country = countries.most_common(1)[0][0] if countries else ('未填', '??', '未知')
    other_countries = [c[0] for c, n in countries.items() if c != country]
    corp_emails = [e for e in emails if registrable_domain(e.split('@')[1]) not in FREEMAIL]
    ent.update(dict(name=name, name_src=name_src, names=names, country=country[0], iso=country[1], region=country[2],
                    other_countries=other_countries, domains=domains, urls=urls, platform_links=platform_links, emails=emails,
                    corp_emails=corp_emails, phones=phones, persons=persons, positions=positions, froms=froms, interests=interests,
                    remarks=remarks, categories=cats, tags=tags, flags=dict(flags), fit=dict(fit), ai_evals=ai_evals,
                    years=sorted(set(years)), sources=sources, followups=followups))
    # 跟进统计
    fu_years = sorted({f['date_iso'][:4] for f in followups if f['date_iso']})
    ent['fu_count'] = len(followups)
    ent['fu_first'] = followups[0]['date_iso'] if followups and followups[0]['date_iso'] else ''
    ent['fu_last'] = max([f['date_iso'] for f in followups if f['date_iso']] or [''])
    ent['fu_years'] = fu_years
    ent['reply_sub'] = sum(1 for f in followups if f['reply_kind'] == 'substantive')
    ent['reply_neg'] = sum(1 for f in followups if f['reply_kind'] == 'negative')
    ent['reply_read'] = sum(1 for f in followups if f['reply_kind'] == 'read')
    ent['reply_other'] = sum(1 for f in followups if f['reply_kind'] == 'other')
    plats = [f['platform'] for f in followups if f['platform']]
    ent['platforms'] = [p for p, _ in Counter(plats).most_common()]
    letters = [p for p in plats if p in ('S', 'A', 'E')]
    ent['last_tier_letter'] = letters[-1] if letters else ''
    ent['wa_in_fu'] = any('whatsapp' in p.lower() or p == '微信' for p in plats)
    ent['deal_in_fu'] = any(has_deal(f['content'] + ' ' + f['reply'] + ' ' + f['note']) for f in followups)
    txt = ' '.join(f['reply'] for f in followups)
    ent['fu_sample'] = bool(SAMPLE_RE.search(txt))
    ent['last_year'] = max([int(y) for y in fu_years] + [y for y in ent['years'] if 2015 <= y <= 2026] or [0])
    return ent


# ----------------------------------------------------------------- 分级
REGION_SCORE = {'北美': 8, '欧洲': 8, '土耳其': 8, '中东': 3, '亚太': 3, '俄语区': 0, '南亚': -6, '拉美': -4, '非洲': -6,
                '中国大陆': -40, '乌克兰': -20, '未知': -3}
APAC_DEVELOPED = {'KR', 'JP', 'SG', 'AU', 'NZ', 'TW', 'HK', 'MY', 'TH'}


def classify(ent):
    s = 0
    rs = []
    tags = ent['tags']
    fl = ent['flags']
    fit = ent['fit']

    def add(v, why):
        nonlocal s
        s += v
        rs.append(f'{"+" if v >= 0 else ""}{v} {why}')

    deal = fl.get('deal') or ent['deal_in_fu'] or any('成单' in f for f in ent['froms'])
    if deal:
        add(50, '有成单/下单/买过记录（用户备注或跟进表）')
    if ent['reply_sub'] >= 2:
        add(30, f'实质回复 {ent["reply_sub"]} 次（问价/要资料/问型号等）')
    elif ent['reply_sub'] == 1:
        add(22, '实质回复 1 次')
    if ent['reply_neg']:
        add(6, f'有互动但表示暂无需求/已有供应商 {ent["reply_neg"]} 次')
    if ent['reply_read'] and not ent['reply_sub']:
        add(4, '仅已读（read）未回复')
    if ent['fu_sample'] or fl.get('sample'):
        add(10, '谈到样品/测样')
    if fl.get('engaged_note') and not ent['reply_sub']:
        add(12, '备注记录了对方问价/要资料/见面等互动')
    tagset = {t.split('(')[0] for t in tags}
    if 'S重点' in tagset:
        add(25, '在 Simon 的 S 重点名单')
    if 'A已回复' in tagset or 'E已回复' in tagset:
        add(18, '在「已回复」名单（A/E Replied）')
    if 'WA跟进' in tagset:
        add(15, 'WhatsApp 已加并有跟进表')
    if 'WA仅电话' in tagset:
        add(6, 'WhatsApp 仅电话名单')
    if 'ISAF2025展会' in tagset:
        add(12, 'ISAF 2025 展会面对面名片')
    if '在用同行产品' in tagset:
        add(10, '用户二筛：在用 Utepo/ONV/Ewind 等同行产品（贴牌切入口）')
    if '询盘流水' in tagset:
        add(12, '主动询盘（阿里巴巴/自建站/转介）')
    if '同行经销商' in tagset:
        add(8, '在卖 DPTEK/SmartByte 同类产品的经销商（已接受深圳供应链）')
    if 'A优质名单' in tagset:
        add(6, '在 A/DONE 优质国家名单（已做过整轮推送）')
    if 'A台湾名单' in tagset:
        add(0, '台湾名单（台系品牌商，按 INH 规则最高 B）')
    if 'AI评估' in tagset:
        add(2, '在 AI 客户评估名单')
    if 'DWDM线索' in tagset:
        add(-8, 'DWDM/光传输线索：Saga 不做 DWDM（Hohunet 线为交换机）')
    if 'DC线索' in tagset:
        add(0, '数据中心交换机线索（Hohunet/CENTEC 线）')
    if 'E冷名单' in tagset:
        add(-6, 'E 冷名单（按国家群发）')
    if '群发' in tagset:
        add(-6, '群发批次名单')
    if tagset == {'群发邮箱清单'} or (len(tagset) == 1 and '群发邮箱清单' in tagset):
        add(-10, '仅出现在群发邮箱 docx 清单')
    if 'WA仅电话' in tagset and not ent['emails']:
        add(-4, '只有电话没有邮箱')
    cats = set(ent['categories'])
    if '1类' in cats:
        add(15, '用户分档 1类')
    if '3类' in cats:
        add(-10, '用户分档 3类')
    # AI / Claude 评估：Claude 优先
    ai_g = None
    for a in ent['ai_evals']:
        if a.get('claude') and a['claude'].get('grade'):
            ai_g = a['claude']['grade']
            break
    if not ai_g:
        for a in ent['ai_evals']:
            if a.get('ai') and a['ai'].get('grade'):
                ai_g = a['ai']['grade']
                break
    if ai_g == 'A':
        add(15, 'AI/Claude 评估 A')
    elif ai_g == 'B':
        add(4, 'AI/Claude 评估 B')
    elif ai_g == 'C':
        add(-15, 'AI/Claude 评估 C')
    # 负面
    if '用户判定不行' in tagset:
        add(-60, '用户已归入「不行及不太相关的」')
    if fl.get('stop'):
        add(-40, '备注含 不再跟进/Spam/骗子 等')
    if fl.get('bounce') and not fl.get('wa_added') and not ent['wa_in_fu']:
        add(-25, '邮件发不过去且无 WhatsApp 通道')
    elif fl.get('bounce'):
        add(-8, '部分邮箱发不过去（有 WhatsApp 兜底）')
    if fl.get('wa_failed'):
        add(-3, 'WhatsApp 加不上')
    if fl.get('big'):
        add(-12, '备注提示大公司/上市公司/运营商（体量不匹配）')
    # 契合
    if fl.get('own_brand'):
        add(12, '自有品牌/贴牌需求（OEM/ODM 首选客户类型）')
    if fit.get('switch'):
        add(8, '兴趣在交换机/PoE/工业/MC 等 Saga 主线')
    elif fit.get('mc_sfp'):
        add(2, '兴趣仅 MC/SFP/配件（边缘品类）')
    if (fit.get('off') or fit.get('vc')) and not fit.get('switch'):
        add(-15, '兴趣只在 Saga 不做的品类（VC/光端机/DWDM/OTDR/CCTV/云管理等）')
    # 通道
    if ent['corp_emails']:
        add(10, '有企业邮箱')
    elif ent['emails']:
        add(0, '仅免费邮箱')
    if ent['domains']:
        add(5, '有可核实的公司网站/域名')
    if not ent['emails'] and (ent['phones'] or fl.get('wa_added')):
        add(-8, '无邮箱，仅电话/WhatsApp')
    if not ent['emails'] and not ent['phones'] and not ent['domains']:
        add(-40, '无任何联系方式')
    if ent['emails'] and not ent['corp_emails'] and not ent['domains'] and not ent['names']:
        add(-15, '只有免费邮箱、无公司名无网站（个人买家特征）')
    # 区域
    reg = ent['region']
    rv = REGION_SCORE.get(reg, -3)
    if reg == '亚太' and ent['iso'] not in APAC_DEVELOPED:
        rv = 0
    add(rv, f'区域 {reg}/{ent["country"]}')
    # 时效
    ly = ent['last_year']
    if ly >= 2025:
        add(5, f'最近活动 {ly}')
    elif ly == 2024:
        add(2, '最近活动 2024')
    elif 0 < ly <= 2022:
        add(-10, f'最近活动 {ly}（陈旧）')
    if ly == 0:
        old_show = any(re.search(r'20(0\d|1[0-5])', f) for f in ent['froms'])
        if old_show:
            add(-10, '来源为 2010–2015 年展会且无后续记录')
    if ent['fu_count'] >= 8 and not (ent['reply_sub'] or ent['reply_neg'] or ent['reply_other']):
        pen = -10 if ent['fu_count'] < 15 else (-16 if ent['fu_count'] < 25 else -22)
        add(pen, f'推送 {ent["fu_count"]} 次无任何回复（聋名单）')
    if fl.get('giant'):
        add(-45, '巨头/品牌厂商/运营商/军工（INH 规则：体量不匹配或非客户）')
    if ent['last_tier_letter'] == 'S':
        add(5, '跟进表最近平台标记 S')
    elif ent['last_tier_letter'] == 'E':
        add(-3, '跟进表最近平台标记 E（已降为群发）')

    # 等级
    if s >= 60:
        g = 'A'
    elif s >= 25:
        g = 'B'
    else:
        g = 'C'
    c_sub = ''
    # 硬规则
    if '用户判定不行' in tagset and not deal and ent['reply_sub'] == 0:
        g, c_sub = 'C', '用户判定不行/不相关'
    if not ent['emails'] and not ent['phones'] and not ent['domains']:
        g, c_sub = 'C', '无联系方式'
    if reg == '中国大陆' and not deal:
        g, c_sub = 'C', '中国大陆（非出口客户）'
    if (reg == '乌克兰' or ent['iso'] == 'UA') and not deal:
        g = 'B' if ent['reply_sub'] else 'C'
        c_sub = '' if g == 'B' else '守界：乌克兰'
        if g == 'B':
            rs.append('封顶 B：乌克兰（守界：不主动投入，仅被动响应）')
    if ent['iso'] == 'TW' and g == 'A' and not deal and 'S重点' not in tagset:
        g = 'B'
        rs.append('封顶 B：台系品牌商（INH 规则：台湾厂商非终端客户，除非成交或用户 S 名单）')
    engaged = deal or ent['reply_sub'] or ent['reply_neg'] or ent['reply_other'] or 'S重点' in tagset or 'ISAF2025展会' in tagset \
        or '询盘流水' in tagset or 'A已回复' in tagset or 'E已回复' in tagset or ('WA跟进' in tagset and ent['wa_in_fu']) \
        or fl.get('engaged_note')
    if ent['reply_sub'] and g == 'C' and not fl.get('stop') and '用户判定不行' not in tagset and not fl.get('giant') and reg not in ('中国大陆',):
        g, c_sub = 'B', ''
        rs.append('托底 B：有实质回复的客户至少 B')
    if g == 'A' and not engaged:
        g = 'B'
        rs.append('封顶 B：无任何互动证据（未回复/未询盘/未见面），A 级须有互动')
    if fl.get('giant') and not deal:
        g, c_sub = 'C', '体量过大/品牌厂商/运营商'
    if (fit.get('off') or fit.get('vc')) and not fit.get('switch') and not fit.get('mc_sfp') and g == 'A' and not deal:
        g = 'B'
        rs.append('封顶 B：需求品类不在 Saga 主线')
    if fl.get('stop') and not deal:
        g = 'C'
        c_sub = c_sub or '用户备注不再跟进/Spam'
    if g == 'C' and not c_sub:
        if fl.get('bounce') and not ent['wa_in_fu'] and not fl.get('wa_added'):
            c_sub = '发不过去'
        elif (fit.get('off') or fit.get('vc')) and not fit.get('switch'):
            c_sub = '品类不符（VC/DWDM/CCTV 等）'
        elif not ent['emails']:
            c_sub = '无邮箱（仅电话）'
        elif ly and ly <= 2022:
            c_sub = '陈旧线索无互动'
        elif '群发' in tagset or 'E冷名单' in tagset or '群发邮箱清单' in tagset:
            c_sub = '群发冷名单无回应'
        elif fl.get('big'):
            c_sub = '体量过大'
        elif reg in ('南亚', '非洲', '拉美'):
            c_sub = '低价值区域冷线索'
        else:
            c_sub = '综合分低'
    # 状态
    if deal:
        status = '成交过·维护'
    elif ent['reply_sub']:
        status = '有回复·跟进中'
    elif ent['reply_neg']:
        status = '回复暂无需求'
    elif fl.get('wa_added') or ent['wa_in_fu']:
        status = 'WhatsApp 已加·未回复'
    elif ent['fu_count']:
        status = f'已推送 {ent["fu_count"]} 次·未回复'
    elif '用户判定不行' in tagset:
        status = '用户判定不行'
    elif fl.get('bounce'):
        status = '发不过去'
    else:
        status = '名单内·未触达'
    return g, s, rs, c_sub, status


# ----------------------------------------------------------------- 输出
MASTER_COLS = ['档案编号', '评级', '自动评级', '人工定级', '分数', '公司名', '国家', '区域', '网站/域名', '企业邮箱', '全部邮箱', '电话',
               '联系人', '来源(From)', '兴趣', '用户标签(所在清单)', '状态', 'C级细分', '成交', '实质回复次数', '推送次数', '首次跟进',
               '最后跟进', 'AI评估', '评级依据', '来源行数', '来源定位']


def write_master(entities):
    with open(os.path.join(DATA, '客户主表.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=MASTER_COLS, lineterminator='\r\n')
        w.writeheader()
        for e in entities:
            ai = ''
            for a in e['ai_evals']:
                parts = []
                if a.get('claude') and a['claude'].get('grade'):
                    parts.append(f"Claude {a['claude']['pct']}% {a['claude']['grade']}")
                if a.get('ai') and a['ai'].get('grade'):
                    parts.append(f"AI {a['ai']['pct']}% {a['ai']['grade']}")
                ai = '; '.join(parts)
                break
            w.writerow({
                '档案编号': e['code'], '评级': e['grade'], '自动评级': e['grade_auto'],
                '人工定级': (e.get('manual') or {}).get('等级', '') or ((e.get('research') or {}).get('grade_override', '')),
                '分数': e['score'], '公司名': e['name'], '国家': e['country'], '区域': e['region'],
                '网站/域名': ' | '.join(e['domains']), '企业邮箱': ' | '.join(e['corp_emails']), '全部邮箱': ' | '.join(e['emails']),
                '电话': ' | '.join(e['phones']), '联系人': ' | '.join(e['persons']), '来源(From)': ' | '.join(e['froms']),
                '兴趣': ' | '.join(e['interests']).replace('\n', ' '), '用户标签(所在清单)': ' | '.join(e['tags']), '状态': e['status'],
                'C级细分': e['c_sub'], '成交': '是' if (e['flags'].get('deal') or e['deal_in_fu']) else '',
                '实质回复次数': e['reply_sub'], '推送次数': e['fu_count'], '首次跟进': e['fu_first'], '最后跟进': e['fu_last'], 'AI评估': ai,
                '评级依据': '；'.join(e['reasons']), '来源行数': len(e['sources']),
                '来源定位': ' | '.join(f"{s['file'].replace('Clients/', '')}#{s['sheet']}:{s['row']}" for s in e['sources']),
            })


def write_merge_log(entities, merge_edges):
    multi = [e for e in entities if len(e['sources']) > 1]
    lines = ['# 重复客户归并记录（Saga Clients）', '',
             f'- 生成方式：`scripts/saga_clients/build.py` 自动归并；归并键 = 公司网站/企业邮箱的注册域名（d:）、完整邮箱（e:）、电话后 9 位（p:）、规范化公司名+国家（n:）；任一键相同即并为同一客户（并查集）。',
             f'- 结果：{len(entities)} 个客户实体，其中 **{len(multi)} 个由 2 行以上来源合并**；被合并的原始行总数 {sum(len(e["sources"]) for e in multi)}。',
             '- 每个客户 MD 的「来源与归并」节列出其全部原始行（文件#表:行号）；本文件按编号列出多来源客户与所用的键。',
             '- 冲突（同一客户同时出现在正向名单与「不行及不太相关的」）单独列在文末，分级时以用户最新判定与实际互动为准，不删除任何一行。', '']
    conflicts = []
    lines.append('| 编号 | 等级 | 公司 | 国家 | 来源行数 | 所在清单 | 来源定位（文件#表:行） |')
    lines.append('|---|---|---|---|---|---|---|')
    for e in multi:
        loc = '<br>'.join(f"{s['file'].replace('Clients/', '')}#{s['sheet']}:{s['row']}" for s in e['sources'])
        lines.append(f"| {e['code']} | {e['grade']} | {e['name']} | {e['country']} | {len(e['sources'])} | {'、'.join(e['tags'])} | {loc} |")
        ts = {t.split('(')[0] for t in e['tags']}
        if '用户判定不行' in ts and (ts & {'S重点', 'A已回复', 'E已回复', 'WA跟进', 'A优质名单', 'ISAF2025展会', '询盘流水', '在用同行产品'}):
            conflicts.append(e)
    lines += ['', f'## 冲突：同一客户既在正向名单又在「不行及不太相关的」（{len(conflicts)} 个）', '',
              '| 编号 | 最终等级 | 公司 | 国家 | 所在清单 | 处理 |', '|---|---|---|---|---|---|']
    for e in conflicts:
        deal = e['flags'].get('deal') or e['deal_in_fu']
        how = '有成交/实质回复 → 按互动定级，保留「不行」标签供人工复核' if (deal or e['reply_sub']) else '无实质互动 → 按用户判定归 C'
        lines.append(f"| {e['code']} | {e['grade']} | {e['name']} | {e['country']} | {'、'.join(e['tags'])} | {how} |")
    with open(os.path.join(DATA, '重复客户归并记录.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
