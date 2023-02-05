import mainTelegram
from ParserCVL import mainParser
from mainTelegram import dp
from aiogram import executor
import handlers
import unittest


def testingParser():
    mainParser.testing()

if __name__ == '__main__':
    #testingParser()
    executor.start_polling(dp, skip_updates=True, on_shutdown=mainTelegram.on_shutdown)

#создание топа игровоков (количество mvp)
#текущее место в таблице(?)