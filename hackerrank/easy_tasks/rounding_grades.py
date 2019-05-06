import os
import sys
from math import ceil


def rounding(grade):

    base = 5
    new_number = base * ceil(grade/base)

    if new_number - grade < 3:
        result = new_number
    else:
        result = grade

    return result


def gradingStudents(grades):

    result_list = []

    [result_list.append(rounding(grade)) if grade >=38
     else result_list.append(grade) for grade in grades]

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
