from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types


#Finite State Machine
class Survey(StatesGroup):
    name = State()
    age = State()
    rating = State()
    cause = State()

async def start_survey(message: types.Message):
    await Survey.name.set()
    await message.answer('Как вас зовут?')

async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

        await Survey.next()
        await message.answer('Сколько вам лет?')

async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer('Введите цифры!')
    elif int(age) > 110 or int(age) < 10:
        await message.answer('Введите нормальный возраст!')
    else:
        async with state.proxy() as data:
            data['age'] = int(age)
        ikb = types.InlineKeyboardMarkup(row_width=3)
        ikb.add(types.InlineKeyboardButton('5', callback_data='5'), types.InlineKeyboardButton('4', callback_data='4'),
                types.InlineKeyboardButton('3', callback_data='3'))
        ikb.add(types.InlineKeyboardButton('2', callback_data='2'), types.InlineKeyboardButton('1', callback_data='1'))

        await Survey.next()
        await message.answer('Вам нравиться наш бот? [Оцените его 🥰]',
                             reply_markup=ikb)

async def cb_cause(cb: types.CallbackQuery):
    await cb.answer(text=cb.data)
async def process_rating(message: types.Message, state: FSMContext):
    rating = message.text
    if not rating.isdigit():
        await message.answer('Выберите из кнопок!')
    else:
        async with state.proxy() as data:
            data['rating'] = rating

            await Survey.next()
            await message.answer('Почему вы так оценили? [Напишите пару слов 😊]')



async def process_cause(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cause'] = message.text

        await message.answer('Спасибо что прошли наш опрос 🙂😘')
        await state.finish()