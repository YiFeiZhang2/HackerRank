#!/usr/local/bin/python3

from collections import OrderedDict
wordDict = OrderedDict()
for _ in range(int(input())):
    line = input().strip()
    wordDict[line] = wordDict.get(line, 0) + 1
print(len(wordDict))

#joins the strings
print(' '.join(str(wordDict[i]) for i in wordDict)) 

#below maps each int to a string, puts in list, and joins list
#print(' '.join(list(map(str, [wordDict[i] for i in wordDict]))))
