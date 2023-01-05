# pip install aiogram
# pip install oauth2client
# pip install gspread
from aiogram import Bot, Dispatcher, executor, types
from keyboards import keyboard_inline_1, keyboard_inline_menu_kz, keyboard_inline_menu_ru, keyboard_inline_menu_eng
from google_sheets import python_test, first_line
from keyboard_3rd_lvl import keyboard_co_kz, keyboard_co_ru, keyboard_co_eng
from keyboard_3rd_lvl import keyboard_ti_kz, keyboard_ti_ru, keyboard_ti_eng
from keyboard_3rd_lvl import keyboard_beer_kz, keyboard_beer_ru, keyboard_beer_eng
from keyboard_3rd_lvl import keyboard_cider_kz, keyboard_cider_ru, keyboard_cider_eng
from keyboard_3rd_lvl import keyboard_snacks_kz, keyboard_snacks_ru, keyboard_snacks_eng
from keyboard_3rd_lvl import keyboard_wine_kz, keyboard_wine_ru, keyboard_wine_eng
from keyboard_3rd_lvl import keyboard_non_alco_kz, keyboard_non_alco_ru, keyboard_non_alco_eng


curr_lang = "ru"

TOKEN = ""
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def rand_command(message: types.Message):
    await message.reply("Select a language:", reply_markup=keyboard_inline_1)


# @dispatcher.message_handler(commands=['start', 'help'])
# async def welcome(message: types.Message):
#     await message.reply("You are good enough! Remember that!")


@dispatcher.callback_query_handler(text=['kz', 'ru', 'eng'])
async def chosen_param(call: types.CallbackQuery):
    global curr_lang
    if call.data == "kz":
        curr_lang = "kz"
        # await call.message.answer("Cен қазақ тілін таңдадың")
        await call.message.answer(text="Санатты таңдаңыз:", reply_markup=keyboard_inline_menu_kz)
    if call.data == "ru":
        curr_lang = "ru"
        # await call.message.answer("Вы выбрали русский язык")
        await call.message.answer(text="Выберите категорию:", reply_markup=keyboard_inline_menu_ru)
    if call.data == "eng":
        curr_lang = "eng"
        # await call.message.answer("You chose english language")
        await call.message.answer(text="Chose category:", reply_markup=keyboard_inline_menu_eng)

    await call.answer()


@dispatcher.callback_query_handler(text=['cocktails', 'tinctures', 'beer', 'cider', 'snacks', 'wine', 'non-alcoholic'])
async def chosen_param(call: types.CallbackQuery):
    global curr_lang
    if curr_lang == "kz":
        if call.data == "cocktails":
            await call.message.answer(text="Коктейльді таңдаңыз 🍸 400мл:", reply_markup=keyboard_co_kz)
        elif call.data == "tinctures":
            await call.message.answer(text="Тұнбаны таңдаңыз ◇ 50мл:", reply_markup=keyboard_ti_kz)
        elif call.data == "beer":
            await call.message.answer(text="Сыраны таңдаңыз:", reply_markup=keyboard_beer_kz)
        elif call.data == "cider":
            await call.message.answer(text="Сидрді таңдаңыз ◇ 500мл:", reply_markup=keyboard_cider_kz)
        elif call.data == "snacks":
            await call.message.answer(text="Tағамдарды таңдаңыз:", reply_markup=keyboard_snacks_kz)
        elif call.data == "wine":
            await call.message.answer(text="Шарап таңдаңыз 🍷 200мл:", reply_markup=keyboard_wine_kz)
        elif call.data == "non-alcoholic":
            await call.message.answer(text="Алкогольсіз сусынды таңдаңыз:", reply_markup=keyboard_non_alco_kz)
    elif curr_lang == "ru":
        if call.data == "cocktails":
            await call.message.answer(text="Выберите коктейль 🍸 400мл:", reply_markup=keyboard_co_ru)
        elif call.data == "tinctures":
            await call.message.answer(text="Выберите найстойку ◇ 50мл:", reply_markup=keyboard_ti_ru)
        elif call.data == "beer":
            await call.message.answer(text="Выберите пиво:", reply_markup=keyboard_beer_ru)
        elif call.data == "cider":
            await call.message.answer(text="Выберите сидр ◇ 500мл:", reply_markup=keyboard_cider_ru)
        elif call.data == "snacks":
            await call.message.answer(text="Снеки на выбор:", reply_markup=keyboard_snacks_ru)
        elif call.data == "wine":
            await call.message.answer(text="Выберите вино 🍷 200мл:", reply_markup=keyboard_wine_ru)
        elif call.data == "non-alcoholic":
            await call.message.answer(text="Выберите безалкогольный напиток:", reply_markup=keyboard_non_alco_ru)
    elif curr_lang == "eng":
        if call.data == "cocktails":
            await call.message.answer(text="Choose a cocktail 🍸 400мл:", reply_markup=keyboard_co_eng)
        elif call.data == "tinctures":
            await call.message.answer(text="Choose a tincture ◇ 50мл:", reply_markup=keyboard_ti_eng)
        elif call.data == "beer":
            await call.message.answer(text="Choose a beer:", reply_markup=keyboard_beer_eng)
        elif call.data == "cider":
            await call.message.answer(text="Choose a cider ◇ 500мл:", reply_markup=keyboard_cider_eng)
        elif call.data == "snacks":
            await call.message.answer(text="Select snacks:", reply_markup=keyboard_snacks_eng)
        elif call.data == "wine":
            await call.message.answer(text="Choose wine 🍷 200мл:", reply_markup=keyboard_wine_eng)
        elif call.data == "non-alcoholic":
            await call.message.answer(text="Choose a soft drink:", reply_markup=keyboard_non_alco_eng)


# @dispatcher.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

executor.start_polling(dispatcher)
