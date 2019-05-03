import heapq
from standart_lib.data_structures.heap_showtree import show_tree
from standart_lib.data_structures.heap_data import data


print('random   :', data)
heapq.heapify(data)
print('heapified')
show_tree(data)
