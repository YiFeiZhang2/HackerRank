import numpy
P = numpy.array(input().strip().split(" "), float)
X = float(input())
print(numpy.polyval(P, X))
