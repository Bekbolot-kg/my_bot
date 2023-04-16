from aiogram import types

async def cmd_ai(message: types.Message):
    ikb = types.InlineKeyboardMarkup(row_width=2)
    ikb.add(types.InlineKeyboardButton(text='Создать логотип', url='https://looka.com/'),
            types.InlineKeyboardButton(text='Создать фото', url='https://www.midjourney.com/home/?callbackUrl=%2Fapp%2F'))
    ikb.add(types.InlineKeyboardButton(text='Создать презентации', url='https://beta.tome.app/'),
            types.InlineKeyboardButton(text='Улучшить качество фото',
                                       url='https://imglarger.com/'))
    await message.answer(text='💣 Топовые нейросети 💣',
                         reply_markup=ikb)
    await message.delete()