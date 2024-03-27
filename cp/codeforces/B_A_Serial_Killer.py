from collections import defaultdict, deque

first, second = list(map(str, input().split()))
memo = defaultdict(str)

print(first, second)

n = int(input())
for _ in range(n):
    f, s = list(map(str, input().split()))
    if first == f:
        first = s
        print(first, second)
    else:
        second = s
        print(first, second)

        
        
        
    

