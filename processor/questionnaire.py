from aiogram import Dispatcher, types
from config import bot, dp
from Database import db
from keyboards.buttons import yes_answer, not_answer, correct_answer, incorrect_answer, third_answer, answer_third
from keyboards import buttons

@dp.callback_query_handler(lambda c: c.data == 'start_questionary')
async def start_questionary_handler(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, 'Is Harry Potter famous for his scar?',
                           reply_markup=await buttons.first_question_button())

@dp.callback_query_handler(lambda c: c.data in ['YES', 'NOT'])
async def first_question_handler(call: types.CallbackQuery):
    if call.data == 'YES':
        await yes_answer(call)
    elif call.data == 'NOT':
        await not_answer(call)
    await second_question_handler(call)


async def second_question_handler(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, 'What Harry pulled out of the splitting hat.',
                           reply_markup=await buttons.second_question_button())

@dp.callback_query_handler(lambda c: c.data == 'sword of gryffindor!' or c.data == 'vodka!')
async def second(call: types.CallbackQuery):
    if call.data == 'sword of gryffindor!':
        await correct_answer(call)
    elif call.data == 'vodka!':
        await incorrect_answer(call)
    await third(call)


async def third(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, 'what the wizards in the Harry Potter movie flew on.',
                           reply_markup=await buttons.third_answer_button())


@dp.callback_query_handler(lambda c: c.data in ['on a broomstick ', 'camry 3.5'])
async def third_question_handler(call: types.CallbackQuery):
    if call.data == 'on a broomstick ':
        await third_answer(call)
    elif call.data == 'camry 3.5':
        await answer_third(call)

