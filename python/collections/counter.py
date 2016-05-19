#!/usr/local/bin/python3

from collections import Counter

numShoes = int(input())
inventory = Counter(list(map(int, input().strip().split(" "))))
numBuyer = int(input())
revenue = 0

for i in range(numBuyer):
    size, cost = map(int, input().split(" "))
    if inventory[size] > 0:
        inventory[size] -= 1
        revenue += cost

print (revenue)
