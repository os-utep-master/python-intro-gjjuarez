#!/usr/bin/python3
import sys
import string

'Name of input and output file as arguments'
in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file, 'r') as f:
    data = f.read()
f.close()

'Goes through file and takes out punctuation given'
data = data.lower()
for char in "-.,!\";?:'":
    data = data.replace(char, ' ')
data = data.split()

'Initializing dictionary and count word frequency'
d = {}
for word in data:
    d[word] = d.get(word, 0) + 1

'Initializing list and sort it alphabetically'
word_list = []
for key, value in d.items():
    word_list.append((key, value))
word_list.sort()
'print(word_list)'

for x, y in word_list:
    print(x, y)

with open(out_file, "w") as f:
    f.write("\n".join("%s %s" % x for x in word_list))
f.close()
