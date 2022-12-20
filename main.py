from ParserCVL import mainParser
from mainTelegram import dp
from aiogram import executor
import handlers


def testingParser():
    mainParser.testing()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

