import functools



def standalone(self, a=1, b=2):
    "Standalone function"
    print('  called standalone with:', (self, a, b))
    if self is not None:
        print('  self.attr=', self.attr)


class MyClass:
    "Demonstration class for functools"

    def __init__(self):
        self.attr = 'instance attribute'

    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)


o = MyClass()
print('standalone')
standalone(None)
print()

print('method1 as partialmethod')
o.method1()
print()

# method1() can be called from an instance of MyClass and the instance
# is passed as the first argument just as with methods defined normally.
# method2() is not set up as a bound method, and so the self argument
# must be passed explicitly, or the call will result in a TypeError
print('method2 as partial')
try:
    o.method2()
except TypeError as err:
    print('ERROR: {}'.format(err))
