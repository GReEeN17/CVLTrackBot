from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from ParserCVL.mainParser import parser
import datetime

@dp.message_handler(commands=["show_next_game"])
async def get_next_game(message: types.Message):
    league_tt = parser.get_league_timetable()
    cup_tt = parser.get_cup_timetable()
    curr_time = datetime.datetime.now()

    '''if next_match is not None:
        match = league_tt[next_match]
        await bot.send_message(message.chat.id,
                               f"_Следующий матч:_ \n\n*· {match[0]} - {match[1]}*: " + f"_{match[2]}, {match[3]}_",
                               parse_mode="Markdown")
    elif rescheduled:
        resulted_message = '_Все несыгранные игры перенесены на неопрелённое время_:\n\n'
        for match in rescheduled_matches:
            resulted_message += f"*· {match[0]} - {match[1]}*: " + f"_{match[2]}_" + 2 * "\n"
        await bot.send_message(message.chat.id, resulted_message, parse_mode="Markdown")
    else:
        await bot.send_message(message.chat.id, "*Все игры сыграны!*\U0001F973", parse_mode="Markdown")'''
