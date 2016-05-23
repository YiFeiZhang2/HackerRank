#!/usr/local/bin/python3

import sys


n,k = map(int, input().strip().split(' '))
a = [int(a_temp) for a_temp in input().strip().split(' ')]
counter = 0
for i in a[0:len(a)-1]:
    for j in a[i+1:]:
        if (i+j)%k == 0:
            counter += 1
print(counter)

