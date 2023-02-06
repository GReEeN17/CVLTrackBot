from database import database


def compare_db_w_tt(league_tt):
    differences_site = []
    differences_db = []
    new_season = False
    responses = []
    count = 0
    response = database.select_lg(count)
    while response:
        count += 1
        responses.append(response)
        response = database.select_lg(count)
    if len(league_tt) != len(responses):
        new_season = True
    for i, match_tt in enumerate(league_tt):
        for j, match_db in enumerate(response):
            if (match_tt[0] == match_db[1] and match_tt[1] == match_db[2]) or (match_tt[0] == match_db[2] and match_tt[1] == match_db[1]):
                if match_tt[2] == match_db[3]:
                    '''прописать случаи к каждому различию и сделать отводные ветки(else), в итоге функция будет возвращать 
                    массив из специальных параметров diff_time, diff_place, diff_result это будет возврщаться из функции 
                    в виде двух массивовв одном differences_site и differences_db далее в паралллеьном потоке от  работы
                    бота они будут обрабатываться и выкидывать на выходе различие, если таковые будут. Остаётся прописать логику
                    это будет муторно((('''

