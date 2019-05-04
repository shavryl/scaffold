import os
import sys
from math import ceil


def rounding(grade):

    for i in range(2):
        if grade % 5 != 0:
            grade +=1

    return grade



def gradingStudents(grades):

    result_list = []

    [result_list.append(rounding(grade))
        for grade in grades if grade >= 38]

    return result_list




if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
