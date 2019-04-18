import pytest
from hackerrank.medium_tasks.task_minion_game import Player, Competition


result_list = [
    [0], [3, 4, 13],
    [6, 7, 14, 15, 20, 21],
    [10, 11],[1, 8, 16, 17],
    [5, 9, 12], [2, 18, 19]
]

list_of_words = [
    'A', 'AR', 'ART', 'ARTD'
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

    def test_count_points(self):
        expected = 4
        result = self._player.count_points(list_of_words)
        assert expected == result

    def test_competition(self):
        round = Competition(self.the_string)
        expected = 'Kevin wins'
        result = round.compare_result()
        assert result == expected
