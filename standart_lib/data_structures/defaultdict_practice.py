import collections


def default_factory():
    return 'default'


d = collections.defaultdict(default_factory, foo='bar')
print(d)
print(d['foo'])
print(d['something'])
print(d['once_again'])