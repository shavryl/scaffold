from heapq import heappush, heappop
import itertools


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [print(heappop(h)) for i in range(len(h))]

# list of entries arranged in a heap
pq = []
# mapping of tasks to entries
entry_finder = {}
# placeholder for a removed task
REMOVED = '<removed-task>'
# unique sequence count
counter = itertools.count()

# Removing the entry of changing its priotiry is more difficult because
# it would break the heap structure invariants. So a possible solution is
# to mark entry as removed and add a new entry with the rivised priority:

def add_task(task, priority=0):
    # Add a new task or update the priority of an existing task
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    # Mark an existing task as REMOVED. Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    # Remove and return the lowest priority task. Raise KeyError if empty.
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')
