# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
s, k=input().split(' ')
k=int(k)
for i in range(1, k+1):
    for j in list(itertools.combinations(sorted(s),i)):
         print(''.join(j))
   
