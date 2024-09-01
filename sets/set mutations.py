# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int, input().split()))
N=int(input())
for i in range(N):
    cmd=input().split()[0]
    b=set(map(int, input().split()))
    getattr(a,cmd)(b)
print(sum(a))
