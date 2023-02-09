import asyncio
from second_thread.league_check import check_updates
from config import GAP_TIME


async def periodic():
    while True:
        await asyncio.sleep(GAP_TIME)
        await check_updates()
