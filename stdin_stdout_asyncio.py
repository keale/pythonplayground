import asyncio
import sys

async def aio_readline(loop):
    while True:
        line = await loop.run_in_executor(None, sys.stdin.readline)
        print('Got line:', line, end='')

loop = asyncio.get_event_loop()
loop.run_until_complete(aio_readline(loop))
loop.close()