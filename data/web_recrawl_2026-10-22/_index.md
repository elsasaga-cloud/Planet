# 供应商外网复抓 2026-10-22（T29-U13 ③b）— 索引
抓取主体：代理（web_search + fetch_page，沙箱）；官网整站复抓由 GitHub Actions `smartbyte-crawl.yml` 执行（crawl.py v3.2，结果在 `data/site_recrawl/20261022/` 与新增的 `data/*_cn_site_raw/`）。
每个文件 = 一个外站来源：URL + 抓取时间戳（UTC）+ 原样内容 / 搜索摘要 + 「对 Saga 的含义」备注。按 Simon 指示：**对错 / 冲突一律入库**，冲突处已标明。

| 品牌 | 文件 | 来源 | 抓取时间 (UTC) | 状态 |
|---|---|---|---|---|
| SmartByte | `smartbyte/computex_taipei_exhibitor.md` | computextaipei.com.tw 参展商页（Huizhou SmartByte）+ FOB 目录 + Peter Hu LinkedIn 摘要 | 12:53–12:59 | ✅ 正文 |
| SmartByte | `smartbyte/made_in_china_showroom.md` | made-in-china.com 展厅（Shenzhen SmartByte，Miss Anna，2023 注册，无产品） | 12:59 | ✅ 正文 |
| SmartByte | `smartbyte/sviaz_2024_moscow_exhibitor.md` | icatalog.expocentr.ru SVIAZ 2024 展商目录（21F38，No MOQ） | 13:05 | ✅ 正文 |
| SmartByte | （旧页残留） | Google 快照 `smartbyte-switch.com/Contact-Us.html`（旧导航 IEC61850-3 / EN50155 / Bypass / IP67）在 2026-09 归档中不存在（`pages_manifest.jsonl` 350 页无此 URL，13:20 核）；RX 展会 PDF 链接（ISE/RX mediabox）访问被拒（13:21） | 13:20–13:21 | ⛔ 旧页 |
| SmartByte | （负面结果，记录于本索引） | Alibaba 无店铺（`site:alibaba.com smartbyte switch`，12:54）；ImportYeti 无美国海运记录（`/supplier/shenzhen-smartbyte-technology` 404，13:03）；smartbyte.com.cn 抓取失败（12:53，疑已停用，交 Actions 探路）；中文工商名未查到（12:56–12:58） | — | ⛔ 负面 |
| HRUI | `hrui/alibaba_product_1600095957148.md` | 阿里国际站产品页 + 店铺卡片（hrgx.en.alibaba.com，13 年金牌，价格） | 12:54–12:55 | ✅ 正文（店铺首页 CAPTCHA） |
| HRUI | `hrui/工商与融资信息_36kr_天眼查摘要.md` | 36 氪创投 / 天眼查转载：**深圳市洪瑞光祥电子技术有限公司**，堵亚林，2013-06-25，520 万，USCC 9144030007175917XK | 12:58 | ✅ 摘要（与既有中文名冲突，已标） |
| HRUI | `hrui/hrgdkj_cn_site_搜索摘要.md` | 中文官网 hrgdkj.com（12,000 ㎡ / 8 线 / 年产 200 万台 / UL CB KC ANATEL / 大事记） | 12:59 | ✅ 摘要（直抓失败 → Actions 整站） |
| HRUI | `hrui/importyeti_美国海运提单_客户名单.md` | ImportYeti 供应商页（44 票 2018–2026）+ Spectrumvoip 客户页：GW Security / Component Specialties / Spectrumvoip / Tycon / Great Wall Security / Spanish Fork City / PoE Texas / CCTV Supply | 13:01–13:03 | ✅ 正文 |
| HRUI | `hrui/made_in_china_showroom_hruitech0901.md` | MIC 展厅（Mr. Tim，ISO9001，出口 2017 起，T/T PayPal WU，年产值 $50–100M）+ LinkedIn 公司页 / Computex / RX 展会 PDF 的 URL 记录 | 13:05 | ✅ 正文 |
| HRUI | （零售渠道，记录于本索引） | Amazon.ae 品牌店 "HRUI PoE Networks"（24 口 FE PoE AED 370；8 口 AED 155，ASIN B0DG33VBXJ / B0DG35NM4Q）；伊朗经销 digikala.com/brand/hrui、rashsystem.com、rundeman.com；越南经销 chuyenpoe.com、truongthinhtelecom.com（HR901-AF-1621GS-300 2,900,000₫ 原价）；阿里产品页 HR901-AF-1621GS-300 https://www.alibaba.com/product-introduction/HRUI-Wholesale-16-Ports-PoE-Switch_60782783934.html | 13:06 | ✅ 摘要 |
| Hohunet | `hohunet/hohunet_cn_home.md` | 中文官网首页 chunk 0（深圳市浩湖网络技术有限公司，产品 / 历程） | 12:57 | ✅ 正文（整站交 Actions） |
| Hohunet | `hohunet/工商信息_天眼查_BOSS直聘_猎聘摘要.md` | 刘驰 87.46%，2015-06-24，500 万，USCC 91440300342943439N，曾用名深圳湾趣堂科技，高企 GR202444203900，1–49 人，专利 11 / 商标 4，成都分公司 | 12:58 | ✅ 摘要 |
| Hohunet | `hohunet/alibaba_店铺与价格_搜索摘要.md` | 阿里店铺 hohunet.en.alibaba.com（Shenzhen haohu Network）缓存价格 $680–$5,000；SDVoE 联盟产品目录 | 13:03–13:04 | ✅ 摘要（店铺直抓 404，疑下线） |
| Hohunet | `hohunet/hohunet_cn_新闻与页面清单_搜索摘要.md` | 中文站导航 / 新闻（乌兹别克 ICT Week 2024 K6/K8，24 口 2.5G 发布，电竞馆方案）/ 产品页 | 13:07 | ✅ 摘要 |
| Hohunet | （负面结果，记录于本索引） | Amazon / AliExpress / 1688 / 京东无零售（13:07）；ImportYeti 无美国海运记录（搜索 13:04）；LinkedIn 个人页 Barnett LIAO https://www.linkedin.com/in/barnett-hohunet/ （38 followers，5 年前帖：48 口 2.5GBase-T L3 + 2×40G + 4×25G）；host.io/hohunet.com（阿里云美国 47.253.43.48，外链 hohunet.cn / sdvoe.org / miit.gov.cn） | — | ⛔/ℹ️ |

## 已搜索过的查询（勿重复）
`smartbyte.com.cn`；`"Smartbyte" industrial switch alibaba.com supplier Huizhou OR Shenzhen`；`"Smartbyte Technology" switch exhibitor Computex OR Sviaz`；`惠州 SmartByte 科技有限公司 镇隆 利和优客 交换机`；`"SmartByte" 深圳 OR 惠州 科技有限公司 交换机 企查查`；`"SmartByte" ethernet switch linkedin company OR youtube OR facebook`；`site:alibaba.com smartbyte switch`；`惠州 镇隆 利和优客创新基地 交换机 … Marvell`；`"smartbyte-switch.com" OR "smartbyte.com.cn" … Sviaz OR youtube …`；`Sviaz 2024 Expocentre exhibitor list "Smartbyte"`；`HRUI PoE switch alibaba "Hongrui" supplier store`；`深圳市洪瑞光电科技有限公司 注册资本 法定代表人 成立日期`；`HRUI switch made-in-china OR aliexpress OR amazon OR 1688 "洪瑞"`；`hrgdkj.com 洪瑞光祥 PoE交换机 工业交换机 官网`；`importyeti.com "Shenzhen Hongrui Optical Technology"`；`"HRUI" PoE switch aliexpress OR amazon OR 1688.com OR ebay HR-SWTG OR HR901`；`Hohunet switch alibaba OR made-in-china OR linkedin "Shenzhen Hohunet Technology"`；`深圳市浩湖网络技术有限公司 法定代表人 注册资本 成立`；`importyeti OR panjiva OR volza "Hongrui Optical" OR "Smartbyte Technology" OR "Hohunet"`；`importyeti.com supplier "Smartbyte" OR "Hohunet" switch Shenzhen`；`alibaba.com product-detail Hohunet S5624XH OR S7606X …`；`"Hohunet" OR "haohu network" importyeti OR panjiva … linkedin.com/company`；`"Hohunet" switch amazon OR aliexpress OR 1688 OR taobao OR jd.com 浩湖`

## 待 Actions 回填
- `data/site_recrawl/20261022/{smartbyte,hrui,hohunet}/diff.md`（三家官网 vs 10-20/10-21 基线）
- `data/hrui_cn_site_raw/`、`data/hohunet_cn_site_raw/`、`data/smartbyte_cn_site_raw/`（v3.2 新增；smartbyte.com.cn 可能 blocked/dead）
| hrui | GitHub（brennoo/terraform-provider-hrui、logicog/RTLPlayground、openwrt/openwrt DTS、up-n-atom/SWTG118AS） | `hrui/github_opensource_ecosystem.md` | HRUI ZX-/SWTG 硬件族 = Horaco/Sodola/XikeStor/MokerLink/AmpCom/keepLINK/Lianguo/TRENDnet 同板；OpenWrt 主线支持 RTL9303/9313 机型 | 13:31Z |
| smartbyte | GitHub（librenms/librenms PR #18681、netdata trap profile、TencentBlueKing/bk-lite、IEEE MA-M 列表） | `smartbyte/github_nms_support_and_oui.md` | LibreNMS 原生支持 SmartByte OS（Frederik Kriewitz/NYNEX 2026-01-11，测试机 STC-4168XGGCM）；netdata/蓝鲸插件；MA-M FC:CD:2F:D + 观澜 D 栋 6 楼地址 | 13:34Z |
| hohunet | GitHub OUI 列表（pg-oui、netpulse、systemd hwdb） | `smartbyte/github_nms_support_and_oui.md` §4 | Hohunet IEEE OUI D8:5B:22 | 13:34Z |
