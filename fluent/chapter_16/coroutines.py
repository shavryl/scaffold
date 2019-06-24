import inspect
from functools import wraps
from collections import namedtuple


Result = namedtuple('Result', 'count average')


def coroutine(func):
    """
    decorator primes 'func' by advancing to first 'yield'
    """
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            # to return a value a coroutine must terminate normally
            # this is why this version has a condition to break out
            break
        total += term
        count += 1
        average = total/count
    # sending None terminates the loop causing coroutine to end by
    # returning the result, as usual generator raises StopIteration
    return Result(count, average)


class DemoException(Exception):
    """
    An exception for coroutines
    """

def demo_exc_handling():
    print(' coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('Demo Exception handled. Continuing...')
        else:
            print('coro received: {!r}'.format(x))

    raise RuntimeError('This line should never run')
