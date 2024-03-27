from collections import defaultdict


test = int(input())

def get_mex(arr):
    arr.sort()
    
    if len(arr) == 1:
        if arr[0] != 0:
            return 0
        else:
            return 1
    
    for i in range(1, 2):
        if arr[i] - arr[i-1] > 1:
            return arr[i - 1] + 1
    return arr[-1] + 1

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    u = list(set(arr))
    u.sort()
    
    memo = defaultdict(int)
    
    
    for a in arr:
        memo[a] +=1
        
    
    
    for i in range(len(u)):
        new_arr = u[:i] + u[i + 1:]
        print(get_mex(new_arr))
        
    
    
    
    
    