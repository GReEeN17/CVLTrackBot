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
