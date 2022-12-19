import logging
from aiogram import Bot, Dispatcher, types
from config import TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher(bot)

'''conn = sqlite3.connect(":memory:")
cursor = conn.cursor()'''

