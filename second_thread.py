import asyncio
from mainTelegram import bot


async def periodic():
    while True:
        asyncio.sleep(10000)
        bot.send_message(1072674059, "working")
