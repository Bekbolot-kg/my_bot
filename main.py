from aiogram import executor
from aiogram.dispatcher.filters import Text
from handler.info import info
from handler.start import start
from handler.picture import picture
from handler.help import cmd_help
from handler.about import cmd_about
from handler.ai import cmd_ai
from handler.survey_fsm import (start_survey,
                                process_name,
                                Survey,
                                process_age,
                                process_rating,
                                process_cause,
                                cb_cause)
from config import dp

import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info, commands=['myinfo'])
    dp.register_message_handler(picture, commands=['picture'])
    dp.register_message_handler(picture, Text(equals='Рандомное фото'))
    dp.register_message_handler(cmd_help, commands=['help'])
    dp.register_message_handler(cmd_about, Text(equals='О Боте'))
    dp.register_message_handler(cmd_ai, Text(equals='Топовые нейросети'))


    #FSM
    dp.register_message_handler(start_survey, commands=['surv'])
    dp.register_message_handler(start_survey, Text(equals='Опрос'))
    dp.register_message_handler(process_name, state=Survey.name)
    dp.register_message_handler(process_age, state=Survey.age)
    dp.register_message_handler(process_cause, state=Survey.cause)
    dp.register_callback_query_handler(process_rating, lambda call: call.data.isdigit(), state=Survey.rating)
    dp.register_callback_query_handler(cb_cause, lambda call: int(call.data) < 6 and int(call.data) > 0)


    executor.start_polling(dp)