test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(n - 2, -1, -1):
        arr[i] = arr[ i + 1] + arr[i]
        
    
    ans = arr[0]
    
    for index in range(1, n):
        if arr[index] > 0:
            ans += arr[index]
    print(ans)