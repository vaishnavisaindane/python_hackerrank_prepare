# Enter your code here. Read input from STDIN. Print output to STDOUT\
from itertools import product
k, m=map(int, input().split())
integers=list(map(int, input().split()[1:])for _ in range(k))

values=product(*integers)

max_profit=0

for val in values:
  max_profit = max(max_profit,sum(map(lambda x:x**2,val))%m)
print(max_profit)
