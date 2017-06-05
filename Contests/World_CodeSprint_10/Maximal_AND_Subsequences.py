#!/bin/python3

import sys
import math

def solve(n, k, a, c):          # c = binary digit to check
    #print(n, k, a, c)
    if c == -1:                          #last digit -> take all that remain
        val = int(a[0][0], 2)
        for i in a[:k]:
            val = val & int(i[0], 2)
            num = math.factorial(n) / (math.factorial(k) / (math.factorial (n-k)
        return (val, int(num)%1000000007)
    l_a = [0]*63
    for i in a:
        l = i[1]
        for j in i[0]:
            l_a[l] += int(j)
            l -= 1
    #print(l_a)
    y = 0
    for x in range(c, -1, -1):
        curr_bin = int(math.pow(2, x))
        n_a = []                #new array
        if l_a[x] >= k:        #having >k in the largest digist means that these are combination
            for i in a:
                if int(i[0], 2) & curr_bin == curr_bin:        #only keep items that match
                    n_a.append(i)
            return solve(len(n_a), k, n_a, x-1)     #out of the >k items, look at next less significant digit
        else:
            continue
            y = x
    return solve(n, k, a, y-1)

#n, k = input().strip().split(' ')
#n, k = [int(n), int(k)]
#a = []
#a_i = 0
#for a_i in range(n):
#    a_t = int(input().strip())
#    x = bin(a_t).lstrip('0b')
#    if x == '': x = '0'
#    a.append((x, a_t.bit_length()-1))

f = open('max_test_7.txt', 'r')
n, k = f.readline().strip().split(' ')
n, k = [int(n), int(k)]
a = []
a_i = 0
for a_i in range(n):
    a_t = int(f.readline().strip())
    x = bin(a_t).lstrip('0b')
    if x == '': x = '0'
    a.append((x, a_t.bit_length()-1))

result = solve(n, k, a, 29)
print ("\n".join(map(str, result)))


