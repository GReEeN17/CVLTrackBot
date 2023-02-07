import asyncio
from second_thread.league_check import check_updates


async def periodic():
    while True:
        await asyncio.sleep(10)
        await check_updates()
