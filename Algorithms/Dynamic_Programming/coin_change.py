#!/bin/python3

import sys

def getWays(n, m, c):
    dp = [[0]*(n+1) for i in range(m+1)]
    # if i == 0, then 0 ways of having change with no coins
    # if j == 0, then 1 way of having change for 0 dollars
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            else:
                if j - c[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-c[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
    return dp[m][n]
    # Complete this function

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'


ways = getWays(n, m, c)
print(ways)
