import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from database import database as db

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def on_shutdown(dp):
    logging.warning('Shutting down..')
    db._conn.close()
    logging.warning("DB Connection closed")