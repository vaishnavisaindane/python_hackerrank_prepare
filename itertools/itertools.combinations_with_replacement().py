import itertools
s, k=input().split(' ')
k=int(k)
for j in list(itertools.combinations_with_replacement(sorted(s),k)):
         print(''.join(j))
   
