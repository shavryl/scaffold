import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))

def callback(reference):
    """
    Invoked when referenced obj is deleted. This callback
    receives the reference object as an argument after
    the reference is 'dead' and no longer refers to the
    original object. One use for this feature is to
    remove the weak reference object from a cache.
    """
    print('callback({!r}'.format(reference))


obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print(obj)
print(r)
print('r()', r())

print('deleting')
del obj
print('r()', r())

