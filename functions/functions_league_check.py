from database import database
from ParserCVL.mainParser import parser


def cycle_cmp_db_tt(tt, responses, league=False):
    add = 0 if league else 1
    differences = []
    count = 0
    for i, match_tt in enumerate(tt):
        for j, match_db in enumerate(responses):
            if (match_tt[0 + add] == match_db[1 + add] and match_tt[1 + add] == match_db[2 + add]) or \
                    (match_tt[0 + add] == match_db[2 + add] and match_tt[1 + add] == match_db[1 + add]):
                count += 1
                if len(match_tt) == 3:
                    if match_tt[2 + add] != match_db[3 + add]:
                        differences.append([i, j, "postponed"])
                    break
                elif len(match_tt) == 4:
                    if match_tt[3 + add] == match_db[4 + add] and match_tt[2 + add] != match_db[3 + add]:
                        differences.append([i, j, "diff_time"])
                    elif match_tt[3 + add] != match_db[4 + add] and match_tt[2 + add] == match_db[3 + add]:
                        differences.append([i, j, "diff_place"])
                    elif match_tt[2 + add] != match_db[3 + add] and match_tt[3 + add] != match_db[4 + add]:
                        differences.append([i, j, "diff_time", "diff_place"])
                    break
                elif len(match_tt) == 5:
                    if match_tt[4 + add] != match_db[5 + add]:
                        differences.append([i, j, "played"])
                    break
    if league:
        return [responses, differences] if count == len(tt) else "new_season"
    elif len(tt) - len(responses) == 1:
        return "added_tour"
    else:
        return [responses, differences] if count == len(tt) else "new_season"


def make_responses(league=False):
    responses = []
    count = 0
    response = database.select_lg(count) if league else database.select_cg(count)
    while response:
        count += 1
        responses.append(response)
        response = database.select_lg(count) if league else database.select_cg(count)
    return responses


def compare_db_w_tt():
    league_tt = parser.get_league_timetable()
    cup_tt = parser.get_cup_timetable()
    responses_league = make_responses(league=True)
    responses_cup = make_responses()
    res_cmp_league = cycle_cmp_db_tt(league_tt, responses_league, league=True)
    res_cmp_cup = cycle_cmp_db_tt(cup_tt, responses_cup)
    return [res_cmp_league, res_cmp_cup]
