


class Player():
    points = 0

    letters_of_type = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    the_string = 'ARTDDSEERSNNSDEERRTTEEW'

    def add_point(self, num):
        self.points = self.points + num

    def get_index(self):
        indexes = []
        for letter in self.letters_of_type:
            # there is a problem that it finds only first index
            indexed = self.the_string.find(letter)
            if indexed >= 0:
                indexes.append(indexed)
        return indexes



    def build_words(self, string):
        for letter in self.letters_of_type:
            ...




class Kevin(Player):
    letters_of_type = 'AEIOUY'


class Stuart(Player):
    letters_of_type = 'BCDFGHJKLMNPVWXZ'


class Competition():

    def pass_it(self):
        ...

def generate_words(index, string):
    list_of_words = []
    word = []
    index = 2
    string = 'BANANA'
    for index in string:
        ...
    # get index as 1 word,
    # add points for it
    # make next word as index+next index
    # ...
    # but indexs shoudl be as player rules
    # vowel or consonant
    # ...
    # add points for it
    # ...
    # calculate sum for both players
    # players is extended counter
    # main method is composition
    # of process and players

    list_of_words.append()
    return list_of_words


def add_points(list_of_words, player):
    for word in list_of_words:
            ...
