from collections import defaultdict



def helper(n, seen):
    opt = 0
    while n % 2 == 0 :
        n //= 2
        seen.add(n)
        opt += 1
    return opt


test = int(input())


for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    seen = set()
    
    memo = defaultdict(int)
    even = []
    
    for a in arr:
        if a % 2 == 0:
            memo[a] += 1
    
            
    ans = 0
    for key in memo.keys():
        even.append(key)
    even.sort(reverse=True)
    # print(even)
    
    for a in even:
        if a not in seen:
            # print("hello")
            ans += helper(a, seen)
    print(ans)
        
    