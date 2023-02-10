from database import database


def compare_db_w_cur_pos(cur_pos):
    record = database.select_cur_pos()
    differences = []
    if record[0] != cur_pos[0]:
        differences.append("diff_pos")
        database.update_cur_pos(int(cur_pos[0]), cur_pos[1])
    elif record[2] != cur_pos[2]:
        differences.append("diff_pl_games")
        database.update_pl_games(int(cur_pos[2]), cur_pos[1])
    elif record[3] != cur_pos[3]:
        differences.append("diff_points")
        database.update_points(int(cur_pos[3]), cur_pos[1])
    return differences
