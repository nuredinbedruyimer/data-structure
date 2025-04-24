import sys

# Direction vectors (Right, Down, Left, Up)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def floodfill(grid, visited, start_row, start_col, rows, cols):
    stack = [(start_row, start_col)]
    
    while stack:
        r, c = stack.pop()
        
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '#' or visited[r][c]:
            continue
        
        visited[r][c] = True  # Mark cell as visited
        
        for dr, dc in DIRECTIONS:
            stack.append((r + dr, c + dc))

def count_rooms(grid, rows, cols):
    visited = [[False] * cols for _ in range(rows)]
    room_count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and not visited[i][j]:
                floodfill(grid, visited, i, j, rows, cols)
                room_count += 1  # Found a new room
    
    return room_count

# Fast input handling
if __name__ == "__main__":
    rows, cols = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(rows)]
    
    print(count_rooms(grid, rows, cols))
