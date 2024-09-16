import numpy
n, m=map(int, input().split())
arr=numpy.array([input().strip().split()for _ in range(n)],dtype=int)
result=numpy.sum(arr, axis=0)
print(numpy.prod(result))


