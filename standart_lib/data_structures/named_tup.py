import collections


Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age='30')
print(bob)

jane = Person(name='Jane', age='29')


for p in [bob, jane]:
    print(p._fields)



dd = jane._asdict()
print(dd)


robert = bob._replace(name='Robert')
print(robert)

print(bob is robert)