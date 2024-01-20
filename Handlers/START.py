from aiogram import Dispatcher, Bot, types
from config import bot, MEDIA_DESTINATION
from Database import db
from keyboards import buttons
from python_file import START_COMMAND

async def start_massage(message: types.Message):
    data = db.DATABASE()
    data.insert_users_tg(
        Telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    print(message)
    with open(MEDIA_DESTINATION + "js.jpg", 'rb') as photo:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=photo,
            caption=START_COMMAND.format(
                name=message.from_user.first_name
            )
        )
        reply_markup = await buttons.keyboard()


def start_chat(dp: Dispatcher):
    dp.register_message_handler(start_massage, commands='start')