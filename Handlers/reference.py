from aiogram import Dispatcher, types
from config import bot
from keyboards import buttons
from Database.db import DATABASE
from aiogram.utils.deep_linking import _create_link
import os
import binascii
from const import REFERENCE_TEXT


async def reference_menu(call: types.CallbackQuery):
    data = DATABASE()
    data = data.sql_select_referral_menu(
        owner=call.from_user.id
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text=REFERENCE_TEXT.format(
            user=call.from_user.first_name,
            balance=data['balance'],
            total_referrals=['total_referrals']
        )
    )

async def link_issuance(call: types.CallbackQuery):
    data = DATABASE()
    user = data.select_tg_users(telegram_id=call.from_user.id)
    if not user['reference_link']:
        token = binascii.hexlify(os.urandom(8)).decode()
        citation = await _create_link('start', payload=token)
        print(citation)
        data.update_tg_users(
            reference_link=reference_menu,
            telegram_id=call.from_user.id
        )
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"it's new link {user['reference_menu']}"
        )

    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"it's old link {user['reference_link']}"
        )

async def list_of_referrals(call: types.CallbackQuery):
    data = DATABASE()
    referrals = data.select_reference_users(owner_telegram_id=call.from_user.id)

    if referrals:
        referrals_text = "\n".join([f"{index + 1}. {referral['first_name']} ({referral['username']})"
                                    for index, referral in enumerate(referrals)])
        message_text = f"Your Referrals:\n{referrals_text}"
    else:
        message_text = "You don't have any referrals yet."

    await bot.send_message(
        chat_id=call.from_user.id,
        text=message_text
    )


def register_menu_referral(dp: Dispatcher):
    dp.register_callback_query_handler(reference_menu,
                                       lambda call: call.data == "reference_menu")
    dp.register_callback_query_handler(link_issuance, lambda call: call.data == "Generate_link")
    dp.register_callback_query_handler(list_of_referrals, lambda call: call.data == "list reference ")