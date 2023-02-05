from datetime import datetime

def set_next_game(league_tt, cup_tt, curr_time):
    rescheduled_league = False
    rescheduled_cup = False
    next_match_league = None
    next_match_cup = None
    rescheduled_league_matches = []
    rescheduled_cup_matches = []
    for i, match in enumerate(league_tt):
        if match[2] == 'перенесена на неопределенную дату':
            rescheduled_league = True
            rescheduled_league_matches.append(match)
            continue
        game_time = match[2].split(' ')
        day, month, year = list(map(int, game_time[0].split('.')))
        hour, minute = list(map(int, game_time[1].split(':')))
        match_date = datetime(year, month, day, hour, minute)
        if curr_time < match_date and next_match_league is None:
            next_match_league = i