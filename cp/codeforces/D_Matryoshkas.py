from collections import defaultdict

test = int(input())


for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    
    
    memo = defaultdict(int)
    
    arr.sort()
    ans = 0
    
    
    for curr_value in arr:
        if memo[curr_value - 1] == 0:
            ans += 1
        else:
            memo[curr_value - 1] -= 1
        memo[curr_value ] += 1
    print(ans)

            
        