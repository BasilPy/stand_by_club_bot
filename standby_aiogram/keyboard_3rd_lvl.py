from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# data for thirds keyboards


data_tinctures = [['Шие 🍒 1500₸', 'Вишня 🍒 1500₸', 'Cherry 🍒 1500₸', 'cherry'],
                  ['Қарақат ◇ 1500₸', 'Смородина ◇ 1500₸', 'Currant ◇ 1500₸', 'currant'],
                  ['Теңіз шырғаны ◇ 1500₸', 'Облепиха ◇ 1500₸', 'Sea buckthorn ◇ 1500₸', 'sea_buckthorn'],
                  ['Мүкжидек ◇ 1500₸', 'Клюква ◇ 1500₸', 'Cranberry ◇ 1500₸', 'cranberry']]

data_beer = [['500мл ◇ HINEKEN 🍺 1500₸', '500мл ◇ HINEkEN 🍺 1500₸', '500ml ◇ Hineken 🍺 1500₸', 'hineken'],
             ['300мл ◇ MILLER 🍺 1500₸', '300мл ◇ MiLLeR 🍺 1500₸', '300ml ◇ Miller 🍺 1500₸', 'miller'],
             ['500мл ◇ Құйылмалы 🍺 1500₸', '500мл ◇ Разливное 🍺 1500₸', '500ml ◇ Draft 🍺 1500₸', 'draft']]

data_cider = [['CHESTER ◇ 2000₸', 'CHЄSTER ◇ 2000₸', 'Chester ◇ 2000₸', 'chester'],
              ['BOZY ◇ 1500₸', 'BOzY ◇ 1500₸', 'Bozy ◇ 1500₸', 'bozy'], ]

data_snacks = [['Нахосч 🍴 1000₸', 'Начос 🍴 1000₸', 'Nachos 🍴 1000₸', 'Nachos'],
               [':Жаңғақтар 🥥 1000₸', 'Орехи 🥥 1000₸', 'Nuts 🥥 1000₸', 'Nuts'],
               ['Крутон қосылған кептірілген ет ◇ 2000₸', ' Вяленое мясо с сухариками ◇ 2000₸',
                'Dried_meat_with_croutons ◇ 2000₸', 'dried_meat_'],
               ['Курт ◇ 1000₸ ', 'Kурт ◇ 1000₸', 'Kurt ◇ 1000₸', 'kurt'],
               ['Челель ◇ 1000₸', 'Чечел ◇ 1000₸', 'Chelel ◇ 1000₸', 'chelel'], ]

data_wines = [['Қызыл жартылай тәтті 🍷', 'Красное полусладкое 🍷', 'Red_semi-sweet 🍷', 'red_semi'],
              ['Құрғақ ақ 🥂 1500₸', 'Белое сухое 🥂 1500₸', 'White dry 🥂 1500₸', 'white_dry '],
              ['Қызғылт 💗 1500₸', 'Розовое 💗 1500₸', 'Pink 💗 1500₸', 'pink'], ]

data_non_alco = [['330мл ◇ Алкогольсіз сыра 1000₸', '330мл ◇ Безалкогольное піво 1000₸',
                  '330ml ◇ Non-alcoholic_beer 1000₸', 'non_a_beer'],
                 ['330мл ◇ COLA 1000₸', '330мл ◇ CoLA 1000₸', '330ml ◇ Cola 1000₸', 'cola'],
                 ['330мл ◇ Red BULL 🧚🏾‍♀️1000₸', '330мл ◇ RED BULL 🧚🏾‍♀️1000₸', '330ml ◇ RED BULL 🧚🏾‍♀️1000₸',
                  'red_bull'],
                 ['330мл ◇ ШЫРЫН + 1000₸', '330мл ◇ COK + 1000₸', '330мл ◇ Juice + 1000₸', 'juice'],
                 ['400мл ◇ Шай 🥤 500₸', '400мл ◇ Чай 🥤 500₸', '400ml ◇ Tea 🥤 500₸', 'tea'],
                 ['400мл ◇ Кофе ☕ 500₸', '400мл ◇ Кофє ☕ 500₸', '400ml ◇ Сoffee ☕ 500₸', 'coffee'],
                 ['500мл ◇ Су 🧊 500₸', '500мл ◇ Вода 🧊 500₸', '500ml ◇ Water 🧊 500₸', 'water'], ]

data_soki = [['Алма 🍎 1000₸', 'Яблоко 🍎 1000₸', 'Apple 🍎 1000₸', 'apple_j'],
             ['Шие 🍒 1000₸', 'Вишня 🍒 1000₸', 'Cherry 🍒 1000₸', 'cherry_j'],
             ['Апельсин 🍊 1000₸', 'Апєльсин 🍊 1000₸', 'Orange 🍊 1000₸', 'orange_j']]

# ______________________________________________________
# for data_cocktails
# ______________________________________________________

# ______________________________________________________
# for data_tinctures
# ______________________________________________________
list_ti_kz = [x for list_i in data_tinctures for x in list_i if x == list_i[0]]
list_ti_ru = [x for list_i in data_tinctures for x in list_i if x == list_i[1]]
list_ti_eng = [x for list_i in data_tinctures for x in list_i if x == list_i[2]]
list_ti_callback = [x for list_i in data_tinctures for x in list_i if x == list_i[3]]


btn_ti_kz_1 = InlineKeyboardButton(text=list_ti_kz[0], callback_data=list_ti_callback[0])
btn_ti_kz_2 = InlineKeyboardButton(text=list_ti_kz[1], callback_data=list_ti_callback[1])
btn_ti_kz_3 = InlineKeyboardButton(text=list_ti_kz[2], callback_data=list_ti_callback[2])
btn_ti_kz_4 = InlineKeyboardButton(text=list_ti_kz[3], callback_data=list_ti_callback[3])
btns_ti_kz = [btn_ti_kz_1, btn_ti_kz_2, btn_ti_kz_3, btn_ti_kz_4]
keyboard_ti_kz = InlineKeyboardMarkup()
for row_btn in btns_ti_kz:
    keyboard_ti_kz.row(row_btn)
# -------------
btn_ti_ru_1 = InlineKeyboardButton(text=list_ti_ru[0], callback_data=list_ti_callback[0])
btn_ti_ru_2 = InlineKeyboardButton(text=list_ti_ru[1], callback_data=list_ti_callback[1])
btn_ti_ru_3 = InlineKeyboardButton(text=list_ti_ru[2], callback_data=list_ti_callback[2])
btn_ti_ru_4 = InlineKeyboardButton(text=list_ti_ru[3], callback_data=list_ti_callback[3])
btns_ti_ru = [btn_ti_ru_1, btn_ti_ru_2, btn_ti_ru_3, btn_ti_ru_4]
keyboard_ti_ru = InlineKeyboardMarkup()
for row_btn in btns_ti_ru:
    keyboard_ti_ru.row(row_btn)
# -------------
btn_ti_eng_1 = InlineKeyboardButton(text=list_ti_eng[0], callback_data=list_ti_callback[0])
btn_ti_eng_2 = InlineKeyboardButton(text=list_ti_eng[1], callback_data=list_ti_callback[1])
btn_ti_eng_3 = InlineKeyboardButton(text=list_ti_eng[2], callback_data=list_ti_callback[2])
btn_ti_eng_4 = InlineKeyboardButton(text=list_ti_eng[3], callback_data=list_ti_callback[3])
btns_ti_eng = [btn_ti_eng_1, btn_ti_eng_2, btn_ti_eng_3, btn_ti_eng_4]
keyboard_ti_eng = InlineKeyboardMarkup()
for row_btn in btns_ti_eng:
    keyboard_ti_eng.row(row_btn)

# ______________________________________________________
# for data_beer
# ______________________________________________________

list_beer_kz = [x for list_i in data_beer for x in list_i if x == list_i[0]]
list_beer_ru = [x for list_i in data_beer for x in list_i if x == list_i[1]]
list_beer_eng = [x for list_i in data_beer for x in list_i if x == list_i[2]]
list_beer_callback = [x for list_i in data_beer for x in list_i if x == list_i[3]]

btn_beer_kz_1 = InlineKeyboardButton(text=list_beer_kz[0], callback_data=list_beer_callback[0])
btn_beer_kz_2 = InlineKeyboardButton(text=list_beer_kz[1], callback_data=list_beer_callback[1])
btn_beer_kz_3 = InlineKeyboardButton(text=list_beer_kz[2], callback_data=list_beer_callback[2])

btns_beer_kz = [btn_beer_kz_1, btn_beer_kz_2, btn_beer_kz_3]
keyboard_beer_kz = InlineKeyboardMarkup()
for row_btn in btns_beer_kz:
    keyboard_beer_kz.row(row_btn)
# -------------
btn_beer_ru_1 = InlineKeyboardButton(text=list_beer_ru[0], callback_data=list_beer_callback[0])
btn_beer_ru_2 = InlineKeyboardButton(text=list_beer_ru[1], callback_data=list_beer_callback[1])
btn_beer_ru_3 = InlineKeyboardButton(text=list_beer_ru[2], callback_data=list_beer_callback[2])

btns_beer_ru = [btn_beer_ru_1, btn_beer_ru_2, btn_beer_ru_3]
keyboard_beer_ru = InlineKeyboardMarkup()
for row_btn in btns_beer_ru:
    keyboard_beer_ru.row(row_btn)
# -------------
btn_beer_eng_1 = InlineKeyboardButton(text=list_beer_eng[0], callback_data=list_beer_callback[0])
btn_beer_eng_2 = InlineKeyboardButton(text=list_beer_eng[1], callback_data=list_beer_callback[1])
btn_beer_eng_3 = InlineKeyboardButton(text=list_beer_eng[2], callback_data=list_beer_callback[2])

btns_beer_eng = [btn_beer_eng_1, btn_beer_eng_2, btn_beer_eng_3]
keyboard_beer_eng = InlineKeyboardMarkup()
for row_btn in btns_beer_eng:
    keyboard_beer_eng.row(row_btn)

# ______________________________________________________
# for data_cider  // without list comprehension
# ______________________________________________________

btn_cider_kz_1 = InlineKeyboardButton(text=data_cider[0][0], callback_data=data_cider[0][3])
btn_cider_kz_2 = InlineKeyboardButton(text=data_cider[1][0], callback_data=data_cider[1][3])


btns_cider_kz = [btn_cider_kz_1, btn_cider_kz_2]
keyboard_cider_kz = InlineKeyboardMarkup()
for row_btn in btns_cider_kz:
    keyboard_cider_kz.row(row_btn)
# -------------
btn_cider_ru_1 = InlineKeyboardButton(text=data_cider[0][1], callback_data=data_cider[0][3])
btn_cider_ru_2 = InlineKeyboardButton(text=data_cider[1][1], callback_data=data_cider[1][3])

btns_cider_ru = [btn_cider_ru_1, btn_cider_ru_2]
keyboard_cider_ru = InlineKeyboardMarkup()
for row_btn in btns_cider_ru:
    keyboard_cider_ru.row(row_btn)
# -------------
btn_cider_eng_1 = InlineKeyboardButton(text=data_cider[0][2], callback_data=data_cider[0][3])
btn_cider_eng_2 = InlineKeyboardButton(text=data_cider[1][2], callback_data=data_cider[1][3])


btns_cider_eng = [btn_cider_eng_1, btn_cider_eng_2]
keyboard_cider_eng = InlineKeyboardMarkup()
for row_btn in btns_cider_eng:
    keyboard_cider_eng.row(row_btn)

# ______________________________________________________
# for data_snacks  // without list comprehension
# ______________________________________________________
btn_snack_kz_1 = InlineKeyboardButton(text=data_snacks[0][0], callback_data=data_snacks[0][3])
btn_snack_kz_2 = InlineKeyboardButton(text=data_snacks[1][0], callback_data=data_snacks[1][3])
btn_snack_kz_3 = InlineKeyboardButton(text=data_snacks[2][0], callback_data=data_snacks[2][3])
btn_snack_kz_4 = InlineKeyboardButton(text=data_snacks[3][0], callback_data=data_snacks[1][3])
btn_snack_kz_5 = InlineKeyboardButton(text=data_snacks[4][0], callback_data=data_snacks[2][3])

btns_snacks_kz = [btn_snack_kz_1, btn_snack_kz_2, btn_snack_kz_3, btn_snack_kz_4, btn_snack_kz_5]
keyboard_snacks_kz = InlineKeyboardMarkup()
for row_btn in btns_snacks_kz:
    keyboard_snacks_kz.row(row_btn)
# -------------
btn_snack_ru_1 = InlineKeyboardButton(text=data_snacks[0][1], callback_data=data_snacks[0][3])
btn_snack_ru_2 = InlineKeyboardButton(text=data_snacks[1][1], callback_data=data_snacks[1][3])
btn_snack_ru_3 = InlineKeyboardButton(text=data_snacks[2][1], callback_data=data_snacks[2][3])
btn_snack_ru_4 = InlineKeyboardButton(text=data_snacks[3][1], callback_data=data_snacks[1][3])
btn_snack_ru_5 = InlineKeyboardButton(text=data_snacks[4][1], callback_data=data_snacks[2][3])

btns_snacks_ru = [btn_snack_ru_1, btn_snack_ru_2, btn_snack_ru_3, btn_snack_ru_4, btn_snack_ru_5]
keyboard_snacks_ru = InlineKeyboardMarkup()
for row_btn in btns_snacks_ru:
    keyboard_snacks_ru.row(row_btn)
# -------------
btn_snack_eng_1 = InlineKeyboardButton(text=data_snacks[0][2], callback_data=data_snacks[0][3])
btn_snack_eng_2 = InlineKeyboardButton(text=data_snacks[1][2], callback_data=data_snacks[1][3])
btn_snack_eng_3 = InlineKeyboardButton(text=data_snacks[2][2], callback_data=data_snacks[2][3])
btn_snack_eng_4 = InlineKeyboardButton(text=data_snacks[3][2], callback_data=data_snacks[1][3])
btn_snack_eng_5 = InlineKeyboardButton(text=data_snacks[4][2], callback_data=data_snacks[2][3])

btns_snacks_eng = [btn_snack_eng_1, btn_snack_eng_2, btn_snack_eng_3, btn_snack_eng_4, btn_snack_eng_5]
keyboard_snacks_eng = InlineKeyboardMarkup()
for row_btn in btns_snacks_eng:
    keyboard_snacks_eng.row(row_btn)

# ______________________________________________________
# for data_wines  // without list comprehension
# ______________________________________________________
btn_wine_kz_1 = InlineKeyboardButton(text=data_wines[0][0], callback_data=data_wines[0][3])
btn_wine_kz_2 = InlineKeyboardButton(text=data_wines[1][0], callback_data=data_wines[1][3])
btn_wine_kz_3 = InlineKeyboardButton(text=data_wines[2][0], callback_data=data_wines[2][3])

btns_wines_kz = [btn_wine_kz_1, btn_wine_kz_2, btn_wine_kz_3]
keyboard_wine_kz = InlineKeyboardMarkup()
for row_btn in btns_wines_kz:
    keyboard_wine_kz.row(row_btn)
# -------------
btn_wine_ru_1 = InlineKeyboardButton(text=data_wines[0][1], callback_data=data_wines[0][3])
btn_wine_ru_2 = InlineKeyboardButton(text=data_wines[1][1], callback_data=data_wines[1][3])
btn_wine_ru_3 = InlineKeyboardButton(text=data_wines[2][1], callback_data=data_wines[2][3])

btns_wines_ru = [btn_wine_ru_1, btn_wine_ru_2, btn_wine_ru_3]
keyboard_wine_ru = InlineKeyboardMarkup()
for row_btn in btns_wines_ru:
    keyboard_wine_ru.row(row_btn)
# -------------
btn_wine_eng_1 = InlineKeyboardButton(text=data_wines[0][2], callback_data=data_wines[0][3])
btn_wine_eng_2 = InlineKeyboardButton(text=data_wines[1][2], callback_data=data_wines[1][3])
btn_wine_eng_3 = InlineKeyboardButton(text=data_wines[2][2], callback_data=data_wines[2][3])

btns_wines_eng = [btn_wine_eng_1, btn_wine_eng_2, btn_wine_eng_3]
keyboard_wine_eng = InlineKeyboardMarkup()
for row_btn in btns_wines_eng:
    keyboard_wine_eng.row(row_btn)

# ______________________________________________________
# for data_non_alco  // without list comprehension
# ______________________________________________________

btn_non_alco_kz_1 = InlineKeyboardButton(text=data_non_alco[0][0], callback_data=data_non_alco[0][3])
btn_non_alco_kz_2 = InlineKeyboardButton(text=data_non_alco[1][0], callback_data=data_non_alco[1][3])
btn_non_alco_kz_3 = InlineKeyboardButton(text=data_non_alco[2][0], callback_data=data_non_alco[2][3])
btn_non_alco_kz_4 = InlineKeyboardButton(text=data_non_alco[3][0], callback_data=data_non_alco[3][3])
btn_non_alco_kz_5 = InlineKeyboardButton(text=data_non_alco[4][0], callback_data=data_non_alco[4][3])
btn_non_alco_kz_6 = InlineKeyboardButton(text=data_non_alco[5][0], callback_data=data_non_alco[5][3])
btn_non_alco_kz_7 = InlineKeyboardButton(text=data_non_alco[6][0], callback_data=data_non_alco[6][3])

btns_non_alcos_kz = [btn_non_alco_kz_1, btn_non_alco_kz_2, btn_non_alco_kz_3,
                     btn_non_alco_kz_4, btn_non_alco_kz_5, btn_non_alco_kz_6, btn_non_alco_kz_7]
keyboard_non_alco_kz = InlineKeyboardMarkup()
for row_btn in btns_non_alcos_kz:
    keyboard_non_alco_kz.row(row_btn)
# -------------
btn_non_alco_ru_1 = InlineKeyboardButton(text=data_non_alco[0][1], callback_data=data_non_alco[0][3])
btn_non_alco_ru_2 = InlineKeyboardButton(text=data_non_alco[1][1], callback_data=data_non_alco[1][3])
btn_non_alco_ru_3 = InlineKeyboardButton(text=data_non_alco[2][1], callback_data=data_non_alco[2][3])
btn_non_alco_ru_4 = InlineKeyboardButton(text=data_non_alco[3][1], callback_data=data_non_alco[3][3])
btn_non_alco_ru_5 = InlineKeyboardButton(text=data_non_alco[4][1], callback_data=data_non_alco[4][3])
btn_non_alco_ru_6 = InlineKeyboardButton(text=data_non_alco[5][1], callback_data=data_non_alco[5][3])
btn_non_alco_ru_7 = InlineKeyboardButton(text=data_non_alco[6][1], callback_data=data_non_alco[6][3])

btns_non_alcos_ru = [btn_non_alco_ru_1, btn_non_alco_ru_2, btn_non_alco_ru_3,
                     btn_non_alco_ru_4, btn_non_alco_ru_5, btn_non_alco_ru_6, btn_non_alco_ru_7]
keyboard_non_alco_ru = InlineKeyboardMarkup()
for row_btn in btns_non_alcos_ru:
    keyboard_non_alco_ru.row(row_btn)
# -------------
btn_non_alco_eng_1 = InlineKeyboardButton(text=data_non_alco[0][2], callback_data=data_non_alco[0][3])
btn_non_alco_eng_2 = InlineKeyboardButton(text=data_non_alco[1][2], callback_data=data_non_alco[1][3])
btn_non_alco_eng_3 = InlineKeyboardButton(text=data_non_alco[2][2], callback_data=data_non_alco[2][3])
btn_non_alco_eng_4 = InlineKeyboardButton(text=data_non_alco[3][2], callback_data=data_non_alco[3][3])
btn_non_alco_eng_5 = InlineKeyboardButton(text=data_non_alco[4][2], callback_data=data_non_alco[4][3])
btn_non_alco_eng_6 = InlineKeyboardButton(text=data_non_alco[5][2], callback_data=data_non_alco[5][3])
btn_non_alco_eng_7 = InlineKeyboardButton(text=data_non_alco[6][2], callback_data=data_non_alco[6][3])

btns_non_alcos_eng = [btn_non_alco_eng_1, btn_non_alco_eng_2, btn_non_alco_eng_3,
                      btn_non_alco_eng_4, btn_non_alco_eng_5, btn_non_alco_eng_6, btn_non_alco_eng_7]
keyboard_non_alco_eng = InlineKeyboardMarkup()
for row_btn in btns_non_alcos_eng:
    keyboard_non_alco_eng.row(row_btn)

# ______________________________________________________
# for data_soki  // without list comprehension  4th lvl menu
# ______________________________________________________

btn_soki_kz_1 = InlineKeyboardButton(text=data_soki[0][0], callback_data=data_soki[0][3])
btn_soki_kz_2 = InlineKeyboardButton(text=data_soki[1][0], callback_data=data_soki[1][3])
btn_soki_kz_3 = InlineKeyboardButton(text=data_soki[2][0], callback_data=data_soki[2][3])

btns_soki_kz = [btn_soki_kz_1, btn_soki_kz_2, btn_soki_kz_3]
keyboard_soki_kz = InlineKeyboardMarkup()
for row_btn in btns_soki_kz:
    keyboard_soki_kz.row(row_btn)
# -------------
btn_soki_ru_1 = InlineKeyboardButton(text=data_soki[0][1], callback_data=data_soki[0][3])
btn_soki_ru_2 = InlineKeyboardButton(text=data_soki[1][1], callback_data=data_soki[1][3])
btn_soki_ru_3 = InlineKeyboardButton(text=data_soki[2][1], callback_data=data_soki[2][3])

btns_soki_ru = [btn_soki_ru_1, btn_soki_ru_2, btn_soki_ru_3]
keyboard_soki_ru = InlineKeyboardMarkup()
for row_btn in btns_soki_ru:
    keyboard_soki_ru.row(row_btn)
# -------------
btn_soki_eng_1 = InlineKeyboardButton(text=data_soki[0][2], callback_data=data_soki[0][3])
btn_soki_eng_2 = InlineKeyboardButton(text=data_soki[1][2], callback_data=data_soki[1][3])
btn_soki_eng_3 = InlineKeyboardButton(text=data_soki[2][2], callback_data=data_soki[2][3])

btns_soki_eng = [btn_soki_eng_1, btn_soki_eng_2, btn_soki_eng_3]
keyboard_soki_eng = InlineKeyboardMarkup()
for row_btn in btns_soki_eng:
    keyboard_soki_eng.row(row_btn)