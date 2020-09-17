

c = [0, 1, 0, 0, 0, 0]


def jumping(c):
    jumps = 0
    cloud_list = list(enumerate(c))
    for item in cloud_list:
        print(item)
        check_index = item[0] + 2
        if check_index[1] != 1:
            jumps += 1
            return check_index
        else:
            check_index + 1
            jumps += 1
            return check_index

    return jumps