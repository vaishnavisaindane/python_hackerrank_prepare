# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
m=list(map(int,input().split()))
list_set=set(m)
for val in list_set:
    if val in m:
        m.remove(val)
    if val not in m:
        print(val)
