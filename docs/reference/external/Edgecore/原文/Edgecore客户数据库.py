#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Edgecore 客户数据库生成脚本
============================
按 MikroTik 同等范式处理 Edgecore 信息：
  - 渠道伙伴库（Edgecore 官网 Where-to-Buy 全球名录）
  - 案例客户库（Edgecore 官方案例 + 合作伙伴/新闻稿公开案例）
  - 目标客户评估（按我方客户画像打分排序）
数据来源均为公开渠道；采集时间 2026-10-18（Asia/Shanghai）。
运行: python3 Edgecore客户数据库.py  → 生成 Edgecore客户数据库.xlsx
"""

import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

COLLECT_TIME = "2026-10-18 17:30:00"   # 采集/生成时间 Asia/Shanghai

# ============================================================
# Sheet 1 渠道伙伴库
# 字段: 大区, 国家/地区, 公司名称, 渠道类型, 地址, 电话, 来源页
# 渠道类型: 分销商 / SI·VAR·经销商 / 线上电商
# ============================================================
PARTNERS = [
    # ---------- 亚太 分销商 ----------
    ("亚太", "澳大利亚", "D2UNet Pty Ltd", "分销商", "8 Darter Street, The Ponds, NSW 2769", "(02) 9629 8780", "asia-distributors"),
    ("亚太", "澳大利亚", "Endy Australia", "分销商", "1/14 Wellington Street, Acacia Ridge Brisbane QLD 4110", "1300 725 323", "asia-distributors"),
    ("亚太", "澳大利亚", "Newgen Systems Pty Ltd", "分销商", "Suite 401, 737 Burwood Road Hawthorn East 3123", "+61-3-9894 5130", "asia-distributors"),
    ("亚太", "孟加拉国", "Richman Informatics", "分销商", "Navana DH Tower, Suite # 502, 6 Panthopath, Dhaka-1215", "+880-2-9143683", "asia-distributors"),
    ("亚太", "柬埔寨", "Mekong Link Co. LTD", "分销商", "S3-08–S3 09, Olympia Mall Street 217 and 182 Blvd, Phnom Penh", "+855-23902239", "asia-distributors"),
    ("亚太", "印度尼西亚", "PT Converion Solution Informatica", "分销商", "Centennial Tower 12th Floor, Jl. Jend. Gatot Subroto Kav.24-25, Jakarta 12930", "+62-21-806 22278", "asia-distributors"),
    ("亚太", "印度尼西亚", "PT. Sysware Indonesia", "分销商", "Komplek Puri Mutiara Blok BD No.5, Jakarta 14350", "+62-21-29569443", "asia-distributors"),
    ("亚太", "印度尼西亚", "PT. Krida Hasta Tama", "分销商", "Jl. Arjuna Utara 50, Jakarta Barat 11510", "+62-21-564 4843", "asia-distributors"),
    ("亚太", "日本", "APRESIA Systems, Ltd.", "分销商", "8F, Tsukiji Daiichi Nagaoka Bldg. 2-3-4 Tsukiji, Chuo-ku, Tokyo", "03-6369-0401", "asia-distributors"),
    ("亚太", "日本", "ITOCHU Techno-Solutions Corporation", "分销商", "Kasumigaseki Bldg., 3-2-5 Kasumigaseki, Chiyoda-ku, Tokyo", "03-6203-5000", "asia-distributors"),
    ("亚太", "日本", "MACNICA, Inc.", "分销商", "Macnica Bldg. No.1, 1-6-3 Shin-Yokohama, Kohoku-ku, Yokohama", "+81-45-470-9831", "asia-distributors"),
    ("亚太", "马来西亚", "E-TECH IT Sdn Bhd", "分销商", "No 15, Jalan Astaka U8/83, Bukit Jelutong, 40150 Shah Alam, Selangor", "+60-3-7846-2338", "asia-distributors"),
    ("亚太", "缅甸", "Loi Heng International", "分销商", "253(B), Seikkan Thar Street, Kyauktada Township, Yangon", "(01) 246221", "asia-distributors"),
    ("亚太", "缅甸", "TrustForce Myanmar", "分销商", "No(22), MyitZu Street (4), Parami Road, Yankin Township, Yangon", "+95-9-952252591-2", "asia-distributors"),
    ("亚太", "尼泊尔", "Green Cube Technologies Pvt. Ltd.", "分销商", "Buddhanagar, New Baneshwor, Kathmandu", "01-4787059", "asia-distributors"),
    ("亚太", "新西兰", "Computer Dynamics Limited", "分销商", "130 Bush Road, North Harbour Industrial Estate, Albany, Auckland", "64-9-415 9002", "asia-distributors"),
    ("亚太", "菲律宾", "BANBROS COMMERCIAL., INC.", "分销商", "#32 Pilar St. Corner Araullo St., Addition Hills, San Juan City", "63-2-7051700", "asia-distributors"),
    ("亚太", "新加坡", "Starview Technologies Pte Ltd", "分销商", "60 Kaki Bukit Place #05-19 Eunos Techpark, Singapore 415979", "+65-3157 5338", "asia-distributors"),
    ("亚太", "新加坡", "VSTECS (Singapore) Pte Ltd", "分销商", "19 Kallang Avenue #07-153, Singapore 339410", "+65-6299 9433", "asia-distributors"),
    ("亚太", "韩国", "STN Infotech Co., Ltd.", "分销商", "A-303 URBAN HUN, 60, Gwacheon-daero7na-gil, Gwacheon-si, Gyeonggi-do", "+82-2-507-8088", "asia-distributors"),
    ("亚太", "中国台湾", "PETACOM TECHNOLOGY CO., LTD.", "分销商", "Rm.B, 2F., No.6, Ln.107, Sec.3, Minsheng E. Rd., Songshan Dist., Taipei", "(02)2719-1128", "asia-distributors"),
    ("亚太", "中国台湾", "Xander international corp.", "分销商", "5F., No.531, Zhongzheng Rd., Xindian Dist., New Taipei City 231", "(02)2219-1600", "asia-distributors"),
    ("亚太", "泰国", "Easy Net Co.,Ltd.", "分销商", "162/45 Sudsawat road, Khwaeng Rat Burana Khet Rat Burana, Bangkok 10140", "+66-81722 6111", "asia-distributors"),
    ("亚太", "泰国", "SWS Group Company Limited", "分销商", "2126 Kromadit Building, 1st Floor, New Petchburi Road, Huay Kwang, Bangkok 10310", "+66-2-016 3006", "asia-distributors"),
    ("亚太", "越南", "NETMARK DISTRIBUTION", "分销商", "37 Sixth Street, Cityland Park Hills, Go Vap District, Ho Chi Minh City", "(84) 906 814 510", "asia-distributors"),
    ("亚太", "越南", "PAVANA TECHNOLOGIES", "分销商", "The Vista, 4/15 Duy Tan, Cau Giay 123000, Hanoi", "(+84) 8 5333 5995", "asia-distributors"),
    ("亚太", "越南", "SSS Vietnam Joint Stock Company", "分销商", "SSS Building, No10/2, lane 124 Minh Khai Street, Hanoi", "(+84) 948398837", "asia-distributors"),
    # ---------- 亚太 SI/VAR/经销商 ----------
    ("亚太", "澳大利亚", "SAPPLY Pty Ltd", "SI·VAR·经销商", "25 Dickson Avenue, Artarmon, New South Wales 2064", "+61-2-9439 8887", "asia-reseller"),
    ("亚太", "文莱", "C. F. KING Enterprise", "SI·VAR·经销商", "Unit 23, Bgn Awg Hj Matussin, Kg. Kiulap, Bandar Seri Begawan BE1518", "+673-2237382", "asia-reseller"),
    ("亚太", "柬埔寨", "Positron Multiverse Co., Ltd", "SI·VAR·经销商", "#05, Street 604, Beng Kok II, Phnom Penh", "+855-23-884 242", "asia-reseller"),
    ("亚太", "中国香港", "SKYWARE PROTECH LIMITED", "SI·VAR·经销商", "Room 3806A, 38/F., Cable TV Tower, 9 Hoi Shing Road, Tsuen Wan, N.T.", "(852) 31060868", "asia-reseller"),
    ("亚太", "印度尼西亚", "PT. Gwen Tekno Pratama", "SI·VAR·经销商", "Jl.Gemini No.22 Kel.Gumuruh Kec.Batununggal Kota Bandung 40275", "+62-22-73512118", "asia-reseller"),
    ("亚太", "印度尼西亚", "PT Trinet Prima Solusi", "SI·VAR·经销商", "Jl. Tanah Abang II No.104, Cideng, Gambir, Jakarta Pusat 10150", "021-3483-1212", "asia-reseller"),
    ("亚太", "菲律宾", "Algorithmic Digital Solutions Inc.", "SI·VAR·经销商", "Unit 3F Virt.53 Symphony Tower 2, Sgt Esguerra Ave., Quezon City 1103", "+63-968-8777 100", "asia-reseller"),
    ("亚太", "日本", "MITSUI KNOWLEDGE INDUSTRY CO., LTD.", "SI·VAR·经销商", "Atago Green Hills MORI Tower, 2-5-1 Atago, Minato-ku, Tokyo", "+81-3-6376-1000", "asia-reseller"),
    ("亚太", "日本", "NEC Networks & System Integration Corporation", "SI·VAR·经销商", "1753 Shimonumabe, Nakahara-KU, Kawasaki, Kanagawa 211-8666", "+81-44-435-1636", "asia-reseller"),
    ("亚太", "马来西亚", "DataOne Solutions Sdn Bhd", "SI·VAR·经销商", "14-8, 2 Rio Tower, Persiaran Rio Bandar Puteri, 47100 Puchong, Selangor", "603-8604 5978", "asia-reseller"),
    ("亚太", "马来西亚", "Tech Trad Solution Sdn Bhd", "SI·VAR·经销商", "Unit 12-07, Tower A, Vertical Business Suite, Bangsar South, Kuala Lumpur 59200", "(603) 2303 5899", "asia-reseller"),
    ("亚太", "马来西亚", "VEMAX TECHNOLOGY", "SI·VAR·经销商", "LOT 10995, Second Floor, Jalan Sungai Apong, 93450 Kuching Sarawak", "+6016-8747515", "asia-reseller"),
    ("亚太", "马来西亚", "VESC Solution Sdn. Bhd", "SI·VAR·经销商", "Unit 8-3, Wisma PJ5 SOHO, Jalan SS 5D/6, Kelana Jaya, 47301 Petaling Jaya", "1700 81 5648", "asia-reseller"),
    ("亚太", "新西兰", "Snapper Network Distributors Ltd", "SI·VAR·经销商", "13 Beatrice Tinsley Crescent, Albany, Auckland", "+64-9-415 4182", "asia-reseller"),
    ("亚太", "新加坡", "AsiaPac Distribution Pte Ltd", "SI·VAR·经销商", "Blk 219 Henderson Road, #05-01/02/03/04 Henderson Industrial Park, SG 159556", "(+65) 6270 8281", "asia-reseller"),
    ("亚太", "新加坡", "ComWorth Solutions Pte Ltd", "SI·VAR·经销商", "81 Ubi Avenue 4, #06-02 UB.One, Singapore 408830", "+65-6748 2260", "asia-reseller"),
    ("亚太", "韩国", "AHNNET CO., Ltd.", "SI·VAR·经销商", "#313, 3F, Samhwan Hypex B, 230 Pangyoyeok-ro Bundang-gu, Seongnam-si", "+82-31-698 2020", "asia-reseller"),
    ("亚太", "韩国", "AI TECH CO., Ltd", "SI·VAR·经销商", "8, Teheran-ro 44-gil, Gangnam-gu, Seoul (7F ICON YEOKSAM B/D)", "+82-2-557 6366", "asia-reseller"),
    ("亚太", "韩国", "DONGIL TECH Co., Ltd", "SI·VAR·经销商", "39, Maeyoungro 269beon-gil, Youngtong-gu, Suwon-si, Gyeonggi-do", "+82-31-216 7122", "asia-reseller"),
    ("亚太", "韩国", "DS&G Co., Ltd.", "SI·VAR·经销商", "1-501, 502, ACE Hitech City, 775, Gyeongin-ro, Yeongdeungpo-gu, Seoul", "+82-2-6949 1850", "asia-reseller"),
    ("亚太", "韩国", "INFO-A Inc", "SI·VAR·经销商", "Shinsung bldg B-205, Achasanro 96, Sungdong-gu, Seoul 04782", "+82-2-469 7550", "asia-reseller"),
    ("亚太", "韩国", "LANOASIS Co., Ltd.", "SI·VAR·经销商", "17F, G-Highcity Building, Digital-ro 243, Guro-gu, Seoul 08382", "+82-2-3272 7911", "asia-reseller"),
    ("亚太", "韩国", "NEWGENS Co., Ltd.", "SI·VAR·经销商", "6F, Gwacheon Smart-K A-Tower 20, Gwacheon-daero 7-gil, Gwacheon-si", "+82-2-6247 3901", "asia-reseller"),
    ("亚太", "韩国", "Opasnet Co., Ltd.", "SI·VAR·经销商", "10F Shinan bldg, 512, Teheran-ro, Gangnam-gu, Seoul 06179", "+82-2-2193 8600", "asia-reseller"),
    ("亚太", "韩国", "TRENTO SYSTEMS Inc.", "SI·VAR·经销商", "50, Techno jungang-ro, Yuseong-gu, Daejeon 34018", "+82-42-710-5600", "asia-reseller"),
    ("亚太", "韩国", "UNIQUEST CORP.", "SI·VAR·经销商", "8F Uniquest Building, 314, Hwangsaeul-ro, Bundang-gu, Seongnam-si", "+82-31-798 9988", "asia-reseller"),
    ("亚太", "中国台湾", "COMMVERGE TECHNOLOGIES HOLDINGS (ASIA) LIMITED", "SI·VAR·经销商", "6F., No.192, Jingye 1st Rd., Zhongshan Dist., Taipei City 10462", "+886-2-8502-7258", "asia-reseller"),
    ("亚太", "中国台湾", "HPI CORPORATION", "SI·VAR·经销商", "No.118, Wugong 3rd Rd., Wugu Dist., New Taipei City", "02-2298 2958", "asia-reseller"),
    ("亚太", "中国台湾", "ISON Technology", "SI·VAR·经销商", "No.332, Zhongbei 3rd St., Linkou Dist., New Taipei City 244016", "+886-2-26036619", "asia-reseller"),
    ("亚太", "中国台湾", "SilverShine Technology Inc.", "SI·VAR·经销商", "Rm.1, 2F., No.18, Ln.48, Xingshan Rd., Neihu Dist., Taipei City 11469", "+886-2-8792-6128", "asia-reseller"),
    ("亚太", "泰国", "CTC GLOBAL (THAILAND) LTD.", "SI·VAR·经销商", "1788 Singha Complex, Unit 2301-2305, 23rd Floor, New Phetchaburi Road, Bangkok 10310", "+66-2-059-0411", "asia-reseller"),
    ("亚太", "泰国", "DATA IN MOTION CO., LTD.", "SI·VAR·经销商", "25 AlmaLink Building 9th, Soi Chidlom, Ploenchit Road, Lumpini, Bangkok 10330", "+66-2-255-6691", "asia-reseller"),
    ("亚太", "泰国", "Success Network", "SI·VAR·经销商", "81/19 Moo.5 Nawamin Road, Khongkum, Bangkum, Bangkok 10240", "6681-659-4477", "asia-reseller"),
    ("亚太", "泰国", "Throughwave (Thailand) Co., Ltd.", "SI·VAR·经销商", "43 Thai CC Tower, 23rd Floor, Room 234, South Sathorn Rd., Bangkok 10120", "66-2-210-0968-9", "asia-reseller"),
    ("亚太", "越南", "FPT INFORMATION SYSTEM CORPORATION", "SI·VAR·经销商", "22F, Keangnam Landmark 72 Tower, E6 Pham Hung road, Nam Tu Liem, Hanoi", "+84-24-35626000", "asia-reseller"),
    ("亚太", "越南", "NDC JOINT STOCK COMPANY", "SI·VAR·经销商", "4th Floor, Estar Building, 147–149 Vo Van Tan, District 3, Ho Chi Minh City", "(028) 35200096", "asia-reseller"),
    ("亚太", "越南", "NETCOM Co., Ltd.", "SI·VAR·经销商", "46A/120 Truong Chinh, Dong Da, Hanoi", "+84-4-35737747", "asia-reseller"),
    # ---------- 印度次大陆 ----------
    ("印度次大陆", "印度", "Electronic Product Services India Pvt. Ltd.", "分销商", "Ground Floor, No.235-O/2, Bommasandra Industrial Area, Phase III, Bangalore 560099", "+91-9873381338", "indian-distributors"),
    ("印度次大陆", "印度", "PalC Networks Pvt. Ltd.", "分销商", "Unit 8, 5th Floor, Navigator Building, International Tech Park Bangalore, Whitefield", "+91-8040905088", "indian-distributors"),
    ("印度次大陆", "印度", "Saimaa Technologies LLP", "分销商", "11 GRND FLR C-WING BLDG NO 1, KAILAS IND CMPLX, PARKSITE VIKHROLI, MUMBAI 400079", "+91-9820919959", "indian-distributors"),
    ("印度次大陆", "印度", "Sheeltron Digital Systems Pvt. Ltd.", "分销商", "#2/1, East Park Road, Kumara Park East, South End Street, Bangalore 560001", "+91-8067572222", "indian-distributors"),
    ("印度次大陆", "尼泊尔", "Green Cube Technologies Pvt. Ltd.", "分销商", "New Baneshwor, Kathmandu", "01-4787059", "indian-distributors"),
    ("印度次大陆", "印度", "COMPUTERS NETWORK & TELECOM", "SI·VAR·经销商", "512, Sector 43, Golf Course Road, Gurgaon, Haryana 122002", "0124-4125747", "indian-reseller"),
    ("印度次大陆", "印度", "Khushi Communications Pvt. Ltd.", "SI·VAR·经销商", "705-706, 7th Floor, Kirti Shikhar Building, Janakpuri District Centre, New Delhi 110058", "011-4161 5459", "indian-reseller"),
    ("印度次大陆", "印度", "KRUPAM SOLUTIONS LLP", "SI·VAR·经销商", "403, Hir-Asha Arcade, Nr Shaleen Hospital, Sola Gam Rd. Sciencecity, Ahmedabad", "+91-7405375321", "indian-reseller"),
    ("印度次大陆", "印度", "Maheshwari Computer Pvt. Ltd.", "SI·VAR·经销商", "203, Apollo Trade Centre, Geeta Bhavan Square, A.B. Road, INDORE (MP)", "0731-4068836", "indian-reseller"),
    ("印度次大陆", "印度", "Micromap Electronic Systems Private Limited", "SI·VAR·经销商", "House No.137, First Floor, Sant Nagar, East of Kailash, New Delhi 110065", "+91-8048964250", "indian-reseller"),
    ("印度次大陆", "印度", "Ovin Technologies", "SI·VAR·经销商", "MSR CAPITAL Office No.403, 4th Floor, Samrat Chowk, Pimpri, Pune-411018", "+91-89561 36940", "indian-reseller"),
    ("印度次大陆", "印度", "Ravi and Singh Communication", "SI·VAR·经销商", "The Cloverleaf, 1st Floor, Plot-37, Sector-11 (Metro Station), Dwarka, New Delhi-110075", "+91-11-40558635", "indian-reseller"),
    ("印度次大陆", "印度", "Sapphire Micro Systems", "SI·VAR·经销商", "A/129 Ansa Industrial Estate, Saki Vihar Road, Andheri East, Mumbai 400072", "+91-22-28472160", "indian-reseller"),
    ("印度次大陆", "印度", "SEC Communications Pvt Ltd.", "SI·VAR·经销商", "T-301, 3rd Floor, Phoenix Victoria, 16, Victoria Road, Bangalore 560025", "+91-80-42286554", "indian-reseller"),
    ("印度次大陆", "印度", "Team5 Technologies Pvt. Ltd.", "SI·VAR·经销商", "No.63, OVH Road, Basavanagudi, Bangalore 560004", "+91-9738413329", "indian-reseller"),
    # ---------- EMEA 分销商 ----------
    ("EMEA", "塞浦路斯", "ASBIS Enterprises PLC", "分销商", "1, Iapetou Street Agios Athanasios, 4101 Limassol (Head Office)", "357-25-857 000", "emea-distributors"),
    ("EMEA", "塞浦路斯", "MCS IT Distribution Ltd.", "分销商", "Evagora Papachristoforou 6, 1st floor 3030, Limassol", "+357-25-101 565", "emea-distributors"),
    ("EMEA", "捷克", "PROFIcomms s.r.o.", "分销商", "Turgenevova 5, 625 00 Brno", "+420-548210406", "emea-distributors"),
    ("EMEA", "法国", "ALLNET France", "分销商", "96 rue Lamarck", "+33-4-48 23 02 90", "emea-distributors"),
    ("EMEA", "德国", "Allnet GmbH Computersysteme", "分销商", "Maistr. 2, D-82110 Germering", "+49-89-89422222", "emea-distributors"),
    ("EMEA", "德国", "Electronic Product Services", "分销商", "Rheinstrasse 41, 64283 Darmstadt", "+49-6151-501 2454", "emea-distributors"),
    ("EMEA", "德国", "STORDIS GmbH", "分销商", "Rübteile 24, 72574 Bad Urach / Rosenwiesstr.17, 70567 Stuttgart", "+49-711-342 158 0", "emea-distributors"),
    ("EMEA", "德国", "Syserso Networks GmbH", "分销商", "Ahrensburger Straße 8, 30659 Hannover", "+49-511-740192-0", "emea-distributors"),
    ("EMEA", "爱尔兰", "Electronic Product Services", "分销商", "Unit 17 Kinsealy Business Park, Kinsealy, Co. Dublin", "+353-1-8038918", "emea-distributors"),
    ("EMEA", "以色列", "ScaleIL LTD", "分销商", "1 Zarchin St., Raanana 4366229", "052-665-2070", "emea-distributors"),
    ("EMEA", "沙特阿拉伯", "MBUZZ", "分销商", "Building CS-01, Al-Raidah, Digital City, Riyadh", "+966-53-037 8192", "emea-distributors"),
    ("EMEA", "波兰", "ASBIS Poland Sp.z o.o", "分销商", "Ul. M. Słowikowskiego 81C, Budynek H4, 05-090 Raszyn", "48-501867434", "emea-distributors"),
    ("EMEA", "罗马尼亚", "Electronic Product Services", "分销商", "Calea Torontalului DN6 KM7 Timisoara 1900", "+40-256-22 33 07", "emea-distributors"),
    ("EMEA", "土耳其", "Erete Bilgi Sistemleri Dis. Tic ve San. Ltd. Sti.", "分销商", "19 Mayıs Mah. Güven Sk. No: 4/2 Şişli-İSTANBUL", "+90-212-2128103", "emea-distributors"),
    ("EMEA", "土耳其", "NOKTA ELEKTRONIK VE BILISIM SISTEMLERI SAN. TIC. A.S.", "分销商", "Perpa Ticaret Merkezi A Blok Kat.2 No.1 Okmeydanı-Şişli-Istanbul", "+90-212-222 8780", "emea-distributors"),
    ("EMEA", "巴基斯坦", "IntruGrid LLP", "分销商", "2nd Floor, Olympus Mall F-11 Markaz Islamabad 44000", "+92-3335156428", "emea-distributors"),
    ("EMEA", "巴基斯坦", "NETSOFT SOLUTIONS", "分销商", "Capri Centre 2nd Floor, Firdous Market Gulberg III Lahore", "(+92) 323 406 1842", "emea-distributors"),
    ("EMEA", "巴基斯坦", "STARCOM Technologies (Private) Limited", "分销商", "401-C, Panorama Center II, Raja Ghazanfar Ali Road, Saddar Karachi", "+92-21-3566 1550", "emea-distributors"),
    ("EMEA", "阿联酋", "ASBIS Middle East FZE", "分销商", "P.O. Box 17706, Jebel Ali South, S10806, Dubai", "+971-4-8863850", "emea-distributors"),
    ("EMEA", "阿联酋", "Evollabs Tech FZ-LLC", "分销商", "Dubai Internet City, DIC-Bldg.05-118, Dubai", "+971-4-529 9011", "emea-distributors"),
    ("EMEA", "阿联酋", "MBUZZ", "分销商", "#313, Al Nazr Plaza, Dubai", "+971-4-330 4125", "emea-distributors"),
    ("EMEA", "英国", "Electronic Product Services", "分销商", "14A Church Street, Caversham, Reading RG4 8AU", "+44-20-3008 9709", "emea-distributors"),
    ("EMEA", "英国", "STORDIS Limited", "分销商", "The Barn, 36 High Street, Pershore WR10 1DP", "+44-7307412298", "emea-distributors"),
    # ---------- EMEA SI/VAR/经销商 ----------
    ("EMEA", "奥地利", "Fionis GmbH", "SI·VAR·经销商", "Anton-Hubmann-Platz 2, 8071 Goessendorf", "+43-3135-40 960-0", "emea-reseller"),
    ("EMEA", "比利时", "Deca Consulting", "SI·VAR·经销商", "Haldertstraat 116, 3390 Houwaart", "+32-16-89 87 71", "emea-reseller"),
    ("EMEA", "法国", "Alyseo", "SI·VAR·经销商", "44 rue Armand Carrel 93100 Montreuil", "+33-1-83 35 10 10", "emea-reseller"),
    ("EMEA", "法国", "CELERIS Informatique", "SI·VAR·经销商", "6 rue de l'Abbé Hazard, 92 000 NANTERRE", "01-71-12-60-23", "emea-reseller"),
    ("EMEA", "法国", "Pine Networks", "SI·VAR·经销商", "219, Grande Rue, 92380 Garches", "+33-1-88 94 77 04", "emea-reseller"),
    ("EMEA", "德国", "ADN – Advanced Digital Network Distribution GmbH", "SI·VAR·经销商", "Josef-Haumann-Str. 10, 44866 Bochum", "+49-2327-9912-0", "emea-reseller"),
    ("EMEA", "德国", "DELTA Computer Products GmbH", "SI·VAR·经销商", "Rontgenstr. 4, D-21465 Reinbek bei Hamburg", "+49-40-300 672-0", "emea-reseller"),
    ("EMEA", "德国", "KTI Distribution GmbH", "SI·VAR·经销商", "Meisenstraße 79a, 33607 Bielefeld", "+49-521-96680-0", "emea-reseller"),
    ("EMEA", "德国", "primeLine Solutions GmbH", "SI·VAR·经销商", "Zur Bauernwiese 25, 32549 Bad Oeynhausen", "+49-5731-8694-400", "emea-reseller"),
    ("EMEA", "德国", "Xantaro Deutschland GmbH", "SI·VAR·经销商", "An der Alster 3, 20099 Hamburg", "+49-40-4134980", "emea-reseller"),
    ("EMEA", "匈牙利", "Cell-Core Industrial Technologies Ltd", "SI·VAR·经销商", "1142 Budapest, Szőnyi út 36 / HU-2120 Dunakeszi", "+36-30-589 0788", "emea-reseller"),
    ("EMEA", "匈牙利", "LaserNetworks Kft", "SI·VAR·经销商", "2112 Veresegyház Levendula 45", "1-44-54-129", "emea-reseller"),
    ("EMEA", "意大利", "Active Solution & Systems S.r.l.", "SI·VAR·经销商", "Via Angelo Moro 97, 20097 San Donato Milanese (Milano)", "+39-02-514843", "emea-reseller"),
    ("EMEA", "肯尼亚", "Mart Networks Kenya", "SI·VAR·经销商", "2nd Floor Museum Hill Centre, Nairobi", "+254-20-5135200", "emea-reseller"),
    ("EMEA", "肯尼亚", "Soliton Telmec Limited", "SI·VAR·经销商", "Soliton Park, North Airport Road, Embakasi, Nairobi", "+254-709-499000", "emea-reseller"),
    ("EMEA", "摩洛哥", "ODDnet", "SI·VAR·经销商", "Technopark Bd-Dammam, Casablanca", "+212-520-275 227", "emea-reseller"),
    ("EMEA", "荷兰", "Circle B", "SI·VAR·经销商", "Zekeringstraat 17, 1014 BM, Amsterdam", "+31-85-800 0430", "emea-reseller"),
    ("EMEA", "荷兰", "Distri X BV", "SI·VAR·经销商", "Mariniersweg 3E, 3011 INB Rotterdam", "+31-85-0204141", "emea-reseller"),
    ("EMEA", "荷兰", "Exclusive Networks", "SI·VAR·经销商", "Ekkersrijt 4601, 5692 DR SON", "+31-499-462121", "emea-reseller"),
    ("EMEA", "荷兰", "FiberUnlimited B.V.", "SI·VAR·经销商", "Smitspol 15E, 3861 RS Nijkerk", "+31-85-076 1501", "emea-reseller"),
    ("EMEA", "荷兰", "Infradata Group", "SI·VAR·经销商", "Nieuwenhuizenweg 3, 2314 XP Leiden", "+31-71-7501525", "emea-reseller"),
    ("EMEA", "荷兰", "Xentech B.V.", "SI·VAR·经销商", "Vredeweg 46 / D1, 1505-HH Zaandam", "+31-85-002 0796", "emea-reseller"),
    ("EMEA", "新西兰", "Computer Dynamics Limited", "SI·VAR·经销商", "130 Bush Road, Albany, Auckland", "64-9-415 9002", "emea-reseller"),
    ("EMEA", "波兰", "Stovaris Sp. z o.o.", "SI·VAR·经销商", "Staniewicka 12, 03-310 Warsaw", "+48-22-24 84 000", "emea-reseller"),
    ("EMEA", "葡萄牙", "TELCARIA", "SI·VAR·经销商", "Barrionuevo 8, Local 1, 28911 Leganés (Madrid), Spain", "+34-910261014", "emea-reseller"),
    ("EMEA", "卢旺达", "MART NETWORKS RWANDA", "SI·VAR·经销商", "Kigali City Tower, Kigali", "(+250) 788180100", "emea-reseller"),
    ("EMEA", "罗马尼亚", "Datanet Systems", "SI·VAR·经销商", "18 Sfântul Elefterie Str., Bucharest 050525", "+40-21-3178787", "emea-reseller"),
    ("EMEA", "塞尔维亚", "Upstream ICT Alliance", "SI·VAR·经销商", "Druge Srpske Armije no.9, Beograd 11000", "+381-11-4051779", "emea-reseller"),
    ("EMEA", "斯洛文尼亚", "Aero-IT distribucija d.o.o.", "SI·VAR·经销商", "Obrtna Cona Logatec 21, 1370 Logatec", "+386-40-130902", "emea-reseller"),
    ("EMEA", "斯洛文尼亚", "Kontron, d.o.o.", "SI·VAR·经销商", "Ljubljanska cesta 24a, 4000 Kranj", "+386-4-207 20 00", "emea-reseller"),
    ("EMEA", "南非", "Miro Distribution", "SI·VAR·经销商", "Unit No.6, N1 Industrial Park, Landmarks Avenue, Kosmosdal Ext 11, Samrand 0157", "+27-12-657 0960", "emea-reseller"),
    ("EMEA", "西班牙", "Telcaria", "SI·VAR·经销商", "Barrionuevo 8, Local 1, 28911 Leganés (Madrid)", "+34-910261014", "emea-reseller"),
    ("EMEA", "西班牙", "Wisi Spain (WISI Communicaciones, S.A.)", "SI·VAR·经销商", "Calle Duero 47, B, 28840, Mejorada del Campo Madrid", "+34-91-679 42 80", "emea-reseller"),
    ("EMEA", "瑞典", "Direktronik Aktiebolag AB", "SI·VAR·经销商", "Konsul Johnson vag 15, 149 45 Stockholm", "+46-8-52400700", "emea-reseller"),
    ("EMEA", "瑞典", "Vinnergi AB", "SI·VAR·经销商", "Platensgatan 26, 582 20 Linköping", "+46-101-02 44 00", "emea-reseller"),
    ("EMEA", "坦桑尼亚", "Mart Networks Tanzania", "SI·VAR·经销商", "Chole Road, Plot No.1935/4, Dar es Salaam", "(+255) 784 444490", "emea-reseller"),
    ("EMEA", "乌干达", "MART NETWORKS UGANDA", "SI·VAR·经销商", "7th Floor, Regus Course View Towers, Kampala", "(+256) 703 834115", "emea-reseller"),
    ("EMEA", "阿联酋", "Core Technologies LLC", "SI·VAR·经销商", "P6-89, Sharjah Airport Free Zone, Sharjah", "+971-52-99-444-56", "emea-reseller"),
    ("EMEA", "英国", "Astute Electronics Ltd.", "SI·VAR·经销商", "Astute House, Rutherford Close, Stevenage, Hertfordshire SG1 2EF", "+44-1438-909 909", "emea-reseller"),
    ("EMEA", "英国", "M2M Enterprise", "SI·VAR·经销商", "Hanover Place, 8 Ravensbourne Road, Bromley, Kent BR1 1HP, London", "+44-208-676 6067", "emea-reseller"),
    ("EMEA", "英国", "Telent Technology Services Ltd", "SI·VAR·经销商", "Point 3, Haywood Road, Warwick, CV34 5AH", "+44-1926-693 000", "emea-reseller"),
    ("EMEA", "英国", "Utopia Technology Limited", "SI·VAR·经销商", "15 Carnarvon Street, Manchester M3 1HJ", "0333-241 2526", "emea-reseller"),
    ("EMEA", "英国", "Vesper Technologies Ltd", "SI·VAR·经销商", "Units 5/6 Rugby Park Bletchley Road Stockport Cheshire SK4 3EJ", "+44-161-947 4321", "emea-reseller"),
    # ---------- 北美 ----------
    ("北美", "加拿大", "E.C.I. NETWORKS INC.", "分销商", "1405 Rte Transcanadienne, Dorval, QC H9P 2V9", "1-800-967-1672", "northamerica-distributors"),
    ("北美", "加拿大", "FONEX Data Systems Inc.", "分销商", "5400 chemin St-François, St-Laurent, Québec, H4S 1P6", "1-514-333-6639", "northamerica-distributors"),
    ("北美", "加拿大", "info-logic ebm", "分销商", "1400, boulevard Marie-Victorin, suite 103 St-Bruno (Québec) J3V 6B9", "1-450-653-7575", "northamerica-distributors"),
    ("北美", "加拿大", "Planiselect Inc.", "分销商", "653, ave Léo-Lacombe Laval (Québec) H7N 3Y7", "450-663-3973", "northamerica-distributors"),
    ("北美", "美国", "ASI", "分销商", "48289 Fremont Blvd. Fremont, CA 94538", "(510) 226-8000", "northamerica-distributors"),
    ("北美", "美国", "Avnet", "分销商", "2211 S. 47th St. Phoenix, Arizona 85034", "480-643-2000", "northamerica-distributors"),
    ("北美", "美国", "CTD", "分销商", "1200 Woodruff Rd, F9 Greenville, SC 29607", "1-864-527-9600", "northamerica-distributors"),
    ("北美", "美国", "EPS Global LLC", "分销商", "7920 Georgetown Road Suite 800, Indianapolis, Indiana 46268", "1-317-222-6334", "northamerica-distributors"),
    ("北美", "美国", "Global Convergence, Inc.", "分销商", "700 Brooker Creek Blvd. Ste.1000, Oldsmar, FL 34677", "(813) 925-6021", "northamerica-distributors"),
    ("北美", "美国", "Network Distributors", "分销商", "894 Faulstich Bld. A, San Jose, CA 95112", "1-408-392-0066", "northamerica-distributors"),
    ("北美", "美国", "TD SYNNEX", "分销商", "44201 Nobel Drive, Fremont, CA 94538", "800-237-8931", "northamerica-distributors"),
    ("北美", "美国", "Tech Data", "分销商", "8700 S Price Road, Tempe, AZ 85284", "800-237-8931", "northamerica-distributors"),
    ("北美", "加拿大", "Nine-One-One Communication Supply Inc.", "SI·VAR·经销商", "Bay 'F' 7004-5th Street S.E. Calgary AB T2H 2G3", "(800) 665-9911", "northamerica-reseller"),
    ("北美", "加拿大", "Solimedia Technology Inc.", "SI·VAR·经销商", "329-470 Granville Street, Vancouver BC V6C 1V5", "604-568 9797", "northamerica-reseller"),
    ("北美", "加拿大", "Tuangru", "SI·VAR·经销商", "Suite 800–510 West Hastings Street, Vancouver, BC V6B 1L8", "1-866-612-3637", "northamerica-reseller"),
    ("北美", "美国", "Advanced HPC", "SI·VAR·经销商", "Corporate Headquarters 8228 Mercury Court Suite 100, San Diego", "(858) 716-8262", "northamerica-reseller"),
    ("北美", "美国", "AMAX", "SI·VAR·经销商", "1565 Reliance Way, Fremont, CA 94539", "(800) 800-6328", "northamerica-reseller"),
    ("北美", "美国", "Anixter", "SI·VAR·经销商", "2301 Patriot Blvd. Glenview, IL 60026", "(800) 323 8167", "northamerica-reseller"),
    ("北美", "美国", "ASA Computers", "SI·VAR·经销商", "48761 Kato Road, Fremont, CA 94538", "800-732-5727", "northamerica-reseller"),
    ("北美", "美国", "Blue Chip Tek, Inc.", "SI·VAR·经销商", "3030 Olcott St, Santa Clara, CA 95054", "408-731-7700", "northamerica-reseller"),
    ("北美", "美国", "Blue Core (BlueCore Networks)", "SI·VAR·经销商", "28 Lord Road, Suite 260, Marlboro, MA 01752", "800-708-2785", "northamerica-reseller"),
    ("北美", "美国", "Cambridge Computer", "SI·VAR·经销商", "271 Waverley Oaks Road Suite 301, Waltham, MA 02452", "781-250 3000", "northamerica-reseller"),
    ("北美", "美国", "Champion One", "SI·VAR·经销商", "23645 Mercantile Rd. Beachwood, OH 44122", "216-831-1800", "northamerica-reseller"),
    ("北美", "美国", "Colfax Direct", "SI·VAR·经销商/线上电商", "750 Palomar Avenue, Sunnyvale, CA 94085", "(408) 730 2275", "northamerica-reseller"),
    ("北美", "美国", "Datainterfaces.com", "SI·VAR·经销商", "3000F Danville Blvd., Ste 300, Alamo, CA 94507", "888-959-3282", "northamerica-reseller"),
    ("北美", "美国", "Dorado Software", "SI·VAR·经销商", "PO Box 4701, El Dorado Hills, CA 95762", "916-673-1100", "northamerica-reseller"),
    ("北美", "美国", "ePLUS", "SI·VAR·经销商", "13595 Dulles Technology Drive, Herndon, VA 20171", "703-984-8400", "northamerica-reseller"),
    ("北美", "美国", "GDT", "SI·VAR·经销商", "999 Metromedia Pl, Dallas, TX 75247", "214-857-6997", "northamerica-reseller"),
    ("北美", "美国", "Hardware Nation", "SI·VAR·经销商/线上电商", "2390 Satellite Blvd, Suite P, Buford, GA 30518", "770-924-5847", "northamerica-reseller"),
    ("北美", "美国", "IWNetworks", "SI·VAR·经销商", "44235 Nobel Drive, Fremont, CA 94538", "(510) 248-4448", "northamerica-reseller"),
    ("北美", "美国", "KGPCo", "SI·VAR·经销商", "3305 Highway 60 West, Faribault, MN 55021", "1-800-328-5142", "northamerica-reseller"),
    ("北美", "美国", "Microcom Technologies", "SI·VAR·经销商", "26635 Agoura Road, Calabasas, CA 91302", "818-880-8008", "northamerica-reseller"),
    ("北美", "美国", "Myriad Supply", "SI·VAR·经销商/线上电商", "22 West 19th Street, New York, NY 10011", "866-725-1025", "northamerica-reseller"),
    ("北美", "美国", "PA Computer Connections", "SI·VAR·经销商", "789 East Pittsburgh Street, Greensburg, PA 15601", "724-838-7526", "northamerica-reseller"),
    ("北美", "美国", "Racklive", "SI·VAR·经销商", "48761 Kato Road, Fremont, CA 94538", "1-650-230-8060", "northamerica-reseller"),
    ("北美", "美国", "Redapt, Inc", "SI·VAR·经销商", "12226 134th Court NE, Redmond, WA 98052", "425-882-0400", "northamerica-reseller"),
    ("北美", "美国", "SHI", "SI·VAR·经销商", "290 Davidson Avenue, Somerset, NJ 08873", "888-764-8888", "northamerica-reseller"),
    ("北美", "美国", "Sotel Systems", "SI·VAR·经销商", "2465 Centerline Industrial Dr. Maryland Heights, MO 63043", "(866) 467-6835", "northamerica-reseller"),
    ("北美", "美国", "TESSCO", "SI·VAR·经销商", "11126 McCormick Road, Hunt Valley, MD 21031", "+1-800-472-7373", "northamerica-reseller"),
    ("北美", "美国", "Will Jaya", "SI·VAR·经销商", "19565 E. Walnut Dr. South, #B10, Rowland Heights, CA 91748", "(844) 996-0699", "northamerica-reseller"),
    ("北美", "美国", "WWT", "SI·VAR·经销商", "60 Weldon Parkway, St. Louis, Missouri 63043", "800-432-7008", "northamerica-reseller"),
    ("北美", "美国", "CDW", "线上电商", "Computershare P.O. Box 30170, College Station, TX 77842", "1-800-736-3001", "northamerica-online"),
    ("北美", "美国", "Insight", "线上电商", "6820 S. Harl Ave. Tempe, Arizona 85283", "+1-800-467-4448", "northamerica-online"),
    # ---------- 独联体 ----------
    ("独联体", "亚美尼亚", "META LLC", "分销商", "0031, Armenia, Erevan, 14 Ara Sargsysn Str., 3 floor", "+374-93003333", "cis-distributors"),
    ("独联体", "亚美尼亚", "Redinet CJSC", "分销商", "Azatutyan 24/7-24/8, 0014 Yerevan", "+374-10-249106", "cis-distributors"),
    ("独联体", "格鲁吉亚", "Romsat Georgia", "分销商", "4 Nodar Bokhua, Tbilisi", "+995-32-243 36 63", "cis-distributors"),
    ("独联体", "乌克兰", "ROMSAT", "分销商", "03142, Kyiv, Vasyl Stus str. 35-37", "+380-44-499 7969", "cis-distributors"),
    ("独联体", "白俄罗斯", "FIBERGET", "SI·VAR·经销商", "Брестская обл., Брестский р-н, Тельминский с/с, д.9", "+375-447-952-007", "cis-reseller"),
    ("独联体", "乌兹别克斯坦", "ООО NAGTECH", "SI·VAR·经销商", "52, 7th Sairam Street, Mirzo-Ulugbek District, Tashkent", "+998-55-508 0660", "cis-reseller"),
    ("拉丁美洲", "—", "（官网拉丁美洲名录当前无收录条目）", "—", "—", "—", "latin"),
]

# ============================================================
# Sheet 2 案例客户库（Edgecore 公开案例/新闻中的最终用户）
# 字段: 客户名称, 国家/地区, 行业/类型, 项目/用途, 涉及产品/方案, 来源
# ============================================================
CASES = [
    ("IPNexia", "比利时/欧洲", "电信/IDC", "数据中心 Spine-Leaf 自动化部署（VxLAN EVPN，部署时间从数小时缩到数分钟）", "AS7726-32X + AS7326-56X + Enterprise SONiC", "edge-core.com case-study 2026-01"),
    ("Deca Consulting", "比利时", "方案商/SI", "为 IPNexia 实施 Edgecore+SONiC 数据中心方案（也是 EMEA 渠道伙伴）", "AS7726-32X / AS7326-56X", "edge-core.com case-study"),
    ("Candela Technologies", "美国", "测试/实验室", "大规模园区网络测试，使用 Edgecore TIP OpenWiFi AP", "TIP OpenWiFi AP", "edge-core.com case-study 2022-12"),
    ("台南市校园网（合作中华电信）", "中国台湾", "教育/政府", "275 所学校 Wi-Fi 覆盖", "Edgecore Wi-Fi 方案", "edge-core.com case-study 2022-11"),
    ("Lang Son City（谅山市）", "越南", "政府/城市", "城市网络建设", "L3/L2+ 交换机", "edge-core.com case-study 2020-10"),
    ("LINX（伦敦互联网交换中心）", "英国", "IXP/运营商", "LON2/MAN LAN 升级，开放网络迁移", "Edgecore 开放交换机 + IP Infusion OcNOS", "edge-core.com press-release 2021/2024"),
    ("NCTU（台湾交通大学）", "中国台湾", "教育/科研", "全球 OpenFlow SDN 骨干", "AS4610-54T / AS4610 系列", "edge-core.com case-study 2016"),
    ("Clemson University", "美国", "教育", "Big Cloud Fabric + Edgecore", "Edgecore 开放交换机 + Big Switch", "edge-core.com case"),
    ("UTSA（德州大学圣安东尼奥）", "美国", "教育/科研", "Cloud & Big Data Lab 10G/40G 网络", "AS6712-32X / AS5712-54X + Cumulus", "edge-core.com case"),
    ("NETAS", "土耳其", "集成商/政府项目", "4,000 所学校无线网络，92,000 AP + 4,026 AC", "EWS 系列无线控制器/AP", "Edgecore 产品概览 2018"),
    ("ITM University Gurgaon", "印度", "教育", "校园管理型网络", "Edgecore 有线+无线", "edge-core.com case"),
    ("Dubai Municipality（迪拜市政府）", "阿联酋", "政府", "网络建设 CapEx 优化", "Edgecore 开放网络", "featuredcustomers.com"),
    ("MicroAds", "以色列", "互联网企业", "Cumulus + Edgecore 开放交换机", "Edgecore 开放交换机", "featuredcustomers.com"),
    ("CloudLabs（Ciii）", "美国", "云实验室", "BCF+OpenStack 验证环境", "AS6700-32X / AS5710-54X", "edge-core.com case"),
    ("Scott Data", "美国", "数据中心", "开放网络替代传统厂商", "Edgecore + UfiSpace + Celestica + OcNOS", "ipinfusion.com casestudies"),
    ("Amplex", "美国", "ISP/WISP", "聚合层扩容", "Edgecore + OcNOS", "ipinfusion.com casestudies"),
    ("AnschlussWerk", "德国", "ISP", "300G CRS + 2.4T 聚合路由", "Edgecore + IP Infusion Aggregation Router", "ipinfusion.com casestudies"),
    ("Asia Pacific Telecom（亚太电信）", "中国台湾", "运营商", "开放网络方案", "Edgecore + IP Infusion", "ipinfusion.com casestudies"),
    ("Haefele Connect", "美国", "ISP", "L3 聚合（原 Cisco/Juniper 替代）", "Edgecore + OcNOS", "ipinfusion.com casestudies"),
    ("Nextlink Internet", "美国", "ISP（约10万用户/11州）", "中间 mile 传输 + 站点路由 + 核心 DC", "Edgecore + OcNOS-SP", "ipinfusion.com"),
    ("SK Telecom（SK电讯）", "韩国", "运营商", "IPoDWDM PoC（IOWN 全光网络）", "Edgecore 白盒 + 400G OpenZR+", "ipinfusion.com"),
    ("Indio Networks", "印度", "OEM/MSP 平台商", "OpenWiFi + OpenLAN 量产集成，面向 EMEA MSP/电信", "OpenWiFi AP + OLS 交换机", "wifi.edge-core.com 2026-01"),
    ("City of Hoover", "美国", "政府/城市", "城市网络升级", "AS5812-54X / AS4610-54T + Pica8 PICOS", "edge-core.com case"),
    ("Dojo Networks", "美国", "ISP/MDU", "MDU 间传输改造（替代 Cisco）", "Edgecore + OcNOS", "ipinfusion.com casestudies"),
    ("ASOM-Net", "（东南亚）", "ISP（7.5万用户）", "IPoDWDM 开放网络扩容", "Edgecore 白盒 + 400G ZR+ + Smartoptics", "ipinfusion.com casestudies"),
    ("Prosoluce", "法国", "ISP/MSP", "100G EVPN-VXLAN 核心升级", "Edgecore + OcNOS（Pine Networks 集成）", "ipinfusion.com casestudies"),
    ("ITandTEL", "奥地利", "运营商/ISP", "主权 MPLS 骨干现代化", "Edgecore + OcNOS 400G ZR+", "ipinfusion.com"),
    ("MetaLINK Technologies", "美国", "ISP", "聚合层（与 MikroTik/Arista 混合组网）", "Edgecore + UfiSpace + OcNOS", "ipinfusion.com casestudies"),
    ("HyperVerge", "印度", "AI 平台商", "高带宽低时延数据中心", "Edgecore 数据中心方案", "edge-core.com press-release 2026-06"),
    ("Submer（MoU）", "西班牙/中东非洲", "AI 基础设施", "AI-ready 数据中心合作备忘录", "Edgecore 数据中心", "edge-core.com media-report 2026-09"),
]

# ============================================================
# Sheet 3 目标客户评估（按我方画像打分：品牌商/方案商 > 项目型/技术型 > 分销电商 > 大集团=低）
# 字段: 公司, 国家/地区, 我方目标类型, 匹配理由, 切入点建议, 优先级(1-5,1最高)
# ============================================================
TARGETS = [
    ("Deca Consulting", "比利时", "品牌商/方案商(SI)", "技术型 SI，做 SONiC/Edgecore 深度集成，客户群为欧洲 IDC/运营商", "深度定制 OEM/ODM、CLI/MIB 支持；项目型报价可让利", 1),
    ("Pine Networks", "法国", "品牌商/方案商(SI)", "ISP 集成商，做 100G EVPN-VXLAN 核心项目（Prosoluce）", "汇聚/核心层 CENTEC 方案对标，项目联合投标", 1),
    ("STORDIS GmbH / STORDIS Limited", "德国/英国", "分销商(开放网络专业)", "开放网络专业分销，技术能力强，长期经营 Edgecore/Cumulus 生态", "白牌/OEM 供货、快速交期、芯片库存保障", 1),
    ("Circle B", "荷兰", "分销商/方案商", "荷兰开放网络生态活跃商，OCP 社区关联", "OEM/ODM 贴牌 + 技术支持", 1),
    ("Cell-Core Industrial Technologies Ltd", "匈牙利", "品牌商/方案商", "工业以太网技术公司，工业交换机需求与我方工业线高度重合", "工业 PoE/工业管理型 OEM，宽温方案", 1),
    ("Kontron, d.o.o.", "斯洛文尼亚", "品牌商/方案商(工业)", "工业计算品牌 Kontron 旗下，工业/嵌入式场景", "工业交换机 ODM/OEM 深度定制", 1),
    ("FIBERGET", "白俄罗斯", "分销/集成(独联体)", "独联体市场，价格敏感，习惯亚洲供应链", "高性价比 L2+/PoE，交期优势", 1),
    ("ООО NAGTECH", "乌兹别克斯坦", "分销/集成(独联体)", "中亚新兴市场进口商", "现货+长期供货，价格灵活", 1),
    ("NETMARK DISTRIBUTION", "越南", "分销商(东南亚)", "越南分销，毗邻中国供应链，有进口习惯", "CCTV/PoE 现货，OEM 贴牌", 1),
    ("PAVANA TECHNOLOGIES", "越南", "分销商(东南亚)", "越南分销，安防/园区项目", "CCTV 交换机方案，价格让利", 1),
    ("SSS Vietnam Joint Stock Company", "越南", "分销商(东南亚)", "越南系统集成/分销", "项目型报价，PoE++/ERPS 功能卖点", 1),
    ("Richman Informatics", "孟加拉国", "分销商(南亚)", "孟加拉 IT 分销，价格敏感市场", "高性价比 L2+，长期供货", 1),
    ("Mekong Link Co. LTD", "柬埔寨", "分销商(东南亚)", "柬埔寨新兴分销", "入门级 L2/PoE 现货", 1),
    ("Green Cube Technologies Pvt. Ltd.", "尼泊尔", "分销商(南亚)", "尼泊尔/南亚小市场分销", "小批量+快速交期", 1),
    ("Positron Multiverse Co., Ltd", "柬埔寨", "SI/经销商", "柬埔寨 SI", "项目配合，方案可行性和价格让利", 2),
    ("PT. Gwen Tekno Pratama / PT Trinet Prima Solusi", "印度尼西亚", "SI/经销商", "印尼 SI，非巨头，项目体量适中", "CCTV/园区 PoE 方案", 2),
    ("Mart Networks（Kenya/Tanzania/Uganda/Rwanda）", "东非四国", "分销商(非洲)", "东非分销网络，新兴市场价格敏感", "性价比+长期供货+OEM 贴牌", 1),
    ("Soliton Telmec Limited", "肯尼亚", "SI/经销商", "肯尼亚 SI", "项目型跟进", 2),
    ("ODDnet", "摩洛哥", "SI/经销商", "北非法语区 SI", "项目型跟进", 2),
    ("Miro Distribution", "南非", "分销商(非洲)", "南非分销", "价格+供货稳定性", 2),
    ("IntruGrid LLP / NETSOFT SOLUTIONS / STARCOM Technologies", "巴基斯坦", "分销/SI(南亚)", "巴基斯坦三家，价格敏感、进口活跃", "高性价比 PoE/L2+，灵活付款方式可谈", 1),
    ("MBUZZ（沙特/迪拜）", "沙特/阿联酋", "分销商(中东)", "中东分销，安防/城市场景多", "CCTV/PoE 方案，项目投标支持", 2),
    ("Evollabs Tech FZ-LLC", "阿联酋", "分销/SI(中东)", "迪拜自由区，转口贸易活跃", "OEM/贴牌+快速交期", 1),
    ("Core Technologies LLC", "阿联酋", "SI(中东)", "沙迦自由区", "项目型小单", 2),
    ("Khushi Communications / Micromap / Ravi and Singh 等", "印度", "SI/经销商(南亚)", "印度中小型 SI 群体（多家），项目制采购", "项目报价让利、技术响应速度", 2),
    ("Saimaa Technologies LLP / Sheeltron Digital", "印度", "分销商(南亚)", "孟买/班加罗尔分销", "价格+交期", 2),
    ("BANBROS COMMERCIAL., INC.", "菲律宾", "分销商(东南亚)", "菲律宾老牌分销", "CCTV/PoE，OEM", 2),
    ("C. F. KING Enterprise", "文莱", "SI/经销商", "小市场独家型商", "长期跟进池", 3),
    ("DataOne / Tech Trad / VEMAX / VESC", "马来西亚", "SI/经销商", "马来 SI 群体", "项目型跟进", 2),
    ("AHNNET / AI TECH / LANOASIS / NEWGENS 等 韩国 SI 群体", "韩国", "SI/经销商(东北亚)", "韩国 SI 群体（约10家），技术要求高", "注意 KC 认证缺失——仅接无强制认证项目；深度定制可谈", 3),
    ("M2M Enterprise", "英国", "SI/经销商", "英国 M2M/物联网方向，规模适中", "OEM/物联网配套交换机", 2),
    ("Utopia Technology / Vesper Technologies", "英国", "SI/经销商", "英国中小型技术商", "技术型跟进（CLI/MIB）", 2),
    ("Xentech B.V. / Distri X BV / FiberUnlimited", "荷兰", "分销/SI", "荷兰中小渠道群体", "电商/分销现货供应", 2),
    ("Datanet Systems", "罗马尼亚", "SI/经销商", "罗马尼亚系统集成商", "项目型", 2),
    ("Upstream ICT Alliance", "塞尔维亚", "SI/经销商", "塞尔维亚/巴尔干", "价格敏感市场", 2),
    ("Aero-IT distribucija d.o.o.", "斯洛文尼亚", "分销商", "巴尔干分销", "现货+价格", 2),
    ("Meta LLC / Redinet CJSC / Romsat Georgia / ROMSAT", "亚美尼亚/格鲁吉亚/乌克兰", "分销商(独联体)", "高加索/乌克兰渠道", "价格+供货", 2),
    ("Wisi Spain / Telcaria", "西班牙", "SI/经销商", "西班牙/南欧", "项目型跟进", 2),
    ("Direktronik / Vinnergi", "瑞典", "分销/SI", "北欧渠道", "工业/ISP 线切入", 2),
    ("E.C.I. NETWORKS / FONEX / info-logic / Planiselect", "加拿大", "分销商(北美)", "加拿大分销群体（法语区为主）", "ISP/CCTV 线，项目型", 3),
    ("Nine-One-One Communication Supply", "加拿大", "SI/经销商", "加拿大应急通信方向（911）", "行业项目，避开超大集团", 2),
    ("Blue Core / Cambridge Computer / Myriad Supply / Hardware Nation", "美国", "SI/电商(北美)", "美国中小型技术渠道/电商", "现货+电商供货", 2),
    ("Will Jaya / Sotel Systems / PA Computer Connections", "美国", "SI/经销商", "美国区域型小 SI", "小项目/小批量", 2),
    ("TD SYNNEX / Avnet / Tech Data / Anixter / WWT / CDW / SHI / ePLUS / Insight", "美国", "大型分销/电商", "超大集团，按我方策略难拿下", "仅作品牌背书参考，不作为主攻", 5),
    ("Exclusive Networks", "荷兰", "大型分销", "欧洲大型安全/网络分销", "同上，低优先", 5),
    ("ASBIS（塞浦路斯/波兰/中东）", "欧洲/中东", "大型分销", "EMEA 大型 VAD", "低优先，可关注其细分需求", 4),
    ("ECOM/技术型电商：Colfax Direct、CDW、Insight", "美国", "电商", "线上标品渠道", "现货标品+快速交期，可跟", 3),
    ("APRESIA / ITOCHU / MACNICA / 三井情报 / NEC NSI", "日本", "大型商社/SI", "日本大手，认证门槛高（PSE 等）", "仅长期跟进池", 4),
    ("FPT IS / NDC / NETCOM", "越南", "SI(东南亚)", "越南大 SI，项目体量中等偏大", "选择性跟进，项目制报价", 2),
    ("ScaleIL LTD", "以色列", "SI/经销商", "以色列技术市场", "技术型定制，长期跟进", 2),
    ("Astute Electronics / Telent Technology Services", "英国", "SI(大型)", "英国较大 SI", "选择性跟进", 3),
    ("Active Solution & Systems S.r.l.", "意大利", "SI", "意大利 SI", "项目型跟进", 3),
    ("LaserNetworks Kft", "匈牙利", "SI", "匈牙利网络商", "价格+项目", 2),
    ("primeLine / KTI / DELTA / ADN / Xantaro", "德国", "SI/分销(德国)", "德国技术渠道群体", "技术型客户（CLI/MIB）优先", 2),
    ("Fionis GmbH", "奥地利", "SI", "奥地利 SI", "项目型", 3),
    ("MCS IT Distribution / ASBIS Cyprus", "塞浦路斯", "分销(东地中海)", "转口/区域分销", "价格+供货", 3),
    ("PROFIcomms s.r.o.", "捷克", "SI/分销(中东欧)", "捷克渠道", "中东欧价格敏感市场", 2),
    ("Allnet GmbH / ALLNET France", "德国/法国", "分销(西欧)", "Allnet 体系", "中优先，看细分产品线", 3),
    ("Syserso Networks GmbH", "德国", "SI", "德国 SI", "项目型", 3),
    ("Electronic Product Services（多地）", "德国/爱尔兰/罗马尼亚/英国/印度", "分销(国际网络)", "EPS 全球网络（Edgecore 核心分销；按 2026-10-18 指令不含中国大陆公司）", "了解其需求结构，作为行业情报源；合作空间有限", 4),
]

# ============================================================
# Sheet 5 重点目标联系方式（公开信息补充，2026-10-18 采集）
# 字段: 公司, 国家/地区, 网站, 邮箱, 电话, 备注
# ============================================================
CONTACTS = [
    ("ООО NAGTECH (NAG Uzbekistan)", "乌兹别克斯坦", "shop.nag.uz / nagtech 旗下", "sales@nag.uz", "+998 55 508-06-60", "自有网店 1.5 万 SKU；Volza 显示有 Cisco 等进口记录，进口熟手"),
    ("Deca Consulting", "比利时", "deca-consulting.be", "（官网表单）", "+32 16 89 87 71", "厂商中立 SI：Cisco/Edgecore/Palo Alto/SONiC；IPNexia 数据中心案例主导"),
    ("STORDIS GmbH", "德国", "stordis.com", "info@stordis.com", "+49 711 342 158 0", "欧洲开放网络专家，11-50 人，2007 成立；参与 IPNexia 案例"),
    ("Circle B", "荷兰", "circleb.eu", "info@circleb.eu", "+31 85 800 0430", "Taurus 集团旗下，OCP/开放硬件，51-200 人"),
    ("Pine Networks", "法国", "（官网/LinkedIn 可查）", "（官网表单）", "+33 1 88 94 77 04", "ISP 集成商，Prosoluce 100G EVPN-VXLAN 项目集成方"),
    ("MART NETWORKS（Kenya/Tanzania/Uganda/Rwanda）", "东非四国", "（官网/LinkedIn 可查）", "（官网表单）", "+254 20 5135200 (KE)", "东非分销网络"),
    ("FIBERGET", "白俄罗斯", "（官网/名录可查）", "（电话联系）", "+375 447 952-007", "独联体分销/集成"),
    ("NETMARK DISTRIBUTION", "越南", "（官网可查）", "（电话联系）", "(84) 906 814 510", "越南安防/园区分销"),
    ("PAVANA TECHNOLOGIES", "越南", "（官网可查）", "（电话联系）", "(+84) 8 5333 5995", "越南河内分销"),
    ("IntruGrid LLP", "巴基斯坦", "（官网可查）", "（电话联系）", "+92 333 5156428", "巴基斯坦分销/SI"),
    ("Cell-Core Industrial Technologies Ltd", "匈牙利", "（官网可查）", "（电话联系）", "+36 30 589 0788", "工业以太网技术公司"),
    # ⚠️ 2026-10-18 用户指令：客户库不含中国大陆公司（HK/台湾/澳门 OK），原 大陆公司条目已删
]

# ============================================================
# Sheet 4 数据说明
# ============================================================
NOTES = [
    ("数据来源", "Edgecore 官网 Where-to-Buy 全球名录（asia/indian/emea/northamerica/cis distributors & reseller & online 页面），2026-10-18 采集"),
    ("数据来源", "Edgecore 官方案例页 case-study / case-inquiry、新闻稿、IP Infusion 客户故事等公开资料，2026-10-18 采集"),
    ("处理范式", "与 mikrotik-info 仓库同等方式：产品/价格库 + 客户/渠道研究 + 出货地分析 + 价值分析；mikrotik-info 仅只读参考，未复制其内容"),
    ("优先级定义", "1=优先跟进（项目型/技术型/新兴市场进口商，匹配我方 OEM/ODM 与性价比卖点）；2=可跟；3=长期池；4=情报/背书用；5=大集团低优先"),
    ("使用方法", "结合《Edgecore-vs-交换机价值分析.md》《Edgecore商业L2+主要出货地.md》制定开发信与报价策略"),
    ("注意", "渠道名录来自公开页面，可能随 Edgecore 官网更新变动；联系前建议核对官网最新信息"),
    ("采集时间", COLLECT_TIME),
]


def export(filename="Edgecore客户数据库.xlsx"):
    wb = openpyxl.Workbook()

    HDR_FILL = PatternFill("solid", fgColor="1F4E78")
    HDR_FONT = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
    CELL_FONT = Font(name="Calibri", size=9)
    THIN = Border(*[Side(style="thin", color="BFBFBF")] * 4)

    def style_sheet(ws, headers, rows, widths):
        ws.append(headers)
        for c in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=c)
            cell.fill = HDR_FILL
            cell.font = HDR_FONT
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            ws.column_dimensions[get_column_letter(c)].width = widths[c - 1]
        for r in rows:
            ws.append(list(r))
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, max_col=len(headers)):
            for cell in row:
                cell.font = CELL_FONT
                cell.alignment = Alignment(vertical="top", wrap_text=True)
                cell.border = THIN
        ws.freeze_panes = "A2"

    # Sheet 1
    ws1 = wb.active
    ws1.title = "渠道伙伴库"
    style_sheet(
        ws1,
        ["序号", "大区", "国家/地区", "公司名称", "渠道类型", "地址", "电话", "来源页", "采集时间"],
        [(i, *p, COLLECT_TIME) for i, p in enumerate(PARTNERS, 1)],
        [5, 10, 12, 38, 14, 52, 18, 22, 18],
    )

    # Sheet 2
    ws2 = wb.create_sheet("案例客户库")
    style_sheet(
        ws2,
        ["序号", "客户名称", "国家/地区", "行业/类型", "项目/用途", "涉及产品/方案", "来源", "采集时间"],
        [(i, *c, COLLECT_TIME) for i, c in enumerate(CASES, 1)],
        [5, 30, 14, 14, 44, 36, 26, 18],
    )

    # Sheet 3
    ws3 = wb.create_sheet("目标客户评估")
    style_sheet(
        ws3,
        ["序号", "公司/群体", "国家/地区", "我方目标类型", "匹配理由", "切入点建议", "优先级(1最高)", "跟进状态"],
        [(i, *t, "未联系") for i, t in enumerate(TARGETS, 1)],
        [5, 42, 18, 18, 44, 36, 10, 10],
    )
    for row in ws3.iter_rows(min_row=2, max_row=ws3.max_row, min_col=7, max_col=7):
        for cell in row:
            if cell.value == 1:
                cell.fill = PatternFill("solid", fgColor="FFC7CE")
                cell.font = Font(size=9, bold=True, color="9C0006")
            elif cell.value == 2:
                cell.fill = PatternFill("solid", fgColor="FFEB9C")

    # Sheet 5
    ws5 = wb.create_sheet("重点目标联系方式")
    style_sheet(
        ws5,
        ["序号", "公司", "国家/地区", "网站", "邮箱", "电话", "备注"],
        [(i, *c) for i, c in enumerate(CONTACTS, 1)],
        [5, 42, 14, 28, 22, 22, 52],
    )

    # Sheet 4 数据说明（放最后）
    ws4 = wb.create_sheet("数据说明")
    style_sheet(ws4, ["项目", "说明"], NOTES, [14, 100])

    wb.save(filename)
    print(f"已生成 {filename}")
    print(f"  渠道伙伴: {len(PARTNERS)} 条 | 案例客户: {len(CASES)} 条 | 目标评估: {len(TARGETS)} 条")


if __name__ == "__main__":
    export()
