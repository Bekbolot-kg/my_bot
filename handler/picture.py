import random
from aiogram import types
import os


# @dp.message_handler(commands=["picture"])
async def picture(message: types.Message):
    direct = 'image/'
    photo_files = []

    for filename in os.listdir(direct):
        photo_files.append(os.path.join(direct, filename))

    photos = [open(file, 'rb') for file in photo_files]
    chosen_photo = random.choice(photos)

    await message.answer_photo(photo=chosen_photo)

    for photo in photos:
        photo.close()

    await message.delete()

