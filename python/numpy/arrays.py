#!/usr/local/bin/python3
import numpy
arr = numpy.array(list(map(float, input().strip().split(" "))), float)
print(arr[::-1])
