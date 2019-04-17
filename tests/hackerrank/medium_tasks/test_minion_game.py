import pytest
from hackerrank.medium_tasks.task_minion_game import Player


result_list = [
    [0], [3, 4, 13],
    [6, 7, 14, 15, 20, 21],
    [10, 11],[1, 8, 16, 17],
    [5, 9, 12], [2, 18, 19]
]


class TestPlayer():

    _player = Player()

    the_string = 'ARTDDSEERSNNSDEERRTTEEW'

    def test_get_index(self):
        expected = result_list
        result = self._player.get_index()
        assert result == expected

    def test_buid_words(self):
        result = self._player.build_words(result_list)
        assert 'A' in result
