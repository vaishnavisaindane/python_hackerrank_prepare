import numpy

def arrays(arr):
    # complete this function
    num_arr = numpy.array(arr[::-1],float)
    return num_arr
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
