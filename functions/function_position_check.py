from database import database


def compare_db_w_cur_pos(cur_pos):
    record = database.select_cur_pos()
    differences = []
    if record:
        if int(record[0][0]) != int(cur_pos[0][0]):
            if int(record[0][0]) < int(cur_pos[0][0]):
                differences.append("diff_pos_up")
            else:
                differences.append("diff_pos_down")
            database.update_cur_pos(int(cur_pos[0]), cur_pos[1])
    else:
        database.insert_cur_pos(cur_pos[0], cur_pos[1], cur_pos[2], cur_pos[3])
    return differences
