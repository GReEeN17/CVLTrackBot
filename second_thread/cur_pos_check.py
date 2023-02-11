from mainTelegram import bot
from functions.function_position_check import compare_db_w_cur_pos
from database import database
from ParserCVL.mainParser import parser


def make_resulting_message(differences, request):
    resulting_message = ''
    if 'diff_pos_up' in differences:
        resulting_message += f"Команда *{request[1]}* поднялась в таблице лиги\n\n"
    elif 'diff_pos_down' in differences:
        resulting_message += f"Команда *{request[1]}* опустилась в таблице лиги\n\n"
    resulting_message += f"Текущее место команды *{request[1]}*: *{request[0]}*\n" \
                         f"Количество очков: *{request[3]}*"
    return resulting_message


async def check_cur_pos():
    request = parser.get_current_position()
    differences = compare_db_w_cur_pos(request)
    telegram_ids = database.select_telegram_ids()
    if telegram_ids:
        for tid in telegram_ids:
            if len(differences) == 0:
                continue
            res_message = make_resulting_message(differences, request)
            await bot.send_message(tid, res_message, parse_mode="Markdown")
