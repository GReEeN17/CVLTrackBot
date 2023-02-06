import asyncio
from mainTelegram import bot


async def periodic():
    while True:
        await asyncio.sleep(10)
        await bot.send_message(1072674059, "working")
#sleep в секундах