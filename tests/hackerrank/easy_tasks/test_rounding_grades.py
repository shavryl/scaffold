import pytest
from hackerrank.easy_tasks.rounding_grades import gradingStudents
from pprint import pprint



def test_rounding():
    expected = [50, 70, 90, 100, 40, 39, 60]
    data = [1, 50, 66, 88, 100, 38, 37, 39, 56]
    result = gradingStudents(data)
    pprint(result)

    assert result == expected

