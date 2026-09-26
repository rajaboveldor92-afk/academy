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

base = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "data")
for name, data in [("math_4", math4), ("logic_4", logic4), ("math_6", math6), ("logic_6", logic6)]:
    ids = [t["id"] for t in data["topics"]]
    assert len(ids) == len(set(ids)), name
    for t in data["topics"]:
        assert len(t["levels"]) == 3, t["id"]
    with open(os.path.join(base, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(name, len(data["topics"]), "topics")
