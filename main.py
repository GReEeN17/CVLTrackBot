import asyncio
import mainTelegram
from mainTelegram import dp
from aiogram import executor
from second_thread.sec_thr_main import periodic
import handlers


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(periodic())
    executor.start_polling(dp, skip_updates=True,  on_shutdown=mainTelegram.on_shutdown)

#создание топа игровоков (количество mvp)