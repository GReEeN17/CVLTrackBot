from mainTelegram import dp
from mainTelegram import bot
from aiogram import types
from ParserCVL.mainParser import parser
from support_handlers.date_comparasion import set_next_game
from support_handlers.date_comparasion import make_league_match_mes, make_cup_match_mes
from support_handlers.date_comparasion import make_rescheduled_league_mes, make_rescheduled_cup_mes
import datetime

@dp.message_handler(commands=["show_next_game"])
async def get_next_game(message: types.Message):
    league_tt = parser.get_league_timetable()
    cup_tt = parser.get_cup_timetable()
    curr_time = datetime.datetime.now()
    set_game = set_next_game(league_tt, cup_tt, curr_time)
    rescheduled_league = set_game[0]
    rescheduled_cup = set_game[1]
    rescheduled_league_matches = set_game[2]
    rescheduled_cup_matches = set_game[3]
    next_match_league = set_game[4]
    next_match_cup = set_game[5]
    id_next_match_league = set_game[6]
    id_next_match_cup = set_game[7]
    if next_match_league is not None or next_match_cup is not None:
        if next_match_league is not None and next_match_cup is None:
            league_match = league_tt[id_next_match_league]
            resulted_message = make_league_match_mes(league_match)
            await bot.send_message(message.chat.id, resulted_message, parse_mode="Markdown")
        elif next_match_league is None and next_match_cup is not None:
            cup_match = cup_tt[id_next_match_cup]
            resulted_message = make_cup_match_mes(cup_match)
            await bot.send_message(message.chat.id, resulted_message, parse_mode="Markdown")
        else:
            if next_match_league < next_match_cup:
                match = league_tt[id_next_match_league]
                resulted_message = make_league_match_mes(match)
            else:
                match = cup_tt[id_next_match_cup]
                resulted_message = make_cup_match_mes(match)
            await bot.send_message(message.chat.id, resulted_message, parse_mode="Markdown")
    elif rescheduled_league or rescheduled_cup:
        resulted_message = '_Все несыгранные игры перенесены на неопрелённое время_:\n\n'
        if rescheduled_league:
            resulted_message += "*Матчи лиги:*\n"
            resulted_message += make_rescheduled_league_mes(rescheduled_league_matches)
        if rescheduled_cup:
            resulted_message += "*Матчи кубка:*\n"
            resulted_message += make_rescheduled_cup_mes(rescheduled_cup_matches)
        await bot.send_message(message.chat.id, resulted_message, parse_mode="Markdown")
    else:
        await bot.send_message(message.chat.id, "*Все игры сыграны!*\U0001F973", parse_mode="Markdown")



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
