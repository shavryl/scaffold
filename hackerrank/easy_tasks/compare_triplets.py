import math
import os
import random
import re
import sys
from itertools import zip_longest




# Complete the compareTriplets function below.
def compareTriplets(a, b):

    lesiterables = zip_longest(a, b)

    def compare(iterable):

        Alice_score = 0
        Bob_score = 0

        for item in iterable:
            if item[0] > item[1]:
                Alice_score += 1
            elif item[0] < item[1]:
                Bob_score += 1

        return Alice_score, Bob_score

    result = compare(lesiterables)

    return list(result)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
