#!/usr/local/bin/python3

import numpy
row_num, col_num = map(int, input().strip().split(" "))
arr1 = numpy.array([input().strip().split(" ") for _ in range(row_num)], int)
arr2 = numpy.array([input().strip().split(" ") for _ in range(row_num)], int)
print(numpy.add(arr1, arr2))
print(numpy.subtract(arr1, arr2))
print(numpy.multiply(arr1, arr2))
print(arr1 // arr2)
print(numpy.mod(arr1, arr2))
print(numpy.power(arr1, arr2))

#Can be overloaded to use + - * / ** %
