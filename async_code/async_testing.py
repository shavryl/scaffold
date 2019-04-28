import asyncio
from typing import Callable



async def f(notify: Callable[[str], None]):
    # Imagine a coroutine function f inside which it is necessary
    # to use loop.call_soon() to fire off another alerting function.
    # It might do logging, write messages into Slack, short stocks,
    # or anyting else you can think of!
    ...
    loop = asyncio.get_event_loop()
    # In this function we did not receive the loop via the function
    # parameters, so it is obtained via get_event_loop(); remember
    # this call always returns the loop that is associated with the
    # current thread.
    loop.call_soon(notify, 'Alert!')
    ...

