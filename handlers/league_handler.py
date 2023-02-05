from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from ParserCVL.mainParser import parser
import main

@dp.message_handler(commands=["show_league_tt"])
async def get_league_timetable(message: types.Message):
    league_tt = parser.get_league_timetable()
    resulted_message = ''
    for match in league_tt:
        if len(match) == 3:
            resulted_message += f"*· {match[0]} - {match[1]}*: " + f"_{match[2]}_" + 2 * "\n"
        elif len(match) == 4:
            resulted_message += f"*· {match[0]} - {match[1]}*: " + f"_{match[2]}, {match[3]}_" + 2 * "\n"
        else:
            resulted_message += f"*· {match[0]} - {match[1]}*: " + f"_{match[4]}_" + 2 * "\n"
    await bot.send_message(message.chat.id, resulted_message, parse_mode="Markdown")





