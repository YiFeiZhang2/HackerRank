#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
       M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
       M.append(M_t)
    # your code goes here
    # check whether the number of balls in M[i] matches some total number of balls of a certain colour
    num_colours = [0]*n
    num_balls = [0]*n
    for i in range(n):
        # adds all the colours of type i from all boxes j
        for j in range(n):
            num_colours[i] += M[j][i]
        # adds up all the balls within each box 
        num_balls[i] +=  sum(M[i])
    num_colours.sort()
    num_balls.sort()
    poss = True
    for i in range(n):
        if num_colours[i] != num_balls[i]:
            poss = False
            break
    if poss:
        print("Possible")
    else:
        print("Impossible")
