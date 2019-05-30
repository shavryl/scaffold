from operator import *


class MyObj:
    """example class for attrgetter"""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)

l = [MyObj(i) for i in range(5)]
print('objects   :', l)

# extract the 'arg' value from each object
g = attrgetter('arg')
vals = [g(i) for i in l]
print('arg values:', vals)

# sort using arg
l.reverse()
print('reversed :', l)
print('sorted :', sorted(l, key=g))



ll = [dict(val=-1 * i) for i in range(4)]
print('Dictionaries:')
print('  original:', l)
g = itemgetter('val')
vals = [g(i) for i in ll]
print('    values:', vals)
print('    sorted:', sorted(ll, key=g))

print()
ll = [(i, i * -2) for i in range(4)]
print('\nTuples:')
print('  original:', ll)
g = itemgetter(1)
vals = [g(i) for i in ll]
print('   values:', vals)
print('   sorted:', sorted(ll, key=g))
