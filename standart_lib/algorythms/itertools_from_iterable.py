from itertools import *


def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ['a', 'b', 'c']

for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=' ')
print()

# The islice() function returns an iterator which returns
# selected items from the input iterator, by index
print('Stop at 5:')
for i in islice(range(100), 5):
    print(i, end=' ')
print('\n')

print('Start at 5, Stop at 10:')
for i in islice(range(100), 5, 10):
    print(i, end=' ')
print('\n')

print('By tens to 100:')
for i in islice(range(100), 0, 100, 10):
    print(i, end=' ')
print('\n')

# The tee() function returns several independent iterators
# defaults to 2 based on a single original input
r = islice(count(), 5)
i1, i2, i3, i4, i5 = tee(r, 5)

# if values are consumed from the original input,
# the new iterators will not produce those values:
print('r', end=' ')
for i in r:
    print(i, end=' ')
    if i > 1:
        break
print()

print('i1', list(i1))
print('i2', list(i2))
