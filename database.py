import sqlite3
import logging
import os
import redis
import ujson

import config


class Cache(redis.StrictRedis):
    def __init__(self, host, port, password, charset="utf-8", decode_responses=True):
        super(Cache, self).__init__(host, port, password, charset=charset, decode_responses=decode_responses)
        logging.info("Redis started")

    def jset(self, name, value, ex=0):
        r = self.get(name)
        if r is None:
            return r
        return ujson.loads(r)

    def jget(self, name):
        return ujson.loads(self.get(name))


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
        cursor.execute('''CREATE TABLE local_rating (first_name Text, surname Text PRIMARY KEY, score INT)''')
        cursor.execute('''CREATE TABLE match_table (id INT PRIMARY KEY, place INT, command TEXT, points INT)''')
        connection.commit()
        cursor.close()

    def connection(self):
        db_path = os.path.join(os.getcwd(), f"{self.name}.db")
        if not os.path.exists(db_path):
            self.create_db()
        return sqlite3.connect(f"{self.name}.db")

    def execute_query(self, query, data=None, select=False, clear=False):
        cursor = self.conn.cursor()
        if select:
            cursor.execute(query)
            records = cursor.fetchone()
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
        select_query = f"""SELECT * FROM league_games WHERE id={game_id}"""
        record = self.execute_query(select_query, select=True)
        return record

    def insert_lg(self, league_games):
        for i, game in enumerate(league_games):
            while len(game) != 5:
                game.append('')
            insert_query = "INSERT OR REPLACE INTO league_games (id, hosts, guests, date, place, score) VALUES" \
                           "(?, ?, ?, ?, ?, ?)"
            self.execute_query(insert_query, data=(i, game[0], game[1], game[2], game[3], game[4]))

    def select_cg(self, game_id):
        select_query = f"""SELECT * FROM cup_games WHERE id={game_id}"""
        record = self.execute_query(select_query, select=True)
        return record

    def insert_cg(self, cup_games):
        for i, game in enumerate(cup_games):
            while len(game) != 6:
                game.append('')
            insert_query = "INSERT OR REPLACE INTO cup_games (id, round, hosts, guests, date, place, score) VALUES " \
                           "(?, ?, ?, ?, ?, ?, ?)"
            self.execute_query(insert_query, data=(i, game[0], game[1], game[2], game[3], game[4], game[5]))

    def select_lr(self, first_name, surname):
        select_query = f"""SELECT * FROM local_rating WHERE surname={surname} AND first_name={first_name}"""
        record = self.execute_query(select_query, select=True)
        return record

    def insert_or_update_lr(self, first_name, surname, points):
        record = self.select_lr(first_name, surname)
        if record:
            update_query = "UPDATE local_rating SET points=? WHERE (first_name=?) AND (surname=?)"
            self.execute_query(update_query, data=(record[2] + points, record[0], record[1]))
        else:
            insert_query = "INSERT INTO local_rating (first_name, surname, points) VALUES (?, ?, ?)"
            self.execute_query(insert_query, data=(first_name, surname, points))

    def clear_lg(self):
        insert_query = "DELETE FROM league_games"
        self.execute_query(insert_query, clear=True)

    def clear_cg(self):
        insert_query = "DELETE FROM cup_games"
        self.execute_query(insert_query, clear=True)

    def clear_lr(self):
        insert_query = "DELETE FROM local_rating"
        self.execute_query(insert_query, clear=True)



cache = Cache(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    password=config.REDIS_PASSWORD
)
database = Database(config.BOT_DB_NAME)
