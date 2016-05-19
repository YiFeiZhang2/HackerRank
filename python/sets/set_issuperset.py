#!/usr/local/bin/python3

A = set(map(int, input().strip().split(" ")))
isSuperSet = True
numSet = int(input())
for i in range(numSet):
	currSet = set(map(int, input().strip().split(" ")))
	if not A.issuperset(currSet):
		isSuperSet = False
		break
print(isSuperSet)
