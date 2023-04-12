import random

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os



load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

help_cmd = '''
<b>/start</b> - <em>запускает бота</em>
<b>/myinfo</b> - <em>отправляет информацию о пользователе</em>
<b>/help</b> - <em>отправляет список команд</em>
<b>/picture</b> - <em>отправляет рандомную картинкy</em>'''



@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    first_name = message.from_user.first_name
    await message.answer(f"Добро пожаловать <b>{first_name}</b>",
                         parse_mode='html')



@dp.message_handler(commands=["picture"])
async def picture(message: types.Message):
    photo1 = open('image/111.jpg', 'rb')
    photo2 = open('image/222.jpg', 'rb')
    photo3 = open('image/333.jpg', 'rb')
    photo4 = open('image/444.jpg', 'rb')
    photo5 = open('image/555.jpg', 'rb')
    photo6 = open('image/666.jpg', 'rb')
    photo7 = open('image/777.jpg', 'rb')
    photo8 = open('image/888.jpg', 'rb')
    photo9 = open('image/999.jpg', 'rb')
    photo10 = open('image/101010.jpg', 'rb')
    photo = [photo1, photo10, photo9, photo8, photo7, photo6, photo4, photo5, photo3, photo2]

    await message.reply_photo(photo=random.choice(photo))

    photo1.close()
    photo2.close()
    photo3.close()
    photo4.close()
    photo5.close()
    photo6.close()
    photo7.close()
    photo8.close()
    photo9.close()
    photo10.close()

@dp.message_handler(commands=["help"])
async def sticker(message: types.Message):
    await message.answer(text=help_cmd,
                         parse_mode='html')


@dp.message_handler(commands=["myinfo"])
async def info(message: types.Message):
    firstname = message.from_user.first_name
    username = message.from_user.username
    myid = message.from_user.id
    myinfo_cmd = f'''
        Ваши данные
    first_name - {firstname}
    user_name  - {username}
    id         - {myid}
    
    '''
    await message.reply(text=myinfo_cmd)




if __name__ == "__main__":
    executor.start_polling(dp)