import Giztop
import DataBase

# Assemble list of products to get data


products = ['https://www.giztop.com/oppo-find-x6.html',
'https://www.giztop.com/nubia-z50-ultra.html',
'https://www.giztop.com/oppo-find-x6-pro.html',
'https://www.giztop.com/iqoo-z7.html',
'https://www.giztop.com/oneplus-11-jupiter-rock-edition.html',
'https://www.giztop.com/meizu-20-pro.html',
'https://www.giztop.com/meizu-20.html',
'https://www.giztop.com/meizu-20-infinity.html',
'https://www.giztop.com/asus-rog-phone-7-pro.html',
'https://www.giztop.com/oneplus-ace-2-genshin-impact-limited-edition.html',
'https://www.giztop.com/vivo-x-fold-2.html',
'https://www.giztop.com/vivo-x-flip.html',
'https://www.giztop.com/lenovo-xiaoxin-mini-pc.html',
'https://www.giztop.com/red-magic-8-pro-plus-transformers-16gb-512gb.html',
'https://www.giztop.com/realme-11-pro-plus.html',
'https://www.giztop.com/realme-11-pro.html',
'https://www.giztop.com/realme-11.html',
'https://www.giztop.com/asus-rog-ally-z1-extreme.html',
'https://www.giztop.com/iqoo-neo-8.html',
'https://www.giztop.com/iqoo-neo-8-pro.html',
'https://www.giztop.com/iqoo-pad.html',
'https://www.giztop.com/xiaomi-civi-3.html',
'https://www.giztop.com/oppo-reno-10.html',
'https://www.giztop.com/oppo-reno-10-pro.html',
'https://www.giztop.com/oppo-reno-10-pro-plus.html',
'https://www.giztop.com/redmi-note-12t-pro.html',
'https://www.giztop.com/motorola-razr-40.html',
'https://www.giztop.com/motorola-razr-40-ultra.html',
'https://www.giztop.com/vivo-x90s.html',
'https://www.giztop.com/redmi-note-12r.html',
'https://www.giztop.com/oppo-reno-10-pro-plus-purple-16gb-512gb-1.html',
'https://www.giztop.com/xiaomi-civi-3-almost-new-15-off-gold-12gb-256gb.html',
'https://www.giztop.com/iqoo-11s.html',
'https://www.giztop.com/red-magic-8s-pro.html',
'https://www.giztop.com/red-magic-8s-pro-plus.html',
'https://www.giztop.com/redmi-note-12-pro.html',
'https://www.giztop.com/redmi-note-12-pro-plus.html',
'https://www.giztop.com/redmi-note-12-explorer.html',
'https://www.giztop.com/realme-10.html',
'https://www.giztop.com/vivo-x90.html',
'https://www.giztop.com/vivo-x90-pro.html',
'https://www.giztop.com/vivo-x90-pro-plus.html',
'https://www.giztop.com/realme-10-pro-plus.html',
'https://www.giztop.com/realme-10-pro.html',
'https://www.giztop.com/oppo-reno-9.html',
'https://www.giztop.com/oppo-reno-9-pro.html',
'https://www.giztop.com/oppo-reno-9-pro-plus.html',
'https://www.giztop.com/iqoo-neo-7-se.html',
'https://www.giztop.com/iqoo-11.html',
'https://www.giztop.com/oneplus-11.html',
'https://www.giztop.com/iqoo-11-pro.html',
'https://www.giztop.com/rog-phone-6-diablo-immortal-edition.html',
'https://www.giztop.com/nubia-z50.html',
'https://www.giztop.com/vivo-s16.html',
'https://www.giztop.com/vivo-s16-pro.html',
'https://www.giztop.com/vivo-s16e.html',
'https://www.giztop.com/red-magic-8-pro.html',
'https://www.giztop.com/red-magic-8-pro-plus.html',
'https://www.giztop.com/redmi-k60-pro.html',
'https://www.giztop.com/redmi-k60.html',
'https://www.giztop.com/redmi-note-12-pro-speed-edition.html',
'https://www.giztop.com/redmi-k60-champion-edition.html',
'https://www.giztop.com/lenovo-yoga-paper-e-ink-tablet.html',
'https://www.giztop.com/realme-gt-neo-5.html',
'https://www.giztop.com/oneplus-ace-2.html',
'https://www.giztop.com/zte-axon-40-pro-5g.html',
'https://www.giztop.com/oneplus-ace-racing-edition.html',
'https://www.giztop.com/realme-gt-neo-3-naruto.html',
'https://www.giztop.com/realme-pad-x.html',
'https://www.giztop.com/xiaomi-12s.html',
'https://www.giztop.com/xiaomi-12s-pro.html',
'https://www.giztop.com/xiaomi-12s-ultra.html',
'https://www.giztop.com/nubia-red-magic-7s.html',
'https://www.giztop.com/realme-gt-2-master-explorer-edition.html',
'https://www.giztop.com/iqoo-10.html',
'https://www.giztop.com/nubia-z40s-pro-120w.html',
'https://www.giztop.com/nubia-z40s-pro-spirit-cage-edition.html',
'https://www.giztop.com/red-magic-7s-pro-transformers-edition.html',
'https://www.giztop.com/oneplus-ace-pro.html',
'https://www.giztop.com/moto-razr-2022.html',
'https://www.giztop.com/lenovo-legion-y70.html',
'https://www.giztop.com/rog-phone-6d.html',
'https://www.giztop.com/rog-phone-6d-ultimate.html',
'https://www.giztop.com/vivo-x-fold-plus.html',
'https://www.giztop.com/iqoo-neo-7.html',
'https://www.giztop.com/oppo-find-n.html',
'https://www.giztop.com/iqoo-neo-5s.html',
'https://www.giztop.com/realme-gt-2.html',
'https://www.giztop.com/nubia-red-magic-7-pro.html',
'https://www.giztop.com/oneplus-10-pro-white-edition.html',
'https://www.giztop.com/oppo-find-x5.html',
'https://www.giztop.com/oppo-find-x5-pro.html',
'https://www.giztop.com/oppo-find-x5-pro-dimensity-9000.html',
'https://www.giztop.com/nubia-z40-pro-outcast-limited-edition.html',
'https://www.giztop.com/nubia-z40-pro-magnetic-charging-edition.html',
'https://www.giztop.com/realme-gt-neo-3-80w.html',
'https://www.giztop.com/iqoo-u5x-4g.html',
'https://www.giztop.com/red-magic-7-pro-transparent-12gb-256gb.html',
'https://www.giztop.com/realme-q5-pro.html',
'https://www.giztop.com/realme-q5.html',
'https://www.giztop.com/realme-q5i.html',
'https://www.giztop.com/oneplus-ace.html',
'https://www.giztop.com/red-magic-7-transformers-edition.html',
'https://www.giztop.com/red-magic-7-pro-transformers-edition.html',
'https://www.giztop.com/redmi-note-12-turbo-harry-potter-edition.html',
'https://www.giztop.com/realme-gt-neo-5-240w.html',
'https://www.giztop.com/oneplus-ace-2v.html',
'https://www.giztop.com/xiaomi-civi-3-disney-limited-edition.html',
'https://www.giztop.com/asus-rog-phone-7.html',
'https://www.giztop.com/redmi-note-12-turbo.html',
'https://www.giztop.com/vivo-y55s-5g.html',
'https://www.giztop.com/vivo-x70t.html',
'https://www.giztop.com/xiaomi-mi-11-lite-5g-ve.html',
'https://www.giztop.com/coolpad-cool-20-pro.html',
'https://www.giztop.com/realme-gt-neo-2-global-rom.html',
'https://www.giztop.com/vivo-t1x.html',
'https://www.giztop.com/vivo-t1.html',
'https://www.giztop.com/iqoo-z5x.html',
'https://www.giztop.com/iqoo-z5.html',
'https://www.giztop.com/meizu-18x.html',
'https://www.giztop.com/meizu-18s-pro.html',
'https://www.giztop.com/meizu-18s.html',
'https://www.giztop.com/realme-gt-neo-2.html',
'https://www.giztop.com/vivo-x70-pro-plus-5g.html',
'https://www.giztop.com/vivo-x70-pro-5g.html',
'https://www.giztop.com/iqoo-8-pro.html',
'https://www.giztop.com/iqoo-8.html',
'https://www.giztop.com/asus-rog-phone-6.html',
'https://www.giztop.com/rog-phone-5s.html',
'https://www.giztop.com/vivo-s10-pro-5g.html',
'https://www.giztop.com/vivo-y76s-5g.html',
'https://www.giztop.com/vivo-y53s-5g.html',
'https://www.giztop.com/vivo-x60-curved-screen-edition.html',
'https://www.giztop.com/vivo-y70t-5g.html',
'https://www.giztop.com/oppo-a93-5g-aurora-8gb-128gb.html',
'https://www.giztop.com/iqoo-z3-5g.html',
'https://www.giztop.com/iqoo-u3x-5g.html',
'https://www.giztop.com/vivo-y30g.html',
'https://www.giztop.com/vivo-y31s-5g-standard-edition.html',
'https://www.giztop.com/rog-phone-5-pro.html',
'https://www.giztop.com/meizu-18-5g.html',
'https://www.giztop.com/vivo-s7t-5g.html',
'https://www.giztop.com/vivo-s9-5g.html',
'https://www.giztop.com/vivo-s7e-5g-vitality-edition.html',
'https://www.giztop.com/vivo-y31s-5g.html',
'https://www.giztop.com/iqoo-7.html',
'https://www.giztop.com/vivo-x60-pro-5g.html',
'https://www.giztop.com/vivo-x60-5g.html',
'https://www.giztop.com/iqoo-u3.html',
'https://www.giztop.com/vivo-iqoo-u1x.html',
'https://www.giztop.com/vivo-y3s.html',
'https://www.giztop.com/vivo-y30.html',
'https://www.giztop.com/vivo-s7e-5g-phone.html',
'https://www.giztop.com/oppo-a72-5g.html',
'https://www.giztop.com/oppo-a32.html',
'https://www.giztop.com/oppo-reno4-se.html',
'https://www.giztop.com/zte-axon-20-5g.html',
'https://www.giztop.com/iqoo-5-pro.html',
'https://www.giztop.com/iqoo-5-5g.html',
'https://www.giztop.com/vivo-s7.html',
'https://www.giztop.com/vivo-y50.html',
'https://www.giztop.com/vivo-x50-pro-plus-5g.html',
'https://www.giztop.com/vivo-y70s-5g.html',
'https://www.giztop.com/vivo-z5x-712.html',
'https://www.giztop.com/vivo-x50-pro-5g.html',
'https://www.giztop.com/vivo-x50-5g.html',
'https://www.giztop.com/meizu-17-aircraft-carrier-limited-edition.html',
'https://www.giztop.com/vivo-iqoo-neo-3-5g.html',
'https://www.giztop.com/meizu-17-pro.html',
'https://www.giztop.com/vivo-s6-5g.html',
'https://www.giztop.com/vivo-z6-5g.html',
'https://www.giztop.com/oppo-find-n2.html',
'https://www.giztop.com/oppo-find-n2-flip.html',
'https://www.giztop.com/vivo-x-note.html',
'https://www.giztop.com/vivo-y77.html',
'https://www.giztop.com/vivo-y33s-5g.html',
'https://www.giztop.com/nubia-red-magic-7.html',
'https://www.giztop.com/moto-edge-s30-champion-edition.html',
'https://www.giztop.com/moto-edge-x30-champion-edition.html',
'https://www.giztop.com/motorola-moto-x40.html',
'https://www.giztop.com/moto-x30-pro.html',
'https://www.giztop.com/vivo-t2x.html',
'https://www.giztop.com/iqoo-z6.html',
'https://www.giztop.com/vivo-s12.html',
]
 
# structure the data 
product_data_list = []
for product in products:
    product_data = Giztop.get_product_info(product)
    product_data_list.append(product_data)

# insert data into database 
conn = DataBase.connectDb()
DataBase.giztopSiteToDb(conn,product_data_list) 