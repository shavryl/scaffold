from hackerrank.easy_tasks.counting_valleys import counting
import pytest


@pytest.mark.parametrize('steps, expected', [
    ('UUDDUU', 0), ('DDUUDDUUU', 2), ('DUDUDUDDUU', 4)
])
def test_count_socks(steps, expected):
    n = 10
    result = counting(n, steps)

    assert result == expected
