import numpy
N = int(input())
matrix = numpy.array([input().strip().split(" ") for _ in range(N)], float)
print(numpy.linalg.det(matrix))
