# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
A=list(map(int, input().split()))
B=list(map(int, input().split()))
print (*list(itertools.product(A, B)))
