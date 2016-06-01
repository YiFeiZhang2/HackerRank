import numpy
N, M = map(int, input().strip().split(" "))
array = numpy.array([input().strip().split(" ") for _ in range(N)], float)
print(numpy.mean(array, axis = 1))
print(numpy.var(array, axis = 0))
print(numpy.std(array))
