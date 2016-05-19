#!/bin/python3

numEng = int(input())
listEng = set(map(int, input().split(" ")))
numFre = int(input())
listFre = set(map(int, input().split(" ")))

print(len(listEng.union(listFre)))
