#!/usr/local/bin/python3

import numpy
array = numpy.array(list(map(float, input().strip().split(" "))), float)
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
