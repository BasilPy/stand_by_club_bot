# pip install aiogram
# pip install oauth2client
# pip install gspread
from aiogram import types, executor
from create_bot import bot, dispatcher
from handlers import client

client.register_handlers_client(dispatcher)

if __name__ == "__main__":
    executor.start_polling(dispatcher)
