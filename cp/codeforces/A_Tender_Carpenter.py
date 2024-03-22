from heapq import heappush, heapify, heappop

test = int(input())

for _ in range(test):
    n = int(input())
    
    arr = list(map(int, input().split()))
    ans = 1
    
    
    
    for i in range(n):
        for j in range(i+1, n):
            temp = sorted(arr[i: j + 1])
            if len(temp) < 2:
                continue
            
            if temp[0] * 2 > temp[-1]:
                ans += j - i
                
    print("YES" if ans >= 2 else "NO")
                
                
            