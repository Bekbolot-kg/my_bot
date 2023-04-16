from aiogram import executor
from aiogram.dispatcher.filters import Text
from handler.info import info
from handler.start import start
from handler.picture import picture
from handler.help import cmd_help
from handler.about import cmd_about
from handler.ai import cmd_ai
from config import dp

if __name__ == "__main__":

    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info, commands=['myinfo'])
    dp.register_message_handler(picture, commands=['picture'])
    dp.register_message_handler(picture,Text(equals='Рандомное фото'))
    dp.register_message_handler(cmd_help, commands=['help'])
    dp.register_message_handler(cmd_about, Text(equals='О Боте'))
    dp.register_message_handler(cmd_ai, Text(equals='Топовые нейросети'))
    executor.start_polling(dp)