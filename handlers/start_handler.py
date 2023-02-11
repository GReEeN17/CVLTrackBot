import sqlite3

from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from database import database
import main

@dp.message_handler(commands=["start"])
async def get_id (message: types.Message):
    try:
        database.insert_telegram_id(message.chat.id)
        await bot.send_message(message.chat.id, "ID данного чата успешно добавлен для рассылки")
    except sqlite3.IntegrityError:
        await bot.send_message(message.chat.id, "ID данного чата уже было добавлено в базу данных")
