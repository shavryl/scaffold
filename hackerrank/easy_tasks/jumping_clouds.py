

def jumping(c):
    count = 0
    i = 0
    try:
        while i < (len(c) - 1):
            if c[i + 2] == 0:
                i += 2
                count +=1
            else:
                i -= 1
        return count
    except IndexError as e:
        return count
