test = int(input())

def get_answer(n):
    if n == 2:
        print("-1")
        return 
    
    start = 1
    ans = [[-1 for _ in range(n)] for _ in range(n)]

    for row in range(n):
        for col in range(n):
            ans[row][col] = start
            start += 2
            if start > n * n:  # 
                start = 2

    for row in ans:
        print(" ".join(map(str, row)))

for _ in range(test):
    n = int(input())  
    get_answer(n)
