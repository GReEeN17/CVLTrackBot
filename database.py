import sqlite3
import logging
import os

class Database:
    def __init__(self, name):
        self.name = name
        self.conn = self.connection()
        logging.info("DATABASE CONNECTION ESTABLISHED")

    def create_db(self):
        connection = sqlite3.connect(f"{self.name}.db")
        logging.info("DATABASE CONNECTED")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE league_games (id INT PRIMARY KEY, hosts TEXT, guests TEXT, date TEXT, place TEXT, score TEXT)''')
        cursor.execute('''CREATE TABLE cup_games (id INT PRIMARY KEY, round TEXT, hosts TEXT, guests TEXT, date TEXT, place TEXT, score TEXT)''')
        cursor.execute('''CREATE TABLE table (id INT PRIMARY KEY, place INT, command TEXT, points INT)''')
        connection.commit()
        cursor.close()

    def connection(self):
        db_path = os.path.join(os.getcwd(), f"{self.name}.db")
        if not os.path.exists(db_path):
            self.create_db()
        return sqlite3.connect(f"{self.name}.db")


    def execute_query(self, query, select=False):
        cursor = self.conn.cursor()
        cursor.execute(query)
        if select:
            records = cursor.fetchone()
            cursor.close()
            return records
        else:
            self.conn.commit()
        cursor.close()


    async def selectLG(self, game_id):
        select_query = f"""SELECT * FROM league_games WHERE id={game_id}"""
        record = self.execute_query(select_query, select=True)
        return record


    async def insertLG(self, league_games):
        for i, game in enumerate(league_games):
            while len(game) != 5:
                game.append('')
            insert_query = f"""INSERT OR REPLACE INTO league_games (id, hosts, guests, date, place, score) VALUES 
                               ({i}, {game[0]}, {game[1]}, {game[2]}, {game[3]}, {game[4]})"""
            self.execute_query(insert_query)


    async def selectCG(self, game_id):
        select_query = f"""SELECT * FROM cup_games WHERE id={game_id}"""
        record = self.execute_query(select_query, select=True)
        return record


    async def insertCG(self, cup_games):
        for i, game in enumerate(cup_games):
            while len(game) != 6:
                game.append('')
            insert_query = f"""INSERT OR REPLACE INTO cup_games (id, round, hosts, guests, date, place, score) VALUES ({i}, {game[0]}, {game[1]}, {game[2]}, {game[3]}, {game[4]}, {game[5]})"""
























