from aiogram import Dispatcher, Bot, types
from config import bot, MEDIA_DESTINATION
from Database import db
from keyboards import buttons
from const import START_COMMAND



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
            chat_id=message.chat.id,
            photo=photo,
            caption=START_COMMAND.format(
                name=message.from_user.first_name
            ),
            reply_markup=await buttons.keyboard()
        )

async def last_news(call: types.CallbackQuery):
    data = db.DATABASE()
    scraper = Scraper()
    scrap = scraper.parse()

    for news_entry in scrap[:5]:
        data.insert_news_scrap(call.from_user.id, news_entry['link'])

        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Link: {news_entry['link']}\nImg: {news_entry['img_url']}"
        )

def start_chat(dp: Dispatcher):
    dp.register_message_handler(start_massage, commands=('start'))
    dp.register_callback_query_handler(last_news,
                                       lambda call: call.data == "last news")