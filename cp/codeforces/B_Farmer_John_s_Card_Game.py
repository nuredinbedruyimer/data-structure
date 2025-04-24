test = int(input())


for _ in range(test):
    n, m = list(map(int, input().split()))
    mrr = [[] for _ in range(m)]
    
    for _ in range(n):
        arr = list(map(int, input().split()))
        
        for i in range(m):
            mrr[i].append(arr[i])
    for i in range(m):
        mrr[i].append(i)
    mrr.sort()
    arr = []
    ans = []
    
    for i in range(m):
        arr = arr + mrr[i][0: n]
        ans.append(mrr[i][-1])
    print(*ans)
    # if arr = sorted(range(0, m * n)):
        
    
    print(mrr)
    