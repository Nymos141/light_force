from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from config import bot
from Database import db


async def keyboard():
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        'LETS GET STARTED!',
        callback_data='start_questionary'
    )

    check_ban_button = InlineKeyboardButton(
        'status',
        callback_data='status'
    )

    registration_button = InlineKeyboardButton(
        'Registration',
        callback_data='Registration'
    )

    profile_button = InlineKeyboardButton(
        'display profile',
        callback_data='display profile'
    )

    # all_profile_button = InlineKeyboardButton(
    #     'Start dating',
    #     callback_data='Start dating'
    # )
    # info_button = InlineKeyboardButton(
    #     'menu of destinations',
    #     callback_data='menu of destinations'
    # )

    news_button = InlineKeyboardButton(
        'last news',
        callback_data='last news'
    )
    markup.add(button, check_ban_button)
    markup.add(registration_button, profile_button, news_button)
    # markup.add(all_profile_button, info_button, news_button)
    return markup


async def referral_keyboard():
    markup = InlineKeyboardMarkup()
    reference_button = InlineKeyboardButton(
        "Generate Link ",
        callback_data="Generate_link"
    )

    reference_list_button = InlineKeyboardButton(
        "list reference ",
        callback_data="list reference "
    )
    markup.add(reference_button, reference_list_button)
    return markup


async def like_dislike_buttons(owner):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        'Like👍',
        callback_data=f'Like {owner}'
    )

    dislike_button = InlineKeyboardButton(
        'DisLike👎',
        callback_data=f'DisLike_ {owner}'
    )
    markup.add(like_button, dislike_button)
    return markup


async def first_question_button():
    markup = InlineKeyboardMarkup()
    first_button = InlineKeyboardButton('YES!', callback_data='YES')
    second_button = InlineKeyboardButton('NOT!', callback_data='NOT')
    markup.add(first_button, second_button)
    return markup

async def second_question_button():
    markup = InlineKeyboardMarkup()
    s_button = InlineKeyboardButton('sword of gryffindor!', callback_data='sword of gryffindor!')
    v_button = InlineKeyboardButton('vodka!', callback_data='vodka!')
    markup.add(s_button, v_button)
    return markup

async def third_answer_button():
    markup = InlineKeyboardMarkup()
    magical_button = InlineKeyboardButton('on a broomstick ', callback_data='on a broomstick ')
    not_magical_button = InlineKeyboardButton('camry 3.5', callback_data='camry 3.5')
    markup.add(magical_button, not_magical_button)
    return markup


async def yes_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Yeah, he has a scar'
    )

async def not_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='wrong answer'
    )

async def correct_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='you answered correctly 👍'
    )

async def incorrect_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="No, but I'd like to"
    )

async def third_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='correct answer'
    )

async def answer_third(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='damn bro 🗿'
    )
