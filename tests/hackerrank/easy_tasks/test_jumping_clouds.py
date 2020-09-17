import pytest
from hackerrank.easy_tasks.jumping_clouds import jumping


c = [0, 1, 0, 0, 0, 0]


def test_jusmping():
    result = jumping(c)
    assert result