


class Player():
    points = 0

    letters_of_type = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    the_string = 'ARTDDSEERSNNSDEERRTTEEW'

    def get_index(self):
        result_list = []
        for character in self.letters_of_type:
            index_list = []
            for index, letter in enumerate(self.the_string):
                if letter == character:
                    index_list.append(index)
            if index_list:
                result_list.append(index_list)
        return result_list

    def build_words(self, result_list, the_string):
        list_of_words = []
        for index in result_list:
            try:
                for nested in index:
                    _next = nested + 1
                    first_letter = the_string[nested]
                    substring = the_string[_next:]

                    list_of_words.append(first_letter)
                    for letter in substring:
                        last_word = list_of_words[-1]
                        new_word = last_word + letter
                        list_of_words.append(new_word)
            except IndexError:
                continue
        return list_of_words

    def count_points(self, list_of_words):
        for word in list_of_words:
            self.points += self.the_string.count(word)
        return self.points


class Kevin(Player):
    letters_of_type = 'AEIOUY'


class Stuart(Player):
    letters_of_type = 'BCDFGHJKLMNPVWXZ'


class Competition():

    def __init__(self, the_string):
        self.the_string = the_string
        self.player_one = Kevin()
        self.player_two = Stuart()

    def calculate_for_player(self, player):
        result_list = player.get_index()
        list_of_words = player.build_words(result_list, self.the_string)
        return player.count_points(list_of_words)

    def compare_result(self):
        result_Kevin = self.calculate_for_player(self.player_one)
        result_Stuart = self.calculate_for_player(self.player_two)

        if result_Kevin > result_Stuart:
            return 'Kevin wins'
        elif result_Kevin == result_Stuart:
            return 'This is Draw!'
        else:
            return 'Stuart wins!'
