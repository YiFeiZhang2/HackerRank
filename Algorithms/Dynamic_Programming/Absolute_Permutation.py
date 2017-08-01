#!/bin/python3

import sys

def abs_perm(n, k):
    if k == 0:
        return (' '.join([str(i) for i in range(1, n+1)]))
    
    skip = False
    i = 1
    perm = ['0']*(n+1)
    while (i < n+1):
        if not skip:
            if i+k < n+1:
                perm[i] = str(i+k)
            # n-i+1 represents the index going big to small
            if n-i+1-k > 0: 
                perm[n-i+1] = str(n-i+1-k)
        if i % k == 0:
            skip = not skip
        i += 1
    
    perm = perm[1:]
    if '0' not in perm[1:]:
        return (' '.join(perm))
    else:
        return (-1)
        
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]

    print(abs_perm(n, k))
    


