#!/usr/local/bin/python3

from collections import Counter
d = Counter()
line = input().strip()
for i in range(len(line)):
    d[line[i]] = d.get(line[i],0) + 1   
string = sorted(d.items(), key= lambda x: (-x[1],x[0]))[:3]
print('\n'.join(x[0] + " " + str(x[1]) for x in string))
