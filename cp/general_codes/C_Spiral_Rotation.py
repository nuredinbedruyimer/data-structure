def rotate_90(x, y, r, c):
    return y, r - 1 - x

def rotate_180(x, y, r, c):
    return r - 1 - x, c - 1 - y

def rotate_270(x, y, r, c):
    return c - 1 - y, x

def rotate(x, y, r, c):
    return x, y

# Input the matrix
matrix = []
n = int(input())
rows = n
cols = n

for _ in range(n):
    arr = list(input())
    matrix.append(arr)

grid = [["." for _ in range(cols)] for _ in range(rows)]

# Process each layer
for layer in range((rows + 1) // 2):  # Iterate through each layer
    for col in range(layer, cols - layer):  # Top row
        if layer % 4 == 0:
            x, y = rotate_90(layer, col, rows, cols)
        elif layer % 4 == 1:
            x, y = rotate_180(layer, col, rows, cols)
        elif layer % 4 == 2:
            x, y = rotate_270(layer, col, rows, cols)
        else:
            x, y = rotate(layer, col, rows, cols)
        grid[x][y] = matrix[layer][col]

    for row in range(layer + 1, rows - layer):  # Right column
        if layer % 4 == 0:
            x, y = rotate_90(row, cols - 1 - layer, rows, cols)
        elif layer % 4 == 1:
            x, y = rotate_180(row, cols - 1 - layer, rows, cols)
        elif layer % 4 == 2:
            x, y = rotate_270(row, cols - 1 - layer, rows, cols)
        else:
            x, y = rotate(row, cols - 1 - layer, rows, cols)
        grid[x][y] = matrix[row][cols - 1 - layer]

    for col in range(cols - layer - 2, layer - 1, -1):  # Bottom row
        if layer % 4 == 0:
            x, y = rotate_90(rows - 1 - layer, col, rows, cols)
        elif layer % 4 == 1:
            x, y = rotate_180(rows - 1 - layer, col, rows, cols)
        elif layer % 4 == 2:
            x, y = rotate_270(rows - 1 - layer, col, rows, cols)
        else:
            x, y = rotate(rows - 1 - layer, col, rows, cols)
        grid[x][y] = matrix[rows - 1 - layer][col]

    for row in range(rows - layer - 2, layer, -1):  # Left column
        if layer % 4 == 0:
            x, y = rotate_90(row, layer, rows, cols)
        elif layer % 4 == 1:
            x, y = rotate_180(row, layer, rows, cols)
        elif layer % 4 == 2:
            x, y = rotate_270(row, layer, rows, cols)
        else:
            x, y = rotate(row, layer, rows, cols)
        grid[x][y] = matrix[row][layer]

# Print the rotated grid
for row in grid:
    print("".join(row))
