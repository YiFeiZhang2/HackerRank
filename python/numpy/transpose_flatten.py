#!/usr/local/bin/python3

import numpy
row_num, column_num = map(int, input().split(" "))
num_list = list()
for _ in range(row_num):
    num_list.append(input().split(" "))
num_arr = numpy.array(num_list, int)
print(numpy.transpose(num_arr))
print(num_arr.flatten())
