import heapq
from standart_lib.data_structures.heap_showtree import show_tree
from standart_lib.data_structures.heap_data import data


heapq.heapify(data)
print('start')
show_tree(data)

for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print('replace {} with {}'.format(smallest, n))
    show_tree(data)
