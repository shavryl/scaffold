from math import floor


def sock_merchant(n, arr):
    result = 0

    differs = set(arr)

    for item in differs:
        counted = arr.count(item)
        if counted >= 1:
            devided = floor(counted / 2)
            result += devided

    return result