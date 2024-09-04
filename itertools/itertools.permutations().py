import itertools
s, k=input().split(' ')
for i in list(itertools.permutations(sorted(s), int(k))):
    print(''.join(i))
