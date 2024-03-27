test = int(input())


for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    opt =  0
    
    ans = [False for _ in range(n)]
    
    
    for i in range(n):
        if arr[i] - opt < 0:
            break
        
        if brr[i] > arr[i] - opt:
            ans[i] = True
            opt += brr[i] - arr[i] - opt
        elif brr[i] <= arr[i] - opt:
            ans[i] = True

    print(opt)
        
    


