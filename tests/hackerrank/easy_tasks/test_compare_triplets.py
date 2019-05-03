import pytest
from hackerrank.easy_tasks.compare_triplets import compareTriplets
import random


def random_func():
    iterations = 3
    result = []
    while iterations:
        result.append(random.randint(0, 100))
        iterations -= 1
    return result


@pytest.mark.parametrize('list_a', 'list_b', [
    (random_func(), random_func())
    ])
def test_compare(list_a, list_b):

    result = compareTriplets(list_a, list_b)
    print(result)
