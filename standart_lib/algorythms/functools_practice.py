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
print()


