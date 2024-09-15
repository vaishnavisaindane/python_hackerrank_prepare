from collections import deque

n = int(input())
d = deque()

for _ in range(n): 
    method = input().split()
    command = method[0]
    
    if command == "append":
        d.append(int(method[1]))
    elif command == "pop":
        d.pop()
    elif command == "popleft":
        d.popleft()
    elif command == "appendleft":
        d.appendleft(int(method[1]))

print(" ".join(map(str, d)))

    
    
    
