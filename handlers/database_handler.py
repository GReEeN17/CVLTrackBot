from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from ParserCVL.mainParser import parser
from database import database


@dp.message_handler(commands=["test_db"])
async def trying_receiving(message: types.Message):
    database.clear_cg()
    database.clear_lg()
    await bot.send_message(message.chat.id, "Success")
