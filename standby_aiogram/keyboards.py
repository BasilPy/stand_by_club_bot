from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language_ch = 0
button_language_1 = InlineKeyboardButton(text="Kz", callback_data="kz")
button_language_2 = InlineKeyboardButton(text="Ru", callback_data="ru")
button_language_3 = InlineKeyboardButton(text="Eng", callback_data="eng")

keyboard_inline_1 = InlineKeyboardMarkup().add(button_language_1, button_language_2, button_language_3)

data_menu = [['коктейльдер', 'коктейли', 'cocktails'], ['тұнбалар', 'настойки', 'tinctures'],
             ['сыра', 'пиво', 'beer'], ['сидр', 'сuдр', 'cider'], ['жеңіл тағамдар', 'снеки', 'snacks'],
             ['шарап', 'вино', 'wine'],
             ['алкогольсіз', 'безалкогольные', 'non-alcoholic']]

list_kz = [x for list_i in data_menu for x in list_i if x == list_i[0]]
list_ru = [x for list_i in data_menu for x in list_i if x == list_i[1]]
list_eng = [x for list_i in data_menu for x in list_i if x == list_i[2]]

button_category_1 = InlineKeyboardButton(text=list_kz[0], callback_data=list_eng[0])
button_category_2 = InlineKeyboardButton(text=list_kz[1], callback_data=list_eng[1])
button_category_3 = InlineKeyboardButton(text=list_kz[2], callback_data=list_eng[2])
button_category_4 = InlineKeyboardButton(text=list_kz[3], callback_data=list_eng[3])
button_category_5 = InlineKeyboardButton(text=list_kz[4], callback_data=list_eng[4])
button_category_6 = InlineKeyboardButton(text=list_kz[5], callback_data=list_eng[5])
button_category_7 = InlineKeyboardButton(text=list_kz[6], callback_data=list_eng[6])

button_category_ru_1 = InlineKeyboardButton(text=list_ru[0], callback_data=list_eng[0])
button_category_ru_2 = InlineKeyboardButton(text=list_ru[1], callback_data=list_eng[1])
button_category_ru_3 = InlineKeyboardButton(text=list_ru[2], callback_data=list_eng[2])
button_category_ru_4 = InlineKeyboardButton(text=list_ru[3], callback_data=list_eng[3])
button_category_ru_5 = InlineKeyboardButton(text=list_ru[4], callback_data=list_eng[4])
button_category_ru_6 = InlineKeyboardButton(text=list_ru[5], callback_data=list_eng[5])
button_category_ru_7 = InlineKeyboardButton(text=list_ru[6], callback_data=list_eng[6])

button_category_eng_1 = InlineKeyboardButton(text=list_eng[0], callback_data=list_eng[0])
button_category_eng_2 = InlineKeyboardButton(text=list_eng[1], callback_data=list_eng[1])
button_category_eng_3 = InlineKeyboardButton(text=list_eng[2], callback_data=list_eng[2])
button_category_eng_4 = InlineKeyboardButton(text=list_eng[3], callback_data=list_eng[3])
button_category_eng_5 = InlineKeyboardButton(text=list_eng[4], callback_data=list_eng[4])
button_category_eng_6 = InlineKeyboardButton(text=list_eng[5], callback_data=list_eng[5])
button_category_eng_7 = InlineKeyboardButton(text=list_eng[6], callback_data=list_eng[6])

keyboard_inline_menu_kz = InlineKeyboardMarkup().add(button_category_1, button_category_2, button_category_3,
                                                     button_category_4, button_category_5, button_category_6,
                                                     button_category_7)

keyboard_inline_menu_ru = InlineKeyboardMarkup().add(button_category_ru_1, button_category_ru_2, button_category_ru_3,
                                                     button_category_ru_4, button_category_ru_5, button_category_ru_6,
                                                     button_category_ru_7)

keyboard_inline_menu_eng = InlineKeyboardMarkup().add(button_category_eng_1, button_category_eng_2,
                                                      button_category_eng_3,
                                                      button_category_eng_4, button_category_eng_5,
                                                      button_category_eng_6, button_category_eng_7)


