from aiogram import Dispatcher, Bot, types
from config import bot
import sqlite3
from Database.db import DATABASE
from keyboards import buttons
from const import PROFILE_TEXT
import random
import re
async def call_profile(call: types.CallbackQuery):
    data = DATABASE()
    profile = data.sql_select_profile(
        telegram_id=call.from_user.id
    )
    print(profile)
    if profile:
        with open(profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=profile['nickname'],
                    bio=profile['biography'],
                    age=profile['age'],
                    zodiac=profile['zodiac'],
                    blood_type=profile['blood_type'],
                    favorite_car=profile['favorite_car']
                ),
            )
            reply_markup = await buttons.keyboard()

    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='you not registered'
        )

async def random_filter_profile(call: types.CallbackQuery):
    data = DATABASE()
    profile = data.sql_select_all_profile(owner=call.from_user.id)
    if not profile:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="There's nothing else"
        )
        return

    random_profile = random.choice(profile)
    with open(profile['photo'], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=PROFILE_TEXT.format(
                nickname=profile['nickname'],
                bio=profile['biography'],
                age=profile['age'],
                zodiac=profile['zodiac'],
                blood_type=profile['blood_type'],
                favorite_car=profile['favorite_car']),
            reply_markup=await buttons.like_dislike_buttons(
                owner=random_profile['telegram_id'])
        )

def register_display_profile_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        call_profile, lambda call: call.data == 'display profile'
    )


