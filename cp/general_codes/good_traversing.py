matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63, 64]
]

rows = len(matrix)
cols = len(matrix[0])

ans = []

for row in range(  rows// 2):
    temp = []
    for col in range(row, cols - row):
        temp.append(matrix[row][col])
        temp.append(matrix[rows- 1 - row][col])
        temp.append(matrix[col][cols - row - 1])
        temp.append(matrix[col][row])
        
        
    ans.append(sorted(temp))
for x in ans:
    print(x)