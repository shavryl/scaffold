import pytest

from hackerrank.easy_tasks.repeated_string import count_letters


@pytest.mark.parametrize('string, length, expected', [
    ('onetwothree', 33, 0),
    ('aab', 12, 8),
    ('a', 9, 9),
    ('', 7, 0),
    ('abc', 7, 3),
    ])
def test_count_letters(string, length, expected):
    result = count_letters(string, length)
    assert result == expected
