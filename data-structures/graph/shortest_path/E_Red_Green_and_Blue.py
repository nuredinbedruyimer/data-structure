test = int(input())


for _ in range(test):
    r = list(map(int, input().split()))
    
    
    rrr = list(map(int, input().split()))
    grr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    
    n = max(len(rrr), len(brr), len(grr))
    dp = [(0, 0, 0) for _ in range(n)]
    
    ans = [float("inf")]
    
    def dfs(index, r, g, b):
        if index >= len(rrr):
            return float("inf")
        if index >= len(grr):
            return float("inf")
        if index >= len(brr):
            return float("inf")
        
        r_p = dfs(index + 1, r + 1, g, b)
        r_n_p = dfs(index + 1, r, g, b)
        
        
        g_p = dfs(index + 1, r, g + 1, b)
        g_n_p = dfs(index + 1, r, g, b)
        
        
        b_p = dfs(index + 1, r, g, b + 1)
        b_n_p = dfs(index + 1, r, g, b)
        
        
        if r == b == g == 1:
            return (rrr[index] - brr[index])**2 + (rrr[index] - grr[index])**2 + (grr[index] - brr[index])**2
            
        return min(r_p, r_n_p, g_p, g_n_p, b_p, b_n_p )
    print(dfs(0, 0, 0,0))
        
        

    
    