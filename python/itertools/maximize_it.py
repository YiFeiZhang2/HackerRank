#!/usr/local/bin/python3

from itertools import product

numLines, M = map(int, input().split(" "))
numlist = [list(map(lambda x: int(x)**2, input().split(" ")[1:])) for i in range(numLines)]
prod = list(product(*numlist))
list_sums = list(map(lambda x: sum(x), prod))
mod_sums = list(map(lambda x: x%M, list_sums))
print(max(mod_sums))
