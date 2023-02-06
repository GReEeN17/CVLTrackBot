import mainTelegram
from ParserCVL import mainParser
from mainTelegram import dp
from aiogram import executor
from second_thread import periodic
import handlers
import unittest


def testingParser():
    mainParser.testing()

if __name__ == '__main__':
    #testingParser()
    executor.start_polling(dp, skip_updates=True, on_shutdown=mainTelegram.on_shutdown)
    #dp.loop.create_task(periodic())

#создание топа игровоков (количество mvp)
#текущее место в таблице(?)