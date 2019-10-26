from collections import defaultdict
from pprint import pprint

pairs = [('first', 10), ('next', 17), ('last', 22)]


d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)


pprint(d)
