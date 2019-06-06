import sys
import re
import collections


WORD_RE = re.compile('\w+')

# the default_factory of a defaultdict is only invoked to provide
# default values for __getitem__ calls, and not for the other methods
# For example dd[k] if k is a missing key will call default_factory
# but dd.get[k] still returns None.
index = collections.defaultdict(list)


with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # if word is not initially in the index, the default_factory
            # is called to produce the missing value, which in this case
            # is an empty list that is then assigned to index[word] and
            # returned, so the .append(location) operation always succeeds.
            index[word].append(location)


for word in sorted(index, key=str.upper):
    print(word, index[word])
