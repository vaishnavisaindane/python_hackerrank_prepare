# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
n=int(input())
s=input().split()
k=int(input())
count=sum(1 for data in permutations(s, k) if 'a'in data)
print(f"{count/len(list(permutations(s, k))):.3f}")
