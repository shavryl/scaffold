import inspect
from functools import wraps


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
        term = yield average
        total += term
        count += 1
        average = total/count
