#!/usr/local/bin/python3

import numpy
rows, columns = map(int, input().strip().split(" "))
matrix = numpy.array([input().strip().split(" ") for _ in range(rows)], int)
#print(numpy.sum(matrix))
print(numpy.prod(numpy.sum(matrix, axis=0)))

#Note: default axis is Null -> does sum/product of EVERYTHING
#Does not need to type "axis=" -> Just numpy.sum(NAME, INT) is OK
#By convention "axis=" is typed for clarity?
