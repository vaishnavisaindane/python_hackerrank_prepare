# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m=list(map(int, input().split()))
a_list=[]
b_list=[]
for a in range(n):
    a_list.append(input())
for b in range(m):
     b_list.append(input())
     
final_dict = defaultdict()

for b in b_list:
    if b in a_list:
        final_dict[b]=[i+1 for i,x in enumerate(a_list)if x==b]
        print(' '.join(map(str,final_dict[b])))
    else:
        print(-1)
