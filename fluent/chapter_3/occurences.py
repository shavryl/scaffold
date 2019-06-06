import sys
import re


WORD_RE = re.compile('\w+')


index = {}


with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # occurences = index.get(word, [])
            # occurences.append(location)
            # index[word] = occurences
            index.setdefault(word, []).append(location)
            # my_dict.setdefault(key, []).append(new_value)
            # is the same as running:
            # if key not in my_dict:
            #     my_dict[key] = []
            # my_dict[key].append(new_value)
            # except that latter code performs at least two
            # searches for key, while setdefault in a single


for word in sorted(index, key=str.upper):
    print(word, index[word])
