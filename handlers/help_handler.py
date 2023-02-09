from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from functions.function_help import make_help_message


@dp.message_handler(commands=['help'])
async def get_help(message: types.Message):
    resulting_message = make_help_message()
    await bot.send_message(message.chat.id, resulting_message, parse_mode="Markdown")
