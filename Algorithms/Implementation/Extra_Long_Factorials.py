#!/usr/local/bin/python3

import sys

def fac(n):
	if n == 1:
		return 1
	return n*fac(n-1)

n = int(input().strip())
print(fac(n))
