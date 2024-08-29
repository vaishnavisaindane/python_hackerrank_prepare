n, m=map(int, input().split())
myarray = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

# Calculate the happiness score
happiness_score = sum((i in a) - (i in b) for i in myarray)

print(happiness_score)
