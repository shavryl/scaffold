import queue
import functools
import threading


q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()

# stack data structure : last in first out
q = queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()

# priority queue
@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


q = queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(3, 'Mid-level job'))
q.put(Job(3, 'Mid-level job'))
q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))

def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()

workers = [
    threading.Thread(target=process_job, args=(q, )),
    threading.Thread(target=process_job, args=(q, )),
    threading.Thread(target=process_job, args=(q, )),
]

for w in workers:
    w.setDaemon(True)
    w.start()

q.join()























