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
 "find_big_shape": ("Eng katta shaklni tanla", "Choose the biggest shape", "Выбери самую большую фигуру"),
 "find_small_shape": ("Eng kichik shaklni tanla", "Choose the smallest shape", "Выбери самую маленькую фигуру"),
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
 "which_smaller": ("Qaysi son kichik?", "Which number is smaller?", "Какое число меньше?"),
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
 "odd_shape": ("Qaysi shakl boshqalardan farq qiladi?", "Which shape is different?", "Какая фигура отличается?"),
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
 # --- O'zbek tili
 "uz_find_word": ("{item}ni top", "Find: {item}", "Найди: {item}"),
 "uz_not_in_theme": ("Qaysi biri {theme} emas?", "Which one is not {theme}?", "Что здесь не {theme}?"),
 "uz_first_sound": ("Qaysi rasm «{l}» tovushi bilan boshlanadi?", "Which picture starts with the sound «{l}»?", "Какая картинка начинается на звук «{l}»?"),
 "uz_last_sound": ("Qaysi so‘z «{l}» tovushi bilan tugaydi?", "Which word ends with the sound «{l}»?", "Какое слово заканчивается на звук «{l}»?"),
 "uz_find_letter": ("«{l}» harfini top", "Find the letter «{l}»", "Найди букву «{l}»"),
 "uz_find_small_letter": ("«{l}» harfining kichigini top", "Find the small letter for «{l}»", "Найди строчную букву для «{l}»"),
 "uz_match_letter_picture": ("Harfni rasm bilan juftla", "Match each letter with a picture", "Соедини букву с картинкой"),
 "uz_match_case": ("Bosh harfni kichik harf bilan juftla", "Match capital and small letters", "Соедини заглавную и строчную букву"),
 "uz_count_syllables": ("Bu so‘zda nechta bo‘g‘in bor?", "How many syllables are in this word?", "Сколько слогов в этом слове?"),
 "uz_missing_syllable": ("Qaysi bo‘g‘in yetishmayapti?", "Which syllable is missing?", "Какого слога не хватает?"),
 "uz_build_syllables": ("Bo‘g‘inlardan so‘z yig‘", "Build the word from syllables", "Собери слово из слогов"),
 "uz_build_word": ("Rasmga qarab so‘zni harflardan yig‘", "Look at the picture and build the word", "Посмотри на картинку и собери слово"),
 "uz_read_word": ("So‘zni o‘qi va rasmini top", "Read the word and find its picture", "Прочитай слово и найди картинку"),
 "uz_picture_word": ("Rasmga mos so‘zni top", "Find the word for the picture", "Найди слово к картинке"),
 "uz_fill_letter": ("Qaysi harf tushib qolgan?", "Which letter is missing?", "Какая буква пропущена?"),
 "uz_build_sentence": ("So‘zlardan gap tuz", "Make a sentence from the words", "Составь предложение из слов"),
 "uz_read_sentence": ("Gapni o‘qi va mos rasmni top", "Read the sentence and find the picture", "Прочитай предложение и найди картинку"),
 "uz_missing_word": ("Gapga qaysi so‘z mos keladi?", "Which word fits the sentence?", "Какое слово подходит?"),
 "uz_story_picture": ("Hikoyani o‘qi va mos rasmni top", "Read the story and find the picture", "Прочитай рассказ и найди картинку"),
 "uz_story_question": ("Hikoyani o‘qi va savolga javob ber", "Read the story and answer the question", "Прочитай рассказ и ответь на вопрос"),
 "uz_picture_sentence": ("Rasmga mos gapni top", "Find the sentence for the picture", "Найди предложение к картинке"),
 # --- Yozish
 "wr_trace_line": ("Barmog‘ing bilan chiziq ustidan yur", "Trace the line with your finger", "Обведи линию пальцем"),
 "wr_trace_shape": ("Barmog‘ing bilan shakl ustidan yur", "Trace the shape with your finger", "Обведи фигуру пальцем"),
 "wr_dots": ("Nuqtalarni tartib bilan birlashtir", "Join the dots in order", "Соедини точки по порядку"),
 "wr_letter": ("«{l}» harfini yoz", "Write the letter «{l}»", "Напиши букву «{l}»"),
 "wr_digit": ("{n} raqamini yoz", "Write the number {n}", "Напиши цифру {n}"),
 "wr_word": ("«{w}» so‘zini yoz", "Write the word «{w}»", "Напиши слово «{w}»"),
 "wr_left_right": ("Chapdan o‘ngga yoz", "Write from left to right", "Пиши слева направо"),
}

# Shaxmat (ch_*)
I.update({
 "ch_tap_light": ("Oq katakni bos", "Tap a light square", "Нажми на белую клетку"),
 "ch_tap_dark": ("Qora katakni bos", "Tap a dark square", "Нажми на чёрную клетку"),
 "ch_tap_star": ("Yulduzchali katakni bos", "Tap the square with the star", "Нажми на клетку со звёздочкой"),
 "ch_tap_square": ("{sq} katagini bos", "Tap the square {sq}", "Нажми на клетку {sq}"),
 "ch_tap_piece": ("{piece}ni top", "Find the {piece}", "Найди фигуру: {piece}"),
 "ch_piece_name": ("Bu qaysi figura?", "Which piece is this?", "Какая это фигура?"),
 "ch_find_piece": ("{piece} qaysi biri?", "Which one is the {piece}?", "Где фигура: {piece}?"),
 "ch_three_lang": ("Uch tilda eshit: qaysi figura?", "Listen in three languages: which piece?", "Послушай на трёх языках: какая фигура?"),
 "ch_move_star": ("{piece}ni yulduzchaga olib bor", "Move the {piece} to the star", "Передвинь фигуру на звёздочку: {piece}"),
 "ch_collect": ("{piece} bilan hamma yulduzchalarni yig‘", "Collect all the stars with the {piece}", "Собери все звёздочки. Фигура: {piece}"),
 "ch_capture": ("Qora figurani ol", "Capture the black piece", "Возьми чёрную фигуру"),
 "ch_safe_capture": ("Himoyalanmagan qora figurani ol", "Capture the black piece that is not protected", "Возьми незащищённую чёрную фигуру"),
 "ch_check": ("Qora shohga shax ber", "Put the black king in check", "Объяви шах чёрному королю"),
 "ch_escape": ("Oq shohga shax! Uni qutqar", "The white king is in check! Save it", "Белому королю шах! Спаси его"),
 "ch_defend": ("Hujumdagi figurani qutqar", "Save the piece under attack", "Спаси фигуру от нападения"),
 "ch_mate": ("Bir yurishda mat qil", "Checkmate in one move", "Поставь мат в один ход"),
 "ch_play": ("O‘ynaymiz: {game}", "Let's play: {game}", "Играем: {game}"),
})

# Xotira, diqqat, puzzle, motorika, muloqot
I.update({
 "mem_cards": ("Bir xil rasmli kartalarni juftla", "Find the matching pairs", "Найди одинаковые пары"),
 "mem_recall": ("Rasmlar qanday tartibda edi? Shu tartibda bos", "Tap the pictures in the same order", "Нажми на картинки в том же порядке"),
 "mem_colors": ("Ranglar qanday tartibda edi? Shu tartibda bos", "Tap the colours in the same order", "Нажми на цвета в том же порядке"),
 "mem_changed": ("Nima o‘zgardi? Yangi narsani top", "What changed? Find the new thing", "Что изменилось? Найди новое"),
 "mem_was_there": ("Rasmda nima bor edi?", "What was in the picture?", "Что было на картинке?"),
 "mem_how_many": ("Rasmda nechta {item} bor edi?", "How many were there? ({item})", "Сколько было? ({item})"),
 "mem_where": ("{item} qayerda edi?", "Where was it? ({item})", "Где это было? ({item})"),
 "at_find": ("{item}ni top va bos", "Find and tap: {item}", "Найди и нажми: {item}"),
 "at_find_all": ("Hamma {item}larni top", "Find all of them: {item}", "Найди все: {item}"),
 "at_find_color": ("Hamma {color} narsalarni top", "Find everything {color}", "Найди всё, что {color}"),
 "at_difference": ("Pastki rasmda nima boshqacha? Uni bos", "What is different in the bottom picture? Tap it", "Что изменилось на нижней картинке? Нажми"),
 "at_count": ("Diqqat bilan sana: nechta {item} bor?", "Count carefully: how many? ({item})", "Посчитай внимательно: сколько? ({item})"),
 "pz_jigsaw": ("Bo‘laklardan rasmni yig‘", "Put the picture together", "Собери картинку"),
 "mo_bubbles": ("Hamma pufaklarni bosib yor", "Pop all the bubbles", "Лопни все пузыри"),
 "mo_drag_shadow": ("Rasmni soyasiga sudrab olib bor", "Drag the picture to its shadow", "Перетащи картинку к её тени"),
 "so_emotion_find": ("Qaysi yuz {emotion}?", "Which face is {emotion}?", "Какое лицо — {emotion}?"),
 "so_emotion_name": ("Bu bola qanday his qilyapti?", "How does this child feel?", "Что чувствует этот ребёнок?"),
 "so_situation": ("{text}", "{text} (How would you feel?)", "{text} (Что ты почувствуешь?)"),
 "so_polite": ("{text} Nima deysan?", "{text} What do you say?", "{text} Что ты скажешь?"),
 "so_polite_when": ("Qachon «{word}» deymiz?", "When do we say «{word}»?", "Когда говорят «{word}»?"),
 "so_choice": ("{text}", "{text}", "{text}"),
 "fa_activity": ("Bugun ota-onang bilan birga: {title}", "Today with your parents: {title}", "Сегодня вместе с родителями: {title}"),
})

# Chet tili darslari (lg_*): ekranda va ovozda — ingliz/rus tilida; o'zbekcha matn — faqat umumiy
# yordamchi (javobni oshkor qilmaydi), shuning uchun unda o'rinbosar bo'lmasligi mumkin.
LG = {
 "lg_listen": ("Eshit va rasmni top", "Listen and find", "Слушай и найди"),
 "lg_find": ("Eshit va rasmni top", "Find the {w}", "Где {w}?"),
 "lg_find_action": ("Eshit va rasmni top", "Who is {w}?", "Кто {w}?"),
 "lg_find_word": ("Eshit va rasmni top", "Find: {w}", "Найди: {w}"),
 "lg_find_phrase": ("Qachon shunday deymiz? Rasmni top", "When do we say: {w}", "Когда говорят: {w}"),
 "lg_read": ("O‘qi va rasmni top", "Read and find", "Прочитай и найди"),
 "lg_what": ("Bu nima? So‘zni tanla", "What is this?", "Что это?"),
 "lg_what_action": ("U nima qilyapti? So‘zni tanla", "What is he doing?", "Что он делает?"),
 "lg_what_adj": ("Qanday? So‘zni tanla", "What is it like?", "Какой он?"),
 "lg_what_phrase": ("Nima deysan? Iborani tanla", "What do you say?", "Что ты скажешь?"),
 "lg_find_color": ("Eshit va rangni top", "Find {w}", "Найди цвет: {w}"),
 "lg_find_color_object": ("Eshit va rasmni top", "Find something {w}", "Найди что-то {w}"),
 "lg_what_color": ("Bu qanday rang? So‘zni tanla", "What colour is it?", "Какой это цвет?"),
 "lg_read_color": ("O‘qi va rangni top", "Read and find the colour", "Прочитай и найди цвет"),
 "lg_find_number": ("Eshit va sonni top", "Find {w}", "Найди: {w}"),
 "lg_find_group": ("Eshit va rasmni top", "Find {w}", "Покажи, где {w}"),
 "lg_how_many": ("Nechta? So‘zni tanla", "How many?", "Сколько?"),
 "lg_match_numbers": ("Son va so‘zni juftla", "Match the numbers and the words", "Соедини числа и слова"),
 "lg_find_letter": ("Harfni top", "Find the letter {l}", "Найди букву {l}"),
 "lg_find_small_letter": ("Kichik harfni top", "Find the small letter {l}", "Найди маленькую букву {l}"),
 "lg_match_case": ("Bosh va kichik harfni juftla", "Match the big and small letters", "Соедини большие и маленькие буквы"),
 "lg_first_letter": ("Harf bilan boshlanadigan rasmni top", "Which one starts with {l}?", "Что начинается на букву {l}?"),
 "lg_alphabet": ("Eshit va rasmni top", "{l} is for {w}. Find the {w}.", "{l} — {w}. Где {w}?"),
 "lg_find_vowel": ("Unli harfni top", "Find the vowel", "Найди гласную букву"),
 "lg_find_consonant": ("Undosh harfni top", "Find the consonant", "Найди согласную букву"),
 "lg_count_syllables": ("Bo‘g‘inlarni sana", "How many syllables?", "Сколько слогов в слове?"),
 "lg_build_syllables": ("Bo‘g‘inlardan so‘z yig‘", "Make the word from syllables", "Собери слово из слогов"),
 "lg_missing_syllable": ("Tushib qolgan bo‘g‘inni top", "Find the missing syllable", "Какого слога не хватает?"),
 "lg_spell": ("Harflardan so‘z yig‘", "Spell the word: {w}", "Собери слово: {w}"),
 "lg_find_big": ("Eshit va rasmni top", "Find the {a} {w}", "Где {a} {w}?"),
 "lg_find_line": ("Eshit va chiziqni top", "Find the {a} line", "Где {a} линия?"),
 "lg_read_sentence": ("Gapni o‘qi va rasmni top", "Read and find the picture", "Прочитай и найди картинку"),
 "lg_picture_sentence": ("Rasmga mos gapni tanla", "Which sentence matches the picture?", "Какое предложение подходит к картинке?"),
 "lg_listen_sentence": ("Gapni eshit va rasmni top", "Listen and find: {w}", "Слушай и найди: {w}"),
 "lg_build_sentence": ("So‘zlardan gap tuz", "Make a sentence", "Составь предложение"),
}

# 3 tilda o'rganamiz (tri_*): ekranda o'zbekcha; ovoz bo'laklari generator'da (har so'z o'z tilida).
TRI = {
 "tri_which_picture": ("«{w}» qaysi rasm?", "Which picture is «{w}»?", "Какая картинка — «{w}»?"),
 "tri_what_is": ("«{w}» nima?", "What is «{w}»?", "Что такое «{w}»?"),
 "tri_listen3": ("{w}. Qaysi rasm?", "{w}. Which picture?", "{w}. Какая картинка?"),
 "tri_which_lang": ("Qaysi so‘z {lang}?", "Which word is in {lang}?", "Какое слово — {lang}?"),
 "tri_match": ("So‘zlarni juftla: {lang}", "Match the words: {lang}", "Соедини слова: {lang}"),
}


out = {"schemaVersion": 1, "instructions": {}}
import re
ph = lambda s: sorted(set(re.findall(r"\{(\w+)(?::\w+)?\}", s)))
for k, (uz, en, ru) in LG.items():
    assert k.startswith("lg_")
    assert ph(en) == ph(ru) and set(ph(uz)) <= set(ph(en)), (k, ph(uz), ph(en), ph(ru))
    out["instructions"][k] = {"uz": uz, "en": en, "ru": ru}
I.update(TRI)
for k, (uz, en, ru) in I.items():
    ph = lambda s: sorted(set(re.findall(r"\{(\w+)(?::\w+)?\}", s)))
    # Tarjimalar bir xil o'rinbosarlarga ega bo'lishi kerak (uz dagi p1/p2 kabi so'zlar bundan mustasno emas).
    assert ph(uz) == ph(en) == ph(ru), (k, ph(uz), ph(en), ph(ru))
    out["instructions"][k] = {"uz": uz, "en": en, "ru": ru}
path = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "data", "instructions.json")
json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out["instructions"]), "instructions")
