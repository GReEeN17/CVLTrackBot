import sqlite3
import logging
import os

import config


class Database:
    def __init__(self, name):
        self.name = name
        self.conn = self.connection()
        logging.info("DATABASE CONNECTION ESTABLISHED")

    def create_db(self):
        connection = sqlite3.connect(f"{self.name}.db")
        logging.info("DATABASE CONNECTED")
        cursor = connection.cursor()
        cursor.execute(
            '''CREATE TABLE league_games (id INT PRIMARY KEY, hosts TEXT, guests TEXT, date TEXT, place TEXT, 
            score TEXT)''')
        cursor.execute(
            '''CREATE TABLE cup_games (id INT PRIMARY KEY, round TEXT, hosts TEXT, guests TEXT, date TEXT, 
            place TEXT, score TEXT)''')
        cursor.execute('''CREATE TABLE local_rating (first_name TEXT, surname TEXT PRIMARY KEY, points INT)''')
        cursor.execute('''CREATE TABLE cur_position (cur_pos INT, command TEXT PRIMARY KEY, 
        pl_games INT, points INT)''')
        cursor.execute('''CREATE TABLE telegram_ids (id INT PRIMARY KEY)''')
        connection.commit()
        cursor.close()

    def connection(self):
        db_path = os.path.join(os.getcwd(), f"{self.name}.db")
        if not os.path.exists(db_path):
            self.create_db()
        return sqlite3.connect(f"{self.name}.db")

    def execute_query(self, query, data=None, select=False, select_ids=False, clear=False):
        cursor = self.conn.cursor()
        if select:
            cursor.execute(query, data)
            records = cursor.fetchone()
            cursor.close()
            return records
        elif select_ids:
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            return records
        elif clear:
            cursor.execute(query)
            self.conn.commit()
        else:
            cursor.execute(query, data)
            self.conn.commit()
        cursor.close()

    def select_lg(self, game_id):
        select_query = "SELECT * FROM league_games WHERE id=?"
        record = self.execute_query(select_query, data=(game_id, ), select=True)
        return record

    def insert_lg(self, league_games):
        for i, game in enumerate(league_games):
            while len(game) != 5:
                game.append('')
            insert_query = "INSERT OR REPLACE INTO league_games (id, hosts, guests, date, place, score) VALUES" \
                           "(?, ?, ?, ?, ?, ?)"
            self.execute_query(insert_query, data=(i, game[0], game[1], game[2], game[3], game[4]))

    def select_cg(self, game_id):
        select_query = "SELECT * FROM cup_games WHERE id=?"
        record = self.execute_query(select_query, data=(game_id, ), select=True)
        return record

    def insert_cg(self, cup_games):
        for i, game in enumerate(cup_games):
            while len(game) != 6:
                game.append('')
            insert_query = "INSERT OR REPLACE INTO cup_games (id, round, hosts, guests, date, place, score) VALUES " \
                           "(?, ?, ?, ?, ?, ?, ?)"
            self.execute_query(insert_query, data=(i, game[0], game[1], game[2], game[3], game[4], game[5]))

    def select_lr(self, first_name, surname):
        select_query = "SELECT * FROM local_rating WHERE surname=? AND first_name=?"
        record = self.execute_query(select_query, data=(surname, first_name), select=True)
        return record

    def insert_or_update_lr(self, first_name, surname, points):
        record = self.select_lr(first_name, surname)
        if record:
            update_query = "UPDATE local_rating SET points=? WHERE (first_name=?) AND (surname=?)"
            self.execute_query(update_query, data=(record[2] + points, record[0], record[1]))
        else:
            insert_query = "INSERT INTO local_rating (first_name, surname, points) VALUES (?, ?, ?)"
            self.execute_query(insert_query, data=(first_name, surname, points))

    def select_telegram_ids(self):
        select_query = 'SELECT * FROM telegram_ids'
        record = self.execute_query(select_query, select_ids=True)
        return record

    def insert_telegram_id(self, telegram_id):
        insert_query = 'INSERT INTO telegram_ids (id) VALUES (?)'
        self.execute_query(insert_query, data=(telegram_id, ))

    def select_cur_pos(self):
        select_query = 'SELECT * FROM cur_position'
        record = self.execute_query(select_query, select_ids=True)
        return record

    def insert_cur_pos(self, cur_pos, command, pl_games, points):
        insert_query = 'INSERT INTO cur_position (cur_pos, command, pl_games, points) VALUES (?, ?, ?, ?)'
        self.execute_query(insert_query, data=(cur_pos, command, pl_games, points))

    def update_cur_pos(self, cur_pos, command):
        update_query = 'UPDATE cur_position SET cur_pos=? WHERE command=?'
        self.execute_query(update_query, data=(cur_pos, command))

    def update_pl_games(self, pl_games, command):
        update_query = 'UPDATE cur_position SET pl_games=? WHERE command=?'
        self.execute_query(update_query, data=(pl_games, command))

    def update_points(self, points, command):
        update_query = 'UPDATE cur_position SET points=? WHERE command=?'
        self.execute_query(update_query, data=(points, command))

    def clear_lg(self):
        clear_query = "DELETE FROM league_games"
        self.execute_query(clear_query, clear=True)

    def clear_cg(self):
        clear_query = "DELETE FROM cup_games"
        self.execute_query(clear_query, clear=True)

    def clear_lr(self):
        clear_query = "DELETE FROM local_rating"
        self.execute_query(clear_query, clear=True)

    def clear_ti(self):
        clear_query = "DELETE FROM telegram_ids"
        self.execute_query(clear_query, clear=True)

    def clear_cur_pos(self):
        clear_query = 'DELETE FROM cur_position'
        self.execute_query(clear_query, clear=True)


database = Database(config.BOT_DB_NAME)
