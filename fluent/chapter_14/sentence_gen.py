import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return


class LazySentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # builds an iterator over the matches yielding MatchObject
        for match in RE_WORD.finditer(self.text):
            # match.group() extracts the actual matched text
            # from MatchObject instance
            yield match.group()
        # return (match.group() for match in RE_WORD.finditer(self.text))