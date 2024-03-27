test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = []
    
    for i in range(n):
        if arr[i] == n:
            ans.append(1)
        else:
            ans.append(arr[i] + 1)
    print(*ans)
            
    