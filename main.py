from aiogram import executor
from config import dp
from Handlers import START, questionnaire, chat_actions, registration, profile_2, reference
from Database import db

async def on_startup(_):
    data = db.DATABASE()
    data.sql_create_table()

    START.start_chat(dp=dp)
    await chat_actions.register_ban_words_handlers(dp=dp)
    registration.register_registration(dp=dp)
    profile_2.register_display_profile_handler(dp=dp)
    reference.register_menu_referral(dp=dp)


if __name__ == '__main__':
    executor.start_polling(
         dp,
         skip_updates=True,
         on_startup=on_startup
    )
