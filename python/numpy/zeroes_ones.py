#!/usr/local/bin/python3

import numpy

N = tuple(map(int, input().strip().split(" ")))
print(numpy.zeros(N, dtype=numpy.int))
print(numpy.ones(N, dtype=numpy.int))
