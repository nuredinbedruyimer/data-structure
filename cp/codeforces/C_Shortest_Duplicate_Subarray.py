from collections import defaultdict


n = int(input())

arr = list(map(int, input().split()))

memo = defaultdict(int)

left = 0
ans =  n

for right in range(n):
    memo[arr[right]] += 1
    
    while left < right and len(memo) < right - left + 1:
        memo[arr[left]] -= 1
        
        if memo[arr[left]] == 0:
            del memo[arr[left]] 
        ans = min(ans, right - left + 1)
        left += 1
if ans < n:
    print(ans)
else:
    print(-1)
        
        
    
    
        