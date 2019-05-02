import collections
import threading
import time


d = collections.deque('abcdefg')
print('left end: ', d[0])
print('right end: ', d[-1])

d.remove('c')
print(d)

# add to the right
d1 = collections.deque()
print(d1)
d1.extend('ipqrstuvwxyz')
print(d1)
d1.append('1')
print(d1)


# add to the left
d2 = collections.deque()
# iterates over input and performs equivalent of an appendleft()
# for each item. The result is the input sequence in reverse order
d2.extendleft(range(6))
print(d2)
d2.appendleft('17')
print(d2)

# deques are thread safe
candle = collections.deque(range(50))

def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return


left = threading.Thread(target=burn,
                        args=('Left', candle.popleft))
right = threading.Thread(target=burn,
                         args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()
