test = int(input())


for _ in range(test):
    n = int(input())
    
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if arr[i] - brr[i + 1] >= 0:
            ans += arr[i] - brr[i + 1]
    print(ans + arr[-1])

