from collections import defaultdict


test = int(input())

for _ in range(test):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    memo = defaultdict(int)
    
    for a in arr:
        memo[a] += 1
    curr_sum = 0
    brr = sorted(memo.values())
    ans = len(brr)
    
    for index , curr in enumerate(brr):
        
        if k >= curr and index != n - 1:
            ans -= 1
            k -= curr
        else:
            break
        
            
    print(max(ans, 1))
            
    

