from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from ParserCVL.mainParser import parser


@dp.message_handler(commands=['see_cur_place'])
async def see_cur_place(message: types.Message):
    parser.get_current_position()