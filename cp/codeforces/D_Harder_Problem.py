
for _ in range(int(input())):    
    n = int(input())
    a = list(map(int, input().split()))
    
    b = []
    check = set(list(range(1, n+1)))
    for i in range(n):
        if a[i] in check:
            check.remove(a[i])
            b.append(a[i])
        else:
            b.append(check.pop())
    print(*b)