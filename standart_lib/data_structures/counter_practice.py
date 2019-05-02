import collections



print(collections.Counter(a=4, b=2, c=17))

c = collections.Counter()
print(c)

c.update(z=11)
print(c)
# will not reassign value but add to it
c.update(z=3)
print(c)

# counter will not rise KeyError for unknown items
# if value has not been seen in the input its count is 0
print(c['a'])

# the elements() method will return iterator that produces
# all of the items known to the Counter. The order of elements
# is not guaranteed, and items with counts less than or equal
# to zero are not included
cd = collections.Counter(a=5, b=3, c=1, d=8)
print(list(cd.elements()))

print(cd.most_common())
