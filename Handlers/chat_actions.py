from aiogram import Dispatcher, Bot, types
from config import bot, MEDIA_DESTINATION, GROUP_ID
from Database import db
from keyboards import buttons
from const import START_COMMAND, BAN_USER_TEXT
from profanity_check import predict, predict_prob
import datetime
import sqlite3
from keyboards import buttons

async def check_message(message: types.Message):
    data = db.DATABASE()
    if message.chat.id == int(GROUP_ID):
        ban_words_predict = predict([message.text])
        ban_words_predict_prob = predict_prob([message.text])
        print(ban_words_predict_prob)
        print(message.chat)
        if ban_words_predict_prob > 0.9:
            potential = data.select_ban_user(
                telegram_id=message.from_user.id
            )
            print(potential)
            if potential:
                # if potential['count'] >= [3]:
                # bot.ban_chat_member(
                #     chat_id=message.chat.id,
                #     user_id=message.from_user.id,
                #     until_date=datetime.datetime.now() + datetime.timedelta(minutes=1)
                #     )
                #     return
                data.update(
                    telegram_id=message.from_user.id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=BAN_USER_TEXT.format(
                        name=message.from_user.first_name,
                        count=potential['count'] + 1
                    )

                )
            elif not potential:
                data.insert_telegram_ban_users(
                    telegram_id=message.from_user.id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=BAN_USER_TEXT.format(
                        name=message.from_user.first_name,
                        count=1
                    )
                )

        if ban_words_predict_prob > 0.7:
            await bot.delete_message(message.chat.id, message.message_id)

        print(ban_words_predict)

async def check_ban_status(call: types.CallbackQuery):
    data = db.DATABASE()
    user_id = call.from_user.id
    ban_status = data.select_ban_user(telegram_id=user_id)

    if ban_status:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=f"You are banned! Ban count: {ban_status['count']}"
        )
    else:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="hush."
        )

async def register_ban_words_handlers(dp: Dispatcher):
    dp.register_message_handler(check_message)
    dp.register_callback_query_handler(check_ban_status,lambda call: call.data == 'status')