#!/usr/local/bin/python3

import numpy
firstrows, secondrows, columns = map(int, input().split(" "))
firstlist = numpy.array(list(input().strip().split(" ") for _ in range(firstrows)), int)
secondlist = numpy.array([input().strip().split(" ") for _ in range(secondrows)], int)
#print (firstlist)
#print (secondlist)
print (numpy.concatenate((firstlist, secondlist), axis = 0))
