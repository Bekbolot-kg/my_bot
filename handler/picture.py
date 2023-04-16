import random
from aiogram import types


# @dp.message_handler(commands=["picture"])
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

    await message.answer_photo(photo=random.choice(photo))

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

    await message.delete()

