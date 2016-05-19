#!/usr/local/bin/python3

numEng = int(input())
subEng = set(map(int, input().strip().split(" ")))
numFre = int(input())
subFre = set(map(int, input().strip().split(" ")))

print(len(subEng.difference(subFre)))
