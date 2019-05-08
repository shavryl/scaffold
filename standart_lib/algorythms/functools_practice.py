import functools



def myfunc(a, b=2):
    # Docstring for myfunc().
    print('  called myfunc with:', (a, b))

def show_details(name, f, is_partial=False):
    # Show details of a callable object
    print('{}:'.format(name))
    print('  object:', f)
    if not is_partial:
        print('  __name__:', f.__name__)
    if is_partial:
        print('  func:', f.func)
        print('  func:', f.args)
        print('  keywords:', f.keywords)
    return

show_details('myfunc', myfunc)
myfunc('a', 3)


# the partial object does not have __name__ or __doc__ attributes
# by default, and without those attributes, decorated functions are
# more difficult to defug. Using update_wrapper(), copies or adds
# attributes from the original function to the partial object.
p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)
print('Updating wrapper:')
print('  assign:', functools.WRAPPER_ASSIGNMENTS)
print('  update:', functools.WRAPPER_UPDATES)
print()

# Attributes added to the wrapper are defined in WRAPPER_ASSIGNMENTS,
# while WRAPPER_UPDATES lists values to be modifies.
functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)


class MyClass:

    def __call__(self, e, f=6):
        "Docstring for MyClass.__call__"
        print('  called object with:', (self, e, f))


def show_details2(name, f):
    'Show details of a callable object.'
    print('{}:'.format(name))
    print('   object:', f)
    print('   __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__', repr(f.__doc__))
    return


o = MyClass()

show_details2('instance', o)
o('e goes here')
print()

p = functools.partial(o, e='default for e', f=8)
functools.update_wrapper(p, o)
show_details2('instance wrapper', p)
p()


























