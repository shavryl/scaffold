from hackerrank.easy_tasks.compare_triplets import compareTriplets
import random


def random_func():
    iterations = 3
    result = []
    while iterations:
        result.append(random.randint(0, 100))
        iterations -= 1
    return result

list_a = random_func()
list_b = random_func()

def test_compare(a=list_a, b=list_b):

    result = compareTriplets(a, b)
    print(result)
