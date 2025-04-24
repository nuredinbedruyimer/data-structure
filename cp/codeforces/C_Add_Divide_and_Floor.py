test = int(input())

def helper(smaller, larger):
    count = 0
    while larger > smaller:
        larger = (larger + smaller)// 2
        count += 1
    return count if larger == smaller else 1000
    
    
            


for _ in range(test):
    n = int(input())
    
    
    arr = list(map(int, input().split()))
    arr.sort()
    min_value = arr[0]
    
    ans = 0
    
    for curr_value in arr[-2:]:
        ans = max(ans, helper(min_value, curr_value))
    if ans <= n and ans != 0:
        x = [min_value for _ in range(ans)]
        print(ans)
        print(*x)
        
    else:
        print(ans)
        
        