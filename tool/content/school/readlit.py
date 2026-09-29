"""O‘qish va adabiyot savollari uchun umumiy ma’lumotlar: maqollar, topishmoqlar, asar va mualliflar.

Maqollar — xalq og‘zaki ijodi (umumxalq mulki). Topishmoqlar va hikoyalar — o‘zimiz yozgan.
Asar–muallif juftlari faqat umumma’lum, darsliklarda keltiriladigan faktlardan olingan.
"""

# (birinchi qism, ikkinchi qism, mavzu)
PROVERBS = [
    ("Birlashgan o‘zar,", "birlashmagan to‘zar.", "Birlik va hamjihatlik"),
    ("Sabr tagi —", "sariq oltin.", "Sabr-toqat"),
    ("Hunar —", "hunardan unar.", "Hunar o‘rganish"),
    ("Olim bo‘lsang,", "olam seniki.", "Ilm olish"),
    ("Ilm olish —", "igna bilan quduq qazish.", "Ilm olish"),
    ("Yaxshi so‘z — jon ozig‘i,", "yomon so‘z — bosh qozig‘i.", "So‘z odobi"),
    ("Ona yurting —", "oltin beshiging.", "Vatanni sevish"),
    ("Kattaga hurmatda,", "kichikka izzatda bo‘l.", "Hurmat va odob"),
    ("Bir kun tuz ichgan joyga", "qirq kun salom ber.", "Minnatdorlik"),
    ("Tomchi-tomchi", "ko‘l bo‘lur.", "Tejamkorlik"),
    ("Aql yoshda emas,", "boshda.", "Aql-idrok"),
    ("Bilagi zo‘r birni yiqar,", "bilimi zo‘r mingni yiqar.", "Ilm olish"),
    ("Qush uyasida", "ko‘rganini qiladi.", "Oila tarbiyasi"),
    ("Do‘stsiz boshim —", "tuzsiz oshim.", "Do‘stlik"),
    ("Avval o‘yla,", "keyin so‘yla.", "So‘z odobi"),
    ("Ko‘z qo‘rqoq,", "qo‘l botir.", "Mehnat va jasorat"),
    ("Qo‘li ochiqning", "yo‘li ochiq.", "Saxiylik"),
    ("Otang bolasi bo‘lma,", "odam bolasi bo‘l.", "Insoniylik"),
    ("Yaxshidan bog‘ qoladi,", "yomondan — dog‘.", "Yaxshilik"),
    ("O‘zga yurtda shoh bo‘lguncha,", "o‘z yurtingda gado bo‘l.", "Vatanni sevish"),
]

# (topishmoq, javob, [chalg‘ituvchilar]) — o‘zimiz tuzgan ta’rifiy topishmoqlar
RIDDLES = [
    ("Tunda uxlamas, sichqon poylar, mo‘ylovi bor, “miyov” deydi.", "Mushuk", ["It", "Quyon", "Tovuq"]),
    ("Oyog‘i yo‘q — yuradi, tili yo‘q — vaqtni aytadi.", "Soat", ["Kitob", "Qalam", "Radio"]),
    ("Tishi bor — tishlamaydi, sochni tartibga soladi.", "Taroq", ["Qaychi", "Arra", "Vilka"]),
    ("Varaqlari bor — daraxt emas, gapirmaydi, lekin ko‘p narsani o‘rgatadi.", "Kitob", ["Daftar", "Televizor", "Gazeta"]),
    ("Osmonda yetti rangli ko‘prik, yomg‘irdan keyin paydo bo‘ladi.", "Kamalak", ["Bulut", "Chaqmoq", "Quyosh"]),
    ("Qishda ham yashil, ignasi bor — lekin tikuvchi emas.", "Archa", ["Terak", "Tipratikan", "Olma daraxti"]),
    ("Suvda suzadi, jabrasi bor, tangachasi yaltiraydi.", "Baliq", ["Baqa", "O‘rdak", "Delfin"]),
    ("Uyni qo‘riqlaydi, begonani ko‘rsa vovullaydi.", "It", ["Mushuk", "Echki", "Qo‘y"]),
    ("Bulutdan tomchi-tomchi tushib, yerni sug‘oradi.", "Yomg‘ir", ["Qor", "Shamol", "Tuman"]),
    ("Kunduzi osmonda porlaydi, hammani isitadi.", "Quyosh", ["Oy", "Bulut", "Chiroq"]),
    ("Tunda chiqadi, goh o‘roqday, goh patirday.", "Oy", ["Quyosh", "Bulut", "Kamalak"]),
    ("Ichi qizil, sirti yashil, yozda pishadi, urug‘i qora.", "Tarvuz", ["Olma", "Qovun", "Pomidor"]),
    ("Gul shirasidan asal yig‘adi, g‘uvillab uchadi.", "Asalari", ["Kapalak", "Chivin", "Ninachi"]),
    ("O‘rkachi bor, cho‘lda yuk tashiydi, uzoq chanqamaydi.", "Tuya", ["Ot", "Eshak", "Sigir"]),
    ("Bo‘yni juda uzun, baland daraxt barglarini yeydi, terisi dog‘li.", "Jirafa", ["Fil", "Zebra", "Tuya"]),
    ("Qishda oppoq, qulog‘i uzun, sakrab yuradi, sabzini yaxshi ko‘radi.", "Quyon", ["Tulki", "Olmaxon", "Qo‘y"]),
    ("Kunduzi uxlaydi, tunda ov qiladi, boshini ko‘p buradi, ko‘zlari katta.", "Boyqush", ["Qarg‘a", "Kaptar", "Chumchuq"]),
    ("Yozganimni o‘chiradi, o‘zi esa kichrayadi.", "O‘chirg‘ich", ["Qalam", "Chizg‘ich", "Daftar"]),
]

# Asar — muallif (umumma’lum)
WORKS = [
    ("“Shum bola”", "G‘afur G‘ulom"),
    ("“Sariq devni minib”", "Xudoyberdi To‘xtaboyev"),
    ("“Bolalik”", "Oybek"),
    ("“O‘tkan kunlar”", "Abdulla Qodiriy"),
    ("“Xamsa”", "Alisher Navoiy"),
    ("“Boburnoma”", "Zahiriddin Muhammad Bobur"),
    ("“Kecha va kunduz”", "Abdulhamid Cho‘lpon"),
    ("“Oygul bilan Baxtiyor”", "Hamid Olimjon"),
    ("“Dunyoning ishlari”", "O‘tkir Hoshimov"),
    ("“Qutadg‘u bilig”", "Yusuf Xos Hojib"),
    ("“Devonu lug‘otit turk”", "Mahmud Koshg‘ariy"),
    ("“Zarbulmasal”", "Gulxaniy"),
]
AUTHORS = sorted({a for _, a in WORKS})

FOLK = [
    ("“Zumrad va Qimmat”", "Xalq ertagi"), ("“Ur to‘qmoq”", "Xalq ertagi"), ("“Uch og‘a-ini botirlar”", "Xalq ertagi"),
    ("“Alpomish”", "Xalq dostoni"), ("“Go‘ro‘g‘li”", "Xalq dostoni"),
]
