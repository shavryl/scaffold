
# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = '_' * len(self.word)

    def guess(self, char):
        indexes = [pos for pos, _char in enumerate(self.word) if _char == char]
        if indexes:
            letters_list = list(self.masked_word)
            for index in indexes:
                if letters_list[index] == char:
                    self.remaining_guesses -= 1
                    break
                letters_list[index] = char
            self.masked_word = ''.join(letters_list)
        else:
            if self.status != STATUS_ONGOING:
                raise ValueError(char)
            elif self.remaining_guesses == 0:
                self.status = STATUS_LOSE
            self.remaining_guesses -= 1

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        if '_' not in self.masked_word:
            self.status = STATUS_WIN
        return self.status
