from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
import main

@dp.message_handler()
async def get_admin_id (message: types.Message):
    if message.text == 'admin':
        await bot.send_message(message.chat.id, 'admin_id = {}'.format(message.chat.id))