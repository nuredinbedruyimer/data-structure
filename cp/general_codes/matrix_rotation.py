matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

# 90-degree rotation
grid_after_90_rotation = [[0 for _ in range(cols)] for _ in range(rows)]
for row in range(rows):
    for col in range(cols):
        grid_after_90_rotation[col][cols - 1 - row] = matrix[row][col]
print("90-degree rotation:")
for row in grid_after_90_rotation:
    print(row)

# 180-degree rotation
grid_after_180_rotation = [[0 for _ in range(cols)] for _ in range(rows)]
for row in range(rows):
    for col in range(cols):
        grid_after_180_rotation[rows - 1 - row][cols - 1 - col] = matrix[row][col]
print("\n180-degree rotation:")
for row in grid_after_180_rotation:
    print(row)

# 270-degree rotation
grid_after_270_rotation = [[0 for _ in range(cols)] for _ in range(rows)]
for row in range(rows):
    for col in range(cols):
        grid_after_270_rotation[cols - 1 - col][row] = matrix[row][col]
print("\n270-degree rotation:")
for row in grid_after_270_rotation:
    print(row)

# 360-degree rotation (same as the original matrix)
grid_after_360_rotation = [[0 for _ in range(cols)] for _ in range(rows)]
for row in range(rows):
    for col in range(cols):
        grid_after_360_rotation[row][col] = matrix[row][col]
print("\n360-degree rotation (same as original matrix):")
for row in grid_after_360_rotation:
    print(row)
