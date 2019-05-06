import collections
from collections import ChainMap


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


class DeepChainMap(ChainMap):
    """
    The ChainMap class only makes updates (writes and deletions)to the first
    mapping in the chain while lookups will search the full chain. However,
    if deep writes and deletions are desired, it is easy to make a subclass
    that updates keys found deeper in the chain:
    """
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)






















