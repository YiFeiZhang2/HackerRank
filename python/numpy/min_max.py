#!/usr/local/bin/python3

import numpy

print(numpy.max(numpy.min(numpy.array([input().strip().split(" ") for _ in range(int(input().strip().split(" ")[0]))], int), axis=1)))
