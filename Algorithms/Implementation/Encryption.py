#!/usr/local/bin/python3

import sys
from math import ceil, sqrt, floor


s = input().strip()
c = ceil(sqrt(len(s)))
output = ""
for i in range(c):
    output = output + s[i::c] + " "
print (output)
#print(' '.join(map(lambda x: s[x::c], range(c))))
