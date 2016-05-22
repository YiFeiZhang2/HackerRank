#!/usr/local/bin/python3

numRows, numEle = map(int, input().strip().split(" "))
att_list = [input() for i in range(numRows)]
ele = int(input())
att_list = sorted(att_list, key = lambda row: int(row.split(" ")[ele]))
for i in att_list:
    print(i)
