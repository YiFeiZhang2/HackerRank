#!/usr/local/bin/python3

import sys


length = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
counter = 0

for _ in range(length):
    for i in range(length-1):
        if a[i] > a[i+1]:
            first = int(a[i+1])
            second = int(a[i])
            a[i+1] = second
            a[i] = first
            counter += 1
            
print("Array is sorted in " + str(counter) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[length-1]))
