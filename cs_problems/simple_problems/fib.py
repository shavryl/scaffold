from typing import Dict, Generator
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}  # base cases


def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 2) + fib(n - 1)
    return memo[n]


@lru_cache(maxsize=None)
def fib2(n):
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


def fib3(n):
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


def fib4(n):
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == "__main__":
    for i in fib4(50):
        print(i)
