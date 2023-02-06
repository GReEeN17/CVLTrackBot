from database import database


def compare_db_w_tt(league_tt):
    differences = []
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
    count = 0
    for i, match_tt in enumerate(league_tt):
        for j, match_db in enumerate(responses):
            if (match_tt[0] == match_db[1] and match_tt[1] == match_db[2]) or (match_tt[0] == match_db[2] and
                                                                               match_tt[1] == match_db[1]):
                count += 1
                if len(match_tt) == 3:
                    if match_tt[2] != match_db[3]:
                        differences.append([i, j, "postponed"])
                    break
                elif len(match_tt) == 4:
                    if match_tt[3] == match_db[4] and match_tt[2] != match_db[3]:
                        differences.append([i, j, "diff_time"])
                    elif match_tt[3] != match_db[4] and match_tt[2] == match_db[3]:
                        differences.append([i, j, "diff_place"])
                    elif match_tt[2] != match_db[3] and match_tt[3] != match_db[4]:
                        differences.append([i, j, "diff_time", "diff_place"])
                    break
                elif len(match_tt) == 5:
                    if match_tt[4] != match_db[5]:
                        differences.append([i, j, "played"])
                    break
    return [responses, differences] if count == len(league_tt) else "all_played"


'''прописать случаи к каждому различию и сделать отводные ветки(else), в итоге функция будет возвращать 
массив из специальных параметров diff_time, diff_place, diff_result это будет возврщаться из функции 
в виде двух массивовв одном differences_site и differences_db далее в паралллеьном потоке от  работы
бота они будут обрабатываться и выкидывать на выходе различие, если таковые будут. Остаётся прописать логику
это будет муторно((('''

