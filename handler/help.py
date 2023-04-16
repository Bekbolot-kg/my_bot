from aiogram import types


help_cmd = '''
<b>/start</b> - <em>запускает бота</em>
<b>/myinfo</b> - <em>отправляет информацию о пользователе</em>
<b>/help</b> - <em>отправляет список команд</em>
<b>/picture</b> - <em>отправляет рандомную картинкy</em>'''


# @dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer(text=help_cmd,
                         parse_mode='html')
    await message.delete()