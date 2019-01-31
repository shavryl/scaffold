from collections import namedtuple


def create_player(name):

    player = {'name': name,
              'health': 100}
    return player

def create_undead(name):

    undead = {'name': name,
              'health': 300}

    def hit(target):
        return target['health'] - 20

    return undead


def create_character(name: str, char_name: str):
    """
    Creates a new character and inserts it into the database.
    """
    if not name:
        msg = 'character name is empty'
        raise InvalidCharacterNameError(msg)



class InvalidCharacterNameError(BaseException):

    def __init__(self, message):
        self.message = message

