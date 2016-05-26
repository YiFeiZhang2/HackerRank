#!/usr/local/bin/python3

import numpy
rows, columns = map(int, input().strip().split(" "))
print(numpy.eye(rows, columns))
#print(numpy.eye(rows, columns, k = 0)
