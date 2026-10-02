"""Original Technology activities for grades 3 and 5; no textbook completeness claim.

Run from any directory: python3 tool/content/school/technology.py
Existing topic IDs are preserved so saved progress continues to work.
"""
import copy
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[3] / 'assets/data/school'

def lines(text):
    return [line.split('|') for line in text.strip().splitlines()]

DATA = {
    (3, 'safety'): {
        'pairs': lines('''Chizg‘ich|Uzunlikni o‘lchash
Qalam|Kesishdan oldin belgi qo‘yish
Qaychi|Qog‘ozni belgilangan chiziqda kesish
Elim|Qog‘oz qismlarini biriktirish
Andoza|Bir xil shaklni ko‘chirish
Taglik|Ish stoli yuzasini himoyalash
Chiqindi qutisi|Qog‘oz qoldiqlarini yig‘ish
Yopiq qaychi dastasi|Qaychini xavfsiz uzatish'''),
        'orders': [
            ('Ish stolini tayyorlash', ['Keraksiz buyumlarni olib qo‘yish', 'Stolga taglik qo‘yish', 'Kerakli materiallarni joylash', 'Ishni boshlash']),
            ('Qaychini boshqa kishiga uzatish', ['Kesishni to‘xtatish', 'Qaychi tig‘larini yopish', 'Dastasini oluvchiga qaratish', 'Qaychini ehtiyotkorlik bilan uzatish']),
            ('Dars oxirida ish joyini yig‘ish', ['Asboblarni ishlatishni to‘xtatish', 'Qaychini yopib joyiga qo‘yish', 'Qog‘oz qoldiqlarini yig‘ish', 'Stolni tartibga keltirish']),
        ],
        'sorts': [
            ('Harakatlarni xavfsiz va xavfli guruhga ajrating.', ['Xavfsiz', 'Xavfli'],
             [('Qaychini yopib uzatish', 0), ('Taglikda ishlash', 0), ('Asbobni joyiga qo‘yish', 0), ('Ochiq qaychi bilan yugurish', 1), ('Qaychi tig‘ini odamga qaratish', 1), ('Asbobni stol chetida qoldirish', 1)]),
            ('Buyumlarni o‘lchash-belgilash va biriktirish guruhiga ajrating.', ['O‘lchash / belgilash', 'Biriktirish'],
             [('Chizg‘ich', 0), ('Qalam', 0), ('Andoza', 0), ('Qog‘oz elimi', 1), ('Yelim tayoqchasi', 1), ('Yopishqoq lenta', 1)]),
        ],
    },
    (3, 'paper'): {
        'pairs': lines('''Yupqa qog‘oz|Oson buklanadigan material
Karton|Qog‘ozdan qalinroq maket materiali
Buklash chizig‘i|Qog‘oz buklanadigan belgi
Kesish chizig‘i|Qaychi yuradigan belgi
Andoza|Shaklni nusxalash namunasi
Yelim qopqog‘i|Biriktirish uchun qoldirilgan chet
Chizg‘ich|Tekis chiziq chizish vositasi
Simmetrik buklash|Ikki chetni ustma-ust keltirish'''),
        'orders': [
            ('Tabrik kartochkasini tayyorlash', ['Qog‘ozning ikki chetini tenglashtirish', 'Qog‘ozni o‘rtasidan buklash', 'Old tomoniga naqsh chizish', 'Ichiga tabrik yozish']),
            ('Andozadan karton shakl yasash', ['Andozani karton ustiga qo‘yish', 'Shakl chetini qalam bilan chizish', 'Belgilangan chiziq bo‘ylab kesish', 'Shaklni andoza bilan solishtirish']),
            ('Qog‘oz halqa tayyorlash', ['Qog‘oz tasma uzunligini belgilash', 'Tasmani belgi bo‘ylab kesish', 'Ikki uchini ustma-ust qo‘yish', 'Uchlarini elim bilan biriktirish']),
        ],
        'sorts': [
            ('Buklash va kesish ishlarini ajrating.', ['Buklash', 'Kesish'], [('Qog‘ozni teng ikkiga qayirish', 0), ('Chetlarni ustma-ust keltirish', 0), ('Buklangan joyni bosib tekislash', 0), ('Qaychi bilan tasma ajratish', 1), ('Andoza konturini qaychida ajratish', 1), ('Qog‘ozdan doira qirqish', 1)]),
            ('Ushbu quruq maketlar uchun yupqa qog‘oz yoki kartonni tanlang.', ['Yupqa qog‘oz', 'Karton'], [('Oddiy buklama', 0), ('Qog‘oz zanjir halqasi', 0), ('Yengil bezak tasmasi', 0), ('Maket tagligi', 1), ('Mustahkam quti devori', 1), ('Qalamdon asos qismi', 1)]),
        ],
    },
    (3, 'reuse'): {
        'pairs': lines('''Quruq barg|Tabiiy bezak materiali
Urug‘|O‘simlikdan olinadigan tabiiy material
Quruq novda|Daraxtdan olinadigan tabiiy material
Toza karton quti|Qayta ishlatish mumkin bo‘lgan idish
Toza plastik qopqoq|Mozaika uchun qayta ishlatiladigan detal
Qog‘oz qoldig‘i|Mayda bezak uchun tejaladigan material
Saralash|Turli chiqindilarni alohida yig‘ish
Qayta foydalanish|Buyumga yangi vazifa berish'''),
        'orders': [
            ('Barglardan bezak tayyorlash', ['Quruq toza barglarni tanlash', 'Ularni kartonga yelimsiz joylab ko‘rish', 'Barglarni oz elim bilan yopishtirish', 'Bezakni quritish']),
            ('Eski qutidan tartiblagich yasash', ['Toza va butun qutini tanlash', 'Ichiga karton bo‘luvchilarni joylab ko‘rish', 'Bo‘luvchilarni lenta bilan mahkamlash', 'Qalamlarni tartib bilan joylash']),
            ('Materialni tejamli ishlatish', ['Kerakli shakllarni rejalash', 'Shakllarni kartonga yaqin joylashtirib chizish', 'Shakllarni chiziq bo‘ylab kesish', 'Yaroqli qoldiqlarni keyingi ishga saqlash']),
        ],
        'sorts': [
            ('Materiallarni kelib chiqishi bo‘yicha ajrating.', ['Tabiiy', 'Odam tayyorlagan'], [('Barg', 0), ('Urug‘', 0), ('Novda', 0), ('Karton quti', 1), ('Plastik qopqoq', 1), ('Yopishqoq lenta', 1)]),
            ('Qayta foydalanish uchun yaroqli buyumlarni ajrating.', ['Toza va butun', 'Yaroqsiz / kattaga berish'], [('Toza karton quti', 0), ('Yuvilgan butun qopqoq', 0), ('Toza qog‘oz qoldig‘i', 0), ('Singan shisha', 1), ('Mog‘orlagan quti', 1), ('O‘tkir zanglagan detal', 1)]),
        ],
    },
    (3, 'project'): {
        'pairs': lines('''Maqsad|Buyum nima uchun kerakligini aniqlash
Eskiz|G‘oyaning oddiy chizmasi
Material ro‘yxati|Kerakli narsalarni oldindan yozish
O‘lcham|Buyumning uzunlik va kenglik qiymati
Maket|G‘oyani kichik modelda ko‘rsatish
Sinov|Buyum vazifasini bajarishini tekshirish
Yaxshilash|Topilgan kamchilikni tuzatish
Taqdimot|Tayyor ishni boshqalarga tushuntirish'''),
        'orders': [
            ('Qalamdon loyihasini rejalash', ['Nechta qalam sig‘ishini belgilash', 'Qalamdon eskizini chizish', 'Material va o‘lchamlarni tanlash', 'Yasash rejasini yozish']),
            ('Tayyor qalamdonni sinash', ['Qalamdonni tekis stolga qo‘yish', 'Unga rejalangan qalamlarni joylash', 'Ag‘darilish yoki egilishni kuzatish', 'Natijani yozib yaxshilash rejasini tuzish']),
            ('Qalamdon tagligini yaxshilash', ['Taglik egilganini aniqlash', 'Qalinroq karton tanlash', 'Yangi taglikni mahkamlash', 'Qalamlar bilan qayta sinash']),
        ],
        'sorts': [
            ('Loyiha ishlarini yasashdan oldin va keyin bajarilishiga qarab ajrating.', ['Yasashdan oldin', 'Yasashdan keyin'], [('Maqsadni belgilash', 0), ('Eskiz chizish', 0), ('Materialni tanlash', 0), ('Tayyor buyumni sinash', 1), ('Sinov natijasini yozish', 1), ('Tayyor ishni taqdim qilish', 1)]),
            ('Qalamdon sinovi natijalarini ajrating.', ['Vazifaga mos', 'Yaxshilash kerak'], [('Qalamlar sig‘di', 0), ('Stolda barqaror turdi', 0), ('Biriktirilgan joylar ochilmadi', 0), ('Qalamlar sig‘madi', 1), ('Taglik ag‘darildi', 1), ('Elimlangan joy ajraldi', 1)]),
        ],
    },
    (5, 'design'): {
        'pairs': lines('''Muammo|Yechilishi kerak bo‘lgan ehtiyoj
Talab|Mahsulot bajarishi kerak bo‘lgan shart
Eskiz|G‘oya va shaklning chizmasi
O‘lcham yozuvi|Detallar kattaligini ko‘rsatish
Prototip|G‘oyani sinash uchun dastlabki model
Sinov mezoni|Natijani baholash uchun oldindan belgilangan o‘lchov
Takomillashtirish|Sinovga ko‘ra loyihani tuzatish
Xavfsizlik rejasi|Ishdagi xavflarni oldindan kamaytirish'''),
        'orders': [
            ('Telefon tagligi dizaynini rejalash', ['Ehtiyojni aniqlash', 'Barqarorlik va o‘lcham talablarini yozish', 'Bir nechta eskiz chizish', 'Talabga mos g‘oyani tanlash']),
            ('Taglik prototipini tekshirish', ['Barqarorlik mezonini belgilash', 'Karton prototipni yasash', 'Telefon o‘lchamidagi yengil maket bilan sinash', 'Natijani mezon bilan solishtirish']),
            ('Dizaynni yaxshilash', ['Sinovdagi kamchilikni yozish', 'Kamchilik sababini aniqlash', 'Eskiz va prototipni o‘zgartirish', 'Bir xil sharoitda qayta sinash']),
        ],
        'sorts': [
            ('Talab va yechimni ajrating.', ['Talab', 'Yechim'], [('Stolda ag‘darilmasin', 0), ('Qalamlar sig‘sin', 0), ('Qayta ishlatilgan material bo‘lsin', 0), ('Taglikni kengaytirish', 1), ('Ichiga bo‘luvchi qo‘yish', 1), ('Toza eski qutidan yasash', 1)]),
            ('Ishlarni rejalash va sinov bosqichiga ajrating.', ['Rejalash', 'Sinov'], [('Talablarni yozish', 0), ('Eskiz chizish', 0), ('Material ro‘yxatini tuzish', 0), ('Prototip barqarorligini tekshirish', 1), ('Natijani qayd qilish', 1), ('Natijani talab bilan solishtirish', 1)]),
        ],
    },
    (5, 'materials'): {
        'pairs': lines('''Karton|Yengil va oson kesiladigan quruq maket materiali
Mato|Egiluvchan va tikiladigan material
Yog‘och|Tolali tuzilishga ega qattiq material
Plastmassa|Ko‘p turlari suvni shimimaydigan material
Po‘lat|Mustahkam, temir asosli metall qotishma
Chizg‘ich|Uzunlikni o‘lchash asbobi
Qaychi|Qog‘oz yoki matoni kesish asbobi
Jilvir qog‘oz|Yuzani silliqlash materiali'''),
        'orders': [
            ('Quruq maket uchun material tanlash', ['Maket vazifasini aniqlash', 'Kerakli material xossalarini yozish', 'Mavjud materiallarni solishtirish', 'Mos materialni tanlash']),
            ('Karton detalni aniq tayyorlash', ['Detal o‘lchamini o‘qish', 'Chizg‘ich bilan kartonga belgilash', 'Belgi bo‘ylab ehtiyotkor kesish', 'Detal o‘lchamini qayta tekshirish']),
            ('Materiallarni bir xil sharoitda solishtirish', ['Bir xil o‘lchamli namunalar tayyorlash', 'Har namunaga bir xil kichik yuk qo‘yish', 'Egilishni kuzatib yozish', 'Natijaga mos materialni tanlash']),
        ],
        'sorts': [
            ('Material va asboblarni ajrating.', ['Material', 'Asbob'], [('Karton', 0), ('Mato', 0), ('Yog‘och', 0), ('Chizg‘ich', 1), ('Qaychi', 1), ('Qalam', 1)]),
            ('Egiluvchan mato va qattiq yog‘ochga mos ishlarni ajrating.', ['Mato', 'Yog‘och'], [('Tikiladigan kichik xalta', 0), ('Buklanadigan mato bezak', 0), ('Yumshoq mato g‘ilof', 0), ('Qattiq maket tayanchi', 1), ('Yog‘och detal', 1), ('Qattiq yog‘och ramka', 1)]),
        ],
    },
    (5, 'mechanisms'): {
        'pairs': lines('''Batareya|Elektr energiyasi manbai
Sim|Zanjir qismlarini elektr jihatdan bog‘lash
Kalit|Zanjirni ochish yoki yopish
Lampochka|Elektr energiyasini yorug‘likka aylantirish
Yopiq zanjir|Tok uchun uzluksiz yo‘l
Ochiq zanjir|Tok yo‘li uzilgan holat
Richag|Tayanch atrofida aylanadigan qattiq tayoq
Shkiv|Arqon yo‘nalishini o‘zgartiradigan g‘ildirak'''),
        'orders': [
            ('Virtual lampochka zanjirini tayyorlash', ['Batareya, sim, lampochka va kalitni tanlash', 'Kalit ochiq holatda simlarni ulash', 'Ulanishlarda uzilish yo‘qligini tekshirish', 'Kalitni yopib lampochkani kuzatish']),
            ('Virtual zanjirda uzilishni topish', ['Lampochka yonmayotganini kuzatish', 'Kalit yopilganini tekshirish', 'Ikkala sim ulanishini tekshirish', 'Uzilgan simni ulab qayta sinash']),
            ('Richag modelini tekshirish', ['Tayanchni taglikka joylash', 'Qattiq tayoqni tayanch ustiga qo‘yish', 'Bir uchiga kichik yuk qo‘yish', 'Ikkinchi uchiga yengil kuch berib kuzatish']),
        ],
        'sorts': [
            ('Elektr zanjiri qismlari va mexanizmlarni ajrating.', ['Elektr qismi', 'Mexanizm'], [('Batareya', 0), ('Lampochka', 0), ('Kalit', 0), ('Richag', 1), ('Shkiv', 1), ('G‘ildirak va o‘q', 1)]),
            ('Ideal virtual zanjirda lampochka holatini aniqlang.', ['Yonadi', 'Yonmaydi'], [('Simlar ulangan, kalit yopiq', 0), ('Uzluksiz yo‘l, batareya soz', 0), ('Lampochka soz, zanjir yopiq', 0), ('Bir sim uzilgan', 1), ('Kalit ochiq', 1), ('Batareya ulanmagan', 1)]),
        ],
    },
    (5, 'prototype'): {
        'pairs': lines('''Algoritm|Aniq qadamlar ketma-ketligi
Prototip|G‘oyani erta sinash modeli
Boshlang‘ich ma’lumot|Ishni boshlash uchun kerakli ma’lumot
Shart|Rost yoki yolg‘onligi tekshiriladigan fikr
Takrorlash|Bir qadamni bir necha marta bajarish
Sinov qaydi|Tekshirish natijasini yozib saqlash
Xatoni tuzatish|Nuqson sababini bartaraf etish
Loyiha taqdimoti|Maqsad, jarayon va natijani tushuntirish'''),
        'orders': [
            ('Karton ko‘prik prototipini sinash', ['Bir xil masofadagi tayanchlarni qo‘yish', 'Karton ko‘prikni tayanchlarga joylash', 'Kichik yukni o‘rtasiga ehtiyotkor qo‘yish', 'Egilish natijasini yozish']),
            ('Egilgan ko‘prikni yaxshilash', ['Ko‘prik egilish sababini aniqlash', 'Karton ostiga qo‘shimcha qovurg‘a rejalash', 'Qovurg‘ani prototipga biriktirish', 'Oldingi yuk bilan qayta sinash']),
            ('Loyihani taqdim qilish', ['Maqsad va talablarni aytish', 'Eskiz va materiallarni ko‘rsatish', 'Yasash jarayonini tushuntirish', 'Sinov va yaxshilash natijasini aytish']),
        ],
        'sorts': [
            ('Algoritmdagi ko‘rsatma va natijani ajrating.', ['Ko‘rsatma', 'Natija'], [('Detalni belgilash', 0), ('Tasmani buklash', 0), ('Buyumni sinash', 0), ('Belgi qo‘yilgan detal', 1), ('Buklangan tasma', 1), ('Yozilgan sinov qaydi', 1)]),
            ('Sinovda adolatli solishtirish shartlarini ajrating.', ['Solishtirishga mos', 'Solishtirishga mos emas'], [('Bir xil yuk bilan sinash', 0), ('Bir xil tayanch oralig‘i', 0), ('Bir xil o‘lchamli namunalar', 0), ('Har safar boshqa yuk', 1), ('Tayanch oralig‘ini tasodifan o‘zgartirish', 1), ('Natijani yozmasdan taxmin qilish', 1)]),
        ],
    },
}

TITLES = {
    'safety': ('Tools and safety', 'Инструменты и безопасность'),
    'paper': ('Paper and cardboard', 'Бумага и картон'),
    'reuse': ('Natural and reusable materials', 'Природные материалы и повторное использование'),
    'project': ('Simple projects and models', 'Простые проекты и макеты'),
    'design': ('Design process and safety', 'Проектирование и безопасность'),
    'materials': ('Material properties and tools', 'Свойства материалов и инструменты'),
    'mechanisms': ('Simple mechanisms and electric circuits', 'Простые механизмы и электрические цепи'),
    'prototype': ('Prototypes, algorithms and presentations', 'Прототипы, алгоритмы и презентации'),
}

def build():
    for grade in (3, 5):
        path = BASE / f'technology_g{grade}.json'
        curriculum = json.loads(path.read_text())
        curriculum['topics'] = [t for t in curriculum['topics'] if not t['id'].endswith('_workshop')]
        items, topics = [], []
        for topic in curriculum['topics']:
            topics.append(topic)
            key = topic['id'].split('.')[-1]
            data = DATA.get((grade, key))
            if data is None:
                continue
            topic['title']['en'], topic['title']['ru'] = TITLES[key]
            pairs = data['pairs']
            def add(kind, question, explanation, **extra):
                items.append(dict(topic=topic['id'], id=f'{key}_{len(items)+1}', t=kind,
                    q=question, x=explanation, h=explanation, d=1, **extra))
            for left, right in pairs:
                wrong = [r for _, r in pairs if r != right][:3]
                add('choice', f'«{left}» uchun mos vazifa yoki tavsifni tanlang.',
                    f'{left} — {right.lower()}.', a=right, w=wrong)
            for label, steps in data['orders']:
                add('order', f'{label}: qadamlarni to‘g‘ri tartibda bosing.',
                    ' → '.join(steps) + '.', parts=steps, sep=' → ')
            for label, subset in [('Asosiy juftliklar', pairs[:4]), ('Amaliy juftliklar', pairs[4:]), ('Mavzuni mustahkamlash', pairs)]:
                add('match', f'{topic["title"]["uz"]}: {label.lower()}ni moslang.',
                    '; '.join(f'{a} — {b}' for a, b in subset) + '.', pairs=subset)
            for question, bins, rows in data['sorts']:
                add('sort', question, '; '.join(f'{label}: {", ".join(text for text, group in rows if group == i)}' for i, label in enumerate(bins)) + '.', bins=bins, items=rows)
            if key == 'mechanisms':
                for a, b, closed in [(False, False, False), (True, False, True), (False, True, True), (True, True, False)]:
                    add('circuit', 'Ikkala simni ulang va kalit yordamida lampochkani yoqing.',
                        'Ikkala sim ulangan va kalit yopiq bo‘lsa, ideal zanjirda lampochka yonadi.',
                        targetLit=True, wireA=a, wireB=b, switchClosed=closed)
                add('circuit', 'Simlarni uzmasdan, kalit yordamida lampochkani o‘chiring.',
                    'Kalit ochilganda tok yo‘li uziladi va lampochka o‘chadi. Simlar ulangan holda qoladi.',
                    targetLit=False, wireA=True, wireB=True, switchClosed=True)
                note = ' Ilovadagi tajriba virtual: lampochka faqat ikkala sim ulangan va kalit yopiq bo‘lganda yonadi.'
                if note not in topic['theory']['uz']:
                    topic['theory']['uz'] += note
            workshop = copy.deepcopy(topic)
            workshop.update(id=topic['id']+'_workshop', code=topic['code']+'A', emoji='🧰',
                generator='workshop', skill='workshop', lessonSize=6,
                title={'uz': 'Amaliy ustaxona: '+topic['title']['uz'], 'en': 'Workshop: '+topic['title']['en'], 'ru': 'Практикум: '+topic['title']['ru']},
                levels=[dict(source=topic['id'], pairs=n) for n in (3, 4, 5)])
            topics.append(workshop)
        curriculum['topics'] = topics
        path.write_text(json.dumps(curriculum, ensure_ascii=False, indent=1)+'\n')
        (BASE/f'bank_technology_g{grade}.json').write_text(json.dumps(dict(items=items), ensure_ascii=False, indent=1)+'\n')
    print('Technology: 8 topic workshops, 128 authored items + 5 circuit tasks')

if __name__ == '__main__':
    build()
