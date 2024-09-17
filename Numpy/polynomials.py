import numpy as np
p=list(map(float,input().split()))
x=int(input())
arr=np.array(p)
print(np.polyval(arr, x))


