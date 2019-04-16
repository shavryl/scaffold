import pytest
from hackerrank.medium_tasks.task_minion_game import generate_words, add_points, Player



class TestPlayer():

    _player = Player()

    the_string = 'ARTDDSEERSNNSDEERRTTEEW'

    def test_get_index(self):
        expected = (0, 'A')
        result = self._player.get_index()
        assert result == expected
