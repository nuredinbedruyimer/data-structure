test  = int(input())

for _ in range(test):
    left , right = list(map(int, input().split()))
    
    if left == right == 1:
        print(1)
    
    
    else:
        print(right - left)