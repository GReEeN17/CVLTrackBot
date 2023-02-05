from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
import main

@dp.message_handler(commands=["admin"])
async def get_admin_id (message: types.Message):
    await bot.send_message(message.chat.id, 'admin_id = {}'.format(message.chat.id))