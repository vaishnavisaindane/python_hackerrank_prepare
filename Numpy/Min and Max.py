import numpy
n, m=map(int, input().split())
arr=numpy.array([input().strip().split()for _ in range(n)],dtype=int)
result=numpy.min(arr, axis=1)
print(numpy.max(result))


