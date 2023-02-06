from datetime import datetime


def compare_dates(curr_time, game_time, next_match, id_next_match, i):
    if next_match is not None:
        return [next_match, id_next_match]
    day, month, year = list(map(int, game_time[0].split('.')))
    hour, minute = list(map(int, game_time[1].split(':')))
    match_date = datetime(year, month, day, hour, minute)
    if curr_time < match_date:
        next_match = match_date
        return [next_match, i]
    else:
        return [next_match, None]


def set_next_game(league_tt, cup_tt, curr_time):
    next_match = None
    rescheduled_league = False
    rescheduled_cup = False
    next_match_league = None
    next_match_cup = None
    rescheduled_league_matches = []
    rescheduled_cup_matches = []
    id_next_league_match = None
    id_next_cup_match = None
    for i, match in enumerate(league_tt):
        if match[2] == 'перенесена на неопределенную дату':
            rescheduled_league = True
            rescheduled_league_matches.append(match)
            continue
        game_time = match[2].split(' ')
        next_match_league, id_next_league_match = \
            compare_dates(curr_time, game_time, next_match_league, id_next_league_match, i)
    for i, match in enumerate(cup_tt):
        if match[3] == "перенесена на неопределенную дату":
            rescheduled_cup = True
            rescheduled_cup_matches.append(match)
            continue
        game_time = match[3].split(' ')
        next_match_cup, id_next_cup_match = compare_dates(curr_time, game_time, next_match_cup, id_next_cup_match, i)
    return [rescheduled_league, rescheduled_cup, rescheduled_league_matches, rescheduled_cup_matches,
            next_match_league, next_match_cup, id_next_league_match, id_next_cup_match]


def make_league_match_mes(league_match):
    resulted_message = f"_Следующий матч это матч лиги:_ \n\n*· {league_match[0]} - {league_match[1]}*: "\
                       + f"_{league_match[2]}, {league_match[3]}_"
    return resulted_message


def make_cup_match_mes(cup_match):
    resulted_message = f"_Следующий матч это матч кубка:_ \n\n*·Тур {cup_match[0]}, {cup_match[1]} - {cup_match[2]}*: "\
                       + f"_{cup_match[3]}, {cup_match[4]}_"
    return resulted_message


def make_rescheduled_league_mes(rescheduled_league_matches):
    resulted_message = ''
    for match in rescheduled_league_matches:
        resulted_message += f"*· {match[0]} - {match[1]}*" + "\n"
    return resulted_message


def make_rescheduled_cup_mes(rescheduled_cup_matches):
    resulted_message = ''
    for match in rescheduled_cup_matches:
        resulted_message += f"*· {match[1]} - {match[2]}*" + "\n"
    return resulted_message
