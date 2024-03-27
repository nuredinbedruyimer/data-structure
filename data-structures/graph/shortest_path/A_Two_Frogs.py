test = int(input())


for _ in range(test):
    n, a, b = list(map(int, input().split()))
    
    if abs(a -b)  % 2 == 0:
        print("YES")
    else:
        print("NO")
    