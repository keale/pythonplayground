import asyncio
import time 

async def task_waiting_for_event(event, name, timeout):
    try:
        await asyncio.wait_for(event.wait(), timeout)
        #await asyncio.sleep(1)
    except asyncio.TimeoutError:
        pass

event = asyncio.Event()

async def main():
    start = time.time()
    tasks = [asyncio.create_task(task_waiting_for_event(event, str(i), 7)) for i in range(1000)]

   # await asyncio.sleep(1)
    event.set()
    await asyncio.gather(*tasks)
    dauer = time.time() - start
    print(f"Ausführungsdauer: {dauer}")

asyncio.run(main())