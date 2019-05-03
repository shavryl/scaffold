import heapq
from standart_lib.data_structures.heap_data import data
from standart_lib.data_structures.heap_showtree import show_tree


heap = []
print('random', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)
    