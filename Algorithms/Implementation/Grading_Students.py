#!/bin/python3

import sys

def solve(g):
    if g >= 38 and (x % 5) >= 3:
        g += 5 - (x % 5)
    return g

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(solve(grades_t))
for g in grades:
    print(g)