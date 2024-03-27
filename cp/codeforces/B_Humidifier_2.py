from collections import deque

def bfs(grid, start, D):
    rows, cols = len(grid), len(grid[0]) 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    distance = [[-1] * cols for _ in range(rows)]  
    count = 0  
    
    queue = deque([start])  
    distance[start[0]][start[1]] = 0 

    while queue:
        x, y = queue.popleft()

        if distance[x][y] <= D:
            count += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == '.':
                    queue.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
                    grid[nx][ny] = "#"

    return count

m, n, D = list(map(int, input().split()))
grid = []

for _ in range(m):
    row = input().strip()
    grid.append(row)
ans = []

for row in range(m):
    for col in range(n):
        if grid[row][col] == '.':
            ans.append(bfs(grid, (row, col), D))


ans.sort()
print(ans[-1] + ans[-2])
