# O'quv dasturlari manbasi: `python3 tool/content/curriculum_src.py`
# -> assets/data/math_4.json, logic_4.json, math_6.json, logic_6.json
#
# Har bir mavzu: id, code, emoji, title (uz/en/ru), generator, skill,
# prerequisites, levels (3 daraja — generator parametrlari).
# Metodik asos: bosqichma-bosqich murakkablashish (Xasanova metodikasi,
# Montessori, DONO BOLA mashq turlari) — mazmun original, generatorlar bilan yaratiladi.
import json, os

def T(id, code, emoji, uz, en, ru, gen, levels, skill=None, pre=(), tags=()):
    return {"id": id, "code": code, "emoji": emoji, "title": {"uz": uz, "en": en, "ru": ru},
            "generator": gen, "skill": skill or gen, "prerequisites": list(pre), "tags": list(tags),
            "levels": levels}

C3 = ["red", "yellow", "blue"]
C5 = ["red", "yellow", "blue", "green", "orange"]
C8 = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "brown"]

math4 = {
 "subject": "math", "ageGroup": "4", "ageMin": 3, "ageMax": 5, "lessonSize": 6,
 "title": {"uz": "Matematika", "en": "Maths", "ru": "Математика"},
 "model": "KO‘R → ESHIT → BOS → SUR → MOSLASHTIR → MAQTOV OL",
 "topics": [
  T("math4.one_many","M1","☝️","Bir va ko‘p","One and many","Один и много","one_many",
    [{"manyMin":5,"manyMax":7},{"manyMin":3,"manyMax":5},{"manyMin":3,"manyMax":6,"withEmpty":True}], skill="quantity"),
  T("math4.count_1_3","M2","🔢","1 dan 3 gacha","Numbers 1–3","Числа 1–3","count_objects",
    [{"min":1,"max":3,"modes":["count"]},{"min":1,"max":3,"modes":["count","group"]},{"min":1,"max":3,"modes":["drag","group","numeral"]}],
    skill="counting", pre=["math4.one_many"]),
  T("math4.count_1_5","M3","✋","1 dan 5 gacha","Numbers 1–5","Числа 1–5","count_objects",
    [{"min":1,"max":4,"modes":["count"]},{"min":1,"max":5,"modes":["count","group"]},{"min":1,"max":5,"modes":["drag","group","numeral"],"options":4}],
    skill="counting", pre=["math4.count_1_3"]),
  T("math4.count_1_10","M4","🔟","1 dan 10 gacha","Numbers 1–10","Числа 1–10","count_objects",
    [{"min":3,"max":7,"modes":["count"]},{"min":1,"max":10,"modes":["count","group"]},{"min":1,"max":10,"modes":["drag","group","numeral"],"options":4}],
    skill="counting", pre=["math4.count_1_5"]),
  T("math4.number_match","M5","🔗","Son va miqdor","Number and quantity","Число и количество","number_match",
    [{"pairs":2,"max":3},{"pairs":3,"max":5},{"pairs":4,"max":8}], skill="number_quantity", pre=["math4.count_1_5"]),
  T("math4.big_small","M6","🐘","Katta – kichik","Big and small","Большой – маленький","size_compare",
    [{"items":2,"ask":["big"],"gapPct":50},{"items":2,"ask":["big","small"],"gapPct":40},{"items":3,"ask":["big","small"],"gapPct":45}], skill="size"),
  T("math4.more_less","M7","⚖️","Ko‘p – kam","More and fewer","Больше – меньше","more_less",
    [{"max":7,"minDiff":3,"ask":["more"]},{"max":7,"minDiff":2,"ask":["more","less"]},{"max":9,"minDiff":1,"ask":["more","less"],"groups":3}], skill="compare_quantity", pre=["math4.count_1_5"]),
  T("math4.long_short","M8","📏","Uzun – qisqa","Long and short","Длинный – короткий","long_short",
    [{"items":2,"ask":["long"],"gapPct":50},{"items":2,"ask":["long","short"],"gapPct":35},{"items":3,"ask":["long","short"],"gapPct":45}], skill="length"),
  T("math4.high_low","M9","⬆️","Yuqori – past","High and low","Высоко – низко","high_low",
    [{"items":2,"ask":["high"]},{"items":2,"ask":["high","low"]},{"items":3,"ask":["high","low"]}], skill="position"),
  T("math4.left_right","M10","↔️","Chap – o‘ng","Left and right","Слева – справа","left_right",
    [{"items":2,"ask":["left"]},{"items":2,"ask":["left","right"]},{"items":3,"ask":["left","right","middle"]}], skill="position"),
  T("math4.colors","M11","🎨","Ranglar","Colours","Цвета","colors",
    [{"colors":C3,"options":3},{"colors":C5,"options":4},{"colors":["red","yellow","blue","green","orange","purple"],"options":3,"objects":True}], skill="colors"),
  T("math4.shapes","M12","🔺","Shakllar","Shapes","Фигуры","shapes",
    [{"shapes":["circle","square","triangle"],"options":3},{"shapes":["circle","square","triangle","rectangle","star","heart"],"options":4,"sameColor":False},{"shapes":["circle","square","triangle","star"],"options":4,"withColor":True}], skill="shapes"),
  T("math4.pattern","M13","🔁","Ketma-ketlik","Patterns","Закономерности","pattern",
    [{"patterns":["AB"],"kinds":["emoji","color"],"shown":4},{"patterns":["AB","AAB","ABC"],"kinds":["emoji","shape","color"],"shown":5},{"patterns":["ABB","AABB","ABC"],"kinds":["emoji","shape","color"],"shown":6,"drag":True}], skill="patterns"),
  T("math4.add_5","M14","➕","5 gacha qo‘shish","Adding to 5","Сложение до 5","add_pictures",
    [{"max":3},{"max":4},{"max":5,"drag":True}], skill="addition", pre=["math4.count_1_5"]),
  T("math4.sub_5","M15","➖","5 gacha ayirish","Taking away to 5","Вычитание до 5","sub_pictures",
    [{"max":3},{"max":4},{"max":5,"drag":True}], skill="subtraction", pre=["math4.add_5"]),
 ]}

logic4 = {
 "subject": "logic", "ageGroup": "4", "ageMin": 3, "ageMax": 5, "lessonSize": 6,
 "title": {"uz": "Mantiq", "en": "Logic", "ru": "Логика"},
 "model": "KO‘R → ESHIT → BOS → SUR → MOSLASHTIR → MAQTOV OL",
 "topics": [
  T("logic4.same","L1","👀","Bir xilini top","Find the same","Найди такой же","same_find",
    [{"options":3},{"options":3,"sameCategory":True,"drag":True},{"options":4,"sameCategory":True,"mirror":True}], skill="visual_match"),
  T("logic4.odd","L2","🙅","Ortig‘ini top","Odd one out","Что лишнее?","odd_one",
    [{"items":3},{"items":4},{"items":4,"near":True}], skill="odd_one_out"),
  T("logic4.shadow","L3","🌑","Soyasini top","Find the shadow","Найди тень","shadow",
    [{"options":3},{"options":3,"sameCategory":True,"drag":True},{"options":4,"sameCategory":True}], skill="shadow"),
  T("logic4.pairs","L4","🧦","Juftini top","Find the pair","Найди пару","pairs_match",
    [{"pairs":2},{"pairs":3},{"pairs":4}], skill="associations"),
  T("logic4.sort_color","L5","🌈","Rangiga qarab guruhla","Sort by colour","Разложи по цвету","sort_color",
    [{"bins":2,"items":4},{"bins":2,"items":6,"objects":True},{"bins":3,"items":6,"objects":True}], skill="classification"),
  T("logic4.sort_shape","L6","🔷","Shakliga qarab guruhla","Sort by shape","Разложи по форме","sort_shape",
    [{"bins":2,"items":4},{"bins":2,"items":6,"varySize":True},{"bins":3,"items":6,"varySize":True}], skill="classification"),
  T("logic4.sort_size","L7","📦","Katta-kichikni ajrat","Big or small","Большое и маленькое","sort_size",
    [{"items":4},{"items":6},{"items":6,"sameItem":False}], skill="size"),
  T("logic4.missing","L8","❔","Qaysi biri yo‘qoldi?","What is missing?","Что пропало?","missing_item",
    [{"items":3,"seconds":5},{"items":4,"seconds":5},{"items":5,"seconds":6}], skill="memory"),
  T("logic4.next","L9","⏭️","Navbatdagi rasm","What comes next","Что дальше?","next_picture",
    [{"patterns":["AB"],"kinds":["emoji"],"shown":4},{"growth":True},{"patterns":["ABC","AAB"],"kinds":["emoji"],"shown":5,"drag":True}], skill="patterns"),
  T("logic4.home","L10","🏡","Hayvonni uyiga olib bor","Take the animal home","Отведи зверя домой","habitat_match",
    [{"pairs":2},{"pairs":3},{"pairs":4}], skill="associations"),
  T("logic4.maze","L11","🌀","Labirint","Maze","Лабиринт","maze",
    [{"rows":3,"cols":3,"extraOpenings":2},{"rows":4,"cols":4,"extraOpenings":2},{"rows":5,"cols":5,"extraOpenings":1}], skill="maze"),
  T("logic4.analogy","L12","🧩","Mos rasmni top","Picture analogy","Аналогии","analogy",
    [{"relations":["eats","gives"],"options":3,"drag":True},{"relations":["eats","gives","goes_with"],"options":3},{"relations":["lives","weather","goes_with"],"options":4}], skill="analogy"),
  T("logic4.left_right","L13","👉","Chap va o‘ng","Left and right","Лево и право","direction",
    [{"modes":["row","arrows"],"items":2},{"modes":["arrows","row"],"hands":True,"items":3},{"modes":["arrows4","row"],"hands":True,"items":4}], skill="position"),
  T("logic4.up_down","L14","🗄️","Yuqori va past","Up and down","Верх и низ","shelves",
    [{"shelves":2},{"shelves":3,"ask":["top","bottom"]},{"shelves":3,"ask":["top","bottom","middle"]}], skill="position"),
  T("logic4.puzzle","L15","🧩","Rasmni to‘ldir","Finish the picture","Собери картинку","half_puzzle",
    [{"options":3},{"options":3,"sameCategory":True,"drag":True},{"options":4,"sameCategory":True}], skill="puzzle"),
 ]}

math6 = {
 "subject": "math", "ageGroup": "6", "ageMin": 6, "ageMax": 8, "lessonSize": 10,
 "title": {"uz": "Matematika", "en": "Maths", "ru": "Математика"},
 "model": "KO‘R → TUSHUN → TANLA → HISOBLA → YECH → IZOHNI KO‘R",
 "topics": [
  T("math6.count_10","M1","🔢","0 dan 10 gacha","Numbers 0–10","Числа 0–10","count_objects",
    [{"min":0,"max":10,"modes":["count"],"options":3},{"min":0,"max":10,"modes":["count","group"],"options":4},{"min":0,"max":10,"modes":["numeral","group","count"],"options":4}], skill="counting"),
  T("math6.count_20","M2","🧮","0 dan 20 gacha","Numbers 0–20","Числа 0–20","ten_frame",
    [{"min":8,"max":14},{"min":11,"max":20},{"min":5,"max":20}], skill="counting", pre=["math6.count_10"]),
  T("math6.neighbors","M3","↔️","Oldingi va keyingi son","Before and after","Соседи чисел","neighbors",
    [{"max":10,"ask":["after"]},{"max":20,"ask":["after","before"]},{"max":20,"ask":["after","before","between"]}], skill="number_order"),
  T("math6.compare","M4","⚖️","Katta, kichik, teng","Greater, less, equal","Больше, меньше, равно","compare_numbers",
    [{"max":10},{"max":20},{"max":10,"expressions":True}], skill="compare"),
  T("math6.add_10","M5","➕","10 ichida qo‘shish","Adding within 10","Сложение до 10","arith",
    [{"op":"+","max":8,"modes":["pictures"]},{"op":"+","max":10,"modes":["plain"]},{"op":"+","max":10,"modes":["plain","maketen"]}], skill="addition", pre=["math6.count_10"]),
  T("math6.sub_10","M6","➖","10 ichida ayirish","Subtracting within 10","Вычитание до 10","arith",
    [{"op":"-","max":8,"modes":["pictures"]},{"op":"-","max":10,"modes":["plain"]},{"op":"-","max":10,"modes":["plain"]}], skill="subtraction", pre=["math6.add_10"]),
  T("math6.add_20","M7","🔼","20 ichida qo‘shish","Adding within 20","Сложение до 20","arith",
    [{"op":"+","max":20,"modes":["tens"]},{"op":"+","max":20,"modes":["nocarry"]},{"op":"+","max":20,"modes":["carry","nocarry"]}], skill="addition", pre=["math6.add_10"]),
  T("math6.sub_20","M8","🔽","20 ichida ayirish","Subtracting within 20","Вычитание до 20","arith",
    [{"op":"-","max":20,"modes":["tens"]},{"op":"-","max":20,"modes":["nocarry"]},{"op":"-","max":20,"modes":["carry","nocarry"]}], skill="subtraction", pre=["math6.sub_10"]),
  T("math6.missing","M9","❓","Yetishmayotgan son","Missing number","Пропущенное число","missing_number",
    [{"max":10,"forms":["a+?=c"]},{"max":10,"forms":["a+?=c","?+b=c","a-?=b"]},{"max":20,"forms":["a+?=c","?+b=c","a-?=b","?-a=b"]}], skill="missing_number", pre=["math6.add_10","math6.sub_10"]),
  T("math6.sequence","M10","🔁","Sonli ketma-ketlik","Number patterns","Числовые ряды","sequence",
    [{"steps":["1"],"max":20,"length":4},{"steps":["2","-1"],"max":20,"length":4},{"steps":["2","3","-2","5"],"max":30,"length":4,"missingInside":True}], skill="number_patterns"),
  T("math6.even","M11","👯","Juft va toq","Odd and even","Чётные и нечётные","even_odd",
    [{"modes":["pairs"]},{"modes":["pairs","even"],"max":10},{"modes":["even","odd"],"max":20}], skill="parity"),
  T("math6.by_2","M12","🧦","2 tadan sanash","Counting in 2s","Счёт двойками","skip_count",
    [{"step":2,"modes":["groups"],"maxGroups":5},{"step":2,"modes":["sequence"],"maxGroups":8},{"step":2,"modes":["groups","sequence"],"maxGroups":10}], skill="skip_counting"),
  T("math6.by_5","M13","✋","5 tadan sanash","Counting in 5s","Счёт пятёрками","skip_count",
    [{"step":5,"modes":["groups"],"maxGroups":4},{"step":5,"modes":["sequence"],"maxGroups":8},{"step":5,"modes":["groups","sequence"],"maxGroups":10}], skill="skip_counting"),
  T("math6.by_10","M14","🔟","10 tadan sanash","Counting in 10s","Счёт десятками","skip_count",
    [{"step":10,"modes":["groups"],"maxGroups":5},{"step":10,"modes":["sequence"],"maxGroups":9},{"step":10,"modes":["groups","sequence"],"maxGroups":10}], skill="skip_counting"),
  T("math6.hundred","M15","💯","0 dan 100 gacha","Numbers to 100","Числа до 100","hundred",
    [{"modes":["read"]},{"modes":["tens_ones","read"]},{"modes":["compare","tens_ones"]}], skill="place_value", pre=["math6.by_10"]),
  T("math6.word","M16","📖","Matnli masalalar","Word problems","Задачи","word_problem",
    [{"types":["add"],"max":10},{"types":["add","sub"],"max":10},{"types":["add","sub","compare"],"max":20}], skill="word_problems", pre=["math6.add_10","math6.sub_10"]),
  T("math6.shapes","M17","🔷","Shakllar","Shapes","Фигуры","shapes6",
    [{"modes":["name"],"options":4},{"modes":["name","corners"]},{"modes":["corners","objects"]}], skill="shapes"),
  T("math6.spatial","M18","🧭","Fazoviy tushunchalar","Where is it?","Где находится?","spatial",
    [{"modes":["box"]},{"modes":["box","ordinal"],"items":5},{"modes":["ordinal","grid"],"items":6}], skill="spatial"),
  T("math6.clock","M19","🕒","Soat","Telling the time","Часы","clock",
    [{},{"half":True},{"half":True,"reverse":True}], skill="time"),
  T("math6.money","M20","💰","Pul bilan tanishamiz","Money","Деньги","money",
    [{"modes":["count"],"max":10},{"modes":["mixed"],"max":10},{"modes":["mixed","enough"],"max":15}], skill="money", pre=["math6.add_10"]),
 ]}

logic6 = {
 "subject": "logic", "ageGroup": "6", "ageMin": 6, "ageMax": 8, "lessonSize": 8,
 "title": {"uz": "Mantiq", "en": "Logic", "ru": "Логика"},
 "model": "KO‘R → TUSHUN → TANLA → YECH → IZOHNI KO‘R",
 "topics": [
  T("logic6.picture_seq","L1","🖼️","Rasmli ketma-ketlik","Picture sequences","Ряды картинок","picture_sequence",
    [{"patterns":["ABC","AAB"],"kinds":["emoji","shape"],"shown":5},{"patterns":["AABB","ABB","ABC"],"kinds":["emoji","shape","color"],"shown":6,"growth":True},{"patterns":["AABB","ABBC","ABCB"],"kinds":["shape","color"],"shown":7,"growth":True}], skill="patterns"),
  T("logic6.number_seq","L2","🔢","Sonli ketma-ketlik","Number sequences","Числовые ряды","number_sequence",
    [{"steps":["1","2"],"max":20,"length":4},{"steps":["2","3","-1","-2"],"max":30,"length":4,"missingInside":True},{"steps":["3","4","5","-3","10"],"max":60,"length":4,"missingInside":True}], skill="number_patterns"),
  T("logic6.classify","L3","🗂️","Guruhlarga ajrat","Classification","Классификация","classify",
    [{"bins":2,"items":6},{"bins":2,"items":8},{"bins":3,"items":9}], skill="classification"),
  T("logic6.odd","L4","🙅","Ortiqchasini top","Odd one out","Что лишнее?","odd_attribute",
    [{"items":4},{"items":4},{"items":5}], skill="odd_one_out"),
  T("logic6.analogy","L5","🔗","Analogiya","Analogies","Аналогии","analogy6",
    [{"relations":["eats","gives","goes_with"],"options":3},{"relations":["lives","uses","weather"],"options":4},{"relations":["eats","gives","lives","uses","weather","goes_with"],"options":4}], skill="analogy"),
  T("logic6.pattern","L6","🌀","Naqsh qoidasi","Pattern rules","Правило узора","pattern6",
    [{"modes":["attr"]},{"modes":["rotate","attr"]},{"modes":["rotate"]}], skill="patterns"),
  T("logic6.matrix2","L7","🔲","2×2 matritsa","2×2 matrix","Матрица 2×2","matrix",
    [{"size":2,"drag":True},{"size":2},{"size":2,"rules":["shape_color","count"]}], skill="matrix"),
  T("logic6.matrix3","L8","🔳","3×3 matritsa","3×3 matrix","Матрица 3×3","matrix",
    [{"size":3},{"size":3,"rules":["shape_color","count"]},{"size":3,"rules":["count","shape_color"]}], skill="matrix", pre=["logic6.matrix2"]),
  T("logic6.maze","L9","🌀","Labirint","Maze","Лабиринт","maze6",
    [{"rows":5,"cols":5,"extraOpenings":1},{"rows":6,"cols":6},{"rows":7,"cols":7}], skill="maze"),
  T("logic6.rotation","L10","🔄","Buriladigan rasm","Turn the picture","Поверни картинку","rotation",
    [{"options":2},{"options":3},{"options":4}], skill="spatial"),
  T("logic6.grid","L11","🧭","Chap, o‘ng, yuqori, past","Left, right, up, down","Слева, справа, сверху, снизу","grid_position",
    [{"modes":["ordinal"],"items":5},{"modes":["grid"]},{"modes":["grid","ordinal"],"items":7}], skill="spatial"),
  T("logic6.coding","L12","🤖","Kodlash","Coding","Программирование","coding",
    [{"rows":3,"cols":3,"minSteps":2,"maxSteps":3},{"rows":4,"cols":4,"obstacles":2,"minSteps":3,"maxSteps":5},{"rows":4,"cols":4,"obstacles":3,"minSteps":3,"maxSteps":6,"build":True}], skill="coding"),
  T("logic6.tangram","L13","📐","Shakllardan rasm","Shape pictures","Картинки из фигур","tangram",
    [{"modes":["parts"]},{"modes":["parts","count"]},{"modes":["missing","count"]}], skill="tangram"),
  T("logic6.sudoku","L14","🔢","Mini-sudoku","Mini sudoku","Мини-судоку","sudoku",
    [{"size":4,"minBlanks":3,"maxBlanks":4,"symbols":["emoji"]},{"size":4,"minBlanks":5,"maxBlanks":7,"symbols":["emoji","colors"]},{"size":4,"minBlanks":8,"maxBlanks":10,"symbols":["numbers","emoji"]}], skill="sudoku"),
  T("logic6.problems","L15","💡","Mantiqiy masalalar","Logic puzzles","Логические задачи","logic_problem",
    [{"types":["where","taller"]},{"types":["taller","order","where"]},{"types":["order","syllogism","taller"]}], skill="reasoning"),
 ]}

# ============================================================ O'ZBEK TILI
def theme_topic(id, code, emoji, uz, en, ru, theme):
    return T(id, code, emoji, uz, en, ru, "word_listen",
             [{"theme": theme, "modes": ["listen"], "options": 3},
              {"theme": theme, "modes": ["listen"], "options": 3, "sameTheme": True, "drag": True},
              {"theme": theme, "modes": ["listen", "odd"], "options": 4, "sameTheme": True}],
             skill="vocabulary", tags=["theme:" + theme])

uzbek4 = {
 "subject": "uzbek", "ageGroup": "4", "ageMin": 3, "ageMax": 5, "lessonSize": 6,
 "title": {"uz": "O‘zbek tili", "en": "Uzbek", "ru": "Узбекский язык"},
 "model": "KO‘R → ESHIT → BOS → SUR → MOSLASHTIR → MAQTOV OL",
 "topics": [
  theme_topic("uzbek4.family","S1","👪","Men va oilam","Me and my family","Я и моя семья","family"),
  theme_topic("uzbek4.home","S2","🏠","Uy","Home","Дом","home"),
  theme_topic("uzbek4.kindergarten","S3","🎒","Bog‘cha","Kindergarten","Детский сад","kindergarten"),
  theme_topic("uzbek4.animals","S4","🐾","Hayvonlar","Animals","Животные","animals"),
  theme_topic("uzbek4.birds","S5","🐦","Qushlar","Birds","Птицы","birds"),
  theme_topic("uzbek4.fruits","S6","🍎","Mevalar","Fruit","Фрукты","fruits"),
  theme_topic("uzbek4.vegetables","S7","🥕","Sabzavotlar","Vegetables","Овощи","vegetables"),
  T("uzbek4.colors","S8","🎨","Ranglar","Colours","Цвета","colors",
    [{"colors":["red","yellow","blue"],"options":3},{"colors":["red","yellow","blue","green","white","black"],"options":4},{"colors":["red","yellow","blue","green","orange","purple"],"options":3,"objects":True}], skill="vocabulary"),
  T("uzbek4.numbers","S9","🔢","Sonlar","Numbers","Числа","number_words",
    [{"min":1,"max":3,"modes":["group"]},{"min":1,"max":5,"modes":["group"]},{"min":1,"max":10,"modes":["group"],"options":4}], skill="vocabulary"),
  theme_topic("uzbek4.body","S10","👂","Tana","My body","Тело","body"),
  theme_topic("uzbek4.clothes","S11","👕","Kiyim","Clothes","Одежда","clothes"),
  theme_topic("uzbek4.transport","S12","🚌","Transport","Transport","Транспорт","transport"),
  theme_topic("uzbek4.toys","S13","🧸","O‘yinchoqlar","Toys","Игрушки","toys"),
  theme_topic("uzbek4.nature","S14","🌳","Tabiat","Nature","Природа","nature"),
  theme_topic("uzbek4.professions","S15","👩‍🏫","Kasblar","Jobs","Профессии","professions"),
  T("uzbek4.first_sound","S16","👂","Tovushni top","First sound","Первый звук","first_sound",
    [{"options":3,"letters":["a","o","u","i","m","b","s","t","k","q"]},{"options":3},{"options":4}], skill="phonics"),
  T("uzbek4.letters","S17","🔤","Harfni tanish","Letters","Буквы","letter_find",
    [{"set":"vowels","options":3,"modes":["upper"]},{"set":"all","options":3,"modes":["upper"]},{"set":"consonants","options":4,"modes":["upper"]}], skill="letters"),
  T("uzbek4.letter_picture","S18","🅰️","Harf va rasm","Letter and picture","Буква и картинка","letter_picture",
    [{"pairs":2,"letters":["a","o","u","i","e","m","b","s","t","k"]},{"pairs":3},{"pairs":4}], skill="letters"),
 ]}

uzbek6 = {
 "subject": "uzbek", "ageGroup": "6", "ageMin": 6, "ageMax": 8, "lessonSize": 8,
 "title": {"uz": "O‘zbek tili", "en": "Uzbek", "ru": "Узбекский язык"},
 "model": "KO‘R → TUSHUN → TANLA → O‘QI → YECH → IZOHNI KO‘R",
 "topics": [
  T("uzbek6.letters","U1","🔤","Harf","Letters","Буквы","letter_find",
    [{"set":"vowels","options":3,"modes":["upper","lower"]},{"set":"consonants","options":4,"modes":["upper","lower"]},{"set":"digraphs","options":4,"similar":True,"modes":["upper","mixed"]}], skill="letters"),
  T("uzbek6.sounds","U2","👂","Tovush","Sounds","Звуки","first_sound",
    [{"options":3},{"options":4,"letters":["s","sh","ch","j","g","g‘","q","k","o","o‘","u","x","h"]},{"options":3,"position":"last"}], skill="phonics", pre=["uzbek6.letters"]),
  T("uzbek6.case","U3","🔠","Bosh va kichik harf","Capital and small letters","Заглавные и строчные","case_match",
    [{"pairs":3,"set":"vowels"},{"pairs":4,"set":"single"},{"pairs":5}], skill="letters", pre=["uzbek6.letters"]),
  T("uzbek6.syllables","U4","👏","Bo‘g‘in","Syllables","Слоги","syllables",
    [{"modes":["count"],"minSyl":1,"maxSyl":3},{"modes":["count","missing"],"maxSyl":3},{"modes":["build","missing"],"maxSyl":4,"extra":1}], skill="syllables", pre=["uzbek6.sounds"]),
  T("uzbek6.short_words","U5","📝","2–3 harfli so‘z","Short words","Короткие слова","word_read",
    [{"minLetters":2,"maxLetters":3,"modes":["read"]},{"minLetters":2,"maxLetters":3,"modes":["read","build"]},{"minLetters":2,"maxLetters":3,"modes":["build"],"extra":1}], skill="reading", pre=["uzbek6.syllables"]),
  T("uzbek6.long_words","U6","📖","4–6 harfli so‘z","Longer words","Длинные слова","word_read",
    [{"minLetters":4,"maxLetters":5,"modes":["read"]},{"minLetters":4,"maxLetters":6,"modes":["read","build"]},{"minLetters":4,"maxLetters":6,"modes":["build"],"extra":2}], skill="reading", pre=["uzbek6.short_words"]),
  T("uzbek6.picture_word","U7","🖼️","Rasmga mos so‘z","Word for the picture","Слово к картинке","picture_word",
    [{"similar":"none","maxLetters":5},{"similar":"first","maxLetters":6},{"similar":"theme","maxLetters":7,"options":4}], skill="reading"),
  T("uzbek6.fill_letter","U8","✍️","So‘zni to‘ldir","Missing letter","Пропущенная буква","fill_letter",
    [{"which":"vowel","maxLetters":4},{"which":"consonant","maxLetters":5},{"which":"any","maxLetters":6,"options":4}], skill="spelling"),
  T("uzbek6.build_sentence","U9","🧱","So‘zlardan gap tuz","Build a sentence","Составь предложение","build_sentence",
    [{"types":["this"]},{"types":["this","color","action"]},{"types":["action","count"]}], skill="sentences", pre=["uzbek6.long_words"]),
  T("uzbek6.read_sentence","U10","👓","Gapni o‘qi","Read the sentence","Прочитай предложение","read_sentence",
    [{"types":["this"]},{"types":["color","action"]},{"types":["action","count"]}], skill="sentences"),
  T("uzbek6.missing_word","U11","❓","Yetishmayotgan so‘z","Missing word","Пропущенное слово","missing_word",
    [{"options":3},{"options":3},{"options":4}], skill="sentences"),
  T("uzbek6.story","U12","📚","Kichik hikoya","Short story","Маленький рассказ","story",
    [{"modes":["picture"]},{"modes":["picture"],"long":True},{"modes":["picture","question"],"long":True}], skill="comprehension", pre=["uzbek6.read_sentence"]),
  T("uzbek6.text_question","U13","💬","Matn bo‘yicha savol","Questions about a text","Вопросы по тексту","story",
    [{"modes":["question"]},{"modes":["question"],"long":True},{"modes":["question"],"long":True}], skill="comprehension", pre=["uzbek6.story"]),
  T("uzbek6.picture_sentence","U14","🗨️","Rasm asosida gap","Sentence for a picture","Предложение по картинке","picture_sentence",
    [{"types":["this"]},{"types":["color","action"]},{"types":["action","count"]}], skill="sentences"),
 ]}

# ============================================================ YOZISH
def tr(items, **kw):
    d = {"items": items}; d.update(kw); return d

writing4 = {
 "subject": "writing", "ageGroup": "4", "ageMin": 3, "ageMax": 5, "lessonSize": 4,
 "title": {"uz": "Yozishni o‘rganaman", "en": "Learning to write", "ru": "Учусь писать"},
 "model": "KO‘R → BARMOQ BILAN YUR → MAQTOV OL",
 "topics": [
  T("writing4.lines","W1","📏","Chiziqlar","Lines","Линии","trace",
    [tr(["pre:vertical","pre:horizontal","pre:diagonal","pre:steps"]),
     tr(["pre:curve","pre:rainbow","pre:wave","pre:zigzag"]),
     tr(["pre:circle","pre:spiral","pre:loops","pre:waves2","pre:zigzag2"])], skill="prewriting"),
  T("writing4.dots","W2","🔵","Nuqtalarni birlashtir","Join the dots","Соедини точки","trace",
    [tr(["dots:tent","dots:diamond","dots:kite","dots:boat"]),
     tr(["dots:house","dots:arrow","dots:heart","dots:tent","dots:diamond"]),
     tr(["dots:star","dots:fish","dots:crown","dots:house","dots:heart"])], skill="fine_motor"),
  T("writing4.shapes","W3","⭕","Shakllar","Shapes","Фигуры","trace",
    [tr(["pre:circle","pre:square","pre:triangle","dots:diamond"]),
     tr(["pre:circle","pre:square","pre:triangle","pre:spiral","dots:kite"]),
     tr(["pre:spiral","pre:square","pre:triangle","dots:star","dots:heart"])], skill="fine_motor"),
  T("writing4.letters","W4","🔠","Katta harflar","Big letters","Большие буквы","trace",
    [tr(["glyph:I","glyph:L","glyph:T","glyph:E","glyph:F","glyph:H"]),
     tr(["glyph:O","glyph:U","glyph:V","glyph:A","glyph:X","glyph:Y"]),
     tr(["glyph:M","glyph:N","glyph:K","glyph:Z","glyph:S","glyph:B","glyph:D","glyph:P"])], skill="letters_writing"),
  T("writing4.left_right","W5","➡️","Chapdan o‘ngga","Left to right","Слева направо","trace",
    [tr(["pre:horizontal","pre:wave","pre:zigzag","pre:steps"], leftToRight=True, tolerancePct=125),
     tr(["pre:waves2","pre:zigzag2","pre:loops","pre:wave"], leftToRight=True, tolerancePct=115),
     tr(["pre:waves2","pre:zigzag2","pre:loops","pre:steps","pre:horizontal"], leftToRight=True)], skill="prewriting"),
 ]}

STRAIGHT = ["A","E","F","H","I","K","L","M","N","T","V","X","Y","Z"]
CURVED = ["B","D","G","J","O","P","Q","R","S","U"]
writing6 = {
 "subject": "writing", "ageGroup": "6", "ageMin": 6, "ageMax": 8, "lessonSize": 5,
 "title": {"uz": "Yozishni o‘rganaman", "en": "Learning to write", "ru": "Учусь писать"},
 "model": "KO‘R → YO‘NALISHNI TUSHUN → YOZ → TEKSHIR",
 "topics": [
  T("writing6.letters","W1","🔠","Harf konturidan yurish","Trace the letters","Обведи буквы","trace",
    [tr(["glyph:" + x for x in STRAIGHT]), tr(["glyph:" + x for x in CURVED]),
     tr(["glyph:O‘","glyph:G‘","glyph:SH","glyph:CH","glyph:NG","glyph:R","glyph:Q"])], skill="letters_writing"),
  T("writing6.digits","W2","🔢","Raqam yozish","Write numbers","Пишем цифры","trace",
    [tr(["glyph:0","glyph:1","glyph:2","glyph:3","glyph:4"]), tr(["glyph:5","glyph:6","glyph:7","glyph:8","glyph:9"]),
     tr(["glyph:" + str(i) for i in range(10)], tolerancePct=85)], skill="digits_writing"),
  T("writing6.words","W3","📝","Qisqa so‘z","Short words","Короткие слова","trace",
    [tr(["words:2"]), tr(["words:3"]), tr(["words:4"])], skill="words_writing", pre=["writing6.letters"]),
  T("writing6.shapes","W4","🔷","Shakllar","Shapes","Фигуры","trace",
    [tr(["pre:square","pre:triangle","pre:circle","dots:diamond","dots:kite"]),
     tr(["dots:star","dots:crown","dots:fish","pre:spiral","dots:arrow"]),
     tr(["dots:star","dots:crown","dots:fish","dots:heart","dots:house"], tolerancePct=85)], skill="fine_motor"),
  T("writing6.patterns","W5","〰️","Naqshlar","Patterns","Узоры","trace",
    [tr(["pre:wave","pre:zigzag","pre:steps","pre:loops","pre:rainbow"]),
     tr(["pre:waves2","pre:zigzag2","pre:loops","pre:spiral","pre:curve"]),
     tr(["pre:waves2","pre:zigzag2","pre:loops","pre:spiral","pre:steps"], tolerancePct=85)], skill="prewriting"),
  T("writing6.left_right","W6","➡️","Chapdan o‘ngga yozish","Left to right","Слева направо","trace",
    [tr(["pre:horizontal","pre:wave","pre:zigzag","pre:steps","pre:loops"], leftToRight=True, tolerancePct=115),
     tr(["pre:waves2","pre:zigzag2","pre:loops","pre:wave","pre:steps"], leftToRight=True),
     tr(["pre:waves2","pre:zigzag2","pre:loops","pre:wave","pre:steps"], leftToRight=True, tolerancePct=85)], skill="prewriting"),
 ]}

# ============================================================ ENGLISH / РУССКИЙ / 3 TILDA
C10 = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "brown", "black", "white"]

def voc4(theme, opts3=3, opts4=4):
    """4 yosh lug'at mavzusi: eshit → rasm; 2-darajadan chalg'ituvchilar shu mavzudan."""
    return [{"themes": [theme], "modes": ["listen"], "options": opts3},
            {"themes": [theme], "modes": ["listen"], "options": opts3, "sameTheme": True},
            {"themes": [theme], "modes": ["listen"], "options": opts4, "sameTheme": True}]

def voc6(themes):
    """6 yosh lug'at mavzusi: eshit/o'qi → rasm → rasmga so'z."""
    return [{"themes": themes, "modes": ["listen", "read"], "options": 3},
            {"themes": themes, "modes": ["read", "picture_word"], "options": 3, "sameTheme": True},
            {"themes": themes, "modes": ["picture_word", "read", "listen"], "options": 4, "sameTheme": True}]

def lang4(prefix, subject, title, names):
    """4 yosh (ingliz/rus) dasturi. names: {key: (uz, en, ru)}."""
    n = lambda k: names[k]
    topics = []
    def add(key, emoji, gen, levels, skill, code):
        uz, en, ru = n(key)
        topics.append(T(prefix + "4." + key, code, emoji, uz, en, ru, gen, levels, skill=skill))
    i = 0
    def code():
        nonlocal i
        i += 1
        return ("E" if subject == "english" else "R") + str(i)
    add("colors", "🎨", "colors", [{"colors": C5, "options": 3, "modes": ["listen"]},
                                   {"colors": C8, "options": 3, "modes": ["listen"]},
                                   {"colors": C10, "options": 4, "modes": ["listen", "object"]}], "colors", code())
    add("numbers_5", "✋", "numbers", [{"min": 1, "max": 3, "modes": ["listen_digit", "listen_group"]},
                                      {"min": 1, "max": 5, "modes": ["listen_digit", "listen_group"]},
                                      {"min": 1, "max": 5, "modes": ["listen_digit", "listen_group"], "options": 4}], "numbers", code())
    add("numbers_10", "🔟", "numbers", [{"min": 1, "max": 6, "modes": ["listen_digit", "listen_group"]},
                                       {"min": 1, "max": 10, "modes": ["listen_digit", "listen_group"]},
                                       {"min": 1, "max": 10, "modes": ["listen_digit", "listen_group"], "options": 4}], "numbers", code())
    for key, emoji, theme in [("animals", "🐶", "animals"), ("family", "👨‍👩‍👧", "family"), ("body", "👃", "body"),
                              ("toys", "🧸", "toys"), ("school", "🎒", "school"), ("transport", "🚌", "transport"),
                              ("home", "🏠", "home"), ("fruits", "🍎", "fruits"), ("vegetables", "🥕", "vegetables"),
                              ("food", "🍞", "food"), ("clothes", "👕", "clothes")]:
        add(key, emoji, "vocab", voc4(theme), "vocabulary", code())
    add("actions", "🏃", "vocab", voc4("actions"), "actions", code())
    add("alphabet", "🔤", "alphabet_listen", [{"options": 3, "letters": list("abcdefgh") if subject == "english" else list("абвгдежзкл")},
                                             {"options": 3}, {"options": 4}], "alphabet", code())
    add("phrases", "👋", "vocab", [{"themes": ["phrases"], "modes": ["listen"], "options": 2},
                                   {"themes": ["phrases"], "modes": ["listen"], "options": 3},
                                   {"themes": ["phrases"], "modes": ["listen"], "options": 3}], "phrases", code())
    return {"subject": subject, "ageGroup": "4", "ageMin": 3, "ageMax": 5, "lessonSize": 6, "title": title,
            "model": "ESHIT → KO‘R → BOS → QAYTA ESHIT (🔊) → MAQTOV OL", "topics": topics}

EN_NAMES4 = {
 "colors": ("Ranglar", "Colours", "Цвета"), "numbers_5": ("1–5 sonlar", "Numbers 1–5", "Числа 1–5"),
 "numbers_10": ("1–10 sonlar", "Numbers 1–10", "Числа 1–10"), "animals": ("Hayvonlar", "Animals", "Животные"),
 "family": ("Oila", "Family", "Семья"), "body": ("Tana", "Body", "Тело"), "toys": ("O‘yinchoqlar", "Toys", "Игрушки"),
 "school": ("Bog‘cha va maktab", "School", "Школа"), "transport": ("Transport", "Transport", "Транспорт"),
 "home": ("Uy", "Home", "Дом"), "fruits": ("Mevalar", "Fruits", "Фрукты"), "vegetables": ("Sabzavotlar", "Vegetables", "Овощи"),
 "food": ("Taomlar", "Food", "Еда"), "clothes": ("Kiyimlar", "Clothes", "Одежда"), "actions": ("Harakatlar", "Actions", "Действия"),
 "alphabet": ("Alifbo", "Alphabet", "Алфавит"), "phrases": ("Salom!", "Hello!", "Привет!"),
}
english4 = lang4("english", "english", {"uz": "Ingliz tili", "en": "English", "ru": "Английский"}, EN_NAMES4)
russian4 = lang4("russian", "russian", {"uz": "Rus tili", "en": "Russian", "ru": "Русский язык"}, EN_NAMES4)

english6 = {
 "subject": "english", "ageGroup": "6", "ageMin": 6, "ageMax": 8, "lessonSize": 8,
 "title": {"uz": "Ingliz tili", "en": "English", "ru": "Английский"},
 "model": "KO‘R → ESHIT → TANLA → O‘QI → YOZ → IZOHNI KO‘R",
 "topics": [
  T("english6.alphabet","E1","🔤","Alifbo","Alphabet","Алфавит","letters",
    [{"set":"all","modes":["upper"],"options":3},{"set":"all","modes":["upper","lower"],"options":3,"similar":True},
     {"set":"all","modes":["mixed","lower"],"options":4,"similar":True}], skill="letters"),
  T("english6.case","E2","🔠","Katta va kichik harflar","Big and small letters","Большие и маленькие буквы","case_match",
    [{"pairs":3},{"pairs":4},{"pairs":5}], skill="letters", pre=["english6.alphabet"]),
  T("english6.phonics","E3","👂","Harf va tovush","Letters and sounds","Буквы и звуки","first_letter",
    [{"options":3,"letters":list("bcdfhmpst")},{"options":3},{"options":4}], skill="phonics", pre=["english6.alphabet"]),
  T("english6.numbers","E4","🔢","Sonlar 1–20","Numbers 1–20","Числа 1–20","numbers",
    [{"min":1,"max":10,"modes":["listen_digit","listen_group"]},{"min":1,"max":20,"modes":["listen_digit","read_word"]},
     {"min":1,"max":20,"modes":["read_word","match"],"pairs":4,"options":4}], skill="numbers"),
  T("english6.colors","E5","🎨","Ranglar","Colours","Цвета","colors",
    [{"colors":C8,"options":3,"modes":["listen","read"]},{"colors":C10,"options":3,"modes":["read","picture_word"]},
     {"colors":C10,"options":4,"modes":["picture_word","object","read"]}], skill="colors"),
  T("english6.animals","E6","🐾","Hayvonlar","Animals","Животные","vocab", voc6(["animals"]), skill="vocabulary"),
  T("english6.fruits_veg","E7","🍎","Meva va sabzavotlar","Fruit and vegetables","Фрукты и овощи","vocab", voc6(["fruits_veg"]), skill="vocabulary"),
  T("english6.food","E8","🍞","Taomlar","Food","Еда","vocab", voc6(["food"]), skill="vocabulary"),
  T("english6.family","E9","👨‍👩‍👧","Oila va tana","Family and body","Семья и тело","vocab", voc6(["family_body"]), skill="vocabulary"),
  T("english6.toys_school","E10","🎒","O‘yinchoq va maktab","Toys and school","Игрушки и школа","vocab", voc6(["toys_school"]), skill="vocabulary"),
  T("english6.transport","E11","🚌","Transport","Transport","Транспорт","vocab", voc6(["transport"]), skill="vocabulary"),
  T("english6.home","E12","🏠","Uy","Home","Дом","vocab", voc6(["home"]), skill="vocabulary"),
  T("english6.clothes","E13","👕","Kiyimlar","Clothes","Одежда","vocab", voc6(["clothes"]), skill="vocabulary"),
  T("english6.nature","E14","🌳","Tabiat","Nature","Природа","vocab", voc6(["nature"]), skill="vocabulary"),
  T("english6.jobs","E15","👩‍🚒","Kasblar va joylar","Jobs and places","Профессии и места","vocab", voc6(["jobs_places"]), skill="vocabulary"),
  T("english6.actions","E16","🏃","Harakatlar","Actions","Действия","vocab",
    [{"themes":["actions"],"modes":["listen"],"options":3},{"themes":["actions"],"modes":["listen","read"],"options":3},
     {"themes":["actions"],"modes":["read","picture_word"],"options":4}], skill="actions"),
  T("english6.opposites","E17","↔️","Qarama-qarshi so‘zlar","Opposites","Противоположности","opposites",
    [{"modes":["size","length"]},{"modes":["size","listen"],"options":3},{"modes":["read","listen","length"],"options":4}], skill="adjectives"),
  T("english6.spelling","E18","✏️","So‘z yig‘ish","Spelling","Собери слово","spell",
    [{"minLetters":3,"maxLetters":3},{"minLetters":3,"maxLetters":4,"extra":1},{"minLetters":4,"maxLetters":5,"extra":2}],
    skill="spelling", pre=["english6.phonics"]),
  T("english6.sentences","E19","📖","Oddiy gaplar","Simple sentences","Простые предложения","sentence",
    [{"types":["this"],"modes":["read"]},{"types":["this","color"],"modes":["read","picture"]},
     {"types":["color","count","action"],"modes":["read","picture","build"]}], skill="reading", pre=["english6.spelling"]),
  T("english6.listening","E20","🎧","Tinglab tushunish","Listening","Аудирование","sentence",
    [{"types":["this"],"modes":["listen"]},{"types":["this","color"],"modes":["listen"]},
     {"types":["color","count","action"],"modes":["listen"]}], skill="listening"),
  T("english6.phrases","E21","👋","Kundalik iboralar","Everyday phrases","Вежливые слова","vocab",
    [{"themes":["phrases"],"modes":["listen"],"options":3},{"themes":["phrases"],"modes":["listen","picture_word"],"options":3},
     {"themes":["phrases"],"modes":["picture_word"],"options":4}], skill="phrases"),
 ]}

russian6 = {
 "subject": "russian", "ageGroup": "6", "ageMin": 6, "ageMax": 8, "lessonSize": 8,
 "title": {"uz": "Rus tili", "en": "Russian", "ru": "Русский язык"},
 "model": "KO‘R → ESHIT → HARF → BO‘G‘IN → SO‘Z → GAP",
 "topics": [
  T("russian6.alphabet","R1","🔤","Alifbo","Alphabet","Алфавит","letters",
    [{"set":"all","modes":["upper"],"options":3},{"set":"all","modes":["upper","lower"],"options":3,"similar":True},
     {"set":"all","modes":["mixed","lower"],"options":4,"similar":True}], skill="letters"),
  T("russian6.sounds","R2","👂","Tovush va harf","Sounds and letters","Звуки и буквы","first_letter",
    [{"options":3,"letters":list("мпстклрбдн")},{"options":3},{"options":4}], skill="phonics", pre=["russian6.alphabet"]),
  T("russian6.vowels","R3","🅰️","Unli va undosh","Vowels and consonants","Гласные и согласные","vowels",
    [{"modes":["vowel"]},{"modes":["vowel","consonant"]},{"modes":["vowel","consonant"],"options":4}], skill="letters", pre=["russian6.alphabet"]),
  T("russian6.syllables","R4","👏","Bo‘g‘in","Syllables","Слоги","syllables",
    [{"modes":["count"],"maxSyl":3},{"modes":["count","missing"],"maxSyl":3},{"modes":["build","missing"],"maxSyl":4,"extra":1}],
    skill="syllables", pre=["russian6.vowels"]),
  T("russian6.colors","R5","🎨","Ranglar","Colours","Цвета","colors",
    [{"colors":C8,"options":3,"modes":["listen","read"]},{"colors":C10,"options":3,"modes":["read","picture_word"]},
     {"colors":C10,"options":4,"modes":["picture_word","object","read"]}], skill="colors"),
  T("russian6.numbers","R6","🔢","Sonlar 1–20","Numbers 1–20","Числа до 20","numbers",
    [{"min":1,"max":10,"modes":["listen_digit","listen_group"]},{"min":1,"max":20,"modes":["listen_digit","read_word"]},
     {"min":1,"max":20,"modes":["read_word","match"],"pairs":4,"options":4}], skill="numbers"),
  T("russian6.animals","R7","🐾","Hayvonlar va tabiat","Animals and nature","Животные и природа","vocab", voc6(["animals_nature"]), skill="vocabulary"),
  T("russian6.family","R8","👨‍👩‍👧","Oila va tana","Family and body","Семья и тело","vocab", voc6(["family_body"]), skill="vocabulary"),
  T("russian6.toys_school","R9","🎒","O‘yinchoq va maktab","Toys and school","Игрушки и школа","vocab", voc6(["toys_school"]), skill="vocabulary"),
  T("russian6.city","R10","🏙️","Shahar: transport va kasblar","Town: transport and jobs","Город: транспорт и профессии","vocab", voc6(["transport_city"]), skill="vocabulary"),
  T("russian6.food","R11","🍞","Taomlar","Food","Еда","vocab", voc6(["food_all"]), skill="vocabulary"),
  T("russian6.clothes_home","R12","👕","Kiyim va uy","Clothes and home","Одежда и дом","vocab", voc6(["clothes_home"]), skill="vocabulary"),
  T("russian6.actions","R13","🏃","Harakat, belgi, iboralar","Actions, qualities, phrases","Действия, признаки, вежливые слова","vocab",
    [{"themes":["actions","phrases"],"modes":["listen"],"options":3},
     {"themes":["actions","opposites","phrases"],"modes":["listen","read"],"options":3},
     {"themes":["actions","opposites","phrases"],"modes":["read","picture_word"],"options":4}], skill="actions"),
  T("russian6.spelling","R14","✏️","So‘z yig‘ish","Spelling","Собери слово","spell",
    [{"minLetters":3,"maxLetters":4},{"minLetters":3,"maxLetters":4,"extra":1},{"minLetters":4,"maxLetters":5,"extra":2}],
    skill="spelling", pre=["russian6.syllables"]),
  T("russian6.sentences","R15","📖","Oddiy gap","Simple sentences","Простое предложение","sentence",
    [{"types":["this"],"modes":["read"]},{"types":["this","color"],"modes":["read","picture","listen"]},
     {"types":["color","action"],"modes":["read","picture","listen","build"]}], skill="reading", pre=["russian6.spelling"]),
 ]}

TRI4 = [("fruits","🍎","Mevalar","Fruits","Фрукты"), ("animals","🐶","Hayvonlar","Animals","Животные"),
        ("toys","🧸","O‘yinchoqlar","Toys","Игрушки"), ("food","🍞","Taomlar","Food","Еда"),
        ("family_body","👨‍👩‍👧","Oila va tana","Family and body","Семья и тело"), ("transport","🚌","Transport","Transport","Транспорт"),
        ("clothes","👕","Kiyimlar","Clothes","Одежда"), ("home","🏠","Uy","Home","Дом"), ("vegetables","🥕","Sabzavotlar","Vegetables","Овощи")]
trilingual4 = {
 "subject": "trilingual", "ageGroup": "4", "ageMin": 3, "ageMax": 5, "lessonSize": 6,
 "title": {"uz": "3 tilda o‘rganamiz", "en": "Three languages", "ru": "Учим на трёх языках"},
 "model": "RASM → 🔊 O‘ZBEKCHA → 🔊 RUSCHA → 🔊 INGLIZCHA → TOP",
 "topics": [
  T("trilingual4." + key, "T%d" % (i + 1), emoji, uz, en, ru, "listen",
    [{"themes":[key],"modes":["all3"],"options":3},{"themes":[key],"modes":["all3","en","ru"],"options":3},
     {"themes":[key],"modes":["en","ru"],"options":4}], skill="three_languages")
  for i, (key, emoji, uz, en, ru) in enumerate(TRI4)
 ]}

trilingual6 = {
 "subject": "trilingual", "ageGroup": "6", "ageMin": 6, "ageMax": 8, "lessonSize": 8,
 "title": {"uz": "3 tilda o‘rganamiz", "en": "Three languages", "ru": "Учим на трёх языках"},
 "model": "RASM → 3 TIL → SOLISHTIR → TANLA → JUFTLA",
 "topics": [
  T("trilingual6.listen","T1","🔊","Eshit va top","Listen and find","Слушай и найди","listen",
    [{"themes":["fruits_veg","animals","toys_school"],"modes":["all3"]},{"themes":["fruits_veg","animals","toys_school"],"modes":["en","ru"]},
     {"themes":["fruits_veg","animals","toys_school"],"modes":["en","ru"],"options":4}], skill="three_languages"),
  T("trilingual6.what_is","T2","❓","Bu nima?","What is it?","Что это?","what_is",
    [{"themes":["food_all","family_body"],"langs":["ru"],"pictures":True},{"themes":["food_all","family_body"],"langs":["en"]},
     {"themes":["food_all","family_body"],"langs":["ru","en"],"options":4}], skill="three_languages"),
  T("trilingual6.which_lang","T3","🌍","Qaysi til?","Which language?","Какой язык?","which_lang",
    [{"themes":["animals_nature","clothes_home"],"langs":["en","ru"]},{"themes":["animals_nature","clothes_home"]},
     {"themes":["animals_nature","clothes_home","transport_city"]}], skill="three_languages"),
  T("trilingual6.match","T4","🔗","Juftla","Match","Соедини","match",
    [{"themes":["transport_city","toys_school"],"langs":["en"],"pairs":3},{"themes":["transport_city","toys_school"],"langs":["ru"],"pairs":4},
     {"themes":["transport_city","toys_school"],"langs":["en","ru"],"pairs":5}], skill="three_languages"),
  T("trilingual6.listen3","T5","🎧","Uch tilda eshit","Hear three languages","Слушай на трёх языках","listen",
    [{"themes":["animals_nature"],"modes":["all3"]},{"themes":["animals_nature","clothes_home"],"modes":["all3","en","ru"]},
     {"themes":["animals_nature","clothes_home"],"modes":["en","ru"],"options":4}], skill="three_languages"),
  T("trilingual6.russian_words","T6","🇷🇺","Ruscha so‘zlar","Russian words","Русские слова","what_is",
    [{"themes":["clothes_home","transport_city"],"langs":["ru"],"pictures":True},{"themes":["clothes_home","transport_city"],"langs":["ru"]},
     {"themes":["clothes_home","transport_city","animals_nature"],"langs":["ru"],"options":4}], skill="three_languages"),
  T("trilingual6.english_words","T7","🇬🇧","Inglizcha so‘zlar","English words","Английские слова","what_is",
    [{"themes":["animals_nature","food_all"],"langs":["en"],"pictures":True},{"themes":["animals_nature","food_all"],"langs":["en"]},
     {"themes":["animals_nature","food_all","family_body"],"langs":["en"],"options":4}], skill="three_languages"),
  T("trilingual6.match_ru","T8","🧩","Juftla: ruscha","Match: Russian","Соедини: русский","match",
    [{"themes":["family_body","food_all"],"langs":["ru"],"pairs":3},{"themes":["family_body","food_all"],"langs":["ru"],"pairs":4},
     {"themes":["family_body","food_all","clothes_home"],"langs":["ru","en"],"pairs":5}], skill="three_languages"),
 ]}

# ============================================================ SHAXMAT
def TL(size, *args, **kw):
    """Mavzuga xos dars hajmi bilan (AI bilan o'yin — 1 partiya)."""
    t = T(*args, **kw); t["lessonSize"] = size; return t

ALL_PIECES = ["K", "Q", "R", "B", "N", "P"]
def mv(types, sizes=(5, 5, 6), blockers=(0, 0, 1), coords=False):
    return [{"types": types, "size": sizes[i], "blockers": blockers[i], "coords": coords} for i in range(3)]

chess4 = {
 "subject": "chess", "ageGroup": "4", "ageMin": 3, "ageMax": 5, "lessonSize": 5,
 "title": {"uz": "Shaxmat", "en": "Chess", "ru": "Шахматы"},
 "model": "KO‘R → TANI → BOS → SUR → MAQTOV OL",
 "topics": [
  T("chess4.board","C1","⬜","Oq va qora kataklar","Light and dark squares","Белые и чёрные клетки","board_tap",
    [{"size":4,"modes":["light","dark"]},{"size":5,"modes":["light","dark"]},{"size":6,"modes":["light","dark"]}], skill="board"),
  T("chess4.star","C2","⭐","Yulduzchani top","Find the star","Найди звёздочку","board_tap",
    [{"size":5,"modes":["star"]},{"size":5,"modes":["star"]},{"size":6,"modes":["star"]}], skill="board"),
  T("chess4.king_queen","C3","♔","Shoh va vazir","King and queen","Король и ферзь","piece_tap",
    [{"size":5,"types":["K","Q"],"count":2},{"size":5,"types":["K","Q","R"],"count":3},{"size":5,"types":["K","Q","R","B"],"count":3}], skill="pieces"),
  T("chess4.rook_bishop","C4","♖","Rux va fil","Rook and bishop","Ладья и слон","piece_tap",
    [{"size":5,"types":["R","B"],"count":2},{"size":5,"types":["R","B","K"],"count":3},{"size":5,"types":["R","B","Q","K"],"count":4}], skill="pieces"),
  T("chess4.knight_pawn","C5","♘","Ot va piyoda","Knight and pawn","Конь и пешка","piece_tap",
    [{"size":5,"types":["N","P"],"count":2},{"size":5,"types":["N","P","R"],"count":3},{"size":5,"types":["N","P","B","R"],"count":4}], skill="pieces"),
  T("chess4.names","C6","🗣️","Figuralar nomi (3 tilda)","Piece names (3 languages)","Названия фигур (3 языка)","piece_name",
    [{"types":ALL_PIECES,"modes":["find"],"options":2},{"types":ALL_PIECES,"modes":["find","three_lang"],"options":3},
     {"types":ALL_PIECES,"modes":["three_lang","find"],"options":4}], skill="pieces"),
  T("chess4.rook_move","C7","♖","Rux yurishi","How the rook moves","Как ходит ладья","move_star", mv(["R"]), skill="moves", pre=["chess4.rook_bishop"]),
  T("chess4.bishop_move","C8","♗","Fil yurishi","How the bishop moves","Как ходит слон","move_star", mv(["B"]), skill="moves", pre=["chess4.rook_bishop"]),
  T("chess4.king_move","C9","♔","Shoh yurishi","How the king moves","Как ходит король","move_star", mv(["K"]), skill="moves", pre=["chess4.king_queen"]),
  T("chess4.queen_move","C10","♕","Vazir yurishi","How the queen moves","Как ходит ферзь","move_star", mv(["Q"]), skill="moves", pre=["chess4.king_queen"]),
  T("chess4.knight_move","C11","♘","Ot yurishi","How the knight moves","Как ходит конь","move_star", mv(["N"]), skill="moves", pre=["chess4.knight_pawn"]),
  T("chess4.all_moves","C12","♟️","Hamma figuralar yuradi","All pieces move","Все фигуры ходят","move_star",
    mv(["P","N","R","B","Q","K"], sizes=(5, 6, 6), blockers=(0, 1, 2)), skill="moves"),
 ]}

chess6 = {
 "subject": "chess", "ageGroup": "6", "ageMin": 6, "ageMax": 8, "lessonSize": 6,
 "title": {"uz": "Shaxmat", "en": "Chess", "ru": "Шахматы"},
 "model": "KO‘R → TUSHUN → YUR → TEKSHIR → IZOHNI KO‘R",
 "topics": [
  T("chess6.board","C1","⬜","Doska: oq va qora kataklar","The board: light and dark squares","Доска: белые и чёрные клетки","board_tap",
    [{"size":8,"modes":["light","dark"],"coords":True},{"size":8,"modes":["light","dark","star"],"coords":True},{"size":8,"modes":["dark","light"],"coords":True}], skill="board"),
  T("chess6.coords","C2","🔡","Qator va ustun (a1–h8)","Ranks and files (a1–h8)","Горизонтали и вертикали (a1–h8)","board_tap",
    [{"size":8,"modes":["square"]},{"size":8,"modes":["square"]},{"size":8,"modes":["square"]}], skill="board", pre=["chess6.board"]),
  T("chess6.names","C3","🗣️","Figuralar 3 tilda","Pieces in 3 languages","Фигуры на 3 языках","piece_name",
    [{"types":ALL_PIECES,"modes":["find","name"],"options":3},{"types":ALL_PIECES,"modes":["name","three_lang"],"options":4},
     {"types":ALL_PIECES,"modes":["three_lang","name","find"],"options":4}], skill="pieces"),
  T("chess6.rook","C4","♖","Rux yurishi","The rook","Ладья","move_star", mv(["R"], (8, 8, 8), (0, 2, 4), True), skill="moves", pre=["chess6.names"]),
  T("chess6.bishop","C5","♗","Fil yurishi","The bishop","Слон","move_star", mv(["B"], (8, 8, 8), (0, 2, 4), True), skill="moves", pre=["chess6.names"]),
  T("chess6.queen","C6","♕","Vazir yurishi","The queen","Ферзь","move_star", mv(["Q"], (8, 8, 8), (0, 2, 4), True), skill="moves", pre=["chess6.rook"]),
  T("chess6.knight","C7","♘","Ot yurishi","The knight","Конь","move_star", mv(["N"], (8, 8, 8), (0, 2, 4), True), skill="moves", pre=["chess6.names"]),
  T("chess6.king","C8","♔","Shoh yurishi","The king","Король","move_star", mv(["K"], (8, 8, 8), (0, 2, 3), True), skill="moves", pre=["chess6.names"]),
  T("chess6.pawn","C9","♙","Piyoda yurishi","The pawn","Пешка","move_star", mv(["P"], (8, 8, 8), (0, 2, 4), True), skill="moves", pre=["chess6.names"]),
  T("chess6.collect","C10","🌟","Yulduzchalarni yig‘","Collect the stars","Собери звёздочки","collect",
    [{"types":["R","Q","K"],"stars":2,"coords":True},{"types":["R","Q","K","N","B"],"stars":3,"coords":True},{"types":["N","B","Q"],"stars":4,"coords":True}], skill="moves"),
  T("chess6.capture","C11","⚔️","Olish","Capturing","Взятие","puzzle",
    [{"goals":["capture"],"coords":True},{"goals":["capture"],"extraBlack":1,"coords":True},{"goals":["capture"],"extraBlack":2,"coords":True}], skill="capture", pre=["chess6.pawn"]),
  T("chess6.safe_capture","C12","🛡️","Xavfsiz olish","Safe captures","Безопасное взятие","puzzle",
    [{"goals":["safe_capture"],"coords":True},{"goals":["safe_capture"],"coords":True},{"goals":["safe_capture"],"coords":True}], skill="capture", pre=["chess6.capture"]),
  T("chess6.check","C13","⚡","Shax","Check","Шах","puzzle",
    [{"goals":["check"],"coords":True},{"goals":["check"],"coords":True},{"goals":["check"],"coords":True}], skill="check", pre=["chess6.capture"]),
  T("chess6.escape","C14","🏃","Shaxdan qutulish","Getting out of check","Защита от шаха","puzzle",
    [{"goals":["escape"],"coords":True},{"goals":["escape"],"coords":True},{"goals":["escape"],"coords":True}], skill="check", pre=["chess6.check"]),
  T("chess6.defend","C15","🛡","Figurani himoya qil","Save your piece","Спаси фигуру","puzzle",
    [{"goals":["defend"],"coords":True},{"goals":["defend"],"coords":True},{"goals":["defend"],"coords":True}], skill="defence", pre=["chess6.capture"]),
  T("chess6.mate","C16","👑","Bir yurishda mat","Mate in one","Мат в один ход","puzzle",
    [{"goals":["mate"],"mates":["QK"],"coords":True},{"goals":["mate"],"mates":["RR","QK"],"coords":True},{"goals":["mate"],"mates":["RK","RR","QK"],"coords":True}],
    skill="mate", pre=["chess6.check"]),
  T("chess6.review","C17","🔁","Takrorlash","Review","Повторение","puzzle",
    [{"goals":["capture","check"],"coords":True},{"goals":["capture","check","escape","defend"],"coords":True},
     {"goals":["safe_capture","escape","defend","mate"],"coords":True}], skill="review", pre=["chess6.mate"]),
  TL(1, "chess6.pawn_war","C18","⚔️","Piyodalar jangi (AI)","Pawn battle (AI)","Битва пешек (ИИ)","play",
    [{"games":["pawn_war"],"ai":"very_easy","coords":True},{"games":["pawn_war"],"ai":"very_easy","coords":True},{"games":["pawn_war"],"ai":"easy","coords":True}],
    skill="game", pre=["chess6.pawn"]),
  TL(1, "chess6.queen_game","C19","♕","Vazir piyodalarga qarshi (AI)","Queen against pawns (AI)","Ферзь против пешек (ИИ)","play",
    [{"games":["queen_vs_pawns"],"ai":"very_easy","coords":True},{"games":["queen_vs_pawns"],"ai":"easy","coords":True},{"games":["queen_vs_pawns"],"ai":"easy","coords":True}],
    skill="game", pre=["chess6.queen"]),
  TL(1, "chess6.mini_game","C20","🏆","Mini-o‘yin: oson raqib","Mini game: easy opponent","Мини-игра: лёгкий соперник","play",
    [{"games":["rook_vs_pawns"],"ai":"very_easy","coords":True},{"games":["pawn_war"],"ai":"easy","coords":True},{"games":["pawn_war","queen_vs_pawns"],"ai":"easy","coords":True}],
    skill="game", pre=["chess6.pawn_war"]),
 ]}

base = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "data")
for name, data in [("uzbek_4", uzbek4), ("uzbek_6", uzbek6), ("writing_4", writing4), ("writing_6", writing6), ("english_4", english4), ("english_6", english6), ("russian_4", russian4), ("russian_6", russian6), ("trilingual_4", trilingual4), ("trilingual_6", trilingual6), ("chess_4", chess4), ("chess_6", chess6)]:
    ids = [t["id"] for t in data["topics"]]
    assert len(ids) == len(set(ids)), name
    for t in data["topics"]:
        assert len(t["levels"]) == 3, t["id"]
    with open(os.path.join(base, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(name, len(data["topics"]), "topics")

# Exact-age curricula. Base dictionaries above remain editable source material.
# Keep 4/6 identifiers stable so existing saved progress remains readable.
from copy import deepcopy

def for_age(source, age):
    data = deepcopy(source)
    subject = data['subject']
    old = data['ageGroup']
    data.update(ageGroup=str(age), ageMin=age, ageMax=age,
                lessonSize={3:4, 4:6, 5:7, 6:8, 7:9, 8:10}[age])
    for t in data['topics']:
        t['id'] = t['id'].replace(subject + old + '.', subject + str(age) + '.')
        t['prerequisites'] = [x.replace(subject + old + '.', subject + str(age) + '.')
                              for x in t['prerequisites']]
    if age == 3:
        allowed = ({'one_many','count_1_3','number_match','big_small','long_short',
                    'high_low','colors','shapes'} if subject == 'math' else
                   {'same','shadow','pairs','sort_color','sort_shape','missing','maze','puzzle'})
        data['topics'] = [t for t in data['topics'] if t['id'].split('.')[1] in allowed]
        for t in data['topics']:
            levels = t['levels']
            t['levels'] = [deepcopy(levels[i]) for i in [0,0,1]]
            for params in t['levels']:
                for key in ['options','pairs','bins']:
                    if key in params: params[key] = 2
                if t['generator'] == 'one_many': params.update(manyMin=2, manyMax=3)
                if t['generator'] == 'number_match': params.update(max=3, pairs=2)
                if t['generator'] == 'count_objects': params.update(max=3, options=2, modes=['count','group'])
                if t['generator'] == 'colors': params.update(colors=['red','yellow','blue'], options=2)
                if t['generator'] == 'shapes': params.update(shapes=['circle','square','triangle'], options=2)
                if t['generator'] == 'missing_item': params.update(items=3, seconds=7)
                if t['generator'] == 'maze': params.update(rows=3, cols=3, extraOpenings=2)
                if t['generator'] in ['sort_color','sort_shape']: params.update(items=4, bins=2)
    elif age == 5:
        for t in data['topics']:
            if t['generator'] in ['add_pictures','sub_pictures']:
                op = t['generator'] == 'add_pictures'
                t['id'] = subject + '5.' + ('add_10' if op else 'sub_10')
                t['title'] = {'uz': '10 ichida ' + ('qo‘shish' if op else 'ayirish'),
                              'en': ('Addition' if op else 'Subtraction') + ' within 10',
                              'ru': ('Сложение' if op else 'Вычитание') + ' в пределах 10'}
                t['levels'] = [{'max':5}, {'max':7}, {'max':10, 'drag':True}]
            elif t['generator'] == 'maze':
                t['levels'] = [{'rows':4,'cols':4,'extraOpenings':2},
                               {'rows':5,'cols':5,'extraOpenings':1}, {'rows':6,'cols':6}]
            elif t['generator'] == 'missing_item':
                t['levels'] = [{'items':4,'seconds':6}, {'items':5,'seconds':5}, {'items':6,'seconds':5}]
    elif age == 6:
        excluded = ({'add_20','sub_20','by_5','by_10','hundred'} if subject == 'math'
                    else {'matrix3','sudoku','problems'})
        data['topics'] = [t for t in data['topics'] if t['id'].split('.')[1] not in excluded]
        for t in data['topics']:
            levels = t['levels']
            t['levels'] = [deepcopy(levels[i]) for i in [0,0,1]]
    elif age == 7:
        for t in data['topics']:
            levels = t['levels']
            t['levels'] = [deepcopy(levels[i]) for i in [0,1,1]]
    valid = {t['id'] for t in data['topics']}
    for i,t in enumerate(data['topics'], 1):
        t['code'] = ('M' if subject == 'math' else 'L') + str(i)
        t['prerequisites'] = [x for x in t['prerequisites'] if x in valid]
    return data

for age in range(3,9):
    for source in ([math4,logic4] if age <= 5 else [math6,logic6]):
        data = for_age(source, age)
        name = data['subject'] + '_' + str(age)
        ids = [t['id'] for t in data['topics']]
        assert len(ids) == len(set(ids)), name
        for t in data['topics']: assert len(t['levels']) == 3, t['id']
        with open(os.path.join(base, name + '.json'), 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        print(name, len(data['topics']), 'topics')
