"""Original supplementary practice for the two school profiles (grades 3 and 5).
Not a reproduction of, or claim to cover, an official yearly textbook.
Run from any directory; generates curricula and question banks deterministically.
"""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'assets/data'
OUT = ROOT / 'school'
TITLES = {
 'logic': ('Mantiq', 'Logic', 'Логика', '🧩'),
 'english': ('Ingliz tili', 'English', 'Английский', '🇬🇧'),
 'russian': ('Rus tili', 'Russian', 'Русский', '🇷🇺'),
 'onatili': ('Ona tili', 'Native language', 'Родной язык', '📝'),
 'reading': ('O‘qish', 'Reading', 'Чтение', '📖'),
 'science': ('Tabiiy fan', 'Science', 'Естествознание', '🌿'),
 'informatics': ('Informatika', 'Computer science', 'Информатика', '💻'),
 'history': ('Tarix', 'History', 'История', '🏛️'),
}
CURRICULA = {}
BANKS = {3: [], 5: []}
# Bu fanlar batafsil dasturga ko'chirildi: tool/content/school/<fan>_g<N>.py (schoolkit).
# Bu yerda ular yaratilmaydi, aks holda o'sha fayllar ustidan yozilib ketadi.
MOVED = {'english', 'russian', 'science', 'informatics', 'onatili'}

def topic(subject, grade, key, title, generator, theory, levels=None):
 if subject in MOVED:
  return dict(id=f'{subject}_g{grade}.{key}', title=dict(uz=title, en=title, ru=title))
 c = CURRICULA.setdefault((subject, grade), [])
 t = dict(id=f'{subject}_g{grade}.{key}', code=str(len(c)+1), emoji=TITLES[subject][3],
          title=dict(uz=title, en=title, ru=title), generator=generator, skill=key,
          chapter='Mustahkamlash va yangi ko‘nikmalar', prerequisites=[],
          theory={'uz':theory}, levels=levels or [dict(options=n) for n in (2,3,4)])
 c.append(t)
 return t

def bank(subject, grade, key, title, theory, rows, lang='uz'):
 t=topic(subject, grade, key, title, 'bank', theory)
 if subject in MOVED:
  return t
 assert len(rows)>=15, (t['id'], len(rows))
 for i,(q,a,w,e) in enumerate(rows):
  assert len(set([a]+w))==len(w)+1 and len(w)>=3, (q,a,w)
  BANKS[grade].append(dict(topic=t['id'], id=f'{key}_{i+1}', question=q, answer=a,
                          wrong=w, explanation=e, lang=lang))
 return t

def pairs(subject, grade, key, title, theory, data):
 """Each definition has one explicitly authored answer; distractors are other terms."""
 entries=[line.split('|') for line in data.strip().splitlines() if line.strip()]
 terms=[x[0] for x in entries]
 assert len(terms)==len(set(terms))
 rows=[]
 for i,(term,definition) in enumerate(entries):
  wrong=[terms[(i+j)%len(terms)] for j in (1,2,3)]
  rows.append((definition+' Bu qaysi tushuncha?',term,wrong,f'{term} — {definition[0].lower()+definition[1:]}'))
 return bank(subject,grade,key,title,theory,rows)

# Foreign languages: meaningful reuse of listening, vocabulary and spelling mechanics,
# supplemented with new grade-specific grammar rather than mapping to preschool IDs.
for grade in (3,5):
 for subject in ('english','russian'):
  source=json.loads((ROOT/f'{subject}_6.json').read_text())
  selected=(['toys_school','family','animals','spelling','sentences'] if grade==3 else
            (['jobs','actions','spelling','sentences','listening'] if subject=='english' else ['city','actions','spelling','sentences','food']))
  for key in selected:
   src=next(t for t in source['topics'] if t['id'].endswith('.'+key))
   levels=deepcopy(src['levels'])
   if grade==5 and key=='spelling':
    levels=[dict(minLetters=4,maxLetters=5,extra=1),dict(minLetters=5,maxLetters=6,extra=1),dict(minLetters=5,maxLetters=7,extra=2)]
   if grade==5 and key in ('sentences','listening'):
    levels=[deepcopy(src['levels'][i]) for i in (1,2,2)]
   theory=('Avval so‘z yoki gapni tinglang, keyin ma’nosini rasm bilan bog‘lang. Notanish so‘zni 🔊 tugmasi bilan qayta eshiting. So‘z tuzishda harflar tartibini tekshiring.' if grade==3 else
           'So‘zning ma’nosini gapdagi vaziyat bilan bog‘lang. Harakatni, predmetni va belgini ajrating. Tinglash mashqida barcha so‘zlarni eshitib bo‘lgach javob tanlang; yozishda harflar tartibini tekshiring.')
   t=topic(subject,grade,key,src['title']['uz'],src['generator'],theory,levels)
   t['title']=src['title']

# English grade 3: be, articles and ordinary plural forms.
rows=[]
for pronoun,verb in [('I','am'),('You','are'),('He','is'),('She','is'),('We','are'),('They','are')]:
 for predicate in ['happy','at school','ready']:
  rows.append((f'Choose the missing word: {pronoun} ___ {predicate}.',verb,
               [v for v in ['am','is','are','be'] if v!=verb],
               f'{pronoun} {verb} {predicate}. I → am; he/she/it → is; you/we/they → are.'))
bank('english',3,'be','Am, is, are','I bilan am; he, she, it bilan is; you, we, they bilan are ishlatiladi. Masalan: I am happy. She is ready. We are at school.',rows,'en')
rows=[]
for word,plural in [('cat','cats'),('dog','dogs'),('book','books'),('pen','pens'),('desk','desks'),('bag','bags'),('cup','cups'),('bird','birds'),('car','cars'),('tree','trees'),('box','boxes'),('bus','buses'),('dish','dishes'),('watch','watches'),('class','classes')]:
 wrong=[word,word+'ing',word+'ed']
 rows.append((f'Choose the plural of "{word}".',plural,wrong,f'One {word}, two {plural}.'))
bank('english',3,'plurals','Birlik va ko‘plik','Ko‘p otlarga ko‘plikda -s qo‘shiladi: book → books. -s, -sh, -ch, -x bilan tugagan so‘zlarda odatda -es: bus → buses, box → boxes.',rows,'en')
rows=[]
for word,article in [('apple','an'),('orange','an'),('egg','an'),('umbrella','an'),('elephant','an'),('ant','an'),('insect','an'),('book','a'),('cat','a'),('dog','a'),('pen','a'),('bag','a'),('cup','a'),('desk','a'),('bird','a')]:
 rows.append((f'Use a or an for one object: ___ {word}.',article,[x for x in ['a','an','are','am'] if x!=article],f'{article.capitalize()} {word}. Choose a/an by the first sound.'))
bank('english',3,'articles','A va an','Bitta predmetni aytishda undosh tovushdan oldin a, unli tovushdan oldin an keladi: a book, an apple. So‘zning birinchi tovushiga e’tibor bering.',rows,'en')

# English grade 5: tense contrasts with explicit time markers, and comparatives.
rows=[]
for base,third in [('play','plays'),('read','reads'),('walk','walks'),('work','works'),('cook','cooks'),('swim','swims'),('sing','sings'),('dance','dances'),('write','writes'),('run','runs'),('jump','jumps'),('sleep','sleeps'),('help','helps'),('study','studies'),('watch','watches')]:
 rows.append((f'Choose the Present Simple form: She ___ every day. ({base})',third,[base,'is '+base,base+'ing'],f'She {third} every day. With he/she/it, use the third-person singular form.'))
bank('english',5,'present','Present Simple','Odatdagi ish-harakat Present Simple bilan ifodalanadi. He/she/it bilan fe’lga -s yoki -es qo‘shiladi. Study → studies. Every day odatiylikni bildiradi.',rows,'en')
rows=[]
for base,past in [('go','went'),('see','saw'),('eat','ate'),('come','came'),('take','took'),('write','wrote'),('buy','bought'),('make','made'),('drink','drank'),('give','gave'),('find','found'),('run','ran'),('sing','sang'),('swim','swam'),('play','played')]:
 rows.append((f'Choose the Past Simple form of "{base}".',past,[base,'will '+base,'can '+base],f'{base} → {past}. Use this form for a completed past action.'))
bank('english',5,'past','Past Simple','Tugagan o‘tgan harakat Past Simple bilan ifodalanadi. To‘g‘ri fe’llarga -ed qo‘shiladi: play → played. Noto‘g‘ri fe’llarning shakli yodlanadi: go → went, see → saw.',rows,'en')
rows=[]
for adj,comp in [('tall','taller'),('short','shorter'),('long','longer'),('small','smaller'),('old','older'),('young','younger'),('fast','faster'),('slow','slower'),('cold','colder'),('warm','warmer'),('big','bigger'),('hot','hotter'),('happy','happier'),('easy','easier'),('good','better')]:
 rows.append((f'Choose the comparative form of "{adj}".',comp,[adj,'most '+adj,'the '+adj],f'{adj} → {comp}. Example pattern: A is {comp} than B.'))
bank('english',5,'comparatives','Qiyosiy sifatlar','Ikki narsani qiyoslashda comparative ishlatiladi: tall → taller, big → bigger, easy → easier. Good so‘zining qiyosiy shakli better. Qiyosda than kelishi mumkin.',rows,'en')

# Russian grade 3: gender and singular/plural; grade 5: agreement and verb forms.
ru_nouns=[('стол','мужской род'),('дом','мужской род'),('мяч','мужской род'),('карандаш','мужской род'),('кот','мужской род'),('книга','женский род'),('школа','женский род'),('ручка','женский род'),('лампа','женский род'),('кошка','женский род'),('окно','средний род'),('море','средний род'),('поле','средний род'),('письмо','средний род'),('яблоко','средний род')]
rows=[(f'Определи род слова «{w}».',a,[v for v in ['мужской род','женский род','средний род','это глагол'] if v!=a],f'«{w}» — {a}.') for w,a in ru_nouns]
bank('russian',3,'gender','Otlarning jinsi','Rus tilida otlar uch jinsga bo‘linadi: мужской (он), женский (она), средний (оно). Masalan: стол — он, книга — она, окно — оно.',rows,'ru')
rows=[]
for one,many in [('стол','столы'),('дом','дома'),('книга','книги'),('ручка','ручки'),('кот','коты'),('кошка','кошки'),('лампа','лампы'),('школа','школы'),('окно','окна'),('море','моря'),('поле','поля'),('письмо','письма'),('яблоко','яблоки'),('мяч','мячи'),('карандаш','карандаши')]:
 rows.append((f'Выбери множественное число: один предмет — «{one}», много предметов — …',many,[one,'он','она'],f'{one} → {many}.'))
bank('russian',3,'plural','Ko‘plik shakllari','Bitta va ko‘p predmet shakllarini farqlang: стол — столы, книга — книги, окно — окна. Ko‘plik qo‘shimchalari bir xil emas; so‘zni juftlikda o‘rganing.',rows,'ru')
rows=[]
for noun,gender in ru_nouns:
 forms=['новый','новая','новое','новые'];a=forms[['мужской род','женский род','средний род'].index(gender)]
 rows.append((f'Выбери форму прилагательного: ___ {noun}.',a,[x for x in forms if x!=a],f'{a.capitalize()} {noun}: прилагательное согласуется с существительным в роде и числе.'))
bank('russian',5,'agreement','Sifat va otning moslashuvi','Sifat otga jins va sonda moslashadi: новый стол, новая книга, новое окно, новые книги. Avval otning jinsi yoki ko‘plik shaklini aniqlang.',rows,'ru')
rows=[]
for verb,forms in [('читать',['читаю','читаешь','читает','читаем','читаете','читают']),('играть',['играю','играешь','играет','играем','играете','играют']),('работать',['работаю','работаешь','работает','работаем','работаете','работают'])]:
 for i,pronoun in enumerate(['Я','Ты','Он','Мы','Вы','Они']):
  a=forms[i];rows.append((f'Выбери форму глагола «{verb}»: {pronoun} ___.',a,[forms[(i+j)%6] for j in (1,2,3)],f'{pronoun} {a}. Форма глагола зависит от лица и числа.'))
bank('russian',5,'verbs','Fe’lning shaxs-son shakllari','Hozirgi zamon fe’li shaxs va songa qarab o‘zgaradi: я читаю, ты читаешь, он читает, мы читаем, вы читаете, они читают. Ega bilan fe’lni moslang.',rows,'ru')
rows=[]
for verb,stem in [('читать','читал'),('играть','играл'),('работать','работал'),('гулять','гулял'),('рисовать','рисовал')]:
 for who,ending in [('Он',''),('Она','а'),('Они','и')]:
  a=stem+ending;pool=[stem,stem+'а',stem+'о',stem+'и']
  rows.append((f'Выбери прошедшее время глагола «{verb}»: {who} вчера ___.',a,[x for x in pool if x!=a],f'{who} вчера {a}. В прошедшем времени учитываются род и число.'))
bank('russian',5,'past','O‘tgan zamon','O‘tgan zamonda fe’l jins va songa moslashadi: он читал, она читала, оно читало, они читали. Вчера so‘zi kecha bajarilgan ishni bildiradi.',rows,'ru')

# Native language: original, unambiguous word-class and case exercises.
classes={
 'Ot':['kitob','daftar','qalam','maktab','bog‘','daraxt','gul','daryo','tog‘','shahar','qishloq','bola','ustoz','qush','uy'],
 'Sifat':['qizil','yashil','baland','past','katta','kichik','uzun','qisqa','shirin','achchiq','yumshoq','qattiq','keng','tor','chiroyli'],
 'Fe’l':['o‘qidi','yozdi','yugurdi','keldi','ketdi','ochdi','yopdi','chizdi','kuldi','uxladi','sakradi','o‘ynadi','ichdi','yedi','ishladi'],
 'Son':['bir','ikki','uch','to‘rt','besh','olti','yetti','sakkiz','to‘qqiz','o‘n','yigirma','o‘ttiz','qirq','ellik','yuz'],
}
rows=[]
for cls,words in classes.items():
 for word in words:
  rows.append((f'«{word}» so‘zi qaysi so‘z turkumiga kiradi?',cls,[x for x in classes if x!=cls],f'«{word}» — {cls.lower()}.'))
bank('onatili',3,'word_classes','So‘z turkumlari','Ot shaxs yoki narsani, sifat belgini, son miqdorni, fe’l harakatni bildiradi. Kitob — ot, yashil — sifat, uch — son, o‘qidi — fe’l. So‘zning ma’nosiga qarab ajrating.',rows)
rows=[]
for name in ['Ali','Zarina','Bobur','Madina','Jasur','Nodira','Malika','Sardor']:
 for statement in [True,False]:
  sentence=f'{name} kitob o‘qidi.' if statement else f'{name} qaysi kitobni o‘qidi?'
  a='Darak gap' if statement else 'So‘roq gap'
  rows.append((f'«{sentence}» Mazmuniga ko‘ra qanday gap?',a,[x for x in ['Darak gap','So‘roq gap','Buyruq gap','Istak gap'] if x!=a], 'Bu gap xabar beradi.' if statement else 'Bu gap savol so‘raydi.'))
bank('onatili',3,'sentences','Darak va so‘roq gap','Darak gap xabar beradi va odatda nuqta bilan tugaydi. So‘roq gap savol bildiradi va so‘roq belgisi bilan tugaydi. Masalan: Ali o‘qidi. Ali nima o‘qidi?',rows)
rows=[]
cases=[('', 'Bosh kelishik'),('ning','Qaratqich kelishigi'),('ni','Tushum kelishigi'),('ga','Jo‘nalish kelishigi'),('da','O‘rin-payt kelishigi'),('dan','Chiqish kelishigi')]
for word in ['kitob','daftar','maktab','shahar','uy','daraxt']:
 for i,(suffix,case) in enumerate(cases):
  rows.append((f'«{word+suffix}» so‘zi qaysi kelishikda?',case,[cases[(i+j)%6][1] for j in (1,2,3)],f'«{word+suffix}»: '+(f'-{suffix} qo‘shimchasi {case.lower()}ni bildiradi.' if suffix else 'Bosh kelishikning maxsus qo‘shimchasi yo‘q.')))
bank('onatili',5,'cases','Otlarning kelishiklari','O‘zbek tilida oltita kelishik bor: bosh (qo‘shimchasiz), qaratqich (-ning), tushum (-ni), jo‘nalish (-ga), o‘rin-payt (-da), chiqish (-dan). So‘zning gapdagi bog‘lanishini ham tekshiring.',rows)
rows=[]
for derived,base,suffix in [('ishchi','ish','chi'),('suvchi','suv','chi'),('ovchi','ov','chi'),('gulchi','gul','chi'),('sportchi','sport','chi'),('paxtakor','paxta','kor'),('ijodkor','ijod','kor'),('mehnatkash','mehnat','kash'),('guldon','gul','don'),('tuzdon','tuz','don'),('suvli','suv','li'),('kuchli','kuch','li'),('tuzli','tuz','li'),('suvsiz','suv','siz'),('ishsiz','ish','siz')]:
 wrong=[f'-{x}' for x in ['ning','dan','ni']]
 rows.append((f'«{derived}» so‘zida «{base}» asosiga qaysi yasovchi qo‘shimcha qo‘shilgan?',f'-{suffix}',wrong,f'{base} + {suffix} = {derived}. Bu qo‘shimcha yangi so‘z hosil qilgan.'))
bank('onatili',5,'formation','Asos va so‘z yasovchi qo‘shimcha','So‘z yasovchi qo‘shimcha asosdan yangi so‘z hosil qiladi: ish + chi = ishchi, suv + li = suvli. Kelishik qo‘shimchasi esa so‘zlarni bog‘laydi: kitob + ning.',rows)

for grade in (3,5):
 topic('reading',grade,'understand','Matnni tushunish' if grade==3 else 'Matndan xulosa chiqarish','comprehension',
       'Matnni boshidan oxirigacha o‘qing. Kim, nima, qayerda va nima sababdan degan savollarga matndan dalil toping. Sarlavha matndagi asosiy voqeani ifodalashi kerak. Javobni tekshirgach izohni ham o‘qing.',
       [dict(options=n,infer=grade==5) for n in (2,3,4)])

# Grade-specific logic beyond the preschool curricula.
logic=json.loads((ROOT/'logic_8.json').read_text())
for grade in (3,5):
 topic('logic',grade,'sequence','Sonli qonuniyatlar','rule_sequence',
       'Ketma-ketlikda sonlar qanday o‘zgarayotganini aniqlang. Bir xil son qo‘shilishi yoki bir xil songa ko‘paytirish qoidasini tekshiring. Qoidani har bir qo‘shni juftlikka qo‘llang.',
       [dict(maxStart=10+level*10,maxStep=level+2,multiply=grade==5,mode='choice' if level==1 else 'mixed') for level in (1,2,3)])
 topic('logic',grade,'ordering','Taqqoslashdan xulosa','ordering',
       'A B dan baland, B esa C dan baland bo‘lsa, tartib A → B → C bo‘ladi. Demak A eng baland, C eng past. Xulosani faqat berilgan ma’lumotdan chiqaring.')
 if grade==5:
  topic('logic',grade,'sets','Kesishuvchi guruhlar','set_count',
        'Ikki guruhdagi odamlarni qo‘shganda ikkala guruhga kiradiganlar ikki marta sanaladi. Umumiy son = birinchi guruh + ikkinchi guruh − ikkala guruhdagilar. Misol: 8 + 7 − 3 = 12.',
        [dict(mode=m) for m in ('choice','mixed','input')])
 for key in (['matrix2','coding','sudoku'] if grade==3 else ['matrix3','coding','sudoku']):
  src=next(t for t in logic['topics'] if t['id'].endswith('.'+key))
  levels=deepcopy(src['levels'])
  if grade==5: levels=[deepcopy(src['levels'][i]) for i in (1,2,2)]
  theory={'coding':'Buyruqlarni qahramon turgan katakdan boshlab bajaring. Har bir o‘q bitta katakka yurishni bildiradi. Chegaradan yoki to‘siqdan o‘tmasdan maqsadga olib boradigan yo‘lni tanlang.',
          'sudoku':'Har bir satr, ustun va belgilangan kichik kataklar guruhida har bir belgi bir martadan bo‘lsin. Bo‘sh katak uchun boshqa kataklardagi belgilarni chiqarib tashlab, qolganini toping.'}.get(key,'Satr va ustunlarda shakl, rang yoki miqdor qanday o‘zgarayotganini tekshiring. Yetishmagan katak ham shu qoidaga mos kelishi kerak. Ikkala yo‘nalishni solishtiring.')
  t=topic('logic',grade,key,src['title']['uz'],src['generator'],theory,levels);t['title']=src['title']
pairs('science',3,'living','O‘simliklar va hayvonlar',
 'Tirik tabiatga o‘simliklar va hayvonlar kiradi. O‘simlikning ildizi suvni shimadi, poyasi tayanch bo‘ladi, barglari yorug‘likda oziq modda hosil qilishda qatnashadi. Hayvonlarni yashash muhiti va belgilari bilan taqqoslang.', '''
Ildiz|O‘simlikni tuproqqa mahkamlaydigan va undan suv shimadigan qism.
Poya|Barg va gullarni tutib turadigan o‘simlik qismi.
Barg|O‘simlikning yorug‘likdan foydalanib oziq modda hosil qilishida asosiy qatnashadigan yassi yashil qismi.
Gul|Gulli o‘simlikning urug‘ hosil bo‘lishi bilan bog‘liq ko‘payish organi.
Urug‘|Qulay sharoitda unib, yangi o‘simlikka boshlang‘ich bo‘ladigan tuzilma.
Meva|Olma daraxtida urug‘larni o‘rab turadigan, gul tugunchasidan rivojlanadigan qism.
Nihol|Urug‘dan yaqinda o‘sib chiqqan yosh o‘simlik.
Daraxt|Asosiy yog‘ochlashgan tanasi bo‘lgan ko‘p yillik o‘simlik shakli.
Buta|Asosidan bir nechta yog‘ochlashgan poya chiqaradigan o‘simlik shakli.
Qush|Tanasi pat bilan qoplangan hayvon guruhi.
Baliq|Suvda yashab, jabralari yordamida nafas oladigan umurtqali hayvon guruhi.
Hasharot|Voyaga yetganida olti oyog‘i bo‘ladigan hayvon guruhi.
Sutemizuvchi|Bolalarini sut bilan oziqlantiradigan hayvon guruhi.
O‘txo‘r|Asosan o‘simlik bilan oziqlanadigan hayvon.
Yirtqich|Boshqa hayvonlarni ovlab oziqlanadigan hayvon.
''')
pairs('science',3,'environment','Suv, havo va ob-havo',
 'Suv qattiq, suyuq va gaz holatida uchraydi. Ob-havoni kuzatishda harorat, shamol va yog‘inga e’tibor beriladi. Atrofdagi o‘zgarishlarni nomlashdan oldin kuzatgan belgingizni aniqlang.', '''
Muz|Suvning qattiq holati.
Suv bug‘i|Suvning gaz holati.
Bug‘lanish|Suyuqlikning sirtidan gaz holatiga o‘tish jarayoni.
Erish|Muzning suyuq suvga aylanish jarayoni.
Muzlash|Suyuq suvning muzga aylanish jarayoni.
Yomg‘ir|Bulutdan suyuq suv tomchilari ko‘rinishida tushadigan yog‘in.
Qor|Bulutdan muz kristallari ko‘rinishida tushadigan yog‘in.
Shamol|Havoning Yer yuzasiga nisbatan harakati.
Termometr|Haroratni o‘lchash asbobi.
Bulut|Havoda muallaq turgan mayda suv tomchilari yoki muz kristallari to‘plami.
Tuman|Yer yuzasiga yaqin havoda mayda suv tomchilari to‘planishi.
Ko‘l|Quruqlikdagi tabiiy chuqurlikni egallagan suv havzasi.
Daryo|O‘zan bo‘ylab oqadigan tabiiy suv oqimi.
Buloq|Yer osti suvining tabiiy ravishda yer yuzasiga chiqadigan joyi.
Kamalak|Suv tomchilarida quyosh nuri bilan bog‘liq holda ko‘rinadigan rangli yoy.
''')
pairs('science',5,'matter','Modda va uning o‘zgarishlari',
 'Jism — alohida narsa, modda esa u nimadan tuzilganini bildiradi. Aralashmalarni ajratishda moddalarning eruvchanligi, zarracha o‘lchami va magnitga tortilishi kabi xususiyatlardan foydalaniladi.', '''
Modda|Jismlar tarkibini tashkil etadigan material: masalan, temir yoki suv.
Jism|Muayyan shakl va hajmga ega alohida narsa: masalan, qoshiq yoki shar.
Qattiq holat|Moddaning odatdagi sharoitda o‘z shakli va hajmini saqlaydigan holati.
Suyuq holat|Moddaning hajmini saqlab, idish shaklini oladigan holati.
Gaz holat|Moddaning berilgan idish bo‘shlig‘ini to‘ldirishga intiladigan holati.
Aralashma|Ikki yoki undan ortiq modda birga mavjud bo‘lgan tizim.
Eritma|Bir modda ikkinchisida bir tekis tarqalgan bir jinsli aralashma.
Erituvchi|Eritmada boshqa moddani eritadigan modda; tuzli suvda bu suvdir.
Filtrlash|Suvdagi erimagan qumni g‘ovak to‘siq yordamida ajratish usuli.
Bug‘latish|Tuzli suvdan suvni bug‘ga aylantirib chiqarish orqali tuzni ajratish usuli.
Magnit bilan ajratish|Temir qirindisini qumdan magnitga tortilishi asosida ajratish usuli.
Kondensatsiya|Suv bug‘ining sovib, suyuq tomchilarga aylanish jarayoni.
Diffuziya|Zarrachalarning tartibsiz harakati tufayli moddalarning o‘zaro tarqalish jarayoni.
Massa|Tarozida o‘lchanadigan, kilogramm bilan ifodalanadigan fizik kattalik.
Hajm|Jism yoki modda egallagan fazo miqdorini ifodalovchi kattalik.
''')
pairs('science',5,'ecosystems','Tabiatdagi bog‘lanishlar',
 'Ekotizimda organizmlar va muhit o‘zaro bog‘langan. Oziq zanjiridagi strelka oziq va energiya yo‘nalishini ko‘rsatadi. O‘simliklar, hayvonlar va parchalovchilar tabiatda turli vazifalarni bajaradi.', '''
Ekotizim|Tirik organizmlar va ularning yashash muhiti birgalikda hosil qiladigan o‘zaro bog‘liq tizim.
Yashash muhiti|Organizm hayot kechiradigan tabiiy sharoit va joy.
Populyatsiya|Muayyan hududda yashaydigan bir turga mansub organizmlar guruhi.
Produtsent|Yorug‘likdan foydalanib organik oziq hosil qiladigan yashil o‘simlik kabi organizm.
Konsument|Tayyor organik oziq bilan oziqlanadigan organizm.
Parchalovchi|O‘lik qoldiqlarni parchalaydigan zamburug‘ yoki bakteriya kabi organizm.
Oziq zanjiri|Organizmlar bir-biri bilan oziqlanishi orqali bog‘langan ketma-ketlik.
Oziq to‘ri|Bir nechta oziq zanjirining o‘zaro tutashgan tizimi.
Moslanish|Organizmning muhitida yashashiga yordam beradigan belgi yoki xususiyat.
Migratsiya|Hayvonlarning joylar orasidagi ko‘chishi, masalan, qushlarning mavsumiy ko‘chishi.
Changlanish|Changning urug‘chi tumshuqchasiga ko‘chishi jarayoni.
Urug‘larning tarqalishi|O‘simlik urug‘larining shamol, suv yoki hayvonlar orqali boshqa joyga ko‘chishi.
Biologik xilma-xillik|Tirik organizmlar turlari va boshqa biologik farqlarning boyligi.
Qo‘riqxona|Tabiatni saqlash uchun maxsus muhofaza qilinadigan hudud turi.
Qayta ishlash|Ishlatilgan materialdan yana foydalanish mumkin bo‘lgan mahsulot olish jarayoni.
''')
pairs('informatics',3,'devices','Kompyuter qurilmalari',
 'Kompyuterga ma’lumot kiritish, natijani chiqarish va saqlash uchun turli vositalar kerak. Klaviatura kiritadi, monitor ko‘rsatadi, printer qog‘ozga chiqaradi. Qurilmani uning vazifasiga qarab ajrating.', '''
Klaviatura|Kompyuterga harf va raqamlarni tugmalar yordamida kiritish qurilmasi.
Sichqoncha|Ko‘rsatkichni boshqarib, ekrandagi narsalarni tanlash qurilmasi.
Monitor|Kompyuterning tasvirini ekranda ko‘rsatish qurilmasi.
Printer|Matn yoki rasmni qog‘ozga chiqarish qurilmasi.
Skaner|Qog‘ozdagi rasm yoki matnning raqamli tasvirini olish qurilmasi.
Mikrofon|Ovozni kompyuterga kiritish qurilmasi.
Karnay|Kompyuterdagi ovozni eshittirish qurilmasi.
Veb-kamera|Kompyuterga video tasvir kiritish kamerasi.
Sensorli ekran|Barmoq tegishi orqali ham boshqariladigan ekran.
USB xotira|Fayllarni ko‘chirish uchun USB portga ulanadigan ixcham saqlash vositasi.
Fayl|Kompyuterda nom bilan saqlangan ma’lumotlar birligi.
Papka|Fayllarni tartib bilan guruhlash uchun ishlatiladigan joy.
Dastur|Kompyuter bajaradigan ko‘rsatmalar to‘plami.
Brauzer|Veb-sahifalarni ochish uchun ishlatiladigan dastur.
Kursor|Matn kiritiladigan joyni ko‘rsatadigan ekrandagi belgi.
''')
pairs('informatics',3,'safe_use','Raqamli odob va xavfsizlik',
 'Internetda ism, manzil va parol kabi shaxsiy ma’lumotlarni ehtiyot qiling. Noma’lum xabar yoki havolani kattalar bilan tekshiring. Boshqalar bilan muloyim gaplashing va ish orasida tanaffus qiling.', '''
Parol|Hisobga kirishni himoyalash uchun sir saqlanadigan belgilar ketma-ketligi.
Shaxsiy ma’lumot|Bolaning uy manzili, telefon raqami kabi unga tegishli maxfiy saqlanishi kerak bo‘lgan ma’lumot.
Ota-onadan yordam so‘rash|Begona kishi manzil so‘raganda bolaning ishonchli kattaga murojaat qilishi.
Havolani tekshirtirish|Noma’lum xabardagi tugmani bosishdan oldin ishonchli katta bilan manzilni tekshirish harakati.
Ruxsat olish|Birovning rasmini ulashishdan oldin uning roziligini so‘rash harakati.
Muloyim yozish|Suhbatdoshni haqorat qilmay, hurmat bilan xabar yuborish odati.
Tanaffus|Ekran oldidagi ishni vaqtincha to‘xtatib dam olish va harakatlanish.
Saqlash|Yozilgan hujjatdagi o‘zgarishlarni faylga yozib qo‘yish amali.
Zaxira nusxa|Asl fayl yo‘qolsa tiklash uchun saqlangan qo‘shimcha nusxa.
Hisobdan chiqish|Umumiy kompyuterda ish tugagach shaxsiy hisob seansini yopish amali.
Qurilmani qulflash|Qurilma qarovsiz qolganda undan boshqalarning foydalanishini cheklash amali.
Manbani ko‘rsatish|Boshqaning matni yoki rasmidan foydalanganda uning qayerdan olinganini yozish odati.
Xabarni tekshirish|Internetdagi da’voni ishonchli boshqa manba bilan solishtirish harakati.
Bloklash|Bezovta qilayotgan hisobdan keladigan muloqotni to‘sish vositasi.
Shikoyat yuborish|Platformaga nomaqbul xabar yoki hisob haqida bildirish vositasi.
''')
pairs('informatics',5,'files','Fayllar va axborot',
 'Fayl nomi va kengaytmasi uni tanishda yordam beradi. Fayllarni papkalarga tartiblang va muhim ishning zaxira nusxasini saqlang. Axborot matn, tasvir, ovoz va video shaklida bo‘lishi mumkin.', '''
Bit|Ikkita qiymatdan birini, odatda nol yoki birni ifodalovchi axborot birligi.
Bayt|Sakkiz bitdan iborat axborot birligi.
Fayl kengaytmasi|Fayl nomi oxiridagi nuqtadan keyin kelib, formatini tanishga yordam beradigan qism.
TXT|Oddiy matn fayli uchun keng ishlatiladigan kengaytma.
PNG|Rastrli tasvirni, jumladan shaffoflikni saqlay oladigan rasm formati.
MP3|Ovoz saqlash uchun ishlatiladigan siqilgan audio format.
PDF|Hujjatning sahifa ko‘rinishini saqlashga mo‘ljallangan format.
ZIP|Fayllarni bitta arxivga jamlash va siqish uchun ishlatiladigan format.
Nusxalash|Asl faylni qoldirib, boshqa joyda uning nusxasini yaratish amali.
Ko‘chirish|Faylni eski joyidan boshqa joyga o‘tkazish amali.
Nomini o‘zgartirish|Fayl mazmunini almashtirmasdan uning nomini yangilash amali.
Zaxiralash|Yo‘qotishdan himoyalash uchun ma’lumotlarning qo‘shimcha nusxasini saqlash amali.
Qidirish|Fayl yoki ma’lumotni nomi yoki belgilari orqali topish amali.
Operatsion tizim|Qurilma resurslarini boshqarib, dasturlar ishlashiga sharoit yaratadigan asosiy dasturiy tizim.
Algoritm|Vazifani bajarish uchun aniq va tartibli ko‘rsatmalar ketma-ketligi.
''')
pairs('informatics',5,'algorithms','Algoritm va dasturlash tushunchalari',
 'Algoritm qadamlari aniq bo‘lishi kerak. Ketma-ketlikda amallar navbat bilan bajariladi; tarmoqlanish shartga bog‘liq yo‘lni tanlaydi; takrorlash bir amalni qayta bajaradi. Natijani misollar bilan tekshiring.', '''
Ijrochi|Algoritmdagi buyruqlarni bajaradigan odam yoki qurilma.
Buyruq|Ijrochiga bitta ishni bajarishni bildiradigan ko‘rsatma.
Ketma-ketlik|Amallar birin-ketin bajariladigan algoritmik tuzilma.
Tarmoqlanish|Shart natijasiga qarab turli yo‘ldan birini tanlash tuzilmasi.
Takrorlash|Bir amal yoki amallar guruhini bir necha marta bajarish tuzilmasi.
Shart|Rost yoki yolg‘on deb baholanadigan tekshiruv.
O‘zgaruvchi|Qiymati dastur davomida o‘zgarishi mumkin bo‘lgan nomlangan saqlash joyi.
Kiritish|Dasturga boshlang‘ich ma’lumot berish amali.
Chiqarish|Dastur natijasini foydalanuvchiga taqdim etish amali.
Sinov|Dastur ishlashini tanlangan kirish ma’lumotlari bilan tekshirish jarayoni.
Xatoni tuzatish|Dasturdagi nuqsonni topib, uning sababini bartaraf etish jarayoni.
Blok-sxema|Algoritmni maxsus shakllar va strelkalar bilan ifodalash usuli.
Takrorlash soni|Sikl tanasi necha marta bajarilishini bildiradigan miqdor.
Cheksiz sikl|To‘xtash sharti bajarilmay, davom etaveradigan takrorlash.
Natija|Algoritm bajarilgandan keyin olinadigan yakuniy ma’lumot.
''')

# History: source literacy and calendar reasoning, avoiding fabricated dates/events.
rows=[]
source_examples={
 'Yozma manba':['qadimgi qo‘lyozma matni','yozilgan maktub','soliq haqidagi yozma hujjat','yozma shartnoma','yilnomadagi matn','eski gazeta maqolasi','safar kundaligi'],
 'Moddiy manba':['yozuvsiz sopol ko‘za','tosh mehnat quroli','yozuvsiz bronza bilaguzuk','qadimgi uy poydevori','yozuvsiz sopol haykalcha','suyakdan yasalgan igna','qadimgi o‘choq qoldig‘i'],
 'Og‘zaki manba':['avloddan avlodga og‘zaki aytilgan rivoyat','og‘zaki saqlangan xalq ertagi','voqea guvohining og‘zaki xotirasi','og‘zaki ijro etilgan doston','boboning voqea haqidagi og‘zaki hikoyasi','og‘zaki saqlangan xalq qo‘shig‘i','voqeani ko‘rgan odamning og‘zaki bayoni'],
}
for kind,examples in source_examples.items():
 for example in examples:
  rows.append((f'«{example}» ifoda shakliga ko‘ra qaysi turdagi tarixiy manba?',kind,[x for x in [*source_examples,'Tarixiy manba emas'] if x!=kind],f'Bu misolda ma’lumot {"yozuv" if kind.startswith("Yozma") else "buyum yoki inshoot" if kind.startswith("Moddiy") else "og‘zaki bayon"} orqali yetkazilgan.'))
bank('history',5,'sources','Tarixiy manbalar','O‘tmish haqidagi ma’lumot yozma, moddiy va og‘zaki manbalardan olinadi. Manbaning qachon, kim tomonidan va nima maqsadda yaratilganini so‘rang. Bitta manbadagi ma’lumotni boshqa dalillar bilan solishtiring.',rows)
topic('history',5,'centuries','Yil va asr','timeline','Bir asr — yuz yil. Milodiy birinchi asr 1–100-yillar, ikkinchi asr 101–200-yillar. 1901–2000-yillar yigirmanchi asr, 2001–2100-yillar yigirma birinchi asr. Yuzlikning oxirgi yili avvalgi asrga kiradi.',[dict(mode=m) for m in ('choice','mixed','input')])

# A second reading skill for each grade.
topic('reading',3,'reason','Sabab va natijani tushunish','comprehension',
      'Qahramon nima qilgani va uning natijasini ajrating. Xulosa matndagi dalilga mos bo‘lsin. Masalan, nihol parvarish qilinsa o‘sadi; unutmaslik uchun sana yozib qo‘yiladi.',
      [dict(options=n,infer=True) for n in (2,3,4)])
pairs('reading',5,'literature','Adabiy matnni tahlil qilish',
 'Badiiy matnni o‘qiganda voqea, qahramon va muallif aytmoqchi bo‘lgan asosiy fikrni ajrating. Asarning nomi, mavzusi va g‘oyasi bir xil tushuncha emas. Xulosangizni matndan dalil bilan asoslang.', '''
Muallif|Asarni yaratgan kishi.
Qahramon|Badiiy asardagi voqeada qatnashuvchi obraz.
Sarlavha|Asarning nomi.
Mavzu|Asarda nima haqida so‘z yuritilganini bildiradigan tushuncha.
G‘oya|Asar orqali ilgari surilgan asosiy fikr.
Voqealar ketma-ketligi|Asardagi hodisalarning qanday tartibda yuz bergani.
Dialog|Ikki yoki undan ortiq qahramonning o‘zaro suhbati.
Monolog|Bitta qahramonning kengroq nutqi yoki ichki o‘ylari bayoni.
Portret|Qahramonning tashqi ko‘rinishi tasviri.
Peyzaj|Badiiy asarda tabiat manzarasining tasviri.
O‘xshatish|Bir narsa yoki belgini boshqasiga qiyoslab tasvirlash usuli.
Jonlantirish|Jonsiz narsaga insonga xos xatti-harakat yoki xususiyat berish usuli.
Mubolag‘a|Ta’sirchanlik uchun belgini ataylab kuchaytirib tasvirlash usuli.
Qofiya|She’r misralari oxirida tovush jihatidan ohangdosh so‘zlarning kelishi.
Band|She’rda mazmun va tuzilish jihatidan birlashgan misralar guruhi.
''')

# Every added subject has a short mixed review using its real topic generators.
for (subject,grade),topics in list(CURRICULA.items()):
 ids=[t['id'] for t in topics]
 topic(subject,grade,'review','Bo‘limni takrorlash','test',
       'Bu mashg‘ulot oldingi mavzularni aralashtirib tekshiradi. Har bir savol shartini o‘qing. Yakunda xatolarni ko‘rib, shu mavzuning qoidasiga qayting.',
       [dict(topics=ids,level=n) for n in (1,2,3)])
 title=TITLES[subject]
 data=dict(subject=subject,ageGroup=f'g{grade}',lessonSize=6,
           title=dict(zip(('uz','en','ru'),title[:3])), model='QOIDA → MASHQ → IZOH → TAKRORLASH',topics=topics)
 if subject=='reading' and grade==5: data['title']=dict(uz='Adabiyot',en='Literature',ru='Литература')
 (OUT/f'{subject}_g{grade}.json').write_text(json.dumps(data,ensure_ascii=False,indent=1)+'\n')
for grade,items in BANKS.items():
 (OUT/f'bank_practice_g{grade}.json').write_text(json.dumps(dict(items=items),ensure_ascii=False,indent=1)+'\n')
print(f'{len(CURRICULA)} curricula; {sum(map(len,CURRICULA.values()))} topics; {sum(map(len,BANKS.values()))} authored questions')
