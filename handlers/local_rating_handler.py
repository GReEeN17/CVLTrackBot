from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from database import database


@dp.message_handler(commands=['add_points'])
async def add_points(message: types.Message):
    info = message.text.split(' ')
    database.insert_or_update_lr(info[2], info[1], int(info[3]))
    record = database.select_lr(info[2], info[1])
    await bot.send_message(message.chat.id, f"Очки добавлены:\nСейчас у игрока _{info[1]} {info[2]}_  - "
                                            f"*{record[2]} очков*", parse_mode="Markdown")
