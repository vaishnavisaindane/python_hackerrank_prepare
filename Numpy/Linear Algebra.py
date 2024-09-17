import numpy
numpy.set_printoptions(legacy='1.13')
n=int(input())
a=numpy.array([input().split()for _ in range(n)], float)
print(numpy.linalg.det(a))


