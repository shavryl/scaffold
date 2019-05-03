import heapq
from standart_lib.data_structures.heap_showtree import show_tree
from standart_lib.data_structures.heap_data import data



print('random', data)
heapq.heapify(data)
print('heapified')
show_tree(data)
print()

for i in range(2):
    smallest = heapq.heappop(data)
    print('pop {}'.format(smallest))
    show_tree(data)
    