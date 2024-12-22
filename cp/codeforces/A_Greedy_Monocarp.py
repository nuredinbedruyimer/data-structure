test = int(input())
for _ in range(test):
    n, k = list(map(int,input().split()))
    
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    
    ans = 0
    
    for i in range(n):
        if arr[i] <= k:
            k-= arr[i]
        else:
            break
    print(k)

    