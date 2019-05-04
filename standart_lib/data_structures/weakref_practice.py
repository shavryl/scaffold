import weakref
import sys


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

def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


obj = ExpensiveObject()
r = weakref.ref(obj, callback)
f = weakref.finalize(obj, on_finalize, 'extra argument')
# finalize instance has a writable propertly atexit to
# control whether the callback is invoked as a program
# is exiting, if it hasn't already been called.
f.atexit = bool(int(sys.argv[1]))


print(obj)
print(r)
print('r()', r())

print('deleting')
del obj
print('r()', r())

