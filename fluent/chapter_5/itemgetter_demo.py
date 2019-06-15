from operator import itemgetter, attrgetter, methodcaller, mul
from pprint import pprint
from collections import namedtuple
from functools import partial


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New Yourk-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

by_city = [city for city in sorted(metro_data, key=itemgetter(1))]

cc_name = itemgetter(1, 0)
jobb = [print(cc_name(city)) for city in metro_data]

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]
# retrieve nested attribute 'coord.lat'
name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))

s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))

hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))

triple = partial(mul, 3)
triple_res = [triple(num) for num in range(1, 10)]
print(triple_res)
