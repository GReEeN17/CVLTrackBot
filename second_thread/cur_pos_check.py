from mainTelegram import bot
from functions.function_position_check import compare_db_w_cur_pos
from database import database
from ParserCVL.mainParser import parser


def make_resulting_message(differences, request):
    resulting_message = ''
    for diff in differences:
        if diff == "diff_pos":
            resulting_message += ''


def check_cur_pos():
    request = parser.get_current_position()
    differences = compare_db_w_cur_pos(request)
    telegram_ids = database.select_telegram_ids()
    if telegram_ids:
        for tid in telegram_ids:
            if len(differences) == 0:
                await bot.send_message(tid, "Изменений в текущей позиции команды нету")
                continue

