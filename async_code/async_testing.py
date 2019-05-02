import asyncio
from typing import Callable
from itertools import zip_longest



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


ls = range(40)
res = list(ls)


def func3():
    reslist = []

    for x in ls:
        if x % 3 != 0:
            reslist.append(x)

    return reslist


def func2():
    reslist = []

    for x in ls:
        if x % 2 != 0:
            reslist.append(x)

    return reslist

l1, l2, l3 = func3(), func2(), res

result = zip_longest(l1, l2, l3)
for i in result:

    print(i)
