from aiogram import types


about_cmd = '''
Бот отпрваляет интересные фото 
сгенированые с помощи нейросети 
и топовые нейросети 😊'''


async def cmd_about(message: types.Message):
    await message.answer(text=about_cmd)
    await message.delete()