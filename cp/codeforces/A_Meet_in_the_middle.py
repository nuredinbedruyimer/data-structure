test = int(input())


for _ in range(test):
    x, y, a, b = list(map(int, input().split()))
    
    
    if (y -x) % (a +b):
        print(-1)
    else:
        print((y-x)// (a + b))
    