from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from ParserCVL.mainParser import parser
import datetime
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


@dp.message_handler(commands=["show_next_game"])
async def get_next_league_game(message:types.Message):
    league_tt = parser.get_league_timetable()
    rescheduled = False
    next_match = None
    curr_time = datetime.datetime.now()
    rescheduled_matches = []
    for i, match in enumerate(league_tt):
        if match[2] == 'перенесена на неопределенную дату':
            rescheduled = True
            rescheduled_matches.append(match)
            continue
        game_time = match[2].split(' ')
        day, month, year = list(map(int, game_time[0].split('.')))
        hour, minute = list(map(int, game_time[1].split(':')))
        match_date = datetime.datetime(year, month, day, hour, minute)
        if curr_time < match_date and next_match is None:
            next_match = i
    if next_match is not None:
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
        await bot.send_message(message.chat.id, "*Все игры сыграны!*\U0001F973", parse_mode="Markdown")




