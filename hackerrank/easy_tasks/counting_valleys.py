

def counting(n, s):
    result = 0
    start = 0

    for item in s:
        if item == 'U' and start == -1:
            start += 1
            result += 1
        elif item == 'U':
            start += 1
        else:
            start -= 1

    return result