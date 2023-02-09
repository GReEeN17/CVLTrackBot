from mainTelegram import bot
from functions.functions_league_check import compare_db_w_tt
from ParserCVL.mainParser import parser
from database import database


def make_resulting_message(tt, responses, differences, league=False):
    competition = 'лиги' if league else 'кубка'
    add = 0 if league else 1
    if len(differences) == 0:
        return f'Изменений в расписании {competition} нету'
    resulting_message = f'Изменение в расписании {competition}: \n'
    for elem in differences:
        if elem[2] == 'postponed':
            resulting_message += f'· Матч {competition} {tt[elem[0]][0 + add]} - {tt[elem[0]][1 + add]} ' \
                                 f'перенесён на неопределённое время\n\n'
        elif elem[2] == 'diff_time' and elem[3] == 'diff_place':
            resulting_message += f'· Матч {competition} {tt[elem[0]][0 + add]} - {tt[elem[0]][1 + add]} ' \
                                 f'перенесён по времени и месту\n' \
                                 f'Было: {responses[elem[1]][3 + add]}, {responses[elem[1]][4 + add]}\n' \
                                 f'Стало: {tt[elem[0]][2 + add]}, {tt[elem[0]][3 + add]}\n\n'
        elif elem[2] == 'diff_time':
            resulting_message += f'· Матч {competition} {tt[elem[0]][0 + add]} - {tt[elem[0]][1 + add]} ' \
                                 f'перенесён по времени\n' \
                                 f'Было: {responses[elem[1]][3 + add]}\n' \
                                 f'Стало: {tt[elem[0]][2 + add]}\n\n'
        elif elem[2] == 'diff_place':
            resulting_message += f'· Матч {competition} {tt[elem[0]][0 + add]} - {tt[elem[0]][1 + add]} ' \
                                 f'перенесён по месту\n' \
                                 f'Было: {responses[elem[1]][4 + add]}\n' \
                                 f'Стало:{tt[elem[0]][3 + add]}\n\n'
        elif elem[2] == 'played':
            resulting_message += f'· Матч {competition} {tt[elem[0]][0 + add]} - {tt[elem[0]][1 + add]} сыгран \n' \
                                 f'Счёт: {tt[elem[0]][4 + add]}'
    return resulting_message


async def check_updates():
    league_tt = parser.get_league_timetable()
    cup_tt = parser.get_cup_timetable()
    cmp_res = compare_db_w_tt(league_tt, cup_tt)
    new_season_l, new_season_c = False, False
    responses_c, differences_c = None, None
    responses_l, differences_l = None, None
    if cmp_res[0] == 'new_season' and cmp_res[1] == 'new_season':
        new_season_l = True
        new_season_c = True
    elif cmp_res[0] == 'new_season' and cmp_res[1] != 'new_season':
        new_season_l = True
        responses_c, differences_c = cmp_res[1][0], cmp_res[1][1]
    elif cmp_res[0] != 'new_season' and cmp_res[1] == 'new_season':
        new_season_c = True
        responses_l, differences_l = cmp_res[0][0], cmp_res[0][1]
    else:
        responses_l, differences_l = cmp_res[0][0], cmp_res[0][1]
        responses_c, differences_c = cmp_res[1][0], cmp_res[1][1]
    id_response = database.select_telegram_ids()
    if id_response:
        for i in id_response:
            if new_season_l:
                await bot.send_message(int(i[0]), 'Начался новый сезон лиги, чтобы посмотреть актуальное расписание'
                                                  ' лиги наберите */show_league_tt*', parse_mode='Markdown')
            if new_season_c:
                await bot.send_message(int(i[0]), 'Начался новый сезон лиги, чтобы посмотреть актуальное расписание'
                                                  ' кубка наберите */show_cup_tt*', parse_mode='Markdown')
            if not new_season_l:
                res_message = make_resulting_message(league_tt, responses_l, differences_l, league=True)
                await bot.send_message(int(i[0]), res_message, parse_mode='Markdown')
            if not new_season_c:
                res_message = make_resulting_message(cup_tt, responses_c, differences_c)
                await bot.send_message(int(i[0]), res_message, parse_mode='Markdown')

