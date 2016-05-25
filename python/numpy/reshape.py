#!/usr/local/bin/python3

import numpy
#arr = numpy.array(list(map(int, input().strip().split(" "))))
#arr.shape = (3,3)
#print(arr)
print (numpy.reshape(numpy.array(list(map(int, input().strip().split(" ")))), (3, 3)))
