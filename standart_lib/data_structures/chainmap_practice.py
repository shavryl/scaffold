import collections


a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
d = {'d': 'D', 'b': 'Z'}

m = collections.ChainMap(a, b, d)


for k, v in m.items():
    print('{} = {}'.format(k, v))


lm = collections.ChainMap(a, b)

lm.maps = list(reversed(lm.maps))

rm = collections.ChainMap(a, b)

rm2 = rm.new_child()

rm2['c'] = 'E'

# for situations where the new context is known or built in advance
# it is also possible to pass a mapping to new_child()
c = {'c': 'E'}
tm = collections.ChainMap(a, b)
tm2 = tm.new_child(c)
# or another way
tm3 = collections.ChainMap(c, *tm.maps)
