from aiogram import types

# @dp.message_handler(commands=["start"])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton('Рандомное фото'), types.KeyboardButton('Топовые нейросети'))
    kb.add(types.KeyboardButton('Опрос'), types.KeyboardButton('О Боте'))
    first_name = message.from_user.first_name
    await message.answer(f"Добро пожаловать <b>{first_name}</b>",
                         parse_mode='html',
                         reply_markup=kb)
    await message.delete()