"""Original service/craft track. Both tracks are available to every parent."""
import copy


def rows(text):
    return [r.split('|') for r in text.strip().splitlines()]


DATA = {
 (3, 'service_textile'): {
  'title': ('Mato, naqsh va andoza', 'Fabric, patterns and templates', 'Ткань, узоры и шаблоны'),
  'pairs': rows('''Mato|Tolalardan tayyorlangan egiluvchan material
Ip|Tolalarni birlashtirish yoki bezash materiali
Andoza|Bir xil shaklni takrorlash namunasi
Naqsh|Shakl va ranglarning tartibli bezagi
Takroriy naqsh|Bir belgi ketma-ket qaytariladigan bezak
Simmetrik bezak|Ikki tomoni bir-biriga mos bezak
Mato qoldig‘i|Mayda bezak uchun saqlanadigan bo‘lak
Qog‘oz namunasi|Matoga o‘tishdan oldin sinash shakli'''),
  'orders': [
   ('Qog‘ozda mato bezagini rejalash', ['Buyum shaklini tanlash', 'Shaklni qog‘ozga chizish', 'Naqsh ranglarini belgilash', 'Naqshning takrorlanishini tekshirish']),
   ('Matodan yopishtirma bezak rejalash', ['Toza mato qoldiqlarini tanlash', 'Qog‘oz andozalarni ustiga joylash', 'Kesish chiziqlarini belgilash', 'Qismlarni kartonda joylab ko‘rish']),
   ('Simmetrik qog‘oz andoza tayyorlash', ['Qog‘ozni teng ikkiga buklash', 'Buklangan chetga yarim shakl chizish', 'Chiziq bo‘ylab ehtiyotkor kesish', 'Qog‘ozni ochib ikki tomonini tekshirish']),
  ],
  'sorts': [
   ('Material va naqsh rejasini ajrating.', ['Material', 'Reja / namuna'], [('Mato bo‘lagi',0),('Ip bo‘lagi',0),('Mato qoldig‘i',0),('Qog‘oz andoza',1),('Ranglar eskizi',1),('Naqsh chizmasi',1)]),
   ('Materialni tejash va isrof qilishni ajrating.', ['Tejash', 'Isrof'], [('Andozalarni yaqin joylash',0),('Toza qoldiqni saqlash',0),('Avval qog‘ozda sinash',0),('Keragidan ortiq kesish',1),('Yaroqli bo‘lakni tashlash',1),('O‘lchamasdan kesish',1)]),
  ],
 },
 (3, 'service_table'): {
  'title': ('Dasturxon va buyumlarni tartiblash', 'Table setting and organization', 'Сервировка и порядок'),
  'pairs': rows('''Likopcha|Taom solinadigan yassi idish
Piyola|Ichimlik quyiladigan kichik idish
Qoshiq|Suyuq taom yeyish vositasi
Salfetka|Qo‘l va og‘izni artish vositasi
Taglik|Stol yuzasini himoya qiladigan buyum
Qo‘l yuvish|Ovqatlanishdan oldingi gigiyena odati
Tartiblagich|Mayda buyumlarni ajratib saqlash qutisi
Joy rejasi|Buyumlar qayerda turishini ko‘rsatadigan chizma'''),
  'orders': [
   ('Dasturxonni tayyorlash', ['Qo‘llarni yuvish', 'Toza stol va taglikni tayyorlash', 'Butun toza idishlarni joylash', 'Salfetkalarni qo‘yish']),
   ('Shaxsiy buyumlarni tartiblash', ['Buyumlarni stolga yig‘ish', 'Vazifasiga qarab guruhlash', 'Har guruh uchun joy belgilash', 'Buyumlarni belgilangan joyga qo‘yish']),
   ('Idishning yaroqliligini tekshirish', ['Idishni kattalar bilan ko‘zdan kechirish', 'Yoriq va siniq yo‘qligini tekshirish', 'Tozaligini tekshirish', 'Yaroqli idishni dasturxonga qo‘yish']),
  ],
  'sorts': [
   ('Dasturxon buyumlari va o‘quv qurollarini ajrating.', ['Dasturxon', 'O‘qish'], [('Likopcha',0),('Piyola',0),('Salfetka',0),('Daftar',1),('Qalam',1),('Chizg‘ich',1)]),
   ('Dasturxon uchun yaroqli va yaroqsiz buyumlarni ajrating.', ['Yaroqli', 'Kattaga berish'], [('Toza likopcha',0),('Butun piyola',0),('Toza salfetka',0),('Yoriq piyola',1),('Singan likopcha',1),('Iflos qoshiq',1)]),
  ],
 },
 (5, 'service_sewing'): {
  'title': ('To‘qimachilik va tikuv loyihasi', 'Textiles and sewing design', 'Текстиль и швейный проект'),
  'pairs': rows('''Paxta tolasi|Paxta o‘simligidan olinadigan tola
Jun tolasi|Hayvon junidan olinadigan tola
Sintetik tola|Kimyoviy usulda tayyorlanadigan tola
Gazlama|O‘zaro to‘qilgan iplardan tayyorlangan material
Andoza|Detal konturining qog‘oz namunasi
Chok haqi|Biriktirish uchun qoldiriladigan qo‘shimcha chet
O‘lchov lentasi|Egiluvchan buyum uzunligini o‘lchash vositasi
Chok chizig‘i|Qismlar biriktiriladigan belgilangan yo‘l'''),
  'orders': [
   ('Mato g‘ilofini rejalash', ['Ichiga solinadigan buyumni o‘lchash', 'Qog‘oz eskizini chizish', 'Chok haqi bilan andoza tayyorlash', 'Andozani buyum o‘lchami bilan tekshirish']),
   ('Gazlamani tejamli bichishni rejalash', ['Andozalar sonini aniqlash', 'Gazlama yuzasini tekislash', 'Andozalarni kam chiqindi bilan joylash', 'Detal va chok chiziqlarini belgilash']),
   ('Tikuv loyihasini baholash', ['Buyum talablarini qayta o‘qish', 'O‘lchamlarni talab bilan solishtirish', 'Chok chiziqlari mosligini tekshirish', 'Tuzatish kerak bo‘lgan joyni yozish']),
  ],
  'sorts': [
   ('Tolalarni tabiiy va sintetik guruhga ajrating.', ['Tabiiy', 'Sintetik'], [('Paxta',0),('Jun',0),('Zig‘ir',0),('Poliester',1),('Neylon',1),('Akril',1)]),
   ('Bichish rejasidagi mos va nomos ishlarni ajrating.', ['Mos', 'Tuzatish kerak'], [('O‘lchovlarni yozish',0),('Chok haqi qoldirish',0),('Avval andozani sinash',0),('Chok haqini unutish',1),('Andozani chetdan chiqarish',1),('O‘lchovsiz kesish',1)]),
  ],
 },
 (5, 'service_food'): {
  'title': ('Ovqatlanish gigiyenasi va sovuq taom rejasi', 'Food hygiene and cold dish planning', 'Гигиена и план холодного блюда'),
  'pairs': rows('''Qo‘l gigiyenasi|Taomga tegishdan oldin qo‘lni yuvish
Yaroqlilik muddati|Mahsulot yorlig‘ida ko‘rsatilgan foydalanish vaqti
Yorliq|Mahsulot tarkibi va saqlash shartlari yozuvi
Toza sirt|Taom tayyorlashdan oldin tozalangan ish joyi
Xom mahsulot|Hali pishirilmagan mahsulot
Tayyor taom|Iste’mol qilish uchun tayyorlangan ovqat
Alohida saqlash|Xom va tayyor mahsulot tegishishini oldini olish
Retsept rejasi|Mahsulotlar va qadamlarning oldindan yozilgan ro‘yxati'''),
  'orders': [
   ('Virtual meva salatini rejalash', ['Retsept va mahsulotlar ro‘yxatini tanlash', 'Yaroqlilik va saqlash shartlarini tekshirish', 'Qo‘l va ish joyi tozaligini rejalash', 'Yuvilgan mevalarni aralashtirish bosqichini belgilash']),
   ('Mahsulot yorlig‘ini tekshirish', ['Mahsulot nomini o‘qish', 'Tarkibini o‘qish', 'Yaroqlilik muddatini tekshirish', 'Saqlash shartini tekshirish']),
   ('Sovuq taom tayyorlash joyini rejalash', ['Stoldagi ortiqcha buyumlarni olish', 'Ish sirtini tozalash', 'Toza idishlarni joylash', 'Mahsulotlarni alohida joylashtirish']),
  ],
  'sorts': [
   ('Gigiyenaga mos va nomos holatlarni ajrating.', ['Mos', 'Nomos'], [('Qo‘lni yuvish',0),('Toza idish ishlatish',0),('Yorliqni tekshirish',0),('Iflos sirtga meva qo‘yish',1),('Xom va tayyor taomni aralashtirish',1),('Mog‘orlagan mahsulotni ishlatish',1)]),
   ('Mahsulotni tekshirish va stolni bezash ishlarini ajrating.', ['Mahsulotni tekshirish', 'Stolni bezash'], [('Yaroqlilikni o‘qish',0),('Tarkibni o‘qish',0),('Saqlash shartini o‘qish',0),('Salfetka rangini tanlash',1),('Taglik naqshini tanlash',1),('Gullarni joylash',1)]),
  ],
 },
 (5, 'service_home'): {
  'title': ('Uy buyumlari va tejamkor loyiha', 'Household organization and resource planning', 'Порядок дома и экономный проект'),
  'pairs': rows('''Buyumlar ro‘yxati|Mavjud narsalarni yozib chiqish
Guruhlash|Bir vazifadagi narsalarni bir joyga ajratish
Belgi yorlig‘i|Quti ichidagi guruh nomini ko‘rsatish
Qayta foydalanish|Eski buyumdan yangi maqsadda foydalanish
Tejamkor reja|Kerakli materialni isrofsiz belgilash
Suvni tejash|Keraksiz oqayotgan suvni to‘xtatish
Elektrni tejash|Keraksiz yoritishni o‘chirish
Sinov mezoni|Tartiblagich vazifasini baholash sharti'''),
  'orders': [
   ('O‘quv buyumlari tartiblagichini rejalash', ['Buyumlar ro‘yxatini tuzish', 'Buyumlarni vazifasiga qarab guruhlash', 'Har guruh uchun bo‘lim eskizini chizish', 'Qayta ishlatiladigan toza qutini tanlash']),
   ('Tartiblagichni sinash', ['Buyumlarni bo‘limlarga joylash', 'Har bo‘lim yorlig‘ini tekshirish', 'Buyumni tez topishni sinash', 'Kerak bo‘lsa bo‘lim o‘lchamini tuzatish']),
   ('Material xarajatini rejalash', ['Buyumning o‘lchamini belgilash', 'Kerakli detallarni sanash', 'Mavjud material miqdorini tekshirish', 'Faqat yetishmaydigan materialni yozish']),
  ],
  'sorts': [
   ('Tejash va isrof holatlarini ajrating.', ['Tejash', 'Isrof'], [('Bo‘sh xonada chiroqni o‘chirish',0),('Keraksiz oqayotgan kranni yopish',0),('Toza qutini qayta ishlatish',0),('Bo‘sh xonada chiroqni yoqib qo‘yish',1),('Kranni ochiq unutish',1),('Yaroqli kartonni tashlash',1)]),
   ('Buyumlarni o‘quv qurollari va dasturxon guruhiga ajrating.', ['O‘quv quroli', 'Dasturxon'], [('Qalam',0),('Chizg‘ich',0),('Daftar',0),('Salfetka',1),('Piyola',1),('Likopcha',1)]),
  ],
 },
}


def prepare(curriculum, grade):
    # Rebuild only this generated extension, preserving all original topic IDs.
    curriculum['topics'] = [t for t in curriculum['topics'] if not t['id'].split('.')[-1].startswith('service_')]
    technical = {'project', 'test4', 'final'} if grade == 3 else {'mechanisms', 'prototype', 'test3', 'test4', 'final'}
    for t in curriculum['topics']:
        key = t['id'].split('.')[-1]
        t['tags'] = ['track:technical'] if key in technical else []
    template = next(t for t in curriculum['topics'] if t['generator'] != 'test')
    tests = []
    for n, ((g, key), data) in enumerate((p for p in DATA.items() if p[0][0] == grade), 1):
        t = copy.deepcopy(template)
        t.update(id=f'technology_g{grade}.{key}', code=f'S{n}', emoji='🧵' if 'textile' in key or 'sewing' in key else '🏡',
          title=dict(zip(('uz','en','ru'), data['title'])), generator='bank', skill='bank',
          tags=['track:service'], prerequisites=[], levels=[{'options':3},{'options':4},{'options':4}],
          chapter=f'{n+1}-chorak. Servis va hunarmandchilik',
          theory={'uz':'Bu darsda buyumning vazifasini aniqlaymiz, reja tuzamiz va natijani tekshiramiz. ' + '; '.join(f'{a} — {b.lower()}' for a,b in data['pairs']) + '. Misol: ' + data['orders'][0][0] + ': ' + ' → '.join(data['orders'][0][1]) + '. Mashqlar virtual; amaliy ish kattalar bilan bajariladi.'})
        curriculum['topics'].append(t)
        test = copy.deepcopy(next(t for t in curriculum['topics'] if t['generator'] == 'test'))
        test.update(id=f'technology_g{grade}.service_test{n}', title={'uz':f'Servis: {n}-nazorat','en':f'Service test {n}','ru':f'Сервис: контроль {n}'}, chapter=t['chapter'], tags=['track:service'], prerequisites=[])
        test['levels'] = [{'topics':[t['id']], 'level':level} for level in (1,2,3)]
        tests.append(test)
    final = copy.deepcopy(tests[-1])
    common = ['safety','paper','reuse'] if grade == 3 else ['design','materials']
    sources = [f'technology_g{grade}.{k}' for k in common] + [t['id'] for t in curriculum['topics'] if t['id'].split('.')[-1].startswith('service_')]
    final.update(id=f'technology_g{grade}.service_final', code='SY', title={'uz':'Servis: yakuniy nazorat','en':'Service final test','ru':'Сервис: итоговая работа'}, chapter='Yakuniy nazorat')
    final['levels'] = [{'topics':sources,'level':level} for level in (1,2,3)]
    curriculum['topics'].extend(tests+[final])
