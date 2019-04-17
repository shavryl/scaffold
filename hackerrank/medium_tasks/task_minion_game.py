


class Player():
    points = 0

    letters_of_type = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    the_string = 'ARTDDSEERSNNSDEERRTTEEW'

    def add_point(self, num):
        self.points = self.points + num

    def get_index(self):
        result_list = []
        for character in self.letters_of_type:
            index_list = []
            for index, letter in enumerate(self.the_string):
                if letter == character:
                    index_list.append(index)
                    print(index, result_list)
            if index_list:
                result_list.append(index_list)
        return result_list

    def build_words(self, result_list):
        # take index in result_list
        # by index select letter from the_string
        # create first word with this 1 letter
        # iterate and add next letters to it
        # save as seperate words
        list_of_words = []
        for index in result_list:
            for nested in index:
                _next = nested + 1
                first_letter = self.the_string[nested]
                substring = self.the_string[_next:]
                list_of_words.append(first_letter)

                for letter in substring:
                    # take last word in list
                    # add letter to it and save
                    last_word = list_of_words[-1]
                    new_word = last_word + letter
                    list_of_words.append(new_word)

        return list_of_words

    def count_points(self, list_of_words):
        # get list of words
        # compare every word to the_string
        # get 1 point for every equal
        ...


class Kevin(Player):
    letters_of_type = 'AEIOUY'


class Stuart(Player):
    letters_of_type = 'BCDFGHJKLMNPVWXZ'


class Competition():

    def pass_it(self):
        ...
