#!/usr/local/bin/python3

from collections import defaultdict
word_tracker = defaultdict(list)


n, m = map(int, input().strip().split(" "))

for i in range(n):
    word_tracker[input()].append(i+1)
    
for i in range(m):
    a = input()
    if len(word_tracker[a]) > 0:
        print(' '.join(map(str, word_tracker[a])))
    else:
        print(-1)
