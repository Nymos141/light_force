from aiogram import Dispatcher, Bot, types
from config import bot
from Database import db
from keyboards import buttons

async def start_massage(message: types.Message):
    data = db.DATABASE()
    data.insert_users_tg(
        Telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    print(message)
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Hi {message.from_user.first_name}',
        reply_markup=await buttons.keyboard()
    )

def start_chat(dp: Dispatcher):
    dp.register_message_handler(start_massage, commands='start')