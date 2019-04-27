import time
import asyncio
from concurrent.futures import ThreadPoolExecutor as Executor


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')
    loop.stop()


def blocking():
    time.sleep(2.0)
    print(f"{time.ctime()} Hello from a thread!")


loop = asyncio.get_event_loop()
executor = Executor()
# you have to set your custom executor as the default one for
# the loop. This means that anywhere the code calls
# run_in_executor() it will be using your custom instance
loop.set_default_executor(executor)
loop.create_task(main())
future = loop.run_in_executor(None, blocking)
loop.run_forever()
tasks = asyncio.Task.all_tasks(loop=loop)
for t in tasks:
    t.cancel()
group = asyncio.gather(*tasks, return_exceptions=True)
loop.run_until_complete(group)
# we can explicitly wait for all the executor jobs to finish
# before closing the loop. This will avoid the "Event loop is
# closed" messages. We can do this because we have access to
# the executor object; the default executor is not exposed
# in the asyncio API which is why we cannot call shutdown on it.
executor.shutdown(wait=True)
# finally we have a strategy with general applicability: you
# can call run_in_executor() anywhere and your program will
# still shut down cleanly.
loop.close()
