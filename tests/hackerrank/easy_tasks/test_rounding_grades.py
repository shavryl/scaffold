import pytest
from hackerrank.easy_tasks.rounding_grades import gradingStudents, rounding
from pprint import pprint



def test_grading():
    expected = [1, 50, 66, 90, 100, 40, 37, 40, 56]
    data = [1, 50, 66, 88, 100, 38, 37, 39, 56]
    result = gradingStudents(data)
    pprint(result)

    assert result == expected
