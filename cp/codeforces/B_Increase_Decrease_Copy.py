
test = int(input())


for _ in range(test):
    n = int(input())
    
    arr = list(map(int,  input().split()))
    brr = list(map(int,  input().split()))
    small_change = float("inf")
    index = -1
    
    for i in range(n):
        need = abs(brr[-1] - arr[i]) + abs(brr[-1] - brr[i])
        print(need, small_change)
        if need < small_change:
            index = i
            small_change = need
            
    print()
        
        
    ans = max(1, small_change)
    for i in range(n):
        if index == i:
            continue
        # print("index : ", index, "Value : ", ans)
        ans += abs(arr[i] - brr[i])
    # print(ans)
    