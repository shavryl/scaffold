import functools


@functools.singledispatch
def myfunc(arg):
    print('default myfunc({!r})'.format(arg))


# The register attribute of the new function serves as another decorator
# for registering alternative implementations. The first function wrapped
# with singledispatch() is the default implementation if no other type-
# specific function is found, as with the float case in this example.
@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))

@myfunc.register(list)
def myfunc_list(arg):
    print('myfunc_list()')
    for item in arg:
        print('  {}'.format(item))


myfunc('string argument')
myfunc(1)
myfunc(2.3)
myfunc(['a', 'b', 'c'])
