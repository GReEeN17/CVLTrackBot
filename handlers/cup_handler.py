from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from ParserCVL.mainParser import parser
from second_thread.league_check import check_updates


@dp.message_handler(commands=["show_cup_tt"])
async def get_cup_timetable(message: types.Message):
    cup_tt = parser.get_cup_timetable()
    await check_updates()
    resulted_message = ''
    for match in cup_tt:
        if len(match) == 4:
            resulted_message += f"*·Тур {match[0]}, {match[1]} - {match[2]}*: " + f"_{match[3]}_" + 2 * "\n"
        elif len(match) == 5:
            resulted_message += f"*·Тур {match[0]}, {match[1]} - {match[2]}*: " + f"_{match[3]}, {match[4]}_" + 2 * "\n"
        else:
            resulted_message += f"*·Тур {match[0]}, {match[1]} - {match[2]}*: " + f"_{match[5]}_" + 2 * "\n"
    await bot.send_message(message.chat.id, resulted_message, parse_mode="Markdown")
