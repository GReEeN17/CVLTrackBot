from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from ParserCVL.mainParser import parser
from second_thread.cur_pos_check import make_resulting_message
from functions.function_position_check import compare_db_w_cur_pos


@dp.message_handler(commands=['see_cur_place'])
async def see_cur_place(message: types.Message):
    request = parser.get_current_position()
    differences = compare_db_w_cur_pos(request)
    res_message = make_resulting_message(differences, request)
    await bot.send_message(message.chat.id, res_message, parse_mode="Markdown")
