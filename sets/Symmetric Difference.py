# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int,input().split(' ')))
m=int(input())
b=set(map(int,input().split(' ')))
c=a.symmetric_difference(b)
sorted_c=sorted(c)
for item in sorted_c:
    print(item)
