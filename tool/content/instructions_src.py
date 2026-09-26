# Ko'rsatmalar banki: `python3 tool/content/instructions_src.py` -> assets/data/instructions.json
# Har bir kalit: uz / en / ru (+ ixtiyoriy "speech" — ovoz uchun o'zbekcha matn).
# Qoida: ruscha va inglizcha matnlarda otni kelishikka solish shart bo'lmasin
# (ot ":" yoki qavs ichida), shunda har qanday so'z bilan grammatik to'g'ri chiqadi.
import json, os

I = {
 # --- Bir va ko'p
 "one_many_one":  ("Qayerda bitta {item} bor?", "Where is just one? ({item})", "Где только один? ({item})"),
 "one_many_many": ("Qayerda {item} ko‘p?", "Where are there many? ({item})", "Где много? ({item})"),
 "one_many_none": ("Qayerda hech narsa yo‘q?", "Where is there nothing?", "Где ничего нет?"),
 # --- Sanash
 "count_how_many": ("Nechta {item} bor?", "How many? ({item})", "Сколько? ({item})"),
 "find_group_n": ("{n} ta {item} bor rasmni top", "Find the picture with {n} ({item})", "Найди картинку, где {n} ({item})"),
 "find_numeral": ("{n} sonini top", "Find the number {n}", "Найди число {n}"),
 "match_number_group": ("Har bir sonni rasm bilan juftla", "Match each number with a picture", "Соедини каждое число с картинкой"),
 "count_dots": ("Nechta doira bor?", "How many dots are there?", "Сколько кружков?"),
 # --- Katta/kichik, ko'p/kam, uzun/qisqa
 "find_big": ("Eng kattasini top", "Find the biggest one", "Найди самый большой"),
 "find_small": ("Eng kichigini top", "Find the smallest one", "Найди самый маленький"),
 "where_more": ("Qayerda ko‘proq?", "Where are there more?", "Где больше?"),
 "where_less": ("Qayerda kamroq?", "Where are there fewer?", "Где меньше?"),
 "find_long": ("Eng uzun lentani top", "Find the longest ribbon", "Найди самую длинную ленту"),
 "find_short": ("Eng qisqa lentani top", "Find the shortest ribbon", "Найди самую короткую ленту"),
 # --- Joylashuv
 "which_high": ("Qaysi biri eng yuqorida?", "Which one is the highest?", "Что выше всех?"),
 "which_low": ("Qaysi biri eng pastda?", "Which one is the lowest?", "Что ниже всех?"),
 "which_left": ("Chapda qaysi biri turibdi?", "Which one is on the left?", "Что слева?"),
 "which_right": ("O‘ngda qaysi biri turibdi?", "Which one is on the right?", "Что справа?"),
 "which_middle": ("O‘rtada qaysi biri turibdi?", "Which one is in the middle?", "Что посередине?"),
 "first_from_left": ("Chapdan birinchisini top", "Find the first one from the left", "Найди первый слева"),
 "first_from_right": ("O‘ngdan birinchisini top", "Find the first one from the right", "Найди первый справа"),
 "nth_from_left": ("Chapdan {k}sini top", "Find the one at this place from the left: {k}", "Найди по счёту слева: {k}"),
 "nth_from_right": ("O‘ngdan {k}sini top", "Find the one at this place from the right: {k}", "Найди по счёту справа: {k}"),
 "points_right": ("O‘ngni ko‘rsatayotganini top", "Find the one pointing right", "Найди, что показывает вправо"),
 "points_left": ("Chapni ko‘rsatayotganini top", "Find the one pointing left", "Найди, что показывает влево"),
 "shelf_top": ("Eng yuqori javonda nima bor?", "What is on the top shelf?", "Что на верхней полке?"),
 "shelf_bottom": ("Eng pastki javonda nima bor?", "What is on the bottom shelf?", "Что на нижней полке?"),
 "shelf_middle": ("O‘rta javonda nima bor?", "What is on the middle shelf?", "Что на средней полке?"),
 "grid_left": ("{item}ning chap tomonida nima bor?", "What is to the left of it? ({item})", "Что слева? ({item})"),
 "grid_right": ("{item}ning o‘ng tomonida nima bor?", "What is to the right of it? ({item})", "Что справа? ({item})"),
 "grid_above": ("{item}ning tepasida nima bor?", "What is above it? ({item})", "Что сверху? ({item})"),
 "grid_below": ("{item}ning pastida nima bor?", "What is below it? ({item})", "Что снизу? ({item})"),
 "where_is": ("{item} qayerda?", "Where is it? ({item})", "Где он? ({item})"),
 # --- Ranglar va shakllar
 "find_color": ("{color} rangni top", "Find the colour {color}", "Найди цвет: {color}"),
 "find_color_object": ("{color} rangli narsani top", "Find something {color}", "Найди предмет, цвет — {color}"),
 "find_shape": ("{shape}ni top", "Find the {shape}", "Найди: {shape}"),
 "find_color_shape": ("{color} {shape}ni top", "Find the {color} {shape}", "Найди: {shape}, цвет — {color}"),
 "how_many_corners": ("{shape}ning nechta burchagi bor?", "How many corners does it have? ({shape})", "Сколько углов? ({shape})"),
 "object_shape": ("{item} qaysi shaklga o‘xshaydi?", "Which shape does it look like? ({item})", "На какую фигуру похоже? ({item})"),
 # --- Naqsh / ketma-ketlik
 "what_next": ("Keyingisi qaysi?", "What comes next?", "Что дальше?"),
 "continue_sequence": ("Qaysi son tushib qolgan?", "Which number is missing?", "Какое число пропущено?"),
 "count_by": ("{n} tadan sana. Keyingi son qaysi?", "Count in {n}s. What comes next?", "Считай по {n}. Какое число дальше?"),
 "count_pairs": ("Juftlab sana: hammasi nechta?", "Count in pairs: how many in all?", "Считай парами: сколько всего?"),
 "count_fingers": ("5 tadan sana: hammasi nechta?", "Count in fives: how many in all?", "Считай по пять: сколько всего?"),
 "count_tens": ("10 tadan sana: hammasi nechta?", "Count in tens: how many in all?", "Считай десятками: сколько всего?"),
 # --- Hisob
 "add_pictures": ("Hammasi bo‘lib nechta?", "How many altogether?", "Сколько всего?"),
 "sub_pictures": ("{n} tasini olib ketishdi. Nechta qoldi?", "{n} were taken away. How many are left?", "{n} забрали. Сколько осталось?"),
 "solve_add": ("{a} ga {b} ni qo‘sh", "Add {a} and {b}", "Сложи {a} и {b}"),
 "solve_sub": ("{a} dan {b} ni ayir", "Take {b} away from {a}", "Вычти {b} из {a}"),
 "make_ten": ("10 bo‘lishi uchun nechta kerak?", "How many more make 10?", "Сколько нужно добавить до 10?"),
 "missing_number": ("? o‘rniga qaysi son keladi?", "Which number goes in place of the ?", "Какое число вместо «?»"),
 "number_after": ("{n} dan keyin qaysi son keladi?", "Which number comes after {n}?", "Какое число идёт после {n}?"),
 "number_before": ("{n} dan oldin qaysi son keladi?", "Which number comes before {n}?", "Какое число идёт перед {n}?"),
 "number_between": ("{a} va {b} orasida qaysi son bor?", "Which number is between {a} and {b}?", "Какое число между {a} и {b}?"),
 "compare_sign": ("Qaysi belgi to‘g‘ri: katta, kichik yoki teng?", "Which sign fits: greater, less or equal?", "Какой знак: больше, меньше или равно?"),
 "which_bigger": ("Qaysi son katta?", "Which number is bigger?", "Какое число больше?"),
 "tens_and_ones": ("{t} ta o‘nlik va {o} ta birlik. Bu qaysi son?", "{t} tens and {o} ones. Which number is it?", "{t} десятков и {o} единиц. Какое это число?"),
 "can_pair": ("Hamma {item}ni juftlab bo‘ladimi?", "Can they all be put in pairs? ({item})", "Можно ли всё разложить парами? ({item})"),
 "find_even": ("Juft sonni top", "Find the even number", "Найди чётное число"),
 "find_odd": ("Toq sonni top", "Find the odd number", "Найди нечётное число"),
 "problem_add": ("{name}da {a} ta {item} bor edi. {name2} unga yana {b} ta berdi. {name}da hammasi nechta bo‘ldi?",
                 "{name} had {a} ({item}). {name2} gave {b} more. How many does {name} have now?",
                 "У {name} было {a} ({item}). {name2} дал(а) ещё {b}. Сколько стало у {name}?"),
 "problem_sub": ("{name}da {a} ta {item} bor edi. U {b} tasini {name2:ga} berdi. Nechta qoldi?",
                 "{name} had {a} ({item}) and gave {b} to {name2}. How many are left?",
                 "У {name} было {a} ({item}). {b} отдал(а) {name2}. Сколько осталось?"),
 "problem_compare": ("{name}da {a} ta {item}, {name2}da {b} ta {item} bor. {name}da nechta ko‘p?",
                     "{name} has {a} and {name2} has {b} ({item}). How many more does {name} have?",
                     "У {name} {a}, у {name2} {b} ({item}). На сколько у {name} больше?"),
 "what_time": ("Soat necha bo‘ldi?", "What time is it?", "Который час?"),
 "find_clock": ("{time} ni ko‘rsatayotgan soatni top", "Find the clock showing {time}", "Найди часы, которые показывают {time}"),
 "how_much_money": ("Hammasi bo‘lib necha so‘m?", "How much money in all?", "Сколько всего денег?"),
 "enough_money": ("{item} {n} so‘m turadi. Qaysi hamyonda pul yetadi?", "It costs {n} (sum). Which purse has enough? ({item})", "Стоит {n} сумов. В каком кошельке хватит денег? ({item})"),
 # --- Mantiq (4 yosh)
 "find_same": ("Xuddi shunday rasmni top", "Find the same picture", "Найди такую же картинку"),
 "odd_one_out": ("Qaysi biri ortiqcha?", "Which one does not belong?", "Что лишнее?"),
 "find_shadow": ("{item}ning soyasini top", "Find its shadow ({item})", "Найди тень ({item})"),
 "match_pairs": ("Bir-biriga mosini juftla", "Match the things that go together", "Соедини то, что подходит друг другу"),
 "animal_home": ("Har bir jonivorni uyiga olib bor", "Take each animal to its home", "Отведи каждого к его дому"),
 "sort_by_color": ("Rangiga qarab savatlarga sol", "Sort them by colour", "Разложи по цвету"),
 "sort_by_shape": ("Shakliga qarab savatlarga sol", "Sort them by shape", "Разложи по форме"),
 "sort_by_size": ("Kattalarini bir tomonga, kichiklarini boshqa tomonga sol", "Put big ones on one side and small ones on the other", "Большие — в одну сторону, маленькие — в другую"),
 "what_missing": ("Qaysi biri yo‘qoldi?", "What is missing?", "Что пропало?"),
 "maze_go": ("{hero}ni {target:ga} olib bor", "Help it reach the goal ({hero} → {target})", "Помоги дойти до цели ({hero} → {target})"),
 "analogy": ("Qaysi rasm mos keladi?", "Which picture fits?", "Какая картинка подходит?"),
 "complete_picture": ("Rasmning ikkinchi yarmini top", "Find the other half of the picture", "Найди вторую половинку картинки"),
 # --- Mantiq (6 yosh)
 "classify": ("Har birini o‘z guruhiga joyla", "Put each one in its group", "Разложи всё по группам"),
 "matrix_missing": ("Bo‘sh katakka qaysi rasm keladi?", "Which picture goes in the empty box?", "Какая картинка в пустой клетке?"),
 "same_rotated": ("Qaysi biri shu rasmning o‘zi, faqat burilgan?", "Which one is the same picture, just turned?", "Какая картинка та же, только повёрнута?"),
 "code_choose": ("Robot yulduzga qaysi yo‘l bilan boradi?", "Which program takes the robot to the goal?", "Какая программа приведёт робота к цели?"),
 "code_build": ("Strelkalardan yo‘l tuz va robotni yurgiz", "Build a path with arrows and run the robot", "Составь путь из стрелок и запусти робота"),
 "tangram_parts": ("{name} qaysi shakllardan tuzilgan?", "Which shapes make this picture? ({name})", "Из каких фигур эта картинка? ({name})"),
 "count_shapes_in_figure": ("Rasmda nechta {shape} bor?", "How many are in the picture? ({shape})", "Сколько их на картинке? ({shape})"),
 "tangram_missing": ("{name:ga} qaysi bo‘lak yetishmayapti?", "Which piece is missing? ({name})", "Какой детали не хватает? ({name})"),
 "sudoku": ("Bo‘sh kataklarni to‘ldir: har qator va ustunda belgilar takrorlanmasin", "Fill the empty boxes: no repeats in any row or column", "Заполни пустые клетки: в ряду и столбце без повторов"),
 "where_riddle": ("Qutiga qara. {item} qutining {p1} emas, {p2} ham emas. U qayerda?", "Look at the box. It is not {p1} the box and not {p2} it. Where is it? ({item})", "Посмотри на коробку. {item}: не {p1} и не {p2}. Где?"),
 "tallest": ("{a} {b}dan baland. {b} {c}dan baland. Kim eng baland?", "{a} is taller than {b}. {b} is taller than {c}. Who is the tallest?", "{a} выше, чем {b}. {b} выше, чем {c}. Кто самый высокий?"),
 "shortest": ("{a} {b}dan baland. {b} {c}dan baland. Kim eng past?", "{a} is taller than {b}. {b} is taller than {c}. Who is the shortest?", "{a} выше, чем {b}. {b} выше, чем {c}. Кто самый низкий?"),
 "race_first": ("{a} {b}dan oldinda yugurdi. {b} {c}dan oldinda. Kim birinchi keldi?", "{a} ran ahead of {b}. {b} was ahead of {c}. Who came first?", "{a} бежал впереди {b}. {b} — впереди {c}. Кто пришёл первым?"),
 "race_last": ("{a} {b}dan oldinda yugurdi. {b} {c}dan oldinda. Kim oxirgi keldi?", "{a} ran ahead of {b}. {b} was ahead of {c}. Who came last?", "{a} бежал впереди {b}. {b} — впереди {c}. Кто пришёл последним?"),
 "syllogism": ("{f1} {f2} {q}", "{f1} {f2} {q}", "{f1} {f2} {q}"),
}

out = {"schemaVersion": 1, "instructions": {}}
import re
for k, (uz, en, ru) in I.items():
    ph = lambda s: sorted(set(re.findall(r"\{(\w+)(?::\w+)?\}", s)))
    # Tarjimalar bir xil o'rinbosarlarga ega bo'lishi kerak (uz dagi p1/p2 kabi so'zlar bundan mustasno emas).
    assert ph(uz) == ph(en) == ph(ru), (k, ph(uz), ph(en), ph(ru))
    out["instructions"][k] = {"uz": uz, "en": en, "ru": ru}
path = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "data", "instructions.json")
json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(I), "instructions")
