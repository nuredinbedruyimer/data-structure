test = int(input())

for _ in range(test):
    n , a, b = list(map(int, input().split()))
    directions = input()
    directions = directions * 100
    
    grid = [[0 for _ in range(11)] for _ in range(11)]
    grid[a][b] = 1
    
    memo = {
        "N": (0, 1), 
        "E": (1, 0), 
        "W":(-1, 0), 
        "S": (0, -1)
    }
    start = (0, 0)
    
    ans = "NO"
    
    for char in directions:
        if start == (a, b):
            ans = "YES"
            break
        start = (start[0] + memo[char][0],start[1] + memo[char][1] )
    print(ans)
            
        
    
    
    
    