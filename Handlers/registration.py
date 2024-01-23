from aiogram import Dispatcher, Bot, types
from config import bot, MEDIA_DESTINATION
from Database.db import DATABASE
from keyboards import buttons
from const import PROFILE_TEXT
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class Registration(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    zodiac = State()
    blood_type = State()
    favorite_car = State()
    photo = State()

async def start_registration(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="what's your nickname?"
    )
    await Registration.nickname.set()

async def load_registration(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["nickname"] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="tell me about yourself"
    )
    await Registration.next()

async def biography_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="how old you? (only numbers)"
    )
    await Registration.next()

async def age_load(message: types.Message, state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        async with state.proxy() as data:
            data['Registration failed. You did not fulfill the requirement.'] = message.text
            await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="what's your zodiac sign"
    )
    await Registration.next()

async def zodiac_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['zodiac'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="what's your blood type?"
    )
    await Registration.next()

async def blood_type_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['blood_type'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="what's your favorite car?"
    )
    await Registration.next()

async def favorite_car_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['favorite_car'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="send me a photo"
    )
    await Registration.next()

async def load_photo(message: types.Message, state: FSMContext):
    db = DATABASE()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )

    async with state.proxy() as data:
        db.insert_telegram_profile(
            telegram_id=message.from_user.id,
            nickname=data['nickname'],
            biography=data['biography'],
            age=data['age'],
            zodiac=data['zodiac'],
            blood_type=data['blood_type'],
            favorite_car=data['favorite_car'],
            photo=path.name,
        )

    with open(path.name, 'rb') as photo:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=photo,
            caption=PROFILE_TEXT.format(
                nickname=data['nickname'],
                bio=data['biography'],
                age=data['age'],
                zodiac=data['zodiac'],
                blood_type=data['blood_type'],
                favorite_car=data['favorite_car']),
            ),

    await bot.send_message(
        chat_id=message.from_user.id,
        text="you've been registered "
    )

def register_registration(dp: Dispatcher):
    dp.register_callback_query_handler(
        start_registration,
        lambda call: call.data == 'Registration'
    )

    dp.register_message_handler(
        load_registration,
        state=Registration.nickname,
        content_types=['text'],
    )

    dp.register_message_handler(
        biography_load,
        state=Registration.biography,
        content_types=['text'],
    )

    dp.register_message_handler(
        age_load,
        state=Registration.age,
        content_types=['text'],
    )

    dp.register_message_handler(
        zodiac_load,
        state=Registration.zodiac,
        content_types=['text'],
    )

    dp.register_message_handler(
        blood_type_load,
        state=Registration.blood_type,
        content_types=['text'],
    )

    dp.register_message_handler(
        favorite_car_load,
        state=Registration.favorite_car,
        content_types=['text'],
    )

    dp.register_message_handler(
        load_photo,
        state=Registration.photo,
        content_types=types.ContentTypes.PHOTO
    )
