#!/usr/local/bin/python3

numNumbers, numbers = int(input()), input().strip().split(" ")
print (all([int(i) > 0 for i in numbers]) and any([j == j[::-1] for j in numbers]))
