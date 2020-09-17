from typing import Dict
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




if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
    print(fib2(50))