from aiogram import types


# @dp.message_handler(commands=["myinfo"])
async def info(message: types.Message):
    firstname = message.from_user.first_name
    username = message.from_user.username
    myid = message.from_user.id
    myinfo_cmd = f'''
    !   🤫🤫🤫    !
    <b>first_name -   {firstname}
    user_name  -   {username}
    id         -   {myid}</b>

    '''
    await message.answer(text=myinfo_cmd, parse_mode='html')
    await message.delete()