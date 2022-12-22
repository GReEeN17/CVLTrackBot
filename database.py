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
            records = cursor
        self.conn.commit()
        cursor.close()


    def selectLG(self, game_id):
        select_query = f"""SELECT * FROM league_games WHERE id={game_id}"""



    def insertLG(self, league_games):
        for i, game in enumerate(league_games):
            insert_query = f"""INSERT"""

