from presetup.data_for_testing import (create_player,
    create_undead,
    InvalidCharacterNameError,
    create_character)
import pytest




class TestPlayerHits():

    player_name = 'vasya'
    undead_name = 'kolya'


    def test_player_hit(self):

        player = create_player(self.player_name)
        assert player['health'] == 100

        undead = create_undead(self.undead_name)
        create_undead.hit(player)
        assert player['health'] == 80

    def test_pretty(self):
        ...



def test_empty_name():

    with pytest.raises(InvalidCharacterNameError,
                       match='character name is empty'):
        create_character(name='', char_name='warrior')

