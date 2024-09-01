# Enter your code here. Read input from STDIN. Print output to STDOUT
testcase=int(input())
for i in range(testcase):
    asize=int(input())
    a=set(map(int, input().split()))
    bsize=int(input())
    b=set(map(int, input().split()))
    print(a.issubset(b))

